# Chapter 24 — Feedback into Introspective, Memory, and Control Layers

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: April 12, 2026 — ★★ April 12, 2026: Revised for the 92-container rebuild stack. Container count corrected to 92 (from 96). ChromaDB updated to 49 collections, 6,722,589+ vectors, host 127.0.0.1:8002→8000, chroma 0.6.3 pinned. gisdb updated to 551 public tables (supersedes March 28 baseline of 501). msallis_docs updated to 7,465 items. local_resources confirmed 101 items, all 55 WV counties seeded. mvw_gbim_landowner_spatial confirmed 20,593 rows. autonomous_learner canonical community-memory collection noted. Concrete RAG example (Fayette County food pantry) added. Gate-enforced feedback subsection added. EEG partial-implementation note corrected. allis-memory:8056 treated as authenticated black-box store on this stack. ML-DSA-65 verdict signing noted as architecturally complete but not yet fully wired on this stack. Status table and §24.7 rewritten. ★ March 28, 2026 baseline preserved where unchanged.*

> **Stack scope note:** This chapter documents the 92-container rebuild configuration, a reduced but fully governed instance of the 105-container thesis stack described in Chapters 39–40. All mechanisms described here operate on this rebuild stack; where behavior differs from the canonical thesis configuration, that difference is explicitly noted with a cross-reference to the relevant chapter.

---

> **Why This Matters for Polymathmatic Geography**
> This chapter describes how material processed in the container paths and dual tracks feeds back into introspective records, long-term semantic memory, and high-level control settings. It supports:
> - **P1 – Every where is entangled** by ensuring that outputs from both the analytical and meaning-oriented tracks are written into shared ChromaDB (★★ **49 collections, 6,722,589+ total vectors**) and PostgreSQL `msallisgis` (port **5432**, **551 public tables**, 993 ZCTA centroids, supersedes March 28 baseline) and `msallis` (port **5433**, 5,416,521 GBIM entities with `confidence_decay` metadata, re-confirmed April 12 on this stack) memory structures that future queries across all paths can retrieve.
> - **P3 – Power has a geometry** by making feedback pathways explicit, named, and traceable — specific sync scripts, named ChromaDB collections, PostgreSQL tables, and queryable health endpoints — rather than allowing them to operate as hidden implicit updates. BBB audit trail events for every feedback decision persist to `allis-memory:8056` (authenticated black-box store on this stack; full event schema per Ch. 42) — the geometry of feedback power is durably logged.
> - **P5 – Design is a geographic act** by coupling semantic embeddings to specific spatial features in PostgreSQL GeoDB/PostGIS (`msallisgis:5432`, 551 public tables, 993 ZCTA centroids), so that feedback from community interactions becomes grounded in real West Virginia places and data.
> - **P12 – Intelligence with a ZIP code** by populating collections like `geodb_*`, `appalachian_english_corpus`, and `mountainshares_knowledge` with place-specific content sourced from PostgreSQL `msallisgis` that future RAG queries will retrieve. The AAPCAppE pipeline (`msallis_docs` 7,465 items) and `local_resources` (101 items, all 55 WV counties) now supplement this ZIP-coded substrate with systematic community resource data — including county-level emergency food and social services.
> - **P16 – Power accountable to place** by maintaining explicit sync logs, verification reports, and curator-facing endpoints so that communities can audit how and when the system's memory and control settings were updated. `allis-memory:8056` is the canonical durable store for BBB and truth-verdict audit events on this stack (event schema fully specified in Ch. 42) — accountability to place is persistently secured.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the concrete mechanisms by which container-level processing feeds back into introspective records, PostgreSQL long-term memory stores, and system configuration. Correctness and presence of these mechanisms are now continuously enforced by `scripts/VERIFYANDTEST.sh` and `scripts/preflight_gate.sh` rather than ad-hoc checks — see §24.2a.

```
┌─────────────────────────────────────────────────────────────┐
│   Feedback Pathways Architecture                            │
│   ★★ Updated April 12, 2026 — 92 containers Up             │
│      (92-container rebuild stack)                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Container-Level Processing (Chapters 19-23)                │
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
│  │     - PostgreSQL msallisgis (port 5432)        │         │
│  │       - 993 ZCTA centroids, 551 public tables  │         │
│  │         (supersedes March 28 baseline)         │         │
│  │     - PostgreSQL msallis (port 5433)           │         │
│  │       - 5,416,521 GBIM entities                │         │
│  │       - confidence_decay metadata              │         │
│  │       - re-confirmed April 12 on this stack    │         │
│  │     - ChromaDB (127.0.0.1:8002→8000)           │         │
│  │       49 collections, 6,722,589+ vectors       │         │
│  │       chroma 0.6.3 pinned                      │         │
│  │     - autonomous_learner (canonical community  │         │
│  │       memory collection; autonomouslearning    │         │
│  │       is historical name only)                 │         │
│  │     - local_resources: 101 items, 55 WV cntys  │         │
│  │     - msallis_docs: 7,465 items (Apr 12)       │         │
│  │     - mvw_gbim_landowner_spatial: 20,593 rows  │         │
│  │     - GeoDB sync scripts & logs                │         │
│  │     - AAPCAppE pipeline (ingest-api + watcher) │         │
│  │                                                │         │
│  │  3. Global Configuration & Control             │         │
│  │     - TruthFilterBBBValidator                  │         │
│  │       grounded in msallis:5433 GBIM entities   │         │
│  │     - masterspatialknowledge.csv               │         │
│  │     - Service registry (SERVICES dict)         │         │
│  │     - ueididentity & ueidaccessaudit tables    │         │
│  │     - allis-memory:8056 (auth black-box store) │         │
│  │       127.0.0.1, _auth() confirmed, API key set│         │
│  │     - Judge pipeline: containers running,      │         │
│  │       signing key wiring still a gate TODO     │         │
│  │       (see §24.4d; canonical in Ch. 33 & 42)   │         │
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

> **Figure 24.1.** Feedback pathways architecture: container-level processing feeds back through three directions — introspective records, long-term memory in PostgreSQL `msallisgis` (port **5432**, **551 public tables**, 993 ZCTA centroids, supersedes March 28 baseline), `msallis` (port **5433**, 5,416,521 GBIM entities with `confidence_decay` metadata, re-confirmed April 12 on this stack), and ChromaDB (**49 collections, 6,722,589+ total vectors**, chroma 0.6.3, host 127.0.0.1:8002→8000), and global configuration — with explicit logging and audit trails maintaining accountability to PostgreSQL ground truth. BBB and `truthverdict` audit events persist to `allis-memory:8056` (authenticated; event schema per Ch. 42). Gate suite (`VERIFYANDTEST.sh` + `preflight_gate.sh`) continuously enforces the presence and correctness of all mechanisms described in this chapter.

---

## Status as of ★★ April 12, 2026 (92-container rebuild stack)

| Category | Details |
|---|---|
| **Stack configuration** | **92 containers Up** on the rebuild stack (`docker ps -q \| wc -l`). This is a reduced but fully governed instance of the 105-container thesis stack described in Chapters 39–40. Zero Restarting, zero Exited. |
| **ChromaDB** | **49 collections, 6,722,589+ total vectors**, host **127.0.0.1:8002→8000** (container port 8000), **chroma 0.6.3 pinned**. `/api/v2/heartbeat` confirmed 200. Primary `chroma_db` directory ~12 GB. |
| **msallisgis** | PostgreSQL at **127.0.0.1:5432** — **551 public tables** (supersedes March 28 baseline of 501), **993 ZCTA centroids**. Actual `pg_size_pretty` result: see preflight gate log for current value. |
| **msallis** | PostgreSQL at **127.0.0.1:5433** — **5,416,521 GBIM entities** with `confidence_decay` metadata. Restored March 28 and **re-confirmed April 12 on this stack**. |
| **msallis_docs** | **7,465 items** as of April 12, 2026 on the rebuild stack. |
| **local_resources** | **101 items, all 55 WV counties seeded.** |
| **mvw_gbim_landowner_spatial** | **20,593 rows** (consistent with Ch. 36). |
| **autonomous_learner** | Canonical community-memory collection. `autonomouslearning` is a historical name only — see §24.3. |
| **RAG** | `allis-rag-server:8003/query` schema requires `collection` + `message`. A POST with `collection: "local_resources"` and `message: "nearest food pantry in Fayette County WV"` returns `n_results: 8` with documents including a Fayette County Community Action Agency food-assistance entry tagged `county=Fayette`, ZIPs 25801, 25840, 25880, plus neighboring county resource sheets. Preflight gate confirms: RAG query against `local_resources` returns ≥ 1 document. |
| **allis-memory** | **Reachable and healthy; auth enforced (`ALLIS_API_KEY` required).** Canonical durable audit sink for BBB and truth-verdict events on this stack. Precise event schema (Phase 1.4/2/3/4.5, AU-02 v2 fields) is specified and enforced in the 105-container thesis configuration described in Ch. 42. This stack treats `allis-memory` as an **authenticated black-box store**. |
| **Judge pipeline** | All five judges and `rag_grounded_v2` truth judge are running and integrated into the inference pipeline. **Signing key volume wiring still reported as a gate TODO on this stack.** Full ML-DSA-65 verdict enforcement loop is architecturally complete but not yet fully wired here; canonical fully wired implementation is in Chs. 33 and 42 (105-container thesis stack). |
| **EEG layer** | Delta EEG band (port 8073) is live and reporting PIA status. Theta/beta bands are implemented architecturally (see Ch. 42) but not exposed as HTTP endpoints in this 92-container configuration. **EEG feedback on this stack is partial.** |
| **Gate enforcement** | `scripts/VERIFYANDTEST.sh` + `scripts/preflight_gate.sh` continuously validate all feedback mechanisms described in this chapter. Gates currently confirm: Chroma collections ≥ 40 (49 found), `psychological_rag` ≥ 968 docs, `msallis_docs` and `local_resources` populated, `mvw_gbim_landowner_spatial` row count, BBB EthicalFilter 0 false positives, unauthenticated `/chat` → HTTP 401. |
| **Partially implemented** | Watchdog endpoints defined in code but not confirmed running as an independent service. Automated scheduled System Verification Reports not yet implemented. Not all ChromaDB instances listed in code are confirmed active — `allis-chroma` at 8002→8000 is the confirmed primary. Cross-path analytics not yet exposed via a dedicated endpoint. |
| **Future work** | Automated System Verification Report generation. Real-time feedback-volume dashboard. Automated `identitycandidates` promotion pipeline. Full deduplication at `ms_allis_memory` write path. Structured PIA review loop automation. Full ML-DSA-65 judge signing key wiring on this rebuild stack. |

> **Cross-reference:** The `background_rag_store` mechanism that produces `ms_allis_memory` entries is described in **Chapter 17 §17.6** and **Chapter 20 §20.3**. The `identitycandidates` and identity-layer elements fed by these feedback paths are described in **Chapter 22**. The dual-track structure whose outputs feed these mechanisms is described in **Chapter 23**.

---

# 24. Feedback into Introspective, Memory, and Control Layers

This chapter describes how material processed in the container paths and dual tracks feeds back into introspective records, long-term semantic memory in PostgreSQL `msallisgis` (port **5432**, **551 public tables**, 993 ZCTA centroids, supersedes March 28 baseline), `msallis` (port **5433**, **5,416,521 GBIM entities** with `confidence_decay` metadata, re-confirmed April 12 on this stack), and ChromaDB (**49 active collections, 6,722,589+ total vectors**, chroma 0.6.3, host 127.0.0.1:8002→8000), and high-level control settings.

This chapter documents the **92-container rebuild configuration**. In the current deployment, feedback mechanisms operate primarily through confirmed ChromaDB collections written by `background_rag_store`, PostgreSQL as the authoritative spatial and institutional ground truth, GeoDB synchronization scripts and their logs, `getidentitycandidates` and `getdatabasehealth` endpoints, and curator-facing tools for inspecting `ms_allis_memory`. As of April 12, 2026, the BBB audit trail persists to `allis-memory:8056` (authenticated; event schema per Ch. 42). All feedback mechanisms described in this chapter are continuously validated by `scripts/VERIFYANDTEST.sh` and `scripts/preflight_gate.sh`.

---

## 24.1 Overview of Feedback Paths

In the current deployment, the system provides three concrete directions for feedback from container-level activity into other layers, all ultimately anchored to PostgreSQL `msallisgis` and `msallis`.

**Introspective and health records.** `allis-main-brain` (port **8050**) exposes status endpoints that summarize per-service health in structured JSON, and the `/curator/background` endpoint provides direct inspection of `ms_allis_memory` entries. The secured gateway exposes `getdatabasehealth` (returning `status`, `database`, `identityelements`, `candidates`, `integrity`, timestamps anchored to `msallisgis:5432`) and `getidentitycandidates` (returning candidate identity statements validated against PostgreSQL GBIM from `msallis:5433` — 5,416,521 entities with `confidence_decay` metadata, re-confirmed April 12). BBB `barrier_stats` events persist to `allis-memory:8056` (authenticated black-box store; event schema per Ch. 42). Gate enforcement via `VERIFYANDTEST.sh` + `preflight_gate.sh` continuously validates these mechanisms — see §24.2a.

**Long-term semantic and spatial memory.** `allis-chroma` runs at **127.0.0.1:8002→8000** (container port 8000) with **49 confirmed collections** and **6,722,589+ total vectors** as of April 12, 2026, chroma 0.6.3 pinned. PostgreSQL `msallisgis` at **127.0.0.1:5432** (551 public tables, 993 ZCTA centroids, supersedes March 28 baseline) and `msallis` at **127.0.0.1:5433** (5,416,521 GBIM entities with `confidence_decay` metadata, re-confirmed April 12) serve as the authoritative sources for all spatial, institutional, and community data. RAG queries use explicit collection + message contracts — for example, `collection: "local_resources"` returns county-tagged Appalachian resource documents (see §24.3 for a concrete Fayette County example). The canonical community-memory collection is `autonomous_learner`; the name `autonomouslearning` is historical only. The AAPCAppE ingest pipeline (`allis-ingest-api` + `allis-ingest-watcher`) provides a systematic external-source long-term memory pathway: community resource documents flow into `msallis_docs` (7,465 items as of April 12) and `autonomous_learner`.

**Global configuration and control.** Truth filters, BBB verification validators grounded in PostgreSQL GBIM from `msallis:5433`, and `masterspatialknowledge.csv` define explicit policy constraints. `allis-memory:8056` is the canonical durable store for `TruthFilterBBBValidator` audit events on this stack (authenticated; event schema per Ch. 42). The judge pipeline (all five judges + `rag_grounded_v2`) is running and integrated; however, signing key volume wiring is still reported as a gate TODO on this 92-container stack — see §24.4d.

### 24.1a Consciousness Pipeline — OPERATIONAL

As of March 25, 2026 (confirmed Up on this rebuild stack), the consciousness pipeline (Chroma → WOAH → RAG → Bridge) is **OPERATIONAL**. The `allis-consciousness-bridge` is a confirmed feedback pathway writing into `consciousnesslayers` of every `UltimateResponse`:

- `chromadb_context` (str) — semantic context retrieved from ChromaDB at 127.0.0.1:8002→8000 (49 collections, 6,722,589+ total vectors)
- `woah_reasoning` (dict) — reasoning output from the WOAH algorithms layer
- `rag_consensus` (dict) — consensus result from the RAG bridge pipeline

These fields appear in `consciousnesslayers` on every call, making the consciousness bridge a first-class, always-active feedback path alongside `background_rag_store`. All `chromadb_context` retrieval uses 384-dim (`all-minilm:latest`) — the only compatible model for all 49 ChromaDB collections (see Ch. 19 §19.8.8a). See **Ch. 25 §25.9** for the full bridge patch log.

---

## 24.2 Writing Back to Introspective Records

In the current deployment, introspective records are implemented as confirmed endpoints, logs, and verification outputs anchored to PostgreSQL `msallisgis` and `msallis`.

**`getdatabasehealth` and `getidentitycandidates`.** `getidentitycandidates` returns statements such as "I serve the community," "I speak truth," "I value ethics," and "I am conscious," each with `importance` and diagnostic scores validated against PostgreSQL GBIM from `msallis:5433` (5,416,521 entities with `confidence_decay` metadata, re-confirmed April 12). `getdatabasehealth` reports `identityelements`, `candidates`, `integrity`, and timestamps for the `GISGEODBACTIVE` database (`msallisgis:5432`, 551 public tables, 993 ZCTA centroids).

**Main-brain status and `/curator/background`.** `allis-main-brain` status endpoints summarize per-service health including PostgreSQL connection status in a single queryable structure, confirmed operational 2026-02-15. The `/curator/background` endpoint provides direct inspection of `ms_allis_memory` ChromaDB contents, allowing operators to see exactly which `bg_<ISO8601>` entries were written and what metadata they carry.

**System Verification Reports.** Verification scripts produce outputs with sections including "VERIFICATION SUMMARY" and "HONEST ASSESSMENT," listing PostgreSQL `msallisgis` table sizes (now 551 public tables, supersedes March 28 501), ChromaDB operational status (49 collections, 6,722,589+ vectors), numbers of responding services, and the state of production testing. Generated by manual script execution; automated scheduled generation is future work.

**BBB barrier stats and secured audit trail.** `allis-blood-brain-barrier` (port **8016**) maintains `total_filtered`, `total_blocked`, and `pass_rate` counters. All BBB audit events persist to `allis-memory:8056` (authenticated black-box store; event schema for Phase 1.4/2/3/4.5 and AU-02 v2 fields is specified and enforced in the 105-container thesis configuration described in Ch. 42).

### 24.2a Gate-Enforced Feedback

`scripts/VERIFYANDTEST.sh` and `scripts/preflight_gate.sh` now continuously validate the feedback mechanisms described in this chapter. These scripts do not replace the endpoint and log verification described above — they run alongside it and provide machine-enforced confirmation that the mechanisms are live and populated.

Gates currently confirm on this rebuild stack:

- Chroma collections ≥ 40 (49 found)
- `psychological_rag` ≥ 968 docs
- `msallis_docs` populated (7,465 items)
- `local_resources` populated (101 items, all 55 WV counties)
- `mvw_gbim_landowner_spatial` row count (20,593 rows)
- BBB EthicalFilter 0 false positives
- Unauthenticated `/chat` → HTTP 401 (OI-36-A enforcement confirmed)

This gate suite is the enforcement layer for the feedback correctness guarantees stated throughout this chapter. If a gate fails, the feedback mechanism it validates is to be treated as degraded until the gate passes again.

---

## 24.3 Integration with Long-Term Memory

In the current deployment, material that passes through container and service layers is preserved in several confirmed long-term memory structures anchored to PostgreSQL `msallisgis` and `msallis`.

**`ms_allis_memory` — the primary feedback collection.** Every successful `/chat` call through `allis-main-brain` (port **8050**) produces a `bg_<ISO8601>` entry in `ms_allis_memory` ChromaDB (UUID: `79240788-0828-45f3-b1bc-a9a3593628a6`, confirmed in 49-collection inventory) via `background_rag_store`, with concatenated `USER:`/`EGERIA:` text and metadata including `userid`, `timestamp`, `type: "background"`, and `services: ["llm20production"]`. This collection is append-only in the current deployment. Confirmed 2026-02-15 (Chapter 9 §9.3.5, Chapter 17 §17.6).

> **March 25, 2026:** Emergent cross-session context passing (name, topic, entity recall) confirmed — likely via `_get_url` read path through the consciousness bridge into `ms_allis_memory`. See **Ch. 22 §22.9** (OI-05) for the full finding.

**PostgreSQL msallisgis and msallis — the authoritative ground truth.** PostgreSQL 16 at **127.0.0.1:5432** (**551 public tables**, 993 ZCTA centroids, supersedes March 28 baseline of 501 tables) and **127.0.0.1:5433** (5,416,521 GBIM entities with `confidence_decay` metadata, restored March 28 and **re-confirmed April 12 on this stack**) serve as the source of truth for all spatial, institutional, and community data. The `confidence_decay` metadata provides a graded evidentiary signal for feedback pathway triage — beliefs with high `confidence_decay` are weaker candidates for promotion to identity-level storage.

**Chroma + PostGIS integration and explicit RAG collection contracts.** As of April 12, 2026, ChromaDB has **49 collections** and RAG queries use explicit `collection` + `message` contracts. Callers must specify the collection name — e.g., `collection: "local_resources"` for WV county resource queries, or `collection: "appalachian_cultural_intelligence"` for broader cultural context. There is no implicit default collection.

> **Concrete RAG example (Fayette County food pantry).** A POST to `allis-rag-server:8003/query` with `collection: "local_resources"` and `message: "nearest food pantry in Fayette County WV"` returns `n_results: 8` with documents including a Fayette County Community Action Agency food-assistance entry tagged `county=Fayette`, ZIPs 25801, 25840, 25880, plus neighboring county resource sheets. This demonstrates that feedback from the AAPCAppE ingest pipeline and GBIM spatial data now supports county-level emergency food questions end-to-end — from ingestion through RAG retrieval to answer.

**`autonomous_learner` — canonical community-memory collection.** The canonical name for the community-memory ChromaDB collection on this stack is `autonomous_learner`. The name `autonomouslearning` was used historically and appears in older code and documentation — it is a historical alias only and should not be used in new code or chapter references.

**Additional confirmed ChromaDB collections.** `allis-chroma` at **127.0.0.1:8002→8000** (container port 8000, chroma 0.6.3 pinned) hosts **49 confirmed collections** including `allis_consciousness` (over 11,000 items), `autonomous_learner` (canonical), `learning_suggestions`, `research_history`, `spiritual_wisdom`, `appalachian_english_corpus`, `appalachian_cultural_intelligence`, `psychological_rag` (968 docs), `msallis_docs` (**7,465 items** as of April 12, 2026 on the rebuild stack), `local_resources` (**101 items, all 55 WV counties seeded**), `mvw_gbim_landowner_spatial` (**20,593 rows**, consistent with Ch. 36), and numerous `geodb_*` collections. Total confirmed vector count: **6,722,589+** as of April 12. Additional ChromaDB instances listed in code (`persistent/chroma`, `persistent/chroma_primary`, `services/prod_chroma_db`, `services/rag_chroma_db`) are not all confirmed active in the current deployment — `allis-chroma` at 8002→8000 is the confirmed primary.

**GeoDB sync scripts and logs.** The following scripts and their logs are confirmed on disk: `sync_geodb_to_chromadb.py`, `extract_all_chromadb_to_gis.py`, `vectorize_gis_to_chromadb.py`, `recover_chromadb_to_gisgeodb.py`, with corresponding logs `chromadb_v2_to_gis_sync.log`, `extract_all_chromadb_to_gis.log`, `vectorize_gis_to_chromadb.log`, `recover_chromadb_to_gisgeodb.log`. These logs record when new semantic embeddings are created, which PostgreSQL spatial features they correspond to (`msallisgis:5432` — 551 public tables, 993 ZCTA centroids), and how inconsistencies are resolved.

**AAPCAppE external-source ingest pathway.** The AAPCAppE ingest pipeline (`allis-ingest-api` + `allis-ingest-watcher`) provides a systematic external-source long-term memory pathway. Community resource documents flow into `msallis_docs` (**7,465 items** as of April 12, 2026 on the rebuild stack) and `autonomous_learner`. This is the first long-term memory pathway that directly ingests community resource data — including the `local_resources` collection (101 items, all 55 WV counties) — rather than deriving it from user interactions. See the Fayette County RAG example above for end-to-end confirmation.

**Service-specific knowledge bases.** Collections such as `mountainshares_knowledge`, `h4h_cultural_heritage`, `egeria_docs`, and `ms_allis_memory` allow certain services to promote their distilled outputs into reusable knowledge stores backed by PostgreSQL `msallisgis`, influencing future responses long after the original interactions.

---

## 24.4 Influence on Global Settings and Coordination

In the current deployment, high-level control is implemented through explicit configuration parameters and scripted verification anchored to PostgreSQL `msallisgis` and `msallis` rather than implicit learning from behavior alone.

**Truth and registration filters.** `TruthFilterBBBValidator` enforces minimum accuracy scores, expiration-date buffers, and age constraints validated against PostgreSQL GBIM ground truth from `msallis:5433` (5,416,521 entities with `confidence_decay` metadata, re-confirmed April 12), and records verification decisions in `ueididentity` and `ueidaccessaudit` tables. All `TruthFilterBBBValidator` audit events persist to `allis-memory:8056` (authenticated black-box store; event schema per Ch. 42). `GISTruthFilter` validates geographic data against USGS, NRCS, NOAA, and US Census Bureau sources before allowing writes to PostgreSQL GeoDB (`msallisgis:5432`). For full detail on these validators see **Chapter 16 §16.5**.

**`masterspatialknowledge.csv` and access documentation.** `masterspatialknowledge.csv` is confirmed present with `accesslevelrequired` and `isproprietary` fields describing PostgreSQL GeoDB access policies for `msallisgis:5432` (551 public tables). Security-related files (`SECURITY-OVERVIEW.md`, `SOURCEACCESS.md`, `accesscontrollevels.csv`) are checked by verification routines to ensure that documentation and access models exist alongside PostgreSQL data.

**Service registry and orchestration parameters.** The `SERVICES` dictionary in `allis-main-brain` (port **8050**) lists expected modules and ports including PostgreSQL `msallisgis` at port **5432** and `msallis` at port **5433**. `discover_services()` health-checks these at request time and updates `available_services`. For the canonical description of how this operates see **Chapter 17 §17.2**.

### 24.4a AU-02 v2 — Active at BBB Layer

AU-02 v2 (regex v2: 6 compiled patterns, ~0ms; embedding v2: 30 seeds, cosine threshold ≥ 0.72, ~300ms cached; false-positive guard: 8 overly broad triggers removed) is active and enforced at the BBB layer on this rebuild stack. All intercepts are routed to `allis-memory:8056` in the production configuration described in Ch. 42. This rebuild stack uses the same BBB container and filters, but local event inspection of AU-02 v2 intercepts is deferred to that canonical description — this stack treats `allis-memory` as an authenticated black-box store.

### 24.4b EEG Layer — Partial on This Stack

On this 92-container stack, the **delta EEG band (port 8073) is live** and reporting PIA status. The theta and beta bands are implemented architecturally (see Ch. 42 §42.13) but are **not exposed as HTTP endpoints in this configuration**. EEG feedback on this rebuild stack is therefore **partial** — delta only. Full three-band EEG feedback is available in the 105-container thesis stack described in Ch. 42 §42.13.

### 24.4c allis-memory:8056 — Authenticated Black-Box Store

`allis-memory:8056` is reachable and healthy, requires `ALLIS_API_KEY`, and is the canonical durable audit sink for BBB and truth-verdict events on this stack. The precise event schema — including Phase 1.4, Phase 2, Phase 3, Phase 4.5, and AU-02 v2 fields — is specified and enforced in the 105-container thesis configuration described in **Chapter 42**. This chapter treats `allis-memory` as an authenticated black-box store: events flow in, authentication is confirmed, and retrieval of specific event records is deferred to the canonical Ch. 42 description.

Any prior examples in this chapter that assume direct JSON inspection of `/events` on this rebuild stack should be treated as illustrative of the schema rather than confirmed live queries on the 92-container configuration.

### 24.4d Judge Pipeline and ML-DSA-65 Verdict Signing — Status on This Stack

On this 92-container rebuild stack, all five judges and the `rag_grounded_v2` truth judge are running and integrated into the inference pipeline. However, the **preflight gate still reports missing signing-key volume wiring** for judge services. As such, the full ML-DSA-65 verdict enforcement loop is **architecturally complete but not yet fully wired** on this rebuild stack. The canonical, fully wired implementation — with liboqs ML-DSA-65 confirmed as the primary runtime, `dilithium_py` as graceful fallback, all five judges signing, and `rotate_judge_keys.sh` production-grade — is documented in **Chapters 33 and 42** for the 105-container thesis stack.

---

## 24.5 Cross-Path Effects

In the current deployment, because the same ChromaDB collections (49 collections, 6,722,589+ vectors), PostgreSQL `msallisgis` and `msallis` structures, and configuration parameters are shared across both the meaning-oriented and analytical tracks (see Chapter 23), feedback from one path naturally affects the other.

**Shared semantic and spatial memory.** Collections such as `mountainshares_knowledge`, `spiritual_wisdom`, `allis_consciousness`, `autonomous_learner` (canonical; `autonomouslearning` is historical), and `geodb_*` datasets are accessible by both experiential/meaning-oriented modules and technical/analytical modules. A new embedding written to any of these collections by a `background_rag_store` task or a sync script changes what both tracks retrieve for future queries about the same region or topic. The `local_resources` collection (101 items, all 55 WV counties) and `msallis_docs` (7,465 items, AAPCAppE) are now shared community resource substrates — regional service and community resource embeddings can surface in both analytical and meaning-oriented RAG retrievals.

**Shared identity and database health.** `getdatabasehealth` and `getidentitycandidates` are not track-specific. If container-level processing leads to changes in identity candidates validated against PostgreSQL GBIM from `msallis:5433` (5,416,521 entities with `confidence_decay` metadata, re-confirmed April 12) or if verification activity alters the integrity status of PostgreSQL GeoDB (`msallisgis:5432`, 551 public tables), those changes are visible to any path that queries these endpoints.

**Coordinated sync scripts.** GeoDB/ChromaDB sync scripts alter the shared memory substrate — changing how PostgreSQL features are embedded, which ChromaDB collections are active (49 collections), or how provider summaries are generated. Both the analytical path and the meaning-oriented path see a consistently updated view anchored to PostgreSQL `msallisgis`.

> **⚠️ neuro_master status:** `allis-neurobiological-master` (port **8018**) was unreachable at chapter open (March 28) and was subsequently confirmed healthy (HTTP 200, 131 processes) as of Chapter 25 closure (April 12, 2026 — see Ch. 25 §25.4). Chroma health checks rerouted directly to `allis-chroma:8000` as a bridge patch (see Ch. 25 §25.9 Patch 1) remain in place for resilience. The neuro_master open item is closed as of Ch. 25 seal.

---

## 24.6 Logging and Audit of Feedback

In the current deployment, explicit mechanisms for logging and auditing feedback processes with traceability to PostgreSQL `msallisgis` and `msallis` are confirmed present, though their completeness varies.

**GeoDB/ChromaDB sync logs.** `chromadb_v2_to_gis_sync.log`, `extract_all_chromadb_to_gis.log`, `vectorize_gis_to_chromadb.log`, and `recover_chromadb_to_gisgeodb.log` record how ChromaDB collections (49 collections, 6,722,589+ vectors as of April 12) and PostgreSQL GeoDB datasets (`msallisgis:5432` — 551 public tables, 993 ZCTA centroids) are updated and reconciled.

**RAG and bridge logs.** Bridge logs (e.g. `bridge_ms_allis_main_gateway_to_chromadb_rag_helper.log`, `ms_allis_chromadb_query_9014.log`) capture interactions between the main gateway and ChromaDB-backed RAG helpers, recording queries, result counts, and error conditions. The consciousness bridge produces `chromadb_context`, `woah_reasoning`, and `rag_consensus` on every call — these fields are themselves auditable artifacts of the RAG feedback loop.

**`/curator/background` and verification outputs.** The `/curator/background` endpoint on `allis-main-brain` (port **8050**) provides a stable, auditable view of `ms_allis_memory` ChromaDB contents (confirmed in 49-collection inventory). Historical System Verification Report scripts produce human-readable summaries with timestamps, PostgreSQL table counts, and candid operational assessments.

**`ueididentity` and `ueidaccessaudit` tables, and `allis-memory:8056`.** `TruthFilterBBBValidator` writes verification outcomes and audit records into `ueididentity` and `ueidaccessaudit` tables with references to PostgreSQL GBIM validation from `msallis:5433` (5,416,521 entities with `confidence_decay` metadata, re-confirmed April 12). All BBB and `truthverdict` audit events additionally persist to `allis-memory:8056` (authenticated black-box store; event schema per Ch. 42) — the audit trail for feedback decisions is doubly secured: PostgreSQL tables and authenticated `allis-memory` store.

**Gate enforcement logs.** `scripts/VERIFYANDTEST.sh` and `scripts/preflight_gate.sh` produce machine-readable pass/fail records that serve as a continuous audit of feedback mechanism presence and correctness. The current gate suite confirms 49 Chroma collections, `local_resources` and `msallis_docs` populated, `mvw_gbim_landowner_spatial` at 20,593 rows, 0 EthicalFilter false positives, and HTTP 401 on unauthenticated `/chat` — see §24.2a for the full confirmed gate list.

---

## 24.7 Summary

Three feedback directions are **fully live** on this 92-container rebuild stack:

1. **Introspective health records** — `getdatabasehealth`, `getidentitycandidates`, `/curator/background`, BBB `barrier_stats`, System Verification Reports, and the consciousness bridge all provide confirmed, queryable introspective snapshots of the running system, anchored to PostgreSQL `msallisgis` (551 public tables, 993 ZCTA centroids) and `msallis` (5,416,521 GBIM entities with `confidence_decay` metadata, re-confirmed April 12).

2. **Long-term semantic and spatial memory** — ChromaDB (49 collections, 6,722,589+ vectors, chroma 0.6.3, host 127.0.0.1:8002→8000), PostgreSQL `msallisgis` and `msallis`, GeoDB sync scripts, `background_rag_store`, and the AAPCAppE ingest pipeline (`msallis_docs` 7,465 items, `local_resources` 101 items, all 55 WV counties) are all active and feeding the long-term memory substrate.

3. **Global configuration and control** — `TruthFilterBBBValidator`, `masterspatialknowledge.csv`, the service registry, AU-02 v2 at the BBB layer, and `allis-memory:8056` define explicit, auditable control constraints enforced at every inference step.

Their correctness and presence are now **enforced by `VERIFYANDTEST.sh` and `preflight_gate.sh`** rather than ad-hoc checks — see §24.2a for the confirmed gate list.

**One concrete RAG example proves feedback end-to-end on this stack.** A POST to `allis-rag-server:8003/query` with `collection: "local_resources"` and `message: "nearest food pantry in Fayette County WV"` returns documents including a Fayette County Community Action Agency food-assistance entry tagged `county=Fayette`, ZIPs 25801, 25840, 25880, plus neighboring county resource sheets. This confirms that AAPCAppE ingest → ChromaDB storage → RAG retrieval → answer is a closed, working loop on this stack.

**Two mechanisms are governed at the thesis level (Chapters 33–42) and partially implemented on this rebuild stack.** `allis-memory:8056` is reachable and authenticated, but its event schema (Phase 1.4/2/3/4.5, AU-02 v2 fields) is specified and enforced in the 105-container thesis configuration described in Ch. 42 — this stack treats it as an authenticated black-box store. The ML-DSA-65 judge signing loop is architecturally complete but judge signing-key volume wiring is still a gate TODO on this stack; the canonical fully wired implementation is in Chs. 33 and 42.

The `ms_allis_memory` `_get_url` read path through the consciousness bridge is a confirmed emergent vector for cross-session context passing (OI-05 — see Ch. 22 §22.9). EEG feedback on this rebuild stack is partial — delta band only; theta/beta are architecturally implemented (Ch. 42 §42.13) but not exposed as HTTP endpoints here. For the canonical description of how `background_rag_store` fits into the live `ultimatechat` execution sequence, see **Chapter 17**. For the identity layer these feedback paths ultimately serve, see **Chapter 22**.

---

*Last updated: April 12, 2026 by Carrie Kidd (Mamma Kidd), Oak Hill / Mount Hope WV*

*★ March 28, 2026: 96 containers Up on original stack — baselines established for ChromaDB (40 collections, 6,675,442 vectors), msallisgis (501 tables), msallis_docs (4,192 items), allis-memory:8056 secured.*

*★★ April 12, 2026: Chapter revised for 92-container rebuild stack. All hard numbers updated (see top-of-chapter revision log). §24.2a Gate-Enforced Feedback added. §24.4a AU-02 v2 status added. §24.4b EEG partial-implementation note added. §24.4c allis-memory black-box treatment added. §24.4d Judge pipeline / ML-DSA-65 signing status on this stack added. Concrete Fayette County RAG example added (§24.3, §24.7). autonomous_learner canonical collection name confirmed throughout. Status table and §24.7 fully rewritten. Cross-reference to Ch. 25 neuro_master closure added (§24.5).*
