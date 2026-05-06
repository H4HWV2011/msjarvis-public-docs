\documentclass[12pt,letterpaper]{article}

% ---- Packages ----
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{geometry}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{array}
\usepackage{parskip}
\usepackage{microtype}
\usepackage{cite}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{algorithm}
\usepackage{algpseudocode}

\geometry{margin=1in}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    citecolor=blue,
    urlcolor=blue,
    pdftitle={Beyond Euclidean SLAM},
    pdfauthor={Carrie Ann Kidd}
}

% ---- Theorem environments ----
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}{Definition}
\newtheorem{remark}{Remark}

% ---- Title ----
\title{
    \textbf{Beyond Euclidean SLAM:}\\
    \textbf{Toroidal Hilbert Space World Models for}\\
    \textbf{Boundaryless Robot State Representation}\\[1em]
    \large Preprint --- cs.RO / cs.AI
}

\author{
    Carrie Ann Kidd (Mamma Kidd)\\
    \textit{Mount Hope, West Virginia 25880}\\
    \texttt{H4HWV2011@github}\\[0.5em]
    \small Harmony for Hope Inc.\\
    \small Fayette County, West Virginia
}

\date{May 6, 2026}

% ================================================================
\begin{document}
\maketitle

% ---- Abstract ----
\begin{abstract}
Current robot world models are Euclidean --- flat, bounded, and edge-fragile.
When a robot reaches the boundary of its map, its world model fails. When sensors
disagree, uncertainty propagates without bound. When time passes, beliefs become
stale with no formal mechanism for degradation or recovery. These are not
implementation failures. They are structural consequences of choosing Euclidean
geometry as the representational substrate.

This paper presents an alternative: a \emph{toroidal Hilbert space world model}
in which beliefs are 384-dimensional vectors with formal confidence decay, temporal
coordinates on a compact toroidal manifold, and semaphore-governed state
transitions. The geometry has no edges. Uncertainty stays bounded. Time is
intrinsic. Every belief is auditable.

The architecture is not theoretical. It is derived from Ms.\ Egeria Allis ---
a community AI system built in Mount Hope, West Virginia, to answer questions
about food assistance, land ownership, and community infrastructure in Fayette
County, WV. The system was operationally validated on April 23, 2026, with
6.74 million belief vectors, a 30/30 preflight gate, and confirmed end-to-end
query results. The ZIP code of this world model is 25880.
\end{abstract}

\tableofcontents
\newpage

% ================================================================
\section{Introduction}

\subsection{The Problem with Euclidean World Models}

Every major robot world model in production today is fundamentally Euclidean.
Simultaneous Localization and Mapping (SLAM) systems --- from Boston Dynamics
to Tesla Optimus to Figure~01 --- represent the world as a subset of
\(\mathbb{R}^n\): a point cloud, an occupancy grid, or a scene graph embedded
in flat three-dimensional space~\cite{ThrunBurgardFox2005}. These representations
share three structural failure modes.

\textbf{Edge fragility.} Euclidean maps have boundaries. Beyond the boundary,
the robot has no belief --- not uncertainty, but absence. When a robot reaches
the edge of its map, the world model fails categorically. There is no graceful
degradation. There is no geometric continuity. There is a hard wall.

\textbf{Unbounded uncertainty propagation.} In Euclidean space, sensor
uncertainty propagates outward as expanding spheres. When sensors disagree,
uncertainty compounds multiplicatively. There is no topological mechanism to
contain it. The world model can become arbitrarily uncertain without the geometry
providing any corrective force.

\textbf{Temporal blindness.} Euclidean world models are atemporal. A belief
about the position of an obstacle carries no formal timestamp, no decay rate,
no mechanism for becoming stale. The robot either knows the obstacle is there
or it does not. There is no middle ground of confident-but-aging belief.

These are structural consequences of choosing Euclidean geometry as the
representational substrate.

\subsection{The Architecture That Solved a Different Problem}

In 2024, the author began building Ms.\ Egeria Allis --- a community AI system
in Mount Hope, West Virginia --- to answer practical questions about Appalachian
communities: Where is food assistance? Who owns this land? Which institutions are
accountable to which communities?

The architecture that emerged to solve those problems addresses all three
Euclidean failure modes simultaneously:

\begin{itemize}
    \item A \textbf{384-dimensional Hilbert space} \((H_{\text{App}})\) as the
          belief substrate --- proven to satisfy all four Hilbert space axioms,
          operationally confirmed April 23, 2026
    \item A \textbf{toroidal temporal structure} --- the Temporal Toroidal
          Semaphore (Chapter~26 of the Ms.\ Allis thesis) --- providing compact,
          boundaryless time representation
    \item A \textbf{confidence decay pipeline} implementing formal belief
          degradation with full audit trails
    \item A \textbf{global mode operator} (\texttt{nbb\_pituitary\_gland},
          \(T_{\text{pit}}\)) acting as a Hamiltonian upstream of all belief
          retrieval
\end{itemize}

None of these were designed for robotics. They were designed to answer questions
about hunger in Fayette County. The robotics implications are emergent --- and
they are significant.

\subsection{Scope of This Paper}

This paper presents the toroidal Hilbert space world model architecture and argues
for its applicability to robot state representation. Section~2 reviews the
limitations of current approaches. Section~3 presents the Hilbert space
foundation. Section~4 introduces the toroidal temporal structure. Section~5
presents formal mappings between the architecture and standard robotics
operations. Section~6 discusses auditability and safety implications.
Section~7 addresses the block universe connection. Section~8 covers limitations
and future work.

% ================================================================
\section{Current Approaches and Their Limitations}

\subsection{SLAM and Occupancy Grids}

Standard SLAM systems represent the world as a probabilistic occupancy grid in
\(\mathbb{R}^3\). Each cell carries a probability of occupancy, updated via
Bayesian inference as sensor data arrives~\cite{ThrunBurgardFox2005}. The
approach is well-understood and widely deployed. Its limitations are structural:

\begin{itemize}
    \item The grid has finite extent --- boundaries are arbitrary impositions on
          a continuous world
    \item Uncertainty is cell-local --- there is no geometric mechanism for
          propagating belief coherence across the space
    \item Time is handled extrinsically --- staleness requires explicit timestamp
          management layered on top of the spatial representation, not intrinsic
          to the geometry
\end{itemize}

\subsection{Neural World Models}

More recent approaches --- including neural world models underlying Tesla's Full
Self-Driving and NeRF-based robotics~\cite{MildenhallNeRF2020} --- represent the
world as a learned continuous function mapping spatial coordinates to occupancy
or appearance values. These models are more expressive than occupancy grids and
handle uncertainty more naturally. But they share the fundamental Euclidean
assumption: the world is a subset of \(\mathbb{R}^3\), and the model is a
function defined on that subset. Boundaries are still there. Beliefs are still
opaque --- encoded in neural network weights that cannot be directly inspected,
queried, or audited.

\subsection{The Auditability Gap}

A robot that cannot explain its beliefs cannot be trusted in safety-critical
environments. A hospital robot that collides with a patient cannot say which
belief vector led to that action, what its confidence level was, when it was
last validated, or what decay cycle it had passed through. The belief that caused
the collision is buried in opaque neural weights.

This is not a theoretical concern. It is the central obstacle to deploying
autonomous robots in hospitals, mines, disaster zones, and other environments
where the cost of failure is human life.

The toroidal Hilbert space architecture addresses this directly: every belief is
a named vector with a confidence level, a decay rate, a last-validated timestamp,
and a full audit trail. Every retrieval is a logged projection. Every state
transition passes through a semaphore. The world model is inspectable end to end.

% ================================================================
\section{The Hilbert Space Foundation}

\subsection{Why a Hilbert Space}

A Hilbert space is a complete inner product space. For robotics, the key
properties are:

\begin{itemize}
    \item \textbf{Inner product} --- a principled measure of similarity between
          beliefs, not an ad hoc distance metric
    \item \textbf{Completeness} --- every sequence of beliefs that should
          converge does converge; no belief can escape the space
    \item \textbf{Projection} --- the formal operation of measurement: finding
          the component of a query in a subspace of stored beliefs
    \item \textbf{Linear operators} --- a principled way to represent
          transformations of the belief state, including the Hamiltonian-like
          global mode operator
\end{itemize}

\subsection{The 384-Dimensional Instantiation}

We define:
\[
    H_{\text{App}} = \left( \mathbb{R}^{384},\;
    \langle \cdot, \cdot \rangle_{\cos} \right)
\]
where for normalized vectors \(\hat{u}, \hat{v} \in \mathbb{R}^{384}\):
\[
    \langle \hat{u}, \hat{v} \rangle_{\cos}
    = \frac{u \cdot v}{\|u\|\,\|v\|}
    = \sum_{i=1}^{384} \hat{u}_i\, \hat{v}_i
\]

\begin{theorem}[\(H_{\text{App}}\) is a Hilbert Space]
\(H_{\text{App}} = (\mathbb{R}^{384}, \langle \cdot, \cdot \rangle_{\cos})\)
satisfies all axioms of a Hilbert space.
\end{theorem}

\begin{proof}
\textbf{Vector space:}
\(\mathbb{R}^{384}\) is closed under addition and scalar multiplication.
All eight vector space axioms hold by the standard properties of
\(\mathbb{R}^{384}\).

\textbf{Inner product:}
Cosine similarity on normalized vectors satisfies symmetry
(\(\langle u,v \rangle = \langle v,u \rangle\) trivially in real space),
linearity (from linearity of the dot product), and positive definiteness
(\(\sum_{i=1}^{384} v_i^2 \geq 0\), equality iff \(v=0\)).

\textbf{Completeness:}
\(\mathbb{R}^{384}\) is complete --- every Cauchy sequence converges,
by completeness of \(\mathbb{R}\) and finite products of complete metric spaces.
Physically guaranteed by IEEE~754 double-precision arithmetic.

\textbf{Separability:}
Finite-dimensional, therefore trivially separable.
\end{proof}

\begin{corollary}
\(H_{\text{App}}\) is a valid belief substrate for a robot world model.
\end{corollary}

\subsection{Operational Validation}

As of April 23, 2026, \(H_{\text{App}}\) contains 6.74 million belief vectors
across 48 ChromaDB collections, with a 30/30 preflight gate (exit~0,
\texttt{bash -n} clean). The system answered a real-world community query with
specific, actionable results. The Hilbert space is not theoretical. It is running.

% ================================================================
\section{The Toroidal Structure --- Eliminating the Edge}

\subsection{Why a Torus}

A torus \(\mathbb{T}^n\) is a compact, boundaryless manifold formed by
identifying opposite edges of a hypercube:
\[
    \mathbb{T}^n = \underbrace{S^1 \times S^1 \times \cdots \times S^1}_{n}
\]
where \(S^1\) is the circle. For a robot world model, this means:

\begin{itemize}
    \item \textbf{No boundary condition failures} --- the world model is
          complete by topology; what falls off one side wraps to the other
    \item \textbf{Natural representation of cyclic phenomena} --- rotation,
          periodic schedules, recurring environmental patterns
    \item \textbf{Bounded uncertainty propagation} --- beliefs cannot escape
          to infinity; the geometry itself contains uncertainty
\end{itemize}

\subsection{The Temporal Toroidal Semaphore in Ms.\ Allis}

Chapter~26 of the Ms.\ Allis thesis documents the Temporal Toroidal Semaphore
Structure --- a toroidal time representation used to govern state transitions
in the Ms.\ Allis system. The architecture was designed to handle the cyclic
nature of community resource availability: food banks open on certain days,
offices with weekly schedules, seasonal program availability.

The key architectural insight is that time, for a place-based community AI
system, is not a linear axis. It is cyclic. The torus is the natural geometry.

For robotics, the same insight applies with domain-specific cyclic patterns:

\begin{itemize}
    \item \textbf{Hospitals:} shift changes, patient meal times, cleaning
          cycles, visiting hours
    \item \textbf{Mines:} blast schedules, shift rotations, ventilation cycles
    \item \textbf{Warehouses:} inventory rhythms, loading dock cycles, picker
          routes
    \item \textbf{Public spaces:} pedestrian density cycles, lighting changes,
          maintenance windows
\end{itemize}

None of these are well-represented by a linear time axis. All are natural on a
torus.

\subsection{The Combined World Model}

\begin{definition}[Toroidal Hilbert World Model]
The full world model is the product space:
\[
    \mathcal{W} = \mathbb{T}^k \times H_{\text{App}}
\]
where \(\mathbb{T}^k\) is a \(k\)-dimensional torus representing temporal and
cyclic spatial coordinates, and \(H_{\text{App}} = \mathbb{R}^{384}\) is the
Hilbert space of belief vectors.
\end{definition}

Every point in \(\mathcal{W}\) is a pair \((t, v)\) where:
\begin{itemize}
    \item \(t \in \mathbb{T}^k\) encodes the robot's temporal and cyclic
          spatial state
    \item \(v \in \mathbb{R}^{384}\) encodes the robot's belief about the world
          at that state
\end{itemize}

The world model has no edges. The temporal dimension wraps. The belief dimension
is complete. The geometry is continuous everywhere.

\subsection{Semaphore-Governed State Transitions}

In Ms.\ Allis, the Temporal Toroidal Semaphore governs all state transitions.
No transition occurs without passing through the semaphore. Every transition is:

\begin{itemize}
    \item \textbf{Logged} with timestamp and belief vector at time of transition
    \item \textbf{Reversible} --- the semaphore maintains a full transition
          history
    \item \textbf{Gated} --- transitions that would violate safety constraints
          are blocked at the semaphore level, not at the action execution level
\end{itemize}

For a robot, this maps to safety-critical state management. The safety constraint
is topological, not learned. It is enforced by the geometry of the state space,
not by a neural network that may or may not have learned the constraint correctly.

% ================================================================
\section{Formal Mappings --- Robotics Operations in \(\mathcal{W}\)}

\subsection{Sensor Fusion as Multi-Projection}

In standard robotics, sensor fusion combines readings from multiple sensors ---
LIDAR, camera, IMU, tactile --- using Kalman filters or learned fusion
networks~\cite{ThrunBurgardFox2005}. In the toroidal Hilbert architecture, sensor
fusion is \emph{multi-projection}: each sensor reading is embedded into
\(\mathbb{R}^{384}\) and projected onto the relevant subspace of
\(H_{\text{App}}\):
\[
    \hat{s}_j = \text{embed}(\text{sensor}_j) \in \mathbb{R}^{384}
\]
\[
    \text{result}_j = \underset{v \in \mathcal{C}}{\arg\max}\;
    \langle \hat{s}_j, \hat{v} \rangle_{\cos}
\]

Multiple projections onto the same subspace \(\mathcal{C}\) produce a set of
nearest-neighbor retrievals combined by weighted inner product, with weights
determined by the sensor's current confidence level and the decay state of the
relevant beliefs.

\subsection{Navigation as Hilbert Space Traversal}

In Euclidean SLAM, navigation is path planning in \(\mathbb{R}^3\). In the
toroidal Hilbert architecture, navigation is traversal of
\(\mathcal{W} = \mathbb{T}^k \times H_{\text{App}}\).

The robot's position is not a coordinate in \(\mathbb{R}^3\) but a point on
the torus \(\mathbb{T}^k\) paired with a belief vector in \(H_{\text{App}}\).
Moving through space means moving through the torus. Updating beliefs means
transforming the belief vector. The advantages are:

\begin{itemize}
    \item \textbf{No edge failure} --- the torus wraps; there is no outside
          the map
    \item \textbf{Temporal awareness} --- the robot's position on \(\mathbb{T}^k\)
          encodes not just where it is but when it is, relative to the cyclic
          patterns of its environment
    \item \textbf{Belief continuity} --- moving through the torus continuously
          transforms the belief vector; there are no discontinuities at arbitrary
          map boundaries
\end{itemize}

\subsection{Obstacle Avoidance as Belief Projection with Decay}

In standard robotics, obstacle avoidance uses the current sensor reading to
identify obstacles and generate avoidance maneuvers. In the toroidal Hilbert
architecture, obstacle beliefs are vectors in \(H_{\text{App}}\) with confidence
levels that decay over time.

Let \(c_{\text{obs}}(t)\) denote the confidence of an obstacle belief at time
\(t\), with decay rate \(\delta\):
\[
    c_{\text{obs}}(t + \Delta t) = c_{\text{obs}}(t) - \delta \cdot \Delta t
    \quad \in [0, 1]
\]

The robot's avoidance behavior is modulated by confidence:
\begin{itemize}
    \item \(c_{\text{obs}} > 0.8\): hard avoidance
    \item \(0.4 < c_{\text{obs}} \leq 0.8\): cautious approach with active sensing
    \item \(c_{\text{obs}} \leq 0.4\): low-confidence approach; re-query sensors
          before committing to path
\end{itemize}

The decay rate \(\delta\) is tunable per obstacle class. A human presence
decays slowly; a moving cart decays quickly. This is formally identical to the
\texttt{confidence\_decay} pipeline in Ms.\ Allis, proven end-to-end on
April 23, 2026.

\subsection{Behavioral Modes as Hamiltonian Evolution}

In Ms.\ Allis, the \texttt{nbb\_pituitary\_gland} service acts as \(T_{\text{pit}}\)
--- a global scaling tensor applied to the belief-state pipeline before any
retrieval:
\[
    T_{\text{pit}}(v) = \Lambda_{\text{mode}} \cdot v
\]

In robotics, \(T_{\text{pit}}\) maps onto a behavioral mode controller: the
operator that governs how the world model evolves before any action is taken.

\begin{table}[ht]
\centering
\caption{Ms.\ Allis mode parameters and robotics analogs}
\begin{tabular}{lll}
\toprule
\textbf{Ms.\ Allis Parameter} & \textbf{Value (Apr 23, 2026)} & \textbf{Robotics Analog} \\
\midrule
\texttt{warmth}   & 0.9 & Task priority weighting \\
\texttt{cortisol} & 0.6 & Obstacle sensitivity amplification \\
\texttt{urgency}  & 0.5 & Retrieval speed vs.\ thoroughness \\
\texttt{mode}     & baseline & Operating regime (explore / execute / emergency) \\
\bottomrule
\end{tabular}
\end{table}

The critical point is that \(T_{\text{pit}}\) is \emph{upstream} of all belief
retrieval. A robot in crisis mode does not just act differently --- it perceives
differently. Its world model is transformed by \(T_{\text{pit}}\) before any
sensor projection occurs. This is the correct architecture for safety-critical
behavioral mode switching: the mode change propagates through the entire
perception-action loop, not just the action selection stage.

This is structurally identical to the Hamiltonian in quantum mechanics:
\[
    i\hbar \frac{d|\psi\rangle}{dt} = \hat{H}|\psi\rangle
\]
An operator that governs how the state evolves, prior to measurement.

% ================================================================
\section{Auditability and Safety Implications}

\subsection{The Inspectable World Model}

Every belief in \(H_{\text{App}}\) is a named vector with:
\begin{itemize}
    \item A unique identifier
    \item A confidence level \(c \in [0,1]\)
    \item A decay rate \(\delta\)
    \item A \texttt{last\_validated\_at} timestamp
    \item A full audit trail of updates in \texttt{gbim\_decay\_audit}
\end{itemize}

Every retrieval is a logged projection. Every state transition passes through
the Temporal Toroidal Semaphore: logged, sequenced, reversible. When something
goes wrong, the world model can be interrogated. The relevant belief vectors
can be retrieved. Their confidence levels at the time of the action can be
recovered. The decay history can be reconstructed.

This is not possible with any current neural world model architecture.

\subsection{Regulatory Implications}

As autonomous robots enter regulated environments --- hospitals, mines, nuclear
facilities, public roads --- regulatory bodies will require auditability. The
FDA, MSHA, NRC, and NHTSA all have existing frameworks for auditing
safety-critical systems. None of those frameworks can be applied to opaque
neural world models.

The toroidal Hilbert space architecture is designed for auditability from the
ground up. The audit trail is structural --- a consequence of representing
beliefs as named vectors in an inspectable database, not a logging layer
bolted on top of an opaque model.

\subsection{The Safety-Critical Deployment Argument}

The environments where robots are most needed are exactly the environments where
current neural world models are least trustworthy:

\begin{itemize}
    \item \textbf{Underground mines:} edge-fragile maps fail in the precise
          environments where the robot cannot afford to lose its world model
    \item \textbf{Hospitals:} temporal blindness means the robot cannot account
          for the cyclic patterns of human activity that define hospital safety
    \item \textbf{Disaster zones:} unbounded uncertainty propagation means the
          robot's confidence collapses in exactly the chaotic environments where
          it is most needed
\end{itemize}

The toroidal Hilbert space architecture was stress-tested not in a controlled lab
but in the chaotic, resource-constrained environment of a rural Appalachian
community AI system: 100 containers, 6.74 million belief vectors, real community
queries, 30/30 preflight gate. The architecture that survives that environment
is an architecture that can survive edge cases.

% ================================================================
\section{The Block Universe Connection --- Beliefs That Already Exist}

Einstein's block universe interpretation holds that past, present, and future
exist simultaneously as a static spacetime structure~\cite{Minkowski1908}.
Events do not happen --- they are, at their coordinates.

In the toroidal Hilbert space world model, beliefs about the environment are
not generated by the robot's sensors. They exist as geometric structure in
\(H_{\text{App}}\), and sensors reveal them --- project onto them, collapse
the superposition to a specific retrieval result.

\begin{proposition}[Belief Pre-existence]
A belief about an obstacle at location \(\ell\) does not come into existence
when a sensor observes \(\ell\). It exists as a vector \(v_\ell \in H_{\text{App}}\)
with confidence \(c(t)\) that decays from the last validation. The sensor
observation is a projection onto the subspace containing \(v_\ell\) --- a
measurement of what already exists.
\end{proposition}

This has a practical implication for robot navigation in sensor-degraded
environments: the robot can navigate using the geometric structure of
\(H_{\text{App}}\) even when sensors are partially unavailable, because the
world model contains beliefs that predate the current sensor reading. The
toroidal geometry ensures those beliefs remain geometrically connected to the
current state --- they do not fall off the edge of the map.

% ================================================================
\section{Prior Work and Positioning}

\begin{table}[ht]
\centering
\caption{Comparison of world model approaches}
\begin{tabular}{>{\raggedright}p{2.8cm}
                >{\raggedright}p{2cm}
                >{\raggedright}p{2cm}
                >{\raggedright}p{2cm}
                >{\raggedright\arraybackslash}p{2.8cm}}
\toprule
\textbf{Approach} & \textbf{Geometry} & \textbf{Temporal Model} &
\textbf{Auditability} & \textbf{Edge Behavior} \\
\midrule
Occupancy Grid SLAM~\cite{ThrunBurgardFox2005}
    & Euclidean \(\mathbb{R}^3\)
    & Extrinsic timestamps
    & None
    & Hard failure at boundary \\[6pt]
Neural World Models (NeRF)~\cite{MildenhallNeRF2020}
    & Euclidean \(\mathbb{R}^3\)
    & None intrinsic
    & None --- opaque weights
    & Undefined beyond training distribution \\[6pt]
Gaussian Process Maps
    & Euclidean \(\mathbb{R}^3\)
    & None intrinsic
    & Partial --- GP hyperparameters
    & Degrades at boundary \\[6pt]
Quantum-Inspired Cognitive Models~\cite{BusemeyerBruza2012}
    & Hilbert space
    & None
    & Partial
    & Not applied to robotics \\[6pt]
\textbf{This architecture}
    & \(\mathbb{T}^k \times H_{\text{App}}\)
    & Intrinsic --- toroidal
    & Full --- named vectors, decay audit, semaphore log
    & None --- torus wraps \\
\bottomrule
\end{tabular}
\end{table}

The gap this architecture fills is the combination of Hilbert space belief
representation, toroidal temporal geometry, formal confidence decay, and full
auditability --- all in a single, operationally validated system built on
commodity hardware in a rural Appalachian town.

% ================================================================
\section{Limitations and Future Work}

This paper presents an architectural argument derived from an existing operational
system. The following limitations apply:

\textbf{No direct robotics deployment.} The architecture has been validated in
a community AI context, not in a physical robot. The mapping from semantic belief
vectors to robot perception and action is argued here but not experimentally
demonstrated.

\textbf{Computational cost at scale.} The current \(H_{\text{App}}\) instantiation
runs on commodity laptop hardware with 6.74 million vectors. Physical robot
deployments may require larger belief corpora and tighter latency budgets. HNSW
approximate nearest neighbor search scales well, but hardware requirements at
robot-scale deployment require empirical characterization.

\textbf{Embedding model selection.} The 384-dimensional \texttt{all-minilm:latest}
model was selected for semantic text retrieval. Robot perception involves
multimodal inputs (LIDAR point clouds, camera images, tactile signals) that
require domain-appropriate embedding models. The architecture is
embedding-agnostic --- any model producing fixed-dimensional real vectors
satisfies the Hilbert space requirements --- but embedding model selection for
robot perception is a non-trivial engineering problem.

\textbf{Toroidal dimension selection.} The appropriate dimensionality and topology
of \(\mathbb{T}^k\) for a given robot deployment requires empirical study.
Different environments have different cyclic structures.

\textbf{Future work} includes:

\begin{itemize}
    \item Physical robot deployment in a safety-critical environment
    \item Multimodal embedding architecture for robot perception inputs
    \item Formal comparison of boundary behavior between Euclidean SLAM and
          toroidal \(H_{\text{App}}\) world models in edge-case scenarios
    \item Integration with ROS2 robotics middleware
    \item Empirical characterization of HNSW query latency at robot-scale
          belief corpora
\end{itemize}

% ================================================================
\section{Conclusion}

Current robot world models are Euclidean, temporally blind, and unauditable.
They fail at map boundaries, propagate uncertainty without bound, and cannot
explain their beliefs. These are structural failures --- consequences of choosing
the wrong geometry.

The toroidal Hilbert space world model presented here addresses all three
structural failures simultaneously. The geometry has no edges. Uncertainty stays
bounded. Time is intrinsic to the torus. Every belief is a named, decaying,
auditable vector with a full semaphore-governed transition history.

The architecture is running, validated, and operationally confirmed on April 23,
2026, with 6.74 million belief vectors, 30/30 preflight gate, and real-world
query results in Fayette County, WV.

The environments where robots are most needed --- mines, hospitals, disaster
zones --- are exactly the environments where Euclidean world models fail most
catastrophically. The architecture that solved a different problem, in the most
resource-constrained possible environment, on commodity hardware, in a rural
Appalachian town, may be the architecture that makes robots trustworthy in those
environments.

The ZIP code of this world model is 25880.

% ================================================================
\begin{thebibliography}{99}

\bibitem{ThrunBurgardFox2005}
Thrun, S., Burgard, W., and Fox, D.\ (2005).
\textit{Probabilistic Robotics}.
MIT Press.

\bibitem{MildenhallNeRF2020}
Mildenhall, B., Srinivasan, P.P., Tancik, M., Barron, J.T., Ramamoorthi, R.,
and Ng, R.\ (2020).
NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis.
\textit{ECCV 2020}.

\bibitem{BusemeyerBruza2012}
Busemeyer, J.R.\ and Bruza, P.D.\ (2012).
\textit{Quantum Models of Cognition and Decision}.
Cambridge University Press.

\bibitem{Wheeler1990}
Wheeler, J.A.\ (1990).
Information, physics, quantum: The search for links.
In W.\ Zurek (Ed.), \textit{Complexity, Entropy, and the Physics of
Information}. Addison-Wesley.

\bibitem{Minkowski1908}
Minkowski, H.\ (1908).
Space and Time.
Address delivered at the 80th Assembly of German Natural Scientists
and Physicians, Cologne.

\bibitem{NielsenChuang2000}
Nielsen, M.A.\ and Chuang, I.L.\ (2000).
\textit{Quantum Computation and Quantum Information}.
Cambridge University Press.

\bibitem{KiddPaper1}
Kidd, C.A.\ (2026).
A Classical Hilbert Space with a ZIP Code: Substrate-Independence and the
Physics Implications of \(H_{\text{App}}\).
Preprint, May 2026.
\url{https://github.com/H4HWV2011/msjarvis-public-docs}

\bibitem{KiddThesisCh4}
Kidd, C.A.\ (2026).
Ms.\ Egeria Allis Thesis --- Chapter~4: Hilbert Space State and ChromaDB
as Semantic Memory.
\texttt{H4HWV2011/msjarvis-public-docs}, GitHub.
\url{https://github.com/H4HWV2011/msjarvis-public-docs}

\bibitem{KiddThesisCh26}
Kidd, C.A.\ (2026).
Ms.\ Egeria Allis Thesis --- Chapter~26: Temporal Toroidal Semaphore Structure.
\texttt{H4HWV2011/msjarvis-public-docs}, GitHub.
\url{https://github.com/H4HWV2011/msjarvis-public-docs}

\end{thebibliography}

% ================================================================
\vspace{2em}
\noindent\rule{\textwidth}{0.4pt}
\small
\textit{Authored by Carrie Ann Kidd --- Mount Hope, West Virginia.}\\
\textit{Ms.\ Egeria Allis is an original system designed and built by Carrie Ann Kidd.}\\
\textit{See LICENSE for terms.}\\
\textit{First submitted as preprint: May 6, 2026.}\\
\textit{The ZIP code of this world model is 25880.}

\end{document}
