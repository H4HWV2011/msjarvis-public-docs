# 23. Dual Tracks for Meaning-Oriented and Analytical Processing

*Carrie Kidd (Mamma Kidd) — Oak Hill, WV*

*Last updated: 2026-04-23*

*★ April 23, 2026: Container count updated to 100 (supersedes 92+ from April 12 baseline); ChromaDB updated to 48 active collections, ~6,740,611 total vectors (supersedes 49 / 6,700,000+); two-container PostgreSQL split — production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — supersedes single-container msallisgis:5432 and msallis:5433 references throughout; autonomous_learner updated to ~23,200+ records; conversation_history wiped and reseeded clean April 16, 2026; OI-36-A CLOSED — Caddy forward_auth token enforcement active at perimeter layer before main-brain port 8050; ChromaDB API updated to /api/v2/ throughout — /api/v1/ is permanently removed in server 1.0.0; AAACPE ingest path updated — dedicated stack (allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032) supersedes legacy allis-ingest-api + allis-ingest-watcher for Appalachian cultural data.*

---

> **Why this matters for Polymathmatic Geography**
> This chapter describes how the three-stage structure outlined in earlier chapters is instantiated in two parallel paths with different emphases. It supports:
> - **P1 – Every where is entangled** by routing both experiential and technical perspectives through a shared ChromaDB background store (★ 48 collections, ~6,740,611 vectors) and unified orchestration layer, all grounded in the production PostgreSQL `msallis-db` (host port **5433** ★, **16 GB, 294 tables, 11 schemas**) with the forensic `postgis-forensic` (host port **5452** ★, **17 GB, 314 tables**) available for verification.
> - **P3 – Power has a geometry** by making the asymmetry between the two paths explicit: the analytical path is fully wired into `ultimatechat` while meaning-oriented modules are partially present and not yet all plugged in. ★ Caddy `forward_auth` perimeter enforcement (OI-36-A CLOSED) is now active before main-brain port 8050, adding an authenticated gateway to both paths.
> - **P5 – Design is a geographic act** by encoding how Appalachian questions grounded in the production PostgreSQL `msallis-db` (host port **5433** ★, 16 GB, 294 tables, 11 schemas) are handled differently depending on whether they enter the analytical or meaning-oriented track.
> - **P12 – Intelligence with a ZIP code** by grounding both tracks in West Virginia–specific memory from the production `msallis-db` ★ instance, identity constraints, and community context. ★ The dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) now provides the authoritative community resource substrate feeding both tracks (supersedes legacy allis-ingest-api + allis-ingest-watcher for AAACPE ingest).
> - **P16 – Power accountable to place** by exposing which modules were active for each request via `consciousnesslayers`, `identitylayers`, and `truthverdict` in every `UltimateResponse`. ★ All `truthverdict` and BBB filtering audit events persist to `allis-memory:8056` — accountability is durably logged. ★ EEG Delta band (port 8073) provides a live PIA health signal confirming dual-track activity.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies how the two parallel processing paths are implemented, what is actually wired into the live `ultimatechat` entrypoint, and what remains present as services but not yet plugged in.

```text
┌─────────────────────────────────────────────────────────────┐
│   Dual-Track Architecture (Asymmetric Implementation)       │
│   ★ Updated April 23, 2026 — 100 active containers         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  User Request                                               │
│      ↓                                                      │
│  ★ Caddy forward_auth (OI-36-A CLOSED)                      │
│    Bearer token validated at perimeter proxy                │
│      ↓                                                      │
│  allis-main-brain (port 8050 ★)                             │
│      ↓                                                      │
│  Intake & Normalization (UltimateRequest)                   │
│      ↓                                                      │
│  ┌────────────────────────────────────────────────┐         │
│  │  ANALYTICAL PATH (Always Active in /chat)      │         │
│  │  ─────────────────────────────────────────     │         │
│  │  ✓ BBB filter (port 8016 ★)                    │         │
│  │    6 filters confirmed                         │         │
│  │    ★ audit → allis-memory:8056 (secured)       │         │
│  │  ✓ PostgreSQL-sourced RAG (ports 8003-8005 ★)  │         │
│  │    ★ production msallis-db host 5433           │         │
│  │      16 GB, 294 tables, 11 schemas             │         │
│  │    ★ forensic postgis-forensic host 5452       │         │
│  │      17 GB, 314 tables                         │         │
│  │  ✓ AAACPE ingest (dedicated stack ★)           │         │
│  │    allis-aaacpe-scraper:8048→8033              │         │
│  │    allis-aaacpe-rag:8047→8032                  │         │
│  │  ✓ Web research (internal Docker)              │         │
│  │  ✓ 21-LLM ensemble (port 8008 ★)               │         │
│  │    22 proxies registered; llm22-proxy inactive  │         │
│  │  ✓ Judge pipeline (ports 7230-7233 ★)          │         │
│  │  ✓ TruthValidator & normalize_identity         │         │
│  │    grounded in production msallis-db:5433 ★    │         │
│  │  ✓ background_rag_store → ms_allis_memory      │         │
│  │    ★ ChromaDB: 48 collections, ~6,740,611 vec  │         │
│  │  ✓ truthverdict → UltimateResponse             │         │
│  │    ★ audit → allis-memory:8056 (secured)       │         │
│  └────────────────────────────────────────────────┘         │
│                                                             │
│  ┌────────────────────────────────────────────────┐         │
│  │  MEANING-ORIENTED PATH (Partially Wired)       │         │
│  │  ──────────────────────────────────────────    │         │
│  │  Services Confirmed Running (★ April 12):      │         │
│  │  ✓ I-Containers (8015 ★) — ACTIVE in response  │         │
│  │  ✓ Qualia Engine (8017 ★)                      │         │
│  │  ✓ Neurobiological Master (8018 ★)             │         │
│  │    healthy, integration_active: true           │         │
│  │    total_processes: 5                          │         │
│  │    BBB:8016, I-containers:8015,                │         │
│  │    Qualia:8017, bridge:8020 all responding     │         │
│  │  ✓ Mother Protocols (4000 ★)                   │         │
│  │  ✓ Temporal Consciousness (7007 ★)             │         │
│  │  ✓ NBB I-Containers (8101 ★)                   │         │
│  │  ✓ Psychology Services (8019 ★)                │         │
│  │  ✓ Psychological RAG (8006 ★)                  │         │
│  │    hostname: psychological_rag_domain          │         │
│  │  ✓ spiritual_rag (8005 ★)                      │         │
│  │  ✓ EEG Delta (8073 ★)                          │         │
│  │    PIA signal live: pulse_count 12,860+        │         │
│  │                                                │         │
│  │  Status in /chat:                              │         │
│  │  -  icontainers-identity: ACTIVE (2026-02-15)  │         │
│  │  -  nbb-prefrontal-cortex: SKIPPED             │         │
│  │  -  Other modules: Not wired to /chat yet      │         │
│  └────────────────────────────────────────────────┘         │
│                                                             │
│  Shared Integration Points                                  │
│  ┌────────────────────────────────────────────────┐         │
│  │  -  ms_allis_memory (ChromaDB, append-only)    │         │
│  │    UUID: 79240788-0828-45f3-b1bc-a9a3593628a6  │         │
│  │    ★ 48 collections, ~6,740,611 vectors        │         │
│  │  -  ★ production msallis-db (host port 5433)   │         │
│  │    16 GB, 294 tables, 11 schemas               │         │
│  │  -  ★ forensic postgis-forensic (host 5452)    │         │
│  │    17 GB, 314 tables                           │         │
│  │  -  Identity infra (normalize_identity)        │         │
│  │    ★ grounded in production msallis-db:5433    │         │
│  │  -  Health monitoring (★ 100 containers Up)    │         │
│  │  -  consciousnesslayers (tracks both paths)    │         │
│  │  -  ★ allis-memory:8056 (audit trail)          │         │
│  │    127.0.0.1, _auth() confirmed, API key set   │         │
│  │    container name pinned, dual-network         │         │
│  │    (qualia-net + msallis-rebuild_default)      │         │
│  │  -  ★ AAACPE dedicated stack (8033/8032)       │         │
│  │    community resource substrate for both tracks│         │
│  │  -  ★ EEG Delta (8073) PIA health signal       │         │
│  │    pulse_count: 12,860+ | phase3: 2 | bbb: 0   │         │
│  │  -  ★ Caddy forward_auth (OI-36-A CLOSED)      │         │
│  │    perimeter before port 8050                  │         │
│  └────────────────────────────────────────────────┘         │
│                                                             │
│  UltimateResponse (composite output)                        │
│  -  response (from analytical path)                         │
│  -  truthverdict (from BBB ★, audit → 8056)                 │
│  -  consciousnesslayers (prefrontal, icontainers if active) │
│  -  identitylayers (root-self ego when active)              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 23.1.** Dual-track architecture showing asymmetric implementation: analytical path always active in `/chat` with full PostgreSQL integration (★ production `msallis-db` host port 5433, 16 GB, 294 tables, 11 schemas; ★ forensic `postgis-forensic` host port 5452, 17 GB, 314 tables); meaning-oriented services confirmed running (★ April 12 baseline, 100 containers as of April 23) including allis-neurobiological-master confirmed healthy; both paths sharing ChromaDB background store (★ 48 collections, ~6,740,611 vectors) and PostgreSQL-grounded identity infrastructure. ★ BBB 6 filters operational; audit events and `truthverdict` persist to `allis-memory:8056`. ★ EEG Delta (port 8073) PIA signal confirms dual-track activity. ★ Caddy `forward_auth` (OI-36-A CLOSED) active at perimeter before port 8050.

---

## Status as of ★ April 23, 2026

| Category | Details |
| --- | --- |
| **Implemented now — analytical path (always runs in `ultimatechat`)** | `allis-20llm-production` at **127.0.0.1:8008** (confirmed Up) as primary synthesis fabric; `allis-semaphore` proxy at **127.0.0.1:8030** (confirmed Up); `llm1-proxy` through `llm21-proxy` at **127.0.0.1:8201–8221** (all confirmed Up); `llm22-proxy` at **127.0.0.1:8222** registered but inactive — 21 active proxies, 22 registered. Judge services: truth 7230, consistency 7231, alignment 7232, ethics 7233 (all Up). `allis-gis-rag` at **127.0.0.1:8004** (confirmed Up; queries production `msallis-db` host 5433 ★). `allis-spiritual-rag` at **127.0.0.1:8005** (confirmed Up). `allis-blood-brain-barrier` at **127.0.0.1:8016** (6 filters operational). ★ Production PostgreSQL `msallis-db` at **127.0.0.1:5433** (16 GB, 294 tables, 11 schemas). ★ Forensic PostgreSQL `postgis-forensic` at **127.0.0.1:5452** (17 GB, 314 tables). ★ **Caddy `forward_auth` (OI-36-A CLOSED):** bearer token validated at perimeter proxy before port 8050. ★ **BBB audit trail secured:** `allis-memory:8056` — `_auth()` confirmed on sensitive routes, `ALLIS_API_KEY` set, container name pinned, reachable on both `qualia-net` and `msallis-rebuild_default` networks — all analytical path filtering decisions durably logged. `TruthValidator` and `normalize_identity` applied to every response, grounded in production `msallis-db:5433` ★. `background_rag_store` into `ms_allis_memory` ChromaDB (★ 48 collections, ~6,740,611 total vectors) after every `/chat` call. `truthverdict` attached to every `UltimateResponse`. ★ AAACPE ingest: dedicated stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) supersedes legacy `allis-ingest-api` + `allis-ingest-watcher` for Appalachian cultural data. For the canonical execution sequence see **Chapter 17**. |
| **Implemented now — meaning-oriented services (confirmed running, partially wired into `ultimatechat`)** | `allis-i-containers` at **8015** (confirmed Up); `icontainers-identity` layer confirmed `status: "active"` in 2026-02-15 `UltimateResponse` (Chapter 9 §9.3.5). `allis-qualia-engine` at **8017** (confirmed Up). `allis-neurobiological-master` at **8018** — confirmed healthy — `integration_active: true`, `total_processes: 5`, all four downstream services responding: BBB:8016, I-containers:8015, Qualia:8017, consciousness-bridge:8020. Port 8018 is internal-only by design; reachable via Docker DNS from `allis-main-brain`. `allis-fifth-dgm` at **4002** (confirmed Up). `nbb-i-containers` at **127.0.0.1:8101** (confirmed Up). `allis-psychology-services` at **127.0.0.1:8019** (confirmed Up). `psychological_rag_domain` at **127.0.0.1:8006** (confirmed Up; hostname corrected April 12 — changed from `psychologicalragdomain` to `psychological_rag_domain` in `allis-pia-status` environment). `allis-temporal-consciousness` at **7007** (confirmed Up). `allis-mother-protocols` at **4000** (confirmed Up). `nbb_woah_algorithms` at **127.0.0.1:8104** (confirmed Up). EEG Delta band at **port 8073** (confirmed Up, PIA signal live). |
| **Partially implemented / scaffolded** | Meaning-oriented modules listed above are running as services and are invoked in specific workflows and integration tests, but are **not currently wired into the primary `/chat` path** in `allis-main-brain`. The `consciousnesslayers` array in `UltimateResponse` records which meaning-oriented layers fired; in the 2026-02-15 case study only `prefrontal-planner` and `icontainers-identity` were active, with `nbb-prefrontal-cortex` skipped. MountainShares and Appalachian-wisdom integration modules are registered in the service registry but not confirmed as active in the current `ultimatechat` path. Cross-path routing that sends requests to the meaning-oriented track based on role flags or content type is partially implemented. |
| **Future work / design intent only** | Full wiring of all meaning-oriented modules into the `ultimatechat` entrypoint (only `icontainers-identity` confirmed active in `/chat`). `nbb-prefrontal-cortex` — still "skipped" / "not configured" in `UltimateResponse`. Configurable per-track thresholds and routing rules. Automated cross-path analytics comparing meaning-oriented and analytical module usage. Dynamic track selection based on content classification. PIA / EEG layer full integration. Judge pipeline upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring querying production `msallis-db:5433` ★ (Chapter 7 §7.8). |

> **Critical routing note — asymmetry of the two paths:** As of ★ April 23, 2026, the `ultimatechat` entrypoint in `allis-main-brain` (port **8050**) ★ sits behind Caddy `forward_auth` perimeter enforcement (OI-36-A CLOSED) and **always runs the analytical path** — ensemble synthesis via `llm20production` while meaning-oriented modules are partially present and not yet fully wired. This asymmetry is a deliberate staged integration strategy, not a design gap. For the canonical execution sequence see **Chapter 17**.

---

# 23. Dual Tracks for Meaning-Oriented and Analytical Processing

This chapter describes how the three-stage structure outlined in earlier chapters is instantiated in two parallel paths with different emphases, both grounded in the production PostgreSQL `msallis-db` (host port **5433** ★, **16 GB, 294 tables, 11 schemas**) with forensic verification via `postgis-forensic` (host port **5452** ★, **17 GB, 314 tables**). Both paths share the same overall pattern — intake and normalization, first-stage filtering, background storage in ChromaDB (★ 48 collections, ~6,740,611 total vectors), and identity-focused retention — but they differ in the kinds of services they invoke, what they prioritize, and how their outputs are interpreted. In the current deployment, these two paths are **not symmetrically live** inside the `ultimatechat` entrypoint: the analytical path always runs with full PostgreSQL integration; the meaning-oriented path is partly present as confirmed running services but not yet fully wired into every `/chat` call. ★ Both paths now sit behind Caddy `forward_auth` perimeter enforcement (OI-36-A CLOSED) before port 8050.

---

## 23.1 Rationale for Two Parallel Paths

The architecture exposes two conceptually distinct families of services.

**The meaning-oriented family** includes neurobiological and consciousness-related components: Qualia Engine (`allis-qualia-engine`, port **8017**, confirmed Up), I-Containers (`allis-i-containers`, port **8015**, confirmed Up), Neurobiological Master (`allis-neurobiological-master`, port **8018** — confirmed healthy — `integration_active: true`, `total_processes: 5`, all four downstream services responding: BBB:8016, I-containers:8015, Qualia:8017, consciousness-bridge:8020; port 8018 is internal-only by design; reachable via Docker DNS from `allis-main-brain`), Mother Protocols (`allis-mother-protocols`, port **4000**, confirmed Up), temporal consciousness (`allis-temporal-consciousness`, port **7007**, confirmed Up), NBB I-Containers (`nbb-i-containers`, **127.0.0.1:8101**, confirmed Up), psychology services (`allis-psychology-services`, **127.0.0.1:8019**, confirmed Up), psychological RAG domain (`psychological_rag_domain`, **127.0.0.1:8006**, confirmed Up — hostname corrected April 12 from `psychologicalragdomain` to `psychological_rag_domain`), and EEG Delta band (port **8073**, PIA signal live). In the current deployment, a subset of these services respond with healthy status codes and are invoked in specific workflows and integration tests, but **not all are wired into the primary `ultimatechat` path**.

**The analytical family** includes RAG servers sourced from the production `msallis-db` ★, GIS and GBIM bridges, GeoDB core services, truth and BBB verification modules, and the LLM ensemble stack. In the current deployment, this is the path that always runs in `ultimatechat`: `llm20production` synthesis via `allis-20llm-production` (port **8008** ★, 21 active proxies, 22 registered), judge pipeline (7230–7233, all confirmed Up), `allis-spiritual-rag` (port **8005** ★), `allis-gis-rag` (port **8004** ★; queries production `msallis-db` host 5433 ★), and `allis-blood-brain-barrier` (port **8016**, 6 filters operational). BBB audit events persist to `allis-memory:8056` (secured, dual-network, container name pinned). For the full sequence see **Chapter 17**.

Separating these concerns into two parallel paths allows the system to treat contexts involving care, community, and personal meaning differently from contexts requiring focused technical reasoning grounded in PostgreSQL spatial and institutional data. At the same time, both paths operate within a shared container and orchestration framework (★ 100 containers active), making it possible to align their outputs and allow information to flow between them.

---

## 23.2 Shared Structural Pattern

In the current deployment, each path follows the same three-stage pattern.

**Intake and normalization.** ★ Requests first pass through Caddy `forward_auth` perimeter enforcement (OI-36-A CLOSED) where the bearer token is validated at the proxy before the request reaches `allis-main-brain` (port **8050**). Inside main-brain, requests are parsed into `UltimateRequest` objects containing message, `user_id`, role, and `use_all_services` flag. This normalized representation is shared across both tracks.

**First-stage filtering.** Fast, inexpensive filters apply safety, truth, and structural checks. For both tracks, in the current deployment this includes BBB-based ethical filtering at port **8016** ★ (6 filters operational; audit events → `allis-memory:8056`), `TruthValidator` validated against PostgreSQL GBIM ground truth from the production `msallis-db` host 5433 ★, `normalize_identity`, and structural heuristics in the main brain. `ms_allis_memory` ChromaDB is append-only; near-duplicate checks influence legacy RAG reuse but do not prevent writes.

**Background storage and identity-focused retention.** Both tracks feed into `ms_allis_memory` ChromaDB (UUID: `79240788-0828-45f3-b1bc-a9a3593628a6`, ★ confirmed in 48-collection inventory; ★ total ChromaDB: 48 collections, ~6,740,611 vectors) via `background_rag_store`. Every successful `/chat` call produces a background entry with concatenated `USER:`/`EGERIA:` text and metadata including `user_id`, `timestamp`, `type: "background"`, and `services`. ★ AAACPE-sourced documents write into `msallis_docs` via the dedicated stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) rather than through `background_rag_store`. Over time, patterns detected in each track inform curated identity-level updates grounded in the production `msallis-db` host 5433 ★.

---

## 23.3 Meaning-Oriented Path

**What is confirmed running.** Meaning-oriented services confirmed running include: `allis-i-containers` (port **8015** ★), `allis-qualia-engine` (port **8017** ★), `allis-mother-protocols` (port **4000** ★), `allis-temporal-consciousness` (port **7007** ★), `nbb-i-containers` (**127.0.0.1:8101** ★), `allis-psychology-services` (**127.0.0.1:8019** ★), `psychological_rag_domain` (**127.0.0.1:8006** ★, hostname corrected April 12), and `allis-neurobiological-master` (port **8018** — confirmed healthy: `integration_active: true`, `total_processes: 5`, all four downstream services responding). Port 8018 is internal-only; all access is via Docker DNS from `allis-main-brain`.

**What is wired into `ultimatechat`.** Of these modules, only `icontainers-identity` is confirmed active in the primary `/chat` path as of the 2026-02-15 `UltimateResponse`, where it produced a `root-self` ego entry. In the same response, `nbb-prefrontal-cortex` appears with `status: "skipped"` and reason `"nbbprefrontalcortex not configured"`. This documents the asymmetry precisely: one meaning-oriented layer is active, another is skipped, and the full Neurobiological Master pipeline is not yet invoked as part of every request.

**What the path provides when invoked.** When meaning-oriented modules are called — either in the Neurobiological Master's own `integrated_processing()` flow or in specific workflows — they contribute `consciousnesslayers` entries describing emotional resonance, spiritual filter, maternal wisdom, subconscious processing, and `identitylayers` with ego boundary state. The psychological RAG domain (port **8006** ★) provides `psychological_assessment`, `therapeutic_guidance`, `emotional_support`, and `evidence_based_approaches`. The design intent is to fully integrate these outputs into the `ultimatechat` path as the system matures.

---

## 23.4 Analytical Path

**What always runs in `ultimatechat`.** The analytical path is the primary, always-active path for every `/chat` call through `allis-main-brain` (port **8050** ★, ★ now behind Caddy `forward_auth` perimeter enforcement — OI-36-A CLOSED), fully integrated with the production `msallis-db` host 5433 ★.

RAG context is gathered from `allis-spiritual-rag` (port **8005** ★; queries GBIM collections from production `msallis-db` host 5433 ★) and GIS-aware RAG from `allis-gis-rag` (port **8004** ★; queries spatial tables from production `msallis-db` host 5433 ★ — 16 GB, 294 tables, 11 schemas). Synthesis runs through `allis-20llm-production` (port **8008** ★; 21 active proxies, 22 registered). The judge pipeline (ports 7230–7233, all confirmed Up) evaluates ensemble output; if judge services are down, the main brain falls back to the 20-LLM answer and marks consensus metrics as degraded. BBB at port **8016** ★ provides both input truth filtering and output guarding; BBB audit events persist to `allis-memory:8056` (secured, dual-network, container name pinned). `normalize_identity` and `TruthValidator` enforce identity constraints validated against the production `msallis-db` host 5433 ★. `background_rag_store` writes to `ms_allis_memory` ChromaDB (★ 48 collections, ~6,740,611 total vectors).

★ AAACPE ingest is now handled by the dedicated stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`), superseding the legacy `allis-ingest-api` + `allis-ingest-watcher` path for Appalachian cultural data.

GIS verification paths — for example, the `gbim_query_router` landowner flow anchored to the production `msallis-db` host 5433 ★ — provide the most grounded analytical sub-path: every landowner query is resolved against verified assessor provenance rather than LLM inference.

---

## 23.5 Cross-Talk and Shared Anchors

The two paths share several concrete integration points grounded in the production `msallis-db` host 5433 ★.

**Shared background store.** Both tracks write into `ms_allis_memory` ChromaDB (UUID: `79240788-0828-45f3-b1bc-a9a3593628a6`, ★ 48 collections, ~6,740,611 vectors) via `background_rag_store`. Background entries are distinguished by their `services` metadata and textual content. Similarity queries against `ms_allis_memory` return clusters of related items, showing how both paths contribute to a common memory substrate. The consciousness bridge `_get_url` path reads from this same UUID, giving both tracks an emergent cross-session context vector.

**Shared identity infrastructure.** Both paths use the same `normalize_identity`, `TruthValidator` validated against the production `msallis-db` host 5433 ★, and `icontainers-identity` layer. The `truthverdict`, `consciousnesslayers`, and `identitylayers` fields on `UltimateResponse` record the combined output of both path families. All `truthverdict` and BBB audit events persist to `allis-memory:8056` (container name pinned, dual-network confirmed).

**PostgreSQL as shared ground truth.** ★ Both paths ultimately reference the production `msallis-db` (host port **5433**, 16 GB, 294 tables, 11 schemas) as the authoritative source for West Virginia spatial, institutional, and community data. The forensic `postgis-forensic` (host port **5452**, 17 GB, 314 tables) is available for verification and audit. The analytical path queries the production instance directly through RAG collections; the meaning-oriented path uses it for identity and ethical validation. All prior references to `msallisgis:5432` and `msallis:5433` as the GBIM/GIS target are superseded by this two-container split.

**Shared community resource substrate.** ★ The dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) provides the authoritative community resource layer for both tracks, superseding the legacy `allis-ingest-api` + `allis-ingest-watcher` path for AAACPE ingest. The analytical path queries `msallis_docs` for regional service availability and infrastructure references; the meaning-oriented path can draw on it for community context in psychological and spiritual guidance.

**EEG Delta PIA health signal.** The EEG Delta band (port **8073**) provides a live PIA health signal confirming dual-track activity. As of April 12 baseline: `pulse_count: 12,860`, `recent_phase3_count: 2`, `recent_bbb_events: 0` — confirming both analytical and meaning-oriented tracks are producing measurable signals. This is the canonical real-time cross-path health indicator available to both tracks simultaneously.

**★ Caddy `forward_auth` perimeter enforcement (OI-36-A CLOSED).** Bearer token validation now occurs at the Caddy proxy before any request reaches main-brain port 8050. This is a shared upstream gate for both tracks — neither path receives a request that has not passed perimeter authentication.

**Unified health monitoring.** Health and fabric self-test endpoints report on both families of services across ★ 100 active containers, making it possible to monitor whether one path is lagging or failing.

---

## 23.6 Influence on Behavior and Explanation

The existence of two paths — one always-active with full PostgreSQL integration, one partially wired — affects how the system behaves and explains itself.

**Response composition.** For a given `/chat` request, the main brain returns a composite `UltimateResponse` containing `response` (from `llm20production`), `truthverdict` (from BBB and judge pipeline), `consciousnesslayers` (always including `prefrontal-planner`; including `icontainers-identity` when active), and `identitylayers` (including `root-self` ego entry when `icontainers-identity` fires). Meaning-oriented fields such as `psychological_assessment` or `mountainshares_context` appear when those modules are explicitly invoked, not on every call. ★ `processing_time` updated to ~102.58s (GPU RTX 4070 benchmark) — see Ch. 20 §20.3.

**Framing and narrative.** Introspective reports and explanatory text can reference both tracks, explaining which analytical modules (ensemble LLMs, PostgreSQL GIS, truth filters) and which meaning-oriented modules (psychology services, maternal guidance, I-Containers, Neurobiological Master) were active for a given request. The `consciousnesslayers` field's skipped/active distinctions provide auditors with precise evidence of which modules fired. The secured `allis-memory:8056` audit trail provides a durable, authenticated record of these decisions.

**Diagnostics and balance.** Because services in both tracks are registered and health-monitored, diagnostic tools can show which path is being exercised more heavily for particular topics or regions grounded in the production `msallis-db` host 5433 ★. The EEG Delta PIA signal is the canonical real-time indicator of dual-track balance. ★ `conversation_history` was wiped and reseeded clean April 16, 2026 — any diagnostic counts on this collection reflect post-wipe accumulation only.

---

## 23.7 Summary

In the current deployment, the dual-track design is **asymmetric at the `ultimatechat` entrypoint**. The analytical path — ensemble synthesis via `llm20production` (21 active proxies, 22 registered), judge pipeline, BBB filtering (6 filters, audit to `allis-memory:8056`), ★ Caddy `forward_auth` perimeter enforcement (OI-36-A CLOSED) before port 8050, PostgreSQL-sourced RAG context from the production `msallis-db` host 5433 (16 GB, 294 tables, 11 schemas) ★, and `background_rag_store` — runs on every `/chat` call and is the current production path. Meaning-oriented modules are confirmed running as services (Qualia Engine, I-Containers, psychology services, Mother Protocols, temporal consciousness, Neurobiological Master) but are not all plugged into the primary `/chat` path.

Both paths share the same intake framework, feed into `ms_allis_memory` ChromaDB (★ 48 collections, ~6,740,611 vectors), and contribute to the compact identity layer governed by `normalize_identity` and `TruthValidator` validated against the production `msallis-db` host 5433 ★. The `consciousnesslayers` and `identitylayers` fields on `UltimateResponse` provide transparent, per-request evidence of which layers from each path were active. The shared `ms_allis_memory` write/read path through the consciousness bridge is a confirmed emergent vector for cross-session context passing. All `truthverdict` and BBB audit events persist to `allis-memory:8056` (container name pinned, dual-network confirmed). The EEG Delta band (port 8073) PIA signal is the first live cross-path health indicator, confirming both analytical and meaning-oriented tracks are producing measurable output. ★ As of April 23, 2026: 100 active containers, 48 ChromaDB collections, ~6,740,611 vectors, production `msallis-db` host 5433 (16 GB, 294 tables, 11 schemas), forensic `postgis-forensic` host 5452 (17 GB, 314 tables), Caddy `forward_auth` active at perimeter. Future work will focus on fully wiring meaning-oriented modules into the `ultimatechat` entrypoint and extending cross-path analytics.

---

## Automated Commands — Verification

The following shell commands confirm current state. Run from the Legion 5 host inside `crypto-venv` unless noted.

```bash
# ── CONFIRM EXACT METRICS ────────────────────────────────────────────────────

# 1. Active container count (should be 100 as of April 23, 2026)
docker ps -q | wc -l

# 2. Exact ChromaDB collection count and names (★ /api/v2/ — /api/v1/ is permanently removed)
curl -s "http://127.0.0.1:8002/api/v2/tenants/default_tenant/databases/default_database/collections" \
  | python3 -c "
import json, sys
cols = json.load(sys.stdin)
print(f'Collections: {len(cols)}')
for c in cols:
    print(f'  {c[\"name\"]}')
"

# 3. Total vector count across all collections (★ /api/v2/ paths)
curl -s "http://127.0.0.1:8002/api/v2/tenants/default_tenant/databases/default_database/collections" \
  | python3 -c "
import json, sys, urllib.request
cols = json.load(sys.stdin)
total = 0
base = 'http://127.0.0.1:8002/api/v2/tenants/default_tenant/databases/default_database'
for c in cols:
    cname = c['name']
    resp = urllib.request.urlopen(f'{base}/collections/{cname}/count')
    n = json.loads(resp.read())
    total += n
    print(f'  {cname}: {n}')
print(f'TOTAL VECTORS: {total}')
"

# 4. ★ Production PostgreSQL — msallis-db host 5433 (two-container split)
psql -h 127.0.0.1 -p 5433 -U postgres -d msallis -c "
SELECT
  (SELECT count(*) FROM pg_tables WHERE schemaname='public') AS public_tables,
  (SELECT count(*) FROM information_schema.schemata) AS schemas,
  pg_size_pretty(pg_database_size('msallis')) AS db_size;
"

# 5. ★ Forensic PostgreSQL — postgis-forensic host 5452
psql -h 127.0.0.1 -p 5452 -U postgres -c "
SELECT
  (SELECT count(*) FROM pg_tables) AS all_tables,
  pg_size_pretty(pg_database_size('postgres')) AS db_size;
"

# 6. Neurobiological master health (internal — run from allis-main-brain container)
docker exec allis-main-brain \
  curl -s http://allis-neurobiological-master:8018/health | python3 -m json.tool

# ── ALLIS-MEMORY NETWORK CONFIRMATION ────────────────────────────────────────

# 7. Confirm allis-memory is on both networks
docker inspect allis-memory \
  --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}}{{"\\n"}}{{end}}'

# 8. Confirm DNS resolution and HTTP 200 from pia-status
docker exec allis-pia-status \
  curl -s -o /dev/null -w "%{http_code}" http://allis-memory:8056/health

# ── BBB FILTER CONFIRMATION ───────────────────────────────────────────────────

# 9. Confirm BBB 6 filters operational
curl -s http://127.0.0.1:8016/health | python3 -m json.tool

# ── EEG DELTA PIA SIGNAL ──────────────────────────────────────────────────────

# 10. Current PIA pulse count and phase3 activity
curl -s http://127.0.0.1:8073/status | python3 -m json.tool

# ── PSYCHOLOGICAL RAG DOMAIN ──────────────────────────────────────────────────

# 11. Confirm psychological_rag_domain reachable on correct hostname
docker exec allis-pia-status \
  curl -s -o /dev/null -w "%{http_code}" http://psychological_rag_domain:8006/health

# ── AAACPE DEDICATED STACK ★ ──────────────────────────────────────────────────

# 12. Confirm AAACPE scraper and RAG containers Up
docker ps | grep allis-aaacpe

# 13. Full service health sweep — qualia-net containers
docker exec allis-main-brain curl -s http://allis-neurobiological-master:8018/health
docker exec allis-main-brain curl -s http://allis-consciousness-bridge:8020/health
docker exec allis-main-brain curl -s http://allis-qualia-engine:8017/health
docker exec allis-main-brain curl -s http://allis-i-containers:8015/health
docker exec allis-main-brain curl -s http://allis-blood-brain-barrier:8016/health

# 14. RAG pipeline end-to-end test
curl -s -X POST http://127.0.0.1:8003/query \
  -H "Content-Type: application/json" \
  -d '{
    "collection": "appalachian_cultural_intelligence",
    "message": "West Virginia community resources Fayette County",
    "user_id": "ch23-verify",
    "n_results": 3
  }' | python3 -c "
import json, sys
r = json.load(sys.stdin)
docs = r.get('chroma_raw',{}).get('documents',[[]])
print(f'RAG docs returned: {len(docs)}')
for i,d in enumerate(docs):
    print(f'  [{i}] {str(d)[:80]}...')
"
```

---

*Last updated: 2026-04-23 by Carrie Kidd (Mamma Kidd), Oak Hill WV*

*★ April 23, 2026: Container count updated to 100 (supersedes 92+ April 12 baseline). ChromaDB updated to 48 active collections, ~6,740,611 total vectors (supersedes 49 / 6,700,000+). Two-container PostgreSQL split: production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — all references to msallisgis:5432 and msallis:5433 as GBIM/GIS targets superseded throughout. OI-36-A CLOSED — Caddy forward_auth perimeter enforcement active before port 8050 (§23.0 figure, §23.1, §23.2, §23.4, §23.5, §23.7, status table). ChromaDB API updated to /api/v2/ throughout in verification commands — /api/v1/ permanently removed in server 1.0.0. AAACPE ingest path updated — dedicated stack (allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032) supersedes legacy allis-ingest-api + allis-ingest-watcher (§23.2, §23.4, §23.5, status table, verification commands). conversation_history wiped and reseeded clean April 16, 2026 — post-wipe accumulation only (§23.6). processing_time updated to ~102.58s GPU RTX 4070 benchmark (§23.6). autonomous_learner updated to ~23,200+ records. Port reference table updated with AAACPE stack ports and two-container DB split.*

*April 12, 2026: allis-neurobiological-master confirmed healthy (Ch. 19 §19.8.7 closed). ChromaDB updated to 49 collections, 6,700,000+ vectors. msallisgis updated to 548 tables, 45 GB. psychological_rag_domain hostname corrected. allis-memory container name pinned, dual-network confirmed. BBB restarted — 6 filters operational. EEG Delta (port 8073) PIA signal added (§23.5). Container count updated to 92+. Future-work register pruned: neuro_master unreachability and allis-memory DNS reliability items removed (both resolved). All April 12 confirmations propagated throughout.*
