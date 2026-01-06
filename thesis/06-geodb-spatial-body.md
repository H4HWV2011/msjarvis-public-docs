## 6. GeoDB and the Spatial Body of Ms. Jarvis

### 6.1 Purpose and Scope

This chapter describes the geospatial substrate that anchors Ms. Egeria Jarvis in the physical world of West Virginia. The GeoDB layer is tightly coupled to GBIM and to the Chroma‑based Hilbert space accessed via RAG services, so that beliefs and narratives are grounded not only in abstract embeddings but also in specific buildings, river reaches, floodplains, mines, and infrastructure corridors. The focus here is on the structure and status of the PostGIS‑based geodatabase and its relationship to ChromaDB collections, not on exhaustive cataloging of every possible dataset.

Within the Quantarithmia program, GeoDB provides the spatial backbone of Ms. Jarvis’s “body”: a coherent, queryable mesh of features and boundaries for reasoning about risk, access, infrastructure, and spatial justice. The chapter documents what is currently integrated, what is staged, and how these layers are linked into the broader Hilbert‑space and GBIM framework.

---

### 6.2 Design Goals for the GeoDB Layer

The GeoDB layer is designed to satisfy three primary goals:

- **Coherent statewide mesh.**  
  Represent West Virginia as a coherent, queryable geospatial mesh of structures, hazards, networks, civic facilities, administrative boundaries, and named places.

- **Programmatic access.**  
  Provide fast, programmatic access to that mesh for reasoning, retrieval, visualization, and analytics through well‑defined schemas and APIs.

- **Integration with GBIM and Chroma.**  
  Integrate cleanly with GBIM and Chroma so that spatial, semantic, and governance dimensions can be used together in a single reasoning pipeline.

In practice, this means maintaining a PostGIS‑backed geodatabase that holds authoritative feature classes for core themes and, for a prioritized subset, maintaining corresponding `geodb*` and `gedb*` collections in ChromaDB. These collections store embeddings and compact metadata for selected layers so that spatial features can be discovered both by location and by semantic similarity.

---

### 6.3 PostGIS as Ms. Jarvis’s Spatial Backbone

At the storage level, Ms. Jarvis uses a PostGIS database (for example, a database analogous to `msjarvis_gis`) as the main container for West Virginia vector datasets. Feature classes are organized by theme and provenance—census units, structure points, building footprints, hydrology, transportation networks, hazards, and facilities—with consistent naming and key conventions.

Where appropriate, tables exist in projected coordinate systems such as UTM83, and in some cases also in WMA84 or related systems to support different analysis and mapping workflows. For the majority of production layers, SRIDs and geometry types are normalized; a smaller set of legacy tables retain provisional SRID or geometry metadata and are explicitly flagged in the schema registry for cleanup.

The database is populated from state and federal sources, including the WVU GIS Technical Center, USGS, the U.S. Census Bureau, USACE, NREL, and various state agencies. Ingestion converts shapefiles and file geodatabases into PostGIS tables, resolves geometry and projection issues, and normalizes keys so that features can be cross‑referenced from GBIM, Chroma, and higher‑level reasoning services. The ingestion process is scripted and versioned so that table structures and provenance can be audited.

---

### 6.4 Currently Integrated Statewide Layers

The current deployment includes a substantial, production‑usable subset of West Virginia’s public geospatial data, with additional layers actively being integrated. At a high level, the Steward System already has:

- **Census units.**  
  Statewide 2020 Census blocks and block groups in projected coordinate systems suitable for analysis and mapping. Representative tables include:
  - blocks tables with tens of thousands of features (on the order of statewide block counts),
  - block group tables with on the order of a few thousand polygons.

- **Structures and buildings.**  
  A dense statewide structure inventory combining:
  - SAMB structure points (north and south) for large numbers of structures across northern and southern counties,
  - WV GIS Technical Center building footprints numbering in the millions, and
  - Microsoft building point datasets contributing additional building‑like points.

- **Hazard and infrastructure layers.**  
  Datasets such as:
  - abandoned mine lands (lines and polygons),
  - dams (coal‑ and non‑coal‑related) from Army Corps and USGS,
  - floodplain structure inventories,
  - rail networks and associated facilities,
  - navigable waterways and river mile indexing.

- **Civic and facility coverage.**  
  Layers representing:
  - hospitals, nursing homes, and other healthcare facilities,
  - fire and police stations,
  - higher‑education campuses,
  - libraries and community centers,
  - parks and recreational areas,
  - solid waste sites and sewer plants, among others.

- **Governance and index layers.**  
  Tables capturing:
  - county and state boundaries,
  - ZIP Code Tabulation Areas and related postal geography,
  - regional planning council boundaries and similar governance regions,
  - named places, summits, and other geographic names,
  - National Register points and polygons and other historic resources.

Exact feature counts and table names are recorded in database inventories maintained alongside this thesis, so that claims about coverage can be verified and updated as ingestion continues. These datasets are wired into the live system via PostGIS connections and, for a prioritized subset of layers, mirrored into `geodb*` and `gedb*` collections in Chroma for semantic retrieval.

---

### 6.5 Chroma `geodb*` / `gedb*` Collections and Spatial Embeddings

To bridge geometric features and high‑dimensional semantic reasoning, Ms. Jarvis maintains a large set of `geodb*` collections in ChromaDB. Many of these collections correspond directly to PostGIS layers such as census blocks, dams, hospitals, nursing homes, 911 centers, cities, ZIPs, building footprints, and various civic, environmental, and hazard layers.

Each `geodb*` collection contains:

- embeddings derived from feature‑level descriptions and attributes,
- compact metadata including a stable feature identifier, source table reference, and selected classification fields,
- optional document fields summarizing the feature’s role or risk context.

The system uses these identifiers to rejoin each document back to the full attribute row and geometry in PostGIS. This supports hybrid queries such as:

- identifying structures in a county that lie within a modeled floodplain and within a specified distance of a hospital,
- retrieving documents and prior analyses relevant to a specific dam or mine site, plus similar facilities for comparative risk assessment,
- surfacing named places and features near a proposed project site and reasoning about access, exposure, or service coverage.

For nearly every `geodb*` collection, there is a corresponding `gedb*` collection. The `geodb*` collections hold embeddings and base metadata; the `gedb*` collections serve as stable aliases, often with simplified or placeholder documents and mirrored metadata. Higher‑level services can depend on `gedb*` names as a compatibility layer, even if ingestion pipelines or underlying table structures evolve.

Periodic inventories of `geodb*` and `gedb*` collections, including collection names and document counts, provide auditable snapshots of the current spatial integration state. These inventories are used both in operations and as empirical support for claims in this chapter.

---

### 6.6 Staged and Partially Integrated Layers

Not every dataset present on disk or in PostGIS is fully integrated into the live geospatial reasoning stack. Several classes of layers are staged or partially integrated:

- **Legacy and irregular schemas.**  
  Some older datasets required schema adjustments and numeric precision fixes before they could be reliably imported. Many have now been cleaned and loaded; a smaller tail of legacy layers remains flagged for further work.

- **Specialized and high‑volume layers.**  
  Certain HSIP‑derived or specialized layers have encountered type mismatches or throughput constraints during bulk operations. These layers may exist in PostGIS with provisional keys or geometry columns but are not yet mirrored into Chroma with full embeddings and standardized metadata.

- **Additional WVU and federal/state layers.**  
  Additional datasets reside on SSD‑backed working storage and in PostGIS but have not yet been embedded into `geodb*` collections with consistent identifier schemes and metadata. They are tracked in ingestion plans and marked as “staged” rather than fully live.

For these datasets, the accurate description is that they are present and often queryable in PostGIS but are not yet part of the default geospatial reasoning path that the Hilbert‑space RAG and GBIM pipelines use. Their eventual integration will follow the same key‑normalization, embedding, and aliasing patterns described above.

---

### 6.7 Linking GeoDB to GBIM and Hilbert Space

Within the broader GBIM framework, spatial information is one dimension of a geometric belief state that also includes semantic, temporal, and governance components. GeoDB provides the concrete anchor for this spatial dimension. Belief nodes that refer to places—counties, neighborhoods, structures, industrial sites, or facilities—are linked to specific feature identifiers and geometries in PostGIS.

Embeddings stored in `geodb*` collections often carry location‑related metadata such as county FIPS codes, municipality names, and feature IDs, as well as keys that link back to source tables. This linkage allows Ms. Jarvis to move fluidly among:

- **Semantic proximity.**  
  Retrieval of documents or features that are similar in content or role (for example, dams with similar design and hazard classifications).

- **Spatial proximity.**  
  Selection of features that are geographically close or share relevant spatial relationships (for example, homes within a buffer of a floodplain boundary).

- **Belief‑space relationships.**  
  GBIM edges that encode causal, normative, or governance‑relevant links between spatial entities (for example, relationships between facilities and service regions, or between hazard sites and vulnerable populations).

By tying embeddings, beliefs, and geometries together, Ms. Jarvis can answer questions that depend on all three—for example, which nursing homes in a flood‑prone region are near rail lines and lie within the jurisdiction of a particular regional council—and feed those answers into governance and risk‑analysis workflows.

---

### 6.8 Geo‑Aware RAG and Multi‑Model Use

The GeoDB and `geodb*` / `gedb*` collections play a direct role in retrieval‑augmented generation, especially for spatially explicit queries. When a query has an explicit or implicit spatial component—references to towns, hollows, rivers, counties, or facilities—the RAG pipeline can:

- apply spatial filters in PostGIS to constrain candidate features or regions,
- query `geodb*` collections in ChromaDB to retrieve semantically relevant documents, notes, or prior analyses associated with those features, and
- provide spatially filtered context to different models and tools in the ensemble.

Different models may specialize in different types of geo‑aware tasks: narrative explanations for public audiences, technical risk assessments, code that manipulates spatial data, or governance‑oriented recommendations. The GeoDB layer ensures that, regardless of which model is active, the Steward System’s answers remain grounded in specific, verifiable places with clear links back to underlying data.

---

### 6.9 Roadmap for Full Statewide Integration

The near‑term roadmap for the GeoDB layer is to move from “a substantial integrated subset plus staged layers” toward a more comprehensive mirror of the state’s public geospatial infrastructure. Concretely, this entails:

- **Completing schema normalization.**  
  Cleaning up remaining geometry, SRID, and numeric precision issues in the residual set of WVU GIS Technical Center and federal/state layers.

- **Ensuring stable keys.**  
  Verifying that all relevant vector datasets are loaded into PostGIS with stable, documented primary keys and supporting indexes, enabling consistent linkage from GBIM and Chroma.

- **Mirroring into Chroma.**  
  Creating or updating matching `geodb*` collections in ChromaDB with consistent metadata, and where appropriate, `gedb*` aliases, so that each prioritized spatial feature has both a geometric representation and a semantic footprint accessible via RAG.

- **Maintaining inventories and audit trails.**  
  Periodically regenerating and archiving CSV inventories of PostGIS tables and Chroma collections, including feature counts and embedding coverage, so that claims about coverage and integration remain auditable over time.

As these steps are completed, Ms. Jarvis will be able to reason over an increasingly comprehensive set of statewide layers—structures, hazards, networks, demographics, land use, and more—at the scale of tens of millions of features. At that point, the spatial body of the Steward System will be mature enough to support detailed, location‑specific reasoning about risk, infrastructure, governance, and community well‑being across West Virginia.
