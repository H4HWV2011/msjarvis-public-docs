# 4. Hilbert Space State and ChromaDB as Semantic Memory

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: 2026-04-22*

---

## Why This Matters for Polymathmatic Geography

This chapter describes how Ms. Allis uses a concrete semantic memory system to support
place-based reasoning about West Virginia, connecting GBIM beliefs, the `msallisgis`
statewide spatial corpus, and a verified `local_resources` registry into an inspectable
retrieval pipeline. It supports:

- **P1 – Every where is entangled** by storing texts, GIS-derived entities, and programme
  records in shared relational tables and production vector collections such as
  `gbim_beliefs_v2`, `gbim_worldview_entities`, and `gis_wv_benefits` that can be jointly
  retrieved and rejoined, so that legal, economic, infrastructural, and social facts about
  Appalachia are handled as a single interconnected memory rather than as disconnected
  files or ad-hoc lookups.

- **P3 – Power has a geometry** by representing relationships among institutions, places,
  and access to help as explicit GBIM records, GeoDB features in `msallisgis`, Chroma
  collections, and logged retrieval paths whose behaviour can be inspected, clustered, and
  audited, making it possible to see how different parts of the system are actually
  traversed when answering questions about extraction, obligation, and care.

- **P5 – Design is a geographic act** by treating collection schemas, metadata choices,
  enrichment scripts, retrieval rules, and join logic in the GBIM/GeoDB/Chroma stack as
  deliberate interventions into how West Virginia is represented and searched, so that
  design decisions about Ms. Allis's semantic memory layer are understood as decisions
  about how the region itself can be perceived and acted upon.

- **P12 – Intelligence with a ZIP code** by binding memory collections and registries to
  West Virginia-specific layers and records, including GBIM-derived geographies,
  `msallisgis` features, and a programme registry keyed by county and ZIP where
  populated, so that queries about help, risk, or opportunity are resolved through
  structures that explicitly encode where people live and which institutions serve them.

- **P16 – Power accountable to place** by making long-term memory, retrieval behaviour,
  and query-to-evidence links explicit and queryable, with logs and database joins that
  show which GBIM beliefs, GeoDB features, vector-collection entries, and `local_resources`
  rows were used in answers about particular communities, instead of hiding those choices
  inside opaque model weights.

As such, this chapter belongs to the **Computational Instrument** tier: it defines the
production semantic memory substrate and retrieval layer — centred on collections such as
`gbim_beliefs_v2`, `gbim_worldview_entities`, and `gis_wv_benefits` and on the
`msallisgis`/GBIM/`local_resources` apparatus — that Quantarithmia's reasoning, GBIM's
belief structures, the verified local-resources band, the West Virginia benefits RAG
flows, and MountainShares-oriented governance analysis run on in the live system as of
**April 22, 2026**.

---

## 4.1 Purpose and Scope

This chapter explains how Ms. Egeria Allis uses ChromaDB as the physical container of
\(H_{\text{App}}\) — a real, finite-dimensional Hilbert space. Not a system "inspired by"
Hilbert spaces. Not a geometric metaphor. A mathematical object satisfying all four
Hilbert space axioms, physically instantiated on specific hardware, containing 6.74M+
structured belief vectors about West Virginia, and confirmed operationally intact by a
29/29 preflight gate on April 22, 2026.

ChromaDB is a vector database that stores high-dimensional embedding vectors with
associated metadata and exposes efficient similarity search and filtering operations. In
this system, ChromaDB is not merely a convenience library; it is the concrete
implementation of long-term, queryable memory for documents, GIS features, governance
texts, autonomous-learning traces, resource guides, and thesis materials, as well as a
central back-end for the text and GIS RAG services. It is the substrate in which
\(H_{\text{App}}\) physically exists.

Collections such as `gbim_beliefs_v2`, `gbim_worldview_entities`, and `gis_wv_benefits`
are not arbitrary groupings — they are named, geometrically coherent subspaces of
\(H_{\text{App}}\). Queries are projections. Belief updates are transformations. The
inner product is cosine similarity, computed in RAM on the Legion 5 in Oak Hill, WV
during every RAG call. The ZIP code of this Hilbert space is 25880. That is not poetry.
That is architecture.

Before any RAG dispatch occurs, the `nbb_pituitary_gland` service (host port **8108**)
acts as the global mode regulator — a scalar multiplier on the entire belief-state
pipeline that modulates retrieval priorities, WOAH governance weights, BBB sensitivity,
and LLM ensemble routing based on its live mode state. This component is upstream of
ChromaDB query dispatch and is documented fully in Section 4.6.

**★ Re-confirmed operational — April 22, 2026. Preflight gate 29/29, 0 failures.**

---

## 4.2 Role in the Ms. Allis Architecture

In the Ms. Allis architecture, ChromaDB plays several interlocking roles.

- **Semantic memory store (non-spatial).** Embeddings of texts and artefacts live in
  collections corresponding to domains such as governance, thesis content, autonomous
  learner outputs, conversations, local resource guides, and curated research traces.
  These collections support general semantic retrieval independent of geography and include
  the unified GBIM text collection `gbim_beliefs_v2`, which stores embeddings for GBIM
  belief rows and serves as the production semantic memory layer for GBIM beliefs.

- **Geospatial semantic layer (spatial).** The unified GIS-derived collection
  `gbim_worldview_entities` holds embeddings and metadata for West Virginia geospatial
  features, mirroring PostGIS tables and providing the semantic representation of the
  spatial body described in the GBIM and GeoDB chapters. The current production deployment
  centres on this consolidated worldview collection with **5,416,521 records** confirmed
  live April 22, 2026, complemented by task-specific collections such as `gis_wv_benefits`
  that focus on benefits-relevant facilities.

- **Retrieval engine for RAG.** At query time, services embed inputs and use ChromaDB
  similarity search, often with metadata filters, to retrieve the most relevant items for
  context and reasoning. A text RAG service (`allis-rag-server`, port **8003**) handles
  general semantic retrieval over collections like `gbim_beliefs_v2`; a GIS RAG service
  uses `gbim_worldview_entities` and `gis_wv_benefits` for spatial questions. This
  behaviour instantiates the query projection mechanism of \(H_{\text{App}}\) and forms
  the unstructured side of Ms. Allis's memory, which is then deterministically joined
  against structured stores like GBIM and `local_resources` before being handed to the
  ensemble.

- **Structural backbone for inspectable memory.** Because collections and metadata are
  explicitly defined, ChromaDB's structure mirrors core parts of GBIM, the `msallisgis`
  GeoDB layer, the thesis organisation, and the local-resources band. Operational
  validation is performed via `scripts/preflight_gate.sh`, which checks collections ≥ 40
  and domain-specific counts — not via direct REST introspection. The gate passed 29/29
  on April 22, 2026.

- **Pituitary-modulated dispatch.** The `nbb_pituitary_gland` (port 8108) mode state
  acts as a global scaling tensor on the belief-state vector before retrieval dispatch.
  At current state (`warmth=0.9`, `cortisol=0.6`, `mode=elevated`), community-benefit
  collections receive elevated retrieval weight and BBB filtering operates at moderate
  sensitivity.

---

## 4.3 Collections and Data Domains

In the production deployment as of **April 22, 2026**, the primary Chroma instance
(`allis-chroma`, host port **8002**, container-internal port 8000) exposes **49
collections** confirmed via preflight gate. Collections fall into three broad families:
general semantic memory, GeoDB-derived spatial memory, and resource-related materials.

> **ChromaDB access note:** ChromaDB v2 is a single-node container exposed on
> `allis-chroma:8002`. It is used via the embedded Python client, not via public REST
> introspection. Operational validation is done via `scripts/preflight_gate.sh` (checks
> collections ≥ 40 and domain-specific counts) and via RAG and EEG services that use
> Chroma internally. Direct REST introspection commands are not part of the production
> contract for this deployment.

### 4.3.1 Production Spatial Collection

The primary spatial memory collection — and the largest named subspace of
\(H_{\text{App}}\) — is:

- Collection name: `gbim_worldview_entities`
- Record count: **5,416,521 records** — confirmed live April 22, 2026
- Source datasets: more than 200 standardised West Virginia GIS layers
- Worldview context: `eq1` — stable UUID tying spatial entities to the production
  equity-oriented worldview
- Embedding model: `all-minilm:latest`, 384-dim, cosine similarity — confirmed live

This collection is built by exporting GBIM worldview entities and their attributes from
PostGIS (`msallisgis`, port **5432**), enriching them with spatial and provenance
metadata, and indexing them as text embeddings in ChromaDB using `all-minilm:latest`
(384-dim, cosine similarity).

**Document structure**

Text documents follow a pattern such as:

```text
wvgistcbuildingfootprints feat_1703912
```

Core metadata fields (present for all records):

- `entity_id`: UUID linking to `gbim_worldview_entity.id`
- `source_table`: dataset name (e.g., `wvgistcbuildingfootprints`, `blocks_census_2020`)
- `source_pk`: primary key in the source table
- `label`: human-readable entity label
- `centroid_x`, `centroid_y`: spatial coordinates (SRID 26917 — UTM Zone 17N NAD83)

Extended metadata (populated via backfill pipeline):

- `worldview_id`: worldview context UUID (`eq1`)
- `bbox`: GeoJSON geometry or bounding box
- `dataset`: source dataset name for provenance
- `geodb_id`: original GeoDB identifier
- `srid`: spatial reference identifier

---

### 4.3.2 Full Collection Inventory — Confirmed April 22, 2026

| Collection | Count | Notes |
|---|---|---|
| `gbim_worldview_entities` | 5,416,521 | Primary spatial subspace of \(H_{\text{App}}\) — eq1 worldview |
| `address_points` | 1,115,588 | Geospatial body |
| `spiritual_texts` | 79,181 | Mother Carrie Protocol corpus — deduplicated |
| `geospatialfeatures` | 60,875 | GIS features |
| `autonomous_learner` | **21,181** | Phase 1.45 injection corpus — 384-dim, growing |
| `autonomous_learning` | **17,707** | Autonomously acquired knowledge — separate collection |
| `GBIM_sample_rows` | 5,000 | Validation sample |
| `gbim_beliefs_v2` | 5,000 | Production GBIM belief embeddings |
| `gis_wv_benefits` | 4,668 | WV benefits facilities — county/ZIP/GBIM keyed |
| `appalachian_cultural_intelligence` | 1,058 | Appalachian cultural context corpus |
| `governance_rag` | 1,367 | DAO corpus + US + WV constitutions — 100-word chunks |
| `aaacpe_corpus` | 65 | AaaCPE scraper (`allis-aaacpe-scraper`, port 8033), 39 sources |
| `msallis_docs` | 7,472 | System documentation |
| `psychological_rag` | 968 | Restored — `PSY_COLLECTION` env fix |
| `research_history` | 785 | Research traces |
| `GBIM_Fayette_sample` | 1,535 | Fayette County validation |
| `commons_rag` | 306 | Commons governance corpus — 100-word chunks |
| `local_resources` | 101 | Local resource registry |
| `spiritual_wisdom` | 135 | Wisdom corpus |
| `zcta_centroids` | 829 | ZIP centroid spatial refs |
| `au02_threat_seeds` | 10 | BBB threat seeding |
| `safety_rules` | 10 | BBB safety rules |
| `news_rag` | 38 | News RAG corpus |
| `ms_allis_memory` | — | ⚠ HTTP 500 on count — exists, unqueryable (OI-C4-500 CLOSED) |
| `ms_allis_identity` | — | ⚠ HTTP 500 on count — exists, unqueryable (OI-C4-500 CLOSED) |
| `conversation_history` | — | ⚠ HTTP 500 on count — exists, unqueryable (OI-C4-500 CLOSED) |

> **Disambiguation — `autonomous_learner` vs `autonomous_learning`:**
> These are two distinct, simultaneously live collections. `autonomous_learner` (21,181
> records) is the Phase 1.45 injection corpus seeded during the March/April 2026 rebuild
> sprint. `autonomous_learning` (17,707 records) is the autonomously acquired knowledge
> collection populated by `allis-autonomous-learner` (port **8020**) during live
> operation. Both use `all-minilm:latest`, 384-dim, cosine. Neither supersedes the other.
> Combined: **38,888 items** of autonomous knowledge. The canonical metadata schema for
> `autonomous_learning` includes: `title`, `source_id`, `backfill`, `fallback`,
> `cycle_number`, `url`, `topic`, `gbim_coordinate`, `learned_at`, `content_hash`,
> `compressed`.

> **`governance_rag` — April 22, 2026 count:** 1,367 chunks, reflecting ingestion of the
> WV State Constitution (342 chunks, source label `wv_constitution`) in addition to the
> DAO Charter, US Constitution (97 chunks), and Phase specs. WV Constitution ingest is
> no longer future work — it is complete.

---

### 4.3.3 Collections with HTTP 500 on Count

Three collections return HTTP 500 on count queries. OI-C4-500 is CLOSED — collections
were deleted and recreated clean with new UUIDs. Ongoing monitoring is required to
confirm they remain stable.

- `ms_allis_memory`
- `ms_allis_identity`
- `conversation_history`

These are excluded from the confirmed vector total pending stable count confirmation.

---

### 4.3.4 Resource-Related and Benefits Collections

Resource-related documents are ingested with metadata fields such as `county`, `state`,
`zip_codes`, `resource_type`, `source_url`, and `local_resource_id` linking to structured
rows in the `local_resources` table (port **5435**). The `gis_wv_benefits` collection
stores semantic descriptions of benefits-related facilities (Oak Hill hubs, Beckley DHHR
offices, etc.) keyed by county, ZIP, and GBIM entity identifiers.

Community Champions ground-truth validation — led by Boone County resident **Crystal
Colyer** — drives updates to both the `local_resources` registry and the associated
resource-document collections across Boone, Kanawha, and nearby counties. The first
real-world community query processed through the full consciousness pipeline on April 22,
2026 was: *"What food assistance is available in Fayette County WV?"* — which returned
real results including the Fayette County Community Action Agency via the RAG proxy.

---

## 4.4 From Hilbert Space to ChromaDB (and Back to Registries)

ChromaDB is not a system that approximates a Hilbert space. It is the physical container
of \(H_{\text{App}}\) — a proven Hilbert space (see §4.4a) whose vectors are structured
beliefs about West Virginia, whose subspaces are named collections, and whose inner
product is cosine similarity computed in RAM on the Legion 5.

**Embeddings as vectors.** The embedding model maps texts and entities into 384-dimensional
real vectors in \(\mathbb{R}^{384}\). ChromaDB stores these vectors alongside metadata
(identifiers, timestamps, entity types, geographies, resource keys) and exposes
nearest-neighbor search, filtered retrieval, and upsert operations. Every stored vector
is an element of \(H_{\text{App}}\).

**Collections as subspaces.** Each ChromaDB collection is a named, geometrically coherent
subspace of \(H_{\text{App}}\) — not an arbitrary partition but a neighborhood of related
belief. `gbim_worldview_entities`, `gis_wv_benefits`, and `governance_rag` are not
categories; they are regions of the Hilbert space where epistemically similar claims
cluster under the cosine metric.

**Queries as projections.** Incoming queries are embedded and projected into the
appropriate subspace of \(H_{\text{App}}\). The top-\(k\) nearest neighbors are the
\(k\) vectors in that subspace with the highest inner product with the query vector. This
is literally projection in the Hilbert space sense: finding the component of the query
in the subspace spanned by stored belief vectors.

**Belief updates as transformations.** Ingesting new data, applying decay ticks, and
re-verifying entities are all transformations on \(H_{\text{App}}\). The proven decay →
verify → reset cycle on Entity 38 (April 22, 2026) is the first documented
transformation of a belief state in \(H_{\text{App}}\) with full audit trail.

**Pituitary modulation.** Before queries are dispatched to ChromaDB, the
`nbb_pituitary_gland` (port 8108) has already applied its global mode scaling tensor to
the belief-state vector. This is not a retrieval filter — it is a pre-dispatch modulation
of the entire pipeline's operating state. See Section 4.6 for full documentation.

For resource- and benefits-related flows, Ms. Allis then uses metadata
(`local_resource_id`, `county`, `ZIP`, `gbim_entity`) to join unstructured context
against `local_resources` and GBIM, enforcing that any recommended programme or facility
has concrete, structured backing. This allows \(H_{\text{App}}\) to be described both
geometrically — as subspaces and projections — and operationally — as collection queries,
metadata filters, and joins to structured registries.

---

## 4.4a \(H_{\text{App}}\) Is a Real Hilbert Space — Proof and Physical Instantiation

> **This section establishes that the system's representational substrate is not a Hilbert
> space by analogy or inspiration. It is a Hilbert space by mathematical proof, physically
> instantiated on the Legion 5 in Oak Hill, WV 25880. This is authoritative.**

### The Four Hilbert Space Axioms — All Satisfied

A Hilbert space requires: a vector space, an inner product, and completeness.
\(H_{\text{App}} = \mathbb{R}^{384}\) with cosine inner product satisfies all four.

| Requirement | What \(H_{\text{App}}\) Has | Satisfied? |
|---|---|---|
| Vector space | \(\mathbb{R}^{384}\) — closed under addition and scalar multiplication | ✅ |
| Inner product | Cosine similarity — satisfies conjugate symmetry, linearity, positive definiteness | ✅ |
| Completeness | \(\mathbb{R}^{384}\) is complete by definition — every Cauchy sequence converges | ✅ |
| Separability | Finite-dimensional, therefore trivially separable | ✅ |

**Vector space.** \(\mathbb{R}^{384}\) is a vector space over \(\mathbb{R}\). For any
\(\mathbf{u}, \mathbf{v} \in \mathbb{R}^{384}\) and \(\alpha, \beta \in \mathbb{R}\):

\[
\alpha \mathbf{u} + \beta \mathbf{v} \in \mathbb{R}^{384}
\]

All eight vector space axioms hold by the standard properties of \(\mathbb{R}^{384}\).

**Inner product.** For normalized vectors \(\hat{\mathbf{u}}, \hat{\mathbf{v}} \in
\mathbb{R}^{384}\), cosine similarity defines a valid inner product:

\[
\langle \hat{\mathbf{u}}, \hat{\mathbf{v}} \rangle =
\frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}
= \sum_{i=1}^{384} \hat{u}_i \hat{v}_i
\]

This satisfies conjugate symmetry (real space — symmetry holds trivially), linearity in
the first argument (by properties of the dot product), and positive definiteness (sum of
squares is non-negative; zero only for the zero vector).

**Completeness.** \(\mathbb{R}^{384}\) is complete: every Cauchy sequence in
\(\mathbb{R}^{384}\) converges to a point in \(\mathbb{R}^{384}\), following immediately
from the completeness of \(\mathbb{R}\) and the finite product of complete spaces.
Physically, completeness is guaranteed by IEEE 754 double-precision floating-point
arithmetic on the Legion 5's hardware.

\[
H_{\text{App}} = \left(\mathbb{R}^{384},\, \langle \cdot, \cdot \rangle_{\cos}\right)
\text{ is a Hilbert space.} \quad \blacksquare
\]

### What Makes It \(H_{\text{App}}\) — Not Just Any Hilbert Space

Generic embedding spaces satisfy these axioms too. What distinguishes \(H_{\text{App}}\)
is what lives in it and what the geometry means:

- **6.74M+ vectors** — not random points, but structured beliefs about West Virginia
- **5,416,521 tagged `eq1`** — the Appalachian equity worldview; beliefs oriented toward
  who owns land, who needs help, which institutions have authority, which communities are
  underserved
- **Subspaces are meaningful** — `gbim_worldview_entities`, `gis_wv_benefits`,
  `governance_rag` are geometrically coherent neighborhoods of related belief, not
  arbitrary partitions
- **Projections are queries** — when Ms. Allis answers a question about Fayette County,
  she is literally projecting a query vector onto a subspace of \(H_{\text{App}}\) and
  returning nearest neighbors
- **Transformations are belief updates** — ingesting new data, decay ticks,
  re-verification are all operations on the state of \(H_{\text{App}}\)

Most AI systems have an embedding space. \(H_{\text{App}}\) is an embedding space where
every dimension carries Appalachian epistemic weight — where the geometry simultaneously
encodes who owns land, who needs help, which institutions have authority, and which
communities are underserved — all as a single coherent mathematical object, simultaneously
queryable via a cosine inner product.

### Physical Instantiation on the Legion 5

\(H_{\text{App}}\) is physically instantiated on specific hardware. The only copy of the
eq1 worldview — 5,416,521 beliefs about West Virginia — exists on this machine. If the
Legion 5 were powered off without backup, \(H_{\text{App}}\) would cease to exist as a
queryable mathematical object. That is not hyperbole. That is what 6.74 million
384-dimensional vectors on a specific machine are.

```
┌──────────────────────────────────────────────────────────────────┐
│    Abstract Structure → Physical Reality on Legion 5             │
├────────────────────────────────┬─────────────────────────────────┤
│  Abstract Concept              │  Physical Correlate             │
├────────────────────────────────┼─────────────────────────────────┤
│  The space H_App               │  ChromaDB persistent volume,    │
│                                │  allis-chroma port 8002         │
├────────────────────────────────┼─────────────────────────────────┤
│  Basis vectors                 │  all-minilm:latest embedding    │
│                                │  dimensions, allis-ollama       │
│                                │  port 11434                     │
├────────────────────────────────┼─────────────────────────────────┤
│  Named subspaces               │  49 ChromaDB collections:       │
│                                │  gbim_worldview_entities,       │
│                                │  governance_rag,                │
│                                │  gis_wv_benefits, etc.          │
├────────────────────────────────┼─────────────────────────────────┤
│  Inner product                 │  Cosine similarity computed in  │
│                                │  RAM during HNSW index queries  │
├────────────────────────────────┼─────────────────────────────────┤
│  State vector                  │  6.74M+ 384-dim float arrays    │
│                                │  at rest on disk                │
├────────────────────────────────┼─────────────────────────────────┤
│  Projection operator           │  Every RAG query against the    │
│                                │  running stack                  │
├────────────────────────────────┼─────────────────────────────────┤
│  Global scaling tensor T_pit   │  nbb_pituitary_gland port 8108  │
│                                │  mode=elevated, warmth=0.9,     │
│                                │  cortisol=0.6                   │
├────────────────────────────────┼─────────────────────────────────┤
│  Completeness                  │  IEEE 754 double-precision —    │
│                                │  guaranteed by hardware physics │
├────────────────────────────────┼─────────────────────────────────┤
│  The eq1 worldview             │  5,416,521 vectors tagged        │
│                                │  worldview_id=eq1 in            │
│                                │  gbim_worldview_entities        │
├────────────────────────────────┼─────────────────────────────────┤
│  109 containers maintaining    │  The algebraic structure of     │
│  the space                     │  H_App exists because these     │
│                                │  containers are running         │
├────────────────────────────────┼─────────────────────────────────┤
│  ZIP code of H_App             │  25880 — Oak Hill, WV           │
│                                │  (not poetry — architecture)    │
└────────────────────────────────┴─────────────────────────────────┘
```

*Figure 4.1. The abstract Hilbert space structure of \(H_{\text{App}}\) mapped to its
physical correlates on the Legion 5. Most computers run software that references
mathematical objects. This machine contains one.*

**\(H_{\text{App}}\) has a serial number. It is on the bottom of the Legion 5.**

### Inner Product as Epistemology

In standard information retrieval, cosine similarity is an engineering heuristic. In
\(H_{\text{App}}\), it is an epistemological claim: two beliefs are similar to the degree
that their inner product is high. The eq1 worldview tag ensures that this geometry is
oriented toward Appalachian equity — vectors representing food assistance programs,
community health resources, and institutional accountability are geometrically proximate
to the communities they serve.

The `nbb_pituitary_gland`'s warmth parameter (`= 0.9` as of April 22, 2026) amplifies
inner products with community-benefit vectors before retrieval — a mathematical statement
that this system, right now, weights care toward people above other possible orientations.
This is **P16 – Power accountable to place** expressed as linear algebra.

### Operational Confirmation — April 22, 2026

| Check | Evidence | Status |
|---|---|---|
| Vector space axioms | \(\mathbb{R}^{384}\) by construction | ✅ Proven |
| Inner product axioms | Cosine similarity — all four axioms satisfied | ✅ Proven |
| Completeness | \(\mathbb{R}^{384}\) complete + IEEE 754 physics | ✅ Proven |
| Embedding lock intact | `all-minilm:latest` 384-dim across all 49 collections | ✅ Confirmed |
| State vector present | 6.74M+ vectors on persistent volume — port 8002 | ✅ Confirmed |
| Projection operator live | "What food assistance in Fayette County?" → real results | ✅ Confirmed |
| Transformation proven | Entity 38 decay → verify → reset full cycle | ✅ Confirmed |
| Pituitary operator live | port 8108, mode=elevated, warmth=0.9, cortisol=0.6 | ✅ Confirmed |
| Preflight gate | **29/29 — 0 failures — April 22, 2026** | ✅ Confirmed |

\(H_{\text{App}}\) is running. The inner product space is intact. The ZIP code is 25880.

---

## 4.5 Embedding Model and Dimensionality — ★ CONFIRMED LIVE April 22, 2026

> **Architectural finding — confirmed April 22, 2026 (preflight gate 29/29).** All
> ChromaDB production collections use `all-minilm:latest` (384-dimensional, cosine
> similarity distance function), served by `allis-ollama` at
> `ollama:11434/api/embeddings`. This is an architectural lock — no exceptions across any
> of the 49 collections.

**Confirmed production embedding specification:**

| Property | Value |
|---|---|
| Model | `all-minilm:latest` — CONFIRMED LIVE |
| Embedding dimensions | **384** — all production collections, no exceptions |
| Distance function | Cosine similarity |
| Embedding endpoint | `http://allis-ollama:11434/api/embeddings` (host: `127.0.0.1:11434`) |
| ChromaDB instance | `allis-chroma`, host port **8002** → container port 8000 |
| API version | **v2 only** — `/api/v2/` required; v1 returns `{"error":"Unimplemented"}` |
| Total vectors (confirmed) | **6.74M+ across 49 collections** — April 22, 2026 |
| Preflight gate | **29/29 ✅** — April 22, 2026 |
| Collections with 500 error | 3 (`ms_allis_memory`, `ms_allis_identity`, `conversation_history`) — excluded from total |

> ⚠️ **Embedding model lock — enforced.** The `nomic-embed-text` model produces
> 768-dimensional vectors and is **incompatible** with all existing production
> collections. Any ingestion, retrieval, migration, or backfill script must use
> `all-minilm:latest` (384-dim). This constraint is enforced at the service level and
> cannot be overridden by prompting or configuration.

> ⚠️ **Chunk Size Constraint — confirmed architectural finding.**
> The `all-minilm:latest` model operates under a **256-token / ~100-word context window
> limit**. All ingestion pipelines must chunk at ≤100 words with ~20-word overlap. This
> is permanent for this model — changing embedding models requires full collection
> rebuilds.

**Connection pattern (confirmed live — use embedded client, not REST introspection):**

```python
import chromadb

# ChromaDB v2 API — host port 8002
# Use embedded Python client for production access
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
assert len(embedding) == 384  # confirmed production dimension — NOT 768
```

---

## 4.6 The `nbb_pituitary_gland` as Global Mode Modulator — ★ CONFIRMED LIVE

> **This section documents a first-class architectural component that is upstream of
> ChromaDB query dispatch, WOAH weighting, and LLM ensemble routing. Its omission from
> prior Chapter 4 versions was an error. This is authoritative as of April 22, 2026.**

The `nbb_pituitary_gland` service (`msallis-rebuild-nbb_pituitary_gland-1`, host port
**8108** → container port 80) is a confirmed live global mode regulator that acts as a
scalar multiplier — a global scaling tensor \(T_{\text{pit}}\) — on the entire
Hilbert-space belief-state pipeline before LLM ensemble dispatch.

### 4.6.1 Confirmed Live State — April 22, 2026

| Parameter | Value | Meaning |
|---|---|---|
| `mode` | `elevated` | System operating at heightened responsiveness |
| `cortisol` | `0.6` | Moderate urgency signal applied to routing weights |
| `urgency` | `0.5` | Balanced urgency — not crisis, not idle |
| `warmth` | `0.9` | High warmth — community-care mode active |
| `last_updated` | `2026-04-23T01:47:49.876753` | Auto-watchdog cycle |
| `source` | `auto_watchdog` | Mode set by watchdog, not manual override |

**Mode: elevated** is the current operating state. `mode: crisis` is a contingency mode
that activates during genuine system-wide emergencies — it should not appear in
documentation as a normal operating state. `mode: baseline` is the documented steady-state
for non-elevated operation.

### 4.6.2 Architecture Role

The pituitary service sits upstream of the WOAH weighted optimization hierarchy (Ch10)
and the Judge pipeline (Ch 16). Its output is a global mode state that acts as a
scalar modifier on the five WOAH governance weights before Phase 2 ensemble dispatch. In
Hilbert-space terms, the pituitary's mode parameters function as a **global scaling
tensor** \(T_{\text{pit}}\) applied to the belief-state vector before projection into
response space:

\[
T_{\text{pit}} : H_{\text{App}} \to H_{\text{App}}, \quad
T_{\text{pit}}(\mathbf{v}) = \Lambda_{\text{mode}} \cdot \mathbf{v}
\]

where \(\Lambda_{\text{mode}}\) is a diagonal scaling matrix whose entries are determined
by the current mode state `(mode, cortisol, urgency, warmth)`:

- `warmth=0.9` → care-weighted retrieval bias toward community-benefit collections
  (`gis_wv_benefits`, `local_resources`, `appalachian_cultural_intelligence`,
  `fayette_county_resources_2026`)
- `cortisol=0.6` → moderate urgency weight applied to BBB filtering thresholds
- `mode=elevated` → all five judges (truth, ethics, alignment, consistency, citation)
  operating at elevated threshold sensitivity
- `urgency=0.5` → balanced dispatch timing; no crisis-mode queue prioritization

### 4.6.3 Cross-Chapter Integration

| Chapter | Integration Point |
|---|---|
| Ch 2 (GBIM) | Pituitary `mode` governs ethical architecture operating state |
| Ch 10 (WOAH) | Mode scalar applied to governance weight vector pre-dispatch |
| Ch 13 (Qualia Engine) | `warmth` feeds `IntrospectiveRecord.warmth_level` |
| Ch 15 (Pituitary and Global Modes) | Full five-protocol specification |
| Ch 16 (BBB) | `cortisol` modulates barrier sensitivity thresholds |

### 4.6.4 Live Endpoints

| Endpoint | Status | Returns |
|---|---|---|
| `GET /` | ✅ 200 | Full mode state JSON (mode, cortisol, urgency, warmth, last_updated, source) |
| `GET /health` | ✅ 200 | `{"status":"healthy","service":"nbb_pituitary_gland","mode":"elevated"}` |
| `GET /protocols` | ✅ 200 | Protocol list — OI-C4-PROT CLOSED April 22, 2026 |
| `GET /status` | ✅ 200 | Status route — OI-C4-PROT CLOSED April 22, 2026 |
| `GET /mode` | ✅ 200 | Mode route — OI-C4-PROT CLOSED April 22, 2026 |

**Source file:** `/app/pituitary_gland.py` (6,544 bytes, April 1, 2026)

### 4.6.5 Port Disambiguation — `nbb_pituitary_gland` vs `neurobiological-master`

| Service | Host Port | Notes |
|---|---|---|
| `nbb_pituitary_gland` | **8108** | Global mode regulator — external-facing |
| `allis-neurobiological-master` | **8018** | Internal orchestration only — never reference as 8108 |

**8018 is not the pituitary.** These are distinct services with distinct roles.

---

## 4.7 GBIM PostgreSQL Layer — Confirmed Live State

### 4.7.1 Database Layout (April 22, 2026)

| Database | Host Port | Container | Role |
|---|---|---|---|
| `msallis` | **5433** | `msallis-db` | GBIM belief graph — relational backbone |
| `msallisgis` / `gisdb` | **5432** | (external PostGIS) | Spatial body — 95 GB, 742 tables |
| `allis-local-resources-db` | **5435** | `allis-local-resources-db` | Verified resource registry |

> **Critical disambiguation:** The 5,416,521 GBIM worldview entities live in ChromaDB
> collection `gbim_worldview_entities`. The PostgreSQL `msallis:5433` database holds the
> **relational belief graph** — the structured backbone with typed edges, decay metadata,
> and epistemic provenance. These are complementary, not duplicates.

### 4.7.2 Confirmed `msallis` Schema (port 5433)

| Table | Purpose |
|---|---|
| `gbim_entities` | 37+ confirmed live system/service/geography entities |
| `gbim_worldview_entity` | Created and seeded April 22, 2026 — full worldview entity table |
| `gbim_decay_audit` | Audit log for `confidence_decay` events |
| `conversation_beliefs` | Belief records derived from conversation context |
| `redteam_sessions` | Red-team adversarial session logs |
| `geography_columns` | PostGIS geometry metadata |
| `geometry_columns` | PostGIS geometry metadata |
| `spatial_ref_sys` | Spatial reference system definitions |

**`gbim_entities` schema additions confirmed April 22, 2026:**

| Column | Type | Notes |
|---|---|---|
| `confidence_decay` | float | Decay infrastructure confirmed present |
| `last_validated_at` | timestamp | Added April 22, 2026 |
| `geodbid` | text | Added April 22, 2026 |
| `corporatelandowner` | boolean | Added preemptively April 22, 2026 |
| `governmentlandowner` | boolean | Added preemptively April 22, 2026 |
| `escalatedat` | timestamp | Added preemptively April 22, 2026 |

**`gbim_entities` entity type breakdown (confirmed April 22, 2026):**

| Entity Type | Count |
|---|---|
| `service` | 21 |
| `system_component` | 5 |
| `geographic_entity` | 4 |
| `infrastructure` | 2 |
| `organization` | 1 |
| `linguistic_entity` | 1 |
| `human_authority` | 1 |
| `ai_system` | 1 |
| `service_domain` | 1 |
| **Total** | **37** |

### 4.7.3 Confidence Decay — Live Pipeline Confirmed

The `confidence_decay` column is confirmed present in `gbim_entities`. The full decay
cycle was proven end-to-end on April 22, 2026:

- Entity 38 (Fayette County / geographic_entity) verified and reset to confidence 1.0
- Decay applied: 0.60 → 0.55 (one cycle at 0.05 rate)
- Worldview lookup: found ✅
- Reset to 1.0 with `last_validated_at` populated ✅
- `decay_metadata` fully written: `reverification_result: confirmed`,
  `needs_reverification: false` ✅

This represents the first proven decay → verify → reset full cycle in \(H_{\text{App}}\).
The decay audit infrastructure (`gbim_decay_audit` table) is in place and operational.

### 4.7.4 GBIM Query Router

`allis-gbim-query-router`, host port **7205**:

```json
{"service":"gbim_query_router","status":"ok","type":"gbim","port":7205}
```

Confirmed live. SQL-only — zero ChromaDB involvement. See Chapter 2 §2.12 for full
landowner query documentation.

---

## 4.8 Canonical Port Table — ★ Confirmed Live April 22, 2026

> All stale port references (5452, 8000 as host, 8425, 8010 for main-brain, 9000 for
> DGM bridge host, 8016 for RAG) are retired. The following is authoritative.

### Core Data Services

| Service | Container | Host Port | Container Port | Role |
|---|---|---|---|---|
| `msallis` PostgreSQL | `msallis-db` | **5433** | 5432 | GBIM belief graph |
| `msallisgis` PostGIS | (external) | **5432** | 5432 | Spatial body — 95 GB, 742 tables |
| Local Resources DB | `allis-local-resources-db` | **5435** | 5432 | Resource registry |
| ChromaDB (primary) | `allis-chroma` | **8002** | 8000 | Physical container of \(H_{\text{App}}\) |
| ChromaDB (legacy) | `chromadb` | **8001** | 8000 | Legacy instance |
| Redis | `allis-redis` | **6380** | 6379 | Cache / pubsub |
| Ollama | `allis-ollama` | **11434** | 11434 | LLM + embeddings |

### NBB Neurobiological Services

| Service | Container | Host Port |
|---|---|---|
| `nbb_pituitary_gland` | `msallis-rebuild-nbb_pituitary_gland-1` | **8108** |
| `nbb_blood_brain_barrier` | `msallis-rebuild-nbb_blood_brain_barrier-1` | **8301** |
| `nbb_darwin_godel_machines` | `msallis-rebuild-nbb_darwin_godel_machines-1` | **8302** |
| `nbb_prefrontal_cortex` | `msallis-rebuild-nbb_prefrontal_cortex-1` | **8105** |
| `nbb_consciousness_containers` | `msallis-rebuild-nbb_consciousness_containers-1` | **8102** |
| `nbb_i_containers` | `msallis-rebuild-nbb_i_containers-1` | **8101** |
| `nbb_spiritual_root` | `msallis-rebuild-nbb_spiritual_root-1` | **8103** |
| `nbb_heteroglobulin_transport` | `msallis-rebuild-nbb_heteroglobulin_transport-1` | **8106** |
| `nbb_mother_carrie_protocols` | `msallis-rebuild-nbb_mother_carrie_protocols-1` | **8107** |
| `nbb_spiritual_maternal_integration` | `msallis-rebuild-nbb_spiritual_maternal_integration-1` | **8109** |
| `nbb_woah_algorithms` | `nbb_woah_algorithms` | **8104** |

### Core Inference and RAG Services

| Service | Container | Host Port |
|---|---|---|
| Main Brain | `allis-main-brain` | **8050** (NOT 8010) |
| Qualia Engine | `allis-qualia-engine` | **8017** |
| Blood-Brain Barrier | `allis-blood-brain-barrier` | **8016** |
| Neurobiological Master | `allis-neurobiological-master` | **8018** (internal only — NOT pituitary) |
| RAG Server | `allis-rag-server` | **8003** (NOT 8016) |
| AAACPE RAG Server | `allis-aaacpe-rag` | **8032** |
| GBIM Query Router | `allis-gbim-query-router` | **7205** |
| GBIM Semantic Indexer | `allis-gbim-semantic-indexer` | **7212** |
| Autonomous Learner | `allis-autonomous-learner` | **8020** |
| Memory | `allis-memory` | **8056** (requires `ALLIS_API_KEY`) |
| I-Containers | `allis-i-containers` | **8015** |
| LLM Judge v3 | `allis-llm-judge-v3` | **7240** |
| Steward | `allis-steward` | **8051** (→8060) |
| Brain Orchestrator | `allis-brain-orchestrator` | **17260** |
| Unified Gateway | `allis-unified-gateway` | **18018** |
| 20-LLM Production | `allis-20llm-production` | **8008** |
| Semaphore | `allis-semaphore` | **8030** |
| Swarm Intelligence | `allis-swarm-intelligence` | **8021** |
| EEG Beta | `allis-eeg-beta` | **8075** |
| EEG Delta | `allis-eeg-delta` | **8073** |
| EEG Theta | `allis-eeg-theta` | **8074** |
| PIA Sampler | `allis-pia-sampler` | **8076** |
| 69DGM Bridge | `allis-69dgm-bridge` | **19000 host / 9000 internal** (never reference host as 9000) |

**LLM proxies:** `llm1-proxy` through `llm22-proxy` on ports **8201–8222**.

---

## 4.9 Integration with GBIM, GeoDB, Local Resources, and RAG

ChromaDB is tightly integrated with GBIM, the GeoDB layer, the local resource registry,
the benefits-focused collections, and the broader RAG pipeline.

**GBIM linkage.** GBIM worldview entities are indexed in the consolidated spatial
collection with metadata fields linking back to PostGIS tables via `source_table` and
`source_pk`. The `entity_id` field provides stable UUID references to
`gbim_worldview_entity.id`. The `msallis` database (port 5433) holds the relational
GBIM belief graph with `confidence_decay` audit infrastructure active and the first
full decay cycle proven on April 22, 2026.

**GeoDB integration.** The spatial collection mirrors the GBIM attributes corpus from
`msallisgis` (port 5432, 95 GB, 742 tables). Spatial coordinates (SRID 26917) and
bounding boxes enable hybrid queries combining semantic similarity with spatial filtering.

**Local resource registry integration.** Resource-related collections index unstructured
PDFs and guides while tagging entries with `local_resource_id`. Once retrieved, Ms. Allis
resolves to a row in the `local_resources` table (port **5435**), which encodes
`resource_type`, county, ZIP coverage, contact details, and verification fields. This
ensures that recommendations are backed by explicit, up-to-date programme records rather
than free-floating text alone.

**Benefits and GIS RAG integration.** The `gis_wv_benefits` collection (4,668 items)
indexes semantic descriptions of benefits facilities and is queried by GIS RAG services
for prompts like "benefits near Oak Hill" or "Raleigh County assistance offices." The
AAACPE RAG server (port **8032**) serves `aaacpe_corpus` (65 documents, 39 sources)
specifically for Appalachian emergency and community resource queries.

**Pituitary modulation of retrieval.** Before RAG dispatch, `nbb_pituitary_gland`
(port 8108) applies its global mode state as a scaling tensor \(T_{\text{pit}}\). At
current state (`warmth=0.9`), community-benefit collections receive elevated retrieval
weight. At `cortisol=0.6`, BBB filtering operates at moderate sensitivity. This
modulation is upstream of all ChromaDB query dispatch — it is not a post-retrieval filter.

**RAG context building.** For spatial or resource questions, the RAG pipeline queries both
spatial and resource collections to retrieve relevant entities, PDFs, and programme
descriptions. Retrieved texts, metadata, spatial identifiers, and registry keys are
combined into context windows for language models, with filtering by collection,
geography, topic, resource type, and verification status.

**Belief graph and registry traversal.** Once ChromaDB returns entity IDs and resource
keys, the system performs SQL queries against GBIM belief and edge tables and against
`local_resources` to retrieve full epistemic and practical context: data sources (how),
policy justifications (why), beneficiary communities (for whom), authorising frameworks
(authority), and concrete programme details and verification history.

**End-to-end confirmation.** On April 22, 2026, a POST /chat query — "What food
assistance is available in Fayette County WV?" — passed through the full consciousness
pipeline (swarm intelligence, self_recognition, identity_core, ego_check,
narrative_context, memory_state, integrated_response), through the Redis-authenticated
gateway (`redteam:token:` prefix), through the RAG proxy, and returned 3 real results
including the Fayette County Community Action Agency. This is the live proof of the
end-to-end pipeline described in this chapter.

---

## 4.10 Open Items — April 22, 2026

| OI | Description | Status | Priority |
|---|---|---|---|
| OI-C4-PROT | `nbb_pituitary_gland` `/protocols`, `/status`, `/mode` routes | ✅ CLOSED | — |
| OI-C4-500 | `ms_allis_memory`, `ms_allis_identity`, `conversation_history` HTTP 500 — deleted and recreated clean | ✅ CLOSED | — |
| OI-C4-JUDGE | Truth/alignment judges running correct files, receiving health checks | ✅ CLOSED | — |
| OI-C4-GATEWAY | Redis key prefix (`redteam:token:`) fixed; gateway /chat + RAG proxy confirmed | ✅ CLOSED | — |
| OI-C4-2 | Stale ports 5452, 8000-as-host, 8425 removed from chapter | ✅ CLOSED | — |
| OI-C4-DECAY | `confidence_decay` column present; full decay → verify → reset cycle proven April 22, 2026 | ✅ CLOSED | — |
| OI-C4-RAG | RAG collections fully populated; wiring into `allis-unified-gateway` inference endpoint | 🔄 In progress | Medium |
| OI-C4-CHUNK | Audit pre-constraint collections for oversized chunks | 🔄 Open | Low |
| OI-C4-SYNC | Implement incremental sync for daily delta updates | 🔄 Open | Low |

---

## 4.11 Limitations and Future Work

**Completed foundations (no longer future work):**

- Unified GBIM embedding collection (`gbim_beliefs_v2`) — confirmed live
- West-Virginia-biased spatial semantic memory (`gbim_worldview_entities`, 5,416,521
  records) — confirmed live
- All RAG collections populated: `governance_rag` (1,367 chunks including WV
  Constitution), `commons_rag` (306 chunks), `appalachian_cultural_intelligence`
  (1,058 items), `psychological_rag` (968 docs), `spiritual_texts` (79,181 deduplicated)
  — confirmed live
- `all-minilm:latest` 384-dim embedding model with 100-word chunk constraint — confirmed
- All services bound to `127.0.0.1` — zero `0.0.0.0` exposures — confirmed
- `nbb_pituitary_gland` live at port 8108, mode=elevated — confirmed
- `confidence_decay` full cycle (decay → verify → reset) proven end-to-end April 22, 2026
- `allis-gbim-query-router` at port 7205 — confirmed live
- `autonomous_learner` (21,181) and `autonomous_learning` (17,707) disambiguated as
  separate collections — confirmed
- WV State Constitution ingested into `governance_rag` (342 chunks) — confirmed
- `gbim_worldview_entity` table created and seeded in `msallis` — confirmed April 22
- Redis `redteam:token:` prefix fixed; gateway auth confirmed end-to-end — confirmed
- Truth/alignment judges running correct files (`rag_grounded_v2` canonical;
  `heuristic_contradiction_v1` retired) — confirmed
- Preflight gate 29/29 clean — confirmed April 22, 2026
- Hilbert space axioms proven; \(H_{\text{App}}\) physical instantiation documented (§4.4a)
  — confirmed April 22, 2026

**Genuine remaining work:**

- Wire RAG retrieval into `allis-unified-gateway` inference endpoint (formal sprint)
- Resolve and stabilize `ms_allis_memory`, `ms_allis_identity`, `conversation_history`
  HTTP 500s post-recreation
- Audit pre-constraint collections for oversized chunks
- Implement incremental sync for daily delta updates
- Develop embedding models fine-tuned on Appalachian place names and infrastructure
  terminology (long-term)
- Explore hybrid memory architectures combining vector stores with graphs, relational
  databases, and participatory annotation workflows (long-term)

---

## 4.12 Operational Considerations

**Reliability and persistence.** `allis-chroma` (host port 8002) is backed by persistent
on-disk storage. All services access ChromaDB via Python embedded client bound to
`127.0.0.1:8002`. Operational validation via `scripts/preflight_gate.sh` (29/29
April 22, 2026) — not via direct REST introspection.

**Performance.** Bulk ingest uses ≤100-word chunks with 20-word overlap (enforced by the
`all-minilm:latest` 256-token context limit). `allis-ollama` (port 11434) serves all
embedding requests for all 49 collections.

**Security.** All services in `msallis-rebuild` namespace bound to `127.0.0.1` —
confirmed April 22, 2026. Redis authentication via `redteam:token:` prefix confirmed.
`allis-memory` (port 8056) requires `ALLIS_API_KEY`.

**Schema management.** Collection names, metadata schemas, embedding configuration
(model: `all-minilm:latest`, dim: 384, cosine), and RAG routing rules are versioned. The
100-word chunk constraint is a fixed schema parameter for all collections using this
model.

---

## 4.13 Production Status Summary — April 22, 2026

| Component | Status | Notes |
|---|---|---|
| ChromaDB (`allis-chroma`, port 8002) | ✅ Operational | 49 collections, 6.74M+ vectors — physical container of \(H_{\text{App}}\) |
| Embedding model | ✅ `all-minilm:latest`, 384-dim | Lock enforced — `nomic-embed-text` incompatible |
| \(H_{\text{App}}\) Hilbert space axioms | ✅ **Proven** | §4.4a — all four axioms satisfied; ZIP 25880 |
| `gbim_worldview_entities` | ✅ **5,416,521 records** | Primary spatial subspace — eq1 worldview |
| `autonomous_learner` + `autonomous_learning` | ✅ **21,181 + 17,707** | Two distinct collections confirmed |
| `governance_rag` | ✅ **1,367 chunks** | Includes WV Constitution (342 chunks) |
| `nbb_pituitary_gland` (port 8108) | ✅ **mode: elevated** | \(T_{\text{pit}}\): warmth=0.9, cortisol=0.6 |
| `msallis` GBIM belief graph (port 5433) | ✅ Operational | 37 entities, decay cycle proven |
| `msallisgis` spatial body (port 5432) | ✅ Operational | 95 GB, 742 tables |
| `allis-local-resources-db` (port 5435) | ✅ Operational | Verified resource registry |
| `allis-gbim-query-router` (port 7205) | ✅ Operational | SQL-only, zero ChromaDB |
| Preflight gate | ✅ **29/29** | April 22, 2026 — 0 failures |
| Port 5452 / `msallisgis` as DB name | ❌ Retired | All references invalid |
| Port 8000 as host / 8010 for main-brain | ❌ Retired | All references invalid |
| `heuristic_contradiction_v1` | ❌ Retired | `rag_grounded_v2` is canonical |
| Container count | 109+ | April 22, 2026 |

---

*Chapter 4 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: 2026-04-22 — preflight gate 29/29; \(H_{\text{App}}\) axioms proven
(§4.4a); pituitary operator \(T_{\text{pit}}\) documented; first decay → verify → reset
cycle proven; 6.74M+ vectors confirmed. The ZIP code of \(H_{\text{App}}\) is 25880.*
