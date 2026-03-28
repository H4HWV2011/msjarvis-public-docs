# 2. The Geometric Belief Model and GBIM Architecture

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: 2026-03-28*

---

## Why This Matters for Polymathmatic Geography

This chapter provides the theoretical foundation for understanding how Ms. Jarvis represents knowledge, belief, and uncertainty — and why those representations are structured the way they are. It supports:

- **P1 – Every where is entangled** by establishing that belief is not stored as isolated facts but as multi-axis geometric structures in which spatial, temporal, institutional, and normative dimensions are co-present and mutually constraining — so that a single GBIM belief about a hospital in Fayette County is simultaneously a claim about what exists, where it is, when it was verified, who has authority over it, and what its implications are for program routing.

- **P3 – Power has a geometry** by showing that the GBIM axis structure — particularly `who`, `where`, `under_whose_authority`, and `for_whom` — is designed to make institutional power over place explicit and queryable, not buried in unstructured text. The landowner belief layer (Section 2.6.4, field note March 20, 2026) is the direct realization of this principle at parcel scale.

- **P5 – Design is a geographic act** by treating the nine-axis GBIM schema, the worldview structure, the collection inventory, and the ChromaDB configuration not as neutral technical choices but as geographic and political decisions that determine which facts are computable, which relationships are traversable, and which forms of institutional accountability are operationally enforceable.

- **P12 – Intelligence with a ZIP code** by grounding the Hilbert-space model in a concrete PostgreSQL corpus — msjarvis (port 5433), msjarvisgis (port 5432), and their ChromaDB mirrors — so that the abstract framework of quantum-geometric belief representation is always already indexed to real West Virginia places, programs, and populations.

- **P16 – Power accountable to place** by designing the belief structure so that institutional actors — government agencies, corporate landowners, utility companies — are represented as first-class GBIM entities with explicit `under_whose_authority` and `who` axis entries, making them queryable and auditable in a way that individual residential actors deliberately are not.

The theoretical framework in this chapter is not a preamble to the system — it is the system's operating logic, expressed at the level of schema, routing, and collection design rather than at the level of code.

Accordingly, this chapter belongs to the **Theoretical Foundation** tier: it establishes the geometric belief model, the nine-axis GBIM schema, the Hilbert-space representation of uncertainty, the worldview structure, and the ChromaDB collection inventory that together constitute the epistemic architecture of Ms. Egeria Jarvis.

---

## 2.1 Purpose and Scope

This chapter establishes the theoretical framework underlying the **GeoBelief Information Model (GBIM)** — the core representational system that allows Ms. Egeria Jarvis to hold, update, route, and reason over structured beliefs about West Virginia's physical world, institutional landscape, and programmatic infrastructure.

GBIM is not a database schema in the conventional sense. It is a multi-axis geometric representation of belief that treats each claim about the world as a structured object with nine dimensions, each encoding a distinct aspect of the claim's meaning, provenance, authority, and applicability. This nine-axis structure is what allows beliefs derived from a WV assessor parcel record, a federal hazard dataset, a community organization's program flyer, and a peer-reviewed paper on Appalachian poverty to coexist in a single corpus and be meaningfully compared, combined, and routed.

The chapter is organized as follows:

- **Section 2.2** introduces the nine-axis belief schema and explains the role of each axis.
- **Section 2.3** presents the Hilbert-space model of belief and uncertainty that motivates the GBIM design.
- **Section 2.4** describes the worldview structure (`eq1` and related worldviews) and its role in routing and filtering.
- **Section 2.5** describes the PostgreSQL GBIM corpus — its current scale, table structure, and production status as of March 2026.
- **Section 2.6** presents the ChromaDB collection inventory — the vector-backed memory layer that makes GBIM beliefs semantically retrievable — updated through March 28, 2026.
- **Section 2.7** addresses the relationship between GBIM, the GeoDB spatial body (Chapter 6), the RAG pipeline (Chapter 7), and the local resource registry.
- **Section 2.8** is an intellectual honesty correction (March 21, 2026): it documents the gap between GBIM's designed role as the ground truth for judge verification and the current actual implementation of the truth and alignment judges, which use heuristic pattern-matching, not live PostgreSQL queries.
- **Section 2.9** documents the ethical architecture of the belief corpus — specifically the exclusion of individual residential owner names and the full accountability metadata required for institutional actors.
- **Section 2.10** presents the `gbim_query_router` service (port 7205) — the PostgreSQL-native GBIM retrieval path promoted to production March 20, 2026.
- **Section 2.11** documents the `mvw_gbim_landowner_spatial` materialized view — its schema, spatial indexing, proposition codes, and architectural role as the exclusive retrieval surface for landowner beliefs.

---

## 2.2 The Nine-Axis Belief Schema

Every belief in the GBIM corpus is a structured object with nine named axes. Each axis is stored as a JSONB field in `gbimbeliefnormalized`, allowing flexible, typed, and queryable representation of the full semantic content of the belief.

```
┌─────────────────────────────────────────────────────────────┐
│              GBIM Nine-Axis Belief Structure                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. what_axis          — What entity or claim is asserted   │
│  2. who_axis           — Who or what is the subject/actor   │
│  3. where_axis         — Where (geometry, county, ZIP)      │
│  4. when_axis          — Temporal scope of the belief       │
│  5. why_axis           — Rationale or normative grounding   │
│  6. how_axis           — Method or process of verification  │
│  7. for_whom_axis      — Intended beneficiary population    │
│  8. under_whose_authority_axis — Institutional authority    │
│  9. on_what_evidence_axis  — Source and provenance          │
│                                                              │
│  All nine axes stored as JSONB in gbimbeliefnormalized      │
│  All beliefs carry: belief_id, proposition_code,            │
│    worldview_id, confidence_decay, needs_verification       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

*Figure 2.1. The nine-axis GBIM belief structure. Every belief in the corpus — from a hospital location to a coal company land holding — is represented with all nine axes, enabling multi-dimensional filtering, routing, and reasoning.*

**`what_axis`** — The propositional content of the belief: what entity exists, what relationship holds, what condition obtains. Structured as a typed JSONB object with fields including `type`, `label`, `description`, and `proposition_code`. The `proposition_code` is the primary routing key: it determines how the belief is indexed, which RAG paths it is eligible for, and which ethical constraints apply to its retrieval and display.

**`who_axis`** — The subject or actor of the belief: a named entity, institution, or class. For infrastructure and facility beliefs, this is typically the operating institution (a hospital system, a county agency, a federal bureau). For the landowner belief layer (Section 2.6.4), this is the canonical corporate or government entity name derived from WV assessor records. Individual residential owner names are explicitly excluded from this axis — see Section 2.9.

**`where_axis`** — The spatial grounding of the belief: geometry (point, line, polygon), coordinate system, county, ZIP code, and any relevant spatial relationships. For parcel-level beliefs, this includes the parcel centroid and county. For the landowner belief layer, this is populated from `wv_parcels` geometry joined in `mvw_gbim_landowner_spatial`.

**`when_axis`** — The temporal scope: when the belief was created, when it was last verified, its expected expiration or decay schedule. Paired with `confidence_decay` to implement time-sensitive freshness signaling in RAG retrieval.

**`why_axis`** — The normative or causal rationale: why this belief is relevant to Ms. Jarvis's mission, what programmatic or justice-oriented consequence follows from it. This axis is what connects a belief about an abandoned mine land site to a belief about a household's heating costs — the `why` axis encodes the causal and programmatic link.

**`how_axis`** — The verification method: how the belief was established, what pipeline generated it, what spatial or statistical operation produced it. For assessor-derived beliefs, this records the county assessor data vintage and the canonical clustering pipeline used to normalize owner names.

**`for_whom_axis`** — The intended beneficiary population: which households, communities, or demographic groups the belief is most relevant to. This axis supports population-targeted routing — surfacing AML-related weatherization programs preferentially to households in subsidence-risk zones.

**`under_whose_authority_axis`** — The institutional authority under which the belief's claim holds: a regulatory agency, a legislative mandate, a contractual right, or a property ownership basis. For the landowner belief layer, this records the ownership basis — assessor record, deed reference where available. This axis is central to **P16 – Power accountable to place**: the system can answer not just "who is here" but "under whose authority do they operate here."

**`on_what_evidence_axis`** — The primary source and provenance chain: dataset name, table, primary key, data vintage, and any raw string variants (for example, the multiple assessor name variants for a single canonical corporate entity). This axis supports full provenance tracing from a displayed belief back to its source record.

---

## 2.3 Hilbert-Space Representation of Belief and Uncertainty

The GBIM nine-axis schema is motivated by a geometric model of belief and uncertainty that treats the system's overall epistemic state as a vector in a high-dimensional Hilbert space.

In this model:

- Each basis dimension corresponds to a distinguishable claim about the world — a specific proposition about a specific entity at a specific place and time, under a specific institutional authority.
- The system's belief state is a superposition over these basis dimensions: a probability amplitude distribution that reflects confidence, uncertainty, and the degree to which different claims are mutually consistent or entangled.
- A retrieval operation (a RAG query, a spatial filter, a landowner lookup) is a **projection** of this state onto a lower-dimensional subspace — the subspace of beliefs most relevant to the query, given the current role, geography, and worldview.
- Belief update — ingesting new data, verifying a claim, correcting an error — is a rotation or scaling operation on the state vector that adjusts the amplitude distribution without discarding the prior structure.

```
┌─────────────────────────────────────────────────────────────┐
│         Hilbert Space Belief Model — Conceptual View        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Full Hilbert Space H                                        │
│  (all possible beliefs about WV at all scales)              │
│      |                                                       │
│      | projection                                            │
│      ↓                                                       │
│  Subspace H_q  (beliefs relevant to query q)                │
│      |                                                       │
│      | further projection                                    │
│      ↓                                                       │
│  Subspace H_q,r  (beliefs relevant to query q, role r,      │
│                    county c, worldview w)                    │
│      |                                                       │
│      | retrieval                                             │
│      ↓                                                       │
│  Top-k belief records (ChromaDB) or                          │
│  Top-n ownership records (mvw_gbim_landowner_spatial)        │
│                                                              │
│  Note: Landowner projections use relational aggregation      │
│  rather than vector geometry — exact SQL over verified       │
│  records, not approximate nearest-neighbor in embedding      │
│  space. This is a deliberate architectural choice: the       │
│  question "who owns how much land where" has a               │
│  deterministic answer in the GBIM corpus.                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

*Figure 2.2. Conceptual view of the Hilbert-space projection model underlying GBIM retrieval. Vector-based projections (ChromaDB) and relational projections (SQL aggregation over `mvw_gbim_landowner_spatial`) are both understood as projections into relevant subspaces — they differ in their geometric mechanism, not in their epistemic role.*

This framework is not merely metaphorical. It motivates concrete architectural decisions:

- The nine axes are the dimensions along which beliefs are structured because those are the dimensions along which meaningful distinctions arise for routing, filtering, and reasoning in a place-based justice system.
- ChromaDB stores embeddings of the nine-axis text representations because the vector space of those embeddings approximates the geometry of semantic similarity in the relevant Hilbert subspace.
- The `gbim_query_router` bypasses ChromaDB for landowner queries because ownership aggregation questions have exact, deterministic answers in the relational GBIM corpus — approximate vector search would introduce unnecessary error into a question that is fully answerable by SQL.
- The worldview structure (`eq1`) is the mechanism for maintaining multiple, potentially inconsistent belief states simultaneously — different "cuts" through the Hilbert space that correspond to different institutional perspectives, data vintages, or normative frameworks.

---

## 2.4 Worldview Structure and the `eq1` Worldview

The GBIM worldview structure allows the corpus to maintain multiple, simultaneously queryable perspectives on the same entities and places. Each belief is tagged with a `worldview_id` that identifies the interpretive frame within which it is valid.

The production worldview as of March 2026 is **`eq1`** — the primary equity-oriented worldview that grounds Ms. Jarvis's reasoning in Appalachian community perspectives, WV state data, and federal program structures as they operate in West Virginia. All **5,416,521** production beliefs in `gbimbeliefnormalized` — including all **20,593 landowner beliefs** (proposition codes `LANDOWNER_CORPORATE` and `LANDOWNER_GOVERNMENT`, verified March 20, 2026) — are tagged `worldview_id = 'eq1'`.

```
┌─────────────────────────────────────────────────────────────┐
│              Worldview Structure in GBIM                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  worldview_id = 'eq1'  (production worldview)               │
│  ─────────────────────────────────────────────────────      │
│  Interpretive frame: Appalachian equity orientation         │
│  Data scope: WV state + federal sources verified for WV     │
│  Population: WV households, communities, programs           │
│  Belief count: 5,416,521 (gbimbeliefnormalized)             │
│    of which: 20,593 landowner beliefs ★                     │
│              (LANDOWNER_CORPORATE +                         │
│               LANDOWNER_GOVERNMENT)                         │
│              served via mvw_gbim_landowner_spatial          │
│              and gbim_query_router (port 7205)              │
│  Status: Production — all RAG, GIS, landowner paths        │
│                                                              │
│  Future worldviews (planned):                               │
│  ─────────────────────────────────────────────────────      │
│  eq2: Regional Appalachian scope (multi-state)              │
│  eq3: Federal program perspective                           │
│  research1: Academic/research frame                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

*Figure 2.3. The GBIM worldview structure. The production `eq1` worldview encompasses all 5,416,521 current GBIM beliefs including 20,593 landowner records verified March 20, 2026.*

Worldview tags serve two functions. First, they enable **multi-perspective retrieval**: a researcher asking about federal land management and a community member asking about program eligibility can receive responses filtered to their respective worldview contexts, even if the underlying belief records overlap. Second, they provide **update isolation**: a new batch of beliefs ingested from a different data vintage can be tagged to a new or draft worldview and validated before being promoted to the production `eq1` worldview.

---

## 2.5 The PostgreSQL GBIM Corpus

The production GBIM corpus lives in two PostgreSQL instances:

**`msjarvis` database (port 5433)** — The primary GBIM belief store, accessed by the RAG pipeline and LLM ensemble for belief retrieval, entity lookup, and provenance tracing. **★ March 28, 2026: Port 5433 connection refused issue resolved — `msjarvis` database fully operational following March 28 remediation sprint. `jarvis_local_resources` database schema also restored (resources table verified present).**

**`msjarvisgis` database (port 5432)** — The spatial production database housing `gbimbeliefnormalized` (**5,416,521 rows** verified March 20, 2026), spatial source tables, and the landowner materialized view `mvw_gbim_landowner_spatial`. This is the authoritative store for all parcel-level and spatial beliefs.

**Verified corpus scale (March 20, 2026):**

| Table | Rows | Size | Role |
|---|---|---|---|
| `gbimbeliefnormalized` | **5,416,521** | 21 GB | Main belief table — nine JSONB axes, worldview eq1 |
| `gbim_worldview_entity` | 5,416,521 | 47 GB | Entity relationships and worldview |
| `gbim_beliefs` | 5,289,747 | 3 GB | Core beliefs — structured columns |
| `gbim_evidence` | 2,121,230 | 680 MB | Supporting evidence |
| `gbim_belief_evidence` | 2,121,230 | 232 MB | Belief-evidence linkages |
| `mvw_gbim_landowner_spatial` ★ | **20,593** | spatially indexed | Landowner beliefs — materialized view, `LANDOWNER_CORPORATE` + `LANDOWNER_GOVERNMENT`, `worldview_id = 'eq1'` — verified March 20, 2026. **⚠️ 0 rows returned at runtime as of March 28, 2026 — rebuild pending (Item 21, known backlog, pre-existing).** |

The 5,416,521-row corpus represents the accumulated GBIM ingestion from WV GIS, SAMB, federal datasets, and facility registries. The 20,593-row landowner materialized view represents a distinct class of belief — parcel ownership — added March 20, 2026 and described fully in Sections 2.6.4, 2.10, and 2.11.

**Access pattern:**

```python
import psycopg2

# msjarvis — GBIM belief store (port 5433)
conn_msjarvis = psycopg2.connect(
    host="localhost", port=5433,
    database="msjarvis", user="postgres", password="postgres"
)

# msjarvisgis — spatial + landowner beliefs (port 5432)
conn_spatial = psycopg2.connect(
    host="localhost", port=5432,
    database="msjarvisgis", user="postgres", password="postgres"
)

# Query landowner beliefs by proposition code
cursor = conn_spatial.cursor()
cursor.execute("""
    SELECT belief_id,
           what_axis->>'proposition_code'       AS proposition_code,
           who_axis->>'canonical_entity_name'   AS entity_name,
           where_axis->>'county'                AS county,
           under_whose_authority_axis->>'basis' AS authority_basis
    FROM gbimbeliefnormalized
    WHERE (what_axis->>'proposition_code') IN
          ('LANDOWNER_CORPORATE', 'LANDOWNER_GOVERNMENT')
    AND worldview_id = 'eq1'
    LIMIT 10;
""")
```

---

## 2.6 ChromaDB Collection Inventory — ★ UPDATED March 28, 2026

The ChromaDB instance (host port 8002, container-internal port 8000) is the vector-backed semantic memory layer that makes GBIM beliefs and related documents retrievable by semantic similarity. All collections use 384-dimensional embeddings produced by `all-minilm:latest` via `jarvis-ollama:11434/api/embeddings`.

> ⚠️ **Embedding Model Lock:** All ChromaDB collections in production use `all-minilm:latest` (384-dim, cosine similarity). The `nomic-embed-text` model produces 768-dimensional vectors and is incompatible with all existing collections. Chunk size constraint confirmed: **100 words maximum per chunk** (256-token context limit on `all-minilm`), 20-word overlap. Any ingestion, retrieval, or migration script must use `all-minilm:latest`. This constraint is enforced at the service level and must not be overridden.

> **ChromaDB API note:** v2 API is active. All service calls must use `/api/v2/` endpoints. The `/api/v1/` path returns HTTP 410 Gone.

> **Embedding API note (March 26, 2026):** Both `/api/embeddings` (Ollama legacy endpoint, single-string `prompt` key) and `/api/embed` (Ollama v0.4+ endpoint, list input with `input` key) are available on `jarvis-ollama` port 11434. The production ingest pipeline uses `/api/embeddings` for compatibility across all existing scripts. Do not switch existing scripts to `/api/embed` without testing — the key name differs (`prompt` vs. `input`).

> **March 28, 2026 remediation summary:** ChromaDB full inventory mapped — **6,675,442 vectors across 40 active collections**. 7 orphaned empty collections confirmed present — no active service queries them. 19,338 duplicate vectors removed from `spiritual_rag`. `psychological_rag` restored to 968 documents via `PSY_COLLECTION=psychological_rag` env var fix.

```
┌─────────────────────────────────────────────────────────────┐
│       Ms. Jarvis ChromaDB Collection Architecture           │
│    (host port 8002 — all-minilm:latest, 384-dim, cosine)    │
│      ★ UPDATED March 28, 2026 — 6,675,442 total vectors     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  GBIM Belief Collections                                    │
│  ┌────────────────────────────────────────────────┐         │
│  │  gbim_worldview_entities — 5,416,521 entities  │         │
│  │  gbim_beliefs_v2         — active GBIM v2      │         │
│  │  GBIM_sample_rows        — 5,000 (test)        │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
│  ⚠️  LANDOWNER BELIEFS NOT IN CHROMADB                      │
│  LANDOWNER_CORPORATE and LANDOWNER_GOVERNMENT beliefs        │
│  (20,593 records, worldview eq1) are accessed exclusively   │
│  via gbim_query_router (port 7205) →                        │
│  mvw_gbim_landowner_spatial (msjarvisgis, port 5432).       │
│  PostgreSQL-native path only. No vector embeddings.         │
│  See Sections 2.10 and 2.11.                                │
│                                                              │
│  Spatial & Benefits Collections ★ UPDATED                  │
│  ┌────────────────────────────────────────────────┐         │
│  │  gis_wv_benefits — WV benefits facilities  ✅  │         │
│  │  geospatialfeatures — ★ 60,000 items ✅        │         │
│  │    (was: 0 items — OI-12 CLOSED March 26)      │         │
│  │  GBIM_Fayette_sample — ★ 1,535 items ✅        │         │
│  │    (was: 0 items — OI-13 CLOSED March 26)      │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
│  Community Memory & Learning                                │
│  ┌────────────────────────────────────────────────┐         │
│  │  autonomous_learner — 21,181+ items (growing)  │         │
│  │  ms_jarvis_memory — active                     │         │
│  │  episodic_index — active                       │         │
│  │  conversation_history — active (OI-05 open)    │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
│  Governance & Knowledge Collections ★ UPDATED              │
│  ┌────────────────────────────────────────────────┐         │
│  │  governance — WV governance texts              │         │
│  │  governance_rag — ★ 643 chunks ✅              │         │
│  │    MountainShares DAO full corpus +            │         │
│  │    US Constitution (97 chunks, Gutenberg)      │         │
│  │    Retrieval-verified March 26, 2026           │         │
│  │  commons_rag — ★ 306 chunks ✅                 │         │
│  │    Full Commons governance + gamification      │         │
│  │    Retrieval-verified March 26, 2026           │         │
│  │  thesis — theoretical framework                │         │
│  │  mountainshares_knowledge — DAO economics      │         │
│  │  msjarvis_docs — ★ 4,192 items ✅              │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
│  Specialized Corpora ★ UPDATED March 28, 2026              │
│  ┌────────────────────────────────────────────────┐         │
│  │  psychological_rag — ★ 968 items ✅            │         │
│  │    (was: 0 docs served — PSY_COLLECTION env    │         │
│  │     var fixed March 28, 2026)                  │         │
│  │  appalachian_cultural_intelligence             │         │
│  │    ★ 820 items ✅ (was: 5 items)               │         │
│  │    OI-14 CLOSED March 26, 2026                 │         │
│  │  spiritual_rag ★                               │         │
│  │    Deduplicated March 28, 2026                 │         │
│  │    19,338 duplicate vectors removed            │         │
│  │    Mother Carrie Protocol                      │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
│  AAPCAppE Corpus ★ NEW March 27, 2026                      │
│  ┌────────────────────────────────────────────────┐         │
│  │  aaacpe_corpus — 65 docs (growing) ✅          │         │
│  │    39 sources; total_runs: 1                   │         │
│  │    jarvis-aaacpe-scraper (port 8033) ACTIVE    │         │
│  │    jarvis-aaacpe-rag (port 8032) ACTIVE        │         │
│  │    RAG retrieval verified (emergency protocol  │         │
│  │    + Fayette County utility examples)          │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
│  Total: 6,675,442 vectors across 40 active collections      │
│  7 orphaned empty collections present — no active queries   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

*Figure 2.4. ChromaDB collection architecture as of March 28, 2026. ★ marks collections updated in the March 26–28, 2026 sprints. Total: 6,675,442 vectors across 40 active collections. All previously sparse or empty RAG collections are now fully populated and semantically verified. `spiritual_rag` deduplicated (−19,338 vectors). `psychological_rag` restored to 968 documents. `msjarvis_docs` expanded to 4,192 items. Landowner beliefs (`LANDOWNER_CORPORATE` / `LANDOWNER_GOVERNMENT`) remain outside ChromaDB — served via dedicated PostgreSQL-native path through `gbim_query_router` (port 7205). See Sections 2.10 and 2.11.*

### 2.6.1 GBIM Belief Collections

| Collection | Items | Description | Metadata Keys |
|---|---|---|---|
| `gbim_worldview_entities` | 5,416,521 | Complete GBIM spatial corpus — all WV geospatial features embedded from the nine-axis belief structure | `worldview_id`, `entity_id`, `dataset`, `county`, `gbim_entity`, `centroid_x`, `centroid_y` |
| `gbim_beliefs_v2` | Active | GBIM beliefs v2 — production belief collection with nine-axis embeddings | `belief_id`, `source_table`, `source_pk`, `epoch`, `county` |
| `GBIM_sample_rows` | 5,000 | Random sample for testing and validation | `belief_id`, `proposition_code` |

All GBIM belief collections: 384-dim, `all-minilm:latest`, `worldview = eq1`.

> **Landowner beliefs are not in this table.** The `LANDOWNER_CORPORATE` and `LANDOWNER_GOVERNMENT` proposition codes are stored in `mvw_gbim_landowner_spatial` in `msjarvisgis` (port 5432) and are accessed via `gbim_query_router` (port 7205) — a PostgreSQL-native SQL aggregation path, not a vector similarity path. See Sections 2.10 and 2.11.

### 2.6.2 Spatial and Benefits Collections — ★ UPDATED March 26, 2026

| Collection | Items | Description | Metadata Keys |
|---|---|---|---|
| `gis_wv_benefits` | Active | WV benefits-relevant facilities — DHHR offices, community action agencies, food banks, utility assistance sites | `facility_type`, `county`, `zip`, `local_resource_id`, `centroid_x`, `centroid_y` |
| `geospatialfeatures` ★ | **60,000** | ✅ **POPULATED March 26, 2026** — PostGIS spatial features ingested from WV geospatial layers (was: 0 items — OI-12 CLOSED) | `dataset`, `county`, `feature_type` |
| `GBIM_Fayette_sample` ★ | **1,535** | ✅ **POPULATED March 26, 2026** — Fayette County GBIM belief sample (was: 0 items — OI-13 CLOSED) | `belief_id`, `proposition_code`, `county` |

### 2.6.3 Community Memory and Learning Collections

| Collection | Items | Description | Notes |
|---|---|---|---|
| `autonomous_learner` | 21,181+ (growing ~288/day) | Autonomous research findings — MountainShares security, Appalachian development, governance, AI ethics | Queried at Phase 1.45 before every RAG call; top-5 prepended to `enhanced_message` |
| `ms_jarvis_memory` | Active | Persistent memory for cross-session continuity | — |
| `episodic_index` | Active | Episodic memory index for temporal reasoning | — |
| `conversation_history` | Active | Conversation history for context maintenance | OI-05 open — formal pipeline wiring pending |

### 2.6.4 GBIM Landowner Belief Layer — Field Note, March 20, 2026

> **Field note — March 20, 2026, evening session.** The GBIM landowner belief layer is now live in the GBIM production stack. 20,593 parcel-level `LANDOWNER_CORPORATE` and `LANDOWNER_GOVERNMENT` belief records have been inserted into `gbimbeliefnormalized` in `msjarvisgis`, clustered by canonical entity name across the full statewide WV assessor owner name corpus, and materialized in `mvw_gbim_landowner_spatial`. The `gbim_query_router` service (port 7205) is live and verified on both statewide and county-scoped natural-language ownership queries.
>
> *Verified March 20, 2026, ~19:45 EDT by Carrie Kidd (Mamma Kidd), Oak Hill WV*

> **⚠️ March 28, 2026 note:** `mvw_gbim_landowner_spatial` is returning 0 rows at runtime. The belief records are present in `gbimbeliefnormalized` (20,593 verified), but the materialized view requires a rebuild. This is Item 21 in the known backlog — pre-existing, not introduced during the March 28 remediation sprint. The `gbim_query_router` service is healthy; the view rebuild is the outstanding step.

This closes a meaningful gap in the GBIM nine-axis coverage. Prior to March 20, 2026, the `who_axis` and `under_whose_authority_axis` of GBIM were populated for facility operators, government agencies, and program administrators — but not for parcel landowners. The landowner belief layer fills that gap for the most consequential class of institutional actors in Appalachian land governance: corporate surface rights holders, coal and energy companies, timber companies, and government landholding agencies.

**The landowner belief layer is not embedded in ChromaDB.** This is a deliberate architectural decision: landowner queries ask *who owns how much land where* — a structured aggregation question with a deterministic, exact answer in the relational GBIM corpus. Embedding those records in ChromaDB and retrieving them by vector similarity would introduce approximation error into a query type that does not require it. The `gbim_query_router` route is PostgreSQL-native, exact, and auditable. See Sections 2.10 and 2.11 for full documentation of the service and materialized view.

**Landowner layer specifications:**

| Property | Value |
|---|---|
| Proposition codes | `LANDOWNER_CORPORATE`, `LANDOWNER_GOVERNMENT` |
| Belief count | **20,593 verified records** (March 20, 2026) |
| Geographic scope | Statewide West Virginia — all counties |
| Source | WV assessor parcel records (canonical entity clustering pipeline) |
| Worldview | `eq1` |
| Storage | `gbimbeliefnormalized` in `msjarvisgis` (port 5432) |
| Spatial view | `mvw_gbim_landowner_spatial` (materialized, spatially indexed — see §2.11) |
| View runtime status | **⚠️ 0 rows — rebuild pending (Item 21, backlog)** |
| Query service | `gbim_query_router` (port 7205) — **PostgreSQL-native, no ChromaDB** (see §2.10) |
| Routing schema | `mode: landowner_gbim`, `route_type: parcel_ownership` |
| Date verified | March 20, 2026 |
| Ethical constraint | **Individual residential owner names are NOT present** — institutional and government entities only (see §2.9) |

### 2.6.5 Governance and Knowledge Collections — ★ UPDATED March 26–28, 2026

| Collection | Items | Description |
|---|---|---|
| `governance` | Active | WV governance documents — legislation, policy, regulatory texts |
| `governance_rag` ★ | **643 chunks** | ✅ **POPULATED March 26, 2026** — MountainShares DAO Charter, Terms, Program Rules, Parameter Tables, Phase 0–3 docs, KPI Spec, Safety Champion, Funder Overview + US Constitution (97 chunks, Project Gutenberg pg5.txt). Semantic retrieval verified. (OI-19 CLOSED) |
| `commons_rag` ★ | **306 chunks** | ✅ **POPULATED March 26, 2026** — Full Commons governance and gamification corpus. Retrieval verified: Daily Life Game → Contribution Game + Participation Map ✅ (OI-20 CLOSED) |
| `thesis` | Active | Polymathmatic Geography theoretical framework |
| `mountainshares_knowledge` | Active | MountainShares DAO governance and economic model documentation |
| `msjarvis_docs` ★ | **4,192** | ✅ **UPDATED March 28, 2026** — expanded from 2,348 items |

### 2.6.6 Specialized Corpora — ★ UPDATED March 26–28, 2026

| Collection | Items | Port | Description |
|---|---|---|---|
| `psychological_rag` ★ | **968** | 8006 | ✅ **RESTORED March 28, 2026** — was serving 0 documents despite 968 present in ChromaDB; fixed via `PSY_COLLECTION=psychological_rag` env var |
| `appalachian_cultural_intelligence` ★ | **820** | 8000 | ✅ **POPULATED March 26, 2026** (was: 5 items — OI-14 CLOSED) |
| `spiritual_rag` ★ | Deduplicated | 8000 | ✅ **DEDUPLICATED March 28, 2026** — 19,338 duplicate vectors removed; Mother Carrie Protocol corpus clean |
| `aaacpe_corpus` ★ | **65 docs** (growing) | 8032 | ✅ **ACTIVATED March 27, 2026** — 39 sources, `total_runs: 1`; emergency protocol + Fayette County utility RAG verified |

---

## 2.7 The Relationship Between GBIM, GeoDB, RAG, and Registries

The nine-axis belief structure and the ChromaDB collection inventory are not self-contained systems — they are the representational and retrieval layers of a four-database architecture that includes:

1. **`msjarvis` / `msjarvisgis`** (PostgreSQL, ports 5433 and 5432) — the GBIM belief corpus and spatial body
2. **ChromaDB** (host port 8002) — the semantic memory layer for vector-based retrieval
3. **`jarvis-local-resources-db`** (PostgreSQL, port 5435) — the structured program and resource registry. **★ March 28, 2026: `jarvis_local_resources` schema restored — resources table confirmed present following March 28 remediation.**
4. **`gbim_query_router`** (port 7205) — the PostgreSQL-native routing service for structured GBIM belief queries, including the landowner path (see §2.10)

```
┌─────────────────────────────────────────────────────────────┐
│     GBIM Four-Database Architecture (March 28, 2026) ★      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  gbimbeliefnormalized (msjarvisgis, port 5432)              │
│    5,416,521 beliefs (nine JSONB axes, worldview eq1)       │
│    + 20,593 landowner beliefs (CORPORATE + GOVERNMENT) ★    │
│          ↓ embedding pipeline (all-minilm:latest, 384-dim)  │
│  ChromaDB (host port 8002) ★ 6,675,442 total vectors        │
│    gbim_worldview_entities — 5,416,521 vectors              │
│    gbim_beliefs_v2 — production belief embeddings           │
│    gis_wv_benefits — WV benefits facilities                 │
│    geospatialfeatures — ★ 60,000 items ✅                   │
│    GBIM_Fayette_sample — ★ 1,535 items ✅                   │
│    governance_rag — ★ 643 chunks ✅                         │
│    commons_rag — ★ 306 chunks ✅                            │
│    appalachian_cultural_intelligence — ★ 820 items ✅       │
│    spiritual_rag — ★ deduplicated (−19,338 dups) ✅         │
│    psychological_rag — ★ 968 docs restored ✅               │
│    msjarvis_docs — ★ 4,192 items ✅                         │
│    aaacpe_corpus — ★ 65 docs ✅ (March 27)                  │
│    autonomous_learner — 21,181+ community memories          │
│    [NOTE: landowner beliefs NOT in ChromaDB]                │
│          ↓ metadata links (entity_id, local_resource_id)    │
│  jarvis-local-resources-db (port 5435) ★ schema restored    │
│    Verified program records — county, ZIP, type             │
│          ↓ direct SQL (no embeddings)                       │
│  gbim_query_router (port 7205) ★                            │
│    → mvw_gbim_landowner_spatial                             │
│      (msjarvisgis, port 5432)                               │
│    20,593 landowner beliefs — ranked by area, county        │
│    proposition_code IN ('LANDOWNER_CORPORATE',              │
│                         'LANDOWNER_GOVERNMENT')             │
│    worldview_id = 'eq1'                                     │
│    ⚠️ view returning 0 rows — rebuild pending (Item 21)     │
│    PostgreSQL-native — NO ChromaDB (see §2.10, §2.11)      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

*Figure 2.5. The four-database architecture that operationalizes the GBIM belief model, updated March 28, 2026. ★ All RAG collections fully populated; 6,675,442 total vectors. `spiritual_rag` deduplicated, `psychological_rag` restored, `msjarvis_docs` expanded to 4,192. `jarvis-local-resources-db` schema restored. Landowner beliefs bypass ChromaDB and are accessed via direct SQL aggregation through `gbim_query_router` — see Sections 2.10 and 2.11. ⚠️ `mvw_gbim_landowner_spatial` view rebuild still pending (Item 21).*

The key architectural distinction is between **vector-based projection** (ChromaDB, appropriate for semantic similarity over unstructured or semi-structured belief content) and **relational projection** (SQL aggregation over `mvw_gbim_landowner_spatial`, appropriate for structured ownership queries with deterministic answers). Both are Hilbert-space projections in the conceptual model — they differ in implementation because the geometry of the relevant subspace differs.

---

## 2.8 Intellectual Honesty Correction — Judge GBIM Claims vs. Actual Implementation (March 21, 2026)

> This section was added March 21, 2026 to correct a materially misleading claim that has appeared in multiple earlier chapters of this thesis and in the system's own judge service documentation.

### 2.8.1 The Claim Being Corrected

Chapters 17, 33, and associated judge pipeline documentation describe the truth and alignment judges as validating AI responses against "PostgreSQL GBIM (5,416,521 entities)." The architecture diagrams in those chapters show `judge-truth` making lookups into `msjarvis` (port 5433) and `judge-alignment` cross-referencing claims against the GBIM belief corpus as part of their scoring logic.

This description represents the **design intent** of the judge pipeline — what GBIM-grounded judge validation is meant to become. It does not describe what those judges currently do.

### 2.8.2 What the Judges Actually Do (March 21, 2026)

The actual implementations of `judge_truth_filter.py` and `judge_alignment_filter.py`, as confirmed by source file inspection on March 21, 2026, use a heuristic pattern-matching approach internally labeled `heuristic_contradiction_v1`. There are no live PostgreSQL queries to `msjarvis` or `msjarvisgis` in either file. The truth and alignment judges score responses based on:

- Contradiction detection heuristics — keyword and phrase patterns that flag likely factual inconsistencies, logical contradictions, or hedging language
- Identity adherence pattern matching — regular-expression and string-matching rules that check whether the response text stays within the expected Ms. Egeria Jarvis persona framing
- Hardcoded scoring thresholds — score values that reflect the designer's prior about typical response quality, not a computed comparison against a ground truth corpus

The ethics and consistency judges (`judge_ethics_filter.py`, `judge_consistency_engine.py`) similarly use heuristic pattern matching — harm keyword detection, coherence heuristics, and structural consistency checks — not GBIM queries.

### 2.8.3 The Gap in Plain Language

| | Design Intent | Actual Implementation (March 21, 2026) |
|---|---|---|
| Truth judge | Queries `msjarvis` GBIM beliefs; checks factual claims against 5,416,521 verified entities | Runs `heuristic_contradiction_v1` — pattern-matching on response text; no DB query |
| Alignment judge | Validates response against GBIM worldview constraints; checks community-value alignment against `eq1` belief set | Pattern-matches against identity adherence rules and hardcoded persona constraints |
| Ethics judge | Cross-references against ethical constraints grounded in GBIM `why_axis` and `for_whom_axis` | Harm keyword screening; heuristic harm scoring |
| Consistency judge | Checks cross-session behavioral consistency against stored belief state | Structural coherence heuristics within a single response window |
| Scores | GBIM-grounded confidence measures | Heuristic pattern-match outputs presented as scores |

### 2.8.4 Why This Matters

1. **External stakeholders.** Regional Development Authorities, state agencies, and community partners evaluating Ms. Jarvis as a potential infrastructure partner need to understand what the judge pipeline actually validates. Telling them that AI outputs are "validated against 5.4 million PostgreSQL GBIM entities" when the judges run heuristics is a misrepresentation of the system's current capability — regardless of intent.

2. **Thesis integrity.** This thesis makes claims about constitutional AI enforcement grounded in GBIM. Those claims must accurately distinguish between architectural design and operational reality.

3. **Trust as infrastructure.** Ms. Jarvis is being built to serve communities who have been historically subjected to systems that overstated their capabilities or accountability. If the system's own audit documentation misrepresents what the judges do, the accountability infrastructure is undermined at its foundation.

### 2.8.5 The Intended Architecture (Design Target)

```python
# judge_truth_filter.py (target implementation)
# ├── Receives: consensus answer + question context
# ├── Extracts: factual claims, named entities, locations
# ├── Queries: msjarvis (port 5433) for matching GBIM beliefs
# │   └── SELECT belief_id, what_axis, confidence_decay
# │       FROM gbimbeliefnormalized
# │       WHERE <entity or claim matches>
# │       AND worldview_id = 'eq1'
# ├── Computes: factual consistency score vs. retrieved beliefs
# ├── Flags: claims that contradict or are unsupported by GBIM
# └── Returns: truth_score with provenance

# judge_alignment_filter.py (target implementation)
# ├── Receives: consensus answer + question context
# ├── Queries: msjarvis for relevant community-value beliefs
# │   └── Filter on why_axis, for_whom_axis,
# │       under_whose_authority_axis
# ├── Checks: response alignment vs. GBIM worldview constraints
# └── Returns: alignment_score with GBIM belief citations
```

### 2.8.6 Path to Closing the Gap

1. Add PostgreSQL connection pool to `Dockerfile.judge` — `psycopg2` or `asyncpg` must be available in the judge image.
2. Implement GBIM query functions in `judge_truth_filter.py` — entity extraction from response text, belief lookup against `gbimbeliefnormalized`, contradiction scoring.
3. Implement GBIM worldview filter in `judge_alignment_filter.py` — query the `eq1` worldview for normative and community-value beliefs, compute alignment score.
4. Update `UltimateResponse` schema — add `gbim_beliefs_consulted: int` and `gbim_contradictions_detected: int` fields.
5. Update Chapters 17, 33, and all judge pipeline documentation to reflect the current heuristic implementation until the GBIM-grounded implementation is deployed.

Until these steps are complete, the correct accurate description of the truth and alignment judges is: **heuristic pattern-matching filters that approximate constitutional validation but do not consult the GBIM corpus.**

### 2.8.7 What Is Not Affected by This Correction

The following are unaffected by this correction and remain accurate as documented:

- The GBIM corpus itself — **5,416,521 beliefs** including **20,593 landowner beliefs** (`eq1` worldview) — is real, verified, and production-operational.
- The `gbim_query_router` (port 7205) **does** make live PostgreSQL queries against `mvw_gbim_landowner_spatial` — landowner routing is accurate as documented in Sections 2.10 and 2.11 (pending view rebuild, Item 21).
- The `jarvis-spiritual-rag` and `jarvis-gis-rag` services do query GBIM-derived ChromaDB collections as part of Phase 1 context assembly — RAG grounding is operational.
- **All ChromaDB RAG collections are fully populated and semantically verified** as of March 26–28, 2026. Total: 6,675,442 vectors across 40 active collections.
- The BBB gate's constitutional filters are active and enforced.
- The nine-axis schema, Hilbert-space model, and worldview architecture described in this chapter accurately represent the intended operational architecture.
- **March 28, 2026:** All 5 tracked security/audit items closed — CRIT-CRYPTO, REM-06 (false positive confirmed), REM-09 (full route inventory documented), REM-13, REM-16. `_auth()` present and correctly called on all 4 sensitive routes in `ms_jarvis_memory.py`. Both `0.0.0.0` port exposures corrected to `127.0.0.1`.

---

## 2.9 Ethical Architecture of the Belief Corpus

The nine-axis structure is not value-neutral. Every axis encodes a design decision about what matters, who is accountable, and what the system should be able to know. Two design decisions are treated as foundational constraints enforced at the schema level:

**Constraint 1: Individual residential owner names are excluded from the GBIM belief corpus.**

The `who_axis` of the landowner belief layer contains only institutional and corporate entity names. Individual residential owner names from WV assessor records are not ingested into any GBIM belief table, materialized view, ChromaDB collection, or RAG-accessible store. The ingestion pipeline selects only records matching corporate and government entity patterns, and `gbim_query_router` queries only `proposition_code IN ('LANDOWNER_CORPORATE', 'LANDOWNER_GOVERNMENT')`.

The rationale is the **aggregation problem**: individual owner names are legally public as friction-protected courthouse records. Embedding them into a semantically searchable, spatially indexed, multi-million-parcel AI system would convert friction-protected public records into operational surveillance infrastructure — not justified by Ms. Jarvis's purpose of routing households to assistance.

**Constraint 2: Institutional actors are represented with full accountability metadata.**

The `under_whose_authority_axis` and `on_what_evidence_axis` for institutional beliefs — including all landowner beliefs — must include sufficient provenance to allow any displayed belief to be traced back to its source record. Corporate and government landholders are named, counted, and area-summarized with full assessor provenance, precisely because accountability for institutions with power over place is the counterpart to privacy protection for individuals.

These two constraints define the ethical architecture of the GBIM belief corpus: **a system that makes power legible without making vulnerability exploitable.**

---

## 2.10 The `gbim_query_router` Service — ★ Production, March 20, 2026

> **Field note — March 20, 2026.** `gbim_query_router` (port 7205) promoted to production. This service is the primary GBIM retrieval path for all structured landowner belief queries. It is architecturally distinct from every other retrieval service in the Ms. Jarvis stack in one critical way: **it does not touch ChromaDB.** It routes directly to `mvw_gbim_landowner_spatial` in `msjarvisgis` (port 5432) via PostgreSQL SQL aggregation.
>
> *Verified March 20, 2026, ~19:45 EDT — Carrie Kidd (Mamma Kidd), Oak Hill WV*

> **⚠️ March 28, 2026:** `gbim_query_router` service is healthy. `mvw_gbim_landowner_spatial` is returning 0 rows — materialized view rebuild is pending (Item 21, backlog). All other `gbim_query_router` infrastructure is operational.

### 2.10.1 Architectural Role

`gbim_query_router` occupies the fourth leg of the GBIM four-database architecture (Figure 2.5). It is the exclusive query surface for `LANDOWNER_CORPORATE` and `LANDOWNER_GOVERNMENT` proposition codes. No other service in the Ms. Jarvis stack provides access to these records.

The reason this service exists as a separate FastAPI container rather than as a query path inside the main RAG pipeline is that ownership aggregation queries have a fundamentally different information-theoretic structure from the semantic similarity queries served by ChromaDB:

- **ChromaDB queries** find records that are *similar* to a query embedding — approximate nearest-neighbor in 384-dimensional vector space.
- **Landowner queries** find records that *match* a specific ownership relationship — exact SQL aggregation over verified parcel-level data.

Combining these paths would either force ownership queries through unnecessary approximate-search machinery or require landowner records to be embedded and stored in ChromaDB — both architecturally unsound.

### 2.10.2 Service Specification

| Property | Value |
|---|---|
| Container name | `jarvis-gbim-query-router` |
| Host port | **7205** |
| Framework | FastAPI |
| Endpoint | `POST /query` |
| Database target | `mvw_gbim_landowner_spatial` in `msjarvisgis` (host port 5432) |
| ChromaDB dependency | **None** |
| Production status | ✅ **Live — March 20, 2026** |
| Namespace | `msjarvis-rebuild` |

### 2.10.3 Routing Schema

```python
# gbim_query_router routing schema — verified March 20, 2026
LANDOWNER_ROUTE = {
    "mode": "landowner_gbim",
    "route_type": "parcel_ownership",
    "target_view": "mvw_gbim_landowner_spatial",
    "database": "msjarvisgis",
    "port": 5432,
    "proposition_codes": ["LANDOWNER_CORPORATE", "LANDOWNER_GOVERNMENT"],
    "worldview": "eq1",
    "chromadb_bypass": True   # explicit — no vector path
}
```

### 2.10.4 Verified Query Patterns

Both patterns confirmed March 20, 2026:

```python
import httpx

# Pattern 1 — Statewide top landowners
statewide = httpx.post(
    "http://127.0.0.1:7205/query",
    json={
        "question": "Who are the largest landowners in West Virginia?",
        "mode": "landowner_gbim",
        "route_type": "parcel_ownership",
        "scope": "statewide",
        "limit": 20
    }
)

# Pattern 2 — County-scoped landowners
county = httpx.post(
    "http://127.0.0.1:7205/query",
    json={
        "question": "Who owns the most land in Fayette County?",
        "mode": "landowner_gbim",
        "route_type": "parcel_ownership",
        "county": "Fayette",
        "limit": 20
    }
)
```

### 2.10.5 Relationship to GBIM Principles

`gbim_query_router` is the operational realization of **P3 – Power has a geometry** and **P16 – Power accountable to place**. It is the first service in the Ms. Jarvis stack whose exclusive purpose is making institutional power over land legible and queryable by natural language at parcel scale. The 20,593 landowner beliefs it serves represent the most direct accountability infrastructure in the current production system — a corpus that can answer *who owns how much land, where, under what basis of authority* for every major corporate and government landowner in West Virginia.

---

## 2.11 The `mvw_gbim_landowner_spatial` Materialized View

The `mvw_gbim_landowner_spatial` materialized view is the direct query target for all `gbim_query_router` landowner requests. It is a spatially indexed, PostgreSQL-native view over `gbimbeliefnormalized` filtered to the two landowner proposition codes.

### 2.11.1 View Specification

| Property | Value |
|---|---|
| View name | `mvw_gbim_landowner_spatial` |
| View type | Materialized view (PostgreSQL) |
| Database | `msjarvisgis` (host port 5432) |
| Row count | **20,593 verified records** (March 20, 2026) |
| Runtime status | **⚠️ 0 rows returned — rebuild pending (Item 21, backlog, March 28, 2026)** |
| Proposition codes | `LANDOWNER_CORPORATE`, `LANDOWNER_GOVERNMENT` |
| Worldview | `eq1` |
| Spatial index | ✅ Yes — geometry column spatially indexed (GIST) |
| Source table | `gbimbeliefnormalized` |
| Geometry source | `wv_parcels` geometry joined via parcel ID |
| Production status | ✅ **Live — March 20, 2026** (view rebuild required to restore row count) |

### 2.11.2 Logical Schema

```sql
-- mvw_gbim_landowner_spatial — logical schema
-- Materialized view in msjarvisgis (port 5432)
-- Verified production: 20,593 rows, worldview eq1
-- ⚠️ March 28, 2026: view returning 0 rows — refresh required (Item 21)

CREATE MATERIALIZED VIEW mvw_gbim_landowner_spatial AS
SELECT
    b.belief_id,
    b.worldview_id,                                          -- 'eq1'
    b.what_axis->>'proposition_code'        AS proposition_code,
    -- LANDOWNER_CORPORATE or LANDOWNER_GOVERNMENT

    b.who_axis->>'canonical_entity_name'    AS canonical_entity_name,
    -- Normalized corporate/government entity name
    -- Individual residential names are EXCLUDED

    b.who_axis->>'raw_name_variants'        AS raw_name_variants,
    -- JSONB array of assessor string variants for this entity

    b.where_axis->>'county'                 AS county,
    b.where_axis->>'parcel_id'              AS parcel_id,
    ST_Centroid(p.geom)                     AS centroid_geom,
    -- Spatial geometry — parcel centroid (GIST indexed)

    b.under_whose_authority_axis->>'basis'  AS authority_basis,
    -- 'wv_assessor_record' | 'deed_reference' | 'government_registry'

    b.on_what_evidence_axis->>'source_table'    AS source_table,
    b.on_what_evidence_axis->>'source_pk'       AS source_pk,
    b.on_what_evidence_axis->>'data_vintage'    AS data_vintage,

    b.when_axis->>'verified_date'           AS verified_date,
    b.confidence_decay

FROM gbimbeliefnormalized b
JOIN wv_parcels p ON p.parcel_id = (b.where_axis->>'parcel_id')
WHERE
    (b.what_axis->>'proposition_code')
        IN ('LANDOWNER_CORPORATE', 'LANDOWNER_GOVERNMENT')
    AND b.worldview_id = 'eq1';

-- Spatial index on centroid geometry
CREATE INDEX idx_mvw_landowner_geom
    ON mvw_gbim_landowner_spatial USING GIST (centroid_geom);

-- Index on county for county-scoped queries
CREATE INDEX idx_mvw_landowner_county
    ON mvw_gbim_landowner_spatial (county);

-- Index on canonical_entity_name for entity lookups
CREATE INDEX idx_mvw_landowner_entity
    ON mvw_gbim_landowner_spatial (canonical_entity_name);
```

### 2.11.3 GBIM Axis Coverage in the View

| GBIM Axis | View Column | Content |
|---|---|---|
| `what_axis` | `proposition_code` | `LANDOWNER_CORPORATE` or `LANDOWNER_GOVERNMENT` |
| `who_axis` | `canonical_entity_name`, `raw_name_variants` | Normalized entity name; original assessor string variants |
| `where_axis` | `county`, `parcel_id`, `centroid_geom` | County; parcel ID; spatially indexed centroid geometry |
| `when_axis` | `verified_date`, `confidence_decay` | March 20, 2026; decay schedule |
| `why_axis` | *(not surfaced in view — queryable in base table)* | Institutional land accountability |
| `how_axis` | *(not surfaced in view)* | Canonical clustering pipeline |
| `for_whom_axis` | *(not surfaced in view)* | WV communities, researchers, accountability users |
| `under_whose_authority_axis` | `authority_basis` | Assessor record / deed reference / government registry |
| `on_what_evidence_axis` | `source_table`, `source_pk`, `data_vintage` | Full provenance chain to source record |

### 2.11.4 Typical Query Pattern (Internal — `gbim_query_router`)

```sql
-- Statewide top landowners by total parcel area
SELECT
    canonical_entity_name,
    proposition_code,
    COUNT(*)            AS parcel_count,
    SUM(p.calc_acres)   AS total_acres
FROM mvw_gbim_landowner_spatial m
JOIN wv_parcels p ON p.parcel_id = m.parcel_id
WHERE worldview_id = 'eq1'
GROUP BY canonical_entity_name, proposition_code
ORDER BY total_acres DESC
LIMIT 20;

-- County-scoped top landowners
SELECT
    canonical_entity_name,
    proposition_code,
    COUNT(*)            AS parcel_count,
    SUM(p.calc_acres)   AS total_acres
FROM mvw_gbim_landowner_spatial m
JOIN wv_parcels p ON p.parcel_id = m.parcel_id
WHERE worldview_id = 'eq1'
  AND county = 'Fayette'
GROUP BY canonical_entity_name, proposition_code
ORDER BY total_acres DESC
LIMIT 20;
```

### 2.11.5 Refresh and Maintenance

The materialized view must be refreshed when the underlying `gbimbeliefnormalized` landowner records are updated (new assessor vintage, canonical entity re-clustering, correction of a specific record):

```sql
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_gbim_landowner_spatial;
```

The `CONCURRENTLY` option allows refresh without locking the view for reads — required for production refresh without service interruption. A `UNIQUE INDEX` must exist on the view for concurrent refresh; if not present, use the blocking form and schedule during a low-traffic window:

```sql
REFRESH MATERIALIZED VIEW mvw_gbim_landowner_spatial;
```

> **⚠️ March 28, 2026 — Item 21 (open backlog):** The materialized view is currently returning 0 rows. This is a pre-existing condition that predates the March 28 remediation sprint. The belief records are present in `gbimbeliefnormalized` (20,593 verified). The required remediation step is:
>
> ```sql
> REFRESH MATERIALIZED VIEW mvw_gbim_landowner_spatial;
> -- or CONCURRENTLY if unique index is in place
> ```
>
> This is script infrastructure work, not a runtime failure of the GBIM belief corpus itself. The `gbim_query_router` service (port 7205) is healthy and will return correct results once the view is rebuilt.

---

## 2.12 Production Status Summary — March 28, 2026

| Component | Status | Notes |
|---|---|---|
| `gbimbeliefnormalized` | ✅ **5,416,521 rows** | `msjarvisgis` port 5432 — verified March 20, 2026 |
| Landowner beliefs | ✅ **20,593 records** | `LANDOWNER_CORPORATE` + `LANDOWNER_GOVERNMENT`, worldview `eq1` |
| `mvw_gbim_landowner_spatial` | ⚠️ **0 rows at runtime** | View rebuild pending — Item 21, backlog |
| `msjarvis` port 5433 | ✅ **Operational** | Restored March 28, 2026 remediation sprint |
| `jarvis_local_resources` schema | ✅ **Restored** | Resources table confirmed present — March 28, 2026 |
| ChromaDB total vectors | ✅ **6,675,442 across 40 collections** | Post-deduplication audit March 28, 2026 |
| `gbim_worldview_entities` | ✅ **5,416,521** | All-minilm 384-dim, cosine |
| `geospatialfeatures` | ✅ **60,000** | OI-12 closed March 26, 2026 |
| `GBIM_Fayette_sample` | ✅ **1,535** | OI-13 closed March 26, 2026 |
| `governance_rag` | ✅ **643 chunks** | US Constitution + full MountainShares corpus |
| `commons_rag` | ✅ **306 chunks** | Full Commons gamification corpus |
| `msjarvis_docs` | ✅ **4,192 items** | Expanded from 2,348 — March 28, 2026 |
| `psychological_rag` | ✅ **968 documents** | Restored via `PSY_COLLECTION` env var fix — March 28, 2026 |
| `appalachian_cultural_intelligence` | ✅ **820 items** | OI-14 closed March 26, 2026 |
| `spiritual_rag` | ✅ **Deduplicated** | 19,338 duplicate vectors removed — March 28, 2026 |
| `aaacpe_corpus` | ✅ **65 docs (growing)** | Activated March 27, 2026; 39 sources |
| `autonomous_learner` | ✅ **21,181+ items** | ~288/day growth rate |
| `gbim_query_router` port 7205 | ✅ **Healthy** | Service live; awaiting view rebuild for full landowner queries |
| Judge GBIM grounding | ⚠️ **Heuristic only** | Design target: live GBIM queries — see §2.8 |
| `VERIFYANDTEST.sh` line 190 | ⚠️ **Syntax error** | Script infrastructure — pre-existing open item |
| 7 empty orphaned collections | ⚠️ **Present** | No active service queries them; cleanup optional |

---

*Chapter 2 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Jarvis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: March 28, 2026 — 6,675,442 ChromaDB vectors across 40 collections, 5,416,521 GBIM beliefs, all critical security findings resolved.*
