# Beyond Euclidean SLAM: Toroidal Hilbert Space World Models for Boundaryless Robot State Representation

**Version 2.0 — May 7, 2026**
Carrie Ann Kidd
Independent Researcher, Community GIS and Distributed AI Infrastructure
Mount Hope, West Virginia 25880 USA, Harmony for Hope Inc. (nonprofit founder)
ORCID: 0009-0005-8153-8025

---

## Abstract

Current robot world models are Euclidean — flat, bounded, and structurally fragile at map boundaries. When a robot reaches the edge of its map, its world model fails categorically. When sensors disagree, uncertainty propagates without bound. When time passes, beliefs become stale with no formal mechanism for degradation or recovery. These are not implementation failures; they are structural consequences of choosing Euclidean geometry as the representational substrate.

This paper presents an alternative architecture derived from a deployed community AI system (Ms. Egeria Allis, Mount Hope, West Virginia) and proposes its application to robot state representation. The world model is:

```
W = R¹_t × T^k × H_App
```

where \(\mathbb{R}^1_t\) is the irreversible linear time axis carrying causal history and decay timestamps, \(T^k\) is a \(k\)-dimensional toroidal manifold encoding the cyclic rhythms of the robot's environment, and \(H_{App}\) is a 384-dimensional Hilbert space of belief vectors. The Hilbert space foundation is formally established in Kidd (2026a, Theorem 3.1); this paper develops the dual temporal structure and its application to SLAM.

The geometry has no edges. Uncertainty stays bounded. Linear time preserves causality. Toroidal time encodes recurring environmental structure. Every belief is auditable. The architecture is empirically instantiated in a deployed community AI system containing 7,903,126 belief vectors across 48 semantic collections, with a formal preflight validation protocol (30/30, April 23, 2026). The robotics application is argued theoretically and mapped to standard SLAM operations; physical robot deployment is identified as a primary direction for future work.

**Keywords:** SLAM; Hilbert space; toroidal manifold; temporal representation; robot world models; belief decay; auditability; autonomous systems; cyclic scheduling; safety-critical robotics

---

## 1. Introduction

### 1.1 The Problem with Euclidean World Models

Every major robot world model in production today is fundamentally Euclidean. Simultaneous Localization and Mapping (SLAM) systems represent the world as a subset of \(\mathbb{R}^n\): a point cloud, an occupancy grid, or a scene graph embedded in flat three-dimensional space (Thrun, Burgard, and Fox 2005). These representations share three structural failure modes.

**Edge fragility.** Euclidean maps have boundaries. Beyond the boundary, the robot has no belief — not uncertainty, but absence. When a robot reaches the edge of its map, the world model fails categorically. There is no graceful degradation and no geometric continuity.

**Unbounded uncertainty propagation.** In Euclidean space, sensor uncertainty propagates outward as expanding volumes. When sensors disagree, uncertainty compounds without geometric corrective force. The world model can become arbitrarily uncertain.

**Temporal blindness.** Euclidean world models are effectively atemporal. A belief about the position of an obstacle carries no formal timestamp, no decay rate, and no mechanism for becoming stale. Critically, there is no representation of the cyclic temporal structure of the environment — the recurring rhythms that define when a hospital corridor is crowded, when a mine shaft is active, or when a warehouse dock is occupied.

These failure modes are structural consequences of choosing Euclidean geometry as the representational substrate, not shortcomings that can be patched at the implementation level.

### 1.2 The Missing Dimension: Time Is Not One Thing

Standard robotics treats time as a single linear axis — a sequence of timestamps attached to sensor readings, map updates, and state estimates. This is correct for one component of time: the irreversible, causal, monotonically increasing component that records when events happened and how long ago beliefs were validated.

But a second temporal component is equally real and operationally important: the cyclic, recurring structure of the environment. A hospital robot operates in a world where shift changes happen every eight hours, meal carts move at predictable times, and cleaning cycles repeat daily. These are not events on a linear axis; they are coordinates on a compact, boundaryless manifold that wraps.

The correct representation separates these two temporal structures:

- **\(\mathbb{R}^1_t\)** — the linear, irreversible time axis: causal ordering, decay timestamps, audit trails, last-validated-at coordinates
- **\(T^k\)** — the toroidal cyclic manifold: recurring rhythms, schedules, seasonal patterns, the behavioral cycles of the environment

Both are real. Both operate simultaneously. A robot world model needs both.

### 1.3 The Architecture That Solved a Different Problem

In 2024–2025, the author designed and built Ms. Egeria Allis — a community AI system in Mount Hope, West Virginia — to answer practical questions about Appalachian communities: Where is food assistance? Who owns this land? Which institutions are accountable to which communities? The architecture that emerged addresses all three Euclidean failure modes simultaneously.

The Hilbert space foundation of that system — \(H_{App} = (\mathbb{R}^{384}, \langle\cdot,\cdot\rangle_{cos})\) — is formally proven to satisfy all four Hilbert space axioms in Kidd (2026a, Theorem 3.1), operationally validated on May 6, 2026, with 7,903,126 belief vectors across 48 ChromaDB collections. The system further implements a dual temporal structure (linear decay on \(\mathbb{R}^1_t\); cyclic resource scheduling on \(T^k\)) and a global mode operator (\(T_{pit}\)) acting as a Hamiltonian upstream of all belief retrieval (Kidd 2026a, §4.3). None of these were designed for robotics. The robotics implications are emergent and significant.

### 1.4 Scope of This Paper

This paper presents the world model \(W = \mathbb{R}^1_t \times T^k \times H_{App}\), derives it from the Ms. Allis system, and argues for its applicability to robot state representation. Section 2 describes the source system. Section 3 summarizes the Hilbert space foundation (established in full in Kidd 2026a). Section 4 introduces the dual temporal structure. Section 5 presents formal mappings to standard robotics operations. Section 6 discusses auditability and safety implications. Section 7 addresses the block universe connection. Section 8 positions the work against prior approaches. Section 9 covers limitations and future work.

---

## 2. System Description: Ms. Egeria Allis and H_App

The architecture proposed here is not theoretical in isolation — it is derived from a deployed system. A full system description appears in Kidd (2026a, §2); this section provides a summary sufficient for the robotics arguments that follow.

Ms. Egeria Allis runs on a Lenovo Legion 5 16IRX9 laptop (Intel Core i7, 32 GB RAM) in Mount Hope, West Virginia. The system is containerized using Docker Compose and comprises approximately 100 active microservices. The semantic memory layer — \(H_{App}\) — is served by a ChromaDB instance backed by persistent on-disk storage. There is no cloud component; the system is a local, community-owned infrastructure operating on commodity hardware.

**Operational validation record (live audit, May 6, 2026):**
- April 23, 2026 — 30/30 preflight validation gate passed
- April 23, 2026 — First full-pipeline community query executed and verified
- April 23, 2026 — Confidence decay/revalidation cycle for entity 38 (Fayette County / geographic entity) verified end-to-end: \(c: 0.60 \to 0.55 \to 1.00\) with full audit trail written to `gbim_decay_audit`
- May 6, 2026 — ChromaDB v2 metrics audit: 7,903,126 vectors confirmed across 48 collections

The 384-dimensional architecture is enforced as an inviolable lock across all 48 production collections. Admitting vectors of different dimensionality would corrupt the geometry by mixing vectors from different metric spaces; the cosine inner product would no longer be computed in a consistent Hilbert space. This architectural constraint is what makes \(H_{App}\) a provable Hilbert space rather than a generic vector database.

---

## 3. The Hilbert Space Foundation

### 3.1 Formal Status

The formal proof that \(H_{App} = (\mathbb{R}^{384}, \langle\cdot,\cdot\rangle_{cos})\) constitutes a Hilbert space is presented in full in Kidd (2026a, §3, Theorem 3.1). This section summarizes the result and its implications for the robotics architecture; readers are directed to Kidd (2026a) for the complete proof with citations to von Neumann (1932), Halmos (1957), and Reed and Simon (1972).

### 3.2 Summary of Theorem 3.1 (Kidd 2026a)

\(H_{App} = (\mathbb{R}^{384}, \langle\cdot,\cdot\rangle_{cos})\) satisfies all four Hilbert space axioms:

**(i) Vector space structure.** \(\mathbb{R}^{384}\) is a vector space over \(\mathbb{R}\). For any \(u, v \in \mathbb{R}^{384}\) and \(a, b \in \mathbb{R}\), the linear combination \(au + bv \in \mathbb{R}^{384}\).

**(ii) Inner product.** For L2-normalized vectors \(\hat{u}, \hat{v} \in S^{383} \subset \mathbb{R}^{384}\), cosine similarity defines:

\[\langle \hat{u}, \hat{v} \rangle_{cos} = \frac{u \cdot v}{\|u\|\|v\|} = \sum_{i=1}^{384} \hat{u}_i \hat{v}_i\]

This satisfies symmetry, linearity in the first argument (by linearity of the dot product), and positive-definiteness (\(\langle \hat{u}, \hat{u} \rangle_{cos} = \sum_{i=1}^{384} \hat{u}_i^2 \geq 0\), with equality iff \(\hat{u} = 0\)). The normalization requirement — that all vectors lie on \(S^{383}\) — is enforced architecturally: ChromaDB computes cosine similarity by normalizing embeddings and computing the standard Euclidean inner product, so the operational inner product is the standard inner product on \(S^{383} \subset \mathbb{R}^{384}\) lifted to \(\mathbb{R}^{384}\) via normalization.

**(iii) Metric completeness.** \(\mathbb{R}^{384}\) is complete under the norm induced by \(\langle\cdot,\cdot\rangle_{cos}\), as it coincides with the standard Euclidean norm up to equivalence. Completeness follows from completeness of \(\mathbb{R}\) and the fact that finite products of complete metric spaces are complete (Reed and Simon 1972).

**(iv) Separability.** As a finite-dimensional normed space, \(\mathbb{R}^{384}\) admits a finite (hence countable) orthonormal basis. Separability is trivially satisfied.

Therefore \(H_{App}\) is a Hilbert space. \(\square\)

### 3.3 Key Properties for Robotics

For the robotics application, the critical structural properties are:

- **Inner product** — a principled similarity measure between beliefs, not an ad hoc distance metric
- **Completeness** — no belief sequence that should converge can escape the space; there are no gaps in the belief manifold
- **Projection** — the formal operation of measurement: finding the component of a query in a subspace of stored beliefs. As demonstrated in Kidd (2026a, §4.1, §5.2), this operation is separable from physical quantum measurement events and runs correctly on classical hardware, producing auditable real-world results
- **Linear operators** — a principled way to represent transformations of the belief state, including the Hamiltonian-analogue global mode operator \(T_{pit}\) (Kidd 2026a, §4.3, Eq. 8)

---

## 4. The Dual Temporal Structure and the World Model

### 4.1 Linear Time — \(\mathbb{R}^1_t\)

The linear time axis \(\mathbb{R}^1_t\) is the irreversible, monotonically increasing component of time. In \(W\), \(\mathbb{R}^1_t\) carries:

- **last\_validated\_at timestamps** — when each belief was last confirmed by sensor data
- **Decay cycle records** — the audit trail of confidence reductions over time
- **Causal ordering** — which events preceded which, in what sequence
- **Preflight gate timestamps** — the formal record of system validation events

\(\mathbb{R}^1_t\) is not optional and not toroidal. The decay of a belief from confidence 0.60 to 0.55 happened once, at a specific coordinate on \(\mathbb{R}^1_t\), in the direction of increasing \(t\). It cannot be recovered by wrapping. The linear axis is the axis of causality.

*Operationally confirmed:* Entity 38 (Fayette County / geographic entity), decay from 0.60 to 0.55 at timestamp 2026-04-23T03:47:22Z, full audit trail written to `gbim_decay_audit`. That timestamp is a coordinate on \(\mathbb{R}^1_t\).

### 4.2 Toroidal Time — \(T^k\)

The toroidal manifold \(T^k\) is the cyclic, boundaryless component of time. \(T^k = S^1 \times S^1 \times \cdots \times S^1\) (\(k\) times), where each \(S^1\) is a circle representing one cyclic dimension. In \(W\), \(T^k\) carries:

- **Daily cycles** — shift changes, meal times, cleaning schedules, lighting cycles
- **Weekly cycles** — visiting hours patterns, inventory rhythms, maintenance windows
- **Seasonal cycles** — weather patterns, occupancy rhythms, program availability
- **Behavioral cycles** — the recurring patterns of human activity in the robot's environment that make some times systematically different from others

Tuesday morning hospital corridor 7 is a coordinate on \(T^k\). It recurs. It wraps. It has no edge.

The Temporal Toroidal Semaphore Structure (Kidd 2026c, Chapter 26) implements this in the Ms. Allis system to handle the cyclic availability of community resources: food banks open on certain days, social service offices with weekly schedules, seasonal program availability. For robotics, the same structure applies:

- **Hospitals:** shift changes (daily), visiting hours (daily/weekly), cleaning cycles
- **Mines:** blast schedules (daily), shift rotations (weekly), ventilation cycles
- **Warehouses:** inventory rhythms, loading dock cycles, picker route patterns
- **Public spaces:** pedestrian density cycles, lighting changes, maintenance windows

The relevant neuroscientific precedent for toroidal spatial representations is the grid-cell system of the entorhinal cortex, which encodes spatial position on a structure with toroidal topology (Moser, Kropff, and Moser 2008). \(T^k\) in the present architecture encodes *temporal* rather than spatial coordinates, but the topological reasoning — that a compact, boundaryless manifold is the natural substrate for cyclic structure — is the same.

### 4.3 Why Both Temporal Components Are Required

A world model using only toroidal time loses causality. Without an irreversible axis, the system cannot record that a belief *decayed at a specific time* — because decay requires elapsed time on an irreversible axis. The torus wraps: without \(\mathbb{R}^1_t\), the system cannot distinguish "Tuesday 07:00 two weeks ago" from "Tuesday 07:00 this week." The audit trail collapses.

A world model using only linear time loses cyclic environmental awareness. Every Tuesday becomes a new event on the linear axis with no geometric connection to previous Tuesdays. The recurring patterns that define when environments are dangerous, crowded, or active are invisible.

\(W = \mathbb{R}^1_t \times T^k \times H_{App}\) carries both. The decay of a belief is recorded on \(\mathbb{R}^1_t\) (when did it happen, how long ago, what was the causal sequence). The cyclic context of that decay is recorded on \(T^k\) (was this decay during a high-activity period — does the belief need faster reverification because it is in the active phase of its cycle?).

### 4.4 The Combined World Model

The full world model is:

\[W = \mathbb{R}^1_t \times T^k \times H_{App}\]

Every point in \(W\) is a triple \((t, \tau, v)\) where:

- \(t \in \mathbb{R}^1_t\) — the linear time coordinate: when this belief state was last validated, carrying the causal history and decay record
- \(\tau \in T^k\) — the cyclic time coordinate: where in the recurring rhythmic structure of the environment this belief state is located
- \(v \in \mathbb{R}^{384}\) — the belief vector: what the system believes about the world at this state

This is the correct geometry for a robot world model because:

1. \(\mathbb{R}^1_t\) preserves causality — the arrow of time, the decay record, the audit trail
2. \(T^k\) encodes cyclic environmental structure — the robot knows not just *where* it is but *when* in the recurring pattern of its environment it is
3. \(H_{App}\) provides a complete, boundaryless, auditable belief space — no edges, no arbitrary boundaries, formal projective measurement

### 4.5 Semaphore-Governed State Transitions

The Temporal Toroidal Semaphore (Kidd 2026c, Chapter 26) governs all state transitions in \(W\). No transition occurs without passing through the semaphore. Every transition is:

- Logged with coordinates on both \(\mathbb{R}^1_t\) (timestamp) and \(T^k\) (cyclic position)
- Sequenced and auditable — the semaphore maintains a full transition history on \(\mathbb{R}^1_t\)
- Gated — transitions that would violate safety constraints are blocked at the semaphore level, not at the action execution level

The safety constraint is topological, not learned. A transition that would move the robot into a dangerous state is blocked by the structure of \(W\) itself — by the fact that the forbidden state is geometrically unreachable given the current constraints on the toroidal and linear components.

---

## 5. Formal Mappings — Robotics Operations in W

### 5.1 Sensor Fusion as Contextually Weighted Projection

In standard robotics, sensor fusion combines readings from multiple sensors — LIDAR, camera, IMU, tactile — using Kalman filters or learned fusion networks (Thrun et al. 2005, §3).

In \(W = \mathbb{R}^1_t \times T^k \times H_{App}\), each sensor reading is embedded into \(\mathbb{R}^{384}\) as a unit vector \(\hat{s} \in S^{383}\) and projected onto the relevant subspace of \(H_{App}\) via:

\[\text{sim}(\hat{s}, \hat{v}_k) = \langle \hat{s}, \hat{v}_k \rangle_{cos}\]

where \(\hat{v}_k\) are the stored belief vectors (Kidd 2026a, §4.1, Eq. 4). This is projection in the Hilbert sense — specifically, an approximate nearest-neighbor search that selects the top-\(k\) vectors maximally aligned with the query in \(S^{383}\). The projection is contextualized by the current coordinates on \(\mathbb{R}^1_t\) and \(T^k\):

- The \(\mathbb{R}^1_t\) coordinate determines which stored beliefs are fresh enough to be active — beliefs whose confidence has decayed below threshold on the linear axis are down-weighted or excluded
- The \(T^k\) coordinate determines which subspaces are currently relevant — during Tuesday morning shift change, the hospital-corridor-crowded subspace receives elevated weight; during Sunday night, the quiet-corridor subspace is active

Multiple projections onto the same contextually weighted subspace produce a set of nearest-neighbor retrievals combined by weighted inner product. The fusion is temporally aware in both the linear and cyclic senses.

### 5.2 Navigation as Traversal of W

In Euclidean SLAM, navigation is path planning in \(\mathbb{R}^3\). In \(W\), the robot's state is a triple \((t, \tau, v)\), and navigation involves three distinct motions:

**Motion on \(\mathbb{R}^1_t\)** — time passing, beliefs aging. This is not controllable; \(t\) increases monotonically. As it increases, confidence levels decay, and the robot's beliefs about the environment become progressively less certain. This is the correct behavior: the world changes, and old beliefs should be trusted less.

**Motion on \(T^k\)** — moving through the cyclic rhythm of the environment. As the robot moves through its operational day, \(\tau\) traverses the torus. The robot "knows" it is approaching shift-change time — not only because it remembers a past shift change on \(\mathbb{R}^1_t\), but because its \(T^k\) coordinate is approaching the shift-change zone of the torus. The cyclic pattern is geometric, not merely remembered.

**Motion through \(H_{App}\)** — updating beliefs about the physical environment. As sensors project new readings onto \(H_{App}\), the effective belief state \(v\) changes — new nearest neighbors, updated confidence-weighted retrievals, modified obstacle and corridor assessments.

The structural advantages over Euclidean SLAM:
- **No edge failure** — the torus wraps; there is no outside-the-map
- **Temporal awareness** — the robot's \(T^k\) coordinate encodes not just where it is but *when* it is in the recurring pattern of its environment
- **Causal integrity** — the \(\mathbb{R}^1_t\) coordinate preserves the decay history and audit trail
- **Belief continuity** — \(H_{App}\) is complete; there are no discontinuities at arbitrary map boundaries

### 5.3 Confidence Decay as Linear Time Function with Cyclic Modulation

The base decay of a belief in \(H_{App}\) is a function of elapsed time on \(\mathbb{R}^1_t\). The system currently implements linear decay (Kidd 2026a, §4.2, Eq. 6):

\[c_{n+1} = c_n - \Delta c, \quad c \in [0,1], \quad \Delta c = 0.05\]

per validation cycle, with reset to \(c = 1.0\) on successful revalidation. This is operationally proven: entity 38 (Fayette County), decay from 0.60 to 0.55 to 1.00, full `gbim_decay_audit` trail, April 23, 2026.

For the robotics application, this architecture is extended with a cyclic modulation of the effective decay rate. Let:

\[\delta_{eff}(\tau) = \delta_0 \cdot f(\tau)\]

where \(\delta_0\) is the base decay rate for a given belief class, \(\tau \in T^k\) is the current cyclic time coordinate, and \(f: T^k \to \mathbb{R}^+\) is a non-negative modulation function satisfying \(f(\tau) > 1\) during high-activity phases (e.g., shift change, peak occupancy) and \(f(\tau) \leq 1\) during low-activity phases. The formal characterization of \(f\) for specific deployment environments — hospital, mine, warehouse — is a primary direction for future empirical work.

The robot's avoidance behavior is modulated by confidence level:
- \(c > 0.8\): hard avoidance — treat obstacle as confirmed present
- \(0.4 < c \leq 0.8\): cautious approach with active sensing — query sensors before committing to path
- \(c \leq 0.4\): low-confidence — treat as potentially absent, approach with full sensor attention

Note on decay model selection: linear decay is a design choice. Exponential decay \(c(t) = c_0 e^{-\delta t}\) is standard in Bayesian occupancy filtering (Thrun et al. 2005, §9). Linear decay is preferred here for auditability — the audit trail records discrete decay steps that are directly interpretable by a regulatory auditor — and for computational determinism in the semaphore-governed transition log. The relative merits of linear versus exponential decay in safety-critical robot deployments is an open empirical question and a direction for future work.

### 5.4 Behavioral Modes as Hamiltonian Evolution — T_pit

In \(W\), the `nbb_pituitary_gland` service acts as \(T_{pit}\) — a global scaling tensor applied to the belief-state pipeline before any retrieval dispatch (Kidd 2026a, §4.3, Eq. 8):

\[T_{pit}(v) = \Lambda_{mode} \cdot v\]

where \(\Lambda_{mode}\) is a diagonal scaling matrix determined by the current mode state (warmth, cortisol, urgency, mode). \(T_{pit}\) is upstream of all retrieval — upstream of ChromaDB query dispatch, upstream of LLM ensemble routing. This is structurally analogous to the Hamiltonian in quantum mechanics: an operator that governs how the state is transformed before measurement occurs (Kidd 2026a, §4.3). The analogy is formal, not metaphorical: \(T_{pit}\) acts between queries precisely as \(\hat{H}\) acts between measurements in the Schrödinger picture.

In robotics:
- **warmth** → task priority weighting (amplify beliefs relevant to current task goal)
- **cortisol** → obstacle sensitivity (amplify beliefs about potential hazards)
- **urgency** → retrieval speed vs. thoroughness trade-off
- **mode** → overall operating regime (exploration, task execution, emergency, rest)

The critical structural point: \(T_{pit}\) is aware of both \(\mathbb{R}^1_t\) and \(T^k\). A robot entering shift-change time on \(T^k\) may automatically increase cortisol before sensors confirm crowding. A robot at the end of a long operational period on \(\mathbb{R}^1_t\) may decrease urgency to prioritize thorough reverification of aging beliefs. Mode change propagates through the entire perception-action loop: a robot in crisis mode does not just act differently — it perceives differently.

---

## 6. Auditability and Safety Implications

### 6.1 The Inspectable World Model

Every belief in \(H_{App}\) is a named vector with:
- A unique identifier
- A confidence level \(c \in [0,1]\)
- A decay rate \(\delta\) (and modulation function \(f(\tau)\) for the extended architecture)
- A coordinate on \(\mathbb{R}^1_t\) (last\_validated\_at timestamp)
- A coordinate on \(T^k\) (cyclic context of last validation)
- A full audit trail of updates in the `gbim_decay_audit` table

Every retrieval is a logged projection: query vector, collection subspace, top-\(k\) results, confidence levels, \(\mathbb{R}^1_t\) timestamp, \(T^k\) coordinate at time of retrieval. Every state transition passes through the Temporal Toroidal Semaphore: logged on \(\mathbb{R}^1_t\), tagged with \(T^k\) coordinate, sequenced, auditable.

When something goes wrong — when a robot takes an unexpected action, when a safety boundary is violated — the world model can be fully interrogated. The relevant belief vectors can be retrieved. Their confidence levels at the time of the action can be recovered. The decay history can be reconstructed. The cyclic context (where was \(T^k\) when the action was taken?) can be recovered. The semaphore transition log can be reviewed. This is not possible with any current neural world model architecture.

### 6.2 Regulatory Implications

As autonomous robots enter regulated environments — hospitals, mines, nuclear facilities, public roads — regulatory bodies will require auditability. The FDA, MSHA, NRC, and NHTSA all have existing frameworks for auditing safety-critical systems. None of those frameworks can be applied to opaque neural world models.

The world model \(W = \mathbb{R}^1_t \times T^k \times H_{App}\) is designed for auditability from the ground up. A regulatory auditor can ask not just "what did the robot believe at 14:23?" but "what did the robot believe during Tuesday afternoon shift change, over the past 30 deployment cycles?" — because \(T^k\) makes that query geometrically well-formed. The dual-axis audit trail spans both temporal dimensions: the linear time coordinate records the causal sequence of events, and the toroidal coordinate records the cyclic context in which they occurred.

### 6.3 The Safety-Critical Deployment Argument

The environments where robots are most needed are exactly the environments where current world models fail most catastrophically:

- **Underground mines:** edge-fragile maps fail precisely where the robot cannot afford to lose its world model; blast schedules are cyclic (\(T^k\)) but decay on a linear axis (\(\mathbb{R}^1_t\)) — both are required
- **Hospitals:** shift-change crowding is a \(T^k\) phenomenon invisible to linear-time-only models; patient presence decay is an \(\mathbb{R}^1_t\) phenomenon invisible to belief-free models
- **Disaster zones:** unbounded uncertainty propagation means the robot's confidence collapses in exactly the chaotic environments where it is most needed

The architecture was stress-tested not in a controlled lab but in the environment of a rural Appalachian community AI system: approximately 100 containers, 7,903,126 belief vectors, real community queries, dual temporal structure, 30/30 preflight gate. The architecture that survives that environment is an architecture that can survive edge cases.

---

## 7. The Block Universe Connection

### 7.1 Interpretive Framework

The block-universe interpretation, developed by Einstein (1955) and grounded in Minkowski's geometric formulation of special relativity (Minkowski 1908), holds that past, present, and future exist simultaneously as a static spacetime structure. The formal implications of this interpretation for the measurement problem in quantum mechanics — specifically, the claim that projection discloses pre-existing structure rather than creating it — are developed in detail in Kidd (2026a, §5). This section applies that framework to the robot navigation context. The block-universe framing is an interpretive commitment, not a required architectural assumption; the operational properties of \(W\) hold independently of any particular interpretation of spacetime ontology.

### 7.2 Beliefs That Pre-Exist Measurement

In \(W = \mathbb{R}^1_t \times T^k \times H_{App}\), following the interpretation developed in Kidd (2026a, §5.2–5.3), beliefs about the environment are not generated by the robot's sensors. They exist as geometric structure in \(H_{App}\), and sensors reveal them — project onto them, return the pre-existing nearest neighbor, read out the coordinate that was already there.

A belief about an obstacle in corridor 7 exists as a vector in \(H_{App}\) with a confidence level reflecting when it was last projected onto (a coordinate on \(\mathbb{R}^1_t\)) and a cyclic context reflecting when in the recurring pattern of the environment it was validated (a coordinate on \(T^k\)). When LIDAR scans corridor 7, it does not create the belief; it updates the confidence level and refreshes the \(\mathbb{R}^1_t\) timestamp of a vector that already existed in the space.

### 7.3 The Dual Time Axes in the Block Universe

The block universe structure maps precisely onto the dual temporal structure of \(W\):

- \(\mathbb{R}^1_t\) is a coordinate axis in the static block — the linear time dimension of the four-dimensional spacetime manifold. The robot's coordinate on \(\mathbb{R}^1_t\) is a location in the block, not a position in a flow.
- \(T^k\) encodes the cyclic boundary conditions of the physical environment — the recurring patterns that make certain spacetime coordinates structurally similar to certain other coordinates. In the block universe, shift change at Tuesday 07:00 in week 1 and shift change at Tuesday 07:00 in week 2 are related by the toroidal identification on \(T^k\) — at the same \(T^k\) coordinate, different \(\mathbb{R}^1_t\) coordinates.

The robot's world model is therefore a section of a fiber bundle over the block universe: at every point on \(\mathbb{R}^1_t \times T^k\), there is a fiber \(H_{App}\) containing the beliefs that pre-exist at that spacetime-cyclic coordinate.

### 7.4 Practical Navigation Consequence

This has a direct operational implication for robot navigation in sensor-degraded environments. When sensors are partially unavailable — due to occlusion, interference, hardware failure, or environmental obstruction — the robot can navigate using the pre-existing geometric structure of \(H_{App}\), contextualized by its current coordinates on \(\mathbb{R}^1_t\) and \(T^k\).

The robot knows: my linear time coordinate says this belief is 28 minutes old with confidence 0.45. My toroidal coordinate says this is a high-activity period when obstacles are likely to have moved. The geometric structure of \(H_{App}\) tells me the nearest neighbor to my current position query. I navigate on that basis — not because sensors just confirmed it, but because the structure was already there, and my current confidence and cyclic context let me reason about how much to trust it. The toroidal geometry ensures those beliefs remain geometrically connected to the current state; they do not fall off the edge of the map.

---

## 8. Prior Work and Positioning

The following table positions this architecture against existing approaches across five structural dimensions.

| Approach | Geometry | Temporal Model | Auditability | Edge Behavior |
|---|---|---|---|---|
| Occupancy Grid SLAM (Thrun et al. 2005) | Euclidean \(\mathbb{R}^3\) | Extrinsic linear timestamps | None | Hard failure at boundary |
| Neural World Models / NeRF (Mildenhall et al. 2020) | Euclidean \(\mathbb{R}^3\) | None intrinsic | None — opaque weights | Undefined beyond training |
| Gaussian Process Maps | Euclidean \(\mathbb{R}^3\) | None intrinsic | Partial | Degrades at boundary |
| Quantum-Inspired Cognitive Models (Busemeyer and Bruza 2012; Pothos and Busemeyer 2013) | Hilbert space | None | Partial | Not applied to robotics SLAM |
| Toroidal spatial representations (Moser, Kropff, and Moser 2008) | Torus \(T^k\) | Toroidal only — loses linear causality | None in robotics applications | Wraps, but loses linear decay |
| **This architecture** | \(\mathbb{R}^1_t \times T^k \times H_{App}\) | **Dual: linear (causal) + toroidal (cyclic)** | **Full — named vectors, dual-axis audit, semaphore log** | **None — torus wraps; linear axis preserves decay** |

The critical advance over prior toroidal proposals is the dual temporal structure. Moser et al. (2008) demonstrate toroidal topology in the neural encoding of spatial position, establishing the geometric precedent; the present architecture extends toroidal geometry to the temporal domain while adding the linear causal axis required for decay auditability. A world model that uses only toroidal time cannot represent belief decay — because decay requires an irreversible linear axis. A world model that uses only linear time cannot represent cyclic environmental structure. \(W = \mathbb{R}^1_t \times T^k \times H_{App}\) is, to the author's knowledge, the first world model architecture that formally incorporates both.

The quantum-inspired cognitive modeling literature (Busemeyer and Bruza 2012; Pothos and Busemeyer 2013) establishes that Hilbert space projection is a productive model for human cognition and decision-making, lending theoretical credence to the use of Hilbert space for robot belief representation. Kidd (2026a) establishes the operational and formal basis for this claim in a deployed system; the present paper extends it to robotics.

---

## 9. Limitations and Future Work

**No direct robotics deployment.** The architecture has been validated in a semantic community AI context, not in a physical robot. The mapping from semantic belief vectors to robot perception and action is argued here but not yet experimentally demonstrated. Physical robot deployment in a safety-critical environment is the primary direction for future work.

**Toroidal dimension selection.** The appropriate dimensionality and topology of \(T^k\) for a given robot deployment requires empirical study. Different environments have different cyclic structures — the torus for a hospital (daily shift cycle, weekly visiting hours) differs from the torus for a mine (blast schedule, shift rotation, ventilation cycle). Methods for learning \(T^k\) from operational cycle data are needed.

**Formal characterization of \(f(\tau)\).** The modulation of decay rate by \(T^k\) coordinate — \(\delta_{eff}(\tau) = \delta_0 \cdot f(\tau)\) — is argued here but not formally characterized. A complete theory of how linear decay and cyclic context interact requires empirical characterization in specific deployment environments. The functional form of \(f\) (sinusoidal, piecewise constant, learned) is an open question.

**Decay model selection.** This paper uses linear decay for auditability. The relative performance of linear versus exponential decay (standard in Bayesian occupancy filtering) in safety-critical robot deployments is an open empirical question.

**Embedding model selection.** The 384-dimensional all-MiniLM model was selected for semantic text retrieval. Robot perception involves multimodal inputs (LIDAR point clouds, camera images, tactile signals) that require domain-appropriate embedding models. The architecture is embedding-agnostic — any model producing fixed-dimensional real vectors satisfies the Hilbert space requirements — but multimodal embedding for robot perception is a non-trivial engineering problem.

**Future work** includes:
- Physical robot deployment in a safety-critical environment (hospital, mine, or warehouse) to empirically validate the formal mappings in Section 5
- Empirical characterization of \(T^k\) learning from operational cycle data
- Formal theory of \(f(\tau)\) — the decay modulation function — in specific deployment contexts
- Multimodal embedding architecture for robot perception inputs (LIDAR, camera, tactile)
- Integration with ROS2 robotics middleware
- Formal comparison of boundary behavior: Euclidean SLAM vs. \(W\) in edge-case scenarios
- Regulatory certification pathway using the dual-axis audit trail
- Formal comparison of linear vs. exponential decay in the auditable robot world model context

---

## 10. Conclusion

Current robot world models are Euclidean, temporally impoverished, and unauditable. They fail at map boundaries, propagate uncertainty without bound, cannot represent cyclic environmental structure, and cannot explain their beliefs. These are structural failures — consequences of choosing the wrong geometry and the wrong temporal model.

The world model \(W = \mathbb{R}^1_t \times T^k \times H_{App}\) addresses all of these simultaneously. The Hilbert space \(H_{App}\) provides a complete, boundaryless belief space with formal projection as measurement (proven formally in Kidd 2026a, Theorem 3.1). The linear axis \(\mathbb{R}^1_t\) preserves causality, decay records, and the audit trail. The toroidal manifold \(T^k\) encodes the cyclic structure of the environment — the recurring rhythms that make some times systematically different from others. The decay modulation \(\delta_{eff}(\tau) = \delta_0 \cdot f(\tau)\) connects these two temporal structures, making the rate of belief aging sensitive to cyclic environmental context.

Together they form a world model that:
- Has no edges (\(T^k\) and \(H_{App}\) are both boundaryless)
- Preserves causality (\(\mathbb{R}^1_t\) is linear and irreversible)
- Encodes cyclic environmental structure (\(T^k\))
- Decays beliefs correctly (confidence decay on \(\mathbb{R}^1_t\), modulated by \(\delta_{eff}(\tau)\))
- Is fully auditable (named belief vectors, dual-axis audit trail, semaphore log)
- Is operationally instantiated (7,903,126 belief vectors, 48 collections, 30/30 preflight gate, April–May 2026, Fayette County WV)

The architecture was built to answer questions about hunger and land ownership in Appalachia — and in doing so, it discovered a temporal geometry suited to robot world models. The geographic grounding of \(H_{App}\) is not incidental; as argued in Kidd (2026a, §7), the spatial and relational structure of knowledge about specific places gives \(H_{App}\) its specific geometry. The system runs in ZIP code 25880. The mathematics followed from the place.

---

## Acknowledgments

Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd in collaboration with community partners in West Virginia. The `fayettecountyresources2026` collection was contributed by Crystal D. Colyer, Community Solutions Advocate, whose community resource documentation work made the operational validation in Section 2 possible. Any errors or oversights in the theoretical framing are the author's responsibility alone.

---

## References

Busemeyer, J.R. and Bruza, P.D. (2012). *Quantum Models of Cognition and Decision*. Cambridge University Press.

Dirac, P.A.M. (1930). *The Principles of Quantum Mechanics*. Oxford University Press.

Einstein, A. (1955). Letter to the family of Michele Besso. March 21, 1955.

Halmos, P.R. (1957). *Introduction to Hilbert Space and the Theory of Spectral Multiplicity*. Chelsea.

Husemoller, D. (1994). *Fibre Bundles*. 3rd ed. Springer-Verlag.

Kidd, C.A. (2026a). A Classical Hilbert Space with a ZIP Code: Substrate-Independence, the Measurement Problem, and the Multiverse Question. *Zenodo*. https://doi.org/10.5281/zenodo.20059834

Kidd, C.A. (2026b). Ms. Egeria Allis Thesis — Chapter 4: Hilbert Space State and ChromaDB as Semantic Memory. Technical documentation. H4HWV2011/msjarvis-public-docs, GitHub. [Archival deposit pending; current version at https://github.com/H4HWV2011/msjarvis-public-docs]

Kidd, C.A. (2026c). Ms. Egeria Allis Thesis — Chapter 26: Temporal Toroidal Semaphore Structure. Technical documentation. H4HWV2011/msjarvis-public-docs, GitHub. [Archival deposit pending; current version at https://github.com/H4HWV2011/msjarvis-public-docs]

Mildenhall, B., Srinivasan, P.P., Tancik, M., Barron, J.T., Ramamoorthi, R., and Ng, R. (2020). NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis. *ECCV 2020*.

Minkowski, H. (1908). Space and Time. Address delivered at the 80th Assembly of German Natural Scientists and Physicians, Cologne.

Moser, E.I., Kropff, E., and Moser, M.-B. (2008). Place cells, grid cells, and the brain's spatial representation system. *Annual Review of Neuroscience*, 31, 69–89.

Nielsen, M.A. and Chuang, I.L. (2000). *Quantum Computation and Quantum Information*. Cambridge University Press.

Pothos, E.M. and Busemeyer, J.R. (2013). Can quantum probability provide a new direction for cognitive modeling? *Behavioral and Brain Sciences*, 36(3), 255–274.

Reed, M. and Simon, B. (1972). *Methods of Modern Mathematical Physics I: Functional Analysis*. Academic Press.

Rudin, W. (1976). *Principles of Mathematical Analysis*. 3rd ed. McGraw-Hill.

Thrun, S., Burgard, W., and Fox, D. (2005). *Probabilistic Robotics*. MIT Press.

von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik*. Springer. (English translation: *Mathematical Foundations of Quantum Mechanics*, Princeton University Press, 1955.)

Wheeler, J.A. (1990). Information, physics, quantum: The search for links. In W. Zurek (Ed.), *Complexity, Entropy, and the Physics of Information*. Addison-Wesley.

Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics*, 75(3), 715–775.

---

*Authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
*Original draft: May 5, 2026. Version 2.0 (academically revised): May 7, 2026.*
*This paper builds directly on Kidd (2026a), DOI: 10.5281/zenodo.20059834.*
