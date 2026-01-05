## 6. GeoDB and the Spatial Body of Ms. Jarvis

This chapter describes the geospatial substrate that anchors Ms. Egeria Jarvis in the physical world of West Virginia. This spatial layer is tightly coupled to GBIM and to the Chroma‑based Hilbert space (accessed via RAG services), so that beliefs and narratives are grounded not only in abstract embeddings but also in specific buildings, river reaches, floodplains, mines, and infrastructure corridors.

## 6.1 Design Goals for the GeoDB Layer

The GeoDB layer has three primary design goals:

- Represent West Virginia as a coherent, queryable geospatial mesh.  
- Provide fast, programmatic access to that mesh for reasoning, retrieval, and visualization.  
- Integrate cleanly with GBIM and Chroma so that spatial, semantic, and governance dimensions can be used together.  

In practice, this means maintaining a PostGIS‑backed geodatabase that holds authoritative feature classes for structures, hazards, networks, civic facilities, administrative boundaries, and named places across the state. On top of this, a family of `geodb_*` collections in Chroma provides vector embeddings and compact metadata for many of these layers, so that spatial features can be discovered both by location and by semantic similarity through the Steward System’s RAG services.

## 6.2 PostGIS as Ms. Jarvis’s Spatial Backbone

At the storage level, Ms. Jarvis uses a PostGIS database (for example, `msjarvis_gis`) as the main container for West Virginia vector datasets. Feature classes are organized by theme and provenance: census units, structure points, building footprints, hydrology, transportation networks, hazards, and facilities. Each table is organized into UTM83 and WMA84 variants where appropriate, and most layers are already in suitable projected coordinate systems, with SRID metadata cleanup still in progress for a minority of legacy tables.

This database is populated from a mix of state and federal sources, including the WVU GIS Technical Center, USGS, USACE, NREL, the U.S. Census Bureau, and various state agencies. The ingestion process converts shapefiles and file geodatabases into PostGIS tables, fixes obvious schema issues (such as geometry types and projections), and normalizes keys so that features can be cross‑referenced from GBIM, Chroma, and higher‑level reasoning services.

## 6.3 What Is Currently Integrated

The current deployment includes a substantial, production‑usable subset of West Virginia’s public geospatial data, with additional layers actively being integrated. In broad strokes, the Steward System already has:

- 2020 Census blocks and block groups for West Virginia in appropriate projected coordinate systems, including:  
  - `blocks_census_2020_utm83`: 72 558 features (statewide blocks).  
  - `blockgroups_census_2020_utm83`: 1 639 features (statewide block groups).  
- A dense statewide structure inventory, combining SAMB structure points (north and south) with WV GISTC building footprints and Microsoft building points, yielding several million total structures, including for example:  
  - `structurepointsnorth_samb_2003_utm83`: on the order of hundreds of thousands of structures in northern counties.  
  - `structurepointssouth_samb_2003_utm83`: a comparable number of structures in southern counties.  
  - `wvgistc_building_footprints` (or equivalent canonicalized table): over 2.1 million building footprints.  
  - `wv_microsoft_20180207_utm17n83`: roughly one million additional building‑like points.  
- Hazard and infrastructure layers such as abandoned mine lands, dams, floodplain structures at risk, rail networks, navigable waterways, and tower inventories, including representative tables like:  
  - `minesabandonedlandsline_wvdep_1996_noprojectoin`: more than 10 000 linear features.  
  - `minesabandonedlandspolygon_wvdep_1996_noprojection`: over 2 000 polygons.  
  - `dams_usarmycorpsofengineers_200010_utm83` and `damsnoncoal_usgs_2002_utm83`: hundreds of dam sites statewide.  
  - `floodplain_structures_at_risk_usarmycorpsofengineers_200303_utm83`: structures intersecting modeled floodplains.  
  - `railnetwork_wv_usdot_200203_utm83` and related regional rail layers.  
  - `navigablewaterways_rivermiles_usarmycropsofengineers_2006_utm83` and associated structures.  
- Civic and facility coverage, including hospitals, nursing homes, fire and police stations, higher‑education campuses, VA facilities, solid waste sites, sewer plants, community health providers, libraries, and parks, for example:  
  - `hospitals_wvdem_040519_utm83` and `nursinghomes_wvdem_041219_utm83`.  
  - `firedept_wvdem_092017_utm83` and `policedept_wvdem_012319_utm83`.  
  - `highered_wvemd_072420_utm83`, `libraries_manysources_2001_utm83`, and `countycity_park_boundaries_20201104_utm83`.  
- Rich geographic index and governance layers drawn largely from USGS and state sources: named summits, springs, weather stations, index grids, state and county boundaries, regional council boundaries, and historic resources, including:  
  - `wv_county_boundaries_24k_topo_updated_2022_utm83`: 55 county polygons.  
  - `zipcodetabulationarea_census_2020_utm83`: several hundred ZIP code tabulation areas.  
  - `geographic_names_on_usgs_topomaps_current_usgs_20110801_utm83` and related historical name tables.  
  - `nationalregister_point_20200923` and associated National Register polygon datasets.  

These datasets are wired into the live system via PostGIS connections and, for a prioritized subset of layers, corresponding `geodb_*` collections in Chroma, so that other services can query and reason over them in real time rather than treating them as static files.

## 6.4 Chroma `geodb_*` Collections and Spatial Embeddings

To bridge between geometric features and high‑dimensional semantic reasoning, Ms. Jarvis maintains a large set of `geodb_*` collections in a local Chroma store accessed via embedded clients and exposed through RAG endpoints. In the current system, there are on the order of a few hundred collections, many of which correspond directly to PostGIS layers such as census blocks, dams, hospitals, nursing homes, 911 centers, cities and ZIPs, building footprints, and a variety of civic, environmental, and hazard layers.

Each `geodb_*` collection contains embeddings keyed by compact GeoDB metadata (typically a stable identifier plus a source table reference), which the Steward System uses to rejoin each document back to the full attribute row in PostGIS. This allows hybrid queries such as:

- Find structures in a county that are both in a 100‑year floodplain and near a hospital.  
- Retrieve documents and prior analyses relevant to a specific dam or mine site, plus thematically similar facilities.  
- Surface named places and features (ridges, hollows, communities) near a proposed project site and then reason about risk or access.  

By treating the Chroma data directory as the semantic index for integrated West Virginia geospatial embeddings, Ms. Jarvis maintains a stable bridge between the spatial backbone and the Hilbert‑space memory. Periodic inventories of these collections and their counts provide auditable snapshots of the current spatial integration state.

## 6.5 Staged but Not Yet Fully Integrated Layers

Not every dataset sitting on disk is fully integrated into the live reasoning stack. Several classes of layers are currently staged or partially integrated:

- Some legacy datasets required schema and numeric precision fixes before they could be reliably imported; many have now been cleaned and loaded, but a small tail still needs attention.  
- Certain HSIP and historical or specialized layers have encountered type mismatches (such as inconsistent ID fields) or locking/throughput issues during heavy write activity; these are present in PostGIS but not yet mirrored into Chroma with full metadata.  
- Additional WVU GIS Technical Center and federal/state layers reside on SSD‑backed working storage and in PostGIS, but have not yet been embedded into `geodb_*` collections with consistent keys and metadata.  

For these datasets, the honest description is that they are present and often queryable in PostGIS, but are not yet part of the end‑to‑end geospatial reasoning fabric that Hilbert‑space RAG and GBIM use by default.

## 6.6 Linking GeoDB to GBIM and Hilbert Space

Within the broader GBIM framework, spatial information is one dimension of a geometric belief state that also includes semantic, temporal, and governance components. GeoDB provides the concrete anchor for that spatial dimension. Belief nodes that refer to places—counties, neighborhoods, structures, industrial sites, or facilities—are linked to specific feature IDs and geometries in the PostGIS database.

Hilbert‑space embeddings in Chroma often carry location‑related metadata (for example, county FIPS codes or feature IDs stored in PostGIS, plus keys that link back to source tables). This allows the Steward System to move fluidly between:

- Semantic proximity: documents or features that are similar in content or meaning.  
- Spatial proximity: features that are geographically close or share relevant spatial relationships.  
- Belief‑space relationships: GBIM edges that encode causal, normative, or governance‑relevant links between spatial entities.  

By tying embeddings, beliefs, and geometries together, Ms. Jarvis can answer questions that depend on all three, such as which nursing homes in a flood‑prone region are near rail lines and within the jurisdiction of a given regional council, and then push those answers into governance or risk‑analysis workflows.

## 6.7 Geo‑Aware RAG and Multi‑LLM Use

The GeoDB and `geodb_*` collections also play a direct role in retrieval‑augmented generation. When a query has an explicit or implicit spatial component—references to specific towns, hollows, rivers, counties, or facilities—the RAG pipeline can:

- Use spatial filters in PostGIS to constrain candidate features or regions.  
- Use `geodb_*` collections in Chroma to pull semantically relevant documents, notes, or prior analyses associated with those features.  
- Provide this spatially filtered context to different models and tools in the ensemble, such as generalist reasoning models, code models, or governance‑oriented judges.  

Different models may specialize in different types of geo‑aware tasks: narrative explanations for lay audiences, technical risk assessments, code that manipulates spatial data, or governance‑oriented recommendations. The GeoDB layer ensures that, regardless of which model is active, the Steward System’s answers can be grounded back into specific, verifiable places.

## 6.8 Roadmap for Full Statewide Integration

The near‑term roadmap for the GeoDB layer is to move from “a substantial integrated subset plus staged layers” toward a more comprehensive mirror of the state’s public geospatial infrastructure. Concretely, this means:

- Cleaning up remaining schema issues (numeric precision, ID typing, geometry consistency) in the tail of WVU GIS Technical Center and federal/state layers.  
- Ensuring that all relevant vector datasets are loaded into PostGIS with stable, documented keys.  
- Creating or updating matching `geodb_*` collections in Chroma with consistent metadata, so that every important spatial feature has both a geometric representation and a semantic footprint accessible via RAG.  
- Periodically regenerating and archiving CSV inventories of the GeoDB and Chroma collections, so that claims about coverage and feature counts remain auditable over time.  

As this work progresses, Ms. Jarvis will be able to reason over essentially all relevant statewide layers—structures, hazards, networks, demographics, land use, and more—on the order of tens of millions of features. At that point, the spatial body of the Steward System will be mature enough to support detailed, location‑specific reasoning about risk, infrastructure, governance, and community well‑being across West Virginia.
