> **Why this matters for Polymathmatic Geography**  
> This chapter defines the spatial “body” of Ms. Jarvis and shows how West Virginia’s physical infrastructures, hazards, civic facilities, and benefits‑related sites become part of a living, computable geography. It supports:  
> - **P1 – Every where is entangled** by treating structures, rivers, floodplains, institutions, and program sites as one connected mesh rather than isolated map layers.  
> - **P3 – Power has a geometry** by making it possible to trace how risk, access, infrastructure, and access‑to‑help are distributed across counties, hollows, ZIPs, and corridors.  
> - **P5 – Design is a geographic act** by framing schema choices, key conventions, RAG routing, and layer prioritization as design decisions that reshape how the state “shows up” in analysis and governance.  
> - **P12 – Intelligence with a ZIP code** by binding Ms. Jarvis’s reasoning to a concrete, statewide PostGIS geodatabase, a verified local‑resources registry keyed by ZIP and county, and their Chroma‑mirrored embeddings, especially the consolidated `gbim_worldview_entities` and `gis_wv_benefits` collections.  
> - **P16 – Power accountable to place** by ensuring that advisory and governance behaviors can be traced back to specific, queryable features, facilities, and program footprints in West Virginia, with logged retrieval paths from GeoDB and `local_resources` into the RAG and ensemble stack.  
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the GeoDB substrate that allows Quantarithmia’s justice‑oriented reasoning to act on real communities, infrastructures, and landscapes in Appalachia, and to route real households to concrete, locally valid help.

## 6. GeoDB and the Spatial Body of Ms. Jarvis

### 6.1 Purpose and Scope

This chapter describes the geospatial substrate that anchors Ms. Egeria Jarvis in the physical world of West Virginia. The GeoDB layer is tightly coupled to GBIM, to the Chroma‑based Hilbert space accessed via text and GIS RAG services, and to the local‑resources registry, so that beliefs and narratives are grounded not only in abstract embeddings but also in specific buildings, river reaches, floodplains, mines, benefits hubs, and infrastructure corridors. The focus here is on the structure and status of the PostGIS‑based geodatabase and its relationship to ChromaDB collections and RAG flows, not on exhaustive cataloging of every possible dataset. Figure 6.1 summarizes the main containers and data stores involved in this spatial body.

<img src="https://github.com/user-attachments/assets/10927cf5-f1df-455e-b4d9-7eb560d62375"
     alt="Ms. Jarvis Geospatial System Architecture"
     width="1376" />

>>- Figure 6.1. High‑level container‑style view of the Ms. Jarvis Steward System, showing user clients, the 21‑LLM >>ensemble, and the containerized backing stores (PostGIS GeoDB, GBIM, ChromaDB, local_resources, Redis, Neo4j). The >>diagram emphasizes PostGIS as the spatial backbone, GBIM as the worldview and belief layer, and Chroma collections >>(gbim_worldview_entities, gis_wv_benefits, geodb*) as the primary spatial memory in Hilbert space.


Within the Quantarithmia program, GeoDB provides the spatial backbone of Ms. Jarvis’s “body”: a coherent, queryable mesh of features and boundaries for reasoning about risk, access, infrastructure, and spatial justice. In the current deployment, this spatial backbone runs as part of a containerized microservice stack orchestrated with Docker Compose, alongside core services such as ChromaDB, Redis, Neo4j, the local‑resources Postgres instance, and the 21‑LLM ensemble. The chapter documents what is currently integrated, what is staged, and how these layers are linked into the broader Hilbert‑space and GBIM framework, including their consolidated representation in the `gbim_worldview_entities` and `gis_wv_benefits` Chroma collections and their use in `/chat/light` and `/chat/sync`.

---

### 6.2 Design Goals for the GeoDB Layer

The GeoDB layer is designed to satisfy three primary goals:

- **Coherent statewide mesh.**  
  Represent West Virginia as a coherent, queryable geospatial mesh of structures, hazards, networks, civic facilities, benefits sites, administrative boundaries, and named places.

- **Programmatic access.**  
  Provide fast, programmatic access to that mesh for reasoning, retrieval, visualization, and analytics through well‑defined schemas and APIs.

- **Integration with GBIM, Chroma, `local_resources`, and RAG.**  
  Integrate cleanly with GBIM, Chroma, and the local‑resources registry so that spatial, semantic, institutional, and program dimensions can be used together in a single reasoning pipeline.

In practice, this means maintaining a PostGIS‑backed geodatabase that holds authoritative feature classes for core themes and, for prioritized subsets, mirroring those features into vector collections. Historically, this mirroring used many `geodb*` and `gedb*` collections in ChromaDB; as of early 2026, the primary spatial memory index is the unified `gbim_worldview_entities` collection, with `geodb*` collections serving as thematic and historical subsets, and `gis_wv_benefits` capturing benefits‑focused facilities.

---

### 6.3 PostGIS as Ms. Jarvis’s Spatial Backbone

At the storage level, Ms. Jarvis uses a PostGIS database (for example, `msjarvis_gis`) as the main container for West Virginia vector datasets. This PostGIS instance runs as one of the shared backing stores in the live Docker Compose stack, alongside ChromaDB, Redis, MySQL, Neo4j, and the local‑resources Postgres, and is accessed by multiple services for spatial reasoning and data access.

Feature classes are organized by theme and provenance—census units, structure points, building footprints, hydrology, transportation networks, hazards, facilities, and benefits‑related sites—with consistent naming and key conventions.

The core production schema includes:

- Raw and normalized source tables for individual datasets (for example, county boundaries, blocks, dams, hospitals).  
- A consolidated attribute table (`gbim.gbim_attrs`) that flattens attributes from 204 statewide datasets into a single, indexed catalog keyed by `sourcetable` and `geodbid`.  
- GBIM worldview entities (`public.gbim_worldview_entity`) that bind spatial features to belief state, provenance, and worldview context.

The majority of production layers share a common projected coordinate system, SRID 26917 (UTM Zone 17N NAD83). Legacy tables that retain provisional SRIDs, mixed geometry types, or inconsistent precision are explicitly flagged in a schema registry for cleanup.

The database is populated from state and federal sources including the WV GIS Technical Center, USGS, the U.S. Census Bureau, USACE, NREL, and various state agencies. Ingestion converts shapefiles and file geodatabases into PostGIS tables, resolves geometry and projection issues, and normalizes keys so that features can be cross‑referenced from GBIM, Chroma, `local_resources`, and higher‑level reasoning services. Ingestion and transformation steps are scripted and versioned so that table structures and provenance can be audited.

---

### 6.4 Currently Integrated Statewide Layers

The current deployment includes a substantial, production‑usable subset of West Virginia’s public geospatial data, with additional layers actively being integrated. At a high level, the Steward System already has:

- **Census units.**  
  Statewide 2020 Census blocks and block groups in projected coordinate systems suitable for analysis and mapping. Representative tables include:
  - blocks tables with statewide 2020 block coverage,  
  - block group tables with polygons at neighborhood and community scales.

- **Structures and buildings.**  
  A dense statewide structure inventory combining:
  - SAMB structure points (north and south) for large numbers of structures across northern and southern counties,  
  - WV GIS Technical Center building footprints numbering in the millions,  
  - Microsoft building point datasets contributing additional building‑like points.

- **Hazard and infrastructure layers.**  
  Datasets such as:
  - abandoned mine lands (lines and polygons),  
  - dams (coal‑ and non‑coal‑related) from Army Corps and USGS,  
  - floodplain structure inventories,  
  - rail networks and associated facilities,  
  - navigable waterways and river mile indexing,  
  - energy and communication infrastructure where available.

- **Civic, facility, and benefits coverage.**  
  Layers representing:
  - hospitals, nursing homes, and other healthcare facilities,  
  - fire and police stations and 911 centers,  
  - higher‑education campuses,  
  - libraries and community centers,  
  - parks and recreational areas,  
  - solid waste sites, sewer plants, and related utilities,  
  - benefits‑relevant facilities such as DHHR offices, community action agencies, and local hubs (modeled both as GeoDB features and as GBIM entities referenced by `gis_wv_benefits`).

- **Governance and index layers.**  
  Tables capturing:
  - county and state boundaries,  
  - ZIP Code Tabulation Areas and related postal geography,  
  - regional planning council boundaries and similar governance regions,  
  - named places, summits, and other geographic names,  
  - National Register points and polygons and other historic resources.

Across these themes, the production GBIM/GeoDB deployment integrates on the order of 5.5 million features from 204 standardized datasets into `gbim.gbim_attrs` and `gbim_worldview_entity`. Exact feature counts and table names are recorded in database inventories maintained alongside this thesis, so that claims about coverage can be verified and updated as ingestion continues. Figure 6.2 summarizes these themes at a glance.

<img src="https://github.com/user-attachments/assets/cff5cc65-84e2-402d-aa53-07ada47b57d9"
     alt="GeoDB and the Spatial Body of Ms. Jarvis"
     width="1376" />

>>- Figure 6.2. Conceptual overview of the statewide geospatial mesh maintained in GeoDB and GBIM, summarizing integrated >>census units, structures, hazards, civic facilities, governance layers, and benefits‑relevant sites. The current >>deployment integrates on the order of 5.5 million features from 204 standardized datasets into gbim.gbim_attrs and >>gbim_worldview_entity.

---

### 6.5 Chroma Spatial Collections and GeoDB Mirrors

To bridge geometric features and high‑dimensional semantic reasoning, Ms. Jarvis maintains spatially derived collections in ChromaDB. Figure 6.3 illustrates how these identifiers link GeoDB, GBIM, and Chroma.

<img src="https://github.com/user-attachments/assets/323dd7de-aef9-4019-b703-22ea667e6175"
     alt="West Virginia Data Architecture Flow"
     width="1376" />

>>- Figure 6.3. Key relationships between GeoDB source tables, GBIM attribute and worldview entities (gbim.gbim_attrs, >>gbim_worldview_entity), and the gbim_worldview_entities and gis_wv_benefits Chroma collections. Deterministic joins are >>maintained via sourcetable/geodbid from GeoDB into GBIM and via entity_id and source_table/source_pk from Chroma back >>to GBIM and GeoDB.


As of early 2026, there are two main patterns:

- **Unified worldview collection.**  
  The `gbim_worldview_entities` collection is the primary spatial memory index. It contains roughly 6.1M records representing 5.49M worldview entities from 204 datasets, with the great majority of records enriched with `worldview_id`, `bbox`, and `dataset` metadata. Each record includes:
  - a textual document of the form `{source_table} {label}`,  
  - an `entity_id` UUID linking to `gbim_worldview_entity.id`,  
  - `source_table` and `source_pk` fields that join back to `gbim.gbim_attrs`,  
  - centroid coordinates and spatial metadata in SRID 26917.

- **Legacy and thematic `geodb*` / `gedb*` collections.**  
  Earlier in the project, many PostGIS layers were mirrored into `geodb*` collections, with corresponding `gedb*` aliases for compatibility. These collections:
  - store embeddings derived from feature‑level descriptions and attributes,  
  - carry compact metadata including stable feature identifiers and source table references,  
  - support thematic or experimental RAG over specific layers (for example, dams, hospitals, ZIPs, or energy infrastructure).

In the current architecture, new spatial RAG and stewardship behaviors are expected to use `gbim_worldview_entities` as the canonical spatial collection. The `geodb*` and `gedb*` collections remain available as historical snapshots, thematic subsets, or specialized indexes where a narrower semantic context is beneficial.

Regardless of collection, identifiers are designed so that Chroma results can be deterministically rejoined to PostGIS:

- `entity_id` ↔ `gbim_worldview_entity.id` for worldview entities;  
- `source_table` / `source_pk` ↔ `gbim.gbim_attrs.sourcetable` / `geodbid` for underlying features.

This join pattern allows Ms. Jarvis to retrieve full geometries and attributes for any spatial item surfaced through vector search.

---

### 6.6 Staged and Partially Integrated Layers

Not every dataset present on disk or in PostGIS is fully integrated into the live geospatial reasoning stack. Several classes of layers are staged or partially integrated:

- **Legacy and irregular schemas.**  
  Some older datasets required schema adjustments and numeric precision fixes before they could be reliably imported. Many have now been cleaned and loaded; a smaller tail of legacy layers remains flagged for further work and is excluded from GBIM and `gbim_worldview_entities` until normalized.

- **Specialized and high‑volume layers.**  
  Certain HSIP‑derived or specialized layers have encountered type mismatches or throughput constraints during bulk operations. These layers may exist in PostGIS with provisional keys or geometry columns but are not yet mirrored into `gbim_worldview_entities` or dedicated `geodb*` collections with full embeddings and standardized metadata.

- **Additional WVU and federal/state layers.**  
  Additional datasets reside on SSD‑backed working storage and in PostGIS but have not yet been embedded into Chroma with consistent identifier schemes and metadata. They are tracked in ingestion plans and marked as “staged” rather than fully live.

For these datasets, the accurate description is that they are present and often queryable in PostGIS, but are not yet part of the default geospatial reasoning path that the Hilbert‑space RAG, GBIM, and benefits pipelines use. Their eventual integration will follow the same key‑normalization, embedding, and worldview‑binding patterns used for `gbim_worldview_entities`.

---

### 6.7 Linking GeoDB to GBIM, `local_resources`, and Hilbert Space

Within the broader GBIM framework, spatial information is one dimension of a geometric belief state that also includes semantic, temporal, institutional, and program components. GeoDB provides the concrete anchor for this spatial dimension.

- **From GeoDB to GBIM.**  
  Each row in `gbim.gbim_attrs` corresponds to a concrete feature in a source dataset, with `sourcetable`, `geodbid`, `label`, `geom`, and bounding‑box metadata. GBIM’s `gbim_worldview_entity` table wraps these features in worldview context and belief state, adding `worldview_id`, `entity_type`, timestamps, and structured provenance.

- **From GBIM to Hilbert space via Chroma.**  
  The `gbim_worldview_entities` collection embeds each worldview entity into a 384‑dimensional text space and attaches spatial metadata and identifiers. Together with other semantic and institutional collections, this collection realizes a large finite subset of the geospatial component \(H_{\text{geo}}\) and its linkage into \(H_{\text{App}}\), the overall Hilbert‑space state.

- **From spatial facilities to programs.**  
  Benefits‑relevant facilities (for example, DHHR offices or community action agencies) appear both as GBIM entities (and thus as GeoDB features and Chroma vectors) and as anchors for entries in the `local_resources` registry. Spatial joins (for example, parcels → ZIP → county → facility catchments) connect households to both physical sites and program records.

Belief nodes that refer to places—counties, neighborhoods, structures, industrial sites, facilities, or service areas—are thus linked end‑to‑end:

1. From embeddings and metadata in Chroma (`gbim_worldview_entities`, `gis_wv_benefits`),  
2. To worldview entities and belief graphs in GBIM (`gbim_worldview_entity`, `gbim_beliefs`, `gbim_graph_edges`),  
3. Down to concrete geometries and attributes in GeoDB (`gbim.gbim_attrs` and source tables),  
4. Across to `local_resources` rows that describe programs and services tied to those places.

This linkage allows Ms. Jarvis to move fluidly among:

- **Semantic proximity.**  
  Retrieval of entities and texts that are similar in content or role (for example, dams with similar attributes and risk profiles, or facilities with similar service roles).

- **Spatial proximity.**  
  Selection of features that are geographically close or share relevant spatial relationships (for example, homes within a buffer of a floodplain boundary, or households near a benefits facility).

- **Belief‑space relationships.**  
  GBIM edges that encode causal, normative, or governance‑relevant links between spatial entities (for example, relationships between facilities and service regions, or between hazard sites and vulnerable populations).

- **Program proximity.**  
  Joins from spatial context and facility entities to structured program records in `local_resources`, which encode who is served, where, how, and under what conditions.

---

### 6.8 Geo‑Aware RAG, Benefits Flows, and Multi‑Model Use

The GeoDB layer and its Chroma mirrors play a direct role in retrieval‑augmented generation, especially for spatially explicit and benefits‑oriented queries. When a query has an explicit or implicit spatial component—references to towns, hollows, rivers, counties, facilities, or ZIPs—the RAG pipeline can: Figure 6.4 sketches the main stages of the geo‑aware RAG pipeline that underpins benefits‑oriented queries.

<img src="https://github.com/user-attachments/assets/a7e894db-fd24-4dc6-aba1-51ed4676bc79"
     alt="West Virginia Geo-Aware RAG Pipeline"
     width="1376" />

>>- 6.4. Geo‑aware retrieval‑augmented generation pipeline for benefits queries. User prompts with spatial references are >>routed through spatial filters in PostGIS, vector search over gbim_worldview_entities, gis_wv_benefits, and selected >>geodb* collections, joins to GBIM and local_resources, and finally synthesized by the multi‑model ensemble.

- Use PostGIS filters to constrain candidate features or regions (for example, `ST_Intersects` with floodplain polygons or buffers around facilities).  
- Query `gbim_worldview_entities` to retrieve semantically and spatially relevant entities, using metadata filters such as `worldview_id`, `dataset`, or `source_table`.  
- Query `gis_wv_benefits` to retrieve benefits facilities relevant to the query’s county, ZIP, or named place.  
- Where appropriate, fall back to specialized `geodb*` collections for narrow thematic retrieval.  
- Combine retrieved documents, metadata, geometries, and registry keys into context windows for language models, with filtering by collection, geography, topic, resource type, and verification status.

Different models in the Ms. Jarvis ensemble may specialize in different types of geo‑aware tasks:

- Narrative explanations for public audiences that must reference specific places, facilities, and programs.  
- Technical risk assessments that combine hazard layers, infrastructure networks, demographics, and benefit access.  
- Code‑generation models that construct spatial queries, buffers, intersections, or joins in SQL or GIS scripting languages.  
- Governance‑oriented advisors that reason about service coverage, jurisdictional responsibilities, and distributional impacts.

The GeoDB layer ensures that, regardless of which model is active, the Steward System’s answers remain grounded in specific, verifiable places and program footprints, with clear links back to underlying data, registries, and belief structures.

---

### 6.9 Roadmap for Full Statewide Integration

The near‑term roadmap for the GeoDB layer is to move from “a substantial integrated subset plus staged layers” toward a more comprehensive mirror of the state’s public geospatial infrastructure and its entanglement with GBIM, Chroma, `local_resources`, and RAG. Concretely, this entails:

- **Completing schema normalization.**  
  Cleaning up remaining geometry, SRID, and numeric precision issues in the residual set of WV GIS Technical Center and federal/state layers, and bringing them into the same SRID 26917 convention where feasible.

- **Ensuring stable keys.**  
  Verifying that all relevant vector datasets are loaded into PostGIS with stable, documented primary keys and supporting indexes, enabling consistent linkage from GBIM (`gbim_worldview_entity`, `gbim_beliefs`, `gbim_graph_edges`), Chroma (`gbim_worldview_entities`, `gis_wv_benefits`, and any remaining `geodb*` collections), and `local_resources`.

- **Maintaining worldview and metadata coverage.**  
  Continuing metadata backfills so that remaining spatial entities in `gbim_worldview_entities` receive `worldview_id`, `bbox`, `dataset`, and related fields, and ensuring that new datasets added to GeoDB are incorporated into GBIM and Chroma with consistent coverage.

- **Mirroring into Chroma.**  
  Creating or updating matching Chroma collections where necessary, and keeping `gbim_worldview_entities` and `gis_wv_benefits` as the canonical spatial and benefits vector indexes backed by clear documentation of provenance, coverage, and schema.

- **Maintaining inventories and audit trails.**  
  Periodically regenerating and archiving CSV inventories of PostGIS tables, GBIM worldview entities, Chroma collections, and `local_resources`, including feature counts and metadata coverage, so that claims about coverage and integration remain auditable over time.

As these steps are completed, Ms. Jarvis will be able to reason over an increasingly comprehensive set of statewide layers—structures, hazards, networks, demographics, benefits facilities, and more—at the scale of millions of features and entities. At that point, the spatial body of the Steward System will be mature enough to support detailed, location‑specific reasoning about risk, infrastructure, governance, benefits access, and community well‑being across West Virginia, with every advisory behavior traceable back to specific, inspectable geographies and program records.
