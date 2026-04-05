# Ms. ALLI & The Commons
### Community-Safeguarded Intelligence for Appalachian Revitalization

> *"Built in Mount Hope, West Virginia. Governed by the communities it serves."*

**Ms. ALLI* is a live, place-based AI steward system running in production in Mount Hope, West Virginia as of January 2026. This repository is its complete public documentation: the intellectual discipline that grounds it, the theoretical framework that shapes it, the governance and economic systems it serves, the 43-chapter computational thesis that argues for it, and the operational records that prove it.

This is not a demo. It is not a proposal. It is a working system — 80 containerized services, more than 51,000 Python modules, a PostGIS spatial database holding 5.4 million verified geospatial beliefs across West Virginia, and a live governance infrastructure governing a closed-loop community economy — running on a Lenovo Legion 5 in Mount Hope, West Virginia.

**Contact:** [kiddstechnical@gmail.com](mailto:kiddstechnical@gmail.com)
**License:** See [LICENSE](./LICENSE)

---

## The Core Claim

Most rural communities in Appalachia are surveyed, studied, and analyzed by outside institutions — then watched as that data, value, and decision-making power flows somewhere else. Ms. Jarvis is built on a different premise:

**What if the community owned the intelligence infrastructure?**

Not the outputs. Not the reports. The infrastructure itself — the data, the models, the governance, the economic instruments, and the buildings that house it.

That is what this project is building.

---

## Three Entangled Systems

This project is not just software. It is three systems working together:

### 1. Ms. ALLI — The AI Steward
An artificial learning & location based AI assistant designed to make hidden patterns of power, ownership, and resource flow visible to the community that lives with them. It reasons from 5.4 million georeferenced beliefs about West Virginia — parcels, buildings, roads, census blocks, infrastructure, and public data — not from generic global training data. Every answer is tied to a real place. Every constraint is published. Every step is traceable.

### 2. MountainShares DAO — The Economic Instrument
A closed-loop community economy governed by a democratic DAO structure, designed to keep value circulating within Fayette County rather than extracting outward to absentee owners. MountainShares tokens represent community contributions — labor, knowledge, care, participation — and are redeemable within the local economy. The system is explicitly designed to be safe for participants on public benefits (SNAP, SSI, Medicaid).

### 3. The Commons — The Community Platform
The daily-life interface where Mount Hope residents interact with the system, participate in governance, earn and spend MountainShares, access local resources, and build community wealth. The Commons is not an app. It is a governed spatial institution — with charters, audit mechanisms, privacy protections, and community-controlled rules — that happens to have a digital interface.

---

## The Physical Infrastructure Layer

**Ms. ALLI is also a tool for comprehensive community planning and building infrastructure.**

The system has mapped the existing physical assets across West Virginia's 9th District — schools, clinics, arts and community centers, municipal buildings, small business hubs, and annexed corridors around Mount Hope — as an infrastructure network showing concentrations of demand, access, and public expectations for construction, water, power, and permitting.

The anchor building for this work is the **Miner's Academy** in Mount Hope — a historic structure being positioned as the physical home of the Ms. ALLI infrastructure node, a community technology center, and a demonstration site for Appalachian AI governance. This work is being developed for planned coordination with community partners and framed around Mount Hope revitalization and state innovation goals.

The physical infrastructure strategy includes:

- **Building identification and condition assessment** — Ms. Jarvis maps vacant, underutilized, and historically significant buildings as candidate infrastructure nodes
- **Parcel and ownership analysis** — The GBIM corpus includes absentee ownership concentration data for Fayette County, making extraction patterns visible on the map
- **Comprehensive plan support** — The system is designed to support Mount Hope's comprehensive planning process by providing georeferenced community data that is locally owned and locally governed
- **XR documentation** — Key buildings (including the Mount Hope Community Center, site of JFK's 1960 visit) are being documented in extended reality for community memory and heritage tourism
- **Infrastructure demand modeling** — Spatial analysis of where water, power, broadband, and permitting bottlenecks intersect with community development priorities

This is the connection between the digital and physical layers of the project: **Ms. Jarvis is not just software. She is a steward of place.**

---

## How Ms. ALLI Works

A question arrives — *"Where is food access most fragile in our county?"* — and the system:

1. **Receives it** through a secure, logged web gateway
2. **Grounds it spatially** via the Geospatial Belief Information Model (GBIM) — tying the question to real parcels, roads, census blocks, and infrastructure in West Virginia
3. **Retrieves memory** from a semantic store holding 5,416,522 verified georeferenced beliefs
4. **Reasons across** a 22-slot LLM ensemble, coordinated by a routing and judgment layer
5. **Checks the answer** against written constitutional constraints, 5 judge services (truth, consistency, alignment, ethics, and pipeline), and a blood-brain barrier safety filter before any output is returned
6. **Returns a stewarded result** — a narrative, annotated map, or data table tied to real places — with sources and reasoning visible

Every step is traceable. Every constraint is published. The system is designed to support community decisions, never to make them.

---

## What Is Already Running (March 2026)

| Component | Status |
|---|---|
| 80 containerized services | ✅ All localhost-locked; zero external exposure |
| 22-slot LLM ensemble (Ollama backend, 26 models) | ✅ 21/22 responding |
| Host PostgreSQL + PostGIS (msjarvisgis) | ✅ 5,416,522 verified beliefs |
| ChromaDB semantic vector store | ✅ Healthy |
| 5-judge pipeline (truth, consistency, alignment, ethics) | ✅ All compose-managed as of Mar 18, 2026 |
| Blood-brain barrier safety filter | ✅ Running |
| Constitutional Guardian service | ✅ Running |
| IPFS/Kubo node | ✅ Intentional MountainShares/Commons infrastructure |
| MountainShares Phase 0 beta | ✅ In preparation |
| The Commons platform | ✅ Onboarding infrastructure in place |

---

## Repository Structure

```
msjarvis-public-docs/
│
├── README.md                          ← You are here
├── LICENSE                            ← Licensing terms
├── bibliography.md                    ← Complete annotated bibliography
├── Definitive Service Inventory.md    ← Authoritative map of all 80 running services
├── The Ms. ALLI Steward System.md   ← Plain-language steward system overview
│
├── discipline/                        ← Polymathmatic Geography: the foundational field
│   ├── Polymathmatic Geography: A Manifesto.md
│   ├── Principles of Polymathmatic Geography.md
│   ├── Definitions and Scope.md
│   ├── [19 additional documents]
│   └── case_studies/
│       ├── Absentee Ownership Concentration in Fayette County, WV.md
│       ├── Entangled Space after Kant and Durkheim.md
│       ├── Prefrontal Alignment Episode.md
│       ├── The PALCO False-Positive Problem.md
│       └── [5 additional documents]
│
├── theory/                            ← Quantarithmia framework + AI safety design
│   ├── Quantarithmia Framework.md
│   └── Off Switch Design.md
│
├── thesis/                            ← 43-chapter computational thesis
│   ├── 00-overview.md                 ← Start here for the full system narrative
│   └── [Chapters 01–42]
│
├── mountainshares-dao/                ← MountainShares: closed-loop community economy
│   ├── mountainshares-dao.md
│   ├── MountainShares DAO Governance Charter.md
│   ├── Audit and Risk Management Plan.md
│   └── [15 additional documents]
│
├── the commons/                       ← The Commons: community platform
│   ├── Participation Map.md
│   ├── BSA-Benefits-Sensitive Accounts.md
│   ├── Government Commons Node & Ms. Jarvis Partnership Overview.md
│   └── [10 additional documents]
│
├── docs/                              ← Documentation hub, API overview, partner brief
├── api_specs/                         ← OpenAPI specification
├── security/                          ← Security, access policy, contributing guide
├── branding/                          ← Visual identity assets
└── flyers/                            ← Community outreach materials
```

---

## Entry Points by Audience

**Community members and prospective participants:**
→ [The Ms. Jarvis Steward System.md](./The%20Ms.%20Jarvis%20Steward%20System.md) · [mountainshares-dao/mountainshares-dao.md](./mountainshares-dao/mountainshares-dao.md) · [the commons/Onboarding Checklists.md](./the%20commons/Onboarding%20Checklists.md)

**Public benefits recipients (SNAP, SSI, Medicaid):**
→ [the commons/BSA-Benefits-Sensitive Accounts.md](./the%20commons/BSA-Benefits%E2%80%91Sensitive%20Accounts%20.md) · [mountainshares-dao/MountainShares Phase 1: Economic Safety Specification.md](./mountainshares-dao/MountainShares%20Phase%201%3A%20Economic%20Safety%20Specification.md)

**Funders and institutional partners:**
→ [mountainshares-dao/MountainShares Funder Overview.md](./mountainshares-dao/MountainShares%20Funder%20Overview%20.md) · [docs/Partner Brief.md](./docs/Partner%20Brief.md) · [thesis/00-overview.md](./thesis/00-overview.md) · [docs/kidd_technical_services_detailed_timesheet_2025-2026.md](./docs/kidd_technical_services_detailed_timesheet_2025-2026.md)

**Government agencies, elected officials, and comprehensive planners:**
→ [the commons/Government Commons Node & Ms. Jarvis Partnership Overview.md](./the%20commons/Government%20Commons%20Node%20%26%20Ms.%20Jarvis%20Partnership%20Overview.md) · [discipline/case_studies/Absentee Ownership Concentration in Fayette County, West Virginia.md](./discipline/case_studies/Absentee%20Ownership%20Concentration%20in%20Fayette%20County%2C%20West%20Virginia.md) · [mountainshares-dao/MountainShares DAO Governance Charter.md](./mountainshares-dao/MountainShares%20DAO%20Governance%20Charter.md)

**Building infrastructure and economic development partners:**
→ [Definitive Service Inventory.md](./Definitive%20Service%20Inventory.md) · [discipline/case_studies/Absentee Ownership Concentration in Fayette County, West Virginia.md](./discipline/case_studies/Absentee%20Ownership%20Concentration%20in%20Fayette%20County%2C%20West%20Virginia.md) · [thesis/06-geodb-spatial-body.md](./thesis/06-geodb-spatial-body.md) · [mountainshares-dao/MountainShares Funder Overview.md](./mountainshares-dao/MountainShares%20Funder%20Overview%20.md)

**University and research partners:**
→ [the commons/University Commons Node Partnership Overview.md](./the%20commons/University%20Commons%20Node%20Partnership%20Overview.md) · [thesis/01-researcher-position.md](./thesis/01-researcher-position.md) · [discipline/Comparative Frameworks in Geography and Commons.md](./discipline/Comparative%20Frameworks%20in%20Geography%20and%20Commons.md)

**AI safety researchers:**
→ [theory/Off Switch Design.md](./theory/Off%20Switch%20Design.md) · [thesis/10-woah-weighted-optimization-hierarchy.md](./thesis/10-woah-weighted-optimization-hierarchy.md) · [thesis/16-blood-brain-barrier-and-safeguards.md](./thesis/16-blood-brain-barrier-and-safeguards.md) · [thesis/29-psychological-safeguards-and-pia.md](./thesis/29-psychological-safeguards-and-pia.md) · [discipline/case_studies/Prefrontal Alignment Episode.md](./discipline/case_studies/Prefrontal%20Alignment%20Episode.md)

**Lawyers, regulators, and policy researchers:**
→ [mountainshares-dao/Terms and Conditions.md](./mountainshares-dao/Terms%20and%20Conditions.md) · [the commons/The Commons – Terms of Use.md](./the%20commons/The%20Commons%20%E2%80%93%20Terms%20of%20Use.md) · [security/SOURCE_ACCESS.md](./security/SOURCE_ACCESS.md) · [mountainshares-dao/Audit and Risk Management Plan.md](./mountainshares-dao/Audit%20and%20Risk%20Management%20Plan.md)

**Developers and technical integrators:**
→ [docs/API-OVERVIEW.md](./docs/API-OVERVIEW.md) · [api_specs/openapi.json.md](./api_specs/openapi.json.md) · [Definitive Service Inventory.md](./Definitive%20Service%20Inventory.md) · [thesis/19-container-architecture-and-routing.md](./thesis/19-container-architecture-and-routing.md)

**Completely new readers:**
→ [theory/What-is-Quantarithmia.pdf](./theory/What-is-Quantarithmia.pdf) · [discipline/what-is-polymatmatic-geography.md](./discipline/what-is-polymatmatic-geography.md) · [thesis/00-thesis-overview.md](./thesis/00-thesis-overview.md)

---

## Three Questions Being Tested

This system is a live research project. The questions under active investigation are:

1. **Trust and clarity** — Do residents, partners, and auditors find Ms. ALLI more understandable and trustworthy than black-box AI or opaque government process?
2. **Seeing extraction** — Can the system make hidden patterns of absentee ownership and resource extraction visible on the map, so local people can act on them?
3. **Stronger local safety nets** — Does MountainShares keep more value circulating in the community and make people feel safer, without becoming an unregulated financial institution?

---

## About This Project

**Harmony for Hope, Inc.** is a West Virginia nonprofit headquartered in Mount Hope, Fayette County, West Virginia. It is the institutional home of Ms. ALLI, MountainShares DAO, and The Commons platform. **Kidd's Technical Services, Inc.** provides the technical development and infrastructure services.

**Founder and Principal Investigator:** Carrie Ann Kidd (Mamma Kidd) — Mount Hope, West Virginia
**Contact:** [kiddstechnical@gmail.com](mailto:kiddstechnical@gmail.com)

---

*This repository is a living document. Sections are published as they are completed.*
*© Carrie Ann Kidd / Harmony for Hope, Inc. See [LICENSE](./LICENSE) for terms.*
*Polymathmatic Geography, Quantarithmia, and the Ms. Jarvis system are original works authored by Carrie Ann Kidd.*
*Ms. ALLI is an original system designed and built by Carrie Ann Kidd.*
