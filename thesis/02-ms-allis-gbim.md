# 2. The Geometric Belief Model and GBIM Architecture

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: April 23, 2026*
---

## Why This Matters for Polymathmatic Geography

This chapter provides the theoretical foundation for understanding how Ms. Allis represents knowledge, belief, and uncertainty — and why those representations are structured the way they are. It supports:

- **P1 – Every where is entangled** by establishing that belief is not stored as isolated facts but as multi-axis geometric structures in which spatial, temporal, institutional, and normative dimensions are co-present and mutually constraining — so that a single GBIM belief about a hospital in Fayette County is simultaneously a claim about what exists, where it is, when it was verified, who has authority over it, and what its implications are for program routing.

- **P3 – Power has a geometry** by showing that the GBIM axis structure — particularly `who`, `where`, `under_whose_authority`, and `for_whom` — is designed to make institutional power over place explicit and queryable, not buried in unstructured text. The landowner belief layer (Section 2.6.4) is the direct realization of this principle at parcel scale, confirmed fully operational end-to-end as of April 23, 2026.

- **P5 – Design is a geographic act** by treating the nine-axis GBIM schema, the worldview structure, the collection inventory, and the ChromaDB configuration not as neutral technical choices but as geographic and political decisions that determine which facts are computable, which relationships are traversable, and which forms of institutional accountability are operationally enforceable.

- **P12 – Intelligence with a ZIP code** by grounding the Hilbert-space model in a concrete PostgreSQL corpus on `msjarvis-db` (host port 5433, container port 5432), so that the abstract framework of quantum-geometric belief representation is always already indexed to real West Virginia places, programs, and populations.

- **P16 – Power accountable to place** by designing the belief structure so that institutional actors — government agencies, corporate landowners, utility companies — are represented as first-class GBIM entities with explicit `under_whose_authority` and `who` axis entries, making them queryable and auditable in a way that individual residential actors deliberately are not.

The theoretical framework in this chapter is not a preamble to the system — it is the system's operating logic, expressed at the level of schema, routing, and collection design rather than at the level of code.

Accordingly, this chapter belongs to the **Theoretical Foundation** tier: it establishes the geometric belief model, the nine-axis GBIM schema, the Hilbert-space representation of uncertainty, the worldview structure, and the ChromaDB collection inventory that together constitute the epistemic architecture of Ms. Egeria Allis.

---

## 2.1 Purpose and Scope

This chapter establishes the theoretical framework underlying the **GeoBelief Information Model (GBIM)** — the core representational system that allows Ms. Egeria Allis to hold, update, route, and reason over structured beliefs about West Virginia's physical world, institutional landscape, and programmatic infrastructure.

GBIM is not a database schema in the conventional sense. It is a multi-axis geometric representation of belief that treats each claim about the world as a structured object with nine dimensions, each encoding a distinct aspect of the claim's meaning, provenance, authority, and applicability. This nine-axis structure is what allows beliefs derived from a WV assessor parcel record, a federal hazard dataset, a community organization's program flyer, and a peer-reviewed paper on Appalachian poverty to coexist in a single corpus and be meaningfully compared, combined, and routed.

The chapter is organized as follows:

- **Section 2.2** introduces the nine-axis belief schema and explains the role of each axis.
- **Section 2.3** presents the Hilbert-space model of belief and uncertainty that motivates the GBIM design.
- **Section 2.4** describes the worldview structure (`eq1` and related worldviews) and its role in routing and filtering.
- **Section 2.5** describes the PostgreSQL GBIM corpus — its current scale, table structure, and production status as of April 2026.
- **Section 2.6** presents the ChromaDB collection inventory — the vector-backed memory layer that makes GBIM beliefs semantically retrievable.
- **Section 2.7** addresses the relationship between GBIM, the GeoDB spatial body (Chapter 6), the RAG pipeline (Chapter 7), and the local resource registry.
- **Section 2.8** documents the `nbb_pituitary_gland` governance module — the neural-behavioral bridge operating at `host:8108` that modulates every Ms. Allis response through five active governance protocols.
- **Section 2.9** documents the GBIM confidence decay pipeline — the live 24-hour decay loop with `needs_verification` escalation.
- **Section 2.10** is an intellectual honesty record: it documents the retirement of `heuristic_contradiction_v1` and the promotion of `rag_grounded_v2` as the canonical truth judge, now DGM-corroborated.
- **Section 2.11** documents the ethical architecture of the belief corpus — specifically the exclusion of individual residential owner names and the full accountability metadata required for institutional actors.
- **Section 2.12** presents the `jarvis-gbim-query-router` service (port 7205) — the PostgreSQL-native GBIM retrieval path, fully operational end-to-end as of April 23, 2026.
- **Section 2.13** documents the `mvw_gbim_landowner_spatial` materialized view — its schema, spatial indexing, confirmed row count, and RBAC gate.

---

## 2.2 The Nine-Axis Belief Schema

Every belief in the GBIM corpus is a structured object with nine named axes stored as JSONB in `gbim_worldview_entities` (L2 distance; primary spatial collection in ChromaDB) and `gbim_beliefs_v2` (cosine distance; production belief embeddings):

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
│  PostgreSQL storage: msjarvis-db (host port 5433,           │
│    container port 5432), database: msjarvisgis              │
│  ChromaDB: gbim_worldview_entities (L2) for spatial         │
│    corpus; gbim_beliefs_v2 (cosine) for belief embeddings   │
│  All beliefs carry: belief_id, proposition_code,            │
│    worldview_id, confidence_decay, needs_verification       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

*Figure 2.1. The nine-axis GBIM belief structure. Every belief in the corpus — from a hospital location to a coal company land holding — is represented with all nine axes, enabling multi-dimensional filtering, routing, and reasoning.*

**`what_axis`** — The propositional content of the belief: what entity exists, what relationship holds, what condition obtains. Structured as a typed JSONB object with fields including `type`, `label`, `description`, and `proposition_code`. The `proposition_code` is the primary routing key.

**`who_axis`** — The subject or actor of the belief. For the landowner belief layer, this is the canonical corporate or government entity name derived from WV assessor records. Individual residential owner names are explicitly excluded — see Section 2.11.

**`where_axis`** — The spatial grounding: geometry (point, line, polygon), coordinate system, county, ZIP code. For parcel-level beliefs, includes parcel centroid and county derived from `mvw_gbim_landowner_spatial` in `msjarvisgis`.

**`when_axis`** — Temporal scope: when the belief was created, last verified, expected decay schedule. Paired with `confidence_decay` to implement time-sensitive freshness signaling — see Section 2.9.

**`why_axis`** — The normative or causal rationale: why this belief is relevant to Ms. Allis's mission.

**`how_axis`** — The verification method: what pipeline generated the belief, what spatial or statistical operation produced it.

**`for_whom_axis`** — The intended beneficiary population: which households, communities, or demographic groups the belief is most relevant to.

**`under_whose_authority_axis`** — The institutional authority under which the claim holds. For the landowner belief layer, records the ownership basis — assessor record, deed reference, government registry. Central to **P16 – Power accountable to place**.

**`on_what_evidence_axis`** — The primary source and provenance chain: dataset name, table, primary key, data vintage.

---

## 2.3 Hilbert-Space Representation of Belief and Uncertainty

The GBIM nine-axis schema is motivated by a geometric model of belief that treats the system's overall epistemic state as a vector in a high-dimensional Hilbert space:

- Each basis dimension corresponds to a distinguishable claim about the world at a specific place and time, under a specific institutional authority.
- The system's belief state is a superposition over these dimensions — a probability amplitude distribution reflecting confidence, uncertainty, and entanglement between claims.
- A retrieval operation (RAG query, spatial filter, landowner lookup) is a **projection** of this state onto a relevant subspace.
- Belief update — ingesting new data, verifying a claim — is a rotation or scaling on the state vector.

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
│  Top-k belief records (ChromaDB gbim_worldview_entities /   │
│    gbim_beliefs_v2) or                                       │
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

*Figure 2.2. Conceptual view of the Hilbert-space projection model underlying GBIM retrieval. Vector-based projections (ChromaDB) and relational projections (SQL aggregation over `mvw_gbim_landowner_spatial`) are both projections into relevant subspaces — they differ in geometric mechanism, not epistemic role.*

---

## 2.4 Worldview Structure and the `eq1` Worldview

The production worldview is **`eq1`** — the primary equity-oriented worldview grounding Ms. Allis's reasoning in Appalachian community perspectives, WV state data, and federal program structures. All production beliefs in `gbim_worldview_entities` (ChromaDB, L2) are tagged `worldview_id = 'eq1'`.

```
┌─────────────────────────────────────────────────────────────┐
│              Worldview Structure in GBIM                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  worldview_id = 'eq1'  (production worldview)               │
│  ─────────────────────────────────────────────────────      │
│  Interpretive frame: Appalachian equity orientation         │
│  Data scope: WV state + federal sources verified for WV     │
│  ChromaDB collections:                                      │
│    gbim_worldview_entities — L2 distance (spatial corpus)   │
│    gbim_beliefs_v2 — cosine distance (belief embeddings)    │
│  Landowner view: mvw_gbim_landowner_spatial                 │
│    ✅ 38,979 rows in msjarvis-db (April 23, 2026)            │
│    536 unattributed — normal for roads/easements            │
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

*Figure 2.3. The GBIM worldview structure. The production `eq1` worldview is the authoritative belief frame for all Ms. Allis reasoning.*

---

## 2.5 The PostgreSQL GBIM Corpus — Authoritative Layout (April 23, 2026)

Ms. Allis runs one primary production PostgreSQL database container. All references to a database named `msallisgis`, `gisdb`, or port `5452` are retired — those names do not exist in the current production stack.

> **⚠️ ChromaDB API Version Notice:** All ChromaDB API calls must use the **v2 path**
> (`/api/v2/...`). The v1 path (`/api/v1/...`) returns **HTTP 410 Gone** and is
> permanently deprecated. Update any scripts, services, or documentation that reference
> `/api/v1/` immediately.

### Live Database Layout

| Layer | Container | Host Port | Container Port | Database | Owner | Contents |
|---|---|---|---|---|---|---|
| Production PostGIS / GBIM | `msallis-db` | **5433** | **5432** | `msallisgis` | postgres | Full spatial GBIM, landowner view, provider summaries, TIGER, topology |

**Production database:** `msallis-db` — 16 GB / 294 tables / 11 schemas (April 23, 2026).

### Key Tables in `msallisgis`

| Table | Role |
|---|---|
| `gbim_worldview_entity` | Full spatial GBIM entity table — nine-axis JSONB, worldview eq1, all WV GIS source layers |
| `mvw_gbim_landowner_spatial` | Materialized view — ✅ **38,979 rows in msjarvis-db** (April 23, 2026); centroid_x/y, county, state, source_dataset |
| `gbim_entities` | 4-column application mirror — `id`, `worldview_id`, `entity_type`, `label` |
| `gbim_decay_audit` | Decay pipeline audit log — records each decay tick and escalation event |
| `gbim_provider_block_join_block` | Provider-block join (block perspective) |
| `gbim_block_provider_summary` | Block-level provider summaries |
| `gbim_provider_population_summary` | Provider population summaries |
| `tiger.*` | TIGER/Line schemas: `tiger.addr`, `tiger.edges`, `tiger.zcta5`, etc. |
| `topology.*` | PostGIS topology schema |

### Access Patterns

```python
import psycopg2

# Production database: msjarvis-db (host port 5433, container port 5432)
# Database name: msjarvisgis
conn = psycopg2.connect(
    host="localhost", port=5433,
    database="msjarvisgis", user="postgres", password="postgres"
)

cursor = conn.cursor()

# Query GBIM worldview entities
cursor.execute("""
    SELECT
        id,
        worldview_id,
        entity_type,
        label AS display_name,
        ((belief_state->'spatialmetadata')->>'centroidx')::double precision AS centroid_x,
        ((belief_state->'spatialmetadata')->>'centroidy')::double precision AS centroid_y,
        ((belief_state->'axes')->'where')->>'county' AS county
    FROM gbim_worldview_entity
    WHERE ((belief_state->'axes')->'where')->>'county' = 'Fayette'
    LIMIT 10;
""")

# Query landowner materialized view
cursor.execute("""
    SELECT owner_name, parcel_id, county, centroid_x, centroid_y
    FROM mvw_gbim_landowner_spatial
    WHERE county = 'Fayette'
    LIMIT 20;
""")

# Query decay audit
cursor.execute("""
    SELECT entity_id, decay_value, needs_verification, audit_ts
    FROM gbim_decay_audit
    WHERE needs_verification = TRUE
    ORDER BY decay_value DESC
    LIMIT 20;
""")
```

### Shell / psql Access

```bash
# Production database — docker exec msjarvis-db
docker exec msjarvis-db psql -U postgres -d msjarvisgis

# Forensic database — with explicit host binding
docker exec postgis-forensic psql -h 127.0.0.1 -U jarvis -d msjarvisgis
```

---

## 2.6 ChromaDB Collection Inventory

The ChromaDB instance (host port 8002, container-internal port 8000) is the vector-backed semantic memory layer. All collections use 384-dimensional embeddings produced by `all-minilm:latest`.

> **⚠️ ChromaDB API v2 — REQUIRED:** All API calls must use `/api/v2/...` paths.
> `/api/v1/...` returns **HTTP 410 Gone** permanently. This affects all services,
> scripts, and integrations. No exceptions.

> **UUID two-step pattern for collection operations:** ChromaDB v2 does not support
> count by collection name directly. Use the UUID two-step:
> ```python
> # Step 1: resolve collection name → UUID
> resp = httpx.get("http://localhost:8002/api/v2/collections/gbim_worldview_entities")
> collection_id = resp.json()["id"]
>
> # Step 2: count using UUID
> count_resp = httpx.get(
>     f"http://localhost:8002/api/v2/collections/{collection_id}/count"
> )
> count = count_resp.json()
> ```
> Direct `/count` calls by name are not reliable in v2. Always resolve UUID first.

> **Embedding lock:** `all-minilm:latest`, 384-dim. `nomic-embed-text` (768-dim) is
> incompatible with all existing collections.
> **Chunking rule:** ≈100 words per chunk, ~20-word overlap (256-token context limit).
> **Container count:** 112 confirmed (April 16, 2026 — thesis-verified) /
> 100 point-in-time (April 23, 2026).

### 2.6.1 GBIM and Spatial Collections

| Collection | Distance | Count | Role |
|---|---|---|---|
| `gbim_worldview_entities` | **L2** | Active | Complete GBIM spatial corpus — all WV geospatial features embedded; metadata: `worldview_id`, `entity_id`, `dataset`, `county`, centroid_x/y |
| `gbim_beliefs_v2` | **cosine** | Active | Production belief embeddings — nine-axis text representations; separate from spatial corpus |
| `GBIM_Fayette_sample` | cosine | **1,535** | Fayette County GBIM belief sample |
| `geospatialfeatures` | cosine | **60,000** | Vectorized PostGIS spatial features |
| `gis_wv_benefits` | cosine | Active | WV benefits-relevant facilities — DHHR, CAAs, food banks |
| `GBIM_sample_rows` | cosine | 5,000 | Random sample for testing and validation |

> **`gbim_worldview_entities` vs. `gbim_beliefs_v2`:** These are distinct collections
> serving distinct roles. `gbim_worldview_entities` (L2) is the spatial GBIM corpus —
> geospatial features embedded for proximity-based retrieval. `gbim_beliefs_v2` (cosine)
> is the production belief embedding corpus — nine-axis text representations optimized
> for semantic similarity. Do not conflate them. Landowner queries bypass both: they
> route via SQL through `jarvis-gbim-query-router` (port 7205) → `mvw_gbim_landowner_spatial`.

> **Landowner beliefs are NOT in ChromaDB.** Landowner queries route exclusively via
> SQL through `jarvis-gbim-query-router` (port 7205) →
> `msjarvisgis.mvw_gbim_landowner_spatial` (container port 5432 on `msjarvis-db`).
> Zero ChromaDB involvement. See Sections 2.12 and 2.13.

### 2.6.2 Community Memory and Autonomous Learning

| Collection | Distance | Count | Role |
|---|---|---|---|
| `autonomous_learner` | cosine | **21,181** | Older corpus; pre-fix history preserved |
| `autonomous_learning` | cosine | **17,685** | Newer corpus; current write path |
| `conversation_history` | cosine | **580** | Wired into main brain after OI-05 fix |
| `ms_allis_memory` | cosine | Active | Persistent cross-session memory |
| `episodic_index` | cosine | Active | Episodic memory index |

Both autonomous learning collections are confirmed distinct with no dedup required — they serve different temporal roles and are intentionally preserved. Combined: **38,866** items of community interaction and research history.

### 2.6.3 Governance and Constitutional Corpus

| Collection | Distance | Count | Notes |
|---|---|---|---|
| `governance_rag` | cosine | **1,367 chunks** | MountainShares DAO Charter + rules; Phase specs; KPI Spec; Safety Champion Protocol; US Constitution (97 chunks); WV Constitution (342 chunks, source label `wv_constitution`) |
| `commons_rag` | cosine | **306 chunks** | Commons governance and gamification corpus |
| `governance` | cosine | Active | WV governance texts |
| `thesis` | cosine | Active | Polymathmatic Geography theoretical framework |
| `mountainshares_knowledge` | cosine | Active | MountainShares DAO economics and governance |

### 2.6.4 Legal, Safety, Economic, and Resource Collections

| Collection | Distance | Count | Notes |
|---|---|---|---|
| `legal_rag` | cosine | **340 chunks** | WV Code and legal texts, rechunked |
| `safety_rules` | cosine | **25** | Six guardrail groups, 15 constitutional principles |
| `economic_rag` | cosine | **72 chunks** | Tax + agriculture law |
| `contracts` | cosine | **673 chunks** | Rechunked |
| `policy_rag` | cosine | 9 | Policy corpus |
| `grants_rag` | cosine | 9 | Grants and funding corpus |
| `meeting_minutes` | cosine | 1 | Governance record |
| `fayette_county_resources_2026` | cosine | **1,205 chunks** | Fayette resource packet — baseline for Phase 1 |
| `wv_resources` | cosine | 8 | Active expansion target through Phase 1 red teaming |
| `local_resources` | cosine | 101 | Active expansion target through Phase 1 red teaming |
| `msallis_docs` | cosine | **4,192** | System docs + resources (April 23, 2026) |

### 2.6.5 Specialized Corpora

| Collection | Distance | Count | Notes |
|---|---|---|---|
| `spiritual_rag` | cosine | Active | Deduplicated; 19,338 duplicate vectors removed March 28, 2026 |
| `psychological_rag` | cosine | **968 documents** | Restored March 28, 2026 |
| `appalachian_cultural_intelligence` | cosine | **820** | Curated Appalachian cultural corpus |
| `aaacpe_corpus` | cosine | **65** | AaaCPE live web scrape (39 sources) |

**Total ChromaDB:** ~6.74M vectors across **48 collections** (mixed L2/cosine; April 17, 2026).

---

## 2.7 Relationship Between GBIM, GeoDB, RAG, and Registries

```
┌─────────────────────────────────────────────────────────────┐
│     GBIM Architecture — April 23, 2026                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  msjarvis-db (host port 5433, container port 5432)          │
│    database: msjarvisgis — 16 GB / 294 tables / 11 schemas  │
│    gbim_worldview_entity — nine-axis JSONB, worldview eq1   │
│    mvw_gbim_landowner_spatial — ✅ 38,979 rows               │
│    gbim_provider_* / gbim_block_* summaries                 │
│    gbim_entities — 4-col application mirror                 │
│    gbim_decay_audit — decay pipeline records                │
│    tiger.* / topology.* — TIGER/Line spatial schemas        │
│          ↓ embedding pipeline (all-minilm:latest, 384-dim)  │
│  ChromaDB (host port 8002) — ~6.74M vectors / 48 collections│
│    gbim_worldview_entities — L2 (spatial corpus)            │
│    gbim_beliefs_v2 — cosine (belief embeddings)             │
│    fayette_county_resources_2026 — 1,205 chunks             │
│    governance_rag — 1,367 chunks                            │
│    [landowner beliefs NOT in ChromaDB]                      │
│          ↓ metadata links (entity_id, local_resource_id)    │
│  jarvis-local-resources-db (port 5435)                      │
│    Verified program records — county, ZIP, type             │
│          ↓ direct SQL (no embeddings)                       │
│  jarvis-gbim-query-router (port 7205)                       │
│    → msjarvisgis.mvw_gbim_landowner_spatial                 │
│    ✅ 38,979 rows — EPSG:4326, GIST index                    │
│    X-Allis-Role: carrie_admin — RBAC gate active            │
│    PostgreSQL-native — ZERO ChromaDB involvement            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

*Figure 2.4. The GBIM architecture as of April 23, 2026. Production database is `msjarvisgis` on `msjarvis-db` (host 5433 / container 5432). Landowner queries bypass ChromaDB entirely and route through `jarvis-gbim-query-router` (port 7205).*

---

## 2.8 The `nbb_pituitary_gland` Governance Module

The `nbb_pituitary_gland` service is a neural-behavioral bridge operating at **`host:8108`** that modulates every Ms. Allis response. It is not optional infrastructure — it is the governance layer that regulates response tone, urgency, and constitutional alignment in real time.

### 2.8.1 Operational State (April 23, 2026)

| Property | Value |
|---|---|
| Host | `host:8108` |
| Current mode | **baseline** |
| Steady-state behavior | Normal governance — standard cortisol, urgency, warmth |
| Five governance protocols | All active |
| Health endpoint | `GET /health` — operational |
| Mode endpoint | `GET /mode` — returns `baseline` |
| Network membership | `qualia-net` + `msallis-rebuild_default` — dual confirmed April 23, 2026 |

**Mode: baseline is the correct steady-state.** `mode: crisis` is a contingency mode that activates during genuine system-wide emergencies — it must not appear in documentation as the normal operating state.

### 2.8.2 Five Governance Protocols

The five active governance protocols modulate:

1. **Cortisol regulation** — urgency calibration; prevents panic-mode responses to routine queries.
2. **Warmth calibration** — community-appropriate tone for Appalachian users; avoids clinical detachment.
3. **Constitutional alignment** — cross-references response framing against WV and US constitutional principles.
4. **Escalation gating** — determines when a response requires elevation to human review.
5. **Ethical brake** — hard stop on responses that cross harm, privacy, or dignity thresholds regardless of other judge scores.

### 2.8.3 Integration with the Judge Pipeline

`nbb_pituitary_gland` operates upstream of the BBB barrier. Before the judge consensus gate evaluates a response, the pituitary module has already modulated the ensemble output's affective register. Judge scores therefore reflect the post-modulation response, not the raw LLM ensemble output. This ordering is intentional: constitutional governance precedes adversarial safety checking.

```python
import httpx

# Check current governance mode
resp = httpx.get("http://host:8108/mode")
# Returns: {"mode": "baseline", "cortisol": ..., "urgency": ..., "warmth": ...}

# Health check
health = httpx.get("http://host:8108/health")
# Returns: {"status": "ok", "protocols_active": 5}
```

---

## 2.9 GBIM Confidence Decay Pipeline

The confidence decay pipeline is a live 24-hour loop monitoring all GBIM entities for temporal staleness and escalating verified-stale entities to the POC (point-of-contact) re-verification workflow.

### 2.9.1 Pipeline Components (All Operational — April 23, 2026)

| Component | Status | Role |
|---|---|---|
| `allis-confidence-decay` | ✅ Running | 24-hour decay loop — applies decay ticks to all entities |
| `allis-decay-escalation-consumer` | ✅ Running | Consumes escalation events; routes to POC workflow |
| `allis-gbim-verifier` | ✅ Running | Polls every 120s; reports totals, stale counts, average decay |
| `confidence_decay_loop.py` | ✅ Deployed | Core decay logic |
| `allis_decay_escalation_consumer.py` | ✅ Deployed | Escalation consumer logic |
| `db/gbim_confidence_decay_schema.sql` | ✅ Deployed | Schema — `gbim_decay_audit` in `msjarvisgis` |
| `scripts/gbim_decay_tick.sh` | ✅ Operational | Manual decay tick trigger |
| `scripts/gbim_decay_refresh.sh` | ✅ Operational | Refresh script |
| `observability/prometheus/alert_confidence_decay_rules.yaml` | ✅ Configured | Prometheus alerting |

### 2.9.2 Decay Behavior

- **Decay interval:** 24 hours.
- **Entities processed:** 461 processed in the first documented decay cycle.
- **`needs_verification = TRUE`** is set when an entity's `confidence_decay` value crosses the configured threshold. This flag drives the POC re-verification loop.
- **"No stale entities" from `allis-gbim-verifier`** is correct behavior — it means no entities have yet crossed the decay threshold, not that the service is inactive.
- **Decay audit records** are written to `msjarvisgis.public.gbim_decay_audit` on `msjarvis-db` for every tick processed.

### 2.9.3 Decay Schema

```sql
-- msjarvisgis.public.gbim_decay_audit
-- Written by confidence_decay_loop.py on each decay tick
-- Access: docker exec msjarvis-db psql -U postgres -d msjarvisgis

SELECT
    entity_id,
    decay_value,
    needs_verification,
    audit_ts
FROM gbim_decay_audit
WHERE needs_verification = TRUE
ORDER BY decay_value DESC
LIMIT 20;
```

---

## 2.10 Truth Judge — Retirement of `heuristic_contradiction_v1`, Promotion of `rag_grounded_v2`

The `heuristic_contradiction_v1` judge is **retired**. All references to it in source files, comments, and documentation are superseded. The canonical truth judge is `rag_grounded_v2`, confirmed operational and DGM-corroborated.

### 2.10.1 What Changed

| Component | Before (retired) | After (current) |
|---|---|---|
| Truth judge implementation | `heuristic_contradiction_v1` — pattern-matching on response text; no DB query | `rag_grounded_v2` — RAG-grounded scoring; DGM-corroborated verdicts |
| Source file | `allis-judge-truth_lm_synthesizer.py` stale comments referencing v1 | All stale `heuristic_contradiction_v1` references updated to `rag_grounded_v2` — verified April 23, 2026 |
| Evidence annotations | None | `[RAG] Grounded:` and `[GBIM]` annotations in judge output — correct behavior showing evidence chain |
| DGM corroboration | Not present | Active — DGM cross-references `rag_grounded_v2` verdicts |

### 2.10.2 Judge Evidence Annotations

The `rag_grounded_v2` truth judge produces inline evidence annotations in its output:

- `[RAG] Grounded: Ms. Allis must prioritize West Virginia community needs...` — drawn from `safety_rules`, `governance_rag`, `legal_rag`, `economic_rag`.
- `[GBIM] Fayette County — Program: UTILITY20 | Active enrollments: 0...` — drawn from live GBIM data via `msjarvisgis`.

These annotations are **correct judge behavior** showing the evidence chain. They must be preserved in internal logs and stripped from user-facing `issues` arrays before returning responses to end users.

### 2.10.3 Judge Pipeline Status (April 23, 2026)

| Judge | Status | Notes |
|---|---|---|
| Truth (`rag_grounded_v2`) | ✅ Canonical | DGM-corroborated; all v1 references retired |
| Ethics | ✅ Operational | Tiered thresholds live; gemma:2b hedge fix deployed |
| Harm/Patterns | ✅ Operational | Six-pattern guardrail groups active |
| Alignment | ✅ Operational | Consensus gate wired into main brain |
| BBB barrier | ✅ Operational | Six filters; 97.8% historical pass rate |
| ML-DSA-65 signatures | ✅ Enforced | All judge outputs signed via `judgesigner` + `liboqs` |
| ONNX caches | ✅ Pre-warmed | No cold-start latency |

---

## 2.11 Ethical Architecture of the Belief Corpus

The nine-axis structure is not value-neutral. Two constraints are enforced at the schema level:

**Constraint 1: Individual residential owner names are excluded from the GBIM belief corpus.**

The `who_axis` of the landowner belief layer contains only institutional and corporate entity names. Individual residential owner names are not ingested into any GBIM belief table, materialized view, ChromaDB collection, or RAG-accessible store. The ingestion pipeline selects only records matching corporate and government entity patterns.

The rationale is the **aggregation problem**: individual owner names are legally public as friction-protected courthouse records. Embedding them into a semantically searchable, spatially indexed, multi-million-parcel AI system converts friction-protected public records into operational surveillance infrastructure.

**Constraint 2: Institutional actors are represented with full accountability metadata.**

The `under_whose_authority_axis` and `on_what_evidence_axis` for all institutional beliefs must include sufficient provenance to allow any displayed belief to be traced back to its source record. Corporate and government landholders are named, counted, and area-summarized with full assessor provenance.

These two constraints define the ethical architecture: **a system that makes power legible without making vulnerability exploitable.**

---

## 2.12 The `jarvis-gbim-query-router` Service — Fully Operational, April 23, 2026

The `jarvis-gbim-query-router` is the GBIM entrypoint for all structured landowner and spatial GBIM queries. It is the only service in the Ms. Allis stack whose exclusive purpose is routing natural-language ownership queries to deterministic SQL results over the verified GBIM parcel corpus.

> **Note on naming:** The container is `jarvis-gbim-query-router` — the `jarvis-` prefix
> is retained in the production stack. The public-facing system name is **Ms. Allis**.

### 2.12.1 Service Specification

| Property | Value |
|---|---|
| Container | `jarvis-gbim-query-router` |
| Host port | **7205** |
| Framework | FastAPI |
| Endpoint | `POST /query` |
| Database target | `msjarvisgis` via `msjarvis-db` (container port 5432) |
| `POSTGRES_HOST` | `msjarvis-db` |
| `POSTGRES_DB` | `msjarvisgis` |
| `POSTGRES_PORT` | `5432` (container-internal) |
| ChromaDB dependency | **None — zero ChromaDB involvement** |
| RBAC gate | `X-Allis-Role: carrie_admin` passes; unauthenticated returns `403 Forbidden for this role` |
| Health endpoint | `GET /health` — returns `{"status": "ok", "type": "gbim"}` |
| Production status | ✅ **Fully operational end-to-end — April 23, 2026** |

### 2.12.2 End-to-End Verification (April 23, 2026)

All five layers confirmed:

- ✅ **RBAC gate** — `carrie_admin` role passes.
- ✅ **DSN** — connecting to `msjarvisgis` on `msjarvis-db`.
- ✅ **Materialized view** — `mvw_gbim_landowner_spatial` — ✅ 38,979 rows in msjarvis-db.
- ✅ **Spatial query** — returning real lat/lon centroids.
- ✅ **Real data** — United States of America (NPS/New River Gorge), American Canadian Expeditions, local landowners all returned. Source attribution: *"WV 2025 Tax Parcel Data — authoritative county assessor records."*

The NPS parcel returned in queries — United States of America, Oak Hill, Land Resources Office address — is the New River Gorge National Park boundary land, confirmed present in the query results for the Mount Hope area. The system is working exactly as designed.

### 2.12.3 Verified Query Pattern

```python
import httpx

# Spatial landowner query with RBAC header
resp = httpx.post(
    "http://127.0.0.1:7205/query",
    headers={"X-Allis-Role": "carrie_admin"},
    json={
        "question": "Who are the largest landowners near Mount Hope?",
        "mode": "landowner_gbim",
        "route_type": "parcel_ownership",
        "county": "Fayette",
        "limit": 20
    }
)
# Returns: owner_name, parcel_id, address, acreage, centroid lat/lon,
#          source: "WV 2025 Tax Parcel Data — authoritative county assessor records"

# Unauthenticated — returns 403
resp_unauth = httpx.post(
    "http://127.0.0.1:7205/query",
    json={"question": "Who owns land near Mount Hope?"}
)
# {"detail": "Forbidden for this role"}
```

---

## 2.13 The `mvw_gbim_landowner_spatial` Materialized View

`mvw_gbim_landowner_spatial` is the canonical spatial GBIM worldview materialization in `msjarvisgis`, derived from `gbim_worldview_entity`, consumed by `jarvis-gbim-query-router`.

### 2.13.1 View Specification

| Property | Value |
|---|---|
| View name | `mvw_gbim_landowner_spatial` |
| View type | Materialized view |
| Container | `msjarvis-db` (host port 5433, container port 5432) |
| Database | `msjarvisgis` |
| Row count | ✅ **38,979 rows in msjarvis-db** (April 23, 2026) |
| Geometry CRS | **EPSG:4326** |
| Spatial index | ✅ GIST on geometry |
| Owner name index | ✅ Fast landowner lookups |
| Source table | `gbim_worldview_entity` |
| Production status | ✅ **Fully operational — April 23, 2026 (OI-E CLOSED)** |

### 2.13.2 View Definition

```sql
-- msjarvisgis.public.mvw_gbim_landowner_spatial
-- Materialized view derived from gbim_worldview_entity
-- Access: docker exec msjarvis-db psql -U postgres -d msjarvisgis
-- Forensic access: docker exec postgis-forensic psql -h 127.0.0.1 -U jarvis -d msjarvisgis

SELECT
    id,
    worldview_id,
    entity_type,
    source_table,
    source_pk,
    label                                                        AS display_name,
    created_at,
    ((belief_state->'spatialmetadata')->>'centroidx')::double precision AS centroid_x,
    ((belief_state->'spatialmetadata')->>'centroidy')::double precision AS centroid_y,
    ((belief_state->'spatialmetadata')->>'srid')::integer               AS srid,
    belief_state->>'entity_type'                                 AS belief_entity_type,
    belief_state->>'display_name'                                AS belief_display_name,
    belief_state->>'source_dataset'                              AS source_dataset,
    (belief_state->'axes')->>'what'                              AS what,
    ((belief_state->'axes')->'where')->>'county'                 AS county,
    ((belief_state->'axes')->'where')->>'state'                  AS state
FROM gbim_worldview_entity e
WHERE ((belief_state->'spatialmetadata')->>'centroidx') IS NOT NULL;
```

### 2.13.3 Indexes

Three clean indexes, no redundancy:

| Index | Type | Purpose |
|---|---|---|
| `landowner_assessor_parcels_pkey` | B-tree | Row ID — primary key |
| `idx_landowner_parcels_geom` | GIST | Spatial queries — geometry column |
| `idx_landowner_owner_name` | B-tree | Owner name lookups |

### 2.13.4 Confirmed Data (April 23, 2026)

- ✅ **38,979 rows in msjarvis-db** — OI-E CLOSED.
- ✅ All rows with geometry; 536 unattributed (roads/easements) — normal.
- ✅ Mount Hope / New River Gorge area confirmed present.
- ✅ City of Mount Hope, CSX, local landowners all present.
- ✅ NPS (United States of America) New River Gorge National Park boundary parcel confirmed.
- ✅ `msjarvis-db` accessible to Docker containers via internal network.
- ⚠️ `mvw_gbim_landowner_spatial` not present in `postgis-forensic` — production view only.

### 2.13.5 Refresh and Maintenance

```sql
-- Non-blocking refresh (requires unique index)
-- Run via: docker exec msjarvis-db psql -U postgres -d msjarvisgis
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_gbim_landowner_spatial;

-- Blocking refresh (schedule during low-traffic window if no unique index)
REFRESH MATERIALIZED VIEW mvw_gbim_landowner_spatial;
```

---

## 2.14 Production Status Summary — April 23, 2026

| Component | Status | Notes |
|---|---|---|
| `msjarvis-db` (host 5433 / container 5432) | ✅ Operational | 16 GB / 294 tables / 11 schemas; database: `msjarvisgis` |
| `postgis-forensic` | ✅ Recovered | April 23, 2026 — ExitCode 255 was ungraceful stop; `docker start` confirmed Up. Access: `docker exec postgis-forensic psql -h 127.0.0.1 -U jarvis -d msjarvisgis` |
| `msallisgis` / port `5452` / `gisdb` | ❌ Retired | These names and ports do not exist — all references invalid |
| `gbim_worldview_entity` (msjarvisgis) | ✅ Present | Full spatial table — nine-axis JSONB, worldview eq1 |
| `gbim_beliefs` (bare) | ❌ Retired | Replaced by `gbim_worldview_entities` (ChromaDB, L2) and `gbim_beliefs_v2` (ChromaDB, cosine) |
| `gbim_worldview_entities` (ChromaDB) | ✅ **L2 distance** | Spatial GBIM corpus |
| `gbim_beliefs_v2` (ChromaDB) | ✅ **cosine distance** | Production belief embeddings — separate from spatial corpus |
| `gbim_entities` (msjarvisgis) | ✅ Present | 4-column application mirror |
| `mvw_gbim_landowner_spatial` | ✅ **38,979 rows in msjarvis-db** | OI-E CLOSED — April 23, 2026; not present in postgis-forensic |
| TIGER/topology schemas | ✅ In `msjarvisgis` | `tiger.addr`, `tiger.edges`, `tiger.zcta5`, etc. |
| `nbb_pituitary_gland` (host:8108) | ✅ **mode: baseline** | Five governance protocols active; dual-network confirmed April 23, 2026 |
| Confidence decay pipeline | ✅ Operational | 3 containers + schema + scripts + Prometheus alerting |
| `jarvis-gbim-query-router` (port 7205) | ✅ **End-to-end operational** | RBAC, DSN, mat. view, spatial query, real data all verified April 23, 2026 |
| Truth judge | ✅ `rag_grounded_v2` | `heuristic_contradiction_v1` retired; DGM-corroborated |
| ChromaDB (port 8002) | ✅ **48 collections, ~6.74M vectors** | v2 API only (`/api/v1/` → 410 Gone); mixed L2/cosine; April 17, 2026 |
| ChromaDB count pattern | ✅ UUID two-step | Name → UUID → count; direct name count unreliable in v2 |
| `fayette_county_resources_2026` | ✅ **1,205 chunks** | Baseline; ongoing expansion through Phase 1 |
| `wv_resources` / `local_resources` | 🔄 Expanding | 8 / 101 items; active Phase 1 red teaming targets |
| Autonomous learning collections | ✅ **21,181 + 17,685** | Both preserved; distinct temporal roles confirmed |
| Container count | ✅ **112 thesis-verified (April 16) / 100 point-in-time (April 23)** | `msallis-rebuild` namespace |
| Container naming | ℹ️ `jarvis-` prefix retained | Public name is Ms. Allis |

---

*Chapter 2 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: April 23, 2026 — `msjarvis-db` (host 5433 / container 5432) authoritative;
`msjarvisgis` database confirmed; 16 GB / 294 tables / 11 schemas;
`postgis-forensic` recovered (ExitCode 255 — ungraceful stop);
`gbim_worldview_entities` (L2) + `gbim_beliefs_v2` (cosine) confirmed distinct collections;
`mvw_gbim_landowner_spatial` ✅ 38,979 rows in msjarvis-db (OI-E CLOSED);
`jarvis-gbim-query-router` port 7205 fully operational end-to-end;
ChromaDB v2 only — /api/v1/ returns 410; UUID two-step count pattern required;
48 collections / ~6.74M vectors / mixed L2-cosine;
`nbb_pituitary_gland` baseline mode / dual-network confirmed;
112 containers thesis-verified (April 16) / 100 point-in-time (April 23).*
