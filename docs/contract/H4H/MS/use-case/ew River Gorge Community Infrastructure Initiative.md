# New River Gorge Community Infrastructure Initiative
## Use Case Report — Harmony for Hope, Inc. | Kidd's Technical Services
**Document Status:** Working Draft — June 2026  
**Prepared by:** Carrie Kidd, Executive Director, Harmony for Hope, Inc.  
**Contact:** ckidd@harmonyforhopewv.org  
**Repository:** [msjarvis-public-docs](https://github.com/H4HWV2011/msjarvis-public-docs)

---

## Executive Summary

The New River Gorge Community Infrastructure Initiative is a place-based, community-governed development program operating along the New River Gorge corridor in Fayette and Mercer Counties, West Virginia. The initiative integrates three interdependent programmatic layers — land stewardship, broadband and heritage connectivity, and a regional capital stack — to establish a replicable pattern of community-owned infrastructure for New River Gorge gateway towns. Pilot deployment is anchored in Mount Hope and Thurmond, with a corridor-scale expansion horizon of 53 miles and a 12-month collaboration framework currently under development with NRG Towns.

The initiative is convened by Harmony for Hope, Inc., a 501(c)(3) cultural production nonprofit operating at 704 and 708 Main Street, Mount Hope, West Virginia — the site of the Fayette County Community Arts Center (FCCAC) — with technical services provided by Kidd's Technical Services. Harmony for Hope's role is that of cultural anchor and organizational convener; community development functions are carried through purpose-built subsidiary and partner structures described in Section 2. Active institutional support has been secured from the New River Gorge National Park and Preserve (NRGNPS), WV Community Development Hub, and the City of Mount Hope.

The core project statement is as follows:

> *Harmony for Hope is building community-governed heritage and broadband infrastructure for New River Gorge gateway towns, starting with Mount Hope and Thurmond, by combining a community land trust for key historic district buildings, a free visitor-focused mesh broadband pilot, and a regional development fund stack (Beckley Area Foundation, Bank of Richmond CTFI, MIT/Truist Inspire Awards) to prove a pattern that other corridor towns can adopt.*

---

## 1. Problem Statement

### 1.1 Historic Fabric Vulnerability

The gateway communities of the New River Gorge National Park and Preserve face a well-documented challenge common to post-industrial Appalachian towns: historic main street buildings are held by a fragmented mix of private investors, absentee owners, and undercapitalized local stakeholders. In Mount Hope, key properties along the commercial corridor — including multiple historic district buildings, entertainment venues, and adjacent shell structures — are currently changing hands. Without a coordinating ownership or stewardship structure, individual investor decisions — however well-intentioned — may expose adjacent historic fabric to architectural compromise, depressing the investment value of neighboring properties and undermining corridor-level preservation goals.

Active correspondence with community partners engaged in the Mount Hope historic district confirms that current private investment interest in the corridor is substantial, but that investors themselves recognize the structural vulnerability: the absence of a coordinating stewardship mechanism means that one incompatible renovation or prolonged vacancy can compromise the return on otherwise sound investments. The problem is therefore not a lack of private capital interest; it is the absence of a governance and stewardship structure that aligns individual investments with corridor-wide preservation and community economic outcomes.

### 1.2 Connectivity and Heritage Interpretation Gap

Visitor and resident connectivity across New River Gorge gateway communities remains inconsistent and commercially fragile. The Thurmond Depot — one of the most visited heritage sites in the park — has no reliable broadband for visitor orientation, interpretive programming, or operational support. The Mount Hope Historic Walking Trail lacks digital wayfinding infrastructure. Commercial internet outages in small gateway towns are frequent enough that no heritage or safety service dependent on a single commercial ISP can be considered reliably operational.

At the same time, heritage content — oral histories, architectural documentation, trail narratives, local maps — exists in scattered formats and is not accessible at the physical locations where visitors and residents would most benefit from it. The absence of a locally hosted, resilient connectivity layer means that even well-documented heritage assets are not discoverable in the field.

### 1.3 Structural Gap in Community Ownership

Existing grant and financing instruments for rural Appalachian communities are not designed to address the intersection of physical asset stewardship, broadband infrastructure, and heritage content delivery within a single community-governed structure. Individual grants fund discrete projects; no coordinated mechanism exists for a gateway community to simultaneously protect its built environment, deliver free public connectivity, and document its own story within a governance framework that keeps those functions under local control over time.

---

## 2. Proposed Initiative Structure

The New River Gorge Community Infrastructure Initiative addresses all three problem dimensions through three programmatic layers, each with distinct governance, financing, and operational characteristics. These layers are not sequential; they are designed to develop in parallel and to reinforce one another.

### 2.1 Layer One: Land and Building Stewardship

**Mechanism:** Harmony for Hope Community Land Trust (subsidiary program of Harmony for Hope, Inc.)

The Harmony for Hope Community Land Trust (H4H CLT) will operate initially as a subsidiary program of Harmony for Hope, Inc., governed by a dedicated board of directors with representation from Fayette and Mercer Counties. Subject to board determination, the H4H CLT may incorporate as an independent 501(c)(3) as organizational capacity and asset portfolio warrant. This structure allows the CLT to begin operations under H4H's existing tax-exempt status while developing the governance track record and capitalization required for independent incorporation.

The H4H CLT would acquire and steward key historic district properties in Mount Hope and, pending feasibility analysis, in Mercer County — creating a nonprofit ownership layer that separates land value from building value, protects affordability and architectural integrity over time, and provides a governance vehicle for multi-county property management. Under this framework, the FCCAC building (704/708 Main Street), the proposed restaurant incubator, and potentially the geospatial company space identified for 708 could be held in a structure that prevents speculative resale while enabling community-serving uses to continue indefinitely.

Governance of the H4H CLT would include representation from both Fayette and Mercer Counties. Active outreach is underway to Greg Puckett (Mercer County Community Connections) as a prospective board member. Additional board recruitment is focused on stakeholders with demonstrated investment in the historic district and alignment with the CLT's preservation and community economic mission.

The Bank of Richmond CTFI Cohort application (due July 7, 2026) is the primary near-term financing vehicle for this layer. A Letter of Support from aligned stakeholders in the district would materially strengthen this application.

**Decision dependency:** The CLT question requires a board-level decision before the Bank of Richmond application deadline. This is the critical path item for Layer One.

### 2.2 Layer Two: Heritage and Visitor Connectivity Mesh Pilot

**Program designation:** MS.NPS.ALLIS — New River Gorge Heritage & Visitor Connectivity Mesh Pilot  
**Operating under:** MountainShares / Kidd's Technical Services  
**Sponsor:** Harmony for Hope, Inc.

The connectivity layer deploys a small-footprint, heritage-sensitive mesh network in Mount Hope and Thurmond to provide free public broadband for residents, visitors, and partner institutions. The network is not a commercial ISP service; it is a community-governed infrastructure layer designed specifically for heritage interpretation, visitor orientation, and operational resilience in a national park gateway context.

**Architecture (Mount Hope node: MS.MHHWT.ALLIS)**

- Starlink satellite uplink mounted at or near the FCCAC, 704/708 Main Street
- Local mesh distribution serving the Mount Hope Historic Walking Trail kiosk and adjacent Main Street corridor
- Edge-cached content: trail maps, walking tour narratives, community announcements, emergency information
- Resilient to commercial internet outages — cached content remains accessible when upstream connectivity drops

**Architecture (Thurmond node: MS.THURMOND.ALLIS — example configuration)**

- Ubiquiti Rocket Prism 5AC Gen2 backbone radio at Thurmond Depot
- Second endpoint at the Main Street Post Office building
- Six Silvanet mesh endpoints distributed through visitor circulation areas
- Reversible mounts, neutral finishes, and no penetration of historic fabric
- All installations subject to heritage review and NPS coordination prior to deployment

The network is provided to users at no cost. No subscriber data is collected. Content is locally hosted and locally governed. The MountainShares Commons platform serves as the governance and content management layer, with Harmony for Hope holding the organizational relationship to partner institutions including NRGNPS, the City of Mount Hope, and Thurmond.

NRGNPS support for the broadband pilot has been confirmed; letters of support from Thurmond, Mount Hope, and Starry Eyes Media are in hand. Dr. Srivastava has indicated support. The pilot is targeted for launch in Mount Hope and Thurmond by Spring 2027, contingent on successful grant outcomes in the June–August 2026 application window.

### 2.3 Layer Three: Regional Capital and Governance Stack

The initiative is financed through a layered grant strategy coordinated by WV Community Development Hub, which identified the Bank of Richmond and MIT/Truist pathways and is actively engaged in application development. The capital stack is structured to provide overlapping coverage across infrastructure, operations, and institutional capacity.

| Funding Source | Program | Deadline | Primary Layer Funded |
|---|---|---|---|
| Beckley Area Foundation | Community Grant (x2) | June 30, 2026 | Connectivity / Operations |
| Bank of Richmond | 2027 CTFI Cohort | July 7, 2026 | Land Stewardship (H4H CLT) |
| MIT / Truist Inspire Awards | Year 4 | August 7, 2026 | Technology / Heritage Layer |
| Marshall University | Use Case Partnership | September 2026 | Research / Field Lab |

The Beckley Area Foundation grants are assessed as high-probability outcomes; a determination is expected by end of July 2026. The MIT/Truist and Bank of Richmond applications are designed as complementary instruments — the former funding the technology and heritage content layer, the latter the community land trust structure.

Marshall University President Brad Smith has been briefed on the initiative and has requested ongoing updates. The September 2026 deliverable to Marshall is a use case package demonstrating a live or near-live pilot deployment in Mount Hope, suitable for academic partnership, student field engagement, and potential Wing 2 Wing Foundation alignment. The Wing 2 Wing Foundation's documented focus on economic development in overlooked zip codes and entrepreneurship in Appalachian communities aligns directly with the corridor model this initiative is designed to prove.

---

## 3. Replication Pattern

The initiative is explicitly designed as a proof-of-pattern, not a corridor-wide build-out. Each component — CLT structure, mesh node, governance agreement — is documented in the public repository at [H4HWV2011/msjarvis-public-docs](https://github.com/H4HWV2011/msjarvis-public-docs) in formats suitable for replication by any New River Gorge gateway community operating under comparable conditions.

The NRG Towns initiative has indicated interest in a 12-month collaboration to expand the technology and governance model along all 53 miles of the corridor. This horizon is treated as a planning assumption, not a committed deployment schedule. Replication in any additional community proceeds only after: (1) local stakeholder engagement and siting review; (2) heritage review for all proposed installation points; (3) execution of a Corridor Partner Community Governance Agreement under the MS.__.ALLIS program framework; and (4) independent funding secured for that community's node.

The pattern that Mount Hope and Thurmond are proving is:

> One town at a time — protect the buildings, run your own free broadband, tell your own stories, own the structure that holds all three together. Document what works. Share it with the next town.

---

## 4. Key Stakeholders and Roles

| Stakeholder | Role | Status |
|---|---|---|
| Harmony for Hope, Inc. | Cultural production anchor; organizational convener; FCCAC site; program sponsor | Active |
| Harmony for Hope Community Land Trust | Subsidiary land stewardship entity under H4H; property acquisition and governance | Formation in progress |
| Kidd's Technical Services | Technical installation and system operations (MS.NPS.ALLIS) | Active |
| MountainShares Commons | Governance and content management platform layer | Active |
| NRGNPS | In-kind partner; heritage review; NPS coordination | Letter of Support secured |
| City of Mount Hope | Municipal partner; site access; community anchor | Supportive |
| Thurmond | Gateway community partner; MS.THURMOND.ALLIS site | Letter of Support secured |
| WV Community Development Hub | Grant navigation; application support; BAF and MIT/Truist referrals | Actively engaged |
| Greg Puckett / Mercer County Community Connections | Prospective H4H CLT board member; Mercer County anchor | Networked |
| Brad Smith, Marshall University | Institutional partner; use case audience; potential Wing 2 Wing alignment | Primed; awaiting use case package |
| David Sibray / West Virginia Explorer | Community connector; historic district context; real estate network | Engaged |
| Historic district private investors | Prospective H4H CLT board members; Letter of Support opportunity | In conversation |
| Anna Ziegler | Land law consultation (referred; availability uncertain) | Pending |
| Patricia Shepard Kelly | Prospective restaurant incubator partner for 708 | Outreach pending |
| Starry Eyes Media | Community media partner | Letter of Support secured |

---

## 5. Near-Term Critical Path

The following decisions and deliverables are sequentially dependent and must be resolved in order for the initiative to move forward on the current timeline.

1. **H4H CLT formation decision (by ~July 5, 2026):** Board-level determination on whether to pursue the CLT subsidiary route for the Bank of Richmond application. This unlocks board recruitment, the Letter of Support request from historic district stakeholders, and the Bank of Richmond narrative framework.
2. **BAF submission (June 30, 2026):** Two grants to Beckley Area Foundation — broadband and operations focused. Determination expected by end of July.
3. **Bank of Richmond CTFI submission (July 7, 2026):** Contingent on H4H CLT decision. Letter of Support from aligned investors strengthens application.
4. **MIT/Truist Inspire Awards submission (August 7, 2026):** Technology and heritage layer. Package development in progress.
5. **Marshall University use case package (September 2026):** Live or near-live pilot documentation, field lab framing, Wing 2 Wing alignment brief.

---

## 6. Repository and Supporting Documentation

All technical proposals, governance agreements, and grant application frameworks are maintained in the public repository at [H4HWV2011/msjarvis-public-docs](https://github.com/H4HWV2011/msjarvis-public-docs/tree/main/docs/contract/H4H/MS/NPS). Key documents include:

- [Greater Mount Hope Community Fund 2026](https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/contract/H4H/MS/NPS/GREATER%20MOUNT%20HOPE%20COMMUNITY%20FUND%202026.md)
- [New River Highlands Development Fund](https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/contract/H4H/MS/NPS/NEW%20RIVER%20HIGHLANDS%20DEVELOPMENT%20FUND.md)
- [Truist Foundation Inspire Awards — Year 4](https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/contract/H4H/MS/NPS/TRUIST%20FOUNDATION%20INSPIRE%20AWARDS%20%E2%80%94%20YEAR%204.md)
- [Mount Hope Heritage Infrastructure Workflow](https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/contract/H4H/MS/NPS/Mount%20Hope%20Heritage%20Infrastructure%20Workflow.md)
- [MS.__.ALLIS Corridor Partner Community Governance Agreement](https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/contract/H4H/MS/NPS/MS.___.ALLIS%20Corridor%20Partner%20Community%20Governance%20Agreement.md)
- [New River Gorge Heritage & Visitor Connectivity Mesh Pilot](https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/contract/H4H/MS/NPS/New%20River%20Gorge%20Heritage%20%26%20Visitor%20Connectivity%20Mesh%20Pilotc.md)

---

*This document is a working use case report prepared for internal coordination and institutional partnership development. It does not constitute a binding commitment between any parties. Binding instruments are established only through executed governance agreements and executed grant award letters. Document maintained at H4HWV2011/msjarvis-public-docs.*
