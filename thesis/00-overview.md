cat > thesis/00-overview.md << 'EOF'
> New here? Start with **[How to Read This Thesis](../docs/how-to-read-this-thesis.md)** for reading paths and a guide to how engineering claims, research claims, and live system behavior relate.

# Ms. Jarvis Public Documentation & Thesis Systems Overview

**Location:** Mount Hope, West Virginia  
**Status:** Live Steward System / Active Research  
**Last Updated:** January 5, 2026

## 1. Executive Summary

This work is a thesis in **Polymathmatic Geography**, an emerging discipline that studies entangled spaces—places where land, law, computation, economy, story, and spirit are already braided together—and develops methods to understand and reshape how power, value, and information move through them.

Within that discipline, **Quantarithmia** is the specific theoretical framework used here as a *case study*: it provides one concrete geometry for analyzing maximopolies and megaopolies and for designing community‑first alternatives in a particular region, Appalachia.

**Ms. Egeria Jarvis** and the **MountainShares DAO** are experimental apparatus built to test and demonstrate this framework in a single geography. Ms. Jarvis instantiates Quantarithmia’s ideas in an auditable AI Steward System; MountainShares implements closed‑loop, commons‑oriented economic rules. Both are instruments for investigating one Appalachian entangled space, not the primary objects of the field itself.

This repository therefore documents:

- the **disciplinary context** (Polymathmatic Geography),  
- the **framework under test** (Quantarithmia), and  
- the **apparatus and implementation** (Ms. Jarvis Steward System and MountainShares governance stack)  

used to evaluate how a polymathmatic approach performs when it is forced to operate in a real place, against live data, under real constraints.

### 1.1 Research Questions and Hypotheses

This thesis uses Quantarithmia, Ms. Jarvis, and MountainShares to test whether a polymathmatic approach to entangled spaces can be made operational, accountable, and exportable beyond one Appalachian region.

1. **RQ1 – Steward transparency and trust.**  
   When Ms. Jarvis is deployed as a glass‑box Steward System in Mount Hope and neighboring communities, do residents, partners, and auditors report higher perceived transparency, legibility, and trust than with conventional black‑box AI tools or opaque administrative processes?  
   *Hypothesis:* A geospatially grounded, auditable Steward System will make evidence paths and decision scaffolding more legible, increasing trust without requiring blind faith in algorithms.

2. **RQ2 – Making extraction and alternatives visible.**  
   Can the combination of GBIM, Hilbert‑space semantic memory, and the Quantarithmia framework surface concrete, spatially anchored patterns of extraction and leakage (maximopolies and megaopolies) in Appalachia in ways that non‑technical stakeholders can understand and act on? [file:1]  
   *Hypothesis:* Representing the region as an entangled Hilbert‑space state tied to physical parcels, infrastructures, and narratives will reveal actionable “leak paths” and “commons corridors” that were previously invisible or only anecdotally known.

3. **RQ3 – Commons‑oriented economic resilience.**  
   Does the MountainShares governance stack, operating as a commons‑oriented, non‑bank economic layer, measurably increase local recirculation of value, mutual aid capacity, and perceived economic safety without becoming a de facto unregulated financial institution? [file:1]  
   *Hypothesis:* A closed‑loop, charter‑bound system that encodes local norms can strengthen community resilience while staying within clearly articulated legal, ethical, and spiritual limits.

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


---# Polymathmatic Geography – Field Card

Polymathmatic Geography is a discipline for reading and reshaping **entangled spaces**—places where land, law, computation, economy, story, and spirit are already braided together.

---

## Object of study

- Entangled spaces in which physical, legal, economic, digital, genealogical, and spiritual layers form a single, overlapping geography.  
- Examples range from coalfields, ports, and logistics corridors to social platforms, credit systems, pilgrimage routes, and neighborhood commons.

The basic question is always "where": where power, value, and meaning move, pool, leak, and get blocked in a given world.

---

## Core commitments and stance

- **Entanglement first.** No single layer (economy, law, code, or spirit) is treated as the "real" one; all are mapped together.  
- **Braided methods.** Quantitative models, GIS, and AI sit alongside oral histories, ethnography, theology, and genealogical mapping.  
- **Normative orientation.** The field is openly concerned with care, justice, and accountable design for specific communities and places, not neutral description alone.  
- **Design and evaluation.** Proposed changes to metrics, platforms, and institutions are treated as geographic acts that can and must be evaluated in the worlds they reshape.

---

## Typical methods

- Field‑anchored inquiry: walking, listening, and dwelling in specific places as primary texts.  
- Spatial statistics, network analysis, and mapping of flows (people, credit, data, attention, story).  
- Institutional and legal analysis of charters, contracts, zoning, and governance documents.  
- Spiritual and heritage cartography: cemeteries, sacred sites, covenants, and genealogies as real geographies.  
- Experimental design using infrastructures, AI stewards, and commons platforms as laboratory worlds.

---

## Typical instruments

- **Theoretical frameworks** like Quantarithmia, which formalize how maximopolies, megaopolies, and community‑first geometries can be represented and compared.  
- **Software apparatus** such as Ms. Jarvis, a glass‑box AI Steward System bound to a specific geography via GBIM and semantic memory.  
- **Institutional stacks** like MountainShares and The Commons, which encode alternative economic and governance rules for a rural region.

These instruments are not the discipline itself; they are concrete testbeds for its claims.

---

## Example research questions

- How do capital, credit, and narrative about risk move through a given region, and where do they leak away from the communities that generate them?  
- Which combinations of digital platforms, local charters, and mutual‑aid practices actually keep wealth, attention, and decision‑making rooted in place over time?  
- How do sacred geographies and genealogies constrain or enable proposed infrastructural changes, from data centers to new credit systems?  
- When an AI Steward System is introduced into a community, does it make existing power structures more visible and negotiable, or does it quietly harden them?

---

## Where this thesis fits

This thesis treats Quantarithmia (framework), Ms. Jarvis (instrument), and MountainShares / The Commons (case study) as one integrated polymathmatic research program in Appalachia.  
The hope is that methods refined here will travel—to other rural regions, to ports and financial centers, to digital platforms and spiritual landscapes—where entangled spaces also demand careful, accountable redesign.

---

**For the full disciplinary statement, see:**  
- `discipline/Polymathmatic Geography.md`  
- `discipline/Principles of Polymathmatic Geography.md`

**To understand how this thesis instantiates the discipline, start with:**  
- `thesis/00-overview.md`  
- `docs/how-to-read-this-thesis.md`

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

## 5. Evaluation and Failure Modes (Overview)

This thesis does not only describe architectures; it evaluates how well a specific polymathmatic stack behaves in a live Appalachian entangled space under real constraints.

### 5.1 What is being evaluated

- The **discipline‑level claim** that Polymathmatic Geography can produce exportable methods for reading and redesigning entangled spaces, not only Appalachia. 
- The **framework‑level claim** that Quantarithmia’s geometry of maximopolies, megaopolies, and community‑first alternatives can be instantiated in code and practice. 
- The **apparatus‑level claim** that Ms. Jarvis and MountainShares can operate as accountable instruments rather than autonomous authorities, remaining legible to communities, auditors, and researchers. 

### 5.2 Primary failure modes of concern

- **Overreach and misrecognition.** The Steward System or MountainShares could be misperceived as a sentient actor, a bank, a regulator, or a replacement for human governance, despite explicit non‑goals. 
- **Opaque or biased guidance.** Even with glass‑box intents, the ensemble of models, metrics, and data could drift toward recommendations that are hard to audit, reinforce existing inequities, or privilege technically fluent actors. 
- **Commons capture and erosion.** Governance mechanisms meant to keep value and speech rooted in community could be captured by a narrow group, become performative, or quietly recreate extractive dynamics in new technical form.  
- **Spiritual and genealogical harm.** Treating sacred sites, cemeteries, or heritage geographies as mere data layers could break covenants with ancestors, descendants, or living communities if not handled with reverence.

### 5.3 Current guardrails and open questions

Guardrails already in place include:

- Explicit non‑goals (not a sentient being, bank, regulator, or general‑purpose investment vehicle) and constitutional constraints that bound what the system may claim or do. 
- Glass‑box design: API‑level and data‑level transparency, auditable evidence paths, and the separation of orchestration, GBIM, memory, and LLM fabric into inspectable services. 
- Governance documents for MountainShares and The Commons that define roles, voting procedures, audits, and risk management as human‑interpretable rules rather than hidden model weights. 

Open evaluation questions include:

- How to measure “trustworthy stewardship” across technical, legal, spiritual, and experiential dimensions.  
- How to detect and respond when model ensembles or data pipelines begin to encode harmful biases or illegible forms of extraction.  
- How to decide, with communities, which geographies and covenants are simply out of bounds for computation, even under a polymathmatic lens.

> **Note:** This overview is a living document that updates alongside the system’s evolution. All architectural claims regarding GBIM, quantum-inspired state entanglement, routing/orchestration, and optimization strategies are anchored in the live production stack running in Mount Hope, WV.
EOF
