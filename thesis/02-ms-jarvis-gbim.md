## Why this matters for Polymathmatic Geography

This chapter describes how Ms. Jarvis already holds and uses structured claims about West Virginia that are explicitly tied to **who**, **what**, **where**, **when**, **how**, **why**, **for whom**, **under whose authority**, and **on what evidence**, using the live GBIM corpus of 10,221,702 beliefs and the current CSV‑driven enrichment pipeline. It supports:  
- **P1 – Every where is entangled** by encoding legal, economic, infrastructural, social, and cultural facts about Appalachia as one interconnected belief space, with axes instantiated from the existing West Virginia geodatabase and the loaded services CSV exports, rather than from speculative or placeholder layers.  
- **P3 – Power has a geometry** by representing exposure, access, obligation, and flow as explicit graph and spatial relationships between concrete entities and regions, grounded in the actual GBIM tables and CSV‑derived attributes that reflect the present institutional and physical structure of the state.  
- **P5 – Design is a geographic act** by showing how choices about schemas, keys, CSV ingestion, enrichment scripts, and retrieval and routing services have already reshaped how West Virginia is seen and acted upon in analysis, governance, and search, with those choices embedded in the 10.22‑million‑belief GBIM corpus.  
- **P12 – Intelligence with a ZIP code** by binding Ms. Jarvis’s reasoning to specific West Virginia and Appalachian locations through GBIM, a CSV‑backed spatial corpus, a separate programme registry keyed by county and ZIP where deployed, and running retrieval‑augmented services that route real questions through these structures instead of abstract national averages.  
- **P16 – Power accountable to place** by requiring that system recommendations can be inspected, challenged, and traced back to concrete claims about particular communities, including which datasets, epochs, and retrieval paths were involved and how those were processed by the multi‑model ensemble.  

In this sense, the chapter belongs to the **Computational Instrument** tier: it describes the representational machinery and retrieval‑and‑routing behaviour that already anchor Quantarithmia’s spatial commitments in an operational Steward System backed by GBIM, PostGIS, and Chroma.

## Ms. Jarvis and the Geospatial Belief Information Model (GBIM)

Within Polymathmatic Geography, Ms. Egeria Jarvis is a bounded, biologically inspired Steward System whose commitments are explicitly anchored in geography, time, community, and source. The **Geospatial Belief Information Model (GBIM)** is the central structure that ties this reasoning to concrete locations and institutions in West Virginia and Appalachia, implemented over PostgreSQL/PostGIS and populated from services‑derived CSV tables and embeddings.

In the Quantarithmia framework, GBIM is also where region‑specific founding keys are attached: each ZIP‑ or county‑based region can be treated as a parameterizing element whose configuration encodes local conditions in the global state, so that differences between places show up as differences in stored structure and in the resulting embedding landscape. These elements appear as identifiable objects within the schema and embedding collections, not just as metaphors.

The chapter thus presents Ms. Jarvis as a transparent, inspectable Steward System, and GBIM as the formal structure underpinning her reasoning. The focus is on an auditable design for layered reasoning, memory, and judgment tied to named features, time spans, provenance, and the actual state of West Virginia datasets and programme information. Within Quantarithmia, Ms. Jarvis and GBIM provide a working example of spatially grounded, distribution‑sensitive reasoning: they support questions such as *“What does the system currently hold about this place, for whom, under whose authority, with which sources, and with what temporal coverage?”* and produce answers that can be traced back through the GBIM rows and associated embeddings.

---

## What GBIM Is

<div align="center">
  <img width="60%" alt="geospatial belief information model" src="https://github.com/user-attachments/assets/331685c5-977e-4b60-9a96-3150b71787a2" />
</div>

> Figure 1. High‑level structure of the Geospatial Belief Information Model (GBIM), showing the PostGIS‑backed spatial corpus, CSV‑derived tables, Chroma collections, the belief table, external programme registries, and the retrieval/ensemble layer, all coordinated through nine axes (who, what, where, when, how, why, for whom, under whose authority, on what evidence).

GBIM is the internal representation that ties each belief about West Virginia to **who**, **what**, **where**, **when**, **how**, **why**, **for whom**, **under whose authority**, and **on what evidence**. In the running system, these axes are populated from the converted statewide shapefiles and geodatabases (via attrs‑style CSVs), from epoch manifests, and from hand‑curated family‑level metadata. The deployed system combines five cooperating layers:

1. **PostGIS‑backed statewide spatial corpus** – Vector datasets imported from original files into PostGIS and summarized in lightweight CSV‑derived tables. Features are keyed by `sourcetable` and a stable feature identifier, aligned to a common projected coordinate system where possible, and linked to GBIM beliefs through identity keys embedded in the `identity` axis.

2. **Chroma embedding collections** – High‑dimensional embeddings and metadata for beliefs and texts derived from GBIM. Collections such as `gbim_beliefs_v2` store vectors for rows in `gbimbeliefnormalized`, using text built from the nine axes. Additional collections focus on thematic content (for example, assistance facilities and guidance documents) and extend the metric space to unstructured material, all derived from the live database state.

3. **Belief table and related catalogs** – The `gbimbeliefnormalized` table is the main belief store, with approximately 10.22 million rows and JSONB columns for `identity`, `when`, `where`, `what`, `who`, `forwhom`, `why`, `how`, `authority`, and `evidence`. Enrichment scripts driven by epoch tables and CSV‑based spatial summaries have filled most axes at scale. Associated catalogs provide persistent identifiers, handle the dual identity key variants, and support joins to spatial tables and logs.

4. **External programme registry** – A separate PostgreSQL database (for example, exposed as `local_resources`) holds normalized representations of community programmes such as food assistance, housing, utilities, seasonal support, senior services, and education. Each row includes types, coverage by ZIP and county, contacts, links, and verification status. Where populated, this registry connects directly to places and organizations that also appear as GBIM entities.

5. **Retrieval and ensemble layer** – A set of services that perform retrieval‑augmented generation over GBIM, Chroma, web sources, and local registries, orchestrated by a coordinator that delegates to a multi‑model ensemble. These services expose structured retrieval, spatial filters, and semantic search over GBIM beliefs and related corpora, with logging that records which beliefs, collections, and registry entries were used for each answer.

Within this structure, each belief row is recorded across all nine axes, using values derived from real datasets and enrichment runs rather than speculative text:

<div align="center">
  <img width="60%" alt="Belief Neighborhood for One Building" src="https://github.com/user-attachments/assets/9855f916-dadd-46af-8276-60e797549932" />
</div>

> Figure 2. The nine axes in GBIM, showing how a single belief can be situated in relation to actors, types, locations, time, mechanisms, purposes, beneficiaries, authorities, and evidence, and how neighborhood‑style queries over this structure support interpretation and contestation.

In the current deployment, the nine axes function as follows:

- **Who** captures people and institutions involved in or responsible for the feature or situation (for example, agencies, operators, governing bodies, and sometimes communities). These values are drawn from epoch metadata and, where available, from source attributes.

- **What** records what sort of thing is being described: types of infrastructure, land use, facilities, events, or states. Baseline values (such as geometry, feature family, and domain) are synthesized from epoch‑level descriptions and later refined where more detailed attributes exist.

- **Where** stores spatial information, including latitudes and longitudes derived from attrs tables and the underlying source layer name, and is ultimately anchored in PostGIS geometries when available. This axis allows beliefs to be anchored to points, polygons, and named areas and to be grouped by county, ZIP, or other boundaries.

- **When** captures temporal aspects: dataset vintage, epoch label, and other timing information. Enrichment scripts have assigned epoch labels across the corpus so that each belief can be associated with a particular year or period, with a small residual of unclassified entries explicitly recorded.

- **How** summarizes methods, processes, and mechanisms (for example, how a dataset was produced, which survey or modeling approach was used, or which institutional process gives rise to the feature). These values are currently supplied at the dataset‑family level and applied consistently across all beliefs in that family.

- **Why** collects motivations and purposes where available, such as policy objectives or reasons for maintaining particular infrastructures. At present, this axis is fully populated for a large subset of named epochs with hand‑curated descriptions, and remains empty elsewhere.

- **For whom** is intended to describe who benefits or is affected; in the present corpus the formal column exists but has not yet been populated at scale, and distributional questions are instead inferred through combinations of `who`, `what`, `where`, and external programme and demographic information.

- **Under whose authority** captures the legal and institutional bases for a belief: statutes, regulations, and formal powers associated with the infrastructure or programme. This axis is fully populated for the main dataset families and supports inspection of governing frameworks.

- **On what evidence** is reserved for explicit citations to source documentation, clearinghouse entries, or other references. In the current GBIM table this axis is available but not yet populated; source provenance is instead tracked via `sourcetable`, key fields, epoch manifests, and service logs.

Taken together, these axes ensure that each belief in GBIM is attached to identifiable actors, types, places, timeframes, procedures, purposes, beneficiaries, authorizing frameworks, and sources, using the data that are actually present in the PostgreSQL and embedding deployments as of early 2026.

---

## How GBIM Is Represented

GBIM’s implementation combines a belief table with JSONB axes, a statewide spatial database, epoch and attribute manifests, vector embeddings, programme registries, and retrieval infrastructure. The design supports both structured queries and semantic traversal.

### Schema layer

The schema layer includes:

- **Belief table** – `gbimbeliefnormalized` holds one row per belief (10,221,702 rows), with JSONB columns for the nine axes. Enrichment passes have produced complete or near‑complete coverage for most axes, with clear gaps in `forwhom` and `evidence`, and partial coverage in `why`.

- **Epoch and identity structures** – Tables that map each `sourcetable` to an epoch label and vintage and handle the dual `identity` key variants produced by earlier ingestion pipelines. All update scripts use `COALESCE` on these keys to maintain compatibility across the entire corpus.

- **CSV‑derived attribute tables** – Attrs‑style tables created from statewide `*_attrs.csv` exports store feature‑level identifiers, latitudes, longitudes, bounding boxes, labels, and table names. These are the primary sources for the `where` axis and support joins back into PostGIS layers where available.

- **Programme registries and other stores** – Separate databases host tables such as `local_resources`, which model community programmes at a level appropriate for benefits routing and assistance queries, and are linked to GBIM via shared identifiers, names, and spatial references.

- **Retrieval and logging tables** – Logs record which GBIM beliefs, epochs, datasets, and collections are touched during particular requests, adding an operational layer of evidence about how the system has actually used its knowledge.

### Integrated layers

When considered as a whole, GBIM supports multiple forms of reasoning:

- **Structured and graph‑like reasoning** – GBIM axes and associated relationships define directed links between entities, institutions, regions, and programmes, enabling queries such as which facilities serve which areas, which regulations apply to which sites, and how responsibilities and flows are organized.

- **Spatial reasoning** – PostGIS geometries, attrs tables, and the `where` axis support spatial operations and proximity analyses. Buildings, roads, districts, hazard zones, and facilities can be selected and analyzed by location, buffer, intersection, or membership in administrative units.

- **Embedding‑based reasoning** – Text representations built from the nine axes for each belief are embedded into Chroma collections such as `gbim_beliefs_v2`. This allows similarity search and clustering over the beliefs, linking conceptually related items even when they arise from different datasets or epochs.

For example, a single building can appear as:

- A row in `gbimbeliefnormalized` with fields describing its identity, location, type, responsible entities, family‑level method and purpose, and applicable authority.  
- A spatial feature in PostGIS, with geometry and attributes suitable for map display and spatial analysis.  
- A vector in Chroma, located near other buildings and entities that share similar semantics, and accessible via text‑based queries.  

In the current configuration (February 2026), the live system comprises:

- A belief table with complete coverage for `identity`, `when`, `what`, `who`, `how`, and `authority`, near‑complete coverage for `where`, partial coverage for `why`, and planned use of `forwhom` and `evidence`.  
- Statewide attribute tables derived from services CSV files, furnishing basic location and labeling for features across roughly eighty epochs.  
- Embedding collections that hold vectors for a large subset of beliefs and for selected programme and facility descriptions.  
- External registries and services that tie beliefs to real benefits programmes where those registries have been populated.  
- Retrieval and ensemble services that already use these structures to answer questions about West Virginia’s geography, institutions, and assistance landscape in a way that can be inspected and refined.

This chapter therefore treats GBIM not as a prospective design but as an existing apparatus that can be measured, queried, and audited, and that serves as the spatial and institutional backbone of Ms. Jarvis within the broader Polymathmatic Geography programme.
