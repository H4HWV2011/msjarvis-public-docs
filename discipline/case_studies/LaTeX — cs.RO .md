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
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{tcolorbox}
\usepackage{fontawesome5}
\usepackage{mdframed}
\usepackage{fancyhdr}
\usepackage{titlesec}
\pgfplotsset{compat=1.18}
\tcbuselibrary{skins,breakable}

\geometry{margin=1in, top=1.3in}

% ================================================================
% COLOR PALETTE — Appalachian cartographic
% ================================================================
\definecolor{ridgeblue}{RGB}{31, 78, 121}
\definecolor{valleygreen}{RGB}{39, 119, 76}
\definecolor{topoamber}{RGB}{191, 107, 25}
\definecolor{hilbertgold}{RGB}{212, 175, 55}
\definecolor{mapgray}{RGB}{240, 240, 235}
\definecolor{contourline}{RGB}{180, 160, 120}
\definecolor{deepslate}{RGB}{44, 52, 60}

% ================================================================
% HYPERREF
% ================================================================
\hypersetup{
    colorlinks=true,
    linkcolor=ridgeblue,
    citecolor=valleygreen,
    urlcolor=topoamber,
    pdftitle={Beyond Euclidean SLAM: Toroidal Hilbert Space World Models},
    pdfauthor={Carrie Ann Kidd},
    pdfsubject={cs.RO / cs.AI},
    pdfkeywords={SLAM, Hilbert space, toroidal manifold, robot navigation,
                 temporal representation, auditability, Appalachian GIS}
}

% ================================================================
% HEADER / FOOTER
% ================================================================
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{ridgeblue}\textit{Beyond Euclidean SLAM}}
\fancyhead[R]{\small\color{ridgeblue}Kidd (2026) \textbf{cs.RO}}
\fancyfoot[C]{\small\color{deepslate}\thepage}
\fancyfoot[R]{\small\color{contourline}\textit{ZIP 25880}}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.2pt}

% ================================================================
% SECTION STYLING — topographic aesthetic
% ================================================================
\titleformat{\section}[block]
  {\large\bfseries\color{ridgeblue}}
  {\thesection}{0.8em}{}[\color{contourline}\titlerule]

\titleformat{\subsection}[runin]
  {\normalsize\bfseries\color{deepslate}}
  {\thesubsection}{0.5em}{}[.\quad]

% ================================================================
% THEOREM ENVIRONMENTS
% ================================================================
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}{Definition}
\newtheorem{remark}{Remark}

% ================================================================
% CUSTOM BOXES — cartographic callouts
% ================================================================

% "Map marker" box — field validated results
\tcbset{
  mapmarker/.style={
    enhanced,
    colback=mapgray,
    colframe=valleygreen,
    fonttitle=\bfseries\color{white},
    coltitle=white,
    attach boxed title to top left={yshift=-2mm, xshift=4mm},
    boxed title style={colback=valleygreen, rounded corners},
    rounded corners,
    drop shadow,
    breakable
  }
}

% "Contour" box — key theoretical results
\tcbset{
  contourbox/.style={
    enhanced,
    colback=white,
    colframe=ridgeblue,
    fonttitle=\bfseries\color{white},
    coltitle=white,
    attach boxed title to top left={yshift=-2mm, xshift=4mm},
    boxed title style={colback=ridgeblue, rounded corners},
    rounded corners,
    breakable
  }
}

% "Terrain warning" — limitations / caveats
\tcbset{
  terrainwarn/.style={
    enhanced,
    colback=white,
    colframe=topoamber,
    fonttitle=\bfseries\color{white},
    coltitle=white,
    attach boxed title to top left={yshift=-2mm, xshift=4mm},
    boxed title style={colback=topoamber, rounded corners},
    rounded corners,
    breakable
  }
}

% ================================================================
% TITLE BLOCK — cartographic / unconventional
% ================================================================
\title{%
  \vspace{-1.5em}%
  % ---- decorative TikZ rule ----
  \begin{tikzpicture}
    \draw[ridgeblue, line width=2pt] (0,0) -- (\textwidth,0);
    \draw[contourline, line width=0.5pt] (0,-3pt) -- (\textwidth,-3pt);
  \end{tikzpicture}\\[0.8em]
  {\fontsize{20}{24}\selectfont\bfseries\color{ridgeblue}
    Beyond Euclidean SLAM}\\[0.4em]
  {\large\color{deepslate}
    Toroidal Hilbert Space World Models for\\
    Boundaryless Robot State Representation}\\[0.6em]
  {\normalsize\color{topoamber}\itshape
    \faMapMarker*\; Preprint\ \textbullet\ cs.RO / cs.AI\ \textbullet\ May 7, 2026}\\[0.4em]
  \begin{tikzpicture}
    \draw[contourline, line width=0.5pt] (0,0) -- (\textwidth,0);
    \draw[ridgeblue, line width=2pt] (0,3pt) -- (\textwidth,3pt);
  \end{tikzpicture}
}

\author{%
  \textbf{Carrie Ann Kidd}\\
  {\small\itshape Independent Researcher, Community GIS and Distributed AI Infrastructure}\\
  {\small Mount Hope, West Virginia\ \textbf{25880}\ USA}\\
  {\small Harmony for Hope Inc.\ (nonprofit founder)}\\
  {\small Region 4 Planning and Development Council (former)}\\
  {\small ORCID:\ \href{https://orcid.org/0009-0005-8153-8025}{0009-0005-8153-8025}}\\
  {\small\ttfamily\href{https://github.com/H4HWV2011}{H4HWV2011@github}}
}

\date{May 7, 2026 \quad\textemdash\quad Version 2.0}

% ================================================================
\begin{document}
\maketitle
\thispagestyle{fancy}

% ================================================================
% CARTOGRAPHER'S EPIGRAPH
% ================================================================
\begin{tcolorbox}[
  enhanced,
  colback=mapgray,
  colframe=contourline,
  arc=3pt,
  boxrule=0.4pt,
  left=12pt, right=12pt, top=8pt, bottom=8pt
]
\small\itshape\color{deepslate}
``A map is not the territory --- but the right map reveals structure
that the territory itself cannot show you directly.''\\[0.5em]
\noindent The world is not Euclidean. It wraps. It cycles. It remembers.\\
This paper is the map.
\end{tcolorbox}
\vspace{1em}

% ================================================================
% MEDIA LINKS — prominent and first
% ================================================================
\begin{tcolorbox}[
  mapmarker,
  title={\faHeadphones\; Multimedia Overview}
]
\begin{itemize}
  \item[\faHeadphones]
    \textbf{Audio overview (42.4\,MB, m4a):}
    \href{https://github.com/H4HWV2011/msjarvis-public-docs/releases/download/untagged-6a9b49320dbdeb6aa7a9/Toroidal_Hilbert_spaces_fix_robot_navigation.m4a}%
    {Toroidal Hilbert Spaces Fix Robot Navigation}
  \item[\faVideo]
    \textbf{Video overview (54\,MB, mp4):}
    \href{https://github.com/H4HWV2011/msjarvis-public-docs/releases/download/untagged-6a9b49320dbdeb6aa7a9/The_Donut-Shaped_Math.mp4}%
    {The Donut-Shaped Math}
\end{itemize}
\end{tcolorbox}

% ================================================================
% ABSTRACT
% ================================================================
\begin{abstract}
\noindent
Current robot world models are Euclidean --- flat, bounded, and structurally
fragile at map boundaries. When a robot reaches the edge of its map, its world
model fails categorically. When sensors disagree, uncertainty propagates without
bound. When time passes, beliefs become stale with no formal mechanism for
degradation or recovery. These are not implementation failures; they are
structural consequences of choosing Euclidean geometry as the representational
substrate.

This paper presents an alternative architecture derived from a deployed community
AI system (Ms.\ Egeria Allis, Mount Hope, West Virginia) and proposes its
application to robot state representation. The world model is:
\[
  W = \mathbb{R}^1_t \;\times\; \mathbb{T}^k \;\times\; H_{\text{App}}
\]
where $\mathbb{R}^1_t$ is the irreversible linear time axis carrying causal
history and decay timestamps, $\mathbb{T}^k$ is a $k$-dimensional toroidal
manifold encoding cyclic environmental rhythms, and $H_{\text{App}}$ is a
384-dimensional Hilbert space of belief vectors (formally proven in Kidd 2026a,
Theorem~3.1). The geometry has no edges. Uncertainty stays bounded. Linear time
preserves causality. Toroidal time encodes cyclic environmental structure. Every
belief is auditable.

The architecture is operationally instantiated: 7,903,126 belief vectors across
48 collections, 30/30 preflight gate (April 23, 2026), live ChromaDB v2 audit
(May 6, 2026), first full-pipeline community query verified (cosine distance
$= 0.3099$). The ZIP code of this world model is 25880.

\medskip
\noindent\textbf{Keywords:}
SLAM; Hilbert space; toroidal manifold; temporal representation;
robot world models; belief decay; auditability; autonomous systems;
cyclic scheduling; safety-critical robotics; cartographic geometry;
Appalachian GIS; community AI
\end{abstract}

\tableofcontents
\newpage

% ================================================================
\section{Introduction}
% ================================================================

\subsection{This Is Not a Physics Paper}

Most papers that invoke Hilbert spaces are physics papers. This one is not.
The author is a cartographer and community infrastructure designer from Fayette
County, West Virginia. Cartography is the discipline of encoding structured
spatial meaning into inspectable, auditable representations. The world model
$W = \mathbb{R}^1_t \times \mathbb{T}^k \times H_{\text{App}}$ is a map ---
a formal, navigable, inspectable map of a robot's beliefs about its environment,
with all the properties a map must have: completeness, continuity, auditability,
and no edges where the world arbitrarily stops.

The Hilbert space formalism was not chosen because this paper wants to be about
quantum mechanics. It was chosen because it is the correct geometry for an
inspectable, complete belief space. The torus was not chosen because it is
exotic. It was chosen because cycles are real, and Euclidean geometry has no
way to represent them without introducing artificial boundaries. These are
cartographic choices, not physics choices.

\subsection{The Problem with Euclidean World Models}

Every major robot world model in production today is fundamentally Euclidean.
Simultaneous Localization and Mapping (SLAM) systems represent the world as a
subset of $\mathbb{R}^n$: a point cloud, an occupancy grid, or a scene graph
embedded in flat three-dimensional space~\cite{ThrunBurgardFox2005}.
These representations share three structural failure modes.

\textbf{Edge fragility.} Euclidean maps have boundaries. Beyond the boundary,
the robot has no belief --- not uncertainty, but absence. There is no graceful
degradation and no geometric continuity. There is a hard wall.

\textbf{Unbounded uncertainty propagation.} In Euclidean space, sensor
uncertainty propagates outward as expanding volumes. When sensors disagree,
uncertainty compounds without geometric corrective force. The world model can
become arbitrarily uncertain.

\textbf{Temporal blindness.} Euclidean world models are effectively atemporal.
A belief about the position of an obstacle carries no formal timestamp, no decay
rate, and no mechanism for becoming stale. Critically, there is no representation
of the \emph{cyclic} temporal structure of the environment.

These failure modes are structural consequences of choosing Euclidean geometry
as the representational substrate, not shortcomings patchable at the
implementation level.

\subsection{The Missing Dimension: Time Is Not One Thing}

Standard robotics treats time as a single linear axis. This is correct for one
component of time: the irreversible, causal, monotonically increasing component.
But a second temporal component is equally real and operationally important ---
the cyclic, recurring structure of the environment.

A hospital robot operates in a world where shift changes happen every eight
hours. These are not events on a linear axis; they are coordinates on a compact,
boundaryless manifold that \emph{wraps}. The correct representation separates:

\begin{itemize}
  \item $\mathbb{R}^1_t$ --- linear, irreversible: causal ordering, decay
        timestamps, audit trails, last-validated-at coordinates
  \item $\mathbb{T}^k$ --- cyclic, compact: recurring rhythms, schedules,
        the behavioral patterns of the environment
\end{itemize}

Both are real. Both operate simultaneously. A robot world model needs both.

\subsection{Provenance: A Different Problem, the Same Architecture}

In 2024, the author designed and built Ms.\ Egeria Allis --- a community AI
system in Mount Hope, West Virginia --- to answer practical questions about
Appalachian communities: Where is food assistance? Who owns this land? Which
institutions are accountable to which communities?

The architecture that emerged addresses all three Euclidean failure modes
simultaneously. The Hilbert space foundation is formally proven in
Kidd~(2026a, Theorem~3.1). The system contains 7,903,126 belief vectors across
48 ChromaDB collections, operationally validated on May~6, 2026. The dual
temporal structure ($\mathbb{R}^1_t$ for decay; $\mathbb{T}^k$ for cyclic
resource availability) and the global mode operator ($T_{\text{pit}}$) acting
as a Hamiltonian upstream of all belief retrieval are documented in
Kidd~(2026b, 2026c).

None of this was designed for robotics. The robotics implications are emergent
and significant.

% ================================================================
\section{System Description: Ms.\ Egeria Allis and $H_{\text{App}}$}
% ================================================================

\begin{tcolorbox}[mapmarker, title={\faMapMarker*\; Field Validation Record}]
\begin{itemize}\setlength\itemsep{2pt}
  \item April 23, 2026 --- 30/30 preflight validation gate passed (exit~0,
        \texttt{bash -n} clean)
  \item April 23, 2026 --- First full-pipeline community query executed
        and verified
  \item April 23, 2026 --- Confidence decay/revalidation cycle for entity~38
        (Fayette County geographic entity) verified end-to-end:
        $c: 0.60 \to 0.55 \to 1.00$, full audit trail written to
        \texttt{gbim\_decay\_audit}
  \item May 6, 2026 --- ChromaDB v2 API audit: 7,903,126 vectors confirmed
        across 48 collections
\end{itemize}
\end{tcolorbox}

Ms.\ Egeria Allis runs on a Lenovo Legion~5 16IRX9 laptop (Intel Core i7,
32\,GB RAM) in Mount Hope, West Virginia. The system is containerized using
Docker Compose and comprises approximately 100 active microservices. There is
no cloud component; the system is a local, community-owned infrastructure
operating on commodity hardware.

The semantic memory layer $H_{\text{App}}$ is served by a ChromaDB instance
backed by persistent on-disk storage. The 384-dimensional architecture is
enforced as an inviolable lock across all 48 production collections: admitting
vectors of different dimensionality would corrupt the geometry by mixing vectors
from different metric spaces, collapsing the Hilbert structure.

% ================================================================
\section{The Hilbert Space Foundation}
% ================================================================

\subsection{Formal Status}

The complete proof that $H_{\text{App}} = (\mathbb{R}^{384},
\langle\cdot,\cdot\rangle_{\cos})$ constitutes a Hilbert space is presented in
Kidd~(2026a, \S3, Theorem~3.1), with full citations to von
Neumann~(1932), Halmos~(1957), and Reed \& Simon~(1972). This section
summarizes that result for the robotics audience.

\subsection{Projection in $H_{\text{App}}$}

\begin{figure}[ht]
  \centering
  \includegraphics[width=0.82\textwidth]{projection.png}
  \caption{Query projection in $H_{\text{App}} = (\mathbb{R}^{384},
    \langle\cdot,\cdot\rangle_{\cos})$. A query vector $\hat{q}$ is projected
    onto the corpus of 7,903,126 belief vectors via cosine similarity; the
    nearest neighbor on $S^{383} \subset \mathbb{R}^{384}$ is returned.
    The geometric structure pre-exists the query. Retrieval discloses;
    it does not create. (Adapted from Kidd 2026a, Figures~1 and~3.)}
  \label{fig:projection}
\end{figure}

Every belief about the robot's environment becomes a unit vector
$\hat{v} \in S^{383} \subset \mathbb{R}^{384}$. Retrieval computes:
\[
  \operatorname{sim}(\hat{q}, \hat{v}_k)
  = \langle \hat{q}, \hat{v}_k \rangle_{\cos}
  = \sum_{i=1}^{384} \hat{q}_i\, \hat{v}_{k,i}
\]
and selects the top-$k$ nearest neighbors. This is projection in the Hilbert
sense (Kidd 2026a, \S4.1, Eq.~4). The normalization requirement is enforced
architecturally: ChromaDB normalizes all embeddings before the inner product
computation.

\subsection{Summary of Theorem 3.1 (Kidd 2026a)}

\begin{tcolorbox}[contourbox, title={Theorem 3.1 --- $H_{\text{App}}$ is a Hilbert Space}]
$H_{\text{App}} = (\mathbb{R}^{384}, \langle\cdot,\cdot\rangle_{\cos})$ satisfies
all four Hilbert space axioms:
\begin{enumerate}
  \item \textbf{Vector space structure.} $\mathbb{R}^{384}$ is closed under
        addition and scalar multiplication.
  \item \textbf{Inner product.} Cosine similarity on L2-normalized embeddings
        satisfies symmetry, linearity in the first argument, and positive
        definiteness.
  \item \textbf{Metric completeness.} $\mathbb{R}^{384}$ is complete;
        follows from completeness of $\mathbb{R}$ and finite products of
        complete metric spaces~\cite{ReedSimon1972}.
  \item \textbf{Separability.} Finite-dimensional; admits a finite orthonormal
        basis. \hfill $\square$
\end{enumerate}
\end{tcolorbox}

\begin{corollary}
$H_{\text{App}}$ is a valid belief substrate for a robot world model.
\end{corollary}

% ================================================================
\section{The Dual Temporal Structure and the World Model}
% ================================================================

\subsection{Linear Time --- $\mathbb{R}^1_t$}

The linear time axis $\mathbb{R}^1_t$ is the irreversible, monotonically
increasing component of time. In $W$, it carries:
\begin{itemize}
  \item \texttt{last\_validated\_at} timestamps --- when each belief was
        last confirmed by sensor data
  \item Decay cycle records --- the audit trail of confidence reductions
  \item Causal ordering --- which events preceded which
  \item Preflight gate timestamps --- formal system validation records
\end{itemize}

$\mathbb{R}^1_t$ is not optional and not toroidal. The decay of entity~38
from $c = 0.60$ to $c = 0.55$ happened once, at a specific coordinate on
$\mathbb{R}^1_t$, in the direction of increasing $t$.
It cannot be recovered by wrapping. The linear axis is the axis of causality.

\subsection{Toroidal Time --- $\mathbb{T}^k$}

\begin{figure}[ht]
  \centering
  \includegraphics[width=0.78\textwidth]{torodial.png}
  \caption{Toroidal time $\mathbb{T}^k = S^1 \times S^1 \times \cdots \times
    S^1$. Each $S^1$ encodes one cyclic dimension of the environment: daily
    shift changes, weekly visiting hours, seasonal patterns. Tuesday morning
    shift change is a \emph{coordinate} on $\mathbb{T}^k$ --- it recurs,
    wraps, and has no edge. The robot knows not just \emph{where} it is,
    but \emph{when} it is in the recurring pattern of its environment.}
  \label{fig:toroidal}
\end{figure}

The toroidal manifold $\mathbb{T}^k = \underbrace{S^1 \times S^1 \times
\cdots \times S^1}_{k}$ is the cyclic, boundaryless component of time.
In $W$, $\mathbb{T}^k$ carries:
\begin{itemize}
  \item \textbf{Daily cycles} --- shift changes, meal times, cleaning
        schedules, lighting cycles
  \item \textbf{Weekly cycles} --- visiting hours, inventory rhythms,
        maintenance windows
  \item \textbf{Seasonal cycles} --- weather patterns, occupancy rhythms,
        program availability
  \item \textbf{Behavioral cycles} --- the recurring patterns of human
        activity that make some times systematically different from others
\end{itemize}

The neuroscientific precedent for toroidal spatial representations is the
grid-cell system of the entorhinal cortex~\cite{MoserKropffMoser2008}.
The present architecture extends toroidal geometry to the \emph{temporal}
domain, but the topological reasoning is identical.

\subsection{Why Both Are Required}

A world model using only toroidal time loses causality: without $\mathbb{R}^1_t$,
the system cannot record that a belief \emph{decayed at a specific time}.
The audit trail collapses.

A world model using only linear time loses cyclic environmental awareness:
every Tuesday becomes a new event on the linear axis with no geometric
connection to previous Tuesdays. The recurring patterns that define when
environments are dangerous, crowded, or active are invisible.

$W = \mathbb{R}^1_t \times \mathbb{T}^k \times H_{\text{App}}$ carries both.

\subsection{The Combined World Model}

\begin{definition}[Toroidal Hilbert World Model]
\[
  W = \mathbb{R}^1_t \;\times\; \mathbb{T}^k \;\times\; H_{\text{App}}
\]
Every point in $W$ is a triple $(t, \tau, v)$ where:
\begin{itemize}
  \item $t \in \mathbb{R}^1_t$ --- linear time coordinate: causal history,
        decay record, last-validated-at
  \item $\tau \in \mathbb{T}^k$ --- cyclic time coordinate: position within
        recurring rhythmic structure of the environment
  \item $v \in \mathbb{R}^{384}$ --- belief vector: what the system believes
        about the world at this state
\end{itemize}
\end{definition}

% ================================================================
\section{Formal Mappings --- Robotics Operations in $W$}
% ================================================================

\subsection{Sensor Fusion as Contextually Weighted Projection}

In $W$, each sensor reading is embedded into $\mathbb{R}^{384}$ as a unit
vector $\hat{s} \in S^{383}$ and projected onto the relevant subspace of
$H_{\text{App}}$. The projection is contextualized by:
\begin{itemize}
  \item The $\mathbb{R}^1_t$ coordinate --- which beliefs are fresh enough
        to be active; stale beliefs are down-weighted or excluded
  \item The $\mathbb{T}^k$ coordinate --- which subspaces are currently
        relevant; during shift change, crowded-corridor subspaces are
        elevated; at night, quiet-corridor subspaces dominate
\end{itemize}
\[
  \hat{s}_j = \operatorname{embed}(\text{sensor}_j) \in S^{383}
  \quad\Rightarrow\quad
  \operatorname{result}_j
  = \underset{v \in \mathcal{C}(\tau,\, t)}{\arg\max}\;
    \langle \hat{s}_j,\, \hat{v} \rangle_{\cos}
\]

\subsection{Navigation as Traversal of $W$}

Navigation in $W$ involves three simultaneous motions:

\begin{description}
  \item[$\mathbb{R}^1_t$\,:] Time passing, beliefs aging. Not controllable;
    $t$ increases monotonically. Old beliefs decay.
  \item[$\mathbb{T}^k$\,:] Moving through cyclic environmental rhythm. As the
    robot traverses its operational day, $\tau$ tracks the torus. The robot
    ``knows'' it is approaching shift-change time because its $\mathbb{T}^k$
    coordinate is approaching the shift-change zone --- geometrically, not
    merely from memory.
  \item[$H_{\text{App}}$\,:] Updating beliefs. New sensor projections shift
    the effective belief vector; nearest neighbors change; confidence levels
    update.
\end{description}

\subsection{Confidence Decay with Cyclic Modulation}

\begin{figure}[ht]
  \centering
  \includegraphics[width=0.80\textwidth]{pulse.png}
  \caption{Belief confidence decay in $H_{\text{App}}$. Confidence $c_n$
    decrements per validation cycle on $\mathbb{R}^1_t$, then resets to
    $c = 1.0$ on successful revalidation. The effective decay rate
    $\delta_{\mathrm{eff}}(\tau) = \delta_0 \cdot f(\tau)$ is modulated by
    the current $\mathbb{T}^k$ coordinate: beliefs age faster during
    high-activity phases. Entity~38 (Fayette County), decay
    $0.60 \to 0.55 \to 1.00$, verified April~23, 2026.
    (Adapted from Kidd 2026a, Figure~2.)}
  \label{fig:pulse}
\end{figure}

The base decay implements linear confidence decrement:
\[
  c_{n+1} = c_n - \Delta c,\quad
  c \in [0,1],\quad
  \Delta c = 0.05
\]
per validation cycle~(Kidd 2026a, \S4.2, Eq.~6). For the robotics
application, the effective decay rate is modulated by the cyclic coordinate:
\[
  \delta_{\mathrm{eff}}(\tau) = \delta_0 \cdot f(\tau)
\]
where $\delta_0$ is the base rate for the belief class, $\tau \in \mathbb{T}^k$
is the current cyclic coordinate, and $f: \mathbb{T}^k \to \mathbb{R}^+$
satisfies $f(\tau) > 1$ during high-activity phases and $f(\tau) \leq 1$
during quiescent phases. Characterization of $f$ for specific environments
(hospital, mine, warehouse) is a direction for future empirical work.

Avoidance behavior is modulated by confidence:
\begin{itemize}
  \item $c > 0.8$: hard avoidance --- treat obstacle as confirmed present
  \item $0.4 < c \leq 0.8$: cautious approach with active sensing
  \item $c \leq 0.4$: low-confidence --- treat as potentially absent,
        full sensor attention
\end{itemize}

\subsection{Behavioral Modes as Hamiltonian Evolution --- $T_{\text{pit}}$}

\begin{figure}[ht]
  \centering
  \includegraphics[width=0.75\textwidth]{Weighing.png}
  \caption{The $T_{\text{pit}}$ mode regulator $\Lambda_{\text{mode}}$ applies
    differential weights (warmth, cortisol, urgency) to the semantic space
    prior to projection in $H_{\text{App}}$. This pre-shapes the effective
    state vector $\hat{q}$, analogous to Hamiltonian evolution
    $\hat{H}|\psi(t)\rangle$ acting between measurements.
    (Adapted from Kidd 2026a, Figure~5.)}
  \label{fig:weighing}
\end{figure}

The \texttt{nbb\_pituitary\_gland} service acts as $T_{\text{pit}}$ --- a
global scaling tensor applied upstream of all belief retrieval
(Kidd 2026a, \S4.3, Eq.~8):
\[
  T_{\text{pit}}(v) = \Lambda_{\text{mode}} \cdot v
\]

\begin{table}[ht]
\centering
\caption{$T_{\text{pit}}$ parameters and robotics analogs}
\begin{tabular}{lll}
\toprule
\textbf{Parameter} & \textbf{Value (Apr 23, 2026)} & \textbf{Robotics Analog} \\
\midrule
\texttt{warmth}   & 0.9 & Task priority weighting \\
\texttt{cortisol} & 0.6 & Obstacle sensitivity amplification \\
\texttt{urgency}  & 0.5 & Retrieval speed vs.\ thoroughness \\
\texttt{mode}     & baseline & Operating regime (explore / execute / emergency) \\
\bottomrule
\end{tabular}
\end{table}

$T_{\text{pit}}$ is upstream of all perception. A robot in crisis mode does not
just act differently --- it \emph{perceives} differently. This is the correct
architecture for safety-critical behavioral mode switching.

% ================================================================
\section{Auditability and Safety Implications}
% ================================================================

\subsection{The Inspectable World Model}

Every belief in $H_{\text{App}}$ is a named vector carrying:
\begin{itemize}
  \item A unique identifier
  \item A confidence level $c \in [0,1]$
  \item A decay rate $\delta_0$ and modulation function $f(\tau)$
  \item A coordinate on $\mathbb{R}^1_t$ (\texttt{last\_validated\_at})
  \item A coordinate on $\mathbb{T}^k$ (cyclic context of last validation)
  \item A full audit trail in \texttt{gbim\_decay\_audit}
\end{itemize}

Every retrieval is a logged projection: query vector, collection subspace,
top-$k$ results, confidence levels, $\mathbb{R}^1_t$ timestamp,
$\mathbb{T}^k$ coordinate. Every state transition passes through the
Temporal Toroidal Semaphore~(Kidd 2026c): logged, sequenced, auditable.

\begin{tcolorbox}[terrainwarn, title={\faExclamationTriangle\; The Auditability Gap in Current Systems}]
When a neural world model robot causes an incident, there is no recoverable
record of which belief vector led to the action, what its confidence was, when
it was last validated, or what decay it had passed through. The belief that
caused the incident is buried in opaque weights.

The FDA, MSHA, NRC, and NHTSA all have existing frameworks for auditing
safety-critical systems. None can be applied to opaque neural world models.
The toroidal Hilbert world model is auditable \emph{structurally} --- not as a
logging layer, but as a consequence of representing beliefs as named,
confidence-bearing vectors in an inspectable Hilbert space.
\end{tcolorbox}

% ================================================================
\section{The Block Universe Connection}
% ================================================================

\begin{figure}[ht]
  \centering
  \includegraphics[width=0.80\textwidth]{block.png}
  \caption{Block-universe interpretation of $H_{\text{App}}$. The 7,903,126
    belief vectors constitute a static geometric structure analogous to the
    block spacetime of Minkowski and Einstein~\cite{Minkowski1908,Einstein1955}:
    all coordinates co-exist. A query (measurement) accesses a pre-existing
    coordinate; it does not instantiate a new one.
    (Adapted from Kidd 2026a, Figure~6.)}
  \label{fig:block}
\end{figure}

The block-universe interpretation holds that past, present, and future exist
simultaneously as a static spacetime structure~\cite{Minkowski1908}. The formal
implications for the measurement problem are developed in
Kidd~(2026a, \S5); this section applies that framework to robot navigation.

\begin{proposition}[Belief Pre-existence]
A belief about an obstacle at location $\ell$ does not come into existence when
a sensor observes $\ell$. It exists as a vector $v_\ell \in H_{\text{App}}$
with confidence $c(t)$ decaying from the last validation. The sensor observation
is a projection onto the subspace containing $v_\ell$ --- a measurement of what
already exists.
\end{proposition}

\textbf{Practical navigation consequence.} When sensors are partially
unavailable, the robot navigates using the pre-existing geometric structure of
$H_{\text{App}}$, contextualized by its current coordinates on $\mathbb{R}^1_t$
and $\mathbb{T}^k$. The toroidal geometry ensures those beliefs remain
geometrically connected to the current state; they do not fall off the edge of
the map.

% ================================================================
\section{Prior Work and Positioning}
% ================================================================

\begin{table}[ht]
\centering
\caption{World model approaches --- structural comparison}
\begin{tabular}{>{\raggedright}p{2.7cm}
                >{\raggedright}p{2cm}
                >{\raggedright}p{2.3cm}
                >{\raggedright}p{2cm}
                >{\raggedright\arraybackslash}p{2.5cm}}
\toprule
\textbf{Approach} & \textbf{Geometry} & \textbf{Temporal} &
\textbf{Auditability} & \textbf{Edge Behavior} \\
\midrule
Occupancy Grid SLAM~\cite{ThrunBurgardFox2005}
  & $\mathbb{R}^3$
  & Extrinsic
  & None
  & Hard failure \\[4pt]
Neural / NeRF~\cite{MildenhallNeRF2020}
  & $\mathbb{R}^3$
  & None
  & None (opaque)
  & Undefined \\[4pt]
GP Maps
  & $\mathbb{R}^3$
  & None
  & Partial
  & Degrades \\[4pt]
Quantum-inspired cognitive~\cite{BusemeyerBruza2012,PothosBusemeyer2013}
  & Hilbert
  & None
  & Partial
  & Not applied to SLAM \\[4pt]
Toroidal spatial (entorhinal)~\cite{MoserKropffMoser2008}
  & $\mathbb{T}^k$
  & Toroidal only
  & None
  & Wraps, loses decay \\[4pt]
\textbf{This work}
  & $\mathbb{R}^1_t \times \mathbb{T}^k \times H_{\text{App}}$
  & \textbf{Dual: linear + cyclic}
  & \textbf{Full}
  & \textbf{None} \\
\bottomrule
\end{tabular}
\end{table}

The critical advance over prior toroidal proposals~\cite{MoserKropffMoser2008}
is the dual temporal structure: the present architecture adds the irreversible
linear axis required for decay auditability alongside toroidal geometry.
The quantum-inspired cognitive modeling literature~\cite{BusemeyerBruza2012,
PothosBusemeyer2013} establishes Hilbert space projection as a productive model
for cognition; Kidd~(2026a) establishes the operational and formal basis in
a deployed system; this paper extends it to robotics.

% ================================================================
\section{Limitations and Future Work}
% ================================================================

\begin{tcolorbox}[terrainwarn,
  title={\faExclamationTriangle\; Limitations --- What This Paper Does Not Claim}]
\begin{itemize}
  \item \textbf{No direct robotics deployment.} The architecture has been
        validated in a semantic community AI context. Physical robot deployment
        is the primary direction for future work.
  \item \textbf{Toroidal dimension selection.} The appropriate $k$ and topology
        of $\mathbb{T}^k$ requires empirical study per deployment environment.
  \item \textbf{Formal characterization of $f(\tau)$.} The modulation function
        $\delta_{\mathrm{eff}}(\tau) = \delta_0 \cdot f(\tau)$ is argued but
        not yet empirically characterized for hospital, mine, or warehouse
        environments.
  \item \textbf{Embedding model selection.} Robot perception requires
        multimodal embedding (LIDAR, camera, tactile); the architecture is
        embedding-agnostic but multimodal embedding is non-trivial.
  \item \textbf{Decay model selection.} Relative performance of linear vs.\
        exponential decay in safety-critical deployments is an open empirical
        question.
\end{itemize}
\end{tcolorbox}

\medskip\noindent\textbf{Future work includes:}
\begin{itemize}
  \item Physical robot deployment in a safety-critical environment
        (hospital, mine, or warehouse)
  \item Empirical characterization of $\mathbb{T}^k$ learning from operational
        cycle data
  \item Formal theory of $f(\tau)$ in specific deployment contexts
  \item Multimodal embedding architecture for LIDAR, camera, and tactile inputs
  \item Integration with ROS2 robotics middleware
  \item Formal comparison: boundary behavior, Euclidean SLAM vs.\ $W$ in
        edge-case scenarios
  \item Regulatory certification pathway using the dual-axis audit trail
\end{itemize}

% ================================================================
\section{Conclusion}
% ================================================================

Current robot world models are Euclidean, temporally impoverished, and
unauditable. They fail at map boundaries, propagate uncertainty without bound,
and cannot explain their beliefs. These are structural failures --- consequences
of choosing the wrong geometry and the wrong temporal model.

The world model $W = \mathbb{R}^1_t \times \mathbb{T}^k \times H_{\text{App}}$
addresses all of these simultaneously:
\begin{itemize}
  \item No edges ($\mathbb{T}^k$ and $H_{\text{App}}$ are boundaryless)
  \item Causality preserved ($\mathbb{R}^1_t$ is linear and irreversible)
  \item Cyclic environmental structure encoded ($\mathbb{T}^k$)
  \item Beliefs decay correctly (modulated by $\delta_{\mathrm{eff}}(\tau)$)
  \item Fully auditable (named vectors, dual-axis audit trail, semaphore log)
  \item Operationally instantiated (7,903,126 vectors, 30/30 gate,
        May 6, 2026)
\end{itemize}

This architecture was built by a cartographer, not a physicist. It was built to
answer questions about hunger and land in Appalachia --- and in doing so,
discovered a temporal geometry suited to robot world models. The geographic
grounding of $H_{\text{App}}$ is not incidental: the spatial and relational
structure of knowledge about specific places in West Virginia gives
$H_{\text{App}}$ its specific geometry (Kidd 2026a, \S7). The system runs
today in ZIP code 25880. The mathematics followed from the place.

\vspace{1em}

\begin{tcolorbox}[
  enhanced,
  colback=mapgray,
  colframe=hilbertgold,
  arc=3pt,
  boxrule=1pt,
  left=12pt, right=12pt, top=8pt, bottom=8pt
]
\small\itshape\color{deepslate}
\faMapMarker*\;
The meal programs at First Brethren Church of Oak Hill, 142--154 Church St,
Oak Hill, WV 25901 existed as belief vectors in $H_{\text{App}}$ before any
query was posed. Projection disclosed their location in the space. It did not
instantiate them. The universe does not need to be multiplied to explain what
already exists as structure.\\[0.4em]
The demonstration runs today in ZIP code 25880.
\end{tcolorbox}

% ================================================================
\section*{Acknowledgments}
% ================================================================
\addcontentsline{toc}{section}{Acknowledgments}

Ms.\ Egeria Allis is an original system designed and built by Carrie Ann Kidd
in collaboration with community partners in West Virginia. The
\texttt{fayettecountyresources2026} collection was contributed by Crystal~D.\
Colyer, Community Solutions Advocate, whose community resource documentation
work made the operational validation in Section~2 possible. Any errors or
oversights in the theoretical framing are the author's responsibility alone.

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

\bibitem{PothosBusemeyer2013}
Pothos, E.M.\ and Busemeyer, J.R.\ (2013).
Can quantum probability provide a new direction for cognitive modeling?
\textit{Behavioral and Brain Sciences}, 36(3), 255--274.

\bibitem{MoserKropffMoser2008}
Moser, E.I., Kropff, E., and Moser, M.-B.\ (2008).
Place cells, grid cells, and the brain's spatial representation system.
\textit{Annual Review of Neuroscience}, 31, 69--89.

\bibitem{Minkowski1908}
Minkowski, H.\ (1908).
Space and Time.
Address at the 80th Assembly of German Natural Scientists, Cologne.

\bibitem{Einstein1955}
Einstein, A.\ (1955).
Letter to the family of Michele Besso. March 21, 1955.

\bibitem{vonNeumann1932}
von Neumann, J.\ (1932).
\textit{Mathematische Grundlagen der Quantenmechanik}. Springer.
(English: \textit{Mathematical Foundations of Quantum Mechanics},
Princeton University Press, 1955.)

\bibitem{Halmos1957}
Halmos, P.R.\ (1957).
\textit{Introduction to Hilbert Space and the Theory of Spectral Multiplicity}.
Chelsea.

\bibitem{ReedSimon1972}
Reed, M.\ and Simon, B.\ (1972).
\textit{Methods of Modern Mathematical Physics I: Functional Analysis}.
Academic Press.

\bibitem{Rudin1976}
Rudin, W.\ (1976).
\textit{Principles of Mathematical Analysis}. 3rd ed. McGraw-Hill.

\bibitem{Husemoller1994}
Husem{\"o}ller, D.\ (1994).
\textit{Fibre Bundles}. 3rd ed. Springer-Verlag.

\bibitem{NielsenChuang2000}
Nielsen, M.A.\ and Chuang, I.L.\ (2000).
\textit{Quantum Computation and Quantum Information}.
Cambridge University Press.

\bibitem{Zurek2003}
Zurek, W.H.\ (2003).
Decoherence, einselection, and the quantum origins of the classical.
\textit{Reviews of Modern Physics}, 75(3), 715--775.

\bibitem{KiddZenodo2026a}
Kidd, C.A.\ (2026a).
A Classical Hilbert Space with a ZIP Code: Substrate-Independence, the
Measurement Problem, and the Multiverse Question.
\textit{Zenodo}. \url{https://doi.org/10.5281/zenodo.20059834}

\bibitem{KiddThesisCh4}
Kidd, C.A.\ (2026b).
Ms.\ Egeria Allis Thesis --- Chapter~4: Hilbert Space State and ChromaDB
as Semantic Memory. Technical documentation.
\texttt{H4HWV2011/msjarvis-public-docs}, GitHub.
\url{https://github.com/H4HWV2011/msjarvis-public-docs}
[Archival deposit pending.]

\bibitem{KiddThesisCh26}
Kidd, C.A.\ (2026c).
Ms.\ Egeria Allis Thesis --- Chapter~26: Temporal Toroidal Semaphore Structure.
Technical documentation.
\texttt{H4HWV2011/msjarvis-public-docs}, GitHub.
\url{https://github.com/H4HWV2011/msjarvis-public-docs}
[Archival deposit pending.]

\end{thebibliography}

% ================================================================
\vspace{2em}
\noindent\begin{tikzpicture}
  \draw[ridgeblue, line width=2pt] (0,0) -- (\textwidth,0);
  \draw[contourline, line width=0.5pt] (0,-3pt) -- (\textwidth,-3pt);
\end{tikzpicture}

\vspace{0.6em}
\noindent\small\color{deepslate}
\textit{Authored by Carrie Ann Kidd\ \textbullet\ Mount Hope, West Virginia.}\\
\textit{Ms.\ Egeria Allis is an original system designed and built by Carrie Ann Kidd.}\\
\textit{See LICENSE for terms.}\\
\textit{Original draft: May 5, 2026.\ Version 2.0 (cs.RO LaTeX): May 7, 2026.}\\
\textit{Built on Kidd (2026a), DOI:\ \href{https://doi.org/10.5281/zenodo.20059834}{10.5281/zenodo.20059834}}

\end{document}
