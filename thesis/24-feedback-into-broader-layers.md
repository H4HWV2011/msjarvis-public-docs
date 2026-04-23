# Chapter 24 — Feedback into Introspective, Memory, and Control Layers

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: 2026-04-23*

*★ April 23, 2026: Container count updated to 100 (supersedes 92 from April 12 baseline); ChromaDB updated to 48 active collections, ~6,740,611 total vectors (supersedes 49 / 6,722,589+); ChromaDB host port confirmed 8002→8000 (container port 8000), API updated to /api/v2/ throughout — /api/v1/ is permanently removed in server 1.0.0; two-container PostgreSQL split — production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — supersedes single-container msallisgis:5432 and msallis:5433 references throughout; autonomous_learner updated to ~23,200+ records (~288/day from 21,181 April 13 baseline); conversation_history wiped and reseeded clean April 16, 2026 — post-wipe accumulation only; OI-36-A CLOSED — Caddy forward_auth token enforcement active at perimeter before main-brain port 8050; local_resources updated to 207 items (supersedes 101); AAACPE ingest path updated — dedicated stack (allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032) supersedes legacy allis-ingest-api + allis-ingest-watcher for Appalachian cultural data; msallis_docs item count updated to verify-current (was 7,465 on April 12 rebuild stack — current count must be confirmed).*

> **Stack scope note:** This chapter documents the current production configuration. All mechanisms described here operate on the live stack; where behavior differs from the canonical thesis configuration, that difference is explicitly noted with a cross-reference to the relevant chapter.

---

> **Why This Matters for Polymathmatic Geography**
> This chapter describes how material processed in the container paths and dual tracks feeds back into introspective records, long-term semantic memory, and high-level control settings. It supports:
> - **P1 – Every where is entangled** by ensuring that outputs from both the analytical and meaning-oriented tracks are written into shared ChromaDB (★ **48 collections, ~6,740,611 total vectors**) and the production PostgreSQL `msallis-db` (host port **5433** ★, **16 GB, 294 tables, 11 schemas**) memory structures that future queries across all paths can retrieve. Forensic verification uses `postgis-forensic` (host port **5452** ★, **17 GB, 314 tables**).
> - **P3 – Power has a geometry** by making feedback pathways explicit, named, and traceable — specific sync scripts, named ChromaDB collections, PostgreSQL tables, and queryable health endpoints — rather than allowing them to operate as hidden implicit updates. BBB audit trail events for every feedback decision persist to `allis-memory:8056` (authenticated; event schema per Ch. 42) — the geometry of feedback power is durably logged. ★ Caddy `forward_auth` (OI-36-A CLOSED) enforces bearer token authentication at the perimeter before any feedback pathway is exercised.
> - **P5 – Design is a geographic act** by coupling semantic embeddings to specific spatial features in the production `msallis-db` host 5433 ★, so that feedback from community interactions becomes grounded in real West Virginia places and data.
> - **P12 – Intelligence with a ZIP code** by populating collections like `geodb_*`, `appalachian_english_corpus`, and `mountainshares_knowledge` with place-specific content sourced from the production `msallis-db` ★ that future RAG queries will retrieve. ★ The dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) and `local_resources` (★ 207 items, all 55 WV counties) supplement this ZIP-coded substrate with systematic community resource data — including county-level emergency food and social services.
> - **P16 – Power accountable to place** by maintaining explicit sync logs, verification reports, and curator-facing endpoints so that communities can audit how and when the system's memory and control settings were updated. `allis-memory:8056` is the canonical durable store for BBB and truth-verdict audit events (event schema fully specified in Ch. 42) — accountability to place is persistently secured. ★ Caddy `forward_auth` (OI-36-A CLOSED) ensures no unauthenticated path reaches any feedback mechanism.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the concrete mechanisms by which container-level processing feeds back into introspective records, PostgreSQL long-term memory stores, and system configuration. Correctness and presence of these mechanisms are continuously enforced by `scripts/VERIFYANDTEST.sh` and `scripts/preflight_gate.sh` — see §24.2a.

```text
┌─────────────────────────────────────────────────────────────┐
│   Feedback Pathways Architecture                            │
│   ★ Updated April 23, 2026 — 100 containers Up             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Container-Level Processing (Chapters 19-23)                │
│      ↓                                                       │
│  ★ Caddy forward_auth (OI-36-A CLOSED)                       │
│    Bearer token validated at perimeter proxy                │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Three Feedback Directions                     │         │
│  │                                                │         │
│  │  1. Introspective & Health Records             │         │
│  │     - getdatabasehealth endpoint               │         │
│  │     - getidentitycandidates endpoint           │         │
│  │     - /curator/background (main-brain 8050)    │         │
│  │     - BBB barrier_stats (port 8016)            │         │
│  │       audit → allis-memory:8056 (auth req'd)   │         │
│  │     - System Verification Reports              │         │
│  │     - Consciousness bridge → consciousnesslayers│        │
│  │       OPERATIONAL (§24.1a)                     │         │
│  │     - Gate enforcement: VERIFYANDTEST.sh       │         │
│  │       preflight_gate.sh (see §24.2a)           │         │
│  │                                                │         │
│  │  2. Long-Term Semantic & Spatial Memory        │         │
│  │     - ms_allis_memory (ChromaDB, append-only)  │         │
│  │       UUID: 79240788-0828-45f3-b1bc-a9a3593628a6│        │
│  │     - ★ production msallis-db (host 5433)      │         │
│  │       16 GB, 294 tables, 11 schemas            │         │
│  │     - ★ forensic postgis-forensic (host 5452)  │         │
│  │       17 GB, 314 tables                        │         │
│  │     - ChromaDB (127.0.0.1:8002→8000)           │         │
│  │       ★ 48 collections, ~6,740,611 vectors     │         │
│  │       /api/v2/ (★ /api/v1/ removed)            │         │
│  │     - autonomous_learner: ~23,200+ records ★   │         │
│  │       (autonomouslearning is historical only)  │         │
│  │     - local_resources: ★ 207 items, 55 WV cntys│         │
│  │     - msallis_docs: verify-current ★           │         │
│  │     - GeoDB sync scripts & logs                │         │
│  │     - ★ AAACPE dedicated stack (8033/8032)     │         │
│  │       supersedes legacy allis-ingest-api       │         │
│  │                                                │         │
│  │  3. Global Configuration & Control             │         │
│  │     - TruthFilterBBBValidator                  │         │
│  │       grounded in production msallis-db:5433 ★ │         │
│  │     - masterspatialknowledge.csv               │         │
│  │     - Service registry (SERVICES dict)         │         │
│  │     - ueididentity & ueidaccessaudit tables    │         │
│  │     - allis-memory:8056 (auth black-box store) │         │
│  │       127.0.0.1, _auth() confirmed, API key set│         │
│  │     - Judge pipeline: containers running,      │         │
│  │       signing key wiring still a gate TODO     │         │
│  │       (see §24.4d; canonical in Ch. 33 & 42)   │         │
│  │     - ★ Caddy forward_auth (OI-36-A CLOSED)    │         │
│  │       perimeter before port 8050               │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Shared Across Both Tracks                                  │
│  - Analytical path: Always queries PostgreSQL               │
│  - Meaning-oriented: Validates against PostgreSQL           │
│  - Both write to ms_allis_memory ChromaDB                   │
│  - Both update PostgreSQL when validated                    │
│      ↓                                                       │
│  Audit & Logging                                            │
│  - GeoDB/Chroma sync logs                                   │
│  - RAG bridge logs                                          │
│  - ueididentity/ueidaccessaudit writes                      │
│  - PostgreSQL query logs                                    │
│  - System Verification Reports                              │
│  - allis-memory:8056 (BBB + truthverdict audit,             │
│    auth enforced; event schema per Ch. 42)                  │
│  - Gate suite: VERIFYANDTEST.sh + preflight_gate.sh         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 24.1.** Feedback pathways architecture: container-level processing feeds back through three directions — introspective records, long-term memory in the production `msallis-db` (host port **5433** ★, 16 GB, 294 tables, 11 schemas), forensic `postgis-forensic` (host port **5452** ★, 17 GB, 314 tables), and ChromaDB (★ **48 collections, ~6,740,611 total vectors**, host 127.0.0.1:8002→8000, /api/v2/), and global configuration — with explicit logging and audit trails maintaining accountability to PostgreSQL ground truth. BBB and `truthverdict` audit events persist to `allis-memory:8056` (authenticated; event schema per Ch. 42). Gate suite (`VERIFYANDTEST.sh` + `preflight_gate.sh`) continuously enforces the presence and correctness of all mechanisms. ★ Caddy `forward_auth` (OI-36-A CLOSED) is active at the perimeter before port 8050.

---

## Status as of ★ April 23, 2026

| Category | Details |
|---|---|
| **Stack configuration** | ★ **100 containers Up** (`docker ps -q \| wc -l`). Zero Restarting, zero Exited. |
| **ChromaDB** | ★ **48 collections, ~6,740,611 total vectors**, host **127.0.0.1:8002→8000** (container port 8000). `/api/v2/` — `/api/v1/` permanently removed in server 1.0.0. Primary `chroma_db` directory ~12 GB. |
| **Production PostgreSQL** | ★ `msallis-db` at **127.0.0.1:5433** — **16 GB, 294 tables, 11 schemas**. Supersedes all prior `msallisgis:5432` and `msallis:5433` single-container references. |
| **Forensic PostgreSQL** | ★ `postgis-forensic` at **127.0.0.1:5452** — **17 GB, 314 tables**. Available for verification and audit. |
| **msallis_docs** | ★ **Verify-current** (was 7,465 items on April 12 rebuild stack — confirm with `preflight_gate.sh`). |
| **local_resources** | ★ **207 items, all 55 WV counties seeded.** (Supersedes April 12 value of 101.) |
| **autonomous_learner** | ★ **~23,200+ records**, growing approximately 288/day from 21,181 April 13 baseline. Canonical community-memory collection. `autonomouslearning` is a historical name only — see §24.3. |
| **conversation_history** | ★ **Wiped and reseeded clean April 16, 2026.** Post-wipe accumulation only. Pre-wipe counts are historical values. |
| **RAG** | `allis-rag-server:8003/query` schema requires `collection` + `message`. A POST with `collection: "local_resources"` and `message: "nearest food pantry in Fayette County WV"` returns documents including a Fayette County Community Action Agency food-assistance entry tagged `county=Fayette` — end-to-end Appalachian community resource loop confirmed. ★ `local_resources` is now 207 items / all 55 WV counties, expanding the resource coverage. |
| **AAACPE ingest** | ★ Dedicated stack: `allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`. Supersedes legacy `allis-ingest-api` + `allis-ingest-watcher` for Appalachian cultural data. |
| **allis-memory** | **Reachable and healthy; auth enforced (`ALLIS_API_KEY` required).** Canonical durable audit sink for BBB and truth-verdict events. Precise event schema (Phase 1.4/2/3/4.5, AU-02 v2 fields) specified and enforced in Ch. 42. This chapter treats `allis-memory` as an **authenticated black-box store**. |
| **Caddy forward_auth** | ★ **OI-36-A CLOSED.** Bearer token validation active at perimeter proxy before main-brain port 8050. |
| **Judge pipeline** | All five judges and `rag_grounded_v2` truth judge running and integrated. **Signing key volume wiring still a gate TODO.** Full ML-DSA-65 verdict enforcement loop architecturally complete but not yet fully wired; canonical implementation in Chs. 33 and 42. |
| **EEG layer** | Delta EEG band (port 8073) live and reporting PIA status. Theta/beta bands implemented architecturally (Ch. 42) but not exposed as HTTP endpoints in current configuration. **EEG feedback is partial — delta only.** |
| **Gate enforcement** | `scripts/VERIFYANDTEST.sh` + `scripts/preflight_gate.sh` continuously validate all feedback mechanisms. Gates confirm: Chroma collections ≥ 40 (★ 48 found), `psychological_rag` ≥ 968 docs, `msallis_docs` populated (verify-current ★), `local_resources` populated (★ 207 items), `autonomous_learner` growing (~23,200+), BBB EthicalFilter 0 false positives, unauthenticated `/chat` → HTTP 401 (★ OI-36-A CLOSED). |
| **Partially implemented** | Watchdog endpoints defined in code but not confirmed running as an independent service. Automated scheduled System Verification Reports not yet implemented. Cross-path analytics not yet exposed via a dedicated endpoint. |
| **Future work** | Automated System Verification Report generation. Real-time feedback-volume dashboard. Automated `identitycandidates` promotion pipeline. Full deduplication at `ms_allis_memory` write path. Structured PIA review loop automation. Full ML-DSA-65 judge signing key wiring. |

> **Cross-reference:** The `background_rag_store` mechanism that produces `ms_allis_memory` entries is described in **Chapter 17 §17.6** and **Chapter 20 §20.3**. The `identitycandidates` and identity-layer elements fed by these feedback paths are described in **Chapter 22**. The dual-track structure whose outputs feed these mechanisms is described in **Chapter 23**.

---

# 24. Feedback into Introspective, Memory, and Control Layers

This chapter describes how material processed in the container paths and dual tracks feeds back into introspective records, long-term semantic memory in the production `msallis-db` (host port **5433** ★, **16 GB, 294 tables, 11 schemas**), forensic `postgis-forensic` (host port **5452** ★, **17 GB, 314 tables**), and ChromaDB (★ **48 active collections, ~6,740,611 total vectors**, host 127.0.0.1:8002→8000, /api/v2/), and high-level control settings.

In the current deployment, feedback mechanisms operate primarily through confirmed ChromaDB collections written by `background_rag_store`, PostgreSQL as the authoritative spatial and institutional ground truth, GeoDB synchronization scripts and their logs, `getidentitycandidates` and `getdatabasehealth` endpoints, and curator-facing tools for inspecting `ms_allis_memory`. As of April 23, 2026, the BBB audit trail persists to `allis-memory:8056` (authenticated; event schema per Ch. 42). ★ Caddy `forward_auth` (OI-36-A CLOSED) is active at the perimeter before main-brain port 8050. All feedback mechanisms described in this chapter are continuously validated by `scripts/VERIFYANDTEST.sh` and `scripts/preflight_gate.sh`.

---

## 24.1 Overview of Feedback Paths

In the current deployment, the system provides three concrete directions for feedback from container-level activity into other layers, all ultimately anchored to the production `msallis-db` host 5433 ★.

**Introspective and health records.** `allis-main-brain` (port **8050**, ★ behind Caddy `forward_auth` — OI-36-A CLOSED) exposes status endpoints that summarize per-service health in structured JSON, and the `/curator/background` endpoint provides direct inspection of `ms_allis_memory` entries. The secured gateway exposes `getdatabasehealth` (returning `status`, `database`, `identityelements`, `candidates`, `integrity`, timestamps anchored to the production `msallis-db:5433` ★) and `getidentitycandidates` (returning candidate identity statements validated against PostgreSQL GBIM from the production `msallis-db:5433` ★). BBB `barrier_stats` events persist to `allis-memory:8056` (authenticated black-box store; event schema per Ch. 42). Gate enforcement via `VERIFYANDTEST.sh` + `preflight_gate.sh` continuously validates these mechanisms — see §24.2a.

**Long-term semantic and spatial memory.** `allis-chroma` runs at **127.0.0.1:8002→8000** (container port 8000) with ★ **48 confirmed collections** and **~6,740,611 total vectors** as of April 23, 2026. All ChromaDB API calls use `/api/v2/` — `/api/v1/` is permanently removed in server 1.0.0. The production `msallis-db` at **127.0.0.1:5433** ★ (16 GB, 294 tables, 11 schemas) and forensic `postgis-forensic` at **127.0.0.1:5452** ★ (17 GB, 314 tables) serve as the authoritative sources for all spatial, institutional, and community data. RAG queries use explicit collection + message contracts. The canonical community-memory collection is `autonomous_learner` (★ ~23,200+ records); the name `autonomouslearning` is historical only. ★ The dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) provides the authoritative external-source long-term memory pathway (supersedes legacy `allis-ingest-api` + `allis-ingest-watcher` for AAACPE data).

**Global configuration and control.** Truth filters, BBB verification validators grounded in the production `msallis-db:5433` ★, and `masterspatialknowledge.csv` define explicit policy constraints. `allis-memory:8056` is the canonical durable store for `TruthFilterBBBValidator` audit events on this stack (authenticated; event schema per Ch. 42). The judge pipeline (all five judges + `rag_grounded_v2`) is running and integrated; however, signing key volume wiring is still reported as a gate TODO — see §24.4d. ★ Caddy `forward_auth` (OI-36-A CLOSED) is active at the perimeter before port 8050.

### 24.1a Consciousness Pipeline — OPERATIONAL

As of March 25, 2026 (confirmed Up, remains active on current stack), the consciousness pipeline (Chroma → WOAH → RAG → Bridge) is **OPERATIONAL**. The `allis-consciousness-bridge` is a confirmed feedback pathway writing into `consciousnesslayers` of every `UltimateResponse`:

- `chromadb_context` (str) — semantic context retrieved from ChromaDB at 127.0.0.1:8002→8000 (★ 48 collections, ~6,740,611 total vectors)
- `woah_reasoning` (dict) — reasoning output from the WOAH algorithms layer
- `rag_consensus` (dict) — consensus result from the RAG bridge pipeline

These fields appear in `consciousnesslayers` on every call, making the consciousness bridge a first-class, always-active feedback path alongside `background_rag_store`. All `chromadb_context` retrieval uses 384-dim (`all-minilm:latest`) — the only compatible model for all 48 ChromaDB collections (see Ch. 19 §19.8.8a). See **Ch. 25 §25.9** for the full bridge patch log.

---

## 24.2 Writing Back to Introspective Records

In the current deployment, introspective records are implemented as confirmed endpoints, logs, and verification outputs anchored to the production `msallis-db` host 5433 ★.

**`getdatabasehealth` and `getidentitycandidates`.** `getidentitycandidates` returns statements such as "I serve the community," "I speak truth," "I value ethics," and "I am conscious," each with `importance` and diagnostic scores validated against PostgreSQL GBIM from the production `msallis-db:5433` ★. `getdatabasehealth` reports `identityelements`, `candidates`, `integrity`, and timestamps for the production `msallis-db` host 5433 ★ (16 GB, 294 tables, 11 schemas).

**Main-brain status and `/curator/background`.** `allis-main-brain` status endpoints summarize per-service health including PostgreSQL connection status in a single queryable structure. The `/curator/background` endpoint provides direct inspection of `ms_allis_memory` ChromaDB contents, allowing operators to see exactly which `bg_<ISO8601>` entries were written and what metadata they carry. ★ `conversation_history` was wiped and reseeded clean April 16, 2026 — counts on this collection reflect post-wipe accumulation only.

**System Verification Reports.** Verification scripts produce outputs with sections including "VERIFICATION SUMMARY" and "HONEST ASSESSMENT," listing PostgreSQL `msallis-db` table sizes (★ production: 294 tables, 16 GB; forensic: 314 tables, 17 GB), ChromaDB operational status (★ 48 collections, ~6,740,611 vectors), numbers of responding services, and the state of production testing. Generated by manual script execution; automated scheduled generation is future work.

**BBB barrier stats and secured audit trail.** `allis-blood-brain-barrier` (port **8016**) maintains `total_filtered`, `total_blocked`, and `pass_rate` counters. All BBB audit events persist to `allis-memory:8056` (authenticated black-box store; event schema for Phase 1.4/2/3/4.5 and AU-02 v2 fields is specified and enforced in Ch. 42).

### 24.2a Gate-Enforced Feedback

`scripts/VERIFYANDTEST.sh` and `scripts/preflight_gate.sh` now continuously validate the feedback mechanisms described in this chapter. These scripts do not replace the endpoint and log verification described above — they run alongside it and provide machine-enforced confirmation that the mechanisms are live and populated.

Gates currently confirm on this stack:

- ★ Chroma collections ≥ 40 (48 found)
- `psychological_rag` ≥ 968 docs
- ★ `msallis_docs` populated (verify-current — confirm with `preflight_gate.sh`)
- ★ `local_resources` populated (207 items, all 55 WV counties)
- ★ `autonomous_learner` growing (~23,200+ records)
- BBB EthicalFilter 0 false positives
- Unauthenticated `/chat` → HTTP 401 (★ OI-36-A CLOSED — Caddy `forward_auth` active)

This gate suite is the enforcement layer for the feedback correctness guarantees stated throughout this chapter. If a gate fails, the feedback mechanism it validates is to be treated as degraded until the gate passes again.

---

## 24.3 Integration with Long-Term Memory

In the current deployment, material that passes through container and service layers is preserved in several confirmed long-term memory structures anchored to the production `msallis-db` host 5433 ★.

**`ms_allis_memory` — the primary feedback collection.** Every successful `/chat` call through `allis-main-brain` (port **8050**, ★ behind Caddy `forward_auth`) produces a `bg_<ISO8601>` entry in `ms_allis_memory` ChromaDB (UUID: `79240788-0828-45f3-b1bc-a9a3593628a6`) via `background_rag_store`, with concatenated `USER:`/`EGERIA:` text and metadata including `userid`, `timestamp`, `type: "background"`, and `services: ["llm20production"]`. This collection is append-only in the current deployment. ★ `conversation_history` was wiped and reseeded clean April 16, 2026 — any count on that collection reflects post-wipe accumulation only.

> **March 25, 2026:** Emergent cross-session context passing (name, topic, entity recall) confirmed — likely via `_get_url` read path through the consciousness bridge into `ms_allis_memory`. See **Ch. 22 §22.9** (OI-05) for the full finding.

**PostgreSQL — the authoritative ground truth (two-container split ★).** ★ The production `msallis-db` at **127.0.0.1:5433** (16 GB, 294 tables, 11 schemas) is the authoritative source of truth for all spatial, institutional, and community data. The forensic `postgis-forensic` at **127.0.0.1:5452** (17 GB, 314 tables) is available for verification and audit. All prior references to `msallisgis:5432` and `msallis:5433` as PostgreSQL ground truth targets are superseded by this two-container split. The `confidence_decay` metadata carried by GBIM entities provides a graded evidentiary signal for feedback pathway triage — beliefs with high `confidence_decay` are weaker candidates for promotion to identity-level storage.

**Chroma + PostGIS integration and explicit RAG collection contracts.** As of April 23, 2026, ChromaDB has ★ **48 collections** and RAG queries use explicit `collection` + `message` contracts. All API calls use `/api/v2/` — `/api/v1/` is permanently removed in server 1.0.0. Callers must specify the collection name — e.g., `collection: "local_resources"` for WV county resource queries, or `collection: "appalachian_cultural_intelligence"` for broader cultural context. There is no implicit default collection.

> **Concrete RAG example (Fayette County food pantry).** A POST to `allis-rag-server:8003/query` with `collection: "local_resources"` and `message: "nearest food pantry in Fayette County WV"` returns documents including a Fayette County Community Action Agency food-assistance entry tagged `county=Fayette`, ZIPs 25801, 25840, 25880, plus neighboring county resource sheets. ★ `local_resources` is now 207 items / all 55 WV counties, expanding coverage beyond the April 12 baseline of 101 items. This confirms that AAACPE ingest → ChromaDB storage → RAG retrieval → answer is a closed, working loop.

**`autonomous_learner` — canonical community-memory collection.** ★ The canonical name for the community-memory ChromaDB collection is `autonomous_learner`. It has grown to **~23,200+ records**, approximately 288/day from the 21,181 April 13 baseline. The name `autonomouslearning` was used historically and appears in older code and documentation — it is a historical alias only and must not be used in new code or chapter references.

**Additional confirmed ChromaDB collections.** `allis-chroma` at **127.0.0.1:8002→8000** (container port 8000) hosts ★ **48 confirmed collections** including `allis_consciousness` (over 11,000 items), `autonomous_learner` (★ ~23,200+ records, canonical), `learning_suggestions`, `research_history`, `spiritual_wisdom`, `appalachian_english_corpus`, `appalachian_cultural_intelligence`, `psychological_rag` (968 docs), `msallis_docs` (★ verify-current), `local_resources` (★ 207 items, all 55 WV counties), and numerous `geodb_*` collections. ★ Total confirmed vector count: **~6,740,611** as of April 23. ChromaDB API uses `/api/v2/` throughout — `/api/v1/` is permanently removed. `allis-chroma` at 8002→8000 is the confirmed primary instance.

**GeoDB sync scripts and logs.** The following scripts and their logs are confirmed on disk: `sync_geodb_to_chromadb.py`, `extract_all_chromadb_to_gis.py`, `vectorize_gis_to_chromadb.py`, `recover_chromadb_to_gisgeodb.py`, with corresponding logs `chromadb_v2_to_gis_sync.log`, `extract_all_chromadb_to_gis.log`, `vectorize_gis_to_chromadb.log`, `recover_chromadb_to_gisgeodb.log`. These logs record when new semantic embeddings are created, which PostgreSQL spatial features they correspond to (★ production `msallis-db:5433`, 16 GB, 294 tables, 11 schemas), and how inconsistencies are resolved.

**★ AAACPE external-source ingest pathway (dedicated stack).** ★ The dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) is the authoritative external-source long-term memory pathway, superseding the legacy `allis-ingest-api` + `allis-ingest-watcher` for Appalachian cultural data. Community resource documents flow into `msallis_docs` (★ verify-current) and `autonomous_learner` (★ ~23,200+ records). This is the first long-term memory pathway that directly ingests community resource data — including the `local_resources` collection (★ 207 items, all 55 WV counties) — rather than deriving it from user interactions. See the Fayette County RAG example above for end-to-end confirmation.

**Service-specific knowledge bases.** Collections such as `mountainshares_knowledge`, `h4h_cultural_heritage`, `egeria_docs`, and `ms_allis_memory` allow certain services to promote their distilled outputs into reusable knowledge stores backed by the production `msallis-db` host 5433 ★, influencing future responses long after the original interactions.

---

## 24.4 Influence on Global Settings and Coordination

In the current deployment, high-level control is implemented through explicit configuration parameters and scripted verification anchored to the production `msallis-db` host 5433 ★ rather than implicit learning from behavior alone.

**Truth and registration filters.** `TruthFilterBBBValidator` enforces minimum accuracy scores, expiration-date buffers, and age constraints validated against PostgreSQL GBIM ground truth from the production `msallis-db:5433` ★, and records verification decisions in `ueididentity` and `ueidaccessaudit` tables. All `TruthFilterBBBValidator` audit events persist to `allis-memory:8056` (authenticated black-box store; event schema per Ch. 42). `GISTruthFilter` validates geographic data against USGS, NRCS, NOAA, and US Census Bureau sources before allowing writes to PostgreSQL GeoDB (production `msallis-db:5433` ★). For full detail on these validators see **Chapter 16 §16.5**.

**`masterspatialknowledge.csv` and access documentation.** `masterspatialknowledge.csv` is confirmed present with `accesslevelrequired` and `isproprietary` fields describing PostgreSQL GeoDB access policies for the production `msallis-db:5433` ★ (16 GB, 294 tables, 11 schemas). Security-related files (`SECURITY-OVERVIEW.md`, `SOURCEACCESS.md`, `accesscontrollevels.csv`) are checked by verification routines to ensure that documentation and access models exist alongside PostgreSQL data.

**Service registry and orchestration parameters.** The `SERVICES` dictionary in `allis-main-brain` (port **8050**, ★ behind Caddy `forward_auth`) lists expected modules and ports including the production `msallis-db` at host port **5433** ★. `discover_services()` health-checks these at request time and updates `available_services`. For the canonical description of how this operates see **Chapter 17 §17.2**.

### 24.4a AU-02 v2 — Active at BBB Layer

AU-02 v2 (regex v2: 6 compiled patterns, ~0ms; embedding v2: 30 seeds, cosine threshold ≥ 0.72, ~300ms cached; false-positive guard: 8 overly broad triggers removed) is active and enforced at the BBB layer. All intercepts are routed to `allis-memory:8056` in the production configuration described in Ch. 42. This stack uses the same BBB container and filters, but local event inspection of AU-02 v2 intercepts is deferred to that canonical description — this stack treats `allis-memory` as an authenticated black-box store.

### 24.4b EEG Layer — Partial on Current Stack

The **delta EEG band (port 8073) is live** and reporting PIA status. The theta and beta bands are implemented architecturally (see Ch. 42 §42.13) but are **not exposed as HTTP endpoints in this configuration**. EEG feedback is therefore **partial** — delta only. Full three-band EEG feedback is available in the 105-container thesis stack described in Ch. 42 §42.13.

### 24.4c allis-memory:8056 — Authenticated Black-Box Store

`allis-memory:8056` is reachable and healthy, requires `ALLIS_API_KEY`, and is the canonical durable audit sink for BBB and truth-verdict events on this stack. The precise event schema — including Phase 1.4, Phase 2, Phase 3, Phase 4.5, and AU-02 v2 fields — is specified and enforced in the 105-container thesis configuration described in **Chapter 42**. This chapter treats `allis-memory` as an authenticated black-box store: events flow in, authentication is confirmed, and retrieval of specific event records is deferred to the canonical Ch. 42 description.

### 24.4d Judge Pipeline and ML-DSA-65 Verdict Signing — Current Status

All five judges and the `rag_grounded_v2` truth judge are running and integrated into the inference pipeline. However, the **preflight gate still reports missing signing-key volume wiring** for judge services. As such, the full ML-DSA-65 verdict enforcement loop is **architecturally complete but not yet fully wired**. The canonical, fully wired implementation — with liboqs ML-DSA-65 confirmed as the primary runtime, `dilithium_py` as graceful fallback, all five judges signing, and `rotate_judge_keys.sh` production-grade — is documented in **Chapters 33 and 42**.

---

## 24.5 Cross-Path Effects

In the current deployment, because the same ChromaDB collections (★ 48 collections, ~6,740,611 vectors), production `msallis-db` host 5433 ★ structures, and configuration parameters are shared across both the meaning-oriented and analytical tracks (see Chapter 23), feedback from one path naturally affects the other.

**Shared semantic and spatial memory.** Collections such as `mountainshares_knowledge`, `spiritual_wisdom`, `allis_consciousness`, `autonomous_learner` (★ canonical, ~23,200+ records; `autonomouslearning` is historical), and `geodb_*` datasets are accessible by both experiential/meaning-oriented modules and technical/analytical modules. ★ The `local_resources` collection (207 items, all 55 WV counties) and `msallis_docs` (verify-current) are now shared community resource substrates — regional service and community resource embeddings can surface in both analytical and meaning-oriented RAG retrievals. ★ AAACPE ingest flows through the dedicated stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) into these shared collections.

**Shared identity and database health.** `getdatabasehealth` and `getidentitycandidates` are not track-specific. If container-level processing leads to changes in identity candidates validated against the production `msallis-db:5433` ★ or if verification activity alters the integrity status of the production PostgreSQL (16 GB, 294 tables, 11 schemas), those changes are visible to any path that queries these endpoints.

**Coordinated sync scripts.** GeoDB/ChromaDB sync scripts alter the shared memory substrate — changing how production `msallis-db` features are embedded, which ChromaDB collections are active (★ 48 collections), or how provider summaries are generated. Both the analytical path and the meaning-oriented path see a consistently updated view anchored to the production `msallis-db` host 5433 ★.

> **neuro_master status:** `allis-neurobiological-master` (port **8018**) was unreachable at chapter open (March 28) and was subsequently confirmed healthy (HTTP 200, `integration_active: true`, `total_processes: 5`) as of April 12, 2026 — see Ch. 25 §25.4. The neuro_master open item is closed as of Ch. 25 seal.

> **★ conversation_history:** This collection was wiped and reseeded clean April 16, 2026. Any cross-path effect or diagnostic count referencing `conversation_history` volume reflects post-wipe accumulation only.

---

## 24.6 Logging and Audit of Feedback

In the current deployment, explicit mechanisms for logging and auditing feedback processes with traceability to the production `msallis-db` host 5433 ★ are confirmed present, though their completeness varies.

**GeoDB/ChromaDB sync logs.** `chromadb_v2_to_gis_sync.log`, `extract_all_chromadb_to_gis.log`, `vectorize_gis_to_chromadb.log`, and `recover_chromadb_to_gisgeodb.log` record how ChromaDB collections (★ 48 collections, ~6,740,611 vectors) and production PostgreSQL data (`msallis-db:5433` ★ — 16 GB, 294 tables, 11 schemas) are updated and reconciled.

**RAG and bridge logs.** Bridge logs (e.g. `bridge_ms_allis_main_gateway_to_chromadb_rag_helper.log`, `ms_allis_chromadb_query_9014.log`) capture interactions between the main gateway and ChromaDB-backed RAG helpers, recording queries, result counts, and error conditions. The consciousness bridge produces `chromadb_context`, `woah_reasoning`, and `rag_consensus` on every call — these fields are themselves auditable artifacts of the RAG feedback loop.

**`/curator/background` and verification outputs.** The `/curator/background` endpoint on `allis-main-brain` (port **8050**, ★ behind Caddy `forward_auth`) provides a stable, auditable view of `ms_allis_memory` ChromaDB contents. Historical System Verification Report scripts produce human-readable summaries with timestamps, PostgreSQL table counts, and candid operational assessments.

**`ueididentity` and `ueidaccessaudit` tables, and `allis-memory:8056`.** `TruthFilterBBBValidator` writes verification outcomes and audit records into `ueididentity` and `ueidaccessaudit` tables with references to PostgreSQL GBIM validation from the production `msallis-db:5433` ★. All BBB and `truthverdict` audit events additionally persist to `allis-memory:8056` (authenticated black-box store; event schema per Ch. 42) — the audit trail for feedback decisions is doubly secured: PostgreSQL tables and authenticated `allis-memory` store.

**Gate enforcement logs.** `scripts/VERIFYANDTEST.sh` and `scripts/preflight_gate.sh` produce machine-readable pass/fail records that serve as a continuous audit of feedback mechanism presence and correctness. The current gate suite confirms ★ 48 Chroma collections, `local_resources` ★ 207 items and `msallis_docs` populated (verify-current), `autonomous_learner` at ~23,200+ records, 0 EthicalFilter false positives, and HTTP 401 on unauthenticated `/chat` (★ OI-36-A CLOSED) — see §24.2a for the full confirmed gate list.

---

## 24.7 Summary

Three feedback directions are **fully live** on the current stack:

1. **Introspective health records** — `getdatabasehealth`, `getidentitycandidates`, `/curator/background`, BBB `barrier_stats`, System Verification Reports, and the consciousness bridge all provide confirmed, queryable introspective snapshots of the running system, anchored to the production `msallis-db` host 5433 ★ (16 GB, 294 tables, 11 schemas) and forensic `postgis-forensic` host 5452 ★ (17 GB, 314 tables).

2. **Long-term semantic and spatial memory** — ChromaDB (★ 48 collections, ~6,740,611 vectors, host 127.0.0.1:8002→8000, /api/v2/), production `msallis-db` and forensic `postgis-forensic`, GeoDB sync scripts, `background_rag_store`, and ★ the dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) with `msallis_docs` (verify-current ★) and `local_resources` (★ 207 items, all 55 WV counties) are all active and feeding the long-term memory substrate. ★ `autonomous_learner` is at ~23,200+ records and growing.

3. **Global configuration and control** — `TruthFilterBBBValidator`, `masterspatialknowledge.csv`, the service registry, AU-02 v2 at the BBB layer, `allis-memory:8056`, and ★ Caddy `forward_auth` perimeter enforcement (OI-36-A CLOSED) define explicit, auditable control constraints enforced at every inference step.

Their correctness and presence are now **enforced by `VERIFYANDTEST.sh` and `preflight_gate.sh`** — see §24.2a for the confirmed gate list.

**One concrete RAG example proves feedback end-to-end.** A POST to `allis-rag-server:8003/query` with `collection: "local_resources"` and `message: "nearest food pantry in Fayette County WV"` returns documents including a Fayette County Community Action Agency food-assistance entry tagged `county=Fayette`, ZIPs 25801, 25840, 25880, plus neighboring county resource sheets. ★ `local_resources` is now 207 items / all 55 WV counties. This confirms that AAACPE ingest → ChromaDB storage → RAG retrieval → answer is a closed, working loop.

**Two mechanisms are governed at the thesis level (Chapters 33–42) and partially implemented on this stack.** `allis-memory:8056` is reachable and authenticated, but its event schema (Phase 1.4/2/3/4.5, AU-02 v2 fields) is specified and enforced in Ch. 42 — this stack treats it as an authenticated black-box store. The ML-DSA-65 judge signing loop is architecturally complete but judge signing-key volume wiring is still a gate TODO; the canonical fully wired implementation is in Chs. 33 and 42.

The `ms_allis_memory` `_get_url` read path through the consciousness bridge is a confirmed emergent vector for cross-session context passing (OI-05 — see Ch. 22 §22.9). ★ `conversation_history` was wiped and reseeded clean April 16, 2026 — post-wipe accumulation only; pre-wipe counts are historical. EEG feedback is partial — delta band only; theta/beta are architecturally implemented (Ch. 42 §42.13) but not exposed as HTTP endpoints. For the canonical description of how `background_rag_store` fits into the live `ultimatechat` execution sequence, see **Chapter 17**. For the identity layer these feedback paths ultimately serve, see **Chapter 22**.

---

*Last updated: 2026-04-23 by Carrie Kidd (Mamma Kidd), Oak Hill / Mount Hope WV*

*★ April 23, 2026: Container count updated to 100 (supersedes 92 April 12 baseline). ChromaDB updated to 48 active collections, ~6,740,611 total vectors (supersedes 49 / 6,722,589+). Two-container PostgreSQL split: production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — all prior msallisgis:5432 and msallis:5433 references superseded throughout. OI-36-A CLOSED — Caddy forward_auth perimeter enforcement active before main-brain port 8050 (figure, §24.1, §24.2a, §24.4, §24.6, §24.7, status table). ChromaDB API updated to /api/v2/ throughout — /api/v1/ permanently removed (§24.3, verification commands). AAACPE ingest path updated — dedicated stack supersedes legacy allis-ingest-api + allis-ingest-watcher (§24.1, §24.3, §24.5, §24.7, figure, status table). autonomous_learner updated to ~23,200+ records (~288/day from 21,181 April 13 baseline). local_resources updated to 207 items / all 55 WV counties (supersedes 101). msallis_docs updated to verify-current (was 7,465 on April 12 rebuild stack). conversation_history wiped and reseeded clean April 16, 2026 — post-wipe accumulation only (§24.2, §24.5, §24.7). Gate list updated for new values (§24.2a). Status table fully updated. Summary (§24.7) fully updated.*

*★★ April 12, 2026: Chapter revised for 92-container rebuild stack. All hard numbers updated. §24.2a Gate-Enforced Feedback added. §24.4a AU-02 v2 status added. §24.4b EEG partial-implementation note added. §24.4c allis-memory black-box treatment added. §24.4d Judge pipeline / ML-DSA-65 signing status added. Concrete Fayette County RAG example added. autonomous_learner canonical collection name confirmed throughout. Status table and §24.7 fully rewritten.*

*★ March 28, 2026: 96 containers Up on original stack — baselines established for ChromaDB (40 collections, 6,675,442 vectors), msallisgis (501 tables), msallis_docs (4,192 items), allis-memory:8056 secured.*
