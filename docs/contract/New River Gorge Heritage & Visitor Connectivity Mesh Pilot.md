# New River Gorge Heritage & Visitor Connectivity Mesh Pilot
## Artificial Learning & Location Intelligence — MS.NPS.ALLIS
### A Two-Phase Pilot for Safety, Heritage, and Edge Intelligence

**Prepared by:** Carrie Kidd, GIS Specialist | M.A. in Leadership
**Technical Installation:** Aubrey Dickerson, Kidd's Technical Services
**Primary Contact:** kiddstechnical@gmail.com
**Date:** April 2026

---

## Project Overview

### What This Project Is

The New River Gorge Heritage & Visitor Connectivity Mesh Pilot — operating under the designation **MS.NPS.ALLIS** — is a small, careful experiment to add a quiet layer of free public connectivity, safety communications support, and heritage interpretation in one New River Gorge gateway community at a time. Initially envisioned for Thurmond, it is suitable for any interested Gorge community such as Hinton, Gauley Bridge, Mount Hope, or Prince, without changing how these places look and feel.

The pilot is structured in two distinct phases that can be evaluated and approved independently:

- **Phase 1 — Radios (Internet Bubble):** Backbone and endpoint radio infrastructure plus Starlink satellite backhaul, creating a free, locally owned internet layer for visitors, park staff, and municipal partners. This phase functions as a standalone public benefit — no edge AI, no data complexity, no interference with licensed radio systems.

- **Phase 2 — Prisms (Edge Intelligence / Ms. Allis):** Deployment of edge computing nodes running artificial learning and location intelligence locally. This phase activates the MS.NPS.ALLIS validation testbed, enabling heritage content delivery, location-aware visitor services, and real-world stress-testing of edge AI in a resource-constrained Appalachian environment.

This structure allows NPS, community partners, and the town of Thurmond to evaluate and commit to Phase 1 independently, with Phase 2 introduced only after Phase 1 has demonstrated value and earned trust.

### Why Start in a New River Gorge Town

Communities along and around New River Gorge National Park and Preserve — Thurmond, Hinton, Gauley Bridge, Prince, Mount Hope, and towns along the Midland Trail corridor — are among the most historically significant rail and river communities in the region. They are also among the most underserved when it comes to reliable connectivity.

The gorge is beautiful, steep, and remote. Visitors frequently arrive expecting to access park information and find no signal at the trailhead, the depot, or the riverfront overlook. That connectivity gap is a heritage interpretation gap. NPS and community partners have invested in preservation, signage, and interpretive programs across the Gorge — but much of that investment goes unreached when visitors cannot load a map, find a trail narrative, or access a walking-tour story on their device.

Proving a small, respectful connectivity layer in one town first creates a documented option that other interested New River Gorge communities could choose to adapt later, without assuming a corridor-wide rollout.

### What Will Actually Be Built

**Phase 1 hardware (per community):**

- Two higher-capacity backbone radios (Ubiquiti Rocket Prism 5AC Gen2) to create a private wireless spine along key sightlines
- Six smaller endpoint radios (MikroTik SXTsq 5 ac) to reach specific visitor-facing and safety-critical locations — trailheads, depots, visitor centers, park facilities, EMS staging points
- One Starlink Business satellite terminal, where needed, providing up to 400 Mbps of shared broadband delivered free across every node on the mesh
- Small enclosures, cabling, surge protection, and UPS units so the system continues operating through short power or network interruptions

**Phase 2 hardware (added after Phase 1 evaluation):**

- Edge computing nodes (prisms) co-located with or near Phase 1 radio infrastructure
- Local AI model hosting for Ms. Allis — location intelligence, heritage content delivery, visitor-facing decision support
- Content-addressed local data store for trail narratives, maps, points of interest, and safety protocols
- Validation instrumentation for academic and operational review

All equipment is chosen and sited to be as unobtrusive and reversible as possible — neutral colors, minimal size, mounted on existing structures or previously disturbed areas where allowed, and documented with photographs and drawings for historic-preservation review.

Because no fees are charged to users, the Phase 1 network operates as free public infrastructure — the same legal model as a library or park Wi-Fi — with no ISP licensing required.

---

## Executive Summary

The New River Gorge Heritage & Visitor Connectivity Mesh Pilot (MS.NPS.ALLIS) is a corridor-scale, small-footprint connectivity and intelligence initiative designed for Thurmond or another New River Gorge gateway community as a first deployment, with a clear path to extend the pattern across the wider Gorge region.

**Phase 1** uses discreet wireless nodes and limited satellite backhaul to keep visitors, park staff, and municipal partners connected when conventional cell coverage fails, while preserving the historic character and visual integrity of these communities. This phase does not replace or interfere with licensed radio systems such as WV SIRN or Motorola-managed networks, which remain the primary voice communications backbone for emergency responders. It functions as an internet data layer only.

**Phase 2** moves heritage interpretation, mapping, and location intelligence to the edge of the network. Trail content, historic narratives, maps, and visitor information are processed and served locally in real time, even in steep, forested terrain where cell connectivity is intermittent. This phase also serves as the primary validation environment for the Ms. Allis edge AI system — a real-world, resource-constrained Appalachian testbed for artificial learning running close to where people actually are.

NPS participation in both phases is structured as an in-kind contribution — site access, a designated point of contact, and network permission where appropriate — with no budget obligation or procurement requirement on the part of the park. The infrastructure is provided at no cost to NPS under the MS.NPS.ALLIS free tier. Future service tiers, if ever relevant, would be a separate conversation governed by MountainShares community agreements at that time.

---

## Context and Objectives

### Corridor Context

The New River Gorge region is anchored by a set of historic rail, coal, and river towns — Thurmond, Hinton, Mount Hope, Fayetteville, Oak Hill, Ansted, Smithers, Montgomery, Gauley Bridge, and others — that sit in and around New River Gorge National Park and Preserve. Many of these communities have small or declining populations but high symbolic and recreational importance as preserved railroad-era landscapes and gateway towns to the Gorge.

That same terrain — steep, heavily forested, deeply incised by the New and Gauley rivers — creates sharp elevation changes and narrow corridors that are beautiful but consistently challenging for cell coverage. Visitors arriving at gateway towns such as Thurmond find connectivity limited or absent. Heritage content, trail information, and visitor orientation materials that depend on external networks simply do not reach people when and where they are most needed.

The opportunity is not to overlay these places with visible technology — it is to add a quiet, locally owned connectivity and intelligence layer that makes their stories more accessible without changing what makes them worth visiting.

### Problem Statement

The specific problem this program addresses is the lack of locally owned, resilient connectivity and edge intelligence in New River Gorge gateway communities that:

- Serves visitors reliably, independent of which commercial carrier they use or whether backhaul to distant data centers is available
- Delivers heritage content, trail information, maps, and points of interest directly at the edge — close to where visitors actually are, including at park facilities, depots, trailheads, and riverfront sites where cell coverage is limited or absent
- Continues to function even when access to external networks is degraded, by storing and serving key content locally rather than depending on cloud infrastructure that the terrain and corridor conditions routinely interrupt
- Provides a real-world validation environment for edge AI that is observable, stress-testable, and grounded in genuine community need rather than laboratory conditions

### Project Objectives

1. **Reliable visitor and operational connectivity (Phase 1)**
   Provide locally owned, redundant internet connectivity for visitors, park staff, and municipal partners in defined coverage areas around an initial gateway community. This program does not replace or interfere with licensed radio systems such as WV SIRN or Motorola-managed networks, which remain the primary voice communications backbone for emergency responders.

2. **Local, edge-based heritage interpretation and location intelligence (Phase 2)**
   Deploy modest edge computing in gateway communities that can host heritage content, artificial learning models, and geospatial services locally — enabling visitors to access trail narratives, historic context, maps, and points of interest in real time without depending on external connectivity.

3. **Heritage-compatible infrastructure design (both phases)**
   Demonstrate that connectivity and intelligence infrastructure can be deployed across historic towns and cultural landscapes with minimal visual and physical impact, using discrete hardware, reversible mounts, neutral colors, and siting on existing structures or disturbed areas.

4. **Transferable regional model (both phases)**
   Use Thurmond as a testbed to develop a small, well-documented pattern that can be adapted to other Gorge communities — Mount Hope, Glen Jean, Hinton, Montgomery, Smithers, Fayetteville, Oak Hill — that share similar terrain, heritage, and connectivity challenges.

---

## Technical Design

### Physical Architecture — Phase 1: Radio Backbone

**Backbone radios — 2× Ubiquiti Rocket Prism 5AC Gen2**
High-performance 5 GHz basestation radios for point-to-point and point-to-multipoint links, supporting more than 450 Mbps throughput and 50 or more client devices when paired with appropriate antennas. Integrated GPS synchronization and advanced RF filtering help maintain performance where multiple radios are co-located on shared structures or ridge sites.

**Endpoint radios — 6× MikroTik SXTsq 5 ac**
Compact 5 GHz 802.11ac devices with integrated 16 dBi antennas and gigabit Ethernet, suitable as cost-effective clients or short point-to-point links to EMS vehicles, small structures, trailheads, depots, or utility poles. Weather-rated, low-power, and widely used in community mesh deployments.

**Satellite uplink — 1× Starlink Business terminal where needed**
Provides broadband backhaul with downlink speeds up to roughly 400 Mbps. This uplink is not required for the mesh to function locally but allows each participating community to exchange data with external systems when connectivity is available.

**Supporting infrastructure**
Outdoor PoE switches, weatherproof enclosures, surge protection, grounding, mounting hardware, shielded outdoor cabling, and small UPS units sized for the Gorge's climate and heritage setting.

### Physical Architecture — Phase 2: Edge Intelligence Nodes (Prisms)

Edge computing nodes co-located with Phase 1 infrastructure, running:

- Ms. Allis artificial learning models locally — no cloud dependency for core function
- GeoBelief location intelligence services — context-aware content delivery based on visitor position, terrain, and nearby heritage assets
- Content-addressed local data store — trail narratives, maps, walking-tour stories, safety protocols, cached and served locally
- Validation instrumentation — uptime, coverage, model performance, usage patterns, stress-test logging

Phase 2 nodes are sized for the Gorge's constraints: low power, weather-rated, reversible mounts, documented for historic-preservation review.

### Logical Architecture — Three Layers

**Connectivity layer (Phase 1 — mesh and backhaul)**
Rocket Prism radios form the core 5 GHz backbone in each participating town. SXTsq devices extend coverage to specific visitor-facing locations. A Starlink terminal provides backhaul to external networks, but the mesh maintains local connectivity and core visitor services even when that uplink is degraded or offline.

**Content layer (Phase 2 — local-first heritage and services)**
Core assets — trail and heritage narratives, maps, points of interest, visitor orientation materials — are stored and cached on edge nodes using a content-addressed data store. A visitor at the Thurmond Depot, on a trailhead, or at a riverfront overlook receives the same rich, locally cached content whether or not their carrier has signal.

**Intelligence layer (Phase 2 — artificial learning and location intelligence)**
Ms. Allis components run on or near edge nodes, surfacing relevant heritage content based on a visitor's location, suggesting optimal routes given known conditions, and highlighting points of interest and hazards nearby. These services function primarily on local hardware, with cloud augmentation only as a secondary layer.

### Design Principles

**Heritage-sensitive deployment**
Radios and enclosures are mounted to minimize visual intrusion and avoid damage to historic fabric, prioritizing reversible mounts, neutral colors, and consolidation with existing utility or structural elements where allowed. Every installation is documented — photos, diagrams, descriptions — for review by historic-preservation staff and NPS teams.

**Local resilience, cloud optional**
Core functions — visitor connectivity, cached heritage content, maps, trail information, and key location-intelligence services — are designed to continue working in each participating community even when the Starlink uplink or broader internet is unavailable. Cloud and centralized data centers are treated as enhancement layers, not hard dependencies.

**Small, extensible footprint**
Initial deployments use a small number of nodes focused on specific coverage goals. The architecture allows additional nodes or Phase 2 services to be added later without major redesign.

---

## Example Deployment Scenario — Thurmond as First Testbed

**Phase 1 — Radio deployment:**

- Place one Rocket Prism radio and a Starlink terminal at a non-intrusive, high-elevation location with power and a clear view over the town and gorge — forming the invisible backbone of the connectivity layer
- Place a second Rocket Prism radio on or near a structure closer to town, creating a high-capacity link along the river corridor
- Use SXTsq devices to extend connectivity to:
  - The Thurmond Depot visitor center, replacing the carrier-dependent hotspot with locally owned connectivity available to any visitor device
  - A trailhead or riverfront access point serving the highest visitor foot traffic
  - One or two additional locations identified with NPS interpretation staff and local partners

**Phase 2 — Prism deployment (following Phase 1 evaluation):**

- Co-locate edge nodes with existing Phase 1 infrastructure — no new structural footprint required
- Activate Ms. Allis locally: heritage content delivery, location intelligence, trail-aware visitor services
- Begin validation period: collect operational metrics, run stress tests with changing datasets, gather qualitative feedback from EMS, park staff, and visitors
- Prepare academic and operational findings for corridor-wide review

---

## Governance, Data, and MountainShares Framework

### Ownership and Operational Roles

**Infrastructure ownership**
In each participating New River Gorge community, physical assets — radios, satellite terminals, edge nodes, enclosures, mounts, cabling, UPS units — are owned by the municipality, a designated public safety agency, or an agreed public-benefit partner, with all assets and sites formally documented. Sites, easements, and mounting rights are governed by written agreements with landowners or agencies.

**Operational responsibility**
A primary operating entity in each town manages day-to-day operation, configuration, monitoring, and first-line troubleshooting. EMS, fire, law enforcement, and park staff remain operational users, involved in defining coverage priorities but not expected to administer nodes directly.

**Lifecycle management**
Hardware and software lifecycles — replacement schedules, firmware and model updates, security patches — are documented in simple runbooks with clear role assignments. A lightweight regional working group can share lessons learned without centralizing control of local assets.

### MountainShares Community Agreement

Participation in MS.NPS.ALLIS at the free tier requires signing the MountainShares community governance agreement, available in the MountainShares DAO section of the project repository. This is not a financial commitment — it is a data stewardship and community governance commitment. It defines:

- How locally generated data is owned, governed, and protected
- Who may access operational and heritage data, and under what conditions
- How communities federate only what is necessary across the region
- The terms under which a community could, in the future, choose to move to an expanded service tier — a conversation that would happen at that time, not today

NPS participation is framed as an in-kind contribution. The park is not purchasing a service. If, at a future date, NPS or any participating community chooses to move beyond the free tier to a front-facing `nps.allis` expanded service, that would be a separate commercial conversation governed by the MountainShares agreements already in place. That conversation is not on the table today.

### Data Governance and Privacy

**Data categories:**
- Operational network data: status, throughput, errors, uptime
- Location and incident context: positions where appropriate, incident markers, map interactions
- Content and reference data: maps, trail and heritage content, protocols, playbooks

**Local-first, minimized collection**
Only data needed to deliver visitor connectivity, safety support, and heritage services is collected. Location data for responders is limited to operational contexts, not continuous tracking outside mission needs.

**Access control and protection**
Access to detailed operational and location data is restricted to authorized roles in the relevant jurisdiction, with authentication and audit logging. When data must leave the local environment — for regional analysis, training, or research — it is de-identified or aggregated wherever possible.

**Retention and transparency**
Retention periods are defined per data category, with automatic deletion where feasible. Agencies and, where appropriate, the public receive clear explanations of what is collected, how it is used, and how privacy is protected.

### Decentralization and Reduced Dependence on Data Centers

**Edge-first processing**
Ms. Allis models and location-intelligence services run primarily on local edge nodes, executing core analytics in place rather than routing every query over backhaul links — saving bandwidth, reducing latency, and keeping visitor-facing content available whether or not the Starlink uplink is active.

**Decentralized data architecture**
Local EMS, visitor, and heritage data in each community is treated as a domain resource, owned and governed by the agencies and communities that produce and use it. Additional New River Gorge communities can operate their own nodes and data products, federating only what is necessary across the region.

**Resilience to outages and policy change**
The system does not depend on constant access to a single cloud or data-center provider. Real-time safety, visitor connectivity, and heritage content delivery in each New River Gorge community do not fail if external systems are unavailable.

---

## Ethical and Regulatory Considerations

**Regulatory alignment**
Phase 1 operates as an internet data layer only. It does not carry licensed radio transmissions and does not require WV SIRN or Motorola permissions. Voice radio communications for EMS and SAR remain entirely on existing licensed infrastructure. Any future integration with 911 or PSAPs follows existing federal and state guidance.

**Ethical use of artificial learning and location intelligence**
Ms. Allis models focus on decision support — suggested routes, hazard highlighting, contextual heritage content for visitors — not automated decision-making about people or enforcement actions. Regular review with local stakeholders, including EMS, NPS, community representatives, and academic partners, ensures that models can be corrected, retrained, or retired, and that community values are reflected in how the tools are used.

---

## Heritage and NPS Alignment

### Historic Context

Thurmond is a preserved railroad-era townscape within New River Gorge National Park and Preserve, with the restored Thurmond Depot serving as a visitor center and more than twenty park-owned historic structures. Similar rail and coal landscapes extend into other Gorge communities and gateways — Fayetteville, Hinton, Mount Hope, Oak Hill, and Ansted.

NPS has invested in preservation work and interpretation training across the park, emphasizing retention of historic materials and character in buildings, rail corridors, and cultural landscapes. New infrastructure in Thurmond and other Gorge historic areas must support safety, enable reuse, and respect the visual and material integrity of remaining resources.

### Alignment with NPS Telecommunications and Preservation Guidance

NPS telecommunications planning emphasizes enhancing coverage while minimizing impacts on cultural landscapes, historic viewsheds, and historic districts. Section 106 guidance indicates that major towers inside historic districts are generally disfavored; small nodes, antennas on existing infrastructure, and carefully sited low-profile equipment may be acceptable; ground disturbance should be minimized and focused on existing corridors and disturbed areas.

The MS.NPS.ALLIS program follows these principles by relying on small, distributed radios and edge nodes, minimal new ground disturbance, and siting on or near existing infrastructure wherever feasible.

### Siting and Visual Impact Principles

**Use existing structures and corridors**
Candidate locations include existing utility poles, non-contributing or replacement structures, and discrete areas near developed sites — depots, service buildings, non-historic support structures — subject to appropriate approvals.

**Minimize visibility**
Equipment size and color are chosen to reduce contrast with existing materials and vegetation in each town. Key viewpoints and the ability of historic properties to convey significance are considered.

**Reversibility and documentation**
Installations on or near historic fabric are reversible where feasible. Each site is documented — maps, photographs, narratives — before and after installation, and this documentation is shared with NPS and state historic-preservation offices as appropriate.

### Heritage Interpretation and Community Value

The same edge infrastructure that supports safety and visitor connectivity can cache and deliver curated historic and interpretive content — Mount Hope's walking-trail stories, Thurmond rail-era narratives, Hinton and Alderson riverfront histories — to visitors' devices or future XR tools, even when external networks are down. This ensures that preservation investments across the Gorge are matched by high-quality, accessible interpretation that works in the low-connectivity conditions visitors most frequently encounter in the park.

---

## Implementation Plan

### Phase 0 — Engagement, Siting, and Design (4–8 weeks)

Initial meetings with municipal leaders, NPS, EMS and SAR teams, and community stakeholders in the selected gateway community to confirm priorities and define a realistic first coverage area. Site walks and RF assessments identify candidate locations and constraints. A draft siting plan, visual simulations, and preservation documentation are prepared for NPS, SHPO, and local review, alongside a refined technical design and updated budget.

This phase includes execution of MountainShares community governance agreements with all participating partners before any hardware procurement begins.

### Phase 1 — Radio Installation and Commissioning (approximately 1–2 weeks on-site)

- Procurement of Phase 1 hardware according to the approved bill of materials
- Physical installation of backbone radios, endpoint radios, enclosures, power, and Starlink terminal, following heritage-sensitive siting principles
- Configuration, alignment, and integration with local EMS and SAR, NPS, and municipal workflows
- Baseline testing, documentation, and handoff to the operating entity in that town
- **Deliverable:** A functioning free internet layer across defined coverage areas in the first community, at no cost to NPS or the town

### Phase 1 Evaluation Period (3–6 months)

Live operation of the internet layer during real-world visitor seasons, EMS workflows, and day-to-day park operations. Collection of baseline metrics — uptime, coverage, usage, qualitative feedback from EMS, park staff, and visitors. This period determines whether Phase 2 is appropriate and desired by the community.

### Phase 2 — Edge Intelligence Deployment (following Phase 1 evaluation)

- Procurement and co-location of edge computing nodes (prisms) with existing Phase 1 infrastructure
- Activation of Ms. Allis locally: heritage content delivery, location intelligence, visitor-facing decision support
- Begin formal validation period: operational metrics, multipack validation with changing datasets, model robustness testing, academic review
- Preparation of findings for corridor-wide review and potential replication in additional New River Gorge communities

### Phase 3 — Review and Next-Site Decisions

Joint evaluation workshop with local stakeholders — government, EMS and SAR, NPS, community representatives, and any interested regional partners — to review results and lessons learned. The group then decides whether to maintain the initial deployment as-is, expand coverage modestly within the first town, explore a similarly scoped second deployment in one additional New River Gorge community, or retire or repurpose components if the approach is not a good fit.

---

## Budget Summary

Costs are framed as a per-community starter kit, using Thurmond's design as the reference point.

| Category | Estimated Cost |
|---|---|
| Backbone radios (2× Ubiquiti Rocket Prism 5AC Gen2) | Included in Phase 1 |
| Endpoint radios (6× MikroTik SXTsq 5 ac) | Included in Phase 1 |
| Starlink Business hardware + first year of service | Included in Phase 1 |
| Enclosures, mounts, cabling, surge protection, UPS | Included in Phase 1 |
| Installation labor (Kidd's Technical Services) | Included in Phase 1 |
| Preliminary engineering and siting review | Included in Phase 1 |
| **Phase 1 subtotal (pre-contingency)** | **~$12,955** |
| **Phase 1 total (with 10% contingency)** | **~$14,250** |
| Starlink Business monthly subscription (recurring) | ~$250/month |
| Phase 2 edge nodes (prisms) — scoped separately | TBD after Phase 1 evaluation |

NPS has no budget obligation or procurement requirement under either phase. All infrastructure is provided at no cost to the park under the MS.NPS.ALLIS free tier. Any future service tier discussion, if ever relevant, occurs at that time and is governed by MountainShares agreements already in place.

---

## About MS.NPS.ALLIS and the MountainShares Framework

MS.NPS.ALLIS is the National Park Service node of the MountainShares ALLIS (Artificial Learning & Location Intelligence System) network. It is designed as a free-tier, community-governed service. The broader MountainShares framework — including governance agreements, DAO structure, and community credit instruments — is documented in the project repository.

Participation in MS.NPS.ALLIS at the free tier requires signing the MountainShares community agreement as a governance and data stewardship commitment, not a financial one. This ensures that all participating communities — NPS, Thurmond, and future Gorge partners — share consistent principles for data ownership, local resilience, and community benefit.

The goal is a corridor-wide, locally owned connectivity and heritage interpretation mesh that New River Gorge communities can extend, replicate, or retire on their own timelines — delivered at the edge, close to where visitors actually are, and without losing what makes these places worth saving in the first place.

---

*Prepared by Carrie Kidd, Kidd's Technical Services | kiddstechnical@gmail.com*
*Technical installation: Aubrey Dickerson, Kidd's Technical Services*
*For questions about the MountainShares governance framework, see the project repository under mountainshares-dao.*
````
