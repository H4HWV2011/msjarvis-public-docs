# Chapter 00 — System Overview
## Ms. Egeria Jarvis: Architecture, Services, and Production Status

*Last updated: 2026-03-25 by Carrie Kidd (Mamma Kidd), Mount Hope WV*
*(Previous update: 2026-03-22)*

---

## 00.0 Purpose of This Chapter

This chapter is the single authoritative reference for the current production state of the Ms. Egeria Jarvis Steward System: what is running, at what port, at what scale, and verified on what date. It is not a theoretical introduction — that is Chapter 02. It is not a build log — those are the sprint notes appended to each chapter. It is an operational snapshot: the reference you consult when you need to know how many services are live, what the GBIM corpus actually contains as of today, and where each service sits in the overall architecture.

Every number in this chapter is verified. Every service listed is production-live or explicitly marked as staged. When a sprint advances the stack — as the March 20, 2026 landowner belief sprint, the March 22, 2026 red team hardening sprint, and the March 22–25, 2026 consciousness pipeline restoration sprint did — this chapter is updated first.

---

## 00.1 System Identity

**Name:** Ms. Egeria Jarvis (Ms. Jarvis)
**Role:** Steward System — AI-mediated benefits intelligence, spatial justice reasoning, and community resource routing for West Virginia
**Program:** Quantarithmia / Polymathmatic Geography / Harmony for Hope, Inc.
**Home:** Oak Hill / Mount Hope, Fayette County, West Virginia
**Architecture:** Distributed microservice stack, Docker Compose orchestrated + 3 external systemd services
**Production as of:** March 25, 2026
**Public URL:** https://egeria.mountainshares.us (confirmed live March 22, 2026)

Ms. Jarvis is not a general-purpose assistant with a West Virginia skin. She is a place-bound intelligence system whose reasoning is structurally anchored to the physical geography, institutional landscape, landowner record, and programmatic infrastructure of West Virginia. The service architecture described in this chapter is the operational expression of that commitment.

---

## 00.2 Production Service Registry

The Ms. Jarvis stack comprises **83 Docker Compose–managed services** plus **3 external systemd services** as of March 22, 2026.

> **Field note — March 20, 2026:** `gbim_query_router` (port 7205) promoted to production. This service handles all structured GBIM landowner belief queries via a PostgreSQL-native path against `mvw_gbim_landowner_spatial` in `msjarvisgis`. It does not use ChromaDB. It does not use the embedding pipeline. It is the first Ms. Jarvis service whose retrieval path is entirely relational — and it makes 20,593 verified landowner beliefs queryable by natural language for the first time.

> **Field note — March 21–22, 2026:** Three containers (`jarvis-crypto-policy`, `jarvis-ingest-api`, `jarvis-ingest-watcher`) were previously running as orphaned `docker run` instances not defined in `docker-compose.yml`. They have been added to `docker-compose.yml` with `restart: unless-stopped` and are now compose-managed. Verified production Docker Compose count: **83**.

> **Field note — March 22, 2026 (hardening sprint):** Three external services added as systemd units — they are not part of Docker Compose and are not counted in the 83: `caddy.service` (port 8443), `jarvis-auth.service` (port 8055), `cloudflared.service` (Cloudflare Tunnel). All auto-start on boot independently of Docker Compose.

> **Field note — March 22–25, 2026 (consciousness pipeline restoration sprint):** `jarvis-woah` (port 7012) brought online via stdlib stub on `qualia-net`. `msjarvisconsciousnessbridge.py` patched for Chroma v2 API, corrected neuro_master proxy, and gateway `dict.lower()` crash guard added. `jarvis-rag-server` port mapping corrected (host 8003 → container 8016), endpoint corrected (`/direct_rag` → `/query`), env vars injected (`OLLAMA_HOST=http://jarvis-ollama:11434`, `EMBED_MODEL=nomic-embed-text`). RAG embedder v2 Chroma query patch written and applied; pending container restart confirmation. Consciousness pipeline confirmed **ACTIVE** March 25, 2026 — end-to-end chat producing persona-consistent Appalachian-voice responses with Hilbert local entity recall and prior session context. Two commits merged to `main`: `fix: chroma v2 endpoint, woah network, gateway dict.lower() guards` and `fix: RAG endpoint /direct_rag -> /query`.

```
┌─────────────────────────────────────────────────────────────────────┐
│         Ms. Jarvis Production Service Registry — March 25, 2026     │
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
│ CONSCIOUSNESS PIPELINE ★ UPDATED │          │                       │
│ jarvis-consciousness-bridge      │ 8020     │ ✅ ACTIVE ★ (3 patches│
│                                  │          │   applied Mar 25)     │
│ jarvis-woah                      │ 7012     │ ✅ ACTIVE ★ (stdlib   │
│                                  │          │   stub, qualia-net)   │
│ jarvis-rag-server                │ 8003→    │ ⚠ PARTIALLY ACTIVE ★ │
│   (host:8003 → container:8016)   │ 8016     │   /query confirmed;   │
│                                  │          │   embedder v2 patch   │
│                                  │          │   pending restart     │
│ jarvis-neurobiological-master    │ 8018     │ ⚠ Unreachable during  │
│                                  │          │   Mar 25 sprint;      │
│                                  │          │   Chroma check        │
│                                  │          │   rerouted directly   │
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
│   (jarvis-rag-server             │ host→    │ ⚠ PARTIALLY ACTIVE ★ │
│    host:8003→container:8016)     │ 8016     │   /query reachable;   │
│                                  │          │   embed fix in-prog   │
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
│   (landowner belief path)        │          │   PostgreSQL-native   │
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
│   31 confirmed collections ★     │          │   6,665,093 items ★   │
│   all-minilm:latest (384-dim)    │          │   v2 API confirmed ★  │
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

> Figure 00-1. Ms. Jarvis production service registry as of March 25, 2026. ★ marks entries added or updated March 20–25, 2026. **Critical corrections:** (1) `bbb-output-filter` at port 8017 does not exist — port 8016 handles both phases; (2) MountainShares services 8080–8084 are NOT DEPLOYED; (3) LLM ensemble ports are 8201–8222, not 8020–8039; (4) Caddy is v2.6.2 Ubuntu package — no xcaddy, no caddy-ratelimit, no forward_auth; (5) three systemd services are external to Docker Compose and not counted in the 83; (6) jarvis-rag-server host:container port is 8003:8016; (7) consciousness pipeline **ACTIVE** as of March 25, 2026; (8) ChromaDB updated to **31 confirmed collections**, **6,665,093 total items**, v2 API confirmed.

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

All vector collections use **`all-minilm:latest` (384-dimensional embeddings)** via `jarvis-ollama` (port 11434). This embedding model is locked for all production collections. `nomic-embed-text` (768-dim) is **incompatible** with all existing collections and must not be used for any ingestion or retrieval operation against the production corpus. The `jarvis-rag-server` uses `nomic-embed-text` only for its own query-time embedding at the service level — this does not affect the shared production ChromaDB corpus.

> **Port note (March 22, 2026):** ChromaDB host port is **8002** (`127.0.0.1:8002->8000/tcp`). Container-internal port is 8000. All scripts and health checks must use port **8002** for host-side access. Auto-detect: `docker port jarvis-chroma 8000/tcp`.

> **API note (March 25, 2026):** ChromaDB v2 API confirmed active. All internal service calls must use `/api/v2/` endpoints. The `/api/v1/` path returns **HTTP 410 Gone**. Heartbeat: `GET /api/v2/heartbeat`. Collection queries: `POST /api/v2/tenants/default_tenant/databases/default_database/collections/{collection_name}/query`. Two commits to `main` update the consciousness bridge and rag-server to v2 endpoints.

```
┌─────────────────────────────────────────────────────────────────────┐
│   ChromaDB Production Collections — March 25, 2026 ★ UPDATED       │
│   host port 8002 — all-minilm:latest (384-dim)                      │
│   31 confirmed collections ★ — 6,665,093 total items ★             │
├──────────────────────────────────────┬──────────────┬───────────────┤
│ Collection                           │ Items        │ Notes         │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ gbim_worldview_entities              │ 5,416,521    │ Full GBIM     │
│                                      │              │ spatial corpus│
├──────────────────────────────────────┼──────────────┼───────────────┤
│ gbim_beliefs_v2                      │ ⚠ UNVERIFIED │ Not confirmed │
│                                      │              │ in Mar 22 CLI │
│                                      │              │ output. Do NOT│
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
│   ⚠ not formally wired to pipeline  │              │ OI-05 open    │
│ appalachian_cultural_intelligence    │ 5            │ Cultural RAG  │
│                                      │              │ (minimal —    │
│                                      │              │ expand needed)│
│ spiritual_texts                      │ 23           │ Mother Carrie │
│                                      │              │ Protocol      │
│ GBIM_sample_rows                     │ 5,000        │ Test/validate │
│ local_resources                      │ Active       │ Default RAG ★ │
│                                      │              │ collection for│
│                                      │              │ rag-server    │
│ economic_rag                         │ Active       │ Economic intel│
│ policy_rag                           │ Active       │ Policy corpus │
│ grants_rag                           │ Active       │ Grant corpus  │
│ legal_rag                            │ Active       │ Legal corpus  │
│ health_rag                           │ Active       │ Health corpus │
│ news_rag                             │ Active       │ News corpus   │
│ commons_rag                          │ Active       │ Commons corpus│
│ meeting_minutes                      │ Active       │ Meeting docs  │
│ contracts                            │ Active       │ Contracts     │
│ address_points                       │ Active       │ WV addresses  │
│ safety_rules                         │ Active       │ Safety rules  │
│ fifth_dgm_subconscious               │ Active       │ Subconscious  │
│                                      │              │ write = stub  │
│ conversation_gbim_private            │ Active       │ GBIM private  │
│ conversation_gbim_public             │ Active       │ GBIM public   │
│ GBIM_sample                          │ Active       │ Sample subset │
│ GBIM_Fayette_sample                  │ 0            │ ⚠ Scaffolded  │
│                                      │              │ pending ingest│
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

> Figure 00-3. ChromaDB collection inventory, March 25, 2026. **★ UPDATED:** 31 confirmed collections (up from 13 at March 22 audit); total items confirmed at **6,665,093**; v2 API active — all `/api/v1/` calls return 410 Gone; `local_resources` confirmed as default RAG server collection; `conversation_history` confirmed present — formal pipeline wiring remains OI-05 (open); `geospatialfeatures` and `GBIM_Fayette_sample` confirmed 0 items; `gbim_beliefs_v2` remains UNVERIFIED.

---

## 00.5 Database Infrastructure Summary

```
┌─────────────────────────────────────────────────────────────────────┐
│          Ms. Jarvis Database Infrastructure — March 25, 2026        │
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
│                         │        │ redteam_sessions table ★         │
│                         │        │ redteam_feedback table ★         │
│                         │        │   (both: DB postgres)            │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ ChromaDB                │ 8002   │ ✅ Docker (jarvis-chroma)        │
│ (vector store)          │ (host) │ host port 8002 →                 │
│                         │        │ container-internal 8000          │
│                         │        │ 31 collections ★ (6,665,093 items│
│                         │        │ 5,416,521 gbim_worldview_        │
│                         │        │ entities — 384-dim, all-minilm  │
│                         │        │ 21,181+ autonomous_learner items │
│                         │        │ msjarvis_docs: 2,348 ✅ Active ★ │
│                         │        │ v2 API active ★                  │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Redis                   │ 6380   │ ✅ Docker (jarvis-redis)         │
│ (cache + session)       │ (host) │ host port 6380 →                 │
│                         │        │ container-internal 6379          │
│                         │        │ Spatial cache + session state    │
│                         │        │ Async job status key: 'complete' │
│                         │        │   (NOT 'done')                   │
│                         │        │ NOTE: Host scripts use 6380;     │
│                         │        │ Docker containers use            │
│                         │        │ jarvis-redis:6379 (same Redis)   │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Neo4j                   │ 7474 / │ ✅ Docker                        │
│ (graph)                 │ 7687   │ Graph relationships + GBIM links │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ MySQL                   │ 3307   │ ✅ Host — Running                │
│                         │        │ ⚠ Schema dump not yet in docs/  │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ jarvis-auth-service ★   │ 8055   │ ✅ systemd (NOT Docker Compose)  │
│ (standalone auth)       │        │ scripts/jarvis_auth_service.py   │
│                         │        │ FastAPI — Redis 6380 (host)      │
│                         │        │ Token TTL: 30 days               │
│                         │        │ Rate limit: 10 req/hour          │
│                         │        │   (configured; not enforced      │
│                         │        │    at gateway layer ⚠)          │
│                         │        │ UI-initiated only — Caddy does   │
│                         │        │ NOT enforce auth on /chat        │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Caddy reverse proxy ★   │ 8443   │ ✅ systemd (NOT Docker Compose)  │
│                         │        │ Version: 2.6.2 (Ubuntu package)  │
│                         │        │ ⚠ NOT xcaddy custom build        │
│                         │        │ ⚠ NO caddy-ratelimit module      │
│                         │        │ ⚠ NO forward_auth support        │
│                         │        │ CORS: Access-Control-Allow-      │
│                         │        │   Origin "*" — active ✅         │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Cloudflare Tunnel ★     │ —      │ ✅ systemd (NOT Docker Compose)  │
│                         │        │ Tunnel name: msjarvis            │
│                         │        │ UUID: 42ef9893-f4df-4cc5-        │
│                         │        │       8881-bb55b995e022          │
│                         │        │ TLS: Cloudflare terminates ✅    │
│                         │        │   (§42.10 TLS gap CLOSED)        │
└─────────────────────────┴────────┴──────────────────────────────────┘
```

> Figure 00-4. Database and external service infrastructure summary, March 25, 2026. ★ marks entries updated March 25, 2026. ChromaDB updated to **31 confirmed collections** and **6,665,093 total items**; v2 API active. MySQL credentials removed from public-facing documentation — see secure credential store.

---

## 00.6 Full Pipeline Flow (March 25, 2026)

The production query pipeline as of March 25, 2026. Validated through first public end-to-end test (March 22, 2026) and consciousness pipeline confirmation (March 25, 2026).

> **Critical corrections carried forward:** Port 8017 (`bbb-output-filter`) does not exist — port 8016 handles both phases. LLM ensemble runs on ports 8201–8222, not 8020–8039. `jarvis-rag-server` internal port is 8016 (host port 8003). All consciousness pipeline services confirmed on `qualia-net` as of March 25, 2026.

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
    ⚠ NOTE: Caddy does NOT enforce token validation.
    ⚠ Unauthenticated /chat requests reach the gateway (OI-36-A).
    ↓
jarvis-auth-service (port 8055) — UI-initiated token validation only
    Validates redteam:token:<token> in Redis (host:6380)
    NOT called automatically before /chat
    ↓ (chat requests proceed regardless of auth state — known gap OI-36-A)
Unified Gateway (port 8050) — ms_jarvis_unified_gateway.py
    Endpoints: /chat, /chat/async, /chat/status/{job_id},
               /feedback, /auth/token, /health, /systems
    dict.lower() guard patched March 25, 2026 ★
    ↓
BBB Input Filter (port 8016) — Phase 1.4
    6 active filters: EthicalFilter, SpiritualFilter, SafetyMonitor,
    ThreatDetection, steganography filter, truth verification
    content_approved check — BLOCKING ✅
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
    │     Web Research Gateway (port 8007)
    │     Registry Resolver (port 8008)
    │     GIS RAG (port 8005) — msjarvisgis (port 5432) + ChromaDB 8002
    │     GBIM Landowner Router (port 7205) — PostgreSQL-native, NO ChromaDB
    │     Text RAG / jarvis-rag-server (port 8003→8016) ★ PARTIALLY ACTIVE
    │       /query endpoint confirmed; embedder fix in progress
    │       CHROMA v2 query patch written; pending container restart
    │
    ├── [CONSCIOUSNESS PIPELINE] ★ ACTIVE as of March 25, 2026
    │     jarvis-consciousness-bridge (port 8020)
    │       → Chroma health: GET /api/v2/heartbeat → 200 ✅
    │       → WOAH: POST jarvis-woah:7012/process
    │            → {status: ok, confidence: 0.8} ✅
    │       → RAG: POST jarvis-rag-server:8016/query ★ reachable
    │            → rag_consensus: pending embedder fix
    │
    ├── Phase 2.5: 21-LLM Ensemble (ports 8201–8222)
    │     Sequential consensus — 88–115s (GPU, RTX 4070)
    │
    ├── Phase 3: Judge Pipeline — parallel evaluation
    │     jarvis-judge-truth       (port 7230)
    │     jarvis-judge-consistency (port 7231)
    │     jarvis-judge-alignment   (port 7232)
    │     jarvis-judge-ethics      (port 7233)
    │
    ├── Phase 3.5: LM Synthesizer (internal port 8001)
    │     Persona injection — Ms. Egeria Jarvis identity
    │     No model names leaked ✅ (validated March 25, 2026)
    │
    ├── Phase 4: Storage queue (background — non-blocking)
    │     Session log → redteam_sessions (PostgreSQL port 5435)
    │
    └── Phase 4.5: BBB Output Filter (port 8016 — SAME SERVICE as Phase 1.4)
          LOG+PASSTHROUGH mode (not blocking)
          ⚠ Recalibration required before production (OI-02)
    ↓
Response object:
    {
      "response": "<Ms. Jarvis answer>",
      "consciousness_level": "ultimate_collective",
      "processing_time": ~100–107s,
      "architecture_layers": 9
    }
    ↓
Caddy (port 8443) → Cloudflare Tunnel → User browser
```

> Figure 00-5. Full production pipeline flow, March 25, 2026. **★ Changes confirmed March 25:** consciousness pipeline ACTIVE; dict.lower() guard in gateway patched; jarvis-rag-server port corrected to 8003→8016; Chroma v2 API in use throughout.

---

## 00.7 Service Count History

| Date | Services | Notable Addition / Change |
|---|---|---|
| Initial deployment | 79 | Core stack |
| Pre-March 14, 2026 | 82 | Phase 1.45 community memory services added |
| March 14, 2026 | 83 | `psychological-rag` (port 8006) promoted to production |
| March 19, 2026 | 84 | Spatial infrastructure services finalized (3D GiST, materialized views) |
| March 20, 2026 | 85 (reported) | `gbim_query_router` (port 7205) — landowner belief layer live |
| March 21–22, 2026 | **83 (verified)** | 3 orphaned containers added to `docker-compose.yml`; verified compose count: 83 |
| March 22, 2026 (afternoon) | **83 compose + 3 systemd** | Caddy (8443), jarvis-auth (8055), cloudflared added as systemd; public URL https://egeria.mountainshares.us confirmed live |
| March 22–25, 2026 | **83 compose + 3 systemd** | Consciousness pipeline sprint: `jarvis-woah`, bridge, `jarvis-rag-server` patched and confirmed active. No compose count change. |

---

## 00.8 System Health Snapshot — March 25, 2026 ★ UPDATED

| Metric | Value | Verified |
|---|---|---|
| Total services (Docker Compose–managed) | **83** | March 21–22, 2026 |
| External systemd services | **3** (Caddy, jarvis-auth, cloudflared) | March 22, 2026 |
| Public HTTPS URL | **https://egeria.mountainshares.us** | March 22, 2026 — confirmed live |
| Pipeline speed (single-user, GPU) | **~100–107s** | March 22, 2026 (99.6s, 105.9s, 106.5s) |
| LLM models contributing | **21/21** | March 22, 2026 |
| **Preflight gate** | **24 PASS 0 FAIL ★** | **March 22, 2026 — re-validated March 25, 2026; no regression** |
| Output BBB block rate | **0% (log+passthrough)** | March 22, 2026 |
| Community resources verified | **52** | March 22, 2026 (50 Kanawha + 2 Fayette) |
| Active red team tokens | **4** | March 22, 2026 |
| LLM ensemble ports | **8201–8222** | March 22, 2026 |
| GBIM beliefs (`gbimbeliefnormalized`) | **5,416,522** | March 20, 2026 |
| — of which: landowner beliefs ★ | **20,593** | March 20, 2026 |
| — of which: spatial/facility beliefs | **5,395,929** | March 20, 2026 |
| GBIM worldview entities (ChromaDB) | **5,416,521** | March 20, 2026 |
| `autonomous_learner` items | **21,181+** | March 20, 2026 (~288/day) |
| `psychological_rag` items | **968** | March 20, 2026 |
| `msjarvis_docs` items | **2,348** | March 22, 2026 |
| **ChromaDB collections (confirmed)** | **31 ★** | **March 25, 2026 (up from 13 at March 22 audit)** |
| **ChromaDB total items** | **6,665,093 ★** | **March 25, 2026** |
| **ChromaDB API version** | **v2 active ★ — v1 returns 410** | **March 25, 2026** |
| **Consciousness pipeline** | **ACTIVE ★** | **March 25, 2026 — Chroma 200, WOAH stub live, bridge patched** |
| **RAG pipeline (`jarvis-rag-server`)** | **PARTIALLY ACTIVE ★** | **March 25, 2026 — /query confirmed; embedder v2 fix pending restart** |
| Canonical buildings (`wv_buildings`) | **2,120,976** | March 19, 2026 |
| Building-parcel records (MV) | **7,354,707** | March 19, 2026 |
| Address coverage (verified situs) | **97.17%** | March 19, 2026 |
| `msjarvisgis` tables | **501** | March 20, 2026 |
| `msjarvisgis` size | **91 GB** | March 20, 2026 |
| Embedding dimensions (all collections) | **384** | `all-minilm:latest` |
| Worldview | **eq1** | All production beliefs |
| ChromaDB host port | **8002** (`127.0.0.1:8002->8000/tcp`) | March 22, 2026 |
| Redis host port | **6380** (`127.0.0.1:6380->6379/tcp`) | March 22, 2026 |
| Redis async job status key | **`'complete'`** (NOT `'done'`) | March 22, 2026 |
| Caddy version | **2.6.2 (Ubuntu apt package)** | March 22, 2026 — NOT xcaddy; no caddy-ratelimit; no forward_auth |
| MountainShares services (8080–8084) | **❌ NOT DEPLOYED** | March 22, 2026 — all return HTTP 000 |
| BBB output filter port | **8016** (same as input) | March 22, 2026 — port 8017 does not exist |
| BBB output filter mode | **log+passthrough** (not blocking) | March 22, 2026 |
| LM Synthesizer identity guard | **Active — no leakage confirmed** | March 25, 2026 |
| Cloudflare Tunnel UUID | **42ef9893-f4df-4cc5-8881-bb55b995e022** | March 22, 2026 |
| Auth service token TTL | **30 days** | March 22, 2026 |

---

## 00.9 Sprint Progress Log

| Sprint | Dates | Items Closed | Status |
|---|---|---|---|
| Landowner belief sprint | March 20, 2026 | `gbim_query_router` promoted; 20,593 landowner beliefs ingested; `mvw_gbim_landowner_spatial` live | ✅ Complete |
| Red team hardening sprint | March 21–22, 2026 | Orphaned containers added to compose; systemd services (Caddy, jarvis-auth, cloudflared) deployed; public URL live; 0.0.0.0→127.0.0.1 hardening; 3 immutable containers protected; BBB bbbCheckVerdict wired; MS docs ingested (2,348 items); first public end-to-end test PASS | ✅ Complete |
| Consciousness pipeline restoration sprint | March 22–25, 2026 | WOAH service fixed (stdlib stub, qualia-net confirmed); Chroma v2 API migration (bridge + rag-server patched); RAG server port/endpoint/schema corrected (8003→8016, `/direct_rag`→`/query`); gateway `dict.lower()` crash guard added; end-to-end chat **ACTIVE** with Hilbert entity recall and prior session context; two commits merged to `main` | ✅ Closed — RAG embedder restart pending |

---

*Last updated: 2026-03-25 (evening), Carrie Kidd (Mamma Kidd), Mount Hope WV*
*Public URL: https://egeria.mountainshares.us*
