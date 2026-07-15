# 44. Phi Probe — Semantic Coherence Measurement in H_App
*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 15, 2026*

---

## 44.0 Overview

The Phi probe measures semantic coherence within **H_App**, the application-facing Hilbert domain of Ms. Allis. Its purpose is not to declare whether a claim is true, but to determine whether an active semantic state, candidate conclusion, or cross-domain configuration is internally well-formed, structurally aligned, and sufficiently coherent to support further reasoning, validation, or governed promotion.

This chapter places Phi inside the live architecture rather than outside it. Semantic coherence is tied to hilbert-state service coherence keys, can influence sandbox validation and promotion decisions, and functions as one component of the broader gate structure that governs whether provisional reasoning may cross into higher-authority system state.

As with Chapters 42 and 43, this revision separates design from audit. Sections 44.1 through 44.9 state what the probe is and how it participates in governance. Sections 44.10 through 44.12 record what is verified as built as of this writing: the measurement substrate that is live, the first real coherence reading produced against all three governed geographic grains, and one production incident that demonstrates why the quality of the measured state matters as much as the measurement itself.

---

## 44.1 What Phi Measures

Phi is a semantic coherence probe. It evaluates how strongly the active contents of H_App hold together across the relevant dimensions, entities, contexts, and relations that make up the application-facing state of the system.

In this chapter, coherence means measured internal fit. It refers to whether a given state preserves meaningful relation among its parts: semantic consistency, non-arbitrary alignment across domains, and structural compatibility with the active Hilbert-state representation. A highly coherent state is one whose elements reinforce rather than fracture one another under the applicable metrics. A weakly coherent state is one whose elements pull apart, contradict, or fail to integrate into the active semantic geometry.

Phi therefore measures the quality of fit within the represented state. It does not by itself determine factual correctness. A coherent configuration can still be wrong about the world, and an initially low-coherence configuration can still contain important truth that has not yet been integrated.

---

## 44.2 H_App and Live Coherence Keys

H_App is the application-facing Hilbert domain in which semantic state becomes operationally legible to live services. It is not only a conceptual space for analysis; it is the structured environment in which active semantic configuration can be read, compared, and acted upon.

Within this environment, hilbert-state services maintain coherence keys. These keys expose measured properties of the current state, such as alignment across active dimensions, stability of semantic trajectories, compatibility among linked entities, or the degree to which a working state remains internally non-fractured. The exact form of a key may differ by service, but the architectural role is the same: the key provides a live, inspectable signal about the coherence condition of some portion of the active Hilbert-state.

Phi is related to those keys directly. It does not float above the system as a separate philosophical score. It reads and interprets coherence conditions through the live service layer. The hilbert-state services maintain the keyed structure of the current semantic condition; Phi acts as the probe that measures, compares, and evaluates coherence against that structure.

For that reason, semantic coherence in this chapter is a service-linked measurement. Phi and the hilbert-state coherence keys belong to the same operational substrate.

---

## 44.3 Service-Linked Coherence Measurement

The relation between Phi and the hilbert-state services can be understood as a measurement relationship.

The hilbert-state services provide the current semantic geometry in keyed form. Phi uses those coherence keys to evaluate whether a current or candidate state hangs together in a way that is acceptable for the relevant mode of operation. If a candidate state strongly conflicts with the keyed structure of H_App, Phi can register reduced coherence. If a candidate preserves or improves alignment across active domains, Phi can register stronger coherence.

This connection matters because it ties coherence to live system behavior. A coherence score that is disconnected from the active services would remain interpretive only. Phi belongs to governance because it operates over the same state that live services use for active reasoning, routing, and internal evaluation.

In this sense, Phi is not merely a descriptive instrument. It is part of the architecture's running semantic instrumentation.

---

## 44.4 Multidomain Coherence

Ms. Allis reasons across multiple domains rather than within one flat semantic field. Governance, geography, identity, memory, community knowledge, benefits reasoning, and other domains may all be active together inside or adjacent to H_App.

Multidomain coherence refers to the measured degree to which those domains remain structurally compatible under the active semantic state. A candidate may show strong coherence in one domain while showing weakness in another. For example, a state may be semantically tight in a local geographic frame while remaining poorly integrated with memory, governance, or identity-linked context. Phi is useful because it helps locate such imbalance rather than hiding it.

This chapter therefore treats multidomain coherence as a measured property of the represented state. It is not automatic truth, not infallible alignment, and not a mystical guarantee of correctness. It is an instrumented reading of how well the active domains fit together under the metrics and coherence keys available to the system.

That distinction is essential. A multidomain state may be coherent and still false. A state may also be temporarily incoherent because it contains new information that has not yet been reconciled with the rest of the system. Coherence is thus a governance-relevant signal, not an oracle.

---

## 44.5 Phi in Sandbox Validation

The sandbox is the place where provisional reasoning may be explored without automatically acquiring promotion authority. In that setting, coherence measurement becomes especially useful.

When a sandbox cycle produces a candidate output, Phi may be used to measure how that output relates to the current coherence keys of the hilbert-state services. If the candidate creates substantial fracture across active domains, introduces unresolved contradiction, or fails to integrate into the present semantic geometry, the sandbox validator may treat that coherence finding as a reason to block, narrow, or return the candidate for revision. If the candidate shows acceptable coherence, it may continue through the governed review path.

This use of Phi does not collapse validation into coherence alone. Sandbox validation may also depend on truth checks, guardian review, provenance, privacy, or security conditions. Phi contributes one form of disciplined semantic measurement inside that larger process. Its role is to help determine whether a provisional state is internally stable enough to justify further consideration.

That makes Phi part of the difference between merely generating a candidate and validating one.

---

## 44.6 Phi in Promotion Decisions

Coherence findings may also participate in promotion decisions after sandbox validation.

A candidate that reaches the promotion boundary is not judged solely by whether it exists, nor solely by whether it is coherent. Rather, the system asks whether it satisfies the full set of conditions required to move from provisional reasoning into higher-authority state. Phi contributes to that judgment by indicating whether the candidate's semantic structure is sufficiently coherent in the relevant domains for the requested transition.

A strong coherence finding may support promotion. A weak coherence finding may instead support reject, revise, human review, or limited approval outcomes. This is especially important when the candidate affects several domains at once, since apparent adequacy in one area may conceal fracture in another. Phi helps prevent promotion decisions from depending only on surface fluency or local fit.

In this role, coherence remains one contributing gate condition rather than a total decision rule.

---

## 44.7 Coherence in the Gate Structure

The broader promotion path can be written as a conjunction of required gate conditions:

\[
G(x) = G_{\mathrm{truth}}(x)\, G_{\mathrm{guardian}}(x)\, G_{\mathrm{constitutional}}(x)\, G_{\mathrm{provenance}}(x)\, G_{\mathrm{coherence}}(x)\, G_{\mathrm{privacy}}(x)\, G_{\mathrm{security}}(x)
\]

Here \(G_{\mathrm{coherence}}(x)\) is the coherence gate for candidate state \(x\). It represents the measured semantic coherence of that candidate as evaluated in relation to H_App and the live hilbert-state service coherence keys.

Placing coherence explicitly inside the gate structure clarifies its status. Coherence is not decorative, and it is not sovereign over the other conditions. It is one of the operational requirements for promotion. A candidate that fails the coherence gate may still contain useful material, but it is not yet in the right condition to cross an authority boundary without additional revision or review.

This also helps preserve the proper distinction between semantic fit and truth. The gate does not ask whether coherence proves correctness. It asks whether the candidate's measured internal structure is sufficiently sound to proceed alongside the other required checks.

---

## 44.8 Coherence Is Not Truth

One of the most important safeguards in this chapter is conceptual clarity about what Phi can and cannot say.

Phi measures semantic coherence. It does not certify external reality. A candidate may be highly coherent because its components mutually reinforce one another inside H_App, yet still rest on mistaken premises, bad data, or incomplete evidence. Conversely, a candidate may initially reduce coherence because it introduces a disruptive but accurate correction that the system has not yet absorbed.

For that reason, coherence must always remain paired with other forms of review. Truth filtering, guardian review, provenance retention, privacy checks, constitutional constraints, and security conditions all remain necessary. Phi strengthens governance by adding a measured account of semantic fit, but governance becomes unsafe if coherence is confused with truth itself.

This chapter therefore places Phi in the correct epistemic role: powerful, informative, operationally meaningful, but not self-sufficient.

---

## 44.9 Operational Meaning

The Phi probe gives Ms. Allis a live way to measure whether a state is internally holding together before that state is trusted with greater authority.

Because the probe is tied to hilbert-state service coherence keys, its findings are not isolated diagnostics. They belong to the same operational environment that produces active semantic state in the first place. Because Phi can be used during sandbox validation, it helps discipline provisional reasoning before it reaches promotion. Because it participates as \(G_{\mathrm{coherence}}(x)\) within the gate structure, it helps ensure that promotion decisions account for semantic integrity across active domains.

The result is a governance-relevant coherence instrument embedded in the live architecture of H_App.

---

## 44.10 The Three Modes and What They Mean in This System

Before recording the implementation status, it is worth stating precisely what the probe's three modes mean in the context of Ms. Allis — because the probe was calibrated against *this* system's natural resting state, not against an abstract theoretical norm.

Ms. Allis reasons simultaneously across seven maximally diverse semantic domains: worldview, Appalachian culture, civic infrastructure, governance and law, psychology and learning, self-identity, and spiritual grounding. These domains are deliberately chosen to be as different from each other as possible. The empirically observed baseline cross-domain cosine similarity across them is approximately 0.15. The three modes are defined relative to that baseline:

**Superposition (0.08–0.35)** is the healthy normal state. The seven domains are doing their jobs independently — each contributing its own semantic perspective without collapsing into each other. The system holds multiple distinct frames of reference simultaneously. This is not fragmentation; it is the designed condition of a system meant to reason across culture, geography, governance, identity, and spirit at once. The name is deliberate: like quantum superposition, it means multiple states coexisting without forcing premature resolution.

**Coherent (above 0.35)** means the sampled domains are reading as unusually unified — their centroids pull toward each other beyond the expected baseline. For a purposely unified corpus, such as geographic beliefs all rendered with the same template and the same embedder, a coherent reading is expected and positive. For the full seven-domain system, a coherent reading would warrant inspection: unusual unity can mean genuine integration, or it can mean the echo saturation problem Section 44.11 documents.

**Decoherent (below 0.08)** means the domains have fragmented below the minimum expected cross-domain similarity — a signal that something has gone wrong with the measurement substrate itself.

Understanding these modes is essential to interpreting the reading in Section 44.10 correctly. A coherent score on the GEO_BELIEF domain is a good finding. The same score on the full seven-domain system would be a warning.

---

## 44.11 Implementation Status (July 2026)

In the demonstrated/not-yet-demonstrated discipline of Chapter 52:

**Demonstrated — the measurement substrate and the first real reading:**

- The hilbert-state service is live. State writeback POSTs to the hilbert-state embed endpoint on every chat job, producing a 384-dimensional vector stored in Redis under per-job coherence keys of the form `hilbert:state:chat:<jobid>`. Cold-start embedding runs near 37 seconds; warm embedding completes in under 100 milliseconds. This is the keyed structure Section 44.2 describes, and it exists in production.
- The embedding-space discipline the probe depends on is enforced by hard experience: all coherence-bearing collections use the all-minilm 384-dimensional model, and the incompatible 768-dimensional alternative was ruled out after a live dimension-mismatch incident earlier in the build. Coherence comparison is only meaningful inside a single embedding space, so this constraint is a precondition of every claim in this chapter.
- The probe runs as a live service (`jarvis-phi-probe`, port 8026) with `/phi`, `/phi/cached`, and `/health` endpoints, auto-resampling every five minutes and writing state to Redis under `pituitary:phi_state`. A `GEO_BELIEF` domain was added to its cluster map covering `gbimwvcountiesv2`, `gbimwvtractsv2`, and `gbimwvblockgroupsv1` in both `PROBE_COLLECTIONS` and `QUERY_COLLECTIONS`.
- **The first real coherence reading was produced on July 15, 2026** against all three governed WV geographic grains. With counties (55 vectors), tracts (200 vectors), and block groups (200 vectors) sampled at dim=384, the probe returned:
  - `mode: coherent`
  - `coherence_raw: 0.414911`
  - `coherence_normalized: 0.364034`
  - `collections_sampled: [gbimwvcountiesv2, gbimwvtractsv2, gbimwvblockgroupsv1]`

  A score of 0.415 is above the `PHI_COHERENT` threshold of 0.35. The result is substantive: the county, tract, and block group governed beliefs are semantically integrated across all three grains in the all-minilm embedding space. The score drop from an earlier two-grain reading of 0.828 (counties and tracts only) to 0.415 when block groups are added is expected and meaningful — block group beliefs are more locally specific than county beliefs, so adding a finer grain pulls cross-grain cosine similarity down. That is the data telling the truth about the corpus: finer granularity introduces more local semantic variation, which is a property of the data, not a defect. A corpus where block groups read identically to counties would be suspicious. The three-grain reading is the definitive baseline for the GEO_BELIEF domain.
- The per-user memory decomposition of Chapter 50 is already wired into the probe's domain map: the self-identity domain resolves through `conversation_history_user_<slug>` at request time rather than reading a shared conversation collection. Cross-user echoes are structurally excluded from the self-identity reading before any coherence measurement begins.

**Not yet demonstrated:**

- \(G_{\mathrm{coherence}}\) is not wired as an enforced gate. No sandbox validation or manifest promotion currently blocks, narrows, or escalates on a Phi finding. The coherence gate exists in the algebra and the service produces readings; the wiring between them does not yet exist.
- Coherence thresholds for the governed geographic domain are not calibrated against outcomes. The probe produced a reading and the score is interpretable against the probe's built-in thresholds, but there is no validated mapping from geographic coherence scores to the reject / revise / review / approve outcomes Section 44.6 describes. The July 15 reading is a baseline, not a calibration.
- Cross-domain coherence between the GEO_BELIEF cluster and non-geographic domains (identity, governance, spiritual) has not been measured. The July 15 reading covers three grains of one cluster; the broader seven-cluster coherence the probe was designed to measure requires the other primary collections to reach the `MIN_COHERENCE_VECTORS` threshold of 10.

---

## 44.12 Worked Lesson: When the Measured State Degenerates

One production incident belongs in this chapter because it demonstrates the failure mode this probe is most vulnerable to — not a wrong measurement, but a faithful measurement of a degenerate state.

During the June 2026 autonomous-learner audit, the Hilbert state in Redis was found to be roughly 98 percent conversation echoes: near-duplicate restatements of recent exchanges, written back cycle after cycle, crowding out genuinely new semantic material. A coherence probe reading that state would have reported high coherence — and the reading would have been technically correct, because a state composed of echoes of itself is maximally self-consistent. It would also have been governance-useless, because the coherence was an artifact of redundancy, not of integration.

The remediation was structural rather than interpretive: near-duplicate detection at a 0.92 cosine-similarity threshold was added to the write path, collapsing the echo fan-out and restoring genuine diversity to the measured state. The lesson generalizes and belongs in the chapter's permanent record:

1. **A coherence instrument inherits the quality of its substrate.** Phi measures fit within the represented state; if the representation process is degenerate, high coherence is a symptom, not a virtue.
2. **Write-path hygiene is part of the measurement architecture.** Deduplication, provenance discipline, and the governed intake of Chapter 52 are not adjacent concerns — they are what make a Phi reading interpretable.
3. **Suspiciously stable coherence is itself a diagnostic signal.** A state whose coherence never moves should prompt inspection of the write path before celebration of the score. The 26-hour topic pin that accompanied the echo saturation was exactly such a signal, visible in retrospect.

This incident is the coherence-domain instance of the pattern Chapters 42 and 45 record in their own domains: discovering that an instrument was reading a silently corrupted substrate is an epistemic event, and recording it is part of the instrument's provenance.

---

## 44.13 Closing Statement

The Phi probe measures semantic coherence in H_App by reading and evaluating the live coherence conditions exposed through hilbert-state service coherence keys. Its findings may be used during sandbox validation and may also contribute to promotion decisions as the coherence component of the broader gate structure.

Multidomain coherence is treated in this chapter as a measured property of internal semantic fit across coupled domains. It is not automatic truth. Phi therefore serves as a live architectural instrument for evaluating whether a candidate state is sufficiently coherent to continue through governed reasoning and authority-preserving promotion.

As of this writing, the substrate is live and disciplined, the probe service is running and auto-resampling every five minutes, and the first coherence reading has been taken across all three governed geographic grains: `coherence_raw 0.415`, mode coherent. The gate remains unwired and cross-domain calibration remains future work — but the chapter can no longer say the probe has never been exercised. It has been, and the governed geographic corpus passed at the coherent threshold. The score itself is interpretable: not so high as to suggest echo saturation, not so low as to suggest fragmentation, but unified enough to confirm that counties, tracts, and block groups form a semantically coherent body of governed belief across three levels of geographic granularity. That is what this system was built to say about West Virginia, and now it has said it with a number.
