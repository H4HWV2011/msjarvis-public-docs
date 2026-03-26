## Why This Matters for Polymathmatic Geography

This chapter describes how Ms. Jarvis uses a concrete semantic memory system to support place‑based reasoning about West Virginia, connecting GBIM beliefs, the `msjarvisgis` statewide spatial corpus, and a verified `local_resources` registry into an inspectable retrieval pipeline. It supports:

- **P1 – Every where is entangled** by storing texts, GIS‑derived entities, and programme records in shared relational tables and production vector collections such as `gbim_beliefs_v2`, `gbim_worldview_entities`, and `gis_wv_benefits` that can be jointly retrieved and rejoined, so that legal, economic, infrastructural, and social facts about Appalachia are handled as a single interconnected memory rather than as disconnected files or ad‑hoc lookups.
- **P3 – Power has a geometry** by representing relationships among institutions, places, and access to help as explicit GBIM records, GeoDB features in `msjarvisgis`, Chroma collections, and logged retrieval paths whose behaviour can be inspected, clustered, and audited, making it possible to see how different parts of the system are actually traversed when answering questions about extraction, obligation, and care.
- **P5 – Design is a geographic act** by treating collection schemas, metadata choices, enrichment scripts, retrieval rules, and join logic in the GBIM/GeoDB/Chroma stack as deliberate interventions into how West Virginia is represented and searched, so that design decisions about Ms. Jarvis's semantic memory layer are understood as decisions about how the region itself can be perceived and acted upon.
- **P12 – Intelligence with a ZIP code** by binding memory collections and registries to West Virginia–specific layers and records, including GBIM‑derived geographies, `msjarvisgis` features, and a programme registry keyed by county and ZIP where populated, so that queries about help, risk, or opportunity are resolved through structures that explicitly encode where people live and which institutions serve them.
- **P16 – Power accountable to place** by making long‑term memory, retrieval behaviour, and query‑to‑evidence links explicit and queryable, with logs and database joins that show which GBIM beliefs, GeoDB features, vector‑collection entries, and `local_resources` rows were used in answers about particular communities, instead of hiding those choices inside opaque model weights.

As such, this chapter belongs to the **Computational Instrument** tier: it defines the production semantic memory substrate and retrieval layer—centred on collections such as `gbim_beliefs_v2`, `gbim_worldview_entities`, and `gis_wv_benefits` and on the `msjarvisgis`/GBIM/`local_resources` apparatus—that Quantarithmia's reasoning, GBIM's belief structures, the verified local‑resources band, the West Virginia benefits RAG flows, and MountainShares‑oriented governance analysis run on in the live system as of March 26, 2026.

---

## 4. Hilbert Space State and ChromaDB as Semantic Memory

### 4.1 Purpose and Scope

This chapter explains how Ms. Egeria Jarvis uses ChromaDB as the primary semantic memory layer backing the Hilbert‑space representation, GBIM, the verified local resource registry, and the broader semantic fabric. ChromaDB is a vector database that stores high‑dimensional embedding vectors with associated metadata and exposes efficient similarity search and filtering operations. In this system, ChromaDB is not merely a convenience library; it is the concrete implementation of long‑term, queryable memory for documents, GIS features, governance texts, autonomous‑learning traces, resource guides, and thesis materials, as well as a central back‑end for the text and GIS RAG services.

<p align="center">
  <img src="https://github.com/user-attachments/assets/5f6bf0d9-91ca-4692-8b1c-95fbceec81b7"
       alt="ChromaDB as Semantic Memory in Ms. Jarvis"
       width="900">
</p>

> *Figure 1 – ChromaDB as Semantic Memory in Ms. Jarvis. Services embed texts and GIS features into ChromaDB collections so that abstract Hilbert‑space state becomes a concrete, queryable memory layer for RAG. Local resource documents sit alongside GBIM exports and are linked to structured entries in a `local_resources` table keyed by ZIP and programme type. Dedicated collections such as `gis_wv_benefits` support benefits‑focused GIS RAG.*

Within the Quantarithmia programme, ChromaDB is treated as the bridge between abstract Hilbert‑space representation and stored embeddings: vectors in each collection approximate elements of the high‑dimensional inner‑product space described in the previous chapter, but are realized through a specific embedding model and index implementation. It is the place where beliefs, contexts, resource descriptions, and references become durable and retrievable for reasoning and retrieval‑augmented generation (RAG). Conceptually, collections such as `gbim_beliefs_v2`, `gbim_worldview_entities`, and `gis_wv_benefits` correspond to empirically instantiated subsets of the Hilbert space \(H_{\text{App}}\), and stored vectors approximate elements of the spaces described in the previous chapter while linking out to structured registers such as GBIM and `local_resources`.

---

### 4.2 Role in the Ms. Jarvis Architecture

In the Ms. Jarvis architecture, ChromaDB plays several interlocking roles.

- **Semantic memory store (non‑spatial).**
  Embeddings of texts and artefacts live in collections corresponding to domains such as governance, thesis content, autonomous learner outputs, conversations, local resource guides, and curated research traces. These collections support general semantic retrieval independent of geography and include the unified GBIM text collection `gbim_beliefs_v2`, which stores embeddings for rows in `gbimbeliefnormalized` and serves as the production semantic memory layer for GBIM beliefs.

- **Geospatial semantic layer (spatial).**
  A unified GIS‑derived collection such as `gbim_worldview_entities` holds embeddings and metadata for West Virginia geospatial features, mirroring PostGIS tables and providing the semantic representation of the spatial body described in the GBIM and GeoDB chapters. The current production deployment centres on this consolidated worldview collection with 5,416,521 records and spatial provenance linking back to PostGIS geometries and belief rows, complemented by task‑specific collections such as `gis_wv_benefits` that focus on benefits‑relevant facilities.

- **Retrieval engine for RAG.**
  At query time, services embed inputs and use ChromaDB similarity search, often with metadata filters, to retrieve the most relevant items for context and reasoning. A text RAG service handles general semantic retrieval over collections like `gbim_beliefs_v2`; a GIS RAG service uses `gbim_worldview_entities` and `gis_wv_benefits` for spatial questions. This behaviour instantiates the query projection and neighbourhood selection mechanisms described in the Hilbert‑space model and forms the unstructured side of Ms. Jarvis's memory, which is then deterministically joined against structured stores like GBIM and `local_resources` before being handed to the ensemble.

- **Structural backbone for inspectable memory.**
  Because collections and metadata are explicitly defined, ChromaDB's structure mirrors core parts of GBIM, the `msjarvisgis` GeoDB layer, the thesis organisation, and the local‑resources band. This makes it possible to enumerate collections, inspect document counts, audit metadata, and correlate logs of RAG calls with the underlying memory, rather than relying on hidden internal state.

Taken together, this design makes the semantic memory system inspectable and debuggable: researchers and community partners can see what is stored, how it is grouped, which collections underpin particular advisory behaviours, how unstructured resource documents tie back to specific, verified programme rows in the relational registry, and how RAG and the ensemble use these elements to answer live questions.

---

### 4.3 Collections and Data Domains

In the production deployment as of March 26, 2026, the primary Chroma instance exposes collections that fall into three broad families: general semantic memory, GeoDB‑derived spatial memory, and resource‑related materials that link into `local_resources` and benefits RAG paths.

#### 4.3.1 Production Spatial Collection

The primary spatial memory collection in production as of March 2026 is a consolidated GBIM export:

- Collection name: `gbim_worldview_entities`
- Record count: **5,416,521 records** — confirmed live, March 26, 2026
- Records with worldview context and spatial provenance: a large majority of the collection
- Records currently lacking full worldview, bounding box, and dataset metadata: a residual backlog tracked for enrichment
- Source datasets: more than 200 standardised West Virginia GIS layers
- Worldview context: `eq1` — stable UUID tying spatial entities to the production equity-oriented worldview

This collection is built by exporting GBIM worldview entities and their attributes from PostGIS, enriching them with spatial and provenance metadata, and indexing them as text embeddings in ChromaDB using `all-minilm:latest` (384-dim, cosine similarity) — confirmed live.

<p align="center">
  <img src="https://github.com/user-attachments/assets/1469b3c1-f9e8-4b9d-a021-a79baa89ee58"
       alt="End-to-End Spatial RAG Query through ChromaDB and GBIM"
       width="900">
</p>

> *Figure 2 – Consolidated spatial memory collection. The unified spatial collection links ChromaDB vectors back to GBIM worldview entities and PostGIS geometries, and forward into GIS RAG responses.*

**Document structure**

Text documents follow a simple pattern such as:

```text
wvgistcbuildingfootprints feat_1703912
```

Core metadata fields (present for all records):

- `entity_id`: UUID linking to `gbim_worldview_entity.id`
- `source_table`: dataset name (for example, `wvgistcbuildingfootprints`, `blocks_census_2020_utm83_full`)
- `source_pk`: primary key in the source table (linked to GBIM/GeoDB attributes)
- `label`: human‑readable entity label
- `centroid_x`, `centroid_y`: spatial coordinates in the standard projected system

Extended metadata (populated via a backfill pipeline):

- `worldview_id`: worldview context UUID (`eq1`)
- `bbox`: GeoJSON geometry or bounding box
- `dataset`: source dataset name for provenance
- `geodb_id`: original GeoDB identifier
- `srid`: spatial reference identifier

A dedicated backfill process derives these extended fields from GBIM and GeoDB tables and attaches them to existing records in the consolidated spatial collection. Coverage is monitored via scripts that iterate over the collection and count non‑null values for key metadata fields.

---

#### 4.3.2 Legacy and Historical Spatial Collections

Prior to consolidation, spatial memory was distributed across individual `*_attrs` collections corresponding to each GIS layer. These collections remain in the system for backward compatibility but are superseded by the unified spatial collection. Migration practice is: new queries target the consolidated index; legacy collections are maintained for historical queries, validation, and debugging.

---

#### 4.3.3 General Semantic Collections

In the current deployment, principal general‑semantic collections are defined for:

- autonomous learning traces (`autonomous_learner` — 21,181+ items, growing ~288/day)
- research history and notebook‑like notes
- thesis and GBIM‑related documentation
- personal and organisational documents for the steward/author
- Hilbert‑space and learner‑corpus materials

The flagship GBIM belief collection `gbim_beliefs_v2` sits in this family. It is populated directly from `gbimbeliefnormalized`, with each row embedded as a document whose text is constructed from the nine GBIM axes and whose metadata carries belief identifiers, epochs, and dataset provenance. This collection is in production and is the primary semantic memory surface for structured beliefs in the RAG services.

---

#### 4.3.4 Resource‑Related and Benefits Collections

Resource‑related documents (for example, county quick guides, seasonal assistance flyers, teacher resource lists, utility assistance PDFs, and agency fact sheets) are ingested into one or more semantic collections, with metadata fields such as:

- `county`, `state`, `zip_codes` or `zip_hint`
- `resource_type` (for example, `seasonal_assistance`, `housing`, `utilities`, `senior_services`, `education_support`)
- `source_url` or `file_id`
- `local_resource_id` linking to a structured row in the `local_resources` table when available

In addition, a dedicated `gis_wv_benefits` collection stores semantic descriptions and metadata for benefits‑related facilities (for example, Oak Hill hubs and Beckley DHHR offices), keyed by county, ZIP, and GBIM entities. These collections provide the unstructured side of local resources and benefits. At retrieval time, Ms. Jarvis uses metadata and `local_resource_id` (or facility IDs) to resolve from an embedded snippet in ChromaDB to a normalized registry entry or GBIM entity that contains ZIP coverage, phones, emails, contacts, and verification metadata.

A key aspect of this band is that the underlying data are not purely desk‑compiled. Harmony for Hope has convened a **Community Champions** group to ground‑truth resource information, with Boone County resident **Crystal Colyer** serving as a lead "boots‑on‑the‑ground" validator. Working especially across Boone, Kanawha, and nearby counties, she verifies the existence, hours, and accessibility of food pantries and other supports, and her findings drive updates to both the `local_resources` registry and the associated resource‑document collections.

---

### 4.4 From Hilbert Space to ChromaDB (and Back to Registries)

ChromaDB provides the concrete realization of the Hilbert‑space representation described in the previous chapter, while structured stores such as GBIM tables and `local_resources` provide the "hard edges" that RAG resolves into.

**Embeddings as vectors.**
The embedding model maps texts and entities into high‑dimensional real vectors. ChromaDB stores these vectors alongside metadata (identifiers, timestamps, entity types, geographies, resource keys) and exposes operations such as nearest‑neighbor search, filtered retrieval, and upsert.

**Collections as working subspaces.**
Each ChromaDB collection corresponds to an empirically instantiated subset of \(H_{\text{App}}\), grouping related vectors by purpose (for example, governance, conversation, thesis, resource guides) or by entity type (for example, blocks, buildings, infrastructure, benefits hubs). The consolidated spatial collection represents a comprehensive spatial subspace in this deployment, while resource and benefits collections approximate a semantic subspace of "who helps whom, where, and how."

**Queries as projections plus joins.**
Incoming queries are embedded and used to probe relevant collections. This effectively projects each query into the appropriate subset of \(H_{\text{App}}\), retrieves nearby vectors with respect to the inner‑product‑induced similarity measure, and returns documents and metadata. For resource‑ and benefits‑related flows, Ms. Jarvis then uses metadata (such as `local_resource_id`, `county`, `ZIP`, and `gbim_entity`) to join that unstructured context against `local_resources` and GBIM, enforcing that any recommended programme or facility has concrete, structured backing and a verification state, and that RAG answers can be traced back to specific entities and rows.

This mapping allows Ms. Jarvis's memory to be described both geometrically, in terms of subsets and projections of a Hilbert space, and operationally, in terms of concrete collection queries, metadata filters, RAG calls, and joins to structured registries.

---

### 4.5 Embedding Model and Dimensionality — ★ CONFIRMED LIVE March 26, 2026

> **Architectural finding — confirmed March 26, 2026.** The embedding model and its constraints are no longer planned or provisional. All ChromaDB production collections use `all-minilm:latest` (384-dimensional, cosine similarity distance function), served by `jarvis-ollama` at `ollama:11434/api/embeddings`. This is confirmed live across all collections in the `msjarvis-rebuild` namespace.

**Confirmed production embedding specification:**

| Property | Value |
|---|---|
| Model | `all-minilm:latest` — **CONFIRMED LIVE** |
| Embedding dimensions | **384** — confirmed, all production collections |
| Distance function | Cosine similarity |
| Embedding endpoint | `http://jarvis-ollama:11434/api/embeddings` |
| ChromaDB host port | 8002 (container-internal: 8000) |
| API version | v2 — all calls must use `/api/v2/` endpoints (v1 returns HTTP 410 Gone) |

> ⚠️ **Embedding model lock — enforced.** The `nomic-embed-text` model produces 768-dimensional vectors and is **incompatible** with all existing production collections. Any ingestion, retrieval, migration, or backfill script must use `all-minilm:latest` (384-dim). This constraint is enforced at the service level and cannot be overridden by prompting or configuration.

> **⚠️ Architectural Finding — Chunk Size Constraint (discovered March 26, 2026).**
>
> The `all-minilm:latest` model operates under a **256-token context window limit**. At approximately 0.75 tokens per word, this constrains meaningful semantic content to roughly **100 words per chunk maximum**. This is not a soft preference — chunks exceeding ~100 words risk truncation, degraded embedding quality, and reduced retrieval precision.
>
> **Implications for the corpus architecture:**
> - All ingestion pipelines must chunk source documents at ≤100 words with ~20-word overlap before embedding
> - The 643-chunk `governance_rag` collection and 306-chunk `commons_rag` collection were ingested using this constraint and are correctly structured
> - Legacy collections ingested before this constraint was documented should be audited for oversized chunks
> - Any future RAG collection (WV Constitution, additional governance docs, resource guides) must apply the 100-word/20-word-overlap chunking rule at ingest time
> - This constraint is architectural and permanent for the `all-minilm:latest` model — it cannot be resolved by configuration changes; changing embedding models would require full collection rebuilds
>
> This finding is documented here as an architectural fact of the production system, not as a limitation to be worked around. The 100-word chunk constraint shapes ingestion pipeline design for all future RAG collections.

**Connection pattern (confirmed live):**

```python
import chromadb

# ChromaDB v2 API — host port 8002
client = chromadb.HttpClient(host="localhost", port=8002)
collection = client.get_collection("gbim_worldview_entities")
print("Total entities:", collection.count())
# Returns: 5416521
```

```python
import httpx

# Embedding via all-minilm:latest — confirmed live
response = httpx.post(
    "http://localhost:11434/api/embeddings",
    json={"model": "all-minilm:latest", "prompt": "Fayette County land access programs"}
)
embedding = response.json()["embedding"]
assert len(embedding) == 384  # confirmed production dimension
```

Any ChromaDB collection that stores embeddings produced by this model is configured to accept 384-dimensional vectors. This applies uniformly to general semantic collections, spatial and benefits collections, governance RAG collections, and resource‑document collections.

---

### 4.6 Clients, RAG Services, and Deployment Topology

ChromaDB is accessed as a shared HTTP service; earlier patterns using per‑service local stores are now considered legacy.

#### 4.6.1 Shared HTTP Service

In the active environment, services connect to a shared ChromaDB instance through an HTTP client configured with explicit host and port, with:

- a container dedicated to the vector store (`jarvis-chroma`, host port 8002)
- persistent on‑disk storage mounted into the container
- ChromaDB v2 API (`/api/v2/` endpoints required — v1 returns HTTP 410 Gone)
- a single catalog that includes spatial, semantic, resource‑document, and benefits collections

The shared instance is treated as the canonical semantic memory store for this deployment and is used by the text RAG, GIS RAG, and other memory‑aware services behind the main chat and search endpoints.

---

### 4.7 Integration with GBIM, GeoDB, Local Resources, and RAG

ChromaDB is tightly integrated with GBIM, the GeoDB layer, the local resource registry, the benefits‑focused collections, and the broader RAG pipeline.

**GBIM linkage.**
GBIM worldview entities are indexed in the consolidated spatial collection with metadata fields linking back to PostGIS tables via `source_table` and `source_pk`. The `entity_id` field provides stable UUID references to `gbim_worldview_entity.id`, enabling round‑trip queries from semantic search results to full belief provenance, including the nine epistemic axes described in the GBIM chapter.

**GeoDB integration.**
The spatial collection mirrors the GBIM attributes corpus. Spatial coordinates and bounding boxes enable hybrid queries that combine semantic similarity with spatial filtering. Keys and metadata allow retrieval results to be rejoined to GBIM entities and geometries for display in geospatial tools and for inclusion in GIS RAG responses.

**Local resource registry integration.**
Resource‑related collections index unstructured PDFs and guides while tagging entries with `local_resource_id` or other keys. Once a snippet is retrieved, Ms. Jarvis resolves it to a row in the `local_resources` table, which encodes `resource_type`, county, ZIP coverage, contact details, and verification fields. This ensures that recommendations are backed by explicit, up‑to‑date programme records rather than free‑floating text alone.

**Benefits and GIS RAG integration.**
The `gis_wv_benefits` collection indexes semantic descriptions of benefits facilities and is queried by GIS RAG services for prompts like "benefits near Oak Hill" or "Raleigh County assistance offices." Metadata such as county and GBIM entity identifiers enable joins back to GBIM and relationships to other worldview entities. Combined with text RAG over other collections, this yields blended semantic and spatial context for the ensemble.

**RAG context building.**
For spatial or resource questions, the RAG pipeline queries both spatial and resource collections to retrieve relevant entities, PDFs, and programme descriptions. Retrieved texts, metadata, spatial identifiers, and registry keys are combined into context windows for language models, with filtering by collection, geography, topic, resource type, and verification status. Logs record which collections and IDs were used per query.

**Belief graph and registry traversal.**
Once ChromaDB returns entity IDs and resource keys, the system performs SQL queries against GBIM belief and edge tables and against `local_resources` to retrieve the full epistemic and practical context: data sources (how), policy justifications (why), beneficiary communities (for whom), authorising frameworks (authority), and concrete programme details and verification history.

End‑to‑end, the pipeline behaves as a structured walk through curated, domain‑specific memory organised around GBIM, the GeoDB spatial body, resource registries, and Quantarithmia's research concepts, mediated by ChromaDB and observed through RAG and ensemble logs.

---

### 4.8 Query Paths and JSON Structures

To connect the conceptual description with concrete operations, this section outlines canonical request and response shapes.

#### 4.8.1 ChromaDB Query Request (v2 API)

A typical query against a collection includes:

- `query_texts`: list of query strings to embed and search
- `n_results`: number of nearest neighbours to return per query
- `where`: optional metadata filter (for example, restricting to certain `source_table` values or to entities in a given county)
- `include`: fields to return (for example, `["metadatas", "documents", "distances"]`)

Resource and benefits collections follow the same pattern, with additional filters like `resource_type`, `local_resource_id`, or `county`.

> **v2 API note:** All ChromaDB API calls in production use the `/api/v2/` path. The `/api/v1/` path returns HTTP 410 Gone. All client code, ingestion scripts, and RAG service configurations must specify v2 endpoints.

#### 4.8.2 ChromaDB Response Structure

ChromaDB responses contain parallel lists of IDs, distances, metadatas, and documents, where metadata entries include the identifiers needed to rejoin to GBIM entities or to registry rows in `local_resources`. This structure underpins traceable, explainable RAG behaviour and supports reconstruction of which memory elements contributed to a given ensemble answer.

---

### 4.9 Operational Considerations

Using ChromaDB as a production memory layer introduces several practical considerations.

**Reliability and persistence.**
The main ChromaDB instance (`jarvis-chroma`, host port 8002) is backed by persistent on‑disk storage, with regular backups around large ingests and metadata backfills. Legacy local stores are archived or decommissioned to avoid ambiguity.

**Performance and scaling.**
As collections grow into the millions of records, index configuration and hardware resources directly affect query latency and throughput for similarity search. Bulk ingest is performed in batches of ≤100-word chunks (enforced by the `all-minilm` context limit), with attention to index compaction and memory usage. Latency characteristics of chat and search endpoints reflect both model inference and ChromaDB query performance.

**Security and privacy.**
The documented deployment focuses on public or research‑grade data: West Virginia GIS layers, public resource guides, and internal research corpora. Collections containing sensitive user data are excluded or carefully controlled. Conversational or personal‑memory collections are curated before being used in broader contexts.

**Schema and configuration management.**
Collection names, metadata schemas, embedding configurations (model: `all-minilm:latest`, dim: 384, cosine), and RAG routing rules are versioned and recorded. Consolidations are treated as explicit migrations with before/after evaluation. The 100-word chunk size constraint is treated as a fixed schema parameter for all collections using `all-minilm:latest`.

---

### 4.10 Production Deployment Characteristics — March 26, 2026

In production as of March 26, 2026 (56 confirmed live containers, `msjarvis-rebuild` namespace):

| Collection | Status | Items | Notes |
|---|---|---|---|
| `gbim_worldview_entities` | ✅ Live | 5,416,521 | Confirmed — all-minilm 384-dim, cosine |
| `gbim_beliefs_v2` | ✅ Live | Active | Production GBIM belief embeddings |
| `GBIM_sample_rows` | ✅ Live | 5,000 | Test/validation sample |
| `gis_wv_benefits` | ✅ Live | Active | WV benefits facilities |
| `geospatialfeatures` | ✅ Live | 60,000 | Confirmed March 26, 2026 |
| `GBIM_Fayette_sample` | ✅ Live | 1,535 | Confirmed March 26, 2026 |
| `governance_rag` | ✅ Live | 643 chunks | Full DAO corpus + US Constitution; 100-word chunks |
| `commons_rag` | ✅ Live | 306 chunks | Full Commons corpus; 100-word chunks |
| `appalachian_cultural_intelligence` | ✅ Live | 820 | Confirmed March 26, 2026 |
| `spiritual_texts` | ✅ Live | 19,338 | Mother Carrie Protocol |
| `autonomous_learner` | ✅ Live | 21,181+ | Growing ~288/day |
| `ms_jarvis_memory` | ✅ Live | Active | Cross-session continuity |
| `episodic_index` | ✅ Live | Active | Temporal reasoning |
| `conversation_history` | ✅ Live | Active | OI-05 open — pipeline wiring pending |
| `psychological_rag` | ✅ Live | 968 | Port 8006 |
| `msjarvis_docs` | ✅ Live | 2,348 | 52 verified WV community resources + system docs |

All spatial collections use SRID 26917 (UTM Zone 17N NAD83) for spatial coordinates. The GBIM belief and edge tables encode how, why, for whom, authority, and evidence relationships for all 5,416,522 worldview entities. All embeddings across all collections use `all-minilm:latest` (384-dim, cosine) — no exceptions, no planned model upgrades without full collection rebuilds.

---

### 4.11 Limitations and Future Work

Several originally "future‑work" items have now been completed and should be treated as foundations rather than as open tasks:

- A unified GBIM embedding collection (`gbim_beliefs_v2`) populated from `gbimbeliefnormalized` and used by RAG — **confirmed live**
- A West‑Virginia‑biased spatial semantic memory built around `gbim_worldview_entities` with 5,416,521 records — **confirmed live**
- All RAG collections fully populated: `governance_rag` (643), `commons_rag` (306), `geospatialfeatures` (60,000), `GBIM_Fayette_sample` (1,535), `appalachian_cultural_intelligence` (820), `spiritual_texts` (19,338) — **confirmed live March 26, 2026**
- Deterministic joins from ChromaDB results back to GBIM and GeoDB via stable identifiers (`entity_id`, `source_table`, `source_pk`) and to `local_resources` via `local_resource_id` — **confirmed operational**
- `all-minilm:latest` 384-dim embedding model with confirmed 100-word chunk constraint — **confirmed live and documented**

Remaining limitations and genuine future work include:

- **Judge GBIM grounding gap.** Truth and alignment judges still use `heuristic_contradiction_v1` rather than live GBIM queries. This is the highest-priority architectural gap (see Chapter 2, Section 2.8).

- **RAG → gateway inference wiring.** All RAG collections are populated; formal wiring of RAG retrieval into the `jarvis-gateway` inference endpoint is the next sprint milestone.

- **WV Constitution ingest.** US Constitution is ingested (97 chunks in `governance_rag`); WV state constitution is the next governance document to ingest, applying the 100-word chunk rule.

- **Chunk audit for pre-constraint collections.** Collections ingested before the 100-word chunk constraint was formally documented (March 26, 2026) should be audited for oversized chunks that may degrade retrieval quality.

- **Semantic gaps and representational limits.**
  Certain forms of knowledge—embodied experience, oral history, spiritual traditions—are difficult to represent as short text embeddings alone. Additional representational strategies (graphs, qualitative annotations, GBIM‑linked justice metrics, community‑led tagging, and registries like `local_resources`) are needed to supplement the vector store.

- **Evolving schema and topology.**
  As GBIM, GeoDB, RAG services, and Quantarithmia evolve, the set of collections, metadata fields, and indexing strategies will continue to change.

Future work will:

- Maintain consolidated spatial and GBIM belief collections via incremental updates and periodic metadata backfills
- Ingest WV state constitution into `governance_rag` using confirmed 100-word chunking
- Document all collection schemas and RAG routing rules in a single, queryable registry
- Add traced end‑to‑end examples showing ChromaDB retrieval → GBIM provenance → belief‑graph traversal → local resource resolution → ensemble answer
- Explore hybrid memory architectures combining vector stores with graphs, relational databases, and participatory annotation workflows
- Implement incremental sync infrastructure for daily delta updates instead of full rebuilds
- Develop embedding models fine‑tuned on Appalachian place names, infrastructure terminology, and local programme language

**Implementation Status**

**Badge: PRODUCTION — ALL COLLECTIONS LIVE**
The conceptual role of ChromaDB as semantic memory is fully implemented across all planned collections as of March 26, 2026. The `all-minilm:latest` 384-dim embedding model is confirmed live with a documented 100-word chunk constraint that shapes all future ingestion pipelines. A verified `local_resources` band in Postgres complements ChromaDB, providing structured, ZIP‑aware, and periodically re‑verified programme information that Ms. Jarvis uses alongside semantic retrieval to act as an accountable, place‑based Steward System in West Virginia.

---

*Last updated: 2026-03-26, Mount Hope WV — Carrie Kidd (Mamma Kidd)*
*Section 4.5 updated March 26, 2026: `all-minilm:latest` 384-dim embedding confirmed live; "planned embedding model" language removed throughout; 100-word/256-token chunk size constraint documented as confirmed architectural finding.*
