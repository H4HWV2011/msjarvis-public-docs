<!-- AS-BUILT REWRITE: 2026-07-22T13:34:06.890157+00:00 -->
<!-- Gate status: CLOSED_FOR_REWRITE → REWRITTEN -->
<!-- Gate report loaded: False -->
<!-- Injected facts: -->
<!--   Chroma Appalachian linguistic corpus from AAPCAppE:8033 is live GBIM input -->
<!--   GBIM promotion contract: trigger=gbim_active_collection BEFORE, evaluator=coherence_ok, procedure=promote_gbim_collection -->
<!--   scripts/refresh_gbim_spatial.sh runs daily 02:00; gbim_decay_tick.sh runs daily 02:00 -->
<!--   ms-allis-internal-sandbox:8042 bbb_enforced=true v1.2.0 confirmed live -->

# 2. The Geometric Belief Model and GBIM Architecture


> **As-Built Evidence Block — July 22, 2026**
>
> - Chroma Appalachian linguistic corpus from AAPCAppE:8033 is live GBIM input
> - GBIM promotion contract: trigger=gbim_active_collection BEFORE, evaluator=coherence_ok, procedure=promote_gbim_collection
> - scripts/refresh_gbim_spatial.sh runs daily 02:00; gbim_decay_tick.sh runs daily 02:00
> - ms-allis-internal-sandbox:8042 bbb_enforced=true v1.2.0 confirmed live
>

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 9, 2026*

---

## Why This Matters for Polymathmatic Geography

This chapter provides the theoretical and operational foundation for understanding how Ms. Allis represents knowledge, belief, authority, uncertainty, and governed action in place. It supports:

- **P1 – Every where is entangled** by establishing that belief is not stored as isolated facts but as multi-axis geometric structures in which spatial, temporal, institutional, normative, and governed dimensions are co-present and mutually constraining, so that a single GBIM belief about a hospital in Fayette County is simultaneously a claim about what exists, where it is, when it was verified, who has authority over it, how it may be disclosed, and whether it is permitted to affect routing, memory, or action.

- **P3 – Power has a geometry** by showing that the GBIM axis structure — particularly `who`, `where`, `under_whose_authority`, and `for_whom` — is designed to make institutional power over place explicit and queryable, not buried in unstructured text. That principle now extends beyond representation into governed promotion: a belief may describe power, but it does not become operationally authoritative until it passes truth, constitutional, privacy, and system-safety gates.

- **P5 – Design is a geographic act** by treating the nine-axis GBIM schema, the worldview structure, the collection inventory, the ChromaDB configuration, and the promotion architecture not as neutral technical choices but as geographic and political decisions that determine which facts are computable, which relationships are traversable, which identity-bearing structures remain protected, and which forms of institutional accountability are operationally enforceable.

- **P12 – Intelligence with a ZIP code** by grounding the Hilbert-space model and governed-state model in concrete West Virginia infrastructure: PostgreSQL corpora, Chroma-backed retrieval, GBIM views, routing services, sandboxed reasoning, and promotion gates that remain answerable to real places, programs, and populations.

- **P16 – Power accountable to place** by designing the belief structure so that institutional actors — government agencies, corporate landowners, utility companies, and formal authorities — are represented as first-class GBIM entities with explicit `under_whose_authority` and `who` axis entries, while residential individuals remain deliberately protected from exposure as public accountability targets.

The theoretical framework in this chapter is not a preamble to the system. It is the system’s operating logic, expressed at the level of schema, routing, collection design, governed transitions, and controlled disclosure rather than only at the level of code.

Accordingly, this chapter belongs to the **Theoretical Foundation** tier. It establishes the geometric belief model, the nine-axis GBIM schema, the Hilbert-space representation of uncertainty, the worldview structure, the ChromaDB collection inventory, the promotion architecture, and the governed-state formalization that together constitute the epistemic architecture of Ms. Egeria Allis.

---

## 2.1 Purpose and Scope

This chapter establishes the theoretical and operational framework underlying the **GeoBelief Information Model (GBIM)** — the core representational system that allows Ms. Egeria Allis to hold, update, route, govern, and reason over structured beliefs about West Virginia’s physical world, institutional landscape, and programmatic infrastructure.

GBIM is not a database schema in the conventional sense. It is a multi-axis geometric representation of belief that treats each claim about the world as a structured object with distinct dimensions encoding meaning, provenance, authority, temporal status, disclosure bounds, and applicability. This structure is what allows beliefs derived from a WV assessor parcel record, a federal hazard dataset, a community organization’s program flyer, and a peer-reviewed paper on Appalachian poverty to coexist in one corpus and still be meaningfully compared, combined, routed, governed, and, when appropriate, promoted.

GBIM must now be understood as a **governed representational layer**, not merely a semantic or spatial one. A retrieved statement, a sandbox inference, a corroborated conclusion, an approved memory object, and an actionable civic state are not the same object simply because they share textual or vector similarity. Promotion changes status, not merely storage location.

The chapter is organized as follows:

- **Section 2.2** introduces the nine-axis belief schema and explains the role of each axis.
- **Section 2.3** presents the Hilbert-space and governed-state model of belief and uncertainty that motivates the GBIM design.
- **Section 2.4** describes the worldview structure (`eq1` and related worldviews) and its role in routing, filtering, and authority context.
- **Section 2.5** describes the PostgreSQL GBIM corpus — its current scale, table structure, and production status.
- **Section 2.6** presents the ChromaDB collection inventory — the vector-backed memory layer that makes GBIM beliefs semantically retrievable.
- **Section 2.7** addresses the relationship between GBIM, the GeoDB spatial body (Chapter 6), the RAG pipeline (Chapter 7), the internal-state sandbox, and the local resource registry.
- **Section 2.8** documents the pituitary governance layer and its modulation role.
- **Section 2.9** documents the GBIM confidence decay pipeline and time-sensitive freshness signaling.
- **Section 2.10** records the promotion of `rag_grounded_v2` and the broader truth-judging architecture.
- **Section 2.11** documents the ethical architecture of the belief corpus, especially institutional accountability and non-surveillance constraints for individuals.
- **Section 2.12** presents the `allis-gbim-query-router` service.
- **Section 2.13** documents the `mvw_gbim_landowner_spatial` materialized view.
- **Section 2.14** introduces dual sandbox domains and the governed GBIM promotion path.
- **Section 2.15** connects GBIM to Hilbert People Space, identity-focused retention, and the Community Hilbert Commons.

---

## 2.2 The Nine-Axis Belief Schema

Every belief in the GBIM corpus is a structured object with nine named axes stored as JSONB in `gbim_worldview_entities` and related belief tables.

```text
┌─────────────────────────────────────────────────────────────┐
│              GBIM Nine-Axis Belief Structure                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. what_axis          — What entity or claim is asserted   │
│  2. who_axis           — Who or what is the subject/actor   │
│  3. where_axis         — Where (geometry, county, ZIP)      │
│  4. when_axis          — Temporal scope of the belief       │
│  5. why_axis           — Rationale or normative grounding   │
│  6. how_axis           — Method or process of verification  │
│  7. for_whom_axis      — Intended beneficiary population    │
│  8. under_whose_authority_axis — Institutional authority    │
│  9. on_what_evidence_axis  — Source and provenance          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Every axis contributes to meaning, but no axis by itself is sufficient to make a belief operationally authoritative. The same propositional content can appear in more than one governed state depending on its provenance, authority, disclosure level, confidence, or gate outcome.

**`what_axis`** — The propositional content of the belief: what entity exists, what relationship holds, what condition obtains.

**`who_axis`** — The subject or actor of the belief. In institutional contexts this includes government, corporate, nonprofit, and utility actors. In residential contexts this axis is privacy-constrained by design.

**`where_axis`** — The spatial grounding: geometry, coordinate system, county, ZIP code, parcel relation, or other location-bearing structure.

**`when_axis`** — Temporal scope: when the belief was created, verified, observed, or scheduled for decay and re-verification.

**`why_axis`** — The normative or causal rationale: why the belief matters to Ms. Allis’s mission and how it bears on civic reasoning.

**`how_axis`** — The verification method: the workflow, service, spatial transformation, or institutional path through which the belief was produced.

**`for_whom_axis`** — The intended beneficiary population or population-of-concern.

**`under_whose_authority_axis`** — The institutional, legal, civic, or documentary authority under which the claim is asserted or held.

**`on_what_evidence_axis`** — The primary source and provenance chain.

This nine-axis schema remains foundational, but it must now be paired with a governed-state formalism so that belief structure is not mistaken for operational authorization.

---

## 2.3 Governed State and Hilbert-Space Representation

The GBIM nine-axis schema is motivated by a geometric model of belief, but Ms. Allis no longer treats semantic or geometric content as self-authorizing.

A GBIM state should therefore be represented as:

\[
x = (v, \alpha, p, c, \tau, \ell, g)
\]

where:

- \(v\) is the semantic, spatial, temporal, relational, or composite content representation;
- \(\alpha\) is authority or epistemic status;
- \(p\) is provenance;
- \(c\) is confidence or evidentiary support;
- \(\tau\) is temporal status;
- \(\ell\) is disclosure or access level;
- \(g\) is governance and gate state.

This means:

\[
(v, \alpha_1, p, c, \tau, \ell, g)
\neq
(v, \alpha_2, p, c, \tau, \ell, g)
\]

whenever:

\[
\alpha_1 \neq \alpha_2
\]

Thus a sandbox hypothesis, corroborated conclusion, approved memory, and actionable civic state may all carry similar content while remaining fundamentally different governed states.

The Hilbert-space interpretation still matters. The system’s broader epistemic state may be understood as a vector over a high-dimensional space of possible world-claims, with retrieval and routing functioning as projections into relevant subspaces. But the projected vector is not enough. A GBIM belief becomes operationally meaningful only when it is accompanied by authority, provenance, temporal, disclosure, and governance metadata.

```text
┌─────────────────────────────────────────────────────────────┐
│   Hilbert-Space and Governed-State View of GBIM            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Full belief space H                                        │
│      ↓ projection                                           │
│  Query-relevant subspace H_q                                │
│      ↓ role / place / worldview filtering                   │
│  Operational subspace H_q,r,c,w                             │
│      ↓ governed-state evaluation                            │
│  x = (v, α, p, c, τ, ℓ, g)                                  │
│      ↓ gate / promotion                                     │
│  validated memory or actionable state                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

The correct revision principle is therefore: **GBIM is geometric, but it is also governed**.

---

## 2.4 Worldview Structure and the `eq1` Worldview

The production worldview is **`eq1`** — the primary equity-oriented worldview grounding Ms. Allis’s reasoning in Appalachian community perspectives, WV state data, and federal program structures.

The worldview remains a filtering and interpretive frame, but it should not be described as the final authority source by itself. A worldview organizes relevance, weighting, and interpretive commitments; it does not replace provenance, legal authority, constitutional validity, privacy constraints, or gate review.

In the revised architecture, worldview participates in the authority context of a belief without exhausting it. A belief may be worldview-compatible yet still fail promotion because it lacks adequate evidence, violates disclosure rules, conflicts with constitutional constraints, or remains temporally stale.

---

## 2.5 The PostgreSQL GBIM Corpus

The PostgreSQL GBIM corpus remains the authoritative relational substrate for structured beliefs, landowner views, civic entities, and graph-adjacent state.

However, this chapter must now distinguish between:

1. **authoritative production stores**, including GBIM tables, materialized views, and spatially grounded relational records; and
2. **provisional reasoning state**, which may inspect or reason over GBIM but may not directly alter it without passing promotion gates.

This distinction is critical because GBIM is no longer documented as a simple endpoint of retrieval and routing. It is the durable, governed layer that receives only approved transitions.

---

## 2.6 ChromaDB Collections and Semantic Retrieval

The Chroma-backed layer remains the semantically retrievable memory substrate for GBIM beliefs and worldview entities.

But retrieval should no longer be documented as if semantic proximity itself authorizes state change. Semantic retrieval produces candidate context, candidate evidence, and candidate neighborhood structure. It does not directly produce approved GBIM truth.

The revised chapter should make explicit that retrieval may contribute to:

- sandbox hypotheses;
- corroboration;
- confidence adjustment;
- worldview-scoped projection;
- provenance enrichment;

but not direct graph consequence absent governance.

---

## 2.7 GBIM, GeoDB, RAG, and the Internal-State Sandbox

GBIM now sits in a broader governed pipeline.

GeoDB provides the spatial body. RAG provides retrieval context. Chroma provides semantic access. The GBIM query router provides structured relational retrieval. But the emerging internal-state reasoning architecture adds a new distinction: reasoning about GBIM is not equivalent to committing GBIM.

A belief or inferred relation may be retrieved from GBIM, combined with spatial context, compared with other records, and reasoned over inside the internal-state sandbox without thereby changing GBIM itself.

This is a crucial revision. The system now has two sandbox domains:

- the **DGM code sandbox**, which governs code, configuration, and system-change promotion;
- the **internal-state reasoning sandbox**, which governs provisional internal reasoning about identity, geography, civic interpretation, and candidate conclusions before those conclusions can affect durable memory, graph structure, or action.

GBIM belongs downstream of governed promotion, not upstream of unconstrained inference.

---

## 2.8 Pituitary Governance and Affective Modulation

The pituitary layer remains a neural-behavioral governance module that modulates urgency, warmth, escalation, and ethical restraint.

Its role should now be described in relation to the sandboxed reasoning flow. Pituitary modulation does not merely shape final responses; it also conditions internal reasoning context, affective caution, and escalation behavior before candidate conclusions move toward promotion review.

This becomes especially important for GBIM when civic, identity-bearing, or place-sensitive claims are under consideration. A belief may be semantically coherent yet still require cautious modulation, human review, or nonpromotion.

---

## 2.9 Confidence Decay, Temporality, and Hysteresis

GBIM beliefs are temporally situated and subject to decay, re-verification, and freshness signaling.

The revised chapter should not describe confidence as a static scalar attached once and for all. A better formalism is evidence-bounded and temporally governed.

Let \(C(x)\) denote system confidence and \(E(x)\) the maximum confidence justified by available evidence. Then a core safety condition is:

\[
C(T_{\mathrm{promote}}(x)) \leq E(x)
\]

This prevents a provisional inference from becoming an asserted fact merely because it crossed a system boundary.

Where stability matters, belief revision should include hysteresis. Let entry and exit thresholds satisfy:

\[
\theta_{\mathrm{exit}} < \theta_{\mathrm{enter}}
\]

and let accepted-state behavior be governed by:

\[
b_{t+1}(x) =
\begin{cases}
1, & C_t(x) \geq \theta_{\mathrm{enter}}, \\
0, & C_t(x) \leq \theta_{\mathrm{exit}}, \\
b_t(x), & \theta_{\mathrm{exit}} < C_t(x) < \theta_{\mathrm{enter}}
\end{cases}
\]

This prevents GBIM from oscillating rapidly between accepted and rejected status because of minor fluctuations near a single threshold. For civic, spatial, or identity-linked beliefs, that stability is essential.

---

## 2.10 Truth Judging, DGM Corroboration, and Non-Direct Promotion

The retirement of weaker contradiction heuristics and the promotion of `rag_grounded_v2` as canonical truth judge should now be documented as part of a broader gate architecture, not as a standalone validation note.

A belief does not become GBIM-valid merely because it was retrieved or generated. It must move through truth-oriented corroboration and then pass constitutional, privacy, security, domain, and disclosure controls.

A useful formalization is:

\[
S_{\mathrm{raw}}
\rightarrow
S_{\mathrm{sandbox}}
\rightarrow
S_{\mathrm{validated}}
\rightarrow
S_{\mathrm{memory}}
\rightarrow
S_{\mathrm{action}}
\]

with:

\[
T_{\mathrm{promote}} : S_{\mathrm{sandbox}} \rightharpoonup S_{\mathrm{validated}}
\]

and:

\[
T_{\mathrm{promote}}(x) =
\begin{cases}
P(x), & G(x)=1, \\
\bot, & G(x)=0
\end{cases}
\]

This makes explicit that truth judging is necessary but not sufficient. GBIM promotion is gated, partial, and fail-closed.

---

## 2.11 Ethical Architecture, Non-Surveillance, and Institutional Accountability

The exclusion of individual residential owner names remains an ethical and structural design principle. That principle now sits inside a more explicit sovereignty framework.

GBIM is not a surveillance graph. It is a governed civic knowledge model in which institutional actors may be represented as first-class accountability-bearing entities, while residential individuals remain protected by disclosure limits, role gates, and non-surveillance commitments.

This can be formalized through disclosure projections such as:

\[
\Pi_1, \Pi_2, \Pi_3
\]

with the principle:

\[
\Pi_2(x) \not\Rightarrow \Pi_3(x)
\]

Permission to reveal one level of identity-bearing structure does not automatically authorize a more revealing projection.

Thus, GBIM must never be documented as a direct public identity surface. It is a sovereignty-aware structure in which visibility depends on role, consent, purpose, time, lawful authority, and constitutional legitimacy.

---

## 2.12 The `allis-gbim-query-router` Service

The `allis-gbim-query-router` remains a PostgreSQL-native retrieval path for GBIM.

Its revised role is to provide authoritative structured access, not direct commitment semantics. It returns relationally grounded candidate structures that may then be interpreted, combined, or evaluated in governed reasoning paths.

This is an important distinction: retrieval is not action, and access is not promotion.

---

## 2.13 The `mvw_gbim_landowner_spatial` Materialized View

The landowner spatial view remains a concrete realization of parcel-scale institutional accountability.

The revised chapter should emphasize that this materialized view is one of the strongest examples of place-bound power made queryable without collapsing into generalized surveillance. It demonstrates that institutional ownership and land control can be represented as auditable civic structure while still preserving limits on private individual exposure.

It should also be described as a source of evidence and structured grounding for GBIM reasoning rather than as an automatically action-bearing truth surface.

---

## 2.14 Governed Promotion Path for GBIM

This section is a required update.

GBIM is no longer accurately described by an implicit direct-routing model. Reasoning about identity, space, or civic state must pass through explicit governed transitions before altering GBIM or related graph structures.

The operative update path is:

1. retrieval, routing, or model inference produces candidate content;
2. candidate content enters the internal-state reasoning sandbox;
3. truth and corroboration judges evaluate the candidate state;
4. constitutional and blood-brain-barrier review evaluate legality, disclosure, alignment, and risk;
5. DGM-governed approval determines whether promotion is permitted;
6. only promoted conclusions may affect GBIM, identity graphs, durable memory, or actionable civic state.

The gate can be decomposed as:

\[
G(x) =
G_{\mathrm{constitutional}}(x)
\land
G_{\mathrm{provenance}}(x)
\land
G_{\mathrm{coherence}}(x)
\land
G_{\mathrm{privacy}}(x)
\land
G_{\mathrm{security}}(x)
\land
G_{\mathrm{domain}}(x)
\]

This means a GBIM-relevant state may fail promotion for many reasons beyond semantic plausibility alone.

A central rule of this chapter is therefore:

**GBIM state is not changed by raw LLM output. Only promoted conclusions may affect graph or identity structures.**

Promotion also changes status, not merely location:

\[
T_{\mathrm{promote}}(x) \neq x
\]

Even where the semantic content remains unchanged, authority, provenance, disclosure, temporal status, and governance state may all change.

---

## 2.15 GBIM, Hilbert People Space, and the Community Hilbert Commons

GBIM must be placed inside the broader sovereignty architecture of Ms. Allis.

GBIM interacts with **Hilbert People Space** because identity-bearing and relation-bearing structure does not exist in a single flattened graph. A useful formalization is:

\[
H_{\mathrm{people}} = \bigoplus_{u \in U} H_u
\]

where each \(H_u\) is a sovereign user subspace.

This means GBIM should not be interpreted as a universal surveillance layer over all persons. Instead, it interacts with sovereign subspaces whose internal structure may only be projected or shared under governed conditions.

For approved commons aggregation, a suitable formalization is:

\[
H_{\mathrm{commons}} =
\mathcal A
\left(
\left\{
\Pi_{\mathrm{approved},u}(H_u)
\right\}_{u \in U}
\right)
\]

Thus, community-scale civic intelligence should aggregate over approved projections of sovereign subspaces rather than raw personal traces.

This is the correct location of GBIM within the broader thesis:

- linked to **identity-focused retention**, because durable identity-bearing memory is gated;
- linked to **Hilbert People Space**, because person-linked structure remains sovereign and non-surveillant;
- linked to **Community Hilbert Commons**, because civic-scale intelligence arises from approved aggregation rather than direct extraction.

---

## 2.16 Qualia Tension and Commitment Operators in GBIM

Some GBIM-relevant states remain semantically plausible but unresolved. They may be coherent in one sense while conflicted in another: legally restricted, evidentially incomplete, temporally stale, or ethically unsafe.

A useful control signal for this condition is:

\[
q_{\mathrm{tension}} = \sigma(D_{\mathrm{MA}}(x))
\]

where \(D_{\mathrm{MA}}(x)\) represents a discrepancy between meaning and analysis, and \(\sigma\) maps that discrepancy into a control signal.

In this chapter, that signal should be treated as a functional indicator that a GBIM interpretation remains unresolved, conflicted, or in need of further corroboration. It is not a claim about human subjective feeling.

GBIM must also distinguish between internal deliberation and committed consequence. A useful operator is:

\[
K : S_{\mathrm{deliberative}} \rightharpoonup S_{\mathrm{committed}}
\]

This marks the difference between internally entertained structure and externally consequential graph state. A place-linked, identity-bearing, or civic interpretation does not become committed GBIM reality merely because it was generated. It becomes graph-consequential only after governed transition.

---

## 2.17 Revision Principle

The governing revision principle for GBIM is straightforward:

- GBIM is not a direct write target for raw model output.
- GBIM states are governed states rather than bare semantic vectors.
- Promotion changes authority, provenance, disclosure, temporal, and operational status, not merely storage location.
- Identity-bearing and geospatially anchored knowledge must remain bounded by constitutional, jurisdictional, evidentiary, and sovereignty constraints.
- GBIM belongs inside a broader architecture that includes dual sandbox domains, identity-focused retention, Hilbert People Space, and the Community Hilbert Commons.

Under this revised framing, GBIM becomes a governed civic identity-and-geography layer within Ms. Allis rather than a passive semantic graph or an implicitly self-authorizing routing destination.
