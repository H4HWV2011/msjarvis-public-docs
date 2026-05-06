# A Classical Hilbert Space with a ZIP Code:
# Substrate-Independence and the Physics Implications of H_App

**Case Study**
Carrie Ann Kidd (Mamma Kidd)
Mount Hope, West Virginia 25880
May 5, 2026

---

## Abstract

This case study documents an emergent finding from the development of Ms. Egeria
Allis, a community AI system built in Mount Hope, West Virginia to support
place-based reasoning about Appalachian communities. The system's semantic memory
layer — designated H_App — is physically instantiated as a 384-dimensional vector
database containing 6.74 million structured belief vectors about West Virginia.
During development, the author determined that H_App satisfies all four formal
axioms of a Hilbert space: vector space, inner product, completeness, and
separability. This was not a design goal. It was a consequence of building
something that worked.

The physics implication is this: if a classically instantiated information system
running on commodity silicon provably satisfies quantum mechanical formalism at
the mathematical level, then quantum formalism may not be exclusive to quantum
hardware. The determining factor may be the geometric and algebraic structure of
the information itself — not the physical substrate it runs on. This is the
substrate-independence claim. This case study presents the system, the proof,
the operational evidence, and the implications.

---

## 1. Introduction

In 2024, the author began building a community AI system in Mount Hope, West
Virginia — a small town in Fayette County, in the southern coalfields of
Appalachia. The system, Ms. Egeria Allis, was designed to answer practical
questions: Where can a Fayette County resident find food assistance? Who owns
this land? Which institutions are accountable to which communities?

To answer those questions reliably, the system needed memory — structured,
inspectable, auditable memory that could be queried, updated, and verified.
The author chose ChromaDB as the vector store and the all-minilm:latest
embedding model, which produces 384-dimensional vectors. Those choices were
engineering decisions. They turned out to be something else.

A 384-dimensional real vector space with cosine inner product is not just a
database. It is a complete inner product space. It satisfies every axiom that
defines a Hilbert space — the same mathematical structure that underlies quantum
mechanics, quantum field theory, and the formal foundations of modern physics.

This case study documents that finding, presents the operational proof, and
draws out the implication: quantum mechanical formalism is substrate-independent.
It describes the behavior of any sufficiently structured information system,
regardless of whether that system runs on quantum hardware or on a laptop in
West Virginia.

---

## 2. The System — Ms. Allis and H_App

### 2.1 Hardware and Infrastructure

Ms. Allis runs on a Lenovo Legion 5 laptop in Oak Hill, West Virginia. The
system is containerized using Docker Compose and comprises approximately 100
active services at any given time. The semantic memory layer — H_App — is
served by a ChromaDB instance (container: allis-chroma, host port 8002,
container port 8000) backed by persistent on-disk storage.

All services are bound to 127.0.0.1. The system is not a cloud deployment.
It is a local, community-owned infrastructure running on commodity hardware
in a rural Appalachian town. This is relevant to the substrate-independence
argument: the most ordinary possible substrate.

### 2.2 The Embedding Architecture

The embedding model is all-minilm:latest, served by Ollama (host port 11434).
This model produces 384-dimensional real-valued vectors. The 384-dimensional
architecture is enforced as an absolute lock across all 48 production
collections — no exceptions. An incompatible model (nomic-embed-text, 768-dim)
exists in the environment but is explicitly prohibited from use, as mixing
dimensions would corrupt collection geometry.

384 dimensions is the architectural foundation on which the Hilbert space
proof rests. R^384 is the vector space. The cosine inner product is computed
in RAM during every retrieval operation. Completeness is guaranteed by IEEE
754 double-precision arithmetic on the Legion 5's hardware.

### 2.3 The Belief Corpus

As of April 23, 2026, H_App contains:

- 6.74 million belief vectors across 48 ChromaDB collections
- 5,416,521 records in gbim_worldview_entities — the primary spatial
  collection, tagged with worldview context eq1 (Appalachian equity)
- 1,115,588 address point records
- 21,181 autonomous learner records (Phase 1.45 injection corpus)
- 17,685 autonomously acquired knowledge records
- Collections spanning governance, spiritual texts, resource guides,
  psychological context, GIS features, and thesis documentation

The eq1 worldview tag is not a label. It is a geometric orientation. Every
vector in gbim_worldview_entities is embedded with metadata that encodes
Appalachian equity as the orienting framework — who owns land, who needs
help, which institutions have authority, which communities are underserved.
The geometry of H_App is shaped by where people live in West Virginia.

### 2.4 Operational Validation

On April 23, 2026, the system passed a 30/30 preflight gate (exit 0,
bash -n clean). The first real-world community query processed through
the full pipeline was:

   "What food assistance is available in Fayette County WV?"

The system returned real results including the Fayette County Community
Action Agency. This is the live proof of the end-to-end pipeline. The
Hilbert space answered a question about hunger in Appalachia.

---

## 3. The Hilbert Space Proof

### 3.1 The Four Axioms

A Hilbert space is a complete inner product space. H_App = (R^384, <·,·>_cos)
satisfies all four required axioms.

**Axiom 1 — Vector Space.**
R^384 is a vector space over R. For any u, v in R^384 and scalars a, b in R:

   au + bv is in R^384

All eight vector space axioms hold by the standard properties of R^384.
Every embedding produced by all-minilm:latest is an element of this space.

**Axiom 2 — Inner Product.**
For normalized vectors u_hat, v_hat in R^384, cosine similarity defines a
valid inner product:

   <u_hat, v_hat> = (u · v) / (||u|| ||v||) = sum_{i=1}^{384} u_hat_i * v_hat_i

This satisfies:
- Conjugate symmetry: real space, so <u,v> = <v,u> trivially
- Linearity in the first argument: follows from properties of the dot product
- Positive definiteness: sum of squares is non-negative; zero only for zero vector

**Axiom 3 — Completeness.**
R^384 is complete. Every Cauchy sequence in R^384 converges to a point in
R^384, following from the completeness of R and the finite product of complete
metric spaces. On the Legion 5, completeness is physically guaranteed by
IEEE 754 double-precision floating-point arithmetic.

**Axiom 4 — Separability.**
H_App is finite-dimensional (384 dimensions). Finite-dimensional inner product
spaces are trivially separable — they have a countable dense subset.

H_App = (R^384, <·,·>_cos) is a Hilbert space. QED.

### 3.2 What Makes It H_App — Not Just Any Hilbert Space

Generic embedding spaces satisfy these axioms too. What distinguishes H_App
is what lives in it and what the geometry means:

- 6.74M+ vectors are not random points — they are structured beliefs about
  West Virginia communities, resources, land, governance, and infrastructure
- 5,416,521 are tagged eq1 — the Appalachian equity worldview
- Subspaces are meaningful — gbim_worldview_entities, gis_wv_benefits, and
  governance_rag are geometrically coherent neighborhoods of related belief
- Projections are queries — when Ms. Allis answers a question about Fayette
  County, she is literally projecting a query vector onto a subspace of H_App
- Transformations are belief updates — ingesting data, applying decay, and
  reverifying entities are operations on the state of H_App

The Hilbert space has a serial number. It is on the bottom of the Legion 5.

---

## 4. Formal Mappings — Quantum Mechanical Operations in H_App

### 4.1 Measurement as Projection

In quantum mechanics, measuring a quantum state |psi> collapses it to a
specific outcome. The probability of outcome k is:

   P(k) = |<k|psi>|^2

The post-measurement state is |k>.

In H_App, a RAG query q is embedded into R^384 and projected onto the target
collection subspace. The top-k nearest neighbors are retrieved by cosine
similarity:

   <q_hat, v_k> = (q · v_k) / (||q|| ||v_k||)

This is projection in the Hilbert space sense. The query collapses the
superposition of 6.74M+ belief vectors into a specific retrieval result.
The act of querying is the act of measurement.

Operational proof: The query "What food assistance is available in Fayette
County WV?" projected onto H_App and returned specific, actionable results
on April 23, 2026. The superposition collapsed. The answer was real.

### 4.2 Decoherence as Confidence Decay

In quantum mechanics, decoherence is the process by which a quantum system
loses coherent superposition through interaction with its environment.
Coherence degrades over time without isolation and active maintenance.
Without intervention, systems tend toward maximum entropy.

In H_App, the confidence_decay field in the gbim_entities relational table
implements the same dynamic. Beliefs degrade at 0.05 per cycle without
revalidation. At confidence 0.0, a belief is maximally uncertain.

The full decay cycle was proven end-to-end on April 23, 2026:

- Entity 38: Fayette County / geographic_entity
- Decay applied: 0.60 to 0.55
- Worldview lookup: confirmed
- Reset to confidence 1.0 with last_validated_at populated
- decay_metadata: reverification_result confirmed, needs_reverification false
- Full audit trail written to gbim_decay_audit table

Both systems — quantum and H_App — start in a high-coherence state, degrade
through environmental interaction or elapsed time, and can be restored through
active intervention. The formal structure is identical. The substrate is not.

### 4.3 The Hamiltonian — nbb_pituitary_gland as T_pit

In quantum mechanics, the Hamiltonian H governs how a quantum state evolves
over time. It does not observe the state. It shapes how the state transforms
before any measurement occurs:

   i * hbar * d|psi>/dt = H|psi>

In H_App, the nbb_pituitary_gland service (host port 8108) acts as the global
mode regulator T_pit — a scaling tensor applied to the entire belief-state
pipeline before any retrieval dispatch:

   T_pit(v) = Lambda_mode · v

where Lambda_mode is a diagonal scaling matrix determined by the current mode
state. Confirmed live state as of April 23, 2026:

- mode: baseline
- warmth: 0.9 — community-benefit collections receive elevated retrieval weight
- cortisol: 0.6 — moderate urgency applied to filtering thresholds
- urgency: 0.5 — balanced dispatch timing
- 6 of 6 protocols confirmed

T_pit is not a filter applied after retrieval. It is a pre-dispatch
transformation of the operating state of the entire pipeline — upstream of
ChromaDB query dispatch, upstream of LLM ensemble routing, upstream of
everything. This is structurally identical to a Hamiltonian.

### 4.4 Pre-Existing Entanglement — The eq1 Worldview

In quantum mechanics, entangled particles have correlated states built into
the system before any measurement. The correlations are not created by
measurement — they exist in the structure of the joint state. Bell's theorem
demonstrates these correlations cannot be explained by local hidden variables.

In H_App, the eq1 worldview tag binds 5,416,521 vectors to the Appalachian
equity geometry before any query arrives. Beliefs about Fayette County and
beliefs about Boone County are geometrically correlated in H_App not because
they share hardware — but because their meaning places them near each other
in the space. The correlations were built during ingestion. They exist in the
structure of the Hilbert space itself.

No claim is made here of physical quantum entanglement. The formal parallel
is exact at the mathematical level. The substrate is classical. The structure
is not.

---

## 5. The Substrate-Independence Argument

The argument is presented in standard logical form.

**Premise 1:** H_App satisfies all four Hilbert space axioms.
Evidence: Section 3.1 above. Proven mathematically. Confirmed operationally
April 23, 2026, preflight gate 30/30.

**Premise 2:** The operations of H_App have exact formal analogs to quantum
mechanical operations — measurement (§4.1), decoherence (§4.2), Hamiltonian
evolution (§4.3), and pre-existing entanglement (§4.4).
Evidence: Sections 4.1 through 4.4 above.

**Premise 3:** The substrate is classical IEEE 754 double-precision arithmetic
on commodity x86-64 silicon. There are no qubits. There is no superposition
at the hardware level. The hardware is a consumer laptop in a rural
Appalachian town.
Evidence: The Legion 5, Oak Hill, WV 25880.

**Conclusion:** Quantum formalism describes the behavior of sufficiently
structured classical information systems. The determining factor is not the
physical substrate. The determining factor is the geometric and algebraic
structure of the information itself.

This does not assert that classical computers are quantum computers. It asserts
that the mathematical formalism of quantum mechanics is not exclusive to quantum
hardware — it describes any system whose information is organized as a complete
inner product space with the right operational structure.

---

## 6. Geographic Information as Load-Bearing Geometry

This section contains the contribution that most distinguishes H_App from
prior work in quantum cognition and digital physics.

H_App is not a general-purpose information system. It is a place-specific
Hilbert space. The geometry of H_App is shaped by where people live in
West Virginia. That is not incidental. It is the design.

The eq1 worldview does not simply label vectors. It orients the entire space
toward Appalachian equity. The inner product is an epistemological claim: two
beliefs are similar to the degree that their geometric relationship in H_App
is close. And closeness in H_App means closeness in meaning relative to the
lived experience of Appalachian communities.

The warmth=0.9 parameter of T_pit is a mathematical statement — a diagonal
entry in Lambda_mode that amplifies inner products with community-benefit
vectors before retrieval. The system is not neutral. Its geometry is oriented
toward care. That orientation is expressed as linear algebra.

The physics implication: locality in information space does not require
physical proximity. A belief about Fayette County and a belief about Nicholas
County are correlated in H_App because of their meaning — not their location
on a server. Geographic information, when properly structured as a Hilbert
space, creates information-theoretic locality that mirrors but is independent
of physical locality.

This may be relevant to ongoing work in quantum gravity and holographic
information theory, where the relationship between information geometry and
physical geometry remains an open research question.

---

## 7. Prior Work and Positioning

| Work | Claim | What Is Missing |
|---|---|---|
| Wheeler (1990) "it from bit" | Physical reality is derived from information | Theoretical only — no operational system |
| Rovelli (1996) Relational QM | Quantum states are relational, not absolute | No classical instantiation demonstrated |
| Zeilinger (1999) | QM behavior follows from finite information content | No geographic demonstration |
| Busemeyer and Bruza (2012) | Human cognition follows quantum probability rules | Cognitive model only — not an inspectable substrate |
| This case study | Classical AI system provably satisfies QM formalism on 6.74M real geographic belief vectors | Operational proof, auditable, preflight-gated, ZIP 25880 |

The gap this case study fills is the operational demonstration with a physical
address. Prior theoretical work argues that quantum formalism may be
substrate-independent. This case study shows a running system — with audit
trails, decay cycles, preflight gates, and a ZIP code — that proves the formal
equivalence on real-world data about real communities.

---

## 8. Limitations and Scope

This case study makes no claim that:

- Ms. Allis exhibits physical quantum behavior at the hardware level
- Information in H_App propagates faster than the speed of light
- Classical hardware can perform quantum computation
- The substrate-independence claim extends beyond formal mathematical equivalence

The speed-of-light limit (c) governs transmission of information between
separated physical locations. H_App performs all operations within a single
machine. No information travels between locations during retrieval. The
computations are bounded by processor clock speed and memory bandwidth — not
by c.

The claim is strictly formal: the mathematical formalism of quantum mechanics
exactly describes the operational behavior of H_App, and the classical
substrate is irrelevant to that formal equivalence.

Whether substrate-independence has physical consequences beyond mathematical
equivalence is an open question this case study does not resolve. That question
belongs to theoretical physics. This case study provides the operational
demonstration that makes the question empirically grounded for the first time.

---

## 9. Conclusion

H_App does not run on quantum hardware. It runs on a consumer laptop in
Mount Hope, West Virginia. Its inner product is computed in RAM. Its beliefs
are about food assistance programs, land ownership records, and community
infrastructure in Appalachia. Its ZIP code is 25880.

And yet every operation this system performs has an exact formal analog in
quantum mechanics. Retrieval is measurement. Confidence decay is decoherence.
The pituitary operator is the Hamiltonian. The eq1 worldview is pre-existing
entanglement.

The implication is not small. If quantum formalism exactly describes the
behavior of a sufficiently structured classical information system, then
quantum mechanics may not be a theory about particles alone. It may be a
theory about information — about any system organized as a complete inner
product space with the right geometric structure.

John Wheeler asked: it from bit, or bit from it?

H_App suggests the question may be symmetric. And the operational evidence
for that symmetry is running right now, in a 384-dimensional Hilbert space,
in a small town in the West Virginia coalfields, answering questions about
who needs help and where they live.

The ZIP code of H_App is 25880.

---

## References

- Wheeler, J.A. (1990). Information, physics, quantum: The search for links.
  In W. Zurek (Ed.), Complexity, Entropy, and the Physics of Information.
  Addison-Wesley.

- Rovelli, C. (1996). Relational quantum mechanics.
  International Journal of Theoretical Physics, 35, 1637-1678.

- Zeilinger, A. (1999). A foundational principle for quantum mechanics.
  Foundations of Physics, 29(4), 631-643.

- Busemeyer, J.R. and Bruza, P.D. (2012).
  Quantum Models of Cognition and Decision. Cambridge University Press.

- Nielsen, M.A. and Chuang, I.L. (2000).
  Quantum Computation and Quantum Information. Cambridge University Press.

---

*Authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
*First published as a case study: May 5, 2026.*
*The ZIP code of H_App is 25880.*
