# University Commons Node Partnership Overview
*(Draft for Discussion – Not Legal Advice)*

This document describes how a university (the “University Partner”) could realistically participate in the MountainShares / The Commons ecosystem as a **Commons Node Operator** and research collaborator. It is intended as a technical–policy overview for inclusion in public documentation and as a starting point for formal MOUs or agreements.

---

## 1. Purpose and Goals

A University Commons Node partnership has three primary goals:

1. **Durable regional memory.**  
   Provide long‑term, institutionally backed storage for key Appalachian cultural, economic, and resilience records (historic trail content, commons work logs, governance history, and related datasets).

2. **Decentralized research data management.**  
   Distribute storage and computation across multiple trusted institutions instead of a single data center, while maintaining coherent schemas and governance.

3. **Mutual value.**  
   Give the University high‑value, real‑world datasets for research and teaching, while giving MountainShares a stable, credible partner for data preservation and analysis.

The partnership is about **data and research infrastructure**, not about the University issuing, selling, or promoting MountainShares units.

---

## 2. What a University Commons Node Does

A University Commons Node is a combination of storage, services, and governance that runs under University IT and research‑data policies.

At a high level, the node:

- Hosts one or more **data “shards”** relevant to its region or focus, such as:
  - Heritage and trail content (historic trail entries, CLIO‑linked records, oral histories, photos, other media).
  - GBIM “memory” records: pseudonymous, structured logs of Earned MountainShares (EMS) hours, events, value interactions, and governance activity.
  - Resilience and environment records: NOAA‑derived weather series, storm and outage traces, emergency‑response interactions tied to specific places.
  - Aggregated indicators and KPIs derived from these sources.

- Runs defined **services and tools**, for example:
  - A containerized worker that ingests, validates, and indexes GBIM data.
  - A pinning or replication service for content‑addressed storage used by MountainShares (e.g., IPFS or a similar system).
  - Optional APIs or dashboards that expose public or research‑grade views of the data.

- Integrates with **central MountainShares infrastructure** via documented protocols:
  - Secure channels (VPN/SSH/HTTPS) to receive curated data pushes and updates.
  - Scheduled or event‑driven sync jobs.
  - Health and status reporting for monitoring.

The University Node does *not* run payment rails, hold user wallets, or control token economics. Those functions remain with Harmony for Hope and its designated technical operators.

---

## 3. Data Scope and Treatment

### 3.1 Data Categories

For clarity, MountainShares data replicated to a University Node are organized into categories such as:

- **Public / open data**
  - Aggregated KPIs (e.g., total EMS hours by county, circulation velocity, participation metrics).
  - Public heritage records that are already intended for general access (e.g., trail narratives, approved photos, and public‑facing Commons content).

- **Restricted research data**
  - Pseudonymous GBIM records keyed by internal IDs or UEIs instead of names.
  - De‑identified transaction and participation logs suitable for approved research and evaluation work.

- **Sensitive / controlled data**
  - Any records that could reasonably be re‑identified or that involve vulnerable populations or benefits‑sensitive participants.
  - These are encrypted at rest, and access requires explicit authorization and, where appropriate, ethics review on the University side.

Each dataset that is replicated to a University Node should come with a short metadata profile that states:

- What the dataset contains.
- Which category it falls into (public, restricted, sensitive).
- Who is allowed to access it and under what conditions.
- How long it is intended to be retained.

### 3.2 Identifiability and Safeguards

To protect participants:

- GBIM records replicated to University Nodes are **pseudonymous by default**, keyed by UEIs or internal IDs rather than direct personal identifiers (names, SSNs, etc.).
- Sensitive fields are either:
  - removed from the replicated dataset, or
  - encrypted so that they are not readable without keys controlled by MountainShares backend services.

The University Node should not store raw identity verification documents, payment card data, or other high‑risk PII used in KYC or payment processing. Those remain solely in MountainShares’ secure payment and identity systems.

### 3.3 Retention and Immutable Layers

Some MountainShares data (for example, governance logs and historic content hashes) may be written to immutable or append‑only systems.

The partnership should acknowledge:

- Certain records are intended as part of a **permanent historical and governance record**.
- Even where application‑layer access is limited, low‑level content identifiers or encrypted blobs may persist.
- Sensitive personal details are not written directly into public immutable layers; instead, University Nodes host curated, privacy‑respecting replicas.

Retention policies should state:

- Which datasets are intended for long‑term archival (e.g., heritage content, governance history).
- Which datasets may be rotated to cold storage or summarized over time (e.g., raw low‑level transaction logs).

---

## 4. Roles and Responsibilities

### 4.1 Harmony for Hope / MountainShares

Harmony for Hope and its technical operators are responsible for:

- Designing and maintaining the **data model and schemas** (GBIM), including field definitions, ontologies, and update procedures.
- Curating and preparing datasets for replication to University Nodes, including:
  - anonymization or pseudonymization,
  - encryption of sensitive fields,
  - quality control and documentation.
- Maintaining Terms, Privacy Policy, Program Rules, and governance documents that define how data are collected, used, and shared with participants.
- Managing all aspects of the **MountainShares economic system**:
  - token issuance rules,
  - PMS/EMS mechanics,
  - treasury and reserve logic,
  - legal and regulatory obligations (including any securities, money‑transmission, and benefits‑related issues).
- Providing technical support for:
  - initial node setup (images, configuration),
  - upgrades and schema changes,
  - monitoring hooks and incident response coordination.

### 4.2 University Partner

The University Partner is responsible for:

- Provisioning and maintaining the **infrastructure** for the Commons Node:
  - servers or virtual machines,
  - storage allocations,
  - network connectivity,
  - backups and disaster recovery to a standard comparable to research data services.
- Applying University **security and compliance controls**:
  - access controls and authentication for local staff,
  - patching and system updates,
  - local logging and incident response.
- Governing access to replicated datasets under University **data governance and ethics** processes, including:
  - IRB review where required,
  - data‑use approvals for internal and external researchers,
  - adherence to any restrictions in the Data Sharing / Data Use Agreement.
- Optionally developing:
  - local dashboards or tools for teaching and research,
  - outreach and training for students and partners who want to use the data.

The University is **not** expected to:

- Operate payment or wallet services.
- Market MountainShares as an investment product.
- Take responsibility for the financial performance or legal classification of MountainShares.

---

## 5. Data Sharing and Use Agreements

Formal collaboration will require one or more written agreements, likely including:

- A **Data Sharing Agreement (DSA)** or **Data Use Agreement (DUA)** that specifies:
  - which datasets are shared with the University Node,
  - the permitted uses (e.g., academic research, teaching, non‑commercial evaluation),
  - prohibited uses (e.g., re‑identification attempts, commercial resale, certain law‑enforcement uses without due process),
  - publication and authorship expectations,
  - any required acknowledgements when publishing results or derivatives.

- A **Node Operations MOU** or similar, covering:
  - infrastructure responsibilities and service expectations,
  - security and incident‑response coordination,
  - points of contact on both sides,
  - a basic framework for cost‑sharing or in‑kind contributions.

The documentation in this repository is intended as a starting point for these agreements and not a substitute for institution‑specific legal review.

---

## 6. Regulatory and Legal Posture

### 6.1 MountainShares Program

The MountainShares Program is developed and administered by a nonprofit and is framed as a **closed‑loop rewards and community‑credit system**. Key points include:

- MountainShares are not bank deposits, not legal tender, and not guaranteed to have any particular external cash value.
- EMS (earned units) are primarily for in‑network use, recognition, and governance and are not designed for general cash redemption.
- PMS (purchased units) have limited refundability and are subject to program rules and treasury constraints.
- Participation may have **benefits and tax implications**, especially for individuals on means‑tested programs; users are informed of these risks in the Program Terms and related documents.

If, in the future, any aspect of MountainShares is treated as a regulated financial instrument, Harmony for Hope and its advisors are responsible for the associated filings, registrations, or exemptions. The University Partner does not act as an issuer, underwriter, broker, or financial intermediary by operating a Commons Node.

### 6.2 University’s Role

The University’s role is limited to:

- Hosting and serving defined datasets as a **data custodian**.
- Participating in and benefiting from a **data commons** for research, teaching, and community engagement.
- Optionally collaborating on methods, analysis, and publications.

The University:

- Does not sell or promote MountainShares as an investment.
- Does not guarantee any financial return to participants.
- Does not provide individualized benefits or financial advice based on MountainShares participation.

Any limited receipt of MountainShares units by the University (if such a mechanism is ever used) should be framed as programmatic support or recognition for participation, not as equity or a speculative asset.

---

## 7. Security, Privacy, and Ethics

The partnership should codify a set of minimum expectations:

- **Security**
  - Encryption in transit for data transfers between MountainShares infrastructure and the University Node.
  - Encryption at rest for any datasets that are not explicitly public.
  - Role‑based access control for staff and researchers.
  - Procedures for vulnerability patching and security incident handling.

- **Privacy**
  - Use of pseudonymous identifiers where possible.
  - Avoidance of direct storage of high‑risk PII (e.g., identity documents, financial account numbers).
  - Clear communication of the limits of de‑identification and the possibility of re‑identification in small or rare populations, with associated restrictions on data use.

- **Ethics**
  - Recognition that many datasets describe vulnerable communities, benefits‑sensitive households, and historically marginalized groups.
  - Requirements for IRB or equivalent ethics review when datasets are used in ways that meet human‑subjects research definitions.
  - Community‑engaged practices where feasible, including sharing findings back with affected communities and considering impacts of analysis and publication.

---

## 8. Benefits and ROI for Each Party

### 8.1 For Communities and Participants

- More durable and transparent records of commons work, cultural preservation, and resilience activities.
- Better visibility into how value and opportunities move through specific Appalachian places.
- Stronger basis for funding, advocacy, and policy work grounded in local data.

### 8.2 For Harmony for Hope / MountainShares

- Long‑term, redundant storage and increased resilience of key datasets.
- Access to academic expertise, methods, and feedback.
- Stronger case for grants and partnerships that require institutionally supported data infrastructure.

### 8.3 For University Partners

- Rich, longitudinal, geospatial datasets for:
  - GIS, data science, and CS courses.
  - Public policy, social science, and humanities research.
  - Community‑based participatory research and extension work.

- Opportunities for:
  - Co‑authored publications and technical reports.
  - Student projects, theses, capstones, and practicums.
  - Distinctive positioning as a hub for “Appalachian digital commons” and rural technology work.

Return on investment here is primarily **research value, community impact, and institutional reputation**, not speculative financial gain.

---

## 9. Next Steps for Interested Universities

For universities considering a Commons Node partnership, a realistic sequence looks like:

1. **Exploratory discussion**
   - Meet with Harmony for Hope / MountainShares technical and governance leads.
   - Identify overlapping research and community priorities.

2. **Scoping and design**
   - Choose initial data shards and services (e.g., heritage + public KPIs to start).
   - Define storage, compute, and network requirements.

3. **Draft agreements**
   - Co‑develop a Data Sharing / Data Use Agreement aligned with University policies.
   - Draft a Node Operations MOU covering infra and governance.

4. **Pilot deployment**
   - Stand up a small Commons Node instance.
   - Sync and validate a limited dataset.
   - Use it in at least one course, lab, or pilot research project.

5. **Evaluation and expansion**
   - Review technical performance, governance experience, and community/research value.
   - Decide whether and how to expand to additional datasets or services.

This overview is intended to make those steps concrete and to show how a University Node can fit cleanly into existing research‑data and community‑engagement missions.

