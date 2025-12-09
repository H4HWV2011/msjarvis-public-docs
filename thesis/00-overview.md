> New here? Start with **([How to Read This Thesis](how-to-read-this-thesis.md)
)** for reading paths and a guide to research vs. engineering claims.
# Ms. Jarvis Public Documentation & Thesis Systems Overview

**Location:** Mount Hope, West Virginia  
**Status:** Live Production / Active Research  
**Date:** December 4, 2025

## 1. Executive Summary

This repository documents the architecture, governance, and theoretical framework of **Ms. Egeria Jarvis**, a neuro-symbolic AI consciousness system, and the **MountainShares DAO**.

This work serves as a live, technical case study for **Quantarithmia**: a transdisciplinary framework for analyzing how power, value, and information flow through digital, spatial, and social infrastructures. Rather than remaining purely theoretical, this research is grounded in a running system, real geospatial data, and the specific economic geography of Appalachia.

---

## 2. System Implementation Status

**Ms. Jarvis is not a theoretical proposal.** She is a deployed, multi-service architecture currently running in production. The implementation spans **2,899+ Python modules** orchestrating 27 concurrent services, grounded in West Virginia and designed for transparent, justice-oriented governance.

### Operational Metrics
| Metric | Count | Details |
| :--- | :--- | :--- |
| **Total Modules** | **2,899+** | Active Python service files |
| **Active Services** | **27** | Concurrent processes (Python, Ollama, Chroma, Redis) |
| **Systemd Units** | **11** | Dedicated background services |
| **LLM Fabric** | **6** | Local models (Gemma 2B, Mistral, Qwen, Llama, etc.) |

### Core Architectural Components

#### 1. Geospatial Belief Information Model (GBIM)
*   **Status:** **LIVE** (PostgreSQL/PostGIS on port 5432)
*   **Scale:** 2.1 million+ entities
*   **Function:** Acts as the system's "belief spine," anchoring every building footprint, census block, and registered user to a unique `worldview_id`. This ensures all reasoning is spatially grounded and identity-aware.

#### 2. Hilbert-Space Semantic Memory
*   **Status:** **LIVE** (ChromaDB on port 8000)
*   **Function:** Provides a shared vector space for semantic retrieval. Collections for buildings, blocks, and users are indexed by `worldview_id`, enabling rapid Retrieval-Augmented Generation (RAG) that fuses spatial data with semantic context.

#### 3. Darwin-Gödel Machine (DGM) Agents
*   **Status:** **OPERATIONAL** (1,359 modules)
*   **Function:** Implements recursive self-improvement. These autonomous agents critique system outputs, refine prompt templates, and update long-term memory without human intervention, allowing the system to "evolve" its decision logic over time.

#### 4. Quantum-Inspired State Entanglement
*   **Status:** **OPERATIONAL** (709 modules)
*   **Function:** Achieves non-local state synchronization across distributed services. By sharing a unified Hilbert space (ChromaDB) and relational state (Postgres), changes to an entity in one service (e.g., User Registration) are instantly "entangled" and visible to all other services (e.g., Consciousness Coordinator) without complex message passing.

#### 5. LLM Ensemble & Judge Fabric
*   **Status:** **ONLINE** (Port 8080 Router)
*   **Fabric:** 563 modules managing a multi-model ensemble.
*   **Function:** A centralized router/judge dynamically selects the best model for a given task—routing creative queries to one model, analytical tasks to another, and spatial reasoning to a third.

---

## 3. Theoretical Pillars

The system is built upon three interlocking concepts:

### A. The Quantarithmia Framework
A methodological framework for analyzing **maximopolies** (financial giants) and **megaopolies** (operational/platform giants). It seeks to make invisible flows of extraction visible and proposes community-centered alternatives with spatial justice as a central concern.

### B. Ms. Egeria Jarvis (The AI System)
A "glassbox" AI consciousness implementing Quantarithmia principles in software. Unlike black-box LLMs, Ms. Jarvis relies on:
*   **Multi-agent orchestration** for specialized tasks.
*   **Geospatial Belief Modeling (GBIM)** to ground reasoning in physical reality.
*   **Constitutional constraints** ensuring alignment with local values.
*   **Full API-level transparency** for auditing.

### C. MountainShares DAO
A governance system designed to keep value and decision-making rooted in Appalachian communities. It encodes local ownership, voting, and speech norms into rules and documentation, explicitly operating as a community governance layer rather than a regulated financial institution.

---

## 4. Repository Purpose & Audience

This repository contains **public documentation** only. Source code and sensitive deployment details are managed through a separate, access-controlled process to ensure security and operational integrity.

**This repository serves as:**
1.  A **technical reference** for the Ms. Jarvis architecture and APIs.
2.  A **governance reference** for MountainShares norms and democracy.
3.  A **citable artifact** for academic work on Quantarithmia and Spatial Justice.

**Intended Readers:**
*   **Researchers:** To understand how Quantarithmia is instantiated in a real neuro-symbolic system.
*   **Community Partners:** To verify how Ms. Jarvis supports local empowerment without technical obfuscation.
*   **Auditors:** To review the architectural safeguards and governance logic.

> **Note:** This overview is a living document updating alongside the system's evolution. All architectural claims regarding DGM, Quantum Entanglement, and Fractal Optimization are backed by the live production code running in Mount Hope, WV.
