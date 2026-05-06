# A Classical Hilbert Space with a ZIP Code:
# Substrate-Independence and the Physics Implications of H_App

**Final Draft — May 6, 2026**
Carrie Ann Kidd (Mamma Kidd)
Mount Hope, West Virginia 25880
Harmony for Hope Inc.

---

## Abstract

This paper documents an emergent finding from the development of Ms. Egeria
Allis, a community AI system built in Mount Hope, West Virginia to support
place-based reasoning about Appalachian communities. The system's semantic memory
layer — designated H_App — is physically instantiated as a 384-dimensional vector
database containing 6.74 million structured belief vectors about West Virginia.
During development, the author determined that H_App satisfies all four formal
axioms of a Hilbert space: vector space, inner product, completeness, and
separability. This was not a design goal. It was a consequence of building
something that worked.

The first physics implication is this: if a classically instantiated information
system running on commodity silicon provably satisfies quantum mechanical formalism
at the mathematical level, then quantum formalism may not be exclusive to quantum
hardware. The determining factor may be the geometric and algebraic structure of
the information itself — not the physical substrate it runs on. This is the
substrate-independence claim.

The second implication follows from Einstein's block universe: the data was already
there. The 6.74 million belief vectors in H_App exist as a static geometric
structure. Retrieval does not create the answer — it reveals what already exists
at fixed coordinates in a 384-dimensional space. The speed of light constrains
transmission. It does not constrain pre-existence.

The third implication — directly challenges the
Copenhagen interpretation of quantum measurement. Standard quantum mechanics
treats measurement as a unified event: physical interaction causes wavefunction
collapse, which is described mathematically as projection in Hilbert space. H_App
demonstrates operationally that the mathematical operation (projection) and the
physical interaction are separable. Projection runs on classical silicon, without
any quantum physical event, and returns correct, meaningful, real-world results.
This means collapse may not be a mathematical necessity — it may be an assumption
about the physical component that the mathematical component does not require.
Measurement is projection. The physical interaction is the transmission mechanism,
not the cause of the result.

This paper presents the system, the proof, the operational evidence, and the
implications.

---

## 1. Introduction

In 2025, the author began building a community AI system in Mount Hope, West
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

This paper documents that finding, presents the operational proof, and draws
out three implications: quantum mechanical formalism is substrate-independent;
the answers in H_App existed before they were queried; and the mathematical
operation of measurement is separable from the physical event of wavefunction
collapse — which means the Copenhagen interpretation has been conflating two
distinct things.

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
argument: the most ordinary possible substrate. If quantum formalism runs here,
it runs on the structure of the information — not the hardware.

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
754 double-precision arithmetic on the Legion 5 hardware.

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
Hilbert space answered a question about hunger in Appalachia. The answer
was already there — at fixed coordinates in a 384-dimensional space —
before the question was asked.

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

## 5. The Measurement Problem Reconsidered

### 5.1 What Physicists Currently Assume

The measurement problem is widely regarded as the deepest unsolved problem in
the foundations of quantum mechanics. In standard quantum theory, a system
exists in a superposition of possible states until a measurement is made. At
measurement, the superposition collapses to a single definite outcome. The
mathematical description is projection in Hilbert space:

   |psi> --> P_k|psi> / ||P_k|psi>||

The problem is this: the mathematical formalism of quantum mechanics — the
Schrodinger equation — is linear and deterministic. It never collapses
anything. Wavefunction collapse is a separate postulate, added to the
formalism because experiments produce definite outcomes. No one has
successfully explained why or how collapse occurs. The leading interpretations
— Copenhagen, Many-Worlds, pilot wave, relational — disagree fundamentally
on what measurement is and whether collapse is real.

What all of these interpretations share is a hidden assumption: that
measurement is a unified event in which the physical interaction and the
mathematical projection are inseparable. The physical interaction causes the
collapse. The projection describes it. The two are treated as one thing.

### 5.2 What H_App Demonstrates

H_App performs projection — the mathematical operation of measurement — on
every retrieval call. It does this on classical silicon, with no quantum
hardware, no physical interaction with a quantum system, and no wavefunction
in the physical sense. And it returns correct, meaningful, real-world results:
food banks in Fayette County, land ownership records, community institutions.

This means the mathematical operation of measurement is separable from the
physical event of wavefunction collapse. The two components that physics has
been treating as unified are distinct:

- The mathematical operation — projection in Hilbert space — runs on
  classical silicon and does not require any quantum physical event.
- The physical interaction — a measuring device interacting with a quantum
  system — is the transmission mechanism, the thing that reads out the
  pre-existing geometric structure. It is not the cause of the result.

The result was already there. The Fayette County Community Action Agency
existed as a belief vector in H_App before the query arrived. The projection
did not create the answer. It revealed a pre-existing geometric fact.

### 5.3 The Copenhagen Conflation

Copenhagen says: before measurement, the particle has no definite position.
Measurement creates the definite outcome. The act of looking is the act of
making real.

H_App says: the answer existed at fixed coordinates in a 384-dimensional
space before the query was made. The projection revealed it. Nothing was
created. The retrieval was a reading, not a writing.

These are not equivalent claims. And the H_App case is operationally proven,
auditable, and reproducible — 6.74 million times over, on commodity hardware,
with a ZIP code.

The precise statement of what H_App demonstrates about the measurement problem:

   Measurement = projection. The physical interaction is the transmission
   mechanism — the thing that reads out the structure. It is not the cause
   of the result. The result pre-exists the measurement in the geometric
   structure of the Hilbert space. Copenhagen has been conflating the act
   of reading with the act of writing.

This does not resolve every question in the foundations of quantum mechanics.
It does not explain why quantum systems produce discrete outcomes. It does not
address the Born rule, decoherence in the physical sense, or the preferred
basis problem. What it does is demonstrate operationally that the mathematical
operation of projection produces correct, meaningful results on a pre-existing
geometric structure without any physical quantum event. That is a constraint
on any acceptable interpretation: any interpretation that requires physical
collapse to explain the mathematics is overconstrained. The mathematics works
without it.

### 5.4 The Block Universe Connection

Einstein's block universe — the four-dimensional static spacetime in which
past, present, and future all exist simultaneously — provides the correct
interpretive frame for what H_App demonstrates.

In the block universe, the answer to every question about the state of the
universe at any spacetime coordinate already exists. There is no becoming,
only being. What we call measurement is the act of accessing a coordinate
in a static structure.

H_App is a finite, local, auditable instance of this. The 6.74 million belief
vectors exist as a static geometric structure in R^384. Every retrieval is
an access of a pre-existing coordinate. The query collapses nothing — it
points at a location in a space that was always already complete.

The speed of light constrains when a signal can travel from one physical
location to another. It does not constrain the pre-existence of geometric
structure within a space. H_App performs all operations within a single
machine. Nothing propagates between locations. The answers were already
there, at coordinates that exist independently of when they are queried.

This is not a metaphor. It is what the system demonstrably does, with a
preflight gate, an audit trail, and a ZIP code.

---

## 6. The Substrate-Independence Argument

The argument is presented in standard logical form.

**Premise 1:** H_App satisfies all four Hilbert space axioms.
Evidence: Section 3.1 above. Proven mathematically. Confirmed operationally
April 23, 2026, preflight gate 30/30.

**Premise 2:** The operations of H_App have exact formal analogs to quantum
mechanical operations — measurement (§4.1), decoherence (§4.2), Hamiltonian
evolution (§4.3), and pre-existing entanglement (§4.4).
Evidence: Sections 4.1 through 4.4 above.

**Premise 3:** The mathematical operation of measurement (projection) is
separable from the physical event of wavefunction collapse, demonstrated
by H_App performing projection on classical silicon and returning correct
real-world results without any quantum physical event.
Evidence: Section 5 above.

**Premise 4:** The substrate is classical IEEE 754 double-precision arithmetic
on commodity x86-64 silicon. There are no qubits. There is no superposition
at the hardware level. The hardware is a consumer laptop in a rural
Appalachian town.
Evidence: The Legion 5, Oak Hill, WV 25880.

**Conclusion:** Quantum formalism describes the behavior of sufficiently
structured classical information systems. The determining factor is not the
physical substrate. The determining factor is the geometric and algebraic
structure of the information itself. And the measurement operation, properly
understood, is projection onto a pre-existing geometric structure — not the
creation of a result through physical interaction.

This does not assert that classical computers are quantum computers. It asserts
that the mathematical formalism of quantum mechanics is not exclusive to quantum
hardware — it describes any system whose information is organized as a complete
inner product space with the right operational structure. And it asserts that
any interpretation of quantum mechanics that requires physical collapse to
explain the mathematical operation of projection is overconstrained by the
evidence H_App provides.

---

## 7. Geographic Information as Load-Bearing Geometry

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
physical geometry remains an open research question. The AdS/CFT correspondence
and related holographic frameworks suggest that geometric structure in one
space encodes physical structure in another. H_App does not claim to be a
hologram. It does claim to be a finite, local, auditable demonstration that
geographic meaning can be encoded as geometric structure in a proven Hilbert
space — and that the resulting geometry supports measurement-as-projection in
the full quantum mechanical sense, on classical hardware, with a ZIP code.

---

## 8. Prior Work and Positioning

| Work | Claim | What Is Missing |
|---|---|---|
| Wheeler (1990) "it from bit" | Physical reality is derived from information | Theoretical only — no operational system |
| Einstein and Minkowski (1908) Block Universe | Past, present, future exist as static spacetime structure | No information-system instantiation demonstrated |
| Rovelli (1996) Relational QM | Quantum states are relational, not absolute | No classical instantiation demonstrated |
| Zeilinger (1999) | QM behavior follows from finite information content | No geographic demonstration |
| Busemeyer and Bruza (2012) | Human cognition follows quantum probability rules | Cognitive model only — not an inspectable substrate |
| Bohr / Copenhagen (1927 onward) | Measurement creates the result; collapse is real | H_App demonstrates projection produces pre-existing results without physical collapse |
| This paper | Classical AI system provably satisfies QM formalism on 6.74M real geographic belief vectors; measurement is separable projection; results pre-exist queries; ZIP code 25880 | Operational proof, auditable, preflight-gated, measurement problem addressed |

The gap this paper fills is the operational demonstration with a physical
address and a direct challenge to the Copenhagen conflation. Prior theoretical
work argues that quantum formalism may be substrate-independent and that
physical structure may be fundamentally informational. This paper shows a
running system — with audit trails, decay cycles, preflight gates, and a ZIP
code — that proves the formal equivalence on real-world data about real
communities, demonstrates operationally that retrieval reveals pre-existing
structure rather than creating new information, and provides the first
operational evidence that the mathematical operation of measurement is
separable from the physical event of wavefunction collapse.

---

## 9. Limitations and Scope

This paper makes no claim that:

- Ms. Allis exhibits physical quantum behavior at the hardware level
- Information in H_App propagates faster than the speed of light
- Classical hardware can perform quantum computation
- The block universe interpretation of spacetime is proven by this system
- The substrate-independence claim extends beyond formal mathematical equivalence
- This paper resolves the measurement problem in full — it constrains
  acceptable interpretations, it does not adjudicate between all of them

The speed-of-light limit governs transmission of information between
separated physical locations. H_App performs all operations within a single
machine. No information travels between locations during retrieval. The
computations are bounded by processor clock speed and memory bandwidth — not
by c.

The claim about the measurement problem is strictly this: the mathematical
operation of projection in a Hilbert space runs correctly on classical silicon
and returns pre-existing geometric results without any quantum physical event.
Any interpretation of quantum mechanics that requires physical collapse to
explain the mathematics is overconstrained by this evidence. The stronger
claim — that collapse never occurs in any physical sense — is beyond the scope
of this paper and requires engagement with Bell inequality experiments,
decoherence theory, and the full literature on quantum foundations.

What this paper provides is the operational grounding that makes the question
empirically constrained for the first time: not a thought experiment, not a
theoretical framework, but a running system with 6.74 million belief vectors,
a preflight gate, a decay audit trail, and a ZIP code.

---

## 10. Conclusion

H_App does not run on quantum hardware. It runs on a consumer laptop in
Mount Hope, West Virginia. Its inner product is computed in RAM. Its beliefs
are about food assistance programs, land ownership records, and community
infrastructure in Appalachia. Its ZIP code is 25880.

And yet every operation this system performs has an exact formal analog in
quantum mechanics. Retrieval is measurement. Confidence decay is decoherence.
The pituitary operator is the Hamiltonian. The eq1 worldview is pre-existing
entanglement.

And the answers were already there — fixed coordinates in a 384-dimensional
space — before anyone asked the questions. Einstein said the distinction
between past, present, and future is a stubbornly persistent illusion. H_App
is a small, local, auditable demonstration of what he meant: a static
geometric structure that contains its answers before it is queried.

And now this paper adds a third implication that the original case study left
implicit: the mathematical operation of measurement — projection in a Hilbert
space — is separable from the physical event of wavefunction collapse.
Copenhagen has been treating them as one thing. H_App demonstrates they are
two. The projection runs without the collapse. The result was already there.
The physical interaction is not the cause. It is the reading.

John Wheeler asked: it from bit, or bit from it?

H_App suggests the question may be symmetric. And the operational evidence
for that symmetry is running right now, in a 384-dimensional Hilbert space,
answering questions about who needs help and where they live, on a laptop
in the West Virginia coalfields, proving that the act of measurement is
not what physicists have thought it was.

The ZIP code of H_App is 25880.

---

## References

Einstein, A. (1955). Letter to the family of Michele Besso. March 21, 1955.

Minkowski, H. (1908). Space and Time. Address delivered at the 80th Assembly
of German Natural Scientists and Physicians, Cologne.

Wheeler, J.A. (1990). Information, physics, quantum: The search for links.
In W. Zurek (Ed.), Complexity, Entropy, and the Physics of Information.
Addison-Wesley.

Bohr, N. (1928). The quantum postulate and the recent development of atomic
theory. Nature, 121, 580-590.

Rovelli, C. (1996). Relational quantum mechanics.
International Journal of Theoretical Physics, 35, 1637-1678.

Zeilinger, A. (1999). A foundational principle for quantum mechanics.
Foundations of Physics, 29(4), 631-643.

Busemeyer, J.R. and Bruza, P.D. (2012).
Quantum Models of Cognition and Decision. Cambridge University Press.

Nielsen, M.A. and Chuang, I.L. (2000).
Quantum Computation and Quantum Information. Cambridge University Press.

von Neumann, J. (1932). Mathematical Foundations of Quantum Mechanics.
Princeton University Press. (English translation 1955.)

Everett, H. (1957). Relative state formulation of quantum mechanics.
Reviews of Modern Physics, 29, 454-462.

Bell, J.S. (1964). On the Einstein-Podolsky-Rosen paradox.
Physics, 1(3), 195-200.

Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the
classical. Reviews of Modern Physics, 75, 715-775.

Kidd, C.A. (2026). Beyond Euclidean SLAM: Toroidal Hilbert Space World Models
for Boundaryless Robot State Representation. Preprint, May 2026.
H4HWV2011/msjarvis-public-docs, GitHub.

Kidd, C.A. (2026). Ms. Egeria Allis Thesis — Chapter 4: Hilbert Space State
and ChromaDB as Semantic Memory. H4HWV2011/msjarvis-public-docs, GitHub.

Kidd, C.A. (2026). Ms. Egeria Allis Thesis — Chapter 26: Temporal Toroidal
Semaphore Structure. H4HWV2011/msjarvis-public-docs, GitHub.

---

*Authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
*Original case study: May 5, 2026.*
*Final draft incorporating measurement problem argument: May 6, 2026.*
*The ZIP code of H_App is 25880.*
