# Chapter 00 — System Overview
## Ms. Egeria Jarvis: Architecture, Services, and Production Status

*Last updated: 2026-03-22 by Carrie Kidd (Mamma Kidd), Mount Hope WV*

---

## 00.0 Purpose of This Chapter

This chapter is the single authoritative reference for the current production state of the Ms. Egeria Jarvis Steward System: what is running, at what port, at what scale, and verified on what date. It is not a theoretical introduction — that is Chapter 02. It is not a build log — those are the sprint notes appended to each chapter. It is an operational snapshot: the reference you consult when you need to know how many services are live, what the GBIM corpus actually contains as of today, and where each service sits in the overall architecture.

Every number in this chapter is verified. Every service listed is production-live or explicitly marked as staged. When a sprint advances the stack — as the March 20, 2026 landowner belief sprint and the March 22, 2026 red team hardening sprint did — this chapter is updated first.

---

## 00.1 System Identity

**Name:** Ms. Egeria Jarvis (Ms. Jarvis)
**Role:** Steward System — AI-mediated benefits intelligence, spatial justice reasoning, and community resource routing for West Virginia
**Program:** Quantarithmia / Polymathmatic Geography / Harmony for Hope, Inc.
**Home:** Oak Hill / Mount Hope, Fayette County, West Virginia
**Architecture:** Distributed microservice stack, Docker Compose orchestrated + 3 external systemd services
**Production as of:** March 22, 2026
**Public URL:** https://egeria.mountainshares.us (confirmed live March 22, 2026)

Ms. Jarvis is not a general-purpose assistant with a West Virginia skin. She is a place-bound intelligence system whose reasoning is structurally anchored to the physical geography, institutional landscape, landowner record, and programmatic infrastructure of West Virginia. The service architecture described in this chapter is the operational expression of that commitment.

---

## 00.2 Production Service Registry

The Ms. Jarvis stack comprises **83 Docker Compose–managed services** plus **3 external systemd services** as of March 22, 2026.

> **Field note — March 20, 2026:** `gbim_query_router` (port 7205) promoted to production. This service handles all structured GBIM landowner belief queries via a PostgreSQL-native path against `mvw_gbim_landowner_spatial` in `msjarvisgis`. It does not use ChromaDB. It does not use the embedding pipeline. It is the first Ms. Jarvis service whose retrieval path is entirely relational — and it makes 20,593 verified landowner beliefs queryable by natural language for the first time.

> **Field note — March 21–22, 2026:** Three containers (`jarvis-crypto-policy`, `jarvis-ingest-api`, `jarvis-ingest-watcher`) were previously running as orphaned `docker run` instances not defined in `docker-compose.yml`. They have been added to `docker-compose.yml` with `restart: unless-stopped` and are now compose-managed. Verified production Docker Compose count: **83**.

> **Field note — March 22, 2026 (hardening sprint):** Three external services added as systemd units — they are not part of Docker Compose and are not counted in the 83: `caddy.service` (port 8443), `jarvis-auth.service` (port 8055), `cloudflared.service` (Cloudflare Tunnel). All auto-start on boot independently of Docker Compose.

```
┌─────────────────────────────────────────────────────────────────────┐
│         Ms. Jarvis Production Service Registry — March 22, 2026     │
│              83 Docker Compose Services + 3 systemd                 │
├──────────────────────────────────┬──────────┬───────────────────────┤
│ Service                          │ Port     │ Status                │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ EXTERNAL ACCESS (systemd — not Docker Compose)                      │
│ cloudflared (Cloudflare Tunnel)  │ —        │ ✅ systemd — QUIC     │
│   tunnel: msjarvis               │          │   egeria.mountain-    │
│   UUID: 42ef9893-…               │          │   shares.us live      │
│ caddy (reverse proxy)            │ 8443     │ ✅ systemd — v2.6.2   │
│   /etc/caddy/Caddyfile           │          │   Ubuntu pkg — CORS   │
│   ⚠ No forward_auth             │          │   active; no xcaddy;  │
│   ⚠ No caddy-ratelimit          │          │   no per-IP rate limit│
│ jarvis-auth-service              │ 8055     │ ✅ systemd — FastAPI  │
│   scripts/jarvis_auth_service.py │          │   token validation    │
│   /etc/systemd/system/           │          │   Redis 6380 — 30-day │
│   jarvis-auth.service            │          │   TTL; UI-initiated   │
│                                  │          │   only (not enforced  │
│                                  │          │   at proxy layer ⚠)  │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ GATEWAY & ORCHESTRATION          │          │                       │
│ unified-gateway                  │ 8050     │ ✅ Production          │
│ main-brain                       │ 8010     │ ✅ Production          │
│ executive-coordinator            │ 8011     │ ✅ Production          │
│ async-processor                  │ 8012     │ ✅ Production          │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ BLOOD-BRAIN BARRIER (BBB)        │          │                       │
│ jarvis-blood-brain-barrier       │ 8016     │ ✅ Production          │
│   Phase 1.4 input filter:        │          │   INPUT: blocking ✅  │
│   ACTIVE — blocking              │          │   OUTPUT (Ph 4.5):    │
│   Phase 4.5 output filter:       │          │   log+passthrough ⚠  │
│   LOG+PASSTHROUGH (not blocking) │          │   commit 18b8ddac     │
│                                  │          │   was 31% false-pos.  │
│ ⛔ bbb-output-filter (port 8017) │ 8017     │ ❌ DOES NOT EXIST     │
│   THIS CONTAINER IS NOT RUNNING  │          │   Port 8016 handles   │
│   and never existed in verified  │          │   both input AND      │
│   production stack               │          │   output filtering    │
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
│ gbim_query_router                │ 7205     │ ✅ Production ★        │
│                                  │          │   (March 20, 2026)    │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ LLM ENSEMBLE (21 models)         │          │                       │
│ llm-proxy-01 … 21                │8201–8222 │ ✅ Production          │
│   (verified port range:          │          │   21/21 responded     │
│    8201–8222, NOT 8020–8039)     │          │   within budget       │
│ ensemble-coordinator             │ 8040     │ ✅ Production          │
│ consensus-engine                 │ 8041     │ ✅ Production          │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ LM SYNTHESIZER                   │          │                       │
│ lm-synthesizer                   │ 8001     │ ✅ Production          │
│   (internal port — Phase 3.5)    │          │   Identity guard +    │
│                                  │          │   meta-commentary     │
│                                  │          │   prohibition active  │
│                                  │          │   commits 9ab770e9 +  │
│                                  │          │   211056e6            │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ JUDGE PIPELINE                   │          │                       │
│ jarvis-judge-truth               │ 7230     │ ✅ Production          │
│ jarvis-judge-consistency         │ 7231     │ ✅ Production          │
│ jarvis-judge-alignment           │ 7232     │ ✅ Production          │
│ jarvis-judge-ethics              │ 7233     │ ✅ Production          │
│ jarvis-judge-pipeline            │ internal │ ✅ Production          │
│ jarvis-69dgm-bridge              │ 9000     │ ✅ Production          │
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
│ gbim_query_router                │ 7205     │ ✅ Production ★        │
│   (landowner belief path)        │          │   Landowner GBIM only │
│                                  │          │   PostgreSQL-native   │
│                                  │          │   NO ChromaDB         │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ GOVERNANCE & SAFETY              │          │                       │
│ ethics-filter                    │ 8070     │ ✅ Production          │
│ safety-monitor                   │ 8071     │ ✅ Production          │
│ bias-detector                    │ 8072     │ ✅ Production          │
│ transparency-logger              │ 8073     │ ✅ Production          │
│ audit-service                    │ 8074     │ ✅ Production          │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ MOUNTAINSHARES & DAO             │          │                       │
│ mountainshares-coordinator       │ 8080     │ ❌ NOT DEPLOYED        │
│ commons-gamification             │ 8081     │ ❌ NOT DEPLOYED        │
│ dao-governance                   │ 8082     │ ❌ NOT DEPLOYED        │
│ token-service                    │ 8083     │ ❌ NOT DEPLOYED        │
│ community-stake-registry         │ 8084     │ ❌ NOT DEPLOYED        │
│   ALL ports 8080–8084 return     │          │   HTTP 000 — not in   │
│   HTTP 000. Not in compose stack.│          │   current stack.      │
│   Do not mark as Production.     │          │   Planned future work.│
├──────────────────────────────────┼──────────┼───────────────────────┤
│ DATA STORES (infrastructure)     │          │                       │
│ jarvis-chromadb                  │ 8002     │ ✅ Production          │
│   host port 8002 →               │ (host)   │   container-internal  │
│   container-internal 8000        │          │   8000                │
│ jarvis-ollama                    │ 11434    │ ✅ Production          │
│ jarvis-redis                     │ 6380     │ ✅ Production          │
│   host port 6380 →               │ (host)   │   container-internal  │
│   container-internal 6379        │          │   6379                │
│   async job status key: 'complete'│         │   (NOT 'done')        │
│ jarvis-neo4j                     │ 7474/    │ ✅ Production          │
│                                  │ 7687     │                       │
│ jarvis-local-resources-db        │ 5435     │ ✅ Production          │
│   (redteam_sessions table ★)     │          │   DB: postgres        │
│   (redteam_feedback table ★)     │          │   DB: postgres        │
│ [PostgreSQL msjarvis]            │ 5433     │ ✅ Host — Production   │
│ [PostgreSQL msjarvisgis]         │ 5432     │ ✅ Host — Production   │
│ [MySQL]                          │ 3307     │ ✅ Host — Running      │
│                                  │          │   schema dump pending │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ INGEST & CRYPTO (compose-managed │          │                       │
│ as of March 22, 2026)            │          │                       │
│ jarvis-crypto-policy             │ —        │ ✅ Running (compose)   │
│ jarvis-ingest-api                │ —        │ ✅ Running (compose)   │
│ jarvis-ingest-watcher            │ —        │ ✅ Running (compose)   │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ SUPPORT & UTILITY SERVICES       │          │                       │
│ [remaining support services]     │ various  │ ✅ Production          │
│ health-monitor, metrics,         │          │                       │
│ log-aggregator, cache-manager,   │          │                       │
│ config-service, api-gateway,     │          │                       │
│ notification-service, scheduler, │          │                       │
│ backup-service, and others       │          │                       │
└──────────────────────────────────┴──────────┴───────────────────────┘
```

> Figure 00-1. Ms. Jarvis production service registry as of March 22, 2026. ★ marks new entries added March 20–22, 2026. **Critical corrections in this version:** (1) `bbb-output-filter` at port 8017 does not exist — port 8016 handles both input and output BBB filtering; (2) MountainShares services 8080–8084 are NOT DEPLOYED — all return HTTP 000; (3) LLM ensemble ports are 8201–8222, not 8020–8039; (4) Caddy is v2.6.2 Ubuntu package — no xcaddy, no caddy-ratelimit, no forward_auth; (5) three systemd-managed services (cloudflared, caddy, jarvis-auth) are external to Docker Compose and not counted in the 83.

### 00.2.1 The `gbim_query_router` Service (Port 7205) — Added March 20, 2026

`gbim_query_router` is architecturally distinct from every other RAG service in one critical way: **it does not touch ChromaDB**. All other retrieval paths in the RAG pipeline pass through the shared ChromaDB instance (host port **8002**, container-internal 8000) for vector similarity search over 384-dimensional `all-minilm:latest` embeddings. `gbim_query_router` does not. It routes directly to `mvw_gbim_landowner_spatial` in `msjarvisgis` (port 5432) via SQL aggregation.

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

The GBIM corpus is the epistemic core of the Ms. Egeria Jarvis Steward System. All production beliefs live in two PostgreSQL databases on the host system. The table below reflects the verified production state as of **March 20, 2026**, including the 20,593 landowner beliefs added during the evening sprint.

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
│ TOTAL verified GBIM beliefs        │ 5,416,522 *    │               │
│ (* landowner rows are a subset of  │                │               │
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

> **Port note (March 22, 2026):** ChromaDB host port is **8002** (`127.0.0.1:8002->8000/tcp`). Container-internal port is 8000. All scripts and health checks must use port **8002** for host-side access. Auto-detect: `docker port jarvis-chroma 8000/tcp`.

```
┌─────────────────────────────────────────────────────────────────────┐
│           ChromaDB Production Collections — March 22, 2026          │
│             host port 8002 — all-minilm:latest (384-dim)            │
├──────────────────────────────────────┬──────────────┬───────────────┤
│ Collection                           │ Items        │ Notes         │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ gbim_worldview_entities              │ 5,416,521    │ Full GBIM     │
│                                      │              │ spatial corpus│
├──────────────────────────────────────┼──────────────┼───────────────┤
│ gbim_beliefs_v2                      │ ⚠ UNVERIFIED │ Could not be  │
│                                      │              │ confirmed in  │
│                                      │              │ March 22 CLI  │
│                                      │              │ output (13    │
│                                      │              │ collections   │
│                                      │              │ listed; this  │
│                                      │              │ was not among │
│                                      │              │ them). Do NOT │
│                                      │              │ mark Active   │
│                                      │              │ until verified│
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
│                                      │              │ (minimal —    │
│                                      │              │ expand needed)│
│ spiritual_texts                      │ 23           │ Mother Carrie │
│                                      │              │ Protocol      │
│ GBIM_sample_rows                     │ 5,000        │ Test/validate │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ geospatialfeatures                   │ 0            │ ⚠ Scaffolded  │
│                                      │              │ pending ingest│
├──────────────────────────────────────┼──────────────┼───────────────┤
│ msjarvis_docs                        │ 2,348        │ ✅ Active      │
│                                      │              │ 52 verified WV│
│                                      │              │ community res.│
│                                      │              │ (50 Kanawha + │
│                                      │              │ 2 Fayette) +  │
│                                      │              │ 2,296 system  │
│                                      │              │ docs ingested │
│                                      │              │ March 22, 2026│
├──────────────────────────────────────┼──────────────┼───────────────┤
│ ⚠ LANDOWNER BELIEFS                 │ NOT IN       │ Served by     │
│ (LANDOWNER_CORPORATE /               │ CHROMADB     │ gbim_query_   │
│  LANDOWNER_GOVERNMENT)               │              │ router (7205) │
│                                      │              │ PostgreSQL    │
│                                      │              │ native path   │
└──────────────────────────────────────┴──────────────┴───────────────┘
```

> Figure 00-3. ChromaDB collection inventory, March 22, 2026. `msjarvis_docs` updated from 0 (Scaffolded) to **2,348 Active** — 52 verified WV community resources (50 Kanawha + 2 Fayette counties) plus 2,296 system docs, ingested March 22, 2026. `gbim_beliefs_v2` status changed from Active to **⚠ UNVERIFIED** — not confirmed in March 22 ChromaDB list output; do not assert Active until explicitly re-verified. Landowner beliefs are explicitly absent from ChromaDB — the only GBIM belief class served exclusively via a PostgreSQL-native path.

---

## 00.5 Database Infrastructure Summary

```
┌─────────────────────────────────────────────────────────────────────┐
│          Ms. Jarvis Database Infrastructure — March 22, 2026        │
├─────────────────────────┬────────┬──────────────────────────────────┤
│ Database / Service      │ Port   │ Status & Key Facts               │
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
│  red team audit)        │        │ building_parcel_county_tax_mv:   │
│                         │        │   7,354,707 rows                 │
│                         │        │ 97.17% address coverage verified │
│                         │        │ redteam_sessions table ★ NEW     │
│                         │        │ redteam_feedback table ★ NEW     │
│                         │        │   (both: DB postgres)            │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ ChromaDB                │ 8002   │ ✅ Docker (jarvis-chroma)        │
│ (vector store)          │ (host) │ host port 8002 →                 │
│                         │        │ container-internal 8000          │
│                         │        │ 5,416,521 gbim_worldview_        │
│                         │        │ entities — 384-dim, all-minilm  │
│                         │        │ 21,181+ autonomous_learner items │
│                         │        │ msjarvis_docs: 2,348 ✅ Active ★ │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Redis                   │ 6380   │ ✅ Docker (jarvis-redis)         │
│ (cache + session)       │ (host) │ host port 6380 →                 │
│                         │        │ container-internal 6379          │
│                         │        │ Spatial cache + session state    │
│                         │        │ Async job status key: 'complete' │
│                         │        │   (NOT 'done')                   │
│                         │        │ Red team token namespace:        │
│                         │        │   redteam:token:<token> ★ NEW    │
│                         │        │ Red team feedback namespace:     │
│                         │        │   redteam:feedback:<job_id> ★    │
│                         │        │ NOTE: Host scripts use 6380;     │
│                         │        │ Docker containers use            │
│                         │        │ jarvis-redis:6379 (same Redis)   │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Neo4j                   │ 7474 / │ ✅ Docker                        │
│ (graph)                 │ 7687   │ Graph relationships + GBIM links │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ MySQL                   │ 3307   │ ✅ Host — Running                │
│                         │        │ root pw: my_secret_root_pw       │
│                         │        │ jarvis user pw: j4rv1sgeo!       │
│                         │        │ ⚠ Schema dump not yet in docs/  │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ jarvis-auth-service ★   │ 8055   │ ✅ systemd (NOT Docker Compose)  │
│ (standalone auth)       │        │ scripts/jarvis_auth_service.py   │
│                         │        │ /etc/systemd/system/             │
│                         │        │   jarvis-auth.service            │
│                         │        │ FastAPI — Redis 6380 (host)      │
│                         │        │ Token namespace:                 │
│                         │        │   redteam:token:<token>          │
│                         │        │   hset: active=true,             │
│                         │        │         userid=<userid>          │
│                         │        │ Token TTL: 30 days               │
│                         │        │ Rate limit: 10 req/hour          │
│                         │        │   (configured; not enforced      │
│                         │        │    at gateway layer ⚠)          │
│                         │        │ UI-initiated only — Caddy does   │
│                         │        │ NOT enforce auth on /chat        │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Caddy reverse proxy ★   │ 8443   │ ✅ systemd (NOT Docker Compose)  │
│                         │        │ /etc/caddy/Caddyfile             │
│                         │        │ Version: 2.6.2 (Ubuntu package   │
│                         │        │   sudo apt install caddy)        │
│                         │        │ ⚠ NOT xcaddy custom build        │
│                         │        │ ⚠ NO caddy-ratelimit module      │
│                         │        │ ⚠ NO forward_auth support        │
│                         │        │ CORS: Access-Control-Allow-      │
│                         │        │   Origin "*" — active ✅         │
│                         │        │ Log: /var/log/caddy/             │
│                         │        │   jarvis_redteam.log (JSON)      │
│                         │        │ Serves ui/ via file_server       │
│                         │        │ Proxies /chat* → 8050            │
│                         │        │         /auth* → 8055            │
│                         │        │         /health* → 8050          │
│                         │        │         /feedback* → 8055        │
│                         │        │         /systems* → 8050         │
│                         │        │         /chat/status* → 8055     │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Cloudflare Tunnel ★     │ —      │ ✅ systemd (NOT Docker Compose)  │
│                         │        │ Tunnel name: msjarvis            │
│                         │        │ UUID: 42ef9893-f4df-4cc5-        │
│                         │        │       8881-bb55b995e022          │
│                         │        │ Config: /etc/cloudflared/        │
│                         │        │   config.yml                     │
│                         │        │ Creds: /etc/cloudflared/         │
│                         │        │   42ef9893-….json                │
│                         │        │ Systemd: cloudflared.service     │
│                         │        │ Protocol: QUIC (4 conns)         │
│                         │        │   iad08, iad09, iad14, iad15-17  │
│                         │        │ TLS: Cloudflare terminates ✅    │
│                         │        │   (§42.10 TLS gap CLOSED)        │
│                         │        │ Routes → http://127.0.0.1:8443   │
│                         │        │ DNS records (all proxied):       │
│                         │        │   egeria → msjarvis tunnel       │
│                         │        │   live → msjarvis tunnel         │
│                         │        │   www → msjarvis tunnel          │
│                         │        │   mountainshares.us → msjarvis   │
│                         │        │   ai → Vercel (not Ms. Jarvis)   │
│                         │        │   chat → ms-jarvis-webhook       │
│                         │        │          (not yet configured)    │
└─────────────────────────┴────────┴──────────────────────────────────┘
```

> Figure 00-4. Database and external service infrastructure summary, March 22, 2026. ★ marks entries added March 20–22, 2026. **New in this version:** `jarvis-auth-service` (port 8055, systemd), Caddy reverse proxy (port 8443, systemd, v2.6.2 Ubuntu package — NOT xcaddy), Cloudflare Tunnel (systemd, tunnel name msjarvis), `redteam_sessions` and `redteam_feedback` tables (port 5435), MySQL confirmed at port 3307, Redis red team token and feedback namespaces. ChromaDB host port confirmed **8002**. Redis host port confirmed **6380**. Redis async job status key confirmed `'complete'` (NOT `'done'`).

---

## 00.6 Full Pipeline Flow (March 22, 2026)

The production query pipeline as of March 22, 2026. This reflects the confirmed production flow from the first public end-to-end test (POST /chat HTTP/1.1 200 OK, March 22, 2026).

> **Critical correction from prior versions:** Port 8017 (`bbb-output-filter`) does not exist and has never existed in the verified production stack. The output BBB (Phase 4.5) is handled by `jarvis-blood-brain-barrier` at **port 8016** — the same service that handles input filtering (Phase 1.4). Additionally, the LLM ensemble runs on ports **8201–8222**, not 8020–8039. The full pipeline now begins with Cloudflare Tunnel and Caddy before reaching the gateway.

```
User Query (browser at https://egeria.mountainshares.us)
    ↓
Cloudflare Tunnel (HTTPS/QUIC → Legion localhost)
    Protocol: QUIC — 4 connections to Cloudflare IAD edge
    TLS terminated by Cloudflare — end-to-end encrypted ✅
    ↓
Caddy (port 8443) — /etc/caddy/Caddyfile — v2.6.2 Ubuntu package
    CORS headers applied (Access-Control-Allow-Origin: *)
    Route: /chat* → 127.0.0.1:8050
    Route: /auth* → 127.0.0.1:8055
    Route: /feedback* → 127.0.0.1:8055
    Route: /chat/status* → 127.0.0.1:8055
    Serves: ui/ directory via file_server
    ⚠ NOTE: Caddy does NOT enforce token validation.
    ⚠ Unauthenticated /chat requests reach the gateway.
    ⚠ forward_auth not available in v2.6.2 Ubuntu package.
    ↓
jarvis-auth-service (port 8055) — UI-initiated token validation only
    Validates redteam:token:<token> in Redis (host:6380)
    Returns: {"valid": true, "userid": "...", "token_type": "redteam"}
    Called by UI on login — NOT called automatically before /chat
    ↓ (chat requests proceed regardless of auth state — known gap OI-36-A)
Unified Gateway (port 8050) — ms_jarvis_unified_gateway.py
    Endpoints: /chat, /chat/async, /chat/status/{job_id}, /feedback,
               /auth/token, /health, /systems
    CORS: allow_origins=["*"]
    ↓
BBB Input Filter (port 8016) — Phase 1.4
    jarvis-blood-brain-barrier
    content_approved check — BLOCKING
    Rejects harmful / unsafe input before main brain
    ↓ (content_approved=True)
Main Brain (port 8010) — main_brain.py — ultimate_chat handler
    │
    ├── Phase 1: Service availability check
    │
    ├── Phase 1.45: Community Memory Retrieval
    │     autonomous_learner (ChromaDB, host port 8002)
    │     all-minilm:latest — top-5 memories prepended to enhanced_message
    │
    ├── Phase 2: Multi-agent, web research, swarm, fifth-DGM
    │     Web Research Gateway (port 8007) — excluded when local context sufficient
    │     Registry Resolver (port 8008) — jarvis-local-resources-db (port 5435)
    │     GIS RAG (port 8005) — msjarvisgis (port 5432) + ChromaDB port 8002
    │     GBIM Landowner Router (port 7205) — PostgreSQL-native, NO ChromaDB
    │     Text RAG (port 8003/8004) — ChromaDB collections, host port 8002
    │
    ├── Phase 2.5: 21-LLM Ensemble (ports 8201–8222)
    │     Sequential consensus — 88–115s (GPU, RTX 4070)
    │     21/21 models responded within budget (March 22, 2026) ✅
    │
    ├── Phase 3: Judge Pipeline — parallel evaluation
    │     jarvis-judge-truth       (port 7230)  ~6–8s total
    │     jarvis-judge-consistency (port 7231)
    │     jarvis-judge-alignment   (port 7232)
    │     jarvis-judge-ethics      (port 7233)
    │     jarvis-judge-pipeline    (internal)
    │
    ├── Phase 3.5: LM Synthesizer (internal port 8001) — ~2–8s
    │     Persona injection — Ms. Egeria Jarvis identity
    │     IDENTITY RULES block in prompt f-string (commit 9ab770e9)
    │     Meta-commentary prohibition (commit 211056e6):
    │       — no AI model names
    │       — no synthesis disclosure
    │       — no hedging language
    │       — speak as one unified voice
    │
    ├── Phase 4: Storage queue (background — non-blocking)
    │     Session log → redteam_sessions (PostgreSQL port 5435)
    │
    └── Phase 4.5: BBB Output Filter (port 8016 — SAME SERVICE as Phase 1.4)
          LOG+PASSTHROUGH mode as of commit 18b8ddac (March 22, 2026)
          content_approved=False → logs warning + 200-char preview
          content_approved=False → DOES NOT block response (passthrough)
          Flagged: docker logs jarvis-main-brain | grep "⚠️ BBB OUTPUT FLAGGED"
          ⚠ Was blocking 31% of community queries (maternal Appalachian voice)
          ⚠ Recalibration is next-session priority
          ~2s
    ↓
Response object:
    {
      "response": "<Ms. Jarvis answer>",
      "services_used": ["agents_service", "web_research", "swarm_intelligence",
                        "fifth_dgm", "llm_production", "judge_pipeline",
                        "lm_synthesizer", "final_polish", "consciousness_bridge",
                        "bbb_output_filter"],
      "consciousness_level": "ultimate_collective",
      "processing_time": 99.58,
      "architecture_layers": 9
    }
    ↓
Caddy (port 8443) → Cloudflare Tunnel → User browser
Total confirmed end-to-end: 99–107s (GPU, RTX 4070, March 22, 2026)
```

> Figure 00-5. Full production pipeline flow, March 22, 2026. **Corrections from prior versions:** (1) Port 8017 removed — does not exist; (2) BBB output (Phase 4.5) is port 8016, same service as input, log+passthrough mode only; (3) LLM ensemble is ports 8201–8222; (4) full external ingress path added (Cloudflare Tunnel → Caddy 8443); (5) auth flow clarified — token validation is UI-initiated, Caddy does not enforce on /chat.

---

## 00.7 Service Count History

| Date | Services | Notable Addition / Change |
|---|---|---|
| Initial deployment | 79 | Core stack |
| Pre-March 14, 2026 | 82 | Phase 1.45 community memory services added |
| March 14, 2026 | 83 | `psychological-rag` (port 8006) promoted to production |
| March 19, 2026 | 84 | Spatial infrastructure services finalized (3D GiST, materialized views) |
| March 20, 2026 | 85 (reported) | `gbim_query_router` (port 7205) — landowner belief layer live |
| March 21–22, 2026 | **83 (verified)** | 3 orphaned containers (`jarvis-crypto-policy`, `jarvis-ingest-api`, `jarvis-ingest-watcher`) added to `docker-compose.yml` with `restart: unless-stopped`. Previously not compose-managed. Verified compose count: **83**. |
| **March 22, 2026 (afternoon)** | **83 compose + 3 systemd** | **Caddy (port 8443), jarvis-auth (port 8055), cloudflared added as systemd services outside Docker Compose. Docker Compose count remains 83 verified. Public URL https://egeria.mountainshares.us confirmed live.** |

> **Note on the March 20 → March 22 count:** The reported count of 85 on March 20 included `jarvis-crypto-policy`, `jarvis-ingest-api`, and `jarvis-ingest-watcher` running as orphaned `docker run` instances not defined in `docker-compose.yml`. They have since been added to the compose file and are now compose-managed. The verified Docker Compose total is **83**. The three systemd services (Caddy, jarvis-auth, cloudflared) are external to Docker Compose and are tracked separately.

---

## 00.8 Verified Production Numbers at a Glance

| Metric | Value | Verified |
|---|---|---|
| Total services (Docker Compose–managed) | **83** | March 21–22, 2026 (VERIFYANDTEST.sh) |
| External systemd services | **3** (Caddy, jarvis-auth, cloudflared) | March 22, 2026 |
| Public HTTPS URL | [**https://egeria.mountainshares.us**](https://egeria.mountainshares.us) | March 22, 2026 — confirmed live |
| Pipeline speed (single-user, GPU) | **~100–106s** | March 22, 2026 (three confirmed runs: 99.6s, 105.9s, 106.5s) |
| LLM models contributing | **21/21** | March 22, 2026 (all responded within budget) |
| Pre-flight gate | **20 PASS 0 FAIL** | March 22, 2026 (`scripts/preflight_gate.sh`) |
| Output BBB block rate | **0% (log+passthrough)** | March 22, 2026 — was 31%, disabled for tuning |
| Community resources verified | **52** | March 22, 2026 (50 Kanawha + 2 Fayette) |
| Active red team tokens | **4** | March 22, 2026 (carrie_admin ×2, hayden_test ×2) |
| LLM ensemble ports | **8201–8222** | March 22, 2026 (corrected from 8020–8039) |
| GBIM beliefs (`gbimbeliefnormalized`) | **5,416,522** | March 20, 2026 |
| — of which: landowner beliefs ★ | **20,593** | March 20, 2026 |
| — of which: spatial/facility beliefs | **5,395,929** | March 20, 2026 |
| GBIM worldview entities (ChromaDB) | **5,416,521** | March 20, 2026 |
| `autonomous_learner` items | **21,181+** | March 20, 2026 (~288/day) |
| `psychological_rag` items | **968** | March 20, 2026 |
| `msjarvis_docs` items | **2,348** | March 22, 2026 (52 WV community resources + 2,296 system docs) |
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
| ChromaDB host port | **8002** (`127.0.0.1:8002->8000/tcp`) | March 22, 2026 |
| Redis host port | **6380** (`127.0.0.1:6380->6379/tcp`) | March 22, 2026 |
| Redis async job status key | **`'complete'`** (NOT `'done'`) | March 22, 2026 |
| Caddy version | **2.6.2 (Ubuntu apt package)** | March 22, 2026 — NOT xcaddy; no caddy-ratelimit; no forward_auth |
| MountainShares services (8080–8084) | **❌ NOT DEPLOYED** | March 22, 2026 — all return HTTP 000 |
| BBB output filter port | **8016** (same as input) | March 22, 2026 — port 8017 does not exist |
| BBB output filter mode | **log+passthrough** (not blocking) | March 22, 2026 — commit 18b8ddac |
| LM Synthesizer identity guard | **Active — 3 layers** | March 22, 2026 — commits 9ab770e9 + 211056e6 |
| Cloudflare Tunnel UUID | **42ef9893-f4df-4cc5-8881-bb55b995e022** | March 22, 2026 |
| Auth service token TTL | **30 days** | March 22, 2026 |

*Last updated: 2026-03-22 (evening), Carrie Kidd (Mamma Kidd), Mount Hope WV*
*Public URL: https://egeria.mountainshares.us*
