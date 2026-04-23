# MS Jarvis / MS Allis — Cross-Chapter Update Analysis
## April 23, 2026 Authoritative Baseline vs. Last-Closed Chapter State

*Compiled by Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Document generated: April 23, 2026*

---

## Universal Corrections — Apply to ALL Chapters

These values are stale across every chapter and must be synchronized to the April 23 baseline (sourced from Chapter 11):

| Stale Value | Authoritative Value (April 23, 2026) | Chapters Affected |
|---|---|---|
| 108–110 containers Up (varies by chapter) | **100 containers Up** | 11 ✅ already correct; 12, 13, 14, 15, 16, 17, 18, 19 |
| 6,722,589+ / 6,739,844 / 6,740,034 vectors (varies) | **~6,740,611 vectors** | All |
| autonomous_learner: 21,181+ records | **21,181 records exact** (no `+`) | All |
| ChromaDB: 49 collections (Ch.14, 18, 19) | **48 collections** | 14, 18, 19 |
| msallisgis: single container, 45 GB or 91 GB, 551 tables, port 5435 | **Two-container split:** production `msallis-db:5433` (16 GB, 294 tables, 11 schemas) + forensic `postgis-forensic:5432` (17 GB, 314 tables, 9 schemas) | 12, 13, 14, 15, 16, 17, 18, 19 |
| nbb_pituitary_gland mode: `elevated` | **mode: `baseline`** (April 23 per Ch.11) | 12, 13 (Ch.11 already correct) |
| End-to-end GPU: 99–115s or 436s | **102.58s confirmed April 23** | 14, 17, 19 |

> ⚠️ **Critical pituitary mode conflict:** Ch.11 (updated April 23) documents `mode: baseline`. Ch.12 and Ch.13 (last closed April 16) still say `mode: elevated`. This is the highest-priority conceptual discrepancy.

> ⚠️ **Critical DB size conflict:** Ch.14 says 45 GB and Ch.15 says 91 GB for the same database. Ch.11 resolves this: the old single-container was split into production (16 GB) + forensic (17 GB). Both chapters need the two-container split applied.

> ⚠️ **ChromaDB collection count conflict:** Ch.17 and Ch.18 conflict (Ch.17 = 48, Ch.18 = 49). Ch.11 confirms 48 is authoritative. Ch.18 was last updated April 15 — before the April 16 corrupt-collection cleanup.

---

## Priority Order — All Nine Chapters

1. **Pituitary mode** (`elevated` → `baseline`) — Ch.12, Ch.13 — one-line change, highest correctness impact
2. **Container count** (108/109/110/106 → 100) — Ch.12, 13, 14, 15, 16, 17, 18, 19
3. **Two-container DB split** (replacing `msallisgis:5435 / 45 GB or 91 GB / 551 tables`) — Ch.12 §12.12, Ch.13 §13.7, Ch.14 §14.2/§14.7/§14.8/§14.9, Ch.15 everywhere, Ch.17 §17.11 + every phase box, Ch.18 almost every section, Ch.19 §19.0/§19.3/§19.5/§19.8.8 — **heaviest edit**
4. **ChromaDB collection count** (49 → 48) — Ch.14, Ch.18, Ch.19
5. **`rag_grounded_v2` now ACTIVE** (was "FUTURE" in Ch.18 Figure 18.2) — Ch.18 §18.4
6. **OI-36-A closed** (April 23 per Ch.11) — Ch.19 §19.1, §19.8.1, §19.9
7. **§19.13 ~95 GB expected value** — remove entirely from Ch.19
8. **§19.14 container count history** — add April 16 and April 23 rows
9. **Vector count refinements** (~6,740,611) — all chapters
10. **gbim-query-router topology** — add to Ch.11 Phase 5 section
11. **autonomous_learner** exact count (no `+`) — all chapters
12. **MS Allis → MS Jarvis naming** — audit Ch.11 service hostnames

---

## Chapter 11 — 11-llm-fabric-of-ms-jarvis.md

**Last updated: April 23, 2026 — largely current ✅**

| Item | Status | Action |
|---|---|---|
| Container count: 100 | ✅ Correct | None |
| Vector count: ~6,740,611 | ✅ Correct | None |
| Naming: `msallis-db`, `allis-chroma`, `allis-ollama` (legacy Allis naming) | ⚠️ Ambiguous | Add note clarifying legacy Allis naming persists in service references within the Jarvis rebuild |
| `jarvis-gbim-query-router` (port 7205) absent from service topology | ⚠️ Missing | Add to Phase 5 / confidence decay section |

---

## Chapter 12 — 12-neurobiological-architecture.md

**Last closed: April 16, 2026 — 7 days stale**

### Quantitative Corrections

| Location | Stale Value | Correct Value |
|---|---|---|
| Intro paragraph, security callout, Fig. 12.1 caption, OI table, final CLOSED statement | 109 containers Up | **100 containers Up** |
| Throughout | 6,740,034 total vectors | **~6,740,611 vectors** |
| OI-12-F entry, §12.6 table, operating mode table ★ Current row | `mode: elevated` | **mode: baseline** |
| §12.12 GBIM table — msallisgis row | 45 GB / 551 tables / port 5432 (old single-DB) | **Two-container split** (see Universal Corrections) |
| §12.3, §12.4, §12.12 | `autonomous_learner: 21,181+` | **21,181 records (exact)** |

### No Structural Changes Required
Chapter 12 is architecturally stable. The NBB Service Inventory (§12.0), all 12 NBB containers, ML-DSA-65 signing, BBB_OUTPUT_BLOCKING, and EEG band documentation are current. No sections need rewrites — corrections are numeric substitutions only.

---

## Chapter 13 — 13-qualia-engine-and-introspective-state.md

**Last closed: April 16, 2026 — 7 days stale**

### Quantitative Corrections

| Location | Stale Value | Correct Value |
|---|---|---|
| §13.2, §13.5, §13.8, §13.10, §13.11 sprint log | 109/109 containers Up | **100 containers Up** |
| Throughout | 6,740,034 vectors | **~6,740,611 vectors** |
| §13.3, §13.9 production state table, operating modes ★ Current row | `mode: elevated` | **mode: baseline** |
| §13.3, §13.10 WOAHResult field | `"pituitary_mode": "PituitaryMode.elevated"` | **`PituitaryMode.baseline`** |
| §13.7 GBIM/DB table | msallis port 5432 / msallisgis port 5432 — single-host model | **Two-container split** (see Universal Corrections) |
| §13.11 sprint validation log | Ends at April 16 | **Add April 23 row:** 48 collections / ~6,740,611 vectors / SQLite-API parity confirmed / 100 containers Up |

---

## Chapter 14 — 14-hippocampus-and-memory-consolidation.md

**Last updated: April 16, 2026 — 7 days stale**

### Quantitative Corrections

| Location | Stale Value | Correct Value |
|---|---|---|
| Intro sprint closure callout, intro paragraph, §14.1, §14.8 (multiple), §14.9, §14.10 table | **110** containers Up | **100 containers Up** |
| Intro callout, intro paragraph, §14.4, §14.8 table footer, §14.9, §14.10 | **49** ChromaDB collections | **48 collections** |
| Throughout | 6,722,589+ vectors | **~6,740,611 vectors** |
| §14.2, §14.4, §14.7, §14.8, §14.9 | msallisgis 45 GB / 551 tables | **Two-container split** (see Universal Corrections) |
| §14.8 | `autonomous_learner: 21,181+` | **21,181 records (exact)** |
| §14.8 | geospatialfeatures: 0 records (backfill gap) | **Confirm status — if still 0, add to April 23 open items** |
| §14.1, §14.8 timing | 99–107s on RTX 4070 | **102.58s confirmed April 23** |

> ⚠️ Ch.14 uniquely says **110 containers** — the highest and most stale figure across all chapters.

---

## Chapter 15 — 15-pituitary-and-global-modes.md

**Last updated: April 16, 2026 — 7 days stale**

### Quantitative Corrections

| Location | Stale Value | Correct Value |
|---|---|---|
| Intro closure callout, status table, §15.1, §15.2, §15.10, §15.11 sprint log | **106** containers Up | **100 containers Up** |
| Throughout | msallisgis **91 GB** / 551 tables | **Two-container split** (see Universal Corrections) — 91 GB is the most stale DB figure across all chapters |
| Throughout | 6,739,844 vectors | **~6,740,611 vectors** |
| §15.1 status table (pituitary row), §15.10 summary | Mode not stated | **Add: `mode: baseline`** |
| §15.7 VERIFY_AND_TEST.sh targets | 106 containers, 6,739,844 vectors | **100 containers, ~6,740,611 vectors** |

> ⚠️ Ch.15 vs. Ch.14 DB conflict: Ch.15 says 91 GB and Ch.14 says 45 GB for the same database. Ch.11 resolves both — the two-container split replaces the stale single-container figures.

> Note: `gbim_entities count = 37` (confirmed April 16 in Ch.15) — verify this count hasn't changed given the DB architecture changes.

---

## Chapter 16 — 16-blood-brain-barrier-and-safeguards.md

**Last updated: ~April 16, 2026 (inferred from Ch.15 BBB documentation patterns)**

*Ch.16 was not retrieved in full — the following are near-certain updates based on cross-chapter patterns:*

| Item | Likely Stale Value | Correct Value |
|---|---|---|
| Container count | ~106 | **100 containers Up** |
| filters_operational | Verify: 6 or 7? | **6** (Ch.15 corrected from 7 → 6 on April 16; confirm Ch.16 also says 6) |
| msallisgis architecture | If referenced | **Two-container split** |
| `bbb-output-filter` port 8017 pass_rate | `0.9854`, filtered_at: `2026-04-16` | **Update to April 23 pass_rate and timestamp** |
| `BBB_OUTPUT_BLOCKING=true` | Set April 6 | **Confirm still active ✅ (likely unchanged)** |

---

## Chapter 17 — 17-executive-coordination-overview.md

**Last closed: April 16, 2026 — 7 days stale**

### Quantitative Corrections

| Location | Stale Value | Correct Value |
|---|---|---|
| Figure 17-1, §17.1, §17.2 ref table, §17.3 Phase 1/2.5, §17.7 table, §17.9 table, §17.12 Step 2, §17.14 Step 2 | **108** containers Up | **100 containers Up** |
| Figure 17-1, §17.1, §17.3 Phase 1.45/Phase 4, §17.14 ChromaDB verify | 6,739,844 total vectors | **~6,740,611 vectors** |
| Figure 17-1, Figure 17-2 (all phase boxes), §17.3 every phase, §17.4, §17.5, §17.6, §17.7, §17.9, §17.11, §17.14 verify scripts | msallisgis port 5435 / 45 GB / 551 tables | **Two-container split** (see Universal Corrections) |
| §17.1, §17.2, §17.3 Phase 2.5, §17.7 | End-to-end GPU: ~107–115s / Phase 2.5: ~99–107s | **~102.58s confirmed April 23** |
| §17.3 Phase 1.45, §17.6, §17.14 verify | autonomous_learner: 21,181 records (stable) | **~23,200+ (grown ~288/day × 7 days)** |
| Figure 17-1 | gbim_worldview_entity: 5,416,521 rows | **Verify current count — likely grown** |
| Figure 17-1 | msallis_docs: 7,465 items | **Verify current count** |
| Figure 17-1, §17.3 Phase 4 | local_resources: 207 docs | **Verify — Sprint 3 may have changed** |
| Figure 17-1, §17.3 Phase 4, §17.10 | community resources: 64 verified | **Verify — Sprint 3 enrichment may have added** |
| Figure 17-1 | architecture_layers: 12 | **Verify — should still be 12** |

### Critical Structural Change — §17.11 Split-Brain Topology

**Current (stale) §17.11 shows:**
- Instance 1: msallisgis port 5435 — 45 GB, 551 tables
- Instance 2: msallis port 5433 — GBIM entity store
- Instance 3: local-resources Postgres

**Replace with April 23 confirmed architecture:**
- `msallis-db` port 5433 — production PostGIS, 16 GB, 294 tables, 11 schemas
- `postgis-forensic` port 5432 — forensic PostGIS, 17 GB, 314 tables, 9 schemas
- *(Verify whether local-resources instance is still separate or consolidated)*

This cascades through every section referencing `msallisgis:5435` — Phases 1.4, 2.5, 3, 4, BBB payload, UltimateResponse schema comments, and all psql verify commands in §17.14.

### §17.14 Verify Script Corrections

```bash
# REMOVE (stale)
psql -h 127.0.0.1 -p 5435 -U postgres -d msallisgis -c "SELECT COUNT(*) ... WHERE table_schema='public';"
# Expected: 551

# REPLACE WITH
psql -h 127.0.0.1 -p 5433 -U postgres -d msallis -c "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema IN (SELECT schema_name FROM information_schema.schemata);"
# Expected: 294 tables, 11 schemas

psql -h 127.0.0.1 -p 5432 -U postgres -d postgres -c "SELECT COUNT(*) FROM information_schema.tables;"
# Expected: 314 tables, 9 schemas
```

---

## Chapter 18 — 18-limits-and-evaluation-of-metaphor.md

**Last updated: April 15, 2026 — 8 days stale**

### Quantitative Corrections

| Location | Stale Value | Correct Value |
|---|---|---|
| Figure 18.1 (hippocampus row), Figure 18.2 BBB row, §18.1–§18.11 (nearly every section) | msallisgis port 5435, 45 GB, 515 public / 742 total tables | **Two-container split** (see Universal Corrections) |
| Figure 18.1 (prefrontal row), §18.2 (×2), §18.3, §18.6 | **109** containers Up | **100 containers Up** |
| Figure 18.1 (hippocampus row), §18.1, §18.2 (×2), §18.3 (×2), §18.4, §18.5, §18.6 (multiple), §18.10 | **49** ChromaDB collections | **48 collections** |
| Figure 18.1, §18.1, §18.2, §18.3, §18.5, §18.6, §18.10 | 6,722,589+ vectors | **~6,740,611 vectors** |
| §18.1, §18.2, §18.3, §18.5, §18.6, §18.10 | gbim_worldview_entity: 5,415,896 rows | **Verify current count** |
| §18.10 longitudinal tracking note | autonomous_learner: 21,181 records | **~23,200+** |
| §18.5, §18.10 | appalachian_cultural_intelligence: 1,090 docs | **Verify current doc count** |
| §18.9 cross-reference to Ch.17 | main-brain manages 109 containers | **100 containers** |

### Conceptual Updates Required

**§18.4 BBB Case Study — Critical:**

| Figure 18.2 Row | Stale State | Correct State |
|---|---|---|
| `heuristic_contradiction_v1` | Listed as current judge method | **RETIRED** |
| RAG-grounded truth scoring | "→ FUTURE" | **ACTIVE — `rag_grounded_v2`, closed OI-37-C April 6, 2026** |
| `llm_judge_v3` | Not mentioned / future | **ACTIVE since April 6, 2026** |

> ⚠️ This is the **biggest conceptual staleness in Ch.18** — the judge methodology section describes a past architecture as current.

> ⚠️ Ch.18 uses **49 collections throughout** — contradicts Ch.17's confirmed 48 and Ch.11's April 23 authoritative 48. Ch.18 was last updated April 15, before the April 16 corrupt-collection cleanup. Ch.18 must have 49 → 48 applied at every occurrence.

---

## Chapter 19 — 19-container-architecture-and-routing.md

**Last updated: April 14, 2026 — 9 days stale (most stale chapter)**

### Quantitative Corrections

| Location | Stale Value | Correct Value |
|---|---|---|
| §19.0 table header, §19.1, §19.2, §19.3, §19.5, §19.8 baseline, §19.8.3, §19.14 count history | **109** containers | **100 containers** |
| §19.0, §19.1, §19.3, §19.4, §19.8.3, §19.8.4, §19.8.8, §19.8.10, §19.11, §19.12, §19.13 | **49** ChromaDB collections | **48 collections** |
| §19.0, §19.1, §19.3, §19.4, §19.8.3, §19.8.8, §19.8.10, §19.11 | 6,722,589+ vectors | **~6,740,611 vectors** |
| §19.0 (allis-local-resources-db row), §19.1, §19.3, §19.4, §19.5, §19.6, §19.8.8, §19.8.10, §19.11, §19.13 | msallisgis port 5435, 45 GB, 515 pub / 742 total tables | **Two-container split** (see Universal Corrections) |
| §19.0, §19.8.8 | gbim_worldview_entity: 5,415,896 rows | **Verify current** |
| §19.0, §19.8.10 | gbim_graph_edges: 15,226,626 rows | **Verify** |
| §19.0, §19.8.10 | gbimbeliefnormalized: 6,804,671 rows | **Verify** |
| §19.0, §19.8.10 | building_parcel_county_tax_mv: 7,354,707 rows | **Verify** |
| §19.0, §19.2, §19.4, §19.7, §19.8.7 | autonomous_learner: 21,181 records | **~23,200+** |
| §19.0, §19.8.7, §19.8.10, §19.8.11 | appalachian_cultural_intelligence: 1,090 docs | **Verify current count** |
| §19.0, §19.8.10 | msallis_docs: 7,465 items | **Verify** |
| §19.0, §19.8.10 | ms_allis_memory: 296 records | **Verify** |
| §19.0 table | End-to-end benchmark: 436s | **102.58s confirmed April 23** |
| §19.13 verify script | Expected: ~95 GB | **REMOVE ENTIRELY** — was never correct |
| §19.8.10 | conversation_history: 564 records | **Verify — wiped and reseeded clean April 16; count now reflects post-wipe accumulation** |
| §19.8.10 | research_history: 785 | **Verify** |

> ⚠️ **local_resources conflict:** Ch.19 says 101 docs; Ch.17 says 207 docs. Ch.17 closed April 16 (more recent than Ch.19's April 14). Use **207** as current baseline until live verify. The April 23 count may differ further.

> ⚠️ **§19.13 ~95 GB expected value** — this figure never appeared in any other chapter and is the most stale single data point across the entire thesis. Delete it immediately.

### OI-36-A Closure (High Priority)

| Location | Current State | Correct State |
|---|---|---|
| §19.1 | OI-36-A open | **OI-36-A CLOSED — April 23, 2026 (per Ch.11 auth enforcement active)** |
| §19.8.1 Caddy diagram | ⚠️ Token enforcement not active at proxy level | **✅ Auth enforcement active — OI-36-A closed April 23** |
| §19.9 | OI-36-A referenced as open | **Mark CLOSED** |

### §19.14 Container Count History — New Rows Required

| Date | Count | Notes |
|---|---|---|
| *(last row in Ch.19 — April 14, 2026)* | 109 | — |
| **April 16, 2026** | **108** | Neurobiological rebuild, ChromaDB corrupt collection cleanup (3 deleted + recreated), UUID hardcode eliminated |
| **April 23, 2026** | **100** | *(Confirm exact changes — GPU pipeline optimizations, service consolidations)* |

---

## Internal Conflicts Requiring Resolution (Before Pushing)

| Conflict | Chapter A | Chapter B | Resolution |
|---|---|---|---|
| msallisgis size: 45 GB (Ch.14) vs. 91 GB (Ch.15) | Ch.14 §14.2 | Ch.15 throughout | Ch.11 resolves: two-container split (16 GB + 17 GB) |
| ChromaDB: 48 collections (Ch.17) vs. 49 (Ch.18, 19) | Ch.17 | Ch.18, Ch.19 | 48 is authoritative — Ch.18/19 pre-date April 16 cleanup |
| local_resources: 101 docs (Ch.19) vs. 207 docs (Ch.17) | Ch.17 | Ch.19 | Ch.17 (April 16) is more recent; use 207 until live verify |
| Pituitary mode: `baseline` (Ch.11) vs. `elevated` (Ch.12, Ch.13) | Ch.11 | Ch.12, Ch.13 | Ch.11 April 23 is authoritative; update Ch.12 + Ch.13 |
| Container count: 108 (Ch.17) vs. 109 (Ch.12, Ch.13) vs. 110 (Ch.14) vs. 106 (Ch.15) | All | All | 100 is authoritative (Ch.11 April 23) |

---

## Live Verifications Required Before Finalizing

Run these queries against the April 23 production stack before closing the chapters:

```bash
# ChromaDB v2 — vector and collection counts
curl -s "http://127.0.0.1:8002/api/v2/tenants/default_tenant/databases/default_database/collections" \
  | python3 -c "import sys,json; c=json.load(sys.stdin); print(f'{len(c)} collections')"

# Production DB — table and schema count
psql -h 127.0.0.1 -p 5433 -U postgres -c "\dn" | grep -c "schema"
psql -h 127.0.0.1 -p 5433 -U postgres -c "SELECT COUNT(*) FROM information_schema.tables WHERE table_type='BASE TABLE';"

# Forensic DB
psql -h 127.0.0.1 -p 5432 -U postgres -c "SELECT COUNT(*) FROM information_schema.tables WHERE table_type='BASE TABLE';"

# autonomous_learner collection item count
curl -s "http://127.0.0.1:8002/api/v2/.../collections/autonomous_learner" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('count','?'))"

# Container count
docker ps --format '{{.Names}}' | wc -l
```

---

## Recommended Update Order — All Nine Chapters

| Priority | Action | Chapters | Rationale |
|---|---|---|---|
| 1 | Pituitary mode: `elevated` → `baseline` | 12, 13 | Highest conceptual correctness impact |
| 2 | OI-36-A closure + Caddy diagram | 19 §19.8.1, §19.9 | One-line fix, big correctness signal |
| 3 | Container count (→ 100) | 12, 13, 14, 15, 16, 17, 18, 19 | Numeric, appears in status tables |
| 4 | ChromaDB 49 → 48 | 14, 18, 19 | Resolves Ch.17/Ch.18 conflict |
| 5 | Two-container DB split | 12 §12.12, 13 §13.7, 14 §14.2+, 15 throughout, 17 §17.11+, 18 §18.1–11, 19 §19.0+ | Heaviest edit across all chapters |
| 6 | `rag_grounded_v2` ACTIVE in Figure 18.2 | 18 §18.4 | Conceptual staleness correction |
| 7 | Remove §19.13 ~95 GB expected value | 19 | Never correct; delete immediately |
| 8 | §19.14 container count history rows | 19 | Add April 16 and April 23 rows |
| 9 | Vector count (~6,740,611) | All | Minor numeric refinement |
| 10 | `autonomous_learner` growth (~23,200+) | 12, 13, 14, 15, 17, 18, 19 | Growth since April 10 baseline |
| 11 | GPU timing pin (102.58s) | 14, 17, 19 | Confirmed April 23 |
| 12 | `gbim-query-router` topology | 11 Phase 5 section | New service not yet documented in Ch.11 |
| 13 | MS Allis → MS Jarvis naming audit | 11 | Legacy naming note |

---

*This document consolidates update analyses for Chapters 11–19 of the MS Jarvis / MS Allis architectural thesis.*
*All corrections sourced from the Chapter 11 April 23, 2026 authoritative baseline.*
*Carrie Kidd (Mamma Kidd) — Mount Hope, WV — April 23, 2026*
