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
> - scripts/refresh_gbim_spatial.sh run daily at 02:00; gbim_decay_tick.sh runs daily at 02:00  
> - ms-allis-internal-sandbox:8042 bbb_enforced=true v1.2.0 confirmed live  
>
> *Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
> *Last updated: July 22, 2026*

***

## 2.1 Purpose, Scope, and Audience

This chapter establishes the theoretical and operational framework underlying the **GeoBelief Information Model (GBIM)** — the core representational system that allows Ms. Egeria Allis to hold, update, route, govern, and reason over structured beliefs about West Virginia’s physical world, institutional landscape, and programmatic infrastructure.

For university readers (WVU, Marshall), GBIM should be understood as a formal, geometric, and governed belief architecture. It combines multi‑axis semantic and spatial representation with explicit authority, provenance, temporal, disclosure, and governance metadata. For rural leaders and practitioners, GBIM should be understood as a pattern for building a place‑accountable, non‑surveillant civic knowledge layer on top of existing local data: parcels, programs, hazards, clinics, utilities, and community organizations.

GBIM is not a conventional database schema. It is a multi‑axis geometric representation of belief that treats each claim about the world as a structured object in which meaning and power are co‑present. This structure allows beliefs derived from a county assessor parcel record, a federal hazard dataset, a community organization’s flyer, and a peer‑reviewed paper on Appalachian poverty to coexist in one corpus and still be meaningfully compared, combined, routed, governed, and, when appropriate, promoted.

Under the as‑built system, GBIM must be understood as a **governed representational layer**, not merely a semantic or spatial one. A retrieved statement, a sandbox inference, a corroborated conclusion, an approved memory object, and an actionable civic state are not the same object simply because they share textual or vector similarity. Promotion changes status — authority, provenance, disclosure and consequence class — not merely storage location.

This chapter belongs to the **Theoretical Foundation** tier. It establishes:

- the geometric belief model;
- the nine‑axis GBIM schema;
- the Hilbert‑space and governed‑state representation of uncertainty;
- the worldview structure;
- the ChromaDB collection inventory;
- the promotion and decay architecture; and
- the governed‑state formalization that together constitute the epistemic architecture of Ms. Egeria Allis.

The chapter is organized as follows:

- **Section 2.2** introduces the nine‑axis belief schema and explains the role of each axis.  
- **Section 2.3** presents the Hilbert‑space and governed‑state model of belief and uncertainty that motivates the GBIM design.  
- **Section 2.4** describes the worldview structure (`eq1` and related worldviews) and its role in routing, filtering, and authority context.  
- **Section 2.5** describes the PostgreSQL GBIM corpus — its current role, table structure, and production status.  
- **Section 2.6** presents the ChromaDB collection inventory — the vector‑backed memory layer that makes GBIM beliefs semantically retrievable.  
- **Section 2.7** addresses the relationship between GBIM, the GeoDB spatial body, the RAG pipeline, the internal‑state sandbox, and the local resource registry.  
- **Section 2.8** documents the pituitary governance layer and its modulation role.  
- **Section 2.9** documents the GBIM confidence decay pipeline and time‑sensitive freshness signaling.  
- **Section 2.10** records the promotion path for truth‑judged states, including `rag_grounded_v2` and the broader gate architecture.  
- **Section 2.11** documents the ethical architecture of the belief corpus, especially institutional accountability and non‑surveillance constraints for individuals.  
- **Section 2.12** presents the `allis-gbim-query-router` service.  
- **Section 2.13** documents the `mvw_gbim_landowner_spatial` materialized view.  
- **Section 2.14** introduces dual sandbox domains and the governed GBIM promotion path.  
- **Section 2.15** connects GBIM to Hilbert People Space, identity‑focused retention, and the Community Hilbert Commons.  
- **Section 2.16** introduces qualia tension and commitment operators as internal control signals.  
- **Section 2.17** states the governing revision principle and offers a concrete implementation roadmap for rural deployments.

With this structure, the chapter is written so that a reader — including a rural community member with local GIS and data capacity — can use it as a template: by substituting their own spatial corpus, institutional actors, and governance rules, they can construct a locally accountable GBIM‑like system.

***

## 2.2 The Nine‑Axis Belief Schema

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

Each axis contributes to meaning, but no axis by itself is sufficient to make a belief operationally authoritative. The same propositional content can appear in more than one governed state depending on provenance, authority, disclosure, confidence, or gate outcome.

- **`what_axis`** — The propositional content: what entity exists, what relationship holds, what condition obtains (e.g., “Food pantry open on Tuesdays,” “Parcel lies in 100‑year floodplain”).  
- **`who_axis`** — The subject or actor. In institutional contexts this axis includes agencies, corporate actors, nonprofits, and utilities. In residential contexts this axis is privacy‑constrained; individuals appear only when explicitly required and under strict disclosure rules.  
- **`where_axis`** — The spatial grounding: geometry, coordinate system, county, ZIP, tract, blockgroup, parcel relation, or other location‑bearing structure. This axis links beliefs directly to the spatial body described elsewhere in the thesis.  
- **`when_axis`** — Temporal scope: when the belief was created, verified, observed, or scheduled for decay and re‑verification. It distinguishes current program status from historical records and supports confidence decay.  
- **`why_axis`** — The normative or causal rationale: why the belief matters to Ms. Allis’s mission and how it bears on civic reasoning (e.g., “Supports food security for low‑income households,” “Required for hazard mitigation planning”).  
- **`how_axis`** — The verification method: the workflow, service, spatial transformation, or institutional path through which the belief was produced. This axis links beliefs to concrete procedures and services.  
- **`for_whom_axis`** — The intended beneficiary population or population‑of‑concern (e.g., “Fayette County residents,” “children under six,” “elderly living alone,” “SNAP‑eligible households”).  
- **`under_whose_authority_axis`** — The institutional, legal, civic, or documentary authority under which the claim is asserted or held (e.g., “County Commission,” “State Department of Health,” “Local nonprofit board,” “Federal statute”).  
- **`on_what_evidence_axis`** — The primary source and provenance chain: underlying documents, datasets, services, and transformations that support the belief.

For a developer in Wisconsin, this schema can be implemented as a JSONB column with checked keys, or as a normalized table family, but the key point is conceptual: every belief is multi‑axis and governance‑aware, not just a text blob with a coordinate.

***

## 2.3 Governed State and Hilbert‑Space Representation

The nine‑axis schema is motivated by a geometric model of belief: the corpus of beliefs is treated as a high‑dimensional state over which projections, filters, and updates can be defined. The current architecture, however, no longer treats semantic or geometric content as self‑authorizing.

A GBIM state is therefore represented as:

\[
x = (v, \alpha, p, c, \tau, \ell, g)
\]

where:

- \(v\) is the semantic, spatial, temporal, relational, or composite content representation (for example, an embedding, a structured record, or a hybrid);  
- \(\alpha\) is authority or epistemic status (e.g., sandbox hypothesis, expert‑validated, legally certified);  
- \(p\) is provenance (source documents, services, transformations);  
- \(c\) is confidence or evidentiary support;  
- \(\tau\) is temporal status (last verification time, expiry, decay state);  
- \(\ell\) is disclosure or access level (who may see or use the claim, at what resolution); and  
- \(g\) is governance and gate state (which gates it has passed, failed, or is awaiting).

Even if the content \(v\) is unchanged, differences in authority make two states distinct:

\[
(v, \alpha_1, p, c, \tau, \ell, g)
\neq
(v, \alpha_2, p, c, \tau, \ell, g)
\quad \text{whenever} \quad
\alpha_1 \neq \alpha_2
\]

In practice, this means that:

- a sandbox hypothesis,  
- a corroborated conclusion,  
- an approved memory object, and  
- an actionable civic state  

may each reference similar content but carry different authority, provenance, disclosure, and governance metadata. Only the last category is allowed to alter civic‑facing behaviour, routing decisions, or durable graphs.

For a professor, this is a Hilbert‑space state paired with a governance vector; for a developer, it is a structured record with explicit control fields that drive promotion and access.

***

## 2.4 Worldview Structure and the `eq1` Worldview

The production worldview **`eq1`** is the primary equity‑oriented worldview grounding Ms. Allis’s reasoning in Appalachian community perspectives, West Virginia state data, and federal program structures. It encodes commitments about relevance, centrality of certain voices, and how trade‑offs are evaluated.

In the revised architecture, worldview plays a **filtering and interpretive role** but is not itself an authority source. A worldview organizes:

- relevance (which beliefs are considered for a given question);  
- weighting (which sources are treated as more trusted); and  
- interpretive commitments (how to understand conflict or uncertainty);

but it does not replace:

- provenance tracking;  
- legal and constitutional constraints;  
- privacy and disclosure rules; or  
- gate‑based governance.

A belief may be compatible with `eq1` yet still fail promotion because it lacks adequate evidence, violates disclosure rules, conflicts with constitutional constraints, or remains temporally stale. For deployments outside West Virginia, this suggests that any local worldview (for example, centred on tribal sovereignty or county‑level equity goals) should be implemented as a filter and weighting layer, not as a substitute for law, ethics, or evidence.

***

## 2.5 The PostgreSQL GBIM Corpus

The PostgreSQL GBIM corpus is the authoritative relational substrate for structured beliefs, landowner views, civic entities, and graph‑adjacent state. One must distinguish between:

1. **authoritative production stores**, including:
   - GBIM tables (such as `gbim_worldview_entities`, `gbim_beliefs`);  
   - materialized views (such as `mvw_gbim_landowner_spatial`); and  
   - spatially grounded relational records; and  

2. **provisional reasoning state**, which:
   - may inspect or reason over GBIM;  
   - may produce candidate updates or interpretations; but  
   - may not directly alter GBIM without passing promotion gates.

GBIM is the durable governed layer that receives only approved transitions. For a developer, this means designing a clear boundary between core tables (authoritative, governed) and working tables or sandboxes (ephemeral, non‑authoritative).

***

## 2.6 ChromaDB Collections and Semantic Retrieval

The Chroma‑backed layer serves as the semantically retrievable memory substrate for GBIM beliefs and worldview entities. In production, this includes:

- GBIM‑backed semantic collections (geographic and institutional beliefs);  
- an Appalachian linguistic corpus from AAPCAppE:8033, which functions as live GBIM input; and  
- additional collections supporting RAG for legal, programmatic, and community texts.

Retrieval from Chroma produces **candidate context**, **candidate evidence**, and **candidate neighbourhood structure**; it does **not** directly produce approved GBIM truth or civic action. Semantic retrieval contributes to:

- sandbox hypotheses;  
- corroboration of existing records;  
- confidence adjustment;  
- worldview‑scoped projection; and  
- provenance enrichment;

but any consequent state change must still pass through the governed promotion pipeline described in Section 2.14.

For a Wisconsin developer, the pattern is: use Chroma or an equivalent vector store to retrieve candidates, but never treat “nearest neighbours” as automatically true or actionable; they feed into gates, not directly into writes.

***

## 2.7 GBIM, GeoDB, RAG, and the Internal‑State Sandbox

GBIM sits within a broader governed pipeline that integrates:

- **GeoDB**, the spatial body (blockgroups, tracts, counties, parcels, hazard zones);  
- **RAG**, the retrieval‑augmented generation pipeline combining text, GBIM, and spatial context;  
- **Chroma**, the semantic memory layer;  
- the **GBIM query router**, which retrieves structured relational state; and  
- the **internal‑state reasoning sandbox**, which is a dedicated environment for provisional reasoning about GBIM and identity‑bearing state.

Reasoning about GBIM is not equivalent to committing GBIM. A belief or inferred relation may be retrieved from GBIM, combined with spatial context, compared with other records, and reasoned over inside the internal‑state sandbox; changes to GBIM tables, identity graphs, or civic‑facing views must be mediated by explicit promotion gates.

This introduces two distinct sandbox domains:

- the **code and configuration sandbox**, which governs system‑change promotion; and  
- the **internal‑state reasoning sandbox**, which governs provisional internal reasoning about identity, geography, and candidate conclusions.

A developer implementing a similar architecture should explicitly separate “read/think” environments from “write/commit” environments and enforce that only gated promotions reach the latter.

***

## 2.8 Pituitary Governance and Affective Modulation

The pituitary layer is modelled as a governance module that modulates urgency, warmth, escalation, and ethical restraint. In Ms. Allis, it:

- shapes responses when sensitive GBIM‑linked topics are involved; and  
- conditions internal reasoning context before candidate conclusions move toward promotion.

Pituitary modulation influences:

- whether the system leans toward caution or assertiveness in borderline cases;  
- whether human review is requested before promotion; and  
- how follow‑up evidence gathering is prioritised.

For GBIM, this is relevant when identity‑bearing or place‑sensitive claims are under consideration, when evidence is limited or authority is ambiguous, or when disclosure or harm potential is high. A developer need not implement a full “pituitary model,” but should encode policies for deferring to human review and avoiding strong claims under uncertainty.

***

## 2.9 Confidence Decay, Temporality, and Hysteresis

GBIM beliefs are temporally situated. They:

- carry timestamps for creation, verification, and last update;  
- are subject to decay and re‑verification; and  
- participate in freshness signalling for downstream services.

Scripts such as `refresh_gbim_spatial.sh` and `gbim_decay_tick.sh` run on schedule (for example, daily at 02:00) to:

- refresh spatial state where new data has arrived;  
- decrease confidence in stale beliefs; and  
- mark beliefs for re‑inspection or deactivation.

Let \(C(x)\) denote system confidence and \(E(x)\) the maximum confidence justified by the available evidence. A safety condition is:

\[
C(T_{\mathrm{promote}}(x)) \leq E(x)
\]

Promotion must not inflate certainty beyond what evidence supports.

Where stability matters, belief revision should include hysteresis. Let thresholds satisfy \(\theta_{\mathrm{exit}} < \theta_{\mathrm{enter}}\), with accepted‑state behaviour:

\[
b_{t+1}(x) =
\begin{cases}
1, & C_t(x) \geq \theta_{\mathrm{enter}}, \\
0, & C_t(x) \leq \theta_{\mathrm{exit}}, \\
b_t(x), & \theta_{\mathrm{exit}} < C_t(x) < \theta_{\mathrm{enter}}
\end{cases}
\]

This prevents oscillation near a single threshold, which is particularly important for hazard classifications and eligibility zones.

***

## 2.10 Truth Judging, Corroboration, and Non‑Direct Promotion

Weaker contradiction heuristics have been retired and `rag_grounded_v2` promoted as the canonical truth judge. This promotion is part of a broader gate architecture and does not authorise direct writes into GBIM.

The promotion path for beliefs can be described as:

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

with a partial operator:

\[
T_{\mathrm{promote}} : S_{\mathrm{sandbox}} \rightharpoonup S_{\mathrm{validated}}
\]

Truth judging is necessary but not sufficient: a candidate state must meet both evidentiary and governance requirements before it can move into durable memory or action. For other implementations, this implies separating “is this likely true?” from “are we allowed to act on this?”.

***

## 2.11 Ethical Architecture, Non‑Surveillance, and Institutional Accountability

The exclusion of individual residential owner names from GBIM’s public identity surfaces is a design principle. GBIM is not a surveillance graph; it is a governed civic knowledge model.

In this model:

- **institutional actors** (agencies, corporations, utilities) are represented as first‑class accountability‑bearing entities; and  
- **residential individuals** are protected by disclosure limits, role‑based access controls, non‑surveillance commitments, and contextual constraints on use.

This can be expressed in terms of disclosure projections \(\Pi_1, \Pi_2, \Pi_3\). A key principle is:

\[
\Pi_2(x) \not\Rightarrow \Pi_3(x)
\]

Permission to reveal one level of identity‑bearing structure does not automatically authorise a more revealing projection. For rural communities, this means designing maps and dashboards that expose institutional and program structures while keeping individual‑level data under stricter controls.

***

## 2.12 The `allis-gbim-query-router` Service

The `allis-gbim-query-router` is a PostgreSQL‑native retrieval path for GBIM. It:

- accepts structured queries (by county, program, hazard, institutional actor);  
- returns relationally grounded structures from GBIM tables and views; and  
- provides a consistent interface for downstream reasoning and RAG pipelines.

It does not perform promotion or gate logic and does not directly change GBIM state. A similar service elsewhere should be designed as a read‑oriented gateway to core tables.

***

## 2.13 The `mvw_gbim_landowner_spatial` Materialized View

The `mvw_gbim_landowner_spatial` materialized view realises parcel‑scale institutional accountability. It integrates:

- parcel geometries;  
- institutional ownership or control;  
- programmatic and legal attributes; and  
- GBIM‑aligned belief metadata.

This view demonstrates that place‑bound power can be made queryable without collapsing into generalised surveillance. For a developer, this suggests designing views that join spatial units with institutional actors and program flags, while omitting sensitive personal identifiers from public outputs.

***

## 2.14 Governed Promotion Path for GBIM

A central update is explicit documentation of GBIM’s governed promotion path. GBIM is not accurately described by a direct‑routing model, where reasoning outputs immediately alter core state.

The operative path is:

1. **Retrieval or inference.** Retrieval, routing, or model inference produces candidate content, possibly combining GBIM records, embeddings, GeoDB geometries, and external text.  
2. **Internal‑state sandbox.** Candidate content enters an internal sandbox, where it is examined and scored without changing GBIM.  
3. **Truth judging and corroboration.** Dedicated judges evaluate semantic coherence, evidential support, and alignment.  
4. **Constitutional and privacy review.** Constitutional principles and blood‑brain‑barrier safeguards evaluate legality, disclosure, and risk.  
5. **Governance approval.** Governance tasks determine whether promotion is permitted; this may include human review or fixed policy checks.  
6. **Promotion and write.** Only promoted conclusions may affect GBIM, identity graphs, durable memory, or actionable civic state.

The gate predicate can be decomposed as:

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

A central rule is:

> **GBIM state is not changed by raw model output. Only promoted conclusions may affect graph or identity structures.**

Promotion changes status, not merely location:

\[
T_{\mathrm{promote}}(x) \neq x
\]

Even where semantic content is preserved, authority, provenance, disclosure, temporal status, and governance state may all change.

***

## 2.15 GBIM, Hilbert People Space, and the Community Hilbert Commons

GBIM is situated within a broader sovereignty architecture. Identity‑bearing and relation‑bearing structures are not collapsed into a single flattened graph.

A person‑linked state can be abstracted as:

\[
H_{\mathrm{people}} = \bigoplus_{u \in U} H_u
\]

where each \(H_u\) is a sovereign user subspace. GBIM interacts with these through governed projections and retention policies.

Commons aggregation can be formalised as:

\[
H_{\mathrm{commons}} =
\mathcal A
\left(
\left\{
\Pi_{\mathrm{approved},u}(H_u)
\right\}_{u \in U}
\right)
\]

with \(\Pi_{\mathrm{approved},u}\) projecting user subspaces into commons‑eligible representations and \(\mathcal A\) aggregating across users.

This pattern supports community‑scale intelligence built from approved projections, not raw personal traces.

***

## 2.16 Qualia Tension and Commitment Operators in GBIM

Some GBIM‑relevant states remain unresolved or conflicted. A control signal for such conditions can be defined as:

\[
q_{\mathrm{tension}} = \sigma(D_{\mathrm{MA}}(x))
\]

where \(D_{\mathrm{MA}}(x)\) represents a discrepancy between **meaning** (narrative or interpretation) and **analysis** (quantitative evidence or legal constraints), and \(\sigma\) maps that discrepancy into a bounded signal.

Here, \(q_{\mathrm{tension}}\) is treated as an internal indicator that a GBIM interpretation remains contested or in need of further corroboration, not as a claim about human subjective feeling.

GBIM also distinguishes between internal deliberation and committed consequence. A commitment operator can be defined as:

\[
K : S_{\mathrm{deliberative}} \rightharpoonup S_{\mathrm{committed}}
\]

marking the transition between deliberative states and committed states that alter GBIM, identity graphs, or civic‑facing views.

***

## 2.17 Revision Principle and Rural Implementation Roadmap

The governing revision principle for GBIM is:

- GBIM is not a direct write target for raw model output.  
- GBIM states are governed states rather than bare semantic vectors.  
- Promotion changes authority, provenance, disclosure, temporal, and operational status, not merely storage location.  
- Identity‑bearing and geospatially anchored knowledge must remain bounded by constitutional, jurisdictional, evidentiary, and sovereignty constraints.  
- GBIM belongs inside a broader architecture that includes dual sandbox domains, identity‑focused retention, Hilbert People Space, and the Community Hilbert Commons.

For rural communities seeking to build a similar system, this chapter serves as a **template**. A minimal implementation roadmap is:

1. **Define a GBIM‑like schema tailored to local context.**  
2. **Implement governed state metadata in relational stores.**  
3. **Deploy spatial and semantic layers for local data.**  
4. **Establish sandbox domains and explicit gate functions.**  
5. **Protect individuals and centre institutional accountability.**  
6. **Integrate with local leadership and governance processes.**

By following these steps, a practitioner can use this chapter as a prompt — in an LLM or in design meetings — to generate concrete schemas, gate functions, and reasoning flows tailored to their own data, laws, and community values. Under this revised framing, GBIM becomes a governed civic identity‑and‑geography layer within Ms. Allis and offers a pattern for other communities to build place‑accountable, non‑surveillant intelligence systems.
