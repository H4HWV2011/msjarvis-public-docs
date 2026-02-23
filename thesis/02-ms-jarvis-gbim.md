## Why this matters for Polymathmatic Geography

This chapter operationalizes Polymathmatic Geography by specifying how a Steward System can represent beliefs explicitly tied to **who**, **what**, **where**, **when**, **how**, **why**, **for whom**, **under whose authority**, and **on what evidence**, using the actually implemented GBIM and CSV‑based enrichment pipeline rather than hypothetical future datasets. The framework supports:  
- **P1 – Every where is entangled** by encoding legal, economic, infrastructural, social, and spiritual facts about Appalachia as a unified belief space whose axes are instantiated from the current West Virginia geospatial corpus and services CSV exports, instead of disconnected layers or purely narrative descriptions.  
- **P3 – Power has a geometry** by modeling dependencies, exposures, and flows as explicit graph and spatial relationships between entities and regions, grounded in the present GBIM tables and the joined CSV attributes that capture the real structure of state and local institutions.  
- **P5 – Design is a geographic act** by treating schemas, APIs, CSV ingestion pipelines, enrichment scripts, and retrieval guards as design decisions that alter how institutions perceive territory and act within it, with those decisions reflected concretely in the 10.2‑million‑belief GBIM corpus.  
- **P12 – Intelligence with a ZIP code** by binding the Steward’s cognition to specific West Virginia and Appalachian geographies via GBIM, a CSV‑backed geospatial corpus, a local resource registry keyed by ZIP, county, and program type, and production retrieval‑augmented generation (RAG) services that route live benefits queries through these structures; within Quantarithmia, each ZIP‑anchored region functions as a Tacet (founding key) with its own embedding tuning and a local estimate of the Material Field \( \xi \), preventing drift toward placeless averages.  
- **P16 – Power accountable to place** by requiring that beliefs be inspectable, contestable, and traceable to concrete evidence about particular communities, including whether local resource information has been recently verified with program operators and whether retrieval paths and model decisions are logged via the RAG and 21‑model ensemble stack.  

On this basis, the chapter defines the **Computational Instrument** tier: the core representational machinery and the retrieval‑and‑routing pipeline that enforce and audit Quantarithmia’s spatial‑justice commitments in a running Steward System grounded in the existing GBIM and Chroma deployments.

## Ms. Jarvis and the Geospatial Belief Information Model (GBIM)

Within Polymathmatic Geography, Ms. Egeria Jarvis is a bounded, biologically inspired Steward System whose beliefs are explicitly anchored in place, time, community, and evidence. The **Geospatial Belief Information Model (GBIM)** is the core layer tying this reasoning to concrete geographies in West Virginia and Appalachia, implemented as a **Generalized Bio‑inspired Machine** design and populated from the current PostgreSQL/PostGIS database and CSV‑derived attribute tables.

In Quantarithmia, GBIM is also the locus where Tacets are instantiated: each ZIP‑ or county‑anchored region is treated as a founding key that sets local parameters and hosts a slowly varying Material Field \( \xi \), providing a formal representation of community‑level “vibe” within the Steward’s state. Tacets thereby enter the architecture not as metaphor but as indexed components that can be interrogated and tuned.

The chapter therefore presents Ms. Jarvis as a glass‑box AI Steward System, and GBIM as the formal structure underpinning its reasoning. The emphasis is on an inspectable architecture for layered reasoning, memory, and judgment tied to geospatial entities, temporal context, evidential provenance, and the actually ingested state of local programs and institutions. Within Quantarithmia, Ms. Jarvis and GBIM constitute a concrete realization of spatially grounded, justice‑oriented reasoning: they support questions of the form *“What does the Steward System hold about this place, for whom, under whose authority, on what evidence, and when was this last confirmed with those involved?”* and yield auditable, contestable answers based on the present GBIM and embedding state rather than aspirational future datasets.

---

## What GBIM Is

<div align="center">
  <img width="60%" alt="geospatial belief information model" src="https://github.com/user-attachments/assets/331685c5-977e-4b60-9a96-3150b71787a2" />
</div>

> Figure 1. High‑level structure of the Geospatial Belief Information Model (GBIM), showing the PostGIS‑backed geospatial corpus, CSV‑derived attribute tables, Chroma semantic collections, the belief graph schema, the local resource registry, and the RAG/ensemble orchestration layer, all tied together by nine epistemic axes (who, what, where, when, how, why, for whom, under whose authority, on what evidence).

GBIM is an internal model for tying beliefs to **who**, **what**, **where**, **when**, **how**, **why**, **for whom**, **under whose authority**, and **on what evidence** for West Virginia and Appalachia. In the current deployment, these axes are populated entirely from the actually converted shapefiles and service CSV files. The production system integrates five cooperating layers:

1. **PostGIS‑backed regional geospatial corpus** – Entities and geometries derived from original shapefiles and geodatabases, realized in the GBIM schema and in CSV‑derived tables. Features are keyed by `sourcetable` and `geodb_id`, standardised to a common spatial reference system, and connected to beliefs via identity keys. Earlier limitations of an “attrs‑only” schema have been superseded by a services CSV pipeline that encodes the attributes actually used in practice.

2. **Chroma embedding collections** – High‑dimensional embeddings and metadata for GBIM‑derived beliefs and texts. Dedicated collections such as `gbim_beliefs_v1` and `gbim_beliefs_v2` store embeddings for rows in `gbimbeliefnormalized`, using text representations that combine the nine axes. Additional Chroma collections (for example, those focused on benefits facilities or local program documentation) extend this metric space to unstructured inputs. These collections are constructed from the live GBIM tables and CSV‑fed axes, so their semantic geometry reflects the existing corpus rather than a speculative one.

3. **Belief graph schema** – The `gbimbeliefnormalized` table constitutes the primary belief store, with JSONB columns for `identity`, `when`, `where`, `what`, `who`, `for_whom`, `why`, `how`, and `authority`. Enrichment scripts operating over the services CSVs and epoch metadata ensure that these axes are populated across approximately 10.2 million beliefs. Additional tables (for example, worldview entity catalogues and edge lists) connect beliefs to stable identifiers, worldviews, and typed relationships.

4. **Local resource registry** – A normalized PostgreSQL table (here denoted `local_resources`) that records community programmes (such as food assistance, housing support, utility relief, seasonal assistance, senior services, and educational support). Each record includes identifiers, program type, county and state, an explicit list of ZIP codes served, contact information, URLs, short descriptions, and a verification state machine with fields such as `verification_status`, `last_verified_at`, and `verification_notes`. This registry links unstructured documents and web sources to structured entities and provides a bridge between GBIM’s spatial body and concrete social programmes.

5. **RAG and ensemble orchestration layer** – A set of retrieval‑augmented generation services over Chroma and the GBIM corpus, together with a web research gateway and a local resource resolver, orchestrated by a main‑brain service that delegates to a 21‑model ensemble. These services expose GBIM and the registry as logged, queryable artefacts via HTTP endpoints, ensuring that live answers can be traced back to specific GBIM beliefs, CSV‑derived attributes, embeddings, and resource records.

Each belief attaches to all nine epistemic axes, with values grounded in the present CSV‑backed enrichments rather than placeholder text:

<div align="center">
  <img width="60%" alt="Belief Neighborhood for One Building" src="https://github.com/user-attachments/assets/9855f916-dadd-46af-8276-60e797549932" />
</div>

> Figure 2. The nine epistemic axes in GBIM, illustrating how each belief is simultaneously anchored in actors, kinds, places, time, mechanisms, purposes, constituencies, authorities, and evidential sources, including beliefs about local programmes serving particular ZIP codes, verification timestamps for programme data, CSV exports that contributed attributes, and retrieval paths used in live RAG pipelines.

The axes, as implemented, may be summarised as follows:

- **Who** represents persons, institutions, and communities (including actors, subjects, beneficiaries, and decision‑makers). It is instantiated by fields in the GBIM corpus (such as agency names and owner attributes) together with records in the local resource registry (such as programme directors and case managers).  

- **What** denotes kinds of entities or states (infrastructure assets, events, obligations, harms, benefits). It is represented by feature classes, layer names (`sourcetable`), and CSV‑derived attributes pushed into the `what` axis (for example, `feature_type`, `geometry`, and `domain`), as well as by programme categories (`resource_type`) in the registry.

- **Where** captures concrete locations, both as geometries (points, lines, and polygons for buildings, census units, roads, districts, facilities, environmental features, and community boundaries) and as service footprints over ZIP codes and counties. The `where` axis is populated from services CSV attributes such as latitude, longitude, and bounding boxes, mapped into a common spatial reference, while the registry encodes coverage through `zip_codes` and `county` fields.

- **When** records temporal information, including dataset vintages, epochs, and update times. Enrichment scripts have assigned epoch labels across the corpus, and registry entries record the most recent verification for each programme through timestamp fields. Runtime logs for retrieval pipelines further document when specific evidence was last used.

- **How** describes mechanisms, processes, and flows (service delivery mechanisms, data collection pipelines, regulatory processes). It is instantiated by descriptions in the `how` axis derived from epoch metadata and by descriptions of programme operation in the registry and associated documentation.

- **Why** encodes motives, justifications, and purposes (policy rationales, programme goals, safety standards). It is populated for major dataset families through enrichment SQL scripts and, in the case of local resources, by descriptive text that articulates aims such as maintaining housing stability or improving rural health access.

- **For whom** characterises distributional effects across people and places (beneficiary populations and burdens). It is represented in GBIM both as an axis and as explicit relationships linking entities to beneficiary geographies and constituencies, and in the registry through explicit targeting of particular groups (for example, SNAP households, older adults, or teachers in specific subjects).

- **Under whose authority** refers to authorising laws, policies, and institutional bodies. The `authority` axis stores references to statutes, regulations, and agencies that legitimise specific infrastructures and programmes.

- **On what evidence** records the datasets, documents, observations, and outputs that support each belief. Provenance fields in GBIM reference source tables and IDs together with epoch information, while the local resource registry tracks URLs, source documents, and verification notes. Retrieval service logs document which collections and rows contributed to each answer.

GBIM thereby ensures that beliefs are not free‑floating, but always associated with specific actors, entities, geographies, temporal frames, mechanisms, purposes, constituencies, authorising structures, and evidential bases, using the data actually present in the current PostgreSQL and Chroma deployments.

---

## How GBIM Is Represented

The representation of GBIM combines graph‑style relationships, geospatial indexing, temporal/version metadata, Hilbert‑space embeddings over the CSV‑backed belief corpus, a normalised community resource registry, and a production‑grade RAG and ensemble layer. Within Quantarithmia, Tacet‑indexed parameters and the Material Field \( \xi \) are conceptual overlays on this representational base, so that differences in how places feel correspond to differences in state rather than in narrative framing alone.

### Schema layer

The schema layer defines entities and relations as they are currently implemented:

- **Belief table** – `gbimbeliefnormalized` stores one row per belief (approximately 10.2 million rows), with JSONB columns for the nine axes. Enrichment scripts driven by services CSVs and epoch metadata have populated these axes across the corpus, yielding a dense, institutionally coherent representation.

- **Worldview and identity tables** – Associated tables (for example, `gbim_worldview_entity`) provide stable identifiers and worldviews, with explicit handling of multiple identity key variants via `COALESCE` on `source_table` and `source_pk`. These tables mediate between beliefs, geometries, and embeddings.

- **CSV‑derived source tables** – A family of tables (for example, `gbim_source_csv.*`) created from `*_attrs.csv` services exports store attributes converted directly from shapefiles and other GIS formats. These tables provide the attribute‑level ground truth for enrichment of `what` and `where`.

- **Local resource registry** – `local_resources` stores normalised representations of community programmes, including service types, spatial coverage (ZIP codes and counties), contact details, descriptive text, source links, and verification state. It is the authoritative source for programme‑level assistance information.

- **RAG and logging structures** – Schemas supporting RAG endpoints and logging maintain records of queries, collections and IDs retrieved (including from `gbim_beliefs_v2`), model responses, and guardrail outcomes, thereby adding an “operational evidence” dimension to GBIM.

### Integrated layers

At the integrated level, GBIM supports graph‑like reasoning, spatial queries, and semantic similarity:

- **Graph relationships** arise through the interpretation of axes and through explicit edge tables, capturing `how`, `why`, `for whom`, and `authority` relationships among entities, programmes, and worldviews.  
- **Spatial relationships** are defined by geometries in the GBIM corpus and by ZIP/county coverage in the registry, enabling queries that combine physical proximity with service eligibility.  
- **Embedding‑based relationships** are defined by the Chroma collections built from `gbimbeliefnormalized` and related texts, allowing similarity queries that traverse the corpus in a high‑dimensional Hilbert space.

A single building footprint provides a concrete illustration. Its corresponding belief row includes identity, spatial location, ontological classification, responsible institutions, beneficiary communities, purpose, method of creation, and authorising legal context. That belief is embedded into Chroma via `msjarvis_embed_gbim.py`. The building is also associated with a ZIP code and county, which connect it to programmes listed in `local_resources`. When a query concerns assistance near that location, the system performs a combined retrieval over embeddings, spatial relations, and the registry, and logs the full retrieval path.

In its present state (February 2026), the system consists of:

- A GBIM belief table populated across all nine axes, based on actual services CSVs and epoch metadata.  
- CSV‑derived attribute tables serving as the primary per‑feature attribute source.  
- Chroma collections (including `gbim_beliefs_v2`) holding embeddings of GBIM beliefs.  
- A local resource registry populated for selected West Virginia counties and ZIP codes.  
- RAG and ensemble services that use these components to answer geography and benefits questions with traceable evidence and explicit spatial grounding.

This configuration constitutes a concrete, academically tractable instantiation of Polymathmatic Geography’s demand for a Steward System whose intelligence is explicitly and verifiably tied to place, institutional structure, and lived community conditions.
