# New River Gorge Heritage & Visitor Connectivity Mesh Pilot
## Artificial Learning & Location Intelligence — MS.NPS.ALLIS

**Prepared by:** Carrie Kidd, GIS Specialist | M.A. in Leadership
**Technical Installation:** Aubrey Dickerson, Kidd's Technical Services
**Primary Contact:** kiddstechnical@gmail.com
**Date:** April 2026

---

## Project Overview

### What This Project Is

The New River Gorge Heritage & Visitor Connectivity Mesh Pilot — operating under the designation **MS.NPS.ALLIS** — is a small, careful experiment to add a quiet layer of free public connectivity, safety communications support, and heritage interpretation in one New River Gorge gateway community at a time. The corridor includes communities such as Hinton, Gauley Bridge, Mount Hope, Prince, and others — any of which could serve as a first participating town — without changing how these places look and feel.

The pilot brings together a small number of discreet wireless devices, a single satellite link, and locally hosted intelligence tools so that visitors can access maps, trail information, and heritage stories anywhere in a participating town even when carrier signal is unavailable — and so that first responders and park staff have a more reliable data communications layer when cell coverage drops out.

The infrastructure is community-owned from the start, with no carrier dependency and no cost to the people who use it.

### Why Start in a New River Gorge Town

Communities along and around New River Gorge National Park and Preserve are among the most historically significant rail and river communities in the region. They are also among the most underserved when it comes to reliable connectivity.

The gorge is beautiful, steep, and remote. Visitors frequently arrive expecting to access park information and find no signal at the trailhead, the depot, or the riverfront overlook. That connectivity gap is a heritage interpretation gap. NPS and community partners have invested in preservation, signage, and interpretive programs across the Gorge — but much of that investment goes unreached when visitors cannot load a map, find a trail narrative, or access a walking-tour story on their device.

Demonstrating a small, respectful connectivity layer in one community first creates a documented option that other interested New River Gorge towns could choose to adapt later, without assuming a corridor-wide commitment from the start.

### What Will Actually Be Built

The minimal starting configuration for the first participating community consists of three components:

- **1× Ubiquiti Rocket Prism 5AC Gen2** — a high-performance backbone radio providing the wireless spine and serving as the host for locally running intelligence services
- **1× MikroTik SXTsq 5 ac** — a compact endpoint radio extending coverage to a second priority location within the community
- **1× Starlink Business terminal** — satellite backhaul providing up to 400 Mbps of shared broadband delivered free across every node on the mesh

Supporting hardware — a weatherproof enclosure, PoE switch, surge protection, grounding, cabling, and a small UPS unit — ensures the system continues operating through short power or network interruptions.

All equipment is chosen and sited to be as unobtrusive and reversible as possible: neutral colors, minimal size, mounted on existing structures or previously disturbed areas where allowed, and documented with photographs and drawings for historic-preservation review.

Because no fees are charged to users, the network operates as free public infrastructure — the same model as a library or park Wi-Fi — with no ISP licensing required.

As the pilot matures and a community chooses to deepen participation, additional endpoint radios and locally hosted intelligence capabilities can be added to the same backbone without rebuilding the installation.

---

## Executive Summary

MS.NPS.ALLIS is a corridor-scale, small-footprint connectivity and intelligence initiative designed for one New River Gorge gateway community as a first deployment, with a clear path to extend the pattern across the wider Gorge region.

The starting build uses a single backbone radio, one endpoint radio, and a Starlink terminal to create a resilient local internet layer — a connectivity presence tailored to visitor experience and park operations, including at sites where coverage gaps are already an identified need, addressed here at no cost to NPS.

Rather than sending every request to distant data centers, the program is designed to move heritage interpretation, mapping, and locally hosted intelligence to the network's edge. Trail content, historic narratives, maps, and visitor information are processed and served locally in real time, even in steep, forested terrain where cell connectivity is intermittent. Visitors get a richer, more reliable experience. Park staff and community partners get a locally owned layer of connectivity that works when commercial networks do not.

This program does not replace or interfere with licensed radio systems such as WV SIRN or Motorola-managed networks, which remain the primary voice communications backbone for emergency responders. MS.NPS.ALLIS operates as an internet data layer only.

NPS participation is structured as an in-kind contribution — site access, a designated point of contact, and network permission where appropriate — with no budget obligation or procurement requirement on the part of the park. If, at a future date, NPS or any participating community chooses to explore an expanded service arrangement, that would be a separate conversation governed by MountainShares community agreements already in place. That conversation is not part of this proposal.

---

## Context and Objectives

### Corridor Context

The New River Gorge region is anchored by a set of historic rail, coal, and river towns — Thurmond, Hinton, Mount Hope, Fayetteville, Oak Hill, Ansted, Smithers, Montgomery, Gauley Bridge, and others — that sit in and around New River Gorge National Park and Preserve. Many of these communities have small or declining populations but high symbolic and recreational importance as preserved railroad-era landscapes and gateway towns to the Gorge. They draw visitors precisely because of what they have not lost: their visual integrity, their rail corridors, their riverfronts, and the stories embedded in both.

That same terrain — steep, heavily forested, deeply incised by the New and Gauley rivers — creates sharp elevation changes and narrow corridors that are beautiful but consistently challenging for cell coverage. Heritage content, trail information, and visitor orientation materials that depend on external networks simply do not reach people when and where they are most needed.

The opportunity is not to overlay these places with visible technology. It is to add a quiet, locally owned connectivity and intelligence layer that makes their stories more accessible without changing what makes them worth visiting.

### Problem Statement

The specific problem this program addresses is the lack of locally owned, resilient connectivity in New River Gorge gateway communities that:

- Serves visitors reliably, independent of which commercial carrier they use or whether backhaul to distant data centers is available
- Delivers heritage content, trail information, maps, and points of interest close to where visitors actually are — at park facilities, depots, trailheads, and riverfront sites where cell coverage is limited or absent
- Continues to function even when access to external networks is degraded, by storing and serving key content locally rather than depending on infrastructure that the terrain and corridor conditions routinely interrupt
- Provides a real-world environment where locally hosted intelligence can be observed, evaluated, and refined under genuine operating conditions

### Project Objectives

1. **Reliable visitor and operational connectivity**
   Provide locally owned, redundant internet connectivity for visitors, park staff, and municipal partners in defined coverage areas around an initial gateway community. This program does not replace or interfere with licensed radio systems such as WV SIRN or Motorola-managed networks, which remain the primary voice communications backbone for emergency responders.

2. **Locally hosted heritage interpretation and location intelligence**
   Deploy modest edge computing in gateway communities that can host heritage content, location-aware intelligence, and geospatial services locally — enabling visitors to access trail narratives, historic context, maps, and points of interest in real time without depending on external connectivity.

3. **Heritage-compatible infrastructure design**
   Demonstrate that connectivity and intelligence infrastructure can be deployed across historic towns and cultural landscapes with minimal visual and physical impact, using discrete hardware, reversible mounts, neutral colors, and siting on existing structures or disturbed areas.

4. **Transferable regional pattern**
   Use the first participating community as a testbed to develop a small, well-documented approach that can be adapted by other Gorge communities — Mount Hope, Glen Jean, Hinton, Montgomery, Smithers, Fayetteville, Oak Hill — that share similar terrain, heritage, and connectivity challenges. The long-term goal is a corridor-wide, locally owned connectivity and heritage interpretation network that communities can extend, replicate, or retire on their own timelines.

---

## Technical Design

### Physical Architecture

**Backbone radio — 1× Ubiquiti Rocket Prism 5AC Gen2**
A high-performance 5 GHz basestation radio providing the wireless spine of the community mesh, supporting more than 450 Mbps throughput and 50 or more connected devices when paired with appropriate antennas. Integrated GPS synchronization and advanced RF filtering maintain performance in the narrow corridor terrain typical of New River Gorge communities. This radio also serves as the host platform for locally running intelligence and content services.

**Endpoint radio — 1× MikroTik SXTsq 5 ac**
A compact 5 GHz 802.11ac device with an integrated 16 dBi antenna and gigabit Ethernet, extending coverage from the backbone to a second priority location — a trailhead, a town common, an EMS staging point, or another visitor-facing site identified with NPS and community partners. Weather-rated, low-power, and widely used in community network deployments.

**Satellite uplink — 1× Starlink Business terminal**
Provides broadband backhaul with downlink speeds up to roughly 400 Mbps. The uplink is not required for the mesh to function locally — core content and intelligence services continue to operate from the backbone node whether or not the satellite connection is active — but it allows the community to exchange data with external systems when connectivity is available.

**Supporting infrastructure**
A weatherproof enclosure, outdoor PoE switch, surge protection, grounding, mounting hardware, shielded outdoor cabling, and a small UPS unit, sized for the Gorge's climate and heritage setting.

### Illustrative Siting — One Possible Configuration

*The following describes one possible siting arrangement for illustrative purposes. Actual locations in any participating community would be determined through conversations with NPS, community stakeholders, and local partners — including any approvals required from property owners or agencies — before any installation takes place.*

In a community such as Thurmond, one possible configuration would place the backbone radio and Starlink terminal on or near the depot building, which serves as the primary visitor hub and sits at the center of pedestrian activity along the river corridor. The Starlink terminal would bring satellite backhaul to that site, and the backbone radio would distribute connectivity along the narrow gorge corridor in both directions.

A single endpoint radio placed on or near a second civic structure further along the main street — such as a post office or a community building — would extend coverage to that part of the pedestrian corridor, giving visitors and staff a consistent connection across the walkable core of town.

This two-point configuration — depot anchor, street-level endpoint — creates a connected layer along the town's most-used path without introducing any new poles, towers, or structures. Both installations would use reversible mounts on existing buildings, documented for historic-preservation review.

Any siting arrangement in a historic district requires review and approval from NPS, the State Historic Preservation Office, and relevant property owners or agencies before work begins. This example is intended to illustrate the scale and character of the installation, not to commit to specific locations.

### Logical Architecture — Three Layers

**Connectivity layer**
The backbone radio forms the wireless spine of the community mesh. The endpoint radio extends that coverage to a second location. The Starlink terminal provides a path to external networks when available. The mesh is designed to maintain local connectivity and core visitor services even when that uplink is degraded or offline.

**Content layer**
Trail and heritage narratives, maps, points of interest, visitor orientation materials, and safety information are stored and served locally from the backbone node using a content-addressed data store. A visitor anywhere on the mesh receives the same locally cached content whether or not their carrier has signal in that location.

**Intelligence layer**
Locally running models surface relevant heritage content based on a visitor's location, suggest routes given known conditions, and highlight nearby points of interest and hazards. These services function on local hardware, with external connectivity treated as an optional enhancement rather than a requirement.

### Design Principles

**Heritage-sensitive deployment**
Equipment is mounted to minimize visual intrusion and avoid damage to historic fabric, using reversible mounts, neutral colors, and consolidation with existing utility or structural elements where allowed. Every installation is documented — photographs, diagrams, written descriptions — for review by preservation staff, NPS teams, and relevant local authorities.

**Local resilience, external connectivity optional**
Core functions — visitor connectivity, cached heritage content, maps, trail information, and location-aware services — are designed to continue working even when the satellite uplink or broader internet is unavailable. External systems are treated as enhancement layers, not hard dependencies.

**Small, extensible footprint**
The starting configuration is intentionally minimal. Additional endpoint radios, content, and intelligence capabilities can be added to the same backbone as a community's needs and confidence grow, without rebuilding the installation.

---

## Governance, Data, and MountainShares Framework

### Ownership and Operational Roles

**Infrastructure ownership**
In each participating community, physical assets — the radio, satellite terminal, enclosure, mounts, cabling, and UPS — are owned by the municipality, a designated public safety agency, or an agreed public-benefit partner, with all assets and sites formally documented. Sites, easements, and mounting rights are governed by written agreements with landowners or agencies that define responsibilities for access, maintenance, and eventual removal or upgrade.

**Operational responsibility**
A primary operating entity in the community manages day-to-day operation, monitoring, and first-line troubleshooting. EMS, fire, law enforcement, and park staff remain operational users, involved in defining coverage priorities but not expected to administer the hardware directly.

**Lifecycle management**
Hardware and software lifecycles — replacement schedules, firmware updates, security patches — are documented in straightforward runbooks with clear role assignments. A lightweight regional working group can share lessons learned across corridor communities without centralizing control of local assets.

### MountainShares Community Agreement

Participation in MS.NPS.ALLIS at the no-cost tier requires signing the MountainShares community governance agreement, available in the project repository under mountainshares-dao. This is a data stewardship and community governance commitment, not a financial one. It defines:

- How locally generated data is owned, governed, and protected
- Who may access operational and heritage data, and under what conditions
- How communities share only what is necessary across the corridor
- The terms under which a community could, in the future, choose to explore an expanded arrangement — a conversation that would happen at that time, not as part of this proposal

NPS participation is framed as an in-kind contribution. The park is not purchasing a service. Any future conversation about an expanded service arrangement would be governed by the MountainShares agreements already in place at that time.

### Data Governance and Privacy

**Data categories:**
- Operational network data: status, throughput, errors, uptime
- Location and incident context: positions where appropriate, incident markers, map interactions
- Content and reference data: maps, trail and heritage content, protocols

**Local-first, minimized collection**
Only data needed to deliver visitor connectivity, safety support, and heritage services is collected. Location data for responders is limited to operational contexts, not continuous tracking outside mission needs.

**Access control and protection**
Access to detailed operational and location data is restricted to authorized roles, with authentication and audit logging. When data leaves the local environment for regional analysis or research, it is de-identified or aggregated wherever possible.

**Retention and transparency**
Retention periods are defined per data category, with automatic deletion where feasible. Agencies and, where appropriate, the public receive clear explanations of what is collected, how it is used, and how it is protected.

### Decentralization and Reduced Dependence on External Infrastructure

**Locally hosted processing**
Intelligence models and location services run on the backbone node, executing core functions in place rather than routing every request over the satellite link — reducing latency and keeping visitor-facing content available whether or not external connectivity is active.

**Community-owned data**
Local operational, visitor, and heritage data is treated as a community resource, owned and governed by the agencies and communities that produce and use it. Additional corridor communities can operate their own nodes and data, sharing only what is necessary at the regional level.

**Resilience to outages**
The system does not depend on constant access to any single external provider. Real-time visitor connectivity and locally cached content delivery continue in each participating community even if external systems are unavailable.

---

## Ethical and Regulatory Considerations

**Regulatory alignment**
MS.NPS.ALLIS operates as an internet data layer only. It does not carry licensed radio transmissions and does not require WV SIRN or Motorola permissions. Voice communications for EMS and SAR remain entirely on existing licensed infrastructure. Any future integration with 911 or public safety answering points follows existing federal and state guidance.

**Responsible use of locally hosted intelligence**
Locally running models are designed to support decisions — suggesting routes, highlighting hazards, delivering contextual heritage content — not to make automated decisions about people or enforcement actions. Regular review with local stakeholders ensures that models can be corrected, retrained, or retired, and that community values are reflected in how the tools operate.

---

## Heritage and NPS Alignment

### Historic Context in New River Gorge Communities

The New River Gorge corridor contains some of the most intact railroad-era townscapes in Appalachia. Preserved depots, commercial buildings, rail corridors, and riverfronts are central to the region's coal and transportation story, making them highly sensitive settings for any new infrastructure. Visitors, residents, and agencies value their visual integrity, and any connectivity system must blend into the existing fabric and be clearly documented in ways that respect both heritage and the visitor experience that draws people to the Gorge.

NPS has invested in preservation work and interpretation training across the park, emphasizing retention of historic materials and character in buildings, rail corridors, and cultural landscapes. New infrastructure in historic areas must support safety, enable reuse, and respect the visual and material integrity of remaining resources.

### Alignment with NPS Telecommunications and Preservation Guidance

NPS telecommunications planning emphasizes enhancing coverage while minimizing impacts on cultural landscapes, historic viewsheds, and historic districts. Section 106 guidance indicates that major towers inside historic districts are generally disfavored; small nodes, antennas on existing infrastructure, and carefully sited low-profile equipment may be acceptable; ground disturbance should be minimized and focused on existing corridors and disturbed areas; and all actions must follow the Secretary of the Interior's Standards and NPS cultural-resource policies.

MS.NPS.ALLIS follows these principles by relying on a minimal number of small, distributed components, no new ground disturbance, and siting on or near existing structures wherever feasible.

### Siting and Visual Impact Principles

**Use existing structures and corridors**
Candidate locations include existing utility poles, non-contributing or replacement structures, and discrete areas near developed sites — depots, service buildings, non-historic support structures — subject to appropriate approvals. Cabling follows existing utility corridors or disturbed ground, avoiding new disturbance in sensitive areas.

**Minimize visibility**
Equipment size and color are chosen to reduce contrast with existing materials and vegetation. Key viewpoints and the ability of historic properties to convey significance are considered throughout the siting process.

**Reversibility and documentation**
Installations on or near historic fabric are reversible where feasible, using mounts that avoid permanent alteration and can be removed without visible damage. Each site is documented — maps, photographs, narratives — before and after installation, and this documentation is shared with NPS and the State Historic Preservation Office as appropriate.

### Heritage Interpretation and Community Value

The same infrastructure that supports visitor connectivity can cache and deliver curated historic and interpretive content — walking-trail stories, rail-era narratives, riverfront histories — to visitors' devices or future extended-reality tools, even when external networks are down. This ensures that preservation investments across the Gorge are matched by accessible interpretation that works in the low-connectivity conditions visitors most frequently encounter in the park.

Improved connectivity and digital access can also make it more feasible for partners to program or adaptively reuse historic structures — a factor NPS has noted in decisions to retain buildings with reuse potential. Demonstrating that safety, connectivity, and heritage can reinforce one another across multiple New River Gorge communities offers a model for how this kind of infrastructure can serve preservation goals rather than compete with them.

---

## Implementation Plan

### Engagement, Siting, and Design (4–8 weeks)

Initial conversations with municipal leaders, NPS, EMS and SAR teams, and community stakeholders in the first participating community to confirm priorities and define a realistic coverage area. Site walks identify candidate locations and constraints. A draft siting plan, visual documentation, and preservation notes are prepared for NPS, SHPO, and local review alongside a refined technical design and updated budget.

MountainShares community governance agreements are executed with all participating partners before any hardware procurement begins.

### Installation and Commissioning (approximately 1–2 weeks on-site)

- Procurement of hardware according to the approved configuration for the first community
- Physical installation of the backbone radio, endpoint radio, enclosure, power, and Starlink terminal, following heritage-sensitive siting and any required preservation approvals
- Configuration, alignment, and integration with local EMS and SAR, NPS, and municipal workflows
- Baseline testing, documentation, and handoff to the designated operating entity
- **Deliverable:** A functioning free connectivity layer across the defined coverage area in the first community, at no cost to NPS or the town

### Pilot Operations and Evaluation (6–12 months)

Live operation during real-world visitor seasons, EMS workflows, and day-to-day park operations. Collection of operational metrics — uptime, coverage, usage — alongside qualitative feedback from EMS, park staff, and visitors. Iterative refinement of content, models, and workflows based on actual experience. Preparation of a concise summary describing what worked, what did not, and what another community could adapt if interested.

### Review and Next-Community Decisions

A joint evaluation with local stakeholders — municipal government, EMS and SAR, NPS, community members, and any interested regional partners — to review results and lessons learned. The group then decides whether to maintain the current deployment, add modest coverage within the same community, explore a similarly scoped installation in one additional New River Gorge community, or retire components if the approach is not a good fit for that place.

---

## Budget

The starting configuration uses three core components, with Thurmond as the illustrative reference point. Actual costs for any participating community would be refined during the siting and design period.

| Category | Estimated Cost |
|---|---|
| 1× Ubiquiti Rocket Prism 5AC Gen2 (backbone radio) | ~$200 |
| 1× MikroTik SXTsq 5 ac (endpoint radio) | ~$90 |
| 1× Starlink Business terminal + first year of service | ~$2,500 hardware + ~$3,000 service |
| Enclosure, PoE switch, surge protection, cabling, UPS | ~$400–600 |
| Installation labor (Kidd's Technical Services) | ~$1,500–2,500 |
| Siting review and preservation documentation | ~$1,200–2,000 |
| **Estimated total (single community, starting configuration)** | **~$8,700–11,100** |
| Starlink Business monthly subscription (recurring after year 1) | ~$250/month |
| Additional endpoint radios or edge compute, if added later | Scoped separately per community decision |

NPS has no budget obligation or procurement requirement. All infrastructure is provided at no cost to the park under the MS.NPS.ALLIS no-cost tier. Any future service arrangement, if ever relevant, is a separate conversation governed by MountainShares agreements already in place at that time.

---

## About MS.NPS.ALLIS and the MountainShares Framework

MS.NPS.ALLIS is the National Park Service node of the MountainShares ALLIS (Artificial Learning & Location Intelligence System) network. It is designed as a no-cost, community-governed service. The broader MountainShares framework — including governance agreements, DAO structure, and community instruments — is documented in the project repository.

Participation at the no-cost tier requires signing the MountainShares community agreement as a governance and data stewardship commitment, not a financial one. This ensures that all participating communities — NPS, the first gateway town, and future Gorge partners — share consistent principles for data ownership, local resilience, and community benefit.

The goal is a corridor-wide, locally owned connectivity and heritage interpretation network that New River Gorge communities can extend, replicate, or retire on their own timelines — delivered close to where visitors actually are, and without losing what makes these places worth saving in the first place.

---

*Prepared by Carrie Kidd, Kidd's Technical Services | kiddstechnical@gmail.com*
*Technical installation: Aubrey Dickerson, Kidd's Technical Services*
*For questions about the MountainShares governance framework, see the project repository under mountainshares-dao.*
