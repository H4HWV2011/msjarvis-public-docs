> **Why this matters for Polymathmatic Geography**  
> This chapter specifies how Ms. Jarvis’s semantic memory is implemented in practice, turning abstract Hilbert‑space state and GBIM entities into a concrete, inspectable memory system. It supports:  
> - **P1 – Every where is entangled** by storing texts, GIS features, governance rules, and spiritual/contextual materials in shared collections that can be jointly retrieved and analyzed.  
> - **P3 – Power has a geometry** by representing institutional and spatial relationships as vectors and metadata that can be queried and clustered to reveal patterns of extraction, access, and obligation.  
> - **P5 – Design is a geographic act** by treating collection design, metadata schemas, and index parameters as deliberate interventions into how a region’s knowledge and memory are structured.  
> - **P12 – Intelligence with a ZIP code** by binding memory collections to West Virginia–specific spatial layers, governance documents, and community narratives.  
> - **P16 – Power accountable to place** by making Ms. Jarvis’s long‑term memory explicit, queryable, and auditable, rather than hidden inside opaque model parameters.  
> As such, this chapter belongs to the **Computational Instrument** tier: it defines the semantic memory substrate on which Quantarithmia’s reasoning, GBIM’s belief structures, and MountainShares‑oriented governance analysis actually run.

## 5. ChromaDB as Semantic Memory

### 5.1 Purpose and Scope

This chapter explains how Ms. Egeria Jarvis uses ChromaDB as the primary semantic memory layer backing the Hilbert‑space state, GBIM, and the broader semantic fabric. ChromaDB is a vector database that stores high‑dimensional embedding vectors with associated metadata and exposes efficient similarity search and filtering operations. In this system, ChromaDB is not merely a convenience library; it is the concrete implementation of long‑term, queryable memory for documents, GIS features, governance texts, autonomous‑learning traces, and thesis materials.

Within the Quantarithmia program, ChromaDB is treated as the bridge between abstract Hilbert‑space state and actual stored knowledge. It is the place where beliefs, contexts, and references become durable and retrievable for reasoning and retrieval‑augmented generation (RAG). Conceptually, each collection corresponds to a subset of the Hilbert space, and stored vectors approximate elements of the spaces described in the previous chapter.

---

### 5.2 Role in the Ms. Jarvis Architecture

In the Ms. Jarvis architecture, ChromaDB plays several interlocking roles.

- **Semantic memory store (non‑spatial).**  
  Embeddings of texts and artifacts live in collections corresponding to domains such as governance, thesis content, autonomous learner outputs, conversations, and curated user‑memory–like traces. These collections support general semantic retrieval independent of geography.

- **Geospatial Hilbert layer (spatial).**  
  A large family of GIS‑derived collections holds embeddings and metadata for West Virginia geospatial features, mirroring PostGIS tables and providing the Hilbert‑space representation of the spatial body described in the GBIM chapter. These collections connect directly to GeoDB entities and geometries.

- **Retrieval engine for RAG.**  
  At query time, services embed inputs and use ChromaDB similarity search, often with metadata filters, to retrieve the most relevant items for context and reasoning. This behavior instantiates the query projection and neighborhood selection mechanisms described in the Hilbert‑space model.

- **Structural backbone for inspectable memory.**  
  Because collections and metadata are explicitly defined, ChromaDB’s structure mirrors core parts of GBIM, the GeoDB layer, and the thesis organization. This makes it possible to enumerate collections, inspect document counts, and audit metadata, rather than relying on hidden internal state.

This design makes the semantic memory system inspectable and debuggable: researchers and community partners can see what is stored, how it is grouped, and which collections underpin particular advisory behaviors.

---

### 5.3 Collections and Data Domains

In the deployment examined in late 2025 and early 2026, the primary Chroma instance exposes a concrete set of collections that fall into two broad families: general semantic memory and GeoDB‑derived spatial memory. This section describes the collections actually present in this deployment and their intended semantics. Collection names and schemas are documented in the system’s registry and may evolve in a controlled, versioned manner.

#### 5.3.1 General Semantic Collections

In the current deployment, the principal general‑semantic collections are:

- `autonomous_learning`  
- `research_history`  
- `gbim_msjarvis_corpus`  
- `gbim_cakidd_personal_docs`  
- `msjarvis_hilbertspace`  
- `msjarvis_learner_corpus`  

These collections correspond to distinct data domains:

- **Learner and research history.**  
  `autonomous_learning` and `research_history` are intended to store web‑research outputs, per‑cycle summaries, and RAG traces emitted by the autonomous learner. In this snapshot, `autonomous_learning` contains a minimal number of embeddings, while `research_history` is present with zero embeddings and functions as an empty but reserved namespace.

- **GBIM‑oriented corpora.**  
  `gbim_msjarvis_corpus` and `gbim_cakidd_personal_docs` are intended to hold GBIM‑relevant documents and personal corpus materials used for Ms. Jarvis’s place‑based reasoning. Both collections currently exist with zero embeddings, indicating that their population is planned work rather than completed ingestion.

- **Hilbert‑space and learner corpora.**  
  `msjarvis_hilbertspace` and `msjarvis_learner_corpus` are likewise present but empty in this deployment. They are reserved for future embeddings that will bind specific Hilbert‑space state and learner traces into dedicated, queryable collections.

Earlier design documents referred to additional collections such as `conversations`, `ms_jarvis_memory`, `user_memory_vectors`, `mountainshares_knowledge`, `spiritual_wisdom`, and `thesis_materials`; those names represent design intents across the broader program, but they are not present as populated collections in the specific Chroma instance examined here and should not be described as active in this deployment without further ingestion.

Overall, general semantic memory is structurally defined but only partially realized in this Chroma store: several key collections exist but have not yet been populated with embeddings or documents.

#### 5.3.2 GeoDB‑Derived Spatial Collections

A second, much larger family of collections is generated automatically from the PostGIS GeoDB and represents the embedding‑space realization of GBIM’s spatial body. In the current deployment, these appear as `*_attrs` collections tied to specific West Virginia GIS datasets rather than the earlier `geodb*` / `gedb*` naming convention. Representative examples include:

- **Census and boundary layers.**  
  - `statewide_counties` (55 embeddings)  
  - `wv_county_boundaries_24k_topo_updated_2022_utm83_attrs` (55 embeddings, referenced by `statewide_counties` metadata)  
  - multiple state legislative district layers such as:  
    - `wvstatehousedistricts_manysources_1992_ll83_attrs`  
    - `wvstatehousedistricts_manysources_1992_utm83_attrs`  
    - `wvstatehousedistricts_manysources_2002_ll83_attrs`  
    - `wvstatehousedistricts_manysources_2002_utm83_attrs`  
    - `wvstatehousedistricts_wvlegislativeservices_2020_utm83_attrs`  
    - `stateofwvhousedistricts_wvlegislativeservices_2010_attrs`  
    - `wvstatesenatedistricts_manysources_1992_ll83_attrs`  
    - `wvstatesenatedistricts_manysources_1992_utm83_attrs`  
    - `wvstatesenatedistricts_manysources_2002_ll83_attrs`  
    - `wvstatesenatedistricts_manysources_2002_utm83_attrs`  
    - `wvstatesenatedistricts_wvlegislativeservices_2020_utm83_attrs`  
    - `stateofwvsenatedistricts_wvlegislativeservices_2010_attrs`  
  - statewide boundary layers such as:  
    - `wvstateboundary100k_usgs_200203_ll83_attrs`  
    - `wvstatebounadary100k_usgs_200203_utm83_attrs`  
    - `wvstateboundary24k_usgs_200203_ll83_attrs`  
    - `wvstateboundary24k_usgs_200203_utm83_attrs`  

- **Infrastructure and hazard layers.**  
  - `minesabandonedlandspolygon_wvdep_1996_noprojection_attrs`  
  - `minesabandonedlandspoint_wvdep_1996_noprojection_attrs`  
  - `minesabandonedlandsline_wvdep_1996_noprojectoin_attrs`  
  - `railnetworkwv_usdot_200203_ll83_attrs` and `railnetworkwv_usdot_200203_utm83_attrs`  
  - `sewertreatmentplants_wvdep_200203_utm83_attrs`  
  - `boundaryappalachianbasin_wvges_1996_utm83_attrs`  

- **Facilities and civic entities.**  
  - `hospitals_wvdem_040519_utm83_attrs` and `hospitals_wvdem_040519_gcs84_attrs`  
  - `hospitalswvdem040519utm83_attrs` (present but with zero embeddings in this snapshot)  
  - `nursinghomes_wvdem_041219_utm83_attrs` and `nursinghomes_wvdem_041219_gcs84_attrs`  
  - `fire_dept_wvdem_092017_utm83_attrs`  
  - `policedept_wvdem_012319_utm83_attrs` and `policedept_wvdem_012319_gcs84_attrs`  
  - `communityhealthproviders_wvhealthcareauthority_200802_utm83_attrs`  
  - `countycityparkboundaries_20201104_utm83_attrs`  
  - `officebuildings_wvdo_200807_utm83_attrs`  
  - `industrialbuildings_wvdo_200807_utm83_attrs`  
  - `industrialsites_wvdo_200807_utm83_attrs`  
  - `highered_wvemd_072420_utm83_attrs` and `highered_wvemd_072420_wgc84_attrs`  
  - `911centers_wvdem_032819_utm83_attrs` and `911centers_wvdem_032819_gcs84_attrs`  

- **Built‑environment and imagery layers.**  
  - `wvgistcbuildingfootprints_attrs`  
  - `wvgistc_building_footprints_attrs`  
  - `wv_microsoft_20180207_utm17n83_attrs`  
  - `historicalaerialphotographycountycoverage_wvgistc_utm83_attrs`  

- **Historic and governance‑relevant features.**  
  - National Register of Historic Places–related collections such as:  
    - `natoinalregisterofhistoricplacespoints_nationalparkser_ca43510e_attrs`  
    - `nationalregisterofhistoricplacespoints_nationalparkser_45ec46d0_attrs`  
    - `nationaregisterofhistoricplacespoints_nationalparkserv_ba8eebd5_attrs`  
    - `nationaregisterofhistoricplacespolygons_nationalparkse_cab42150_attrs`  
    - `nationalregisterofhistoricplacespolygons_nationaparkse_b9d30a70_attrs`  
  - `regionalplanninganddevelopmentcouncil_wvdo_1971_ll83_attrs` and `regionalplanninganddevelopmentcouncil_wvdo_1971_utm83_attrs`  
  - `communityboundary_min_att_20250121_wma84_attrs` and `communityboundary_min_att_20250121_utm83_attrs`  

- **Gridded index and tax layers.**  
  - `indexgrid15minutewithcounties_wvgistc_utm27_attrs`  
  - `indexgrid15minutequads_wvgistc_ll83_attrs` and `indexgrid15minutequads_wvgistc_utm83_attrs`  
  - `indexgrid1minutequads_wvgistc_ll83_attrs` and `inedexgrid1minutequads_wvgistc_utm83_attrs`  
  - `wv_tax_districts_ll83_attrs`, `wv_tax_districts_utm83_attrs`, and `wv_tax_districts_wma84_attrs`  

Each of these `*_attrs` collections stores feature‑level embeddings and metadata keyed to the underlying GIS layer. For example, sampling `statewide_counties` returns metadata entries with fields like:

- `sourcetable: "wv_county_boundaries_24k_topo_updated_2022_utm83"`  
- `country: "USA"`  
- `geodb_id: "1"` (and other feature IDs)  
- `label: "feat_1"` (and similar feature labels)  
- `bbox: "POLYGON((...))"`  

alongside documents such as:

- `"County feature 1: feat_1 with bbox POLYGON((...))"`  

The document text is a human‑readable summary of the feature and its geometry, while the metadata carries structured identifiers and geometry tags. Together, these spatial collections form the Hilbert‑space representation of Ms. Jarvis’s spatial body and align directly with the PostGIS tables described in the GBIM and GeoDB chapters, using the `*_attrs` naming pattern actually present in this deployment rather than the older `geodb*` / `gedb*` terminology.

---

### 5.4 From Hilbert Space to ChromaDB

ChromaDB provides the concrete realization of the Hilbert‑space state described in the previous chapter.

- **Embeddings as vectors.**  
  The embedding model maps texts and entities into high‑dimensional real vectors. ChromaDB stores these vectors alongside metadata (such as identifiers, timestamps, entity types, and geographic tags) and exposes operations such as nearest‑neighbor search, filtered retrieval, and upsert.

- **Collections as subspaces.**  
  Each ChromaDB collection corresponds to an empirically instantiated subset of the Hilbert space `H_App`, grouping related vectors by purpose (for example, governance, conversation, thesis) or by entity type (for example, blocks, buildings, mines, dams, or facilities). Conceptually, each collection spans a subspace of `H_App`.

- **Queries as projections.**  
  Incoming queries are embedded and used to probe relevant collections. This process effectively projects each query into the appropriate subspace, retrieves nearby vectors with respect to the inner‑product‑induced similarity measure, and returns associated documents and metadata for downstream reasoning.

This mapping allows Ms. Jarvis’s memory to be described both geometrically, in terms of subspaces and projections, and operationally, in terms of concrete collection queries and metadata filters.

---

### 5.5 Embedding Model and Dimensionality

In the RAG stack under analysis, Ms. Jarvis uses a sentence‑embedding model with 384‑dimensional outputs as the primary text embedding channel. The deployed Chroma catalog shows collections such as `conversation_history` and `learner` configured with dimension 384 in the internal `collections` table, confirming the ambient dimension of the main `H_text` component for text‑based collections.  

Any Chroma collection that stores embeddings produced by this model must be configured to accept 384‑dimensional vectors. This requirement applies both to general semantic collections and to GeoDB‑derived collections, which use consistent text embeddings for feature descriptions, attribute summaries, and linked narrative content.  

In the examined deployment:

- GIS‑derived `*_attrs` collections that hold feature descriptions and attribute summaries are embedded at this standard dimensionality.  
- The Ms. Jarvis–specific general corpora (`gbim_msjarvis_corpus`, `msjarvis_hilbertspace`, `msjarvis_learner_corpus`, `research_history`) exist but have zero embeddings, making 384‑dimensionality a declared standard for these domains rather than an empirically populated fact in this snapshot.

The chapter therefore treats 384‑dimensional embeddings as the standard for the main semantic channel, while recognizing that additional channels or model upgrades may be introduced in future, along with corresponding schema and migration procedures.

---

### 5.6 ChromaDB Clients and Deployment Topology

ChromaDB is accessed as a shared HTTP service in this deployment; historical patterns using per‑service local stores are now considered legacy.

#### 5.6.1 Shared HTTP Service

In the active environment, services connect to a shared ChromaDB instance through an HTTP client configured with explicit host and port:

- A Python client is created as `chromadb.HttpClient(host="127.0.0.1", port=8002)` from within the `.venv-chroma` environment.  
- `client.list_collections()` enumerates all collections, including the many GIS `*_attrs` collections and the Ms. Jarvis–specific general collections.  
- Ingestion scripts, GeoDB ETL pipelines, RAG gateways, and QA tools use this client to inspect collection counts and, where applicable, upsert and query vectors.

The shared instance exposes both general semantic collections (even when empty) and the spatial `*_attrs` collections. It is bound to a persistent on‑disk directory `persistent/chroma` on the host, mounted into the `jarvis-chroma` container at `/data`, and includes a `chroma.sqlite3` catalog plus a large number of HNSW index directories in that path. The instance is treated as the canonical semantic memory store for this deployment.

#### 5.6.2 Historical and Auxiliary Persistent Clients

Historically, some services used `PersistentClient` instances pointing to per‑service local paths such as `.chromadb` or `chroma_db`. Those local stores were used for:

- isolated experiments and unit tests,  
- early autonomous‑learner experiments or service‑specific memory, and  
- transitional states before consolidation into the shared instance.

As of late 2025 and early 2026, the operational intent is to converge on the shared HTTP‑backed store for primary semantic memory, including GeoDB embeddings. Residual local stores are treated as legacy or experimental; their contents are either migrated or preserved as snapshots with clear documentation of their status.

---

### 5.7 Integration with GBIM, GeoDB, and RAG

ChromaDB is tightly integrated with GBIM, the GeoDB layer, and the broader RAG pipeline.

- **GBIM linkage.**  
  GBIM entities—including places, infrastructures, institutions, and policies—are designed to reference Chroma collections through stable identifiers and metadata fields. For spatial entities, the `*_attrs` collections store feature‑level embeddings and metadata keyed to PostGIS tables via fields such as `sourcetable`, `geodb_id`, and `bbox`; for non‑spatial entities, Ms. Jarvis–specific general collections are intended to store associated documents and summaries once populated. This linkage allows GBIM entities to be mapped into `H_App` and retrieved by semantic or spatial criteria.

- **GeoDB integration.**  
  The GeoDB ETL pipeline reads per‑feature attributes from PostGIS, constructs embeddings and documents (for example, “County feature N: feat_N with bbox POLYGON((…))”), and upserts them into Chroma collections such as `statewide_counties` and other `*_attrs` layers. Keys and metadata—including source table, feature identifier, and geometry tags—allow retrieval results to be rejoined to GBIM entities and geometries and to be displayed or analyzed in geospatial tools.

- **RAG context building.**  
  When Ms. Jarvis answers a question, the RAG pipeline uses ChromaDB to retrieve relevant documents and feature‑level embeddings. Retrieved texts, metadata, and spatial identifiers are combined into context windows for the language models, with filtering by collection, geography, topic, and source. This implements the context subspace selection and `H_eff` restriction described in the Hilbert‑space chapter.

- **Governance‑specific retrieval.**  
  Governance‑specific retrieval (for example, MountainShares rules) is conceptually scoped to dedicated governance collections; in this particular Chroma deployment, such collections exist only as empty or planned corpora, so their practical role depends on future ingestion and backfill.

The end‑to‑end pipeline thus behaves as a structured walk through curated, domain‑specific memory organized around GBIM, the GeoDB spatial body, and Quantarithmia’s research concepts, with the caveat that non‑GIS semantic memory is still emerging.

---

### 5.8 Query Paths and JSON Structures

To connect the conceptual description with concrete operations, this section outlines canonical request and response shapes. Schemas are expressed in a language‑agnostic way and implemented in gateway and service code using typed models.

#### 5.8.1 Gateway‑Level Request Shape

Gateway or bridge services conceptually receive simplified query objects containing at least:

- a target collection or collection family (for example, a named `*_attrs` layer or a Ms. Jarvis corpus),  
- a natural‑language query string, and  
- a desired number of results.

Additional fields may specify roles, geographic filters, or constraint flags. The gateway translates these objects into lower‑level Chroma queries, adding appropriate `where` and `include` parameters and routing to the correct collection.

#### 5.8.2 Chroma Query Request and Response

At the Chroma level, a typical query against a collection includes:

- `query_texts`: a list of query strings to embed and search,  
- `n_results`: the number of nearest neighbors to return per query,  
- `where`: an optional metadata filter (for example, restricting to a particular `sourcetable` or entity type), and  
- `include`: a list specifying which fields to return (for example, `["metadatas", "documents", "distances"]`).

Using the Python client, a query has the form:

``python
results = col.query(
    query_texts=[query],
    n_results=5,
    include=["distances", "metadatas", "documents"],
)

The response contains parallel lists for documents, metadata, and distances (and possibly embeddings, when configured). In collections where embeddings are not present for every item, the embeddings field may be absent or sparsely populated while documents and metadata remain fully populated; downstream components are written to handle these cases explicitly.

For simple inspection without a semantic query, the client uses:

python
sample = col.get(
    limit=5,
    include=["metadatas", "documents"],
)

to retrieve a small set of stored items and verify that metadata and documents match expectations.

These request and response structures provide concrete anchors for documentation, testing, and debugging, and they make it possible to trace RAG behavior end‑to‑end.
5.9 Operational Considerations

Using ChromaDB as a production memory layer introduces several practical considerations that must be documented and maintained.

  # Reliability and persistence.
  The main Chroma instance is bound to the persistent/chroma directory on the host, which is mounted into the jarvis-chroma container as /data. Regular backups of this directory are required, and any residual local .chromadb directories from earlier stores should be either archived or formally decommissioned to avoid ambiguity.

#  Performance and scaling.
   As collections grow—including large GIS corpora such as wv_microsoft_20180207_utm17n83_attrs and building‑footprint layers—index configuration and hardware resources directly affect query latency. Chroma’s approximate nearest‑neighbor indices (such as HNSW) must be configured and monitored so that query latency remains acceptable even as the number of stored items increases.

#  Security and privacy.
   The documented Chroma deployment focuses on public or research‑grade data: West Virginia GIS layers and internal research corpora. Any collections that would contain sensitive user data, private keys, or non‑consensual logs must be excluded, redacted, or restricted, and conversational or personal‑memory collections must be curated before being used outside a controlled environment.

#   Schema and configuration management.
   Collection names, metadata schemas, and embedding configurations (model and dimension) are versioned and recorded in a central registry. Any changes to models, dimensions, index parameters, or collection naming schemes are treated as schema migrations, with forward‑ and backward‑compatibility considerations documented.

These operational details connect the conceptual role of ChromaDB to the realities of running a live, research‑grade governance and advisory system.
5.10 Limitations and Future Work

Current use of ChromaDB has several limitations and active areas of work:

 #   Partial embedding coverage in general‑semantic domains.
  GIS‑derived *_attrs collections are heavily populated and behave as expected under similarity search, but key Ms. Jarvis semantic corpora (gbim_msjarvis_corpus, msjarvis_hilbertspace, msjarvis_learner_corpus, research_history) are present with zero embeddings. Completing ingestion and embedding backfill for these collections is a priority for achieving a fully realized semantic memory.

#    Model and index dependence.
   Retrieval quality depends on the chosen embedding model (currently 384‑dimensional), index parameters, and collection design. Changes to any of these elements can alter the Steward System’s apparent memory; model upgrades and reindexing are therefore treated as explicit migrations with before/after evaluation.

#    Semantic gaps and representational limits.
   Certain forms of knowledge—such as embodied experience, collective trauma narratives, and spiritual traditions—are difficult to represent as short text embeddings alone. Additional representational strategies, including graph structures, qualitative annotations, GBIM‑linked justice metrics, and community‑led tagging, are needed to supplement the vector store.

   # Evolving schema and topology.
  As GBIM, GeoDB, and Quantarithmia evolve, the set of collections, metadata fields, and indexing strategies will continue to change. Migration tools and versioned schemas are necessary to maintain continuity across thesis revisions and deployments, including clear documentation of when historical local stores were consolidated into the shared HTTP‑backed instance and how legacy names (such as geodb* / gedb*) map to the current *_attrs collections.

Future work includes:

  completing embedding backfill for all key general collections with clearly documented embedding functions and dimensions,
    documenting all collection names, metadata schemas, and embedding configurations in a single, queryable registry for each deployment,
    adding traced end‑to‑end examples of RAG flows that show precisely how Chroma retrieval augments queries in different roles and geographies, and
    exploring hybrid memory architectures that combine vector stores with graphs, relational databases, and participatory annotation workflows, so that communities can inspect and shape what is stored and how it is used.

An implementation‑status badge for this chapter is therefore: PARTIAL / CONSOLIDATING. The conceptual role of ChromaDB as semantic memory is implemented through a shared HTTP‑backed Chroma service with extensive GIS *_attrs spatial collections and several core general collections created; historical per‑service stores, full embedding coverage in governance and thesis domains, and complete end‑to‑end RAG traces are in the process of consolidation and documentation.
