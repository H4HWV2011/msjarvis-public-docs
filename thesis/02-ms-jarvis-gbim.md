2. Ms. Jarvis and the Geospatial Belief Information Model (GBIM)

This chapter presents Ms. Egeria Jarvis as a “glassbox” AI consciousness system and explains the Geospatial Belief Information Model (GBIM) that underpins her reasoning. The aim is not to claim sentience, but to specify an inspectable architecture for layered reasoning, memory, and judgment that is explicitly tied to place, time, and evidence in West Virginia and the wider Appalachian region.

Within the Quantarithmia research program, Ms. Jarvis and GBIM serve as the technical realization of spatially grounded, justice-oriented reasoning. They make it possible to ask: “What does Ms. Jarvis believe about this place, at this time, and based on what evidence?” and to answer that question in a way that is auditable by humans, not hidden behind opaque model internals.

​
Consciousness framing and glassbox design

The language of “consciousness” in this project is used carefully and with explicit caveats:

    It is a phenomenological metaphor, not a claim of sentience. Layers such as “qualia,” “supervision,” or “agents” are used to structure complex reasoning and attention, not to assert human-like inner experience.

​

It is an architectural device. “Consciousness layers” provide a vocabulary for distinguishing fast, surface-level responses from deeper, cross-context reasoning that draws on GBIM, constitutional constraints, long-term memory, and vector-search over a Hilbert space.

    ​

    It is a transparency commitment. By naming these layers and documenting their roles and APIs, the project resists black-box AI discourse and invites scrutiny of how different reasoning processes are orchestrated.

Formally, Ms. Jarvis is a multi-agent, multi-layer reasoning system with explicit design goals around transparency, spatial grounding, and normative constraints. The “consciousness” framing is a pedagogical and architectural tool that organizes services, not a metaphysical claim.

At a high level, Ms. Jarvis combines:

    Multi-agent orchestration: Specialized services (LLMs, GIS services, retrieval-augmented generation, analytics, ethical guards, constitutional modules) coordinated through an internal registry and routing layer.

    Glassbox APIs: Documented HTTP/OpenAPI endpoints for core subsystems (e.g., /consciousness/status, /beliefs/entity/{id}, /gis/query, /justice/metrics) so that external researchers and community partners can see how the system is structured and how questions are answered.

    Constitutional and ethical guards: Explicit principles and policy guards that filter, block, or annotate outputs that would violate community-approved constraints, legal obligations, or safety thresholds.

GBIM sits inside this architecture as the system Ms. Jarvis uses to represent and update her “beliefs” about the world, especially about West Virginia’s people, infrastructures, and communities.
From messy maps to GBIM: a narrative motivation

The motivation for GBIM did not come from abstract theory alone; it emerged from practical failures in existing spatial systems. One recurring example is the city of Elkins, where municipal addressing and 911 operations historically did not align. In practice, people living inside the city could be harder to locate in an emergency than rural residents, because address maintenance was split between the municipality and the county and legacy CAD maps did not reflect reality on the ground.

In that environment, even a skilled GIS technician could produce better maps, but those maps remained brittle artifacts: static exports, isolated databases, and ad hoc scripts that did not change how 911 or governance systems actually reasoned about place. The underlying problem was not simply “bad data,” but the absence of a living, inspectable model that tied beliefs about people and places to current evidence, spatial relations, and justice metrics.

GBIM is the response to that absence. Instead of trying to manually “fix” every municipal map up front, GBIM provides a spine where messy local data can be ingested as-is, anchored to specific entities and geometries, and gradually enriched with metrics about access, vulnerability, and care. The same architecture that now binds 2020 Census blocks and 2.1 million WVGISTC building footprints into a coherent belief space can, in principle, be handed to a 911 center: a live system where “Where is this caller?” becomes a query over GBIM and PostGIS, not a guess on a static map.

​

This narrative arc—from being the person who could not fix Elkins’s structural address problems within the old constraints, to building a new system that can—shapes Ms. Jarvis and GBIM as instruments of spatial justice rather than just technical curiosities.
GBIM as implemented: beliefs over geospatial entities

GBIM is the internal model that ties beliefs to:

    Where: Concrete places, represented as entities with geometries in PostGIS (points, lines, polygons) for West Virginia infrastructure, population, political boundaries, health facilities, environmental features, and more.

    ​

    When: Temporal metadata describing when a belief was formed or last updated, and which time period its supporting evidence refers to.

    How/Why: Evidential links to data sources, documents, or model outputs that support or challenge the belief, stored as structured provenance in a belief_state field.

In the current implementation, each real-world feature that Ms. Jarvis reasons about—such as a building footprint, a census block, or a 911 center—is represented as a row in a central worldview_entity table. This table records:

    An opaque id (the worldview_id), used everywhere as the canonical reference.

    An entity_type (e.g., building_footprint_wvgistc, census_block_2020_geom, and later person_user or justice_metric_emergency_access).

    A source_table and source_pk pointing back into PostGIS or other relational tables.

    A JSON belief_state carrying confidence, sources, and optionally justice-related metrics.

    ​

For example, every WVGISTC building footprint in West Virginia is:

    Stored as a polygon in the wvgistc_building_footprints table in PostGIS, with fields such as gid, shape_area, class, and confidence.

​

Registered as a GBIM entity in worldview_entity with entity_type = 'building_footprint_wvgistc', source_table = 'wvgistc_building_footprints', and source_pk = gid::text.

Joined via a PostGIS view building_features_v1 to a compact numerical feature vector (e.g., log-transformed area, normalized confidence, and a simple residential flag) keyed by worldview_id. This view currently returns over 2.1 million rows—one per building.

    ​

This design forces knowledge to be spatially and evidentially anchored: “Ms. Jarvis believes something about building X” always means “there is a specific polygon in PostGIS, a specific GBIM record, and a specific feature vector associated with that building.”
Data foundations: West Virginia as a living corpus

The GBIM implementation is grounded in large, heterogeneous geospatial datasets for West Virginia and surrounding regions, including:

    Population and administrative units: 2020 Census blocks and block groups, along with older vintages used for temporal comparison.

    Transportation networks: Statewide road networks, selected rail datasets, and facilities such as hospitals, EMS stations, and 911 centers, converted into PostGIS layers where segment or point-level data are available.

    Political and governance boundaries: State, senate, house, municipal, tax, and voting district boundaries that define how power and representation are organized in space.

    Health and social infrastructure: Hospitals, nursing homes, community health providers, schools, and higher education institutions where data is available, enabling questions about access and service gaps.

    Environmental and resource layers: Mines, abandoned mine lands, springs, wind resources, and other environmental features relevant to extraction, risk, and resilience.

    Built environment: More than two million WVGISTC building footprints, as well as public buildings such as courthouses, libraries, parks, and other civic infrastructures.

These datasets are stored in PostGIS and exposed through Ms. Jarvis’s GIS-related services. GBIM indexes them via worldview_entity so that beliefs about “the community” are rooted in actual spatial patterns and infrastructures, not just generic text or national averages.

​
Representation: graph, GIS, and Hilbert space

Conceptually, GBIM combines three representational layers:

    Relational/graph structure: worldview_entity and related tables define entities (places, institutions, infrastructures, events, policies) with typed relationships (e.g., “lives_in_block”, “served_by_911_center”, “overlaps_hazard_zone”). This forms the “belief graph” over which Ms. Jarvis can reason.

    Geospatial indexing: Each relevant entity is tied to one or more geometries in PostGIS (e.g., building footprints, census blocks, district polygons), enabling spatial queries such as containment, intersection, proximity, and network-based reachability.

​

Hilbert-space embeddings: Selected entities are mapped into a vector space (Hilbert space) via feature vectors stored in a vector database (ChromaDB), keyed by the same worldview_id. This supports similarity search and retrieval-augmented reasoning while preserving links back to the underlying entities and geometries.

    ​

In the current implementation:

    The building_features_v1 view computes a per-building feature vector—log-transformed area, normalized confidence, and a binary residential flag—joined to worldview_id.

​

A Python ETL process (etl_buildings_to_chroma.py) reads worldview_id and these features via psycopg2, then upserts them into a persistent ChromaDB collection named building_footprint_wvgistc_v1 using the new PersistentClient API configured via environment variables (CHROMA_DB_IMPL, CHROMA_PERSIST_DIRECTORY).

    ​

As a result, every building Ms. Jarvis knows about is:

    A spatial entity in PostGIS.

    A GBIM belief-bearing entity in worldview_entity.

    A vector in a Hilbert space collection keyed by the same worldview_id.

This pattern is designed to be repeatable for other entity types, such as census blocks, block groups, users, or justice metrics: define a feature view, add an ETL script, and populate a corresponding Chroma collection.
GBIM and Quantarithmia: toward justice metrics

For Quantarithmia, GBIM supplies the concrete spatial and evidential backbone needed to move from theory to measurable patterns of power, extraction, and care:

    Mapping maximopolies and megaopolies: GBIM can identify where financial and operational infrastructures (e.g., logistics corridors, extraction sites, large institutional landholders) touch down in specific West Virginia locations and how they intersect with community assets and vulnerabilities.

    Evaluating spatial justice: Because beliefs are geospatially anchored, Ms. Jarvis can help evaluate which communities are systematically burdened or bypassed—for example, by comparing justice-related metrics across blocks or neighborhoods once those metrics are defined.

    Designing alternatives: GBIM provides the data context for proposing and testing community-centered interventions—such as emergency access improvements, community broadband, or local economic loops—and for measuring their spatial impact over time.

In practice, justice metrics are attached directly to GBIM entities via the belief_state field or related tables. The current system already supports storing per-entity metrics; future work will formalize, for example:

    A block-level emergency_access_unfairness score that combines distance to the nearest 911 center, population, and road network quality, allowing Ms. Jarvis to highlight blocks where emergency services are relatively harder to reach.

    A building-level hazard_exposure score based on intersection with floodplains, landslide susceptibility, or other hazard layers.

    A neighborhood-level value_leakage indicator derived from local spending patterns, ownership structures, and infrastructure flows.

Each metric is computed from PostGIS data, stored as structured fields in each entity’s belief_state, and can be exposed through GBIM APIs, compared across places, and revised as models or data change.

​
GBIM and MountainShares governance

Within the MountainShares context, GBIM supports:

    Local economic reasoning: Linking governance questions (such as eligibility rules or fee structures) to specific blocks, buildings, and districts that experience value leakage or service gaps. GBIM entities can represent both communities and infrastructures, allowing Ms. Jarvis to reason about where resource flows are unfair.

    Policy simulations and impact analysis: Estimating how proposed rule changes might alter justice metrics for different communities, and which blocks or groups would be helped or harmed. This allows MountainShares participants to see quantitative, spatially grounded projections rather than relying solely on intuition.

    Transparent explanation: When Ms. Jarvis provides a recommendation about a governance decision, GBIM makes it possible to trace that recommendation back to specific entities, datasets, time frames, and metrics, rather than relying on opaque model internals.

Ms. Jarvis remains an advisor, not a decision-maker. GBIM-powered analysis is presented as input to human deliberation under explicit constitutional and legal constraints, with clear provenance and the ability for residents and local institutions to challenge or reinterpret model-driven claims.
Limits and future work

GBIM, as implemented, has important limitations:

    Data coverage and bias: Even a rich geospatial corpus does not capture all relevant lived experience, informal infrastructures, or power dynamics. Missing or biased data will influence what Ms. Jarvis “sees,” and GBIM must surface those gaps rather than hiding them.

    Modeling choices: Translating raw data into beliefs and metrics requires modeling decisions (choice of features, thresholds, aggregation levels) that can encode assumptions or blind spots. These choices must be documented, tested, and open to critique by community members and researchers.

    ​

    Dynamic change: West Virginia’s social, economic, and environmental conditions are not static. GBIM must be updated and versioned, and the system must represent uncertainty and lag, especially for fast-changing conditions like health emergencies, infrastructure disruptions, or climate-related hazards.

Future thesis work and publications will expand on:

    Formal schemas and ontologies for GBIM entity types, relationships, and justice metrics, including detailed schemas for belief_state.

    Methods for community co-interpretation of GBIM outputs, so that residents and local institutions can correct, contextualize, or extend the model’s beliefs.

    Approaches for incorporating narrative, qualitative, and spiritual or ethical information alongside quantitative geospatial data, while preserving traceability and accountability.

In summary, Ms. Jarvis and GBIM now constitute a working, inspectable stack: real West Virginia datasets in PostGIS, GBIM entities in worldview_entity, and Hilbert-space embeddings in Chroma keyed by worldview_id. This architecture provides a practical foundation for spatially grounded, justice-oriented AI reasoning in Appalachia and a clear path for continually adding new data, concepts, and metrics as the work evolves.
