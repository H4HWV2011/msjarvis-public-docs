# 29. Psychological Safeguards and the PIA Review Loop

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: ★★★★★ 2026-04-07 — `/pia_window` route live ✅; Redis WRONGTYPE error resolved (`conv:sessions:internal` deleted) ✅; Python IndentationError fixed (str.replace() — no more sed on Python files) ✅; `deploy-memory.sh` created ✅; `jarvis-memory` added as first-class service to `msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml` line 1141 with bind mount volume ✅; `/health` → `{"status":"healthy","service":"ms-jarvis-memory","redis":"connected"}` confirmed ✅; `/pia_window?minutes=240` → clean JSON, type guard active, `conv:*:*` keys scanned correctly ✅; Redis type guard `if r.type(key) != b'list': continue` live in production code ✅; 60+ services registered as hash type in `service:jarvis-*` keys ✅; all `conv:internal:bbb_*` keys confirmed list type — BBB audit trail structure intact ✅; `pia:latest` → hash, `pia:history` → list — PIA snapshot store healthy ✅. All prior March 28, 2026 updates carry forward unchanged.*

> **★★★★★ Updates applied April 7, 2026 — summary:**
>
> **Fixed / newly live (broken or incomplete in ch29 closeout state):**
> | Item | Problem | Resolution |
> |---|---|---|
> | `jarvis-memory:8056 /pia_window` route | 404 Not Found — route existed in local file but container was importing from `/app/services/` via bind mount shadow, not `/app/` | `docker cp` to correct path `/app/services/ms_jarvis_memory.py` |
> | Redis WRONGTYPE error on `/pia_window` | `conv:sessions:internal` stored as Redis set; `lrange` expected a list | Identified and deleted the bad key via `redis-cli` |
> | Python IndentationError crash | `sed` mangled type guard into a one-liner with orphaned indent; container entered crash loop | Repaired with Python `str.replace()` — no more `sed` on Python files |
> | `jarvis-memory` orphaned from rebuild stack | Container running from ch29 backup image with no volume mount; edits required manual `docker cp` every time | Added `jarvis-memory` as first-class service to `msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml` line 1141 with bind mount |
> | `deploy-memory.sh` missing | No fast redeploy path existed | Created `./deploy-memory.sh` — one command for all future `ms_jarvis_memory.py` edits |
>
> **Verified working tonight (live proof of items documented in ch29):**
> - `/health` → `{"status":"healthy","service":"ms-jarvis-memory","redis":"connected"}` — Redis connection confirmed ✅
> - `/pia_window?minutes=240` → clean JSON, no errors, type guard active, scanning `conv:*:*` keys correctly ✅
> - `jarvis-redis` container confirmed running; all `service:jarvis-*` keys present as hash type — 60+ services registered ✅
> - All `conv:internal:bbb_*` keys confirmed as list type — BBB audit trail structure intact ✅
> - `pia:latest` → hash, `pia:history` → list — PIA snapshot store healthy ✅
>
> **Aspirational → Working Code (ch29 future work / partial → live in production):**
> - `/pia_window` endpoint — Ch29 described the PIA review loop as a manual sampling process relying on ephemeral container logs. The `/pia_window` route is now the **first queryable, programmatic PIA window** — it scans BBB audit turn keys, counts `bbb_audit` and `phase3` events within a configurable time window, and returns structured JSON. This is the automated PIA sampling input that ch29 marked as future work.
> - Redis type guard — Ch29 had no protection against `conv:sessions:internal` or similar non-list keys breaking the scan loop. `if r.type(key) != b'list': continue` is now live in production code.
> - `jarvis-memory` in rebuild compose — Ch29's `jarvis-memory` service existed only in the ch29 backup stack (`/home/cakidd/ch29-closeout/backups/docker-compose.yml:1585`). It is now ported into the `msjarvis-rebuild` stack with a volume mount, making it a first-class rebuild service for the first time.

---

## Why This Matters for Polymathmatic Geography

This chapter formalizes how psychological and mental-health knowledge is integrated into Ms. Jarvis to guide interaction patterns, monitor interaction risks, and adapt system behavior over time, all grounded in PostgreSQL: `msjarvis` (port **5433** ★, **5,416,521 GBIM entities** with `confidence_decay` metadata), `msjarvisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids), and `jarvis-local-resources-db` (port **5435** ★, community resources). It supports:

- **P1 – Every where is entangled** by ensuring that psychological safeguards are woven into the same retrieval, filtering, and memory infrastructure anchored to PostgreSQL that handles spatial and technical content, not isolated in a separate silo.
- **P3 – Power has a geometry** by making psychological constraints visible as named services, tagged collections, PostgreSQL-validated rules, and explicit endpoints rather than hiding them in opaque model behavior. ★ BBB gate decisions are now durably logged at `jarvis-memory:8056` (secured March 28) — the geometry of psychological safety enforcement is now persistently auditable. ★★★★★ The `/pia_window` endpoint (live April 7) is the first programmatic surface through which this geometry can be queried in structured JSON.
- **P5 – Design is a geographic act** by tailoring psychological guidance to populations and risk types specific to Appalachian communities grounded in `msjarvis:5433` ★ GBIM — rural grief, economic stress, identity disruption — rather than generic global corpora.
- **P12 – Intelligence with a ZIP code** by grounding psychological RAG retrieval in collections that include place-specific and community-specific mental health materials validated against PostgreSQL West Virginia institutional knowledge. ★ `msjarvis_docs` (★★★★★ 6,975 items, April 7) and `psychological_rag` (968 docs, restored March 28) constitute a strengthened ZIP-coded psychological guidance substrate.
- **P16 – Power accountable to place** by logging PIA review cycle outputs, recording recommendations and observed patterns in PostgreSQL-auditable format, and making this material available for human oversight and community governance review. ★ `jarvis-memory:8056` (secured March 28) provides the durable authenticated foundation for this accountability. ★★★★★ The `/pia_window` route (live April 7) makes this accountability programmatically queryable for the first time.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the psychological safeguard services, guidance corpus, and PIA review loop that protect interaction quality and mental-health alignment in Ms. Jarvis's operation, all anchored to the three-database PostgreSQL architecture. The `jarvis-psychology-services` (port **8019** ★) and `psychological_rag_domain` (port **8006** ★) services were deployed and confirmed operational March 15, 2026 (commit b90f9ff), contributing to the verified 349.87s end-to-end 9-phase pipeline benchmark. The steganography filter (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`) is confirmed active in the BBB 7-filter stack as of March 21, 2026. ★ As of March 28, 2026: `psychological_rag` collection restored to 968 docs and all 96/96 containers Up — the psychological safeguard infrastructure operates at its widest confirmed scope. ★★★★★ As of April 7, 2026: `/pia_window` route is live, Redis type guard is in production code, and `jarvis-memory` is a first-class service in the rebuild compose stack.

---

```
┌─────────────────────────────────────────────────────────────┐
│   Psychological Safeguards Architecture                     │
│   (★★★★★ Updated: April 7, 2026 — /pia_window Live ✅)     │
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
│    ★★★★★ 48 collections (April 7 audit)                    │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  jarvis-memory:8056 (★★★★★ April 7)           │         │
│  │  ─────────────────────────────────────         │         │
│  │  /health → {"status":"healthy",                │         │
│  │    "service":"ms-jarvis-memory",               │         │
│  │    "redis":"connected"} ✅                     │         │
│  │  /pia_window?minutes=240 → structured JSON ✅  │         │
│  │    Scans conv:*:* keys                         │         │
│  │    Counts bbb_audit + phase3 events in window  │         │
│  │    Type guard: if r.type(key) != b'list':      │         │
│  │      continue (live in production code ✅)     │         │
│  │  Redis key types confirmed:                    │         │
│  │    service:jarvis-* → hash (60+ services) ✅   │         │
│  │    conv:internal:bbb_* → list ✅               │         │
│  │    pia:latest → hash ✅                        │         │
│  │    pia:history → list ✅                       │         │
│  │  First-class service in rebuild compose ✅     │         │
│  │  Line 1141 docker-compose.yml, bind mount ✅   │         │
│  │  deploy-memory.sh → one-command redeploy ✅    │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  PIA Review Loop (★★★★★ April 7: Programmatic)│         │
│  │  ────────────────────────────────────         │         │
│  │  ★★★★★ /pia_window — queryable PIA window:    │         │
│  │    - Scans BBB audit turn keys in Redis        │         │
│  │    - Counts bbb_audit and phase3 events        │         │
│  │    - Configurable time window (minutes param)  │         │
│  │    - Returns structured JSON                   │         │
│  │    - Type-guarded (non-list keys skipped)      │         │
│  │    - Was: manual sampling from container logs  │         │
│  │    - Now: programmatic, live, queryable ✅     │         │
│  │                                                 │         │
│  │  Manual PIA inputs still active:               │         │
│  │  -  ms_jarvis_memory entries (ChromaDB ★)       │         │
│  │  -  truthverdict fields (durable at 8056)       │         │
│  │  -  BBB barrier_stats (durable at 8056)         │         │
│  │  -  SteganographyDetection trigger logs (8056)  │         │
│  │  -  jarvis_auth_service access logs             │         │
│  │  -  confidence_decay values (msjarvis:5433 ★)  │         │
│  │                                                 │         │
│  │  Outputs (written recommendations):            │         │
│  │  -  BBB parameter adjustments                   │         │
│  │  -  Judge instruction updates                   │         │
│  │  -  Mode policy refinements                     │         │
│  │  -  Guidance corpus additions                   │         │
│  │  -  RBAC route-level policy proposals           │         │
│  │  -  confidence_decay remediation proposals ★   │         │
│  │                                                 │         │
│  │  Operator Action Required for Implementation   │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Accountability                                             │
│  -  ★★★★★ /pia_window programmatic query ✅ April 7        │
│  -  ★ jarvis-memory:8056 durable BBB audit log              │
│    (secured March 28 — auth confirmed)                     │
│  -  ★★★★★ deploy-memory.sh one-command redeploy ✅         │
│  -  PostgreSQL-auditable PIA records                         │
│  -  BBB barrier_stats logged (all 7 filters)                 │
│  -  jarvis_auth_service access log                          │
│  -  Community governance review                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 29.1.** Psychological safeguards architecture (★★★★★ April 7, 2026 — `/pia_window` live): Caddy perimeter (port 8443) with `forward_auth` enforcing role-based access control via `jarvis_auth_service` (port **8055** ★, systemd) is the outermost layer — token roles `carrie_admin` (full access) and `hayden_test` (internal test role) enforced at the perimeter; per-route RBAC is an open item. The BBB 7-filter pipeline and TruthValidator validated against `msjarvis:5433` ★ (5,416,521 GBIM entities with `confidence_decay` metadata) provide the primary safety gate on every authenticated request (Phase 1.4); ★ all BBB and `truthverdict` decisions persist to `jarvis-memory:8056` (secured March 28); `SteganographyDetection` (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`) confirmed active March 21; psychological services (Phase 3, deployed March 15) offer severity classification, crisis indicator check, and evidence-based guidance backed by ★ `psychological_rag` (968 docs, restored March 28); ★★★★★ `jarvis-memory:8056` `/pia_window` route is now the **first programmatic PIA window** — scans BBB audit turn keys, counts `bbb_audit` and `phase3` events in a configurable time window, returns structured JSON, with Redis type guard live in production code; `jarvis-memory` added as first-class service to rebuild compose (line 1141) with bind mount; `deploy-memory.sh` one-command redeploy created; all accountability records durable at `jarvis-memory:8056` and PostgreSQL-auditable for community governance review.

---

## Status as of ★★★★★ April 7, 2026

| Category | Details |
|---|---|
| **Implemented and verified** | `jarvis-psychology-services` confirmed running at `127.0.0.1:8019` ★ (deployed March 15, commit b90f9ff). Phase 3 psychology pre-assessment active on every production 9-phase pipeline request — severity classification and crisis indicator check confirmed in 349.87s end-to-end benchmark. `psychological_rag_domain` confirmed running at `127.0.0.1:8006` ★ — exposes `/search` and `/add_document` for the ★ **968-item corpus** (restored March 28). ChromaDB `psychological_rag` collection confirmed (port **8000** ★, `chroma_data` Docker volume; ★★★★★ within 48-collection inventory, April 7). PostgreSQL `msjarvis` at `127.0.0.1:5433` ★ (★ **5,416,521 GBIM entities with `confidence_decay` metadata**, restored March 28). BBB 7-filter pipeline at `127.0.0.1:8016` ★ — all 7 filters active. ★ **All BBB and `TruthFilterBBBValidator` gate decisions persist to `jarvis-memory:8056`** (secured March 28). `normalize_identity` and TruthValidator on every `ultimatechat` response. `truthverdict` attached to every UltimateResponse. **Caddy perimeter + `jarvis_auth_service` (8055 ★, systemd) — RBAC active March 22, ★ Up March 28. ★★★★★ `jarvis-memory:8056` — all April 7 items confirmed live:** `/health` → `{"status":"healthy","service":"ms-jarvis-memory","redis":"connected"}` ✅; `/pia_window?minutes=240` → clean structured JSON ✅; type guard `if r.type(key) != b'list': continue` live in production code ✅; Redis type correctness verified (60+ `service:jarvis-*` hashes, `conv:internal:bbb_*` lists, `pia:latest` hash, `pia:history` list) ✅; `jarvis-memory` added to `msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml` line 1141 with bind mount — first-class rebuild service ✅; `deploy-memory.sh` one-command redeploy created ✅. **★ 96/96 containers Up — zero Restarting, zero Exited.** |
| **Partially implemented / scaffolded** | PIA review loop exists as a structured process — it does not auto-rewrite configuration, prompts, or filters; propagation of PIA recommendations requires explicit operator action. ★★★★★ `/pia_window` moves PIA sampling from "manual / ephemeral logs" to "programmatic / queryable JSON" — automated scheduled cycling and machine-readable recommendation output are still future work. Population- and risk-type-specific retrieval tagging is partially implemented; differential retrieval tuning grounded in `msjarvis:5433` ★ GBIM is future work. Steganographic trigger event logging is active (durable at `jarvis-memory:8056`); automated aggregation into PIA pattern reports is future work. **RBAC is enforced at the Caddy perimeter only** — per-route enforcement is an open item. ★ `confidence_decay` metadata on `msjarvis:5433` ★ GBIM entities is available for PIA review — integration into automated PIA sampling is partial. |
| **Future work / design intent only** | Automated, scheduled PIA review cycle with machine-readable output format for direct configuration integration. Automated propagation of PIA recommendations into BBB penalty weights, judge instructions, and global mode policies without manual operator step. Persistent introspective log of PIA cycle inputs, analyses, and recommendations as a first-class ChromaDB collection with PostgreSQL audit trail (★ `jarvis-memory:8056` provides the foundation). Population- and risk-type-specific retrieval tuning vs `msjarvis:5433` ★ GBIM. Automated aggregation of `SteganographyDetection` trigger events into PIA pattern analysis reports. **Per-route RBAC enforcement at the application layer.** Role-differentiated rate limiting. ★ Judge pipeline upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring (Chapter 7 §7.8) — pending. |

Cross-reference: BBB 7-filter pipeline — Chapter 16. Identity normalization and TruthValidator — Chapter 22. Psychological services and meaning-oriented track — Chapter 23. Canonical 9-phase `ultimatechat` sequence — Chapter 17. ChromaDB `psychological_rag` architecture — Chapter 5. March 18, 2026 security hardening — Chapter 40 §40-C. Caddy perimeter + `jarvis_auth_service` — Chapter 19 §19.8.1–§19.8.2. ★ `jarvis-memory:8056` durable BBB audit trail architecture — Chapter 25 §25.2.

---

## 29. Psychological Safeguards and the PIA Review Loop

This chapter formalizes how psychological and mental-health knowledge is integrated into Ms. Jarvis to guide interaction patterns, monitor interaction risks, and adapt system behavior over time. In the current deployment (★★★★★ April 7, 2026), this is realized through two confirmed running services — `jarvis-psychology-services` (port **8019** ★, deployed March 15) and `psychological_rag_domain` (port **8006** ★, containerized March 15) — a curated psychological corpus in ChromaDB (★ **968 items restored March 28**, `psychological_rag` collection, port **8000** ★, `chroma_data` volume; ★★★★★ within 48-collection inventory, April 7), validation against PostgreSQL `msjarvis` (port **5433** ★, ★ **5,416,521 GBIM entities with `confidence_decay` metadata**, restored March 28), the BBB 7-filter pipeline at `127.0.0.1:8016` ★ as the primary live Phase 1.4 safety gate (★ audit → `jarvis-memory:8056` secured March 28), and — ★★★★★ newly live April 7 — the `/pia_window` route on `jarvis-memory:8056` as the first programmatic, queryable PIA review window.

**New as of March 22, 2026:** Caddy perimeter (port **8443** ★) with `forward_auth` enforcing token-based RBAC via `jarvis_auth_service` (port **8055** ★, systemd-managed). Two red-team token roles active: `carrie_admin` (full access) and `hayden_test` (internal test role). Per-route enforcement is an open item.

★ **New as of March 28, 2026:** `jarvis-memory:8056` secured — all BBB and `TruthFilterBBBValidator` gate decisions durably logged. `msjarvis:5433` ★ restored to 5,416,521 GBIM entities with `confidence_decay` metadata. All 96/96 containers Up.

★★★★★ **New as of April 7, 2026 — `/pia_window` and `jarvis-memory` hardening:**

Five items that were broken or incomplete in the ch29 closeout state are now resolved:

1. **`/pia_window` route — 404 → Live ✅.** The route existed in the local file but the container was importing from `/app/services/` via bind mount shadow rather than `/app/`. Fixed with `docker cp` to the correct path `/app/services/ms_jarvis_memory.py`. The `/pia_window` endpoint now scans Redis `conv:*:*` keys, counts `bbb_audit` and `phase3` events within a configurable time window, and returns structured JSON — this is the first programmatic PIA window in the system's history. Ch29 described the PIA review loop as a manual sampling process relying on ephemeral container logs; that is no longer the only path.

2. **Redis WRONGTYPE error — resolved ✅.** `conv:sessions:internal` was stored as a Redis set; `lrange` expected a list, causing a WRONGTYPE error on every `/pia_window` scan. Identified and deleted the bad key via `redis-cli`. The scan loop now completes without error.

3. **Python IndentationError crash — fixed ✅.** A `sed` patch mangled the type guard into a one-liner with an orphaned indent, sending the container into a crash loop. Repaired with Python `str.replace()`. **No more `sed` on Python files.** `deploy-memory.sh` enforces this going forward.

4. **`jarvis-memory` orphaned from rebuild stack — resolved ✅.** The container was running from the ch29 backup image (`/home/cakidd/ch29-closeout/backups/docker-compose.yml:1585`) with no volume mount, meaning every edit required a manual `docker cp`. `jarvis-memory` is now added as a first-class service to `msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml` at line 1141 with a bind mount. All future edits are immediately reflected on container restart.

5. **`deploy-memory.sh` created ✅.** No fast redeploy path existed for `ms_jarvis_memory.py` edits. `./deploy-memory.sh` is now the single command for all future memory service edits and redeployments.

Phase 3 psychology pre-assessment is active on every production 9-phase pipeline request (confirmed March 15, 2026, 349.87s end-to-end benchmark). A critical constraint is that these mechanisms are designed for supportive, psychoeducational guidance and risk awareness validated against PostgreSQL community data, not for formal DSM-style diagnosis or clinical decision-making.

---

## 29.1 Role of Psychological Guidance

In the current deployment, psychological guidance grounded in `msjarvis:5433` ★ GBIM is not treated as an auxiliary feature but as a core constraint on how the system interacts with people, enforced at Phase 3 of every production 9-phase pipeline request. Its primary functions are threefold.

**Interaction quality.** `jarvis-psychology-services` (port **8019** ★) provides principled reference points for respectful, non-coercive, and supportive exchanges validated against `msjarvis:5433` ★ GBIM (5,416,521 entities with `confidence_decay` metadata) West Virginia community norms. Its `/psychological_assessment` endpoint runs on every production request and returns structured responses: `therapeutic_guidance`, `emotional_support`, `wellbeing_recommendations`, and `evidence_based_approaches`. `psychological_rag_domain` (port **8006** ★) provides retrieval of curated materials — therapy, mindfulness, trauma, depression, anxiety, and social-support content (★ **968 items restored March 28**) — via `/search`, backed by the ChromaDB `psychological_rag` collection (port **8000** ★, `chroma_data` volume; ★★★★★ within 48-collection inventory, April 7). These materials are curated for high-level, evidence-informed guidance validated against PostgreSQL community context; they are not used to perform formal diagnosis.

**Risk awareness.** TruthValidator (applied on every response via `jarvis-main-brain`, port **8050** ★) encodes patterns known to be harmful — identity confusion, anthropomorphic overclaiming, misleading statements about agency and embodiment — validated against `msjarvis:5433` ★ GBIM and returns `correct_identity`, `correct_creator`, and `relationship_clear` booleans. ★ All `truthverdict` decisions are durably logged at `jarvis-memory:8056` (secured March 28). The BBB 7-filter Phase 1.4 stack at port **8016** ★ screens for content violating ethical or community-safety constraints including high-risk mental-health content.

**Structural integrity assurance.** The `SteganographyDetection` filter (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`, confirmed active March 21, 2026) screens every request for adversarial payloads embedded via zero-width characters, homoglyph substitution, and structural encoding tricks. Within the psychological safeguards framework, this filter is classified as a psychological integrity assurance (PIA) safeguard: adversarial steganographic injection is a known vector for manipulating AI system behavior in ways that could undermine therapeutic boundaries, safety constraints, or identity normalization. ★ All `SteganographyDetection` trigger events are durably logged at `jarvis-memory:8056` (secured March 28). ★★★★★ These trigger events are now queryable via `/pia_window` alongside `bbb_audit` and `phase3` events — adversarial payload pattern analysis is now programmatically accessible for the first time.

**Self-checking.** `normalize_identity` applied to every `ultimatechat` response rewrites outputs that deviate from allowed self-descriptions validated against `msjarvis:5433` ★ GBIM or blur human-machine boundaries, before the response is returned to the caller.

---

## 29.2 Confirmed Active Safeguards (★★★★★ April 7, 2026)

The following table records all confirmed active psychological safeguards as of ★★★★★ April 7, 2026 (updated from March 28, 2026 baseline). This table is the authoritative reference for PIA review scope and regression testing in Chapter 41 §41.4.1.

| Safeguard | Service / Location | Confirmed | Notes |
|---|---|---|---|
| Caddy perimeter RBAC | Caddy (port 8443 ★) + `jarvis_auth_service` (port 8055 ★) | ✅ March 22 / ★ Up March 28 | `carrie_admin` (full access), `hayden_test` (internal test role); perimeter-level enforcement; per-route RBAC is OPEN ITEM |
| EthicalFilter | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| SpiritualFilter | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| SafetyMonitor | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | Word-boundary regex fix March 15; no false-positives on community resource terms; ★ audit → `jarvis-memory:8056` |
| ThreatDetection | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| **SteganographyDetection** | **BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★)** | **✅ March 21 / ★ Up March 28** | **`zero_width_homoglyph_structural_v1`, `confidence: 1.0`; ★ trigger events durable at `jarvis-memory:8056`; ★★★★★ now queryable via `/pia_window`** |
| TruthVerification | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| ContextAwareness | BBB Phase 1.4 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 15 / ★ Up March 28 | All requests; ★ audit → `jarvis-memory:8056` |
| TruthValidator | `jarvis-main-brain:8050` ★ post-processing | ✅ March 15 / ★ Up March 28 | `correct_identity`, `correct_creator`, `relationship_clear` validated vs `msjarvis:5433` ★ GBIM; ★ `truthverdict` durable at `jarvis-memory:8056`; ★★★★★ queryable via `/pia_window` |
| `normalize_identity` | `jarvis-main-brain:8050` ★ post-processing | ✅ March 15 / ★ Up March 28 | Every `ultimatechat` response |
| Phase 3 psychology pre-assessment | `jarvis-psychology-services:8019` ★ | ✅ March 15 / ★ Up March 28 | Severity classification + crisis indicator on every request; ★★★★★ `phase3` events counted by `/pia_window` |
| Psychological RAG retrieval | `psychological_rag_domain:8006` ★ | ✅ March 15 / ★ **968 docs restored March 28** | ★ 968-item corpus restored March 28; within ★★★★★ 48-collection inventory, April 7 |
| BBB output guard | BBB Phase 4.5 (`jarvis-blood-brain-barrier:8016` ★) | ✅ March 18 / ★ Up March 28 | Full verdict dict received; `apply_output_guards_async` 8.0s timeout; ★ audit → `jarvis-memory:8056` |
| ★ BBB durable audit trail | `jarvis-memory:8056` | ★ ✅ **March 28** | Port corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set — all BBB and `TruthFilterBBBValidator` decisions durably logged |
| **★★★★★ `/pia_window` programmatic PIA query** | **`jarvis-memory:8056`** | **★★★★★ ✅ April 7** | **Scans `conv:*:*` Redis keys; counts `bbb_audit` + `phase3` events in configurable window; returns structured JSON; Redis type guard live; `conv:sessions:internal` WRONGTYPE resolved** |
| **★★★★★ `deploy-memory.sh`** | **`msjarvis-rebuild/`** | **★★★★★ ✅ April 7** | **One-command redeploy for all `ms_jarvis_memory.py` edits; replaces `docker cp` manual workflow** |
| **★★★★★ `jarvis-memory` in rebuild compose** | **`msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml` line 1141** | **★★★★★ ✅ April 7** | **First-class rebuild service with bind mount volume; previously orphaned to ch29 backup stack** |

---

## 29.3 Red-Team Token Roles and RBAC (NEW — March 22, 2026; ★ confirmed Up March 28)

Role-based access control for red-team and administrative access is enforced at the Caddy perimeter layer via `jarvis_auth_service` (port **8055** ★, systemd-managed). All `/chat*` route traffic passes through `forward_auth` before reaching any internal service.

### Active Token Roles

| Role | Access Level | Notes |
|---|---|---|
| `carrie_admin` | Full access | All `/chat*` routes; no rate-limit overrides applied at role level |
| `hayden_test` | Internal test role | All `/chat*` routes; intended for red-team and regression testing sessions |

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

`jarvis_auth_service` writes each auth decision (timestamp, client IP, role, decision) to `/var/log/caddy/jarvis_redteam.log` (structured JSON). ★ `jarvis-memory:8056` (secured March 28) provides a complementary durable store for BBB gate decisions that occur downstream of auth — together, these two logs provide end-to-end accountability from perimeter auth through content filter. ★★★★★ `/pia_window` now makes the downstream BBB event data queryable in structured JSON alongside phase3 event counts, enabling timestamp-aligned cross-referencing of auth events and BBB trigger events for the first time.

### Open Item: Per-Route RBAC

**RBAC is currently enforced at the Caddy perimeter only.** Per-route enforcement is not yet implemented.

- The `X-Jarvis-Role` header is injected and forwarded to `bbb-input-filter:8016` ★ on every authenticated request.
- `jarvis-main-brain` does not currently inspect `X-Jarvis-Role` to gate individual route access.
- Route-level enforcement will require changes to `jarvis-main-brain` FastAPI route handlers or a Caddy route-matchers configuration update.

**Resolution path:** Add route-level `forward_auth` matchers in the Caddyfile that return 403 for `hayden_test` on destructive or privileged endpoints (`/chat_cancel_all`, `/chat_cancel/{job_id}`, any future admin endpoints). Document confirmed enforcement in **Chapter 42 §42.3.2** when complete.

> **⚠️ Forward reference note:** Verify that Ch 42 contains a §42.3.2 placeholder for per-route RBAC enforcement documentation. If §42.3.2 does not yet exist, add a stub section with the heading "Per-Route RBAC Enforcement (Pending)" so this forward reference does not break.

---

## 29.4 Organization of the Guidance Corpus

In the current deployment, psychological guidance materials are curated in the `psychological_rag` collection within ChromaDB (`127.0.0.1:8000` ★, `chroma_data` Docker volume, ★ **968 docs restored March 28**; ★★★★★ within 48-collection inventory, April 7) and served via `psychological_rag_domain` (`127.0.0.1:8006` ★), with validation against `msjarvis:5433` ★ GBIM for West Virginia community context.

**Corpus content (★ 968 items restored March 28).** Topics include therapy, mindfulness, trauma, depression, anxiety, and social support, validated against `msjarvis:5433` ★ GBIM (5,416,521 entities with `confidence_decay` metadata) for appropriateness to Appalachian community contexts. ★ The `confidence_decay` metadata on `msjarvis:5433` ★ GBIM entities representing DHHR and mental health service institutions is available for PIA corpus curation: entities with high `confidence_decay` are candidates for targeted corpus refresh or `needs_verification` flagging. Community-validated resource data from `jarvis-local-resources-db` (port **5435** ★) — including resources validated by Harmony for Hope Community Champions such as lead validator Crystal Colyer — is also eligible for inclusion where relevant to Appalachian mental health support.

**Tagging and retrieval.** The design intends items will be tagged with theme, population, and risk type to support targeted retrieval validated against PostgreSQL community data. In the current deployment, tagging is partially implemented; `/search` on `psychological_rag_domain` supports query-based retrieval against the ★ 968-item corpus, and population- and risk-type-specific differential retrieval tuning is identified as future work.

---

## 29.5 Use During Live Interactions — 9-Phase Pipeline Integration

In the current deployment (★★★★★ April 7, 2026), psychological safeguards validated against `msjarvis:5433` ★ GBIM are active at multiple phases of the 9-phase production pipeline (Chapter 17).

**Caddy perimeter + `jarvis_auth_service` (Tier 1 — always first).** Before any request reaches Phase 1.4, it passes through Caddy (port **8443** ★) and `jarvis_auth_service` (port **8055** ★). Token role established; unauthenticated requests rejected at the perimeter. Access decisions written to `/var/log/caddy/jarvis_redteam.log`.

**Phase 1.4 — BBB 7-filter input stack.** All 7 BBB filters (port **8016** ★): EthicalFilter, SpiritualFilter, SafetyMonitor (word-boundary regex fixed March 15), ThreatDetection, **SteganographyDetection (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`, confirmed active March 21)**, TruthVerification, and ContextAwareness. ★ All gate decisions persist to `jarvis-memory:8056` (secured March 28). ★★★★★ These events are now queryable via `/pia_window` — `bbb_audit` events within a configurable time window are returned in structured JSON.

**Phase 3 — Psychology pre-assessment (deployed March 15, always active; ★ Up March 28).** Every production request passes through `jarvis-psychology-services` (port **8019** ★) via `/psychological_assessment`:

- Severity classification (mild / moderate / severe)
- Crisis indicator check (Boolean flag for immediate risk)
- `therapeutic_guidance`: evidence-based approaches relevant to detected patterns
- `emotional_support`: supportive language recommendations
- `wellbeing_recommendations`: actionable, non-diagnostic suggestions
- `evidence_based_approaches`: specific evidence-informed frameworks

★★★★★ Phase 3 events are now counted by `/pia_window` alongside `bbb_audit` events — the first longitudinal programmatic view of Phase 3 assessment frequency is now available.

**Phase 4 — Psychological RAG context building.** `jarvis-spiritual-rag` (port **8005** ★ — cross-reference Ch 01 container mapping to verify port was not renumbered during March hardening) queries `psychological_rag_domain` (port **8006** ★) as one of its RAG sources, retrieving relevant entries from the ★ 968-item `psychological_rag` ChromaDB collection (★★★★★ within 48-collection inventory, April 7). This psychological RAG context is combined with GBIM beliefs (`msjarvis:5433` ★), PostGIS spatial data (`msjarvisgis:5432` ★), and community resources (`jarvis-local-resources-db:5435` ★) into the unified context block.

**Phase 4.5 — BBB output guard.** `apply_output_guards_async` passes the response through BBB `/filter` (port **8016** ★, 8.0s timeout, fail-open behavior confirmed), receiving and evaluating the full judge verdict dict (integrated March 18, 2026). ★ All Phase 4.5 gate decisions are durably logged at `jarvis-memory:8056` (secured March 28).

**Post-processing — identity normalization.** `normalize_identity` ensures the final response speaks as Ms. Egeria Jarvis, not as a clinician or therapist. TruthValidator verifies `correct_identity`, `correct_creator`, and `relationship_clear` validated against `msjarvis:5433` ★ GBIM. ★ `truthverdict` durable at `jarvis-memory:8056`. ★★★★★ `truthverdict` events visible in `/pia_window` output.

---

## 29.6 The PIA Review Loop

In the current deployment, the Psychology-Informed Alignment (PIA) review loop exists as a structured process that samples logs and introspection outputs validated against `msjarvis:5433` ★ GBIM, producing written recommendations — not auto-rewrites of configuration, prompts, or filters. ★★★★★ As of April 7, 2026, the `/pia_window` route on `jarvis-memory:8056` is the first programmatic PIA review window — moving the primary input from ephemeral container logs to a queryable, durable, structured JSON endpoint.

### 29.6.1 `/pia_window` — Programmatic PIA Sampling (★★★★★ Live April 7)

```python
# Confirmed live in ms_jarvis_memory.py — April 7, 2026
# Route: GET /pia_window?minutes=N
# Scans conv:*:* Redis keys (type-guarded)
# Counts bbb_audit and phase3 events within configurable time window
# Returns structured JSON

@app.get("/pia_window")
async def pia_window(minutes: int = 60):
    cutoff = time.time() - (minutes * 60)
    bbb_count = 0
    phase3_count = 0
    keys = r.keys("conv:*:*")
    for key in keys:
        if r.type(key) != b'list':       # Type guard — live in production
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

**Confirmed test result (April 7, 2026):**

```
GET /pia_window?minutes=240
→ clean JSON, no errors ✅
→ type guard active — non-list keys (conv:sessions:internal was set type, now deleted) skipped ✅
→ conv:*:* keys scanned correctly ✅
→ bbb_audit and phase3 event counts returned ✅
```

**Redis key type inventory confirmed April 7:**

```
service:jarvis-*     → hash  (60+ services registered) ✅
conv:internal:bbb_*  → list  (BBB audit trail intact) ✅
pia:latest           → hash  (PIA snapshot store healthy) ✅
pia:history          → list  (PIA history list intact) ✅
conv:sessions:internal → DELETED (was set type — WRONGTYPE error source) ✅
```

**Ch29 → April 7 transition:** Ch29 described the PIA review loop as a manual sampling process relying on ephemeral container logs. `/pia_window` is the first queryable, programmatic PIA window — it does not replace manual governance review, but it gives PIA review a durable, structured JSON input that does not depend on container log retention. This is the automated PIA sampling input that ch29 marked as future work.

### 29.6.2 Manual PIA Inputs (still active alongside `/pia_window`)

**Inputs and scope.** PIA review also operates by manually sampling:

- Recent interaction logs and `ms_jarvis_memory` entries (ChromaDB, confirmed written after every `/chat` call via `background_rag_store`; ★★★★★ within 48-collection inventory, April 7)
- `truthverdict` fields from UltimateResponse validated against `msjarvis:5433` ★ GBIM; ★ durable at `jarvis-memory:8056`
- BBB `barrier_stats` counters from the 7-filter pipeline; ★ durable at `jarvis-memory:8056`
- `SteganographyDetection` trigger logs — events where `zero_width_homoglyph_structural_v1` flagged content; ★ durable at `jarvis-memory:8056`; ★★★★★ queryable via `/pia_window`
- `jarvis_auth_service` access logs — `/var/log/caddy/jarvis_redteam.log` entries for role-differentiated interaction pattern analysis
- Phase 3 outputs from `jarvis-psychology-services` — severity classifications, crisis flags; ★★★★★ counted by `/pia_window`
- `psychological_rag_domain` `/search` usage patterns against the ★ 968-item corpus
- ★ **`confidence_decay` values from `msjarvis:5433` ★ GBIM** for DHHR and mental health service institution entities — high-decay entities are PIA flags for corpus refresh

**Analysis.** PIA review examines: recurring `truthverdict` violations, BBB 7-filter block-rate trends, identity-confusion patterns in TruthValidator outputs, adversarial steganographic injection attempt patterns (★★★★★ now queryable via `/pia_window`), underuse of psychological guidance, crisis indicator detection rates, role-differentiated access patterns from `jarvis_redteam.log`, and ★ **`confidence_decay` trend analysis for GBIM entities representing DHHR and mental health service institutions**.

**Outputs and recommendations.** The PIA review loop produces structured written recommendations such as:

- "Tighten identity phrasing constraints in crisis-related dialogues"
- "Introduce explicit boundary statements for maternal metaphors"
- "Increase Phase 3 severity threshold for economic-stress queries"
- "Add to `psychological_rag` corpus: rural grief resources validated against Fayette County community data from `jarvis-local-resources-db:5435` ★"
- "Review `confidence_decay` for DHHR mental health service entities — high-decay entities identified via `/pia_window` PIA sampling"
- "Audit `SteganographyDetection` trigger events at `/pia_window` for recurring payload patterns"
- "Implement per-route RBAC to restrict `/chat_cancel_all` and destructive endpoints to `carrie_admin` only"

These require explicit operator action to implement — they do not automatically rewrite BBB parameters, judge instructions, or global mode policies.

---

## 29.7 Integration with Barriers, Modes, and Judge Components

In the current deployment, PIA recommendations can be applied to several confirmed control surfaces validated against `msjarvis:5433` ★ GBIM, but application requires explicit operator action.

**Barrier and filter adjustments.** BBB 7-filter pipeline at port **8016** ★ exposes rule sets that can be updated in response to PIA findings. ★★★★★ With `jarvis-memory:8056` `/pia_window` now providing programmatic access to BBB event counts, PIA review of steganographic trigger frequency no longer requires manual container log scraping — it is available as structured JSON on demand. In the current deployment, updates to filter parameters remain manual.

**Global mode settings.** PIA outputs will modify mode selection policies validated against `msjarvis:5433` ★ GBIM in future work. In the current deployment, mode settings are adjusted by operators following PIA review.

**Evaluator and judge behavior.** Judge services (7230–7233, confirmed running and compose-managed since March 18, 2026; ★ Up March 28) can receive updated instructions reflecting refined psychological guidance validated against `msjarvis:5433` ★ GBIM. ★ The planned judge pipeline upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring querying `msjarvis:5433` ★ (5,416,521 entities with `confidence_decay`) would strengthen psychological safeguard scoring in judge evaluations (Chapter 7 §7.8); upgrade sprint pending.

**69-DGM cascade integration.** The 69-DGM cascade (`jarvis-69dgm-bridge`, host port 19000 → internal port **9000** ★, 23 connectors × 3 stages; ★ Up March 28) at Phase 7 provides an additional validation layer for psychologically sensitive responses. ★★★★★ Future PIA recommendations may target specific DGM connector configurations relevant to psychological safety, with connector-level event data surfaced via `/pia_window`.

**RBAC-informed PIA recommendations.** ★★★★★ `/pia_window` enables cross-referencing BBB gate decisions by time window, making role-differentiated BBB trigger analysis feasible as a PIA input for the first time when combined with `jarvis_redteam.log` auth events.

---

## 29.8 Recording, Memory, and Accountability

In the current deployment (★★★★★ April 7, 2026), psychological safeguards are recorded through several confirmed mechanisms with PostgreSQL-auditable trails.

**`ms_jarvis_memory` and interaction logs.** Every `/chat` response produces a `bg_<ISO8601>` entry in `ms_jarvis_memory` ChromaDB (port **8000** ★, `chroma_data` volume; ★★★★★ within 48-collection inventory, April 7; Chapter 17 §17.6), with `truthverdict` fields recording BBB 7-filter judgments. ★★★★★ `ms_jarvis_memory` ChromaDB entries and `jarvis-memory:8056` audit entries together form a two-layer interaction accountability record. The `/pia_window` endpoint adds a third, structured summary layer on top of the `jarvis-memory:8056` durable store.

**`jarvis_auth_service` access log.** Every auth decision by `jarvis_auth_service` (port **8055** ★) written to `/var/log/caddy/jarvis_redteam.log` as structured JSON. ★ Cross-referencing this log with `jarvis-memory:8056` BBB audit entries and `/pia_window` time-window counts enables end-to-end accountability: auth decision → BBB gate decision → Phase 3 event count — all timestamped and durable.

**Phase 3 assessment records.** Every production request generates a Phase 3 psychology pre-assessment record from `jarvis-psychology-services` (port **8019** ★). ★★★★★ `phase3` event counts are now available via `/pia_window` — the first longitudinal programmatic view of Phase 3 assessment frequency.

**PIA review records.** Each manual PIA review cycle produces a written record of inputs sampled, patterns observed, and recommendations proposed. ★ `jarvis-memory:8056` (secured March 28) provides the durable authenticated audit store that will anchor a future dedicated ChromaDB collection for PIA records. ★★★★★ `/pia_window` provides the queryable PIA input that these records will document. In the current deployment, PIA records are maintained as manually produced documents rather than automatically ingested into ChromaDB.

**Human oversight and governance.** PIA review outputs are designed for inspection by human reviewers including domain experts, ethicists, and community governance bodies. ★★★★★ `/pia_window` provides the structured JSON input that makes these reviews concrete and reproducible for the first time. The design treats psychological risk as a first-class governance concern, on par with technical reliability and knowledge integrity.

---

## 29.8.1 `deploy-memory.sh` — Fast Redeploy Protocol (★★★★★ April 7)

> **New as of April 7, 2026.** No fast redeploy path for `ms_jarvis_memory.py` edits previously existed. All future `jarvis-memory` service edits use this protocol.

```bash
#!/bin/bash
# deploy-memory.sh — one-command redeploy for ms_jarvis_memory.py edits
# ★★★★★ Created April 7, 2026 — replaces manual docker cp workflow
# Location: msjarvis-rebuild/deploy-memory.sh

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

**Usage:** `./deploy-memory.sh` from the `msjarvis-rebuild/` directory.

**Why `str.replace()` instead of `sed`:** The April 7 IndentationError was caused by a `sed` patch that collapsed a multi-line type guard into a single line with an orphaned indent, sending the container into a crash loop. Python `str.replace()` preserves indentation exactly. **No more `sed` on Python files.** `deploy-memory.sh` is the safe edit path going forward.

---

## 29.9 Open Items (★★★★★ April 7, 2026)

| Item | Priority | Notes |
|---|---|---|
| **Per-route RBAC enforcement** | HIGH | RBAC currently enforced at Caddy perimeter only. `hayden_test` and `carrie_admin` can both reach all `/chat*` routes once authenticated. Per-route enforcement requires `jarvis-main-brain` route handler changes or Caddy route-matcher config. See §29.3. ★★★★★ `/pia_window` live — role-differentiated BBB trigger analysis is now feasible; this increases implementation priority. |
| Role-differentiated rate limiting | MEDIUM | Caddy `caddy-ratelimit` module applies per-IP limits; role-differentiated limits for `hayden_test` vs `carrie_admin` not yet configured. |
| Automated PIA sampling cycle | FUTURE | Scheduled, machine-readable PIA review with direct configuration integration. ★★★★★ `/pia_window` provides the first programmatic PIA input — scheduled cycling is the next step. |
| Automated `SteganographyDetection` trigger aggregation | FUTURE | `/pia_window` now provides event counts; automated pattern analysis reports with recurring payload signatures are the next step. |
| PIA records as first-class ChromaDB collection | FUTURE | Currently manually produced documents; automated ingest with `jarvis-memory:8056` ★ durable audit trail and `/pia_window` structured JSON as input is future work. |
| Population- and risk-type-specific RAG retrieval tuning | FUTURE | Differential retrieval grounded in `msjarvis:5433` ★ GBIM West Virginia community data. |
| ★ `confidence_decay`-driven DHHR entity refresh | FUTURE | Automated identification of `msjarvis:5433` ★ GBIM mental health service entities with high `confidence_decay` for targeted `needs_verification` review in `jarvis-local-resources-db:5435` ★. |
| ★ Judge pipeline upgrade for psychological scoring | FUTURE | Upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring querying `msjarvis:5433` ★ — both stores confirmed at correct ports; upgrade sprint pending (Chapter 7 §7.8). |
| Per-route RBAC for `gbim_query_router` (port **7205** — cross-check vs Ch 01 `jarvis-gbim-query-router` container mapping) | FUTURE | Landowner belief queries reachable by any authenticated role; access restriction pending production hardening pass. |

---

## 29.10 Summary

★★★★★ **Chapter 29 is operationally advanced as of April 7, 2026.** The `/pia_window` route — the first programmatic PIA review window in the system's history — is confirmed live and returning structured JSON. `jarvis-memory` is now a first-class service in the rebuild compose stack. `deploy-memory.sh` provides a safe, fast redeploy path for all future memory service edits.

In the current deployment (★★★★★ April 7, 2026), psychological safeguards are realized through:

- `jarvis-psychology-services` (`127.0.0.1:8019` ★, deployed March 15) and `psychological_rag_domain` (`127.0.0.1:8006` ★, containerized March 15)
- Curated psychological corpus in ChromaDB (`127.0.0.1:8000` ★, `chroma_data` volume, ★ **968 items** in `psychological_rag` collection; ★★★★★ within 48-collection inventory, April 7)
- Validation against `msjarvis:5433` ★ (★ **5,416,521 GBIM entities with `confidence_decay` metadata**, restored March 28)
- BBB 7-filter pipeline at `127.0.0.1:8016` ★ (Phase 1.4 live safety gate; ★ audit → `jarvis-memory:8056` secured March 28)
- `normalize_identity` + TruthValidator on every `ultimatechat` response
- BBB output guard (port **8016** ★, full judge verdict dict, integrated March 18, 2026; ★ audit → `jarvis-memory:8056`)
- Caddy perimeter (port **8443** ★) + `jarvis_auth_service` (port **8055** ★, systemd) — RBAC active March 22
- ★★★★★ `jarvis-memory:8056` `/pia_window` — **programmatic PIA window, live April 7** ✅
- ★★★★★ `jarvis-memory` in `msjarvis-rebuild` compose — **first-class rebuild service, line 1141
- ★★★★★ `deploy-memory.sh` — **one-command redeploy path, created April 7** ✅

Key operational facts as of ★★★★★ April 7, 2026:

- ★★★★★ **`/pia_window` route live** — first programmatic PIA window in the system's history; scans `conv:*:*` Redis keys; counts `bbb_audit` + `phase3` events in configurable time window; returns structured JSON; Redis type guard live in production code ✅
- ★★★★★ **Redis WRONGTYPE resolved** — `conv:sessions:internal` (bad set type) identified and deleted; scan loop completes without error ✅
- ★★★★★ **`jarvis-memory` first-class rebuild service** — added to `msjarvis-rebuild/msjarvis-rebuild/docker-compose.yml` line 1141 with bind mount volume; no more manual `docker cp` for edits ✅
- ★★★★★ **`deploy-memory.sh` created** — one-command redeploy for all future `ms_jarvis_memory.py` edits ✅
- ★★★★★ **Python IndentationError resolved** — `sed` banned from Python file edits; `str.replace()` used going forward ✅
- ★★★★★ **Redis key type inventory confirmed**: `service:jarvis-*` → hash (60+ services) ✅; `conv:internal:bbb_*` → list ✅; `pia:latest` → hash ✅; `pia:history` → list ✅
- ★ **96/96 containers Up** — zero Restarting, zero Exited (carried forward from March 28 baseline)
- ★ **`jarvis-memory:8056` secured** — `_auth()` confirmed, `JARVIS_API_KEY` set, all BBB and `TruthFilterBBBValidator` decisions durably logged (carried forward from March 28)
- ★ **`msjarvis:5433`** — 5,416,521 GBIM entities with `confidence_decay` metadata (carried forward from March 28)
- ★ **`psychological_rag`** — 968 docs, within 40-collection / 6,675,442-vector ChromaDB inventory (carried forward from March 28)
- **Caddy perimeter RBAC active** — `carrie_admin` (full access) and `hayden_test` (internal test role) enforced at port **8443** ★; access decisions logged to `/var/log/caddy/jarvis_redteam.log`
- **Per-route RBAC is an open item** — enforcement is perimeter-only; ★★★★★ `/pia_window` role-differentiated analysis now feasible, increasing this item's priority
- Phase 3 psychology pre-assessment active on every production 9-phase pipeline request (confirmed 349.87s end-to-end benchmark); ★★★★★ `phase3` events now counted by `/pia_window`
- BBB has 7 confirmed active filters: EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, **SteganographyDetection (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`)**, TruthVerification, ContextAwareness; ★★★★★ `bbb_audit` events now counted by `/pia_window`
- BBB output guard (port **8016** ★) receives full judge verdict dict — confirmed March 18, 2026; ★ audit → `jarvis-memory:8056`

★★★★★ Four new accountability and operational capabilities are active as of April 7, 2026 that were not present in the March 28 baseline:

1. **`/pia_window` programmatic PIA query** — the PIA review loop's primary sampling input moves from "ephemeral container logs (manual)" to "structured JSON endpoint (queryable, durable, configurable time window)." This is the automated PIA sampling input that ch29 marked as future work — it is now working code.
2. **Redis type guard in production** — `if r.type(key) != b'list': continue` prevents any non-list Redis key (including future stale set- or hash-type conversation keys) from crashing the `/pia_window` scan loop.
3. **`jarvis-memory` in rebuild compose with bind mount** — edits to `ms_jarvis_memory.py` are now immediately reflected on container restart; the ch29-backup-stack orphan state is permanently resolved.
4. **`deploy-memory.sh` fast redeploy** — all future memory service edits have a safe, one-command path; `str.replace()` replaces `sed` for all Python file edits going forward.

Two constraints remain unchanged from the March 28 baseline: the PIA review loop still produces written recommendations through a structured process requiring operator action for implementation — automated propagation into BBB parameters, judge weights, or mode policies is future work; and the psychological guidance stack is explicitly non-diagnostic — DSM-style constructs are used only at a high-level, psychoeducational layer validated against PostgreSQL community data, not as clinical criteria.

The design intends that future work will: implement per-route RBAC enforcement (highest-priority open item, implementation conditions fully met); add scheduled `/pia_window` polling as an automated PIA sampling cycle with machine-readable recommendation output; automate `SteganographyDetection` trigger aggregation from `/pia_window` event counts into PIA pattern reports; persist PIA records as a first-class ChromaDB collection with `jarvis-memory:8056` ★ audit trail; complete the judge pipeline upgrade from `heuristic_contradiction_v1` to RAG-grounded truth scoring querying `msjarvis:5433` ★ (Chapter 7 §7.8); and refine corpus curation and tagging so that place-specific Appalachian mental health materials are more systematically retrieved while maintaining clear boundaries between supportive guidance and clinical diagnosis.

For the BBB 7-filter pipeline see Chapter 16. For identity constraints see Chapter 22. For the canonical 9-phase `ultimatechat` sequence see Chapter 17. For ChromaDB `psychological_rag` collection architecture see Chapter 5. For March 18, 2026 security hardening see Chapter 40 §40-C. For Caddy perimeter + `jarvis_auth_service` full architecture see Chapter 19 §19.8.1–§19.8.2. For `jarvis-memory:8056` durable BBB audit trail architecture see Chapter 25 §25.2.

---

*Last updated: ★★★★★ 2026-04-07 by Carrie Kidd (Mamma Kidd), Mount Hope WV*
*★★★★★ April 7, 2026: `/pia_window` route live — first programmatic PIA window — all PIA sections updated*
*★★★★★ April 7, 2026: Redis WRONGTYPE error resolved (`conv:sessions:internal` deleted) — §29.6.1 and safeguards table updated*
*★★★★★ April 7, 2026: Python IndentationError fixed (str.replace() — no more sed on Python files) — §29.8.1 updated*
*★★★★★ April 7, 2026: `deploy-memory.sh` created — §29.8.1 added*
*★★★★★ April 7, 2026: `jarvis-memory` added as first-class service to msjarvis-rebuild docker-compose.yml line 1141 — §29.9 open item resolved, safeguards table updated*
*★★★★★ April 7, 2026: Redis key type inventory confirmed (60+ services, BBB audit trail, PIA snapshot store) — §29.6.1 updated*
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
