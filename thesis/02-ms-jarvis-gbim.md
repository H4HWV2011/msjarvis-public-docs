## Why this matters for Polymathmatic Geography

This chapter makes Polymathmatic Geography operational by specifying how a Steward System can hold beliefs explicitly tied to **who**, **what**, **where**, **when**, **how**, **why**, **for whom**, **under whose authority**, and **on what evidence**, using the actual CSV‑converted GBIM corpus now in production rather than hypothetical future layers. It directly supports:  
- **P1 – Every where is entangled** by representing legal, economic, infrastructural, social, and spiritual facts about Appalachia as a unified, structured belief space whose axes are now filled from real West Virginia datasets and services CSVs, not just documentation.  
- **P3 – Power has a geometry** by encoding dependencies, exposures, and flows as graph and spatial relationships between entities and regions, and by reflecting the real service structure captured in GBIM and the local resource CSV exports.  
- **P5 – Design is a geographic act** by treating schemas, APIs, CSV pipelines, RAG routes, and guardrails as design choices that reshape how institutions "see" their territory and act within it, grounded in the actual 10.2M‑belief corpus and the `*_attrs.csv`‑driven enrichment you now run in production.  
- **P12 – Intelligence with a ZIP code** by binding Ms. Jarvis's cognition to specific West Virginia and Appalachian geographies through GBIM, the CSV‑backed spatial corpus, a verified local resource registry keyed by ZIP, county, and program type, and production RAG services that route live benefits questions through these structures; Quantarithmia treats each ZIP‑bound region as a Tacet (founding key) with its own tuning of embeddings and a local estimate of the Material Field \( \xi \), so that intelligence remains keyed to place rather than drifting toward placeless averages.  
- **P16 – Power accountable to place** by requiring that beliefs be inspectable, contestable, and traceable to concrete evidence about particular communities, including whether local resource information has been recently verified with the people running those programs and whether retrieval paths and model decisions are logged through the RAG and 21‑LLM ensemble stack, using the real GBIM + Chroma state you are now populating (for example, `gbim_beliefs_v2`).  

This chapter defines the **Computational Instrument** tier: the core representational machinery and retrieval‑and‑routing pipeline that enforce and audit Quantarithmia's spatial‑justice commitments in a live, production Steward System, now backed by actual CSV‑derived GBIM beliefs and embeddings rather than purely aspirational schemas.

## Ms. Jarvis and the Geospatial Belief Information Model (GBIM)

Within **polymathmatic geography**, Ms. Egeria Jarvis is a bounded, bio‑inspired Steward System whose beliefs are explicitly anchored in place, time, community, and evidence. **GBIM** (Geospatial Belief Information Model) is the core layer tying Ms. Jarvis's reasoning to concrete geographies in West Virginia and Appalachia, implemented as a **Generalized Bio‑inspired Machine** design and populated from the current, CSV‑converted GBIM corpus.

In Quantarithmia, GBIM is also where Tacets are instantiated: each ZIP‑ or county‑anchored region is treated as a founding key that sets local parameters and hosts a slowly varying Material Field \( \xi \), giving formal hooks for the community’s vibe to enter the Steward’s state rather than hovering as metaphor.

This chapter presents Ms. Jarvis as a glassbox AI Steward System and explains the Geospatial Belief Information Model underpinning its reasoning. The focus is on a rigorous, inspectable architecture for layered reasoning, memory, and judgment explicitly tied to geospatial entities, temporal context, evidential provenance, and the current state of local programs and institutions. Within Quantarithmia, Ms. Jarvis and GBIM serve as the technical realization of spatially grounded, justice‑oriented reasoning: they enable asking *“What does the Steward System hold about this place, for whom, under whose authority, and based on what evidence, and when was this last confirmed with the people involved?”* with auditable, contestable answers, now including live RAG‑based flows for Oak Hill, Beckley, and other West Virginia communities backed by the real GBIM + Chroma state you are actively maintaining.

---

## What GBIM Is

<div align="center">
  <img width="60%" alt="geospatial belief information model" src="https://github.com/user-attachments/assets/331685c5-977e-4b60-9a96-3150b71787a2" />
</div>

> Figure 1. High‑level structure of the Geospatial Belief Information Model (GBIM), showing the PostGIS geospatial corpus, CSV‑derived attributes, Chroma semantic collections, the production belief graph schema, the verified local resource registry, and the RAG/21‑LLM orchestration layer, all tied together by nine epistemic axes (who, what, where, when, how, why, for whom, under whose authority, on what evidence).

GBIM is Ms. Jarvis's internal model for tying beliefs to **who**, **what**, **where**, **when**, **how**, **why**, **for whom**, **under whose authority**, and **on what evidence**, focused on West Virginia and Appalachia. In the current deployment, those axes are populated from actual, converted shapefiles and services CSVs rather than from hypothetical source layers. The production system integrates five cooperating layers:

1. **PostGIS‑backed regional geospatial corpus** – The entities and geometries derived from the original shapefiles and geodatabases, now concretely realized through the GBIM tables and the CSV imports you just ran (such as `gbim_source_csv.*` and `gbim.gbim_attrs`) and keyed by `sourcetable` and `geodb_id`. The earlier “attrs only” limitation has been superseded by a CSV pipeline that reflects what you actually exported and use in practice.

2. **ChromaDB collections** – High‑dimensional embeddings and metadata for GBIM‑derived beliefs and texts, including collections such as `gbim_beliefs_v1`/`gbim_beliefs_v2` that you are now filling via `msjarvis_embed_gbim.py`, a consolidated spatial index, and dedicated collections like `gis_wv_benefits` for West Virginia benefits facilities. These collections are built directly from the GBIM rows and CSV‑fed axes, so their geometry is the geometry of your real corpus.

3. **Production belief graph schema** – The `gbimbeliefnormalized` table with its nine JSONB axes, together with any `gbim_worldview_entity`/edge tables, binding the PostGIS/CSV layers into a unified, inspectable worldview with explicit provenance and consistent identity keys (handling both underscore and non‑underscore variants via `COALESCE`).

4. **Verified local resource registry** – A Postgres table (`local_resources`) holding structured records for community programs (food, housing, utilities, seasonal assistance, senior services, education support, etc.), keyed by county and ZIP codes, with contact information, URLs, short descriptions, and a verification state machine (`verification_status`, `last_verified_at`, `verification_notes`). This registry is linked back to unstructured documents and CSVs via metadata (e.g., `source_url`, `source_file`), and forward into Ms. Jarvis’s reasoning via need tags, ZIP‑aware ranking, and explicit joins from Chroma hits to registry rows.

5. **RAG and 21‑LLM orchestration layer** – A text RAG service over Chroma, a GIS RAG service over GBIM/GeoDB‑derived features, a web research gateway, and a local resource resolver, orchestrated by a main‑brain service that calls a 21‑model ensemble (`llm20_production`). This layer turns the GBIM + CSV + registry state into live, logged retrieval and synthesis pathways for `/chat/light` and `/chat/sync`, using the same GBIM rows you enriched with `load_services_attrs_and_enrich.py`.

Each belief attaches to all nine epistemic axes, with values now grounded in your CSV‑backed enrichments rather than placeholder text:

<div align="center">
  <img width="60%" alt="Belief Neighborhood for One Building" src="https://github.com/user-attachments/assets/9855f916-dadd-46af-8276-60e797549932" />
</div>

> Figure 2. The nine epistemic axes in GBIM, showing how every belief is anchored simultaneously in actors, kinds, places, time, mechanisms, purposes, constituencies, authorities, and evidence, including beliefs about which local programs serve which ZIP codes, when this information was last verified, which CSV exports contributed attributes, and which RAG paths and collections were consulted in answering a live query.

- **Who** – persons, institutions, communities (actors, subjects, beneficiaries, decision‑makers), keyed to GBIM entity records and drawn from real fields in your CSV/GBIM corpus and resource registry (owner names, agencies, program sponsors, contact people). In the local resource registry, this includes named contacts such as case managers, program directors, and specialist staff for specific programs.

- **What** – the kind of thing or state (asset, event, obligation, harm/benefit), represented by feature classes, layer names (`sourcetable`), and CSV‑derived attributes that your enrichment scripts now push into the `what` axis (for example, `feature_type`, `geometry`, `domain`, and any per‑family attributes you chose to map), and by `resource_type` in the local resource registry (e.g., `seasonal_assistance`, `housing`, `utilities`, `senior_services`, `education_support`).

- **Where** – concrete places as PostGIS geometries (points, lines, polygons for buildings, census units, roads, districts, facilities, environmental features, community boundaries) and as service footprints over ZIP codes and counties. In the current deployment, these are populated from the CSV exports you processed (latitude, longitude, bbox, labels, sourcetable) and standardized to SRID 26917. The local resource registry ties those geometries to actual served ZIP codes and counties, so that when a resident in Oak Hill or Beckley asks for help, Ms. Jarvis can route them to programs whose coverage includes their actual ZIP.

- **When** – temporal metadata indicating belief formation/update time and evidential period. Production deployment: epoch labels and dataset vintages have been assigned across the corpus; the CSV‑driven enrichments ensured that `when` is non‑NULL for essentially all beliefs; each local resource record carries a `last_verified_at` timestamp indicating when its contact, eligibility, and coverage details were last confirmed; and RAG/ensemble queries are logged with timestamps so that “when the Steward last used this evidence” is auditable, including how recent the observations informing a local \( \xi \) estimate are for a given Tacet.

- **How** – mechanisms, processes, flows (service delivery, value/risk movement, rule application). The `how` axis is populated from your epoch metadata and CSV‑informed scripts, describing how each dataset or program comes into being (e.g., “licensed inpatient facility inventory,” “EPA compliance registry,” “SAMB structure mapping”), and your runtime logs record how RAG and the ensemble actually assembled answers (which collections, which queries, which registry rows).

- **Why** – motives, justifications, purposes (policy rationales, program goals, safety standards). The `why` axis is filled from your existing SQL enrichment scripts, capturing things like “provide rural health care,” “monitor environmental compliance,” or “ensure safe floodplain development.” The local resource registry also carries text describing each program’s purpose, making the “why” of local assistance pathways explicit.

- **For whom** – distributional effects across people and places (burden/benefit allocation). The `for_whom` axis is populated for all named epochs, and your real data encodes which communities benefit from which infrastructure, programs, and policy decisions. Resource records bind programs to particular constituencies (e.g., SNAP households in specific ZIPs, seniors in certain counties, teachers in high‑need subjects), and those bindings now steer RAG retrieval for benefit‑seeking queries.

- **Under whose authority** – laws, policies, institutional bodies authorizing or constraining conditions or actions. The `authority` axis is populated across the corpus from your enrichment SQL, linking features and programs to the agencies and statutes that ground them in law and institutional responsibility (for example, Clean Air Act, WV code sections, DHHR authority, county commission ordinances).

- **On what evidence** – structured links to data sources, documents, observations, and model outputs. In GBIM, provenance is explicit (dataset names, geodb IDs, epoch metadata, CSV source table names); in the resource registry, fields such as `source_url`, `url`, and `verification_notes` record which site, PDF, or contact was used and when; and in the RAG/ensemble layer, logs capture which Chroma collections, GBIM entities, CSV‑fed attributes, and `local_resources` rows were involved in each answer.

GBIM enforces that beliefs are never free‑floating—always anchored to specific actors, kinds, geographies, time frames, mechanisms, purposes, constituencies, authorities, evidential bases, and, for local programs, to a verification history and observable retrieval traces—using the actual CSV‑derived values now present in your database.

---

## How GBIM Is Represented

GBIM's representation combines graph‑style relationships with geospatial indexing, temporal/version history, Hilbert‑space embeddings over the CSV‑backed belief corpus, a normalized registry of community programs, a production RAG/ensemble service layer, and, in Quantarithmia, Tacet‑indexed parameters and a Material Field \( \xi \) so that differences in how places feel show up as differences in state, not just in narrative gloss. The current deployment fully implements all core layers using the actual data you have loaded, not imagined future schemas.

### Schema Layer

GBIM defines **entities**—places, infrastructures, events, policies, institutions, persons, communities—and their relationships, as they exist in your current Postgres and Chroma instances:

- **`gbimbeliefnormalized` table (PRODUCTION)** – The core belief table (≈10.2M rows), with JSONB columns for `identity`, `when`, `where`, `what`, `who`, `for_whom`, `why`, `how`, `authority`, updated via the CSV enrichment flows (`load_services_attrs_and_enrich.py`, epoch SQL scripts) so that each belief now carries both institutional and feature‑level context drawn from your real CSV exports.

- **`gbim_worldview_entity` / related GBIM tables** – Entity catalogs and edge tables (where present) that tie beliefs to stable IDs, worldviews, and relationships. These tables and the enrichment scripts use `COALESCE` on `identity->>'source_table'`/`identity->>'sourcetable'` and `identity->>'source_pk'`/`identity->>'sourcepk'` to handle both ingestion pipelines, ensuring that the CSV‑derived attributes join correctly across all 10M+ rows.

- **`gbim_source_csv.*` schema (PRODUCTION)** – A family of tables created from your `services/*_attrs.csv` files (227 CSVs), each holding the actual exported attributes from the original shapefiles, including `geodb_id`, `lat`, `lon`, `bbox`, `label`, `sourcetable`, `country`, and any extra columns you added. These are the current “source of truth” for per‑feature attributes and have already been used to enrich GBIM.

- **`local_resources` table (PRODUCTION)** – Normalized registry of community programs with fields such as:
  - Identity and classification: `id`, `name`, `resource_type`, `county`, `state`, `zip_codes` (JSON‑encoded list).  
  - Access and description: `phone`, `email`, `url`, `snippet`, `source_url`.  
  - Contact‑level details: `contact_name`, `contact_email`, `contact_phone`.  
  - Verification state: `verification_status`, `last_verified_at`, `verification_notes`.

  This table is linked to GBIM and Chroma via metadata, making the real, CSV‑derived institutional structure and your verification work visible to the Steward System.

- **RAG service schemas and logs (PRODUCTION)** – HTTP APIs (`/chat/light`, `/chat/sync`, `/gis_rag`, `/search`, `/store`) and internal logs that record queries, selected collections (including `gbim_beliefs_v2`), retrieved IDs, ensemble model responses, and guardrail actions, providing an “operational evidence” layer for how GBIM, CSV enrichments, and `local_resources` are actually used at runtime.

### Integrated Layers

**Graph relationships**  
Entities link via typed edges forming a belief graph for dependency, flow, and exposure analysis. In practice, these edges are either explicit (in GBIM edge tables) or implicit in how you query and join the axes:

- `how` relationships: link each entity to its dataset and enrichment pipeline, documenting how each belief is grounded in CSV imports, shapefile conversions, and epoch scripts.  
- `why` relationships: link beliefs and programs to their goals and rationales captured in the `why` axis and resource descriptions.  
- `for_whom` relationships: link entities and programs to their beneficiary populations and geographies, using both GBIM axes and `zip_codes`/`county` from `local_resources`.  
- `authority` relationships: link beliefs to the agencies and legal bases that authorize them.

The local resource registry is integrated by:

- Treating each program as an entity in Ms. Jarvis’s worldview, keyed to specific counties and ZIP codes and backed by CSV‑converted or manually curated data.  
- Linking resource records back to Chroma documents and GBIM entities via IDs and metadata so that unstructured retrieval can be resolved to structured truth.  
- Exposing these rows to the RAG layer, which uses GBIM embeddings and CSV‑derived metadata to find, rank, and explain available help for specific households and places.

**Concrete example: A single building’s belief and resource neighborhood**

A building footprint in Oak Hill:

- Has a row in `gbimbeliefnormalized` with `identity` (source table, geodb_id, label), `where` (lat/lon/bbox from CSV, SRID 26917), `what` (feature_type building, domain built_environment), `who` (e.g., local government or owner inferred from dataset), `for_whom` (residents, West Virginia public), `why` (housing or economic rationale), `how` (SAMB/structure mapping pipeline), and `authority` (state/county authority).  
- Embeds into `gbim_beliefs_v2` with a text representation produced by `msjarvis_embed_gbim.py`, so it participates in Hilbert‑space similarity searches.  
- Is associated, via ZIP and county, with `local_resources` entries such as weatherization programs, tax relief, DHHR benefits offices, or seasonal assistance programs, which carry real phone numbers, emails, URLs, and verification timestamps.

When a user asks, “What help is available near this building in Oak Hill?”, Ms. Jarvis:

- Uses the GBIM embedding (from `gbim_beliefs_v2`) and GIS RAG to understand the building, its neighborhood, and contextual features.  
- Uses ZIP and county from `where` to filter `local_resources` to programs that cover that location.  
- Uses RAG over CSV‑backed Chroma collections to bring in any relevant flyers, PDFs, or notes.  
- Logs which GBIM IDs, CSV‑derived metadata, and `local_resources` rows were used in the final answer.

This neighborhood is queryable via SQL against GBIM and `local_resources`, and explainable in natural language as “Here are the organizations that currently serve your ZIP, what they offer, how to apply, when this information was last confirmed, and which CSV exports, collections, and registries were consulted in answering your question.”

Production deployment characteristics (February 2026), grounded in your real corpus:

- ≈10.2M beliefs in `gbimbeliefnormalized`, all with populated `when`, `who`, `why`, `for_whom`, `how`, and `authority`, and enriched `where`/`what` based on your CSV pipeline.  
- 227 `*_attrs.csv` files imported into `gbim_source_csv.*` and used to enrich GBIM.  
- A growing set of embeddings in `gbim_beliefs_v2` produced by `msjarvis_embed_gbim.py`, directly reflecting the current GBIM + CSV state.  
- A `local_resources` registry that is expanding as you ingest more real program flyers, spreadsheets, and web pages.  
- A live RAG and 21‑LLM orchestration layer that uses all of the above to answer West Virginia geography and benefits questions with logged, inspectable retrieval traces grounded in your actual data, not in aspirational documentation.

