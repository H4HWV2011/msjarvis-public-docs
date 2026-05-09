
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
