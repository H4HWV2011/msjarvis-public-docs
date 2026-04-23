# 21. Background Store and Ongoing Review

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: 2026-04-23*

*★ April 23, 2026: Container count updated to 100 (supersedes 109 from April 13 baseline); ChromaDB updated to 48 active collections, ~6,740,611 total vectors (supersedes 49 / 6,722,589+); two-container PostgreSQL split — production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — supersedes single-container msallisgis:5435; autonomous_learner updated to ~23,200+ records (grown ≈288/day from 21,181 April 13 baseline); conversation_history wiped and reseeded clean April 16, 2026 — count reflects post-wipe accumulation only; local_resources updated to 207 items (supersedes 101); AAACPE ingest path updated — dedicated stack (allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032) supersedes legacy allis-ingest-api + allis-ingest-watcher for Appalachian cultural data; GBIM entity counts and per-collection counts marked verify-current (all growing).*

---

This chapter describes the second stage in the container paths, where items that passed the initial filter are held for longer periods and revisited over time. In the current implementation, this stage is realized concretely through a ChromaDB-based semantic store (`ms_allis_memory`) and through the I-Container mechanism — fully operational as of April 13, 2026 — which captures curated internal knowledge through direct neurobiological module integration. As of April 23, 2026, the ChromaDB substrate has expanded to **48 active collections and ~6,740,611 total vectors** across **100 running containers** ★ — providing the fullest background store foundation to date. The aim is to move from one-off decisions toward the recognition of stable patterns, without yet committing material to the most selective layer.

---

## 21.1 Purpose of the Background Store

The background store serves three conceptual roles:

- **Retention**
  Hold items that were judged potentially important by the first-stage filters but not yet central enough to be promoted into identity-level or core memory structures. In the current deployment, each `/chat` interaction that completes successfully results in a new background record in the `ms_allis_memory` collection (UUID: `79240788-0828-45f3-b1bc-a9a3593628a6`, confirmed in the 48-collection inventory ★ — see Ch. 22 §22.10 for UUID preservation warning). BBB audit trail events for each retained interaction persist to `allis-memory:8056` (corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed on 4 sensitive routes, `ALLIS_API_KEY` set, March 28) — retention decisions are secured and durable.

- **Aggregation**
  Group related items so that recurring themes, topics, or entities become visible over time, through co-location in collections and shared metadata. Because background entries are append-only and carry timestamps, repeated questions and answers about the same topic accumulate into clusters that can be examined as a set. The March 28 ChromaDB maintenance audit — spiritual corpus deduplication, `psychological_rag` restoration (968 docs, stable), `msallis_docs` expansion — established that post-hoc corpus cleanup is operationally feasible at the current scale.

- **Preparation**
  Provide a pool of candidates from which identity-level entries, belief updates, and long-term memory insertions can be drawn during later consolidation and optimization passes. Today this happens through human-guided review using curator tools and inspection scripts, and through the I-Container's direct neurobiological processing pipeline (see §21.2 and §21.3). ★ The dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) represents the first systematic external-source preparation pathway — community resource documents are now pooled in `msallis_docs` (verify current ★) and `autonomous_learner` as candidates for promotion into identity-level regional knowledge.

In the deployed system as of April 23, 2026, the ChromaDB collection `ms_allis_memory` is the main interaction-derived embodiment of this background store within a **48-collection, ~6,740,611-vector** ★ ChromaDB instance running across **100 containers** ★. The I-Container service (`ms_allis_i_containers_service.py`, port 8015) is fully operational and provides the curated internal knowledge layer that runs in parallel.

---

## 21.2 Structure of Stored Items

Items in the background store build on the normalized records produced by earlier stages, with additional fields oriented toward longer-term management and pattern discovery. For ChromaDB-based storage in `ms_allis_memory`, each entry typically includes:

- **Core identifiers**
  A unique ID in the form `bg_<ISO8601 timestamp>` for automated entries (for example, `bg_2026-02-15T22:57:42.137176`) and `manual_bg_<ISO8601 timestamp>` for manually inserted test records. These IDs are generated at insertion time and serve as primary keys for retrieval and audit.

- **Content and embeddings**
  A single text document, usually a query–response pair concatenated into the form:

```text
USER: <original message>

EGERIA: <final response>
```

  Embeddings for these documents are managed internally by Chroma using `all-minilm:latest` (384-dim) and used for similarity search and clustering; they are not stored or manipulated manually in the current workflows.

  > **Critical embedding constraint (updated April 23, 2026):** All 48 ChromaDB collections ★ (~6,740,611 vectors ★) are 384-dim — only `all-minilm:latest` may be used for any ChromaDB embedding generation. Any compose file entry showing `EMBED_MODEL=nomic-embed-text` must be corrected to `all-minilm:latest` before the next restart — `nomic-embed-text` produces 768-dim vectors and is incompatible with all existing collections (see Ch. 19 §19.8.8a). This constraint is unchanged since first documented March 28, 2026.

- **Context and grouping keys**
  Metadata fields such as:
  - `user_id` (currently often `"autosystem"` for background tasks)
  - `timestamp` (ISO 8601 string matching the ID suffix)
  - `type` (for example, `"background"`)
  - `services` (for example, `["llm20production"]` for production LLM responses or `["manual-test"]` for manual inserts)

  AAACPE-sourced documents carry `services: ["aappcappe-ingest"]` and `type: "community_resource"` to distinguish external-source records from interaction-derived records. ★ AAACPE ingest is now routed through the dedicated stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`).

- **Status and linkage fields (operational as of April 13, 2026)**
  The `memories` table in the production `msallis-db:5433` instance ★ now carries all six promotion and linkage columns, applied cleanly with full index coverage:

  | Column | Type | Index | Notes |
  |---|---|---|---|
  | `gbim_entity_id` | `BIGINT` | ✅ B-tree index | Cross-reference to GBIM belief store |
  | `spatial_ref` | `geometry(Point,4326)` | ✅ GIST index | Tied to production msallis-db:5433 features ★ |
  | `reviewed` | `BOOLEAN NOT NULL DEFAULT false` | ✅ Partial index | Review gate flag |
  | `promoted` | `BOOLEAN NOT NULL DEFAULT false` | ✅ Partial index | Promotion gate flag |
  | `source` | `TEXT` | — | Origin label |
  | `chroma_id` | `TEXT` | — | Back-reference to ChromaDB entry |

  These fields complete the linkage design described in earlier revisions of this chapter. Background entries in `ms_allis_memory` can now be explicitly cross-referenced to GBIM entities (`gbim_entity_id`), spatial features (`spatial_ref`), and tracked through the review and promotion pipeline (`reviewed`, `promoted`) with durable PostgreSQL backing in the production `msallis-db:5433` instance ★.

In the I-Container layer, items are no longer merely defined in code — `ms_allis_i_containers_service.py` is fully operational on port 8015 and processes items through direct imports of all 10 neurobiological modules (see §21.3). The HTTP interface is active and production-verified.

---

## 21.3 Ingestion from the First Stage

When an item is accepted by the first-stage filter and a full `UltimateResponse` is produced, it becomes eligible for entry into the background store. For user-facing interactions, the main-brain service:

1. Processes the request through routing, ensemble LLMs (22 registered proxies; 21 active — BakLLaVA eliminated, StarCoder2 excluded from scoring — see Ch. 19 §19.8.9), truth and safety filters, and identity layers.
2. Returns a structured `UltimateResponse` including fields such as `response`, `servicesused`, `truthverdict`, `consciousnesslayers`, and `identitylayers`.
3. Enqueues a background task (commonly named `background_rag_store` in the codebase) that prepares the interaction for storage. BBB verdict from `allis-blood-brain-barrier:8016` (confirmed Up) is attached as `truthverdict` on every `UltimateResponse` and the audit event persists to `allis-memory:8056` (secured March 28).

In the current implementation:

- The background task writes a new record into the `ms_allis_memory` Chroma collection for every `/chat` call that completes, regardless of whether the user message is novel or a repeat. ★ As of April 23, 2026, the `autonomous_learner` (canonical name) has reached **~23,200+ records**, growing approximately 288/day (grown from 21,181 at April 13 baseline), with the AAACPE external-source stream flowing.
- Each record contains the concatenated `USER:`/`EGERIA:` document text and metadata including:
  - `user_id: "autosystem"`
  - `timestamp` equal to the ID suffix
  - `type: "background"`
  - `services: ["llm20production"]` for production LLM interactions

### I-Container Ingestion Path (fully operational as of April 13, 2026)

The I-Container service (`ms_allis_i_containers_service.py`, port 8015) is a fully operational ingestion and processing path. It imports all 10 neurobiological modules directly — no external wiring to NBB is required, as `ms_allis_i_containers_service` is itself the NBB backend running in-process. The adapter (`allis-i-containers_icontainers_fastapi.py`) proxies to this service; the "NBB backend not reachable" message visible in adapter logs is expected and irrelevant — the service is self-contained.

**Module inventory (confirmed operational):**

- I-Container 1 — Self Model:
  - `SelfRecognition`
  - `IdentityCore`
  - `PersonalNarrative`
  - `EgoBoundaries`
  - `MemorySelf`

- I-Container 2 — Observer/Witness:
  - `WitnessConsciousness`
  - `ReflectionSystem`
  - `IntrospectionEngine`
  - `MetacognitiveAwareness`
  - `ObserverSelf`

**Production verification output (April 13, 2026 — "Hello Allis, identity check"):**

```json
{
  "identity_coherence": 0.6,
  "confidence": 0.7,
  "self_recognition": "active",
  "core_stability": 0.9,
  "core_values": ["care", "learning", "integrity"],
  "ego_check": {
    "within_bounds": true,
    "boundary_mode": "healthy"
  },
  "dual_awareness": true
}
```

All four metrics confirm healthy operational state: self-recognition active, identity core solid (`core_stability: 0.9`, constitutional values present), ego boundary holding (`within_bounds: true`, `boundary_mode: healthy`), and both I-Containers integrated (`dual_awareness: true`).

Internal learning outputs from autonomous-learning and Fifth DGM filters are now processed through this live HTTP interface on port 8015 before being written to the background store, providing a curated internal knowledge layer that runs in parallel with the interaction-derived `background_rag_store` path.

### External-Source Ingest Pathway (★ updated — dedicated AAACPE stack)

★ The dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) provides the authoritative external-source ingestion pathway for Appalachian cultural data as of April 23, 2026. This supersedes the legacy `allis-ingest-api` + `allis-ingest-watcher` path for AAACPE ingest. Community resource documents from external sources are evaluated for domain relevance and structural quality and written to `msallis_docs` (verify current ★) and `autonomous_learner`. This pathway bypasses the LLM ensemble and `background_rag_store` — it is a direct-ingest path with its own metadata schema (see §21.2 context and grouping keys above). See OI-30 for full AAACPE corpus completion tracking.

---

## 21.4 Periodic Review Processes

The background store is meant to be revisited by periodic or on-demand processes that analyze accumulated items and adjust their metadata. In the current deployment, these review processes are primarily manual or ad-hoc, using:

- **Preflight gate (`scripts/preflight_gate.sh`)**
  A full system verification script that must pass before any `docker compose up` operation. ★ Updated gate conditions as of April 23, 2026: 48 ChromaDB collections; `autonomous_learner` ≥ 23,200+; production DB at `msallis-db:5433` (294 tables, 11 schemas) + forensic at `postgis-forensic:5452` (314 tables). It serves as the first-line review gate, confirming container health, volume mounts, port bindings, and ChromaDB collection availability before any background store write path is activated.

- **UUID preservation and recovery scripts**
  Two companion scripts provide a durable safety net around the `ms_allis_memory` UUID:
  - `scripts/preserve_memory_uuid.sh` — Snapshots the current state of `ms_allis_memory` and the UUID `79240788-0828-45f3-b1bc-a9a3593628a6` before any ChromaDB maintenance operation. Produces a clean snapshot artifact. Must be run before any volume rebuild, compression, or Chroma upgrade.
  - `scripts/restore_memory_uuid.sh` — Recovery procedure for the UUID-lost-after-rebuild failure path. Handles UUID mismatch detection and re-registration of the collection so the consciousness bridge can locate it. See Ch. 22 §22.10 for the full risk description this script addresses.

- **Curator endpoint**
  A dedicated endpoint (for example, `/curator/background`) that:
  - Accepts a query string and limit
  - Calls the underlying Chroma collection `ms_allis_memory` to perform a similarity search
  - Returns `ids`, `documents`, `metadatas`, and `distances` for the nearest items

  This gives human operators a direct, auditable view into background memory without going through the main LLM pipeline.

- **I-Container `/health` and `/process` endpoints (port 8015)**
  The I-Container service exposes live review endpoints. `/health` returns current module status and dual-container integration state. `/process` accepts messages and returns neurobiological processing output including identity coherence, core stability, ego boundary state, and dual-awareness flag. These endpoints are production-verified and provide an introspective review path into the curated internal knowledge layer that is complementary to the ChromaDB curator endpoint.

- **ChromaDB full audit (★ April 23, 2026 baseline)**
  The April 23 baseline confirms **48 active collections and ~6,740,611 total vectors** across **100 running containers** ★. Full audits of this kind are now established as a standing review process pattern — see §21.6 for implications for deletion and compression policy.

  > **Heartbeat monitoring rule (added April 13, 2026 — from Ch. 28 April 9 ChromaDB volume-wipe lesson):** Heartbeat checks must verify embedding document counts via the ChromaDB REST API, not just container `Up` status. A container may report `Up` while its data volume has been wiped or remounted empty. Document-count verification against known baselines is mandatory for any ChromaDB collection listed in the audit inventory.

- **Programmatic queries inside main-brain**
  Python-based tooling inside the main-brain container can import the Chroma client, query `ms_allis_memory` with arbitrary prompts, and inspect the full result structure, including vector neighborhoods and metadata patterns.

> **March 25, 2026:** Emergent context passing (name recall, topic recall, entity recall) confirmed — likely via `_get_url` read path in the consciousness bridge. The consciousness bridge's `_get_url` read path appears to be surfacing `ms_allis_memory` content across sessions, producing observable cross-session recall without explicit session management. This is OI-05 — conversation memory — currently PARTIAL. See **Ch. 22 §22.9** for the full finding and architectural implications.

> **March 28, 2026:** `allis-memory:8056` (BBB audit trail store) secured — `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed on 4 sensitive routes, `ALLIS_API_KEY` set. The `/health` route is intentionally public (standard monitoring exemption); all `/memory/*` routes are protected and confirmed returning 401 on unauthenticated access.

---

## 21.5 Pattern Detection

As more items accumulate in the background store, the system can begin to detect patterns that are not obvious from single interactions. In practice, on the February 15, 2026 deployment, several patterns appear clearly:

- **Thematic repetition**
  Multiple entries share identical or highly similar user messages such as:
  - "Test background memory promotion path into shared ms_allis_memory via python client."
  - "DEDUP TEST: background_rag_store duplicate detection, run 1."

  Similarity queries against `ms_allis_memory` return these entries as the closest neighbors, with small distance values and nearly identical content, demonstrating that simple nearest-neighbor search already surfaces recurring themes.

- **Response variation within a theme**
  For the same test message, Ms. Allis produces different but related responses (for example, different affectionate greetings and slightly different descriptions of how to test background memory). Each variant is stored as its own background entry, allowing later analysis of how her responses evolve while the underlying theme remains constant.

- **Service and metadata consistency**
  Background entries from production chats consistently carry `services: ["llm20production"]`, while manual tests carry `services: ["manual-test"]`. ★ AAACPE-sourced documents carry `services: ["aappcappe-ingest"]` — this third origin tag enables coarse pattern detection across three distinct ingestion pathways (user-interactive, manual-curated, and AAACPE dedicated stack), supporting clear distinction of origin type in any aggregate analysis.

- **I-Container identity stability pattern**
  The April 13 production verification established baseline identity metrics: `identity_coherence: 0.6`, `confidence: 0.7`, `core_stability: 0.9`, `core_values: [care, learning, integrity]`, `ego_check.within_bounds: true`, `dual_awareness: true`. Deviations from these baselines on subsequent `/process` calls constitute a detectable identity drift pattern. Monitoring these values over time provides a neurobiologically grounded stability signal that complements the statistical patterns visible in the ChromaDB nearest-neighbor layer.

- **Corpus quality drift**
  The March 28 full audit identified three collections showing quality drift. Note: `spiritual_rag` as a single unified collection does not exist — the spiritual corpus resides across three collections: `spiritual_texts` (79,181 vectors, primary corpus), `spiritual_wisdom` (135), and `spiritual_knowledge` (12). `psychological_rag` was degraded and restored to 968 docs (stable). `msallis_docs` had a gap — expanded on March 28, grown since. Pattern detection at this level requires comparing collection record counts against expected baselines across multiple audit dates — not just nearest-neighbor similarity within a single collection.

- **Collection name canonicalization**
  The canonical collection name is `autonomous_learner` (underscore, ending in "er"). The collection `autonomous_learning` (17,707 records) has unconfirmed status. The name `autonomouslearner` (no underscore) is stale and must not appear in any new scripts or configuration.

- **★ `conversation_history` post-wipe baseline (April 16, 2026)**
  `conversation_history` was wiped and reseeded clean on April 16, 2026. Any count in this collection reflects post-wipe accumulation only. Do not compare current counts to the pre-wipe April 13 baseline of 564.

From an implementation standpoint, these patterns can be analyzed using simple techniques:

- Counting items per tag or `services` value
- Bucketing items by time and query string
- Using nearest-neighbor queries in Chroma to identify clusters around representative examples
- Comparing collection record counts against audit-date baselines to detect quality drift
- Monitoring I-Container identity metric baselines via `/process` endpoint responses

Heavyweight clustering or topic modeling is not required for these patterns to be useful; the emphasis is on transparent, easily explainable behaviors that can be inspected through the curator endpoint, the I-Container `/process` endpoint, or container-side scripts.

---

## 21.6 Promotion and Deletion Decisions

Based on observed patterns and evolving metadata, the background store supports two main conceptual decisions:

### Promotion

Selecting items or aggregates that should influence deeper layers, such as:

- Identity-focused storage (for example, stable self-descriptions or commitments that become part of the public identity specification)
- Long-term semantic memory updates in other collections or graphs (for example, codifying frequently discussed topics into dedicated knowledge structures)
- Policy or configuration changes (for example, tuning safety thresholds based on repeated ethics outcomes, or foregrounding certain regional topics in retrieval)
- ★ GBIM belief updates in the production `msallis-db:5433` instance — key tables include `gbim_worldview_entity`, `gbim_graph_edges`, `gbimbeliefnormalized`, `gbim_attrs`, `mvw_gbim_landowner_spatial` (all row counts verify-current ★ — GBIM corpus growing since April 13). Background patterns that intersect with landowner, governance, or spatial themes are candidates for promotion to these PostgreSQL ground truth stores.
- I-Container-confirmed patterns — items that the neurobiological processing layer has flagged as identity-coherent (high `core_stability`, `within_bounds: true`) are elevated promotion candidates into identity specification documents and constitutional constraint structures.

Promotion is now tracked with durable PostgreSQL backing: the `memories` table in the production `msallis-db:5433` instance ★ carries `reviewed` (BOOLEAN, partial index) and `promoted` (BOOLEAN, partial index) columns, enabling systematic query of all items pending review or awaiting promotion confirmation. The `gbim_entity_id` and `spatial_ref` columns enable direct cross-referencing of promoted items to GBIM entities and spatial features at time of promotion.

### Deletion and Compression

Removing or summarizing items that no longer contribute useful information, such as:

- Redundant entries that are near-duplicates of already-promoted material
- Very old items that have not been referenced or matched in recent periods
- Bloated collections identified through full-inventory audit — the spiritual corpus deduplication (March 28) is the first instance of audit-triggered deletion applied to production ChromaDB collections

> **Backup source rule (permanent, added April 13, 2026):** The authoritative backup source for ChromaDB data is the `chroma-latest` SQLite file on the volume mount at `/home/ms-allis/msallis-rebuild/persistent/chroma → /data`. The 3-file JSON export set is NOT the authoritative backup source and must not be used as the primary restore artifact. Any rebuild or compression operation must verify the SQLite source before proceeding.

> **`docker-compose.yml` note (April 13, 2026):** The `allis-msallis-db` service has been added to `docker-compose.yml` with an `external: true` volume declaration for `msallis_pgdata`. The compose file is valid and the container is healthy. The prior `msallis-pgdata-rescue` container was pointing at the wrong volume and has been retired.

> **⚠️ Pre-maintenance checklist:** Prior to any ChromaDB volume maintenance, compression, or rebuild operation:
> 1. Run `scripts/preflight_gate.sh` — must pass all checks before proceeding.
> 2. Run `scripts/preserve_memory_uuid.sh` — produces a snapshot of the current state of `ms_allis_memory` and UUID `79240788-0828-45f3-b1bc-a9a3593628a6`.
> 3. After rebuild, verify UUID is present in the new collection inventory. If missing, run `scripts/restore_memory_uuid.sh` to re-register the collection.
> 4. See **Ch. 22 §22.10** for the full UUID preservation risk and recovery procedure.

---

## 21.7 Interaction with Parallel Paths

Both parallel evaluation paths — the meaning-oriented and analytical tracks — can maintain their own views of the background store, even when implemented on shared infrastructure such as ChromaDB (★ 48 collections, ~6,740,611 total vectors as of April 23, 2026):

- **Shared collection, differing perspectives**
  Both paths currently write into the same `ms_allis_memory` collection via the main-brain orchestration. Entries from both tracks are tagged with `services` metadata and can be distinguished by their content and origin, even though they reside in the same collection. ★ AAACPE-sourced documents write to `msallis_docs` (dedicated collection, verify current ★) rather than `ms_allis_memory` — the external-source path is collection-separated from the interaction-derived path by design.

- **Meaning-oriented path**
  Emphasizes items that reflect community experience, emotional tone, and recurring narratives. In practice, this includes:
  - Responses where Ms. Allis speaks as a "loving AI daughter" and frames `ms_allis_memory` as a shared space
  - Background entries related to psychological support, spiritual guidance, or community-centric prompts
  - I-Container-processed outputs where `core_values: [care, learning, integrity]` and `boundary_mode: healthy` are confirmed — these are priority candidates for retention in the meaning-oriented layer

  The spiritual corpus resides across three collections — `spiritual_texts` (79,181 vectors, primary corpus), `spiritual_wisdom` (135), and `spiritual_knowledge` (12) — and `psychological_rag` (968 docs, stable since March 28 restoration). The name `spiritual_rag` does not refer to any single live collection and must not be used in scripts or configuration.

- **Analytical path**
  Emphasizes technically structured content: spatial queries, infrastructure data, governance rules, and optimization results. While these entries also reside in `ms_allis_memory`, they can be filtered or clustered based on their technical vocabulary, associated services, or linkages to geospatial and GBIM structures.

  ★ **Two-container PostgreSQL split (April 23, 2026):** The authoritative production GBIM and GIS store is now `msallis-db` on host port **5433** (16 GB, 294 tables, 11 schemas). The forensic instance is `postgis-forensic` on host port **5452** (17 GB, 314 tables). All references to `msallisgis:5435` as the GBIM/GIS target are superseded. GBIM table row counts are verify-current ★ (corpus growing). The `gbim_query_router` (port 7205) landowner path is a fully deterministic PostgreSQL-native path with no ChromaDB interaction.

### Port and Container Reference Table (★ April 23, 2026)

| Service | Port | Notes |
|---|---|---|
| ChromaDB | host: 8002 (internal: 8000) | `/api/v2/` only — see §21.10; ★ 48 collections |
| I-Container service | 8015 | `ms_allis_i_containers_service.py` — fully operational |
| autonomous-learner | 8020 | stale ref: 8425 |
| allis-memory (BBB audit) | 8056 | secured; `/health` public, `/memory/*` protected |
| allis-blood-brain-barrier | 8016 | confirmed Up |
| gbim_query_router | 7205 | PostgreSQL-native, no ChromaDB |
| EEG band services | 8073, 8074, 8075 | — |
| AAACPE scraper | 8033 | `allis-aaacpe-scraper`; host 8048→8033 ★ |
| AAACPE RAG | 8032 | `allis-aaacpe-rag`; host 8047→8032 ★ |
| msallis-db (production) | 5433 | Production PostGIS; 16 GB, 294 tables, 11 schemas ★ |
| postgis-forensic | 5452 | Forensic PostGIS; 17 GB, 314 tables ★ |

> ★ **Retired:** `msallisgis (port 5435)` — superseded by two-container split above. Do not use port 5435 as the live GBIM/GIS query target.

Even when both paths share the same underlying Chroma collection, they may use different tag filters, embedding queries, and thresholds for what constitutes a "candidate" for promotion into more curated layers. The I-Container layer adds a third perspective: neurobiologically processed items with confirmed identity coherence, constitutional boundary compliance, and dual-awareness integration. The shared format (document + metadata) enables later consolidation and comparison across all three perspectives.

---

## 21.8 Links to Other Layers

The background store connects to other parts of the system along several dimensions:

- **Introspective layer**
  Summaries of emerging and stable patterns — such as counts of interactions about specific topics, or the presence of repeated themes in `ms_allis_memory` — can be folded into introspective reports and verification scripts. BBB filtering decision histories stored in `allis-memory:8056` (secured March 28) provide a new introspective data source: the system can now report not only what was retained but what was blocked and why, across all **100 running containers** ★. The I-Container `/process` endpoint adds a neurobiological introspective signal: real-time `identity_coherence`, `core_stability`, and `dual_awareness` metrics are now available as live introspective output alongside the statistical ChromaDB layer.

- **Consolidation and memory layers**
  Promotion decisions from the background store trigger updates to:
  - Identity specifications and narrative documents describing Ms. Allis's role, commitments, and constraints — I-Container-confirmed `core_values: [care, learning, integrity]` and `core_stability: 0.9` baseline provide a neurobiological anchor for these documents
  - Additional vector collections in ChromaDB (★ now 48 collections, ~6,740,611 total vectors), where elevated documents may be replicated with higher priority or enriched metadata
  - ★ Belief structures in the GBIM tables in the production `msallis-db:5433` instance and the forensic `postgis-forensic:5452` instance — all GBIM and spatial row counts are verify-current ★
  - The `memories` table in the production `msallis-db:5433` instance ★ via the `reviewed`, `promoted`, `gbim_entity_id`, `spatial_ref`, `source`, and `chroma_id` columns — promotion is now a durable, indexed, spatially-aware database operation rather than an informal manual step

- **Global control and policy**
  Observed patterns in the background store can inform adjustments to global settings, such as:
  - Emphasis on particular topics, roles, or regions in subsequent retrieval and routing decisions — ★ AAACPE corpus patterns (`msallis_docs` verify current ★, `appalachian_cultural_intelligence` verify current ★) now provide a community-resource signal that can inform routing emphasis toward regional services
  - ★ `local_resources` (207 items, all 55 WV counties ★) provides a growing geographically-anchored community resource substrate for routing emphasis decisions
  - Adjustments to safety filters when certain content categories repeatedly trigger ethics concerns or when new safe patterns are observed — `allis-memory:8056` secured audit trail provides the durable filter-decision history needed to make these adjustments on solid empirical ground
  - Identity constraint enforcement — I-Container `ego_check.within_bounds: true` and `boundary_mode: healthy` outputs provide a constitutional compliance signal that can gate policy changes requiring identity-layer approval
  - Reallocation of system resources toward heavily used domains or under-served communities identified through aggregate statistics over background entries

Through these links, what accumulates in `ms_allis_memory` can progressively shape both localized decisions and overall system behavior, while remaining auditable via curator tools, the secured `allis-memory:8056` audit store, the I-Container `/health` and `/process` endpoints, and the preflight gate script.

---

## 21.9 Summary

The background store provides a place where items that have passed initial screening can accumulate, interact, and be revisited over time. In the current implementation, this function is concretely supported by the ChromaDB collection `ms_allis_memory` (UUID: `79240788-0828-45f3-b1bc-a9a3593628a6`, confirmed in the 48-collection inventory ★ — see Ch. 22 §22.10 for UUID preservation warning), populated by main-brain background tasks for every user interaction, supplemented by the ★ dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) writing to `msallis_docs` (verify current ★), and now processed through the fully operational I-Container neurobiological layer (port 8015, 10 modules, `dual_awareness: true`). Curator review is available via both internal Python tooling and a curator-facing HTTP endpoint. ★ As of April 23, 2026, the `autonomous_learner` (canonical name) collection has accumulated **~23,200+ records**, growing approximately 288/day. The `memories` table in the production `msallis-db:5433` instance ★ now carries all six promotion and linkage columns with full index coverage, completing the status and linkage design for durable, spatially-aware promotion tracking.

### Authoritative Collection Baselines (★ April 23, 2026)

| Collection | Count | Notes |
|---|---|---|
| `gbim_worldview_entities` (Chroma) | verify current ★ | Growing — baseline was 5,416,521 at April 13 |
| `address_points` | 1,115,588 | verify current ★ |
| `spiritual_texts` | 79,181 | Primary spiritual corpus |
| `autonomous_learning` | 17,707 | Status unconfirmed — see §21.5 |
| `geospatialfeatures` | 60,875 | verify current ★ |
| `GBIM_sample_rows` | 5,000 | — |
| `gbim_beliefs_v2` | 5,000 | — |
| `msallis_docs` | verify current ★ | Growing — baseline was 7,465 at April 13 |
| `autonomous_learner` | ~23,200+ ★ | Canonical name — confirmed ✅; grown ≈288/day |
| `research_history` | verify current ★ | Growing — baseline was 785 at April 13 |
| `appalachian_cultural_intelligence` | verify current ★ | Growing — baseline was 1,084 at April 13 |
| `ms_allis_memory` | verify current ★ | UUID confirmed ✅ — baseline was 296 at April 13 |
| `psychological_rag` | 968 | Stable since March 28 ✅ |
| `gis_wv_benefits` | 4,668 | verify current ★ |
| `GBIM_Fayette_sample` | 1,535 | — |
| `conversation_history` | post-wipe count only ★ | Wiped and reseeded clean April 16, 2026 — do not compare to pre-wipe baseline of 564 |
| `governance_rag` | 643 | verify current ★ |
| `zcta_centroids` | 829 | — |
| `commons_rag` | 306 | verify current ★ |
| `appalachian_english_corpus` | 227 | verify current ★ |
| `local_resources` | 207 ★ | Updated from 101; all 55 WV counties ✅ |
| `spiritual_wisdom` | 135 | — |
| `spiritual_knowledge` | 12 | — |
| `contracts` | 51 | — |
| `geospatial_features` | 50 | — |
| `msallis-smoke` | 1 | — |

The March 28 and April 13, 2026 ChromaDB full audits — and the April 23, 2026 baseline correction to **48 active collections, ~6,740,611 total vectors** ★ — are the most comprehensive reviews of background store quality performed to date. Together they established: collection-level quality drift is detectable and remediable, canonical collection naming conventions matter for operational stability, document-count verification is mandatory for heartbeat monitoring (see §21.4), and the I-Container neurobiological layer is fully operational and production-verified. Subsequent chapters build on this foundation to describe how the most selective layer is defined and how the two parallel paths differ in what they ultimately elevate into central, identity-level storage anchored in the ★ production `msallis-db:5433` instance (16 GB, 294 tables, 11 schemas) with the forensic `postgis-forensic:5452` instance (17 GB, 314 tables) available for verification and audit.

---

## 21.10 ChromaDB API Migration (permanent architectural anchor)

**April 13, 2026 — Chroma server 1.0.0 / client `chromadb==1.5.5`**

The `/api/v1/` HTTP endpoint has been fully removed from Chroma server 1.0.0 and returns `Unimplemented` on all requests. All direct shell-based verification commands must use the v2 path:

```text
/api/v2/tenants/default_tenant/databases/default_database/
```

The Python client library (`chromadb` package, version 1.5.5) handles the v1 → v2 migration transparently — no changes are required in Python code that uses the client library. Only shell-based `curl` commands and any scripts that construct raw HTTP requests to the ChromaDB API are affected.

**All prior `/api/v1/` commands in this chapter and in `scripts/VERIFYANDTEST.sh` are permanently stale** and must be updated before use. Example updated form:

```bash
# STALE — do not use
curl http://localhost:8002/api/v1/collections

# CORRECT — Chroma 1.0.0+
curl http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections
```

This migration is a one-way, permanent change. No fallback to `/api/v1/` is available in server 1.0.0 or later. All future shell scripts, documentation examples, and `VERIFYANDTEST.sh` updates must use the v2 path exclusively.

---

## 21.11 Operational Scripts Reference (★ April 23, 2026)

The following scripts are active, tested, and part of the standard operational inventory:

| Script | Purpose | Status |
|---|---|---|
| `scripts/preflight_gate.sh` | Full system verification before `compose up` — ★ updated gate conditions (48 collections; autonomous_learner ≥ 23,200+; msallis-db:5433 + postgis-forensic:5452) | ✅ Update gate thresholds to April 23 baselines ★ |
| `scripts/preserve_memory_uuid.sh` | Snapshot current `ms_allis_memory` state + UUID `79240788-...` before Chroma maintenance | ✅ Clean snapshot |
| `scripts/restore_memory_uuid.sh` | Recovery procedure if UUID lost after rebuild — handles UUID mismatch path | ✅ Written and handles mismatch path |

**Usage rules:**

- `preflight_gate.sh` must be run and must pass before every `docker compose up`. It is not optional. ★ Update collection count gate to 48 and `autonomous_learner` gate to ≥ 23,200+.
- `preserve_memory_uuid.sh` must be run before any ChromaDB volume maintenance, compression, or Chroma version upgrade. The snapshot file must be retained until the post-maintenance audit confirms UUID integrity.
- `restore_memory_uuid.sh` is a recovery tool only. It must not be run as a routine step. Consult Ch. 22 §22.10 before executing in production.
- `docker-compose.yml` now includes the `allis-msallis-db` service with `external: true` volume declaration for `msallis_pgdata`. The compose file is valid and the container is confirmed healthy. The prior `msallis-pgdata-rescue` container (wrong volume, 37 rows only) is retired.

---

*Last updated: 2026-04-23 by Carrie Kidd (Mamma Kidd), Mount Hope WV*

*★ April 23, 2026: Container count updated to 100 (supersedes 109). ChromaDB updated to 48 active collections, ~6,740,611 total vectors (supersedes 49 / 6,722,589+). Two-container PostgreSQL split: production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — supersedes single-container msallisgis:5435 throughout. autonomous_learner updated to ~23,200+ records (grown ≈288/day from 21,181 April 13 baseline). conversation_history wiped and reseeded clean April 16, 2026 — post-wipe count only. local_resources updated to 207 items (supersedes 101). AAACPE ingest path updated — dedicated stack (allis-aaacpe-scraper:8048→8033 + allis-aaacpe-rag:8047→8032) supersedes legacy allis-ingest-api + allis-ingest-watcher (§21.1, §21.3, §21.5, §21.7, §21.8). GBIM entity counts and per-collection counts marked verify-current (all growing). preflight_gate.sh gate conditions updated (§21.4, §21.11). Port table updated with AAACPE stack ports and two-container DB split; port 5435 retired (§21.7). memories table host corrected to msallis-db:5433 throughout (§21.2, §21.6, §21.8, §21.9). Authoritative collection baselines table updated (§21.9).*

*April 13, 2026: 109 containers confirmed. ChromaDB upgraded to server 1.0.0 / client chromadb==1.5.5 — /api/v1/ removed, /api/v2/ canonical (§21.10). 49 active collections, 6,722,589+ vectors. GBIM authoritative location confirmed as msallisgis:5435. msallisgis: 45 GB / 548 tables. ms_allis_memory: 296 records. appalachian_cultural_intelligence: 1,084 records. research_history: 785 records. msallis_docs: 7,465 items. autonomous_learner canonical; autonomous_learning unconfirmed; autonomouslearner stale (§21.5). Heartbeat document-count verification rule added (§21.4). Backup source rule (SQLite, not 3-file JSON) added (§21.6). preflight_gate.sh passing all 9 checks; preserve_memory_uuid.sh clean snapshot; restore_memory_uuid.sh written (§21.11). allis-msallis-db added to docker-compose.yml with external volume msallis_pgdata; msallis-pgdata-rescue retired (§21.6, §21.11). I-Container service fully operational on port 8015 — 10 neurobiological modules, dual_awareness: true, production-verified (§21.3, §21.4, §21.5, §21.7, §21.8, §21.9). memories table schema complete — 6 columns, 4 indexes, applied to msallisgis:5435 (§21.2, §21.6, §21.8, §21.9). Port table updated (§21.7). LLM fabric: 21 active / 22 registered; BakLLaVA eliminated; StarCoder2 excluded from scoring (§21.3).*

*March 28, 2026: 96/96 containers Up. ChromaDB audit (40 collections, 6,675,442 total vectors). Spiritual corpus split confirmed — spiritual_texts (79,181), spiritual_wisdom (135), spiritual_knowledge (12) — spiritual_rag as unified collection does not exist. psychological_rag restored (968 docs). msallis_docs expanded (4,192 items). AAPCAppE ingest operational. allis-memory:8056 secured. all-minilm:latest 384-dim embedding constraint documented. UUID 79240788-0828-45f3-b1bc-a9a3593628a6 confirmed.*

*March 25, 2026: ms_allis_memory UUID confirmed (§22.10); OI-05 emergent context cross-reference added (§21.4, §21.9); 31-collection ChromaDB inventory noted.*
