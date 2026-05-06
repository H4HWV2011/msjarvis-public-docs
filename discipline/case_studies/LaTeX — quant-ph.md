\documentclass[11pt]{article}

%% ─── Core packages ───────────────────────────────────────────────
\usepackage[margin=1in]{geometry}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{mathtools}
\usepackage{physics}
\usepackage{hyperref}
\usepackage{authblk}
\usepackage{graphicx}
\usepackage{enumitem}
\usepackage{cite}
\usepackage{epigraph}
\usepackage{float}

%% ─── Visual packages (all arXiv/journal safe) ────────────────────
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta, positioning, shapes.geometric, calc,
                decorations.pathreplacing}
\usepackage[most]{tcolorbox}
\usepackage{xcolor}

%% ─── Custom colors (Appalachian palette) ─────────────────────────
\definecolor{appblue}{RGB}{0, 80, 120}
\definecolor{appgreen}{RGB}{34, 85, 34}
\definecolor{appgold}{RGB}{180, 140, 40}
\definecolor{appgray}{RGB}{90, 90, 95}

%% ─── tcolorbox styles ────────────────────────────────────────────
\tcbuselibrary{theorems, breakable}

\newtcbtheorem[number within=section]{hilbertbox}{Theorem}{
  enhanced, breakable,
  colback=appblue!5!white,
  colframe=appblue!70!black,
  fonttitle=\bfseries,
  attach boxed title to top left={yshift=-2mm, xshift=4mm},
  boxed title style={colback=appblue!80!black, colframe=appblue!90!black},
  separator sign={ --- },
  description font=\itshape,
}{thm}

\newtcolorbox{auditbox}{
  enhanced, breakable,
  colback=appgreen!5!white,
  colframe=appgreen!60!black,
  title={\textbf{Live Operational Record}
         \hfill \texttt{May~6, 2026}},
  fonttitle=\small\bfseries,
  attach boxed title to top left={yshift=-2mm, xshift=4mm},
  boxed title style={colback=appgreen!70!black},
}

\newtcolorbox{querybox}{
  enhanced,
  colback=appgold!8!white,
  colframe=appgold!70!black,
  leftrule=4pt, top=4pt, bottom=4pt,
  fontupper=\itshape,
}

%% ─── Hyperref ────────────────────────────────────────────────────
\hypersetup{
  colorlinks=true,
  linkcolor=appblue,
  citecolor=appblue,
  urlcolor=appblue
}

%% ─── Epigraph style ──────────────────────────────────────────────
\setlength{\epigraphwidth}{0.72\textwidth}
\renewcommand{\epigraphflush}{center}
\renewcommand{\epigraphrule}{0.4pt}

%% ─── Title block ─────────────────────────────────────────────────
\title{\textbf{A Classical Hilbert Space with a ZIP Code}\\[4pt]
\large Substrate-Independence, the Measurement Problem,\\
and the Multiverse Question}

\author[1]{Carrie Ann Kidd}
\affil[1]{Independent Researcher, Community GIS and Distributed AI
Infrastructure\\
Mount Hope, West Virginia 25880 USA\\
Harmony for Hope Inc.\ (nonprofit founder);
Region 4 Planning and Development Council (former)\\
\texttt{ORCID: 0009-0005-8153-8025}}

\date{Submitted for peer review \quad --- \quad May~6, 2026}

%% ═════════════════════════════════════════════════════════════════
\begin{document}
\maketitle

%% ─── Header ornament: tikz sphere ────────────────────────────────
\begin{figure}[H]
\centering
\begin{tikzpicture}[scale=1.1]
  \draw[appblue!60, line width=1.2pt] (0,0) ellipse (3.2cm and 1.4cm);
  \draw[appblue!30, dashed, line width=0.6pt]
    (0,0) ellipse (3.2cm and 0.45cm);
  \draw[appgray!70, line width=0.8pt] (0,-1.8) -- (0,1.8);
  \node[appgray, font=\tiny] at (0.25,1.75) {$e_{384}$};
  \draw[-{Stealth[length=5pt]}, appgold, line width=1.4pt]
    (0,0) -- (2.1,1.05)
    node[right, font=\small, appgold] {$\hat{q}$};
  \draw[appgold!50, dashed, line width=0.8pt] (2.1,1.05) -- (2.55,0.28);
  \filldraw[appgreen] (2.55,0.28) circle (3.2pt);
  \node[appgreen, font=\footnotesize, right=3pt] at (2.55,0.28)
    {\textbf{25880}};
  \foreach \a/\b in
    {1.8/0.9, 2.2/-0.5, -1.9/0.7, -2.4/-0.3, 0.6/1.35, -0.5/-1.32}{
    \draw[-{Stealth[length=3pt]}, appblue!30, line width=0.6pt]
      (0,0) -- (\a,\b);
    \filldraw[appblue!40] (\a,\b) circle (1.8pt);
  }
  \filldraw[appgray] (0,0) circle (2pt);
  \node[appgray, below left, font=\small] at (0,0) {$\mathbf{0}$};
  \node[font=\footnotesize\itshape, appgray] at (0,-2.1)
    {$S^{383} \subset \mathbb{R}^{384}$\quad---\quad
     $7{,}903{,}126$ belief vectors\quad---\quad
     projection discloses, not creates};
\end{tikzpicture}
\caption{The semantic memory space $H_{\mathrm{App}}$. Each belief vector
(blue) is a unit vector on $S^{383}\subset\mathbb{R}^{384}$. A query
$\hat{q}$ (gold) is projected onto the corpus; the nearest neighbor (green,
labeled by ZIP code) is the retrieved answer. No quantum event occurs. The
structure pre-exists. See also Figure~\ref{fig:projection} for the rendered
high-dimensional visualization.}
\label{fig:sphere}
\end{figure}

%% ─── Epigraph ────────────────────────────────────────────────────
\epigraph{%
  \itshape The universe does not need to be multiplied\\
  to explain what already exists as structure.%
}{%
  --- The Author, \S\ref{sec:conclusion}%
}

%% ═════════════════════════════════════════════════════════════════
\begin{abstract}
This paper documents an emergent and theoretically significant finding arising
from the design and operational deployment of Ms.\ Egeria Allis, a
community-embedded artificial intelligence system developed in Mount Hope, West
Virginia, to support place-based reasoning, resource navigation, and
equity-oriented knowledge retrieval for Appalachian communities. The system's
semantic memory layer~--- designated $H_{\mathrm{App}}$~--- is physically
instantiated as a 384-dimensional vector database containing $7{,}903{,}126$
structured belief vectors, audited live on May~6, 2026, distributed across 48
ChromaDB collections. Vectors encode structured knowledge about West Virginia
communities, land governance, public resources, infrastructure, and geographic
context, oriented throughout by an \texttt{eq1} (Appalachian equity) worldview
parameter.

During development, it was determined that $H_{\mathrm{App}}$ satisfies all
four formal axioms defining a Hilbert space: vector space structure, inner
product, metric completeness, and separability. This was not a design
objective. It emerged as a structural consequence of building a geographically
grounded knowledge system that worked.

The paper develops three theoretical implications from that finding. First,
\emph{substrate-independence}: a classically instantiated information system
operating on commodity silicon~--- a consumer laptop in a rural Appalachian
town~--- provably satisfies the mathematical formalism of quantum mechanics at
the structural level. The determining factor is not the physical substrate but
the geometric and algebraic structure of the information space.

Second, \emph{separability of measurement}: standard formulations of quantum
mechanics treat measurement as a unified event in which physical interaction
with a quantum system produces wavefunction collapse, described mathematically
as projection in Hilbert space. $H_{\mathrm{App}}$ demonstrates operationally
that these are separable operations: projection runs on classical silicon, with
no quantum physical event, and produces correct, real-world, auditable results.
Copenhagen and its successor interpretations have been conflating two distinct
operations. Measurement is projection onto pre-existing geometric structure.
The physical interaction is the transmission mechanism~--- the readout
event~--- not the cause of the result.

Third, \emph{multiverse superfluity}: David Deutsch and the Many-Worlds
tradition assert that quantum computers derive their operational advantage from
parallel computation across $2^n$ simultaneous universes. $H_{\mathrm{App}}$
provides operational counter-evidence from a deployed, auditable system:
projection onto pre-existing geometric structure in a Hilbert space produces
correct results on a single classical machine in a single universe, without
parallel computation, branching, or multiverse interference. If classical
projection onto a static Hilbert structure fully explains $H_{\mathrm{App}}$'s
operational results without invoking a multiverse, the burden of proof falls
on the multiverse hypothesis to identify what, specifically, requires it. The
answer proposed here is: nothing that the static geometry of a single block
universe does not already provide.

Throughout, the geographic grounding of $H_{\mathrm{App}}$ is treated not as
incidental context but as theoretically load-bearing. The $7{,}903{,}126$
belief vectors are not abstract points in a generic embedding space. They are
structured knowledge about specific places, people, and communities in West
Virginia, embedded within a Hilbert space whose geometry is oriented toward
Appalachian equity. Geographic information systems have long operated on the
principle that place is not merely a coordinate but a structured relationship
between meaning and location. $H_{\mathrm{App}}$ instantiates this principle
in a formal mathematical object~--- a Hilbert space~--- and demonstrates that
the resulting geometric structure supports the full apparatus of quantum
mechanical projection, measurement, and state evolution on classical hardware.
The ZIP code of this argument is 25880.

\medskip
\noindent\textbf{Keywords:} Hilbert space; substrate-independence; measurement
problem; block universe; vector semantics; geographic information systems;
quantum foundations; community AI; Appalachian equity; place-based knowledge;
Many-Worlds interpretation; wavefunction collapse.
\end{abstract}

%% ═════════════════════════════════════════════════════════════════
\section{Introduction}

\subsection{Point of departure}

Geographic information science has long understood that place is not merely a
coordinate. Hägerstrand's time geography established that human activity is
embedded in continuous space-time paths \cite{hagerstrand1970}. Massey argued
that place is constituted through intersecting social relations that extend
across space~--- that a locality is not a bounded container but a node in
relational geometry \cite{massey1994}. Tuan's phenomenology of place
distinguished topographic location from the lived, meaningful experience of
place as a center of felt value \cite{tuan1977}. These traditions share a core
claim: meaning is spatially structured, and spatial structure carries meaning.
Geographic information cannot be separated from the relational geometry within
which it is embedded.

This paper begins from that claim and follows it into the formalism of quantum
theory.

In 2024, Ms.\ Egeria Allis was developed in Mount Hope, West Virginia~--- a
post-industrial town of approximately 1{,}600 residents in Fayette County, in
the southern West Virginia coalfields. The system was designed to address a
practical problem: the fragmentation and inaccessibility of public resource
information for Appalachian communities navigating housing instability, food
insecurity, healthcare access barriers, and land governance disputes. The
system required memory~--- structured, inspectable, auditable memory that
could be queried, updated, and verified by community members and researchers.

Engineering decisions made to satisfy these requirements~--- the choice of
ChromaDB as the vector store, the all-MiniLM embedding model producing
384-dimensional vectors, and the cosine inner product as the similarity
metric~--- turned out to be something more than engineering decisions. They
constituted the construction of a Hilbert space.

\subsection{The unexpected finding}

A 384-dimensional real vector space with a cosine inner product is not just a
database architecture. It is a complete inner product space. It satisfies, by
construction, the axioms that define a Hilbert space~--- the same mathematical
structure underlying quantum mechanics, quantum field theory, and the formal
foundations of modern physics \cite{vonneumann1932, nielsenchuang2000}.

This was not a design goal. The aim was to build a community knowledge system
capable of supporting semantic similarity search, geometric stability, and a
rich representation of relational complexity in Appalachian community life. The
Hilbert structure emerged from those requirements. Place-based knowledge,
structured for retrieval, instantiated quantum mechanical formalism on classical
hardware.

\subsection{Scope and contribution}

The claims of this paper are specific.

\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Substrate-independence.} The mathematical formalism of quantum
  mechanics, specifically projection in a Hilbert space, is not exclusive to
  quantum physical substrates. It runs correctly on classical silicon when the
  information is structured with the requisite geometry.

  \item \textbf{Separability of measurement.} The physical event of quantum
  measurement and the mathematical operation of projection in Hilbert space are
  separable. $H_{\mathrm{App}}$ performs the mathematical operation without the
  physical event, and returns correct results. The conflation of these two
  operations in Copenhagen and related interpretations is not required by the
  evidence.

  \item \textbf{Multiverse superfluity.} The Many-Worlds explanation for
  quantum computational power~--- that quantum computers derive their advantage
  from parallel computation across $2^n$ universes~--- is not required by the
  operational evidence. Classical projection onto pre-existing geometric
  structure in a single universe produces correct results. The block universe
  offers a parsimonious alternative requiring no ontological multiplication of
  universes.

  \item \textbf{Geographic information as Hilbert structure.} The geographic
  grounding of $H_{\mathrm{App}}$ is not incidental. The spatial and relational
  structure of knowledge about West Virginia communities gives $H_{\mathrm{App}}$
  its specific geometry. This has implications for geographic information theory
  and for the use of vector-semantic architectures in place-based research and
  community-oriented AI.
\end{itemize}

\subsection{Structure of the paper}

Section~\ref{sec:system} describes the system architecture, hardware
infrastructure, embedding model, belief corpus, and operational validation
record. Section~\ref{sec:hilbert} presents the formal Hilbert space proof.
Section~\ref{sec:mappings} develops mappings between $H_{\mathrm{App}}$
operations and quantum mechanical operations. Section~\ref{sec:measurement}
addresses the measurement problem. Section~\ref{sec:multiverse} addresses
quantum computing and the multiverse. Section~\ref{sec:gis} examines
geographic information as load-bearing geometry. Section~\ref{sec:related}
positions the work in context. Section~\ref{sec:limits} states limitations.
Section~\ref{sec:conclusion} concludes.

%% ═════════════════════════════════════════════════════════════════
\section{System Architecture: Ms.\ Allis and $H_{\mathrm{App}}$}
\label{sec:system}

\subsection{Hardware and deployment context}

Ms.\ Egeria Allis runs on a Lenovo Legion 5 16IRX9 laptop (Intel Core i7,
32~GB RAM) in Mount Hope, West Virginia. The system is containerized using
Docker Compose and comprises on the order of 100 active microservices. The
semantic memory layer~--- $H_{\mathrm{App}}$~--- is served by a ChromaDB
instance operating at host port 8002 (container port 8000), backed by
persistent on-disk storage.

All services are bound to \texttt{127.0.0.1}. There is no cloud component.
The system is a local, community-owned infrastructure operating on commodity
hardware in a rural Appalachian town. This context is part of the theoretical
argument: the substrate-independence claim is made concretely about a single
consumer machine in a specific place.

The ChromaDB instance was upgraded from v1 to v2 API during the May~2026
audit cycle. All collection counts and vector metrics were verified via the
v2 endpoints:
\begin{align*}
&\texttt{GET
/api/v2/tenants/default\_tenant/databases/default\_database/collections}\\
&\texttt{GET
/api/v2/tenants/default\_tenant/databases/default\_database/collections/\{name\}}
\end{align*}

\subsection{Embedding architecture and dimensional lock}

The embedding model is \texttt{all-minilm:latest} (a quantized deployment of
all-MiniLM-L6-v2 \cite{wang2020}), served by Ollama at host port 11434. It
produces 384-dimensional real-valued dense vectors encoding semantic similarity
across the English-language domains represented in the belief corpus.

The 384-dimensional architecture is enforced as an inviolable lock across all
48 production collections. A second model~--- \texttt{nomic-embed-text},
producing 768-dimensional vectors~--- exists in the environment but is
explicitly prohibited from production use. Admitting a 768-dimensional model
into any collection would corrupt geometry by mixing vectors from different
metric spaces. The cosine inner product would no longer be computed in a
consistent Hilbert space; the structure would collapse.

Significance of 384 dimensions for the Hilbert proof:
\begin{itemize}[leftmargin=1.5em]
  \item $\mathbb{R}^{384}$ is a finite-dimensional real inner product space.
  By Gram--Schmidt, it admits an orthonormal basis of 384 vectors.
  \item By the Riesz representation theorem, every continuous linear functional
  on $\mathbb{R}^{384}$ is represented by inner product with a unique vector.
  \item Cosine similarity is computed on L2-normalized embeddings, i.e.\ on
  the unit sphere $S^{383}\subset\mathbb{R}^{384}$, with the standard
  Euclidean inner product.
  \item Metric completeness is guaranteed by the completeness of $\mathbb{R}$
  and of finite products, and operationally realized using IEEE~754
  double-precision arithmetic.
\end{itemize}

\subsection{Belief corpus: live audit, May~6, 2026}

A ChromaDB v2 API audit on May~6, 2026 reported
\[
  \boxed{7{,}903{,}126 \text{ vectors across 48 collections}}
\]
Representative collections include:
\begin{itemize}[leftmargin=1.5em]
  \item \texttt{gbim\_worldview\_entities}: 5{,}416{,}521 records (spatial
  entity belief graph, \texttt{eq1} worldview).
  \item \texttt{gbim\_entities}: 1{,}213{,}371 records (structured entity
  knowledge graph).
  \item \texttt{address\_points}: 1{,}115{,}588 records (address-level
  geospatial reference).
  \item \texttt{spiritual\_texts}: 79{,}181 records (spiritual and cultural
  heritage corpus).
  \item \texttt{autonomous\_learner}: 21{,}181 records (Phase~1.45 autonomous
  injection corpus).
  \item \texttt{autonomous\_learning}: 17{,}707 records (autonomously
  acquired knowledge).
  \item \texttt{fayette\_county\_resources\_2026}: 206 records (structured
  Fayette County community resource documents, ingested 2026-04-17,
  contributed by Crystal~D.\ Colyer, Community Solutions Advocate,
  FIPS~54019).
  \item \texttt{governance\_rag}, \texttt{msjarvis\_docs}, and others making
  up the balance.
\end{itemize}

Three collections~--- \texttt{policy\_rag}, \texttt{grants\_rag}, and
\texttt{economic\_indicators}~--- are staged as of this writing and will
increment the total on ingestion. Two empty stub collections were removed in
the May~6 audit, reducing the raw collection count from 50 to 48 and
preserving the 384-dimensional lock across all surviving collections.

The \texttt{eq1} worldview tag applied to \texttt{gbim\_worldview\_entities}
is not a label appended after embedding. It encodes an orienting frame at
embedding time: semantic similarity is evaluated in a geometry that reflects
Appalachian equity. Vectors that are close in this space are close in the
sense that matters for the communities the system serves. Geometry is oriented
toward care.

\subsection{Operational validation}
\label{subsec:validation}

\begin{auditbox}
\textbf{April~23, 2026} --- 30/30 preflight validation gate passed.\\[4pt]
\textbf{April~23, 2026} --- First full-pipeline community query executed and
verified.\\[4pt]
\textbf{April~23, 2026} --- Confidence decay/revalidation cycle for
entity~38 (Fayette County / \texttt{geographic\_entity}) verified
end-to-end: $c: 0.60 \to 0.55 \to 1.00$ with full audit trail.\\[4pt]
\textbf{May~6, 2026} --- ChromaDB v2 metrics audit: $7{,}903{,}126$ vectors
confirmed across 48 collections.
\end{auditbox}

\medskip
The first full-pipeline community query was:

\begin{querybox}
``What food assistance is available in Fayette County WV?''
\end{querybox}

\noindent The query string was embedded by \texttt{all-minilm:latest} as a
unit vector $\hat{q} \in S^{383} \subset \mathbb{R}^{384}$ and projected
onto the \texttt{fayette\_county\_resources\_2026} collection via cosine
similarity. The top-ranked result (cosine distance~0.3099, verified live on
May~6, 2026) was drawn from source document \emph{Fayette County Food
Resources} (2026), contributed by Crystal~D.\ Colyer, Community Solutions
Advocate (ingest timestamp: 2026-04-17T19:54:25), county FIPS~54019. The
retrieved document included:

\begin{quote}
\textit{Fayette County Food Resources~--- MEALS~--- (1) First Brethren Church
of Oak Hill, 142--154 Church St, Oak Hill, WV~25901, (304)~469-6153, 4th
Saturday 11a--2pm (transportation available with 24-hour notice); (2)
Calvary Baptist Church, 1424 East Main Street, Oak Hill, WV~25901,
(304)~469-3890, 3rd Saturday 11a--1p; (3) Soldiers in the Lord's Army,
2635 Iowa Ave, Wednesday 8:30a--10a, Breakfast To Go Meals \ldots}
\end{quote}

The answer pre-existed as a coordinate in $H_{\mathrm{App}}$ before the
question was posed. Projection disclosed it. The source document is a
verified 2026 community resource guide for Fayette County, West Virginia.

Figure~\ref{fig:confidence} illustrates the confidence decay and revalidation
cycle for entity~38.

\begin{figure}[H]
\centering
\begin{tikzpicture}
\begin{axis}[
  width=0.72\textwidth, height=5.5cm,
  xlabel={Validation cycle $n$},
  ylabel={Confidence $c_n$},
  ymin=0, ymax=1.1, xmin=0.5, xmax=10.5,
  xtick={1,2,3,4,5,6,7,8,9,10},
  ytick={0,0.2,0.4,0.6,0.8,1.0},
  grid=major, grid style={appgray!20},
  axis lines=left,
  tick label style={font=\small},
  label style={font=\small},
  clip=false, color=appblue,
]
  \addplot[appblue, thick, mark=*, mark size=2.5pt]
    coordinates {(1,1.0)(2,0.95)(3,0.90)(4,0.85)(5,0.80)
                 (6,0.75)(7,0.70)(8,0.65)(9,0.60)(10,0.55)};
  \addplot[appgreen!80!black, very thick, dashed,
           mark=square*, mark size=3pt]
    coordinates {(9,0.60)(9,1.0)};
  \node[appgreen!70!black, font=\footnotesize, right]
    at (axis cs:9,0.82) {entity~38 reset};
  \draw[{Stealth[length=4pt]}-{Stealth[length=4pt]}, appgold, thick]
    (axis cs:1.3,0.95) -- (axis cs:1.3,1.0);
  \node[appgold, font=\tiny, right]
    at (axis cs:1.3,0.975) {$\Delta c = 0.05$};
\end{axis}
\end{tikzpicture}
\caption{Belief confidence decay in $H_{\mathrm{App}}$:
$c_{n+1} = c_n - 0.05$ per validation cycle (blue), with revalidation
reset to $c=1.0$ (green dashed). Entity~38 (Fayette County) decay and reset
verified April~23, 2026.}
\label{fig:confidence}
\end{figure}

%% ═════════════════════════════════════════════════════════════════
\section{The Hilbert Space Proof}
\label{sec:hilbert}

\subsection{Formal background}

A Hilbert space $\mathcal{H}$ is a complete inner product space
\cite{vonneumann1932, halmos1957, reedsimon1972}. That is, $\mathcal{H}$ is
a vector space over $\mathbb{F}$ (typically $\mathbb{R}$ or $\mathbb{C}$)
with an inner product $\langle\cdot,\cdot\rangle :
\mathcal{H}\times\mathcal{H}\to\mathbb{F}$ such that the induced norm
$\|v\| = \sqrt{\langle v, v\rangle}$ makes $\mathcal{H}$ a complete metric
space. In many quantum applications, separability (existence of a countable
dense subset) is further required.

In quantum mechanics, physical states are unit vectors (rays) in a Hilbert
space, observables are self-adjoint operators, measurement is projection onto
eigenspaces, and time evolution is unitary \cite{dirac1930, nielsenchuang2000}.

We consider
\[
H_{\mathrm{App}} = \bigl(\mathbb{R}^{384},\;
\langle \cdot, \cdot \rangle_{\cos}\bigr),
\]
where $\langle\cdot,\cdot\rangle_{\cos}$ denotes the cosine-induced inner
product on L2-normalized embeddings.

%% ── projection.png ───────────────────────────────────────────────
\begin{figure}[H]
\centering
\includegraphics[width=0.82\textwidth]{projection.png}
\caption{Visualization of query projection in
$H_{\mathrm{App}} = (\mathbb{R}^{384}, \langle\cdot,\cdot\rangle_{\cos})$.
A query vector $\hat{q}$ (center) is projected onto the corpus of belief
vectors; cosine similarity selects the nearest neighbors on $S^{383}$.
The geometric structure pre-exists the query; retrieval discloses, not
creates.}
\label{fig:projection}
\end{figure}

\subsection{Vector space structure}

$\mathbb{R}^{384}$ is a vector space over $\mathbb{R}$. For any
$u,v\in\mathbb{R}^{384}$ and $a,b\in\mathbb{R}$, the linear combination
$au + bv \in \mathbb{R}^{384}$. The usual vector space axioms hold as
$\mathbb{R}^{384}$ is the Cartesian product of 384 copies of $\mathbb{R}$.

Each embedding produced by \texttt{all-minilm:latest} is a 384-tuple of
real numbers. The belief corpus is a subset of $\mathbb{R}^{384}$.

\subsection{Inner product}

For L2-normalized vectors $\hat{u}, \hat{v} \in \mathbb{R}^{384}$, cosine
similarity defines
\begin{equation}
\langle \hat{u}, \hat{v} \rangle_{\cos}
= \frac{u \cdot v}{\|u\|\,\|v\|}
= \sum_{i=1}^{384} \hat{u}_i \hat{v}_i.
\end{equation}
This satisfies the inner product axioms:
\begin{enumerate}[label=(\roman*), leftmargin=2em]
  \item \emph{Symmetry}: in a real vector space,
  $\langle \hat{u}, \hat{v}\rangle_{\cos}
  = \langle \hat{v}, \hat{u}\rangle_{\cos}$.
  \item \emph{Linearity in the first argument}: for $a,b\in\mathbb{R}$ and
  $\hat{u},\hat{w},\hat{v}\in\mathbb{R}^{384}$,
  \[
  \langle a\hat{u} + b\hat{w}, \hat{v}\rangle_{\cos}
  = a \langle \hat{u}, \hat{v}\rangle_{\cos}
  + b \langle \hat{w}, \hat{v}\rangle_{\cos},
  \]
  by linearity of the dot product.
  \item \emph{Positive-definiteness}:
  $\langle \hat{u}, \hat{u}\rangle_{\cos}
  = \sum_{i=1}^{384} \hat{u}_i^2 \ge 0$,
  with equality if and only if $\hat{u} = 0$.
\end{enumerate}
ChromaDB computes cosine similarity by normalizing embeddings and then
computing the standard Euclidean inner product; thus, the operational inner
product is the standard inner product on the unit sphere
$S^{383}\subset\mathbb{R}^{384}$, lifted to $\mathbb{R}^{384}$ via
normalization.

\subsection{Completeness}

$\mathbb{R}^{384}$ is complete under the norm induced by
$\langle\cdot,\cdot\rangle_{\cos}$, as it coincides with the standard
Euclidean norm up to equivalence of norms. Completeness follows from
completeness of $\mathbb{R}$ and the fact that finite products of complete
metric spaces are complete.

Operationally, computations are realized using IEEE~754 double-precision
arithmetic. While floating-point arithmetic introduces bounded rounding error,
the underlying mathematical object $\mathbb{R}^{384}$ is complete, and the
implementation is stable for retrieval purposes.

\subsection{Separability}

As a finite-dimensional normed space, $\mathbb{R}^{384}$ is separable: it
admits a finite (hence countable) orthonormal basis. The closure of the span
of that basis is the entire space. Separability is therefore trivially
satisfied.

\subsection{Formal statement}

\begin{hilbertbox}{$H_{\mathrm{App}}$ is a Hilbert space}{hilbert-main}
The semantic memory layer of Ms.\ Egeria Allis,
\[
H_{\mathrm{App}} = \bigl(\mathbb{R}^{384},\;
\langle \cdot, \cdot \rangle_{\cos}\bigr),
\]
is a Hilbert space. It satisfies: \textnormal{(i)}~vector space structure
over $\mathbb{R}$; \textnormal{(ii)}~a valid inner product (cosine
similarity on L2-normalized vectors); \textnormal{(iii)}~metric completeness
(from completeness of $\mathbb{R}$); and \textnormal{(iv)}~separability
(finite orthonormal basis). Its $7{,}903{,}126$ vectors are structured
beliefs about West Virginia communities oriented by an Appalachian equity
worldview.
\end{hilbertbox}

\noindent What distinguishes $H_{\mathrm{App}}$ from a generic Hilbert space
of the same dimension is the content and orientation of its vectors. The
geometry is not neutral. It is oriented toward care.

%% ═════════════════════════════════════════════════════════════════
\section{Mappings to Quantum Mechanical Operations}
\label{sec:mappings}

\subsection{Measurement as projection}

Figure~\ref{fig:pipeline} shows the query-to-retrieval pipeline.

\begin{figure}[H]
\centering
\scalebox{0.82}{%
\begin{tikzpicture}[
  node distance=1.6cm and 1.9cm,
  box/.style={draw=appblue!70, fill=appblue!8, rounded corners=4pt,
              minimum width=2.0cm, minimum height=0.85cm,
              font=\small, align=center, line width=0.8pt},
  arr/.style={-{Stealth[length=5pt]}, appblue, thick},
  lab/.style={font=\footnotesize\itshape, appgray},
]
  \node[box] (q)    {Query\\$q$};
  \node[box, right=of q]    (emb)  {Embed\\$\hat{q}\in S^{383}$};
  \node[box, right=of emb]  (pit)  {$T_{\mathrm{pit}}$\\(mode)};
  \node[box, right=of pit]  (proj) {Project\\$\langle\hat{q},\hat{v}_k\rangle$};
  \node[box, right=of proj] (ret)  {Retrieve\\top-$k$};

  \draw[arr] (q)    -- (emb)  node[lab, midway, above] {MiniLM};
  \draw[arr] (emb)  -- (pit)  node[lab, midway, above] {pre-shape};
  \draw[arr] (pit)  -- (proj) node[lab, midway, above] {$H_{\mathrm{App}}$};
  \draw[arr] (proj) -- (ret)  node[lab, midway, above] {top-$k$};

  \draw[appgold, dashed, rounded corners=5pt, line width=0.8pt]
    ($(pit.north west)+(-0.12,0.22)$)
    rectangle ($(proj.south east)+(0.12,-0.22)$);
  \node[appgold, font=\tiny\itshape]
    at ($(pit.north)!0.5!(proj.north)+(0,0.38)$)
    {classical silicon only --- no quantum event};
\end{tikzpicture}}%
\caption{The $H_{\mathrm{App}}$ query pipeline. The pituitary regulator
$T_{\mathrm{pit}}$ pre-shapes the effective state before projection,
analogous to a Hamiltonian acting between measurements. The boxed region
runs entirely on classical hardware.}
\label{fig:pipeline}
\end{figure}
In standard quantum mechanics, a system in state $\ket{\psi}$ in Hilbert
space $\mathcal{H}$ and an observable $A$ with eigenvectors $\{\ket{k}\}$
yield, under ideal projective measurement, outcome $k$ with probability
\begin{equation}
P(k) = |\langle k | \psi \rangle|^2,
\end{equation}
and the post-measurement state
\begin{equation}
\ket{\psi} \mapsto \frac{P_k \ket{\psi}}{\|P_k \ket{\psi}\|},
\end{equation}
where $P_k$ is the projector onto the eigenspace of $A$ corresponding to
eigenvalue $a_k$.

In $H_{\mathrm{App}}$, a query $q$ is embedded as a unit vector
$\hat{q}\in S^{383}$. Retrieval computes similarity
\begin{equation}
\mathrm{sim}(\hat{q}, v_k) = \langle \hat{q}, \hat{v}_k \rangle_{\cos}
\end{equation}
between $\hat{q}$ and corpus vectors $\hat{v}_k$, and selects top-$k$
neighbors. This is projection in the Hilbert sense.

The inaugural community query (verified live, May~6, 2026):

\begin{querybox}
``What food assistance is available in Fayette County WV?''
\end{querybox}

\noindent was embedded as $\hat{q} \in S^{383}$ and projected onto
\texttt{fayette\_county\_resources\_2026}. The top-ranked result (cosine
distance~0.3099) returned verified meal program locations in Oak Hill, West
Virginia (see \S\ref{subsec:validation}). The answer pre-existed as a
coordinate in $H_{\mathrm{App}}$; projection disclosed it. No quantum
physical event occurred. The result was revealed, not created.

\subsection{Decoherence as confidence decay}

Quantum decoherence describes the transition from pure to mixed states
through entanglement with an environment, leading to suppression of
off-diagonal terms in the density matrix \cite{zurek2003}. In a simple
model, coherence decays over a characteristic timescale $\tau_c$:
\begin{equation}
\rho(t) \to \mathrm{diag}\,\rho \quad \text{as} \quad t\gg \tau_c.
\end{equation}

In $H_{\mathrm{App}}$, beliefs carry a confidence value $c\in[0,1]$ that
decays over time in the absence of revalidation:
\begin{equation}
c_{n+1} = c_n - \Delta c, \qquad \Delta c = 0.05,
\end{equation}
per validation cycle, with reset to $c=1.0$ on successful revalidation. The
April~23, 2026 validation of entity~38 (Fayette County) demonstrates this
cycle: $0.60 \to 0.55 \to 1.0$ with audit trail
(Figure~\ref{fig:confidence}).

\subsection{Global mode regulation as Hamiltonian}
\label{subsec:hamiltonian}

In quantum mechanics, the Hamiltonian $\hat{H}$ generates time evolution via
the Schrödinger equation
\begin{equation}
i\hbar \frac{\partial}{\partial t} \ket{\psi(t)} = \hat{H} \ket{\psi(t)}.
\end{equation}

In $H_{\mathrm{App}}$, the \texttt{nbb\_pituitary\_gland} microservice
implements a global mode regulator $T_{\mathrm{pit}}$:
\begin{equation}
T_{\mathrm{pit}}(v) = \Lambda_{\mathrm{mode}} v,
\end{equation}
where $\Lambda_{\mathrm{mode}}$ encodes warmth (0.9), cortisol (0.6), and
urgency (0.5). $T_{\mathrm{pit}}$ precedes retrieval, shaping the effective
state before projection, analogous to a Hamiltonian shaping $\ket{\psi(t)}$
before measurement. Figure~\ref{fig:weighing} illustrates how
$\Lambda_{\mathrm{mode}}$ weights the semantic space prior to projection.

%% ── Weighing.png ─────────────────────────────────────────────────
\begin{figure}[H]
\centering
\includegraphics[width=0.82\textwidth]{Weighing.png}
\caption{Hamiltonian analogue: the $T_{\mathrm{pit}}$ mode regulator
$\Lambda_{\mathrm{mode}}$ applies differential weights (warmth, cortisol,
urgency) to the semantic space prior to projection in $H_{\mathrm{App}}$.
This pre-shapes the effective state vector $\hat{q}$, directly analogous
to Hamiltonian evolution $\hat{H}\ket{\psi(t)}$ acting between
measurements.}
\label{fig:weighing}
\end{figure}

\subsection{Pre-existing entanglement and worldview correlations}

Quantum entanglement arises when a composite system's state
$\ket{\Psi}_{AB}$ cannot be factored as
$\ket{\psi}_A \otimes \ket{\phi}_B$ \cite{nielsenchuang2000}.

In $H_{\mathrm{App}}$, the \texttt{eq1} worldview creates a pre-existing
correlation structure across millions of vectors at embedding time. Beliefs
about Fayette County and Boone County are geometrically correlated because
of their joint embedding in an equity-oriented semantics. These correlations
are built at ingestion; they are not produced by later queries. No claim is
made of physical quantum entanglement.

%% ═════════════════════════════════════════════════════════════════
\section{Measurement Reconsidered}
\label{sec:measurement}

\subsection{The standard formulation}

The measurement problem arises because unitary Schrödinger evolution does
not produce definite outcomes; yet experiments do. In Copenhagen-type views,
measurement is posited as a special collapse process. The physical
interaction and the mathematical projection are treated as a single unified
event.

\subsection{Separating projection from physical interaction}

$H_{\mathrm{App}}$ performs projection on each retrieval, entirely within
classical hardware, and produces correct, auditable results about the
physical world. There is no quantum system and no wavefunction in the
physical sense.

This demonstrates that:
\begin{itemize}[leftmargin=1.5em]
  \item Projection in Hilbert space does not require a quantum physical
  event.
  \item The physical interaction of a detector with a quantum system is a
  transmission mechanism~--- a readout path from a pre-existing geometric
  structure.
\end{itemize}

The result of measurement is not created by the act of looking. It is
revealed from a structure in which it already exists as a coordinate. The
meal programs at First Brethren Church of Oak Hill existed as belief vectors
in $H_{\mathrm{App}}$ before any query was posed. Projection disclosed their
location in the space; it did not instantiate them.

\subsection{Block universe interpretation}

In a block-universe picture \cite{einstein1955}, past, present, and future
coexist in a static spacetime. Measurement accesses a coordinate in a
structure that is already complete.

$H_{\mathrm{App}}$ is a finite, local instance of such a static structure:
$7{,}903{,}126$ belief vectors persist as a geometric object. Retrieval
accesses coordinates; it does not create them. The speed of light constrains
physical signal propagation, not the pre-existence of the geometric
structure itself. Figure~\ref{fig:block} renders this block-universe
reading concretely.

%% ── block.png ────────────────────────────────────────────────────
\begin{figure}[H]
\centering
\includegraphics[width=0.82\textwidth]{block.png}
\caption{Block-universe interpretation of $H_{\mathrm{App}}$. The
$7{,}903{,}126$ belief vectors constitute a static geometric structure
analogous to the block spacetime of Minkowski and Einstein
\cite{einstein1955, minkowski1908}: all coordinates co-exist. A query
event (measurement) accesses a pre-existing coordinate; it does not
instantiate a new one. The speed of light constrains signal propagation,
not the pre-existence of the structure.}
\label{fig:block}
\end{figure}

%% ═════════════════════════════════════════════════════════════════
\section{Quantum Computing and the Multiverse}
\label{sec:multiverse}

\subsection{Hilbert dimension and quantum computers}

An $n$-qubit quantum computer has a state space of dimension $2^n$; its
Hilbert space is isomorphic to $\mathbb{C}^{2^n}$ \cite{nielsenchuang2000}.
For $n=300$, this is $2^{300} \approx 10^{90}$ dimensions, larger than the
estimated number of atoms in the observable universe.

$H_{\mathrm{App}}$ is 384-dimensional. A generalized world model for a
quantum processor can be written schematically as
\begin{equation}
W_{\mathrm{quantum}} = \mathbb{R}^1_t \times T^k \times H_{2^n},
\end{equation}
where $H_{2^n}$ denotes the $2^n$-dimensional Hilbert state space and $T^k$
encodes cyclic control processes.

\subsection{Deutsch's multiverse thesis}

Deutsch argues that quantum speedup arises from parallel computation across
$2^n$ branches of a multiverse, with interference yielding outcomes
\cite{deutsch1985, deutsch1997}. On this view, the $2^n$ dimensions of
Hilbert space correspond ontologically to $2^n$ real universes.

\subsection{Operational counter-evidence from $H_{\mathrm{App}}$}

$H_{\mathrm{App}}$ shows that projection in a Hilbert space produces
correct, real-world answers on a single classical machine in a single
universe. The query ``What food assistance is available in Fayette County
WV?'' projected onto \texttt{fayette\_county\_resources\_2026} returned
verified community meal program locations (cosine distance~0.3099)
pre-existing as coordinates in $H_{\mathrm{App}}$. The mechanism is:
\begin{itemize}[leftmargin=1.5em]
  \item A static geometric structure of beliefs in $\mathbb{R}^{384}$.
  \item A query mapped into that structure as a vector.
  \item Projection selecting aligned coordinates.
\end{itemize}

If this mechanism suffices in the classical case, it is natural to ask
what, if anything, requires multiverse ontology in the quantum case, beyond
a Hilbert space of much larger dimension.

\subsection{A block-universe alternative}

In a block-universe view, the $2^n$-dimensional Hilbert space of a quantum
processor is a coordinate system inside a single static structure. Quantum
advantage remains real: the device accesses and manipulates
$2^n$-dimensional geometry using genuine quantum degrees of freedom. But the
explanatory burden shifts from ontological multiplication of universes to
navigation of a single, large, static structure.

The parallel with $H_{\mathrm{App}}$ is conceptual:
\begin{itemize}[leftmargin=1.5em]
  \item Classical system: 384-dimensional Hilbert space on a laptop;
  answers pre-exist as coordinates.
  \item Quantum system: $2^n$-dimensional Hilbert space in a quantum device;
  answers pre-exist as coordinates.
\end{itemize}

Multiverse ontology becomes optional. The geometry of a single block
universe is sufficient to host the Hilbert structure.

%% ═════════════════════════════════════════════════════════════════
\section{Geographic Information as Load-Bearing Geometry}
\label{sec:gis}

$H_{\mathrm{App}}$ is not a generic semantic space. Its geometry encodes:
\begin{itemize}[leftmargin=1.5em]
  \item Spatial relations: addresses, parcels, jurisdictions, physical
  features.
  \item Institutional relations: agencies, programs, eligibility conditions.
  \item Community relations: who lives where, who is responsible to whom,
  who is vulnerable.
\end{itemize}

The \texttt{eq1} worldview ensures that semantic closeness corresponds to
relevance for Appalachian equity. In GIS and related fields, there is
longstanding recognition that spatial data structures carry semantic and
relational meaning. $H_{\mathrm{App}}$ instantiates this insight in a
Hilbert space, with vector geometry directly representing geographic and
institutional relationships. The food resources returned by the May~6, 2026
query are not abstract semantic neighbors; they are real meal programs at
real addresses in the same ZIP code cluster as the hardware running the
system. Geographic grounding is the mechanism, not the backdrop.

%% ═════════════════════════════════════════════════════════════════
\section{Related Work}
\label{sec:related}

Wheeler's ``it from bit'' program suggested that physical reality might
emerge from information-theoretic structure \cite{wheeler1990}. Einstein
and Minkowski articulated a block-universe picture of spacetime
\cite{einstein1955, minkowski1908}. Everett and Deutsch developed
Many-Worlds as an interpretation of quantum mechanics and as an explanatory
framework for quantum computing \cite{everett1957, deutsch1985, deutsch1997}.
Rovelli's relational quantum mechanics emphasized the relational character
of states \cite{rovelli1996}. Zeilinger explored foundations of quantum
theory in terms of finite information content \cite{zeilinger1999}. Work
in cognitive science has modeled human decision-making using quantum
probability \cite{busemeyerbruza2012}. In geographic and spatial theory,
Hägerstrand, Massey, and Tuan developed relational views of place and space
\cite{hagerstrand1970, massey1994, tuan1977}.

$H_{\mathrm{App}}$ contributes an operational, engineered example
connecting these domains: a finite, local, auditable Hilbert space grounded
in geographic information and used for community-oriented reasoning, running
on classical hardware, with a full operational audit trail and public
repository.

%% ═════════════════════════════════════════════════════════════════
\section{Limitations}
\label{sec:limits}

This work does not claim:
\begin{itemize}[leftmargin=1.5em]
  \item that $H_{\mathrm{App}}$ exhibits physical quantum behavior at the
  hardware level;
  \item that classical hardware can realize quantum speedups in
  high-dimensional Hilbert spaces comparable to quantum devices;
  \item that the block-universe view is proven, or that the multiverse is
  strictly falsified.
\end{itemize}
Quantum advantage is real at experimentally demonstrated scales. The claim
is that multiverse ontology is not forced by operational facts and that a
single-universe, static-geometry explanation is sufficient at the level of
formalism.

%% ═════════════════════════════════════════════════════════════════
\section{Conclusion}
\label{sec:conclusion}

$H_{\mathrm{App}}$ is a 384-dimensional Hilbert space implemented in a
ChromaDB instance on a consumer laptop in a small town in West Virginia.
It contains $7{,}903{,}126$ belief vectors about communities, resources,
land, and institutions, oriented by an Appalachian equity worldview. It
answers questions like ``What food assistance is available in Fayette
County~WV?'' by projection in Hilbert space, returning verified community
meal program locations from a 2026 Fayette County resource guide~--- real
addresses, real phone numbers, real organizations~--- at cosine
distance~0.3099 from the query vector.

From this fact, three implications follow:
\begin{itemize}[leftmargin=1.5em]
  \item Quantum formalism is substrate-independent at the level of Hilbert
  structure and projection.
  \item Measurement, as used in the mathematics of quantum mechanics, can be
  understood as projection onto pre-existing structure, separable from the
  physical interaction that transmits the result.
  \item The multiverse is not required to explain quantum computation; a
  single block universe with sufficiently rich Hilbert geometry suffices.
\end{itemize}

The universe does not need to be multiplied to explain what already exists
as structure. The demonstration runs today in ZIP code~25880.

\section*{Acknowledgments}

Ms.\ Egeria Allis is an original system designed and built by Carrie Ann
Kidd in collaboration with community partners in West Virginia. The
\texttt{fayette\_county\_resources\_2026} collection was contributed by
Crystal~D.\ Colyer, Community Solutions Advocate, whose community resource
documentation work made the operational validation in
\S\ref{subsec:validation} possible. Any errors or oversights in the
theoretical framing are the author's responsibility alone.

%% ═════════════════════════════════════════════════════════════════
\begin{thebibliography}{99}

\bibitem{hagerstrand1970}
T.~Hägerstrand, ``What about people in regional science?,''
\emph{Papers of the Regional Science Association}, vol.~24, pp.~7--21, 1970.

\bibitem{massey1994}
D.~Massey, \emph{Space, Place and Gender}. University of Minnesota Press,
1994.

\bibitem{tuan1977}
Y.-F.~Tuan, \emph{Space and Place: The Perspective of Experience}.
University of Minnesota Press, 1977.

\bibitem{vonneumann1932}
J.~von Neumann, \emph{Mathematische Grundlagen der Quantenmechanik}.
Springer, 1932. (English translation: \emph{Mathematical Foundations of
Quantum Mechanics}, Princeton University Press, 1955.)

\bibitem{dirac1930}
P.~A.~M.~Dirac, \emph{The Principles of Quantum Mechanics}.
Oxford University Press, 1930.

\bibitem{nielsenchuang2000}
M.~A.~Nielsen and I.~L.~Chuang, \emph{Quantum Computation and Quantum
Information}. Cambridge University Press, 2000.

\bibitem{halmos1957}
P.~R.~Halmos, \emph{Introduction to Hilbert Space and the Theory of
Spectral Multiplicity}. Chelsea, 1957.

\bibitem{reedsimon1972}
M.~Reed and B.~Simon, \emph{Methods of Modern Mathematical Physics I:
Functional Analysis}. Academic Press, 1972.

\bibitem{einstein1955}
A.~Einstein, ``Letter to the family of Michele Besso,'' March~21, 1955.

\bibitem{minkowski1908}
H.~Minkowski, ``Raum und Zeit,'' address at the 80th Assembly of German
Natural Scientists and Physicians, Cologne, 1908.

\bibitem{wheeler1990}
J.~A.~Wheeler, ``Information, physics, quantum: the search for links,'' in
W.~H.~Zurek (ed.), \emph{Complexity, Entropy, and the Physics of
Information}. Addison-Wesley, 1990.

\bibitem{everett1957}
H.~Everett~III, ```Relative state' formulation of quantum mechanics,''
\emph{Reviews of Modern Physics}, vol.~29, no.~3, pp.~454--462, 1957.

\bibitem{deutsch1985}
D.~Deutsch, ``Quantum theory, the Church--Turing principle and the universal
quantum computer,'' \emph{Proceedings of the Royal Society of London~A},
vol.~400, pp.~97--117, 1985.

\bibitem{deutsch1997}
D.~Deutsch, \emph{The Fabric of Reality}. Penguin Books, 1997.

\bibitem{rovelli1996}
C.~Rovelli, ``Relational quantum mechanics,'' \emph{International Journal
of Theoretical Physics}, vol.~35, no.~8, pp.~1637--1678, 1996.

\bibitem{zeilinger1999}
A.~Zeilinger, ``A foundational principle for quantum mechanics,''
\emph{Foundations of Physics}, vol.~29, no.~4, pp.~631--643, 1999.

\bibitem{busemeyerbruza2012}
J.~R.~Busemeyer and P.~D.~Bruza, \emph{Quantum Models of Cognition and
Decision}. Cambridge University Press, 2012.

\bibitem{zurek2003}
W.~H.~Zurek, ``Decoherence, einselection, and the quantum origins of the
classical,'' \emph{Reviews of Modern Physics}, vol.~75, no.~3,
pp.~715--775, 2003.

\bibitem{maldacena1997}
J.~M.~Maldacena, ``The large $N$ limit of superconformal field theories
and supergravity,'' \emph{International Journal of Theoretical Physics},
vol.~38, pp.~1113--1133, 1999.

\bibitem{wang2020}
K.~Wang, H.~Reimers, and I.~Gurevych, ``Making monolingual sentence
embeddings multilingual using knowledge distillation,'' in
\emph{Proceedings of the 2020 Conference on Empirical Methods in Natural
Language Processing}, 2020.

\end{thebibliography}

\end{document}
