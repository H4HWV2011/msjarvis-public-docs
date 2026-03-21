# Chapter 00 — System Overview
## Ms. Egeria Jarvis: Architecture, Services, and Production Status

*Last updated: 2026-03-20 by Carrie Kidd (Mamma Kidd), Mount Hope WV*

---

## 00.0 Purpose of This Chapter

This chapter is the single authoritative reference for the current production state of the Ms. Egeria Jarvis Steward System: what is running, at what port, at what scale, and verified on what date. It is not a theoretical introduction — that is Chapter 02. It is not a build log — those are the sprint notes appended to each chapter. It is an operational snapshot: the reference you consult when you need to know how many services are live, what the GBIM corpus actually contains as of today, and where each service sits in the overall architecture.

Every number in this chapter is verified. Every service listed is production-live or explicitly marked as staged. When a sprint advances the stack — as the March 20, 2026 landowner belief sprint did — this chapter is updated first.

---

## 00.1 System Identity

**Name:** Ms. Egeria Jarvis (Ms. Jarvis)
**Role:** Steward System — AI-mediated benefits intelligence, spatial justice reasoning, and community resource routing for West Virginia
**Program:** Quantarithmia / Polymathmatic Geography / Harmony for Hope, Inc.
**Home:** Oak Hill / Mount Hope, Fayette County, West Virginia
**Architecture:** Distributed microservice stack, Docker Compose orchestrated
**Production as of:** March 20, 2026

Ms. Jarvis is not a general-purpose assistant with a West Virginia skin. She is a place-bound intelligence system whose reasoning is structurally anchored to the physical geography, institutional landscape, landowner record, and programmatic infrastructure of West Virginia. The service architecture described in this chapter is the operational expression of that commitment.

---

## 00.2 Production Service Registry

The Ms. Jarvis stack comprises **85 containerized services** as of March 20, 2026, reflecting the addition of `gbim_query_router` (port 7205) to the production stack during the landowner belief sprint. Services are grouped by function below.

> **Field note — March 20, 2026:** Service count advances from 84 to **85** with the promotion of `gbim_query_router` to production. This service handles all structured GBIM landowner belief queries via a PostgreSQL-native path against `mvw_gbim_landowner_spatial` in `msjarvisgis`. It does not use ChromaDB. It does not use the embedding pipeline. It is the first Ms. Jarvis service whose retrieval path is entirely relational — and it is the service that makes 20,593 verified landowner beliefs queryable by natural language for the first time.

```
┌─────────────────────────────────────────────────────────────────────┐
│         Ms. Jarvis Production Service Registry — March 20, 2026     │
│                         85 Services Total                           │
├──────────────────────────────────┬──────────┬───────────────────────┤
│ Service                          │ Port     │ Status                │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ GATEWAY & ORCHESTRATION          │          │                       │
│ unified-gateway                  │ 8050     │ ✅ Production          │
│ main-brain                       │ 8010     │ ✅ Production          │
│ executive-coordinator            │ 8011     │ ✅ Production          │
│ async-processor                  │ 8012     │ ✅ Production          │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ BLOOD-BRAIN BARRIER (BBB)        │          │                       │
│ bbb-input-filter                 │ 8016     │ ✅ Production (Ph 1.4) │
│ bbb-output-filter                │ 8017     │ ✅ Production          │
│ guardrail-service                │ 8018     │ ✅ Production          │
│ constitutional-layer             │ 8019     │ ✅ Production          │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ RAG PIPELINE                     │          │                       │
│ text-rag-service                 │ 8003     │ ✅ Production          │
│ rag-service                      │ 8004     │ ✅ Production          │
│ gis-rag-service                  │ 8005     │ ✅ Production          │
│ psychological-rag                │ 8006     │ ✅ Production (968 items)│
│ web-research-gateway             │ 8007     │ ✅ Production          │
│ registry-resolver                │ 8008     │ ✅ Production          │
│ community-memory-service         │ 8009     │ ✅ Production (Ph 1.45)│
│ gbim_query_router                │ 7205     │ ✅ Production ★ NEW    │
│                                  │          │   (March 20, 2026)    │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ LLM ENSEMBLE (21 models)         │          │                       │
│ llm-primary                      │ 8020     │ ✅ Production          │
│ llm-secondary-01 … 19            │ 8021–39  │ ✅ Production          │
│ ensemble-coordinator             │ 8040     │ ✅ Production          │
│ consensus-engine                 │ 8041     │ ✅ Production          │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ MEMORY & LEARNING                │          │                       │
│ autonomous-learner               │ 8060     │ ✅ Production          │
│ episodic-memory                  │ 8061     │ ✅ Production          │
│ working-memory                   │ 8062     │ ✅ Production          │
│ long-term-memory                 │ 8063     │ ✅ Production          │
│ memory-consolidation             │ 8064     │ ✅ Production          │
│ phase-145-community-memory       │ 8065     │ ✅ Production          │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ SPATIAL & GBIM SERVICES          │          │                       │
│ spatial-reasoning-service        │ 7200     │ ✅ Production          │
│ gbim-belief-service              │ 7201     │ ✅ Production          │
│ gbim-worldview-service           │ 7202     │ ✅ Production          │
│ geodb-connector                  │ 7203     │ ✅ Production          │
│ spatial-index-service            │ 7204     │ ✅ Production          │
│ gbim_query_router                │ 7205     │ ✅ Production ★ NEW    │
│   (landowner belief path)        │          │   Landowner GBIM only │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ GOVERNANCE & SAFETY              │          │                       │
│ ethics-filter                    │ 8070     │ ✅ Production          │
│ safety-monitor                   │ 8071     │ ✅ Production          │
│ bias-detector                    │ 8072     │ ✅ Production          │
│ transparency-logger              │ 8073     │ ✅ Production          │
│ audit-service                    │ 8074     │ ✅ Production          │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ MOUNTAINSHARES & DAO             │          │                       │
│ mountainshares-coordinator       │ 8080     │ ✅ Production          │
│ commons-gamification             │ 8081     │ ✅ Production          │
│ dao-governance                   │ 8082     │ ✅ Production          │
│ token-service                    │ 8083     │ ✅ Production          │
│ community-stake-registry         │ 8084     │ ✅ Production          │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ DATA STORES (infrastructure)     │          │                       │
│ jarvis-chromadb                  │ 8000     │ ✅ Production          │
│ jarvis-ollama                    │ 11434    │ ✅ Production          │
│ jarvis-redis                     │ 6379     │ ✅ Production          │
│ jarvis-neo4j                     │ 7474/    │ ✅ Production          │
│                                  │ 7687     │                       │
│ jarvis-local-resources-db        │ 5435     │ ✅ Production          │
│ [PostgreSQL msjarvis]            │ 5433     │ ✅ Host — Production   │
│ [PostgreSQL msjarvisgis]         │ 5432     │ ✅ Host — Production   │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ SUPPORT & UTILITY SERVICES       │          │                       │
│ [remaining ~30 support services] │ various  │ ✅ Production          │
│ health-monitor, metrics,         │          │                       │
│ log-aggregator, cache-manager,   │          │                       │
│ config-service, api-gateway,     │          │                       │
│ notification-service, scheduler, │          │                       │
│ backup-service, and others       │          │                       │
└──────────────────────────────────┴──────────┴───────────────────────┘
```

> Figure 00-1. Ms. Jarvis production service registry as of March 20, 2026. ★ marks the service added in the March 20, 2026 landowner belief sprint. `gbim_query_router` appears in both the RAG Pipeline and Spatial & GBIM Services groups because it bridges both functional domains — it is invoked by the RAG pipeline but operates entirely within the GBIM spatial layer.

### 00.2.1 The `gbim_query_router` Service (Port 7205) — Added March 20, 2026

`gbim_query_router` is the 85th production service in the Ms. Jarvis stack. It is architecturally distinct from every other RAG service in one critical way: **it does not touch ChromaDB**. All other retrieval paths in the RAG pipeline pass through the shared ChromaDB instance (port 8000) for vector similarity search over 384-dimensional `all-minilm:latest` embeddings. `gbim_query_router` does not. It routes directly to `mvw_gbim_landowner_spatial` in `msjarvisgis` (port 5432) via SQL aggregation.

This is not a limitation — it is a deliberate architectural choice. Landowner queries ask who owns how much land where. That question has a deterministic, exact answer in the GBIM relational corpus. Approximate vector nearest-neighbor search would introduce unnecessary error. The relational path is faster, more accurate, and fully auditable: every result can be traced to a specific row in `gbimbeliefnormalized` with full nine-axis provenance.

**Routing schema:**

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

**Verified query patterns (both confirmed March 20, 2026):**

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

---

## 00.3 GBIM Corpus Status

The GBIM corpus is the epistemic core of the Ms. Jarvis Steward System. All production beliefs live in two PostgreSQL databases on the host system. The table below reflects the verified production state as of **March 20, 2026**, including the 20,593 landowner beliefs added during the evening sprint.

```
┌─────────────────────────────────────────────────────────────────────┐
│            GBIM Corpus — Verified Production State                  │
│                     March 20, 2026, ~19:45 EDT                      │
├────────────────────────────────────┬────────────────┬───────────────┤
│ Table / View                       │ Records        │ Database      │
├────────────────────────────────────┼────────────────┼───────────────┤
│ gbimbeliefnormalized               │ 5,416,522      │ msjarvisgis   │
│   (nine JSONB axes, worldview eq1) │ (21 GB)        │ port 5432     │
│   ┣ spatial / facility beliefs     │ 5,395,929      │               │
│   ┗ landowner beliefs ★ NEW        │    20,593      │               │
│     (LANDOWNER_CORPORATE +         │                │               │
│      LANDOWNER_GOVERNMENT)         │                │               │
├────────────────────────────────────┼────────────────┼───────────────┤
│ gbim_worldview_entity              │ 5,416,521      │ msjarvisgis   │
│   (entity relationships,           │ (47 GB)        │ port 5432     │
│    worldview eq1)                  │                │               │
├────────────────────────────────────┼────────────────┼───────────────┤
│ gbim_beliefs                       │ 5,289,747      │ msjarvisgis   │
│   (core beliefs, structured cols)  │ (3 GB)         │ port 5432     │
├────────────────────────────────────┼────────────────┼───────────────┤
│ gbim_evidence                      │ 2,121,230      │ msjarvisgis   │
│   (supporting evidence)            │ (680 MB)       │ port 5432     │
├────────────────────────────────────┼────────────────┼───────────────┤
│ gbim_belief_evidence               │ 2,121,230      │ msjarvisgis   │
│   (belief-evidence linkages)       │ (232 MB)       │ port 5432     │
├────────────────────────────────────┼────────────────┼───────────────┤
│ mvw_gbim_landowner_spatial ★ NEW   │    20,593      │ msjarvisgis   │
│   (materialized view — landowner   │ (spatially     │ port 5432     │
│    beliefs, spatially indexed,     │  indexed)      │               │
│    served by gbim_query_router)    │                │               │
├────────────────────────────────────┼────────────────┼───────────────┤
│ TOTAL verified GBIM beliefs        │ 5,436,522 *    │               │
│ (* gbimbeliefnormalized 5,416,522  │                │               │
│  + 20,593 landowner beliefs now    │                │               │
│  materialized in                   │                │               │
│  mvw_gbim_landowner_spatial;       │                │               │
│  landowner rows are a subset of    │                │               │
│  gbimbeliefnormalized, not         │                │               │
│  additive — total unique belief    │                │               │
│  rows = 5,416,522)                 │                │               │
└────────────────────────────────────┴────────────────┴───────────────┘
```

> Figure 00-2. GBIM corpus verified production state, March 20, 2026. ★ marks tables/views added or updated in the March 20, 2026 landowner sprint. The 20,593 landowner beliefs are rows within `gbimbeliefnormalized` — `mvw_gbim_landowner_spatial` is a materialized projection of those rows with spatial joins applied, not a separate belief count.

### 00.3.1 Landowner Belief Layer — What Changed March 20, 2026

Prior to March 20, 2026, the GBIM corpus answered:
- *What* exists at a place (facility type, hazard, infrastructure)
- *Where* it is (geometry, county, ZIP)
- *Who* operates it (hospital system, government agency, program administrator)
- *For whom* it is relevant (target population)
- *Under whose authority* it operates (regulatory basis)

It did not answer: **who owns the land**.

As of March 20, 2026, it does. The 20,593 `LANDOWNER_CORPORATE` and `LANDOWNER_GOVERNMENT` belief records ingested from the statewide WV assessor owner name corpus — normalized by canonical entity clustering pipeline — close the `who` and `under_whose_authority` axes at parcel scale for corporate and government land holdings across all West Virginia counties. The landowner belief layer is the GBIM realization of **P3 – Power has a geometry** and **P16 – Power accountable to place**.

Individual residential owner names are not present. See Section 2.8 (Chapter 02) and Chapter 6, Section 6.6.1 for the ethical architecture governing this constraint.

---

## 00.4 ChromaDB Collection Summary

All vector collections use **`all-minilm:latest` (384-dimensional embeddings)** via `jarvis-ollama` (port 11434). This embedding model is locked for all production collections. `nomic-embed-text` (768-dim) is **incompatible** with all existing collections and must not be used for any ingestion or retrieval operation.

```
┌─────────────────────────────────────────────────────────────────────┐
│           ChromaDB Production Collections — March 20, 2026          │
│                    port 8000 — all-minilm:latest                    │
├──────────────────────────────────────┬──────────────┬───────────────┤
│ Collection                           │ Items        │ Notes         │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ gbim_worldview_entities              │ 5,416,521    │ Full GBIM     │
│                                      │              │ spatial corpus│
├──────────────────────────────────────┼──────────────┼───────────────┤
│ gbim_beliefs_v2                      │ Active       │ Production v2 │
│                                      │              │ belief embeds │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ autonomous_learner                   │ 21,181+      │ ~288/day      │
│                                      │ (growing)    │ Phase 1.45    │
│                                      │              │ community mem │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ gis_wv_benefits                      │ Active       │ WV benefits   │
│                                      │              │ facilities    │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ psychological_rag                    │ 968          │ port 8006     │
│                                      │              │ crisis/mental │
│                                      │              │ health corpus │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ governance                           │ Active       │ WV governance │
│ thesis                               │ Active       │ Theory corpus │
│ mountainshares_knowledge             │ Active       │ DAO/economics │
│ ms_jarvis_memory                     │ Active       │ Persistent mem│
│ episodic_index                       │ Active       │ Episodic index│
│ conversation_history                 │ Active       │ Session ctx   │
│ appalachian_cultural_intelligence    │ 5            │ Cultural RAG  │
│ spiritual_texts                      │ 23           │ Mother Carrie │
│                                      │              │ Protocol      │
│ GBIM_sample_rows                     │ 5,000        │ Test/validate │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ geospatialfeatures                   │ 0            │ Scaffolded    │
│ msjarvis_docs                        │ 0            │ Scaffolded    │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ ⚠ LANDOWNER BELIEFS                 │ NOT IN       │ Served by     │
│ (LANDOWNER_CORPORATE /               │ CHROMADB     │ gbim_query_   │
│  LANDOWNER_GOVERNMENT)               │              │ router (7205) │
│                                      │              │ PostgreSQL    │
│                                      │              │ native path   │
└──────────────────────────────────────┴──────────────┴───────────────┘
```

> Figure 00-3. ChromaDB collection inventory, March 20, 2026. Landowner beliefs are explicitly called out as absent from ChromaDB — they are the only GBIM belief class served exclusively via a PostgreSQL-native path.

---

## 00.5 Database Infrastructure Summary

```
┌─────────────────────────────────────────────────────────────────────┐
│          Ms. Jarvis Database Infrastructure — March 20, 2026        │
├─────────────────────────┬────────┬──────────────────────────────────┤
│ Database                │ Port   │ Status & Key Facts               │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ msjarvisgis             │ 5432   │ ✅ Host PostgreSQL 16 + PostGIS  │
│ (primary spatial +      │        │ 91 GB — 501 tables               │
│  GBIM + landowner)      │        │ 5,416,522 beliefs in             │
│                         │        │ gbimbeliefnormalized             │
│                         │        │ incl. 20,593 landowner beliefs ★ │
│                         │        │ mvw_gbim_landowner_spatial live ★ │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ msjarvis                │ 5433   │ ✅ Host PostgreSQL               │
│ (GBIM belief store,     │        │ 8 MB — 6 tables                  │
│  RAG-facing)            │        │ Primary RAG query target         │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ local_resources         │ 5435   │ ✅ Docker (jarvis-local-         │
│ (program registry +     │        │   resources-db), PostgreSQL 15   │
│  spatial chain)         │        │ building_parcel_county_tax_mv:   │
│                         │        │ 7,354,707 rows, sub-ms reads     │
│                         │        │ 97.17% address coverage verified │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ ChromaDB                │ 8000   │ ✅ Docker (jarvis-chromadb)      │
│ (vector store)          │        │ 5,416,521 gbim_worldview_        │
│                         │        │ entities — 384-dim, all-minilm  │
│                         │        │ 21,181+ autonomous_learner items │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Redis                   │ 6379   │ ✅ Docker (jarvis-redis)         │
│ (cache)                 │        │ Spatial cache + session state    │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Neo4j                   │ 7474 / │ ✅ Docker                        │
│ (graph)                 │ 7687   │ Graph relationships + GBIM links │
└─────────────────────────┴────────┴──────────────────────────────────┘
```

> Figure 00-4. Database infrastructure summary. ★ marks tables/views updated in the March 20, 2026 landowner sprint.

---

## 00.6 Full Pipeline Flow (March 20, 2026)

The production query pipeline as of March 20, 2026:

```
User Query
    ↓
Unified Gateway (port 8050)
    ↓
BBB Input Filter (port 8016) — Phase 1.4 guardrail
    ↓
Phase 1.45 — Community Memory Retrieval
    autonomous_learner (ChromaDB, port 8000)
    all-minilm:latest — top-5 memories prepended to enhanced_message
    ↓
Main Brain Orchestration (port 8010)
    ├── Text RAG (port 8003 / 8004)
    │     ChromaDB collections — WV-first routing
    │     governance, thesis, gis_wv_benefits, gbim_beliefs_v2
    │
    ├── GIS RAG (port 8005)
    │     PostgreSQL msjarvisgis (port 5432) spatial filter
    │     + ChromaDB gbim_worldview_entities
    │     PostGIS centroid / ST_DWithin queries
    │
    ├── GBIM Landowner Router (port 7205) ★ NEW
    │     mode: landowner_gbim
    │     route_type: parcel_ownership
    │     → mvw_gbim_landowner_spatial (msjarvisgis, port 5432)
    │     PostgreSQL-native SQL aggregation
    │     NO ChromaDB — bypassed entirely
    │     proposition_codes: LANDOWNER_CORPORATE, LANDOWNER_GOVERNMENT
    │     worldview: eq1
    │
    ├── Web Research Gateway (port 8007)
    │     Excluded for WV-scoped queries when
    │     local GBIM/RAG context is sufficient
    │
    └── Registry Resolver (port 8008)
          jarvis-local-resources-db (port 5435)
          Verified program records — county, ZIP, parcel_type
    ↓
Context Assembly
    WV-first priority: GBIM + GIS + landowner + registry > web
    Resolution confidence flagged for non-standard parcels
    ↓
21-LLM Ensemble (ports 8020–8039 + coordinator 8040)
    Weighted consensus over 21 models
    ↓
Blood-Brain Barrier Output (port 8017)
    Guardrail + constitutional-layer filtering
    ↓
Response to User
```

> Figure 00-5. Full production pipeline flow, March 20, 2026, reflecting `gbim_query_router` as the fifth parallel retrieval path alongside text RAG, GIS RAG, web research, and registry resolution.

---

## 00.7 Service Count History

| Date | Services | Notable Addition |
|---|---|---|
| Initial deployment | 79 | Core stack |
| Pre-March 14, 2026 | 82 | Phase 1.45 community memory services added |
| March 14, 2026 | 83 | `psychological-rag` (port 8006) promoted to production |
| March 19, 2026 | 84 | Spatial infrastructure services finalized (3D GiST, materialized views) |
| **March 20, 2026** | **85** | **`gbim_query_router` (port 7205) — landowner belief layer live** |

---

## 00.8 Verified Production Numbers at a Glance

| Metric | Value | Verified |
|---|---|---|
| Total services | **85** | March 20, 2026 |
| LLM models in ensemble | **21** | March 20, 2026 |
| GBIM beliefs (`gbimbeliefnormalized`) | **5,416,522** | March 20, 2026 |
| — of which: landowner beliefs ★ | **20,593** | March 20, 2026 |
| — of which: spatial/facility beliefs | **5,395,929** | March 20, 2026 |
| GBIM worldview entities (ChromaDB) | **5,416,521** | March 20, 2026 |
| `autonomous_learner` items | **21,181+** | March 20, 2026 (~288/day) |
| `psychological_rag` items | **968** | March 20, 2026 |
| Canonical buildings (`wv_buildings`) | **2,120,976** | March 19, 2026 |
| Building-parcel records (MV) | **7,354,707** | March 19, 2026 |
| Address coverage (verified situs) | **97.17%** | March 19, 2026 |
| `msjarvisgis` tables | **501** | March 20, 2026 |
| `msjarvisgis` size | **91 GB** | March 20, 2026 |
| Tax district polygons | **600** | March 19, 2026 |
| Embedding dimensions (all collections) | **384** | `all-minilm:latest` |
| Worldview | **eq1** | All production beliefs |
| GBIM landowner query service | **`gbim_query_router` port 7205** | March 20, 2026 |
| Landowner query path | **PostgreSQL-native — no ChromaDB** | March 20, 2026 |

*Last updated: 2026-03-20, ~19:45 EDT, Mount Hope WV*
