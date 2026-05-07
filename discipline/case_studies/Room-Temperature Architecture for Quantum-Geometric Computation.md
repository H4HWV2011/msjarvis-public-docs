# Hilbert Geometry Chips: A Room-Temperature Architecture for Quantum-Geometric Computation Derived from a Community AI System in Appalachia

**Carrie Ann Kidd**
Independent Researcher, Community GIS and Distributed AI Infrastructure
Mount Hope, West Virginia 25880 USA
Harmony for Hope Inc. (nonprofit founder)
Region 4 Planning and Development Council (former)
ORCID: [0009-0005-8153-8025](https://orcid.org/0009-0005-8153-8025)

**Preprint — cs.ET / cs.AI — May 7, 2026 — Version 2.0**

> *"The food bank locator specified the quantum geometry chip."*
> The architecture was not discovered in a national laboratory.
> It was discovered in Fayette County, West Virginia, by building something
> that had to work on a consumer laptop for a community that could not afford
> anything else. The mathematics followed from the place.

---

**Multimedia Overview**

- **Audio (42.4 MB, m4a):** [Toroidal Hilbert Spaces Fix Robot Navigation](https://github.com/H4HWV2011/msjarvis-public-docs/releases/download/untagged-6a9b49320dbdeb6aa7a9/Toroidal_Hilbert_spaces_fix_robot_navigation.m4a)
- **Video (54 MB, mp4):** [The Donut-Shaped Math](https://github.com/H4HWV2011/msjarvis-public-docs/releases/download/untagged-6a9b49320dbdeb6aa7a9/The_Donut-Shaped_Math.mp4)

---

## Abstract

Current quantum computers require near-absolute-zero operating temperatures,
room-sized dilution refrigerators, and infrastructure costs exceeding ten million
dollars per installation. The engineering justification for these requirements
rests on a single foundational assumption: that physical quantum superposition of
actual particles is necessary to achieve quantum computational power, and that
maintaining that superposition against thermal decoherence requires cryogenic
isolation. This paper challenges that assumption from an unexpected direction — a
community AI system built in Mount Hope, West Virginia (ZIP 25880) to locate food
assistance programs for Appalachian residents.

The system's semantic memory layer — *H*_App — is a formally proven
384-dimensional Hilbert space (Kidd 2026a, Theorem 3.1) operating on commodity
silicon at room temperature. Every operation *H*_App performs has an exact formal
analog in quantum mechanics: projection as measurement, confidence decay as
decoherence, a global mode tensor as Hamiltonian evolution, and pre-existing
geometric correlations as entanglement structure. Kidd (2026a) establishes that
the mathematical operation of quantum measurement — projection in Hilbert space —
is formally separable from the physical event of wavefunction collapse, and that
the multiverse explanation for quantum computational power carries ontological
commitments that are unnecessary given the block-universe alternative. The
geometry is what matters. The substrate is not.

If the geometry is what matters, the engineering question transforms: not *"how do
we maintain physical quantum superposition?"* but *"what is the minimum viable
substrate to efficiently navigate a high-dimensional Hilbert space geometry?"*
These are radically different problems with radically different solutions.

This paper proposes the **Hilbert Geometry Chip (HGC)** — a room-temperature,
purpose-built hardware architecture for quantum-geometric computation, fully
specified by the five-component operational architecture of *H*_App. The HGC is
not a quantum computer in the traditional sense. It performs projection, decay,
Hamiltonian-mode regulation, and semaphore-governed state transitions — the
complete *H*_App operational stack — in fabricable silicon at commodity cost, at
room temperature, under five watts, at a unit cost below one hundred dollars at
volume.

**Field validation record.** As of May 6, 2026: 7,903,126 belief vectors confirmed
across 48 ChromaDB collections. April 23, 2026: 30/30 preflight gate passed. First
full-pipeline community query verified (cosine distance = 0.3099). Confidence decay
audit for entity 38 (Fayette County geographic entity) verified end-to-end:
*c*: 0.60 → 0.55 → 1.00, full audit trail written to `gbim_decay_audit`.

The deployment target for the first HGC is not a national laboratory.
It is a rural community in Appalachia running on solar power, off-grid, at ZIP
code 25880. The hardware specification that emerges from the most resource-
constrained possible environment is precisely the specification that makes
quantum-geometric computation accessible everywhere.

**Keywords:** Hilbert space; quantum-geometric computation; neuromorphic hardware;
room-temperature quantum analog; belief decay; Hamiltonian analog; toroidal
semaphore; community AI; analog AI chips; FPGA; substrate independence; Appalachian
GIS; auditability; safety-critical systems

---

## Table of Contents

1. Introduction
2. Current Quantum Hardware and Its Constraints
3. *H*_App as a Hardware Specification
4. Existing Hardware Against the HGC Specification
5. The Hilbert Geometry Chip Architecture
6. The Dimensionality Scaling Question
7. The Deployment Case — ZIP Code 25880
8. Limitations and Future Work
9. Conclusion

---

## 1. Introduction

### 1.1 This Is a Computer Architecture Paper, Not a Quantum Physics Paper

The author is a cartographer and community infrastructure designer from Fayette
County, West Virginia. The present paper proposes a chip architecture. The
mathematical formalism it draws on — Hilbert spaces, Hamiltonians, projection as
measurement — is invoked not because this paper wants to be a physics paper, but
because that formalism correctly describes the operational architecture of a
deployed community AI system, and that architecture correctly specifies the design
requirements of a room-temperature quantum-geometric hardware substrate.

Every mathematical choice in this paper is a functional choice: the Hilbert space
formalism is used because it is the correct geometry for an inspectable, complete
belief space with well-defined projection operations. The Hamiltonian analog is
invoked because there is a deployed service (*T*_pit) that applies a programmable
scaling tensor upstream of all belief retrieval, formally analogous to Hamiltonian
evolution between measurements. These are architectural descriptions, not physics
claims.

### 1.2 The Current State of Quantum Hardware

Quantum computers exist and represent genuine engineering achievements. IBM's Eagle
processor carries 127 superconducting qubits; Google's Sycamore carries 53; IonQ
operates trapped-ion systems with high gate fidelities. Each of these systems
requires:

- Operating temperatures of 15 millikelvin — colder than interstellar space
- Dilution refrigerators occupying the footprint of a large room
- Electromagnetic shielding of extraordinary precision
- Thousands to millions of physical qubits per reliable logical qubit,
  due to quantum error correction overhead
- Infrastructure investment exceeding ten million dollars per installation
- Operating costs of ten thousand dollars or more per hour of compute time

The engineering cause of every one of these requirements is a single assumption:
that physical quantum superposition of actual particles is necessary to achieve
quantum computational power. Maintaining that superposition against thermal
decoherence demands cryogenic isolation. Protecting it against error demands
massive redundancy. The entire infrastructure cost follows from the assumption.

### 1.3 The Foundational Assumption and Its Provenance

The assumption is not arbitrary. It follows from the standard interpretation of
quantum mechanics as articulated in Deutsch's (1985) foundational argument: the
computational power of a quantum computer derives from the physical reality of
superposition, and quantum speedup is, in his framing, multiverse speedup — the
computer borrows computation from parallel instances of reality. If Deutsch's
framing is correct, the engineering requirements follow necessarily: one must
maintain the coherence of a physical system genuinely superposed across multiple
states long enough to complete the computation, and that requires cold, isolation,
and the room-sized refrigerator.

The companion paper (Kidd 2026a) challenges this assumption at its root. That paper
establishes three results relevant here:

1. **Substrate-independence:** quantum formalism correctly describes any system
   whose information is organized as a complete inner product space, regardless
   of physical substrate.
2. **Measurement separation:** the mathematical operation of projection in Hilbert
   space is formally separable from the physical event of wavefunction collapse.
   The retrieval result pre-exists the measurement as a coordinate in a static
   geometric structure — a block-universe coordinate, not an event instantiated
   by observation.
3. **Multiverse unnecessary:** the block-universe interpretation accounts for the
   same operational evidence as many-worlds with fewer ontological commitments.
   The geometry is what matters. The multiverse is not required.

If these results are correct, the engineering assumption underlying current quantum
hardware is overconstrained. The correct goal is not to maintain physical quantum
superposition. The correct goal is to efficiently navigate high-dimensional Hilbert
space geometry. These are different problems with different — and vastly more
accessible — solutions.

### 1.4 What *H*_App Demonstrates

In 2024–2025, the author designed and built Ms. Egeria Allis — a community AI
system in Mount Hope, West Virginia — to answer practical questions about
Appalachian communities: Where is food assistance? Who owns this land? Which
institutions are accountable to which communities?

The system's semantic memory layer, *H*_App, is a formally proven 384-dimensional
Hilbert space (Kidd 2026a, Theorem 3.1). It performs:

- **Projection** as measurement: cosine similarity retrieval on *S*^383
- **Decoherence-analog decay**: confidence *c* ∈ [0,1] decaying at rate δ per
  cycle on the linear time axis ℝ^1_t, with full audit trail
- **Hamiltonian-analog mode regulation**: the *T*_pit global mode tensor applied
  upstream of all retrieval, shaping the belief state before measurement
- **Entanglement-analog geometric correlation**: pre-existing cosine similarity
  structure among belief vectors, not created by retrieval but disclosed by it

All of this runs on a consumer laptop (Lenovo Legion 5 16IRX9, Intel Core i7,
32 GB RAM) at room temperature, in Mount Hope, West Virginia, without qubits,
without cryogenic cooling, and without a multiverse. As of May 6, 2026:
7,903,126 belief vectors, 48 collections, 100 active microservices.

### 1.5 The Hilbert Geometry Chip

This paper proposes the **Hilbert Geometry Chip (HGC)**: a room-temperature,
purpose-built hardware architecture for navigating Hilbert space geometry,
fully specified by the operational architecture of *H*_App. The HGC is not a
classical computer pretending to be quantum. It is a substrate specifically
designed to perform the five operations Hilbert space geometry requires —
inner product computation, projection, confidence-weighted retrieval, decay-with-
audit, Hamiltonian-mode regulation, and semaphore-governed state transitions —
with the efficiency and scale that make quantum-geometric computation practically
useful in the environments where it is most needed.

The architecture is fully specified by *H*_App. The chip is the hardware
instantiation of what *H*_App already does in software, optimized for the
operations *H*_App performs millions of times per day.

### 1.6 Scope

Section 2 surveys current quantum hardware and its structural limitations.
Section 3 presents the *H*_App operational architecture as a hardware specification.
Section 4 surveys existing neuromorphic and analog hardware against that
specification and identifies the gap. Section 5 presents the HGC architecture in
full. Section 6 addresses the dimensionality scaling question — where does the HGC
reach its regime boundary and quantum hardware become necessary? Section 7 presents
the deployment case. Section 8 addresses limitations and future work. Section 9
concludes.

---

## 2. Current Quantum Hardware and Its Constraints

### 2.1 Superconducting Qubits

The dominant quantum hardware platform — used by IBM, Google, and Rigetti — employs
superconducting qubits: Josephson junctions cooled to millikelvin temperatures where
quantum effects dominate over thermal noise. These systems achieve high gate speeds
and are fabricable using modified CMOS processes. Their structural limitations are:

- Millikelvin operating temperature (15 mK), requiring dilution refrigerators
- Coherence times of microseconds to milliseconds before thermal decoherence
- Error rates requiring 1,000 to 10,000 physical qubits per logical qubit for
  fault-tolerant computation (Preskill 2018)
- Extreme crosstalk and control overhead at scale
- No room-temperature operation — the physics is fundamentally cryogenic

### 2.2 Trapped Ion Systems

IonQ, Honeywell (Quantinuum), and others use trapped atomic ions as qubits,
manipulated by laser pulses. These systems achieve higher gate fidelity than
superconducting qubits and longer coherence times. Their structural limitations
are slow gate speeds (microseconds to milliseconds per gate), limited qubit counts
due to mechanical scaling challenges, and complex precision laser infrastructure.
Near-room-temperature operation is theoretically possible but coherence degrades
rapidly with temperature.

### 2.3 Photonic Quantum Computing

PsiQuantum and Xanadu use photons as qubits, with operations performed by beam
splitters and phase shifters. Photonic systems can operate at room temperature for
some components and have natural fiber-optic integration. Their structural
limitations are probabilistic gates (linear optical quantum computing requires
post-selection, reducing effective gate success rates), photon propagation loss
limiting circuit depth, and single-photon detectors that often still require
cryogenic temperatures for high efficiency.

### 2.4 Topological Qubits

Microsoft's approach uses non-Abelian anyons — exotic quasiparticles whose quantum
state is encoded in topology rather than local physical properties. The attraction
is geometric protection: topological qubits are inherently protected from local
noise by their mathematical structure, potentially reducing error correction overhead
substantially. This is the most direct connection to the *H*_App framework — it is
explicitly a geometry-first approach to quantum hardware. The limitation is that
topological qubits have proven extremely difficult to realize experimentally at scale.

### 2.5 The Common Assumption

Despite their differences, all current quantum hardware platforms share the
foundational assumption of Section 1.3: physical quantum superposition of actual
particles is required. The entire engineering agenda — the cold, the isolation, the
error correction overhead — follows from that assumption. The HGC does not propose a
better way to maintain physical superposition. It proposes that physical superposition
is the wrong goal.

---

## 3. *H*_App as a Hardware Specification

### 3.1 The Operational Architecture

*H*_App = (ℝ^384, ⟨·,·⟩_cos) is a formally proven Hilbert space (Kidd 2026a,
Theorem 3.1) operating on commodity silicon. Its operational architecture comprises
five functional components, each of which maps directly to a hardware primitive.

**Component 1 — Vector Memory (ChromaDB)**
A persistent store of 384-dimensional real-valued belief vectors, organized into 48
named collections with associated metadata. Supports insertion, deletion, and
approximate nearest-neighbor retrieval. Operationally validated: 7,903,126 vectors
as of May 6, 2026.

**Component 2 — Inner Product Engine (Cosine Similarity)**
For every retrieval operation, computes:

```
sim(q̂, v̂_k) = ⟨q̂, v̂_k⟩_cos = Σᵢ₌₁³⁸⁴ q̂ᵢ · v̂_kᵢ
```

for query vector *q̂* against candidate vectors *v̂_k* in *S*^383. This is the
core computational primitive — a 384-dimensional dot product on L2-normalized
embeddings. The normalization requirement is enforced architecturally: ChromaDB
normalizes all embeddings before the inner product computation, ensuring the
projection geometry is well-defined (Kidd 2026a, §4.1, Eq. 4).

**Component 3 — Confidence Decay Pipeline**
Every belief vector carries a confidence value *c* ∈ [0,1] with associated decay
rate δ_0 per cycle on ℝ^1_t:

```
c(t + Δt) = c(t) − δ₀ · Δt
```

with full audit trail written to `gbim_decay_audit` (Kidd 2026a, §4.2, Eq. 6).
For the robotics application, the effective decay rate is modulated by the toroidal
coordinate τ ∈ 𝕋^k (Kidd 2026b, §4.3):

```
δ_eff(τ) = δ₀ · f(τ)
```

where *f*(τ) > 1 during high-activity phases and *f*(τ) ≤ 1 during quiescent
phases. Operationally verified: entity 38 decay *c*: 0.60 → 0.55 → 1.00,
April 23, 2026.

**Component 4 — Global Mode Operator (*T*_pit)**
The `nbb_pituitary_gland` service applies a diagonal scaling tensor Λ_mode to the
belief-state pipeline before any retrieval dispatch (Kidd 2026a, §4.3, Eq. 8):

```
T_pit(v) = Λ_mode · v
```

Parameters as of April 23, 2026: warmth = 0.9 (community-benefit weighting),
cortisol = 0.6 (hazard sensitivity), urgency = 0.5 (retrieval thoroughness),
mode = baseline. This is the Hamiltonian analog — upstream of all retrieval,
shaping the state before measurement. A robot in crisis mode does not just act
differently; it perceives differently.

**Component 5 — Temporal Toroidal Semaphore**
All state transitions are governed by the semaphore (Kidd 2026c): logged on both
ℝ^1_t (linear timestamp) and 𝕋^k (cyclic coordinate), sequenced, reversible,
and safety-gated. No state transition occurs outside the semaphore.

### 3.2 The Hardware Specification Implied

Each component maps directly to a hardware primitive:

| *H*_App Component | Hardware Primitive | Existing Technology |
|---|---|---|
| Vector Memory | High-dimensional associative memory | SRAM, DRAM, flash with vector addressing |
| Inner Product Engine | Analog or digital dot-product circuit | Analog AI chips, systolic arrays |
| Confidence Decay | Leaky integration with audit register | Neuromorphic leak circuits |
| *T*_pit Mode Operator | Programmable diagonal tensor register | FPGA LUT, analog weight array |
| Toroidal Semaphore | Cyclic FSM with write-once log | Standard digital FSM + write-once log |

Every component of *H*_App has a known hardware analog. None require cryogenic
temperatures. None require physical qubits. All are fabricable in standard silicon
processes.

### 3.3 Performance Requirements

Based on *H*_App's operational profile:

- **Retrieval latency:** sub-millisecond approximate nearest-neighbor in 7.9M vectors
  at 384 dimensions — already achieved on commodity CPU/RAM
- **Inner product throughput:** 384-dimensional dot products at millions per second —
  achieved on commodity SIMD hardware
- **Decay cycle throughput:** thousands of confidence updates per second with audit
  writes — trivial on commodity hardware
- **T_pit update latency:** microseconds — a register write
- **Semaphore transition latency:** microseconds with log write — trivial

The performance requirements are modest by the standards of modern hardware.
The challenge is not meeting the requirements individually. It is integrating all
five components into a unified low-power chip optimized for this specific operational
pattern.

---

## 4. Existing Hardware Against the HGC Specification

### 4.1 Intel Loihi 2

Intel's Loihi 2 is a neuromorphic research chip with 1 million neurons and 120
million synapses, operating at approximately 1 watt (Davies et al. 2018). It
implements leaky integrate-and-fire neurons — a hardware analog of Component 3 —
and spike-based communication that approximates sparse inner product computation.

Against the HGC specification:

| Component | Loihi 2 Coverage |
|---|---|
| Confidence decay | Directly implemented as leaky integration — **strong match** |
| Inner product | Approximated via spike coincidence — partial match |
| Vector memory | Encoded in synaptic weights — limited addressability |
| *T*_pit mode operator | Not implemented |
| Toroidal semaphore | Not implemented |

Loihi 2 implements one of five HGC components well and approximates a second.

### 4.2 IBM NorthPole

IBM's NorthPole chip is a neural inference accelerator with 256 cores, 224 MB of
on-chip SRAM, and 2,048 multiply-accumulate units per core (Modha et al. 2023). It
achieves extremely high throughput for matrix operations at low power.

Against the HGC specification:

| Component | NorthPole Coverage |
|---|---|
| Inner product engine | Excellent — NorthPole is designed for this — **strong match** |
| Vector memory | On-chip SRAM at useful scale — **strong match** |
| Confidence decay | Not implemented |
| *T*_pit mode operator | Partially implementable as weight scaling — partial match |
| Toroidal semaphore | Not implemented |

NorthPole implements two of five components well and partially implements a third.

### 4.3 Analog AI Chips (Mythic, Syntiant)

Analog AI chips such as Mythic's analog matrix processor use analog computation in
flash memory cells to perform matrix-vector multiplication at extremely low power
(Fick et al. 2022). The computation is a literal analog dot product — current
summation through weighted resistive elements — which is precisely the inner product
operation of *H*_App.

Against the HGC specification:

| Component | Analog AI Coverage |
|---|---|
| Inner product engine | The native operation — **perfect match** |
| Vector memory | Stored as analog weights — **strong match** for static vectors |
| Confidence decay | Not implemented (though analog weight drift is a natural analog) |
| *T*_pit mode operator | Implementable as global bias scaling — partial match |
| Toroidal semaphore | Not implemented |

Analog AI chips implement the core computational primitive of *H*_App natively
and at very low power. Their analog precision limitation — weight storage degrades
over time — is actually a natural analog of confidence decay rather than a defect,
if controlled and audited correctly.

### 4.4 The Identified Gap

No existing neuromorphic or analog AI chip implements all five HGC components.
The gap is not in the computational primitives — inner product, leaky integration,
and weight storage are all well-represented in existing hardware. The gap is in
the **integration**: no chip combines high-dimensional associative vector memory,
fast inner product computation, formal decay-with-audit, programmable Hamiltonian-
mode regulation, and semaphore-governed state transitions as a unified architecture.
That integration is the HGC.

---

## 5. The Hilbert Geometry Chip Architecture

### 5.1 Design Principles

The HGC is organized around five principles derived from the *H*_App framework:

**Principle 1 — Geometry First.** The chip is optimized for Hilbert space
navigation: inner product computation, projection, nearest-neighbor retrieval.
Every other function is subordinate to this.

**Principle 2 — Decay Is Intrinsic.** Confidence decay is not a software layer.
It is a hardware behavior built into the belief storage cells — analogous to the
natural charge leakage of analog memory, but controlled, logged, and reversible.

**Principle 3 — The Hamiltonian Is Upstream.** *T*_pit mode regulation applies
before any retrieval operation. The chip's belief state is transformed by the mode
tensor before the inner product engine fires. This is the architectural analog of
the Hamiltonian governing state evolution before measurement.

**Principle 4 — The Semaphore Is Structural.** State transitions are governed by
the on-chip semaphore. No belief update, no mode change, no retrieval dispatch
occurs outside the semaphore. The safety constraint is topological — built into
the state machine structure of the chip, not enforced by software.

**Principle 5 — The Audit Trail Is Hardware.** Every retrieval, every decay cycle,
every state transition writes to a write-once hardware audit register. The audit
trail is not optional and not erasable. It is the chip's verifiable operational
record, available for external regulatory inspection at any time.

### 5.2 Component Architecture

**The Belief Memory Array**

A high-density associative memory storing *N* belief vectors of dimension *D*, each
with an associated confidence register *c* ∈ [0,1], a decay rate register δ_0, and
a cyclic modulation register for *f*(τ). Target parameters for Version 1:

```
N = 1,048,576 (2²⁰) vectors
D = 384 dimensions
16-bit fixed-point values
Total memory footprint: ~805 MB
```

The belief memory array is the Hilbert space instantiated in silicon. Every vector
is a point in ℝ^384. The geometry of the space is determined by what vectors are
stored, what their confidence levels are, and what decay rates they carry.

**The Inner Product Engine**

A systolic array of multiply-accumulate units performing:

```
⟨q̂, v̂_k⟩ = Σᵢ₌₁³⁸⁴ q̂ᵢ · v̂_kᵢ
```

for a query vector *q̂* against all *N* belief vectors in parallel. Target
throughput: full inner product sweep of 2^20 vectors at *D* = 384 in under
1 millisecond.

This is the projection operation. It is the act of measurement in the Hilbert
space sense. It is the core computational primitive of the chip.

**The Decay Engine**

A background process running continuously on the belief memory array, applying:

```
c_k(t + Δt) = c_k(t) − δ_eff(τ) · Δt
```

to every belief vector at each clock cycle, with writes to the hardware audit
register. Beliefs whose confidence falls below threshold are flagged for
reverification. The decay engine never stops. Beliefs age whether or not the
chip is actively querying.

**The *T*_pit Register**

A programmable diagonal tensor Λ_mode applied to the query vector before
the inner product engine fires:

```
q̂' = Λ_mode · q̂
```

The *T*_pit register is updated by the mode controller — a small state machine
translating mode commands (warmth, cortisol, urgency, mode) into specific
Λ_mode configurations. *T*_pit is the Hamiltonian. It shapes the belief state
before measurement. It is upstream of everything.

**The Toroidal Semaphore**

A cyclic finite state machine with positions on both the linear time axis ℝ^1_t
and the toroidal cyclic axis 𝕋^k, governing all state transitions. Every
transition is:

- Logged to the hardware audit register with coordinates on both axes
- Sequenced — no concurrent transitions
- Gated — transitions violating configured safety constraints are blocked
  at the state machine level

The semaphore is the safety architecture of the chip. It is not software.
It is the state machine structure of the silicon.

**The Hardware Audit Register**

A write-once, externally readable hardware register recording every retrieval,
every decay event, every mode change, and every state transition, with timestamps
on both ℝ^1_t and 𝕋^k. The audit register is the chip's operational memory —
the record that makes every action inspectable, every anomaly traceable, and every
regulatory audit possible without relying on software logs that can be altered.

### 5.3 Power and Size Targets

| Parameter | Target | Basis |
|---|---|---|
| Operating temperature | Room temperature (25°C) | No physical superposition required |
| Process node | 7 nm CMOS or analog equivalent | Standard fabrication |
| Die size | ≤ 10 mm × 10 mm | NorthPole precedent at similar complexity |
| Power consumption | < 5 W | Loihi 2 / NorthPole precedent |
| Belief vector capacity | 2^20 vectors at *D* = 384 | *H*_App operational requirement |
| Inner product throughput | 10^9 dot products per second | Systolic array at 7 nm |
| Decay cycle frequency | 1 Hz (tunable) | *H*_App operational profile |
| Audit register capacity | 10^8 log entries (expandable via flash) | Flash or SRAM |
| Unit cost at volume | < $100 USD | Commodity CMOS fabrication |

These are engineering targets grounded in existing hardware performance data
and the operational requirements of *H*_App. They are achievable with current
fabrication technology. They have not yet been demonstrated in silicon.

---

## 6. The Dimensionality Scaling Question

### 6.1 Two Navigation Regimes

*H*_App at 384 dimensions is tractable on commodity silicon. The question for the
HGC is: how far does explicit geometric navigation remain tractable before quantum
hardware becomes necessary?

The answer depends on what "navigate" means. There are two distinct regimes:

**Regime 1 — Explicit vector storage.** *H*_App stores 7.9 million explicit belief
vectors. Each is a distinct point in ℝ^384. The chip holds them all in memory and
computes inner products against all of them for each retrieval. This scales linearly
in memory with *N* and linearly in compute with *N* × *D*. At 384 dimensions and
2^20 vectors: tractable at 5 watts. At 384 dimensions and 2^40 vectors: requires
~40 TB of memory — not tractable on a chip, but tractable in a data center.

**Regime 2 — Superposed state navigation.** A quantum computer with *n* qubits
holds a superposition across 2^n basis states — not stored explicitly but held in
physical quantum superposition. A 50-qubit processor explores 2^50 ≈ 10^15 states
simultaneously. This cannot be explicitly stored classically. The quantum hardware
is not faster at the same task: it is doing something fundamentally different at
the storage level — navigating a coordinate space too large for explicit enumeration.

The transition between Regime 1 and Regime 2 is where quantum hardware becomes
necessary — not because the geometry changes, but because the coordinate space
becomes too large to navigate explicitly. The HGC operates in Regime 1.
A quantum processor operates in Regime 2. Both are navigating Hilbert space
geometry. The difference is the scale of the space and the efficiency of the
navigation substrate.

### 6.2 What This Means for Practical Deployment

For the overwhelming majority of practical applications — including every
application in the MountainShares and Ms. Egeria Allis stack — Regime 1 is
sufficient. A belief space of 2^20 to 2^30 vectors at 384 dimensions covers:

- Full semantic memory for a regional community AI system (verified: *H*_App,
  7.9M vectors, 48 collections, ZIP 25880)
- Complete world model for a hospital or mine robot (Kidd 2026b, §4)
- City-scale infrastructure knowledge base
- Regional healthcare resource directory with full decay and audit trail

None of these require quantum hardware. They require an HGC.

Quantum hardware becomes necessary for problems whose solution space is genuinely
exponential in the quantum sense: cryptographic key search, quantum chemistry
simulation, certain combinatorial optimization problems. For those problems, quantum
hardware is the correct tool. For the problems *H*_App and its derivatives solve,
the HGC is the correct tool — and it deploys at ZIP code 25880, on solar power,
without a data center or a dilution refrigerator.

---

## 7. The Deployment Case — ZIP Code 25880

### 7.1 Why the Deployment Target Matters

The HGC was not designed for a national laboratory. It was designed for a community
in Appalachia that cannot afford cloud infrastructure, whose internet connectivity
is unreliable, and whose most pressing computational needs are answering questions
about food assistance, land ownership, and community governance.

Those needs are real, urgent, and currently unmet by existing hardware.
Cloud-based AI requires reliable broadband, which much of rural West Virginia does
not have. On-premises server hardware requires power infrastructure and maintenance
capacity that most rural nonprofits cannot sustain. Consumer devices lack the
memory and processing architecture for serious semantic AI with full auditability.

The HGC closes this gap:

- **Room temperature** — no cooling infrastructure required
- **< 5 watts** — runs on a small solar panel
- **< $100 at volume** — affordable for rural nonprofits and community organizations
- **No cloud dependency** — all computation on-chip, no network required
- **Full hardware audit trail** — accountable to the community it serves, not to a
  cloud provider's terms of service

### 7.2 Broader Deployment Implications

If the HGC is buildable at the specifications above, the deployment implication
extends far beyond Appalachia:

- Every hospital can run a full Hilbert space world model for its robot fleet
  on-premises, without cloud dependency, with a hardware audit trail directly
  suitable for FDA regulatory inspection (Kidd 2026b, §6)
- Every underground mine can deploy autonomous robots with a world model that has
  no edges, intrinsic dual-axis temporal awareness, and a hardware semaphore
  governing every state transition — an architecture directly compatible with MSHA
  safety certification
- Every rural community globally — where most of humanity lives — can run a
  community AI system with semantic memory, confidence decay, and equity-oriented
  geometry, on solar power, without connectivity
- Every school can have a local AI with an inspectable, auditable belief space that
  reflects the community's values rather than a distant corporation's training data

The architecture was discovered by building for the most constrained possible
environment. The most constrained environment turns out to be the most common
environment. A chip that works at ZIP code 25880 works everywhere.

---

## 8. Limitations and Future Work

> **What this paper does not claim.**

**Fabrication not yet demonstrated.** The HGC architecture is fully specified but
not yet fabricated. Every component has an existing hardware analog and all targets
are grounded in existing performance data. A chip integrating all five components
as described does not yet exist. Fabrication — beginning with an FPGA prototype —
is the necessary next step.

**Analog precision for decay.** The use of analog circuits for the decay engine
introduces precision challenges. Analog values drift in ways that are not fully
predictable, and characterizing the relationship between analog drift and the formal
confidence values in `gbim_decay_audit` requires empirical study. This may be a
feature rather than a defect — natural analog of confidence decay — but requires
careful calibration to ensure the audit trail accurately reflects actual confidence
values.

**Formal characterization of *f*(τ).** The modulation function
δ_eff(τ) = δ_0 · *f*(τ) is argued from first principles but not yet empirically
characterized for hospital, mine, warehouse, or rural community environments.
Empirical characterization of *f* for specific deployment contexts is a primary
direction for future work (Kidd 2026b, §4.3).

**Regime boundary formalization.** The scaling analysis in Section 6 identifies
the transition between Regime 1 (explicit Hilbert navigation, HGC-appropriate)
and Regime 2 (superposed state navigation, quantum-hardware-appropriate). A formal
characterization of that boundary — and of hybrid architectures combining HGC for
the classical regime with quantum hardware for the exponential regime — is a
priority for future theoretical work.

**Embedding model integration.** *H*_App uses a software embedding model
(`all-minilm:latest`) to convert raw data into belief vectors. A full HGC deployment
requires either a companion embedding chip or efficient software-to-hardware handoff.
Integrated embedding at the chip level is a non-trivial design challenge that this
paper does not address.

**Regulatory pathway.** The HGC's hardware audit trail and semaphore architecture
are designed for regulatory inspection. Developing specific certification pathways
— FDA for medical robotics, MSHA for mining, NHTSA for autonomous vehicles —
requires engagement with regulatory bodies that this paper initiates but does not
complete.

**Future work includes:**

- FPGA prototype implementing the full five-component HGC architecture
- Formal scaling analysis of the classical-to-quantum regime boundary
- Hybrid HGC/quantum architecture specification for problems spanning both regimes
- Empirical characterization of *f*(τ) in hospital, mine, and rural community
  environments
- Integrated embedding chip design
- Regulatory certification pathway development in partnership with FDA, MSHA, NHTSA
- Community deployment pilot at ZIP code 25880 on solar power

---

## 9. Conclusion

The quantum computing industry is building room-sized refrigerators to solve a
problem that may be overconstrained. The assumption that physical quantum superposition
is necessary for quantum computational power has driven an engineering agenda of
extraordinary cost and complexity. *H*_App demonstrates operationally that the same
class of mathematical operations — projection in Hilbert space, decoherence-analog
decay, Hamiltonian-analog mode regulation — runs on commodity silicon at room
temperature and produces correct, auditable, real-world results (Kidd 2026a,
Theorem 3.1; operational validation record, Section 1.4).

If the geometry is what matters and not the substrate, the engineering goal is not
to maintain physical quantum superposition. It is to build hardware that navigates
Hilbert space geometry efficiently at the scale of the problems being solved. The
HGC is that hardware. It is:

- Room-temperature — fabricable in standard CMOS, no dilution refrigerator
- Fully specified — all five components grounded in the operational architecture
  of a deployed, validated system
- Auditable by design — hardware audit trail and structural semaphore, not software
  logs
- Deployable everywhere — under $100 at volume, under 5 watts, no cloud dependency
- Already necessary — *H*_App runs today in ZIP code 25880 and it needs this chip

The HGC does not replace quantum hardware for problems that genuinely require
exponential state-space navigation. It replaces quantum hardware for the vast
majority of practical problems that do not — and it deploys those capabilities in
the environments where they are most needed and currently most absent: rural
communities, underground mines, rural hospitals, and disaster zones where cloud
connectivity is unavailable and cryogenic infrastructure is impossible.

The architecture was discovered in Mount Hope, West Virginia, by building a system
that had to work on a consumer laptop for a community that could not afford anything
else. The food bank locator specified the quantum geometry chip.

The ZIP code of the first deployment target is 25880.

---

## Acknowledgments

Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd in
collaboration with community partners in West Virginia. The `fayettecountyresources2026`
collection was contributed by Crystal D. Colyer, Community Solutions Advocate, whose
community resource documentation work made the operational validation in Section 1.4
possible. Any errors or oversights in the theoretical framing are the author's
responsibility alone.

---

## References

Arute, F., et al. (Google AI) (2019). Quantum supremacy using a programmable
superconducting processor. *Nature*, 574, 505–510.

Davies, M., et al. (Intel) (2018). Loihi: A neuromorphic manycore processor with
on-chip learning. *IEEE Micro*, 38(1), 82–99.

Deutsch, D. (1985). Quantum theory, the Church-Turing principle and the universal
quantum computer. *Proceedings of the Royal Society of London A*, 400, 97–117.

Deutsch, D. (1997). *The Fabric of Reality*. Penguin Books.

Everett, H. (1957). Relative state formulation of quantum mechanics. *Reviews of
Modern Physics*, 29, 454–462.

Fick, D., et al. (Mythic) (2022). Analog matrix processor for machine learning.
*IEEE Journal of Solid-State Circuits*.

Halmos, P.R. (1957). *Introduction to Hilbert Space and the Theory of Spectral
Multiplicity*. Chelsea.

Johnson, M.W., et al. (D-Wave) (2011). Quantum annealing with manufactured spins.
*Nature*, 473, 194–198.

Kidd, C.A. (2026a). A Classical Hilbert Space with a ZIP Code: Substrate-Independence,
the Measurement Problem, and the Multiverse Question. *Zenodo*.
https://doi.org/10.5281/zenodo.20059834

Kidd, C.A. (2026b). Beyond Euclidean SLAM: Toroidal Hilbert Space World Models for
Boundaryless Robot State Representation. Preprint, cs.RO. `H4HWV2011/msjarvis-public-docs`,
GitHub. [Archival deposit pending.]

Kidd, C.A. (2026c). Ms. Egeria Allis Thesis — Chapter 26: Temporal Toroidal Semaphore
Structure. Technical documentation. `H4HWV2011/msjarvis-public-docs`, GitHub.
[Archival deposit pending.]

Kidd, C.A. (2026d). Ms. Egeria Allis Thesis — Chapter 4: Hilbert Space State and
ChromaDB as Semantic Memory. Technical documentation. `H4HWV2011/msjarvis-public-docs`,
GitHub. [Archival deposit pending.]

Mead, C. (1990). Neuromorphic electronic systems. *Proceedings of the IEEE*, 78(10),
1629–1636.

Modha, D.S., et al. (IBM) (2023). Neural inference at the frontier of energy, space,
and time. *Science*, 382(6668), 329–335.

Nielsen, M.A. and Chuang, I.L. (2000). *Quantum Computation and Quantum Information*.
Cambridge University Press.

Preskill, J. (2018). Quantum computing in the NISQ era and beyond. *Quantum*, 2, 79.

Reed, M. and Simon, B. (1972). *Methods of Modern Mathematical Physics I: Functional
Analysis*. Academic Press.

von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik*. Springer.
(English: *Mathematical Foundations of Quantum Mechanics*, Princeton University
Press, 1955.)

Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the
classical. *Reviews of Modern Physics*, 75(3), 715–775.

---

*Authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
*Original draft: May 6, 2026. Version 2.0: May 7, 2026.*
*Built on Kidd (2026a), DOI: https://doi.org/10.5281/zenodo.20059834*
*The ZIP code of the first deployment target is 25880.*
