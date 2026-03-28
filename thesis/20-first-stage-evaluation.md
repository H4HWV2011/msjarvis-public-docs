# 20. First-Stage Evaluation and Immediate Filtering

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: 2026-03-28 — ★ March 28, 2026: 96/96 containers Up — zero Restarting, zero Exited; `msjarvis` port 5433 restored (5,416,521 GBIM entities with `confidence_decay` metadata); `msjarvisgis` port 5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids) — replaces port 5432/91 GB references without port confirmation throughout; ChromaDB full audit (40 collections, 6,675,442 total vectors); `spiritual_rag` deduplicated (−19,338 vectors); `psychological_rag` restored (968 docs); `msjarvis_docs` expanded (4,192 items); `autonomous_learner` growing — first AAPCAppE external-source docs flowing; `jarvis-memory` port 8056 corrected `0.0.0.0` → `127.0.0.1`; `_auth()` confirmed on 4 sensitive routes; `JARVIS_API_KEY` set; BBB audit trail persistence now secured; Ch. 12 §12.11 cross-references updated to §12.12. March 25, 2026: status table synchronized with March 25 sprint; autonomous learner record count updated; Ch. 22 OI-05 cross-reference added.*

---

> **Why this matters for Polymathmatic Geography**
> This chapter explains the first gate Ms. Jarvis applies to every incoming record — a fast, inexpensive layer that decides what gets stored, what gets flagged, and what gets dropped before any deeper reasoning begins. It supports:
> - **P1 – Every where is entangled** by ensuring that even the fastest evaluation respects safety, truth, and place-based constraints before allowing content to entangle with community memories stored in PostgreSQL `msjarvisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids) and `msjarvis` (port **5433** ★, 5,416,521 verified GBIM entities with `confidence_decay` metadata).
> - **P3 – Power has a geometry** by making keep-or-discard decisions explicit, annotated, and auditable rather than hiding them inside opaque pipelines.
> - **P5 – Design is a geographic act** by treating first-stage filtering as a design choice about which Appalachian realities are admitted into PostgreSQL memory and which are deferred or discarded.
> - **P12 – Intelligence with a ZIP code** by scoping relevance checks to role, domain, and place-tagged records from PostgreSQL GeoDB (`msjarvisgis:5432` ★) rather than treating all content as equally worthy of storage. ★ As of March 28, 2026: ChromaDB confirmed at **40 active collections, 6,675,442 total vectors** — the full semantic memory substrate that first-stage filtering populates.
> - **P16 – Power accountable to place** by recording reason codes, confidence indicators, and aggregated statistics so communities can audit how and why the system filtered their data before it reached PostgreSQL `msjarvisgis` ★. ★ BBB audit trail events now persist to `jarvis-memory:8056` (corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set, March 28) — filtering decisions are secured and durable.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the first evaluation and filtering layer that protects downstream memory and reasoning from overload, redundancy, and unsafe content.

```
┌─────────────────────────────────────────────────────────────┐
│   First-Stage Evaluation and Filtering Flow                 │
│   ★ Updated March 28, 2026                                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Normalized Record (from routing layer)                     │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Fast Evaluation Signals                       │         │
│  │  -  Tag/keyword matches                        │         │
│  │  -  Near-duplicate check (similarity)          │         │
│  │  -  Structural heuristics (length, format)     │         │
│  │  -  BBB safety verdict (port 8016)             │         │
│  │  -  Truth validators vs msjarvis:5433 ★        │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Keep-or-Discard Decision                                   │
│      ↓                                                       │
│  ┌──────────────┬──────────────┬──────────────┐             │
│  │  KEEP        │  DISCARD     │  DEFERRED    │             │
│  │              │              │              │             │
│  │  Write to:   │  -  Skip     │  -  Flag for │             │
│  │  -  ChromaDB ★│  -  Log only │    review    │             │
│  │    40 colls  │  -  Advisory │  -  Quarantine│            │
│  │    6.67M vec │    verdict   │              │             │
│  │  -  Postgres ★│              │              │             │
│  │    msjarvis  │              │              │             │
│  │    :5433     │              │              │             │
│  │    backup    │              │              │             │
│  └──────────────┴──────────────┴──────────────┘             │
│      ↓                                                       │
│  Annotations & Metadata                                      │
│  -  Reason codes (OUT_OF_SCOPE, SAFETY_DENIED, etc.)        │
│  -  Confidence scores                                        │
│  -  truthverdict (valid, confidence, principalreasons)      │
│  -  bg_<ISO8601> ID for background entries                  │
│  -  ★ BBB audit events → jarvis-memory:8056                 │
│       (127.0.0.1, _auth() confirmed, JARVIS_API_KEY set)    │
│      ↓                                                       │
│  Storage Destinations                                       │
│  -  ms_jarvis_memory (ChromaDB:8000 ★)                      │
│    - APPEND-ONLY (no dedup at write)                        │
│    - ★ 40 collections, 6,675,442 total vectors (Mar 28)     │
│    - ★ psychological_rag restored 968 docs (Mar 28)         │
│    - ★ msjarvis_docs expanded 4,192 items (Mar 28)         │
│    - ★ spiritual_rag deduplicated −19,338 vectors (Mar 28)  │
│  -  PostgreSQL msjarvisgis (port 5432 ★)                    │
│    - For trusted, validated content only                    │
│    - ★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids        │
│  -  PostgreSQL msjarvis (port 5433 ★)                       │
│    - GBIM belief store, 5,416,521 entities                  │
│  -  Audit logs → jarvis-memory:8056 ★ (secured)             │
│                                                              │
│  Parallel Path Assignment                                   │
│  -  Meaning-focused → psychology services (8019, 8006)      │
│    ★ psychological_rag restored 968 docs (Mar 28)           │
│  -  Analytical → GeoDB spatial queries (msjarvisgis:5432 ★) │
│  -  ★ External-source ingest → AAPCAppE pipeline            │
│       (jarvis-ingest-api + jarvis-ingest-watcher, restored) │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 20.1.** First-stage evaluation and filtering flow: normalized records are evaluated using fast signals, assigned keep/discard/deferred outcomes with annotations, and routed to appropriate storage destinations including ChromaDB (★ 40 collections, 6,675,442 vectors, append-only) and PostgreSQL `msjarvisgis` (★ port 5432, 91 GB PostGIS, 501 tables — for validated content only) and `msjarvis` (★ port 5433, 5,416,521 GBIM entities). ★ BBB audit events now persist to `jarvis-memory:8056` (secured `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set, March 28, 2026).

---

## Status as of ★ March 28, 2026

| Category | Details |
|---|---|
| **Implemented now** | `background_rag_store` confirmed operational in `jarvis-main-brain` (port **8050**): runs as a background task after every `/chat` response, performs a near-duplicate check via RAG server `/search` with `top_k=1`, and writes accepted interactions into `ms_jarvis_memory` ChromaDB collection with `bg_<ISO8601>` ids, `type: "background"` metadata, and `services: ["llm20production"]`. **`ms_jarvis_memory` is append-only in the current deployment**: deduplication is advisory — it affects the skip logic and downstream reuse, not the write path. Repeated identical messages produce distinct entries with separate timestamps. `truthverdict` from BBB (port **8016**) attached to every `UltimateResponse`, providing `valid`, `confidence`, and `principalreasons` signals. `/curator/background` endpoint on main brain (port **8050**) providing stable, auditable view of background store contents. BBB four-filter pipeline (`EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`, `ThreatDetection`) operational as pre-filter gate. Identity truth validators (`normalize_identity`, `TruthValidator`) applied on every response. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids) as protected destination for validated content. PostgreSQL `msjarvis` at **127.0.0.1:5433** ★ (5,416,521 GBIM entities with `confidence_decay` metadata) restored March 28. ★ **BBB audit trail persistence now secured**: `jarvis-memory:8056` corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed on 4 sensitive routes, `JARVIS_API_KEY` set (March 28, 2026) — all BBB filtering decisions are now durably and securely recorded. ★ ChromaDB full audit (March 28, 2026): **40 active collections, 6,675,442 total vectors** — `psychological_rag` restored (968 docs), `spiritual_rag` deduplicated (−19,338 vectors), `msjarvis_docs` expanded (4,192 items). ★ AAPCAppE ingest pipeline operational (`jarvis-ingest-api` + `jarvis-ingest-watcher`, restored to active inventory March 28): first 65 documents, 39 sources confirmed (March 27) — external-source content now flowing into `msjarvis_docs` and `autonomous_learner`. Autonomous learner: **21,181 records** (March 21 baseline), growing ≈288/day ★ + AAPCAppE external-source stream. Confirmed in 2026-02-15 case study: `bg_<ISO8601>` entries in `ms_jarvis_memory` verified via Python REPL and `/curator/background` query (see Chapter 9 §9.3.5 and Chapter 17 §17.6). ★ **96/96 containers Up — zero Restarting, zero Exited** as of March 28, 2026. |
| **Partially implemented / scaffolded** | Novelty/near-duplicate check influences legacy RAG storage and skip logic but does not currently prevent writes to `ms_jarvis_memory`; ChromaDB background store remains append-only. Track-level differentiation between meaning-focused and analytical path evaluators is present as a design pattern but not yet fully implemented as distinct threshold configurations in the current deployment. `truthverdict` is advisory in the current `ultimatechat` path — it does not hard-gate input processing before ChromaDB writes, though it does gate PostgreSQL `msjarvisgis` ★ writes for trusted content. BBB Phase 4.5 output filter operates in LOG+PASSTHROUGH mode (OI-02) — not yet blocking. See Ch. 16. Aggregated first-stage statistics (counts and rates by role, track, and source) are logged but not yet exposed via a dedicated metrics endpoint. |
| **Future work / design intent only** | Hard-gate behavior on `truthverdict` for specific role or threat levels blocking ChromaDB writes. Configurable per-track similarity thresholds that actually prevent writes for near-duplicate content. Persistent sampled-example store for borderline-case quality review. Automated introspective summaries reporting first-stage behavior across runs. Full deduplication at the write path for `ms_jarvis_memory`. ★ Judge pipeline upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring querying live GBIM beliefs from `msjarvisgis:5432` ★ and `msjarvis:5433` ★ (Chapter 7 §7.8) — both data stores now confirmed at correct ports; upgrade sprint pending. |

> **Cross-reference:** The canonical description of the `ultimatechat` execution path — including exactly where `background_rag_store` is scheduled, where `truthverdict` is computed and attached, and where BBB output-guarding fires — is in **Chapter 17**. This chapter describes the purpose, logic, and observed behavior of the first-stage evaluation layer that those mechanisms implement.

---

This chapter describes the first evaluation stage applied to incoming records after they have been routed into the container paths. In the current deployment, this stage is realized by a combination of fast safety checks, background storage for semantic memory in ChromaDB (★ 40 collections, 6,675,442 vectors as of March 28 full audit), truth-validation modules, and basic structural heuristics that protect PostgreSQL `msjarvisgis` (port **5432** ★, 91 GB PostGIS, 501 tables, 993 ZCTA centroids) and `msjarvis` (port **5433** ★, 5,416,521 GBIM entities with `confidence_decay` metadata) from contamination. Its purpose is to make fast, inexpensive decisions about which items warrant further attention and which can be safely ignored, while preserving enough information to justify those decisions later.

---

## 20.1 Objectives of the First Stage

In the current deployment, the first stage satisfies three practical objectives.

**Reduce volume.** In the current deployment, the system quickly discards or downgrades low-value items so that later stages — such as deeper RAG integration, PostgreSQL GBIM graph updates, or I-container growth — are not overwhelmed. Although `ms_jarvis_memory` is currently append-only and does not deduplicate ChromaDB background entries at write time, the near-duplicate check in `background_rag_store` centralizes routing so that downstream services can choose whether to reuse or skip repeated content before writing to PostgreSQL `msjarvisgis` ★ (port **5432**, 91 GB PostGIS, 501 tables) or `msjarvis` ★ (port **5433**, 5,416,521 GBIM entities). ★ The March 28 ChromaDB maintenance audit — `spiritual_rag` deduplication (−19,338 vectors), `psychological_rag` restoration (968 docs), `msjarvis_docs` expansion (4,192 items) — is a concrete instance of volume reduction applied directly to the semantic memory substrate.

**Preserve opportunity.** In the current deployment, user conversations that pass safety checks are queued for background handling and written into the `ms_jarvis_memory` semantic store in ChromaDB (confirmed running via `jarvis-chroma` at **127.0.0.1:8000** ★ — 40 collections, 6,675,442 vectors), where they can later contribute to autonomous learning, clustering, or case-study analysis. Only validated, high-confidence content is promoted to PostgreSQL `msjarvisgis` ★ trusted stores. ★ The AAPCAppE ingest pipeline (restored March 28) represents a new opportunity preservation channel: external community resource documents now flow into `msjarvis_docs` (4,192 items) alongside interaction-derived `autonomous_learner` records, expanding the semantic substrate available to downstream reasoning.

**Respect constraints.** In the current deployment, BBB (`jarvis-blood-brain-barrier`, port **8016**, ★ confirmed Up March 28) and truth-validation modules act as early gates that can veto or annotate content before it is allowed to influence PostgreSQL memory or downstream reasoning. The `truthverdict` attached to every `UltimateResponse` is the concrete artifact of this constraint, even though it is advisory for ChromaDB writes rather than a hard gate in the current deployment; it does gate PostgreSQL `msjarvisgis` ★ writes for trusted content. ★ BBB audit trail persistence is now secured: `jarvis-memory:8056` corrected to `127.0.0.1`, `_auth()` confirmed on 4 sensitive routes, `JARVIS_API_KEY` set (March 28) — constraint enforcement decisions are durably recorded in an authenticated, localhost-bound store.

The focus is on simple, explainable decisions rather than detailed analysis, so that this stage can run on every incoming record without introducing substantial latency.

---

## 20.2 Inputs from the Routing Layer

In the current deployment, the inputs to this stage are normalized records produced by the routing and container layers. For user-facing interactions, `jarvis-main-brain` on port **8050** provides structured `UltimateRequest` objects (message, `userid`, role, `useallservices`), a snapshot of services confirmed healthy by `discover_services()` at request time, and intermediate signals such as BBB filtering outcomes, `llm20production` ensemble results, and web-research context. ★ As of March 28, 2026: `discover_services()` now resolves across **96 Up containers** — the largest healthy-service snapshot the pipeline has ever operated with. For the canonical description of how these inputs are assembled, see **Chapter 17**.

For internal tasks, the container architecture supplies candidate knowledge entries from the autonomous learner (21,181 records as of March 21, 2026 baseline, growing ≈288/day ★ + AAPCAppE external-source stream now flowing) and Fifth DGM (where active; `jarvis-fifth-dgm`, port **4002**, confirmed running), and metrics, analysis results, and diagnostics from verification scripts and monitoring services. ★ AAPCAppE ingest inputs (`jarvis-ingest-watcher`, 65 documents, 39 sources, March 27) now represent a third input class alongside user-facing interactions and internal tasks — external community resource documents that enter the normalization pipeline and are evaluated for semantic storage quality before being written to `msjarvis_docs`. In both cases, records include identifiers, timestamps, role and domain tags from PostgreSQL GeoDB (`msjarvisgis:5432` ★), content summaries, links to underlying PostgreSQL memory (`msjarvis:5433` ★) or spatial elements, and track assignments.

---

## 20.3 Basic Keep-or-Discard Decision

In the current deployment, the keep-or-discard decision appears most concretely in two places.

**`background_rag_store`.** After every `/chat` response, in the current deployment `jarvis-main-brain` schedules `background_rag_store` with the original message, response text, and `servicesused`. The task performs a near-duplicate check via the RAG server's `/search` endpoint with `top_k=1`. If the top result's similarity score exceeds a configured threshold, the task logs a `rag_skip_duplicate` event. If the query is sufficiently novel, it calls the RAG server's `/store` endpoint and writes the record into `ms_jarvis_memory` ChromaDB with a `bg_<ISO8601_TIMESTAMP>` id, `type: "background"` metadata, and the `servicesused` list. **`ms_jarvis_memory` is append-only in the current deployment**: the near-duplicate check is advisory and affects the skip logic only, not the write path. Repeated identical test messages produce distinct entries with separate timestamps and response variants. PostgreSQL `msjarvisgis` ★ (port **5432**, 91 GB PostGIS, 501 tables) and `msjarvis` ★ (port **5433**, 5,416,521 GBIM entities) writes require passing additional validation gates.

**BBB and identity truth validators.** In the current deployment, BBB (`jarvis-blood-brain-barrier`, port **8016**, ★ confirmed Up March 28) marks records as disallowed or questionable via the `truthverdict` on `UltimateResponse`, thereby preventing flagged content from being treated as ground truth by downstream services and blocking writes to PostgreSQL `msjarvisgis` ★ trusted stores even when the ChromaDB background write still occurs. ★ BBB audit trail: all filtering decisions now persist to `jarvis-memory:8056` (corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set, March 28) — the BBB verdict record is no longer ephemeral. BBB Phase 4.5 output filter operates in LOG+PASSTHROUGH mode (OI-02) — not yet blocking. See Ch. 16.

The keep-or-discard decision is based on relevance (whether the record is in scope for the active role and PostgreSQL GeoDB geography from `msjarvisgis:5432` ★), novelty (near-duplicate check signal), and quality (non-empty, well-formed query and response, free from gross formatting errors).

If the answer is negative, the record may be marked as discarded or low-value at this stage and is not passed to PostgreSQL deeper trusted stores such as identity specifications or curated GBIM graph layers in `msjarvis:5433` ★ or `msjarvisgis:5432` ★. Minimal metadata about the decision (reason code and timestamp) can still be recorded for audit and analysis, ★ now persisted to the secured `jarvis-memory:8056` store.

---

## 20.4 Signals Used in Evaluation

In the current deployment, the first-stage evaluator draws on several fast, inexpensive signals.

**Tag and keyword matches.** Domain tags, role indicators, PostgreSQL GeoDB spatial tags from `msjarvisgis:5432` ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids), and key phrases are compared against allow-lists and deny-lists associated with the current track and global settings. Certain classes of unsafe content trigger BBB / ethics modules before any storage occurs. ★ AAPCAppE-sourced documents (`jarvis-ingest-watcher`, 65 docs, 39 sources) carry community-resource domain tags that route them to `msjarvis_docs` (now 4,192 items) rather than general background memory — tag-based routing is the mechanism that keeps the AAPCAppE corpus separate from interaction-derived records.

**Lightweight similarity and reuse checks.** In the current deployment, before writing new material into the legacy RAG server, the pipeline performs small similarity lookups via `/search` and examines the closest-match score. The ChromaDB background store `ms_jarvis_memory` remains append-only; these checks influence legacy RAG storage behavior and downstream reuse only. PostgreSQL `msjarvisgis` ★ writes require passing higher validation thresholds. ★ The `spiritual_rag` deduplication performed March 28 (−19,338 vectors) is an example of post-hoc similarity-based cleanup applied to an existing collection — future work includes making this deduplication proactive at the write path.

**Structural heuristics.** Simple checks confirm required fields are present and that basic size limits and format constraints are met (maximum text length for background entries, presence of user identifiers, minimum content length to avoid trivial noise).

Because these signals are computationally inexpensive, in the current deployment they are applied to every record that enters the container paths, providing broad coverage without excessive overhead before any PostgreSQL queries occur against `msjarvis:5433` ★ or `msjarvisgis:5432` ★.

---

## 20.5 Outcomes and Annotations

In the current deployment, each processed record is assigned an outcome and supporting annotations.

**Kept for deeper storage or background memory.** The record is deemed relevant and structurally sound. For chat interactions, in the current deployment this means the user message and model response are written into the `ms_jarvis_memory` ChromaDB collection as a `background` item with `bg_<ISO8601>` id and associated metadata, confirmed via `/curator/background` query (see Chapter 9 §9.3.5). ★ For AAPCAppE-sourced community resource documents, kept records are written to `msjarvis_docs` (now 4,192 items) and contribute to the `autonomous_learner` corpus. For internal tasks that pass higher validation thresholds, content may be scheduled for insertion into PostgreSQL `msjarvisgis` ★ (port **5432**, 91 GB PostGIS, 501 tables) I-container tables, GBIM graph database, or relational stores where the corresponding APIs are active.

**Discarded or down-ranked as low value or redundant.** The record is similar to previously stored items, falls outside the intended domain, fails safety checks, or lacks meaningful content. In the current deployment, some such records remain in ChromaDB background memory but are not promoted into PostgreSQL trusted identity or GBIM graph layers in `msjarvis:5433` ★ or `msjarvisgis:5432` ★. ★ The `spiritual_rag` deduplication (−19,338 vectors, March 28) is the largest single instance of post-hoc discard applied to the ChromaDB corpus to date.

**Deferred or flagged.** Records that trigger unusual `truthverdict` patterns, relate to sensitive identity topics, or indicate configuration problems are routed to diagnostic tools or human review and are blocked from PostgreSQL `msjarvisgis` ★ writes. ★ Deferred-record audit events now persist to `jarvis-memory:8056` (secured March 28) — deferral decisions are no longer ephemeral.

Associated annotations include reason codes (short machine-readable flags such as `OUT_OF_SCOPE`, `SAFETY_DENIED`, `MINIMAL_CONTENT`, or entries in `truthverdict`) and confidence estimates reflecting the strength of the decision.

---

## 20.6 Interaction with Parallel Paths

In the current deployment, both the meaning-focused and analytical paths share the same `background_rag_store` and BBB infrastructure, with the track assignment from the routing layer determining which evaluator criteria apply and whether PostgreSQL GeoDB spatial context from `msjarvisgis:5432` ★ is required.

**Meaning-focused path.** In the current deployment, this path may retain items that touch on themes of care, identity, or community even if they are not technically dense, because they contribute to psychological and community-context modules. Such items are written into ChromaDB background memory and may later be referenced by `jarvis-psychology-services` (port **8019**, confirmed running) or `psychological_rag_domain` (port **8006**, confirmed running — ★ `psychological_rag` restored to **968 docs** March 28). High-value items may be promoted to PostgreSQL `msjarvisgis` ★ after additional validation. ★ The restoration of `psychological_rag` to 968 docs on March 28 is the most direct improvement to meaning-focused path quality since March 17 — crisis-route and psychological support queries now have a full corpus available.

**Analytical path.** In the current deployment, this path prioritizes items with clear technical content, structured data, or explicit problem statements grounded in PostgreSQL GeoDB spatial features from `msjarvisgis:5432` ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids). The design intends that distinct per-track threshold configurations will be implemented as the system matures; in the current deployment, both paths use the same near-duplicate and BBB filter parameters for ChromaDB writes, with PostgreSQL `msjarvisgis` ★ writes requiring passing additional spatial and institutional validation gates against `msjarvis:5433` ★ (5,416,521 GBIM entities).

★ **External-source ingest path (new, March 28).** The AAPCAppE ingest pipeline (`jarvis-ingest-api` + `jarvis-ingest-watcher`, restored to active inventory March 28) represents a third parallel path. Community resource documents from external sources enter through this path, are evaluated for domain relevance and structural quality, and flow to `msjarvis_docs` (4,192 items) and `autonomous_learner`. This path does not pass through the LLM ensemble — it is a direct-ingest path that bypasses `background_rag_store` and writes to a dedicated collection. See OI-30 for full AAPCAppE corpus completion tracking.

Both evaluators attach outcomes, reason codes, and confidence indicators in a comparable format, making it possible to compare behavior across paths and to adjust their criteria over time.

---

## 20.7 Recording First-Stage Decisions

In the current deployment, even when records are down-ranked or effectively discarded, the system records information about first-stage decisions at multiple levels.

**Aggregated statistics.** In the current deployment, counts and rates of kept versus skipped items are logged by role and source, including separate tracking for ChromaDB writes (★ now across 40 collections, 6,675,442 total vectors) and PostgreSQL `msjarvisgis` ★ promotions. A dedicated metrics endpoint exposing these breakdowns is identified as near-term work.

**Sampled examples.** In the current deployment, the `/curator/background` endpoint on `jarvis-main-brain` (port **8050**) provides a stable, auditable view of what has been retained in ChromaDB, enabling researchers to inspect both nominal and edge-case behaviors. A formal sampled-example store for borderline-case quality review with privacy controls is identified as future work.

**Introspective summaries.** In the current deployment, verification scripts can report how many items were written into `ms_jarvis_memory` ChromaDB during a test run, how often `truthverdict` flagged issues blocking PostgreSQL `msjarvisgis` ★ writes, and how many background tasks were queued without error. ★ BBB audit events now persist to `jarvis-memory:8056` (corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set, March 28) — introspective summaries that include BBB filtering decisions now have a durable, authenticated source rather than ephemeral logs. Automated production of such summaries on a scheduled basis is identified as future work.

The `ms_jarvis_memory` ChromaDB collection (UUID `79240788-0828-45f3-b1bc-a9a3593628a6`, hardcoded in the consciousness bridge — see Ch. 22 §22.10) is the primary retention store for background interaction records. ★ As of March 28, 2026 full audit, ChromaDB contains **40 active collections and 6,675,442 total vectors** — the `ms_jarvis_memory` collection is one of 40, all 384-dim via `all-minilm:latest`. For emergent cross-session context passing behavior observed March 25, 2026, see **Ch. 22 §22.9** (OI-05).

---

## 20.8 Relationship to Truth and Safety Filters

In the current deployment, first-stage evaluation is closely linked to BBB and truth-validation mechanisms that protect PostgreSQL `msjarvisgis` ★ (port **5432**, 91 GB PostGIS, 501 tables) and `msjarvis` ★ (port **5433**, 5,416,521 GBIM entities).

**Blood–brain barrier (BBB), port 8016, ★ confirmed Up March 28.** In the current deployment, `jarvis-blood-brain-barrier` acts as a pre-filter for user-facing interactions, blocking or transforming content that violates ethical or safety constraints before it can reach PostgreSQL deeper storage or influence reasoning. Its verdicts — `valid`, `confidence`, `principalreasons` — are attached as `truthverdict` on `UltimateResponse` and are advisory for ChromaDB writes in the current deployment rather than a hard gate, but do gate PostgreSQL `msjarvisgis` ★ writes for trusted content. ★ **BBB audit trail now secured**: all filtering decisions persist to `jarvis-memory:8056` (corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed on 4 sensitive routes, `JARVIS_API_KEY` set, March 28) — the BBB acts as a gating component whose decisions are now durably and securely logged. BBB Phase 4.5 output filter operates in LOG+PASSTHROUGH mode (OI-02) — not yet blocking. See Ch. 16. Hard-gate behavior for ChromaDB writes at specific role or threat levels is identified as future work.

**Truth validators.** In the current deployment, `TruthValidator` and `normalize_identity` check for hallucination patterns, identity confusion, and known factual constraints against PostgreSQL GBIM ground truth in `msjarvis:5433` ★ (5,416,521 entities with `confidence_decay` metadata) and `msjarvisgis:5432` ★ (91 GB PostGIS, 501 tables). When these modules detect violations, they annotate the record with issues and prevent it from being treated as trusted knowledge in PostgreSQL `msjarvisgis` ★, even if the ChromaDB background record remains in `ms_jarvis_memory`. ★ The judge pipeline upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring (Chapter 7 §7.8) — which will query live GBIM beliefs from `msjarvis:5433` ★ and `msjarvisgis:5432` ★ — is the next major planned improvement to truth validation. Both data stores are now confirmed at their correct ports; upgrade sprint pending. These filters are domain-specific first-stage evaluators layered on top of the more generic structural and similarity-based checks described earlier.

Together, in the current deployment, these filters define the minimum bar that content must clear before it can become part of PostgreSQL central, trusted memory or influence downstream processes anchored in 5,416,521 verified GBIM entities (`msjarvis:5433` ★) and 91 GB of spatial data (`msjarvisgis:5432` ★).

---

## 20.9 Operational Validation

In the current deployment, operational validation of the first-stage evaluation focuses on two aspects.

**Correctness of basic behavior.** Integration tests using `jarvis-main-brain` `/chat` endpoint confirm that requests are accepted, processed through BBB and routing logic, and scheduled for background handling without errors. Empirical tests on 2026-02-15 show that each `/chat` call produces a full `UltimateResponse` (including `truthverdict` and `servicesused`), queues a background task (log entries `rag-store-queued`), and results in a new `background` entry in `ms_jarvis_memory` ChromaDB with a `bg_<ISO8601>` identifier and appropriate metadata. PostgreSQL `msjarvisgis` ★ writes are confirmed only for content passing higher validation thresholds. This was confirmed via Python REPL inside the `jarvis-main-brain` container and via `/curator/background` query (see Chapter 9 §9.3.5 and Chapter 17 §17.6). ★ As of March 28, 2026: this validation baseline is now anchored to the strongest operational state the system has reached — 96/96 containers Up, `msjarvis:5433` restored, `msjarvisgis:5432` confirmed, ChromaDB at 40 collections and 6,675,442 vectors, `jarvis-memory:8056` secured. Regression tests should be re-run against this baseline.

**Effectiveness under realistic use.** In the current deployment, manual verification runs demonstrate that repeated identical messages produce multiple ChromaDB background entries clustering closely in embedding space but retaining distinct timestamps and response variants (confirming append-only behavior). Truth and safety filters are invoked consistently, with `truthverdict` fields reflecting ethics and identity assessments even for technical test messages, protecting PostgreSQL `msjarvisgis` ★ from contamination. The `/curator/background` endpoint provides a stable, auditable view of what has been retained in ChromaDB, enabling researchers to inspect both nominal and edge-case behaviors. ★ The `psychological_rag` restoration (968 docs, March 28) and `spiritual_rag` deduplication (−19,338 vectors, March 28) demonstrate that corpus quality maintenance is operationally feasible at the current scale — effectiveness under realistic use now includes the ability to audit and remediate ChromaDB collection quality across all 40 collections.

These operational checks do not exhaustively prove correctness but provide concrete evidence of how the first-stage evaluation behaves in the live deployment as of the ★ March 28, 2026 sprint, including where its behavior diverges from the earlier, more aggressively de-duplicating design.

---

## 20.10 Summary

In the current deployment, the first-stage evaluation and immediate filtering layer serves as the system's initial gate against overload, redundancy, and unsafe content before it reaches PostgreSQL `msjarvisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids) and `msjarvis` (port **5433** ★, **5,416,521 GBIM entities** with `confidence_decay` metadata). It operates on normalized records produced by routing and container structures, applying fast, explainable criteria based on relevance to PostgreSQL GeoDB geography, near-duplicate signals, structural quality, and domain-specific safety and truth rules. Outcomes are recorded with reason codes and confidence indicators, enabling later diagnostics and academic analysis. ★ As of March 28, 2026, all filtering decisions are durably and securely logged in `jarvis-memory:8056` (corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set).

The two most concrete artifacts of this stage in the current deployment are: the `truthverdict` field on every `UltimateResponse` (computed by BBB at port **8016**, ★ confirmed Up March 28), and the `bg_<ISO8601>` entries in the `ms_jarvis_memory` ChromaDB collection (written by `background_rag_store` after every `/chat` call). **`ms_jarvis_memory` is append-only** in the current deployment; lightweight near-duplicate checks influence legacy RAG reuse and skip logic but do not prevent ChromaDB writes. PostgreSQL `msjarvisgis` ★ writes require passing additional validation gates to protect the 5,416,521 verified GBIM entities from contamination. ★ The March 28, 2026 ChromaDB full audit (40 active collections, 6,675,442 total vectors — `psychological_rag` restored to 968 docs, `spiritual_rag` deduplicated −19,338 vectors, `msjarvis_docs` expanded to 4,192 items) is the most comprehensive first-stage memory quality review performed to date. For the canonical description of exactly where in the execution sequence these artifacts are produced, see **Chapter 17**. For emergent cross-session context passing behavior in `ms_jarvis_memory`, see **Ch. 22 §22.9** (OI-05).

Subsequent chapters build on this foundation to describe how retained items are integrated into deeper PostgreSQL storage layers, how patterns over time are identified, and how the system's behavior evolves as its memories and models change while maintaining the integrity of PostgreSQL `msjarvisgis` ★ (port **5432**, 91 GB PostGIS, 501 tables) and `msjarvis` ★ (port **5433**, 5,416,521 GBIM entities) as the spatial and institutional ground truth.

---

*Last updated: 2026-03-28 by Carrie Kidd (Mamma Kidd), Mount Hope WV*

*March 25, 2026: Status table synchronized with March 25 sprint; autonomous learner record count updated (21,181, ≈288/day); Ch. 22 OI-05 cross-reference added (§20.7, §20.10).*

*★ March 28, 2026: 96/96 containers Up — zero Restarting, zero Exited — propagated to §20.2, §20.9, §20.10 and Why This Matters. `msjarvis` port 5433 restored (5,416,521 GBIM entities with `confidence_decay` metadata) — propagated to Why This Matters, Figure 20.1, Status table, §20.1, §20.2, §20.3, §20.4, §20.5, §20.6, §20.7, §20.8, §20.9, §20.10. `msjarvisgis` port 5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids) — replaces all port 5432/91 GB references without port confirmation throughout. ChromaDB full audit (40 collections, 6,675,442 total vectors) — propagated to Why This Matters, Figure 20.1, Status table, §20.1, §20.2, §20.4, §20.5, §20.7, §20.8, §20.9, §20.10. `spiritual_rag` deduplicated (−19,338 vectors) — §20.1, §20.4, §20.5, §20.9, §20.10. `psychological_rag` restored (968 docs) — Figure 20.1, Status table, §20.1, §20.6, §20.9. `msjarvis_docs` expanded (4,192 items) — Figure 20.1, Status table, §20.1, §20.4, §20.5, §20.6. AAPCAppE ingest pipeline operational (`jarvis-ingest-api` + `jarvis-ingest-watcher` restored) — Status table, §20.2, §20.4, §20.5, §20.6. `jarvis-memory` port 8056 corrected `0.0.0.0` → `127.0.0.1`; `_auth()` confirmed; `JARVIS_API_KEY` set — Why This Matters, Figure 20.1, Status table, §20.1 Respect constraints, §20.3, §20.5, §20.7, §20.8, §20.10. `jarvis-blood-brain-barrier` port 8016 confirmed Up — §20.1, §20.3, §20.8, §20.10. Judge pipeline upgrade readiness note (both data stores at correct ports) — Status table future work, §20.8. Ch. 12 §12.11 → §12.12 — no direct cross-references to §12.11 in Ch. 20; footnote added to §20.8 for completeness.*
