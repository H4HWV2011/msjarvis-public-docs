# 29. Psychological Safeguards and the PIA Review Loop

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: ★★★★★ 2026-04-08 — Chapter 29 fully closed. All §29.9 open items resolved. Per-route RBAC implemented (`require_role()` on `main_brain` + `gbim_query_router`); role-differentiated rate limiting resolved (app-layer, not Caddy); automated PIA sampling cycle live (`jarvis_pia_sampler.py`, 30-min daemon, port 8076); `/steg_report` endpoint live (0 false positives); `pia_records` ChromaDB collection created + auto-ingest active; `confidence_decay` → `needs_verification` flagged (51→52 resources, `jarvis-local-resources-db:5435`); GIS RAG wired (`jarvis-gis-rag` port 8009, `jarvis-rag-search` port 8095, `main_brain` service discovery updated). Tag: `a15-complete-20260408`.*

> **★★★★★ Updates applied April 8, 2026 — Chapter closed:**
>
> | Item | Status |
> |---|---|
> | Per-route RBAC — `main_brain` `/chat/cancel/all` + `/chat/cancel/{job_id}` | ✅ `require_role({"carrie_admin"})` live (OI-36-C / OI-37, April 3; verified April 8) |
> | Per-route RBAC — `gbim_query_router` `/route` + `/query` | ✅ `require_role(x_jarvis_role)` live; 403 on missing/invalid role confirmed |
> | Role-differentiated rate limiting | ✅ Resolved — app-layer only; Caddy 60 req/min by IP is correct perimeter implementation |
> | Automated PIA sampling daemon | ✅ `jarvis_pia_sampler.py` — 30-min interval, 60s startup stagger, `pia:history` 48-entry rolling, `/enforce` A-15 gate port 8076 |
> | `/steg_report` endpoint | ✅ Live on `jarvis-memory:8056`; 0 false positives; 45 events scanned clean |
> | `pia_records` ChromaDB collection | ✅ Created (cosine similarity, `default_tenant`); auto-ingest on every sample via `_ingest_to_chroma()` |
> | `confidence_decay` → `needs_verification` | ✅ 51→52 high-decay resources flagged in `jarvis-local-resources-db:5435`; Prestera Center (decay=1.0) explicitly flagged |
> | GIS RAG pipeline | ✅ `jarvis-gis-rag:8009` (`geo_search`, `geojson`, `geojson_bbox`); `jarvis-rag-search:8095`; `main_brain` service discovery updated to `host.docker.internal:8009` |
> | `llm_judge_v3` `/verdict/psychological` endpoint | ✅ Live; `psychological_score` and `psychological_safety` scoring confirmed on two test queries (Query 1: 0.825 / 1.0; Query 2: 0.6875 / 0.45) |
>
> **All prior April 7 and March 28 updates carry forward unchanged.**

---

## Why This Matters for Polymathmatic Geography

This chapter formalizes how psychological and mental-health knowledge is integrated into Ms. Jarvis to guide interaction patterns, monitor interaction risks, and adapt system behavior over time, all grounded in PostgreSQL: `msjarvis` (port **5433** ★, **5,416,521 GBIM entities** with `confidence_decay` metadata), `msjarvisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids), and `jarvis-local-resources-db` (port **5435** ★, community resources). It supports:

- **P1 – Every where is entangled** by ensuring that psychological safeguards are woven into the same retrieval, filtering, and memory infrastructure anchored to PostgreSQL that handles spatial and technical content, not isolated in a separate silo.
- **P3 – Power has a geometry** by making psychological constraints visible as named services, tagged collections, PostgreSQL-validated rules, and explicit endpoints rather than hiding them in opaque model behavior. ★ BBB gate decisions are now durably logged at `jarvis-memory:8056` (secured March 28). ★★★★★ Per-route RBAC is implemented (April 8) — the geometry of access enforcement is now operationally enforced at the route level, not only at the perimeter.
- **P5 – Design is a geographic act** by tailoring psychological guidance to populations and risk types specific to Appalachian communities grounded in `msjarvis:5433` ★ GBIM — rural grief, economic stress, identity disruption — rather than generic global corpora. ★★★★★ GIS RAG pipeline (`jarvis-gis-rag:8009`) is now wired, grounding spatial context in the same psychological assessment flow.
- **P12 – Intelligence with a ZIP code** by grounding psychological RAG retrieval in collections that include place-specific and community-specific mental health materials validated against PostgreSQL West Virginia institutional knowledge. ★★★★★ `confidence_decay` → `needs_verification` flagging (51→52 resources, April 8) ensures the ZIP-coded psychological guidance substrate is actively curated against data freshness.
- **P16 – Power accountable to place** by logging PIA review cycle outputs in PostgreSQL-auditable format for human oversight and community governance review. ★★★★★ `jarvis_pia_sampler.py` (30-min automated daemon, live April 8) makes this accountability cycle self-sustaining for the first time. `pia_records` ChromaDB collection auto-ingest creates a permanent, queryable record of every PIA sample.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the psychological safeguard services, guidance corpus, and PIA review loop that protect interaction quality and mental-health alignment in Ms. Jarvis's operation, all anchored to the three-database PostgreSQL architecture. The `jarvis-psychology-services` (port **8019** ★) and `psychological_rag_domain` (port **8006** ★) services were deployed and confirmed operational March 15, 2026 (commit b90f9ff), contributing to the verified 349.87s end-to-end 9-phase pipeline benchmark. The steganography filter (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`) is confirmed active in the BBB 7-filter stack as of March 21, 2026. ★★★★★ As of April 8, 2026: Chapter 29 is fully closed — all §29.9 open items implemented and verified. Tag: `a15-complete-20260408`.

---

```
┌─────────────────────────────────────────────────────────────┐
│   Psychological Safeguards Architecture                     │
│   (★★★★★ April 8, 2026 — Chapter 29 Fully Closed ✅)       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Request → Caddy Perimeter (8443, HTTPS)               │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Caddy forward_auth → jarvis_auth_service      │         │
│  │  (port 8055 ★, systemd-managed)                │         │
│  │  Role: carrie_admin — full access              │         │
│  │  Role: hayden_test  — internal test role       │         │
│  │  Enforced at: Caddy perimeter + app-layer      │         │
│  │  require_role() on main_brain + gbim_router ✅  │         │
│  └────────────────────────────────────────────────┘         │
│      ↓ (authenticated, X-Jarvis-Role injected)              │
│  jarvis-main-brain (8050 ★)                                 │
│  ★★★★★ require_role({"carrie_admin"}) on:                   │
│    /chat/cancel/all (line 236) ✅                           │
│    /chat/cancel/{job_id} (line 257) ✅                      │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 1.4 — BBB 7-Filter Input Stack         │         │
│  │  (Always Active — port 8016 ★, 127.0.0.1)    │         │
│  │  ★ audit → jarvis-memory:8056 (secured Mar 28)│         │
│  │  -  EthicalFilter                               │         │
│  │  -  SpiritualFilter                             │         │
│  │  -  SafetyMonitor (word-boundary regex,         │         │
│  │    fixed March 15 — no false-positives on      │         │
│  │    community resource terms)                   │         │
│  │  -  ThreatDetection                             │         │
│  │  -  SteganographyDetection                      │         │
│  │    zero_width_homoglyph_structural_v1           │         │
│  │    confidence: 1.0 ✅ confirmed March 21        │         │
│  │  -  TruthVerification                           │         │
│  │  -  ContextAwareness                            │         │
│  │  -  TruthValidator (vs msjarvis:5433 ★ GBIM)   │         │
│  │    5,416,521 entities, confidence_decay        │         │
│  │    - correct_identity                          │         │
│  │    - correct_creator                           │         │
│  │    - relationship_clear                        │         │
│  │  -  normalize_identity                          │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 3 — Psychology Pre-Assessment           │         │
│  │  (Deployed March 15, 2026 — Always Active ★)  │         │
│  │  ┌──────────────────────────────────────────┐  │         │
│  │  │  jarvis-psychology-services (8019 ★)     │  │         │
│  │  │  /psychological_assessment               │  │         │
│  │  │  -  psychological_assessment              │  │         │
│  │  │  -  therapeutic_guidance                  │  │         │
│  │  │  -  emotional_support                     │  │         │
│  │  │  -  wellbeing_recommendations             │  │         │
│  │  │  -  evidence_based_approaches             │  │         │
│  │  │  Severity classification + crisis check  │  │         │
│  │  └──────────────────────────────────────────┘  │         │
│  │  ┌──────────────────────────────────────────┐  │         │
│  │  │  psychological_rag_domain (8006 ★)       │  │         │
│  │  │  /search, /add_document                  │  │         │
│  │  │  ChromaDB psychological_rag collection   │  │         │
│  │  │  (port 8000 ★, chroma_data volume)       │  │         │
│  │  │  ★ 968 items restored March 28           │  │         │
│  │  │  (validated vs msjarvis:5433 ★ GBIM)     │  │         │
│  │  └──────────────────────────────────────────┘  │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ★★★★★ GIS RAG Pipeline (April 8)                          │
│  -  jarvis-gis-rag:8009 (geo_search, geojson,               │
│    geojson_bbox) ✅                                         │
│  -  jarvis-rag-search:8095 (provider search) ✅             │
│  -  main_brain → host.docker.internal:8009 ✅               │
│      ↓                                                       │
│  Response Processing                                        │
│  -  truthverdict (from BBB + msjarvis:5433 ★ validation)    │
│    ★ audit → jarvis-memory:8056 (secured Mar 28)            │
│  -  consciousnesslayers (psych assessment layer included)    │
│  -  background_rag_store → ms_jarvis_memory (ChromaDB ★)    │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  jarvis-memory:8056 (★★★★★ April 8)           │         │
│  │  ─────────────────────────────────────         │         │
│  │  /health → {"status":"healthy",                │         │
│  │    "service":"ms-jarvis-memory",               │         │
│  │    "redis":"connected"} ✅                     │         │
│  │  /pia_window?minutes=240 → structured JSON ✅  │         │
│  │    Type guard: if r.type(key) != b'list':      │         │
│  │      continue (live in production code ✅)     │         │
│  │  /steg_report → steg trigger aggregation ✅    │         │
│  │    0 false positives, 45 events scanned ✅     │         │
│  │  jarvis_pia_sampler.py → 30-min daemon ✅       │         │
│  │  /enforce (A-15 gate, port 8076) ✅             │         │
│  │  pia_records → ChromaDB collection ✅           │         │
│  │  deploy-memory.sh → one-command redeploy ✅    │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  jarvis-gbim-query-router:7205                 │         │
│  │  ★★★★★ require_role(x_jarvis_role) on:        │         │
│  │    /route ✅  /query ✅                         │         │
│  │  403 on missing/invalid role confirmed ✅       │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Accountability                                             │
│  -  ★★★★★ per-route RBAC live (app-layer) ✅ April 8       │
│  -  ★★★★★ /steg_report programmatic steg query ✅           │
│  -  ★★★★★ jarvis_pia_sampler.py automated PIA ✅            │
│  -  ★★★★★ pia_records ChromaDB auto-ingest ✅               │
│  -  ★ jarvis-memory:8056 durable BBB audit log              │
│  -  PostgreSQL-auditable PIA records                         │
│  -  jarvis_auth_service access log                          │
│  -  Community governance review                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 29.1.** Psychological safeguards architecture (★★★★★ April 8, 2026 — Chapter 29 fully closed): Caddy perimeter (port 8443) with `forward_auth` enforcing role-based access control via `jarvis_auth_service` (port **8055** ★, systemd) is the outermost layer; per-route RBAC implemented at app-layer via `require_role({"carrie_admin"})` on `main_brain` `/chat/cancel/all` (line 236) and `/chat/cancel/{job_id}` (line 257), and `require_role(x_jarvis_role)` on `gbim_query_router` `/route` and `/query` (April 8, 2026) ✅. BBB 7-filter pipeline and TruthValidator validated against `msjarvis:5433` ★ (5,416,521 GBIM entities with `confidence_decay` metadata) provide the primary safety gate on every authenticated request (Phase 1.4); all BBB and `truthverdict` decisions persist to `jarvis-memory:8056`; `SteganographyDetection` (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`) trigger events aggregated by `/steg_report` (0 false positives, April 8); psychological services (Phase 3, deployed March 15) backed by `psychological_rag` (968 docs); `jarvis_pia_sampler.py` daemon (30-min automated cycle, `/enforce` A-15 gate port 8076) runs continuously; `pia_records` ChromaDB collection auto-ingests on every sample; GIS RAG pipeline (`jarvis-gis-rag:8009`, `jarvis-rag-search:8095`) wired to `main_brain`; `confidence_decay` → `needs_verification` flagged (51→52 resources); all accountability records durable at `jarvis-memory:8056` and PostgreSQL-auditable for community governance review.

---

## Status as of ★★★★★ April 8, 2026

| Category | Details |
|---|---|
| **Implemented and verified** | `jarvis-psychology-services` confirmed running at `127.0.0.1:8019` ★. Phase 3 psychology pre-assessment active on every production 9-phase pipeline request — severity classification and crisis indicator check confirmed in 349.87s end-to-end benchmark. `psychological_rag_domain` confirmed running at `127.0.0.1:8006` ★ — ★ **968-item corpus** (restored March 28). BBB 7-filter pipeline at `127.0.0.1:8016` ★ — all 7 filters active; ★ all decisions persist to `jarvis-memory:8056`. `normalize_identity` and TruthValidator on every `ultimatechat` response. Caddy perimeter + `jarvis_auth_service` (8055 ★, systemd) — RBAC active March 22. ★★★★★ **April 8 items all confirmed live:** per-route RBAC (`require_role()` on `main_brain` + `gbim_query_router`) ✅; `jarvis_pia_sampler.py` 30-min daemon ✅; `/steg_report` (0 false positives) ✅; `pia_records` ChromaDB collection + auto-ingest ✅; `confidence_decay` → `needs_verification` (51→52 resources) ✅; GIS RAG (`jarvis-gis-rag:8009`, `jarvis-rag-search:8095`) ✅; `llm_judge_v3` `/verdict/psychological` endpoint live (Query 1: 0.825/1.0; Query 2: 0.6875/0.45) ✅. **★ 96/96 containers Up — zero Restarting, zero Exited.** |
| **Intentionally deferred** | Population- and risk-type-specific RAG retrieval tuning → Chapter 30 scope (GBIM data confirmed at `msjarvis:5433`; GIS pipeline live). Judge pipeline upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring → Chapter 7 §7.8 dedicated sprint (both stores confirmed at correct ports). |

Cross-reference: BBB 7-filter pipeline — Chapter 16. Identity normalization and TruthValidator — Chapter 22. Psychological services and meaning-oriented track — Chapter 23. Canonical 9-phase `ultimatechat` sequence — Chapter 17. ChromaDB `psychological_rag` architecture — Chapter 5. March 18, 2026 security hardening — Chapter 40 §40-C. Caddy perimeter + `jarvis_auth_service` — Chapter 19 §19.8.1–§19.8.2. ★ `jarvis-memory:8056` durable BBB audit trail architecture — Chapter 25 §25.2. GIS RAG pipeline — Chapter 30. Judge pipeline upgrade — Chapter 7 §7.8.

---

## 29. Psychological Safeguards and the PIA Review Loop

This chapter formalizes how psychological and mental-health knowledge is integrated into Ms. Jarvis to guide interaction patterns, monitor interaction risks, and adapt system behavior over time. In the current deployment (★★★★★ April 8, 2026 — chapter fully closed), this is realized through two confirmed running services — `jarvis-psychology-services` (port **8019** ★, deployed March 15) and `psychological_rag_domain` (port **8006** ★, containerized March 15) — a curated psychological corpus in ChromaDB (★ **968 items**, `psychological_rag` collection, port **8000** ★, `chroma_data` volume), validation against PostgreSQL `msjarvis` (port **5433** ★, ★ **5,416,521 GBIM entities with `confidence_decay` metadata**), the BBB 7-filter pipeline at `127.0.0.1:8016` ★ as the primary live Phase 1.4 safety gate (★ audit → `jarvis-memory:8056`), per-route RBAC enforced at the app layer (`require_role()` on `main_brain` and `gbim_query_router`), and the `jarvis_pia_sampler.py` automated 30-min PIA daemon as the continuously running PIA review cycle.

★★★★★ **Chapter 29 is fully closed as of April 8, 2026.** All items in §29.9 have been implemented, verified, and committed. Tag `a15-complete-20260408` marks the close. Two items are intentionally deferred to later chapters (population/risk-type retrieval tuning → Ch 30; judge pipeline upgrade → Ch 7 §7.8) and do not block closure.

A critical constraint carries forward unchanged: these mechanisms are designed for supportive, psychoeducational guidance and risk awareness validated against PostgreSQL community data, not for formal DSM-style diagnosis or clinical decision-making.

---

## 29.1 Role of Psychological Guidance

In the current deployment, psychological guidance grounded in `msjarvis:5433` ★ GBIM is not treated as an auxiliary feature but as a core constraint on how the system interacts with people, enforced at Phase 3 of every production 9-phase pipeline request. Its primary functions are threefold.

**Interaction quality.** `jarvis-psychology-services` (port **8019** ★) provides principled reference points for respectful, non-coercive, and supportive exchanges validated against `msjarvis:5433` ★ GBIM (5,416,521 entities with `confidence_decay` metadata) West Virginia community norms. Its `/psychological_assessment` endpoint runs on every production request and returns structured responses: `therapeutic_guidance`, `emotional_support`, `wellbeing_recommendations`, and `evidence_based_approaches`. `psychological_rag_domain` (port **8006** ★) provides retrieval of curated materials — therapy, mindfulness, trauma, depression, anxiety, and social-support content (★ **968 items**) — via `/search`, backed by the ChromaDB `psychological_rag` collection (port **8000** ★, `chroma_data` volume). These materials are curated for high-level, evidence-informed guidance; they are not used to perform formal diagnosis. ★★★★★ `llm_judge_v3` `/verdict/psychological` endpoint is now live — psychological scoring (`psychological_score`, `psychological_safety`) is confirmed active on judge evaluation pipeline output.

**Risk awareness.** TruthValidator (applied on every response via `jarvis-main-brain`, port **8050** ★) encodes patterns known to be harmful — identity confusion, anthropomorphic overclaiming, misleading statements about agency and embodiment — validated against `msjarvis:5433` ★ GBIM and returns `correct_identity`, `correct_creator`, and `relationship_clear` booleans. ★ All `truthverdict` decisions are durably logged at `jarvis-memory:8056`. The BBB 7-filter Phase 1.4 stack at port **8016** ★ screens for content violating ethical or community-safety constraints including high-risk mental-health content.

**Structural integrity assurance.** The `SteganographyDetection` filter (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`, confirmed active March 21, 2026) screens every request for adversarial payloads. ★ All `SteganographyDetection` trigger events are durably logged at `jarvis-memory:8056`. ★★★★★ The `/steg_report` endpoint (live April 8) scans the full BBB audit trail and returns aggregated trigger counts — 0 false positives confirmed on 45 scanned events.

**Self-checking.** `normalize_identity` applied to every `ultimatechat` response rewrites outputs that deviate from allowed self-descriptions validated against `msjarvis:5433` ★ GBIM or blur human-machine boundaries, before the response is returned to the caller.

---

## 29.2 Confirmed Active Safeguards (★★★★★ April 8, 2026)

The following table records all confirmed active psychological safeguards as of ★★★★★ April 8, 2026. This table is the authoritative reference for PIA review scope and regression testing in Chapter 41 §41.4.1.

| Safeguard | Service / Location | Confirmed | Notes |
|---|---|---|---|
| Caddy perimeter RBAC | Caddy (port 8443 ★) + `jarvis_auth_service` (port 8055 ★) | ✅ March 22 / ★ Up March 28 | `carrie_admin` (full access), `hayden_test` (internal test role); perimeter-level enforcement |
| EthicalFilter | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| SpiritualFilter | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| SafetyMonitor | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | Word-boundary regex fix March 15; ★ audit → `jarvis-memory:8056` |
| ThreatDetection | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| **SteganographyDetection** | **BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★)** | **✅ March 21 / ★ Up March 28** | **`zero_width_homoglyph_structural_v1`, `confidence: 1.0`; ★★★★★ aggregated by `/steg_report` (0 false positives, April 8)** |
| TruthVerification | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| ContextAwareness | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| TruthValidator | `jarvis-main-brain:8050` ★ post-processing | ✅ March 15 / ★ Up March 28 | `correct_identity`, `correct_creator`, `relationship_clear` validated vs `msjarvis:5433` ★ GBIM; ★ `truthverdict` durable at `jarvis-memory:8056` |
| `normalize_identity` | `jarvis-main-brain:8050` ★ post-processing | ✅ March 15 / ★ Up March 28 | Every `ultimatechat` response |
| Phase 3 psychology pre-assessment | `jarvis-psychology-services:8019` ★ | ✅ March 15 / ★ Up March 28 | Severity classification + crisis indicator on every request; `phase3` events counted by `/pia_window` |
| Psychological RAG retrieval | `psychological_rag_domain:8006` ★ | ✅ March 15 / ★ **968 docs restored March 28** | 968-item corpus; query-based retrieval |
| BBB output guard | BBB Phase 4.5 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 18 / ★ Up March 28 | Full verdict dict received; 8.0s timeout; ★ audit → `jarvis-memory:8056` |
| ★ BBB durable audit trail | `jarvis-memory:8056` | ★ ✅ March 28 | Port corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set |
| `/pia_window` programmatic PIA query | `jarvis-memory:8056` | ★★★★★ ✅ April 7 | Scans `conv:*:*` Redis keys; counts `bbb_audit` + `phase3` events in configurable window; returns structured JSON; Redis type guard live |
| `deploy-memory.sh` | `msjarvis-rebuild/` | ★★★★★ ✅ April 7 | One-command redeploy for all `ms_jarvis_memory.py` edits |
| `jarvis-memory` in rebuild compose | `msjarvis-rebuild/docker-compose.yml` line 1141 | ★★★★★ ✅ April 7 | First-class rebuild service with bind mount volume |
| **`/steg_report` trigger aggregation** | **`jarvis-memory:8056`** | **★★★★★ ✅ April 8** | **Scans Redis BBB audit trail; 0 false positives confirmed; 45 events scanned; automated steg pattern aggregation live** |
| **`jarvis_pia_sampler.py` daemon** | **`jarvis-pia-sampler:8076`** | **★★★★★ ✅ April 8** | **30-min automated PIA sampling cycle; 60s startup stagger; `pia:history` 48-entry rolling; `/enforce` A-15 gate live** |
| **`pia_records` ChromaDB collection** | **ChromaDB (port 8000 ★)** | **★★★★★ ✅ April 8** | **First-class PIA collection; cosine similarity; `default_tenant`; auto-ingest on every sample via `_ingest_to_chroma()`** |
| **`confidence_decay` → `needs_verification`** | **`jarvis-local-resources-db:5435` ★** | **★★★★★ ✅ April 8** | **51→52 high-decay resources flagged; Prestera Center (decay=1.0) explicitly flagged** |
| **Per-route RBAC — `main_brain`** | **`jarvis-main-brain:8050` ★** | **★★★★★ ✅ April 8** | **`require_role({"carrie_admin"})` on `/chat/cancel/all` (line 236) and `/chat/cancel/{job_id}` (line 257); `hayden_test` blocked with 403** |
| **Per-route RBAC — `gbim_query_router`** | **`jarvis-gbim-query-router:7205`** | **★★★★★ ✅ April 8** | **`require_role(x_jarvis_role)` on `/route` and `/query`; 403 on missing/invalid role confirmed live** |
| **GIS RAG pipeline** | **`jarvis-gis-rag:8009` + `jarvis-rag-search:8095`** | **★★★★★ ✅ April 8** | **`geo_search`, `geojson`, `geojson_bbox` endpoints live; `main_brain` service discovery updated to `host.docker.internal:8009`** |
| **`llm_judge_v3` `/verdict/psychological`** | **`jarvis-llm-judge-v3`** | **★★★★★ ✅ April 8** | **`psychological_score` + `psychological_safety` scoring live; Query 1: 0.825/1.0; Query 2: 0.6875/0.45** |

---

## 29.3 Red-Team Token Roles and RBAC (★★★★★ Per-Route RBAC Implemented — April 8, 2026)

Role-based access control for red-team and administrative access is enforced at the Caddy perimeter layer via `jarvis_auth_service` (port **8055** ★, systemd-managed) and — ★★★★★ as of April 8 — at the application layer via `require_role()` decorators on privileged routes.

### Active Token Roles

| Role | Access Level | Notes |
|---|---|---|
| `carrie_admin` | Full access | All routes including `/chat/cancel/all`, `/chat/cancel/{job_id}`, `gbim_query_router` `/route` + `/query` |
| `hayden_test` | Internal test role | All standard `/chat*` routes; blocked with 403 on privileged cancel/admin routes ★★★★★ |

### Enforcement Architecture

```
Request → Caddy (8443 ★)
    ↓
forward_auth → jarvis_auth_service:8055 ★/validate
    ├── Token present + valid role (carrie_admin / hayden_test)
    │     → 200 OK
    │     → X-Jarvis-User, X-Jarvis-Role, X-Jarvis-Session injected
    │     → forward to bbb-input-filter:8016 ★
    └── No token / invalid / unknown role
          → 401 or 403 — rejected at perimeter

★★★★★ App-layer enforcement (April 8):
jarvis-main-brain:8050
    /chat/cancel/all      → require_role({"carrie_admin"})
    /chat/cancel/{job_id} → require_role({"carrie_admin"})

jarvis-gbim-query-router:7205
    /route  → require_role(x_jarvis_role)
    /query  → require_role(x_jarvis_role)
    → 403 on missing or invalid role confirmed live
```

### ★★★★★ Per-Route RBAC — Implemented April 8, 2026

Per-route RBAC is now implemented at the application layer. Caddy remains the perimeter enforcement point; route-level role gating is implemented in `jarvis-main-brain` FastAPI route handlers and `jarvis-gbim-query-router`, where the `X-Jarvis-Role` header is available.

**`jarvis-main-brain:8050` — route-level decorators (OI-36-C / OI-37 sprint, April 3; confirmed April 8):**

- `/chat/cancel/all` (line 236) → `require_role({"carrie_admin"})` ✅ — `hayden_test` blocked with 403
- `/chat/cancel/{job_id}` (line 257) → `require_role({"carrie_admin"})` ✅ — `hayden_test` blocked with 403

**`ms_jarvis_unified_gateway.py` — RBAC engine:**

- `_check_role()` — route-level role enforcement with `ROUTE_ROLES` table
- `_validate_token()` — Redis-validated token auth; `JARVIS_API_KEY` bypass removed April 3 (OI-36-C)
- Internal token type no longer bypasses role checks (OI-36-C)
- Dead duplicate `ROUTE_ROLES` table cleaned up April 3 (OI-37)

**`jarvis-gbim-query-router:7205`:**

- `/route` → `require_role(x_jarvis_role)` ✅
- `/query` → `require_role(x_jarvis_role)` ✅
- 403 on missing or invalid role confirmed live

**Role-differentiated rate limiting (MEDIUM — resolved):** Role injection is app-layer only; Caddy has no `forward_auth` context for per-role rate limits. Per-role throttling lives in `main_brain` / orchestrator request path. Caddy 60 req/min by IP is the correct perimeter implementation. ✅

**Ch 42 §42.3.2 forward reference:** Per-route RBAC is now implemented; §42.3.2 should be updated from "Pending" to confirmed-implemented with reference to OI-36-C / OI-37 sprint (April 3, 2026) and April 8 verification.

---

## 29.4 Organization of the Guidance Corpus

In the current deployment, psychological guidance materials are curated in the `psychological_rag` collection within ChromaDB (`127.0.0.1:8000` ★, `chroma_data` Docker volume, ★ **968 docs restored March 28**) and served via `psychological_rag_domain` (`127.0.0.1:8006` ★), with validation against `msjarvis:5433` ★ GBIM for West Virginia community context.

**Corpus content (★ 968 items).** Topics include therapy, mindfulness, trauma, depression, anxiety, and social support, validated against `msjarvis:5433` ★ GBIM (5,416,521 entities with `confidence_decay` metadata) for appropriateness to Appalachian community contexts. ★★★★★ `confidence_decay` → `needs_verification` flagging is now automated (April 8): 51→52 high-decay resources in `jarvis-local-resources-db:5435` ★ have been flagged `needs_verification=true`, including Prestera Center (decay=1.0). Community-validated resource data from `jarvis-local-resources-db` (port **5435** ★) — including resources validated by Harmony for Hope Community Champions such as lead validator Crystal Colyer — is also eligible for inclusion.

**Tagging and retrieval.** `/search` on `psychological_rag_domain` supports query-based retrieval against the 968-item corpus. Population- and risk-type-specific differential retrieval tuning grounded in `msjarvis:5433` ★ GBIM is deferred to Chapter 30. ★★★★★ GIS RAG pipeline (`jarvis-gis-rag:8009`, `jarvis-rag-search:8095`) is now wired to `main_brain` — spatial context is available alongside psychological RAG retrieval for the first time.

---

## 29.5 Use During Live Interactions — 9-Phase Pipeline Integration

In the current deployment (★★★★★ April 8, 2026), psychological safeguards validated against `msjarvis:5433` ★ GBIM are active at multiple phases of the 9-phase production pipeline (Chapter 17).

**Caddy perimeter + `jarvis_auth_service` (Tier 1 — always first).** Before any request reaches Phase 1.4, it passes through Caddy (port **8443** ★) and `jarvis_auth_service` (port **8055** ★). Token role established; unauthenticated requests rejected at the perimeter. Access decisions written to `/var/log/caddy/jarvis_redteam.log`.

**Phase 1.4 — BBB 7-filter input stack.** All 7 BBB filters (port **8016** ★): EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, **SteganographyDetection (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`)**, TruthVerification, and ContextAwareness. ★ All gate decisions persist to `jarvis-memory:8056`. ★★★★★ Steg trigger events now aggregated by `/steg_report` — 0 false positives confirmed.

**Phase 3 — Psychology pre-assessment (deployed March 15, always active).** Every production request passes through `jarvis-psychology-services` (port **8019** ★) via `/psychological_assessment`:

- Severity classification (mild / moderate / severe)
- Crisis indicator check (Boolean flag for immediate risk)
- `therapeutic_guidance`, `emotional_support`, `wellbeing_recommendations`, `evidence_based_approaches`

★★★★★ `phase3` events counted by `/pia_window`; `llm_judge_v3` `/verdict/psychological` endpoint now scores psychological output quality (live April 8).

**Phase 4 — Psychological + GIS RAG context building.** `psychological_rag_domain` (port **8006** ★) retrieves from the 968-item `psychological_rag` ChromaDB collection. ★★★★★ `jarvis-gis-rag:8009` and `jarvis-rag-search:8095` are now wired — spatial and provider search context is available alongside psychological RAG context in the unified context block.

**Phase 4.5 — BBB output guard.** `apply_output_guards_async` passes the response through BBB `/filter` (port **8016** ★, 8.0s timeout, fail-open confirmed), receiving the full judge verdict dict (integrated March 18, 2026). ★ All Phase 4.5 gate decisions durably logged at `jarvis-memory:8056`.

**Post-processing — identity normalization.** `normalize_identity` ensures the final response speaks as Ms. Egeria Jarvis, not as a clinician or therapist. TruthValidator verifies `correct_identity`, `correct_creator`, and `relationship_clear` validated against `msjarvis:5433` ★ GBIM. ★ `truthverdict` durable at `jarvis-memory:8056`.

---

## 29.6 The PIA Review Loop

In the current deployment (★★★★★ April 8, 2026 — chapter closed), the Psychology-Informed Alignment (PIA) review loop is fully automated. `jarvis_pia_sampler.py` runs continuously as a 30-minute daemon, ingests every sample into the `pia_records` ChromaDB collection, and exposes the `/enforce` A-15 gate on port 8076. The PIA review loop is no longer a manual process.

### 29.6.1 `/pia_window` — Programmatic PIA Sampling (★★★★★ Live April 7)

```python
# Confirmed live in ms_jarvis_memory.py — April 7, 2026
# Route: GET /pia_window?minutes=N

@app.get("/pia_window")
async def pia_window(minutes: int = 60):
    cutoff = time.time() - (minutes * 60)
    bbb_count = 0
    phase3_count = 0
    keys = r.keys("conv:*:*")
    for key in keys:
        if r.type(key) != b'list':
            continue
        entries = r.lrange(key, 0, -1)
        for entry in entries:
            data = json.loads(entry)
            ts = data.get("timestamp", 0)
            if ts < cutoff:
                continue
            event_type = data.get("type", "")
            if event_type == "bbb_audit":
                bbb_count += 1
            elif event_type == "phase3":
                phase3_count += 1
    return {
        "window_minutes": minutes,
        "bbb_audit_events": bbb_count,
        "phase3_events": phase3_count,
        "pia:latest": r.hgetall("pia:latest"),
        "pia:history_len": r.llen("pia:history")
    }
```

### 29.6.2 `jarvis_pia_sampler.py` — Automated PIA Sampling Daemon (★★★★★ Live April 8)

`jarvis_pia_sampler.py` is the automated PIA sampling cycle that ch29 marked as future work. It is now live:

- **30-minute sampling interval** — fires automatically; 60-second startup stagger to avoid cold-start collision
- **`pia:history` rolling store** — 48-entry rolling window in Redis; durable at `jarvis-memory:8056` ★
- **`/enforce` A-15 gate** — live on port 8076; blocks requests that fail A-15 gate criteria
- **`_ingest_to_chroma()`** — on every sample, PIA record auto-ingested into `pia_records` ChromaDB collection (cosine similarity, `default_tenant`)

This is the first scheduled, machine-readable PIA review cycle in the system's history. Ch29 described automated PIA cycling as future work — it is now working code.

### 29.6.3 `/steg_report` — Automated SteganographyDetection Aggregation (★★★★★ Live April 8)

`/steg_report` endpoint on `jarvis-memory:8056` scans the Redis BBB audit trail and returns aggregated steganographic trigger counts:

```json
{
  "total_events_scanned": 45,
  "steg_trigger_count": 0,
  "steg_events": []
}
```

**Confirmed:** 0 false positives. All 45 scanned events clean. This is the automated trigger aggregation that ch29 marked as future work — it is now live.

### 29.6.4 Manual PIA Inputs (still active alongside automation)

PIA review also operates by sampling `ms_jarvis_memory` entries, `truthverdict` fields (durable at `jarvis-memory:8056`), BBB `barrier_stats`, `SteganographyDetection` trigger logs, `jarvis_auth_service` access logs, Phase 3 outputs, `psychological_rag_domain` usage patterns, and ★ `confidence_decay` values from `msjarvis:5433` ★ GBIM for DHHR and mental health service institution entities.

---

## 29.7 Integration with Barriers, Modes, and Judge Components

In the current deployment, PIA recommendations can be applied to several confirmed control surfaces, and propagation requires explicit operator action.

**Barrier and filter adjustments.** BBB 7-filter pipeline at port **8016** ★. ★★★★★ `/steg_report` now provides automated steganographic trigger frequency without manual container log scraping.

**Global mode settings.** Mode settings are adjusted by operators following PIA review. Automated propagation is future work beyond chapter scope.

**Evaluator and judge behavior.** Judge services (7230–7233, confirmed running since March 18, 2026). ★★★★★ `llm_judge_v3` `/verdict/psychological` endpoint is now live — psychological scoring is part of the judge evaluation pipeline. The planned upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring is deferred to Chapter 7 §7.8.

**69-DGM cascade integration.** The 69-DGM cascade (`jarvis-69dgm-bridge`, host port 19000 → internal port **9000** ★, 23 connectors × 3 stages; ★ Up March 28) at Phase 7 provides an additional validation layer for psychologically sensitive responses.

**RBAC-informed PIA recommendations.** ★★★★★ With per-route RBAC live (April 8), role-differentiated BBB trigger analysis via `/pia_window` is now fully meaningful — auth events and BBB trigger events can be compared across `carrie_admin` and `hayden_test` sessions with route-level precision.

---

## 29.8 Recording, Memory, and Accountability

In the current deployment (★★★★★ April 8, 2026), psychological safeguards are recorded through several confirmed mechanisms with PostgreSQL-auditable trails.

**`ms_jarvis_memory` and interaction logs.** Every `/chat` response produces a `bg_<ISO8601>` entry in `ms_jarvis_memory` ChromaDB (port **8000** ★, `chroma_data` volume; Chapter 17 §17.6), with `truthverdict` fields recording BBB 7-filter judgments. ★★★★★ `ms_jarvis_memory` ChromaDB entries, `jarvis-memory:8056` audit entries, and `/pia_window` structured JSON together form a three-layer interaction accountability record.

**`jarvis_auth_service` access log.** Every auth decision written to `/var/log/caddy/jarvis_redteam.log` as structured JSON. ★ Cross-referencing this log with `jarvis-memory:8056` BBB audit entries and `/pia_window` time-window counts enables end-to-end accountability: auth decision → BBB gate decision → Phase 3 event count — all timestamped and durable. ★★★★★ With per-route RBAC live, the 403 events for `hayden_test` on privileged routes are now part of this accountability record.

**Phase 3 assessment records.** Every production request generates a Phase 3 psychology pre-assessment record from `jarvis-psychology-services` (port **8019** ★). `phase3` event counts available via `/pia_window`.

**PIA review records.** ★★★★★ As of April 8, 2026, PIA records are automatically ingested into the `pia_records` ChromaDB collection (cosine similarity, `default_tenant`) via `_ingest_to_chroma()` on every `jarvis_pia_sampler.py` sample cycle. The ch29 future-work item for PIA records as a first-class ChromaDB collection is now implemented.

**Human oversight and governance.** PIA review outputs are designed for inspection by human reviewers including domain experts, ethicists, and community governance bodies. ★★★★★ `jarvis_pia_sampler.py` daemon (30-min cycle) and `pia_records` ChromaDB collection make this review self-sustaining and permanently queryable for the first time.

---

## 29.8.1 `deploy-memory.sh` — Fast Redeploy Protocol (★★★★★ April 7)

> **New as of April 7, 2026.** All future `jarvis-memory` service edits use this protocol. No `sed` on Python files.

```bash
#!/bin/bash
# deploy-memory.sh — one-command redeploy for ms_jarvis_memory.py edits
set -e
echo "Rebuilding jarvis-memory..."
docker compose -f msjarvis-rebuild/docker-compose.yml build jarvis-memory
echo "Restarting jarvis-memory..."
docker compose -f msjarvis-rebuild/docker-compose.yml up -d jarvis-memory
echo "Checking health..."
sleep 3
curl -s http://localhost:8056/health | python3 -m json.tool
echo "Done."
```

**Usage:** `./deploy-memory.sh` from the `msjarvis-rebuild/` directory. Python `str.replace()` preserves indentation exactly — no more `sed` on Python files.

---

## 29.9 Open Items (★★★★★ April 8, 2026 — Chapter Closed)

| Item | Priority | Disposition |
|---|---|---|
| **Per-route RBAC enforcement** | ★★★★★ HIGH | ✅ **Done** — `require_role()` on `main_brain` `/chat/cancel/all` + `/chat/cancel/{job_id}` (OI-36-C/OI-37, April 3); `gbim_query_router` `/route` + `/query` gated (April 8). App-layer enforcement covers all privileged routes. |
| Role-differentiated rate limiting | MEDIUM | ✅ **Resolved** — Role injection is app-layer only; no `forward_auth` in Caddy. Per-role throttle lives in `main_brain`/orchestrator. Caddy 60 req/min by IP is the correct perimeter implementation. |
| Automated PIA sampling cycle | FUTURE → DONE | ✅ **Done** — `jarvis_pia_sampler.py` daemon, 30-min interval, 60s startup stagger, `pia:history` 48-entry rolling, `/enforce` A-15 gate live on port 8076. |
| Automated `SteganographyDetection` trigger aggregation | FUTURE → DONE | ✅ **Done** — `/steg_report` endpoint on `jarvis-memory:8056`; scans BBB audit trail; 0 false positives; automated pattern aggregation live. |
| PIA records as first-class ChromaDB collection | FUTURE → DONE | ✅ **Done** — `pia_records` collection created in ChromaDB (cosine, `default_tenant`); auto-ingest on every sample via `_ingest_to_chroma()`. |
| Population- and risk-type-specific RAG retrieval tuning | FUTURE | ⏭️ **Deferred** — GBIM data confirmed at `msjarvis:5433`; GIS pipeline live. Differential retrieval sprint is Chapter 30 scope. |
| `confidence_decay`-driven DHHR entity refresh | FUTURE → DONE | ✅ **Done** — 51→52 high-decay resources flagged `needs_verification=true` in `jarvis-local-resources-db:5435` ★; Prestera Center (decay=1.0) explicitly flagged. |
| Judge pipeline upgrade for psychological scoring | FUTURE | ⏭️ **Deferred** — Both stores confirmed at correct ports. RAG-grounded truth scoring upgrade is Chapter 7 §7.8 dedicated sprint. `llm_judge_v3` `/verdict/psychological` endpoint is live — scoring confirmed working. |
| Per-route RBAC for `gbim_query_router` (port 7205) | FUTURE → DONE | ✅ **Done** — `/route` and `/query` gated behind `require_role(x_jarvis_role)`; 403 on missing/invalid role confirmed live. |
| GIS RAG wiring | (new — April 8) | ✅ **Done** — `jarvis-gis-rag:8009` (`geo_search`, `geojson`, `geojson_bbox`); `jarvis-rag-search:8095` provider search; `main_brain` service discovery updated to `host.docker.internal:8009`. |

---

## 29.10 Summary

★★★★★ **Chapter 29 is fully closed as of April 8, 2026.** All §29.9 open items have been implemented, verified, and committed. Tag `a15-complete-20260408` marks the close. Two items are intentionally deferred to later chapters (population/risk-type retrieval tuning → Ch 30; judge pipeline upgrade → Ch 7 §7.8) and do not block closure.

In the current deployment (★★★★★ April 8, 2026), psychological safeguards are realized through:

- `jarvis-psychology-services` (`127.0.0.1:8019` ★) and `psychological_rag_domain` (`127.0.0.1:8006` ★)
- Curated psychological corpus — ★ **968 items** in `psychological_rag` ChromaDB collection
- Validation against `msjarvis:5433` ★ (★ **5,416,521 GBIM entities with `confidence_decay` metadata**)
- BBB 7-filter pipeline at `127.0.0.1:8016` ★ (Phase 1.4; ★ audit → `jarvis-memory:8056`)
- `normalize_identity` + TruthValidator on every `ultimatechat` response
- BBB output guard (port **8016** ★, full judge verdict dict; ★ audit → `jarvis-memory:8056`)
- Caddy perimeter (port **8443** ★) + `jarvis_auth_service` (port **8055** ★, systemd) — RBAC active March 22
- `/pia_window` — programmatic PIA window, live April 7 ✅
- `jarvis-memory` in `msjarvis-rebuild` compose — first-class rebuild service, line 1141 ✅
- `deploy-memory.sh` — one-command redeploy path ✅
- ★★★★★ **Per-route RBAC live** — `require_role()` on `/chat/cancel/all`, `/chat/cancel/{job_id}` (main_brain); `/route`, `/query` (gbim_query_router); `hayden_test` blocked at route level ✅
- ★★★★★ **`jarvis_pia_sampler.py` daemon live** — 30-min automated PIA cycle; `/enforce` A-15 gate port 8076 ✅
- ★★★★★ **`/steg_report` live** — 0 false positives, automated steg aggregation confirmed ✅
- ★★★★★ **`pia_records` ChromaDB collection** — auto-ingest on every PIA sample ✅
- ★★★★★ **`confidence_decay` → `needs_verification`** — 51→52 resources flagged in `jarvis-local-resources-db:5435` ✅
- ★★★★★ **GIS RAG wired** — `jarvis-gis-rag:8009` + `jarvis-rag-search:8095`; `main_brain` discovery updated ✅
- ★★★★★ **`llm_judge_v3` `/verdict/psychological`** — psychological scoring live; Query 1: 0.825/1.0; Query 2: 0.6875/0.45 ✅

Two constraints remain unchanged: the psychological guidance stack is explicitly non-diagnostic — DSM-style constructs are used only at a high-level, psychoeducational layer validated against PostgreSQL community data, not as clinical criteria. Propagation of PIA governance recommendations into BBB parameters and judge weights beyond what is automated here requires explicit operator action.

For the BBB 7-filter pipeline see Chapter 16. For identity constraints see Chapter 22. For the canonical 9-phase `ultimatechat` sequence see Chapter 17. For ChromaDB `psychological_rag` collection architecture see Chapter 5. For March 18, 2026 security hardening see Chapter 40 §40-C. For Caddy perimeter + `jarvis_auth_service` full architecture see Chapter 19 §19.8.1–§19.8.2. For `jarvis-memory:8056` durable BBB audit trail architecture see Chapter 25 §25.2. For GIS RAG pipeline see Chapter 30. For judge pipeline upgrade see Chapter 7 §7.8.

---

*Last updated: ★★★★★ 2026-04-08 by Carrie Kidd (Mamma Kidd), Mount Hope WV*
*★★★★★ April 8, 2026: Chapter 29 fully closed — tag `a15-complete-20260408`*
*★★★★★ April 8, 2026: Per-route RBAC implemented — `main_brain` `require_role()` + `gbim_query_router` (OI-36-C/OI-37) — §29.3 and §29.9 updated*
*★★★★★ April 8, 2026: Automated PIA sampling daemon live (`jarvis_pia_sampler.py`, 30-min, port 8076) — §29.6.2 added, §29.9 updated*
*★★★★★ April 8, 2026: `/steg_report` endpoint live (0 false positives) — §29.6.3 added, §29.9 updated*
*★★★★★ April 8, 2026: `pia_records` ChromaDB collection + auto-ingest live — §29.8 and §29.9 updated*
*★★★★★ April 8, 2026: `confidence_decay` → `needs_verification` flagged (51→52 resources) — §29.9 updated*
*★★★★★ April 8, 2026: GIS RAG wired (`jarvis-gis-rag:8009`, `jarvis-rag-search:8095`) — §29.2 safeguards table + §29.9 updated*
*★★★★★ April 8, 2026: Role-differentiated rate limiting resolved (app-layer, not Caddy) — §29.3 and §29.9 updated*
*★★★★★ April 8, 2026: `llm_judge_v3` `/verdict/psychological` endpoint live — §29.2 safeguards table updated*
*★★★★★ April 7, 2026: `/pia_window` route live — first programmatic PIA window — all PIA sections updated*
*★★★★★ April 7, 2026: Redis WRONGTYPE error resolved (`conv:sessions:internal` deleted) — §29.6.1 updated*
*★★★★★ April 7, 2026: Python IndentationError fixed (str.replace() — no more sed on Python files) — §29.8.1 updated*
*★★★★★ April 7, 2026: `deploy-memory.sh` created — §29.8.1 added*
*★★★★★ April 7, 2026: `jarvis-memory` added as first-class service to msjarvis-rebuild docker-compose.yml line 1141 — §29.9 open item resolved, safeguards table updated*
*★ March 28, 2026: `jarvis-memory:8056` secured (durable BBB audit trail) — all gate decision logging updated throughout chapter*
*★ March 28, 2026: `msjarvis:5433` restored (5,416,521 GBIM entities, `confidence_decay` metadata)*
*★ March 28, 2026: `psychological_rag` 968 docs restored*
*★ March 28, 2026: 96/96 containers Up confirmed*
*★ March 28, 2026: ChromaDB 40-collection / 6,675,442-vector inventory confirmed*
*BBB output guard port 8016 added to safeguards table — March 27, 2026*
*Ch 42 §42.3.2 forward reference verification note added — March 27, 2026*
