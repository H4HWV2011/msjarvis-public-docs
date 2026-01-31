> **Why this matters for Polymathmatic Geography**  
> This chapter makes Polymathmatic Geography operational by specifying how a Steward System can hold beliefs explicitly tied to **who**, **what**, **where**, **when**, **how**, **why**, **for whom**, **under whose authority**, and **on what evidence**. It directly supports:  
> - **P1 – Every where is entangled** by representing legal, economic, infrastructural, social, and spiritual facts about Appalachia as a unified, structured belief space rather than disconnected layers.  
> - **P3 – Power has a geometry** by encoding dependencies, exposures, and flows as graph and spatial relationships between entities and regions.  
> - **P5 – Design is a geographic act** by treating schemas, APIs, and guards as design choices that reshape how institutions "see" their territory and act within it.  
> - **P12 – Intelligence with a ZIP code** by binding Ms. Jarvis's cognition to specific West Virginia and Appalachian geographies through GBIM.  
> - **P16 – Power accountable to place** by requiring that beliefs be inspectable, contestable, and traceable to concrete evidence about particular communities.  
> This chapter defines the **Computational Instrument** tier: the core representational machinery that enforces and audits Quantarithmia's spatial‑justice commitments in a live system.

## Ms. Jarvis and the Geospatial Belief Information Model (GBIM)

Within **polymathmatic geography**, Ms. Egeria Jarvis is a bounded, bio‑inspired Steward System whose beliefs are explicitly anchored in place, time, and evidence. **GBIM** (Geospatial Belief Information Model) is the core layer tying Ms. Jarvis's reasoning to concrete geographies in West Virginia and Appalachia, implemented as a **Generalized Bio‑inspired Machine** design.

This chapter presents Ms. Jarvis as a glassbox AI Steward System and explains the Geospatial Belief Information Model underpinning its reasoning. The focus is on a rigorous, inspectable architecture for layered reasoning, memory, and judgment explicitly tied to geospatial entities, temporal context, and evidential provenance. Within Quantarithmia, Ms. Jarvis and GBIM serve as the technical realization of spatially grounded, justice‑oriented reasoning: they enable asking "What does the Steward System hold about this place, for whom, under whose authority, and based on what evidence?" with auditable, con!
testable answers.

---

## What GBIM Is
<div align="center">
  <img width="60%" alt="geospatial belief information model" src="https://github.com/user-attachments/assets/331685c5-977e-4b60-9a96-3150b71787a2" />
</div>

>> Figure 1. High‑level structure of the Geospatial Belief Information Model (GBIM), showing the PostGIS geospatial corpus, Chroma semantic collections, and the production belief graph schema, all tied together by nine epistemic axes (who, what, where, when, how, why, for whom, under whose authority, on what evidence).

GBIM is Ms. Jarvis's internal model for tying beliefs to **who**, **what**, **where**, **when**, **how**, **why**, **for whom**, **under whose authority**, and **on what evidence**, focused on West Virginia and Appalachia. The current production deployment integrates three cooperating layers:

1. **PostGIS-backed regional geospatial corpus** – 204 geometry layers (5.5M features, 2GB) holding actual geometries and core attributes across census, infrastructure, environmental, and governance domains.

2. **ChromaDB collections** – High-dimensional embeddings and metadata for GIS-derived features and texts, including a consolidated `GBIM_ATTRS_CSV` index built from 227 `*_attrs` tables, plus per-layer collections for selected datasets.

3. **Production belief graph schema** – `gbim_worldview_entity`, `gbim_beliefs`, and `gbim_graph_edges` tables binding PostGIS and Chroma layers into a unified, inspectable worldview with explicit provenance.

Each belief attaches to all nine epistemic axes:

<div align="center">
  <img width="60%" alt="Belief Neighborhood for One Building" src="https://github.com/user-attachments/assets/9855f916-dadd-46af-8276-60e797549932" />
</div>

>> Figure 2. The nine epistemic axes in GBIM, showing how every belief is anchored simultaneously in actors, kinds, places, time, mechanisms, purposes, constituencies, authorities, and evidence.

- **Who** – persons, institutions, communities (actors, subjects, beneficiaries, decision‑makers), keyed to GBIM entity records and reflected in source attributes and Chroma metadata (owner names, agencies, program sponsors).

- **What** – the kind of thing or state (asset, event, obligation, harm/benefit), represented by feature classes (`entity_type`) and layer names (`sourcetable` in `gbim.gbim_attrs`).

- **Where** – concrete places as PostGIS geometries (points, lines, polygons for buildings, census units, roads, districts, facilities, environmental features, community boundaries). **Production deployment: 204 standardized datasets in SRID 26917 (UTM Zone 17N NAD83), 5,491,566 worldview entities with full spatial provenance.**

- **When** – temporal metadata indicating belief formation/update time and evidential period. **Production deployment: all 5.5M entities timestamped via `created_at`; dataset vintages, event dates, and ingest metadata captured in source attributes.**

- **How** – mechanisms, processes, flows (service delivery, value/risk movement, rule application). **Production deployment: 5,491,566 `how` edges linking each entity to its source dataset, documenting data collection method and provenance trail.**

- **Why** – motives, justifications, purposes (policy rationales, program goals, safety standards). **Production deployment: 2,121,230 `why` edges linking beliefs to their feature references.**

- **For whom** – distributional effects across people and places (burden/benefit allocation). **Production deployment: 5,491,566 `for_whom` edges linking entities to beneficiary geographies—census blocks linked to themselves (residents as beneficiaries), infrastructure and buildings linked to "west_virginia_public" (general community benefit).**

- **Under whose authority** – laws, policies, institutional bodies authorizing/constraining conditions or actions. **Production deployment: 2,121,230 `authority` edges linking beliefs to authorizing worldviews.**

- **On what evidence** – structured links to data sources, documents, observations, model outputs in `belief_state` JSONB fields. **Production deployment: 100% provenance coverage across all 5.5M entities, with queryable `dataset`, `geodb_id`, and `bbox` fields plus spatial metadata (centroid coordinates, SRID).**

GBIM enforces that beliefs are never free‑floating—always anchored to specific actors, kinds, geographies, time frames, mechanisms, purposes, constituencies, authorities, and evidential bases, enabling examination, challenge, and revision.

---

## How GBIM Is Represented

GBIM's representation combines graph‑style relationships with geospatial indexing, temporal/version history, and Hilbert‑space embeddings. **The current production deployment fully implements all four core layers.**

### Schema Layer

GBIM defines **entities**—places, infrastructures, events, policies, institutions, persons, communities—and their relationships:

- **`gbim.gbim_attrs` table** – Production workhorse holding 5.5M features from 204 datasets with fields: `sourcetable`, `geodbid`, `label`, `country`, `bbox`, `geom` (SRID 26917), `attrs_json`. This table provides the concrete entity catalog.

- **`gbim_worldview_entity` table (PRODUCTION)** – Holds 5,491,566 entities from 204 datasets with fields: `id` (UUID PK), `worldview_id`, `entity_type`, `source_table`, `source_pk`, `label`, `belief_state` (JSONB), `created_at`. Each entity is explicitly tied to a worldview context and contains structured provenance.

- **`belief_state` field (POPULATED)** – JSONB structure containing:
  - **`confidence`**: Numeric value (1.0 for all current production entities)
  - **`provenance`**: Object with `dataset` (sourcetable), `geodb_id`, and `bbox` (GeoJSON point with coordinates in EPSG:26917)
  - **`spatial_metadata`**: Object with `centroid_x`, `centroid_y`, and `srid` (26917 - UTM Zone 17N NAD83)

- **`gbim.mv_infrastructure_summary` materialized view** – Optimized for ChromaDB integration, extracting `geodbid`, `sourcetable`, `label`, centroid coordinates, and `search_text` from `gbim_attrs`.

### Integrated Layers

**Graph relationships**  
Entities link via typed edges forming a belief graph for dependency/flow/exposure analysis. **Production deployment: `cakidd.gbim_graph_edges` table operational with all four edge types:**

- **`how` edges (5,491,566)**: Link each entity to its source dataset, documenting the data collection method and provenance trail
- **`why` edges (2,121,230)**: Link beliefs to their feature references  
- **`for_whom` edges (5,491,566)**: Link entities to beneficiary geographies—census blocks linked to themselves (residents as beneficiaries), infrastructure and buildings linked to "west_virginia_public" (general community benefit)
- **`authority` edges (2,121,230)**: Link beliefs to authorizing worldviews

**Concrete example: A single building's belief neighborhood**
<div align="center">
  <img width="55%" alt="Building Belief Neighborhood Graph" src="https://github.com/user-attachments/assets/7577b4a2-f7f8-44b6-8c1c-c587d0da50e4" />
</div>

>> Figure 3. Belief neighborhood for a single building footprint (feat_1703912), showing how GBIM links the entity to its dataset (how), beneficiary community (for_whom), and authorizing worldview (authority). All nodes and edges carry provenance and spatial metadata.

This neighborhood is queryable via SQL:
``sql
-- Find all edges for a specific building
SELECT 
    e.source_table,
    e.label,
    g.role,
    g.target_ref,
    g.target_kind
FROM public.gbim_worldview_entity e
JOIN cakidd.gbim_graph_edges g ON g.belief_ref = e.id::text
WHERE e.source_table = 'wvgistcbuildingfootprints'
  AND e.label = 'feat_1703912'
ORDER BY g.role;

-- Returns:
-- authority | 002c2c84-2f18-40b7-8a98-b8d813dd6cc7 | worldview
-- for_whom  | west_virginia_public | community
-- how       | wvgistcbuildingfootprints | dataset

The GBIM schema has matured to production readiness: worldview_id provides stable identifiers across PostGIS (gbim_worldview_entity), Chroma metadata, and belief tables; graph relationships materialize how, why, for whom, and under whose authority as queryable edges; and provenance fields make on what evidence first‑class and inspectable for every belief.

Production deployment statistics (January 2026):

   - 5,491,566 worldview entities

   - 204 source datasets

   - 100% provenance coverage (all entities have belief_state with dataset, geodb_id, bbox, spatial_metadata)

   - 100% spatial metadata coverage (centroid coordinates, SRID 26917)

   - 100% graph edge coverage (all entities have how and for_whom edges)

   - SRID 26917 (UTM Zone 17N NAD83) standardization across all geometries

