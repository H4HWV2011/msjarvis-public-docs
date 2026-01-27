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

This chapter presents Ms. Jarvis as a glassbox AI Steward System and explains the Geospatial Belief Information Model underpinning its reasoning. The focus is on a rigorous, inspectable architecture for layered reasoning, memory, and judgment explicitly tied to geospatial entities, temporal context, and evidential provenance. Within Quantarithmia, Ms. Jarvis and GBIM serve as the technical realization of spatially grounded, justice‑oriented reasoning: they enable asking "What does the Steward System hold about this place, for whom, under whose authority, and based on what evidence?" with auditable, contestable answers.

---

## What GBIM Is

GBIM is Ms. Jarvis's internal model for tying beliefs to **who**, **what**, **where**, **when**, **how**, **why**, **for whom**, **under whose authority**, and **on what evidence**, focused on West Virginia and Appalachia. The current production deployment integrates three cooperating layers:

1. **PostGIS-backed regional geospatial corpus** – 204 geometry layers (5.5M features, 2GB) holding actual geometries and core attributes across census, infrastructure, environmental, and governance domains.

2. **ChromaDB collections** – High-dimensional embeddings and metadata for GIS-derived features and texts, including a consolidated `GBIM_ATTRS_CSV` index built from 227 `*_attrs` tables, plus per-layer collections for selected datasets.

3. **Production belief graph schema** – `gbim_worldview_entity`, `gbim_beliefs`, and `gbim_graph_edges` tables binding PostGIS and Chroma layers into a unified, inspectable worldview with explicit provenance.

Each belief is designed to attach to:

- **Who** – persons, institutions, communities (actors, subjects, beneficiaries, decision‑makers), keyed to GBIM entity records where available and reflected in source attributes and Chroma metadata (owner names, agencies, program sponsors).

- **What** – the kind of thing or state (asset, event, obligation, harm/benefit), represented by feature classes and layer names (`sourcetable` in `gbim.gbim_attrs` and Chroma collections) and GBIM entity types in production.

- **Where** – concrete places as PostGIS geometries (points, lines, polygons for buildings, census units, roads, districts, facilities, environmental features, community boundaries), mirrored by `bbox` and spatial tags in Chroma metadata. **Production deployment: 204 standardized datasets in SRID 26917 (UTM Zone 17N NAD83), 5,491,566 worldview entities with full spatial provenance.**

- **When** – temporal metadata indicating belief formation/update time and evidential period, drawn from source vintages, event dates, ingest timestamps, with explicit versioning via `created_at` timestamps on all entities.

- **How** – mechanisms, processes, flows (service delivery, value/risk movement, rule application), currently in governance documents and narrative texts, to be formalized as typed relationships in GBIM graph edges.

- **Why** – motives, justifications, purposes (policy rationales, program goals, safety standards), presently in text corpora and summary fields, with graph edge infrastructure prepared for structured belief relationships.

- **For whom** – distributional effects across people and places (burden/benefit allocation), approximated through spatial analyses over census blocks and block groups, planned as explicit justice metrics on GBIM entities.

- **Under whose authority** – laws, policies, institutional bodies authorizing/constraining conditions or actions, linked through jurisdictional attributes (county, municipality, district, agency) and, over time, to specific legal/policy documents.

- **On what evidence** – structured links to data sources, documents, observations, model outputs in `belief_state` JSONB fields. **Production deployment: 100% provenance coverage across all 5.5M entities, with queryable `dataset`, `geodb_id`, and `bbox` fields plus spatial metadata (centroid coordinates, SRID).**

GBIM enforces that beliefs are never free‑floating—always anchored to specific actors, kinds, geographies, time frames, mechanisms, purposes, constituencies, authorities, and evidential bases, enabling examination, challenge, and revision.

---

## How GBIM Is Represented

GBIM's target representation combines graph‑style relationships with geospatial indexing, temporal/version history, and Hilbert‑space embeddings. **The current production deployment fully implements spatial and embedding layers with operational belief entity catalog**, with graph relationships in active development.

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
Entities link via typed edges (`lives_in_block`, `served_by_911_center`, `overlaps_hazard_zone`, `regulated_by_policy`), forming a belief graph for dependency/flow/exposure analysis. **Current deployment: `gbim_graph_edges` table operational with `why` and `authority` edge types implemented; `how` and `for_whom` relationships in development.**

**Geospatial indexing**  
Each entity ties to PostGIS geometries enabling spatial operations (containment, intersection, proximity, network reachability). **Production implementation: 204 layers indexed with ST_SRID standardization (26917), bbox envelopes, and spatial indexes.** Mirrored in Chroma as `*_attrs` collections and `GBIM_ATTRS_CSV` index with `sourcetable`, `geodbid`, `label`, `bbox` fields bridging Hilbert-space queries to concrete geometries.

**Temporal and version metadata**  
Beliefs and relationships carry timestamps tracking understanding evolution. **Production deployment: all 5.5M entities timestamped via `created_at`; dataset vintages, event dates, and ingest metadata captured in source attributes.**

**Hilbert‑space embeddings**  
Entities mapped to high‑dimensional vectors in ChromaDB. **Production implementation: GIS attributes from 227 `*_attrs` tables embedded in consolidated `GBIM_ATTRS_CSV` collection**, plus selected per-layer collections. Each vector carries metadata (`sourcetable`, feature identifiers, spatial tags) providing semantic/geometric neighborhood structure for similarity-based retrieval and clustering.

### Current State

Any entity the Steward System reasons about is:

1. **A spatial object in PostGIS** – One of 5.5M features in `gbim.gbim_attrs`, identified by `sourcetable` and `geodbid`.

2. **A worldview entity with provenance** – One of 5,491,566 records in `gbim_worldview_entity` with structured `belief_state` containing confidence, dataset provenance, and spatial metadata.

3. **A vector in Hilbert space (Chroma)** – Carrying `sourcetable`, `geodbid`, and metadata linking back to GIS layers and evidence.

**Production provenance example:**

``sql
-- Query the evidence for any entity
SELECT 
    source_table,
    label,
    belief_state->'provenance' AS evidence
FROM gbim_worldview_entity
WHERE source_table = 'wvgistcbuildingfootprints'
LIMIT 3;

-- Returns structured provenance:
-- {"bbox": {"crs": {"type": "name", "properties": {"name": "EPSG:26917"}}, 
--   "type": "Point", "coordinates": [518670.34845000063, 4307829.860150001]}, 
--   "dataset": "wvgistcbuildingfootprints", "geodb_id": 1703912}

As the GBIM schema has matured, these layers have converged: worldview_id provides stable identifiers across PostGIS (gbim_worldview_entity), Chroma metadata, and belief tables; graph relationships are partially materialized with why and authority edges implemented; and provenance fields make "on what evidence" first‑class and queryable for every belief.

#### Production deployment statistics (January 2026):

   5,491,566 worldview entities
   204 source datasets
   100% provenance coverage
   100% spatial metadata coverage
   SRID 26917 (UTM Zone 17N NAD83) standardization
