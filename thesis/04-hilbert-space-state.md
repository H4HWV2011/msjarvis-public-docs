> **Why this matters for Polymathmatic Geography**  
> This chapter specifies how Ms. Jarvis's semantic memory is implemented in practice, turning abstract Hilbert‑space representation, GBIM entities, a verified local resource registry, and WV‑biased entangled retrieval into a concrete, inspectable memory and RAG system. It supports:  
> - **P1 – Every where is entangled** by storing texts, GIS features, governance rules, local program records, and spatial materials in shared collections and tables that can be jointly retrieved, joined to GBIM and `local_resources`, and analyzed through both standard and entangled multi‑collection RAG pipelines.  
> - **P3 – Power has a geometry** by representing institutional, spatial, access‑to‑help, and WV‑entanglement relationships as vectors, metadata, registries, envelopes, and logged retrieval paths that can be queried and clustered to reveal patterns of extraction, access, obligation, and how the 21‑LLM ensemble and `/search` path actually reason over those structures.  
> - **P5 – Design is a geographic act** by treating collection design, metadata schemas, entanglement envelopes and coupling strengths, index parameters, RAG and `/search` routing rules, and verification logic as deliberate interventions into how a region's knowledge and memory are structured and operationalized.  
> - **P12 – Intelligence with a ZIP code** by binding memory collections and registries to West Virginia–specific spatial layers, governance documents, community narratives, ZIP‑keyed resource records, and dedicated collections like `gis_wv_benefits` that tie benefits facilities to Oak Hill, Beckley, and other localities, while the entangled `/search` endpoint uses `wv_entangled_context` to bias retrieval toward the specific counties, facilities, and principles in question.  
> - **P16 – Power accountable to place** by making Ms. Jarvis's long‑term memory and retrieval behavior explicit, queryable, auditable, and, in the case of local resources, explicitly versioned and re‑verifiable over time, with RAG, `/search`, and ensemble logs showing which collections, registry rows, and entanglement envelopes were used, rather than hiding everything inside opaque model parameters.  
> As such, this chapter belongs to the **Computational Instrument** tier: it defines the semantic memory substrate, entangled retrieval layer, and logging regime on which Quantarithmia's reasoning, GBIM's belief structures, the verified local‑resources band, the West Virginia benefits RAG flows, and MountainShares‑oriented governance analysis actually run.

## 5. ChromaDB as Semantic Memory

### 5.1 Purpose and Scope

This chapter explains how Ms. Egeria Jarvis uses ChromaDB as the primary semantic memory layer backing the Hilbert‑space representation, GBIM, the verified local resource registry, WV‑biased entangled retrieval, and the broader semantic fabric. ChromaDB is a vector database that stores high‑dimensional embedding vectors with associated metadata and exposes efficient similarity search and filtering operations. In this system, ChromaDB is not merely a convenience library; it is the concrete implementation of long‑term, queryable memory for documents, GIS features, governance texts, autonomous‑learning traces, resource guides, and thesis materials, as well as a central back‑end for the text and GIS RAG services and the entangled `/search` path.

<p align="center">
  <img src="https://github.com/user-attachments/assets/5f6bf0d9-91ca-4692-8b1c-95fbceec81b7"
       alt="ChromaDB as Semantic Memory in Ms. Jarvis"
       width="900">
</p>

> *Figure 1 – ChromaDB as Semantic Memory in Ms. Jarvis. Shows how services embed texts and GIS features into ChromaDB collections, making abstract Hilbert‑space state a concrete, queryable memory layer for RAG. Local resource documents sit alongside GBIM exports and are linked to structured entries in a `local_resources` table keyed by ZIP and program type. Dedicated collections such as `gis_wv_benefits` support benefits‑focused GIS RAG. An entangled `/search` endpoint spans multiple collections, applying WV‑specific envelopes to bias retrieval.*

Within the Quantarithmia program, ChromaDB is treated as the bridge between abstract Hilbert‑space representation and stored embeddings: vectors in each collection approximate elements of the high‑dimensional inner‑product space described in the previous chapter, but are realized through a specific embedding model and index implementation. It is the place where beliefs, contexts, resource descriptions, and references become durable and retrievable for reasoning and retrieval‑augmented generation (RAG). Conceptually, each collection corresponds to an empirically instantiated subset of the Hilbert space \(H_{\text{App}}\), and stored vectors approximate elements of the spaces described in the previous chapter while linking out to structured registers such as GBIM and `local_resources`. When used through the entangled `/search` API, these collections also participate in WV‑biased, envelope‑driven “measurements” on the multi‑collection belief state.

---

### 5.2 Role in the Ms. Jarvis Architecture

In the Ms. Jarvis architecture, ChromaDB plays several interlocking roles.

- **Semantic memory store (non‑spatial).**  
  Embeddings of texts and artifacts live in collections corresponding to domains such as governance, thesis content, autonomous learner outputs, conversations, local resource guides, and curated user‑memory–like traces. These collections support general semantic retrieval independent of geography and form the non‑spatial part of \(H_{\text{text}}\).

- **Geospatial Hilbert layer (spatial).**  
  A unified GIS‑derived collection holds embeddings and metadata for West Virginia geospatial features, mirroring PostGIS tables and providing the Hilbert‑space representation of the spatial body described in the GBIM chapter. The current production deployment centers on a consolidated worldview collection with millions of records and spatial provenance linking back to PostGIS geometries and belief graph edges, complemented by task‑specific collections such as `gis_wv_benefits` that focus on benefits‑relevant facilities.

- **Retrieval engine for RAG and `/search`.**  
  At query time, services embed inputs and use ChromaDB similarity search, often with metadata filters, to retrieve the most relevant items for context and reasoning. A text RAG service handles general semantic retrieval; a GIS RAG service uses geospatial collections for spatial questions. A dedicated `/search` endpoint performs multi‑collection retrieval and then applies WV‑specific biases derived from a `wv_entangled_context` envelope. This behavior instantiates the query projection and neighborhood selection mechanisms described in the Hilbert‑space model and forms the unstructured side of Ms. Jarvis’s memory, which is then joined against structured stores like GBIM and `local_resources` before being handed to the 21‑LLM ensemble.

- **Structural backbone for inspectable memory.**  
  Because collections and metadata are explicitly defined, ChromaDB's structure mirrors core parts of GBIM, the GeoDB layer, the thesis organization, the local‑resources band, and the entangled retrieval path. This makes it possible to enumerate collections, inspect document counts, audit metadata and entanglement tags, and correlate logs of RAG and `/search` calls with the underlying memory, rather than relying on hidden internal state.

Taken together, this design makes the semantic memory system inspectable and debuggable: researchers and community partners can see what is stored, how it is grouped, which collections underpin particular advisory behaviors, how unstructured resource documents tie back to specific, verified program rows in the relational registry, how multi‑collection entangled retrieval emphasizes particular WV entities and features, and how RAG and the ensemble use these elements to answer live questions.

---

### 5.3 Collections and Data Domains

In the deployment examined in late 2025 and early 2026, the primary Chroma instance exposes collections that fall into three broad families: general semantic memory, GeoDB‑derived spatial memory, and resource‑related materials that link into `local_resources` and benefits RAG and `/search` paths.

#### 5.3.1 Production Spatial Collection

The primary spatial memory collection in production as of early 2026 is a consolidated GBIM export:

- Collection name: `gbim_worldview_entities` (or equivalent consolidated spatial index).  
- Record count: on the order of 6.1M records.  
- Records with worldview context and spatial provenance: on the order of 5.5M.  
- Records currently lacking full worldview, bbox, and dataset metadata: a residual backlog tracked for enrichment.  
- Source datasets: 200+ standardized West Virginia GIS layers.  
- Worldview context: a stable UUID tying spatial entities to a particular worldview.

This collection is built by exporting GBIM worldview entities and their attributes from PostGIS, enriching them with spatial and provenance metadata, and indexing them as text embeddings in ChromaDB.

<p align="center">
  <img src="https://github.com/user-attachments/assets/1469b3c1-f9e8-4b9d-a021-a79baa89ee58"
       alt="End-to-End Spatial RAG Query through ChromaDB and GBIM"
       width="900">
</p>

> *Figure 2 – Consolidated spatial memory collection. Illustrates the unified spatial collection of millions of records with core and extended metadata linking ChromaDB vectors back to GBIM worldview entities and PostGIS geometries, and forward into GIS RAG responses and entangled `/search` neighborhoods.*

**Document structure**

Text documents follow a simple pattern such as:

``text
wvgistcbuildingfootprints feat_1703912
Core metadata fields (present for all records):

- `entity_id`: UUID linking to `gbim_worldview_entity.id`.  
- `source_table`: dataset name (for example, `wvgistcbuildingfootprints`, `blocks_census_2020_utm83_full`).  
- `source_pk`: primary key in the source table (links to `gbim_attrs.geodbid`).  
- `label`: human‑readable entity label.  
- `centroid_x`, `centroid_y`: spatial coordinates (EPSG:26917 – UTM Zone 17N NAD83).

Extended metadata (populated via a backfill pipeline):

- `worldview_id`: worldview context UUID.  
- `bbox`: GeoJSON geometry or bounding box.  
- `confidence`: belief confidence score.  
- `dataset`: source dataset name for provenance.  
- `geodb_id`: original GeoDB identifier.  
- `srid`: spatial reference identifier (26917).

A dedicated backfill process derives these extended fields from `gbim_worldview_entity` and `gbim.gbim_attrs` and attaches them to existing records in the consolidated spatial collection. Coverage is monitored via scripts that iterate over the collection, count non‑null values for key metadata fields, and report totals for `worldview_id`, `bbox`, and `dataset`.

---

### 5.3.2 Legacy and Historical Spatial Collections

Prior to consolidation, spatial memory was distributed across individual `*_attrs` collections corresponding to each GIS layer. These collections remain in the system for backward compatibility but are superseded by the unified spatial collection. Migration practice is: new queries target the consolidated index; legacy collections are maintained for historical queries, validation, and debugging.

---

### 5.3.3 General Semantic Collections

In the current deployment, principal general‑semantic collections are defined for:

- autonomous learning traces.  
- research history and notebook‑like notes.  
- thesis and GBIM‑related documentation.  
- personal and organizational documents for the steward/author.  
- Hilbert‑space, entanglement, and learner‑corpus materials.

These collections have schema declared and are intended to hold embeddings for governance documents, thesis materials, autonomous learner outputs, and personal research corpora. Their presence establishes the intended semantic architecture, even when embeddings are still being backfilled.

---

### 5.3.4 Resource‑Related and Benefits Collections

Resource‑related documents (for example, county quick guides, Christmas Bureau flyers, teacher resource lists, utility assistance PDFs, and agency fact sheets) are ingested into one or more semantic collections, with metadata fields such as:

- `county`, `state`, `zip_codes` or `zip_hint`.  
- `resource_type` (for example, `seasonal_assistance`, `housing`, `utilities`, `senior_services`, `education_support`).  
- `source_url` or `file_id`.  
- `local_resource_id` linking to a structured row in the `local_resources` table when available.

In addition, a dedicated `gis_wv_benefits` collection stores semantic descriptions and metadata for benefits‑related facilities (for example, Oak Hill hubs and Beckley DHHR offices), keyed by `worldview_id`, `county`, and GBIM entities. These collections provide the unstructured side of local resources and benefits. At retrieval time, Ms. Jarvis uses metadata and `local_resource_id` (or facility IDs) to resolve from an embedded snippet in ChromaDB to a normalized registry entry or GBIM entity that contains ZIP coverage, phones, emails, contacts, and verification metadata.

Some collections are also marked as part of the entangled `/search` configuration, meaning their results participate in WV‑biased multi‑collection retrieval when a `wv_entangled_context` envelope is present, and their metadata is interpreted for tag, entity, and feature overlaps during score boosting.

---

### 5.4 From Hilbert Space to ChromaDB (and Back to Registries)

ChromaDB provides the concrete realization of the Hilbert‑space representation described in the previous chapter, while structured stores such as GBIM tables and `local_resources` provide the “hard edges” that RAG and entangled retrieval resolve into.

**Embeddings as vectors.**  
The embedding model maps texts and entities into high‑dimensional real vectors. ChromaDB stores these vectors alongside metadata (identifiers, timestamps, entity types, geographies, resource keys, and, where relevant, entanglement tags) and exposes operations such as nearest‑neighbor search, filtered retrieval, and upsert.

**Collections as working subspaces.**  
Each ChromaDB collection corresponds to an empirically instantiated subset of the Hilbert space \(H_{\text{App}}\), grouping related vectors by purpose (for example, governance, conversation, thesis, resource guides) or by entity type (for example, blocks, buildings, infrastructure, benefits hubs). The consolidated spatial collection represents a comprehensive spatial subspace in this deployment, while resource and benefits collections approximate a semantic subspace of “who helps whom, where, and how.”

**Queries as projections plus joins.**  
Incoming queries are embedded and used to probe relevant collections. This effectively projects each query into the appropriate subset of \(H_{\text{App}}\), retrieves nearby vectors with respect to the inner‑product‑induced similarity measure, and returns documents and metadata. For resource‑ and benefits‑related flows, Ms. Jarvis then uses metadata (such as `local_resource_id`, `county`, `ZIP`, `worldview_id`, and `gbim_entity`) to join that unstructured context against `local_resources` and GBIM, enforcing that any recommended program or facility has concrete, structured backing and a verification state, and that RAG answers can be traced back to specific entities and rows.

In the entangled `/search` path, the same projections and joins occur, but similarity scores from multiple collections are further modulated by a `wv_entangled_context` envelope that encodes domains, principles, GBIM entities, and GeoDB features. This creates an explicitly WV‑biased projection of the query neighborhood before it is used to assemble context for the ensemble.

This mapping allows Ms. Jarvis’s memory to be described both geometrically, in terms of subsets and projections of a Hilbert space, and operationally, in terms of concrete collection queries, metadata filters, entanglement envelopes, RAG calls, and joins to structured registries.

---

### 5.5 Embedding Model and Dimensionality

In the RAG stack under analysis, Ms. Jarvis uses a sentence‑embedding model with 384‑dimensional outputs as the primary text embedding channel. Chroma collections are configured with dimension 384, confirming the ambient dimension of the main \(H_{\text{text}}\) component for text‑based collections.

Any Chroma collection that stores embeddings produced by this model is configured to accept 384‑dimensional vectors. This requirement applies both to general semantic collections and to spatial and benefits collections, which use consistent text embeddings for feature descriptions and attribute summaries, as well as to resource‑document collections.

The chapter therefore treats 384‑dimensional embeddings as the standard for the main semantic channel, while recognizing that additional channels or model upgrades may be introduced in future, along with corresponding schema and migration procedures.

---

### 5.6 Clients, RAG Services, and Deployment Topology

ChromaDB is accessed as a shared HTTP service in this deployment; historical patterns using per‑service local stores are now considered legacy.

#### 5.6.1 Shared HTTP Service

In the active environment, services connect to a shared ChromaDB instance through an HTTP client configured with explicit host and port, with:

- a container dedicated to the vector store,  
- persistent on‑disk storage mounted into the container, and  
- a single catalog that includes spatial, semantic, resource‑document, benefits, and entangled‑retrieval collections.

Connection patterns follow a simple template:

``python
import chromadb

client = chromadb.HttpClient(host="localhost", port=8002)
collection = client.get_collection("gbim_worldview_entities")
print("Total entities:", collection.count())

The shared instance is treated as the canonical semantic memory store for this deployment and is used by the text RAG, GIS RAG, entangled `/search`, and other memory‑aware services behind `/chat/light` and `/chat/sync`.

### 5.6.2 Historical and Auxiliary Persistent Clients

Historically, some services used local persistent stores for isolated experiments and early autonomous‑learner work. As of early 2026, the operational intent is to converge on the shared HTTP‑backed store for primary semantic memory. Residual local stores are treated as legacy or experimental; their contents are either migrated or preserved as snapshots with clear documentation of their status.

---

### 5.7 Integration with GBIM, GeoDB, Local Resources, Entanglement, and RAG

ChromaDB is tightly integrated with GBIM, the GeoDB layer, the local resource registry, the benefits‑focused collections, the entangled `/search` path, and the broader RAG pipeline.

**GBIM linkage.**  
GBIM worldview entities are indexed in the consolidated spatial collection with metadata fields linking back to PostGIS tables via `source_table` and `source_pk`. The `entity_id` field provides stable UUID references to `gbim_worldview_entity.id`, enabling round‑trip queries from semantic search results to full belief provenance, including how, why, for_whom, and authority edges.

**GeoDB integration.**  
The spatial collection mirrors the `gbim.gbim_attrs` corpus. Spatial coordinates and bounding boxes enable hybrid queries that combine semantic similarity with spatial filtering. Keys and metadata allow retrieval results to be rejoined to GBIM entities and geometries for display in geospatial tools and for inclusion in GIS RAG responses and entangled retrieval envelopes.

**Local resource registry integration.**  
Resource‑related collections index unstructured PDFs and guides while tagging entries with `local_resource_id` or other keys. Once a snippet is retrieved, Ms. Jarvis resolves it to a row in the `local_resources` table, which encodes `resource_type`, county, ZIP coverage, `contact_email`, `contact_phone`, `verification_status`, `last_verified_at`, and notes. This ensures that recommendations are backed by explicit, up‑to‑date program records rather than free‑floating text alone.

**Benefits and GIS RAG integration.**  
The `gis_wv_benefits` collection indexes semantic descriptions of benefits facilities and is queried by GIS RAG services for prompts like “Oak Hill benefits” or “Raleigh County DHHR.” Metadata such as `worldview_id`, `county`, and `gbim_entity` enable joins back to GBIM and relationships to other worldview entities. Combined with text RAG over `msjarvisgis` and resource collections, this yields blended semantic and spatial context for the ensemble.

**Entangled `/search` integration.**  
A dedicated RAG server endpoint (`/search`) performs WV‑biased, multi‑collection retrieval. It accepts a `wv_entangled_context` envelope with fields such as `domains`, `principles`, `gbim_entity_ids`, and `geodb_features`. For each query, the server:

- queries a configured set of collections (`GBIM`, `gisgeodata`, `benefit_programs`, `msjarvis`, `compliance_tasks`, `GeoDB`, `utility_enrollments`, `rag_training_data`, `spiritual_texts`),  
- logs raw distances per collection (“before bias”),  
- computes a bias profile from the envelope, and  
- applies multiplicative boosts to scores when metadata overlaps the specified tags, entities, or features.

The final, globally ranked top‑k list is returned and logged (“after bias”), making it clear how WV‑aligned items were favored.

**RAG context building.**  
For spatial or resource questions, the RAG pipeline queries both spatial and resource collections to retrieve relevant entities, PDFs, and program descriptions. Retrieved texts, metadata, spatial identifiers, registry keys, and entangled scores are combined into context windows for language models, with filtering by collection, geography, topic, resource type, and verification status. Logs record which collections, IDs, registry rows, and entanglement envelopes were used per query.

**Belief graph and registry traversal.**  
Once Chroma returns entity IDs and resource keys, the system performs SQL queries against GBIM belief and edge tables and against `local_resources` to retrieve the full epistemic and practical context: data sources (how edges), policy justifications (why edges), beneficiary communities (for_whom edges), authorizing frameworks (authority edges), and concrete program details and verification history.

End‑to‑end, the pipeline behaves as a structured walk through curated, domain‑specific memory organized around GBIM, the GeoDB spatial body, resource registries, entangled retrieval envelopes, and Quantarithmia's research concepts, mediated by ChromaDB and observed through RAG, `/search`, and ensemble logs.

---

### 5.8 Query Paths and JSON Structures

To connect the conceptual description with concrete operations, this section outlines canonical request and response shapes.

#### 5.8.1 ChromaDB Query Request

A typical query against the consolidated spatial collection includes:

- `query_texts`: list of query strings to embed and search.  
- `n_results`: number of nearest neighbors to return per query.  
- `where`: optional metadata filter (for example, restricting to a set of `source_table` values or to entities in a given county).  
- `include`: fields to return (for example, `["metadatas", "documents", "distances"]`).

Resource and benefits collections follow the same pattern, with additional filters like `resource_type`, `local_resource_id`, or `county`.

#### 5.8.2 Entangled `/search` Request

An entangled query against the RAG server wraps the Chroma calls and WV bias in a single JSON body, for example:

``json
{
  "query": "Where are mental health providers most scarce in Fayette County, WV?",
  "topk": 5,
  "wv_entangled_context": {
    "domains": ["health", "mental_health", "access"],
    "principles": ["equity", "geographic_access"],
    "gbim_entity_ids": ["gbim:county:Fayette", "gbim:population_group:low_income"],
    "geodb_features": [
      {
        "feature_id": "hospital_1234",
        "layer": "healthcare_providers",
        "county": "Fayette",
        "state": "WV"
      }
    ]
  }
}

The server then performs multi‑collection Chroma queries under the hood, applies entangled boosts, and returns a globally ranked result set.

### 5.8.3 ChromaDB Response Structure

Chroma responses contain parallel lists of IDs, distances, metadatas, and documents, where metadata entries include the identifiers needed to rejoin to GBIM entities or to registry rows in `local_resources`. The `/search` endpoint wraps these with entangled scores and boost flags. This structure underpins traceable, explainable RAG behavior and supports reconstruction of which memory elements and entanglement conditions contributed to a given ensemble answer.

---

### 5.9 Operational Considerations

Using ChromaDB as a production memory layer introduces several practical considerations.

**Reliability and persistence.**  
The main Chroma instance is backed by persistent on‑disk storage, with regular backups around large ingests and metadata backfills. Legacy local stores are archived or decommissioned to avoid ambiguity.

**Performance and scaling.**  
As collections grow into the millions of records, index configuration and hardware resources directly affect query latency and throughput for similarity search. Bulk ingest is performed in batches, with attention to index compaction and memory usage. Latency characteristics of `/chat/light`, `/chat/sync`, and `/search` reflect not just model inference but also Chroma query performance and entanglement‑bias computation.

**Security and privacy.**  
The documented deployment focuses on public or research‑grade data: West Virginia GIS layers, public resource guides, and internal research corpora. Collections containing sensitive user data or non‑consensual logs are excluded or carefully controlled. Conversational or personal‑memory collections are curated before being used in broader contexts.

**Schema and configuration management.**  
Collection names, metadata schemas, embedding configurations, entanglement envelope schemas, and RAG routing rules are versioned and recorded. Consolidations (such as merging many `*_attrs` collections into a single GBIM‑backed spatial index, adding `local_resource_id` metadata to resource documents, introducing `gis_wv_benefits`, or wiring collections into the entangled `/search` path) are treated as explicit migrations with before/after evaluation.

---

### 5.10 Production Deployment Characteristics (Early 2026)

**Spatial memory**

- A consolidated spatial collection with roughly 6.1M records.  
- Around 5.5M records with extended provenance metadata, with a residual backlog explicitly tracked for enrichment.  
- 200+ source GIS datasets.  
- Core spatial metadata coverage for all records (IDs, source tables, primary keys, centroids).  
- Extended provenance fields attached via a dedicated backfill pipeline, monitored by automated scripts.  
- SRID 26917 (UTM Zone 17N NAD83) standardization.

**Belief‑graph integration**

- GBIM belief and edge tables encode how, why, for_whom, and authority relationships for millions of worldview entities.  
- Chroma metadata enables deterministic joins from semantic results into these belief structures.

**Local resource and benefits integration**

- A growing `local_resources` table captures community programs with `resource_type`, county, ZIP coverage, phones, emails, URLs, contact names, and verification fields.  
- Resource‑document collections in ChromaDB are wired to include `local_resource_id` metadata, enabling RAG to resolve PDF snippets to specific, verifiable registry entries.  
- A `gis_wv_benefits` collection indexes key benefits facilities with `worldview_id`, `county`, and `gbim_entity` metadata for use in GIS RAG.

**RAG, entangled `/search`, and ensemble integration**

- Text and GIS RAG services call ChromaDB collections, apply metadata filters, and pass retrieved content to a 21‑model ensemble (`llm20_production`) via `/chat/light` and `/chat/sync`.  
- An entangled `/search` endpoint orchestrates multi‑collection WV‑biased retrieval using `wv_entangled_context`, then feeds its results into downstream reasoning and logging.  
- Guardrail services (blood–brain barrier) operate downstream to enforce constitutional and safety constraints.  
- Logs capture which collections, IDs, registry rows, and entanglement envelopes were touched per query, enabling post‑hoc inspection of memory usage and WV bias behavior.

**Storage and performance**

- Multi‑gigabyte CSV exports used for bulk ingest and metadata backfill.  
- A dedicated container exposes Chroma over HTTP with persistent storage.  
- Embedding dimension fixed at 384 for main text channels.  
- Batch ingestion with throughput tuned for stable operation on the target hardware.

**General semantic collections**

- Governance, thesis, autonomous learner, and personal‑research collections have schema declared and are in various stages of population and backfill.

---

### 5.11 Limitations and Future Work

**Partial embedding coverage in general‑semantic domains.**  
Spatial collections are heavily populated, but key Ms. Jarvis semantic corpora remain under‑embedded. Completing ingestion and embedding backfill is necessary for a fully realized semantic memory.

**Model, index, entanglement, and RAG dependence.**  
Retrieval quality depends on the embedding model, index parameters, collection design, entanglement envelope configuration, and RAG routing. Upgrades are treated as migrations with explicit evaluation, including checks that benefits and resource flows for places like Oak Hill and Beckley still behave as intended and that WV‑biased boosts align with stewardship goals.

**Semantic gaps and representational limits.**  
Certain forms of knowledge—embodied experience, oral history, spiritual traditions—are difficult to represent as short text embeddings alone. Additional representational strategies (graphs, qualitative annotations, GBIM‑linked justice metrics, community‑led tagging, and registries like `local_resources`) are needed to supplement the vector store.

**Evolving schema and topology.**  
As GBIM, GeoDB, RAG services, entanglement logic, and Quantarithmia evolve, the set of collections, metadata fields, and indexing strategies will continue to change. Consolidations like the GBIM spatial merge, the introduction of `gis_wv_benefits`, the link from resource collections into `local_resources`, and the activation of entangled `/search` demonstrate this evolution.

Future work will:

- Maintain the consolidated spatial collection via incremental updates and periodic metadata backfills.  
- Backfill general semantic collections with governance documents, thesis materials, autonomous learner outputs, and resource guides.  
- Document all collection schemas, entanglement envelope structures, and RAG routing rules in a single, queryable registry.  
- Add traced end‑to‑end examples showing Chroma retrieval → GBIM provenance → belief‑graph traversal → local resource resolution → entangled `/search` scoring → ensemble answer.  
- Explore hybrid memory architectures combining vector stores with graphs, relational databases, participatory annotation workflows, and entangled topic graphs in the autonomous learner.  
- Implement incremental sync infrastructure for daily delta updates instead of full rebuilds.  
- Develop or adopt embedding models and metadata conventions fine‑tuned on Appalachian place names, infrastructure terminology, and local program language, and integrate them with the verified local resource registry, entanglement envelopes, and verification loop.

**Implementation Status**  

**Badge: PRODUCTION / CONSOLIDATING / ENTANGLED‑READY**  
The conceptual role of ChromaDB as semantic memory is fully implemented for spatial entities and increasingly for resource guides and benefits facilities, and it is now directly exercised by text and GIS RAG services behind `/chat/light`, `/chat/sync`, and the entangled `/search` endpoint. A verified `local_resources` band in Postgres complements Chroma, providing structured, ZIP‑aware, and periodically re‑verified program information that Ms. Jarvis uses alongside both standard and entangled semantic retrieval to act as an accountable, place‑based Steward System in West Virginia.
