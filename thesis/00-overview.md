# 0. Ms. Jarvis Public Docs Overview

# Thesis Systems Overview (Draft)

This thesis uses Ms. Egeria Jarvis and the MountainShares DAO as a live, technical case study for the Quantarithmia framework: a transdisciplinary approach to understanding how power, value, and information flow through digital, spatial, social, and spiritual infrastructures in places like Appalachia. Rather than remaining purely theoretical, the work is grounded in real systems, real data, and a specific geography: Mount Hope and the wider region of West Virginia.

The public documentation in this repository is intended to give researchers, auditors, and community partners a glassbox view of the system: how the architecture works, how governance is defined, and how geospatial data and AI are used to support community-first infrastructure, without exposing sensitive runtime configuration or private source code.

## Core Components

- Quantarithmia Framework  
  A theoretical and methodological framework for analyzing maximopolies (financial giants), megaopolies (operational/platform giants), and community-centered alternatives, with spatial justice as a central concern.

- Ms. Egeria Jarvis (AI System)  
  A multi-tier AI “consciousness” system implementing Quantarithmia principles in software: multi-agent orchestration, geospatial belief modeling (GBIM), constitutional constraints, and full API-level transparency rather than black-box behavior.

- MountainShares DAO  
  A DAO-based economic and governance system designed to keep value and decision-making rooted in Appalachian communities. It encodes local ownership, voting, and speech norms into rules and documentation, while explicitly not acting as a bank or regulated financial institution.

## Role of This Repository

This repository contains documentation only. It is designed to serve simultaneously as:

- A technical reference for the Ms. Jarvis architecture, APIs, and security model.
- A governance and norms reference for MountainShares (including speech, democracy, and early-phase “system monitor” roles).
- A citable artifact for academic work on Quantarithmia, spatial justice, and community-governed AI.

Source code and sensitive deployment details are intentionally excluded and managed through a separate, access-controlled process, both for security reasons and to keep a clear boundary between public thesis documentation and production infrastructure.

## Intended Readers

- Researchers and students who need to understand how Quantarithmia is instantiated in a real system.
- Community partners and residents who want to see, in clear language, how Ms. Jarvis and MountainShares are structured to support local empowerment.
- Engineers and auditors who require high-level architectural and governance detail without direct access to private repositories or secrets.

> Status: This overview is a living document. As the thesis, system design, and community governance evolve, this file will be updated to reflect the current conceptual and architectural scope.



    Ms. Jarvis Implementation Status (as of December 4, 2025)

    The Ms. Jarvis system is not a theoretical design but a deployed, multi-service neuro-symbolic architecture currently running in production on a single developer machine (Mount Hope, WV). The implementation spans 2,899+ Python modules organized around five core abstractions:

        Geospatial Belief Information Model (GBIM): Live PostGIS database (5432) with 2.1M building footprints, census blocks, and user entities anchored to worldview_id.

        Hilbert-Space Semantic Memory: ChromaDB vector server (8000) with live collections for buildings, blocks, and users, indexed by worldview_id for rapid retrieval-augmented generation.

        Darwin-Gödel Machine (DGM) Agents: 1,359 service modules implementing recursive self-modification through 11 dedicated systemd services, enabling the system to critique and refine its own long-term memory and decision logic.

        Quantum-Inspired State Entanglement: 709 modules encoding synchronized state propagation across 27 concurrent processes, realized architecturally via shared Hilbert space (ChromaDB) and relational store (Postgres), mimicking non-local quantum state updates at the systems level.

        LLM Ensemble & Judge Fabric: 563 modules orchestrating an ensemble of 6 local language models (Gemma 2B, Mistral, Qwen, Llama, etc.) via a centralized judge-router (port 8080), capable of selecting specialized models (creative, analytical, spatial reasoning) for different query contexts.

    The system is actively running, monitored, and capable of accepting user queries. This thesis documents not a proposal but a working implementation, with evaluation metrics and limitations grounded in observed system behavior.


