> **Why this matters for Polymathmatic Geography**  
> This chapter makes Polymathmatic Geography operational by specifying how a Steward System can hold beliefs explicitly tied to **who**, **what**, **where**, **when**, **how**, **why**, **for whom**, **under whose authority**, and **on what evidence**. It directly supports:  
> - **P1 – Every where is entangled** by representing legal, economic, infrastructural, social, and spiritual facts about Appalachia as a unified, structured belief space rather than disconnected layers.  
> - **P3 – Power has a geometry** by encoding dependencies, exposures, and flows as graph and spatial relationships between entities and regions.  
> - **P5 – Design is a geographic act** by treating schemas, APIs, and guards as design choices that reshape how institutions "see" their territory and act within it.  
> - **P12 – Intelligence with a ZIP code** by binding Ms. Jarvis's cognition to specific West Virginia and Appalachian geographies through GBIM and a verified local resource registry keyed by ZIP, county, and program type.  
> - **P16 – Power accountable to place** by requiring that beliefs be inspectable, contestable, and traceable to concrete evidence about particular communities, including whether local resource information has been recently verified with the people running those programs.  
> This chapter defines the **Computational Instrument** tier: the core representational machinery that enforces and audits Quantarithmia's spatial‑justice commitments in a live system.

## Ms. Jarvis and the Geospatial Belief Information Model (GBIM)

Within **polymathmatic geography**, Ms. Egeria Jarvis is a bounded, bio‑inspired Steward System whose beliefs are explicitly anchored in place, time, community, and evidence. **GBIM** (Geospatial Belief Information Model) is the core layer tying Ms. Jarvis's reasoning to concrete geographies in West Virginia and Appalachia, implemented as a **Generalized Bio‑inspired Machine** design.

This chapter presents Ms. Jarvis as a glassbox AI Steward System and explains the Geospatial Belief Information Model underpinning its reasoning. The focus is on a rigorous, inspectable architecture for layered reasoning, memory, and judgment explicitly tied to geospatial entities, temporal context, evidential provenance, and the current state of local programs and institutions. Within Quantarithmia, Ms. Jarvis and GBIM serve as the technical realization of spatially grounded, justice‑oriented reasoning: they enable asking *“What does the Steward System hold about this place, for whom, under whose authority, and based on what evidence, and when was this last confirmed with the people involved?”* with auditable, contestable answers.

---

## What GBIM Is
<div align="center">
  <img width="60%" alt="geospatial belief information model" src="https://github.com/user-attachments/assets/331685c5-977e-4b60-9a96-3150b71787a2" />
</div>

> Figure 1. High‑level structure of the Geospatial Belief Information Model (GBIM), showing the PostGIS geospatial corpus, Chroma semantic collections, the production belief graph schema, and the verified local resource registry, all tied together by nine epistemic axes (who, what, where, when, how, why, for whom, under whose authority, on what evidence).

GBIM is Ms. Jarvis's internal model for tying beliefs to **who**, **what**, **where**, **when**, **how**, **why**, **for whom**, **under whose authority**, and **on what evidence**, focused on West Virginia and Appalachia. The current production deployment integrates four cooperating layers:

1. **PostGIS‑backed regional geospatial corpus** – 204 geometry layers (5.5M features, ~2GB) holding actual geometries and core attributes across census, infrastructure, environmental, and governance domains.

2. **ChromaDB collections** – High‑dimensional embeddings and metadata for GIS‑derived features and texts, including a consolidated `GBIM_ATTRS_CSV` index built from 227 `*_attrs` tables, plus per‑layer collections for selected datasets.

3. **Production belief graph schema** – `gbim_worldview_entity`, `gbim_beliefs`, and `gbim_graph_edges` tables binding PostGIS and Chroma layers into a unified, inspectable worldview with explicit provenance.

4. **Verified local resource registry** – A Postgres table (`local_resources`) holding structured records for community programs (food, housing, utilities, seasonal assistance, senior services, education support, etc.), keyed by county and ZIP codes, with contact information, URLs, short descriptions, and a verification state machine (`verification_status`, `last_verified_at`, `verification_notes`). This registry is linked back to Chroma and PDFs via metadata (e.g., `source_url`, `source_file`), and forward into Ms. Jarvis’s reasoning via need tags and ZIP‑aware ranking.

Each belief attaches to all nine epistemic axes:

<div align="center">
  <img width="60%" alt="Belief Neighborhood for One Building" src="https://github.com/user-attachments/assets/9855f916-dadd-46af-8276-60e797549932" />
</div>

> Figure 2. The nine epistemic axes in GBIM, showing how every belief is anchored simultaneously in actors, kinds, places, time, mechanisms, purposes, constituencies, authorities, and evidence, including beliefs about which local programs serve which ZIP codes and when that information was last verified.

- **Who** – persons, institutions, communities (actors, subjects, beneficiaries, decision‑makers), keyed to GBIM entity records and reflected in source attributes and Chroma metadata (owner names, agencies, program sponsors). In the local resource registry, this includes named contacts such as case managers, program directors, and specialist staff for specific programs.

- **What** – the kind of thing or state (asset, event, obligation, harm/benefit), represented by feature classes (`entity_type`) and layer names (`sourcetable` in `gbim.gbim_attrs`), and by `resource_type` in the local resource registry (e.g., `seasonal_assistance`, `food_assistance`, `housing`, `utilities`, `senior_services`, `teacher_support`, `case_management`).

- **Where** – concrete places as PostGIS geometries (points, lines, polygons for buildings, census units, roads, districts, facilities, environmental features, community boundaries) and as service footprints over ZIP codes and counties. Production deployment: 204 standardized datasets in SRID 26917 (UTM Zone 17N NAD83), 5,491,566 worldview entities with full spatial provenance, plus a registry of local resources keyed to West Virginia ZIP codes and counties for routing people to geographically valid programs.

- **When** – temporal metadata indicating belief formation/update time and evidential period. Production deployment: all 5.5M entities timestamped via `created_at`; dataset vintages, event dates, and ingest metadata captured in source attributes; and each local resource record carries a `last_verified_at` timestamp indicating when its contact, eligibility, and coverage details were last confirmed.

- **How** – mechanisms, processes, flows (service delivery, value/risk movement, rule application). Production deployment: millions of `how` edges linking each entity to its source dataset, documenting data collection method and provenance trail; in the resource registry, short `snippet`/description fields summarize how a program works in practice (e.g., Christmas Bureau intake via local agencies, weatherization via a designated CAP agency, tax relief via a state division).

- **Why** – motives, justifications, purposes (policy rationales, program goals, safety standards). Production deployment: millions of `why` edges linking beliefs to their feature references and authorizing narratives, and a local resource layer that encodes program goals and target constituencies (e.g., keeping elders at home safely, preventing shutoffs, providing holiday support to SNAP families).

- **For whom** – distributional effects across people and places (burden/benefit allocation). Production deployment: millions of `for_whom` edges linking entities to beneficiary geographies—census blocks linked to themselves (residents as beneficiaries), infrastructure and buildings linked to “west_virginia_public” (general community benefit)—and resource records that bind programs to particular constituencies (e.g., SNAP households in specific ZIPs, seniors in certain counties, teachers in high‑need subjects).

- **Under whose authority** – laws, policies, institutional bodies authorizing or constraining conditions or actions. Production deployment: millions of `authority` edges linking beliefs to authorizing worldviews, and resource entries that can be tied to state agencies, United Way initiatives, local governments, utility regulators, or federal programs that govern eligibility and operation.

- **On what evidence** – structured links to data sources, documents, observations, model outputs in `belief_state` JSONB fields, and in the resource registry, fields such as `source_url`, `url`, and `verification_notes` that record which PDF, website, or direct contact was used as the evidential basis, and when that evidence was last checked.

GBIM enforces that beliefs are never free‑floating—always anchored to specific actors, kinds, geographies, time frames, mechanisms, purposes, constituencies, authorities, and evidential bases, and, for local programs, to a verification history—enabling examination, challenge, and revision.

---

## How GBIM Is Represented

GBIM's representation combines graph‑style relationships with geospatial indexing, temporal/version history, Hilbert‑space embeddings, and a normalized registry of community programs. The current production deployment fully implements all four core layers.

### Schema Layer

GBIM defines **entities**—places, infrastructures, events, policies, institutions, persons, communities—and their relationships:

- **`gbim.gbim_attrs` table** – Production workhorse holding ~5.5M features from 204 datasets with fields: `sourcetable`, `geodbid`, `label`, `country`, `bbox`, `geom` (SRID 26917), `attrs_json`. This table provides the concrete entity catalog.

- **`gbim_worldview_entity` table (PRODUCTION)** – Holds 5,491,566 entities from 204 datasets with fields: `id` (UUID PK), `worldview_id`, `entity_type`, `source_table`, `source_pk`, `label`, `belief_state` (JSONB), `created_at`. Each entity is explicitly tied to a worldview context and contains structured provenance.

- **`belief_state` field (POPULATED)** – JSONB structure containing:
  - `confidence`: numeric value (e.g., 1.0 for current production entities)  
  - `provenance`: object with `dataset` (sourcetable), `geodb_id`, and `bbox` (GeoJSON point with coordinates in EPSG:26917)  
  - `spatial_metadata`: object with `centroid_x`, `centroid_y`, and `srid` (26917 – UTM Zone 17N NAD83)

- **`gbim.mv_infrastructure_summary` materialized view** – Optimized for ChromaDB integration, extracting `geodbid`, `sourcetable`, `label`, centroid coordinates, and `search_text` from `gbim_attrs`.

- **`local_resources` table (PRODUCTION)** – Normalized registry of community programs with fields such as:
  - Identity and classification: `id`, `name`, `resource_type`, `county`, `state`, `zip_codes` (JSON‑encoded list).
  - Access and description: `phone`, `email`, `url`, `snippet`, `source_url`.
  - Contact‑level details: `contact_name`, `contact_email`, `contact_phone`.
  - Verification state: `verification_status` (e.g., `unknown`, `good`), `last_verified_at` (timestamp), `verification_notes` (text).
  
  This table is the bridge between unstructured resource documents (PDFs, flyers, websites) and Ms. Jarvis’s structured, ZIP‑aware, policy‑aware reasoning about “who can actually help this household in this place right now.”

### Integrated Layers

**Graph relationships**  
Entities link via typed edges forming a belief graph for dependency, flow, and exposure analysis. Production deployment includes a `gbim_graph_edges` table (or equivalent) with core edge types:

- `how` edges: link each entity to its source dataset, documenting the data collection method and provenance trail.
- `why` edges: link beliefs to their feature references and rationales.
- `for_whom` edges: link entities to beneficiary geographies—census blocks linked to themselves (residents as beneficiaries), infrastructure and buildings linked to “west_virginia_public” (general community benefit).
- `authority` edges: link beliefs to authorizing worldviews.

The local resource registry is integrated by:

- Treating each program as an entity in Ms. Jarvis’s worldview, keyed to specific counties and ZIP codes, and associated with beneficiary communities (for_whom), authorizing institutions (authority), and evidence sources (on what evidence).
- Linking resource records back to Chroma and PDFs via metadata such as `source_url` and internal identifiers, so that semantic retrieval over unstructured documents can be resolved to a specific, structured row in `local_resources`.

**Concrete example: A single building's belief neighborhood**

<div align="center">
  <img width="55%" alt="Building Belief Neighborhood Graph" src="https://github.com/user-attachments/assets/7577b4a2-f7f8-44b6-8c1c-c587d0da50e4" />
</div>

> Figure 3. Belief neighborhood for a single building footprint, showing how GBIM links the entity to its dataset (how), beneficiary community (for_whom), and authorizing worldview (authority). All nodes and edges carry provenance and spatial metadata.

In parallel, a single household’s **resource neighborhood** can be viewed as:

- A location (parcel → ZIP → county) obtained from the spatial body / GBIM entities.  
- A filtered set of resource rows from `local_resources` whose `zip_codes` or `county` cover that location and whose `resource_type` matches the expressed need.  
- A ranking informed by verification state (`verification_status`, `last_verified_at`), program requirements (e.g., SNAP/Medicaid, age, veteran status), and Ms. Jarvis’s gateway knowledge (e.g., whether the household is on SNAP, SSI, WV WORKS).  

This neighborhood is queryable via SQL against both GBIM and `local_resources`, and explainable in natural language as “Here are the organizations that currently serve your ZIP, what they offer, how to apply, and when this information was last confirmed.”

The GBIM schema has matured to production readiness: `worldview_id` provides stable identifiers across PostGIS (`gbim_worldview_entity`), Chroma metadata, and belief tables; graph relationships materialize how, why, for whom, and under whose authority as queryable edges; the local resource registry materializes ZIP‑ and county‑specific programs and contacts; and provenance and verification fields make “on what evidence” and “how fresh is this information” first‑class and inspectable for every belief Ms. Jarvis uses in her caseworker‑style guidance.

Production deployment characteristics (January 2026):

- 5,491,566 worldview entities in GBIM.  
- 204 source datasets in the geospatial corpus.  
- 100% provenance coverage for GBIM entities (all have `belief_state` with dataset, geodb_id, bbox, spatial_metadata).  
- 100% spatial metadata coverage (centroid coordinates, SRID 26917).  
- Full coverage of core graph edges (all entities have at least `how` and `for_whom` edges, with many carrying `why` and `authority`).  
- A growing `local_resources` registry of verified community programs in Kanawha and surrounding counties, each with contact details, ZIP and county coverage, and a verification timestamp, ready to be expanded as more PDFs and contacts are ingested into the Steward System.
