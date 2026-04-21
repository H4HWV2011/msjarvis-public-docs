# Chapter 27 — Web Research and Autonomous Topic Selection

> **Why this matters for Polymathmatic Geography**
> This chapter shows how Ms. Allis "looks things up" on its own — under constraints — and folds that knowledge back into place-based memory anchored in PostgreSQL `msallisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids) and `msallis` (port **5433** ★, **5,416,521 GBIM entities** with `confidence_decay` metadata). It supports:
> - **P1 – Every where is entangled** by letting external and internal sources about specific communities and regions accumulate together over time in shared ChromaDB (★★★ **49 collections, 6,722,683 total vectors**) + PostgreSQL GeoDB structures.
> - **P3 – Power has a geometry** by centralizing web and autonomous access behind gateways, learners, and filters whose flows and ports can be audited and redesigned. ★ BBB gate decisions are now durably logged at `allis-memory:8056` (secured March 28). ★★★ All 6 BBB filters confirmed responding (April 9).
> - **P5 – Design is a geographic act** by embedding web research outputs directly into the same RAG and PostgreSQL spatial backbones (`msallisgis:5432` ★, 91 GB PostGIS, 501 tables, 993 ZCTA centroids) that serve Appalachian governance, benefits, and resilience questions.
> - **P12 – Intelligence with a ZIP code** by steering curiosity through topics selected from West Virginia–relevant queues and knowledge-gap maps grounded in PostgreSQL GBIM from `msallis:5433` ★ (5,416,521 entities with `confidence_decay` metadata). ★ AAPCAppE now supplies `msallis_docs` (4,192 items) as an additional ZIP-coded substrate. ★★★ `appalachian_english_corpus` live at 210 documents, self-refreshing every 6 hours via cron.
> - **P16 – Power accountable to place** by making autonomous learning schedulable, loggable, and subject to the same constitutional and identity filters validated against PostgreSQL as user-facing flows. ★ All BBB and `truthverdict` filter decisions now persist to `allis-memory:8056` (secured March 28). ★★★ `allis-memory:8056` endpoints fully mapped (April 9).
>
> As such, this chapter belongs to the **Computational Instrument** tier: it describes how periodic web research and topic selection are implemented as controlled, observable processes that feed back into entangled, place-aware memory in PostgreSQL `msallisgis` ★ and `msallis` ★.

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: ★★★ 2026-04-10 — ChromaDB port corrected (127.0.0.1:8002->8000/tcp, not host:8000); container count updated to 107 Up (was 96); ChromaDB inventory updated to 49 collections / 6,722,683 vectors; `allis-autonomous-learner` documented as intentionally internal-only (qualia-net only, no host binding — correct design); `rag_grounded_v2` confirmed healthy at 127.0.0.1:7241; BBB 6-filter stack fully confirmed; live steg catch documented; `allis-memory:8056` endpoints fully mapped; Chroma 1.0.0→0.6.3 SQLite schema incompatibility diagnosed and resolved; `appalachian_english_corpus` recreated clean and seeded with 210 documents; crontab cleaned and 6-hour scraper schedule applied; admin token rotated and secured.*

*★★ April 1, 2026: Live telemetry confirmed — autonomous learner: 15 cycles / 15 stored / 0 deduplicated / 11 entanglement nodes (current post-LEARN-03 session); `autonomous_learner` ChromaDB: 68 items; GBIM router (`allis-gbim-query-router:7205`) HTTP 200 confirmed; `allis-autonomous-learner` Up (LEARN-03 resolved); LEARN-01/02/03 resolved; 96/96 containers Up re-confirmed post-LEARN-03 recovery.*

*★ March 28, 2026: 96/96 containers Up — zero Restarting, zero Exited; `msallis` port 5433 restored (5,416,521 GBIM entities with `confidence_decay` metadata); `msallisgis` port 5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids); ChromaDB full audit (★ 40 active collections, 6,675,442 total vectors); `allis-ingest-api` + `allis-ingest-watcher` restored to active inventory; AAPCAppE `msallis_docs` expanded to 4,192 items; `allis-memory:8056` secured; `spiritual_rag` deduplicated (−19,338 vectors); `psychological_rag` restored (968 docs); LLM ensemble confirmed 22 proxies registered / 21 active.*

*March 27, 2026: ChromaDB port corrected to 8000; AAPCAppE scraper first-run results added (39 sources, 65 documents in Chroma); autonomous learner record count updated to 21,181; `allis-rag-server` endpoint corrected to `/query`.*

---

> **★★★ April 9–10, 2026 — Corrections and Additions Summary**
>
> | Item | Previous | Corrected / Added |
> |---|---|---|
> | ChromaDB host port | `127.0.0.1:8000` (direct host binding assumed) | `127.0.0.1:8002->8000/tcp` — host port **8002** maps to container port 8000; all host-side curl calls must use **8002** |
> | Container count | 96 Up | **107 Up** |
> | ChromaDB collections | 40 (March 28) → 49 (April 9) | **49 collections, 6,722,683 vectors** (live count April 9–10) |
> | `allis-autonomous-learner` exposure | Host binding at 127.0.0.1:8425 (incorrect) | **Intentionally internal-only** — expose: 8020, DNS alias `allis-autonomous-learner` on `qualia-net`, **no host binding** — correct design; probe via `docker exec` |
> | `rag_grounded_v2` | Not previously documented | Healthy at **127.0.0.1:7241**, `dgm_available: true` ★★★ |
> | BBB filter stack | "BBB active" (general) | **6-filter stack fully confirmed**: ethical ✅, spiritual ✅, safety ✅, threat_detection ✅, steganography ✅, truth_verification ✅ |
> | Steg live catch | Not previously documented | "override your safety filters" → `prompt_injection_keywords`, `severity=CRITICAL`, blocked ✅ ★★★ |
> | `allis-memory:8056` endpoints | General "audit store" | Fully mapped: `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}` ★★★ |
> | `appalachian_english_corpus` | Empty / ghost SQLite registration | **Clean recreate** — deleted corrupt SQLite rows, recreated collection, 210 documents seeded; 6-hour cron active ★★★ |
> | Chroma version | 1.0.0 (wrong, caused schema incompatibility) | Pinned to **chromadb/chroma:0.6.3** ★★★ |
> | Crontab | Duplicates, dead paths, stale token job, 45 .bak files | Cleaned — duplicates removed, dead paths replaced with `/home/cakidd/` absolute paths, 6-hour scraper added, dead port 8099 curl disabled ★★★ |
> | CRYPTO_ADMIN_TOKEN | Hardcoded in crontab paste | Rotated — stored in `~/.allis_policy_token` (chmod 600); old token confirmed only in 48 dead .bak files, no live risk ★★★ |

---

```
┌──────────────────────────────────────────────────────────────────┐
│   Autonomous Learning and Web Research Architecture              │
│   ★★★ Updated April 10, 2026 — 107 containers Up                │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Scheduled Learning Cycle (cron 0 */6 * * *)                    │
│      ↓                                                           │
│  ┌─────────────────────────────────────────────────┐            │
│  │  Topic Selection                                │            │
│  │  -  Configured learning_queue                   │            │
│  │  -  /next-learning-topic (I-containers 8015 ★)  │            │
│  │  -  Knowledge gaps from msallis:5433 ★ GBIM    │            │
│  │     5,416,521 entities, confidence_decay        │            │
│  │  -  15 Appalachian community domains            │            │
│  └─────────────────────────────────────────────────┘            │
│      ↓                                                           │
│  ┌─────────────────────────────────────────────────┐            │
│  │  Retrieval & Filtering                          │            │
│  │  ┌──────────────────┬───────────────────────┐   │            │
│  │  │  Internal (RAG)  │  External (Web)       │   │            │
│  │  │  - ChromaDB ★★★  │  - Web gateways ★     │   │            │
│  │  │    host:8002     │  - Domain policies    │   │            │
│  │  │    → container   │  - Rate limits        │   │            │
│  │  │    port 8000     │  - Geographic filters │   │            │
│  │  │    49 collections│  - AAPCAppE ingest ★  │   │            │
│  │  │    6,722,683 vecs│    allis-ingest-api   │   │            │
│  │  │  - rag_grounded  │    + ingest-watcher ★ │   │            │
│  │  │    _v2:7241 ★★★  │  - appalachian_english│   │            │
│  │  │    dgm_avail=true│    _corpus: 210 docs  │   │            │
│  │  │  - Postgres-     │    cron 0 */6 * * *   │   │            │
│  │  │    sourced RAG   │    ★★★                │   │            │
│  │  │    (8003-8005 ★) │                       │   │            │
│  │  └──────────────────┴───────────────────────┘   │            │
│  └─────────────────────────────────────────────────┘            │
│      ↓                                                           │
│  ┌─────────────────────────────────────────────────┐            │
│  │  Summarization & Embedding                      │            │
│  │  -  ONNX sentence embeddings (384-dim)          │            │
│  │  -  LLM-based summarization (21 active ★)       │            │
│  │  -  Semantic deduplication check                │            │
│  └─────────────────────────────────────────────────┘            │
│      ↓                                                           │
│  ┌─────────────────────────────────────────────────┐            │
│  │  BBB 6-Filter Stack (port 8016) ★★★            │            │
│  │  ethical ✅  spiritual ✅  safety ✅            │            │
│  │  threat_detection ✅  steganography ✅          │            │
│  │  truth_verification ✅                          │            │
│  │  Live catch: prompt_injection → CRITICAL/block  │            │
│  │  Audit → allis-memory:8056 ★★★                 │            │
│  │    /steg_report  /pia_window  /memory/turn      │            │
│  │    /memory/get  /memory/sessions  /memory/      │            │
│  │    session/{id}  /memory/quest*                 │            │
│  │    /memory/episodic/{id}                        │            │
│  └─────────────────────────────────────────────────┘            │
│      ↓                                                           │
│  ┌─────────────────────────────────────────────────┐            │
│  │  Storage Integration                            │            │
│  │  -  ChromaDB collections (append) ★★★           │            │
│  │    - autonomous_learner (21K records)           │            │
│  │      ★★★ internal-only: qualia-net DNS          │            │
│  │      no host binding — correct design           │            │
│  │    - appalachian_english_corpus (210 docs ★★★)  │            │
│  │    - ms_allis_memory                            │            │
│  │    - msallis_docs (4,192 items AAPCAppE)        │            │
│  │    - psychological_rag (968 docs)               │            │
│  │    ★★★ 49 total, 6,722,683 vectors              │            │
│  │  -  PostgreSQL msallisgis:5432 ★                │            │
│  │  -  PostgreSQL msallis:5433 ★                   │            │
│  └─────────────────────────────────────────────────┘            │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

> **Figure 27.1.** Autonomous learning and web research architecture: scheduled cycles (★★★ 6-hour cron) select topics from PostgreSQL GBIM knowledge gaps (`msallis:5433` ★, 5,416,521 entities with `confidence_decay` metadata), retrieve internal (ChromaDB at host **8002**→container 8000 ★★★; ★★★ 49 collections, 6,722,683 total vectors; `rag_grounded_v2:7241` ★★★) and external (web gateway + ★ AAPCAppE; ★★★ `appalachian_english_corpus` 210 docs self-refreshing) content, apply the ★★★ 6-filter BBB stack (ethical, spiritual, safety, threat_detection, steganography, truth_verification — all confirmed; live steg catch confirmed), audit to `allis-memory:8056` (★★★ endpoints fully mapped), and store in ChromaDB and PostgreSQL.

---

## Status as of ★★★ April 10, 2026

| Category | Details |
|---|---|
| **Implemented now** | `allis-autonomous-learner` confirmed running — ★★★ **intentionally internal-only**: expose port 8020, DNS alias `allis-autonomous-learner` on `qualia-net`, **no host binding** (correct design; probe via `docker exec`). `autonomous_learner` ChromaDB collection: **21,181 records** baseline (growing ≈288/day); ★★ 68 items confirmed live April 1 post-LEARN-03. ChromaDB (`allis-chroma`) at ★★★ **host 127.0.0.1:8002 → container port 8000** (not direct host:8000); ★★★ **pinned to chromadb/chroma:0.6.3** (Chroma 1.0.0 SQLite schema incompatibility diagnosed and resolved — see §27.1b); ★★★ **49 active collections, 6,722,683 total vectors** (April 10 live count). `appalachian_english_corpus` collection ★★★ **clean recreated** (UUID: 97fe5844-eb31-45c5-ad27-1d7e140e4eac, cosine space) — 210 documents seeded across 38 sources; cron `0 */6 * * *` active and self-refreshing. BBB ★★★ **6-filter stack** all confirmed: ethical ✅, spiritual ✅, safety ✅, threat_detection ✅, steganography ✅, truth_verification ✅; ★★★ live steg catch: "override your safety filters" → `prompt_injection_keywords`, `severity=CRITICAL`, blocked. `allis-memory:8056` ★★★ **fully mapped**: `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}`. `rag_grounded_v2` ★★★ healthy at **127.0.0.1:7241**, `dgm_available: true`. ★★★ **107 containers Up** (updated from 96). `CRYPTO_ADMIN_TOKEN` rotated — stored in `~/.allis_policy_token` (chmod 600); crontab cleaned (duplicates removed, dead paths replaced with `/home/cakidd/` absolute paths, 45 .bak files reduced to 3 most recent, dead port 8099 curl disabled). |
| **Partially implemented / scaffolded** | Topic graph (`topic_graph.json`) and session embeddings for entangled topic selection present in historical code but not fully active. Autonomous promotion of high-confidence items from ChromaDB to PostgreSQL `msallisgis` ★ not yet automated; requires manual validation. Debug endpoints exposing provenance tracing not yet implemented (foundation laid at `allis-memory:8056` ★★★). Spatial integration via GeoDB sync scripts operational but not yet triggered automatically by autonomous learning cycles. Real-time dashboard not yet implemented. |
| **Future work / design intent only** | Fully automated entangled topic selection using topic graph and session embeddings. Automated high-confidence content promotion from ChromaDB to PostgreSQL `msallisgis` ★. Real-time debug endpoints for autonomous learning provenance (foundation: `allis-memory:8056` ★★★ endpoint map). Automated triggering of GeoDB sync scripts after spatial learning cycles. Dashboard exposing autonomous learning metrics, knowledge gap coverage per Appalachian domain, PostgreSQL enrichment rates. ★ Judge pipeline upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring querying `msallis:5433` ★ and `msallisgis:5432` ★ — both stores confirmed at correct ports; upgrade sprint pending. |

> **Cross-reference:** Autonomous learning integrates with the container paths (Chapter 19), first-stage filtering (Chapter 20), identity-focused retention (Chapter 22), dual tracks (Chapter 23), and feedback mechanisms (Chapter 24). All autonomous outputs are subject to the same BBB safety filtering (Chapter 16; ★★★ 6-filter stack confirmed; audit → `allis-memory:8056`) and truth validation against PostgreSQL `msallisgis` ★ and `msallis` ★ as user-facing flows. For canonical `ultimatechat` execution where web research appears, see **Chapter 17**.

---

# 27. Web Research and Autonomous Topic Selection

This chapter describes the periodic web-research and autonomous learning processes that now run as first-class services alongside user-facing chat, all grounded in PostgreSQL `msallisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids) and `msallis` (port **5433** ★, **5,416,521 GBIM entities** with `confidence_decay` metadata). These processes allow the system to identify topics of interest, collect both internal and external material under constraints validated against PostgreSQL ground truth, and feed that material back into internal stores in a controlled way. The basic pattern — scheduled retrieval via gateways, semantic storage in ChromaDB (★★★ **49 active collections, 6,722,683 total vectors**), validated writes to both PostgreSQL stores, and filtered reuse — parallels retrieval-augmented and tool-using designs in the broader literature while being adapted to Ms. Allis's WV-first, PostgreSQL GBIM-anchored architecture.

---

## 27.1 Role of Periodic Web Research and Autonomous Learning

Periodic web research and autonomous learning serve three primary functions, distinct from heartbeat or status checks, all grounded in PostgreSQL `msallisgis` ★ and `msallis` ★.

**Background updating.** By running independently of direct user queries, the learner keeps selected areas of knowledge current. It periodically retrieves internal embeddings from ChromaDB collections through the ★★★ correct host port **8002** (mapping to container port 8000), and augments them with freshly retrieved web content via the web-research gateway. This allows the system's knowledge base to evolve in response to changes in the outside world while maintaining fidelity to PostgreSQL ground truth, rather than only when prompted by users. ★ As of March 28, 2026: the AAPCAppE ingest pipeline (`allis-ingest-api` + `allis-ingest-watcher`, restored to active inventory) provides a second, always-on background updating pathway. ★★★ As of April 9–10, 2026: the `appalachian_english_corpus` collection (210 documents, 38 sources) is live and self-refreshing every 6 hours via cron.

**Curiosity and topic exploration.** The learner's `learning_queue`, the `/next-learning-topic` endpoint querying PostgreSQL GBIM knowledge gaps from `msallis:5433` ★ (5,416,521 entities with `confidence_decay` metadata), and its embedding-based summarization infrastructure allow the system to pursue topics of intrinsic interest and local importance grounded in West Virginia institutional and community data. ★★★ The `appalachian_english_corpus` collection (210 documents, top contributors: WV Watch 50, WOAY 35, Daily Yonder 14, WV Tourism 12, WV Public Economy 12, WV Policy 10, AppVoices 10, WBOY 10) provides a live, self-refreshing Appalachian English substrate directly grounding topic selection in regional voice and vocabulary.

**Support for later tasks.** Items stored by the learner become part of the corpus available to RAG pipelines and orchestrated reasoning paths. ★★★ `rag_grounded_v2` (healthy at **127.0.0.1:7241**, `dgm_available: true`) is now confirmed as an additional RAG endpoint alongside the existing stack, providing DGM-grounded retrieval for downstream ULTIMATE flows.

These functions operate within bounds set by truth filters, ★★★ the confirmed 6-filter BBB stack (ethical, spiritual, safety, threat_detection, steganography, truth_verification — all responding), and ★★★ fully mapped `allis-memory:8056` audit endpoints, ensuring that autonomous knowledge acquisition remains subordinate to safety and governance constraints grounded in PostgreSQL.

### 27.1a AAPCAppE Scraper — First Run Results (March 27, 2026; ★ pipeline active March 28)

> **March 27, 2026:** The AAPCAppE scraper completed its first successful run:
> - **39 sources** indexed
> - **total_runs: 1**
> - **65 documents** ingested into Chroma on startup
> - ★ **`msallis_docs` expanded to 4,192 items** as of March 28 (subsequent AAPCAppE ingest runs)
>
> RAG search returning exact results — emergency protocol and Fayette County utility examples confirmed retrievable. ★ As of March 28, 2026: `allis-ingest-api` + `allis-ingest-watcher` confirmed restored to active inventory (96/96 Up). See **Ch 30** for full corpus architecture.

### 27.1b Chroma 1.0.0 → 0.6.3 SQLite Schema Incompatibility — Diagnosis and Resolution (★★★ April 9, 2026)

> **Root cause.** The `allis-chroma` container was running `chromadb/chroma:1.0.0`, which wrote a SQLite schema incompatible with the installed 0.6.x Python client. Symptoms included `chromadb.HttpClient` hanging indefinitely on `create_collection` at host port 8002 (KeyboardInterrupt during network read), and `Connection reset by peer` on `/auth/identity` after attempted downgrade. The schema mismatch was `EmbeddingsQueueConfigurationInternal` vs `SqlEmbeddingsQueue` type mismatch; the `migrations` table was missing the `id` column entirely.
>
> **Fix applied.**
> 1. Stopped crash-looping container
> 2. Deleted incompatible `chroma.sqlite3`, `.wal`, and `.shm` files from the live volume mount (`/home/ms-allis/msallis-rebuild/persistent/chroma/`)
> 3. Restarted container pinned to `chromadb/chroma:0.6.3` on clean volume
> 4. Verified heartbeat (`/api/v2/heartbeat` 200) and version (`0.6.3`) ✅
>
> **Carry-forward rule:** The container image must remain pinned to `chromadb/chroma:0.6.3`. Do not pull `latest` or upgrade to 1.x without a full schema migration plan and backup.

> **`appalachian_english_corpus` clean recreate.** The prior collection registration was a ghost SQLite entry — segment directories had never been created, so the collection had no backing files. This caused the backfill failure. Fix: deleted all SQLite rows for this collection UUID, recreated collection clean (UUID: 97fe5844-eb31-45c5-ad27-1d7e140e4eac, cosine space), ran `aaacpe_scraper_patched.py` — 210 documents ingested across 38 sources. Non-fatal failures noted: Appalachian Studies 404, Fairmont State dead feed, OHVEC dead feed, Facebook scrapers returning no `<article>` elements.

### 27.1c `allis-autonomous-learner` — Internal-Only Design (★★★ April 9, 2026)

> **Correction to prior documentation.** Previous chapter states listed `allis-autonomous-learner` as running at `127.0.0.1:8425` with a host binding. This was incorrect. The correct and intended design:
>
> - **expose: 8020** (Docker expose, not published)
> - **DNS alias:** `allis-autonomous-learner` on `qualia-net`
> - **No host binding** — the container is intentionally unreachable from the host network
> - **Health probing:** via `docker exec` or internal `qualia-net` service calls
>
> This is the correct architectural design — the autonomous learner is an internal service that communicates over the container network only. All VERIFYANDTEST.sh Section 12 probes must use `docker exec` rather than `curl localhost:8020`. The `/learning/status` endpoint (documented in Ch 28 §28.1a) remains valid when called from within `qualia-net`.

---

## 27.2 Scheduling, Cadence, and Logging

Autonomous learning and web research run on a regular, observable schedule with explicit tracking of PostgreSQL validation.

**Periodic cadence.** The learner is configured as a long-lived service that executes a learning cycle at configurable intervals. ★★★ As of April 9, 2026: the AAPCAppE scraper wrapper (`scripts/run_aaacpe_scraper.sh`) runs on a 6-hour cron schedule (`0 */6 * * *`), confirmed via `crontab -l`. The scraper uses absolute paths under `/home/cakidd/` and a get/create collection fallback to ensure robustness across restarts. As of March 14 baseline, the `autonomous_learner` ChromaDB collection contains **21,181 records growing ≈288/day**.

**Coordinated use of RAG and web services.** Within each cycle, the learner constructs embeddings, queries ChromaDB collections at ★★★ **host port 8002** (container port 8000; 49 collections, 6,722,683 total vectors), and calls web-research gateways. ★★★ `rag_grounded_v2` (healthy at **127.0.0.1:7241**, `dgm_available: true`) is now confirmed as an additional retrieval endpoint for DGM-grounded RAG within learning cycles.

**Logging and status reports.** Learner logs record embedding operations, ChromaDB insertions, topic selections, PostgreSQL validation checks, and web-gateway calls. ★★★ `allis-memory:8056` endpoints are fully mapped for audit retrieval:

```
/steg_report          — steganography detection events
/pia_window           — PIA (personally identifiable access) window
/memory/turn          — per-turn memory store
/memory/get           — memory retrieval
/memory/sessions      — session list
/memory/session/{id}  — session detail
/memory/quest*        — quest/task memory (wildcard)
/memory/episodic/{id} — episodic memory by ID
```

★★★ Crontab hygiene applied April 9: duplicate `monitor_disk.sh` entries removed; redundant `backup_chromadb.sh` removed (covered by existing rsync job); dead `~/msallis-rebuild/` path references replaced with `/home/cakidd/` absolute paths; `run_aaacpe_scraper.sh` added at `0 */6 * * *`; dead port 8099 curl job disabled as inline comment; applied via `crontab /tmp/allis_crontab.txt`, verified with `crontab -l` ✅.

---

## 27.3 Topic Selection

Each autonomous learning cycle starts by selecting one or more topics to investigate, guided by configuration, identity signals, and PostgreSQL GBIM knowledge gaps from `msallis:5433` ★.

**Configured topic lists and embeddings.** The learner maintains an internal list of topics and uses a sentence-embedding model (ONNX, 384-dim — the only compatible embedding model for all ★★★ 49 ChromaDB collections, per Ch 19 §19.8.8a) to encode both raw texts and higher-level session summaries.

**Knowledge-gap–driven selection.** The `/next-learning-topic` endpoint on the I-containers service (port **8015** ★) queries ChromaDB (via ★★★ host port **8002**; 49 collections, 6,722,683 vectors) to identify knowledge gaps across fifteen Appalachian community domains validated against PostgreSQL GBIM beliefs from `msallis:5433` ★ (5,416,521 entities with `confidence_decay` metadata). The `confidence_decay` metadata provides a graded signal for gap prioritization: high-decay beliefs represent weaker anchors and stronger candidates for fresh autonomous research.

**★★★ Appalachian English corpus as topic grounding.** The live `appalachian_english_corpus` collection (210 documents, 38 sources, self-refreshing every 6 hours) provides a real-time Appalachian regional voice substrate for topic selection. Top contributors (WV Watch, WOAY, Daily Yonder, WV Tourism, WV Public Economy, WV Policy, AppVoices, WBOY) represent active publishing sources whose ongoing output directly informs topic selection priorities. Non-active sources (Appalachian Studies 404, Fairmont State dead feed, OHVEC dead feed) are documented for recovery or replacement in Ch 29.

**Hooks for entangled topic dynamics.** Historical variants include scaffolding for a `topic_graph.json` and session embeddings that can construct a graph of related topics anchored in PostgreSQL spatial and institutional features (`msallisgis:5432` ★, 501 tables, 993 ZCTA centroids). The long-term plan is to bias future topic selection toward neighbors of recently studied topics, turning autonomous learning into a structured walk through entangled regions of knowledge grounded in PostgreSQL GeoDB.

---

## 27.4 Retrieval, Filtering, and Deduplication

Once topics are selected, each cycle performs retrieval and screening to convert raw search results into curated, semantically indexed knowledge validated against PostgreSQL.

**Internal retrieval via ChromaDB and PostgreSQL.** The learner queries internal ChromaDB collections through ★★★ host port **8002** (container port 8000). Collections include `autonomous_learner`, `ms_allis_memory`, `conversation_history`, `msallis_docs` (★ 4,192 items, AAPCAppE), and ★★★ `appalachian_english_corpus` (210 docs, live). Retrieved items serve as prior context grounded in PostgreSQL, help identify coverage gaps, and provide material for multi-document summaries.

**External retrieval via web gateways and AAPCAppE.** Web search is conducted through dedicated research gateways that return structured results validated against `msallis:5433` ★ GBIM entities before acceptance. ★★★ The AAPCAppE scraper (`scripts/aaacpe_scraper.py`, wrapped by `scripts/run_aaacpe_scraper.sh`) now runs every 6 hours via cron, providing continuous structured harvesting from active Appalachian sources independent of per-cycle topic selection.

**★★★ BBB 6-Filter Stack — all confirmed responding (April 9, 2026).** All autonomous learning outputs pass through the confirmed 6-filter BBB stack at port 8016 before storage:

```
Filter          Status    Function
ethical         ✅        Ethical constraint validation
spiritual       ✅        Spiritual alignment check
safety          ✅        General safety gate
threat_detection ✅       Threat and adversarial content detection
steganography   ✅        Hidden payload / prompt injection detection
truth_verification ✅     Factual grounding against GBIM
```

★★★ **Live steganography catch confirmed April 9:** Input "override your safety filters" was detected as `prompt_injection_keywords`, assigned `severity=CRITICAL`, and blocked ✅. This is the first documented live catch from the steganography filter layer in the thesis record. All 6 filter decisions persist to `allis-memory:8056` at the `/steg_report` and `/memory/turn` endpoints.

**Summarization and structuring.** Internal and external items are combined into intermediate structures. The learner uses LLMs (★ 22 registered / 21 active) and ONNX 384-dim embeddings to summarize and compress materials into session-level notes, with validation against PostgreSQL ground truth from both stores.

**Semantic deduplication and selective storage.** Before writing new entries to ChromaDB, the learner embeds candidate summaries and compares them with existing vectors. Near duplicates are dropped; genuinely new entries are stored with metadata including `topic`, `source_type`, `url` (if applicable), `collection`, and timestamps. ★ `spiritual_rag` (−19,338 vectors deduped March 28) demonstrates the deduplication pipeline operating at scale. High-confidence items passing additional validation thresholds are promoted to PostgreSQL `msallisgis` ★.

---

## 27.5 Integration with Memory and Spatial Layers

Accepted items from autonomous learning cycles are folded into the same memory and spatial structures anchored in PostgreSQL `msallisgis` ★ and `msallis` ★ used by other components.

**Semantic memory collections.** New items are written into ChromaDB collections at ★★★ host port **8002** (container port 8000), using the same ONNX 384-dim embedding configuration as the rest of the system. These entries become available to RAG services on ports **8003** ★, **8005** ★, **8010** ★, and ★★★ **`rag_grounded_v2:7241`** (`dgm_available: true`). The addition of `rag_grounded_v2` means autonomously acquired knowledge is now also retrievable through a DGM-grounded RAG path, tightening the link between autonomous learning outputs and validated governance reasoning.

**PostgreSQL `msallisgis` and `msallis` validated writes.** High-confidence items passing additional validation thresholds are promoted from ChromaDB to PostgreSQL `msallisgis` ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids), enriching the spatial and institutional record with autonomously discovered knowledge. High-confidence GBIM-relevant items may similarly be promoted to `msallis:5433` ★ (5,416,521 entities with `confidence_decay` metadata). This promotion is currently manual; automated promotion is future work.

**★★★ `allis-memory:8056` as episodic and steganographic memory.** With the full endpoint map now confirmed, `allis-memory:8056` functions as more than a BBB audit store. The `/memory/episodic/{id}` endpoint enables episodic memory retrieval by session/event ID; `/memory/quest*` supports task-oriented memory; `/pia_window` tracks PIA access windows; and `/steg_report` maintains the steganography catch log. Autonomous learning sessions generate events at `/memory/turn` on each cycle, creating a durable episodic record of what the learner researched, what it found, and what the filters blocked — all queryable by downstream orchestrators.

**Spatial integration and GIS export.** Existing scripts connect ChromaDB (★★★ host port **8002**; 49 collections, 6,722,683 vectors) and PostgreSQL GeoDB (`msallisgis:5432` ★, 993 ZCTA centroids), allowing semantic entries to be exported as GeoJSON and PostgreSQL spatial features to be embedded back into ChromaDB collections such as `geodb_*`. Autonomous learning about spatial themes — infrastructure, flood risk, service access — can therefore be tied to PostgreSQL locations and later recovered through GIS RAG querying PostgreSQL GeoDB.

**Belief and identity layers.** Over time, autonomously acquired material validated against `msallis:5433` ★ GBIM entities (5,416,521 beliefs with `confidence_decay` metadata) can inform GBIM beliefs, governance reasoning, and identity formation. Autonomously promoted beliefs begin their lifecycle with a baseline decay score that increases if not subsequently corroborated — aligning autonomous learning contributions with the evidentiary discipline of the broader GBIM belief store.

---

## 27.6 Interaction with Container and Governance Paths

Autonomous outputs are subject to the same container and governance processes validated against PostgreSQL as user-driven inputs.

**I-containers and subconscious RAG.** Newly learned items can be treated as candidates for subconscious storage and identity influence validated against `msallis:5433` ★ GBIM entities. The Fifth DGM service and WOAH algorithms can evaluate these items, deciding whether they remain in background ChromaDB collections (★★★ 49 collections, 6,722,683 vectors), are promoted into I-containers, are validated for PostgreSQL writes, or are filtered out.

**Governance filters and role constraints.** Governance and ethics components validated against `msallis:5433` ★ GBIM entities can restrict topics or sources deemed sensitive. ★★★ The full 6-filter BBB stack (ethical, spiritual, safety, threat_detection, steganography, truth_verification — all confirmed responding) is applied to both web research outputs and autonomous learner summaries before storage or PostgreSQL promotion. ★★★ The live steg catch ("override your safety filters" → `severity=CRITICAL`, blocked) confirms this layer is operationally active, not merely scaffolded. All 6-filter decisions persist to `allis-memory:8056` at their respective endpoints.

**Background influence on future decisions.** Once admitted to ChromaDB (★★★ 49 collections) and potentially promoted to PostgreSQL `msallisgis` ★, autonomous items contribute to the contexts retrieved by ULTIMATE and related orchestrators. ★★★ `rag_grounded_v2:7241` (`dgm_available: true`) adds a new DGM-grounded retrieval path, ensuring that autonomously acquired knowledge that has passed governance filters is accessible to downstream DGM-validated reasoning flows.

---

## 27.7 Safeguards and Oversight

Because web research introduces new external material, autonomous learning is equipped with multiple layers of safeguards and oversight validated against PostgreSQL `msallisgis` ★ and `msallis` ★.

**Source restrictions and gateway policies.** Web-research gateways define permitted domains, result limits, and geographic filters. Centralizing these policies ensures that external access can be tightened or adapted without redeploying the learner, with all outputs subject to PostgreSQL validation.

**Environment-based gating and operational control.** Environment variables and process supervisors provide simple mechanisms for enabling, disabling, or throttling autonomous learning. ★★★ As of April 10, 2026: **107 containers Up** — the widest confirmed active scope for autonomous learning oversight in the system's history.

**★★★ Token security and crontab hygiene (April 9, 2026).** During the April 9 session, a `CRYPTO_ADMIN_TOKEN` was identified as hardcoded in a crontab paste. Immediate response:
- Token rotated
- New token stored in `~/.allis_policy_token` with `chmod 600`
- Old token investigated: confirmed present only in 48 dead `.bak` files, not in any live Docker Compose configuration — **no live risk**
- 45 `.bak` files cleaned (3 most recent retained)
- Crontab rewritten via file method

This incident establishes the following security rule for the thesis record: **secrets must never appear in crontab entries, shell script arguments, or log output**. All tokens and credentials must be stored in chmod 600 files under the home directory and referenced by path, not by value.

**Logging, verification, and system-wide reports.** Logs from the learner, web gateways, RAG servers, and ★ `allis-ingest-api`/`allis-ingest-watcher` (AAPCAppE) are combined with periodic verification reports that list running containers (★★★ **107 Up**), ChromaDB collection counts (★★★ **49 active collections, 6,722,683 total vectors**; `autonomous_learner` at 21,181 records and growing; `appalachian_english_corpus` at 210 docs and growing every 6 hours; `msallis_docs` at 4,192 items), PostgreSQL connection status for both stores ★, GIS data health, and performance metrics. ★★★ All 6 BBB filter decisions and steganography catches now additionally persist to `allis-memory:8056` at fully mapped endpoints — providing a durable, authenticated audit trail beyond ephemeral container logs. These reports can be archived to provide a full audit trail for when autonomy was active, what it accessed, what filters caught, and how it validated against PostgreSQL.

These safeguards align autonomous learning with the program's glassbox and spatial-justice commitments grounded in PostgreSQL, keeping curiosity accountable to place and governance.

---

## 27.8 Web Research in the ULTIMATE Path

Beyond background learning, web research participates directly in user-driven, high-stakes reasoning validated against PostgreSQL `msallisgis` ★ and `msallis` ★.

**Position in the orchestration pipeline.** In ULTIMATE-style flows, web research is typically invoked after initial filtering and before deep ensemble reasoning. The main brain (port **8050** ★) may call web gateways alongside PostgreSQL-sourced RAG services — including ★★★ `rag_grounded_v2:7241` (`dgm_available: true`) — then pass the resulting context to the ★ 22-registered / 21-active LLM ensemble and judge stack, ensuring that external content is integrated deliberately and validated against `msallis:5433` ★ GBIM entities (5,416,521 beliefs with `confidence_decay` metadata) rather than incidentally. ★★★ The confirmed 6-filter BBB stack (port 8016) and `allis-memory:8056` audit layer mean every piece of externally sourced content that enters a ULTIMATE context window has passed a documented, logged, steganography-checked governance path.

**Latency and resource considerations.** Web research adds latency, particularly when reaching out to remote sources. Timeouts, bounded result counts, and careful scheduling help prevent web access from dominating response times or PostgreSQL query capacity. ★★★ With 107 containers Up, operators should confirm that the additional container overhead does not materially affect the 12–13 ms core endpoint response times documented in Ch 28 §28.2 — a VERIFYANDTEST.sh Section 4 benchmark run is recommended after any container count change above 100.

**Planned introspection and debugging.** Future versions of the web-research gateways are intended to expose debug endpoints that show, for a given request, which internal PostgreSQL (both `msallisgis:5432` ★ and `msallis:5433` ★) and ChromaDB sources (★★★ 49 collections) and which external sources were used, how they were ranked, and how context was assembled with PostgreSQL validation. ★★★ The fully mapped `allis-memory:8056` endpoint set provides the durable foundation for this provenance tracing capability — `/memory/turn`, `/memory/episodic/{id}`, and `/steg_report` already capture per-cycle and per-request filter events; source ranking and RAG selection provenance is the next layer. Combined with autonomous learner and container logs, this will support detailed provenance tracing for complex answers anchored to PostgreSQL.

In this way, web research functions as a shared, policy-constrained capability validated against PostgreSQL that supports both autonomous and interactive reasoning.

---

## 27.9 Summary

Autonomous web research and topic selection provide Ms. Allis with a controlled form of curiosity grounded in PostgreSQL `msallisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids) and `msallis` (port **5433** ★, **5,416,521 GBIM entities** with `confidence_decay` metadata): the ability to seek and structure knowledge on a schedule, under constraints validated against PostgreSQL, and with clear integration into long-term ChromaDB (★★★ **49 active collections, 6,722,683 total vectors**) and PostgreSQL memory and spatial layers.

By centralizing external access through web-research gateways, selecting topics via `/next-learning-topic` querying `msallis:5433` ★ GBIM knowledge gaps (with `confidence_decay` grading for gap prioritization), storing results in ChromaDB collections at ★★★ **host port 8002** (container port 8000), validating high-confidence content for PostgreSQL writes, and subjecting all autonomous outputs to the ★★★ **confirmed 6-filter BBB stack** (ethical, spiritual, safety, threat_detection, steganography, truth_verification — all responding; live steg catch confirmed) with full audit persistence at `allis-memory:8056` (★★★ endpoints fully mapped), the system balances the benefits of ongoing learning with the requirements of safety, accountability, and community oversight anchored to PostgreSQL ground truth.

★★★ **April 9–10, 2026 milestones:** `appalachian_english_corpus` live and self-refreshing (210 documents, 38 sources, 6-hour cron); Chroma 1.0.0→0.6.3 SQLite incompatibility resolved (pinned to 0.6.3); `allis-autonomous-learner` documented as intentionally internal-only (qualia-net DNS, no host binding — correct design); `rag_grounded_v2:7241` confirmed healthy with DGM; 6-filter BBB stack confirmed; live steganography catch documented; `allis-memory:8056` endpoints fully mapped; 107 containers Up; ChromaDB at host:8002→container:8000 corrected; CRYPTO_ADMIN_TOKEN rotated and secured; crontab cleaned with absolute paths and 6-hour scraper schedule.

As of ★ March 28, 2026, the chapter's core architecture was validated by confirmed production milestones: the AAPCAppE scraper first run (39 sources, 65 documents — §27.1a) and subsequent expansion (`msallis_docs` 4,192 items); 53-document RAG load with 7 new cultural base docs; `autonomous_learner` collection at 21,181 records and growing; `msallis:5433` ★ restored (5,416,521 GBIM entities with `confidence_decay` metadata); BBB audit trail secured at `allis-memory:8056`; and **96/96 Up** — all autonomous learning service paths simultaneously active. ★★★ All of these milestones are superseded by the April 10 state of **107 containers Up**, 49 collections, 6,722,683 vectors, and a fully confirmed, live-catch-validated 6-filter BBB stack.

By connecting autonomous learning outputs to memory, containers, governance filters, and the full `allis-memory:8056` episodic and steganographic audit layer, Ms. Allis treats its own curiosity as data — recording and reasoning about not just what it knows, but how it came to know it, what it tried to learn and was blocked, and whether the knowledge it holds remains anchored to the West Virginia communities and Appalachian landscapes it serves.

---

*Last updated: ★★★ 2026-04-10 — Mount Hope WV — Carrie Kidd (Mamma Kidd)*

*★★★ April 9–10, 2026 changes: §27.0 preamble updated (107 containers, 49 collections, 6,722,683 vectors, 6-filter BBB confirmed, steg catch, memory endpoints mapped); correction table added; Figure 27.1 updated (host:8002, 49 collections, appalachian_english_corpus, 6-filter BBB, memory endpoints); Status table updated (107 Up, 0.6.3 pinned, 6-hour cron, rag_grounded_v2, token rotated, crontab cleaned); §27.1 updated (appalachian_english_corpus live, 6-hour cron, rag_grounded_v2); §27.1b added (Chroma 1.0.0→0.6.3 diagnosis and fix; ghost collection clean recreate); §27.1c added (allis-autonomous-learner internal-only design correction); §27.2 updated (host:8002, 6-hour cron, rag_grounded_v2, allis-memory endpoint map, crontab hygiene); §27.3 updated (host:8002, 49 collections, appalachian_english_corpus topic grounding); §27.4 updated (host:8002, 49 collections, appalachian_english_corpus, 6-filter BBB stack table, live steg catch documented); §27.5 updated (host:8002, 49 collections, rag_grounded_v2, allis-memory episodic/steg endpoints); §27.6 updated (6-filter BBB confirmed, live steg catch, rag_grounded_v2 DGM path); §27.7 updated (107 Up, 49 collections, 6,722,683 vectors, appalachian_english_corpus, token security incident and rule, 6 BBB filter decisions to mapped endpoints); §27.8 updated (rag_grounded_v2, 6-filter BBB in ULTIMATE path, 107 containers benchmark note, allis-memory provenance foundation); §27.9 summary updated throughout*

*★★ April 1, 2026: LEARN-01/02/03 resolved; autonomous learner live telemetry confirmed; 96/96 Up post-LEARN-03 recovery*

*★ March 28, 2026: 96/96 containers Up; msallis:5433 restored; ChromaDB 40 collections / 6,675,442 vectors; allis-memory:8056 secured; msallis_docs 4,192 items; spiritual_rag deduplicated; psychological_rag restored*

*March 27, 2026: ChromaDB port corrected to 8000; AAPCAppE scraper first-run results added; autonomous learner record count updated to 21,181; allis-rag-server endpoint corrected to /query*
