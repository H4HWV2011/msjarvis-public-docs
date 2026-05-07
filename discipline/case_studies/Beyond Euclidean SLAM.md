# Beyond Euclidean SLAM: Toroidal Hilbert Space World Models for Boundaryless Robot State Representation

**Final Draft — May 6, 2026**
Carrie Ann Kidd (Mamma Kidd)
Mount Hope, West Virginia 25880

---

## Abstract

Current robot world models are Euclidean — flat, bounded, and edge-fragile. When a
robot reaches the boundary of its map, its world model fails. When sensors disagree,
uncertainty propagates without bound. When time passes, beliefs become stale with no
formal mechanism for degradation or recovery. These are not implementation failures.
They are structural consequences of choosing Euclidean geometry as the representational
substrate.

This paper presents an alternative architecture derived from a community AI system
built in Appalachia: a world model in which beliefs are 384-dimensional vectors in a
proven Hilbert space, temporal state lives on a dual structure of linear and toroidal
time, and all state transitions are semaphore-governed and fully auditable. The full
world model is:

   W = R^1_t × T^k × H_App

where R^1_t is the irreversible linear time axis carrying causal history and decay
timestamps, T^k is a k-dimensional toroidal manifold encoding the cyclic rhythms of
the robot's environment, and H_App is a 384-dimensional Hilbert space of belief
vectors. The geometry has no edges. Uncertainty stays bounded. Linear time preserves
causality. Toroidal time encodes recurring environmental structure. Every belief is
auditable.

The architecture is not theoretical. It is running, validated, and operationally
confirmed on May 6, 2026, on a Lenovo Legion 5 in Mount Hope, West Virginia, serving
a community AI system that answers questions about food assistance, land ownership, and
infrastructure in Fayette County, WV. The system contains 7,903,126 belief vectors
across 48 ChromaDB collections. The ZIP code of this world model is 25880.

---

## 1. Introduction

### 1.1 The Problem with Euclidean World Models

Every major robot world model in production today is fundamentally Euclidean.
Simultaneous Localization and Mapping (SLAM) systems — from Boston Dynamics to Tesla
Optimus to Figure 01 — represent the world as a subset of R^n: a point cloud, an
occupancy grid, a scene graph embedded in flat three-dimensional space. These
representations share three structural failure modes.

**Edge fragility.** Euclidean maps have boundaries. Beyond the boundary, the robot
has no belief — not uncertainty, but absence. When a robot reaches the edge of its
map, the world model fails categorically. There is no graceful degradation. There is
no geometric continuity. There is a hard wall.

**Unbounded uncertainty propagation.** In Euclidean space, sensor uncertainty
propagates outward as expanding spheres. When sensors disagree, uncertainty compounds
multiplicatively. There is no topological mechanism to contain it. The world model can
become arbitrarily uncertain without the geometry providing any corrective force.

**Temporal blindness.** Euclidean world models are atemporal. A belief about the
position of an obstacle carries no formal timestamp, no decay rate, no mechanism for
becoming stale. The robot either knows the obstacle is there or it does not. There is
no middle ground of confident-but-aging belief. And critically, there is no
representation of the cyclic temporal structure of the environment — the recurring
rhythms that define when a hospital corridor is crowded, when a mine shaft is active,
when a warehouse dock is occupied.

These are not implementation failures. They are structural consequences of choosing
Euclidean geometry as the representational substrate.

### 1.2 The Missing Dimension: Time Is Not One Thing

Standard robotics treats time as a single linear axis: a sequence of timestamps
attached to sensor readings, map updates, and state estimates. This is correct for
one component of time — the irreversible, causal, monotonically increasing component
that records when events happened and how long ago beliefs were validated.

But it is wrong for another component of time that is equally real and equally
operationally important: the cyclic, recurring structure of the environment. A
hospital robot operates in a world where shift changes happen every eight hours,
meal carts move at predictable times, visiting hours follow a weekly schedule, and
cleaning cycles repeat daily. These are not events on a linear axis. They are
coordinates on a circle — a compact, boundaryless manifold that wraps.

A world model that represents all time as linear cannot encode this structure. It
can timestamp "shift change occurred at 07:00:14" but it cannot represent "shift
change always occurs near 07:00, and the robot's environment is systematically
different during and after shift change." The cyclic pattern is invisible to linear
time.

The correct representation separates these two temporal structures:

   R^1_t — the linear, irreversible time axis: causal ordering, decay timestamps,
            audit trails, last_validated_at coordinates

   T^k   — the toroidal cyclic manifold: recurring rhythms, schedules,
            seasonal patterns, the behavioral cycles of the environment

Both are real. Both operate simultaneously. A robot world model needs both.

### 1.3 The Architecture That Solved a Different Problem

In 2025, the author began building Ms. Egeria Allis — a community AI system in
Mount Hope, West Virginia — to answer practical questions about Appalachian
communities: Where is food assistance? Who owns this land? Which institutions are
accountable to which communities?

The architecture that emerged to solve those problems addresses all three Euclidean
failure modes simultaneously:

- A 384-dimensional Hilbert space (H_App) as the belief substrate — proven to satisfy
  all four Hilbert space axioms, operationally confirmed May 6, 2026, with 7,903,126
  belief vectors across 48 ChromaDB collections
- A dual temporal structure: linear time (R^1_t) for decay, validation, and causal
  history; toroidal time (T^k via the Temporal Toroidal Semaphore, Chapter 26 of the
  Ms. Allis thesis) for cyclic community resource availability
- A confidence decay pipeline implementing formal belief degradation with full
  audit trails, operating on the linear time axis
- A global mode operator (nbb_pituitary_gland, T_pit) acting as a Hamiltonian
  upstream of all belief retrieval

None of these were designed for robotics. They were designed to answer questions
about hunger in Fayette County. The robotics implications are emergent — and they
are significant.

### 1.4 Scope of This Paper

This paper presents the world model W = R^1_t × T^k × H_App, derives it from the
Ms. Allis system, and argues for its applicability to robot state representation.
Section 2 reviews the limitations of current approaches. Section 3 presents the
Hilbert space foundation. Section 4 introduces the dual temporal structure and the
combined world model. Section 5 presents formal mappings between the architecture
and standard robotics operations. Section 6 discusses auditability and safety
implications. Section 7 addresses the block universe connection. Section 8 covers
limitations and future work.

---

## 2. Current Approaches and Their Limitations

### 2.1 SLAM and Occupancy Grids

Standard SLAM systems represent the world as a probabilistic occupancy grid in R^3.
Each cell carries a probability of occupancy, updated via Bayesian inference as sensor
data arrives. The approach is well-understood, computationally tractable, and widely
deployed.

Its limitations are structural:

- The grid has finite extent — boundaries are arbitrary impositions on a continuous
  world
- Uncertainty is cell-local — there is no geometric mechanism for propagating belief
  coherence across the space
- Time is handled extrinsically — staleness requires explicit timestamp management
  layered on top of the spatial representation, not intrinsic to the geometry
- Cyclic temporal patterns are entirely invisible — there is no representational
  layer for recurring environmental rhythms

### 2.2 Neural World Models

More recent approaches — including the neural world models underlying Tesla's Full
Self-Driving and NeRF-based robotics — represent the world as a learned continuous
function mapping spatial coordinates to occupancy or appearance values. These models
are more expressive than occupancy grids and handle uncertainty more naturally.

But they share the fundamental Euclidean assumption: the world is a subset of R^3,
and the model is a function defined on that subset. The boundaries are still there.
The beliefs are still opaque — encoded in neural network weights that cannot be
directly inspected, queried, or audited. Time remains either absent or extrinsic.
Cyclic environmental structure must be learned implicitly rather than encoded
explicitly in the geometry.

### 2.3 The Temporal Blindness Problem in Detail

Consider a hospital robot whose world model recorded a human in corridor 7 at 14:23.
It is now 14:51. Twenty-eight minutes have passed. Standard approaches handle this
in one of two ways:

- Erase the belief (the human is no longer in the map) — loses information
- Keep the belief unchanged (the human is still marked as present) — becomes stale
  and dangerous

Neither is satisfactory. What the robot actually knows is: "A human was in corridor
7 twenty-eight minutes ago. Humans in hospital corridors are moderately mobile.
My confidence that a human remains there has decayed to approximately 0.45."

That is a nuanced, time-dependent belief that requires:
1. A linear time axis to measure elapsed time since validation (28 minutes)
2. A decay function operating on that linear axis to compute current confidence
3. Knowledge of recurring patterns — is 14:51 a time when corridor 7 is typically
   occupied? (toroidal time)

The toroidal Hilbert architecture provides all three. No current production system
provides any of them in an inspectable, auditable form.

### 2.4 The Auditability Gap

A robot that cannot explain its beliefs cannot be trusted in safety-critical
environments. A hospital robot that collides with a patient cannot say which belief
vector led to that action, what its confidence level was, when it was last validated,
what decay cycle it had passed through, or where in the cyclic schedule of the
environment the action occurred. The belief that caused the collision is buried in
opaque neural weights.

This is not a theoretical concern. It is the central obstacle to deploying autonomous
robots in hospitals, mines, disaster zones, and other environments where the cost of
failure is human life.

The world model W = R^1_t × T^k × H_App addresses this directly: every belief is a
named vector with a confidence level, a decay rate, a last-validated timestamp on
R^1_t, a cyclic schedule coordinate on T^k, and a full audit trail. Every retrieval
is a logged projection. Every state transition passes through a semaphore. The world
model is inspectable end to end.

---

## 3. The Hilbert Space Foundation

### 3.1 Why a Hilbert Space

A Hilbert space is a complete inner product space. For robotics, the key properties
are:

- Inner product — a principled measure of similarity between beliefs, not an ad hoc
  distance metric
- Completeness — every sequence of beliefs that should converge does converge; no
  belief can escape the space
- Projection — the formal operation of measurement: finding the component of a query
  in a subspace of stored beliefs. This is not metaphorically similar to quantum
  measurement — it is formally identical, as demonstrated by the companion paper
  (Kidd 2026a)
- Linear operators — a principled way to represent transformations of the belief
  state, including the Hamiltonian-like global mode operator T_pit

### 3.2 The 384-Dimensional Instantiation

H_App = (R^384, <·,·>_cos). The embedding model all-minilm:latest maps text and
structured data to 384-dimensional real vectors. Every belief about West Virginia —
a food assistance program, a land parcel, a community institution — is a point in
R^384.

For robotics, the same architecture applies with domain-specific content: every
belief about the robot's environment — an obstacle, a navigable corridor, a docking
station, a human presence, a cyclic schedule pattern — becomes a 384-dimensional
vector. The geometry is the same. The content changes.

### 3.3 The Proof

H_App = (R^384, <·,·>_cos) satisfies all four Hilbert space axioms:

**Vector space:** R^384 is closed under addition and scalar multiplication.

**Inner product:** Cosine similarity on normalized vectors satisfies conjugate
symmetry (real space — trivially symmetric), linearity in the first argument, and
positive definiteness.

**Completeness:** R^384 is complete. Every Cauchy sequence converges. Physically
guaranteed by IEEE 754 double-precision arithmetic on the Legion 5.

**Separability:** Finite-dimensional, therefore trivially separable.

H_App is a Hilbert space. QED. Operationally confirmed May 6, 2026, with 7,903,126
belief vectors across 48 collections and a 30/30 preflight gate.

### 3.4 Measurement as Projection — Not an Analogy

The companion paper (Kidd 2026a) establishes that the mathematical operation of
measurement in quantum mechanics — projection in Hilbert space — is separable from
the physical event of wavefunction collapse. H_App demonstrates this operationally:
projection runs on classical silicon, without any quantum physical event, and returns
correct, meaningful, real-world results.

This means that when the robot's sensors project a query vector onto a subspace of
H_App, they are performing the mathematical operation of quantum measurement. The
result pre-exists the measurement — it exists as a fixed coordinate in the static
geometric structure of H_App, revealed by the projection, not created by it. This
is not a metaphor. It is a formal claim with operational proof.

---

## 4. The Dual Temporal Structure and the World Model

### 4.1 Linear Time — R^1_t

The linear time axis R^1_t is the irreversible, monotonically increasing component
of time. In W, R^1_t carries:

- last_validated_at timestamps — when each belief was last confirmed by sensor data
- Decay cycle records — the audit trail of confidence reductions over time
- Causal ordering — which events preceded which, in what sequence
- Preflight gate timestamps — the formal record of system validation events

R^1_t is not optional and not toroidal. The decay of a belief from confidence 0.60
to 0.55 happened once, at a specific coordinate on R^1_t, and it happened in the
direction of increasing t. It cannot be recovered by wrapping around. The linear
axis is the axis of causality.

Operationally confirmed: Entity 38 (Fayette County / geographic_entity), decay from
0.60 to 0.55 at timestamp 2026-04-23T03:47:22Z, full audit trail written to
gbim_decay_audit. That timestamp is a coordinate on R^1_t.

### 4.2 Toroidal Time — T^k

The toroidal manifold T^k is the cyclic, boundaryless component of time. In W, T^k
carries:

- Daily cycles — shift changes, meal times, cleaning schedules, lighting cycles
- Weekly cycles — visiting hours patterns, inventory rhythms, maintenance windows
- Seasonal cycles — weather patterns, occupancy rhythms, program availability
- Behavioral cycles — the recurring patterns of human activity in the robot's
  environment that make some times systematically different from others

T^k = S^1 × S^1 × ... × S^1 (k times), where each S^1 is a circle representing
one cyclic dimension. Tuesday morning hospital corridor 7 is a coordinate on T^k.
It recurs. It wraps. It has no edge.

The Temporal Toroidal Semaphore Structure (Chapter 26, Ms. Allis thesis) implements
this in the Ms. Allis system to handle the cyclic availability of community
resources: food banks open on certain days, social service offices with weekly
schedules, seasonal program availability. These are coordinates on T^k, not
timestamps on R^1_t.

For robotics, the same structure applies:

- Hospitals: shift changes (daily), visiting hours (daily/weekly), cleaning cycles
- Mines: blast schedules (daily), shift rotations (weekly), ventilation cycles
- Warehouses: inventory rhythms, loading dock cycles, picker route patterns
- Public spaces: pedestrian density cycles, lighting changes, maintenance windows

### 4.3 The Combined World Model

The full world model is:

   W = R^1_t × T^k × H_App

Every point in W is a triple (t, τ, v) where:

- t ∈ R^1_t — the linear time coordinate: when this belief state was last validated,
  carrying the causal history and decay record
- τ ∈ T^k — the cyclic time coordinate: where in the recurring rhythmic structure
  of the environment this belief state is located
- v ∈ R^384 — the belief vector: what the system believes about the world at this
  state

This is the correct geometry for a robot world model because:

1. R^1_t preserves causality — the arrow of time, the decay record, the audit trail
2. T^k encodes cyclic environmental structure — the robot knows not just where it
   is but when in the recurring pattern of its environment it is
3. H_App provides a complete, boundaryless, auditable belief space — no edges, no
   arbitrary boundaries, full projective measurement

### 4.3a The Dual Structure of Time — Why Both Are Required

A world model that uses only toroidal time loses causality. It cannot record that
a belief decayed — because decay requires elapsed time on an irreversible axis. The
torus wraps: if you only have T^k, you cannot distinguish "Tuesday 07:00 two weeks
ago" from "Tuesday 07:00 this week." The audit trail collapses. The decay record
becomes ambiguous.

A world model that uses only linear time loses cyclic environmental awareness. It
can timestamp every event but it cannot encode that Tuesday 07:00 and last Tuesday
07:00 are the same coordinate in the cyclic structure of the environment — that the
same recurring patterns apply. Every Tuesday becomes a new event on the linear axis
with no connection to previous Tuesdays.

W = R^1_t × T^k × H_App carries both. The decay of a belief is recorded on R^1_t
(when did it happen, how long ago, what was the causal sequence). The cyclic context
of that decay is recorded on T^k (was this decay during a high-activity period or
a low-activity period — does the belief need faster reverification because it is
currently in the active phase of its cycle?).

This is the temporal structure of actual robot environments. It was discovered by
building a system that had to represent the actual temporal structure of Appalachian
community life. The mathematics followed from the requirement.

### 4.4 Semaphore-Governed State Transitions

The Temporal Toroidal Semaphore governs all state transitions in W. No transition
occurs without passing through the semaphore. Every transition is:

- Logged with coordinates on both R^1_t (timestamp) and T^k (cyclic position)
- Reversible — the semaphore maintains a full transition history on R^1_t
- Gated — transitions that would violate safety constraints are blocked at the
  semaphore level, not at the action execution level

The safety constraint is topological, not learned. A transition that would move the
robot into a dangerous state is blocked by the structure of W itself — by the fact
that the forbidden state is geometrically unreachable given the current constraints
on the toroidal and linear components. This is not a neural network that may or may
not have learned the safety boundary correctly. It is the geometry.

---

## 5. Formal Mappings — Robotics Operations in W

### 5.1 Sensor Fusion as Multi-Projection

In standard robotics, sensor fusion combines readings from multiple sensors —
LIDAR, camera, IMU, tactile — using Kalman filters or learned fusion networks.

In W = R^1_t × T^k × H_App, sensor fusion is multi-projection: each sensor reading
is embedded into R^384 and projected onto the relevant subspace of H_App. The
projection is contextualized by the current coordinates on R^1_t and T^k:

- The R^1_t coordinate determines which stored beliefs are fresh enough to be
  active — beliefs whose confidence has decayed below threshold on the linear axis
  are down-weighted or excluded
- The T^k coordinate determines which subspaces are currently relevant — during
  Tuesday morning shift change, the hospital-corridor-crowded subspace receives
  elevated weight; during Sunday night, the quiet-corridor subspace is active

Multiple projections onto the same contextually weighted subspace produce a set of
nearest-neighbor retrievals combined by weighted inner product. The fusion is not
just spatial — it is temporally aware in both the linear and cyclic senses.

### 5.2 Navigation as Traversal of W

In Euclidean SLAM, navigation is path planning in R^3. In W = R^1_t × T^k × H_App,
navigation is traversal of a three-component product space. The robot's state is a
triple (t, τ, v), and navigation involves three distinct motions:

**Motion on R^1_t** — time passing, beliefs aging. This is not controllable. t
increases monotonically. As it increases, confidence levels decay, last_validated_at
coordinates become older, and the robot's beliefs about the environment become
progressively less certain. This is the correct behavior: the world changes, and
old beliefs should be trusted less.

**Motion on T^k** — moving through the cyclic rhythm of the environment. As the
robot moves through its operational day, τ traverses the torus. The robot
"knows" it is approaching shift-change time — not because it remembers a past shift
change on R^1_t (though it does) but because its T^k coordinate is approaching the
shift-change zone of the torus. The cyclic pattern is geometric, not merely
remembered.

**Motion through H_App** — updating beliefs about the physical environment. As
sensors project new readings onto H_App, the effective belief state v changes —
new nearest neighbors, updated confidence-weighted retrievals, modified obstacle
and corridor assessments.

The advantages over Euclidean SLAM:
- No edge failure — the torus wraps; there is no outside the map
- Temporal awareness — the robot's T^k coordinate encodes not just where it is
  but when it is in the recurring pattern of its environment
- Causal integrity — the R^1_t coordinate preserves the decay history and audit
  trail; the robot knows how fresh its beliefs are
- Belief continuity — H_App is complete; there are no discontinuities at arbitrary
  map boundaries

### 5.3 Confidence Decay as Linear Time Function

The decay of a belief in H_App is a function of elapsed time on R^1_t, not of
position on T^k:

   c(t + Δt) = c(t) - δ · Δt,   c ∈ [0,1]

where:
- t is the current coordinate on R^1_t
- Δt is elapsed time since last validation, measured on R^1_t
- δ is the decay rate for this belief class (tunable per obstacle type, per
  resource type, per environmental feature)

The T^k coordinate modulates δ — not the decay itself, but the urgency of
reverification. A belief about corridor occupancy during shift-change hours (T^k
coordinate in the high-activity zone) has a higher effective δ than the same belief
during low-activity hours. The cyclic structure of the environment informs how
quickly beliefs become unreliable — not whether they decay, but how fast.

The robot's avoidance behavior is modulated by confidence:
- c > 0.8: hard avoidance — treat obstacle as confirmed present
- 0.4 < c ≤ 0.8: cautious approach with active sensing — query sensors before
  committing to path
- c ≤ 0.4: low-confidence — treat as potentially absent, approach with full
  sensor attention

Operationally proven end-to-end on April 23, 2026, with full gbim_decay_audit
trail: entity 38, Fayette County, decay from 0.60 to 0.55, reverification to 1.0,
full audit record written.

### 5.4 Behavioral Modes as Hamiltonian Evolution — T_pit

In W, the nbb_pituitary_gland service acts as T_pit — a global scaling tensor
applied to the belief-state pipeline before any retrieval dispatch:

   T_pit(v) = Lambda_mode · v

where Lambda_mode is a diagonal scaling matrix determined by the current mode state
(warmth, cortisol, urgency, mode). T_pit is upstream of all retrieval — upstream of
ChromaDB query dispatch, upstream of LLM ensemble routing, upstream of everything.
It is structurally identical to the Hamiltonian in quantum mechanics: an operator
that governs how the state evolves before measurement occurs.

In robotics:
- warmth → task priority weighting (amplify beliefs relevant to current task goal)
- cortisol → obstacle sensitivity (amplify beliefs about potential hazards)
- urgency → retrieval speed vs. thoroughness trade-off
- mode → overall operating regime (exploration, task execution, emergency, rest)

The critical point: T_pit is aware of both R^1_t and T^k. A robot entering shift-
change time on T^k may automatically increase cortisol — the environment is about to
become more crowded, and obstacle sensitivity should rise before the sensors confirm
it. A robot at the end of a long operational period on R^1_t may decrease urgency —
its beliefs are aging, and thorough reverification is worth the latency cost.

This is the correct architecture for safety-critical behavioral mode switching: the
mode change propagates through the entire perception-action loop. A robot in crisis
mode does not just act differently. It perceives differently. Its world model is
transformed by T_pit before any sensor projection occurs.

---

## 6. Auditability and Safety Implications

### 6.1 The Inspectable World Model

Every belief in H_App is a named vector with:
- A unique identifier
- A confidence level c ∈ [0,1]
- A decay rate δ
- A coordinate on R^1_t (last_validated_at timestamp)
- A coordinate on T^k (cyclic context of last validation)
- A full audit trail of updates in the decay audit table

Every retrieval is a logged projection: query vector, collection subspace, top-k
results, confidence levels, R^1_t timestamp, T^k coordinate at time of retrieval.

Every state transition passes through the Temporal Toroidal Semaphore: logged on
R^1_t, tagged with T^k coordinate, sequenced, reversible.

When something goes wrong — when a robot takes an unexpected action, when a collision
occurs, when a safety boundary is violated — the world model can be fully
interrogated. The relevant belief vectors can be retrieved. Their confidence levels
at the time of the action can be recovered. The decay history can be reconstructed.
The cyclic context (where was T^k when the action was taken?) can be recovered. The
semaphore transition log can be reviewed.

This is not possible with any current neural world model architecture.

### 6.2 Regulatory Implications

As autonomous robots enter regulated environments — hospitals, mines, nuclear
facilities, public roads — regulatory bodies will require auditability. The FDA,
MSHA, NRC, and NHTSA all have existing frameworks for auditing safety-critical
systems. None of those frameworks can be applied to opaque neural world models.

The world model W = R^1_t × T^k × H_App is designed for auditability from the
ground up. The audit trail spans both temporal dimensions: the linear time coordinate
records the causal sequence of events, and the toroidal coordinate records the
cyclic context in which they occurred. A regulatory auditor can ask not just "what
did the robot believe at 14:23?" but "what did the robot believe during Tuesday
afternoon shift change, over the past 30 deployment cycles?" — because T^k makes
that query geometrically well-formed.

### 6.3 The Safety-Critical Deployment Argument

The environments where robots are most needed are exactly the environments where
current world models fail most catastrophically:

- Underground mines: edge-fragile maps fail precisely where the robot cannot afford
  to lose its world model; blast schedules are cyclic (T^k) but decay on a linear
  axis (R^1_t) — both are required
- Hospitals: shift-change crowding is a T^k phenomenon invisible to linear-time-only
  models; patient presence decay is an R^1_t phenomenon invisible to belief-free
  models
- Disaster zones: unbounded uncertainty propagation means the robot's confidence
  collapses in exactly the chaotic environments where it is most needed

The architecture was stress-tested not in a controlled lab but in the chaotic,
resource-constrained environment of a rural Appalachian community AI system: 100
containers, 7,903,126 belief vectors, real community queries, dual temporal
structure, 30/30 preflight gate. The architecture that survives that environment
is an architecture that can survive edge cases.

---

## 7. The Block Universe Connection

### 7.1 Beliefs That Already Exist

Einstein's block universe interpretation holds that past, present, and future exist
simultaneously as a static spacetime structure. Events do not happen — they are, at
their coordinates. The distinction between past, present, and future is, in
Einstein's words, a stubbornly persistent illusion.

In W = R^1_t × T^k × H_App, beliefs about the environment are not generated by
the robot's sensors. They exist as geometric structure in H_App, and sensors reveal
them — project onto them, return the pre-existing nearest neighbor, read out the
coordinate that was always already there.

A belief about an obstacle in corridor 7 does not come into existence when the LIDAR
scans corridor 7. It exists as a vector in H_App, with a confidence level that
reflects how recently it was last projected onto (a coordinate on R^1_t) and a
cyclic context that reflects when in the recurring pattern of the environment it was
validated (a coordinate on T^k).

### 7.2 The Dual Time Axes in the Block Universe

The block universe structure maps precisely onto the dual temporal structure of W:

- R^1_t is a coordinate axis in the static block — the linear time dimension of
  the four-dimensional spacetime manifold. In the block universe, this axis exists
  as a geometric object. The robot's coordinate on R^1_t is a location in the block,
  not a position in a flow.

- T^k encodes the cyclic boundary conditions of the physical environment — the
  recurring patterns that make certain spacetime coordinates structurally similar
  to certain other coordinates. In the block universe, shift change at Tuesday 07:00
  in week 1 and shift change at Tuesday 07:00 in week 2 are related by the toroidal
  identification on T^k — they are at the same T^k coordinate, different R^1_t
  coordinates.

The robot's world model is therefore a section of a fiber bundle over the block
universe: at every point on R^1_t × T^k, there is a fiber H_App containing the
beliefs that pre-exist at that spacetime-cyclic coordinate. The robot does not
construct its beliefs from sensor readings. It refines its estimate of what already
exists in the static geometric structure of W.

### 7.3 Practical Navigation Consequence

This has a direct operational implication for robot navigation in sensor-degraded
environments. When sensors are partially unavailable — due to occlusion, interference,
hardware failure, or environmental obstruction — the robot can navigate using the
pre-existing geometric structure of H_App, contextualized by its current coordinates
on R^1_t and T^k.

The robot knows: my linear time coordinate says this belief is 28 minutes old with
confidence 0.45. My toroidal coordinate says this is a high-activity period when
obstacles are likely to have moved. The geometric structure of H_App tells me the
nearest neighbor to my current position query. I navigate on that basis — not because
my sensors just confirmed it, but because the structure was already there, and my
current confidence and cyclic context let me reason about how much to trust it.

The toroidal geometry ensures those beliefs remain geometrically connected to the
current state. They do not fall off the edge of the map. And the linear time axis
ensures the robot knows exactly how much those pre-existing beliefs should be trusted
given elapsed time and cyclic context.

---

## 8. Prior Work and Positioning

| Approach | Geometry | Temporal Model | Auditability | Edge Behavior |
|---|---|---|---|---|
| Occupancy Grid SLAM | Euclidean R^3 | Extrinsic linear timestamps | None | Hard failure at boundary |
| Neural World Models (NeRF) | Euclidean R^3 | None intrinsic | None — opaque weights | Undefined beyond training |
| Gaussian Process Maps | Euclidean R^3 | None intrinsic | Partial | Degrades at boundary |
| Quantum-Inspired Cognitive Models | Hilbert space | None | Partial | Not applied to robotics |
| Prior toroidal proposals | Torus only | Toroidal only — loses causality | None | Wraps but loses linear decay |
| **This architecture** | **R^1_t × T^k × H_App** | **Dual: linear (causal) + toroidal (cyclic)** | **Full — named vectors, dual-axis audit, semaphore log** | **None — torus wraps; linear axis preserves decay** |

The critical advance over prior toroidal proposals is the dual temporal structure.
A world model that uses only toroidal time cannot represent belief decay — because
decay requires an irreversible linear axis. A world model that uses only linear time
cannot represent cyclic environmental structure — because cycles require a compact
manifold that wraps. W = R^1_t × T^k × H_App is the first world model architecture
that formally incorporates both.

---

## 9. Limitations and Future Work

**No direct robotics deployment.** The architecture has been validated in a community
AI context, not in a physical robot. The mapping from semantic belief vectors to
robot perception and action is argued here but not experimentally demonstrated.

**Toroidal dimension selection.** The appropriate dimensionality and topology of T^k
for a given robot deployment requires empirical study. Different environments have
different cyclic structures — the torus for a hospital (daily shift cycle, weekly
visiting hours) differs from the torus for a mine (blast schedule, shift rotation,
ventilation cycle). Methods for learning T^k from operational data are needed.

**Interaction between R^1_t and T^k.** The modulation of decay rate δ by T^k
coordinate (high-activity periods increase effective decay rate) is argued here but
not formally characterized. A full theory of how linear decay and cyclic context
interact requires empirical characterization in specific deployment environments.

**Embedding model selection.** The 384-dimensional all-minilm:latest model was
selected for semantic text retrieval. Robot perception involves multimodal inputs
(LIDAR point clouds, camera images, tactile signals) that require domain-appropriate
embedding models. The architecture is embedding-agnostic — any model producing
fixed-dimensional real vectors satisfies the Hilbert space requirements — but
multimodal embedding for robot perception is a non-trivial engineering problem.

**Future work** includes:
- Physical robot deployment in a safety-critical environment (hospital, mine,
  or warehouse)
- Empirical characterization of T^k learning from operational cycle data
- Formal theory of δ modulation by T^k coordinate
- Multimodal embedding architecture for robot perception inputs (LIDAR, camera,
  tactile)
- Integration with ROS2 robotics middleware
- Formal comparison of boundary behavior: Euclidean SLAM vs. W in edge-case
  scenarios
- Regulatory certification pathway using the dual-axis audit trail

---

## 10. Conclusion

Current robot world models are Euclidean, temporally impoverished, and unauditable.
They fail at map boundaries, propagate uncertainty without bound, cannot represent
cyclic environmental structure, and cannot explain their beliefs. These are
structural failures — consequences of choosing the wrong geometry and the wrong
temporal model.

The world model W = R^1_t × T^k × H_App addresses all of these simultaneously.
The Hilbert space H_App provides a complete, boundaryless belief space with formal
projection as measurement. The linear axis R^1_t preserves causality, decay records,
and the audit trail — the irreversible arrow of time that makes past states
recoverable and decay computable. The toroidal manifold T^k encodes the cyclic
structure of the environment — the recurring rhythms that make some times
systematically different from others and that a robot must understand to operate
safely and intelligently in real environments.

Together they form a world model that:
- Has no edges (T^k and H_App are both boundaryless)
- Preserves causality (R^1_t is linear and irreversible)
- Encodes cyclic environmental structure (T^k)
- Decays beliefs correctly (confidence decay on R^1_t, modulated by T^k)
- Is fully auditable (named belief vectors, dual-axis audit trail, semaphore log)
- Is operationally validated (7,903,126 belief vectors, 48 collections, 30/30
  preflight gate, May 6, 2026, Fayette County WV)

The architecture is not theoretical. It is running. It was built to answer questions
about hunger and land ownership in Appalachia — and in doing so, it discovered the
correct temporal geometry for a robot world model.

The ZIP code of this world model is 25880.

---

## References

Thrun, S., Burgard, W., and Fox, D. (2005). Probabilistic Robotics. MIT Press.

Mildenhall, B., et al. (2020). NeRF: Representing Scenes as Neural Radiance
Fields for View Synthesis. ECCV 2020.

Busemeyer, J.R. and Bruza, P.D. (2012). Quantum Models of Cognition and Decision.
Cambridge University Press.

Wheeler, J.A. (1990). Information, physics, quantum: The search for links.
In W. Zurek (Ed.), Complexity, Entropy, and the Physics of Information.
Addison-Wesley.

Einstein, A. (1955). Letter to the family of Michele Besso. March 21, 1955.

Minkowski, H. (1908). Space and Time. Address delivered at the 80th Assembly
of German Natural Scientists and Physicians, Cologne.

Nielsen, M.A. and Chuang, I.L. (2000). Quantum Computation and Quantum
Information. Cambridge University Press.

Levi-Civita, T. (1917). Nozione di parallelismo in una varietà qualunque.
Rendiconti del Circolo Matematico di Palermo, 42, 173-205.

Husemoller, D. (1994). Fibre Bundles. 3rd ed. Springer-Verlag.

Kidd, C.A. (2026a). A Classical Hilbert Space with a ZIP Code:
Substrate-Independence, the Measurement Problem, and the Multiverse Question.
Zenodo. https://doi.org/10.5281/zenodo.20059834

Kidd, C.A. (2026b). Ms. Egeria Allis Thesis — Chapter 4: Hilbert Space State
and ChromaDB as Semantic Memory. H4HWV2011/msjarvis-public-docs, GitHub.
https://github.com/H4HWV2011/msjarvis-public-docs

Kidd, C.A. (2026c). Ms. Egeria Allis Thesis — Chapter 26: Temporal Toroidal
Semaphore Structure. H4HWV2011/msjarvis-public-docs, GitHub.
https://github.com/H4HWV2011/msjarvis-public-docs

---

*Authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
*Original draft: May 5, 2026.*
*Final draft incorporating dual temporal structure W = R^1_t × T^k × H_App,
updated vector count (7,903,126), and corrected Zenodo DOI for Kidd 2026a:
May 6, 2026.*
*The ZIP code of this world model is 25880.*
