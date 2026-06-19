# Architecture and Licensing

## System Overview

The MountainShares technology stack powers the MountainShares Commons (DUNA), providing the core technical infrastructure for the mutual-credit ledger, governance workflows, geospatial services, and community-facing applications.

The system is designed so that:

- community mutual credit (EMS and M$) remains benefits-safe inside the Commons, with its securities-law treatment under review by securities counsel, and
- intellectual property, commercial operations, and founder-capital instruments reside on the Kidd's Technical Services (KTS) side, under separate agreements and applicable legal frameworks.

This chapter describes the high-level architecture and the licensing relationships among Harmony for Hope, Inc. (H4H), the DUNA/MountainShares Commons, and KTS.

---

## Entities and Roles

### Harmony for Hope, Inc. (H4H)

H4H is a West Virginia 501(c)(3) public charity that serves as the initial charitable anchor and early implementation sponsor for MountainShares.

Within this architecture:

- H4H operates programmatic and community-facing functions,
- may host infrastructure during early phases,
- administers grants and community partnerships,
- and sponsors the Commons until the DUNA structure is fully stood up.

H4H does **not** own the Commons as private property, does **not** issue founder equity through EMS, and does **not** hold resident EMS or M$ balances as proprietary assets.

### MountainShares Commons (DUNA)

The MountainShares Commons, organized through the DUNA legal wrapper, is the community layer that governs:

- the EMS recognition ledger,
- M$ mutual-credit balances,
- governance participation,
- resident-facing programs,
- and associated community data.

The Commons is member-governed, benefits-sensitive, and non-equity. Participants hold program rights and mutual-credit balances, not ownership interests.

### Kidd's Technical Services (KTS)

KTS is the founder-side technical and commercial vehicle through which:

- ALLIS and GBIM intellectual property are held and commercialized,
- technical operations and commercial services may be offered,
- founder capital and any appreciating founder instruments are structured.

As of the current record, KTS is planned as a West Virginia for-profit LLC / PBC, to be formed. Until formation, references to "KTS" describe Carrie Ann Kidd operating personally and do not create a separate legal entity.

KTS is structurally separate from H4H and the Commons. Any appreciating founder instrument lives on the KTS side and never in the hands of residents via community EMS.

---

## Technical Architecture

### Core Components

The MountainShares stack includes, at a minimum:

- **ALLIS (Artificial Learning Location Intelligence System)** — the core AI and geospatial reasoning engine.
- **GBIM (Geobelief Information Model)** — the structured belief and feature store used to represent geospatial and community knowledge.
- **Microservices and containerized services** — deployed via container orchestration, supporting APIs, background processing, and integrations.
- **Data stores** — including relational databases (e.g., PostgreSQL/PostGIS), object storage, and specialized indices for vector search and geospatial analytics.
- **Public-facing applications** — web and mobile interfaces for participants, administrators, and partners.

The architecture is modular, with clear boundaries between:

- community-facing features (Commons layer), and
- proprietary engines and commercial extensions (KTS layer).

### Deployment Model

The system is designed for deployment on infrastructure controlled by or on behalf of H4H and/or the Commons during early phases, with technical operations provided under agreements with KTS or directly by the founder in a pre-entity capacity.

Over time, the intent is to:

- maintain Commons-facing services in a manner accountable to community governance through the DUNA, and
- clearly separate KTS commercial deployments, pilots, or extended services from the core Commons infrastructure.

---

## Intellectual Property Ownership

### ALLIS and GBIM

ALLIS, GBIM, and associated proprietary algorithms, models, and system designs are owned or controlled by KTS, subject to separate agreements.

This includes:

- model architectures,
- code,
- schemas and ontologies unique to GBIM,
- proprietary training pipelines,
- and related documentation authored as part of the commercial system.

Community-facing use of ALLIS and GBIM occurs under license, not by transferring ownership of the underlying intellectual property to H4H or the Commons.

### Community Data and Content

Data and content contributed by participants, partners, and H4H through MountainShares are subject to:

- privacy and data-governance rules,
- program-specific data-sharing agreements,
- and any applicable legal obligations.

To the extent permitted by law and program rules, the Commons may:

- store,
- process,
- analyze,
- and visualize community data through ALLIS and GBIM,

while remaining subject to:

- data minimization,
- ethical use,
- and community-governance controls.

Ownership of contributed content remains with the original owners except where explicitly licensed or transferred under separate agreements.

---

## Licensing Relationships

### KTS to H4H

KTS licenses ALLIS, GBIM, and related proprietary components to H4H under one or more agreements that may include:

- a master license,
- service or support agreements,
- and supplemental data-processing or integration addenda.

These agreements:

- grant H4H rights necessary to operate MountainShares as a charitable program,
- define permitted uses and limitations,
- set out support and maintenance expectations,
- and maintain clear separation between H4H's charitable operations and KTS's commercial interests.

### KTS to DUNA / Commons

KTS licenses ALLIS and related capabilities to the DUNA / MountainShares Commons at arm's length, under terms designed to:

- support community-governed operations,
- protect residents and participants,
- maintain transparency around system behavior and constraints,
- and avoid embedding private founder equity into community EMS or governance flows.

License terms may be:

- cost-based or subsidized in early phases,
- adjusted over time under community and sponsor review,
- and tied to performance and safety benchmarks approved by governance.

### H4H and DUNA Relationship

H4H sponsors the initial deployment and operation of the Commons, with the DUNA providing the structural community governance layer.

Over time, the relationship is expected to:

- formalize the Commons' legal structure through the DUNA,
- define how H4H and the DUNA share responsibilities, data, and infrastructure,
- and ensure that community governance has meaningful oversight of how the system operates on the ground.

---

## Non-Equity and Non-Inurement Safeguards

This architecture and licensing structure is designed so that:

- community mutual credit (EMS and M$) remains benefits-safe inside the Commons, with its securities-law treatment under review by securities counsel,
- participant EMS and M$ balances are not equity,
- no founder equity is created inside H4H-administered programs, the DUNA, or EMS accounts,
- any appreciating founder instrument exists solely on the KTS side, under appropriate legal frameworks.

Licensing fees, if any, paid by H4H or the DUNA to KTS must:

- be arm's length,
- support program operation and sustainability,
- and avoid creating private inurement or disguised equity within the charitable or commons layers.

Founder capital instruments, if implemented, sit outside this architecture and are documented in separate KTS agreements.

---

## Conflict of Interest and Governance

Because the founder may have roles in H4H, the Commons, and KTS, the following safeguards apply:

- All H4H–KTS and DUNA–KTS agreements are subject to documented conflict-of-interest and recusal procedures.
- The founder abstains from governance decisions where she stands on both sides of the transaction, except as permitted by law and policy under defined recusal procedures.
- Key architectural and licensing decisions are documented, reviewable, and subject to community governance where they materially affect the Commons.

No single individual may unilaterally change architectural or licensing terms in a way that undermines:

- the non-equity commitment of the Commons,
- benefits-sensitive design,
- or the separation between community and commercial layers.

---

## Evolution and Change Management

This Architecture and Licensing chapter is expected to evolve as:

- KTS is formally formed and capitalized,
- the DUNA is implemented and operational,
- system metrics scale (e.g., services, features, and geospatial coverage),
- and legal and regulatory contexts change.

Any material change to:

- IP ownership,
- licensing terms between KTS and H4H or the DUNA,
- the separation between community EMS and founder commercial instruments,

must be recorded in updated governance documents and, where appropriate, subjected to community review and formalization under the governing amendment processes.

---

### Changelog

| Version | Date | Summary |
|---|---|---|
| 1.0 | Prior | Initial draft |
| 1.1 | June 19, 2026 | **Amendment A — two spots:** (1) §System Overview bullet 1 — removed "non-appreciating"; replaced with "remains benefits-safe inside the Commons, with its securities-law treatment under review by securities counsel." (2) §Non-Equity and Non-Inurement Safeguards bullet 1 — same reframe applied. All other structural no-equity language unchanged. |

---

*Architecture and Licensing — MountainShares Commons*
*Harmony for Hope, Inc. (initial sponsor)*
*Kidd's Technical Services (planned owner of ALLIS / GBIM)*
*Draft — Not legal, tax, securities, or benefits advice*

---

**End of Architecture and Licensing v1.1**
