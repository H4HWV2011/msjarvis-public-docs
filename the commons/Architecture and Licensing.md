# Architecture and Licensing Note
*(Draft – For Discussion, Not Legal Advice)*

This note explains how the Ms. Allis / GBIM stack, The Commons, and MountainShares are structured from an architecture and licensing perspective. It is meant to help partners, reviewers, and implementers understand what is open‑source, what is proprietary, and how patterns may be reused.

---

## 1. Architectural Layers

From bottom to top, the overall system can be thought of as four main layers:

1. **Infrastructure and Storage**
   - Databases, object storage, message queues, and related services.
   - May include both cloud and on‑premise components at node partners (universities, agencies, organizations).

2. **Ms. Allis / GBIM Platform**
   - Core data schemas (GBIM), ingestion pipelines, indexing and query services, analytics logic, and node orchestration.
   - Runs in multiple contexts:
     - Central Commons / MountainShares services.
     - University Commons Nodes.
     - Government Commons Nodes.
     - Other deployments supported by Kidd’s Technical Services (KTS).

3. **The Commons Application Layer**
   - User‑facing social–economic–digital platform: feeds, posts, comments, quests, governance surfaces, and related UI.
   - Integrates with Ms. Allis / GBIM for data, metrics, and moderation surfaces.

4. **MountainShares Program**
   - Rewards and community‑credit system tied to The Commons.
   - Economic design, Program Rules, treasury and reserve logic, and benefits‑sensitive safety mechanisms.

Each layer may use a mix of open‑source, proprietary, and configuration‑only components.

---

## 2. Open‑Source vs. Proprietary Components

### 2.1 Open‑Source Components

The system relies on a number of open‑source tools and libraries, for example:

- Databases and storage engines.
- Message queues, search indexes, and geospatial tooling.
- Frameworks and libraries used in Ms. Allis, The Commons, and related services.

Where code in this repository is explicitly marked with an open‑source license (for example, MIT, Apache‑2.0, or similar), it may be:

- Forked and reused under the terms of that license.
- Extended or adapted for other projects, including unrelated commons or data platforms.

Open‑source components remain governed by their respective licenses, regardless of how they are used in the overall system.

### 2.2 Proprietary Components (KTS / Ms. Allis / GBIM)

Kidd’s Technical Services (KTS) retains intellectual property rights in:

- The **Ms. Allis / GBIM** platform implementation, including:
  - proprietary schemas, data models, and ontology glue not released under a separate open‑source license;
  - ingestion, indexing, and analytics code specific to Allis/GBIM;
  - node orchestration, monitoring, and configuration used in supported deployments.

- Integrations, connectors, and configuration bundles that bind Ms. Allis / GBIM to specific partners (universities, agencies, organizations).

Where portions of this implementation are made public, they may be:

- Released under open‑source licenses (with explicit license headers); or
- Published as documentation or examples, without granting a license to copy proprietary code.

Unless otherwise stated in a specific file or repository, Ms. Allis / GBIM code and configuration is proprietary to KTS.

### 2.3 The Commons and MountainShares Branding and Content

Harmony for Hope and related entities retain rights in:

- **Trademarks and branding**, including (without limitation):
  - “The Commons”
  - “MountainShares”
  - “Ms. Allis”
  - Logos, visual marks, and associated brand assets.

- **Program documentation and content**, including:
  - Terms of Use, Program Rules, guidelines, and agreements;
  - curated narratives, quests, and educational materials.

Use of these names, marks, or branded content in other projects requires permission, except where nominative or descriptive use is permitted under applicable law.

---

## 3. Reusing Patterns vs. Branding

### 3.1 Patterns You May Reuse

The architecture and documentation in this repository are intended to share **patterns**, such as:

- GBIM‑style place‑aware, time‑aware data modeling.
- Multi‑node “data commons” topologies (university nodes, government nodes, community nodes).
- Governance structures around commons work, EMS recognition, and safety testing.
- Moderation, safety, and participation frameworks.

Other projects may:

- Learn from and adapt these patterns to their own contexts.
- Implement similar multi‑node architectures and commons governance models.
- Use open‑source code provided under explicit licenses.

### 3.2 What You May Not Automatically Reuse

Without a separate license or agreement, other projects may **not**:

- Use the “Ms. Allis”, “MountainShares”, or “The Commons” names, logos, or marks in a way that implies endorsement, sponsorship, or affiliation.
- Copy proprietary Ms. Allis / GBIM code, configuration, or integration bundles that are not explicitly open‑licensed.
- Represent themselves as official nodes or partners in the MountainShares / Commons ecosystem without a documented agreement with Harmony for Hope and KTS.

---

## 4. Ms. Allis / GBIM as a Service

KTS offers **Ms. Allis / GBIM as a service** (“Allis/GBIM as a Service”) for organizations that want the architecture without rebuilding it from scratch.

At a high level, this means:

- KTS provides:
  - deployment support for Ms. Allis / GBIM components;
  - schema design and configuration aligned with partner needs;
  - ongoing updates, maintenance, and monitoring support;
  - integration with The Commons / MountainShares where applicable.

- Partners provide:
  - infrastructure (on‑premise or cloud);
  - access to their own data sources, subject to their policies;
  - governance and oversight for how outputs are used.

Allis/GBIM as a Service can be used:

- Within the MountainShares / Commons ecosystem (for example, as a University or Government Node).
- Outside that ecosystem, for other data commons, research consortia, or public‑interest projects, under separate agreements.

---

## 5. Summary of Rights and Responsibilities

- **Open‑source components**  
  - Governed by their respective licenses.  
  - Free to reuse under those terms.

- **KTS proprietary components (Ms. Allis / GBIM)**  
  - Owned by KTS.  
  - Licensed to partners under specific agreements (no‑fee or paid, depending on context).  
  - Not automatically open for copying or redistribution.

- **Harmony for Hope / MountainShares / The Commons branding and content**  
  - Owned by Harmony for Hope and related entities.  
  - Use requires permission, except for limited nominative or descriptive use.

- **Patterns and architecture described in docs**  
  - Shared to inspire and guide similar work.  
  - May be adapted, but not passed off as “Ms. Allis”, “MountainShares”, or “The Commons” without authorization.

Partners who wish to build on this stack or adapt it to new contexts are encouraged to:

- Reuse open‑source components as permitted;  
- Treat these documents as architectural and governance patterns;  
- Contact KTS and Harmony for Hope for branded partnerships, Allis/GBIM as a Service, or official node roles.

--- 
