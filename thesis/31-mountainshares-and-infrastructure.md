# 31. MountainShares and Web Infrastructure Integration

**Disciplinary Context: Appalachian Economic Commons**

This chapter instantiates Polymathmatic Geography principles P1, P9, P16, and related axioms for the Appalachian economic commons by treating The Commons as the primary observation and interaction surface of the discipline: the place where inhabitants' behavior becomes data, and data returns as geometry — maps, dashboards, governance flows, and narratives that residents can see and shape. For the underlying framework, see Polymathmatic Geography: A Manifesto and the associated principles at:

[https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/Polymathmatical-Geography.md](https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/Polymathmatical-Geography.md)
[https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/Quantarithmia%20Overview.md](https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/Quantarithmia%20Overview.md)

This chapter describes the relationship between MountainShares, Ms. Jarvis, and the web and infrastructure layers that support cooperative governance, transparency, and long-term stewardship. It focuses on how the cooperative's data, rules, and narratives are represented in Ms. Jarvis, and how web infrastructure — especially The Commons as a public interface — can be used to keep those representations aligned with reality and visible to the people who live inside them.

*As of March 2026, the core MountainShares governance corpus is ingested into Ms. Jarvis's production RAG server with county/role tagging, and a Postgres-backed episodic log with multi-scale aggregates provides an operational and audit surface that The Commons and MountainShares can build on for live cooperative use. The two confirmed running containers anchoring this infrastructure are `jarvis-commons-gamification` and `jarvis-dao-governance` (both ✅ Verified in the March 2026 audit).*

---

## 31.1 MountainShares as a Data and Governance Source

### 31.1.1 Role Inside MountainShares

MountainShares defines a concrete set of governance rules, roles, and data flows that are rendered visible and actionable through The Commons:

- **Governance texts**
  Constitutional principles, bylaws, program Terms and Conditions, Program Rules, and cooperative agreements describe how authority and responsibility are structured, including how MountainShares are issued, capped, and retired.

- **Membership and roles**
  Categories of participants (for example, workers, community members, organizational partners, Benefits-Sensitive accounts) and their associated permissions, such as who may propose, vote, administer promo pools, or view detailed dashboards.

- **Operational data**
  Records of proposals, votes, distributions, audits, treasury snapshots, EMS earning flows, and other cooperative processes, surfaced in The Commons as timelines, dashboards, and maps so that rules are experienced as lived geometry rather than hidden configuration.

These materials are ingested into Ms. Jarvis as part of the governance and norms collections in ChromaDB and as structured entities in the Geospatial Belief and Inference Model (GBIM), making them available for retrieval, comparison across time, and spatial analysis. In the current production system, these governance texts and program rules are continuously indexed into dedicated RAG collections with rich metadata (such as county and role), so that both human queries and backend services can reliably retrieve and recombine them.

**Confirmed containers (March 2026 audit):** The abstract RAG and episodic logging infrastructure described throughout this chapter is anchored in two confirmed running services:

- `jarvis-commons-gamification` ✅ Verified — handles the Commons gamification layer, commons participation tracking, and cooperative engagement surfaces.
- `jarvis-dao-governance` ✅ Verified — handles DAO governance corpus ingestion, governance rule retrieval, and episodic governance logging.

These containers share the `msjarvis` PostgreSQL instance (port 5433) for episodic logging and structured governance data (see §31.3), and expose ChromaDB-backed RAG endpoints for governance corpus retrieval. All references to "a dedicated RAG service" and "an episodic logging service" throughout this chapter refer concretely to these two containers unless otherwise noted.

The Commons acts as the human-facing lens on this process: when residents read or contest a rule in the app, they are effectively querying Ms. Jarvis's internal model of the cooperative stack. As Commons features come online, they increasingly bind to the same retrieval and logging surfaces that Ms. Jarvis uses internally, turning governance texts from static pages into active, queryable geometry.

---

## 31.2 Web Infrastructure for Cooperative Operations

### 31.2.1 Interfaces to Cooperative Data

MountainShares relies on web infrastructure — with The Commons at the center — for:

- **Public documentation**
  Hosting governance documents, explanatory materials, the Economic Safety Specification, Program Rules parameter tables, and public-facing reports in forms that Ms. Jarvis can scrape and that residents can read directly.

- **Operational interfaces**
  Providing forms and dashboards in The Commons for proposals, voting, EMS logging, merchant onboarding, and reporting, so that governance behavior becomes structured data rather than opaque back-office action.

- **Integration points**
  Connecting external systems (for example, payment processors, hosted nodes, monitoring services) to cooperative logic, with status and alerts surfaced back through The Commons so residents can see when infrastructure is healthy or degraded.

Ms. Jarvis interacts with these layers primarily through documented APIs, scraper pipelines, and scheduled update jobs, rather than through opaque integrations. In practice, this means that both the machine and the inhabitants are reading and writing to a shared "surface" — The Commons and its backing APIs — where the geometry of the cooperative is continuously redrawn.

In production, `jarvis-dao-governance` (✅ Verified) exposes search and storage endpoints over the ingested MountainShares corpus, and `jarvis-commons-gamification` (✅ Verified) records interactions with typed, tagged episodes and multi-scale usage statistics. The Commons and related web properties are designed to call into these services so that what residents see in the interface and what Ms. Jarvis reasons over are two views on the same cooperative data.

---

## 31.3 Ms. Jarvis's Role in MountainShares

### 31.3.1 Connections to Hosting and Web Platforms

Ms. Jarvis supports MountainShares by:

- **Retrieval and explanation**
  Answering questions, via The Commons and other interfaces, about rules, historical decisions, spatial impacts, and economic safety tables in a way that is grounded in on-chain records, governance docs, and GIS context.

- **Scenario analysis**
  Exploring the implications of proposed changes — for example, altering EMS→M$ rates, caps, or reserve bands — for different communities, infrastructure corridors, or governance configurations, and returning these as maps or dashboards in The Commons.

- **Narrative support**
  Generating summaries and narratives that explain complex governance decisions in accessible, place-anchored terms (e.g., "what this new reserve band means for Oak Hill merchants"), subject to safeguards and human review.

These roles are always bounded by cooperative-defined constraints and review. The Commons provides the primary channel where those bounded outputs appear and can be interrogated by residents, turning Ms. Jarvis's internal models into public-facing geometry and story.

In the current deployment, the production RAG server (backed by ChromaDB, served via `jarvis-dao-governance` at its internal Docker network endpoint on `qualia-net`) and the episodic log in **PostgreSQL `msjarvis` (port 5433)** provide the core plumbing for these tasks. The `msjarvis` instance (port 5433, containing 5,416,521 verified GBIM entities as of the March 2026 audit) is the authoritative PostgreSQL home for MountainShares governance episodes, role-tagged retrieval metadata, and multi-scale aggregate statistics. Governance-relevant episodes are tagged (for example, as `governance` with specific topical tags) and aggregated over multiple time windows, so that high-impact questions, explanations, and scenarios can be surfaced for human review and later visualized in Commons dashboards without losing their temporal or spatial context.

> **Database reference note:** MountainShares geospatial governance data and spatial policy analysis that require PostGIS are stored in `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ GBIM beliefs). The episodic governance log and structured governance entity records are in `msjarvis` (port 5433). Queries combining both (e.g., governance decisions mapped to Fayette County parcels) will join across both instances.

---

## 31.4 MountainShares Topics in Autonomous Learning

### 31.4.1 Safeguards for External Actions

MountainShares is not only a consumer of Ms. Jarvis's analyses but also a contributor to her ongoing curriculum:

- **GBIM-driven suggestions**
  The MountainShares GBIM emits topic summaries about smart contract audits, validator incentives, governance mechanisms, reserve-ratio behavior, and related infrastructure concerns. These suggestions are sent to the optimized learner via `POST /learning/suggest` with `source_gbim` set to `"mountainshares_gbim"`.

- **Examples of current themes**
  - Audit and security: community-friendly smart contract audit strategies, risk profiles for validator sets, and attack surfaces relevant to EMS/PMS flows.
  - Incentives and accountability: validator rewards, slashing conditions, and mechanisms for aligning economic incentives with community goals and caps in the Economic Safety Specification.

- **Curriculum impact**
  Once stored in the `learning_suggestions` collection, these topics become candidates for autonomous learning cycles alongside the default curriculum. This creates a feedback loop where MountainShares concerns — captured in part by how inhabitants actually use The Commons — directly influence what Ms. Jarvis studies in the background, improving future support for DAO decisions and infrastructure planning.

> **⚠️ EEG / autonomous learner known gap:** The full curriculum loop described above — specifically the `POST /learning/suggest` flow reaching an active autonomous learner — depends on the EEG rhythm services and autonomous learner architecture. As documented in **Chapter 28 §28.4**, all three EEG services were lost in the October 2025 rebuild and have not yet been restored; their recovery is pending retrieval from pre-October 2025 backups (estimated location: 2TB drives on development machine). Until the EEG/autonomous learner services are restored, the MountainShares GBIM suggestion flow is scaffolded but the receiving autonomous learner is not active. The `learning_suggestions` ChromaDB collection and ingestion endpoints remain available; the gap is in the autonomous learner consumer, not the suggestion emitter. Cross-reference: **Ch 28 §28.4** (EEG loss documented), **Ch 28 §28.10** (recovery path), **Ch 28 §28.9** (watchdog system context).

This integration makes MountainShares both a beneficiary and a shaper of the system's long-term learning trajectory, with The Commons acting as the shared surface where learning needs emerge and are reflected back in improved tools. In the current system, the ingestion and logging layers that underpin this curriculum are live via `jarvis-dao-governance` and `jarvis-commons-gamification`; the dedicated autonomous learner and its MountainShares-specific suggestion flows are specified and partially scaffolded, with full deployment dependent on EEG service restoration (see above).

---

## 31.5 Safeguards in Cooperative Contexts

### 31.5.1 Use of Container and Coordinator Layers

Because MountainShares involves real communities and material consequences, safeguards are essential:

- **Constitutional alignment**
  Ms. Jarvis's outputs for MountainShares are filtered through the cooperative's constitutional principles, the Manifesto, the Principles of Polymathmatic Geography, and applicable legal constraints before any recommendation appears in The Commons.

- **Role-aware access**
  Different cooperative roles may see different levels of detail or types of analysis, enforced at the API and routing layers: for example, stewards and auditors may see detailed treasury projections, while general users see simplified dashboards in The Commons.

- **Human oversight**
  High-impact recommendations (such as changes to reserve bands, caps, or cross-region flows) are routed through human review and approval processes, with clear pointers — within The Commons — to the data and assumptions involved.

These protections align the use of Ms. Jarvis with the cooperative's commitment to accountability and non-extractive design. The Commons, in turn, becomes the venue where these safeguards are visible and contestable.

In production, a typed episodic log in PostgreSQL `msjarvis` (port 5433) and role-aware interfaces to the RAG and stats services (via `jarvis-dao-governance` and `jarvis-commons-gamification`, both ✅ Verified) provide the substrate for these safeguards. Governance-type episodes, tagged with topics such as reserve bands or EMS parameters, can be identified and inspected over time, and the same APIs that power Ms. Jarvis's internal reasoning can be restricted or widened based on cooperative roles, forming a practical enforcement layer for constitutional alignment and oversight.

---

## 31.6 Relationship to Live Feeds and Narratives

Integration capabilities connect to the live cycles described in Part V:

- **Narrative alignment**
  Periodic summaries and public updates can reflect cooperative activities and infrastructure changes (for example, "reserve ratio crossed into Band B"), with those narratives delivered through The Commons news feed or notifications, subject to the same safeguards as other outward-facing narratives.

- **Data refresh**
  Scheduled processes pull updated cooperative information (governance decisions, EMS statistics, merchant status) and hosting status, feeding it through the barrier and into memory and containers. The Commons reflects these refreshes in updated dashboards and maps, so inhabitants see the same system Ms. Jarvis reasons about.

- **Diagnostic loops**
  Observed discrepancies between intended and actual infrastructure states — such as a merchant showing as active in The Commons but failing to settle payments — can prompt further analysis or adjustments to policies. These diagnostics appear as alerts or maintenance banners, making the health of the stack a shared concern.

These links help maintain coherence between internal models and external realities, with The Commons serving as the "instrument panel" where residents observe the system's geometry in real time.

As of March 2026, the underlying data flows — governance corpus ingestion, episode logging, and multi-scale statistics — are live via confirmed running containers `jarvis-commons-gamification` and `jarvis-dao-governance` (both ✅ Verified, March 2026 audit), providing a reliable substrate for live feeds and narratives. As The Commons front-end and notification systems attach to these backends, the cooperative will be able to surface rate bands, flows, and anomalies as shared stories rather than opaque back-office events.

---

## 31.7 Summary

Integration with cooperative structures and hosting platforms is handled through scoped interfaces, layered safeguards, and the same container and coordination mechanisms that govern other activities. A small, attached optimizer observes these integrations and proposes incremental refinements, which are evaluated and recorded through the same paths as other self-improvement processes.

By design, The Commons is the observation and interaction surface for polymathmatic geography in Appalachia: it is where inhabitants' behavior becomes data, where that data is braided into Ms. Jarvis's GBIM and containers, and where the resulting geometry — rates, bands, flows, maps, and narratives — returns to the community as something they can read, question, and reshape.

**Confirmed live as of March 2026:** The following specific components are confirmed running and audited:

- `jarvis-dao-governance` ✅ Verified — production RAG service for MountainShares governance corpus, backed by ChromaDB with county/role tagging, episodic governance log writing to PostgreSQL `msjarvis` (port 5433)
- `jarvis-commons-gamification` ✅ Verified — commons participation tracking, gamification layer, multi-scale usage statistics, episodic logging to PostgreSQL `msjarvis` (port 5433)

With these containers live and the MountainShares governance corpus ingested, the remaining work focuses on deepening The Commons' bindings to these services so that what Ms. Jarvis remembers, reasons about, and learns from is always visible and contestable to the people living inside the cooperative geometry. The full autonomous learning curriculum loop (§31.4) additionally depends on restoration of the EEG/autonomous learner services documented as a known gap in **Chapter 28 §28.4**.

---

*Last updated: 2026-03-27 by Carrie Kidd (Mamma Kidd), Pax WV*
*Dateline updated from "early 2026" to "March 2026" — March 27, 2026*
*jarvis-commons-gamification and jarvis-dao-governance named throughout — March 27, 2026*
*PostgreSQL msjarvis (port 5433) specified as episodic log and governance data store — March 27, 2026*
*EEG/autonomous learner known gap cross-reference added to §31.4 — March 27, 2026*
*Summary updated to anchor "already live" claim to confirmed containers — March 27, 2026*
`````
