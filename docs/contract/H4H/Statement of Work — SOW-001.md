# Statement of Work — SOW-001
## The Commons Platform and MountainShares DAO Development

**Issued Under:** Master Services Agreement between Harmony for Hope, Inc. and Kidd's Technical Services, effective July 6, 2025

---

## Header

| Field | Value |
|---|---|
| **SOW Number** | SOW-001 |
| **Effective Date** | March 18, 2025 |
| **Work Commenced** | March 23, 2025 |
| **Estimated Completion** | November 30, 2027 |
| **Client** | Harmony for Hope, Inc. ("H4H") |
| **Contractor** | Kidd's Technical Services ("KTS") |
| **SOW Status** | Addendum — memorializing work agreed March 18, 2025 and commenced March 23, 2025, predating the MSA executed July 6, 2025, which governs this SOW retroactively |

---

## Recitals

The parties reached agreement on the scope described in this SOW on or around March 18, 2025. KTS commenced work on March 23, 2025. The Master Services Agreement between H4H and KTS was subsequently executed on July 6, 2025 and governs this SOW in full. This document is now executed as a formal Statement of Work under that MSA to memorialize the agreed scope, the in-kind compensation structure, and the intellectual property designations applicable to all work performed under this engagement.

This SOW governs KTS's development of The Commons platform and the MountainShares DAO for H4H. ALLIS (the Artificial Learning & Location Intelligence System) is owned solely by KTS and is not a deliverable under this SOW. Where ALLIS capabilities are integrated into The Commons platform, that integration is a licensed use governed by MSA Section 3, not a transfer of ownership. MS.FCCAC.ALLIS and MS.MHHWT.ALLIS appear in this SOW exclusively as Commons platform features — geographic nodes integrated into the H4H application — and not as hardware deployment work orders, which are governed by separate Corridor Partner Agreements.

---

## Section 1 — Scope of Services

KTS shall design, architect, develop, and deliver the following for H4H as part of the MountainShares program and The Commons platform:

### 1.1 MountainShares Mutual Credit System

Development of the MountainShares mutual credit system as a Web3 product for H4H, including:

- Smart contract architecture and proof-of-concept (achieved July 4, 2025)
- Mutual credit ledger backend architecture
- Commons-based governance database schema
- DAO governance structure, voting mechanics, and treasury management framework
- Integration with geographic property data via the GBIM (Geographic Building Information Model)
- Rewards program mechanics and participation tracking infrastructure
- Audit logging for transparent, community-accountable resource allocation

### 1.2 The Commons Platform

Development of The Commons social media and community marketplace application operated by H4H as part of MountainShares, including:

- Full microservices architecture (Docker, FastAPI, Uvicorn)
- API gateway and unified endpoint architecture
- Authentication, authorization, and access control middleware
- Community participation features, member-facing interfaces, and governance tooling
- Integration of MS.FCCAC.ALLIS (Fayette County Community Arts Center) as a named geographic node within The Commons platform UI
- Integration of MS.MHHWT.ALLIS (Mount Hope Historic Walking Trail) as a named geographic node within The Commons platform UI
- Location-aware community features and MountainShares participation hooks at each node location
- Heritage and trail content delivery via The Commons interface at MS.MHHWT.ALLIS
- Cultural programming, event, and community resource features at MS.FCCAC.ALLIS

### 1.3 Ms. Jarvis Geospatial Intelligence Platform (Licensed Integration)

Integration of ALLIS/Ms. Jarvis capabilities into The Commons ecosystem under the H4H License granted in MSA Section 3, including:

- GBIM spatial data pipeline integration
- GeoDB custom geographic database schema and PostGIS spatial indexing
- ChromaDB vector database for LLM embedding optimization and semantic search
- PostgreSQL spatial query optimization
- Full system mesh integration (achieved December 25, 2025)

### 1.4 Infrastructure and Systems Operations

Ongoing infrastructure support as part of the development engagement, including:

- ETL process development for geospatial source integration
- Database migration scripts and data integrity testing
- Real-time geographic data synchronization
- Critical infrastructure recovery operations as required
- System monitoring, error logging, and performance infrastructure

---

## Section 2 — Deliverables and Acceptance Criteria

| # | Deliverable | Status | Acceptance Criteria |
|---|---|---|---|
| D-01 | MountainShares smart contract proof of concept | Completed July 4, 2025 | Smart contract system operational; mutual credit mechanics demonstrated |
| D-02 | Mutual credit ledger backend and governance schema | Completed | Backend architecture operational; commons governance schema documented |
| D-03 | Ms. Jarvis full system mesh integration | Completed December 25, 2025 | All microservices integrated; GBIM, GeoDB, ChromaDB, LLM layer operational |
| D-04 | The Commons platform — core architecture | In progress | Microservices deployment functional; API gateway, auth, and member interfaces operational |
| D-05 | MountainShares DAO governance and rewards platform | In progress | DAO voting mechanics live; rewards tracking and treasury management operational |
| D-06 | MS.MHHWT.ALLIS Commons integration | In progress | Mount Hope Historic Walking Trail node visible and functional within The Commons UI; participation hooks live |
| D-07 | MS.FCCAC.ALLIS Commons integration | In progress | FCCAC node visible and functional within The Commons UI; cultural programming and community resource features live |
| D-08 | System documentation | Ongoing | Architecture, schema, API, and deployment documentation current and accessible |

---

## Section 3 — Timeline

| Milestone | Date |
|---|---|
| Agreement reached | March 18, 2025 |
| Work commenced | March 23, 2025 |
| MSA executed (retroactively governs this SOW) | July 6, 2025 |
| Smart contract proof of concept (D-01) | July 4, 2025 |
| Full system mesh integration (D-03) | December 25, 2025 |
| SOW-001 formally executed | April 18, 2026 |
| The Commons platform — core architecture (D-04) | June 30, 2027 |
| MountainShares DAO governance and rewards platform (D-05) | August 31, 2027 |
| MS.MHHWT.ALLIS Commons integration (D-06) | September 30, 2027 |
| MS.FCCAC.ALLIS Commons integration (D-07) | October 31, 2027 |
| System documentation complete (D-08) | November 30, 2027 |
| **Estimated completion** | **November 30, 2027** |

*Milestones are estimates. Either party may propose adjustments in writing. Amendments require written consent of both parties per MSA Section 9.2.*

---

## Section 4 — Compensation

All work performed by KTS under this SOW constitutes an **in-kind donation** by Kidd's Technical Services to Harmony for Hope, Inc. KTS receives no monetary compensation under this SOW.

The fair market value of services contributed is documented in the Kidd's Technical Services Founder's Technical Investment Statement (March 13, 2026), on file with H4H, which records 5,308 hours at $150/hour through March 13, 2026, for a total documented in-kind contribution of $796,200. That document is incorporated by reference as supporting record of this SOW's compensation structure.

H4H may recognize this contribution on its financial statements as donated services under applicable GAAP guidance and may use it as documented in-kind match for grant applications, consistent with the accounting treatment described in the Investment Statement. Neither party should treat this as a tax-deductible charitable contribution of services under IRC §170.

---

## Section 5 — Work-for-Hire Designations

Consistent with MSA Section 2.2 and 2.3, the following deliverables under this SOW are designated **work-for-hire** and are owned by Harmony for Hope, Inc. upon delivery:

- D-01: MountainShares smart contract proof of concept
- D-02: Mutual credit ledger backend and commons governance schema
- D-05: MountainShares DAO governance and rewards platform
- D-06: MS.MHHWT.ALLIS Commons platform integration features
- D-07: MS.FCCAC.ALLIS Commons platform integration features
- Application-layer features and configurations specific to The Commons UI (D-04)

The following are **not** work-for-hire and remain the sole property of Kidd's Technical Services:

- ALLIS in its entirety, including all components, architecture, models, data pipelines, and derivative works (D-03 and all Ms. Jarvis integration work)
- Microservices deployment methodology, Docker configurations, and infrastructure tooling developed by KTS
- Any ALLIS improvements or extensions made in the course of this engagement

H4H's rights to ALLIS are exclusively those granted by the H4H License in MSA Section 3.

---

## Section 6 — Special Conditions

**6.1 Retroactive Scope**
This SOW memorializes an agreement reached on March 18, 2025 and work commenced March 23, 2025. The parties acknowledge that the MSA was not executed until July 6, 2025 and agree that the MSA governs this SOW and all work performed under it from March 23, 2025 forward.

**6.2 ALLIS Remains Separate**
Nothing in this SOW, and nothing in the history of work performed under it, transfers, assigns, encumbers, or modifies KTS's ownership of ALLIS. The MS. designations (MS.FCCAC.ALLIS, MS.MHHWT.ALLIS) identify ALLIS nodes operating under H4H's MountainShares Sponsorship Tier. They do not constitute H4H ownership of those nodes or of ALLIS.

**6.3 Web3 Product Designation**
The Commons platform and MountainShares mutual credit system are being developed as a Web3 product for H4H. The parties acknowledge this designation for purposes of program documentation, grant applications, and partner communications. The specific blockchain architecture, token mechanics, and smart contract stack are documented in KTS's technical records and are incorporated by reference.

**6.4 Node Integrations Are App Features**
MS.FCCAC.ALLIS and MS.MHHWT.ALLIS appear in this SOW as Commons platform features. Physical hardware deployment for those nodes, site access, and Corridor Partner governance are governed by separate Corridor Partner Community Governance Agreements between KTS and the respective partner organizations.

**6.5 Ongoing Nature**
This SOW governs a continuous development engagement through the estimated completion date of November 30, 2027. Deliverables marked "in progress" shall be completed on the timeline specified in Section 3. Either party may propose amendments to scope, timeline, or deliverables by written notice; amendments require written consent of both parties per MSA Section 9.2.

---

## Signatures

**Harmony for Hope, Inc.**

Signature: ___________________________________   Date: ___________

Printed Name: ___________________________________

Title: ___________________________________

---

**Kidd's Technical Services**

Signature: ___________________________________   Date: ___________

Printed Name: Carrie Kidd

Title: Owner / Operator

---

*This SOW is not effective until signed by authorized representatives of both parties. It is issued under and governed by the Master Services Agreement between Harmony for Hope, Inc. and Kidd's Technical Services, effective July 6, 2025. It is preceded by SOW-000, the initial project agreement effective March 18, 2025.*
