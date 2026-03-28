# 29. Psychological Safeguards and the PIA Review Loop

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: 2026-03-28 — ★ March 28, 2026: 96/96 containers Up — zero Restarting, zero Exited; `msjarvis` port 5433 restored (5,416,521 GBIM entities with `confidence_decay` metadata); `msjarvisgis` port 5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids); ChromaDB full audit (★ **40 active collections, 6,675,442 total vectors**); `psychological_rag` restored (968 docs); `spiritual_rag` deduplicated (−19,338 vectors); `msjarvis_docs` expanded (4,192 items, AAPCAppE); `jarvis-ingest-api` + `jarvis-ingest-watcher` restored to active inventory; `jarvis-memory` port 8056 corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set, BBB audit trail persistence secured; LLM ensemble confirmed 22 proxies registered / 21 active; consciousness pipeline confirmed Up. March 27, 2026: BBB output guard port 8016 added to safeguards table; Ch 42 §42.3.2 forward reference verification note added; `jarvis-spiritual-rag` port 8005 verification note added; `gbim_query_router` port 7205 verification note added.*

---

## Why This Matters for Polymathmatic Geography

This chapter formalizes how psychological and mental-health knowledge is integrated into Ms. Jarvis to guide interaction patterns, monitor interaction risks, and adapt system behavior over time, all grounded in PostgreSQL: `msjarvis` (port **5433** ★, **5,416,521 GBIM entities** with `confidence_decay` metadata), `msjarvisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids), and `jarvis-local-resources-db` (port **5435** ★, community resources). It supports:

- **P1 – Every where is entangled** by ensuring that psychological safeguards are woven into the same retrieval, filtering, and memory infrastructure anchored to PostgreSQL that handles spatial and technical content, not isolated in a separate silo.
- **P3 – Power has a geometry** by making psychological constraints visible as named services, tagged collections, PostgreSQL-validated rules, and explicit endpoints rather than hiding them in opaque model behavior. ★ BBB gate decisions are now durably logged at `jarvis-memory:8056` (secured March 28) — the geometry of psychological safety enforcement is now persistently auditable.
- **P5 – Design is a geographic act** by tailoring psychological guidance to populations and risk types specific to Appalachian communities grounded in `msjarvis:5433` ★ GBIM — rural grief, economic stress, identity disruption — rather than generic global corpora.
- **P12 – Intelligence with a ZIP code** by grounding psychological RAG retrieval in collections that include place-specific and community-specific mental health materials validated against PostgreSQL West Virginia institutional knowledge. ★ `msjarvis_docs` (4,192 items, AAPCAppE) and `psychological_rag` (968 docs, restored March 28) now constitute a strengthened ZIP-coded psychological guidance substrate.
- **P16 – Power accountable to place** by logging PIA review cycle outputs, recording recommendations and observed patterns in PostgreSQL-auditable format, and making this material available for human oversight and community governance review. ★ `jarvis-memory:8056` (secured March 28) provides the durable authenticated foundation for this accountability.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the psychological safeguard services, guidance corpus, and PIA review loop that protect interaction quality and mental-health alignment in Ms. Jarvis's operation, all anchored to the three-database PostgreSQL architecture. The `jarvis-psychology-services` (port **8019** ★) and `psychological_rag_domain` (port **8006** ★) services were deployed and confirmed operational March 15, 2026 (commit b90f9ff), contributing to the verified 349.87s end-to-end 9-phase pipeline benchmark. The steganography filter (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`) is confirmed active in the BBB 7-filter stack as of March 21, 2026. ★ As of March 28, 2026: `psychological_rag` collection restored to 968 docs and all 96/96 containers Up — the psychological safeguard infrastructure operates at its widest confirmed scope.

---

```
┌─────────────────────────────────────────────────────────────┐
│   Psychological Safeguards Architecture                     │
│   (★ Updated: March 28, 2026 — 96/96 containers Up)        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Request → Caddy Perimeter (8443, HTTPS)               │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Caddy forward_auth → jarvis_auth_service      │         │
│  │  (port 8055 ★, systemd-managed)                │         │
│  │  Role: carrie_admin — full access              │         │
│  │  Role: hayden_test  — internal test role       │         │
│  │  Enforced at: Caddy perimeter (not yet at      │         │
│  │  route level — OPEN ITEM: per-route RBAC)      │         │
│  └────────────────────────────────────────────────┘         │
│      ↓ (authenticated, X-Jarvis-Role injected)              │
│  jarvis-main-brain (8050 ★)                                 │
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
│  │  │  ★ 968 items restored March 28:          │  │         │
│  │  │  therapy, mindfulness, trauma,           │  │         │
│  │  │  depression, anxiety, social support     │  │         │
│  │  │  (validated vs msjarvis:5433 ★ GBIM)     │  │         │
│  │  └──────────────────────────────────────────┘  │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Response Processing                                        │
│  -  truthverdict (from BBB + msjarvis:5433 ★ validation)    │
│    ★ audit → jarvis-memory:8056 (secured Mar 28)            │
│  -  consciousnesslayers (psych assessment layer included)    │
│  -  background_rag_store → ms_jarvis_memory (ChromaDB ★)    │
│    ★ 40 collections, 6,675,442 total vectors               │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  PIA Review Loop (Manual Process)             │         │
│  │  ────────────────────────────────────         │         │
│  │  Inputs (manually sampled):                    │         │
│  │  -  ms_jarvis_memory entries (ChromaDB ★)       │         │
│  │  -  truthverdict fields                         │         │
│  │    ★ audit at jarvis-memory:8056               │         │
│  │  -  BBB barrier_stats (★ now durable at 8056)  │         │
│  │  -  Psychology service outputs                  │         │
│  │  -  SteganographyDetection trigger logs         │         │
│  │    (zero_width_homoglyph_structural_v1)        │         │
│  │  -  jarvis_auth_service access logs             │         │
│  │    (role: carrie_admin, hayden_test)           │         │
│  │  -  confidence_decay values (msjarvis:5433 ★)  │         │
│  │    for psych resource GBIM entities            │         │
│  │                                                 │         │
│  │  Analysis:                                      │         │
│  │  -  Recurring truthverdict violations           │         │
│  │  -  BBB 7-filter block-rate trends              │         │
│  │  -  Identity-confusion patterns                 │         │
│  │  -  Steganographic injection attempt patterns   │         │
│  │  -  Underuse of psychological guidance          │         │
│  │  -  Role-differentiated interaction patterns    │         │
│  │    (carrie_admin vs hayden_test)               │         │
│  │  -  confidence_decay trends in psych GBIM ★    │         │
│  │                                                 │         │
│  │  Outputs (written recommendations):            │         │
│  │  -  BBB parameter adjustments                   │         │
│  │  -  Judge instruction updates                   │         │
│  │  -  Mode policy refinements                     │         │
│  │  -  Guidance corpus additions (PostgreSQL-      │         │
│  │    validated for WV community context)         │         │
│  │  -  RBAC route-level policy proposals           │         │
│  │    (current: perimeter-only enforcement)       │         │
│  │  -  confidence_decay remediation proposals ★   │         │
│  │    (DHHR / mental health service entities)     │         │
│  │                                                 │         │
│  │  Operator Action Required for Implementation   │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Accountability                                             │
│  -  ★ jarvis-memory:8056 durable BBB audit log              │
│    (secured March 28 — auth confirmed)                     │
│  -  PostgreSQL-auditable PIA records                         │
│  -  BBB barrier_stats logged (all 7 filters)                 │
│  -  jarvis_auth_service access log → /var/log/caddy/         │
│    jarvis_redteam.log (role field per entry)               │
│  -  Community governance review                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 29.1.** Psychological safeguards architecture (★ March 28, 2026 — 96/96 containers Up): Caddy perimeter (port 8443) with `forward_auth` enforcing role-based access control via `jarvis_auth_service` (port **8055** ★, systemd) is the outermost layer — token roles `carrie_admin` (full access) and `hayden_test` (internal test role) are enforced at the perimeter; per-route RBAC is an open item. The BBB 7-filter pipeline and TruthValidator validated against `msjarvis:5433` ★ (5,416,521 GBIM entities with `confidence_decay` metadata) provide the primary safety gate on every authenticated request (Phase 1.4); ★ all BBB and `truthverdict` decisions now persist to `jarvis-memory:8056` (secured March 28); `SteganographyDetection` (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`) confirmed active March 21 as a structural integrity safeguard against adversarial payload injection; psychological services (Phase 3, deployed March 15 — active on every production request) offer severity classification, crisis indicator check, and evidence-based guidance backed by ★ `psychological_rag` (968 docs, restored March 28); manual PIA review loop samples logs including steganography trigger events, role-access patterns, and ★ `confidence_decay` values for GBIM psychological resource entities, producing written recommendations requiring operator action; all accountability records ★ now durably logged at `jarvis-memory:8056` and PostgreSQL-auditable for community governance review.

---

## Status as of ★ March 28, 2026

| Category | Details |
|---|---|
| **Implemented and verified** | `jarvis-psychology-services` confirmed running at `127.0.0.1:8019` ★ (deployed March 15, commit b90f9ff). Exposes `/psychological_assessment` accepting a query and returning structured fields: `psychological_assessment`, `therapeutic_guidance`, `emotional_support`, `wellbeing_recommendations`, `evidence_based_approaches`. Phase 3 psychology pre-assessment is active on every production 9-phase pipeline request (Chapter 17), including severity classification and crisis indicator check — confirmed in 349.87s end-to-end benchmark. `psychological_rag_domain` confirmed running at `127.0.0.1:8006` ★ (port corrected from 9006 to 8006 as of March 15 containerized deployment). Exposes `/search` and `/add_document` for a curated psychological corpus (★ **968 items restored March 28**: therapy, mindfulness, trauma, depression, anxiety, social support). ChromaDB `psychological_rag` collection ★ confirmed restored (port **8000** ★, `chroma_data` Docker volume, ★ within 40-collection / 6,675,442-vector inventory confirmed March 28 full audit). PostgreSQL `msjarvis` at `127.0.0.1:5433` ★ (★ **5,416,521 GBIM entities with `confidence_decay` metadata**, restored March 28) as ground truth for validating psychological guidance against West Virginia community context — `confidence_decay` metadata now available for DHHR and mental health service entity recency assessment in PIA review. BBB 7-filter pipeline at `127.0.0.1:8016` ★ (all services re-locked to `127.0.0.1`, March 18, 2026): EthicalFilter, SpiritualFilter, SafetyMonitor (word-boundary regex fixed March 15), ThreatDetection, **SteganographyDetection (`zero_width_homoglyph_structural_v1`, `confidence: 1.0` — confirmed active March 21, 2026)**, TruthVerification, ContextAwareness. ★ **All BBB and `TruthFilterBBBValidator` gate decisions now persist to `jarvis-memory:8056`** (corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set, secured March 28) — filter/block/violation counters are now backed by a durable, authenticated audit log. `normalize_identity` and TruthValidator enforce prohibitions on anthropomorphic claims and identity confusion validated against `msjarvis:5433` ★ GBIM on every `ultimatechat` response. `truthverdict` attached to every UltimateResponse with `correct_identity`, `correct_creator`, `relationship_clear` booleans. **Caddy perimeter (port 8443) with `jarvis_auth_service` (port 8055 ★, systemd-managed) enforcing token-based RBAC — confirmed active March 22, 2026; ★ confirmed Up March 28.** Red-team token roles confirmed: `carrie_admin` (full access), `hayden_test` (internal test role). ★ **96/96 containers Up — zero Restarting, zero Exited** as of March 28, 2026 — widest confirmed psychological safeguard operational scope. |
| **Partially implemented / scaffolded** | PIA review loop exists as a structured process that manually samples logs and introspection outputs, producing written recommendations — it does not auto-rewrite configuration, prompts, or filters. Integration of PIA recommendations back into barrier parameters, judge weights, or mode settings requires explicit operator action. Psychological-guidance-specific `consciousnesslayers` entries appear when `jarvis-psychology-services` is explicitly invoked; they are now consistently produced at Phase 3 of the 9-phase pipeline. Population- and risk-type-specific retrieval tagging (e.g. rural grief, adolescent caregivers) is partially implemented; differential retrieval tuning grounded in `msjarvis:5433` ★ GBIM West Virginia data is future work. Steganographic trigger event logging is active but automated aggregation into PIA pattern reports is future work. **RBAC is enforced at the Caddy perimeter only** — per-route role enforcement (e.g. restricting `/chat_async` or `/chat_cancel_all` by role) is an open item. ★ `confidence_decay` metadata on `msjarvis:5433` ★ GBIM entities is now available for PIA DHHR and mental health service entity recency assessment — integration into automated PIA sampling is partial. |
| **Future work / design intent only** | Automated, scheduled PIA review cycle with machine-readable output format for direct configuration integration. Automated propagation of PIA recommendations into BBB penalty weights, judge instructions, and global mode policies without manual operator step. Persistent introspective log of PIA cycle inputs, analyses, and recommendations as a first-class ChromaDB collection with PostgreSQL audit trail (★ `jarvis-memory:8056` now provides the durable foundation for this). Population- and risk-type-specific retrieval tuning driving differential guidance validated against `msjarvis:5433` ★ GBIM West Virginia community data. Automated aggregation of `SteganographyDetection` trigger events into PIA pattern analysis reports. **Per-route RBAC enforcement at the application layer** (currently perimeter-only). Role-differentiated rate limiting (e.g. tighter limits for `hayden_test` vs `carrie_admin`). ★ Judge pipeline upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring querying `msjarvis:5433` ★ (5,416,521 entities with `confidence_decay`) — would strengthen psychological safeguard scoring in the 69-DGM cascade; upgrade sprint pending. |

Cross-reference: The BBB 7-filter pipeline that enforces safety and ethical constraints validated against PostgreSQL is described in Chapter 16. Identity normalization and TruthValidator validated against `msjarvis:5433` ★ GBIM are described in Chapter 22. The psychological services' relationship to the meaning-oriented track is described in Chapter 23. For the canonical 9-phase `ultimatechat` execution sequence see Chapter 17. For ChromaDB `psychological_rag` collection architecture (★ 968 docs, restored March 28; within 40-collection / 6,675,442-vector inventory) see Chapter 5. For the March 18, 2026 security hardening that re-locked all services to `127.0.0.1` and integrated the full verdict dict into the BBB output guard see Chapter 40 §40-C. For the Caddy perimeter layer and `jarvis_auth_service` full architecture see Chapter 19 §19.8.1–§19.8.2. ★ For `jarvis-memory:8056` durable BBB audit trail architecture see Chapter 25 §25.2.

---

## 29. Psychological Safeguards and the PIA Review Loop

This chapter formalizes how psychological and mental-health knowledge is integrated into Ms. Jarvis to guide interaction patterns, monitor interaction risks, and adapt system behavior over time. In the current deployment (★ March 28, 2026), this is realized through two confirmed running services — `jarvis-psychology-services` (port **8019** ★, deployed March 15) and `psychological_rag_domain` (port **8006** ★, containerized March 15) — a curated psychological corpus in ChromaDB (★ **968 items restored March 28**, `psychological_rag` collection, port **8000** ★, `chroma_data` volume; within ★ 40-collection / 6,675,442-vector inventory), validation against PostgreSQL `msjarvis` (port **5433** ★, ★ **5,416,521 GBIM entities with `confidence_decay` metadata**, restored March 28) for West Virginia community context, the BBB 7-filter pipeline at `127.0.0.1:8016` ★ as the primary live Phase 1.4 safety gate (★ audit → `jarvis-memory:8056` secured March 28), and a manual PIA review process that produces recommendations rather than automated rewrites.

**New as of March 22, 2026:** All external `/chat*` traffic now passes through the Caddy perimeter layer (port **8443** ★) with `forward_auth` enforcing token-based role-based access control via `jarvis_auth_service` (port **8055** ★, systemd-managed) before reaching any internal service. Two red-team token roles are active: `carrie_admin` (full access) and `hayden_test` (internal test role). RBAC is currently enforced at the Caddy perimeter only; per-route enforcement is an open item documented in §29.8 and in the open items table.

★ **New as of March 28, 2026:** `jarvis-memory:8056` (corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set) is secured as the durable BBB audit trail store — all BBB and `TruthFilterBBBValidator` gate decisions are now persistently logged. `msjarvis:5433` ★ restored to 5,416,521 GBIM entities with `confidence_decay` metadata — this enables graded recency assessment of psychological resource entities in GBIM for PIA review. All 96/96 containers Up — the psychological safeguard infrastructure operates at its widest confirmed scope.

Phase 3 psychology pre-assessment is active on every production 9-phase pipeline request (confirmed March 15, 2026, 349.87s end-to-end benchmark, all phases approved). Prior to March 15, `jarvis-psychology-services` was unavailable due to missing container builds and the missing ChromaDB `chroma_data` volume. Both services are now confirmed operational. ★ `psychological_rag` (968 docs) confirmed restored March 28 as part of the 40-collection ChromaDB audit.

A critical constraint is that these mechanisms are designed for supportive, psychoeducational guidance and risk awareness validated against PostgreSQL community data, not for formal DSM-style diagnosis or clinical decision-making. Clinical constructs are used at a high level only; the system does not reproduce or implement DSM-5 in full and is not a substitute for professional care.

---

## 29.1 Role of Psychological Guidance

In the current deployment, psychological guidance grounded in `msjarvis:5433` ★ GBIM is not treated as an auxiliary feature but as a core constraint on how the system interacts with people, enforced at Phase 3 of every production 9-phase pipeline request. Its primary functions are threefold.

**Interaction quality.** `jarvis-psychology-services` (port **8019** ★) provides principled reference points for respectful, non-coercive, and supportive exchanges validated against `msjarvis:5433` ★ GBIM (5,416,521 entities with `confidence_decay` metadata) West Virginia community norms. Its `/psychological_assessment` endpoint runs on every production request and returns structured responses: `therapeutic_guidance`, `emotional_support`, `wellbeing_recommendations`, and `evidence_based_approaches`. `psychological_rag_domain` (port **8006** ★) provides retrieval of curated materials — therapy, mindfulness, trauma, depression, anxiety, and social-support content (★ **968 items restored March 28**) — via `/search`, backed by the ChromaDB `psychological_rag` collection (port **8000** ★, `chroma_data` volume; within ★ 40-collection / 6,675,442-vector inventory). These materials are curated for high-level, evidence-informed guidance validated against PostgreSQL community context; they are not used to perform formal diagnosis.

**Risk awareness.** TruthValidator (applied on every response via `jarvis-main-brain`, port **8050** ★) encodes patterns known to be harmful — identity confusion, anthropomorphic overclaiming, misleading statements about agency and embodiment — validated against `msjarvis:5433` ★ GBIM (★ 5,416,521 entities with `confidence_decay` metadata) and returns `correct_identity`, `correct_creator`, and `relationship_clear` booleans. ★ All `truthverdict` decisions are now durably logged at `jarvis-memory:8056` (secured March 28). The BBB 7-filter Phase 1.4 stack at port **8016** ★ screens for content violating ethical or community-safety constraints including high-risk mental-health content. The SafetyMonitor word-boundary regex fix deployed March 15 eliminates false-positives on community resource terms while maintaining protection for genuine risk patterns.

**Structural integrity assurance.** The `SteganographyDetection` filter (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`, confirmed active March 21, 2026) screens every request for adversarial payloads embedded via zero-width characters, homoglyph substitution, and structural encoding tricks. Within the psychological safeguards framework, this filter is classified as a psychological integrity assurance (PIA) safeguard: adversarial steganographic injection is a known vector for manipulating AI system behavior in ways that could undermine therapeutic boundaries, safety constraints, or identity normalization — including attempts to override the non-diagnostic constraint or suppress crisis-flag detection. ★ All `SteganographyDetection` trigger events are now durably logged at `jarvis-memory:8056` (secured March 28) alongside other BBB gate decisions — confirming this filter's decisions are persistently auditable for the first time. Confirming this filter active at `confidence: 1.0` closes a structural gap in the PIA framework that previously relied on human-visible content review alone.

**Self-checking.** `normalize_identity` applied to every `ultimatechat` response rewrites outputs that deviate from allowed self-descriptions validated against `msjarvis:5433` ★ GBIM (5,416,521 entities with `confidence_decay` metadata) or blur human-machine boundaries, before the response is returned to the caller. Together with the BBB 7-filter pipeline, this prevents the system from presenting itself as a clinician, therapist, or human agent.

---

## 29.2 Confirmed Active Safeguards (★ March 28, 2026)

The following table records all confirmed active psychological safeguards as of ★ March 28, 2026 (updated from March 22, 2026 baseline). This table is the authoritative reference for PIA review scope and regression testing in Chapter 41 §41.4.1.

| Safeguard | Service / Location | Confirmed | Notes |
|---|---|---|---|
| Caddy perimeter RBAC | Caddy (port 8443 ★) + `jarvis_auth_service` (port 8055 ★) | ✅ March 22 / ★ Up March 28 | `carrie_admin` (full access), `hayden_test` (internal test role); perimeter-level enforcement; per-route RBAC is OPEN ITEM |
| EthicalFilter | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| SpiritualFilter | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| SafetyMonitor | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | Word-boundary regex fix March 15; no false-positives on community resource terms; ★ audit → `jarvis-memory:8056` |
| ThreatDetection | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| **SteganographyDetection** | **BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★)** | **✅ March 21 / ★ Up March 28** | **`zero_width_homoglyph_structural_v1`, `confidence: 1.0` — PIA structural integrity safeguard; ★ trigger events now durable at `jarvis-memory:8056`** |
| TruthVerification | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| ContextAwareness | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| TruthValidator | `jarvis-main-brain:8050` ★ post-processing | ✅ March 15 / ★ Up March 28 | `correct_identity`, `correct_creator`, `relationship_clear` validated vs `msjarvis:5433` ★ GBIM (5,416,521 entities, `confidence_decay` metadata); ★ `truthverdict` durable at `jarvis-memory:8056` |
| `normalize_identity` | `jarvis-main-brain:8050` ★ post-processing | ✅ March 15 / ★ Up March 28 | Every `ultimatechat` response |
| Phase 3 psychology pre-assessment | `jarvis-psychology-services:8019` ★ | ✅ March 15 / ★ Up March 28 | Severity classification + crisis indicator on every request |
| Psychological RAG retrieval | `psychological_rag_domain:8006` ★ | ✅ March 15 / ★ **968 docs restored March 28** | ★ 968-item corpus restored March 28; query-based retrieval; within ★ 40-collection / 6,675,442-vector inventory |
| BBB output guard | BBB Phase 4.5 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 18 / ★ Up March 28 | Full verdict dict received (not answer text only); `apply_output_guards_async` 8.0s timeout; ★ audit → `jarvis-memory:8056` |
| ★ BBB durable audit trail | `jarvis-memory:8056` | ★ ✅ **March 28** | **Port corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set — all BBB and `TruthFilterBBBValidator` decisions now durably logged** |

---

## 29.3 Red-Team Token Roles and RBAC (NEW — March 22, 2026; ★ confirmed Up March 28)

Role-based access control for red-team and administrative access is enforced at the Caddy perimeter layer via `jarvis_auth_service` (port **8055** ★, systemd-managed). All `/chat*` route traffic passes through `forward_auth` before reaching any internal service.

### Active Token Roles

| Role | Access Level | Notes |
|---|---|---|
| `carrie_admin` | Full access | All `/chat*` routes; no rate-limit overrides applied at role level (Caddy rate limits still apply per-IP) |
| `hayden_test` | Internal test role | All `/chat*` routes; intended for red-team and regression testing sessions; same perimeter enforcement as `carrie_admin` |

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
          → 401 or 403
          → rejected at perimeter
          → no internal service reached
```

`jarvis_auth_service` writes each auth decision (timestamp, client IP, role, decision) to `/var/log/caddy/jarvis_redteam.log` (structured JSON, same file as Caddy access log). This log is the primary input for PIA review of role-differentiated access patterns. ★ `jarvis-memory:8056` (secured March 28) provides a complementary durable store for BBB gate decisions that occur downstream of auth — together, these two logs provide end-to-end accountability from perimeter auth through content filter.

### Open Item: Per-Route RBAC

**RBAC is currently enforced at the Caddy perimeter only.** Once a token is validated and a role is established, all `/chat*` routes are reachable regardless of role. Per-route enforcement — for example, restricting `/chat_cancel_all` to `carrie_admin` only, or limiting `hayden_test` to read-only endpoints — is **not yet implemented**.

This is logged as an open item for the following reasons:

- The `X-Jarvis-Role` header is injected by `jarvis_auth_service` and forwarded to `bbb-input-filter:8016` ★ on every authenticated request, making the role available to internal services for future enforcement.
- `jarvis-main-brain` does not currently inspect `X-Jarvis-Role` to gate individual route access.
- Route-level enforcement will require changes to `jarvis-main-brain` FastAPI route handlers or a Caddy route-matchers configuration update.

**Resolution path:** Add route-level `forward_auth` matchers in the Caddyfile that return 403 for `hayden_test` on destructive or privileged endpoints (`/chat_cancel_all`, `/chat_cancel/{job_id}`, any future admin endpoints). Document confirmed enforcement in **Chapter 42 §42.3.2** when complete.

> **⚠️ Forward reference note:** Verify that Ch 42 (Post-Quantum Security Layer) contains a §42.3.2 placeholder or section for per-route RBAC enforcement documentation. If §42.3.2 does not yet exist, add a stub section in Ch 42 with the heading "Per-Route RBAC Enforcement (Pending)" so this forward reference does not break. If the section is located at a different subsection number, update this cross-reference accordingly.

---

## 29.4 Organization of the Guidance Corpus

In the current deployment, psychological guidance materials are curated in the `psychological_rag` collection within ChromaDB (`127.0.0.1:8000` ★, `chroma_data` Docker volume, ★ **968 docs restored March 28**; within ★ 40-collection / 6,675,442-vector inventory) and served via `psychological_rag_domain` (`127.0.0.1:8006` ★, confirmed running March 15; ★ confirmed Up March 28), with validation against `msjarvis:5433` ★ GBIM for West Virginia community context.

**Corpus content (★ 968 items restored March 28).** `psychological_rag_domain` holds a curated corpus on topics including therapy, mindfulness, trauma, depression, anxiety, and social support, validated against `msjarvis:5433` ★ GBIM (5,416,521 entities with `confidence_decay` metadata) for appropriateness to Appalachian community contexts. `jarvis-psychology-services` uses this corpus to identify patterns such as anxiety, depression, stress, grief, and trauma, pulling evidence-based snippets via RAG to generate structured responses. ★ The `confidence_decay` metadata on `msjarvis:5433` ★ GBIM entities representing DHHR and mental health service institutions is now available for PIA corpus curation: entities with high `confidence_decay` (lower evidentiary confidence) are candidates for targeted corpus refresh or `needs_verification` flagging. The corpus is logically distinct from general reference and technical knowledge, making its normative and clinical role explicit and allowing it to be governed and updated separately with PostgreSQL validation. Community-validated resource data from `jarvis-local-resources-db` (port **5435** ★) — including resources validated by Harmony for Hope Community Champions such as lead validator Crystal Colyer — is also eligible for inclusion in the psychological guidance corpus where relevant to Appalachian mental health support. Where DSM-style constructs appear, they do so at the level of paraphrased, high-level concepts rather than verbatim manual text.

**Tagging and retrieval.** The design intends that items will be tagged with theme (e.g. "trauma-informed care," "addictive dynamics"), population (e.g. adolescents, caregivers, rural Appalachian communities from `msjarvis:5433` ★ GBIM), and risk type (e.g. self-harm risk, identity confusion, dependency, adversarial manipulation) to support targeted retrieval validated against PostgreSQL community data. In the current deployment, tagging is partially implemented; `/search` on `psychological_rag_domain` supports query-based retrieval against the ★ 968-item corpus, and population- and risk-type-specific differential retrieval tuning grounded in `msjarvis:5433` ★ GBIM West Virginia data is identified as future work.

---

## 29.5 Use During Live Interactions — 9-Phase Pipeline Integration

In the current deployment (★ March 28, 2026), psychological safeguards validated against `msjarvis:5433` ★ GBIM are active at multiple phases of the 9-phase production pipeline (Chapter 17). ★ All 96/96 containers Up — every phase of the pipeline operates at full confirmed scope.

**Caddy perimeter + `jarvis_auth_service` (Tier 1 — always first).** Before any request reaches Phase 1.4 or any internal service, it passes through Caddy (port **8443** ★) and `jarvis_auth_service` (port **8055** ★). The token role (`carrie_admin` or `hayden_test`) is established here and injected as `X-Jarvis-Role`. Unauthenticated or unrecognized requests are rejected at the perimeter — no internal service is reached. Access decisions are written to `/var/log/caddy/jarvis_redteam.log`.

**Phase 1.4 — BBB 7-filter input stack.** Before any content reaches the psychological assessment or LLM synthesis phases, the request passes through all 7 BBB filters (port **8016** ★): EthicalFilter, SpiritualFilter, SafetyMonitor (word-boundary regex fixed March 15), ThreatDetection, **SteganographyDetection (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`, confirmed active March 21)**, TruthVerification, and ContextAwareness. This is the primary live gate for psychologically sensitive content, validated against `msjarvis:5433` ★ GBIM ground truth (5,416,521 entities with `confidence_decay` metadata). ★ All gate decisions from Phase 1.4 now persist to `jarvis-memory:8056` (secured March 28). The steganography filter's role within PIA is to ensure that adversarially encoded inputs — which could otherwise bypass human-readable content review — are intercepted before they can influence Phase 3 severity classification, crisis flag detection, or identity normalization.

**Phase 3 — Psychology pre-assessment (deployed March 15, always active; ★ confirmed Up March 28).** Every production request passes through `jarvis-psychology-services` (port **8019** ★) via `/psychological_assessment`. This service provides:

- Severity classification (mild / moderate / severe)
- Crisis indicator check (Boolean flag for immediate risk)
- `therapeutic_guidance`: evidence-based approaches relevant to detected patterns
- `emotional_support`: supportive language recommendations
- `wellbeing_recommendations`: actionable, non-diagnostic suggestions
- `evidence_based_approaches`: specific evidence-informed frameworks

Phase 3 output feeds the LM Synthesizer (Phase 3.5, internal port 8001), which incorporates psychological context alongside `msjarvis:5433` ★ GBIM RAG, `msjarvisgis:5432` ★ PostGIS spatial data, and community resource data from `jarvis-local-resources-db:5435` ★ before passing enriched context to the ★ 22-registered / 21-active LLM ensemble (Phase 2.5).

**Phase 4 — Psychological RAG context building.** `jarvis-spiritual-rag` (port **8005** ★ — cross-reference Ch 01 container mapping to verify this port was not renumbered during March hardening; if renumbered, update this reference) queries `psychological_rag_domain` (port **8006** ★) as one of its RAG sources during Phase 4 context building, retrieving relevant entries from the ★ 968-item `psychological_rag` ChromaDB collection (port **8000** ★; within ★ 40-collection / 6,675,442-vector inventory). This psychological RAG context is combined with GBIM beliefs (`msjarvis:5433` ★, 5,416,521 entities with `confidence_decay` metadata), PostGIS spatial data (`msjarvisgis:5432` ★, 91 GB PostGIS, 501 tables, 993 ZCTA centroids), and community resources (`jarvis-local-resources-db:5435` ★) into the unified context block.

**Phase 4.5 — BBB output guard.** After the ★ 22-registered / 21-active LLM ensemble and 69-DGM cascade, `apply_output_guards_async` passes the response through BBB `/filter` (port **8016** ★, 8.0s timeout, fail-open behavior confirmed), receiving and evaluating the full judge verdict dict (integrated March 18, 2026) rather than answer text only. ★ All Phase 4.5 gate decisions are now durably logged at `jarvis-memory:8056` (secured March 28). This ensures psychologically sensitive generated content is evaluated against all 7 filters including steganographic structure checks before delivery.

**Post-processing — identity normalization.** `normalize_identity` ensures the final response speaks as Ms. Egeria Jarvis, not as a clinician or therapist. TruthValidator verifies `correct_identity`, `correct_creator`, and `relationship_clear` booleans validated against `msjarvis:5433` ★ GBIM (5,416,521 entities with `confidence_decay` metadata). ★ `truthverdict` durable at `jarvis-memory:8056`.

---

## 29.6 The PIA Review Loop

In the current deployment, the Psychology-Informed Alignment (PIA) review loop exists as a structured manual process that samples logs and introspection outputs validated against `msjarvis:5433` ★ GBIM, producing written recommendations — not auto-rewrites of configuration, prompts, or filters.

**Inputs and scope.** PIA review operates by manually sampling:

- Recent interaction logs and `ms_jarvis_memory` entries (ChromaDB, confirmed written after every `/chat` call via `background_rag_store`; Chapter 17 §17.6; within ★ 40-collection / 6,675,442-vector inventory)
- `truthverdict` fields from UltimateResponse (`correct_identity`, `correct_creator`, `relationship_clear`) validated against `msjarvis:5433` ★ GBIM; ★ now durable at `jarvis-memory:8056`
- BBB `barrier_stats` counters (`total_filtered`, `total_blocked`, `pass_rate`) from the 7-filter pipeline, including per-filter trigger rates; ★ now durable at `jarvis-memory:8056`
- **`SteganographyDetection` trigger logs** — events where `zero_width_homoglyph_structural_v1` flagged content at `confidence: 1.0`, including input payload patterns and trigger frequency; ★ now durable at `jarvis-memory:8056`
- **`jarvis_auth_service` access logs** — `/var/log/caddy/jarvis_redteam.log` entries showing role (`carrie_admin`, `hayden_test`), timestamp, and auth decision, for role-differentiated interaction pattern analysis
- Phase 3 outputs from `jarvis-psychology-services` (severity classifications, crisis flags; ★ port **8019** ★, confirmed Up March 28)
- `psychological_rag_domain` `/search` usage patterns against the ★ 968-item corpus
- ★ **`confidence_decay` values from `msjarvis:5433` ★ GBIM** (5,416,521 entities) for DHHR and mental health service institution entities underlying psychological resource recommendations — high-decay entities are PIA flags for corpus refresh

Automated, scheduled sampling and automated aggregation of `SteganographyDetection` trigger events into PIA pattern reports are identified as future work. ★ `jarvis-memory:8056` (secured March 28) now provides the durable foundation for future automated sampling of BBB gate decisions — manual PIA sampling from ephemeral container logs is no longer the only path.

**Analysis.** The PIA review examines recurring patterns in system behavior validated against `msjarvis:5433` ★ GBIM — recurring `truthverdict` violations, BBB 7-filter block-rate trends, identity-confusion patterns in TruthValidator outputs, adversarial steganographic injection attempt patterns (newly confirmable as of March 21; ★ now durably logged at `jarvis-memory:8056`), underuse of psychological guidance in sensitive interaction categories, crisis indicator detection rates from Phase 3, role-differentiated access patterns from `jarvis_redteam.log` (e.g. whether `hayden_test` sessions surface different safeguard trigger patterns than `carrie_admin` sessions), and ★ **`confidence_decay` trend analysis for GBIM entities representing DHHR and mental health service institutions** — entities with rising `confidence_decay` are candidates for targeted `needs_verification` review in `jarvis-local-resources-db:5435` ★. Some classification of patterns is still heuristic; fully automated pattern-detection is identified as future work. Clinical frameworks such as DSM-style nosology inform human reviewers' judgments at this stage but are not implemented as automatic diagnostic pipelines.

**Outputs and recommendations.** The PIA review loop produces structured written recommendations such as:

- "Tighten identity phrasing constraints validated against PostgreSQL in crisis-related dialogues"
- "Introduce explicit boundary statements for maternal metaphors"
- "Increase Phase 3 severity threshold for economic-stress queries common in Appalachian community contexts"
- "Add to `psychological_rag` corpus: rural grief resources validated against Fayette County community data from `jarvis-local-resources-db:5435` ★"
- "Review `confidence_decay` for DHHR mental health service entities (currently `needs_verification=TRUE`) — `msjarvis:5433` ★ entities with high decay score identified via PIA sampling from `jarvis-memory:8056` ★"
- "Audit `SteganographyDetection` trigger log at `jarvis-memory:8056` ★ for recurring payload patterns that may indicate targeted adversarial probing of the psychological safeguard boundary"
- "Implement per-route RBAC to restrict `/chat_cancel_all` and destructive endpoints to `carrie_admin` only — current perimeter-only enforcement does not prevent `hayden_test` from reaching these routes"

These are human-interpretable and require explicit operator action to implement — they do not automatically rewrite BBB parameters, judge instructions, or global mode policies. Machine-readable output format and automated propagation are identified as future work.

---

## 29.7 Integration with Barriers, Modes, and Judge Components

In the current deployment, PIA recommendations can be applied to several confirmed control surfaces validated against `msjarvis:5433` ★ GBIM, but application requires explicit operator action.

**Barrier and filter adjustments.** BBB 7-filter pipeline at port **8016** ★ exposes rule sets validated against `msjarvis:5433` ★ GBIM that can be updated in response to PIA findings. The SafetyMonitor word-boundary regex fix deployed March 15 is an example of a PIA-informed adjustment. The `SteganographyDetection` filter (`zero_width_homoglyph_structural_v1`) is not a newly added safeguard — it was part of the BBB design — but its confirmed active status at `confidence: 1.0` (March 21, 2026) is the first verification that it is functioning as specified within the PIA framework. ★ With `jarvis-memory:8056` (secured March 28) now logging all BBB decisions durably, PIA review can now include steganographic trigger frequency from a persistent, queryable log rather than ephemeral container state alone. In the current deployment, updates to filter parameters validated against PostgreSQL remain manual.

**Global mode settings.** The design intends that PIA outputs will modify mode selection policies validated against `msjarvis:5433` ★ GBIM — for instance, enforcing more cautious orchestration modes for certain user cohorts or topics if recent behavior indicates elevated psychological risk or elevated steganographic trigger rates. In the current deployment, mode settings are adjusted by operators following PIA review rather than by automated policy updates.

**Evaluator and judge behavior.** Judge services (7230–7233, confirmed running and compose-managed since March 18, 2026; ★ confirmed Up March 28) can receive updated instructions reflecting refined psychological guidance validated against `msjarvis:5433` ★ GBIM — for example, stronger penalties for overconfident advice in clinical domains or for failure to recommend professional help when appropriate. In the current deployment, these updates are applied manually following PIA recommendations. ★ The planned judge pipeline upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring querying `msjarvis:5433` ★ (5,416,521 entities with `confidence_decay`) would strengthen psychological safeguard scoring in judge evaluations (Chapter 7 §7.8); both stores confirmed at correct ports as of March 28, upgrade sprint pending. The design intends that future configurations will give judges direct access to `psychological_rag_domain` outputs (★ 968-item corpus) validated against PostgreSQL and PIA summaries as explicit scoring dimensions.

**69-DGM cascade integration.** The 69-DGM cascade (`jarvis-69dgm-bridge`, host port 19000 → internal port **9000** ★, 23 connectors × 3 stages; ★ confirmed Up March 28) at Phase 7 provides an additional validation layer for psychologically sensitive responses. 69-DGM verdicts are architecturally authoritative and grounded in `msjarvis:5433` ★ GBIM beliefs (5,416,521 entities with `confidence_decay` metadata); future PIA recommendations may target specific DGM connector configurations relevant to psychological safety, including connectors that evaluate structural encoding anomalies downstream of the steganography filter.

**RBAC-informed PIA recommendations.** As role-differentiated access log data accumulates in `/var/log/caddy/jarvis_redteam.log`, PIA review will be able to compare safeguard trigger rates across `carrie_admin` and `hayden_test` sessions. Persistent differences in trigger rates may indicate that the test role is surfacing prompts or interaction patterns that stress psychological safeguard boundaries differently from operator sessions — a signal that per-route RBAC or role-differentiated rate limiting should be prioritized. ★ `jarvis-memory:8056` (secured March 28) enables cross-referencing `jarvis_redteam.log` auth events with BBB gate decisions by timestamp — role-differentiated BBB trigger analysis is now feasible as a PIA input for the first time.

---

## 29.8 Recording, Memory, and Accountability

In the current deployment, psychological safeguards are recorded through several confirmed mechanisms with PostgreSQL-auditable trails. ★ As of March 28, 2026: `jarvis-memory:8056` (secured) adds a new durable, authenticated accountability layer across all mechanisms below.

**`ms_jarvis_memory` and interaction logs.** Every `/chat` response produces a `bg_<ISO8601>` entry in `ms_jarvis_memory` ChromaDB (port **8000** ★, `chroma_data` volume; within ★ 40-collection / 6,675,442-vector inventory; Chapter 17 §17.6), with `truthverdict` fields recording BBB 7-filter judgments validated against `msjarvis:5433` ★ GBIM including ethics violations and crisis flag triggers. These entries are the primary raw material for PIA sampling. BBB `barrier_stats` counters provide aggregate counts of filter interventions across all 7 filters, including those triggered by psychologically sensitive content and those triggered by `SteganographyDetection` (`zero_width_homoglyph_structural_v1`). ★ All underlying gate decisions are now additionally logged at `jarvis-memory:8056` — `ms_jarvis_memory` ChromaDB entries and `jarvis-memory:8056` audit entries together form a two-layer interaction accountability record.

**`jarvis_auth_service` access log.** Every auth decision made by `jarvis_auth_service` (port **8055** ★) is written to `/var/log/caddy/jarvis_redteam.log` as structured JSON. Each entry includes: timestamp, client IP, role (`carrie_admin` / `hayden_test` / unknown), auth decision (pass / reject), and HTTP status code returned to Caddy. This log is a PIA input for detecting anomalous access patterns, high-frequency rejection events (potential brute-force), or role-correlated safeguard trigger patterns. ★ Cross-referencing this log with `jarvis-memory:8056` BBB audit entries enables end-to-end accountability: auth decision → BBB gate decision → `truthverdict` — all timestamped and durable.

**Phase 3 assessment records.** Every production request generates a Phase 3 psychology pre-assessment record from `jarvis-psychology-services` (port **8019** ★) — severity classification, crisis indicator Boolean, and five structured guidance fields. These records are included in `consciousnesslayers` of the UltimateResponse and are available for PIA sampling. The March 15 deployment means this is the first date from which a complete longitudinal Phase 3 assessment record exists.

**PIA review records.** Each manual PIA review cycle produces a written record of inputs sampled, patterns observed validated against `msjarvis:5433` ★ GBIM (5,416,521 entities with `confidence_decay` metadata), and recommendations proposed. The design intends these records will be written into a dedicated ChromaDB collection (within ★ 40-collection / 6,675,442-vector inventory) as timestamped introspective artifacts tagged as `psychological-alignment` entries with PostgreSQL audit trail. ★ `jarvis-memory:8056` (secured March 28) provides the durable authenticated audit store that will anchor this ChromaDB collection to a tamper-evident record of gate decisions. In the current deployment, these records are maintained as manually produced documents rather than automatically ingested into ChromaDB.

**Human oversight and governance.** PIA review outputs are explicitly designed for inspection by human reviewers including domain experts, ethicists, and community governance bodies, with all validations traceable to `msjarvis:5433` ★ GBIM ground truth (5,416,521 entities with `confidence_decay` metadata). This material supports questions such as: "Has the system systematically improved in handling crisis-adjacent queries?", "Where have psychological safeguards validated against PostgreSQL been relaxed or tightened?", "Do the recorded mitigations align with declared community norms anchored in `msjarvis:5433` ★ GBIM?", "Are DHHR and mental health service entities in `jarvis-local-resources-db:5435` ★ being confirmed through the POC verification loop promptly?", "Is the steganographic trigger rate at `jarvis-memory:8056` ★ consistent with incidental encoding artifacts or indicative of targeted probing?", and "Does the `hayden_test` access pattern reveal interaction types that should inform per-route RBAC design?" The design treats psychological risk as a first-class governance concern, on par with technical reliability and knowledge integrity. DSM-style frameworks inform human oversight here as reference points, but automated behavior remains conservative and non-diagnostic.

---

## 29.9 Open Items (★ March 28, 2026)

| Item | Priority | Notes |
|---|---|---|
| **Per-route RBAC enforcement** | HIGH | RBAC currently enforced at Caddy perimeter only. `hayden_test` and `carrie_admin` can both reach all `/chat*` routes once authenticated. Per-route enforcement (restrict `/chat_cancel_all`, `/chat_cancel/{job_id}`, future admin endpoints to `carrie_admin` only) requires `jarvis-main-brain` route handler changes or Caddy route-matcher config. See §29.3. ★ 96/96 containers Up — implementation conditions are fully met; this item should be prioritized in the next sprint. |
| Role-differentiated rate limiting | MEDIUM | Caddy `caddy-ratelimit` module applies per-IP limits; role-differentiated limits (e.g. tighter burst limit for `hayden_test`) are not yet configured. |
| Automated PIA sampling cycle | FUTURE | Scheduled, machine-readable PIA review with direct configuration integration. ★ `jarvis-memory:8056` (secured March 28) provides the durable BBB audit foundation for automated sampling. |
| Automated `SteganographyDetection` trigger aggregation | FUTURE | Automated aggregation of trigger events from `jarvis-memory:8056` ★ into PIA pattern analysis reports. |
| Per-route RBAC for `gbim_query_router` (port **7205** — cross-check against Ch 01 `jarvis-gbim-query-router` container mapping to confirm 7205 is the host-exposed port and was not renumbered in the March hardening session) | FUTURE | Landowner belief queries currently reachable by any authenticated role; access restriction pending production hardening pass. |
| PIA records as first-class ChromaDB collection | FUTURE | Currently maintained as manually produced documents; automated ingest with `jarvis-memory:8056` ★ durable audit trail is future work. |
| Population- and risk-type-specific RAG retrieval tuning | FUTURE | Differential retrieval grounded in `msjarvis:5433` ★ GBIM (5,416,521 entities with `confidence_decay` metadata) West Virginia community data for Appalachian-specific guidance corpus. |
| ★ `confidence_decay`-driven DHHR entity refresh | FUTURE | Automated identification of `msjarvis:5433` ★ GBIM mental health service entities with high `confidence_decay` for targeted `needs_verification` review in `jarvis-local-resources-db:5435` ★. |
| ★ Judge pipeline upgrade for psychological scoring | FUTURE | Upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring querying `msjarvis:5433` ★ — both stores confirmed at correct ports March 28; upgrade sprint pending (Chapter 7 §7.8). |

---

## 29.10 Summary

In the current deployment (★ March 28, 2026), psychological safeguards are realized through two confirmed running services — `jarvis-psychology-services` (`127.0.0.1:8019` ★, deployed March 15) and `psychological_rag_domain` (`127.0.0.1:8006` ★, containerized March 15) — a curated psychological corpus in ChromaDB (`127.0.0.1:8000` ★, `chroma_data` volume, ★ **968 items restored March 28** in `psychological_rag` collection; within ★ 40-collection / 6,675,442-vector inventory), validation against `msjarvis:5433` ★ (★ **5,416,521 GBIM entities with `confidence_decay` metadata**, restored March 28) for West Virginia community context, the BBB 7-filter pipeline at `127.0.0.1:8016` ★ as the primary Phase 1.4 live safety gate (★ audit → `jarvis-memory:8056` secured March 28), `normalize_identity` plus TruthValidator validated against `msjarvis:5433` ★ applied to every `ultimatechat` response, the BBB output guard (port **8016** ★) receiving the full judge verdict dict (integrated March 18, 2026; ★ audit → `jarvis-memory:8056`), and — confirmed as of March 22, 2026 and ★ Up March 28 — the Caddy perimeter layer (port **8443** ★) with `jarvis_auth_service` (port **8055** ★, systemd-managed) enforcing token-based RBAC with two active red-team roles.

Key operational facts as of ★ March 28, 2026:

- ★ **96/96 containers Up** — zero Restarting, zero Exited — widest confirmed psychological safeguard scope
- ★ **`jarvis-memory:8056` secured** — port corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set — all BBB and `TruthFilterBBBValidator` decisions durably logged
- ★ **`msjarvis:5433` restored** — 5,416,521 GBIM entities with `confidence_decay` metadata — graded recency assessment for DHHR/mental health entities now available in PIA
- ★ **`psychological_rag` restored** — 968 docs, confirmed in 40-collection / 6,675,442-vector ChromaDB audit
- **Caddy perimeter RBAC active** — token roles `carrie_admin` (full access) and `hayden_test` (internal test role) enforced via `forward_auth` at port **8443** ★; access decisions logged to `/var/log/caddy/jarvis_redteam.log`
- **Per-route RBAC is an open item** — enforcement is perimeter-only; `hayden_test` can reach all `/chat*` routes once authenticated; route-level restriction is pending (see §29.3 and §29.9); ★ 96/96 Up means implementation conditions are fully met
- Phase 3 psychology pre-assessment is active on every production 9-phase pipeline request (confirmed in 349.87s end-to-end benchmark)
- BBB has 7 confirmed active filters: EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, **SteganographyDetection (`zero_width_homoglyph_structural_v1`, `confidence: 1.0` — confirmed active March 21, 2026)**, TruthVerification, ContextAwareness
- SafetyMonitor word-boundary regex fixed March 15 — eliminates false-positives on community resource terms
- BBB output guard (port **8016** ★) receives full judge verdict dict (not answer text only) — confirmed March 18, 2026
- All BBB services re-locked to `127.0.0.1` — zero `0.0.0.0` exposures — confirmed March 18, 2026
- `psychological_rag_domain` port is 8006 (not 9006 — corrected in March 15 containerized deployment)
- ChromaDB `psychological_rag` collection previously unavailable; ★ now restored (968 docs, March 28) via `chroma_data` Docker volume

Two important constraints must be stated clearly: the PIA review loop produces written recommendations through a manual sampling process validated against PostgreSQL, not auto-rewrites; and propagation of PIA recommendations into BBB parameters, judge weights, or mode policies requires explicit operator action. The psychological guidance stack is explicitly non-diagnostic: it does not implement DSM-5 in full, and any DSM-style constructs are used only at a high-level, psychoeducational layer validated against PostgreSQL community data rather than as clinical criteria.

★ Three new accountability capabilities are active as of March 28, 2026 that were not present in the March 22 baseline:
1. **Durable BBB audit trail** — `jarvis-memory:8056` now stores all gate decisions persistently and authentically; manual sampling from ephemeral container logs is no longer the only PIA input path.
2. **`confidence_decay` metadata on GBIM entities** — `msjarvis:5433` ★ (5,416,521 entities) now exposes graded temporal confidence on DHHR and mental health service entities, enabling prioritized corpus refresh signals in PIA.
3. **Full 40-collection ChromaDB inventory confirmed** — `psychological_rag` (968 docs) and `spiritual_rag` (deduplicated −19,338 vectors) are both confirmed within the 6,675,442-vector inventory, giving PIA review a precise and auditable view of the guidance corpus footprint.

The design intends that future work will: implement per-route RBAC enforcement (highest-priority open item as of March 28, 2026); automate the PIA sampling cycle with `jarvis-memory:8056` ★ durable audit trail as the primary input (including automated aggregation of `SteganographyDetection` trigger events and role-differentiated access pattern analysis); produce machine-readable recommendation outputs for direct configuration integration; persist PIA records as a first-class ChromaDB collection with `jarvis-memory:8056` ★ audit trail for ongoing governance review; complete the judge pipeline upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring querying `msjarvis:5433` ★ (Chapter 7 §7.8); and refine corpus curation and tagging so that place-specific and population-specific mental-health materials grounded in Appalachian contexts via `msjarvis:5433` ★ GBIM are more systematically retrieved while maintaining clear boundaries between supportive guidance and clinical diagnosis.

For the BBB 7-filter pipeline that enforces safety constraints validated against PostgreSQL see Chapter 16. For the identity constraints enforced alongside psychological safeguards validated against PostgreSQL see Chapter 22. For the canonical 9-phase `ultimatechat` execution sequence see Chapter 17. For ChromaDB `psychological_rag` collection architecture (★ 968 docs restored March 28; within 40-collection / 6,675,442-vector inventory) see Chapter 5. For the March 18, 2026 security hardening that re-locked all services to `127.0.0.1` and integrated the full verdict dict into the BBB output guard see Chapter 40 §40-C. For the Caddy perimeter layer and `jarvis_auth_service` full architecture see Chapter 19 §19.8.1–§19.8.2. ★ For `jarvis-memory:8056` durable BBB audit trail architecture see Chapter 25 §25.2.

---

*Last updated: ★ 2026-03-28 by Carrie Kidd (Mamma Kidd), Mount Hope WV*
*★ March 28, 2026: `jarvis-memory:8056` secured (durable BBB audit trail) — all gate decision logging updated throughout chapter*
*★ March 28, 2026: `msjarvis:5433` restored (5,416,521 GBIM entities, `confidence_decay` metadata) — all GBIM references updated*
*★ March 28, 2026: `psychological_rag` 968 docs restored — corpus references updated*
*★ March 28, 2026: 96/96 containers Up confirmed — operational scope updated throughout*
*★ March 28, 2026: ChromaDB 40-collection / 6,675,442-vector inventory confirmed — all collection references updated*
*★ March 28, 2026: `confidence_decay`-driven DHHR entity refresh added to open items (§29.9)*
*★ March 28, 2026: Judge pipeline upgrade for psychological scoring added to open items (§29.9)*
*BBB output guard port 8016 added to safeguards table — March 27, 2026*
*Ch 42 §42.3.2 forward reference verification note added — March 27, 2026*
*`jarvis-spiritual-rag` port 8005 verification note added — March 27, 2026*
*`gbim_query_router` port 7205 verification note added — March 27, 2026*
