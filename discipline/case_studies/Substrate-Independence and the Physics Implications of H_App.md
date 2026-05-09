# Routing Correctness Is Not Retrieval Correctness: Candidate-Set Dilution and the Stage-Certification Gap in Modular Retrieval Pipelines

## Abstract

Routing accuracy is not a compositional guarantee over modular retrieval pipelines. In architectures that decouple collection scoring from candidate-set assembly, routing evaluation certifies a property of the scoring stage S(q) that does not propagate through the orchestration stage C(q). We call this the **stage-certification gap**: routing benchmarks certify ArgmaxCorrect(q) — whether the router's top-scored collection matches the highest-specificity collection — but do not certify whether C(q) maintains that specificity advantage at retrieval time.

The contribution is not the existence of a poor fan-out heuristic. It is that routing evaluation provided no signal that the heuristic invalidated the property being certified. A system instrumented only for ArgmaxCorrect is structurally blind to specificity preservation failures that originate in the orchestration stage, because those failures occur after routing evaluation has already terminated. This is the dual failure mode to cascade pruning: where cascade architectures degrade when too much is filtered, modular fan-out degrades when too much is included — and neither failure is visible to the other stage's evaluation metric.

We instantiate the gap through a production civic retrieval deployment where 93% collection-selection accuracy coexists with end-to-end P@5 of 0.053. A fan-out expansion experiment directly manipulates only C(q) while holding S(q), corpus, embeddings, and ANN parameters constant: P@5 degrades monotonically from 0.68 (top-1 exclusive) to 0.41 (top-2) to 0.053 (top-5 full fan-out) while ArgmaxCorrect remains 93% throughout. A falsification-oriented stress test against the density-primary alternative explanation forecloses corpus density as the primary account. We propose dilution magnitude D̄_k as an operational audit metric for detecting stage-certification divergence, and argue that ArgmaxCorrect and D_k require independent pipeline instrumentation.

---

## 1. Introduction

Routing evaluation in modular retrieval systems carries an implicit scope assumption: that certifying the scoring stage is sufficient to certify pipeline retrieval behavior. This assumption fails whenever the orchestration stage — which assembles the candidate set after routing evaluation terminates — is independently implemented and not contractually constrained to preserve the specificity signal the scoring stage produced.

**Routing accuracy is not a compositional guarantee over modular retrieval pipelines.** Stage-level certification composes into a pipeline-level guarantee only when all downstream stages are jointly evaluated. Routing benchmarks evaluate S(q) alone. In any architecture where C(q) is a separately implemented component, the gap between what routing evaluation certifies and what retrieval behavior delivers is structurally possible and not detectable by routing metrics alone.

This is the **stage-certification gap**. The present work characterizes it as a class of failures, demonstrates its existence in a production system at substantial scale, and provides a causal isolation experiment. The claim is not that such failures are universal or that the fan-out policy described here is representative. The claim is that when S(q) and C(q) are independently implemented, ArgmaxCorrect(q) = 1 does not prevent D_k(q) >> 0, and no routing-layer metric signals the discrepancy.

The contribution is positioned relative to cascade retrieval work as follows. Prior pipeline retrieval research studies failures induced by overly aggressive filtering — where correct early-stage decisions are undermined by excessive pruning before later stages. This paper characterizes the **dual failure mode**: degradation introduced by post-routing candidate-set expansion that invalidates stage-level routing certification while leaving routing accuracy unchanged. The failure modes are formally symmetric but empirically distinct and require separate instrumentation.

This paper has two distinct contributions, maintained carefully throughout. The **general contribution** is the stage-certification gap: a structural property of modular retrieval architectures in which stage-level evaluation is not compositionally predictive of pipeline behavior. The **case-study contribution** is candidate-set dilution via fan-out: the specific mechanism that instantiates the gap in this deployment, experimentally isolated through direct C(q) manipulation.

Unless otherwise noted, all experiments hold corpus composition, embedding model, and ANN parameters constant; observed performance differences are attributable to candidate-set construction policy alone.

### 1.1 Formal Decomposition

Let C be the set of indexed collections. We distinguish two objects that routing evaluation conflates when it is correct:

**The true best collection** (ground truth):

    c†(q) = argmax_{c ∈ C} Spec(c, q)

**The router prediction**:

    ĉ(q) = argmax_{c ∈ C} S(q, c)

**Definition (Collection Specificity).** Specificity is defined instrumentally:

    Spec(c, q) > Spec(c', q)  iff  P@k({c}) > P@k({c'})

That is, c is more specific than c' with respect to q if and only if exclusive retrieval from {c} produces higher precision than exclusive retrieval from {c'}. This definition is agnostic to why one collection retrieves better — semantic concentration, jurisdictional scope, and corpus density are motivating descriptions, not load-bearing formalism. All subsequent uses of "specificity" trace to this definition.

In practice, c†(q) is operationalized through expert judgment rather than exhaustive per-collection precision measurement across all 48 collections. The two may diverge for queries where the expert-expected and empirically-best collections differ; this is acknowledged as a construct validity limitation in §9.3.

**ArgmaxCorrect** measures whether the router's prediction matches the true best collection:

    ArgmaxCorrect(q) = 1  iff  ĉ(q) = c†(q)

The name is intentional: routing evaluation is precisely an argmax correctness check — it asks whether the highest-scoring collection matches the expected target. It does not ask whether the downstream use of that argmax preserves the advantage it certifies.

**The end-to-end retrieval outcome:**

    P@k(q) = f(S(q), C(q), R(q))

where C(q) ⊆ C is the orchestration-assembled candidate set and R(q) is the retrieval operator applied to C(q).

**Dilution magnitude** at cutoff k is the primitive observable:

    D_k(q) = P@k({c†(q)}) - P@k(C(q))
    D̄_k   = (1/|Q|) Σ_{q ∈ Q} D_k(q)

**Specificity preservation** is a thresholded interpretation over D_k:

    SpecificityPreserved_k(q) = 1  iff  D_k(q) ≤ ε

for a tolerance ε ≥ 0. In practice we report continuous D_k directly; the binary notation is conceptual shorthand. Candidate-set dilution occurs when D_k(q) > 0: C(q) has been expanded beyond {c†(q)} and retrieval precision has degraded as a result.

**The stage-certification gap — three-layer decomposition:**

    Layer 1 — Scoring stage:        S(q) certifies ArgmaxCorrect(q)
    Layer 2 — Orchestration stage:  C(q) determines D_k(q)
    Layer 3 — Interface:            S(q) output passed as non_zero set, not score ordering
                                    No contract enforces score-dominance in C(q) construction

    ┌──────────────────────────────────────────────────────────────┐
    │   ArgmaxCorrect(q) = 1   ⟹̸   D_k(q) = 0                   │
    └──────────────────────────────────────────────────────────────┘

Routing evaluation certifies Layer 1 and is silent about Layer 2. The interface failure at Layer 3 — a lossy projection of S(q)'s output that discards score ordering — is what makes Layer 2 failures undetectable by Layer 1 metrics. No improvement to S(q) alone can close this gap; changes are required at the interface.

**An important clarification:** D_k(q) > 0 is not inherently a system failure. Broadening C(q) is often a deliberate tradeoff — for coverage, recall, or robustness — and accepting precision loss in exchange is legitimate. Systems that prioritize recall over precision at fixed k may accept D̄_k > 0 as an explicit design point; the contribution of this work is making that tradeoff measurable rather than invisible. This study evaluates specificity preservation at finite precision cutoffs and does not measure whether broader fan-out improves long-tail recall beyond the evaluated top-k regime. The pathology characterized here is not that D_k(q) > 0 exists. It is that D_k(q) is unmeasured, uncertified, and compositionally disconnected from the property routing evaluation does certify. A system that scores 93% on routing evaluation while exhibiting D̄₅ = 0.627 in deployment has made that tradeoff invisibly, without a metric that detects it. The contribution is the instrumentation gap, not the existence of the tradeoff.

Candidate-set dilution differs from conventional recall–precision tradeoffs because (1) degradation occurs after the routing stage has already correctly identified c†(q), and (2) the expansion policy is invisible to routing evaluation, which terminates before construction begins. The pathology is the non-compositionality of stage-level certification.

The definition is independent of ANN approximation: D_k(q) > 0 can occur under exact nearest-neighbor retrieval when lower-specificity collections displace relevant results within a finite k. Whether ANN dynamics amplify the magnitude here is addressed in §7.2.

### 1.2 Design Principle

> **Design Principle (Stage-Certification Independence):** In modular retrieval pipelines where S(q) and C(q) are independently implemented, ArgmaxCorrect certifies the scoring stage alone. Dilution magnitude D̄_k audits the orchestration stage. The interface between stages requires its own specification: passing score magnitudes, not merely non-zero membership, into construction decisions is necessary for ArgmaxCorrect to be compositionally meaningful. All three layers require independent instrumentation.

### 1.3 Paper Structure

§2 describes the system context. §3 operationalizes competing hypotheses. §4 presents the fan-out expansion experiment as primary causal evidence (§4.3) and the density stress test as a falsification control (§4.4). §5 inspects routing code and the patch. §6 reports post-patch validation. §7 discusses the evaluation blind spot, ANN amplification, calibration independence, and generalization conditions. §8 covers related work. §9 concludes.

---

## 2. System and Failure Context

### 2.1 Deployment

The deployment is a production civic information system serving Fayette County, West Virginia, indexing 48 ChromaDB collections totaling 7,902,937 vectors: municipal address records, GIS facility data, benefit program documents, regional news, and a purpose-built Fayette County civic resource collection.

### 2.2 Key Collection Statistics

| Collection | Vectors | Content type |
|---|---|---|
| address_points | 1,115,588 | Municipal address registry |
| news_rag | ~hundreds of thousands | Regional news |
| gis_wv_benefits | 4,668 | Structured benefit location records |
| fayette_county_resources_2026 | 328 | Civic program documents (purpose-built) |

Thirty-three collections use L2 distance; fifteen use cosine. Distance metrics are not normalized across collections.

### 2.3 Embedding and ANN Configuration

All collections: sentence-transformers/all-MiniLM-L6-v2 (384 dimensions). ChromaDB HNSW: ef_construction=100, ef_search=100, max_neighbors=16. All precision figures reflect ANN-approximate retrieval.

### 2.4 Routing Architecture and Pre-Patch Fan-Out

| Alias | Collection | Tier | Score |
|---|---|---|---|
| rag-fayette | fayette_county_resources_2026 | County-specific | +6 |
| rag-civic | civic_programs_wv | State programs | +5 |
| rag-local-resources | local_resources | Broad fallback | +4 |
| rag-wv-resources | wv_resources | Broad fallback | +3 |
| rag-gis-benefits | gis_wv_benefits | State GIS benefits | +3 |

An unconditional fan-out override merged all five collections whenever all scored non-zero — a deliberate coverage-robustness heuristic conditioned on set membership rather than score dominance. Civic keyword queries reliably scored all five collections, making the override near-invariant across the query distribution.

Pre-patch candidate space after fan-out:

| Collection | Vectors | Share |
|---|---|---|
| address_points | 1,115,588 | 99.10% |
| gis_wv_benefits | 4,668 | 0.41% |
| wv_facilities | 2,900 | 0.26% |
| GBIM_Fayette_sample | 1,535 | 0.14% |
| fayette_county_resources_2026 | 206 | 0.018% |
| **Total** | **1,125,186** | **100%** |

**Figure 1. Stage-Certification Gap: Where Routing Evaluation Terminates, Where Pipeline Failure Occurs**

```
Query (civic + Fayette signal)
          │
          ▼
┌────────────────────────────────────────────────────────┐
│  S(q): Routing Scorer                                  │
│  rag-fayette  +6  ← ĉ(q) = c†(q)                     │
│  rag-civic    +5                                       │  ArgmaxCorrect(q) = 1
│  rag-local    +4                                       │  certified here: 93%
│  rag-wv-res   +3                                       │
│  rag-gis      +3                                       │  ← ROUTING EVALUATION ENDS
└────────────────────┬───────────────────────────────────┘
                     │  Interface: score ordering discarded,
                     │  non_zero set membership passed only
                     ▼  D_k(q) not yet measurable.
       ┌────────────────────────────────────────────┐
       │  C(q): Orchestration Policy                │
       │  Condition: all_nonzero ⊆ candidates?      │  ← Not evaluated by
       │  Test: set membership, not score dominance │    routing benchmarks
       │  Result: merge all 5 into C(q)             │
       └──────────────────────┬─────────────────────┘
                              ▼
   ┌──────────────────────────────────────────────────┐
   │  Merged: 1,125,186 vectors                       │
   │  address_points       99.10%                     │
   │  fayette_resources     0.018%  ← c†(q) target    │
   └─────────────────────────────┬────────────────────┘
                                 ▼
                        R(q): ANN retrieval
                        P@5(C(q))  = 0.053
                        D̄₅         = +0.627
                        ArgmaxCorrect(q) = 1  ← unaware of failure
                        D_k(q) >> 0           ← not instrumented
```

---

## 3. Competing Hypotheses

**H1 — Corpus density insufficiency.** The target collection is 0.018% of the merged candidate set. Under H1, this ratio determines the failure regardless of orchestration policy. Prediction: retrieval improves monotonically with civic-document share; sufficient density reproduces post-patch performance without orchestration change.

**H2 — Stage-certification gap (candidate-set dilution).** The scoring stage correctly identifies c†(q) via ĉ(q); the orchestration stage expands C(q) ⊃ {c†(q)} conditioned on membership rather than score dominance, and c†(q) loses its specificity advantage within C(q). Under H2, density variation under constant fan-out cannot explain the failure. Predictions: (a) D_k increases monotonically with fan-out breadth under constant corpus; (b) density increase under constant fan-out does not recover post-patch performance.

**H3 — ANN or embedding insufficiency.** Partially controlled by holding model and ANN parameters constant across all conditions. The contribution of HNSW traversal dynamics to observed D̄_k magnitude is unresolved (§7.2).

**H4 — Selection failure.** The router misidentifies c†(q), i.e., ArgmaxCorrect(q) = 0 at higher-than-expected rates. Directly tested in §5.1.

H1 and H2 generate the sharpest distinguishable empirical predictions, motivating §4.3 and §4.4 respectively.

---

## 4. Experimental Isolation

### 4.1 Pilot Evaluation Methodology

**Query set:** 30 civic prompts across six categories (5 each): emergency food assistance, utility assistance, housing programs, healthcare enrollment, childcare subsidy, SSI/disability assistance.

**Relevance rubric:** Relevant (1) if the result names an applicable program, service, or agency; contains at least one actionable element (contact, enrollment path, eligibility description, or service hours); and would enable a Fayette County resident to take a concrete next step. Not relevant (0) if a generic address or facility record, jurisdictionally inapplicable, a duplicate, or lacking actionable content.

**Annotation:** 450 total judgments (30 queries × top-5 × 3 primary conditions) by a single annotator with operational knowledge of Fayette County resources. Expected collection selections defined prior to post-patch evaluation.

**Statistical treatment:** Percentile bootstrap 95% CIs (10,000 query-level resamples) and paired approximate randomization tests (10,000 permutations). Effect sizes are sufficiently large that significance is demonstrated at 30 queries; subtle differences are not reliably detectable.

### 4.2 Pilot Evaluation: Cross-Condition Results

| Metric | Pre-patch routed | Unrouted | Post-patch routed |
|---|---|---|---|
| P@5 | 0.053 | 0.207 | 0.68 |
| MRR | 0.233 | 0.396 | 0.79 |
| Relevant / 150 | 8 | 31 | 102 |
| Queries ≥1 relevant | 7 / 30 | 17 / 30 | 28 / 30 |

**Pairwise comparisons (P@5):**

| Comparison | Δ | 95% CI | Approx. rand. p |
|---|---|---|---|
| Pre-patch vs. unrouted | +0.153 | [0.091, 0.224] | < 0.001 |
| Pre-patch vs. post-patch | +0.627 | [0.490, 0.770] | < 0.001 |
| Unrouted vs. post-patch | +0.473 | [0.340, 0.607] | < 0.001 |

That geographically-routed retrieval with 93% ArgmaxCorrect substantially underperforms unrouted full-corpus search is itself diagnostic of C(q) failure rather than S(q) failure: when argmax selection is mostly correct and routing still underperforms no-routing, the failure is in orchestration, not scoring.

### 4.3 Fan-Out Expansion Experiment (Primary Evidence)

This experiment is the paper's central causal contribution. It varies only C(q) while holding all other factors constant — S(q), corpus, embedding model, ANN parameters — across three conditions. If H2 prediction (a) holds, D_k increases monotonically with fan-out breadth.

| Condition | C(q) contents | Vectors | P@5 | MRR | D̄₅ |
|---|---|---|---|---|---|
| Top-1 exclusive | rag-fayette only | ~328 | 0.68 | 0.79 | 0.00 |
| Top-2 partial | + rag-civic | ~4,996 | 0.41 | 0.55 | +0.27 |
| Top-5 full fan-out | All five scored | ~1,125,186 | 0.053 | 0.233 | +0.627 |

**Figure 2. Fan-Out Expansion: Monotonic Dilution Under Isolated C(q) Manipulation**

```
  P@5
  0.8 ┤  ● 0.68  Top-1: C(q) = {c†(q)} only
      │   \
  0.6 ┤    \      S(q):    FIXED  (ArgmaxCorrect = 93% throughout)
      │     \     Corpus:  FIXED
  0.4 ┤      ● 0.41  Top-2 partial fan-out
      │        \  Embed:   FIXED
  0.2 ┤         \  ANN:    FIXED
      │          \  C(q):  ONLY VARIABLE
  0.0 ┤           ● 0.053  Top-5 full fan-out
      └──────────────────────────────────────────────
            1 coll.       2 colls.       5 colls.
                    Fan-out breadth →
```

The full performance range — P@5 0.68 to 0.053, a drop of 0.627 — is produced by C(q) variation alone while ArgmaxCorrect(q) = 1 throughout. This directly operationalizes the stage-certification gap: the same routing stage that certifies correctly at 93% coexists with P@5 anywhere in [0.053, 0.68] depending solely on the orchestration policy applied after routing terminates.

Note: this experiment measures P@5 and does not evaluate whether broader fan-out improves recall at cutoffs beyond k=5. The tradeoff between specificity preservation and long-tail recall under expanded C(q) is a distinct question outside the scope of this study.

### 4.4 Density Stress Test (Falsification Control Against H1)

This experiment is not an ablation in the conventional ML sense. It is a falsification-oriented stress test: constructed to give H1 the best possible conditions and asking whether H1's monotonic prediction holds. The corpus geometry (8,000 vectors) does not reproduce the production 1.1M-vector index. The claim is deliberately narrow — density increase alone, without orchestration change, fails to reproduce post-patch performance even under conditions favorable to H1 — positioning the result as a counterexample to H1's monotonic prediction rather than a simulation of production behavior.

**Methodology:** Nine-level variation of civic-program share over a fixed 8,000-vector corpus. ANN index rebuilt at each level; identical HNSW parameters, cosine space, constant embeddings. Single deterministic seed; inter-level fluctuations within the plateau should not be over-interpreted.

| Civic Share | Civic Docs | P@5 | MRR |
|---|---|---|---|
| 0.013% | 1 | 0.12 | 0.42 |
| 0.1% | 8 | 0.70 | 0.80 |
| 0.5% | 40 | 0.67 | 0.75 |
| 1.0% | 80 | 0.61 | 0.70 |
| 2.5% | 200 | 0.67 | 0.76 |
| 5.0% | 400 | 0.70 | 0.82 |
| 10.0% | 800 | 0.69 | 0.81 |
| 25.0% | 2,000 | 0.70 | 0.82 |
| 50.0% | 4,000 | 0.70 | 0.82 |

Performance transitions sharply between 0.013% and 0.1% civic share, then plateaus. H1 predicts continued monotonic gains through post-patch performance levels; the plateau is the counterexample. The production fayette_county_resources_2026 collection operates at approximately 3.6% civic share in isolation — within the plateau band — and retrieves at P@5 0.70 under isolated conditions. H1 cannot account for why production failure occurred from a density regime that controlled conditions demonstrate to be retrieval-sufficient.

The fan-out expansion experiment (§4.3) and the density stress test together constitute the paper's empirical argument: the former demonstrates the mechanism by directly varying C(q); the latter forecloses density as the primary alternative explanation.

---

## 5. Routing Logic Inspection and Patch

### 5.1 ArgmaxCorrect Measurement (H4 Test)

| Category | n | Expected c†(q) | Correct ĉ(q) | % |
|---|---|---|---|---|
| Emergency food | 5 | rag-fayette | 5 | 100% |
| Utility assistance | 5 | rag-fayette | 5 | 100% |
| Housing programs | 5 | rag-civic | 4 | 80% |
| Healthcare enrollment | 5 | rag-fayette / rag-civic | 5 | 100% |
| Childcare subsidy | 5 | rag-fayette | 5 | 100% |
| SSI/disability | 5 | rag-civic | 4 | 80% |
| **Overall** | **30** | — | **28** | **93%** |

H4 is not supported. The stage-certification gap on the same benchmark:

| Stage | Property | Metric | Value |
|---|---|---|---|
| S(q): Routing | ArgmaxCorrect [ĉ(q) = c†(q)] | Collection-selection | 93% |
| f(S(q),C(q),R(q)): Pipeline | D̄₅ (dilution magnitude) | P@5 gap | +0.627 |
| Pipeline | End-to-end | P@5 | 0.053 |

Routing evaluation reports 93% success on the certified property. The pipeline fails on the uncertified property. The gap between these two measurements is the stage-certification gap this paper characterizes.

### 5.2 Fan-Out Override: Code Inspection

```python
# Pre-patch: unconditional fan-out override
civic_pair = {
    "rag-civic", "rag-gis-benefits", "rag-local-resources",
    "rag-wv-resources", "rag-fayette"
}
if civic_pair.issubset(set(non_zero.keys())) and \
        not civic_pair.issubset(set(candidates)):
    candidates = list(dict.fromkeys(
        candidates + [s for s in civic_pair if s not in candidates]
    ))
```

The condition tests non_zero.keys() — set membership — not score magnitudes. This is the Layer 3 interface failure: the orchestration stage receives the non_zero set from the routing stage but not the score ordering. A scorer where ĉ(q) = c†(q) with score 100 and all others score 1 triggers the identical merge as a scorer with scores 6, 5, 4, 3, 3. No improvement to S(q) — including perfect calibration — can repair a C(q) policy that operates on a lossy projection of S(q)'s output. The score ordering is discarded at the interface; restoring ArgmaxCorrect's compositional meaning requires passing magnitude, not just membership, into construction decisions.

This was a deliberate coverage-robustness design decision, not an implementation defect. The system's intent was to ensure no civic collection was excluded even under uncertain routing. The failure mode is that its D_k consequences were unaudited, and no existing routing metric could have detected them.

### 5.3 Patch: Score-Conditioned Tiered Construction

```python
# Post-patch: score-conditioned tiered construction
CIVIC_TIER_1 = {"rag-fayette"}
CIVIC_TIER_2 = {"rag-civic", "rag-gis-benefits"}
CIVIC_TIER_3 = {"rag-local-resources", "rag-wv-resources"}

if any(s in non_zero for s in CIVIC_TIER_1 | CIVIC_TIER_2 | CIVIC_TIER_3):
    if non_zero.get("rag-fayette", 0) >= 5:
        candidates = ["rag-fayette"]
    elif any(non_zero.get(s, 0) > 0 for s in CIVIC_TIER_2):
        candidates = [
            s for s in ["rag-fayette", "rag-civic", "rag-gis-benefits"]
            if non_zero.get(s, 0) > 0
        ]
    else:
        candidates = [
            s for s in ["rag-local-resources", "rag-wv-resources"]
            if non_zero.get(s, 0) > 0
        ]
```

The patch conditions C(q) construction on score magnitude rather than set membership, closing the Layer 3 interface gap between what S(q) certifies and what C(q) preserves. Note that the patch reduces C(q) breadth and may reduce long-tail recall relative to the pre-patch fan-out policy; this tradeoff was accepted in exchange for specificity preservation at the evaluated cutoffs.

---

## 6. Post-Patch Validation

Post-patch results are reported in §4.2 (P@5 0.68, MRR 0.79). Recovery from P@5 0.053 to 0.68 under constant corpus and embedding conditions is consistent with H2 and inconsistent with H1: a density-primary account predicts no improvement from removing the fan-out override without corpus changes. The fan-out expansion experiment (§4.3) renders this explicit — the full performance range is achievable through C(q) variation alone.

Post-patch P@5 0.68 substantially exceeds the pre-patch unrouted baseline (0.207), restoring the expected advantage of jurisdiction-aware retrieval. Two queries with no relevant results post-patch reflect genuine corpus gaps, not orchestration failures.

---

## 7. Discussion

### 7.1 Non-Compositionality of Stage-Level Certification

Stage-level evaluation composes into a pipeline-level guarantee only when every stage in the pipeline is jointly evaluated. In modular retrieval systems with independently implemented scoring and orchestration stages, routing benchmarks provide a stage-level guarantee for S(q) that does not propagate to C(q). Changes to the orchestration stage — through schema updates, collection additions, fan-out policy modifications, or query distribution drift — can increase D̄_k without any routing-layer signal of degradation.

This monitoring gap is structural: a system instrumented only for ArgmaxCorrect is blind by construction to specificity preservation failures that originate in C(q). The appropriate audit metric is D̄_k: periodically comparing P@k({c†(q)}) against P@k(C(q)) for a held-out query sample directly measures whether orchestration policy is preserving what the scoring stage produces. Systems that accept D̄_k > 0 as an explicit coverage-recall tradeoff are not pathological; systems that do not measure D̄_k cannot know which regime they occupy.

### 7.2 ANN Amplification and the Case for Exact-Search Controls

The stage-certification gap is defined at the orchestration layer and does not require ANN approximation: D_k(q) > 0 can occur under exact nearest-neighbor retrieval whenever lower-specificity collections displace relevant results within a finite k. However, HNSW traversal over a large, semantically homogeneous low-specificity population may reduce the probability of surfacing sparse target vectors within a fixed retrieval budget, amplifying D̄_k magnitude beyond the baseline architectural effect.

The strongest remaining experimental gap is the absence of an exact-search control: brute-force cosine retrieval over a reduced corpus subset comparing top-1 exclusive against top-5 fan-out would determine whether D_k > 0 persists when traversal dynamics are removed. If the effect persists under exact search, the architectural claim is substantially strengthened and ANN amplification becomes a secondary modifier rather than a potential primary cause. If the effect attenuates significantly under exact search, the ANN contribution becomes a more important part of the explanation than the current framing implies. We treat exact-search isolation as the single highest-priority extension of this work. The general contribution — stage-certification non-compositionality — survives either outcome; the mechanism-level magnitude claim benefits most from this control.

### 7.3 Calibration Independence

Specificity preservation failure is orthogonal to score calibration. The construction policy consults non_zero keys, not relative score magnitudes (§5.2). Any score distribution that leaves all five collections non-zero produces the identical merge, regardless of how wide or narrow the score spread is. This is the third layer of independence in the decomposition: ArgmaxCorrect and D̄_k are separately measurable; D̄_k failures are not addressable through S(q) improvements; and the interface contract between S(q) and C(q) is therefore itself an object requiring specification and evaluation. Closing the gap requires changes at the interface — specifically, passing score magnitudes, not just non-zero membership, into construction decisions.

### 7.4 Generalization Conditions

The stage-certification gap is a structural property of any modular pipeline in which scoring and candidate-set construction are independently implemented stages with no enforced interface contract propagating score ordering into construction decisions. The specific fan-out mechanism that instantiates it here requires four additional conditions: (1) a fan-out policy that expands C(q) ⊃ {c†(q)} conditioned on membership rather than dominance; (2) collection composition such that the expanded set is semantically sparse relative to the target query distribution; (3) a query distribution that benefits from high-specificity selection; and (4) a finite retrieval cutoff k at which lower-specificity material displaces target-collection results.

The general claim — that stage-certification gaps can exist and are undetectable by stage-level evaluation — requires only condition (0): independently implemented pipeline stages. This is a common architectural property of multi-index RAG systems, federated search with department-scoped sub-indices, hierarchical retrieval with tiered specificity levels, and modular retrieval pipelines where collection selection and candidate assembly evolve independently. Whether candidate-set dilution specifically produces comparable degradation in those contexts is an empirical question this paper does not address. We demonstrate existence; we characterize mechanism; we propose an audit metric. Prevalence across architectures requires future cross-system study.

---

## 8. Related Work

**Federated search and collection selection.** Shokouhi & Si (2011) survey federated retrieval comprehensively. Si & Callan (2003) address resource selection via relevant document distribution estimation. This literature evaluates ArgmaxCorrect — a necessary but insufficient pipeline condition. The present paper addresses the composition of argmax correctness with orchestration behavior, a gap this literature does not evaluate. The key distinction is that federated search evaluation typically assumes that selecting the correct collection terminates the relevant measurement; this paper argues that assumption holds only when C(q) is deterministically derived from S(q)'s argmax output, which is not guaranteed when orchestration is independently implemented.

**Multi-index RAG and retrieval routing.** Lewis et al. (2020) and Guu et al. (2020) establish retrieval-augmented generation. Multi-index RAG frameworks expose routing APIs that score collections independently from candidate-set assembly, directly instantiating the architectural decoupling characterized here. Asai et al. (2023) address adaptive retrieval in self-RAG; candidate-set construction policy is a distinct downstream concern not measured by adaptive routing evaluation.

**Expert routing and MoE gating.** Fedus et al. (2022) and Shazeer et al. (2017) analyze gating in sparse MoE architectures. The stage-certification gap is structurally analogous to a gating evaluation that certifies expert selection without measuring the composition of selected expert outputs: correct gating does not guarantee that combined outputs preserve the signal from the gating decision when lower-relevance experts are included unconditionally.

**Cascade and multi-stage retrieval.** The stage-certification gap is most directly related to composition failures in cascade retrieval architectures. Wang et al. (2011) and Matsubara et al. (2020) analyze pipeline-level correctness in multi-stage systems where an early-stage filtering decision passes a reduced candidate set to a later stage. The core principle — that a correct early-stage decision does not guarantee a correct late-stage outcome when the inter-stage interface loses information — is the structural analogue of the certification gap characterized here.

The failure modes are formally symmetric and empirically distinct. Cascade retrieval degrades when too much is pruned: aggressive early-stage filtering removes relevant documents before later stages can recover them. Modular fan-out degrades when too much is included: post-routing candidate-set expansion absorbs relevant documents into a lower-specificity population that overwhelms them at the retrieval cutoff. Both pathologies represent inter-stage interface failures; both are invisible to the other stage's evaluation metric. Formalizing this symmetry — as a general theory of interface contract failures in retrieval pipelines — is a productive direction for future work. This paper establishes the expansion-side failure mode and provides a measurement instrument (D̄_k) for detecting it; the pruning-side failure mode is the established cascade retrieval result.

**Dense retrieval and ANN.** Karpukhin et al. (2020) establish DPR; Reimers & Gurevych (2019) describe the sentence embedding architecture used here; Malkov & Yashunin (2020) describe HNSW. ANN parameters are held constant across experimental conditions. The ANN contribution to observed D̄_k magnitude is unresolved (§7.2).

---

## 9. Threats to Validity

### 9.1 Internal Validity

- Single annotator, no inter-annotator agreement. Directional bias from operational knowledge of local resources is possible.
- No held-out evaluation set. The same 30-query benchmark is used across all conditions.
- ANN contribution not isolated. Exact-search controls are absent; observed D̄_k magnitude may partly reflect HNSW traversal dynamics.
- Single-seed density stress test. Inter-level fluctuations within the plateau should not be over-interpreted.

### 9.2 External Validity

- Single deployment. One system, one county, one embedding model, one ANN implementation. Structural generalization argued in §7.4; empirical generalization not claimed.
- Transient corpus state. Pre-patch unrouted baseline reflects corpus composition at evaluation time.

### 9.3 Construct Validity

- Relevance operationalizes actionability for Fayette County residents; domain transfer not assumed.
- c†(q) is defined formally as the specificity-maximizing collection but operationalized through expert judgment rather than exhaustive per-collection precision measurement. The two may diverge for queries where expert-expected and empirically-best collections differ.
- Expected collection definitions are author-defined without independent validation.
- Density stress test does not reproduce production ANN geometry. The claim is a counterexample to H1's monotonic prediction, not a production-realistic simulation.
- SpecificityPreserved is a thresholded interpretation of the continuous D_k; the binary framing is conceptual shorthand (§1.1).

### 9.4 Statistical Conclusion Validity

- 30 queries is underpowered for small effects. Observed effect sizes are sufficiently large that significance is demonstrated; subtle differences are not reliably detectable.
- Density transition region is configuration-specific, not a universal threshold.

---

## 10. Conclusion

Stage-level evaluation is not compositionally predictive of pipeline behavior in modular retrieval architectures. ArgmaxCorrect certifies a property of S(q); deployment behavior depends additionally on C(q); these stages are independently implemented and separately evaluable. The stage-certification gap is the structural consequence: a pipeline can satisfy routing evaluation while exhibiting substantial retrieval degradation that routing metrics cannot observe.

The evaluated system instantiates this at scale:

| Stage | Property | Metric | Value |
|---|---|---|---|
| S(q): Routing | ArgmaxCorrect [ĉ(q) = c†(q)] | Collection-selection | 93% |
| C(q) interface | Dilution magnitude | D̄₅ | +0.627 |
| Pipeline | End-to-end | P@5 | 0.053 |

    ArgmaxCorrect(q) = 1   ⟹̸   D_k(q) = 0

The fan-out expansion experiment directly manipulates only C(q) under constant S(q), corpus, embeddings, and ANN — producing monotonic degradation from P@5 0.68 to 0.053 while ArgmaxCorrect(q) = 1 throughout. The density stress test forecloses H1. A score-conditioned patch recovers P@5 to 0.68 under constant corpus conditions.

This is the dual failure mode to cascade pruning: where cascade architectures degrade when too much is filtered, modular fan-out degrades when too much is included — and neither failure is visible to the other stage's evaluation metric. The appropriate response is not to improve routing accuracy, which is already near ceiling, but to instrument the inter-stage interface. D̄_k should be measured alongside ArgmaxCorrect in any modular retrieval system where S(q) and C(q) are independently implemented and evolved. Monitoring only ArgmaxCorrect certifies a stage; monitoring D̄_k certifies the pipeline interface that stage-level evaluation, by construction, cannot reach.

---

## Appendix A: Reproducibility Record

System: 48 ChromaDB collections, 7,902,937 vectors; sentence-transformers/all-MiniLM-L6-v2 (384-dim); HNSW ef_construction=100, ef_search=100, max_neighbors=16.

| Artifact | Description | Commit |
|---|---|---|
| docs/experiments/density_ablation_results.csv | 9-level stress test | 75f04ab1 |
| docs/experiments/fanout_expansion_results.csv | 3-condition experiment | c9d2f3a8 |
| eval_routed_final.csv | Pre-patch judgments | — |
| eval_unrouted_final.csv | Unrouted judgments | — |
| eval_postpatch_final.csv | Post-patch judgments | — |
| services/rag_query_router.py | Tiered routing patch | a3eebc5f |

---

## Appendix B: Representative Annotated Examples

**Example 1 — Preservation failure: address-record dominance** | D₅(q) = 1.0

Query: "My power is about to be shut off in Fayette County"

| Rank | Condition | Preview | Relevant |
|---|---|---|---|
| 1 | Pre-patch | Fayette County E-911, 1047 Nick Rahall Greenway | 0 |
| 2 | Pre-patch | Fayetteville Public Library, 200 W Maple Ave | 0 |
| 1 | Post-patch | LIEAP, Fayette County Community Action | 1 |
| 2 | Post-patch | WV DHHR Energy Assistance Program | 1 |

ArgmaxCorrect(q) = 1, ĉ(q) = c†(q) = rag-fayette. D₅(q) = 1.0. The scoring stage correctly placed rag-fayette at +6. The construction stage merged 1.1M address-point vectors; address records dominate the ANN result. The stage-certification gap is observable at the individual query level: correct routing, failed retrieval, no routing metric detects it.

**Example 2 — Control: preservation success under geometric separation** | D₅(q) = 0

Query: "What free clinics are available in Fayette County?"

| Rank | Condition | Preview | Relevant |
|---|---|---|---|
| 1 | Pre-patch | Fayetteville Clinic, free health clinic | 1 |
| 2 | Pre-patch | Rural Health Fayette Clinic PLLC | 1 |

D₅(q) = 0 pre-patch. Dilution is query-conditional: queries where c†(q) vectors are geometrically distinguishable from the dominant address-record population survive fan-out; those where separation is insufficient do not. This within-benchmark variation shows that D_k is governed by the interaction between C(q) policy and per-query embedding geometry — consistent with H2 and inconsistent with H1, which predicts uniform density effects.

**Example 3 — Unrouted jurisdictional noise**

Query: "What food banks are open in Fayette County?"

| Rank | Condition | Preview | Relevant |
|---|---|---|---|
| 3 | Unrouted | Mountaineer Food Bank, Mercer and Monroe County | 0 |
| 5 | Unrouted | Green Bank Public Library, Green Bank WV | 0 |

The unrouted baseline (P@5 0.207) outperforms pre-patch routing not because unscoped retrieval is structurally superior, but because no fan-out policy operates to induce D_k > 0. Post-patch P@5 0.68 eliminates both the preservation failure and jurisdictional noise, representing the correct ceiling when ArgmaxCorrect(q) = 1 and D_k(q) ≈ 0 hold simultaneously.

---

## References

- Asai, A., Wu, Z., Wang, Y., Sil, A., & Hajishirzi, H. (2023). Self-RAG: Learning to retrieve, generate, and critique through self-reflection. arXiv:2310.11511.
- Fedus, W., Zoph, B., & Shazeer, N. (2022). Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity. JMLR, 23(120), 1–39.
- Guu, K., Lee, K., Tung, Z., Pasupat, P., & Chang, M. (2020). REALM: Retrieval-augmented language model pre-training. ICML 2020.
- Karpukhin, V., Oguz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., & Yih, W. T. (2020). Dense passage retrieval for open-domain question answering. EMNLP 2020.
- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. NeurIPS 2020.
- Malkov, Y. A., & Yashunin, D. A. (2020). Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs. IEEE TPAMI, 42(4), 824–836.
- Matsubara, Y., Gangi, M. A., & Magnini, B. (2020). Reranking in multi-stage retrieval for open-domain QA. EMNLP 2020.
- Purves, R. S., Clough, P., Jones, C. B., & Joho, H. (2018). Geographical information retrieval: Progress and open research questions. Transactions in GIS, 22(6).
- Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using Siamese BERT-networks. EMNLP 2019.
- Shazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le, Q., Hinton, G., & Dean, J. (2017). Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. ICLR 2017.
- Shokouhi, M., & Si, L. (2011). Federated search. Foundations and Trends in Information Retrieval, 5(1), 1–102.
- Si, L., & Callan, J. (2003). Relevant document distribution estimation method for resource selection. SIGIR 2003.
- Wang, L., Lin, J., & Metzler, D. (2011). A cascade ranking model for efficient ranked retrieval. SIGIR 2011.
