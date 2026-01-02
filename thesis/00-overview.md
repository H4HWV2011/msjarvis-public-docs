> New here? Start with **[How to Read This Thesis](../docs/how-to-read-this-thesis.md)** for reading paths and a guide to how engineering claims, research claims, and live system behavior relate.

# Ms. Jarvis Public Documentation & Thesis Systems Overview

**Location:** Mount Hope, West Virginia  
**Status:** Live Production / Active Research  
**Last Updated:** January 2, 2026

## 1. Executive Summary

This work sits within **polymathamatical geography**, an emerging field that integrates quantitative geography, systems theory, AI architectures, and community-centered design to study how power, value, and information move through real places. Within that field, **Quantarithmia** is the specific framework used here to analyze maximopolies and megaopolies and to design community-first alternatives in Appalachia.

This repository documents the architecture, governance, and theoretical framework of **Ms. Egeria Jarvis**, a neuro-symbolic AI consciousness system, and the **MountainShares DAO**.

This work serves as a live, technical case study for **Quantarithmia**: a transdisciplinary framework for analyzing how power, value, and information flow through digital, spatial, and social infrastructures. Rather than remaining purely theoretical, this research is grounded in a running system, real geospatial data, and the specific economic geography of Appalachia.

---

## 2. System Implementation Status

**Ms. Jarvis is not a theoretical proposal.** She is a deployed, multi-service architecture currently running in production. The implementation spans **51,000+ Python modules** across 175 services, grounded in West Virginia and designed for transparent, justice-oriented governance.

### Operational Metrics

| Metric | Count | Details |
| :--- | :--- | :--- |
| **Total Modules** | **51,000+** | Active Python modules across all services (excluding venv and caches) |
| **Active Services** | **175** | Service directories in the current stack |
| **Systemd Units** | **4** | Deployed `jarvis-*` background units (systemd) |
| **Core Datastore** | **1** | PostgreSQL 16 main instance on `127.0.0.1:5432` |
| **Public Gateway** | **Cloudflare Tunnel** | `cloudflared-msjarvis.service` on `127.0.0.1:20242` forwarding external traffic |

### Core Architectural Components

#### 1. Geospatial Belief Information Model (GBIM)

* **Status:** **LIVE** (PostgreSQL/PostGIS via PostgreSQL 16 main on port 5432)  
* **Scale:** 2.1 million+ entities  
* **Function:** Acts as the system's "belief spine," anchoring every building footprint, census block, and registered user to a unique `worldview_id`. This ensures all reasoning is spatially grounded and identity-aware.

#### 2. Hilbert-Space Semantic Memory

* **Status:** **LIVE** (Semantic memory service on `jarvis-memory.service`, port 7007)  
* **Function:** Provides a shared vector/semantic space for retrieval. Collections for buildings, blocks, and users are indexed by `worldview_id`, enabling Retrieval-Augmented Generation (RAG) that fuses spatial data with semantic context.

#### 3. Darwin-Gödel Machine (DGM) Agents

* **Status:** **OPERATIONAL** (distributed across the current service stack)  
* **Function:** Implements recursive self-improvement. These autonomous agents critique system outputs, refine prompt templates, and update long-term memory without human intervention, allowing the system to "evolve" its decision logic over time.

#### 4. Quantum-Inspired State Entanglement

* **Status:** **OPERATIONAL**  
* **Function:** Achieves non-local state synchronization across distributed services. By sharing unified semantic state (memory services) and relational state (Postgres), changes to an entity in one service (e.g., GBIM query router on port 7205) are "entangled" and visible to other services (e.g., consciousness and memory services) without complex message passing.

#### 5. LLM Ensemble & Judge Fabric

* **Status:** **ONLINE** (coordinated behind the Cloudflare tunnel and internal services)  
* **Fabric:** Multi-model ensemble (21+ models, local and remote) coordinated by a judge and router.  
* **Function:** A centralized judge and router dynamically select and coordinate the best models for a given task—routing creative queries, analytical tasks, and spatial reasoning to specialized experts and aggregating their outputs into a single response.

---

## 3. Theoretical Pillars

The system is built upon three interlocking concepts.

### A. The Quantarithmia Framework

A methodological framework for analyzing **maximopolies** (financial giants) and **megaopolies** (operational/platform giants). It seeks to make invisible flows of extraction visible and proposes community-centered alternatives with spatial justice as a central concern.

### B. Ms. Egeria Jarvis (The AI System)

A "glassbox" AI consciousness implementing Quantarithmia principles in software. Unlike black-box LLMs, Ms. Jarvis relies on:

* **Multi-agent orchestration** for specialized tasks.  
* **Geospatial Belief Modeling (GBIM)** to ground reasoning in physical reality.  
* **Constitutional constraints** ensuring alignment with local values.  
* **Full API-level transparency** for auditing.

### C. MountainShares DAO

A governance system designed to keep value and decision-making rooted in Appalachian communities. It encodes local ownership, voting, and speech norms into rules and documentation, explicitly operating as a community governance layer rather than a regulated financial institution.

---

## 4. Repository Purpose & Audience

This repository contains **public documentation** only. Source code and sensitive deployment details are managed through a separate, access-controlled process to ensure security and operational integrity.

**This repository serves as:**

1. A **technical reference** for the Ms. Jarvis architecture and APIs.  
2. A **governance reference** for MountainShares norms and democracy.  
3. A **citable artifact** for academic work on Quantarithmia and Spatial Justice.

**Intended Readers:**

* **Researchers:** To understand how Quantarithmia is instantiated in a real neuro-symbolic system.  
* **Community Partners:** To verify how Ms. Jarvis supports local empowerment without technical obfuscation.  
* **Auditors:** To review the architectural safeguards and governance logic.

> **Note:** This overview is a living document that updates alongside the system's evolution. All architectural claims regarding DGM, quantum-inspired entanglement, and optimization strategies are backed by the live production code running in Mount Hope, WV.
