> New here? Start with **[How to Read This Thesis](../docs/how-to-read-this-thesis.md)** for reading paths and a guide to how engineering claims, research claims, and live system behavior relate.

# Ms. Jarvis Public Documentation & Thesis Systems Overview

**Location:** Mount Hope, West Virginia  
**Status:** Live Steward System / Active Research  
**Last Updated:** January 5, 2026

## 1. Executive Summary

This work sits within **polymathamatical geography**, an emerging field that integrates quantitative geography, systems theory, AI architectures, and community-centered design to study how power, value, and information move through real places. Within that field, **Quantarithmia** is the specific framework used here to analyze maximopolies and megaopolies and to design community-first alternatives in Appalachia.

This repository documents the architecture, governance, and theoretical framework of **Ms. Egeria Jarvis**, a bounded AI Steward System, and the **MountainShares DAO**.

This work serves as a live, technical case study for **Quantarithmia**: a transdisciplinary framework for analyzing how power, value, and information flow through digital, spatial, and social infrastructures. Rather than remaining purely theoretical, this research is grounded in a running system, real geospatial data, and the specific economic geography of Appalachia.

---

## 2. System Implementation Status

**Ms. Jarvis is not a theoretical proposal.** It is a deployed, multi-service Steward System currently running in production. The implementation spans **51,000+ Python modules** across 175 services, grounded in West Virginia and designed for transparent, justice-oriented governance.

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

* **Status:** **LIVE (FOUNDATION)** (PostgreSQL/PostGIS via PostgreSQL 16 main on port 5432)  
* **Scale:** Millions of spatial and entity records across blocks, footprints, structures, infrastructures, and related features  
* **Function:** Acts as the system’s geospatial and belief spine, anchoring buildings, census units, infrastructures, and registered users to stable identifiers and regions so that higher-level reasoning is spatially grounded and auditable. GBIM’s full belief/edge semantics are being incrementally surfaced as explicit schemas and services on top of this foundation.

#### 2. Hilbert-Space Semantic Memory

* **Status:** **LIVE (PRIORITIZED SUBSET)** (semantic memory services backed by Chroma and Postgres)  
* **Function:** Provides a shared vector/semantic space for retrieval. Today, collections for buildings, blocks, key infrastructures, and several cognitive/memory domains are indexed with stable IDs, enabling Retrieval-Augmented Generation (RAG) that fuses spatial data with semantic and historical context. Additional PostGIS layers are being progressively mirrored into this Hilbert-space as embeddings and enriched metadata.

#### 3. Steward-Oriented Orchestration

* **Status:** **OPERATIONAL** (distributed across the current service stack)  
* **Function:** Coordinates many specialized services—geospatial queries, memory retrieval, document analysis, routing, and evaluation—under explicit governance constraints. The Steward System does not act as an autonomous agent or authority; it assembles evidence, scenarios, and explanations as inputs to human and community decision-making.

#### 4. Quantum-Inspired State Entanglement

* **Status:** **OPERATIONAL**  
* **Function:** Achieves non-local state synchronization across distributed services by sharing unified semantic state (memory services) and relational state (Postgres). Changes to an entity in one service (for example, a GBIM update) are reflected consistently to others (such as geospatial reasoning and memory services) without bespoke point-to-point message passing.

#### 5. LLM Ensemble & Judge / Router Fabric

* **Status:** **ONLINE** (coordinated behind the Cloudflare tunnel and internal services)  
* **Fabric:** Multi-model ensemble (local and remote models) coordinated by routing and evaluation components.  
* **Function:** Routing logic selects and coordinates the best models or tools for a given task—creative, analytical, or spatial—then aggregates their outputs into a single, stewarded response, subject to governance and transparency requirements.

---

## 3. Theoretical Pillars

The system is built upon three interlocking concepts.

### A. The Quantarithmia Framework

A methodological framework for analyzing **maximopolies** (financial giants) and **megaopolies** (operational/platform giants). It seeks to make invisible flows of extraction visible and proposes community-centered alternatives with spatial justice and stewardship as central concerns.

### B. Ms. Egeria Jarvis (The Steward System)

A “glassbox” AI Steward System implementing Quantarithmia principles in software. Unlike black-box LLM deployments, Ms. Jarvis relies on:

* **Multi-service orchestration** for specialized tasks rather than a single monolithic model.  
* **Geospatial Belief Information Modeling (GBIM)** to ground reasoning in physical reality and concrete evidence.  
* **Constitutional and governance constraints** to align behavior with local values and community norms.  
* **API-level and data-level transparency** so that inputs, evidence paths, and outputs can be inspected and audited.

### C. MountainShares DAO

A governance system designed to keep value and decision-making rooted in Appalachian communities. It encodes local ownership, voting, and speech norms into rules and documentation, explicitly operating as a community governance layer rather than as a regulated financial institution or autonomous economic actor.

---

## 4. Repository Purpose & Audience

This repository contains **public documentation** only. Source code and sensitive deployment details are managed through a separate, access-controlled process to ensure security and operational integrity.

**This repository serves as:**

1. A **technical reference** for the Ms. Jarvis Steward System architecture and APIs.  
2. A **governance reference** for MountainShares norms and democratic practice.  
3. A **citable artifact** for academic work on Quantarithmia, Steward Systems, and Spatial Justice.

**Intended Readers:**

* **Researchers:** To understand how Quantarithmia and stewardship concepts are instantiated in a real, geospatially grounded AI system.  
* **Community Partners:** To verify how Ms. Jarvis supports local empowerment without technical obfuscation or unchecked autonomy.  
* **Auditors:** To review the architectural safeguards, governance logic, and data flows.

> **Note:** This overview is a living document that updates alongside the system’s evolution. All architectural claims regarding GBIM, quantum-inspired state entanglement, routing/orchestration, and optimization strategies are anchored in the live production stack running in Mount Hope, WV.
