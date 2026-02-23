## Why this matters for Polymathmatic Geography

This chapter defines the spatial “body” of Ms. Jarvis and specifies how West Virginia’s physical infrastructures, hazards, civic facilities, and benefits‑related sites are represented as a computable geography. It supports:  
- **P1 – Every where is entangled** by treating structures, rivers, floodplains, institutions, and program sites as a connected mesh rather than isolated map layers, and by linking them to GBIM belief records and spatial embeddings derived from the current `gbimbeliefnormalized` and `gbim_worldview_entity` tables.  
- **P3 – Power has a geometry** by enabling analysis of how risk, access, infrastructure, and access‑to‑help are distributed across counties, hollows, ZIP codes, and corridors, and by exposing these distributions both through PostGIS queries and through Chroma‑backed RAG neighborhoods over collections such as `gbim_beliefs_v2` and `gis_wv_benefits`.  
- **P5 – Design is a geographic act** by framing schema choices, key conventions, CSV pipelines, RAG and `/search` routing, Chroma collection design, and layer prioritization as design decisions that reshape how the state “appears” in analysis, governance, entangled retrieval, and WV‑biased search.  
- **P12 – Intelligence with a ZIP code** by binding Ms. Jarvis’s reasoning to a concrete, statewide PostGIS geodatabase, to a verified `local_resources` registry keyed by ZIP and county, and to their Chroma‑mirrored embeddings—especially the unified GBIM belief collections (for example, `gbim_beliefs_v2`) and the `gis_wv_benefits` collection used in GIS RAG flows and the entangled `/search` endpoint.  
- **P16 – Power accountable to place** by ensuring that advisory and governance behaviors can be traced back to specific, queryable features, facilities, and programme footprints in West Virginia, with logged retrieval paths from GeoDB, GBIM, Chroma, `local_resources`, and the WV‑biased, entangled RAG path into `/search` and the ensemble stack.  

Accordingly, this chapter belongs to the **Computational Instrument** tier: it specifies the geospatial substrate that allows Quantarithmia’s justice‑oriented reasoning to operate on real communities, infrastructures, and landscapes in Appalachia and to route actual households to concrete, locally valid forms of assistance.

## 6. GeoDB and the Spatial Body of Ms. Jarvis

### 6.1 Purpose and Scope

This chapter describes the geospatial substrate that anchors Ms. Egeria Jarvis in the physical world of West Virginia. The GeoDB layer is tightly coupled to GBIM, to the Chroma‑based Hilbert space accessed via text and GIS RAG services, to the verified `local_resources` registry, and to the entangled `/search` path, so that beliefs and narratives are grounded not only in abstract embeddings but also in specific buildings, river reaches, floodplains, mines, benefits hubs, and infrastructure corridors.

The focus is on the structure and status of the PostGIS‑based geodatabase and its relationship to Chroma collections and RAG flows, rather than on exhaustive cataloguing of every dataset. Figure 6.1 summarizes the main containers and data stores involved in this spatial body.

![Ms. Jarvis Geospatial System Architecture](https://github.com/user-attachments/assets/10927cf5-f1df-455e-b4d9-7eb560d62375)

> Figure 6.1. High‑level container‑style view of the Ms. Jarvis Steward System, showing user clients, the 21‑LLM ensemble, and the containerized backing stores (PostGIS GeoDB, GBIM, ChromaDB, `local_resources`, Redis, Neo4j). The diagram emphasizes PostGIS as the spatial backbone, GBIM as the worldview and belief layer, and Chroma collections (for example, `gbim_beliefs_v2`, `gis_wv_benefits`, legacy `geodb*` collections) as the primary spatial memory in Hilbert space.

Within the Quantarithmia program, GeoDB constitutes the spatial backbone of Ms. Jarvis’s “body”: a coherent, queryable mesh of features and boundaries for reasoning about risk, access, infrastructure, and spatial justice. In the current deployment, this spatial backbone runs as part of a containerized microservice stack orchestrated with Docker Compose, alongside core services such as ChromaDB (exposed over HTTP and used as the canonical vector store), Redis, Neo4j, the `local_resources` Postgres instance, and the multi‑model ensemble.

The chapter documents what is currently integrated, which layers are staged, and how these components are linked into the broader Hilbert‑space and GBIM framework, including their representation in GBIM belief embeddings (for example, `gbim_beliefs_v2`) and the `gis_wv_benefits` Chroma collection, and their use in `/chat/light`, `/chat/sync`, the WV‑biased, entangled RAG path, and the entangled `/search` endpoint.

---

### 6.2 Design Goals for the GeoDB Layer

The GeoDB layer is designed to satisfy three primary goals:

- **Coherent statewide mesh.**  
  Represent West Virginia as a coherent, queryable geospatial mesh of structures, hazards, networks, civic facilities, benefits sites, administrative boundaries, and named places.

- **Programmatic access.**  
  Provide fast, programmatic access to this mesh for reasoning, retrieval, visualization, and analytics through well‑defined schemas, indexes, and APIs.

- **Integration with GBIM, Chroma, `local_resources`, and RAG.**  
  Integrate cleanly with GBIM, Chroma, and the `local_resources` registry so that spatial, semantic, institutional, and programme dimensions can be used together in a single reasoning pipeline, including the WV‑biased, entangled `/search` workflow.

Operationally, this entails maintaining a PostGIS‑backed geodatabase that holds authoritative feature classes for core themes and, for prioritized subsets, mirroring those features into vector collections and belief embeddings. Earlier deployments used many `geodb*` and `gedb*` collections in Chroma; in the 2026 deployment the primary spatial memory indices are the unified GBIM embedding collections (e.g., `gbim_beliefs_v2`) and the `gis_wv_benefits` collection, with legacy `geodb*` collections serving as thematic and historical subsets.

---

### 6.3 PostGIS as Ms. Jarvis’s Spatial Backbone

At the storage level, Ms. Jarvis uses a PostGIS database (for example, `msjarvisgis`) as the main container for West Virginia vector datasets. This PostGIS instance runs as one of the shared backing stores in the live Docker Compose stack, alongside ChromaDB, Redis, MySQL, Neo4j, and the `local_resources` Postgres instance, and is accessed by multiple services for spatial reasoning and data access.

Feature classes are organized by theme and provenance—census units, structure points, building footprints, hydrology, transportation networks, hazards, facilities, benefits‑relevant sites, and governance geometries—with consistent naming and key conventions across ingestion pipelines.

The core production schema includes:

- Raw and normalized source tables for individual datasets, such as county boundaries, census blocks, dams, hospitals, and other facilities.  
- A set of CSV‑derived tables (for example, `gbim_source_csv.*`) created from `*_attrs.csv` exports, which store key attributes (including `geodb_id`, `lat`, `lon`, `bbox`, `label`, `sourcetable`, `country` and, in some cases, additional fields) converted directly from shapefiles and other GIS formats.  
- GBIM‑related tables, including `gbimbeliefnormalized` (the main belief table with the nine JSONB axes) and any `gbim_worldview_entity` tables, which tie features to worldviews, belief state, and provenance.

The majority of production layers share a common projected coordinate system, SRID 26917 (UTM Zone 17N NAD83). Legacy tables that retain provisional SRIDs, mixed geometry types, or inconsistent precision are explicitly flagged in schema registries for cleanup and are not included in the primary GBIM worldview until normalized.

The database is populated from state and federal sources including the WV GIS Technical Center, USGS, the U.S. Census Bureau, USACE, NREL, and various state agencies. Ingestion converts shapefiles and file geodatabases into PostGIS tables, resolves geometry and projection issues, and normalizes keys so that features can be cross‑referenced from GBIM, Chroma, `local_resources`, and the higher‑level reasoning services. Ingestion and transformation processes are scripted and versioned to support auditability.

---

### 6.4 Currently Integrated Statewide Layers

The current deployment includes a substantial, production‑usable subset of West Virginia’s public geospatial data, with additional layers actively being integrated. At a high level, the Steward System already maintains:

- **Census units.**  
  Statewide 2020 Census blocks and block groups in projected coordinate systems appropriate for analysis and mapping, providing population and administrative meshes at fine spatial scales.

- **Structures and buildings.**  
  A dense statewide structure inventory composed of:
  - SAMB structure points in northern and southern regions,  
  - WV GIS Technical Center building footprints numbering in the millions,  
  - Microsoft‑derived building points contributing additional structure‑like locations.

- **Hazard and infrastructure layers.**  
  Datasets representing:
  - abandoned mine lands (lines and polygons),  
  - dams (coal‑related and non‑coal‑related) from Army Corps and USGS,  
  - floodplain structure inventories,  
  - rail networks and terminals,  
  - navigable waterways and river‑mile indexing,  
  - energy and communication infrastructure, where available.

- **Civic, facility, and benefits coverage.**  
  Layers capturing:
  - hospitals, nursing homes, and other healthcare facilities,  
  - fire and police stations and 911 centers,  
  - higher‑education institutions,  
  - libraries and community centers,  
  - parks and recreational sites,  
  - solid waste facilities, sewer plants, and related utilities,  
  - benefits‑relevant facilities such as state and local benefits offices, community action agencies, and local hubs, which are represented both as GeoDB features and as GBIM beliefs and are mirrored into Chroma collections such as `gis_wv_benefits`.

- **Governance and index layers.**  
  Tables representing:
  - county and state boundaries,  
  - ZIP Code Tabulation Areas and related postal geography,  
  - regional planning districts and similar governance regions,  
  - named places, summits, and other geographic names,  
  - National Register points and polygons and related historic resources.

Across these themes, the GBIM/GeoDB deployment integrates millions of features from approximately two hundred statewide datasets. Feature counts and table names are catalogued in database inventories maintained alongside the system and can be updated as additional layers are ingested or normalized.

![GeoDB and the Spatial Body of Ms. Jarvis](https://github.com/user-attachments/assets/cff5cc65-84e2-402d-aa53-07ada47b57d9)

> Figure 6.2. Conceptual overview of the statewide geospatial mesh maintained in GeoDB and GBIM, summarizing integrated census units, structures, hazards, civic facilities, governance layers, and benefits‑relevant sites. The present deployment integrates millions of features from on the order of two hundred standardized datasets into the GBIM corpus.

---

### 6.5 Chroma Spatial Collections and Geo‑Referenced Beliefs

To bridge geometric features and high‑dimensional semantic reasoning, Ms. Jarvis maintains Chroma collections derived from GBIM beliefs and spatial entities. These collections are hosted in a shared HTTP‑backed Chroma instance, configured with 384‑dimensional embeddings, and serve as the canonical spatial memory layer for RAG and `/search`.

![West Virginia Data Architecture Flow](https://github.com/user-attachments/assets/323dd7de-aef9-4019-b703-22ea667e6175)

> Figure 6.3. Key relationships between GeoDB source tables, GBIM beliefs (`gbimbeliefnormalized`), worldview entities (where present), and Chroma collections such as `gbim_beliefs_v2` and `gis_wv_benefits`. Deterministic joins are maintained via `identity` fields (for example, `source_table` and `source_pk`) from Chroma back into GBIM and GeoDB.

The current pattern is as follows:

- **Unified GBIM belief collections.**  
  Collections such as `gbim_beliefs_v2` embed rows from `gbimbeliefnormalized`. For each belief, a text representation is constructed from the JSONB axes (`identity`, `what`, `where`, `who`, `for_whom`, `why`, `how`, `authority`, `when`), and embeddings are stored with metadata including:
  - the belief identifier (for example, `id` from `gbimbeliefnormalized`),  
  - `source_table` and `source_pk` values drawn from the `identity` axis,  
  - epoch information derived from the `when` axis,  
  - optional spatial metadata inherited from `where`.

  This provides a unified embedding space over the entire GBIM corpus, reflecting both institutional and feature‑level information derived from the CSVs.

- **Benefits‑focused spatial collection.**  
  The `gis_wv_benefits` collection stores embeddings and metadata for benefits‑relevant facilities, built from GBIM beliefs and resource descriptions. Documents in this collection encode facility names, locations, roles, and linkages to `local_resources` identifiers, enabling semantically and spatially aware retrieval of benefits sites.

- **Legacy and thematic `geodb*` collections.**  
  Earlier deployments mirrored selected PostGIS layers into `geodb*` collections, with each record representing a feature‑level description and minimal metadata to enable thematic or experimental RAG over specific layers (for example, dams or hospitals). These collections remain available as historical or specialized indexes but are no longer treated as the primary spatial memory layer; new work prefers the GBIM belief collections and `gis_wv_benefits`.

Identifiers and metadata are defined so that Chroma results can be rejoined deterministically to GBIM and GeoDB:

- Belief embeddings carry an `id` field that maps to `gbimbeliefnormalized.id`.  
- Metadata include `source_table` and `source_pk` fields that can be aligned with source tables or attribute tables (for example, `gbim_source_csv.*`) and, where applicable, with geometries in the geodatabase.

This join pattern allows retrieval pipelines to move from vector search results in Chroma to full geometries, attributes, and belief‑graph context in Postgres.

---

### 6.6 Staged and Partially Integrated Layers

Not every dataset present on disk or in PostGIS is fully integrated into the live geospatial reasoning stack. Several categories of layers are staged or partially integrated:

- **Legacy and irregular schemas.**  
  Some older datasets present challenges such as inconsistent geometry types, missing SRIDs, or non‑standard key fields. Many have been cleaned and integrated; a residual group remains flagged for additional preparation and is not yet included in GBIM‑based embeddings or in the default RAG path.

- **Specialized and high‑volume layers.**  
  Selected layers with particularly high feature counts or specialized schemas may reside in PostGIS with provisional structures but await full integration into GBIM embeddings and Chroma collections. These layers may still be available for targeted spatial analysis but do not participate in the standard GBIM → text → Chroma pipeline.

- **New and externally sourced datasets.**  
  Additional state and federal datasets, including recent updates and thematic additions, are stored on local media and in PostGIS schemas pending normalization and key alignment. Their integration is planned following the established patterns of identity, epoch mapping, and embedding.

For these datasets, the accurate characterization is that they are present and, in many cases, spatially queryable in PostGIS, but are not yet part of the default GBIM‑driven Hilbert‑space reasoning path used by the RAG and `/search` services.

---

### 6.7 Linking GeoDB to GBIM, `local_resources`, and Hilbert Space

Within the GBIM framework, spatial information constitutes one dimension of a multi‑axis geometric belief state that also includes semantic, temporal, institutional, and programmatic components.

- **From GeoDB and CSVs into GBIM.**  
  Each feature represented in CSV‑derived tables (for example, `gbim_source_csv.*`) and in geospatial source tables is associated with GBIM beliefs via identity keys. Enrichment scripts use `COALESCE` over `source_table` and `source_pk` variants to join `gbimbeliefnormalized` to these attributes, updating the `what` and `where` axes to incorporate fields such as latitudes, longitudes, labels, and selected family‑specific attributes.

- **From GBIM beliefs to Hilbert space via embeddings.**  
  The `msjarvis_embed_gbim.py` script generates text representations for each belief, combining the nine axes into a summary sentence and embedding them into Chroma collections such as `gbim_beliefs_v2`. This realizes a large finite subset of the spatial and institutional component of the overall Hilbert space, allowing semantic traversal over beliefs that remain grounded in concrete geospatial and institutional facts.

- **From spatial facilities to programme records.**  
  Benefits‑relevant facilities—such as state offices, local hubs, and community organizations—are represented as GBIM beliefs linked to geometries and as entries in the `local_resources` registry. Spatial joins (for example, parcels → ZIP → county → facility catchments) and key relationships (for example, between facility beliefs and registry identifiers) connect households to both physical sites and programme descriptions.

As a result, a belief that refers to a place—whether a county, neighborhood, structure, industrial site, facility, or service area—is linked via a coherent chain:

1. From embeddings and metadata in Chroma (for example, in `gbim_beliefs_v2` and `gis_wv_benefits`),  
2. To JSONB axes and identity keys in `gbimbeliefnormalized`,  
3. To source attributes and geometries in PostGIS and CSV‑derived tables,  
4. To `local_resources` rows describing programmes and services tied to that place.

This linkage allows the Steward System to traverse:

- **Semantic proximity**, retrieving entities and texts that share conceptual similarity;  
- **Spatial proximity**, identifying features that are geographically close or spatially related;  
- **Belief‑space relationships**, reasoning over institutional and normative structures encoded in GBIM;  
- **Program proximity**, resolving beliefs and facilities to concrete programme records with coverage, contact, and verification information.

---

### 6.8 Geo‑Aware RAG, Benefits Flows, and Multi‑Model Use

The GeoDB layer and its GBIM/Chroma mirrors play a direct role in retrieval‑augmented generation, particularly for spatially explicit and benefits‑oriented queries. When a query includes spatial references—such as towns, hollows, counties, rivers, ZIP codes, or named facilities—the RAG pipeline can invoke geo‑aware paths.

![West Virginia Geo-Aware RAG Pipeline](https://github.com/user-attachments/assets/a7e894db-fd24-4dc6-aba1-51ed4676bc79)

> Figure 6.4. Geo‑aware retrieval‑augmented generation pipeline for benefits queries. Prompts with spatial references are routed through spatial filters in PostGIS, vector search over GBIM and benefits collections in Chroma, joins to GBIM and `local_resources`, and finally into the multi‑model ensemble and the entangled `/search` context builder.

For spatial and benefits questions, the system can:

- Apply PostGIS filters (for example, `ST_Intersects` with floodplain polygons, buffers around facilities, or membership in administrative boundaries) to constrain candidate features.  
- Query GBIM belief collections in Chroma to retrieve semantically and spatially relevant beliefs, using metadata filters such as `source_table`, `epoch`, or structured tags in the JSONB axes.  
- Query `gis_wv_benefits` to retrieve benefits facilities relevant to a specified county, ZIP, or named place, using metadata such as facility type and location.  
- Incorporate local resource entries by joining facility beliefs and ZIP/county data to `local_resources`, filtered by programme type and verification status.  
- Assemble retrieved texts, beliefs, geometries, and programme records into context windows for language models, with selection constrained by geography, dataset, resource type, and other metadata.

The entangled `/search` endpoint extends this paradigm by accepting a `wv_entangled_context` envelope (for example, containing domains, principles, GBIM entities, GeoDB features, and target collections). It performs multi‑collection Chroma queries, logs raw similarity scores, applies WV‑specific biasing to favour relevant datasets and regions, and returns a globally ranked result set that feeds the ensemble models.

Different models within the ensemble specialize in tasks such as:

- Public‑facing narrative explanations that reference specific places, facilities, and programmes;  
- Technical analyses of risk that combine hazards, infrastructure, demographics, and benefit access;  
- Code generation for spatial queries in SQL or GIS scripting languages;  
- Governance‑focused advice concerning service coverage, jurisdictional responsibilities, and distributional impacts.

The GeoDB and GBIM layers ensure that, in all cases, outputs remain grounded in specific locations and programme footprints with explicit provenance, enabling post‑hoc inspection of which datasets, beliefs, and registry rows were consulted.

---

### 6.9 Roadmap for Full Statewide Integration

A key near‑term objective for the GeoDB layer is to extend the current “substantial integrated subset plus staged layers” into a more comprehensive mirror of West Virginia’s public geospatial infrastructure and its entanglement with GBIM, Chroma, `local_resources`, and RAG. This roadmap includes:

- **Completing schema normalization.**  
  Resolving remaining geometry, SRID, and numeric precision issues in legacy WV GIS Technical Center and federal/state layers, and adopting the common SRID 26917 convention wherever feasible.

- **Ensuring stable keys and identity alignment.**  
  Confirming that all relevant vector datasets are loaded into PostGIS with stable, documented primary keys and that identity mappings in `gbimbeliefnormalized` correctly reference these sources via `source_table` and `source_pk`, including both historical and current naming conventions.

- **Maintaining coverage in GBIM and embeddings.**  
  Ensuring that beliefs associated with newly normalized datasets receive complete axis values, text representations, and embeddings in collections such as `gbim_beliefs_v2`, and that their spatial and institutional metadata are exposed for RAG and `/search`.

- **Consolidating and documenting Chroma collections.**  
  Treating GBIM belief collections and `gis_wv_benefits` as the primary spatial and benefits vector indexes, with legacy `geodb*` collections documented as historical or specialized. New or updated collections follow clearly documented schemas and provenance practices.

- **Extending the local resource registry.**  
  Continuing to ingest and normalize programme information into `local_resources`, extending coverage across additional West Virginia counties and ZIP codes, and maintaining verification status and timestamps so that the Steward System can reason about the freshness and reliability of programme data.

- **Maintaining inventories and audit trails.**  
  Periodically regenerating and archiving inventories of PostGIS tables, GBIM beliefs, Chroma collections, and `local_resources` entries, including counts and metadata coverage, to ensure that the spatial body of Ms. Jarvis remains transparent and auditable.

As these milestones are met, Ms. Jarvis will be able to reason over an increasingly comprehensive set of statewide layers—structures, hazards, networks, demographics, benefits facilities, and more—at the scale of millions of entities. The spatial body of the Steward System will thereby support detailed, location‑specific reasoning about risk, infrastructure, governance, benefits access, and community well‑being across West Virginia, with each advisory behaviour traceable to specific, inspectable geographies, GBIM beliefs, entangled retrieval contexts, and programme records in `local_resources`.
