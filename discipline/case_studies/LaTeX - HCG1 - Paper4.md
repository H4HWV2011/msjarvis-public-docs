\documentclass[12pt,letterpaper]{article}

% ---- Core packages (order matters) ----
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
\usepackage{cite}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{caption}
\usepackage{listings}
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{tcolorbox}
\usepackage{hyperref}
% ---- TikZ libraries ----
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, fit,
                decorations.pathreplacing, calc, backgrounds,
                automata, shadows.blur}
% ---- pgfplots ----
\pgfplotsset{compat=1.18}
% ---- tcolorbox: NO skins/tikzfill, just breakable ----
\tcbuselibrary{breakable,fitting}
% ---- page geometry ----
\geometry{margin=1in, top=1.3in}
\setlength{\headheight}{15pt}

\geometry{margin=1in, top=1.3in}

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
% HYPERREF
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
                 quant
