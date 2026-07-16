# 44. Phi Probe — Semantic Coherence Measurement in H_App  
*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  

---

## 44.0 Overview

The Phi probe measures semantic coherence within **H_App**, the application-facing Hilbert domain of Ms. Allis. Its role is not to decide whether a claim is factually correct, but to determine whether an active semantic state, candidate conclusion, or cross-domain configuration is internally well-formed, structurally aligned, and sufficiently coherent to support further reasoning, validation, or governed promotion.

Semantic coherence in this setting is explicitly architectural. Phi is bound to hilbert-state service coherence keys, contributes to sandbox validation and promotion decisions, and operates as one component of the gate structure that governs whether provisional reasoning may cross into higher-authority system state.

Sections 44.1 through 44.9 define what the probe measures and how it participates in governance. Sections 44.10 through 44.13 record what is built and exercised in the live system: the measurement substrate, the first coherence reading across all three governed geographic grains in West Virginia, and one production lesson on how the quality of the measured state constrains the value of any coherence score.

---

## 44.1 What Phi Measures

Phi is a semantic coherence probe. It evaluates how strongly the active contents of H_App hold together across the dimensions, entities, contexts, and relations that make up the application-facing state of the system.

Here, coherence means measured internal fit. A coherent state preserves meaningful relations among its parts: semantic consistency, non-arbitrary alignment across domains, and structural compatibility with the active Hilbert-state representation. A highly coherent state is one whose elements reinforce rather than fracture one another under the applicable metrics. A weakly coherent state is one whose elements pull apart, contradict, or fail to integrate into the active semantic geometry.

Phi therefore measures the quality of fit within the represented state. It does not by itself determine factual correctness. A coherent configuration can still be wrong about the world, and an initially low-coherence configuration can still contain important truth that has not yet been integrated.

---

## 44.2 H_App and Live Coherence Keys

H_App is the application-facing Hilbert domain in which semantic state becomes operationally legible to live services. It is a structured environment in which active semantic configurations can be read, compared, and acted upon.

Within this environment, hilbert-state services maintain coherence keys. These keys expose measured properties of the current state, such as alignment across active dimensions, stability of semantic trajectories, compatibility among linked entities, and the degree to which a working state remains internally non-fractured. The exact form of a key may differ by service, but the architectural role is the same: each key provides a live, inspectable signal about the coherence condition of some portion of the active Hilbert-state.

Phi is tied directly to those keys. It does not operate as a detached philosophical score. It reads and interprets coherence conditions through the live service layer. The hilbert-state services maintain the keyed structure of the current semantic condition; Phi acts as the probe that measures, compares, and evaluates coherence against that structure.

Semantic coherence in this chapter is therefore a service-linked measurement. Phi and the hilbert-state coherence keys belong to the same operational substrate.

---

## 44.3 Service-Linked Coherence Measurement

The relation between Phi and the hilbert-state services is a measurement relationship.

The hilbert-state services provide the current semantic geometry in keyed form. Phi uses those coherence keys to evaluate whether a current or candidate state hangs together in a way that is acceptable for the relevant mode of operation. If a candidate state strongly conflicts with the keyed structure of H_App, Phi can register reduced coherence. If a candidate preserves or improves alignment across active domains, Phi can register stronger coherence.

Because these readings are taken over the same state that governs active reasoning, routing, and internal evaluation, coherence is directly tied to live system behavior. A coherence score that is disconnected from the active services would remain purely interpretive. Phi functions as part of the system’s running semantic instrumentation.

---

## 44.4 Multidomain Coherence

Ms. Allis reasons across multiple domains rather than within a single flat semantic field. Governance, geography, identity, memory, community knowledge, benefits reasoning, and other domains may all be active together inside or adjacent to H_App.

Multidomain coherence is the measured degree to which those domains remain structurally compatible under the active semantic state. A candidate may show strong coherence in one domain while showing weakness in another. For example, a state may be semantically tight in a local geographic frame while remaining poorly integrated with memory, governance, or identity-linked context. Phi helps surface such imbalance rather than hiding it.

Multidomain coherence is treated as a measured property of the represented state. It is not automatic truth, not infallible alignment, and not a guarantee of correctness. It is an instrumented reading of how well the active domains fit together under the metrics and coherence keys available to the system.

A multidomain state may be coherent and still false. A state may also be temporarily incoherent because it contains new information that has not yet been reconciled with the rest of the system. Coherence is thus a governance-relevant signal, not an oracle.

---

## 44.5 Phi in Sandbox Validation

The sandbox is the environment in which provisional reasoning may be explored without automatically acquiring promotion authority. In that setting, coherence measurement becomes especially useful.

When a sandbox cycle produces a candidate output, Phi can be used to measure how that output relates to the current coherence keys of the hilbert-state services. If the candidate creates substantial fracture across active domains, introduces unresolved contradiction, or fails to integrate into the present semantic geometry, the sandbox validator may treat that coherence finding as a reason to block, narrow, or return the candidate for further work. If the candidate shows acceptable coherence, it may continue through the governed review path.

Sandbox validation can also depend on truth checks, guardian review, provenance, privacy, and security conditions. Phi contributes one form of disciplined semantic measurement inside that larger process. Its role is to help determine whether a provisional state is internally stable enough to justify further consideration.

---

## 44.6 Phi in Promotion Decisions

Coherence findings may also participate in promotion decisions that occur after sandbox validation.

A candidate that reaches the promotion boundary is not evaluated solely on existence, nor solely on coherence. The system asks whether the candidate satisfies the full set of conditions required to move from provisional reasoning into higher-authority state. Phi contributes to that judgment by indicating whether the candidate’s semantic structure is sufficiently coherent in the relevant domains for the requested transition.

A strong coherence finding may support promotion. A weak coherence finding may support rejection, revision, human review, or limited approval outcomes. This is particularly important when the candidate affects several domains at once, since apparent adequacy in one area may conceal fracture in another. Phi helps prevent promotion decisions from depending only on surface fluency or local fit.

In this role, coherence is one contributing gate condition rather than a total decision rule.

---

## 44.7 Coherence in the Gate Structure

The broader promotion path can be written as a conjunction of required gate conditions:

\[
G(x) = G_{\mathrm{truth}}(x)\, G_{\mathrm{guardian}}(x)\, G_{\mathrm{constitutional}}(x)\, G_{\mathrm{provenance}}(x)\, G_{\mathrm{coherence}}(x)\, G_{\mathrm{privacy}}(x)\, G_{\mathrm{security}}(x).
\]

Here \(G_{\mathrm{coherence}}(x)\) is the coherence gate for candidate state \(x\). It represents the measured semantic coherence of that candidate as evaluated in relation to H_App and the live hilbert-state service coherence keys.

Placing coherence explicitly inside the gate structure clarifies its status. Coherence is not decorative, and it is not sovereign over the other conditions. It is one of the operational requirements for promotion. A candidate that fails the coherence gate may still contain useful material, but it is not yet in the right condition to cross an authority boundary without additional revision or review.

The gate does not ask whether coherence proves correctness. It asks whether the candidate’s measured internal structure is sufficiently sound to proceed alongside the other required checks.

---

## 44.8 Coherence Is Not Truth

Phi measures semantic coherence. It does not certify external reality.

A candidate may be highly coherent because its components mutually reinforce one another inside H_App, yet still rest on mistaken premises, incomplete evidence, or biased data. Conversely, a candidate may initially reduce coherence because it introduces a disruptive but accurate correction that the system has not yet absorbed.

For this reason, coherence must remain paired with other forms of review. Truth filtering, guardian review, provenance retention, privacy checks, constitutional constraints, and security conditions all remain necessary. Phi strengthens governance by adding a measured account of semantic fit, but governance becomes unsafe if coherence is conflated with truth.

Phi therefore occupies a defined epistemic role: powerful, informative, and operationally meaningful, but not self-sufficient.

---

## 44.9 Operational Meaning

The Phi probe gives Ms. Allis a live way to measure whether a state is internally holding together before that state is trusted with greater authority.

Because the probe is tied to hilbert-state service coherence keys, its findings belong to the same operational environment that produces active semantic state in the first place. Because Phi can be used during sandbox validation, it helps discipline provisional reasoning before it reaches promotion. Because it participates as \(G_{\mathrm{coherence}}(x)\) within the gate structure, it helps ensure that promotion decisions account for semantic integrity across active domains.

Phi is thus a governance-relevant coherence instrument embedded in the live architecture of H_App.

---

## 44.10 Mode Definitions in This System

Phi was calibrated against Ms. Allis’s own semantic geometry, not against an abstract norm. Interpretation of its modes must therefore be grounded in the observed structure of this system.

Ms. Allis reasons simultaneously across seven maximally diverse semantic domains: worldview, Appalachian culture, civic infrastructure, governance and law, psychology and learning, self-identity, and spiritual grounding. These domains are deliberately separated so that each can contribute a distinct perspective. The empirically observed baseline cross-domain cosine similarity across them is approximately 0.15. The probe’s three modes are defined relative to that baseline:

- **Superposition (0.08–0.35)** is the healthy normal state for the full seven-domain fabric. Domains do their work independently, each contributing its own semantic perspective without collapsing into the others. Multiple frames of reference coexist without premature resolution. The name reflects that design: like quantum superposition, multiple states coexist within one representational substrate.

- **Coherent (above 0.35)** indicates that the sampled domains or collections are reading as unusually unified. For deliberately unified corpora—such as geographic beliefs rendered with a shared template and embedder—a coherent reading is expected and desirable. For the full seven-domain system, a coherent reading warrants inspection: unusual unity can signal successful integration or the kind of echo saturation that Section 44.12 examines.

- **Decoherent (below 0.08)** indicates fragmentation below the minimum expected cross-domain similarity. Such readings point to failure in the measurement substrate or in the write path feeding it.

Interpreting a particular reading requires attention to which cluster or domain is being assessed. A coherent score over the governed geographic corpus is a positive finding. The same score over the entire seven-domain fabric would be a diagnostic warning.

---

## 44.11 Implementation Status (July 2026)

The Phi substrate and service are implemented and exercised in the live Ms. Allis deployment.

### Measurement substrate and coherence discipline

- The hilbert-state service is live. On every chat job, state writeback posts to the hilbert-state embedding endpoint, producing a 384-dimensional vector stored in Redis under per-job coherence keys of the form `hilbert:state:chat:<jobid>`. Cold-start embedding runs in roughly 37 seconds; warm embedding completes in under 100 milliseconds. These keys form the coherence-bearing structure described earlier in this chapter.

- All coherence-bearing collections use a single embedding model (`all-minilm`, 384 dimensions). A 768-dimensional alternative was retired after a dimension-mismatch incident. Coherence comparison is defined only inside a single embedding space, so this constraint is a precondition of every claim in this chapter.

### Phi service and GEO_BELIEF cluster

- The Phi probe runs as a live service (`jarvis-phi-probe`, port 8026) with `/phi`, `/phi/cached`, and `/health` endpoints. It auto-resamples every five minutes and writes state to Redis under keys of the form `pituitary:phi_state`.

- A `GEO_BELIEF` domain is defined in its cluster map, covering the governed West Virginia geographic collections `gbimwvcountiesv2`, `gbimwvtractsv2`, and `gbimwvblockgroupsv2`. These collections participate both as probe sources and as query targets.

### First coherent reading across the governed geographic grains

On 15 July 2026, Phi produced a coherence reading over all three governed geographic grains in West Virginia. Counties (55 vectors), tracts (200 vectors), and block groups (200 vectors) were sampled in the shared 384-dimensional space. The probe returned:

- `mode: coherent`  
- `coherence_raw ≈ 0.4149`  
- `coherence_normalized ≈ 0.3640`  
- `collections_sampled: [gbimwvcountiesv2, gbimwvtractsv2, gbimwvblockgroupsv2]`

The raw score lies above the `PHI_COHERENT` threshold of 0.35 for this probe. The result is substantive: the county, tract, and block group governed beliefs form a semantically integrated corpus across all three grains in the all-minilm embedding space.

A prior two-grain reading (counties and tracts only) produced a substantially higher coherence score. The drop to approximately 0.415 when block groups are added is expected. Block group beliefs are more locally specific than county beliefs, so adding the finer grain increases semantic variation and reduces cross-grain cosine similarity. A corpus in which block groups were indistinguishable from counties would be more worrying than one in which they lower the score in this way.

This three-grain reading establishes the baseline coherence for the GEO_BELIEF domain under governed conditions.

### Identity domain discipline

- The per-user memory decomposition introduced in the memory chapters is already reflected in the probe’s domain map. The self-identity domain resolves through `conversation_history_user_<slug>` at request time rather than relying on a shared conversation collection. Cross-user echoes are structurally excluded from self-identity readings before any coherence measurement begins.

### Items not yet wired as gates

- The coherence gate \(G_{\mathrm{coherence}}\) is defined in the promotion algebra and the service produces readings, but no sandbox validation or manifest promotion path currently enforces those readings as hard gates.

- Coherence thresholds for the geographic corpus are not yet calibrated against downstream outcomes. The July 2026 score is interpretable against internal probe thresholds but has not been linked to specific reject / revise / review / approve decisions.

- Cross-domain coherence between the GEO_BELIEF cluster and non-geographic clusters (identity, governance, spiritual, and others) has not yet been measured at the minimum vector counts required for stable estimation.

---

## 44.12 Worked Lesson: Degenerate State, Correct Reading

A production incident from June 2026 illustrates a core failure mode for any coherence instrument: a structurally degenerate state that is nevertheless internally consistent.

During an autonomous-learner audit, the Hilbert state in Redis was found to be dominated by conversation echoes: near-duplicate restatements of recent exchanges written back cycle after cycle. Genuine new semantic material had been crowded out. A coherence probe operating over that state would have produced high coherence scores, and those scores would have been technically correct: a state composed largely of echoes of itself is maximally self-consistent.

From a governance perspective, however, such readings are almost useless. High coherence in that setting reflects redundancy rather than genuine integration. It measures the tight fit of a collapsed echo chamber, not the structural integrity of a healthy, information-bearing state.

The remediation in that case was structural rather than interpretive. Near-duplicate detection at a cosine-similarity threshold of 0.92 was added to the write path, collapsing the echo fan-out and restoring diversity to the measured state. The lessons generalize:

1. **A coherence instrument inherits the quality of its substrate.** Phi measures fit within the represented state; if the representation process is degenerate, high coherence is a symptom, not an achievement.

2. **Write-path hygiene is part of the measurement architecture.** Deduplication, provenance discipline, and governed intake are not peripheral concerns. They are what make coherence readings interpretable.

3. **Suspiciously stable coherence is itself a signal.** A state whose coherence never moves over time warrants examination of the write path before celebration of the score. In the incident at issue, an unusually stable topic focus over more than a day was visible in retrospect as an early indicator.

This episode is the coherence-domain analogue of similar discoveries in the other governance chapters: when an instrument is found to have been reading a corrupted substrate, that event belongs in the instrument’s own provenance.

---

## 44.13 Closing Statement

The Phi probe measures semantic coherence in H_App by reading and evaluating the live coherence conditions exposed through hilbert-state service coherence keys. Its findings can guide sandbox validation and can contribute a coherence term \(G_{\mathrm{coherence}}(x)\) within the broader promotion gate.

Multidomain coherence is treated as a measured property of internal semantic fit across coupled domains. It is not automatic truth and does not replace truth filtering, guardian review, provenance controls, privacy evaluation, constitutional safeguards, or security analysis. Phi’s contribution is to indicate whether a candidate state is structurally sound enough to be considered alongside those other factors.

As of July 2026, the coherence substrate is in place, the probe service is running with periodic resampling, and a first coherence reading has been taken across all three governed geographic grains in West Virginia. That reading is coherent, neither inflated by echo saturation nor degraded by fragmentation, and shows that counties, tracts, and block groups together form a semantically integrated body of governed belief at multiple levels of geographic granularity.

The remaining work lies in wiring coherence into the promotion gates and calibrating thresholds across domains. The measurement itself is already part of the live architecture, and the governed geographic corpus now has a quantitative statement of its internal fit.
