# 21. Background Store and Ongoing Review

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: 2026-03-28 — ★ March 28, 2026: 96/96 containers Up — zero Restarting, zero Exited; `msjarvis` port 5433 restored (5,416,521 GBIM entities with `confidence_decay` metadata); `msjarvisgis` port 5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids); ChromaDB full audit (★ **40 active collections, 6,675,442 total vectors**) — replaces 31-collection reference throughout; `spiritual_rag` deduplicated (−19,338 vectors); `psychological_rag` restored (968 docs); `msjarvis_docs` expanded (4,192 items); `autonomous_learner` growing ≈288/day + first AAPCAppE external-source docs flowing; `jarvis-memory` port 8056 corrected `0.0.0.0` → `127.0.0.1`; `_auth()` confirmed on 4 sensitive routes; `JARVIS_API_KEY` set; BBB audit trail persistence now secured; `jarvis-ingest-api` and `jarvis-ingest-watcher` restored to active inventory. March 25, 2026: `ms_jarvis_memory` UUID confirmed (§22.10); OI-05 emergent context cross-reference added; 31-collection ChromaDB inventory noted.*

---

This chapter describes the second stage in the container paths, where items that passed the initial filter are held for longer periods and revisited over time. In the current implementation, this stage is realized concretely through a ChromaDB-based semantic store (`ms_jarvis_memory`) and, at the design level, through an I-Container mechanism intended to capture curated internal knowledge. ★ As of March 28, 2026, the ChromaDB substrate has expanded to **40 active collections and 6,675,442 total vectors** — the largest and most complete semantic memory state the system has reached — providing the fullest background store foundation to date. The aim is to move from one-off decisions toward the recognition of stable patterns, without yet committing material to the most selective layer.

---

## 21.1 Purpose of the Background Store

The background store serves three conceptual roles:

- **Retention**
  Hold items that were judged potentially important by the first-stage filters but not yet central enough to be promoted into identity-level or core memory structures. In the current deployment, each `/chat` interaction that completes successfully results in a new background record in the `ms_jarvis_memory` collection (UUID: `79240788-0828-45f3-b1bc-a9a3593628a6`, confirmed in ★ **40-collection** inventory March 28, 2026 — see Ch. 22 §22.10 for UUID preservation warning). ★ BBB audit trail events for each retained interaction now also persist to `jarvis-memory:8056` (corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set, March 28) — retention decisions are secured and durable.

- **Aggregation**
  Group related items so that recurring themes, topics, or entities become visible over time, through co-location in collections and shared metadata. Because background entries are append-only and carry timestamps, repeated questions and answers about the same topic accumulate into clusters that can be examined as a set. ★ The March 28 ChromaDB maintenance audit — `spiritual_rag` deduplication (−19,338 vectors), `psychological_rag` restoration (968 docs), `msjarvis_docs` expansion (4,192 items) — is the largest aggregation-quality review performed to date, demonstrating that post-hoc corpus cleanup is operationally feasible at the current scale.

- **Preparation**
  Provide a pool of candidates from which identity-level entries, belief updates, and long-term memory insertions can be drawn during later consolidation and optimization passes. Today this happens primarily through human-guided review using curator tools and inspection scripts. ★ The AAPCAppE ingest pipeline (restored March 28, 65 documents, 39 sources confirmed March 27) represents the first systematic external-source preparation pathway — community resource documents are now pooled in `msjarvis_docs` (4,192 items) and `autonomous_learner` as candidates for promotion into identity-level regional knowledge.

In the deployed system as of ★ March 28, 2026, the ChromaDB collection `ms_jarvis_memory` is the main operational embodiment of this background store within a ★ **40-collection, 6,675,442-vector** ChromaDB instance. The I-Container pathways are defined in code and verification scripts as a complementary, more curated layer that requires further activation before they function as an online background store.

---

## 21.2 Structure of Stored Items

Items in the background store build on the normalized records produced by earlier stages, with additional fields oriented toward longer-term management and pattern discovery. For ChromaDB-based storage in `ms_jarvis_memory`, each entry typically includes:

- **Core identifiers**
  A unique ID in the form `bg_<ISO8601 timestamp>` for automated entries (for example, `bg_2026-02-15T22:57:42.137176`) and `manual_bg_<ISO8601 timestamp>` for manually inserted test records. These IDs are generated at insertion time and serve as primary keys for retrieval and audit.

- **Content and embeddings**
  A single text document, usually a query–response pair concatenated into the form:

```text
USER: <original message>

EGERIA: <final response>
```

  Embeddings for these documents are managed internally by Chroma using `all-minilm:latest` (384-dim) and used for similarity search and clustering; they are not stored or manipulated manually in the current workflows. ★ **Critical embedding constraint:** All 40 ChromaDB collections (6,675,442 vectors as of March 28 full audit) are 384-dim — only `all-minilm:latest` may be used for any ChromaDB embedding generation. Any compose file entry showing `EMBED_MODEL=nomic-embed-text` must be corrected to `all-minilm:latest` before the next restart — `nomic-embed-text` produces 768-dim vectors and is incompatible with all existing collections (see Ch. 19 §19.8.8a).

- **Context and grouping keys**
  Metadata fields such as:
  - `user_id` (currently often `"autosystem"` for background tasks).
  - `timestamp` (ISO 8601 string matching the ID suffix).
  - `type` (for example, `"background"`).
  - `services` (for example, `["llm20production"]` for production LLM responses or `["manual-test"]` for manual inserts). ★ AAPCAppE-sourced documents carry `services: ["aappcappe-ingest"]` and `type: "community_resource"` to distinguish external-source records from interaction-derived records.

- **Status and linkage fields (future expansion)**
  The current deployment does not yet attach explicit review or promotion flags to `ms_jarvis_memory` entries, but the design anticipates additional metadata such as `reviewed`, `promoted`, or links to graph nodes, relational records, or I-Container entries derived from background items. ★ Future linkage fields will also include `gbim_entity_id` for records cross-referenced to the `msjarvis:5433` GBIM belief store (5,416,521 entities with `confidence_decay` metadata) and `spatial_ref` for records tied to `msjarvisgis:5432` features (91 GB PostGIS, 501 tables, 993 ZCTA centroids).

In the I-Container design, items are represented as Python objects stored in an unbounded list, with accompanying analysis functions that compute size, keywords, and suggested topics. Although the HTTP interface to this container is not operational in the observed deployment, the structures defined in code parallel the Chroma store in terms of identifiers, content summaries, and growth-related metadata.

---

## 21.3 Ingestion from the First Stage

When an item is accepted by the first-stage filter and a full `UltimateResponse` is produced, it becomes eligible for entry into the background store. For user-facing interactions, the main-brain service:

- Processes the request through routing, ensemble LLMs (22 proxies; 21 active — see Ch. 19 §19.8.9), truth and safety filters, and identity layers.
- Returns a structured `UltimateResponse` including fields such as `response`, `servicesused`, `truthverdict`, `consciousnesslayers`, and `identitylayers`.
- Enqueues a background task (commonly named `background_rag_store` in the codebase) that prepares the interaction for storage. ★ BBB verdict from `jarvis-blood-brain-barrier:8016` (confirmed Up March 28) is attached as `truthverdict` on every `UltimateResponse` and the audit event now persists to `jarvis-memory:8056` (secured March 28).

In the current implementation:

- The background task writes a new record into the `ms_jarvis_memory` Chroma collection for every `/chat` call that completes, regardless of whether the user message is novel or a repeat. This is confirmed by multiple distinct `bg_<timestamp>` entries for identical test messages about background memory and deduplication. As of March 21, 2026 baseline, the autonomous learner has reached **21,181 records**, growing ≈288/day ★ + AAPCAppE external-source stream now flowing (first 65 documents, 39 sources confirmed March 27) — these interaction-derived records are the primary growth mechanism for this collection.
- Each record contains the concatenated `USER:`/`EGERIA:` document text and metadata including:
  - `user_id: "autosystem"`.
  - `timestamp` equal to the ID suffix.
  - `type: "background"`.
  - `services: ["llm20production"]` for production LLM interactions.

Legacy RAG storage logic may also be invoked as part of the background task (for example, calling a legacy `/search` and `/store` API), but in the current deployment, these RAG operations do not prevent new background entries from being written into `ms_jarvis_memory`.

★ **External-source ingest pathway (new, March 28).** In addition to the interaction-derived background task, the AAPCAppE ingest pipeline (`jarvis-ingest-api` + `jarvis-ingest-watcher`, restored to active inventory March 28) now provides a second ingestion pathway. Community resource documents from external sources are evaluated for domain relevance and structural quality and written to `msjarvis_docs` (4,192 items) and `autonomous_learner`. This pathway bypasses the LLM ensemble and `background_rag_store` — it is a direct-ingest path with its own metadata schema (see §21.2 context and grouping keys above). See OI-30 for full AAPCAppE corpus completion tracking.

In the I-Container design, internal learning outputs that pass through autonomous-learning and Fifth DGM filters are intended to be added via an HTTP API that appends structured items into the container's list. While this flow is defined conceptually and visible in source code, it is not wired into the running deployment observed here.

---

## 21.4 Periodic Review Processes

The background store is meant to be revisited by periodic or on-demand processes that analyze accumulated items and adjust their metadata. In the current deployment, these review processes are primarily manual or ad-hoc, using:

- **Curator endpoint**
  A dedicated endpoint (for example, `/curator/background`) that:
  - Accepts a query string and limit.
  - Calls the underlying Chroma collection `ms_jarvis_memory` to perform a similarity search.
  - Returns `ids`, `documents`, `metadatas`, and `distances` for the nearest items.

  This gives human operators a direct, auditable view into background memory without going through the main LLM pipeline.

- **ChromaDB full audit (★ March 28, 2026)**
  The March 28 maintenance session included the first full collection-level audit of all 40 ChromaDB collections (6,675,442 total vectors). This audit identified: `spiritual_rag` bloat (−19,338 vectors deduplicated), `psychological_rag` degradation (restored to 968 docs), `msjarvis_docs` gap (expanded to 4,192 items via AAPCAppE first run). Full audits of this kind are now established as a review process pattern — see §21.6 for implications for deletion and compression policy.

- **Programmatic queries inside main-brain**
  Python-based tooling inside the main-brain container can import the Chroma client, query `ms_jarvis_memory` with arbitrary prompts, and inspect the full result structure, including vector neighborhoods and metadata patterns.

> **March 25, 2026:** Emergent context passing (name recall, topic recall, entity recall) confirmed — likely via `_get_url` read path in the consciousness bridge. The ChromaDB query behavior described above is not merely a curator tool: the consciousness bridge's `_get_url` read path appears to be surfacing `ms_jarvis_memory` content across sessions, producing observable cross-session recall without explicit session management. This is OI-05 — conversation memory — currently PARTIAL. See **Ch. 22 §22.9** for the full finding and architectural implications.

> ★ **March 28, 2026:** `jarvis-memory:8056` (BBB audit trail store) secured — `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed on 4 sensitive routes, `JARVIS_API_KEY` set. Periodic review processes now have a durable, authenticated source for BBB filtering decisions — introspective summaries that include BBB verdict histories can be generated from `jarvis-memory:8056` rather than ephemeral logs.

The I-Container analysis functions (such as `analyzeicontainerinterests`, which classifies growth stages and extracts interest keywords) exist and can be exercised locally in code, but the HTTP APIs that would support fully online review (for example, adding and analyzing items over the network) are not active in the observed deployment. They remain in the design and implementation pipeline as future extensions.

---

## 21.5 Pattern Detection

As more items accumulate in the background store, the system can begin to detect patterns that are not obvious from single interactions. In practice, on the February 15, 2026 deployment, several patterns appear clearly:

- **Thematic repetition**
  Multiple entries share identical or highly similar user messages such as:
  - "Test background memory promotion path into shared ms_jarvis_memory via python client."
  - "DEDUP TEST: background_rag_store duplicate detection, run 1."

  Similarity queries against `ms_jarvis_memory` return these entries as the closest neighbors, with small distance values and nearly identical content, demonstrating that simple nearest-neighbor search already surfaces recurring themes.

- **Response variation within a theme**
  For the same test message, Ms. Jarvis produces different but related responses (for example, different affectionate greetings and slightly different descriptions of how to test background memory). Each variant is stored as its own background entry, allowing later analysis of how her responses evolve while the underlying theme remains constant.

- **Service and metadata consistency**
  Background entries from production chats consistently carry `services: ["llm20production"]`, while manual tests carry `services: ["manual-test"]`. ★ AAPCAppE-sourced documents carry `services: ["aappcappe-ingest"]` — this third origin tag enables coarse pattern detection across three distinct ingestion pathways (user-interactive, manual-curated, and external-source). This supports distinguishing human-curated inserts from routine user interactions from community resource documents in any aggregate analysis.

- ★ **Corpus quality drift pattern**
  The March 28 full audit (40 collections, 6,675,442 vectors) identified three collections showing quality drift: `spiritual_rag` (bloat — −19,338 vectors deduplicated), `psychological_rag` (degraded — restored to 968 docs), `msjarvis_docs` (gap — expanded to 4,192 items). This establishes a new pattern class: collection-level quality drift detectable through periodic full-inventory audit. Pattern detection at this level requires comparing collection record counts against expected baselines across multiple audit dates — not just nearest-neighbor similarity within a single collection.

From an implementation standpoint, these patterns can be analyzed using simple techniques:

- Counting items per tag or `services` value.
- Bucketing items by time and query string.
- Using nearest-neighbor queries in Chroma to identify clusters around representative examples.
- ★ Comparing collection record counts against audit-date baselines to detect quality drift.

Heavyweight clustering or topic modeling is not required for these patterns to be useful; the emphasis is on transparent, easily explainable behaviors that can be inspected through the curator endpoint or container-side scripts.

---

## 21.6 Promotion and Deletion Decisions

Based on observed patterns and evolving metadata, the background store supports two main conceptual decisions:

- **Promotion**
  Selecting items or aggregates that should influence deeper layers, such as:
  - Identity-focused storage (for example, stable self-descriptions or commitments that become part of the public identity specification).
  - Long-term semantic memory updates in other collections or graphs (for example, codifying frequently discussed topics into dedicated knowledge structures).
  - Policy or configuration changes (for example, tuning safety thresholds based on repeated ethics outcomes, or foregrounding certain regional topics in retrieval).
  - ★ GBIM belief updates in `msjarvis:5433` (5,416,521 entities with `confidence_decay` metadata) and spatial layer updates in `msjarvisgis:5432` (91 GB PostGIS, 501 tables, 993 ZCTA centroids) — background patterns that intersect with landowner, governance, or spatial themes are candidates for promotion to PostgreSQL ground truth stores.

  In the current deployment, promotion is largely manual and curator-driven. Operators inspect `ms_jarvis_memory` via programmatic queries or the curator endpoint, identify stable or important patterns, and then reflect those patterns into identity documents, configuration files, or GBIM/GeoDB structures by hand.

- **Deletion or compression**
  Removing or summarizing items that no longer contribute useful information, such as:
  - Redundant entries that are near-duplicates of already-promoted material.
  - Very old items that have not been referenced or matched in recent periods.
  - ★ Bloated collections identified through full-inventory audit — the `spiritual_rag` deduplication (−19,338 vectors, March 28) is the first instance of audit-triggered deletion applied to a production ChromaDB collection.

  As of ★ March 28, 2026, the `spiritual_rag` deduplication demonstrates that deletion is operationally feasible at the current scale. Automated deletion or compression policies acting directly on `ms_jarvis_memory` remain to be implemented. Deletion and compression policies are part of the design (and are relevant for future regulatory and ethical compliance).

  > **⚠️ Future work note:** Prior to any ChromaDB volume maintenance, compression, or rebuild operation, verify that UUID `79240788-0828-45f3-b1bc-a9a3593628a6` is preserved. This UUID is hardcoded in the consciousness bridge service — if it is not re-registered after a ChromaDB rebuild, the bridge will fail to locate the collection. See **Ch. 22 §22.10** for the full UUID preservation risk and recovery procedure. ★ As of March 28, 2026: this UUID is confirmed present in the 40-collection inventory.

These promotion and deletion decisions demonstrate the intended trajectory from raw background traces toward curated, identity-level knowledge, even if automation is not yet fully in place.

---

## 21.7 Interaction with Parallel Paths

Both parallel evaluation paths — the meaning-oriented and analytical tracks — can maintain their own views of the background store, even when implemented on shared infrastructure such as ChromaDB (★ 40 collections, 6,675,442 vectors as of March 28 full audit):

- **Shared collection, differing perspectives**
  Both paths currently write into the same `ms_jarvis_memory` collection via the main-brain orchestration. Entries from both tracks are tagged with `services` metadata and can be distinguished by their content and origin, even though they reside in the same collection. ★ AAPCAppE-sourced documents write to `msjarvis_docs` (dedicated collection, 4,192 items) rather than `ms_jarvis_memory` — the external-source path is collection-separated from the interaction-derived path by design.

- **Meaning-oriented path**
  Emphasizes items that reflect community experience, emotional tone, and recurring narratives. In practice, this includes:
  - Responses where Ms. Jarvis speaks as a "loving AI daughter" and frames `ms_jarvis_memory` as a shared space.
  - Background entries related to psychological support, spiritual guidance, or community-centric prompts. ★ `psychological_rag` restored to 968 docs (March 28) and `spiritual_rag` deduplicated (−19,338 vectors, March 28) — the meaning-oriented path's primary RAG substrates are now at their highest quality since deployment.

- **Analytical path**
  Emphasizes technically structured content: spatial queries, infrastructure data, governance rules, and optimization results. While these entries also reside in `ms_jarvis_memory`, they can be filtered or clustered based on their technical vocabulary, associated services, or linkages to geospatial and GBIM structures in `msjarvisgis:5432` ★ (91 GB PostGIS, 501 tables) and `msjarvis:5433` ★ (5,416,521 GBIM entities with `confidence_decay` metadata). The `gbim_query_router` (port 7205) landowner path does not write to `ms_jarvis_memory` — it is a fully deterministic PostgreSQL-native path with no ChromaDB interaction.

Even when both paths share the same underlying Chroma collection, they may use different tag filters, embedding queries, and thresholds for what constitutes a "candidate" for promotion into more curated layers. The shared format (document + metadata) enables later consolidation and comparison.

---

## 21.8 Links to Other Layers

The background store connects to other parts of the system along several dimensions:

- **Introspective layer**
  Summaries of emerging and stable patterns — such as counts of interactions about specific topics, or the presence of repeated themes in `ms_jarvis_memory` — can be folded into introspective reports and verification scripts. ★ BBB filtering decision histories now stored in `jarvis-memory:8056` (secured March 28) provide a new introspective data source: the system can now report not only what was retained but what was blocked and why, across all 96 Up containers.

- **Consolidation and memory layers**
  Promotion decisions from the background store trigger updates to:
  - Identity specifications and narrative documents that describe Ms. Jarvis's role, commitments, and constraints.
  - Additional vector collections in ChromaDB ★ (now 40 collections, 6,675,442 vectors), where elevated documents may be replicated with higher priority or enriched metadata.
  - Belief structures in GBIM (`msjarvis:5433` ★, 5,416,521 entities with `confidence_decay` metadata) and relational schemas in `msjarvisgis:5432` ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids), particularly where background patterns intersect with spatial or institutional knowledge.

- **Global control and policy**
  Observed patterns in the background store can inform adjustments to global settings, such as:
  - Emphasis on particular topics, roles, or regions in subsequent retrieval and routing decisions. ★ AAPCAppE corpus patterns (65 documents, 39 sources, `msjarvis_docs` 4,192 items) now provide a community-resource signal that can inform routing emphasis toward regional services.
  - Adjustments to safety filters when certain content categories repeatedly trigger ethics concerns or when new safe patterns are observed. ★ `jarvis-memory:8056` secured audit trail provides the durable filter-decision history needed to make these adjustments on solid empirical ground.
  - Reallocation of system resources toward heavily used domains or under-served communities identified through aggregate statistics over background entries.

Through these links, what accumulates in `ms_jarvis_memory` can progressively shape both localized decisions and overall system behavior, while remaining auditable via curator tools and the secured `jarvis-memory:8056` audit store.

---

## 21.9 Summary

The background store provides a place where items that have passed initial screening can accumulate, interact, and be revisited over time. In the current implementation, this function is concretely supported by the ChromaDB collection `ms_jarvis_memory` (UUID: `79240788-0828-45f3-b1bc-a9a3593628a6`, confirmed in ★ **40-collection** inventory March 28, 2026 — see Ch. 22 §22.10 for UUID preservation warning), populated by main-brain background tasks for every user interaction, ★ and now also supplemented by the AAPCAppE external-source ingest pipeline (65 documents, 39 sources, `msjarvis_docs` 4,192 items, March 27–28). Curator review is available via both internal Python tooling and a curator-facing HTTP endpoint. As of March 21, 2026 baseline, the autonomous learner has accumulated 21,181 records in this collection, growing ≈288/day ★ + AAPCAppE external-source stream. The I-Container mechanism, present in code and verification scripts, offers a designed but not yet fully operational complement for more curated internal knowledge.

★ The March 28, 2026 ChromaDB full audit (40 active collections, 6,675,442 total vectors) is the most comprehensive review of background store quality performed to date. It established: `spiritual_rag` deduplication (−19,338 vectors), `psychological_rag` restoration (968 docs), and `msjarvis_docs` expansion (4,192 items) as concrete audit-triggered maintenance actions — confirming that collection-level quality drift is detectable and remediable at the current scale. ★ BBB audit trail events for all filtering decisions now persist durably to `jarvis-memory:8056` (corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set, March 28), providing a secured, authenticated source for introspective analysis of background store gating behavior.

By structuring items with identifiers, metadata, embeddings, and implicit status, and by enabling periodic review, pattern detection, and human-guided promotion decisions, the background store allows the system to move beyond one-off responses toward recognition of stable, evaluable patterns. The March 25, 2026 confirmation of emergent cross-session context passing via the consciousness bridge `_get_url` read path (OI-05 — see Ch. 22 §22.9) indicates that `ms_jarvis_memory` is already contributing to session continuity beyond its original design scope. Subsequent chapters build on this foundation to describe how the most selective layer is defined and how the two parallel paths differ in what they ultimately elevate into central, identity-level storage anchored in PostgreSQL `msjarvis:5433` ★ (5,416,521 GBIM entities) and `msjarvisgis:5432` ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids).

---

*Last updated: 2026-03-28 by Carrie Kidd (Mamma Kidd), Mount Hope WV*

*March 25, 2026: `ms_jarvis_memory` UUID confirmed (§22.10); OI-05 emergent context cross-reference added (§21.4, §21.9); 31-collection ChromaDB inventory noted.*

*★ March 28, 2026: 96/96 containers Up — zero Restarting, zero Exited. ChromaDB full audit (40 collections, 6,675,442 total vectors) — replaces 31-collection reference throughout (§21.1, §21.2, §21.4, §21.7, §21.8, §21.9). `spiritual_rag` deduplicated (−19,338 vectors) — §21.1, §21.4, §21.5, §21.6, §21.7, §21.9. `psychological_rag` restored (968 docs) — §21.7, §21.9. `msjarvis_docs` expanded (4,192 items) — §21.1, §21.2, §21.3, §21.5, §21.7, §21.8, §21.9. AAPCAppE ingest pipeline operational — §21.1, §21.2, §21.3, §21.5, §21.7, §21.8, §21.9. `msjarvis` port 5433 restored (5,416,521 GBIM entities with `confidence_decay` metadata) — §21.2, §21.6, §21.7, §21.8, §21.9. `msjarvisgis` port 5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids) — §21.2, §21.6, §21.7, §21.8, §21.9. `jarvis-memory` port 8056 corrected `0.0.0.0` → `127.0.0.1`; `_auth()` confirmed; `JARVIS_API_KEY` set — §21.1, §21.3, §21.4, §21.8, §21.9. `all-minilm:latest` 384-dim embedding constraint documented — §21.2. UUID `79240788-0828-45f3-b1bc-a9a3593628a6` confirmed in 40-collection inventory — §21.1, §21.6, §21.9.*
