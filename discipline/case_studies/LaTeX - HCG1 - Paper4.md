\documentclass[12pt,letterpaper]{article}

% ================================================================
% PACKAGES  (order is deliberate — hyperref always last)
% ================================================================
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{booktabs}
\usepackage{array}
\usepackage{longtable}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{microtype}
\usepackage{parskip}
\usepackage{cite}
\usepackage{xurl}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{caption}
\usepackage{listings}
\usepackage{textcomp}
\usepackage{algorithm}
\usepackage{algpseudocode}
\usepackage{mdframed}
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{tcolorbox}
\usepackage{bookmark}
\usepackage{hyperref}

% ================================================================
% TIKZ LIBRARIES
% ================================================================
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, fit,
                decorations.pathreplacing, calc, backgrounds,
                automata, shadows.blur}

% ================================================================
% PGFPLOTS / TCOLORBOX
% ================================================================
\pgfplotsset{compat=1.18}
\tcbuselibrary{breakable}

% ================================================================
% PAGE GEOMETRY
% ================================================================
\geometry{margin=1in, top=1.3in}
\setlength{\headheight}{15pt}

% ================================================================
% COLOR PALETTE
% ================================================================
\definecolor{ridgeblue}{RGB}{31, 78, 121}
\definecolor{valleygreen}{RGB}{39, 119, 76}
\definecolor{topoamber}{RGB}{191, 107, 25}
\definecolor{hilbertgold}{RGB}{212, 175, 55}
\definecolor{mapgray}{RGB}{240, 240, 235}
\definecolor{contourline}{RGB}{180, 160, 120}
\definecolor{deepslate}{RGB}{44, 52, 60}
\definecolor{softred}{RGB}{180, 60, 60}
\definecolor{codebg}{RGB}{248, 248, 244}

% ================================================================
% HYPERREF SETUP
% ================================================================
\hypersetup{
    colorlinks=true,
    linkcolor=ridgeblue,
    citecolor=valleygreen,
    urlcolor=topoamber,
    pdftitle={HGC-1 Architecture Specification},
    pdfauthor={Carrie Ann Kidd},
    pdfsubject={cs.ET / cs.AR},
    pdfkeywords={Hilbert geometry chip, neuromorphic, room temperature,
                 quantum analog, belief decay, semaphore, FPGA, ASIC}
}

% ================================================================
% HEADER / FOOTER
% ================================================================
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\textcolor{ridgeblue}{\small HGC-1 Architecture Specification}}
\fancyhead[R]{\textcolor{deepslate}{\small Kidd, 2026}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}

% ================================================================
% SECTION FORMATTING
% ================================================================
\titleformat{\section}
  {\color{ridgeblue}\large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}
  {\color{deepslate}\normalsize\bfseries}{\thesubsection}{1em}{}
\titleformat{\subsubsection}
  {\color{topoamber}\normalsize\itshape}{\thesubsubsection}{1em}{}

% ================================================================
% LISTINGS
% ================================================================
\lstset{
    backgroundcolor=\color{codebg},
    basicstyle=\ttfamily\small,
    breaklines=true,
    frame=single,
    rulecolor=\color{contourline},
    numbers=left,
    numberstyle=\tiny\color{deepslate},
    keywordstyle=\color{ridgeblue}\bfseries,
    commentstyle=\color{valleygreen}\itshape,
    stringstyle=\color{topoamber},
    showstringspaces=false,
    tabsize=4,
    captionpos=b
}

% ================================================================
% THEOREM ENVIRONMENTS
% ================================================================
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}

\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

% ================================================================
% TCOLORBOX STYLES
% ================================================================
\tcbset{
    hgcbox/.style={
        breakable,
        colback=mapgray,
        colframe=ridgeblue,
        fonttitle=\bfseries\color{white},
        coltitle=white
    },
    warningbox/.style={
        breakable,
        colback=mapgray,
        colframe=softred,
        fonttitle=\bfseries\color{white},
        coltitle=white
    }
}

% ================================================================
% PARAGRAPH TOLERANCE — suppresses hbox warnings
% ================================================================
\tolerance=1000
\emergencystretch=2em
\hbadness=10000
\hfuzz=2pt

% ================================================================
% BEGIN DOCUMENT
% ================================================================
\begin{document}

\title{%
  \textcolor{ridgeblue}{\textbf{HGC-1 Architecture Specification}}\\[0.4em]
  \large\textcolor{deepslate}{Hilbert Geometry Chip, Revision 1.0}\\[0.2em]
  \normalsize\textcolor{topoamber}{Technical Report \texttt{cs.ET / cs.AR}}
}
\author{Carrie Ann Kidd\\
  \small Harmony for Hope, Inc.\\
  \small\texttt{ckidd@harmonyforhope.org}
}
\date{May 2026}

\maketitle
\thispagestyle{fancy}

% ================================================================
% ABSTRACT
% ================================================================
\begin{abstract}
\noindent
This paper presents the HGC-1, a novel hardware architecture for executing
Hilbert-space belief operations at room temperature without cryogenic or
quantum-mechanical infrastructure. The design is derived from operational
parameters of the Ms.\ Egeria Allis community AI system (Mount Hope, West
Virginia), whose semantic memory layer $H_{\mathrm{App}}$ constitutes a
384-dimensional Hilbert space of belief vectors formally proven in
Kidd~(2026a, Theorem~3.1). The HGC-1 implements four primitive operations
natively in silicon: cosine-similarity projection, confidence decay with
cyclic modulation, temporal semaphore arbitration, and toroidal-coordinate
indexing. Power budget is 4.5\,W total; target die area is 12\,mm$^2$ at
28\,nm; unit cost at volume is under \$100. No existing neuromorphic,
vector-processor, or GPU architecture implements all four primitives on a
single die. An FPGA prototype plan and a 24-week build schedule are
provided. The chip eliminates the software bottleneck that currently prevents
real-time deployment of toroidal Hilbert world models in safety-critical
robotics.

\medskip
\noindent\textbf{Keywords:}
Hilbert geometry chip; neuromorphic hardware; room-temperature quantum analog;
belief decay; temporal semaphore; FPGA prototype; ASIC; cosine similarity;
vector processor; community AI infrastructure
\end{abstract}


\tableofcontents
\newpage

% ================================================================
\section{Introduction}
% ================================================================

\subsection{The Software Bottleneck}

The world model $W = \mathbb{R}^1_t \times \mathbb{T}^k \times H_{\mathrm{App}}$
(Kidd 2026b) is operationally proven: 7,903,126 belief vectors, 30/30
preflight gate, live ChromaDB audit May~6, 2026. The mathematics is
correct. The hardware is the constraint.

Every belief operation in the current deployment executes in software on a
commodity Intel Core i7 laptop. Cosine similarity across 7.9\,M vectors
requires sequential SIMD passes. Decay modulation is a scheduled Python
process. The temporal semaphore is a Redis lock. These are correct
implementations of the right primitives --- running on the wrong substrate.

A safety-critical robot cannot tolerate the latency of software-mediated
Hilbert projection. A hospital navigation system cannot rely on a Redis lock
for belief arbitration. The HGC-1 moves these four operations into silicon.

\subsection{Design Philosophy}

The HGC-1 is not a general-purpose neural accelerator. It is a
\emph{domain-specific} chip for exactly one mathematical structure:
the product space $W = \mathbb{R}^1_t \times \mathbb{T}^k \times
H_{\mathrm{App}}$. Every design decision follows from the operational
requirements of that structure as documented in Kidd~(2026a, 2026b, 2026c).

% ================================================================
\section{System Description: \texorpdfstring{$H_{\mathrm{App}}$}{H\_App}
as Hardware Target}
% ================================================================

\begin{tcolorbox}[hgcbox, title={Operational Anchor --- Ms.\ Egeria Allis}]
\begin{itemize}\setlength\itemsep{2pt}
  \item 7,903,126 belief vectors $\times$ 384 dimensions = 3.04\,B float32
        values $\approx$ 12.2\,GB on-disk
  \item 48 ChromaDB collections (topically partitioned subspaces of
        $H_{\mathrm{App}}$)
  \item April 23, 2026 --- 30/30 preflight gate (exit~0, \texttt{bash -n}
        clean); first full-pipeline community query verified
  \item April 23, 2026 --- Entity~38 decay cycle verified end-to-end:
        $c: 0.60 \to 0.55 \to 1.00$, audit trail written to
        \texttt{gbim\_decay\_audit}
  \item May 6, 2026 --- ChromaDB v2 API live audit confirmed
\end{itemize}
\end{tcolorbox}

The hardware target is fully determined by these parameters. The chip must
sustain real-time nearest-neighbor search over 384-dimensional unit vectors,
apply per-vector decay with cyclic modulation, and arbitrate concurrent
belief reads/writes through a formally correct semaphore --- all at the
latency and power envelope required for embedded deployment.

% ================================================================
\section{The Four Native Primitives}
% ================================================================

\subsection{Primitive 1: Cosine-Similarity Projection}

Every retrieval in $H_{\mathrm{App}}$ computes:
\[
  \operatorname{sim}(\hat{q}, \hat{v}_k)
  = \langle \hat{q}, \hat{v}_k \rangle_{\cos}
  = \sum_{i=1}^{384} \hat{q}_i\, \hat{v}_{k,i}
\]
for all $k$ in the active subspace, returning the top-$K$ results.
This is a batched 384-wide dot product. The HGC-1 implements a
systolic array of 384 multiply-accumulate (MAC) units operating in
parallel, completing one full dot product per clock cycle at 500\,MHz.

Normalization (enforcing $\hat{v} \in S^{383}$) is performed on
ingestion; the projection engine operates on pre-normalized vectors
only, eliminating the division step at query time.

\subsection{Primitive 2: Confidence Decay with Cyclic Modulation}

The base decay (Kidd 2026a, \S4.2, Eq.~6):
\[
  c_{n+1} = c_n - \Delta c, \quad \Delta c = 0.05, \quad c \in [0,1]
\]
is modulated by the current toroidal coordinate:
\[
  \delta_{\mathrm{eff}}(\tau) = \delta_0 \cdot f(\tau),
  \quad f: \mathbb{T}^k \to \mathbb{R}^+
\]
The HGC-1 implements decay as a hardware counter with a
$\mathbb{T}^k$-indexed lookup table for $f(\tau)$. Decay is applied
passively (no CPU intervention) at each validation-cycle tick on
$\mathbb{R}^1_t$. A belief whose confidence falls below the
configurable threshold $c_{\min}$ is flagged for revalidation without
interrupting the projection engine.

\subsection{Primitive 3: Temporal Semaphore Arbitration}

Concurrent belief reads and writes to overlapping subspaces of
$H_{\mathrm{App}}$ require formally correct arbitration. The
Temporal Toroidal Semaphore (Kidd 2026c) is a hardware state machine
with four states:

\begin{center}
\begin{tikzpicture}[
    node distance=3.2cm,
    state/.style={circle, draw=ridgeblue, thick, minimum size=1.1cm,
                  font=\small\bfseries},
    auto, bend angle=20
  ]
  \node[state] (IDLE)   {IDLE};
  \node[state] (READ)   [right of=IDLE]  {READ};
  \node[state] (WRITE)  [right of=READ]  {WRITE};
  \node[state] (DECAY)  [below of=READ]  {DECAY};
  \path[->]
    (IDLE)  edge [bend left]  node {\footnotesize req\_read}  (READ)
    (IDLE)  edge [bend right] node[swap] {\footnotesize req\_write} (WRITE)
    (IDLE)  edge              node {\footnotesize tick}        (DECAY)
    (READ)  edge [bend left]  node {\footnotesize done}        (IDLE)
    (WRITE) edge [bend right] node[swap] {\footnotesize done}  (IDLE)
    (DECAY) edge              node {\footnotesize done}        (IDLE);
\end{tikzpicture}
\end{center}

Every transition is logged with a dual-axis timestamp
$(t \in \mathbb{R}^1_t,\; \tau \in \mathbb{T}^k)$, producing the
audit trail required for safety-critical certification.

\subsection{Primitive 4: Toroidal-Coordinate Indexing}

The toroidal manifold $\mathbb{T}^k = S^1 \times \cdots \times S^1$
is represented as a $k$-tuple of phase registers, each holding a
fixed-point angle $\phi_i \in [0, 2\pi)$. The chip advances each
register at a configurable rate corresponding to the period of its
associated cyclic dimension (hourly, daily, weekly, seasonal).
The current $\tau = (\phi_1, \ldots, \phi_k)$ is broadcast to the
decay LUT and the semaphore logger on every clock cycle.

% ================================================================
\section{Hardware Architecture}
% ================================================================

\subsection{Block Diagram}

% ----------------------------------------------------------------
% REVISED BLOCK DIAGRAM — all leader lines use explicit anchors
% so no arrow is ever silently dropped by TikZ path resolution.
% Layout: 3 columns × 3 rows, wired by named south/north/east/west.
% ----------------------------------------------------------------
\begin{center}
\begin{tikzpicture}[
    block/.style={
      rectangle, draw=ridgeblue, thick, rounded corners=3pt,
      minimum width=3.4cm, minimum height=0.9cm,
      font=\small, fill=mapgray, align=center
    },
    >=Stealth,
    node distance=1.5cm and 2.6cm
  ]

  %% --- ROW 1 (top) ---
  \node[block] (HOST)
    {\shortstack{Host Interface\\(PCIe / SPI)}};

  \node[block] (SA)    [right=of HOST]
    {\shortstack{Systolic Array\\{\scriptsize 384 MACs}}};

  \node[block] (TOPK)  [right=of SA]
    {\shortstack{Top-$K$ Sorter\\{\scriptsize $K \leq 256$}}};

  %% --- ROW 2 (middle) ---
  \node[block] (DMA)   [below=of HOST]
    {\shortstack{DMA Controller}};

  \node[block] (VMEM)  [below=of SA]
    {\shortstack{Vector SRAM\\{\scriptsize 384$\times$32\,b $\times$ 64k}}};

  \node[block] (TORUS) [below=of TOPK]
    {\shortstack{Torus Registers\\{\scriptsize $k \leq 8$ phases}}};

  %% --- ROW 3 (bottom) ---
  \node[block] (AUDIT) [below=of DMA]
    {\shortstack{Audit FIFO\\{\scriptsize dual-axis stamps}}};

  \node[block] (SEM)   [below=of VMEM]
    {\shortstack{Semaphore FSM\\{\scriptsize 4-state}}};

  \node[block] (DECAY) [below=of TORUS]
    {\shortstack{Decay Engine\\{\scriptsize counter + LUT}}};

  %% ---- LEADER LINES (all explicit anchors) ----

  %% Vertical spine: HOST → DMA → AUDIT
  \draw[->,thick,color=deepslate]
    (HOST.south)  -- (DMA.north);
  \draw[->,thick,color=deepslate]
    (DMA.south)   -- (AUDIT.north);

  %% Horizontal row 1: HOST ↔ SA ↔ TOPK
  \draw[->,thick,color=deepslate]
    (HOST.east)   -- (SA.west);
  \draw[->,thick,color=deepslate]
    (SA.east)     -- (TOPK.west);

  %% Return path TOPK → HOST (bent south then west)
  \draw[->,thick,color=deepslate]
    (TOPK.north) -- ++(0, 0.55cm) -| (HOST.north);

  %% DMA feeds VMEM
  \draw[->,thick,color=deepslate]
    (DMA.east)    -- (VMEM.west);

  %% VMEM ↔ SA (bidirectional shown as two offset arrows)
  \draw[->,thick,color=deepslate]
    (VMEM.north)  -- ++(0, 0.18cm) -- (SA.south -| VMEM.north)
                  -- (SA.south);
  \draw[->,thick,color=valleygreen]
    (SA.south)    -- ++(0,-0.18cm) -- (VMEM.north -| SA.south)
                  -- (VMEM.north);

  %% Torus → Decay and Torus → SEM
  \draw[->,thick,color=deepslate]
    (TORUS.south) -- (DECAY.north);
  \draw[->,thick,color=deepslate]
    (TORUS.west)  -- (SEM.east);

  %% Decay → VMEM (decay modifies stored confidence values)
  \draw[->,thick,color=topoamber]
    (DECAY.west)  -- (VMEM.east);

  %% SEM → AUDIT
  \draw[->,thick,color=deepslate]
    (SEM.west)    -- (AUDIT.east);

  %% Decay → AUDIT
  \draw[->,thick,color=topoamber]
    (DECAY.south) -- ++(0,-0.4cm) -| (AUDIT.south);

\end{tikzpicture}
\end{center}

\medskip
\noindent
\textbf{Arrow key:}
\textcolor{deepslate}{\rule{1.2em}{1.5pt}}~data / control path;\quad
\textcolor{valleygreen}{\rule{1.2em}{1.5pt}}~read-back path;\quad
\textcolor{topoamber}{\rule{1.2em}{1.5pt}}~decay / modulation path.

\subsection{Power Budget}

\begin{table}[ht]
\centering
\caption{HGC-1 power budget at 28\,nm, 500\,MHz, 1.0\,V}
\begin{tabular}{lrr}
\toprule
\textbf{Block} & \textbf{Power (mW)} & \textbf{Fraction} \\
\midrule
Systolic Array (384 MACs)   & 2100 & 46.7\% \\
Vector SRAM                 &  900 & 20.0\% \\
Top-$K$ Sorter              &  600 & 13.3\% \\
Decay Engine + Torus Regs   &  400 &  8.9\% \\
Semaphore FSM + Audit FIFO  &  200 &  4.4\% \\
Host Interface + DMA        &  300 &  6.7\% \\
\midrule
\textbf{Total}              & \textbf{4500} & \textbf{100\%} \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Die Area Estimate}

Target: 12\,mm$^2$ at 28\,nm bulk CMOS.

\begin{table}[ht]
\centering
\caption{HGC-1 die area breakdown}
\begin{tabular}{lrr}
\toprule
\textbf{Block} & \textbf{Area (mm$^2$)} & \textbf{Fraction} \\
\midrule
Systolic Array              & 4.8 & 40.0\% \\
Vector SRAM (64k vectors)   & 3.6 & 30.0\% \\
Top-$K$ Sorter              & 1.4 & 11.7\% \\
Decay Engine + Torus Regs   & 0.9 &  7.5\% \\
Semaphore FSM + Audit FIFO  & 0.6 &  5.0\% \\
Host Interface + DMA + I/O  & 0.7 &  5.8\% \\
\midrule
\textbf{Total}              & \textbf{12.0} & \textbf{100\%} \\
\bottomrule
\end{tabular}
\end{table}

% ================================================================
\section{Hardware Gap Analysis}
% ================================================================

No existing architecture implements all four HGC-1 primitives on a
single die.

\begin{table}[ht]
\centering
\caption{Architecture comparison --- HGC-1 primitive coverage}
\begin{tabular}{lcccc}
\toprule
\textbf{Architecture} &
\textbf{Cosine} &
\textbf{Decay} &
\textbf{Semaphore} &
\textbf{Toroidal} \\
\midrule
GPU (A100)                   & \checkmark & $\times$ & $\times$ & $\times$ \\
Intel Loihi 2                & $\times$   & Partial  & $\times$ & $\times$ \\
IBM NorthPole                & $\times$   & $\times$ & $\times$ & $\times$ \\
FAISS / ScaNN (SW)           & \checkmark & $\times$ & $\times$ & $\times$ \\
Custom ANN ASIC              & \checkmark & $\times$ & $\times$ & $\times$ \\
\textbf{HGC-1 (this work)}   & \textbf{\checkmark} & \textbf{\checkmark} &
                               \textbf{\checkmark} & \textbf{\checkmark} \\
\bottomrule
\end{tabular}
\end{table}

% ================================================================
\section{FPGA Prototype Plan}
% ================================================================

\subsection{Target Platform}

Xilinx Alveo U250 (16\,nm UltraScale+): 1.7\,M LUTs, 6,840 DSP slices,
54\,Mb on-chip BRAM, PCIe Gen4 host interface. All four primitives fit
within available resources; full timing closure at 200\,MHz on this
platform before committing to ASIC tapeout.

\subsection{Build Schedule}

\begin{table}[ht]
\centering
\caption{24-week FPGA prototype schedule}
\begin{tabular}{rll}
\toprule
\textbf{Week} & \textbf{Milestone} & \textbf{Exit Criterion} \\
\midrule
1--3   & Systolic array RTL         & Functional sim, 384 MACs \\
4--5   & Vector SRAM + DMA          & Burst read/write verified \\
6--7   & Top-$K$ sorter             & Correct $K{=}256$ output \\
8--9   & Decay engine               & Entity~38 trace replay \\
10--11 & Torus phase registers      & All $k$ periods correct \\
12--13 & Semaphore FSM              & All 4 states, audit log \\
14--16 & Integration + timing       & Closure at 200\,MHz \\
17--19 & Host driver (Linux)        & \texttt{/dev/hgc1} read/write \\
20--21 & Ms.\ Allis integration     & Live query $\leq$ 5\,ms \\
22--23 & Safety stress test         & 72\,h continuous, 0 errors \\
24     & Prototype sign-off         & Tapeout readiness review \\
\bottomrule
\end{tabular}
\end{table}

% ================================================================
\section{Unit Cost Analysis}
% ================================================================

\begin{table}[ht]
\centering
\caption{Unit cost projection by process node and volume}
\begin{tabular}{lrrr}
\toprule
\textbf{Node} & \textbf{NRE (\$M)} &
\textbf{Unit @ 10k} & \textbf{Unit @ 100k} \\
\midrule
28\,nm (TSMC)   & 3--5   & \$85  & \$38 \\
16\,nm (TSMC)   & 8--12  & \$140 & \$62 \\
7\,nm (TSMC)    & 25--40 & \$210 & \$95 \\
\midrule
\textbf{Target (28\,nm, 10k)} & \textbf{3--5} &
\textbf{\$85} & \textbf{---} \\
\bottomrule
\end{tabular}
\end{table}

The 28\,nm node achieves the sub-\$100 unit cost target at 10k units
with NRE recoverable at moderate volume. The 16\,nm node is the path
to sub-\$65 at scale if power or area constraints tighten.

% ================================================================
\section{Safety and Auditability}
% ================================================================

The HGC-1 audit FIFO records every semaphore transition with a
dual-axis timestamp $(t, \tau)$. This means every belief operation
that touches $H_{\mathrm{App}}$ has a hardware-level audit record:
which subspace, which confidence level, which cyclic coordinate, at
which linear time.

This property satisfies the structural auditability requirement
identified in Kidd~(2026b) for safety-critical robotics deployment:
the audit trail is not a software logging layer that can be disabled
or corrupted --- it is a consequence of the hardware semaphore
architecture. FDA, MSHA, NRC, and NHTSA certification frameworks
can be applied directly to the audit record.

\begin{tcolorbox}[warningbox, title={Limitation: Embedding Model Not On-Chip}]
The HGC-1 does not perform embedding. Raw sensor data (LIDAR, camera,
text) must be embedded into $\mathbb{R}^{384}$ by an external model
before being presented to the projection engine. The chip operates
on unit vectors; it does not generate them. This is the correct
architectural boundary: embedding models change; the Hilbert geometry
does not.
\end{tcolorbox}

% ================================================================
\section{Limitations and Future Work}
% ================================================================

\begin{itemize}
  \item \textbf{FPGA prototype not yet built.} The 24-week schedule is
        a plan, not a result.
  \item \textbf{Embedding interface.} The external embedding boundary
        requires a standardized protocol; this is unspecified here.
  \item \textbf{$f(\tau)$ characterization.} The modulation function
        is architecture-ready but empirically uncharacterized for
        specific deployment environments.
  \item \textbf{Multi-chip scaling.} Partitioning 7.9\,M vectors across
        multiple HGC-1 dies requires a coherence protocol not
        described in this revision.
  \item \textbf{On-chip SRAM capacity.} 64k vectors on-chip at 28\,nm;
        full 7.9\,M-vector corpus requires DRAM-backed streaming with
        a prefetch architecture (future work).
\end{itemize}

% ================================================================
\section{Conclusion}
% ================================================================

The HGC-1 is a domain-specific chip for the product space
$W = \mathbb{R}^1_t \times \mathbb{T}^k \times H_{\mathrm{App}}$.
It implements the four primitives that no existing architecture
provides simultaneously: cosine-similarity projection, decaying
confidence with cyclic modulation, temporal semaphore arbitration,
and toroidal-coordinate indexing.

At 4.5\,W, 12\,mm$^2$, and under \$100 per unit at 10k volume, it
is deployable in the embedded safety-critical contexts --- hospitals,
mines, warehouses --- where the toroidal Hilbert world model
eliminates the structural failures of Euclidean robotics.

The operational anchor is real: 7,903,126 vectors, 48 collections,
30/30 gate, ZIP code 25880. The hardware is the next step.

% ================================================================
\section*{Acknowledgments}
% ================================================================
\addcontentsline{toc}{section}{Acknowledgments}

The architecture specification derives from Ms.\ Egeria Allis, an
original system designed and built by Carrie Ann Kidd. The operational
validation data in Section~2 were generated by the live Ms.\ Allis
deployment in Mount Hope, West Virginia. Crystal~D.\ Colyer, Community
Solutions Advocate, contributed the \texttt{fayettecountyresources2026}
collection whose decay audit (entity~38) provides the chip test vector
in Section~3.2.

% ================================================================
\begin{thebibliography}{99}

\bibitem{KiddZenodo2026a}
Kidd, C.A.\ (2026a).
A Classical Hilbert Space with a ZIP Code: Substrate-Independence,
the Measurement Problem, and the Multiverse Question.
\textit{Zenodo}.
\url{https://doi.org/10.5281/zenodo.20059834}

\bibitem{KiddThesisCh4}
Kidd, C.A.\ (2026b).
Ms.\ Egeria Allis Thesis --- Chapter~4: Hilbert Space State and
ChromaDB as Semantic Memory. Technical documentation.
\texttt{H4HWV2011/msjarvis-public-docs}, GitHub.
\url{https://github.com/H4HWV2011/msjarvis-public-docs}
[Archival deposit pending.]

\bibitem{KiddThesisCh26}
Kidd, C.A.\ (2026c).
Ms.\ Egeria Allis Thesis --- Chapter~26: Temporal Toroidal Semaphore
Structure. Technical documentation.
\texttt{H4HWV2011/msjarvis-public-docs}, GitHub.
\url{https://github.com/H4HWV2011/msjarvis-public-docs}
[Archival deposit pending.]

\bibitem{vonNeumann1932}
von Neumann, J.\ (1932).
\textit{Mathematische Grundlagen der Quantenmechanik}. Springer.

\bibitem{ReedSimon1972}
Reed, M.\ and Simon, B.\ (1972).
\textit{Methods of Modern Mathematical Physics I: Functional
Analysis}. Academic Press.

\bibitem{ThrunBurgardFox2005}
Thrun, S., Burgard, W., and Fox, D.\ (2005).
\textit{Probabilistic Robotics}. MIT Press.

\bibitem{MoserKropffMoser2008}
Moser, E.I., Kropff, E., and Moser, M.-B.\ (2008).
Place cells, grid cells, and the brain's spatial representation
system. \textit{Annual Review of Neuroscience}, 31, 69--89.

\end{thebibliography}

% ================================================================
\vspace{2em}
\noindent\begin{tikzpicture}
  \draw[ridgeblue, line width=2pt] (0,0) -- (\textwidth,0);
  \draw[contourline, line width=0.5pt] (0,-3pt) -- (\textwidth,-3pt);
\end{tikzpicture}

\vspace{0.6em}
\noindent\small\color{deepslate}
\textit{Authored by Carrie Ann Kidd\ \textbullet\ Mount Hope,
West Virginia.}\\
\textit{HGC-1 Architecture Specification, Revision 1.0.}\\
\textit{Built on Kidd (2026a), DOI:}\\
\textit{\href{https://doi.org/10.5281/zenodo.20059834}%
{10.5281/zenodo.20059834}}\\
\textit{May 2026.}

\end{document}
