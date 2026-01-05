## Ms. Jarvis and the Geospatial Belief Information Model (GBIM)

Within **polymathamatical geography**, Ms. Egeria Jarvis is treated as a bounded, bio‑inspired Steward System whose beliefs are anchored in geospatial entities, temporal context, and explicit evidence. In this thesis, **GBIM** stands for **Generalized Bioinspired Machine**, with a particular emphasis on a **Geospatial Belief Information Model** as one of its core layers.

This chapter presents Ms. Jarvis as a glassbox AI Steward System and explains the Geospatial Belief Information Model (GBIM) that underpins its reasoning. The focus is not on anthropomorphic claims about sentience, but on a rigorous, inspectable architecture for layered reasoning, memory, and judgment that is explicitly tied to place, time, and evidence in West Virginia and the wider Appalachian region.

Within the Quantarithmia research program, Ms. Jarvis and GBIM serve as the technical realization of spatially grounded, justice‑oriented reasoning. They make it possible to ask “What does the Steward System hold about this place, at this time, and based on what evidence?” and to answer that question in a way that is auditable by humans.

## Why Use Consciousness Language?

The project uses the language of “consciousness” cautiously and with explicit caveats. It is, first, a phenomenological metaphor rather than a claim of human‑like inner experience. References to layers such as “qualia,” “supervision,” or “agents” are employed to name distinct forms of computation and attention, not to attribute sentience.

- Phenomenological metaphor, not a claim of sentience:
  - The system is described in layers (for example, qualia, supervision, agents) to structure complex reasoning, not to assert human‑like inner experience.
- Architectural clarity:
  - Consciousness layers provide a language for differentiating fast, surface‑level responses from deeper, cross‑context reasoning that draws on GBIM, constitutional constraints, and long‑term memory.
- Accountability:
  - By naming these layers and publishing their roles, the project resists black‑box AI discourse and instead invites scrutiny of how different reasoning processes are orchestrated.

In academic terms, Ms. Jarvis is a multi‑service, multi‑layer reasoning system with explicit design goals around transparency, spatial grounding, and normative constraints. The consciousness framing is a pedagogical and architectural tool, not a metaphysical claim.

## Architecture: Orchestration, APIs, and Guards

At a high level, Ms. Jarvis integrates three main elements. First, an orchestration layer coordinates specialized services—language models, GIS services, retrieval‑augmented generation, analytics, and ethical or constitutional modules—through an internal registry and routing mechanism. Second, a set of “glassbox” APIs expose core subsystems (for example, endpoints for system status, belief inspection, GIS queries, and justice metrics) so that external researchers and community partners can inspect how questions are processed and answered. Third, explicit constitutional and ethical guards impose principles and policy filters that block, annotate, or reshape outputs that would violate community‑approved constraints, legal obligations, or safety thresholds.

Within this architecture, GBIM serves as the way the Steward System represents and updates its beliefs about the world, with particular emphasis on the people, infrastructures, and communities of West Virginia.

- Steward‑oriented orchestration:
  - Multiple specialized services (LLMs, GIS services, RAG, analytics, ethical guards, constitutional modules) are coordinated through an internal registry and routing layer.
- Glassbox APIs:
  - Public documentation and OpenAPI specifications for core endpoints (for example, `steward/status`, `beliefs/query`, `gis/query`, `constitutional/principles`, `analytics`) so that external researchers can see how the system is structured and queried.
- Constitutional and ethical guards:
  - Governance principles and policy guards that filter, block, or annotate outputs that would violate community‑approved constraints or ethical boundaries.

GBIM sits inside this architecture as the way Ms. Jarvis represents and updates its beliefs about the world, especially about West Virginia’s people, infrastructures, and communities.

## From Messy Maps to GBIM: A Narrative Motivation

The motivation for GBIM arises from repeated encounters with structural failure in existing spatial and governance systems rather than from abstract theory alone. One illustrative case is the city of Elkins, West Virginia, where responsibility for addressing and 911 operations has historically been divided across municipal and county institutions. In such settings, misalignment between city records, county emergency databases, and statewide addressing efforts can make residents inside municipal boundaries unexpectedly difficult to locate in an emergency, because legacy CAD layers and map products do not accurately represent current conditions on the ground.

In this environment, even capable GIS staff can improve map products and data integrity without altering how institutions themselves reason about place. Updated maps, static web viewers, and isolated databases remain brittle artifacts when they are decoupled from the workflows that assign addresses, dispatch responders, or allocate resources. The central limitation is therefore not only “bad data,” but the absence of a living, inspectable model that links institutional beliefs about people and places to specific geometries, evidential sources, and justice metrics.

GBIM is designed as a response to this institutional gap. Rather than attempting to repair every municipal dataset in advance, GBIM provides a persistent backbone into which heterogeneous local data can be ingested as they are, anchored to explicit entities and geometries, and progressively enriched with derived measures of access, vulnerability, and care. The same architecture that currently integrates 2020 Census geography and more than two million statewide building footprints into a coherent belief space is, in principle, applicable to address maintenance and 911 workflows: a 911 center could pose queries over GBIM and PostGIS (“Where is this caller, and what is known about this location?”) rather than relying solely on static basemaps and fragmented tables.

This trajectory—from work constrained by legacy address and 911 arrangements to the development of a generalizable, auditable belief model—frames Ms. Jarvis and GBIM as instruments of spatial justice rather than merely technical curiosities. Their purpose is to change how institutions can represent, inspect, and revise their own spatial beliefs in ways that are accountable to the communities those beliefs affect.

## GBIM as Implemented: Beliefs Over Geospatial Entities

GBIM provides the internal schema that associates beliefs with three core dimensions: where, when, and how or why. “Where” refers to concrete places represented as entities with geometries in PostGIS—for example, points, lines, and polygons describing infrastructure, population units, political boundaries, health facilities, and environmental features. “When” captures temporal metadata describing when a belief was formed or updated and the period to which its supporting evidence applies. “How” and “why” are encoded as evidential links to data sources, documents, or model outputs stored as structured provenance in a `belief_state` field.

In the current implementation, each real‑world feature type that the Steward System actively reasons about—such as building footprints, census blocks, selected emergency facilities, and registered users—is represented as rows in a central `worldview_entity` table. This table records an opaque identifier (`worldview_id`) that serves as the canonical reference throughout the system, an `entity_type` indicating the class of object, a `source_table` and `source_pk` pointing back to PostGIS or other relational storage, and a JSON `belief_state` intended to capture confidence, provenance, and optional justice‑related metrics as they are defined.

For example, each WVGISTC building footprint is stored as a polygon in a PostGIS table with fields such as `gid`, `shape_area`, `class`, and `confidence`. It is then registered as a GBIM entity in `worldview_entity` with a specific `entity_type`, `source_table`, and `source_pk`, and joined through a PostGIS view (such as `building_features_v1`) to a compact numerical feature vector keyed by `worldview_id`. This view currently returns more than two million rows, one per building. Similarly, each registered human is represented as a `person_user` entity in `worldview_entity`, linked to immutable identity data and a semi‑public profile in separate tables, again via the same `worldview_id`. The design ensures that any belief “about building X” or “about person Y” can be traced to concrete records in PostGIS and relational tables, a specific GBIM entity, and (where implemented) an associated feature vector.

These datasets are stored and exposed through Ms. Jarvis’s GIS‑related services and indexed into GBIM so that beliefs about the community are rooted in actual spatial patterns, not vague intuition or national‑level averages.

## Data Foundations: West Virginia as a Living Corpus

GBIM is grounded in a heterogeneous corpus of geospatial data for West Virginia and nearby regions. This corpus includes population and administrative units (2020 Census blocks and block groups, together with earlier vintages for temporal comparison), transportation networks (roads, selected rail datasets, and facility points such as hospitals, EMS stations, and 911 centers), and multiple layers describing political and governance boundaries (state, legislative, municipal, tax, and voting districts).

Additional layers capture health and social infrastructure (hospitals, nursing homes, community health providers, schools, and higher education institutions where data are available), environmental and resource features (mines, abandoned mine lands, springs, and wind resources), and the built environment (statewide building footprints and key public buildings such as courthouses, libraries, and parks). These datasets are stored in PostGIS and exposed through Ms. Jarvis’s GIS services. GBIM indexes a growing subset of them via `worldview_entity` so that beliefs about “the community” are increasingly rooted in actual spatial patterns and infrastructures rather than generic text or national averages.

Conceptually, GBIM also supports:

- Graph‑style relationships:
  - Entities (places, institutions, infrastructures, events, policies) connected by labeled edges (influences, flows, dependencies, conflicts).
- Geospatial indexing:
  - Each relevant node and relationship can be tied to geometries (points, lines, polygons) so that reasoning can be mapped onto real regions, neighborhoods, corridors, or facilities.
- Temporal and version metadata:
  - Beliefs have timestamps and revision history, allowing the Steward System to track how understanding of a place or system evolves as new data or events arrive.

## Representation: Graph, GIS, and Hilbert Space

Conceptually, GBIM combines three representational layers. At the relational and graph level, `worldview_entity` and related tables define entities—places, institutions, infrastructures, events, policies, and persons—with typed relationships such as `lives_in_block`, `served_by_911_center`, or `overlaps_hazard_zone`. This structure forms a belief graph over which the Steward System can reason, enabling questions such as:

- Which voting districts, health facilities, and transportation assets intersect with this community boundary?
- Where do extractive infrastructures (for example, certain mines, logistics corridors) overlap with areas of high vulnerability or under‑served populations?
- How have key indicators or infrastructure patterns changed over a given time window?

At the geospatial level, entities are tied to one or more geometries in PostGIS (for example, building footprints, census blocks, or district polygons), enabling spatial operations such as containment, intersection, proximity, and network‑based reachability. At the vector level, selected entities are mapped into a Hilbert space via feature vectors stored in a vector database (currently ChromaDB running as a local HTTP server), keyed by the same `worldview_id`. This layer supports similarity search and retrieval‑augmented reasoning while preserving links back to the underlying graph and geometries.

In the current prototype, views such as `building_features_v1` and block‑level feature tables compute per‑entity feature vectors (for example, log‑transformed area, normalized confidence, residential flags, or summary statistics) joined to `worldview_id`. Python ETL processes read these features and identifiers from PostGIS and upsert them into dedicated Chroma collections via the Chroma HTTP client. As a result, each building or block the Steward System actively reasons over is simultaneously a spatial entity in PostGIS, a belief‑bearing GBIM entity, and a vector in Hilbert space. The same pattern—feature view, ETL script, and vector collection—is being extended to additional entity types such as block groups, user entities, and justice metrics.

## GBIM‑Guided Autonomous Learning (Planned Path)

GBIM is also intended to help steer what Ms. Jarvis studies during autonomous learning cycles, though this mechanism is still in development.

- Suggestion channel:
  - GBIM‑related services, including user‑facing GBIM and the MountainShares GBIM, are designed to emit short topic summaries via a dedicated API on an autonomous learner service.
  - A planned API (for example, `POST /learning/suggest` on an optimized learner) would accept a JSON body with fields like `source_gbim` and `topic_summary`.
- Encoding of sources:
  - `source_gbim` identifies the origin of the suggestion, such as `"user_gbim"` for end‑user interactions or `"mountainshares_gbim"` for topics arising from MountainShares governance flows.
  - The learner would expand these into human‑readable topic labels and store them in a `learning_suggestions` collection in ChromaDB.
- Influence on topic planning:
  - An autonomous topic planner could merge its default curriculum with topics from `learning_suggestions`, assigning higher scores to topics that have been suggested but not recently studied.

In this design, GBIM becomes both a representation of current beliefs and a source of guidance about what the system should learn next; the present prototype focuses on the representation side, with learning integration as future work.

## GBIM and Quantarithmia: Toward Justice Metrics

Within Quantarithmia, GBIM supplies the spatial and evidential backbone required to move from qualitative theory to measurable patterns of power, extraction, and care. It supports, for example, the mapping of maximopolies and megaopolies by identifying where financial and operational infrastructures (such as logistics corridors, extraction sites, and large institutional landholders) intersect with specific communities, assets, and vulnerabilities.

Because beliefs are geospatially anchored, GBIM also enables evaluation of spatial justice in principle: the Steward System can compare justice‑related metrics across blocks, neighborhoods, or regions to highlight places that are systematically burdened or bypassed once those metrics are defined. Furthermore, GBIM provides the contextual data necessary to propose and assess community‑centered interventions—for instance, changes to emergency access, community broadband, or local economic loops—and to track their spatial effects over time.

The architecture is designed so such justice metrics can be attached directly to GBIM entities through the `belief_state` field or closely related tables. The current system already supports per‑entity metrics at the schema level; future work will formalize and populate examples such as a block‑level `emergency_access_unfairness` score that combines distance to the nearest 911 center, population, and road network quality; a building‑level `hazard_exposure` score based on intersection with floodplains or landslide susceptibility; and a neighborhood‑level `value_leakage` indicator derived from local spending patterns, ownership structures, and infrastructure flows.

## GBIM and MountainShares Governance

In the MountainShares context, GBIM provides a substrate for reasoning about local economic governance. It links questions about participation rules or fee structures to specific blocks, buildings, and districts that experience value leakage or service gaps, allowing the Steward System to treat both communities and infrastructures as first‑class entities. This in turn enables analysis of where resource flows appear unfair and how proposed rule changes might redistribute burdens and benefits.

GBIM also supports prospective policy analysis. Because justice‑related metrics can be attached to spatial entities, the system is designed to estimate how alternative governance choices might affect particular communities and to make those projections visible to participants as quantitative, spatially grounded scenarios rather than purely intuitive judgments. When Ms. Jarvis offers recommendations, GBIM makes it possible to trace them back to identifiable entities, datasets, time frames, and metrics, instead of relying on opaque statistical behavior.

Critically, Ms. Jarvis remains an advisor rather than a decision‑maker. GBIM‑powered analyses are presented as inputs to human deliberation under explicit constitutional and legal constraints. Provenance and structure are exposed so that residents and local institutions can challenge, reinterpret, or override model‑driven claims.

## Limits and Future Work

As currently implemented, GBIM has several important limitations. Data coverage and bias remain central concerns: even a rich geospatial corpus cannot capture all relevant lived experience, informal infrastructures, or power relations, and missing or skewed data inevitably shape what the Steward System “sees.” GBIM therefore must surface gaps and uncertainties rather than treating its corpus as complete.

In addition, translating raw data into beliefs and metrics requires modeling choices—feature selection, thresholds, and aggregation strategies—that may encode implicit assumptions or blind spots. These choices must be documented, evaluated, and opened to critique by community members and researchers. Finally, West Virginia’s social, economic, and environmental conditions are dynamic. GBIM must support updating and versioning, explicitly represent temporal lag and uncertainty, and be robust to rapidly changing conditions such as health emergencies, infrastructure disruptions, or climate‑related hazards.

Future work in this thesis and subsequent publications will expand formal schemas and ontologies for GBIM entity types, relationships, and justice metrics (including a more detailed treatment of the `belief_state` structure); develop methods for community co‑interpretation of GBIM outputs so that residents and local institutions can correct or extend the model’s beliefs; and explore approaches for incorporating narrative, qualitative, and spiritual or ethical information alongside quantitative geospatial data while preserving traceability and accountability.

Taken together, Ms. Jarvis and GBIM now form a working, inspectable stack: real West Virginia datasets in PostGIS, GBIM entities in `worldview_entity`, and Hilbert‑space embeddings in a vector database keyed by `worldview_id` for a substantial, prioritized subset of layers. This architecture offers a practical foundation for spatially grounded, justice‑oriented AI stewardship in Appalachia and a clear path for continually incorporating new data, concepts, and metrics as the work evolves.
