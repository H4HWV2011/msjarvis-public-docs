# Beyond Euclidean SLAM: Toroidal Hilbert Space World Models for Boundaryless Robot State Representation

**Version 3.0 — May 7, 2026**
Carrie Ann Kidd
Independent Researcher, Community GIS and Distributed AI Infrastructure
Mount Hope, West Virginia 25880 USA, Harmony for Hope Inc. (nonprofit founder)
ORCID: 0009-0005-8153-8025

---

> **Multimedia Overview**
>
> 🎧 **Audio overview:** [Toroidal Hilbert Spaces Fix Robot Navigation (m4a)](https://github.com/H4HWV2011/msjarvis-public-docs/releases/download/untagged-6a9b49320dbdeb6aa7a9/Toroidal_Hilbert_spaces_fix_robot_navigation.m4a)
>
> 🎬 **Video overview:** [The Donut-Shaped Math (mp4)](https://github.com/H4HWV2011/msjarvis-public-docs/releases/download/untagged-6a9b49320dbdeb6aa7a9/The_Donut-Shaped_Math.mp4)

---

![Conceptual overview: the world model W as a product of time axes and belief space](https://raw.githubusercontent.com/H4HWV2011/msjarvis-public-docs/main/discipline/case_studies/Gemini_Generated_Image_p8hrk8p8hrk8p8hr.png)

*Figure 0. Conceptual overview of the world model W = ℝ¹_t × T^k × H_App: linear time, toroidal cyclic structure, and a boundaryless Hilbert belief space combined into a single robot state representation.*

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

The architecture proposed here is derived from a deployed system. A full system description appears in Kidd (2026a, §2); this section provides a summary sufficient for the robotics arguments that follow.

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

### 3.2 Projection in H_App: Measurement Without Quantum Events

![Hilbert space projection: query vector projected onto belief corpus on S³⁸³](https://raw.githubusercontent.com/H4HWV2011/msjarvis-public-docs/main/discipline/case_studies/projection.png)

*Figure 1. Query projection in \(H_{App} = (\mathbb{R}^{384}, \langle\cdot,\cdot\rangle_{cos})\). A query vector \(\hat{q}\) is projected onto the corpus of belief vectors via cosine similarity; the nearest neighbor on \(S^{383} \subset \mathbb{R}^{384}\) is returned. The geometric structure pre-exists the query. Retrieval discloses; it does not create. No quantum physical event occurs. (Adapted from Kidd 2026a, Figures 1 and 3.)*

The embedding model all-minilm:latest maps text and structured data to 384-dimensional real vectors. Every belief about the robot's environment — an obstacle, a navigable corridor, a docking station, a human presence, a cyclic schedule pattern — becomes a unit vector \(\hat{v} \in S^{383} \subset \mathbb{R}^{384}\). Retrieval computes:

\[\text{sim}(\hat{q}, \hat{v}_k) = \langle \hat{q}, \hat{v}_k \rangle_{cos} = \sum_{i=1}^{384} \hat{q}_i \hat{v}_{k,i}\]

and selects the top-\(k\) nearest neighbors. This is projection in the Hilbert sense (Kidd 2026a, §4.1, Eq. 4).

### 3.3 Summary of Theorem 3.1 (Kidd 2026a)

\(H_{App} = (\mathbb{R}^{384}, \langle\cdot,\cdot\rangle_{cos})\) satisfies all four Hilbert space axioms:

**(i) Vector space structure.** \(\mathbb{R}^{384}\) is a vector space over \(\mathbb{R}\). For any \(u, v \in \mathbb{R}^{384}\) and \(a, b \in \mathbb{R}\), the linear combination \(au + bv \in \mathbb{R}^{384}\).

**(ii) Inner product.** For L2-normalized vectors \(\hat{u}, \hat{v} \in S^{383} \subset \mathbb{R}^{384}\), cosine similarity satisfies symmetry, linearity in the first argument (by linearity of the dot product), and positive-definiteness (\(\langle \hat{u}, \hat{u} \rangle_{cos} = \sum_{i=1}^{384} \hat{u}_i^2 \geq 0\), with equality iff \(\hat{u} = 0\)). The normalization requirement is enforced architecturally: ChromaDB normalizes embeddings before computing the inner product, so the operational inner product is the standard inner product on \(S^{383}\) lifted to \(\mathbb{R}^{384}\) via normalization.

**(iii) Metric completeness.** \(\mathbb{R}^{384}\) is complete under the norm induced by \(\langle\cdot,\cdot\rangle_{cos}\), as it coincides with the standard Euclidean norm up to equivalence. Completeness follows from completeness of \(\mathbb{R}\) and the fact that finite products of complete metric spaces are complete (Reed and Simon 1972).

**(iv) Separability.** As a finite-dimensional normed space, \(\mathbb{R}^{384}\) admits a finite (hence countable) orthonormal basis. Separability is trivially satisfied.

Therefore \(H_{App}\) is a Hilbert space. \(\square\)

For the robotics application, the critical structural properties are: (a) **inner product** — a principled similarity measure between beliefs; (b) **completeness** — no belief sequence that should converge can escape the space; (c) **projection** — formal measurement as nearest-neighbor retrieval in \(S^{383}\); and (d) **linear operators** — principled transformations of the belief state, including \(T_{pit}\) (Kidd 2026a, §4.3).

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

![Toroidal time structure: cyclic environmental rhythms encoded on T^k](https://raw.githubusercontent.com/H4HWV2011/msjarvis-public-docs/main/discipline/case_studies/torodial.png)

*Figure 2. Toroidal time \(T^k = S^1 \times S^1 \times \cdots \times S^1\). Each \(S^1\) encodes one cyclic dimension of the environment: daily shift changes, weekly visiting hours, seasonal patterns. Tuesday morning shift change is a coordinate on \(T^k\) — it recurs, it wraps, it has no edge. The robot knows not just where it is, but when it is in the recurring pattern of its environment.*

The toroidal manifold \(T^k\) is the cyclic, boundaryless component of time. \(T^k = S^1 \times S^1 \times \cdots \times S^1\) (\(k\) times), where each \(S^1\) is a circle representing one cyclic dimension. In \(W\), \(T^k\) carries:

- **Daily cycles** — shift changes, meal times, cleaning schedules, lighting cycles
- **Weekly cycles** — visiting hours patterns, inventory rhythms, maintenance windows
- **Seasonal cycles** — weather patterns, occupancy rhythms, program availability
- **Behavioral cycles** — the recurring patterns of human activity that make some times systematically different from others

The Temporal Toroidal Semaphore Structure (Kidd 2026c, Chapter 26) implements this in the Ms. Allis system for the cyclic availability of community resources. For robotics, the same structure applies to hospitals (shift cycles), mines (blast schedules), warehouses (dock cycles), and public spaces (pedestrian density rhythms).

The relevant neuroscientific precedent for toroidal spatial representations is the grid-cell system of the entorhinal cortex, which encodes spatial position on a structure with toroidal topology (Moser, Kropff, and Moser 2008). \(T^k\) in the present architecture encodes *temporal* rather than spatial coordinates, but the topological reasoning is the same: a compact, boundaryless manifold is the natural substrate for cyclic structure.

### 4.3 Why Both Temporal Components Are Required

A world model using only toroidal time loses causality. Without an irreversible axis, the system cannot record that a belief *decayed at a specific time*. The torus wraps: without \(\mathbb{R}^1_t\), the system cannot distinguish "Tuesday 07:00 two weeks ago" from "Tuesday 07:00 this week." The audit trail collapses.

A world model using only linear time loses cyclic environmental awareness. Every Tuesday becomes a new event on the linear axis with no geometric connection to previous Tuesdays. The recurring patterns that define when environments are dangerous, crowded, or active are invisible.

\(W = \mathbb{R}^1_t \times T^k \times H_{App}\) carries both. The decay of a belief is recorded on \(\mathbb{R}^1_t\) (when did it happen, how long ago). The cyclic context is recorded on \(T^k\) (was this decay during a high-activity period — does the belief need faster reverification?).

### 4.4 The Combined World Model

The full world model is:

\[W = \mathbb{R}^1_t \times T^k \times H_{App}\]

Every point in \(W\) is a triple \((t, \tau, v)\) where:

- \(t \in \mathbb{R}^1_t\) — the linear time coordinate: when this belief state was last validated, carrying the causal history and decay record
- \(\tau \in T^k\) — the cyclic time coordinate: where in the recurring rhythmic structure of the environment this belief state is located
- \(v \in \mathbb{R}^{384}\) — the belief vector: what the system believes about the world at this state

This is the correct geometry for a robot world model because: (1) \(\mathbb{R}^1_t\) preserves causality; (2) \(T^k\) encodes cyclic environmental structure; and (3) \(H_{App}\) provides a complete, boundaryless, auditable belief space with formal projective measurement.

### 4.5 Semaphore-Governed State Transitions

The Temporal Toroidal Semaphore (Kidd 2026c, Chapter 26) governs all state transitions in \(W\). No transition occurs without passing through the semaphore. Every transition is logged with coordinates on both \(\mathbb{R}^1_t\) (timestamp) and \(T^k\) (cyclic position), sequenced, and auditable. Transitions that would violate safety constraints are blocked at the semaphore level, not at the action execution level. The safety constraint is topological, not learned.

---

## 5. Formal Mappings — Robotics Operations in W

### 5.1 Sensor Fusion as Contextually Weighted Projection

In standard robotics, sensor fusion combines readings from multiple sensors — LIDAR, camera, IMU, tactile — using Kalman filters or learned fusion networks (Thrun et al. 2005, §3).

In \(W\), each sensor reading is embedded into \(\mathbb{R}^{384}\) as a unit vector \(\hat{s} \in S^{383}\) and projected onto the relevant subspace of \(H_{App}\). The projection is contextualized by the current coordinates on \(\mathbb{R}^1_t\) and \(T^k\):

- The \(\mathbb{R}^1_t\) coordinate determines which stored beliefs are fresh enough to be active — beliefs whose confidence has decayed below threshold are down-weighted or excluded
- The \(T^k\) coordinate determines which subspaces are currently relevant — during Tuesday morning shift change, the crowded-corridor subspace receives elevated weight; during Sunday night, the quiet-corridor subspace is active

Multiple projections onto the same contextually weighted subspace produce nearest-neighbor retrievals combined by weighted inner product. The fusion is temporally aware in both the linear and cyclic senses.

### 5.2 Navigation as Traversal of W

In Euclidean SLAM, navigation is path planning in \(\mathbb{R}^3\). In \(W\), the robot's state is a triple \((t, \tau, v)\) and navigation involves three simultaneous motions:

**Motion on \(\mathbb{R}^1_t\)** — time passing, beliefs aging. Not controllable; \(t\) increases monotonically. As it increases, confidence levels decay and beliefs become progressively less certain. This is the correct behavior: the world changes, and old beliefs should be trusted less.

**Motion on \(T^k\)** — moving through the cyclic rhythm of the environment. As the robot moves through its operational day, \(\tau\) traverses the torus. The robot "knows" it is approaching shift-change time because its \(T^k\) coordinate is approaching the shift-change zone — not merely because it remembers a past shift change on \(\mathbb{R}^1_t\). The cyclic pattern is geometric, not merely remembered.

**Motion through \(H_{App}\)** — updating beliefs about the physical environment. As sensors project new readings, the effective belief state \(v\) changes: new nearest neighbors, updated confidence-weighted retrievals, modified obstacle assessments.

Structural advantages over Euclidean SLAM: no edge failure (torus wraps); temporal awareness (\(T^k\) encodes cyclic environmental context); causal integrity (\(\mathbb{R}^1_t\) preserves decay history and audit trail); belief continuity (\(H_{App}\) is complete, no discontinuities at arbitrary map boundaries).

### 5.3 Confidence Decay as Linear Time Function with Cyclic Modulation

![Confidence decay pulse and revalidation cycle](https://raw.githubusercontent.com/H4HWV2011/msjarvis-public-docs/main/discipline/case_studies/pulse.png)

*Figure 3. Belief confidence decay in \(H_{App}\). Confidence \(c_n\) decrements per validation cycle on the linear axis \(\mathbb{R}^1_t\), then resets to \(c = 1.0\) on successful revalidation. The effective decay rate \(\delta_{eff}(\tau) = \delta_0 \cdot f(\tau)\) is modulated by the current \(T^k\) coordinate: beliefs age faster during high-activity phases (e.g., shift change) when the environment is more dynamic. Entity 38 (Fayette County), decay \(0.60 \to 0.55 \to 1.00\), verified April 23, 2026. (Adapted from Kidd 2026a, Figure 2.)*

The base decay of a belief in \(H_{App}\) is a function of elapsed time on \(\mathbb{R}^1_t\). The system currently implements linear decay (Kidd 2026a, §4.2, Eq. 6):

\[c_{n+1} = c_n - \Delta c, \quad c \in [0,1], \quad \Delta c = 0.05\]

per validation cycle, with reset to \(c = 1.0\) on successful revalidation.

For the robotics application, the architecture introduces cyclic modulation of the effective decay rate. Let:

\[\delta_{eff}(\tau) = \delta_0 \cdot f(\tau)\]

where \(\delta_0\) is the base decay rate for a given belief class, \(\tau \in T^k\) is the current cyclic time coordinate, and \(f: T^k \to \mathbb{R}^+\) is a non-negative modulation function satisfying \(f(\tau) > 1\) during high-activity phases (e.g., shift change, peak occupancy) and \(f(\tau) \leq 1\) during low-activity phases. The formal characterization of \(f\) for specific deployment environments — hospital, mine, warehouse — is a primary direction for future empirical work.

The robot's avoidance behavior is modulated by confidence level:
- \(c > 0.8\): hard avoidance — treat obstacle as confirmed present
- \(0.4 < c \leq 0.8\): cautious approach with active sensing — query sensors before committing to path
- \(c \leq 0.4\): low-confidence — treat as potentially absent, approach with full sensor attention

*Note on decay model selection:* linear decay is preferred here for auditability — the audit trail records discrete decay steps that are directly interpretable by a regulatory auditor. Exponential decay \(c(t) = c_0 e^{-\delta t}\) is standard in Bayesian occupancy filtering (Thrun et al. 2005, §9); the relative merits of linear versus exponential decay in safety-critical robot deployments is an open empirical question and a direction for future work.

### 5.4 Behavioral Modes as Hamiltonian Evolution — T_pit

![T_pit mode regulator: weighing warmth, cortisol, and urgency across the semantic space](https://raw.githubusercontent.com/H4HWV2011/msjarvis-public-docs/main/discipline/case_studies/Weighing.png)

*Figure 4. The \(T_{pit}\) mode regulator \(\Lambda_{mode}\) applies differential weights — warmth, cortisol, urgency — to the semantic space prior to projection in \(H_{App}\). This pre-shapes the effective state vector \(\hat{q}\), directly analogous to Hamiltonian evolution \(\hat{H}|\psi(t)\rangle\) acting between measurements. A robot entering shift-change time on \(T^k\) may automatically increase cortisol before sensors confirm crowding. (Adapted from Kidd 2026a, Figure 5.)*

In \(W\), the `nbb_pituitary_gland` service acts as \(T_{pit}\) — a global scaling tensor applied to the belief-state pipeline before any retrieval dispatch (Kidd 2026a, §4.3, Eq. 8):

\[T_{pit}(v) = \Lambda_{mode} \cdot v\]

where \(\Lambda_{mode}\) is a diagonal scaling matrix determined by the current mode state. \(T_{pit}\) is upstream of all retrieval — upstream of ChromaDB query dispatch, upstream of LLM ensemble routing. This is structurally analogous to the Hamiltonian in quantum mechanics: an operator that governs how the state is transformed before measurement occurs. The analogy is formal, not metaphorical: \(T_{pit}\) acts between queries precisely as \(\hat{H}\) acts between measurements in the Schrödinger picture (Kidd 2026a, §4.3).

In robotics:
- **warmth** → task priority weighting (amplify beliefs relevant to current task goal)
- **cortisol** → obstacle sensitivity (amplify beliefs about potential hazards)
- **urgency** → retrieval speed vs. thoroughness trade-off
- **mode** → overall operating regime (exploration, task execution, emergency, rest)

\(T_{pit}\) is aware of both \(\mathbb{R}^1_t\) and \(T^k\). Mode change propagates through the entire perception-action loop: a robot in crisis mode does not just act differently — it perceives differently.

---

## 6. Auditability and Safety Implications

### 6.1 The Inspectable World Model

Every belief in \(H_{App}\) is a named vector with: a unique identifier; a confidence level \(c \in [0,1]\); a decay rate \(\delta_0\) and modulation function \(f(\tau)\); a coordinate on \(\mathbb{R}^1_t\) (last\_validated\_at timestamp); a coordinate on \(T^k\) (cyclic context of last validation); and a full audit trail in the `gbim_decay_audit` table.

Every retrieval is a logged projection: query vector, collection subspace, top-\(k\) results, confidence levels, \(\mathbb{R}^1_t\) timestamp, \(T^k\) coordinate. Every state transition passes through the Temporal Toroidal Semaphore: logged on \(\mathbb{R}^1_t\), tagged with \(T^k\) coordinate, sequenced, auditable.

When something goes wrong, the world model can be fully interrogated. The relevant belief vectors can be retrieved. Their confidence levels at the time of the action can be recovered. The decay history can be reconstructed. The cyclic context can be recovered. The semaphore transition log can be reviewed. This is not possible with any current neural world model architecture.

### 6.2 Regulatory Implications

As autonomous robots enter regulated environments — hospitals, mines, nuclear facilities, public roads — regulatory bodies will require auditability. The FDA, MSHA, NRC, and NHTSA all have existing frameworks for auditing safety-critical systems. None of those frameworks can be applied to opaque neural world models.

The world model \(W = \mathbb{R}^1_t \times T^k \times H_{App}\) is designed for auditability from the ground up. A regulatory auditor can ask not just "what did the robot believe at 14:23?" but "what did the robot believe during Tuesday afternoon shift change, over the past 30 deployment cycles?" — because \(T^k\) makes that query geometrically well-formed.

### 6.3 The Safety-Critical Deployment Argument

The environments where robots are most needed are exactly the environments where current world models fail most catastrophically:

- **Underground mines:** edge-fragile maps fail precisely where the robot cannot afford to lose its world model; blast schedules are cyclic (\(T^k\)) but decay on a linear axis (\(\mathbb{R}^1_t\)) — both are required
- **Hospitals:** shift-change crowding is a \(T^k\) phenomenon invisible to linear-time-only models; patient presence decay is an \(\mathbb{R}^1_t\) phenomenon invisible to belief-free models
- **Disaster zones:** unbounded uncertainty propagation means the robot's confidence collapses in exactly the chaotic environments where it is most needed

The architecture was stress-tested not in a controlled lab but in a rural Appalachian community AI system: approximately 100 containers, 7,903,126 belief vectors, real community queries, dual temporal structure, 30/30 preflight gate.

---

## 7. The Block Universe Connection

![Block universe structure: static geometric belief space with coordinate access](https://raw.githubusercontent.com/H4HWV2011/msjarvis-public-docs/main/discipline/case_studies/block.png)

*Figure 5. Block-universe interpretation of \(H_{App}\). The 7,903,126 belief vectors constitute a static geometric structure analogous to the block spacetime of Minkowski and Einstein (1908, 1955): all coordinates co-exist. A query event (measurement) accesses a pre-existing coordinate; it does not instantiate a new one. The speed of light constrains signal propagation, not the pre-existence of the structure. (Adapted from Kidd 2026a, Figure 6.)*

### 7.1 Interpretive Framework

The block-universe interpretation, developed by Einstein (1955) and grounded in Minkowski's geometric formulation of special relativity (Minkowski 1908), holds that past, present, and future exist simultaneously as a static spacetime structure. The formal implications of this interpretation for the measurement problem — specifically, the claim that projection discloses pre-existing structure rather than creating it — are developed in detail in Kidd (2026a, §5). This section applies that framework to the robot navigation context.

The block-universe framing is an interpretive commitment, not a required architectural assumption; the operational properties of \(W\) hold independently of any particular interpretation of spacetime ontology.

### 7.2 Beliefs That Pre-Exist Measurement

In \(W\), following the interpretation developed in Kidd (2026a, §5.2–5.3), beliefs about the environment are not generated by the robot's sensors. They exist as geometric structure in \(H_{App}\), and sensors reveal them — project onto them, return the pre-existing nearest neighbor, read out the coordinate that was already there.

A belief about an obstacle in corridor 7 exists as a vector in \(H_{App}\) with a confidence level reflecting when it was last validated (a coordinate on \(\mathbb{R}^1_t\)) and a cyclic context (a coordinate on \(T^k\)). When LIDAR scans corridor 7, it does not create the belief; it updates the confidence level and refreshes the \(\mathbb{R}^1_t\) timestamp of a vector that already existed in the space.

### 7.3 The Dual Time Axes in the Block Universe

\(\mathbb{R}^1_t\) is a coordinate axis in the static block — the linear time dimension of the four-dimensional spacetime manifold. The robot's coordinate on \(\mathbb{R}^1_t\) is a location in the block, not a position in a flow.

\(T^k\) encodes the cyclic boundary conditions of the physical environment — the recurring patterns that make certain spacetime coordinates structurally similar to certain others. In the block universe, shift change at Tuesday 07:00 in week 1 and shift change at Tuesday 07:00 in week 2 are related by the toroidal identification on \(T^k\): at the same \(T^k\) coordinate, different \(\mathbb{R}^1_t\) coordinates. The robot's world model is therefore a section of a fiber bundle over the block universe: at every point on \(\mathbb{R}^1_t \times T^k\), there is a fiber \(H_{App}\) containing the beliefs that pre-exist at that spacetime-cyclic coordinate (Husemoller 1994).

### 7.4 Practical Navigation Consequence

When sensors are partially unavailable — due to occlusion, interference, hardware failure, or environmental obstruction — the robot can navigate using the pre-existing geometric structure of \(H_{App}\), contextualized by its current coordinates on \(\mathbb{R}^1_t\) and \(T^k\).

The robot knows: my linear time coordinate says this belief is 28 minutes old with confidence 0.45. My toroidal coordinate says this is a high-activity period when obstacles are likely to have moved. The geometric structure of \(H_{App}\) tells me the nearest neighbor to my current position query. I navigate on that basis — not because sensors just confirmed it, but because the structure was already there. The toroidal geometry ensures those beliefs remain geometrically connected to the current state; they do not fall off the edge of the map.

---

## 8. Prior Work and Positioning

| Approach | Geometry | Temporal Model | Auditability | Edge Behavior |
|---|---|---|---|---|
| Occupancy Grid SLAM (Thrun et al. 2005) | Euclidean \(\mathbb{R}^3\) | Extrinsic linear timestamps | None | Hard failure at boundary |
| Neural World Models / NeRF (Mildenhall et al. 2020) | Euclidean \(\mathbb{R}^3\) | None intrinsic | None — opaque weights | Undefined beyond training |
| Gaussian Process Maps | Euclidean \(\mathbb{R}^3\) | None intrinsic | Partial | Degrades at boundary |
| Quantum-Inspired Cognitive Models (Busemeyer and Bruza 2012; Pothos and Busemeyer 2013) | Hilbert space | None | Partial | Not applied to robotics SLAM |
| Toroidal spatial representations (Moser, Kropff, and Moser 2008) | Torus \(T^k\) | Toroidal only — loses linear causality | None in robotics | Wraps, but loses linear decay |
| **This architecture** | \(\mathbb{R}^1_t \times T^k \times H_{App}\) | **Dual: linear (causal) + toroidal (cyclic)** | **Full — named vectors, dual-axis audit, semaphore log** | **None — torus wraps; linear axis preserves decay** |

The critical advance over prior toroidal proposals is the dual temporal structure. Moser et al. (2008) establish toroidal topology in the neural encoding of spatial position; the present architecture extends toroidal geometry to the temporal domain while adding the irreversible linear axis required for decay auditability. The quantum-inspired cognitive modeling literature (Busemeyer and Bruza 2012; Pothos and Busemeyer 2013) establishes Hilbert space projection as a productive model for cognition; Kidd (2026a) establishes the operational and formal basis in a deployed system; the present paper extends it to robotics.

---

## 9. Limitations and Future Work

**No direct robotics deployment.** The architecture has been validated in a semantic community AI context, not in a physical robot. The mapping from semantic belief vectors to robot perception and action is argued here but not yet experimentally demonstrated. Physical robot deployment in a safety-critical environment is the primary direction for future work.

**Toroidal dimension selection.** The appropriate dimensionality and topology of \(T^k\) for a given robot deployment requires empirical study. Methods for learning \(T^k\) from operational cycle data are needed.

**Formal characterization of \(f(\tau)\).** The modulation function \(\delta_{eff}(\tau) = \delta_0 \cdot f(\tau)\) is argued here but not formally characterized. The functional form of \(f\) (sinusoidal, piecewise constant, learned) is an open question requiring empirical characterization in specific deployment environments.

**Decay model selection.** The relative performance of linear versus exponential decay in safety-critical robot deployments is an open empirical question.

**Embedding model selection.** Robot perception involves multimodal inputs (LIDAR point clouds, camera images, tactile signals) requiring domain-appropriate embedding models. The architecture is embedding-agnostic but multimodal embedding for robot perception is a non-trivial engineering problem.

**Future work includes:**
- Physical robot deployment in a safety-critical environment (hospital, mine, or warehouse) to empirically validate the formal mappings in Section 5
- Empirical characterization of \(T^k\) learning from operational cycle data
- Formal theory of \(f(\tau)\) in specific deployment contexts
- Multimodal embedding architecture for robot perception inputs (LIDAR, camera, tactile)
- Integration with ROS2 robotics middleware
- Formal comparison of boundary behavior: Euclidean SLAM vs. \(W\) in edge-case scenarios
- Regulatory certification pathway using the dual-axis audit trail
- Formal comparison of linear vs. exponential decay in the auditable robot world model context

---

## 10. Conclusion

Current robot world models are Euclidean, temporally impoverished, and unauditable. They fail at map boundaries, propagate uncertainty without bound, cannot represent cyclic environmental structure, and cannot explain their beliefs. These are structural failures — consequences of choosing the wrong geometry and the wrong temporal model.

The world model \(W = \mathbb{R}^1_t \times T^k \times H_{App}\) addresses all of these simultaneously. The Hilbert space \(H_{App}\) provides a complete, boundaryless belief space with formal projection as measurement (Kidd 2026a, Theorem 3.1). The linear axis \(\mathbb{R}^1_t\) preserves causality, decay records, and the audit trail. The toroidal manifold \(T^k\) encodes the cyclic structure of the environment. The decay modulation \(\delta_{eff}(\tau) = \delta_0 \cdot f(\tau)\) connects these two temporal structures, making the rate of belief aging sensitive to cyclic environmental context.

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
*Original draft: May 5, 2026. Version 3.0 (with figures and multimedia): May 7, 2026.*
*This paper builds directly on Kidd (2026a), DOI: 10.5281/zenodo.20059834.*
