# 2. The Geometric Belief Model and GBIM Architecture

Carrie Kidd (Mamma Kidd) — Mount Hope, WV

## Why This Matters for Polymathmatic Geography

This chapter provides the theoretical foundation for understanding how Ms. Jarvis represents knowledge, belief, and uncertainty — and why those representations are structured the way they are. It supports:

- **P1 – Every where is entangled** by establishing that belief is not stored as isolated facts but as multi-axis geometric structures in which spatial, temporal, institutional, and normative dimensions are co-present and mutually constraining — so that a single GBIM belief about a hospital in Fayette County is simultaneously a claim about what exists, where it is, when it was verified, who has authority over it, and what its implications are for program routing.

- **P3 – Power has a geometry** by showing that the GBIM axis structure — particularly `who`, `where`, `under_whose_authority`, and `for_whom` — is designed to make institutional power over place explicit and queryable, not buried in unstructured text. The landowner belief layer (Section 2.6.4, field note March 20, 2026) is the direct realization of this principle at parcel scale.

- **P5 – Design is a geographic act** by treating the nine-axis GBIM schema, the worldview structure, the collection inventory, and the ChromaDB configuration not as neutral technical choices but as geographic and political decisions that determine which facts are computable, which relationships are traversable, and which forms of institutional accountability are operationally enforceable.

- **P12 – Intelligence with a ZIP code** by grounding the Hilbert-space model in a concrete PostgreSQL corpus — `msjarvis` (port 5433), `msjarvisgis` (port 5432), and their ChromaDB mirrors — so that the abstract framework of quantum-geometric belief representation is always already indexed to real West Virginia places, programs, and populations.

- **P16 – Power accountable to place** by designing the belief structure so that institutional actors — government agencies, corporate landowners, utility companies — are represented as first-class GBIM entities with explicit `under_whose_authority` and `who` axis entries, making them queryable and auditable in a way that individual residential actors deliberately are not.

The theoretical framework in this chapter is not a preamble to the system — it is the system's operating logic, expressed at the level of schema, routing, and collection design rather than at the level of code.

Accordingly, this chapter belongs to the **Theoretical Foundation** tier: it establishes the geometric belief model, the nine-axis GBIM schema, the Hilbert-space representation of uncertainty, the worldview structure, and the ChromaDB collection inventory that together constitute the epistemic architecture of Ms. Egeria Jarvis.

---

## 2.1 Purpose and Scope

This chapter establishes the theoretical framework underlying the GeoBelief Information Model (GBIM) — the core representational system that allows Ms. Egeria Jarvis to hold, update, route, and reason over structured beliefs about West Virginia's physical world, institutional landscape, and programmatic infrastructure.

GBIM is not a database schema in the conventional sense. It is a multi-axis geometric representation of belief that treats each claim about the world as a structured object with nine dimensions, each encoding a distinct aspect of the claim's meaning, provenance, authority, and applicability. This nine-axis structure is what allows beliefs derived from a WV assessor parcel record, a federal hazard dataset, a community organization's program flyer, and a peer-reviewed paper on Appalachian poverty to coexist in a single corpus and be meaningfully compared, combined, and routed.

The chapter is organized as follows:

- Section 2.2 introduces the nine-axis belief schema and explains the role of each axis.
- Section 2.3 presents the Hilbert-space model of belief and uncertainty that motivates the GBIM design.
- Section 2.4 describes the worldview structure (`eq1` and related worldviews) and its role in routing and filtering.
- Section 2.5 describes the PostgreSQL GBIM corpus — its current scale, table structure, and production status as of March 2026.
- Section 2.6 presents the ChromaDB collection inventory — the vector-backed memory layer that makes GBIM beliefs semantically retrievable — updated through March 20, 2026.
- Section 2.7 addresses the relationship between GBIM, the GeoDB spatial body (Chapter 6), the RAG pipeline (Chapter 7), and the local resource registry.
- **Section 2.8 is an intellectual honesty correction (March 21, 2026):** it documents the gap between GBIM's designed role as the ground truth for judge verification and the current actual implementation of the truth and alignment judges, which use heuristic pattern-matching, not live PostgreSQL queries.

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

> Figure 2.1. The nine-axis GBIM belief structure. Every belief in the corpus — from a hospital location to a coal company land holding — is represented with all nine axes, enabling multi-dimensional filtering, routing, and reasoning.

**`what_axis`** — The propositional content of the belief: what entity exists, what relationship holds, what condition obtains. Structured as a typed JSONB object with fields including `type`, `label`, `description`, and `proposition_code`. The `proposition_code` is the primary routing key: it determines how the belief is indexed, which RAG paths it is eligible for, and which ethical constraints apply to its retrieval and display.

**`who_axis`** — The subject or actor of the belief: a named entity, institution, or class. For infrastructure and facility beliefs, this is typically the operating institution (a hospital system, a county agency, a federal bureau). For the landowner belief layer (Section 2.6.4), this is the canonical corporate or government entity name derived from WV assessor records. Individual residential owner names are explicitly excluded from this axis — see Section 2.9.

**`where_axis`** — The spatial grounding of the belief: geometry (point, line, polygon), coordinate system, county, ZIP code, and any relevant spatial relationships. For parcel-level beliefs, this includes the parcel centroid and county. For the landowner belief layer, this is populated from `wv_parcels` geometry joined in `mvw_gbim_landowner_spatial`.

**`when_axis`** — The temporal scope: when the belief was created, when it was last verified, its expected expiration or decay schedule. Paired with `confidence_decay` to implement time-sensitive freshness signaling in RAG retrieval.

**`why_axis`** — The normative or causal rationale: why this belief is relevant to Ms. Jarvis's mission, what programmatic or justice-oriented consequence follows from it. This axis is what connects a belief about an abandoned mine land site to a belief about a household's heating costs — the `why` axis encodes the causal and programmatic link.

**`how_axis`** — The verification method: how the belief was established, what pipeline generated it, what spatial or statistical operation produced it. For assessor-derived beliefs, this records the county assessor data vintage and the canonical clustering pipeline used to normalize owner names.

**`for_whom_axis`** — The intended beneficiary population: which households, communities, or demographic groups the belief is most relevant to. This axis supports population-targeted routing — surfacing AML-related weatherization programs preferentially to households in subsidence-risk zones.

**`under_whose_authority_axis`** — The institutional authority under which the belief's claim holds: a regulatory agency, a legislative mandate, a contractual right, or a property ownership basis. For the landowner belief layer, this records the ownership basis — assessor record, deed reference where available. This axis is central to P16 – Power accountable to place: the system can answer not just "who is here" but "under whose authority do they operate here."

**`on_what_evidence_axis`** — The primary source and provenance chain: dataset name, table, primary key, data vintage, and any raw string variants (for example, the multiple assessor name variants for a single canonical corporate entity). This axis supports full provenance tracing from a displayed belief back to its source record.

---

## 2.3 Hilbert-Space Representation of Belief and Uncertainty

The GBIM nine-axis schema is motivated by a geometric model of belief and uncertainty that treats the system's overall epistemic state as a vector in a high-dimensional Hilbert space.

In this model:

- Each **basis dimension** corresponds to a distinguishable claim about the world — a specific proposition about a specific entity at a specific place and time, under a specific institutional authority.
- The **system's belief state** is a superposition over these basis dimensions: a probability amplitude distribution that reflects confidence, uncertainty, and the degree to which different claims are mutually consistent or entangled.
- A **retrieval operation** (a RAG query, a spatial filter, a landowner lookup) is a projection of this state onto a lower-dimensional subspace — the subspace of beliefs most relevant to the query, given the current role, geography, and worldview.
- **Belief update** — ingesting new data, verifying a claim, correcting an error — is a rotation or scaling operation on the state vector that adjusts the amplitude distribution without discarding the prior structure.

```
┌─────────────────────────────────────────────────────────────┐
│         Hilbert Space Belief Model — Conceptual View        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Full Hilbert Space H                                       │
│  (all possible beliefs about WV at all scales)              │
│      |                                                       │
│      | projection                                           │
│      ↓                                                       │
│  Subspace H_q  (beliefs relevant to query q)               │
│      |                                                       │
│      | further projection                                   │
│      ↓                                                       │
│  Subspace H_q,r  (beliefs relevant to query q, role r,     │
│                    county c, worldview w)                    │
│      |                                                       │
│      | retrieval                                             │
│      ↓                                                       │
│  Top-k belief records (ChromaDB) or                         │
│  Top-n ownership records (mvw_gbim_landowner_spatial)       │
│                                                              │
│  Note: Landowner projections use relational aggregation     │
│  rather than vector geometry — exact SQL over verified      │
│  records, not approximate nearest-neighbor in embedding     │
│  space. This is a deliberate architectural choice: the      │
│  question "who owns how much land where" has a              │
│  deterministic answer in the GBIM corpus.                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 2.2. Conceptual view of the Hilbert-space projection model underlying GBIM retrieval. Vector-based projections (ChromaDB) and relational projections (SQL aggregation over `mvw_gbim_landowner_spatial`) are both understood as projections into relevant subspaces — they differ in their geometric mechanism, not in their epistemic role.

This framework is not merely metaphorical. It motivates concrete architectural decisions:

- The nine axes are the dimensions along which beliefs are structured because those are the dimensions along which meaningful distinctions arise for routing, filtering, and reasoning in a place-based justice system.
- ChromaDB stores embeddings of the nine-axis text representations because the vector space of those embeddings approximates the geometry of semantic similarity in the relevant Hilbert subspace.
- The `gbim_query_router` bypasses ChromaDB for landowner queries because ownership aggregation questions have exact, deterministic answers in the relational GBIM corpus — approximate vector search would introduce unnecessary error into a question that is fully answerable by SQL.
- The worldview structure (`eq1`) is the mechanism for maintaining multiple, potentially inconsistent belief states simultaneously — different "cuts" through the Hilbert space that correspond to different institutional perspectives, data vintages, or normative frameworks.

---

## 2.4 Worldview Structure and the `eq1` Worldview

The GBIM worldview structure allows the corpus to maintain multiple, simultaneously queryable perspectives on the same entities and places. Each belief is tagged with a `worldview_id` that identifies the interpretive frame within which it is valid.

The production worldview as of March 2026 is **`eq1`** — the primary equity-oriented worldview that grounds Ms. Jarvis's reasoning in Appalachian community perspectives, WV state data, and federal program structures as they operate in West Virginia. All 5.4M+ production beliefs in `gbimbeliefnormalized` and all 20,593 landowner beliefs in `mvw_gbim_landowner_spatial` are tagged `worldview_id = 'eq1'`.

```
┌─────────────────────────────────────────────────────────────┐
│              Worldview Structure in GBIM                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  worldview_id = 'eq1'  (production worldview)              │
│  ─────────────────────────────────────────────────────     │
│  Interpretive frame: Appalachian equity orientation         │
│  Data scope: WV state + federal sources verified for WV    │
│  Population: WV households, communities, programs          │
│  Belief count: 5,416,522 (gbimbeliefnormalized)            │
│               + 20,593 landowner beliefs                    │
│                 (mvw_gbim_landowner_spatial)                │
│  Status: Production — all RAG, GIS, landowner paths        │
│                                                              │
│  Future worldviews (planned):                               │
│  ─────────────────────────────────────────────────────     │
│  eq2: Regional Appalachian scope (multi-state)             │
│  eq3: Federal program perspective                           │
│  research1: Academic/research frame                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 2.3. The GBIM worldview structure. The production `eq1` worldview encompasses all current GBIM beliefs and landowner records. Future worldviews will allow multi-perspective reasoning without disrupting production beliefs.

Worldview tags serve two functions. First, they enable **multi-perspective retrieval**: a researcher asking about federal land management and a community member asking about program eligibility can receive responses filtered to their respective worldview contexts, even if the underlying belief records overlap. Second, they provide **update isolation**: a new batch of beliefs ingested from a different data vintage can be tagged to a new or draft worldview and validated before being promoted to the production `eq1` worldview.

---

## 2.5 The PostgreSQL GBIM Corpus

The production GBIM corpus lives in two PostgreSQL instances:

**`msjarvis` database (port 5433)** — The primary GBIM belief store, accessed by the RAG pipeline and LLM ensemble for belief retrieval, entity lookup, and provenance tracing.

**`msjarvisgis` database (port 5432)** — The spatial production database housing `gbimbeliefnormalized` (5.4M+ rows), spatial source tables, and the landowner materialized view `mvw_gbim_landowner_spatial`. This is the authoritative store for all parcel-level and spatial beliefs.

**Verified corpus scale (March 2026):**

| Table | Rows | Size | Role |
|---|---|---|---|
| `gbimbeliefnormalized` | 5,416,522 | 21 GB | Main belief table — nine JSONB axes |
| `gbim_worldview_entity` | 5,416,521 | 47 GB | Entity relationships and worldview |
| `gbim_beliefs` | 5,289,747 | 3 GB | Core beliefs — structured columns |
| `gbim_evidence` | 2,121,230 | 680 MB | Supporting evidence |
| `gbim_belief_evidence` | 2,121,230 | 232 MB | Belief-evidence linkages |
| `mvw_gbim_landowner_spatial` | 20,593 | — | Landowner beliefs — materialized, spatial (March 20, 2026) |

The 5.4M+ row corpus represents the accumulated GBIM ingestion from WV GIS, SAMB, federal datasets, and facility registries. The 20,593-row landowner materialized view represents a new class of belief — parcel ownership — added March 20, 2026, described fully in Section 2.6.4 and Chapter 6 Section 6.4.3.

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

# Query the nine-axis belief structure
cursor = conn_msjarvis.cursor()
cursor.execute("""
    SELECT belief_id,
           what_axis->>'proposition_code'       AS proposition_code,
           who_axis->>'canonical_entity_name'   AS entity_name,
           where_axis->>'county'                AS county,
           under_whose_authority_axis->>'basis' AS authority_basis
    FROM gbimbeliefnormalized
    WHERE (what_axis->>'proposition_code') IN
          ('LANDOWNER_CORPORATE', 'LANDOWNER_GOVERNMENT')
    LIMIT 10;
""")
```

---

## 2.6 ChromaDB Collection Inventory

The ChromaDB instance (port 8000) is the vector-backed semantic memory layer that makes GBIM beliefs and related documents retrievable by semantic similarity. All collections use **384-dimensional embeddings** produced by **`all-minilm:latest`** via `jarvis-ollama:11434/api/embeddings`.

> ⚠️ **Embedding Model Lock:** All ChromaDB collections in production use `all-minilm:latest` (384-dim). The `nomic-embed-text` model produces 768-dimensional vectors and is **incompatible** with all existing collections. Any ingestion, retrieval, or migration script must use `all-minilm:latest`. This constraint is enforced at the service level and must not be overridden.

```
┌─────────────────────────────────────────────────────────────┐
│       Ms. Jarvis ChromaDB Collection Architecture           │
│                (port 8000 — all-minilm:latest, 384-dim)     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  GBIM Belief Collections                                    │
│  ┌────────────────────────────────────────────────┐         │
│  │  gbim_worldview_entities — 5,416,521 entities  │         │
│  │  gbim_beliefs_v2         — active GBIM v2      │         │
│  │  GBIM_sample_rows        — 5,000 (test)        │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
│  NOTE: Landowner beliefs (LANDOWNER_CORPORATE /             │
│  LANDOWNER_GOVERNMENT) are NOT embedded in ChromaDB.        │
│  They are accessed via gbim_query_router (port 7205)        │
│  → mvw_gbim_landowner_spatial (msjarvisgis, port 5432).     │
│  PostgreSQL-native path only. See Section 2.6.4.            │
│                                                              │
│  Spatial & Benefits Collections                             │
│  ┌────────────────────────────────────────────────┐         │
│  │  gis_wv_benefits — WV benefits facilities      │         │
│  │  geospatialfeatures — scaffolded (0 items)     │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
│  Community Memory & Learning                                │
│  ┌────────────────────────────────────────────────┐         │
│  │  autonomous_learner — 21,181+ items (growing)  │         │
│  │  ms_jarvis_memory — active                     │         │
│  │  episodic_index — active                       │         │
│  │  conversation_history — active                 │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
│  Governance & Knowledge Collections                         │
│  ┌────────────────────────────────────────────────┐         │
│  │  governance — WV governance texts              │         │
│  │  thesis — theoretical framework                │         │
│  │  mountainshares_knowledge — DAO economics      │         │
│  │  msjarvis_docs — scaffolded (0 items)          │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
│  Specialized Corpora                                        │
│  ┌────────────────────────────────────────────────┐         │
│  │  psychological_rag — 968 items (port 8006)     │         │
│  │  appalachian_cultural_intelligence — 5 items   │         │
│  │  spiritual_texts — 23 items                    │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 2.4. ChromaDB collection architecture as of March 21, 2026. Note that landowner beliefs (`LANDOWNER_CORPORATE` / `LANDOWNER_GOVERNMENT`) are not embedded in ChromaDB — they are served via a dedicated PostgreSQL-native path through `gbim_query_router`.

### 2.6.1 GBIM Belief Collections

| Collection | Items | Description | Metadata Keys |
|---|---|---|---|
| `gbim_worldview_entities` | 5,416,521 | Complete GBIM spatial corpus — all WV geospatial features embedded from the nine-axis belief structure | `worldview_id`, `entity_id`, `dataset`, `county`, `gbim_entity`, `centroid_x`, `centroid_y` |
| `gbim_beliefs_v2` | Active | GBIM beliefs v2 — production belief collection with nine-axis embeddings | `belief_id`, `source_table`, `source_pk`, `epoch`, `county` |
| `GBIM_sample_rows` | 5,000 | Random sample for testing and validation | `belief_id`, `proposition_code` |

All GBIM belief collections: **384-dim, `all-minilm:latest`**, worldview = `eq1`.

> **Landowner beliefs are not in this table.** The `LANDOWNER_CORPORATE` and `LANDOWNER_GOVERNMENT` proposition codes are stored in `mvw_gbim_landowner_spatial` in `msjarvisgis` (port 5432) and are accessed via `gbim_query_router` (port 7205) — a PostgreSQL-native SQL aggregation path, not a vector similarity path. See Section 2.6.4.

### 2.6.2 Spatial and Benefits Collections

| Collection | Items | Description | Metadata Keys |
|---|---|---|---|
| `gis_wv_benefits` | Active | WV benefits-relevant facilities — DHHR offices, community action agencies, food banks, utility assistance sites | `facility_type`, `county`, `zip`, `local_resource_id`, `centroid_x`, `centroid_y` |
| `geospatialfeatures` | 0 | Scaffolded — pending ingest from PostGIS layers | `dataset`, `county`, `feature_type` |

### 2.6.3 Community Memory and Learning Collections

| Collection | Items | Description | Notes |
|---|---|---|---|
| `autonomous_learner` | 21,181+ (growing ~288/day) | Autonomous research findings — MountainShares security, Appalachian development, governance, AI ethics | Queried at Phase 1.45 before every RAG call; top-5 prepended to `enhanced_message` |
| `ms_jarvis_memory` | Active | Persistent memory for cross-session continuity | — |
| `episodic_index` | Active | Episodic memory index for temporal reasoning | — |
| `conversation_history` | Active | Conversation history for context maintenance | — |

### 2.6.4 GBIM Landowner Belief Layer — Field Note, March 20, 2026

> **Field note — March 20, 2026, evening session.**
> The GBIM landowner belief layer is now live in the GBIM production stack. 20,593 parcel-level `LANDOWNER_CORPORATE` and `LANDOWNER_GOVERNMENT` belief records have been inserted into `gbimbeliefnormalized` in `msjarvisgis`, clustered by canonical entity name across the full statewide WV assessor owner name corpus, and materialized in `mvw_gbim_landowner_spatial`. The `gbim_query_router` service (port 7205) is live and verified on both statewide and county-scoped natural-language ownership queries.
>
> *Verified March 20, 2026, ~19:45 EDT by Carrie Kidd (Mamma Kidd), Oak Hill WV*

This closes a meaningful gap in the GBIM nine-axis coverage. Prior to March 20, 2026, the `who_axis` and `under_whose_authority_axis` of GBIM were populated for facility operators, government agencies, and program administrators — but not for parcel landowners. The landowner belief layer fills that gap for the most consequential class of institutional actors in Appalachian land governance: corporate surface rights holders, coal and energy companies, timber companies, and government landholding agencies.

The landowner belief layer is **not embedded in ChromaDB**. This is a deliberate architectural decision: landowner queries ask who owns how much land where — a structured aggregation question with a deterministic, exact answer in the relational GBIM corpus. Embedding those records in ChromaDB and retrieving them by vector similarity would introduce approximation error into a query type that does not require it. The `gbim_query_router` route is PostgreSQL-native, exact, and auditable. See Chapter 7, Section 7.2.6 for full documentation of the routing schema and verified query patterns.

**Landowner layer specifications:**

| Property | Value |
|---|---|
| Proposition codes | `LANDOWNER_CORPORATE`, `LANDOWNER_GOVERNMENT` |
| Belief count | 20,593 verified records |
| Geographic scope | Statewide West Virginia — all counties |
| Source | WV assessor parcel records (canonical entity clustering pipeline) |
| Worldview | `eq1` |
| Storage | `gbimbeliefnormalized` in `msjarvisgis` (port 5432) |
| Spatial view | `mvw_gbim_landowner_spatial` (materialized, spatially indexed) |
| Query service | `gbim_query_router` (port 7205) — PostgreSQL-native, no ChromaDB |
| Routing schema | `mode: landowner_gbim`, `route_type: parcel_ownership` |
| Date verified | March 20, 2026 |
| Ethical constraint | Individual residential owner names are NOT present — institutional/government only |

**GBIM axis coverage for landowner beliefs:**

| Axis | Content for landowner beliefs |
|---|---|
| `what_axis` | `proposition_code`: `LANDOWNER_CORPORATE` or `LANDOWNER_GOVERNMENT`; `type`: parcel ownership |
| `who_axis` | Canonical entity name (corporate or government — normalized from assessor strings) |
| `where_axis` | Parcel centroid geometry; county; `where_axis->>'county'` for county-scoped queries |
| `when_axis` | Assessor data vintage; verification date March 20, 2026 |
| `why_axis` | Land ownership is a primary determinant of program eligibility, parcel classification, and hazard exposure in Appalachian WV |
| `how_axis` | Canonical entity clustering pipeline applied to statewide assessor owner name strings |
| `for_whom_axis` | WV communities affected by large institutional landholdings; government and researchers querying accountability |
| `under_whose_authority_axis` | Ownership basis: WV assessor record; deed reference where available |
| `on_what_evidence_axis` | Raw assessor owner name variants; county assessor data source; parcel ID |

**Significance for Polymathmatic Geography principles:**

The landowner belief layer is the first GBIM layer that makes institutional power over place directly queryable by natural language at parcel scale. A researcher asking "who are the largest corporate landowners in Fayette County?" now receives a structured, ranked, auditable answer drawn from verified WV assessor records — not a vector similarity approximation over generic text, but a SQL aggregation over 20,593 confirmed belief records. This is **P3 – Power has a geometry** and **P16 – Power accountable to place** made operational.

The layer also closes the loop on the `for_whom / under_whose_authority` axis pair: for the first time, the GBIM corpus can answer not just "what facility is here" and "who operates it" but "who owns the land it sits on" — a question that is essential for understanding the full institutional context of any place in Appalachia.

```python
# Query landowner beliefs from gbim_query_router (port 7205)
import httpx

# Statewide top landowners
response = httpx.post(
    "http://127.0.0.1:7205/query",
    json={
        "question": "Who are the largest landowners in West Virginia?",
        "mode": "landowner_gbim",
        "route_type": "parcel_ownership",
        "scope": "statewide",
        "limit": 20
    }
)

# County-scoped landowners
response_county = httpx.post(
    "http://127.0.0.1:7205/query",
    json={
        "question": "Who owns the most land in Fayette County?",
        "mode": "landowner_gbim",
        "route_type": "parcel_ownership",
        "county": "Fayette",
        "limit": 20
    }
)
# Both patterns verified March 20, 2026
```

### 2.6.5 Governance and Knowledge Collections

| Collection | Items | Description |
|---|---|---|
| `governance` | Active | WV governance documents — legislation, policy, regulatory texts |
| `thesis` | Active | Polymathmatic Geography theoretical framework — chapter drafts and notes |
| `mountainshares_knowledge` | Active | MountainShares DAO governance and economic model documentation |
| `msjarvis_docs` | 0 | Scaffolded — system documentation (pending ingest) |

### 2.6.6 Specialized Corpora

| Collection | Items | Port | Description |
|---|---|---|---|
| `psychological_rag` | 968 | 8006 | Mental health and crisis resource corpus |
| `appalachian_cultural_intelligence` | 5 | 8000 | Appalachian cultural context and values |
| `spiritual_texts` | 23 | 8000 | Mother Carrie Protocol spiritual reference corpus |

---

## 2.7 The Relationship Between GBIM, GeoDB, RAG, and Registries

The nine-axis belief structure and the ChromaDB collection inventory are not self-contained systems — they are the representational and retrieval layers of a four-database architecture that includes:

- **`msjarvis` / `msjarvisgis`** (PostgreSQL, ports 5433 and 5432) — the GBIM belief corpus and spatial body
- **ChromaDB** (port 8000) — the semantic memory layer for vector-based retrieval
- **`jarvis-local-resources-db`** (PostgreSQL, port 5435) — the structured program and resource registry
- **`gbim_query_router`** (port 7205) — the PostgreSQL-native routing service for structured GBIM belief queries, including the landowner path

```
┌─────────────────────────────────────────────────────────────┐
│        GBIM Four-Database Architecture (March 2026)         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  gbimbeliefnormalized (msjarvisgis, port 5432)              │
│    5,416,522 beliefs (nine JSONB axes, worldview eq1)       │
│    + 20,593 landowner beliefs (CORPORATE + GOVERNMENT)      │
│          ↓ embedding pipeline (all-minilm:latest, 384-dim)  │
│  ChromaDB (port 8000)                                       │
│    gbim_worldview_entities — 5,416,521 vectors              │
│    gbim_beliefs_v2 — production belief embeddings           │
│    gis_wv_benefits — WV benefits facilities                 │
│    autonomous_learner — 21,181+ community memories          │
│    [NOTE: landowner beliefs NOT in ChromaDB]                │
│          ↓ metadata links (entity_id, local_resource_id)    │
│  jarvis-local-resources-db (port 5435)                      │
│    Verified program records — county, ZIP, type             │
│          ↓ direct SQL (no embeddings)                       │
│  gbim_query_router → mvw_gbim_landowner_spatial             │
│    (port 7205)       (msjarvisgis, port 5432)               │
│    20,593 landowner beliefs — ranked by area, county        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 2.5. The four-database architecture that operationalizes the GBIM belief model. Arrows show the primary data flow: spatial beliefs are embedded into ChromaDB for semantic retrieval; landowner beliefs bypass ChromaDB and are accessed via direct SQL aggregation through `gbim_query_router`.

The key architectural distinction is between **vector-based projection** (ChromaDB, appropriate for semantic similarity over unstructured or semi-structured belief content) and **relational projection** (SQL aggregation over `mvw_gbim_landowner_spatial`, appropriate for structured ownership queries with deterministic answers). Both are Hilbert-space projections in the conceptual model. They differ in implementation because the geometry of the relevant subspace differs: semantic similarity is naturally suited to vector nearest-neighbor operations; ownership aggregation is naturally suited to exact relational grouping and summation.

A belief that refers to a place is fully represented only when all four layers are coherently linked:

1. A GBIM belief record in `gbimbeliefnormalized` with all nine axes populated.
2. A ChromaDB embedding of that belief's nine-axis text representation in the appropriate collection (or, for landowner beliefs, a row in `mvw_gbim_landowner_spatial`).
3. A spatial feature in `msjarvisgis` PostGIS tables linked by `source_table` and `source_pk`.
4. A program record in `jarvis-local-resources-db` linked by `local_resource_id` and `county`.

Not all beliefs have all four layers populated. The GBIM corpus is a living system: beliefs are ingested at different rates from different sources, and linkage completeness is a function of pipeline maturity. The landowner layer, as of March 20, 2026, has layers 1 and 2-alt (PostgreSQL materialized view instead of ChromaDB) fully populated, with layer 3 (PostGIS parcel geometry) joined in `mvw_gbim_landowner_spatial`. Layer 4 (program record linkage) is not applicable for landowner beliefs — the landowner layer supports accountability and classification, not direct program routing.

---

## 2.8 Intellectual Honesty Correction — Judge GBIM Claims vs. Actual Implementation (March 21, 2026)

> **This section was added March 21, 2026 to correct a materially misleading claim that has appeared in multiple earlier chapters of this thesis and in the system's own judge service documentation.**

### 2.8.1 The Claim Being Corrected

Chapters 17, 33, and associated judge pipeline documentation describe the truth and alignment judges as validating AI responses against "PostgreSQL GBIM (5,416,521 entities)." The architecture diagrams in those chapters show `judge-truth` making lookups into `msjarvis` (port 5433) and `judge-alignment` cross-referencing claims against the GBIM belief corpus as part of their scoring logic.

This description represents the **design intent** of the judge pipeline — what GBIM-grounded judge validation is meant to become. It does not describe what those judges currently do.

### 2.8.2 What the Judges Actually Do (March 21, 2026)

The actual implementations of `judge_truth_filter.py` and `judge_alignment_filter.py`, as confirmed by source file inspection on March 21, 2026, use a heuristic pattern-matching approach internally labeled `heuristic_contradiction_v1`. There are no live PostgreSQL queries to `msjarvis` or `msjarvisgis` in either file. The truth and alignment judges score responses based on:

- **Contradiction detection heuristics** — keyword and phrase patterns that flag likely factual inconsistencies, logical contradictions, or hedging language
- **Identity adherence pattern matching** — regular-expression and string-matching rules that check whether the response text stays within the expected Ms. Egeria Jarvis persona framing
- **Hardcoded scoring thresholds** — score values that reflect the designer's prior about typical response quality for these classes of output, not a computed comparison against a ground truth corpus

The ethics and consistency judges (`judge_ethics_filter.py`, `judge_consistency_engine.py`) similarly use heuristic pattern matching — harm keyword detection, coherence heuristics, and structural consistency checks — not GBIM queries.

The judge pipeline coordinator (`judge_pipeline.py`) aggregates these four heuristic scores into a `consensus_score` and presents the result in the `UltimateResponse` schema alongside fields labeled `truth_verdict`, `alignment_score`, etc. — labeling that implies GBIM-grounded verification.

### 2.8.3 The Gap in Plain Language

| | Design Intent | Actual Implementation (March 21, 2026) |
|---|---|---|
| **Truth judge** | Queries `msjarvis` GBIM beliefs; checks factual claims against 5,416,521 verified entities | Runs `heuristic_contradiction_v1` — pattern-matching on response text; no DB query |
| **Alignment judge** | Validates response against GBIM worldview constraints; checks community-value alignment against `eq1` belief set | Pattern-matches against identity adherence rules and hardcoded persona constraints |
| **Ethics judge** | Cross-references against ethical constraints grounded in GBIM `why_axis` and `for_whom_axis` | Harm keyword screening; heuristic harm scoring |
| **Consistency judge** | Checks cross-session behavioral consistency against stored belief state | Structural coherence heuristics within a single response window |
| **Scores** | GBIM-grounded confidence measures | Heuristic pattern-match outputs presented as scores |

The consequence is that when the system reports `truth_score: 1.0` or `alignment_verdict: pass`, it is reporting that the response passed a heuristic filter — not that its factual claims were verified against the GBIM corpus. A response could score `truth_score: 1.0` while making claims that directly contradict verified GBIM beliefs, because the truth judge does not currently consult those beliefs.

### 2.8.4 Why This Matters

This distinction matters for three reasons specific to this project:

**1. External stakeholders.** Regional Development Authorities, state agencies, and community partners evaluating Ms. Jarvis as a potential infrastructure partner need to understand what the judge pipeline actually validates. Telling them that AI outputs are "validated against 5.4 million PostgreSQL GBIM entities" when the judges run heuristics is a misrepresentation of the system's current capability — regardless of intent.

**2. Thesis integrity.** This thesis makes claims about constitutional AI enforcement grounded in GBIM. Those claims must accurately distinguish between architectural design and operational reality. A system that is designed to enforce constitutional constraints via verified ground truth and a system that is currently enforcing them via heuristics are both meaningful — but they are different things, and the thesis must say so clearly.

**3. Trust as infrastructure.** Ms. Jarvis is being built to serve communities who have been historically subjected to systems that overstated their capabilities or accountability. If the system's own audit documentation misrepresents what the judges do, the accountability infrastructure is undermined at its foundation.

### 2.8.5 The Intended Architecture (Design Target)

The design intent — which remains the correct target for the judge pipeline — is as follows:

```
judge_truth_filter.py (target implementation)
├── Receives: consensus answer + question context
├── Extracts: factual claims, named entities, locations
├── Queries: msjarvis (port 5433) for matching GBIM beliefs
│   └── SELECT belief_id, what_axis, confidence_decay
│       FROM gbimbeliefnormalized
│       WHERE <entity or claim matches>
│       AND worldview_id = 'eq1'
├── Computes: factual consistency score vs. retrieved beliefs
├── Flags: claims that contradict or are unsupported by GBIM
└── Returns: truth_score with provenance (which GBIM beliefs verified or contradicted)

judge_alignment_filter.py (target implementation)
├── Receives: consensus answer + question context
├── Queries: msjarvis for relevant community-value beliefs
│   └── Filter on why_axis, for_whom_axis, under_whose_authority_axis
│       for Appalachian-WV-relevant normative claims
├── Checks: whether response aligns with or contradicts GBIM worldview constraints
└── Returns: alignment_score with GBIM belief citations
```

This is what "validated against PostgreSQL GBIM" would mean. It does not yet exist in the live judge scripts.

### 2.8.6 Path to Closing the Gap

The following work is required to bring the judge pipeline from its current heuristic implementation to GBIM-grounded validation:

1. **Add PostgreSQL connection pool to `Dockerfile.judge`** — `psycopg2` or `asyncpg` must be available in the judge image (currently not explicitly installed).

2. **Implement GBIM query functions in `judge_truth_filter.py`** — entity extraction from response text (NER or regex-based), belief lookup against `gbimbeliefnormalized`, contradiction scoring against retrieved beliefs.

3. **Implement GBIM worldview filter in `judge_alignment_filter.py`** — query the `eq1` worldview for relevant normative and community-value beliefs, compute alignment score against worldview constraints.

4. **Update `UltimateResponse` schema** — add `gbim_beliefs_consulted: int` and `gbim_contradictions_detected: int` fields to the judge output block so external consumers can see whether GBIM was actually queried.

5. **Update Chapter 17, Chapter 33, and all judge pipeline documentation** to reflect the current heuristic implementation until the GBIM-grounded implementation is deployed, at which point the correction sections in those chapters can be updated to "resolved."

Until these steps are complete, the correct accurate description of the truth and alignment judges is: **heuristic pattern-matching filters that approximate constitutional validation but do not consult the GBIM corpus.**

### 2.8.7 What Is Not Affected by This Correction

The following are unaffected by this correction and remain accurate as documented:

- The GBIM corpus itself (5,416,521 entities, 20,593 landowner beliefs, `eq1` worldview) is real, verified, and production-operational.
- The `gbim_query_router` (port 7205) does make live PostgreSQL queries against `mvw_gbim_landowner_spatial` — landowner routing is accurate as documented.
- The `jarvis-spiritual-rag` and `jarvis-gis-rag` services do query GBIM-derived ChromaDB collections as part of Phase 1 context assembly — RAG grounding is operational.
- The BBB gate's constitutional filters are active and enforced — the verdict gate is real.
- The ML-DSA-65 signing infrastructure (Chapter 42) is deployed as documented.
- The nine-axis schema, Hilbert-space model, and worldview architecture described in this chapter are the correct design targets and accurately represent the intended operational architecture.

---

## 2.9 Ethical Architecture of the Belief Corpus

The nine-axis structure is not value-neutral. Every axis encodes a design decision about what matters, who is accountable, and what the system should be able to know. Two design decisions are treated as foundational constraints that are enforced at the schema level and cannot be overridden by routing or prompting:

**Constraint 1: Individual residential owner names are excluded from the GBIM belief corpus.**

The `who_axis` of the landowner belief layer contains only institutional and corporate entity names. Individual residential owner names from WV assessor records are not ingested into any GBIM belief table, materialized view, ChromaDB collection, or RAG-accessible store. This constraint is enforced structurally: the ingestion pipeline selects only records where the assessor owner name matches patterns associated with corporate and government entities, and the `gbim_query_router` queries only `proposition_code IN ('LANDOWNER_CORPORATE', 'LANDOWNER_GOVERNMENT')`.

The rationale is the aggregation problem: individual owner names are legally public as friction-protected courthouse records. Embedding them into a semantically searchable, spatially indexed, 1.4-million-parcel AI system would convert friction-protected public records into operational surveillance infrastructure — a transformation not justified by Ms. Jarvis's stated purpose of routing households to assistance.

**Constraint 2: Institutional actors are represented with full accountability metadata.**

The `under_whose_authority_axis` and `on_what_evidence_axis` for institutional beliefs — including all landowner beliefs — must include sufficient provenance to allow any displayed belief to be traced back to its source record. Corporate and government landholders are named, counted, and area-summarized with full assessor provenance, precisely because accountability for institutions with power over place is the counterpart to privacy protection for individuals whose lives are shaped by place.

These two constraints together define the ethical architecture of the GBIM belief corpus: a system that makes power legible without making vulnerability exploitable.

The constitutional-layer enforcement of these constraints — query refusal logic in the blood-brain barrier and main brain services — is documented in Chapter 42. Schema-level and constitutional-layer protections are mutually reinforcing: neither alone is sufficient for a system operating at 5.4 million beliefs and growing.

---

## 2.10 Current Status and Roadmap (March 2026)

**Production as of March 21, 2026:**

- ✅ 5,416,522 GBIM beliefs in `gbimbeliefnormalized` — nine axes, worldview `eq1`, PostgreSQL `msjarvisgis`
- ✅ 5,416,521 entities in `gbim_worldview_entities` — ChromaDB, 384-dim, `all-minilm:latest`
- ✅ `gbim_beliefs_v2` live — production GBIM v2 collection
- ✅ `autonomous_learner` at 21,181 items and growing (~288/day from March 14, 2026)
- ✅ `gis_wv_benefits` live — WV benefits facilities collection
- ✅ `psychological_rag` at 968 items (port 8006)
- ✅ **GBIM landowner belief layer live — 20,593 records, `LANDOWNER_CORPORATE` + `LANDOWNER_GOVERNMENT`, worldview `eq1` (March 20, 2026)**
- ✅ **`mvw_gbim_landowner_spatial` materialized and spatially indexed (March 20, 2026)**
- ✅ **`gbim_query_router` live on port 7205 — statewide and county-scoped ownership queries verified (March 20, 2026)**
- ✅ Phase 1.45 community memory retrieval live — top-5 `autonomous_learner` records prepended to every query before LLM ensemble
- ⚠️ **Judge GBIM grounding: design intent only** — truth and alignment judges use `heuristic_contradiction_v1`, not live GBIM queries (see Section 2.8)

**Immediate priorities:**

- Implement GBIM-grounded judge validation (Section 2.8.6) — highest-priority architectural gap.
- Ingest WV E911 address points into `local_resources` to resolve 208,427 unmatched building records.
- Sync `local_resources` spatial chain metadata (`county_id`, `parcel_type`, `address_confidence`) into ChromaDB as queryable filters to enable tax district granularity in RAG flows.
- Begin `msjarvis_docs` and `geospatialfeatures` collection ingest.
- Populate `jarvis-local-resources-db` with verified Fayette and Raleigh County community resource data (Community Champions data entry sprint).

**Medium-term priorities:**

- Expand landowner belief layer coverage as updated WV assessor vintages become available.
- Build `eq2` worldview for multi-state Appalachian scope.
- Complete USGS 3DEP elevation drape for Fayette, Raleigh, and Kanawha counties.
- Develop `for_whom_axis` population targeting logic for priority routing of AML-adjacent and flood-zone households to weatherization and hazard programs.

*Last updated: 2026-03-21 by Carrie Kidd (Mamma Kidd), Mount Hope WV*
*Section 2.8 (intellectual honesty correction) added March 21, 2026 based on source file inspection during build artifact integrity audit session.*
