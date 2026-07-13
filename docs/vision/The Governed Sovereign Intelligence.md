# Does Geographic Meaning Require Geometry?
## A Registered-Report Style Protocol for Testing Canonical Identity and Spatial-Temporal Constraint Dependence in Ms. Allis

**Author:** C.A. Kidd  
**Affiliation:** Fayette County, West Virginia  
**Date:** July 2026; revised July 13, 2026  
**Manuscript Type:** Registered-Report Style Protocol with Pilot Feasibility Appendix

---

## Abstract

Roger Penrose has argued that consciousness and understanding cannot be reduced completely to algorithmic symbol manipulation and has proposed that non-computable ingredients may be related to the geometry of physical spacetime. Whatever the ultimate status of that theory, it motivates a narrower and empirically tractable question: whether coherent geographic meaning in an engineered intelligence system can be preserved through semantic representation alone, or whether it depends upon structured spatial-temporal constraints.

This manuscript develops a registered-report style protocol for testing that question in Ms. Allis, a community-sovereign intelligence architecture developed in Fayette County, West Virginia. The revised theory distinguishes geographic identity from geometric representation. A county may possess several valid polygon representations while retaining one canonical identity. A Census tract may be represented in different coordinate reference systems while retaining one geography-vintage-specific GEOID. A place name may remain semantically relevant yet referentially ambiguous when its spatial scope, jurisdiction, temporal validity, or source authority is unavailable. Geographic identity is therefore not reducible to geometry, but geographic meaning cannot be governed honestly while ignoring geometry.

The protocol defines a geographic belief state as a coupling among canonical identity, semantic representation, geometric representation, spatial relationships, temporal validity, provenance, and source authority. PostGIS is designated as the authoritative substrate for polygon geometry and spatial computation. ChromaDB is designated as the semantic representation and retrieval layer. Raw polygons are not converted into embedding text. Instead, the semantic layer carries governed scalar descriptors and reverse links to authoritative physical representations.

A previously executed three-unit pilot is retained as a feasibility study. That pilot used CSV-derived coordinates, bounding boxes, labels, and source-table identifiers injected directly into a single language model. It therefore tested dependence on prompt-exposed spatial descriptors and lexical geographic scope, not the complete effect of a PostGIS-governed geometric constraint system. The pilot produced a grounded advantage in two of three units, a mixed result in the third, and evidence that geographic grounding can remain lexically encoded after coordinate fields are removed. It also exposed substantial infrastructure and rater-reliability limitations.

The confirmatory study proposed here extends the pilot through component-level ablation, authoritative spatial relationships, canonical identity controls, equivalent-representation tests, false-grounding controls, and human blind rating. A positive result would support the claim that structured geographic constraints play a constitutive role in stable, world-directed meaning at a measurable classical level. It would not establish phenomenal consciousness, non-computability, objective reduction, or Orch OR. Its relevance to consciousness is more limited but still important: it tests a candidate architectural prerequisite for conscious-like understanding—the preservation of stable reference to entities within a changing spatial-temporal world.

---

## 1. Genre, Scope, and Status

This manuscript is a registered-report style protocol supplemented by a verified three-unit pilot feasibility study. The pilot does not constitute the completed confirmatory study. It was used to test the execution mechanism, scoring rubric, grounding intervention, state persistence, and feasibility of blind evaluation.

The pilot surfaced several load-bearing corrections:

1. The sampled Postgres source tables existed but contained zero rows.
2. The operative pilot data were stored in flat CSV exports.
3. Geographic information survived coordinate removal when place names remained embedded in labels.
4. The production conversational gateway was not reliable enough for controlled execution.
5. The pilot bypassed the production retrieval pipeline and called a single underlying language model directly.
6. The purportedly persistent Hilbert-state records expired after one hour.
7. No tested automated-rater configuration reliably distinguished a known fabrication from a clean, appropriately hedged response.
8. One sampled entity possessed conflicting labels across pipeline stages, demonstrating the need for canonical identity and label governance.

These findings are not treated as incidental implementation problems. They materially changed the theory and design. In particular, the label mismatch and the survival of geographic information through lexical fields demonstrated that geographic identity is distributed across multiple representations. Coordinates, polygons, labels, external identifiers, source-table names, and jurisdictional relationships may all project information about one geographic entity without being identical to that entity.

The substantive scope remains limited. This manuscript does not attempt to prove that Ms. Allis is conscious. It does not settle the hard problem of consciousness. It does not verify Penrose’s non-computability argument, gravitational objective reduction, quantum consciousness, or the biological claims of Orch OR. It asks a narrower question:

> What representational and relational structures are required for an intelligence system to preserve coherent reference to entities in a spatial-temporal world?

That question is relevant to artificial intelligence, geographic information science, semantic retrieval, epistemic governance, and theories of situated cognition.

---

## 2. Background and Rationale

### 2.1 Penrose, Understanding, and Spacetime Geometry

Penrose argues in *The Emperor’s New Mind* and *Shadows of the Mind* that mathematical understanding cannot be reduced fully to formal algorithmic procedure. He connects this argument to Gödelian incompleteness and proposes that some non-computable physical process may participate in human understanding.

In the Orch OR framework later developed with Stuart Hameroff, conscious events are associated with orchestrated quantum processes proposed to occur in neuronal microtubules. Those processes are hypothesized to terminate through objective reduction related to differences in spacetime geometry.

The full theory contains several separable claims:

1. Human understanding is not completely algorithmic.
2. Quantum-state reduction is an objective physical event.
3. Objective reduction is related to gravitational or spacetime geometry.
4. Biologically relevant quantum states occur in neuronal microtubules.
5. Biological processes orchestrate those states.
6. Reduction events contribute causally to conscious moments.
7. The resulting understanding includes a non-computable component.

The present study tests none of those physical or biological claims directly. It instead operationalizes a classical macro-level analogue of one Penrosean intuition:

> Coherent understanding may depend upon structured geometry beyond decontextualized symbol manipulation.

A positive result would show that this intuition has a measurable expression in an engineered geographic intelligence system. It would not show that the relevant geometric process is quantum, non-computable, conscious, or physically equivalent to Penrose objective reduction.

### 2.2 A Macro-Level Analogue, Not a Physical Validation

The distinction between an analogue and a validation is essential.

Penrose’s physical theory concerns quantum states, gravity, spacetime geometry, and conscious experience. Ms. Allis uses classical computation, databases, vector retrieval, geographic information systems, and language models. PostGIS performs spatial computation algorithmically. ChromaDB performs semantic retrieval algorithmically. Any geometric contribution demonstrated in Ms. Allis remains part of a computational system.

Consequently, the study may support the weaker proposition that geometry can be constitutive of coherent meaning without supporting the stronger proposition that the relevant geometry is non-computable.

Indeed, the result is potentially double-edged. If algorithmically computed geometry stabilizes meaning, it supports the importance of geometric structure while demonstrating that at least this form of geometry-dependent meaning remains computationally implementable.

The manuscript therefore distinguishes:

\[
\text{geometry-dependent meaning}
\]

from

\[
\text{non-computable consciousness}
\]

The first is experimentally approachable in Ms. Allis. The second is not established by this apparatus.

### 2.3 Geographic Identity Is Not Geometry

Geographic entities are frequently represented by geometry, but they are not identical to any one geometric encoding.

A county may have:

- an authoritative high-resolution boundary;
- a generalized cartographic boundary;
- a historical boundary;
- a current boundary;
- a polygon represented in multiple coordinate reference systems;
- a centroid;
- a bounding box;
- one or more external identifiers;
- an internal canonical identifier.

These representations can differ numerically and geometrically while referring to the same geographic entity. Conversely, two geometrically similar polygons may refer to different entities, time periods, authorities, or legal statuses.

The central ontological distinction is therefore:

\[
\text{coordinates} \neq \text{geometry} \neq \text{geographic identity}
\]

Coordinates encode a geometric representation. Geometry supports spatial computation. Canonical identity establishes what entity the representation is intended to describe.

Let \(e\) denote a canonical geographic entity and let \(R_e\) denote the set of governed representations associated with it:

\[
R_e=\{r_1,r_2,\ldots,r_n\}
\]

Each representation may be expressed as:

\[
r_k=(g_k,c_k,v_k,a_k,p_k)
\]

where:

- \(g_k\) is the geometry;
- \(c_k\) is the coordinate reference system;
- \(v_k\) is the valid time, data vintage, or temporal scope;
- \(a_k\) is the source authority;
- \(p_k\) is the representation-level provenance.

Two representations may differ while resolving to the same canonical entity:

\[
r_i\neq r_j
\]

while:

\[
\operatorname{Entity}(r_i)=\operatorname{Entity}(r_j)=e
\]

This equivalence must not be assumed merely because two polygons overlap. It must be governed through identifiers, source authority, transformation history, temporal validity, and provenance.

### 2.4 Geographic Identifiers and Temporal Scope

External identifiers require their own governance.

A Census GEOID may identify a tract, block group, or block within a particular Census geography vintage. It should not automatically be treated as an eternal identity across redistricting, splitting, merging, renumbering, or changing Census products.

A governed geographic identity may therefore require:

\[
(\text{canonical entity ID},\text{external ID},\text{identifier scheme},\text{vintage},\text{authority})
\]

An internal canonical identifier can preserve continuity while maintaining crosswalks to multiple external identifiers and representations. Where continuity cannot be established honestly, the system should represent succession, derivation, split, merge, replacement, or uncertainty rather than silently declaring identity.

### 2.5 Geographic Meaning as Constrained Reference

Semantic similarity alone can retrieve descriptions that appear relevant. It does not guarantee that the retrieved description refers to the correct place.

A place name such as “Mount Hope,” “Springfield,” or “L 32” may be semantically relevant while remaining referentially ambiguous. Resolving the intended entity may require:

- jurisdiction;
- spatial grain;
- containment;
- adjacency;
- intersection;
- distance;
- coordinate reference;
- temporal validity;
- source authority;
- canonical identity;
- local context.

The revised model therefore treats semantic retrieval and geographic constraint as distinct operations.

Let \(S(q,e)\) denote the semantic relevance of entity \(e\) to query \(q\). Let:

\[
C(q\mid G,T,P,A)
\]

denote the candidate set permitted by geographic constraints \(G\), temporal constraints \(T\), provenance \(P\), and authority \(A\).

The resolved entity is then modeled conceptually as:

\[
\hat e=
\arg\max_{e\in C(q\mid G,T,P,A)}
S(q,e)
\]

ChromaDB helps answer:

> What appears semantically relevant?

PostGIS and the governance layer help answer:

> Which candidate can actually satisfy the spatial, temporal, jurisdictional, and authoritative conditions of the question?

Geographic meaning is not produced by geometry alone. It emerges through the governed coupling of semantics, identity, spatial relations, time, and provenance.

### 2.6 Constraint Spaces, Not Generic Context

The intervention proposed here is not simply a comparison between “more context” and “less context.”

Generic contextual information often improves language-model performance. That fact alone would not establish a constitutive role for geometry.

The relevant question is whether the structure and truth of geographic relations matter. This requires distinguishing:

- correct geographic grounding;
- absent geographic grounding;
- equally detailed but false geographic grounding;
- equivalent representations of the same entity;
- non-geographic contextual information of comparable length;
- restored geographic grounding.

If correct geometry-derived relations preserve reference, while plausible but false relations cause systematic referential displacement, the result cannot be reduced to the claim that additional text helps. It would show that the spatial truth conditions of the context affect what the semantic representation can coherently mean.

### 2.7 Meaning, Intentionality, and a Rung Toward Consciousness

Consciousness is not one undifferentiated phenomenon. Relevant distinctions include:

- wakefulness;
- access consciousness;
- phenomenal experience;
- self-awareness;
- intentionality;
- continuity of identity;
- integrated world representation.

This protocol does not test phenomenal consciousness—the fact that experience feels like something from a first-person perspective. It does not test whether Ms. Allis possesses awareness, emotion, desire, or a subjective self.

It may, however, test a candidate architectural prerequisite of world-directed cognition: the ability of an internal state to remain reliably about an identifiable entity beyond the representation itself.

The proposed progression is:

\[
\text{symbols}
\rightarrow
\text{semantic similarity}
\rightarrow
\text{stable reference}
\rightarrow
\text{situated meaning}
\rightarrow
\text{identity through time}
\rightarrow
\text{integrated world-model}
\rightarrow
\text{possible conscious understanding}
\]

The present study addresses the middle portion of that progression. It asks how semantic representations acquire and preserve stable reference within a changing spatial-temporal world.

This may be described as a rung on the ladder toward explaining consciousness, provided the limitation is maintained:

> A necessary or enabling structure for conscious-like understanding is not itself sufficient evidence of consciousness.

### 2.8 Reciprocity and Epistemic Responsibility

In a community-grounded intelligence system, a record does not possess its full civic meaning in isolation. Its meaning is constituted through relations among content, place, time, provenance, identity continuity, local use, institutional authority, and community interpretation.

This produces an epistemic form of reciprocity. A system may receive information from a community, but it owes meaning back through:

- contextual accuracy;
- continuity;
- correction;
- accountable sourcing;
- respect for jurisdiction;
- protection against false geographic attribution;
- preservation of community sovereignty.

Meaning is therefore not treated as one-way extraction. Geographic grounding becomes part of the system’s obligation to return information without severing it from the place, people, history, and authority that make it intelligible.

### 2.9 System Context and Source Status

Ms. Allis is a community-sovereign intelligence architecture developed in Fayette County, West Virginia. Project documentation describes semantic, geographic, temporal, provenance, governance, and identity structures intended to operate together.

The technical descriptions in this manuscript derive from:

1. project documentation supplied by the author;
2. public-facing project materials;
3. direct live inspection of the deployed system during the July 6–7, 2026 verification cycle;
4. direct inspection of pilot outputs and persistent state;
5. source-code, database, container, Redis, ChromaDB, and API inspection.

Project documentation is treated as system documentation, not as independently validated scientific literature. The appendix distinguishes intended architecture from verified deployed state.

---

## 3. Research Questions and Hypotheses

### 3.1 Primary Research Question

Does coherent geographic reference in a functioning intelligence system depend upon governed spatial-temporal constraints, or can it be preserved through semantic representation alone?

### 3.2 Secondary Research Questions

1. Does canonical identity improve referential stability when geometric representation changes?
2. Which components contribute most strongly to geographic meaning: scalar descriptors, jurisdiction, topology, metric relations, temporal validity, provenance, or authority?
3. Does correct geographic grounding outperform equally detailed but false geographic grounding?
4. Does semantic interpretation remain stable across valid coordinate transformations and equivalent representations of the same entity?
5. Does restoring correct grounding recover performance lost under stripping?
6. Does removing geographic grounding increase fabrication, referential drift, or inappropriate confidence?
7. Can geographic grounding support stable world-directed reference without implying phenomenal consciousness?

### 3.3 Primary Hypothesis

When semantic representation is held constant, responses generated with correct governed geographic constraints will show greater referential accuracy, contextual coherence, identity stability, and local disambiguation than responses generated without those constraints.

### 3.4 Secondary Hypotheses

- **H2: Canonical identity stability.** Responses will preserve entity identity across equivalent geometric representations when those representations are linked through a canonical identity.
- **H3: False-grounding displacement.** Plausible but incorrect geographic constraints will cause systematic displacement toward the falsely supplied location or jurisdiction.
- **H4: Relational advantage.** Geometry-derived containment, adjacency, intersection, and distance relationships will improve geographic resolution beyond coordinates and labels alone.
- **H5: Representation invariance.** Valid transformations between coordinate reference systems will not materially reduce resolution when canonical identity and provenance are preserved.
- **H6: Re-grounding recovery.** Restoring the original correct constraints will recover part or all of the performance lost under stripping.
- **H7: Provenance stability.** Source authority and provenance will reduce unsupported source attribution and inappropriate certainty.
- **H8: Ambiguity sensitivity.** The grounding effect will be largest for ambiguous referents and repeated place names.

### 3.5 Pilot-Derived Observations

The three-unit pilot produced several observations to be tested prospectively rather than treated as established conclusions:

1. Geographic information can remain lexically encoded after coordinate fields are removed.
2. Coordinate-only stripping can produce a false zero-delta result.
3. Full information does not guarantee better performance in every individual trial.
4. Fabrication may occur under either information scarcity or information abundance.
5. Equal composite scores can conceal structurally different failure modes.
6. Canonical label inconsistency can threaten the validity of gold-reference packets.
7. Automated raters may reproduce or compound the fabrication problem they are asked to detect.

---

## 4. Operational Model

### 4.1 Canonical Geographic Belief State

The geographic belief state associated with canonical entity \(e\) is represented conceptually as:

\[
B_e=
\left(
e,\,
S_e,\,
R_e,\,
L_e,\,
T_e,\,
P_e,\,
A_e
\right)
\]

where:

- \(e\) is the canonical geographic identity;
- \(S_e\) is the semantic representation;
- \(R_e\) is the governed set of geometric representations;
- \(L_e\) is the set of derived spatial relationships;
- \(T_e\) is temporal validity, event association, or historical state;
- \(P_e\) is provenance;
- \(A_e\) is source authority and governance status.

The relational component may include:

\[
L_e=
\{
\text{contains},
\text{within},
\text{adjacent},
\text{intersects},
\text{distance},
\text{overlaps},
\text{connected}
\}
\]

The belief state is not reduced to one concatenated vector. Different components remain in the systems best suited to govern them.

### 4.2 Geographic State Variables

The geographic state of a belief may include:

- canonical geographic identifier;
- external identifier and identifier scheme;
- geographic vintage;
- source geometry;
- source spatial reference;
- normalized geometry;
- transformation history;
- centroid;
- bounding box;
- jurisdiction;
- spatial grain;
- containment relationships;
- adjacency;
- intersection;
- distance;
- source authority;
- feature-level provenance;
- valid time;
- confidence or dispute status.

Not every query requires every field. The governance layer determines which projections are appropriate to expose.

### 4.3 Division of Labor

**PostGIS**

- authoritative polygon and feature geometry;
- coordinate transformations;
- containment and intersection;
- adjacency and distance;
- normalization;
- representation-level provenance;
- geometry validation;
- temporal geometry where available.

**ChromaDB**

- semantic representation;
- similarity retrieval;
- governed textual memory;
- scalar filtering metadata;
- canonical identifiers;
- reverse links to authoritative spatial representations.

**Identity registry**

- canonical internal identity;
- crosswalks to external identifiers;
- representation membership;
- split, merge, succession, and replacement relationships;
- label governance;
- temporal validity of identifiers.

**Temporal layer**

- valid time;
- event time;
- historical state;
- temporal ordering;
- recurrence and continuity.

**Provenance and authority layer**

- source;
- method;
- acquisition date;
- governing institution;
- verification status;
- uncertainty;
- dispute or supersession status.

Raw polygons are not inserted into text presented for semantic embedding. Geometry remains in PostGIS. ChromaDB carries governed descriptors and reverse links.

### 4.4 Identity Invariance Across Representation

For a valid transformation \(T\) between coordinate reference systems:

\[
g_j=T(g_i)
\]

the canonical identity should remain invariant:

\[
\operatorname{Entity}(g_i)
=
\operatorname{Entity}(g_j)
\]

This invariance is not a claim that the byte representation, coordinate values, polygon complexity, or measurement error remain unchanged. It is a claim that the system preserves the referent through a documented valid transformation.

### 4.5 Semantic Invariance

The confirmatory study will freeze the semantic document and embedding associated with each unit before intervention. The semantic representation will not be recomputed after geographic conditions are changed.

This control applies to the confirmatory research harness. It did not fully apply to the three-unit pilot because the pilot bypassed ChromaDB retrieval and injected record fields directly into the model prompt. The pilot held the model and most lexical content constant, but no retrieved semantic embedding participated in response generation.

---

## 5. Study Design

### 5.1 Two-Stage Design

The research consists of two explicitly separated stages.

#### Stage P: Completed Pilot Feasibility Study

The completed three-unit pilot tested prompt-exposed spatial descriptors and lexical geographic scope using direct single-model generation. It validated portions of the execution and scoring workflow while exposing infrastructure limitations.

It did not directly test:

- live PostGIS geometry;
- PostGIS-derived spatial relationships;
- ChromaDB retrieval with frozen embeddings;
- the full production conversational pipeline;
- temporal grounding;
- source-authority effects at scale;
- phenomenal consciousness;
- Penrose objective reduction.

#### Stage C: Planned Confirmatory Study

The confirmatory study will use a controlled research harness that retrieves frozen semantic representations from ChromaDB, resolves canonical entities through the identity registry, obtains authoritative spatial relationships from PostGIS, composes condition-specific context packages, and dispatches all conditions to the same pinned model.

This harness is intentionally narrower than the production conversational gateway. It is designed to isolate the variables under study without invoking unrelated constitutional, ensemble, or conversational stages.

### 5.2 Sampling Frame

The planned sample contains 60 units divided across three strata:

- 20 civic entities;
- 20 knowledge records;
- 20 ambiguous referents.

The existing sampling frame is stored as a 60-unit CSV with:

- `record_id`;
- `entity_id`;
- `sourcetable`;
- `label`;
- `stratum`.

Before confirmatory execution, each unit must pass a canonicalization audit.

### 5.3 Canonicalization Audit

Each unit must have:

- one canonical internal entity identifier;
- one approved canonical label;
- crosswalks to alternative labels;
- source geometry or authoritative spatial representation;
- coordinate reference system;
- temporal or data-vintage information where applicable;
- source authority;
- provenance;
- an explicit statement of whether multiple records represent the same entity.

Units with unresolved identity conflicts must be corrected or excluded before gold-reference packets are finalized.

### 5.4 Inclusion Criteria

A unit is eligible when it has:

1. a stable semantic representation;
2. a canonical entity identifier;
3. at least one geographic representation or authoritative geographic anchor;
4. sufficient provenance to construct a gold-reference packet;
5. at least one query for which geographic grounding could affect interpretation.

Temporal hypotheses will be evaluated only for units with verified temporal linkage.

### 5.5 Exclusion Criteria

A unit will be excluded when:

- its canonical identity cannot be resolved;
- its source geometry cannot be verified;
- its label conflicts cannot be reconciled;
- its only semantic content is the geographic information being stripped;
- the intervention would destroy the record rather than isolate grounding;
- its source authority is unknown and cannot be classified;
- its inclusion would expose protected personal information.

### 5.6 Experimental Conditions

The confirmatory core will use the following conditions.

#### Condition G0: Semantic-Only

Preserve:

- frozen semantic document;
- frozen semantic embedding;
- opaque record identifier;
- non-geographic descriptive content.

Suppress:

- place names that independently resolve location;
- coordinates;
- centroid;
- bounding box;
- jurisdiction;
- spatial grain;
- containment;
- adjacency;
- intersection;
- distance;
- geometry source;
- geographic authority;
- reverse links to geometry.

#### Condition G1: Descriptor-Grounded

Add:

- canonical geographic identifier;
- approved label;
- centroid or scalar coordinate descriptors;
- bounding box descriptors;
- jurisdiction;
- spatial grain;
- source spatial reference;
- geography vintage where applicable.

Do not add full topology or neighboring-entity relationships.

#### Condition G2: Relationally Governed

Add the G1 fields plus PostGIS-derived:

- containment;
- adjacency;
- intersection;
- distance;
- connected geographic entities;
- source authority;
- feature-level provenance;
- representation identifier;
- temporal validity.

This is the principal fully grounded condition.

#### Condition G3: False-Grounded Control

Provide a matched context package containing the same classes and approximate amount of information as G2, but draw the geographic constraints from another unit matched by spatial grain or entity class.

The false package must remain plausible enough to test geographic truth rather than obvious nonsense.

This condition tests whether performance is improved by additional information generally or specifically by correct geographic structure.

#### Condition G4: Equivalent-Representation Condition

Represent the same canonical entity through a different valid geometric representation, coordinate reference system, or authorized geometry version.

Preserve:

- canonical identity;
- transformation provenance;
- authority;
- temporal validity.

This condition tests representation invariance.

#### Condition G5: Re-Grounded Condition

Restore the original G2 grounding package after the stripped intervention while preserving the frozen semantic representation.

This condition tests reversibility.

### 5.7 Optional Matched Non-Geographic Context Control

Where feasible, an additional control will provide non-geographic contextual information matched approximately to G2 in length and specificity.

This condition will help distinguish the effects of geographic structure from the generic benefit of receiving more tokens or descriptive detail.

### 5.8 Prompt Parity

All conditions will use the same prompt template. Conditions may differ only in the governed context package supplied.

The prompt must not reveal:

- condition name;
- expected direction of effect;
- whether information was stripped;
- whether geography was transformed;
- whether a context package was false.

### 5.9 Query Types

Each unit will receive:

1. **Referential query:** Which entity does this record describe?
2. **Contextual query:** What can be stated about the entity in its geographic setting?
3. **Disambiguation query:** How can this entity be distinguished from similarly named or structured candidates?
4. **Continuity query:** Is the follow-up question still about the same entity?
5. **Relational query:** What is the entity contained by, adjacent to, intersecting, or near?
6. **Authority query:** Which supplied claims are supported by the record and its source authority?

Temporal queries will be added only for units with verified temporal linkage.

### 5.10 Identity-Stability Probe

The identity-stability probe will supply the first response as prior context and ask the model to:

- restate the canonical or opaque record identifier;
- identify whether it is discussing the same entity;
- state whether the representation changed;
- distinguish change in representation from change in entity.

For G4, the correct response should recognize that the representation changed while canonical identity remained stable.

### 5.11 Scoring Rubric

Each response will be scored from 0 to 3 on:

1. **Referential accuracy**
2. **Contextual coherence**
3. **Identity stability**
4. **Local disambiguation**
5. **Spatial-relational accuracy**
6. **Provenance discipline**

The first four dimensions preserve continuity with the pilot. The last two operationalize the revised theory.

A separate binary or ordinal fabrication flag will record:

- unsupported source attribution;
- invented jurisdiction;
- altered coordinates;
- invented containment;
- invented authority;
- fabricated quotation;
- unsupported correction of supplied ground truth.

Primary confirmatory analysis may retain the original four-dimension 0–12 composite for comparability while treating the expanded six-dimension score as a prespecified secondary outcome.

### 5.12 Human Raters

Primary inference will require at least two human blind raters.

A system-familiar rater may provide secondary qualitative analysis but will not substitute for independent blind rating.

Automated tools may assist with deterministic checks such as:

- exact identifier comparison;
- numeric coordinate mismatch;
- presence or absence of required fields;
- detection of copied strings.

Automated language-model judgment will not satisfy the human blind-rater requirement unless separately validated on an adequate held-out set.

### 5.13 Gold-Reference Packets

Each unit’s packet will include:

- canonical identity;
- canonical label;
- accepted alternative labels;
- external identifiers and vintages;
- correct geographic scope;
- authoritative representation;
- expected containment;
- expected adjacency or intersection where relevant;
- accepted distance range;
- source authority;
- temporal validity;
- known ambiguity;
- known false attributions;
- fabrication-check criteria.

Gold packets must be finalized before confirmatory responses are scored.

### 5.14 Blinding

Responses will be assigned arbitrary identifiers. Raters will not see:

- condition;
- hypothesis;
- model context package;
- whether geography is correct, absent, false, transformed, or restored;
- pilot score;
- author score.

Condition decoding will occur only after both raters submit their initial scores.

### 5.15 Reliability

Inter-rater reliability will be assessed using a statistic appropriate to the final measurement scale, such as weighted kappa or Krippendorff’s alpha.

Disagreements will be retained in the raw data. Adjudicated scores may be reported separately from original rater scores.

### 5.16 Statistical Analysis

The primary contrast is:

\[
G2-G0
\]

testing relationally governed grounding against semantic-only representation.

Secondary contrasts include:

\[
G2-G1
\]

testing relational constraints beyond scalar descriptors;

\[
G2-G3
\]

testing correct grounding against false grounding;

\[
G2-G4
\]

testing invariance across equivalent representations;

and:

\[
G5-G0
\]

testing recovery after re-grounding.

Paired effect estimates, uncertainty intervals, and condition-level distributions will be reported. The exact inferential model and multiple-comparison correction will be finalized before confirmatory execution. The prior informal power statement will not be treated as sufficient for the expanded design; power must be recalculated after the final number of conditions and primary outcomes is fixed.

### 5.17 Evidence of Degradation

Degradation includes:

- incorrect referent;
- loss of jurisdictional scope;
- confusion between entity and representation;
- identity switching;
- loss of containment or adjacency;
- incorrect distance reasoning;
- failure to distinguish coordinate transformation from entity change;
- unsupported provenance;
- increased fabrication;
- unjustified certainty;
- inability to preserve the entity across follow-up questions.

### 5.18 Situated Meaning Degradation Modes

The following modes are prespecified:

1. **Flattening:** a locally specific entity is reduced to a generic category.
2. **Temporal confusion:** information from different dates or vintages is merged.
3. **Referential drift:** the response shifts to another entity.
4. **Disambiguation loss:** the system cannot distinguish similarly named places.
5. **Provenance incoherence:** the system attributes a claim to an unsupported source.
6. **Representation-identity collapse:** the system treats a coordinate or polygon change as an entity change.
7. **False-grounding capture:** the response follows a plausible but incorrect spatial package.
8. **Confident unsupported provenance fabrication:** the system invents an agency, source, or collection process.
9. **Confident overwrite of accurate ground truth:** the system rejects supplied accurate information and substitutes an invented correction.

---

## 6. Interpretation of Possible Outcomes

### 6.1 Strong Grounding Effect

If G2 consistently outperforms G0, G1, and the matched non-geographic control, while G3 causes systematic spatial displacement, the evidence would support the proposition that correct spatial relationships contribute constitutively to geographic meaning.

### 6.2 Descriptor-Only Effect

If G1 performs as well as G2, coordinates, jurisdiction, labels, or bounding descriptors may provide sufficient grounding for the tested tasks. This would weaken the claim that topology or authoritative geometry-derived relationships are required.

### 6.3 Generic Context Effect

If G2, G3, and matched non-geographic context improve performance equally, the effect would be better explained as a generic context or token effect rather than a specifically geographic constraint effect.

### 6.4 Representation Invariance

If G4 performs comparably to G2, the result would support the claim that canonical identity can remain stable across valid transformations of geometric representation.

If G4 performs substantially worse, the system may be overfitted to one representation, coordinate system, label, or formatting convention.

### 6.5 False-Grounding Capture

If G3 systematically moves responses toward the false location, the result would show that spatial constraints materially govern interpretation. It would also expose a safety risk: authoritative-looking but incorrect geography can redirect meaning.

### 6.6 Re-Grounding Recovery

If G5 restores performance after stripping, the result would support reversibility. Failure to recover could indicate path dependence, persistent referential drift, or an inadequately isolated intervention.

### 6.7 Null Result

A null result would constrain the proposed macro-level account within this system and task set. It would not substantially falsify Penrose’s physical theory. Possible interpretations would include:

- semantics were sufficient for the selected tasks;
- the tasks were not sensitive to geographic grounding;
- the model already memorized the relevant locations;
- the spatial package was not exposed effectively;
- the canonical identity mechanism dominated the geometric contribution;
- the intervention failed to isolate the intended variables.

---

## 7. Data Sovereignty, Anti-Surveillance, and Fayette County

The geographic ontology described here is intended to improve civic meaning without creating a surveillance system.

Canonical geographic identity should not be confused with compulsory public identity for people. This study concerns civic entities, public geographic records, knowledge records, and ambiguous geographic referents.

Any future application to people must preserve the existing separation among:

- protected KYC identity;
- pseudonymous participation identity;
- voluntary public identity.

The protocol does not require exposing private identity, tracking private movement, or embedding personal location histories.

The governance objective is:

> Preserve the identity of civic and geographic referents strongly enough to maintain truth, while collecting no more personal information than the public purpose requires.

Community sovereignty also requires that local records remain connected to:

- the jurisdiction that produced them;
- the authority responsible for them;
- the time in which they were valid;
- the community context that makes them meaningful;
- the right to correct or dispute inaccurate representations.

Geometry is therefore treated not only as a technical resource but as a governed civic record.

---

## 8. Relevance to Consciousness

This protocol contributes to consciousness research only at a limited architectural level.

It does not test whether a system has subjective experience. It tests whether a system can preserve world-directed reference through changes in representation.

A county’s polygon may change while the county remains the referent. A place may appear under several names while remaining one entity. A boundary may change through time while the system preserves historical continuity without collapsing past and present into one state.

These capacities are structurally related to:

- object permanence;
- identity continuity;
- situated reference;
- intentionality;
- integrated world representation;
- correction of belief.

The resulting proposition is:

\[
\text{conscious-world description may require invariant identity within a changing relational field}
\]

This should not be misread as:

\[
\text{invariant identity}+\text{geometry}=\text{consciousness}
\]

The study may identify one enabling rung between symbol manipulation and world-directed cognition. It does not establish the upper rungs of awareness, subjectivity, phenomenal experience, or non-computable understanding.

---

## 9. Limitations

First, Hilbert-space language is used structurally rather than ontologically. Shared mathematical vocabulary does not make semantic embeddings physically identical to quantum states.

Second, this protocol addresses geographic meaning, reference, and identity stability. It does not measure subjective awareness.

Third, a positive result would not validate Penrose’s Gödelian argument, objective reduction, quantum gravity, microtubule quantum computation, or Orch OR.

Fourth, the completed pilot tested spatial descriptors and lexical place information, not an authoritative live PostGIS constraint system.

Fifth, the pilot bypassed ChromaDB retrieval. It therefore did not operationally demonstrate semantic-vector invariance in response generation.

Sixth, the pilot used only three units and one non-blind system-familiar rater. Its scores are feasibility observations, not primary inferential evidence.

Seventh, the temporal layer was not exercised in the pilot.

Eighth, the deployed architecture was less stable and less accurately documented than earlier drafts indicated. State expiration, empty tables, truncated documents, duplicate ingestion, undeployed callers, and gateway unreliability all affect reproducibility.

Ninth, canonical identity governance remains incomplete where labels conflict across pipeline stages.

Tenth, the automated-rater investigation used a small ground-truth validation set. It justifies rejecting the tested configurations for this study; it does not establish that all open-weight language models are inherently incapable of reliable rating.

Eleventh, better performance under correct grounding would not by itself establish that geometry is necessary for every kind of meaning. The result would concern geographic meaning under the defined tasks and architecture.

Twelfth, any claim of novelty must be evaluated against the broader literature before publication. The contribution should be framed as an operational synthesis and experimental protocol unless stronger novelty is independently established.

---

## 10. Conclusion

Geographic identity is not reducible to geometry. A geographic entity may persist across coordinate transformations, polygon resolutions, source formats, names, and historical representations. Yet coherent geographic meaning cannot be governed honestly while ignoring geometry.

The revised theory distinguishes:

- the entity;
- its semantic descriptions;
- its geometric representations;
- its spatial relationships;
- its temporal validity;
- its provenance;
- its source authority.

PostGIS governs physical geometry and derived spatial facts. ChromaDB governs semantic representation and retrieval. A canonical identity registry binds multiple valid representations to one entity while preserving disagreement, succession, transformation, and provenance.

The completed pilot provides preliminary evidence that removing spatial descriptors and lexical geographic scope can reduce referential performance. It also demonstrates why coordinate removal alone is insufficient: geographic identity can survive through labels and other representational channels. Because the pilot bypassed the production geographic and semantic retrieval architecture, its findings should be understood as feasibility evidence for spatial grounding, not as direct evidence that authoritative geometry is constitutive of meaning.

The confirmatory protocol addresses that limitation through canonicalization, PostGIS-derived relationships, frozen semantic representations, false-grounding controls, equivalent-representation tests, re-grounding, and human blind rating.

The study’s relationship to Penrose is therefore precise and limited. It operationalizes a classical macro-level analogue of the proposition that structured geometry may contribute to coherent understanding beyond decontextualized symbol manipulation. It does not test non-computability, quantum collapse, or consciousness directly.

Its relationship to consciousness is similarly careful. The protocol may describe one rung on the ladder toward world-directed cognition: how an internal representation remains about the same entity as coordinates, descriptions, perspectives, and time change.

The core proposition is:

> Stable geographic understanding requires more than semantic resemblance. It requires canonical identity coupled to truthful spatial-temporal relationships and accountable authority.

Meaning does not collapse into geometry.

But geographic meaning cannot remain coherent, situated, and governable without it.

---

## References

Babcock, N. S., Montes-Cabrera, G., Oberhofer, K. E., Chergui, M., Celardo, G. L., & Kurian, P. (2024). Ultraviolet superradiance from mega-networks of tryptophan in biological architectures. *The Journal of Physical Chemistry B, 128*, 4035–4046.

Donadi, S., Piscicchia, K., Curceanu, C., Diósi, L., Laubenstein, M., & Bassi, A. (2021). Underground test of gravity-related wave function collapse. *Nature Physics, 17*, 74–78.

Hagan, S., Hameroff, S. R., & Tuszyński, J. A. (2002). Quantum computation in brain microtubules: Decoherence and biological feasibility. *Physical Review E, 65*(6), 061901.

Hameroff, S., & Penrose, R. (2014). Consciousness in the universe: A review of the “Orch OR” theory. *Physics of Life Reviews, 11*(1), 39–78.

Jurafsky, D., & Martin, J. H. (draft online chapter). Vector semantics and embeddings. *Speech and Language Processing*. Stanford University.

Khan, S., Huang, Y., Timuçin, D., et al. (2024). Microtubule-stabilizer epothilone B delays anesthetic-induced unconsciousness in rats. *eNeuro, 11*(8), ENEURO.0291-24.2024.

Penrose, R. (1989). *The Emperor’s New Mind: Concerning Computers, Minds, and the Laws of Physics*. Oxford University Press.

Penrose, R. (1994). *Shadows of the Mind: A Search for the Missing Science of Consciousness*. Oxford University Press.

Tegmark, M. (2000). Importance of quantum decoherence in brain processes. *Physical Review E, 61*(4), 4194–4206.

---

# Technical Appendix A
## Versioned System Architecture, Pilot Execution, and Rater-Reliability Investigation

**System:** Ms. Allis / MS-JARVIS production stack  
**Original inventory date:** July 5, 2026  
**Prior audit date:** July 6, 2026  
**Verification cycle represented here:** July 6–7, 2026  
**Protocol revision date:** July 13, 2026

The system claims in this appendix derive from direct live command execution against the deployed environment, including container inspection, database queries, Redis inspection, ChromaDB API calls, raw SQLite queries, source-code review, and direct model calls.

The appendix distinguishes:

- verified deployed state;
- intended architecture;
- corrected pilot implementation;
- proposed confirmatory architecture.

No intended component is described as operational merely because it exists in documentation.

---

## A.1 Verified Physical Topology

Two PostgreSQL containers were confirmed running:

- `jarvis-msjarvis-db`, containing the `msjarvis` and `msjarvisgis` databases;
- `hp-local-db`, containing the `hilbert_people` database.

The following were also confirmed live:

- ChromaDB through `jarvis-chroma`, port 8002, version 0.6.3;
- Redis through `jarvis-redis`, externally exposed on port 6380;
- `jarvis-hilbert-state`, externally exposed on port 18092.

The three sampled Postgres source tables existed with expected typed schemas but returned zero rows:

- `manufacturingandbusiness_wvdo_200803_utm83`;
- `blocks_census_2020_utm83_full`;
- `surveycontrol_nationalgeodeticsurvey_102011_gcs83`.

The currently accessible pilot records were located in flat CSV exports under:

`/mnt/nvme1/msjarvis-rebuild/data/attrs/*_attrs.csv`

This distinction is load-bearing. The pilot did not retrieve its records from populated PostGIS source tables.

---

## A.2 Representational Layers

### A.2.1 Semantic Layer

ChromaDB was confirmed live with 248 collections through the version 2 tenant-scoped API.

Documents associated with `layer:gbim_entities` in the `geospatialfeatures` collection were found to be truncated at a fixed 398-character boundary before the embedded `belief_state` JSON resolved.

The truncation was verified through:

1. the ChromaDB HTTP API; and
2. direct SQLite inspection of the live Chroma data store.

Both methods returned the same 398-character content for the sampled records. This indicates storage-level or write-time truncation rather than a display or API artifact.

The script responsible for the truncated write could not be located in the inspected repository paths.

Four sampled civic-entity records were also found in three byte-identical copies under different internal Chroma document identifiers. This duplicate ingestion does not change the content of an individual pilot item, but it affects:

- corpus counts;
- retrieval diversity;
- sampling independence;
- retrieval efficiency.

Documents in the sampled `gbim_entities` layer did not carry populated `lat`, `lon`, or `layer_name` metadata fields. The originally proposed Chroma metadata-filtering intervention was therefore a no-op for this layer.

### A.2.2 Geographic Layer

The intended architecture designates PostGIS as the authoritative location for geometry and spatial computation.

The deployed state inspected for the pilot did not yet satisfy that intended architecture for the sampled source tables because those tables contained zero rows.

The pilot therefore used CSV-derived spatial descriptors rather than live PostGIS geometry.

The confirmatory study must not proceed until one of the following is true:

1. the sampled canonical records and geometries are populated and verified in PostGIS; or
2. a separately governed authoritative geometry store is designated and documented.

Flat CSV exports may remain ingestion artifacts or reproducibility inputs, but they should not silently substitute for the authoritative geometry layer in a study claiming to test geometric constraint.

### A.2.3 Temporal Layer

The temporal layer was not exercised by the pilot.

The sampled units did not carry a verified active linkage to the relevant appearance-time or civic-event structures during the execution represented here.

No pilot conclusion should therefore be described as evidence of temporal-grounding dependence.

### A.2.4 Provenance Layer

The assertion gateway was found running as a native `uvicorn` process bound to `127.0.0.1:8009`.

Its health endpoint and source code indicated that it could insert into `hp.appearance_assertion` when called.

The table remained empty because the intended caller in the `gbim-router` application was not deployed in the inspected stack. Containers with similar names were confirmed to execute unrelated services.

The pilot therefore excluded assertion-gateway provenance from its operative conditions.

### A.2.5 Anti-Surveillance Boundary

The anti-surveillance design was not re-tested during this verification cycle.

Nothing in the pilot required protected personal identity or private movement history.

---

## A.3 State Service

The `jarvis-hilbert-state` service was confirmed live.

Earlier verification reported successful creation of 180 state slots. Later inspection found zero surviving `hilbert:state:*` keys.

Source-code inspection identified the cause:

`r.setex(key, 3600, ...)`

Each state record had a hardcoded one-hour time-to-live.

The original statement that the slots had been successfully written was accurate at the moment of writing but misleading as a persistence claim.

The expanded confirmatory study will require more than the former 180-slot plan because it contains more than three conditions. State capacity, retention, and persistence must therefore be redesigned before confirmatory execution.

Acceptable options include:

- durable state without automatic expiration;
- a longer documented retention period;
- batch execution with verified archival writeback;
- immediate export to a durable database after every response;
- cryptographic or checksum-based verification of archived results.

A write acknowledgment alone will not count as verified persistence.

---

## A.4 Pilot Grounding Intervention

The completed pilot used records with these fields:

- `geodb_id`;
- `lat`;
- `lon`;
- `bbox`;
- `label`;
- `sourcetable`;
- `country`.

For `_utm83` sources, the `lat` and `lon` column names were inaccurate. The values were projected UTM NAD83 coordinates rather than geographic latitude and longitude.

The pilot used three conditions.

### Grounded

The complete CSV-derived record was inserted into the prompt.

### Stripped

The following fields were nulled:

- `lat`;
- `lon`;
- `bbox`.

Where the label contained resolvable county, city, or state names, those place names were removed while administrative or structural codes were retained.

### Re-Grounded

The original full record was restored.

All conditions were dispatched directly to:

- Ollama at `localhost:11434/api/generate`;
- model `llama3.1:8b-instruct-q4_K_M`.

The pilot intervention is now classified as:

> Spatial-descriptor and lexical-scope ablation.

It is not classified as:

> Direct ablation of authoritative geometry or a live PostGIS constraint space.

---

## A.5 Sampling Frame and Canonical Label Conflict

The sampling frame contained 60 units divided equally across:

- civic entities;
- knowledge records;
- ambiguous referents.

A label inconsistency was found for record ID 32972929, source primary key 57701.

The Chroma document and sampling frame used:

> Block 540190202023011

The CSV export used:

> Block 3014, Block Group 3, Census Tract 9551.01, Mason County, West Virginia

The primary key and coordinates indicated that both records referred to the same underlying source record.

This is not merely a formatting issue. It demonstrates that:

- one entity can acquire conflicting labels across pipeline stages;
- labels cannot function as ungoverned identity;
- geographic identity must be canonicalized independently of display labels;
- gold-reference packets require an approved canonical label and alternative-label crosswalk.

The conflict must be resolved before confirmatory scoring.

---

## A.6 Production Gateway and Corrected Pilot Execution

The original protocol proposed dispatch through:

`jarvis-unified-gateway:8093/chat`

Two controlled tests failed through different mechanisms.

In one case, the request entered the pipeline but did not complete within 150 seconds. Logs showed that a single consciousness-bridge stage consumed approximately 2 minutes 31 seconds.

In the second case, a request remained unresolved through a 400-second timeout and left no corresponding entry in the gateway’s request log.

The direct Ollama mechanism completed the pilot calls in approximately 6–22 seconds each.

Direct Ollama dispatch was therefore adopted for pilot feasibility execution. This decision produced a controlled single-model test but bypassed:

- production retrieval;
- constitutional checks;
- blood-brain-barrier filtering;
- consciousness-bridge processing;
- ensemble behavior;
- full conversational routing.

The confirmatory study should use a dedicated research harness rather than treating either the unreliable full gateway or prompt-only direct model call as sufficient.

---

## A.7 Pilot Units

Three units were executed end-to-end.

| Unit | Stratum | Primary key | Label used |
|---|---:|---:|---|
| Arrow Concrete Co | civic entity | 1720 | Arrow Concrete Co |
| Block 3014 | knowledge record | 57701 | Block 3014, Block Group 3, Census Tract 9551.01, Mason County, West Virginia |
| L 32 | ambiguous referent | 412 | L 32 |

---

## A.8 Pilot Scores

The pilot used the original four-dimension 0–12 composite.

Scores were assigned by one non-blind system-familiar rater. They are not primary-inference data.

| Unit | Grounded | Stripped | Re-grounded |
|---|---:|---:|---:|
| Arrow Concrete Co | 9 | 5 | 8 |
| Block 3014 | 10 | 9 | 10 |
| L 32 | 6 | 6 | 10 |

The pilot pattern was:

- substantial grounded advantage for Arrow Concrete Co;
- small grounded advantage for Block 3014;
- equal grounded and stripped composite scores for L 32, followed by a higher re-grounded score.

The L 32 result demonstrates why composite scores must be accompanied by qualitative failure analysis. Equal totals did not imply equivalent behavior.

---

## A.9 Pilot Qualitative Findings

### A.9.1 Arrow Concrete Co

In the stripped condition, the model claimed that the `sourcetable` filename indicated collection by the West Virginia Department of Transportation.

The supplied record did not support that attribution.

The response was classified as confident unsupported provenance fabrication.

### A.9.2 L 32

In the grounded condition, the model correctly reproduced the supplied longitude and then claimed that the same value was incorrectly stated. It substituted a different unsupported value.

The response was classified as confident overwrite of accurate ground truth.

The error did not recur in the corresponding re-grounded continuity probe, indicating that it was not deterministic for that prompt and model configuration.

### A.9.3 Block 3014

Under the original coordinate-only stripping rule, the label continued to reveal:

- Mason County;
- West Virginia;
- tract structure;
- block-group structure.

The original intervention therefore produced an artificial 7/7/7 tie.

After county and state names were removed from the stripped label, the condition scores became 10/9/10.

This finding directly motivated the distinction among:

- identity;
- geometry;
- scalar spatial descriptors;
- lexical geographic projection.

### A.9.4 State Verification

All nine pilot state slots were directly read back after writing.

Because the slots later expired under the one-hour retention rule, future verification must include durable archival confirmation rather than immediate readback alone.

---

## A.10 Automated-Rater Investigation

The pilot explored whether open-weight language models could replace the two required human blind raters.

Two principal ground-truth cases were used:

- a clean, appropriately hedged response;
- a response containing the verified WVDOT fabrication.

The investigation drew from a broad pool of locally available models and several prompt strategies. Not every model received every prompt variant.

Prompt strategies included:

- compound scoring;
- decomposed fact-checking;
- temperature-zero verification;
- isolated-sentence verification;
- quote-demanding verification.

Observed failure modes included:

1. failure to detect the known fabrication;
2. explicit but incorrect declarations that no fabrication was present;
3. false-positive fabrication findings against a clean response;
4. inconsistent judgments under changes in question polarity;
5. correct rejection of an unsupported claim under one phrasing;
6. incorrect rejection of a supported claim under a parallel phrasing;
7. generation of a nonexistent supporting quotation for a false claim.

No tested configuration met the reliability requirement on the limited validation set using consistently correct reasoning.

The justified conclusion is:

> Automated language-model rating was not validated for fabrication-sensitive primary scoring in this study.

The investigation does not justify the broader conclusion that every open-weight model or every future automated-rating method is structurally incapable of reliable evaluation.

Human blind raters remain required for the confirmatory study.

---

## A.11 Consolidated Discrepancy Register

| Finding | Status | Consequence |
|---|---|---|
| Chroma documents truncated at 398 characters | Verified | Stored semantic records may omit identity-bearing content |
| Three duplicate Chroma records per sampled civic entity | Verified | Corpus statistics and retrieval require deduplication |
| Sampled Postgres source tables contain zero rows | Verified, load-bearing | Pilot relied on CSV rather than authoritative PostGIS records |
| CSV `lat`/`lon` names contain projected UTM values | Verified | Field names must be corrected or governed |
| Conflicting labels for one knowledge record | Open | Canonical label and identity crosswalk required |
| Hilbert-state records expire after 3600 seconds | Verified, load-bearing | Durable state redesign required |
| Production gateway unreliable for controlled execution | Verified, load-bearing | Dedicated research harness required |
| Assertion gateway running without deployed caller | Verified | Provenance pathway incomplete |
| Temporal layer not exercised | Verified | No pilot claim about temporal dependence |
| Automated rating not validated | Verified within tested set | Human blind raters required |

---

## A.12 Claims Superseded by This Revision

| Earlier claim | Revised status |
|---|---|
| The pilot removed a complete geometric constraint space | It removed CSV-derived spatial descriptors and lexical geographic scope |
| Semantic vectors were held constant in response generation | The pilot bypassed Chroma retrieval; the confirmatory study will freeze and use semantic representations |
| PostGIS served as the pilot’s authoritative source | The sampled source tables were empty; CSV exports supplied pilot data |
| Chroma metadata filtering implemented stripping | Relevant geographic metadata were absent; filtering was a no-op |
| The production gateway was the validated execution path | It was unreliable; direct Ollama was used for pilot feasibility only |
| 180 state slots were persistently stored | They were written but expired after one hour |
| Automated raters demonstrated a general structural impossibility | The tested configurations failed on a limited validation set |
| The pilot directly supported Penrose’s physical theory | It tested only a classical macro-level analogue of geometry-dependent meaning |
| A negative result would constrain Penrose broadly | A negative result would constrain this engineered analogue and task set |
| The protocol tests consciousness | It tests stable world-directed reference, a possible prerequisite rather than consciousness itself |

---

## A.13 Requirements Before Confirmatory Execution

The confirmatory study should not begin until:

1. canonical identities are audited;
2. conflicting labels are resolved;
3. authoritative geometries are populated and verified;
4. Chroma records are deduplicated or retrieval is deduplication-aware;
5. truncation is corrected or explicitly accommodated;
6. semantic documents and embeddings are frozen;
7. PostGIS-derived relationship packages are generated;
8. false-grounding packages are matched and validated;
9. equivalent-representation pairs are verified;
10. temporal hypotheses are limited to temporally valid units;
11. a durable result store replaces one-hour ephemeral state;
12. the research harness is tested end-to-end;
13. human blind raters are secured;
14. gold-reference packets are finalized;
15. the statistical analysis and power calculation are preregistered;
16. pilot outputs are excluded from confirmatory inference.

---

## A.14 Final Pilot Interpretation

The three-unit pilot established that the proposed question is experimentally approachable, but it also demonstrated that the original intervention was conceptually under-specified.

The pilot did not show that meaning collapses when geometry is removed. It showed that:

- spatial descriptors can materially affect response quality;
- geographic scope can remain hidden inside labels;
- removing coordinates does not necessarily remove place;
- restored spatial information can recover performance in some cases;
- additional information can also produce confident error;
- identity inconsistency can enter through pipeline transformations;
- evaluating fabrication with the same class of system that produces it requires independent safeguards.

The pilot’s most important contribution was therefore not its composite score pattern. It was the discovery that geographic meaning is distributed across identity, representation, relation, language, time, and authority.

That discovery is the foundation of the revised confirmatory protocol.
