# Chapter 00 — System Overview
## Ms. Egeria Jarvis: Architecture, Services, and Production Status

*Last updated: 2026-03-26 by Carrie Kidd (Mamma Kidd), Mount Hope WV*
*(Previous update: 2026-03-25)*

---

## 00.0 Purpose of This Chapter

This chapter is the single authoritative reference for the current production state of the Ms. Egeria Jarvis Steward System: what is running, at what port, at what scale, and verified on what date. It is not a theoretical introduction — that is Chapter 02. It is not a build log — those are the sprint notes appended to each chapter. It is an operational snapshot: the reference you consult when you need to know how many services are live, what the GBIM corpus actually contains as of today, and where each service sits in the overall architecture.

Every number in this chapter is verified. Every service listed is production-live or explicitly marked as staged. When a sprint advances the stack — as the March 20, 2026 landowner belief sprint, the March 22, 2026 red team hardening sprint, the March 22–25, 2026 consciousness pipeline restoration sprint, and the March 26, 2026 RAG corpus completion sprint did — this chapter is updated first.

---

## 00.1 System Identity

**Name:** Ms. Egeria Jarvis (Ms. Jarvis)
**Role:** Steward System — AI-mediated benefits intelligence, spatial justice reasoning, and community resource routing for West Virginia
**Program:** Quantarithmia / Polymathmatic Geography / Harmony for Hope, Inc.
**Home:** Oak Hill / Mount Hope, Fayette County, West Virginia
**Architecture:** Distributed microservice stack, Docker Compose orchestrated (`msjarvis-rebuild` namespace) + 3 external systemd services
**Production as of:** March 26, 2026
**Public URL:** https://egeria.mountainshares.us (confirmed live March 22, 2026)

Ms. Jarvis is not a general-purpose assistant with a West Virginia skin. She is a place-bound intelligence system whose reasoning is structurally anchored to the physical geography, institutional landscape, landowner record, and programmatic infrastructure of West Virginia. The service architecture described in this chapter is the operational expression of that commitment.

---

## 00.2 Production Service Registry

The Ms. Jarvis stack comprises **56 Docker Compose–managed services** in the `msjarvis-rebuild` namespace plus **3 external systemd services** as of March 26, 2026.

> **Field note — March 20, 2026:** `gbim_query_router` (port 7205) promoted to production. This service handles all structured GBIM landowner belief queries via a PostgreSQL-native path against `mvw_gbim_landowner_spatial` in `msjarvisgis`. It does not use ChromaDB. It does not use the embedding pipeline. It is the first Ms. Jarvis service whose retrieval path is entirely relational — and it makes 20,593 verified landowner beliefs queryable by natural language for the first time.

> **Field note — March 21–22, 2026:** Three containers (`jarvis-crypto-policy`, `jarvis-ingest-api`, `jarvis-ingest-watcher`) were previously running as orphaned `docker run` instances not defined in `docker-compose.yml`. They have been added to `docker-compose.yml` with `restart: unless-stopped` and are now compose-managed.

> **Field note — March 22, 2026 (hardening sprint):** Three external services added as systemd units — they are not part of Docker Compose and are not counted in the 56: `caddy.service` (port 8443), `jarvis-auth.service` (port 8055), `cloudflared.service` (Cloudflare Tunnel). All auto-start on boot independently of Docker Compose.

> **Field note — March 22–25, 2026 (consciousness pipeline restoration sprint):** `jarvis-woah` (port 7012) brought online via stdlib stub on `qualia-net`. `msjarvisconsciousnessbridge.py` patched for Chroma v2 API, corrected neuro_master proxy, and gateway `dict.lower()` crash guard added. Consciousness pipeline confirmed **ACTIVE** March 25, 2026 — end-to-end chat producing persona-consistent Appalachian-voice responses with Hilbert local entity recall and prior session context.

> **Field note — March 26, 2026 (RAG corpus completion sprint):** All ChromaDB RAG collections fully populated and semantically verified. `governance_rag` ingested to **643 chunks** (MountainShares DAO full corpus + US Constitution 97 chunks from Project Gutenberg). `commons_rag` ingested to **306 chunks** (full Commons governance and gamification corpus). `geospatialfeatures` confirmed **60,000 items**. `GBIM_Fayette_sample` confirmed **1,535 items**. `appalachian_cultural_intelligence` confirmed **820 items**. `spiritual_texts` confirmed **19,338 items**. EEG heartbeat services (`eeg-delta`, `eeg-theta`, `eeg-beta`) confirmed live. Semantic retrieval smoke-tested and verified across all four RAG domains. Rebuild namespace: `msjarvis-rebuild`. **Total confirmed live containers: 56.**

```
┌─────────────────────────────────────────────────────────────────────┐
│     Ms. Jarvis Production Service Registry — March 26, 2026         │
│         56 Docker Compose Services (msjarvis-rebuild) + 3 systemd   │
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
│ CONSCIOUSNESS PIPELINE ★ ACTIVE  │          │                       │
│ jarvis-consciousness-bridge      │ 8020     │ ✅ ACTIVE ★            │
│ jarvis-woah                      │ 7012     │ ✅ ACTIVE ★            │
│ jarvis-rag-server                │ 8003→    │ ⚠ PARTIALLY ACTIVE ★ │
│   (host:8003 → container:8016)   │ 8016     │   /query confirmed;   │
│                                  │          │   embedder v2 patch   │
│                                  │          │   pending restart     │
│ jarvis-neurobiological-master    │ 8018     │ ⚠ Check pending       │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ BLOOD-BRAIN BARRIER (BBB)        │          │                       │
│ jarvis-blood-brain-barrier       │ 8016     │ ✅ Production          │
│   Phase 1.4 input filter:        │          │   INPUT: blocking ✅  │
│   ACTIVE — blocking              │          │   OUTPUT (Ph 4.5):    │
│   Phase 4.5 output filter:       │          │   log+passthrough ⚠  │
│   LOG+PASSTHROUGH (not blocking) │          │                       │
│ ⛔ bbb-output-filter (port 8017) │ 8017     │ ❌ DOES NOT EXIST     │
│   THIS CONTAINER IS NOT RUNNING  │          │   Port 8016 handles   │
│   and never existed              │          │   both phases         │
│ guardrail-service                │ 8018     │ ✅ Production          │
│ constitutional-layer             │ 8019     │ ✅ Production          │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ RAG PIPELINE ★ CORPUS COMPLETE   │          │                       │
│ text-rag-service                 │ 8003     │ ✅ Production          │
│ rag-service                      │ 8004     │ ✅ Production          │
│ gis-rag-service                  │ 8005     │ ✅ Production          │
│ psychological-rag                │ 8006     │ ✅ Production (968)    │
│ web-research-gateway             │ 8007     │ ✅ Production          │
│ registry-resolver                │ 8008     │ ✅ Production          │
│ community-memory-service         │ 8009     │ ✅ Production          │
│ gbim_query_router                │ 7205     │ ✅ Production ★        │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ EEG HEARTBEAT ★ ALL LIVE         │          │                       │
│ eeg-delta                        │ —        │ ✅ LIVE — 30s cadence  │
│                                  │          │   1 pulse confirmed   │
│ eeg-theta                        │ —        │ ✅ LIVE — 60s cadence  │
│                                  │          │   486 pulses confirmed│
│ eeg-beta                         │ —        │ ✅ LIVE — 5-min cadence│
│                                  │          │   topic: Appalachian  │
│                                  │          │   1 pulse confirmed   │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ LLM ENSEMBLE (21 models)         │          │                       │
│ llm-proxy-01 … 21                │8201–8222 │ ✅ Production          │
│ ensemble-coordinator             │ 8040     │ ✅ Production          │
│ consensus-engine                 │ 8041     │ ✅ Production          │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ LM SYNTHESIZER                   │          │                       │
│ lm-synthesizer                   │ 8001     │ ✅ Production          │
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
│   Corpus fully ingested ✅ —     │          │   Services await      │
│   governance_rag: 643 chunks     │          │   Phase 0 beta launch │
│   commons_rag: 306 chunks        │          │                       │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ DATA STORES (infrastructure)     │          │                       │
│ jarvis-chromadb                  │ 8002     │ ✅ Production          │
│   host port 8002 →               │ (host)   │   container 8000      │
│   all-minilm:latest (384-dim)    │          │   v2 API confirmed ★  │
│ jarvis-ollama                    │ 11434    │ ✅ Production          │
│ jarvis-redis                     │ 6380     │ ✅ Production          │
│ jarvis-neo4j                     │ 7474/    │ ✅ Production          │
│                                  │ 7687     │                       │
│ jarvis-local-resources-db        │ 5435     │ ✅ Production          │
│ [PostgreSQL msjarvis]            │ 5433     │ ✅ Host — Production   │
│ [PostgreSQL msjarvisgis]         │ 5432     │ ✅ Host — Production   │
│ [MySQL]                          │ 3307     │ ✅ Host — Running      │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ INGEST & CRYPTO                  │          │                       │
│ jarvis-crypto-policy             │ —        │ ✅ Running (compose)   │
│ jarvis-ingest-api                │ —        │ ✅ Running (compose)   │
│ jarvis-ingest-watcher            │ —        │ ✅ Running (compose)   │
├──────────────────────────────────┼──────────┼───────────────────────┤
│ SUPPORT & UTILITY SERVICES       │          │                       │
│ health-monitor, metrics,         │ various  │ ✅ Production          │
│ log-aggregator, cache-manager,   │          │                       │
│ config-service, api-gateway,     │          │                       │
│ notification-service, scheduler, │          │                       │
│ backup-service, and others       │          │                       │
└──────────────────────────────────┴──────────┴───────────────────────┘
```

> Figure 00-1. Ms. Jarvis production service registry as of March 26, 2026. ★ marks entries added or updated March 26, 2026. **Verified container count: 56 (msjarvis-rebuild namespace).** EEG heartbeat services (delta, theta, beta) confirmed live. RAG corpus collections fully populated — see Section 00.4 for verified counts. MountainShares services 8080–8084 remain NOT DEPLOYED (corpus ingested; services await Phase 0 beta launch). Port 8017 (`bbb-output-filter`) does not exist — port 8016 handles both input and output phases.

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

> Figure 00-2. GBIM corpus verified production state, March 20, 2026. ★ marks tables/views added or updated in the March 20, 2026 landowner sprint.

---

## 00.4 ChromaDB Collection Summary — ★ UPDATED March 26, 2026

All vector collections use **`all-minilm:latest` (384-dimensional embeddings)** via `jarvis-ollama` (port 11434). This embedding model is locked for all production collections. Chunk size constraint confirmed: **100 words maximum per chunk** (256-token context limit on `all-minilm`). 20-word overlap. Cosine similarity space.

> **Port note:** ChromaDB host port is **8002** (`127.0.0.1:8002->8000/tcp`). Container-internal port is 8000. All scripts and health checks must use port **8002** for host-side access.

> **API note:** ChromaDB v2 API confirmed active. All internal service calls must use `/api/v2/` endpoints. The `/api/v1/` path returns **HTTP 410 Gone**.

> **Embedding API note (March 26, 2026):** Use `/api/embeddings` (single-string `prompt` key) — NOT `/api/embed`. The `/api/embed` endpoint with list input was tested and confirmed, but production ingest pipeline uses single-string path for compatibility.

```
┌─────────────────────────────────────────────────────────────────────┐
│   ChromaDB Production Collections — March 26, 2026 ★ UPDATED       │
│   host port 8002 — all-minilm:latest (384-dim, cosine)              │
│   RAG collections fully populated ★                                 │
├──────────────────────────────────────┬──────────────┬───────────────┤
│ Collection                           │ Items        │ Notes         │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ gbim_worldview_entities              │ 5,416,521    │ Full GBIM     │
│                                      │              │ spatial corpus│
├──────────────────────────────────────┼──────────────┼───────────────┤
│ geospatialfeatures ★                 │ 60,000       │ ✅ POPULATED  │
│                                      │              │ OI-12 CLOSED  │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ GBIM_Fayette_sample ★                │ 1,535        │ ✅ POPULATED  │
│                                      │              │ OI-13 CLOSED  │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ appalachian_cultural_intelligence ★  │ 820          │ ✅ POPULATED  │
│                                      │              │ OI-14 CLOSED  │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ spiritual_texts ★                    │ 19,338       │ ✅ POPULATED  │
│                                      │              │ OI-15 CLOSED  │
│                                      │              │ Mother Carrie │
│                                      │              │ Protocol      │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ governance_rag ★                     │ 643 chunks   │ ✅ POPULATED  │
│                                      │              │ OI-19 CLOSED  │
│                                      │              │ MountainShares│
│                                      │              │ DAO full corpus│
│                                      │              │ + US Const.   │
│                                      │              │ (97 chunks,   │
│                                      │              │ Gutenberg)    │
│                                      │              │ Retrieval     │
│                                      │              │ verified ✅   │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ commons_rag ★                        │ 306 chunks   │ ✅ POPULATED  │
│                                      │              │ OI-20 CLOSED  │
│                                      │              │ Full Commons  │
│                                      │              │ governance +  │
│                                      │              │ gamification  │
│                                      │              │ corpus        │
│                                      │              │ Retrieval     │
│                                      │              │ verified ✅   │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ autonomous_learner                   │ 21,181+      │ ~288/day      │
│                                      │ (growing)    │ Phase 1.45    │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ psychological_rag                    │ 968          │ port 8006     │
│                                      │              │ crisis/mental │
│                                      │              │ health corpus │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ msjarvis_docs                        │ 2,348        │ ✅ Active      │
│                                      │              │ 52 WV community│
│                                      │              │ resources +   │
│                                      │              │ 2,296 sys docs│
├──────────────────────────────────────┼──────────────┼───────────────┤
│ governance                           │ Active       │ WV governance │
│ thesis                               │ Active       │ Theory corpus │
│ mountainshares_knowledge             │ Active       │ DAO/economics │
│ ms_jarvis_memory                     │ Active       │ Persistent mem│
│ episodic_index                       │ Active       │ Episodic index│
│ conversation_history                 │ Active       │ Session ctx   │
│   ⚠ not formally wired to pipeline  │              │ OI-05 open    │
│ gis_wv_benefits                      │ Active       │ WV benefits   │
│ GBIM_sample_rows                     │ 5,000        │ Test/validate │
│ local_resources                      │ Active       │ Default RAG   │
│ economic_rag                         │ Active       │ Economic intel│
│ policy_rag                           │ Active       │ Policy corpus │
│ grants_rag                           │ Active       │ Grant corpus  │
│ legal_rag                            │ Active       │ Legal corpus  │
│ health_rag                           │ Active       │ Health corpus │
│ news_rag                             │ Active       │ News corpus   │
│ meeting_minutes                      │ Active       │ Meeting docs  │
│ contracts                            │ Active       │ Contracts     │
│ address_points                       │ Active       │ WV addresses  │
│ safety_rules                         │ Active       │ Safety rules  │
│ fifth_dgm_subconscious               │ Active       │ Subconscious  │
│ conversation_gbim_private            │ Active       │ GBIM private  │
│ conversation_gbim_public             │ Active       │ GBIM public   │
│ GBIM_sample                          │ Active       │ Sample subset │
├──────────────────────────────────────┼──────────────┼───────────────┤
│ ⚠ LANDOWNER BELIEFS                 │ NOT IN       │ Served by     │
│ (LANDOWNER_CORPORATE /               │ CHROMADB     │ gbim_query_   │
│  LANDOWNER_GOVERNMENT)               │              │ router (7205) │
│                                      │              │ PostgreSQL    │
│                                      │              │ native path   │
└──────────────────────────────────────┴──────────────┴───────────────┘
```

> Figure 00-3. ChromaDB collection inventory, March 26, 2026. ★ **UPDATED:** All six previously sparse or missing RAG collections are now fully populated and semantically verified (OI-12 through OI-20 closed). `governance_rag` contains the complete MountainShares DAO corpus plus the full US Constitution (Project Gutenberg pg5.txt). `commons_rag` contains the full Commons governance and gamification corpus. Semantic retrieval smoke-tested: BSA → SNAP/Medicaid/TANF ✅; constitutional rights → Amendment XIV ✅; Daily Life Game → Contribution Game + Participation Map ✅; governance rules → DAO Terms + Phase 0 Audit ✅.

---

## 00.5 Database Infrastructure Summary

```
┌─────────────────────────────────────────────────────────────────────┐
│          Ms. Jarvis Database Infrastructure — March 26, 2026        │
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
│                         │        │ redteam_sessions + feedback tbls │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ ChromaDB                │ 8002   │ ✅ Docker (jarvis-chroma)        │
│ (vector store)          │ (host) │ host port 8002 → container 8000  │
│                         │        │ all-minilm:latest (384-dim)      │
│                         │        │ cosine similarity space          │
│                         │        │ 100-word chunk constraint        │
│                         │        │ v2 API active ★                  │
│                         │        │ RAG collections fully populated ★│
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Redis                   │ 6380   │ ✅ Docker (jarvis-redis)         │
│ (cache + session)       │ (host) │ host port 6380 → container 6379  │
│                         │        │ Async job status key: 'complete' │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Neo4j                   │ 7474 / │ ✅ Docker                        │
│ (graph)                 │ 7687   │ Graph relationships + GBIM links │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ MySQL                   │ 3307   │ ✅ Host — Running                │
│                         │        │ ⚠ Schema dump not yet in docs/  │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ jarvis-auth-service ★   │ 8055   │ ✅ systemd (NOT Docker Compose)  │
│ (standalone auth)       │        │ FastAPI — Redis 6380 (host)      │
│                         │        │ Token TTL: 30 days               │
│                         │        │ UI-initiated only ⚠              │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Caddy reverse proxy ★   │ 8443   │ ✅ systemd (NOT Docker Compose)  │
│                         │        │ Version: 2.6.2 (Ubuntu package)  │
│                         │        │ ⚠ NOT xcaddy — no caddy-ratelimit│
│                         │        │ ⚠ NO forward_auth support        │
│                         │        │ CORS: Access-Control-Allow-      │
│                         │        │   Origin "*" — active ✅         │
├─────────────────────────┼────────┼──────────────────────────────────┤
│ Cloudflare Tunnel ★     │ —      │ ✅ systemd (NOT Docker Compose)  │
│                         │        │ Tunnel name: msjarvis            │
│                         │        │ UUID: 42ef9893-f4df-4cc5-        │
│                         │        │       8881-bb55b995e022          │
│                         │        │ TLS: Cloudflare terminates ✅    │
└─────────────────────────┴────────┴──────────────────────────────────┘
```

> Figure 00-4. Database and external service infrastructure summary, March 26, 2026.

---

## 00.6 Full Pipeline Flow (March 26, 2026)

The production query pipeline as of March 26, 2026. Validated through first public end-to-end test (March 22, 2026) and consciousness pipeline confirmation (March 25, 2026). RAG corpus fully populated March 26, 2026.

```
User Query (browser at https://egeria.mountainshares.us)
    ↓
Cloudflare Tunnel (HTTPS/QUIC → Legion localhost)
    TLS terminated by Cloudflare ✅
    ↓
Caddy (port 8443) — v2.6.2 Ubuntu package
    CORS headers applied
    Route: /chat* → 127.0.0.1:8050
    ⚠ Caddy does NOT enforce token validation (OI-36-A)
    ↓
jarvis-auth-service (port 8055) — UI-initiated token validation only
    ↓ (chat requests proceed regardless of auth state — known gap OI-36-A)
Unified Gateway (port 8050)
    dict.lower() guard patched March 25, 2026 ★
    ↓
BBB Input Filter (port 8016) — Phase 1.4 — BLOCKING ✅
    ↓ (content_approved=True)
Main Brain (port 8010)
    │
    ├── Phase 1.45: Community Memory Retrieval
    │     autonomous_learner (ChromaDB port 8002)
    │
    ├── Phase 2: Multi-agent, web research, spatial, GBIM
    │     GIS RAG (port 8005)
    │     GBIM Landowner Router (port 7205) — PostgreSQL-native
    │     Text RAG / jarvis-rag-server (port 8003→8016) ★
    │       governance_rag: 643 chunks ✅
    │       commons_rag: 306 chunks ✅
    │       All RAG collections fully populated ★
    │       ⚠ Gateway wiring to inference endpoint pending
    │
    ├── [EEG HEARTBEAT] ★ ALL LIVE
    │     eeg-delta: 30s cadence — 1 pulse confirmed ✅
    │     eeg-theta: 60s cadence — 486 pulses confirmed ✅
    │     eeg-beta:  5-min cadence, topic: Appalachian ✅
    │
    ├── [CONSCIOUSNESS PIPELINE] ★ ACTIVE
    │     jarvis-consciousness-bridge (port 8020) ✅
    │     jarvis-woah (port 7012) ✅
    │     jarvis-rag-server (port 8016) ⚠ embedder fix pending
    │
    ├── Phase 2.5: 21-LLM Ensemble (ports 8201–8222)
    │     ~88–115s (GPU, RTX 4070)
    │
    ├── Phase 3: Judge Pipeline
    │     jarvis-judge-truth (7230), -consistency (7231)
    │     jarvis-judge-alignment (7232), -ethics (7233)
    │
    ├── Phase 3.5: LM Synthesizer (port 8001)
    │     Persona injection — no model name leakage ✅
    │
    └── Phase 4.5: BBB Output Filter (port 8016 — same service)
          LOG+PASSTHROUGH mode ⚠ (recalibration pending OI-02)
    ↓
Response → Caddy → Cloudflare Tunnel → User browser
```

> Figure 00-5. Full production pipeline flow, March 26, 2026. ★ RAG corpus fully populated — `governance_rag` (643 chunks) and `commons_rag` (306 chunks) semantically verified. Gateway wiring of RAG collections to inference endpoint remains pending next sprint.

---

## 00.7 Service Count History

| Date | Services | Notable Addition / Change |
|---|---|---|
| Initial deployment | 79 | Core stack |
| Pre-March 14, 2026 | 82 | Phase 1.45 community memory services added |
| March 14, 2026 | 83 | `psychological-rag` (port 8006) promoted to production |
| March 19, 2026 | 84 | Spatial infrastructure services finalized |
| March 20, 2026 | 85 (reported) | `gbim_query_router` (port 7205) — landowner belief layer live |
| March 21–22, 2026 | **83 (verified)** | 3 orphaned containers added to `docker-compose.yml`; verified compose count: 83 |
| March 22, 2026 | **83 compose + 3 systemd** | Caddy, jarvis-auth, cloudflared as systemd; public URL live |
| March 22–25, 2026 | **83 compose + 3 systemd** | Consciousness pipeline sprint — WOAH, bridge, rag-server patched and active |
| March 26, 2026 | **56 confirmed (msjarvis-rebuild)** | RAG corpus completion sprint — all collections populated; EEG heartbeats confirmed; rebuild namespace active |

---

## 00.8 System Health Snapshot — March 26, 2026 ★ UPDATED

| Metric | Value | Verified |
|---|---|---|
| **Total containers (msjarvis-rebuild namespace)** | **56 ★** | **March 26, 2026** |
| External systemd services | **3** (Caddy, jarvis-auth, cloudflared) | March 22, 2026 |
| Public HTTPS URL | **https://egeria.mountainshares.us** | March 22, 2026 |
| Pipeline speed (single-user, GPU) | **~100–107s** | March 22, 2026 |
| LLM models contributing | **21/21** | March 22, 2026 |
| Preflight gate | **24 PASS 0 FAIL** | March 25, 2026 |
| **EEG eeg-delta** | **1 pulse — 30s cadence ★** | **March 26, 2026** |
| **EEG eeg-theta** | **486 pulses — 60s cadence ★** | **March 26, 2026** |
| **EEG eeg-beta** | **1 pulse — 5-min, topic: Appalachian ★** | **March 26, 2026** |
| **governance_rag** | **643 chunks ★** | **March 26, 2026 — OI-19 CLOSED** |
| **commons_rag** | **306 chunks ★** | **March 26, 2026 — OI-20 CLOSED** |
| **geospatialfeatures** | **60,000 items ★** | **March 26, 2026 — OI-12 CLOSED** |
| **GBIM_Fayette_sample** | **1,535 items ★** | **March 26, 2026 — OI-13 CLOSED** |
| **appalachian_cultural_intelligence** | **820 items ★** | **March 26, 2026 — OI-14 CLOSED** |
| **spiritual_texts** | **19,338 items ★** | **March 26, 2026 — OI-15 CLOSED** |
| GBIM beliefs (`gbimbeliefnormalized`) | **5,416,522** | March 20, 2026 |
| — of which: landowner beliefs | **20,593** | March 20, 2026 |
| `autonomous_learner` items | **21,181+** | March 20, 2026 |
| `psychological_rag` items | **968** | March 20, 2026 |
| `msjarvis_docs` items | **2,348** | March 22, 2026 |
| Embedding model | **all-minilm:latest (384-dim, cosine)** | Confirmed |
| Chunk constraint | **100 words max, 20-word overlap** | March 26, 2026 |
| ChromaDB API version | **v2 active — v1 returns 410** | March 25, 2026 |
| Consciousness pipeline | **ACTIVE** | March 25, 2026 |
| MountainShares services (8080–8084) | **❌ NOT DEPLOYED** | March 22, 2026 |
| BBB output filter mode | **log+passthrough** (not blocking) | March 22, 2026 |
| Cloudflare Tunnel UUID | **42ef9893-f4df-4cc5-8881-bb55b995e022** | March 22, 2026 |
| Rebuild namespace | **msjarvis-rebuild** | March 26, 2026 |

---

## 00.9 Sprint Progress Log

| Sprint | Dates | Items Closed | Status |
|---|---|---|---|
| Landowner belief sprint | March 20, 2026 | `gbim_query_router` promoted; 20,593 landowner beliefs ingested; `mvw_gbim_landowner_spatial` live | ✅ Complete |
| Red team hardening sprint | March 21–22, 2026 | Orphaned containers added to compose; systemd services deployed; public URL live; first public end-to-end test PASS | ✅ Complete |
| Consciousness pipeline restoration sprint | March 22–25, 2026 | WOAH fixed; Chroma v2 migration; RAG server corrected; gateway crash guard; end-to-end chat ACTIVE | ✅ Complete — RAG embedder restart pending |
| RAG corpus completion sprint | March 26, 2026 | OI-12 through OI-20 closed; all RAG collections fully populated; EEG heartbeats confirmed; semantic retrieval smoke-tested across all four RAG domains; US Constitution ingested (97 chunks); rebuild namespace `msjarvis-rebuild` confirmed at 56 containers | ✅ Complete |

---

*Last updated: 2026-03-26, Carrie Kidd (Mamma Kidd), Mount Hope WV*
*Public URL: https://egeria.mountainshares.us*
*Rebuild namespace: msjarvis-rebuild — 56 containers confirmed live*
````
