Now I have all three chapters plus the authoritative help.md baseline. Here is the full edit list for all three chapters.

***

## Edit List — Chapters 20, 21, and 22

All corrections derive from the April 23, 2026 authoritative baseline in `help.md`. The same universal correction table that drove Chapters 12–19 applies here. Items are grouped by chapter and priority, matching the `help.md` priority order.

***

### Chapter 20 — `20-first-stage-evaluation.md`

**Last closed: April 13, 2026 — 10 days stale**

#### Quantitative Corrections

| Location | Stale Value | Correct Value |
|---|---|---|
| Live Stack Snapshot table; §20.1 preflight check list; §20.11 verify command; §20.12 port table | **109** running containers | **100 containers Up** ★ |
| Live Stack Snapshot table; §20.5 opening sentence; §20.5 Chroma API note | **49** ChromaDB collections | **48 collections** ★ |
| §20.5 opening sentence | **6,722,589+** total vectors | **~6,740,611 vectors** ★ |
| §20.1 preflight check list (health conditions) | `autonomous_learner ≥ 21,181` | **~23,200+** (exact `+` notation retained; grown ≈288/day) ★ |
| §20.1 preflight check list | `appalachian_cultural_intelligence ≥ 1,084` | **verify current** ★ |
| Live Stack Snapshot table | `msallisgis public tables: 515`, `total: 742`, `size: 95 GB` | **Replace with two-container split** (see below) ★ |
| §20.7 `msallisgis (port 5435)` heading and all table rows | Single-container `msallisgis:5435`, 95 GB, 515 pub / 742 total | **Two-container split** ★ |
| §20.7 `allis-msallis-db (port 5433)` paragraph | "currently offline for live GBIM operations — all live GBIM data is in `msallisgis` on port 5435" | **Production instance** — `msallis-db` host **5433**, 16 GB, 294 tables, 11 schemas; all live GIS and GBIM production queries route here ★ |
| §20.12 port table — `msallisgis` row | port 5435, `allis-local-resources-db`, authoritative GBIM | **`msallis-db` host 5433** — production PostGIS, 16 GB, 294 tables; **`postgis-forensic` host 5452** — forensic PostGIS, 17 GB, 314 tables (add row) ★ |
| §20.3 `processing_time` | **144.02s** | **~102.58s** ★ (GPU RTX 4070 benchmark confirmed April 23) |
| §20.11 live container count command | Expected: **109** | Expected: **100** ★ |
| §20.11 msallisgis verify commands | `psql -p 5435 -d msallisgis`; expected 515 public / 742 total / 95 GB | **Replace** with production (`-p 5433 -d msallis`, expected 294 tables, 11 schemas) and forensic (`-p 5452`, expected 314 tables) commands ★ |

#### Structural / Naming Corrections

| Location | Issue | Fix |
|---|---|---|
| §20.1 ingest path description | References `allis-ingest-api` and `allis-ingest-watcher` as the AAACPE pathway | **Update**: dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) supersedes legacy ingest path for Appalachian cultural data ★ |
| §20.7 GBIM table row counts | `gbim_worldview_entity: 5,415,896`; `gbim_graph_edges: 15,226,626`; etc. | Mark as **verify current** ★ — GBIM corpus has grown since April 13 |
| Live Stack Snapshot header | `April 13, 2026` | Update to **April 23, 2026** ★ |
| §20.12 `autonomous-learner` port | `8020 (stale ref: 8425)` | Retain as-is — no change needed |

#### Preflight Gate Check List Update (§20.1)

The nine-check list must be updated to reflect April 23 baselines:

| Old check | New check |
|---|---|
| 49 ChromaDB collections | **48 collections** ★ |
| `autonomous_learner ≥ 21,181` | **`autonomous_learner` ≥ ~23,200** ★ |
| `appalachian_cultural_intelligence ≥ 1,084` | **verify current** ★ |
| `research_history ≥ 785` | **verify current** ★ |
| `ms_allis_memory ≥ 296` | **verify current** ★ |
| `GBIM entities ≥ 5,416,521` | **verify current** ★ |
| `msallisgis` port 5435 checks | **Replace with `msallis-db:5433` production + `postgis-forensic:5452` forensic checks** ★ |

#### OI-36-A Note to Add (§20.2 or §20.4)

Add a paragraph noting that as of April 23, 2026, **OI-36-A is CLOSED** — Caddy `forward_auth` token enforcement is now active at the perimeter layer before any request reaches main-brain port 8050. The authentication note in §20.2 (`Authorization: Bearer $ALLIS_API_KEY` header) remains correct at the service level, but perimeter enforcement is now Caddy-first. ★

***

### Chapter 21 — `21-background-store-and-patterns.md`

**Last closed: April 13, 2026 — 10 days stale**

#### Quantitative Corrections

| Location | Stale Value | Correct Value |
|---|---|---|
| Opening paragraph; §21.1 opening; §21.7 port table; §21.8 bullets; §21.9 summary | **49 active collections, 6,722,589+ total vectors** across **109 running containers** | **48 active collections, ~6,740,611 total vectors** across **100 containers** ★ |
| §21.1 `ms_allis_memory` UUID note | "confirmed in the 49-collection inventory" | **48-collection inventory** ★ |
| §21.2 embedding constraint callout | "All 49 ChromaDB collections (6,722,589+ vectors)" | **48 collections, ~6,740,611 vectors** ★ |
| §21.3 ingest path first paragraph | "21 active — BakLLaVA eliminated, StarCoder2 excluded" | Retain; counts still correct |
| §21.3 `autonomous_learner` sentence | "reached **21,181 records**, growing approximately 288/day" | **~23,200+ records** ★ (grown ≈288/day from 21,181 April 14 baseline) |
| §21.3 External-Source Ingest Pathway | References `allis-ingest-api` + `allis-ingest-watcher` as operational | **Superseded** — dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) is now the authoritative AAACPE ingest path ★ |
| §21.4 ChromaDB full audit note | "49 active collections, 6,722,589+ total vectors across 109 running containers" | **48 collections, ~6,740,611 vectors, 100 containers** ★ |
| §21.5 `autonomous_learner` count | `21,181 records` | **~23,200+** ★ |
| §21.5 `conversation_history` | `564` | **Post-wipe count — wiped and reseeded clean April 16; count reflects post-wipe accumulation only** ★ |
| §21.6 GBIM promotion bullet | `msallisgis:5435`, 45 GB, 548 tables, 993 ZCTA centroids, 20,593 landowner beliefs | **Replace with two-container split**: production `msallis-db:5433` (16 GB, 294 tables, 11 schemas) + forensic `postgis-forensic:5452` (17 GB, 314 tables, 9 schemas); note landowner materialized view lives in production instance ★ |
| §21.7 port table — `msallisgis` row | port 5435, 45 GB, 548 tables, authoritative GBIM | **`msallis-db` host 5433** — production, 16 GB, 294 tables; add `postgis-forensic:5452` row ★ |
| §21.7 analytical path text | "`msallisgis:5435` (not `:5433`)" and all GBIM row counts | **Update to two-container split**; mark GBIM row counts as **verify current** ★ |
| §21.7 `msallisgis` ChronoDB collections note | "49 collections, 6,722,589+ vectors" | **48 collections, ~6,740,611 vectors** ★ |
| §21.8 consolidation bullet | "49 collections, 6,722,589+ vectors" | **48 collections, ~6,740,611 vectors** ★ |
| §21.8 GBIM tables bullet | `msallisgis:5435`, 45 GB, 548 tables | **Two-container split** ★ |
| §21.9 summary | 49 collections / 6,722,589+ vectors; `autonomous_learner` 21,181; `ms_allis_memory` 296 records; GBIM counts | Update all to April 23 baselines ★ |
| §21.9 authoritative collection baselines table | 49 collections; stale per-collection counts | Update total to **48 collections** ★; mark verify-current counts; `autonomous_learner` → **~23,200+**; `conversation_history` → **post-wipe count (see April 16 note)**; `local_resources` → **207** ★ |
| §21.11 scripts table | `preserve_memory_uuid.sh`: "296 docs" | **verify current** ★ |

#### Structural Correction

- §21.2 `memories` table location: still references `msallisgis:5435`. **Update** to `msallis-db` host **5433** (production instance) ★.
- §21.9 closing paragraph: references `msallisgis:5435`, 45 GB, 548 tables, 993 ZCTA centroids, 20,593 landowner beliefs. **Replace** with two-container split and mark GBIM row counts as verify-current ★.

***

### Chapter 22 — `22-identity-focused-retention.md`

**Last closed: April 12–13, 2026 — 10 days stale**

Chapter 22 is the least numerically dense of the three and has no direct container-count header or preflight snapshot. Most corrections are targeted.

#### Quantitative Corrections

| Location | Stale Value | Correct Value |
|---|---|---|
| §22.2.1 `conversation_history` | "at least 564 documented turns" | **Post-wipe count** — wiped and reseeded clean April 16, 2026; count reflects post-wipe accumulation only ★ |
| §22.9 Limitations paragraph | "92-container rebuild configuration; the 105-container thesis configuration" | **Update container counts**: April 23, 2026 production baseline is **100 containers** ★ |
| §22.12 Final Scoreboard | "49 services available in full pipeline — ✅ CLOSED" | **48 ChromaDB collections** ★ (score-board entry reflects stale 49 count — update label) |
| §22.1 / §22.7 inference stack | `llm_production` — 21/21 models | Retain ✅ — still correct |

#### Structural / Naming Corrections

| Location | Issue | Fix |
|---|---|---|
| §22.0 "By April 12–13, 2026" list | No mention of OI-36-A or two-container DB split | **Add bullet**: "OI-36-A CLOSED April 23, 2026 — Caddy `forward_auth` token enforcement now active at proxy level" ★ |
| §22.6 MountainShares / PostgreSQL references | `ms_user_profile`, `ms_participation` tables — no host/port specified | **Clarify**: these tables reside in the **production `msallis-db` host 5433** instance (not the retired single-container `msallisgis:5435`) ★ |
| Header / metadata block | "Last updated April 12–13, 2026" — missing `*Carrie Kidd*` italic line | **Add** standard author/date italic header consistent with Chs. 20–21 ★ |
| §22.10 UUID section (cross-reference) | Points to "Ch. 22 §22.10" — but §22.10 in the actual file is the **Cross-References** list, not the UUID risk section | **Renumber** or add a dedicated `§22.13 UUID Preservation Risk` section to match the cross-references in Chs. 19–21 ★ |
| §22.9 Limitations | Still references the "92-container rebuild configuration" as a limitation | **Remove** — this is now resolved; April 23 production baseline is 100 containers and this chapter should reflect closure ★ |

***

### Universal Corrections Applying to All Three Chapters

These apply identically to Chs. 20, 21, and 22 per `help.md`:

| Correction | Applies to |
|---|---|
| Container count → **100** ★ | Ch. 20 (everywhere), Ch. 21 (everywhere), Ch. 22 (§22.9) |
| ChromaDB → **48 collections** ★ | Ch. 20 (§20.1, §20.5), Ch. 21 (everywhere), Ch. 22 (§22.12) |
| Total vectors → **~6,740,611** ★ | Ch. 20 (§20.5), Ch. 21 (everywhere) |
| Two-container DB split replacing `msallisgis:5435` single-container | Ch. 20 (§20.7, §20.11, §20.12), Ch. 21 (§21.2, §21.6, §21.7, §21.8, §21.9), Ch. 22 (§22.6) |
| `autonomous_learner` → **~23,200+** ★ | Ch. 20 (§20.1), Ch. 21 (§21.3, §21.5, §21.9) |
| `conversation_history` — **post-wipe (April 16)** ★ | Ch. 21 (§21.5, §21.9 table), Ch. 22 (§22.2.1) |
| End-to-end timing → **102.58s** ★ | Ch. 20 (§20.3 `processing_time`) |
| OI-36-A CLOSED ★ | Ch. 20 (§20.2 / §20.4 — add note), Ch. 22 (§22.0 — add bullet) |
| AAACPE ingest path — dedicated stack supersedes legacy | Ch. 20 (§20.1), Ch. 21 (§21.3) |
| `local_resources` → **207 docs** ★ | Ch. 21 (§21.9 table) |
Now I have all three chapters. Here is the complete edit list for Chapters 23, 24, and 25.

***

## Edit List — Chapters 23, 24, and 25

All corrections apply the April 23, 2026 authoritative baseline from `help.md`. Items are sorted by chapter, then by priority (★ = critical baseline update).

***

### Chapter 23 — `23-dual-tracks-meaning-and-analysis.md`

**Last closed: April 12, 2026 — 11 days stale**

Chapter 23 is the most heavily numerically dense of the three. Nearly every static snapshot figure requires updating, and the chapter header, ASCII diagram, status table, and §23.7 summary all carry stale values.

#### Header / Metadata Block

| Location | Stale Value | Correct Value |
|---|---|---|
| `*Last updated:*` line; chapter header star note | "April 12, 2026: **92+ active containers**" | **100 containers** ★ |
| Chapter header star note | "ChromaDB **49 collections, 6,700,000+ vectors**" | **48 collections, ~6,740,611 vectors** ★ |
| Chapter header star note | "**msallisgis 548 tables, 45 GB PostGIS**" | **Two-container split** — see below ★ |

#### ASCII Architecture Diagram (Figure 23.1 and inline diagram)

Every quantitative annotation in the diagram block must be updated:

| Stale Annotation | Correct Annotation |
|---|---|
| `★ Updated April 12, 2026 — 92+ active containers` | **100 containers Up** ★ |
| `msallisgis:5432 ★ — 45 GB PostGIS, 548 tables` | **`msallis-db` host 5433 — 16 GB, 294 tables (production)** ★ |
| `msallis:5433 ★ — 5,416,521 GBIM entities` | **Retain port; mark GBIM row count as verify-current** ★ |
| `★ 49 collections, 6,700,000+ vec` (analytical path box) | **48 collections, ~6,740,611 vectors** ★ |
| `★ Health monitoring (★ 92+ containers Up)` (shared integration box) | **100 containers Up** ★ |
| `★ 49 collections, 6,700,000+ vectors` (shared integration box) | **48 collections, ~6,740,611 vectors** ★ |
| `PostgreSQL msallisgis (port 5432 ★)` (shared integration box) | **Replace with two-container split** ★ |
| `★ 5,416,521 GBIM beliefs (msallis:5433)` | Mark as **verify-current** ★ |
| `★ 45 GB PostGIS, 548 tables, 993 ZCTAs` | **Replace with two-container split** ★ |
| Figure 23.1 caption: "★ `msallisgis:5432`, 45 GB PostGIS, 548 tables, 993 ZCTA centroids; ★ `msallis:5433`, 5,416,521 GBIM entities" | **Two-container split; GBIM counts verify-current** ★ |
| Figure 23.1 caption: "★ 49 collections, 6,700,000+ vectors", "★ 92+ containers Up" | **48 collections, ~6,740,611 vectors; 100 containers** ★ |

#### Polymathmatic Geography Callout Block

| Location | Stale Value | Correct Value |
|---|---|---|
| P1 bullet | "ChromaDB background store (★ 49 collections, 6,700,000+ vectors)" | **48 collections, ~6,740,611 vectors** ★ |
| P1 bullet | "`msallisgis` (port **5432** ★, **45 GB PostGIS, 548 tables**, 993 ZCTA centroids)" | **Two-container split** ★ |
| P1 bullet | "`msallis` (port **5433** ★, 5,416,521 GBIM entities)" | Mark GBIM count as **verify-current** ★ |
| P5 bullet | "`msallisgis:5432` ★, 45 GB PostGIS, 548 tables, 993 ZCTA centroids" | **Two-container split** ★ |
| P12 bullet | "PostgreSQL `msallisgis` ★ and `msallis` ★" | **two-container split** ★ |

#### Status Table

| Row | Stale Value | Correct Value |
|---|---|---|
| Analytical path — PostgreSQL | "`msallisgis` at **127.0.0.1:5432** ★ (45 GB PostGIS, 548 tables, 993 ZCTA centroids)" | **`msallis-db` host 5433 — production, 16 GB, 294 tables; add `postgis-forensic:5452` forensic row** ★ |
| Analytical path — PostgreSQL | "`msallis` at **127.0.0.1:5433** ★ (5,416,521 GBIM entities)" | Port still correct; mark GBIM count as **verify-current** ★ |
| Analytical path — AAPCAppE | "`allis-ingest-api` + `allis-ingest-watcher`" | **Superseded by dedicated AAACPE stack** (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) ★ |
| Analytical path — ChromaDB | "49 collections, 6,700,000+ total vectors" | **48 collections, ~6,740,611 vectors** ★ |
| Critical routing note | "★ April 12, 2026 … 21 active proxies, 22 registered" | Container count bullet: **100 containers** ★ |

#### §23.1 Rationale

| Location | Stale Value | Correct Value |
|---|---|---|
| Meaning-oriented family — EEG Delta | "pulse_count: 12,860 … as of April 12" | Update to current PIA baseline; note this is a live metric — **remove hard-coded April 12 reading** ★ |
| Analytical family | "`msallisgis:5432` ★ — 45 GB PostGIS, 548 tables, 993 ZCTA centroids" | **Two-container split** ★ |
| Analytical family | "`allis-gis-rag` (port **8004** ★; queries PostgreSQL GeoDB `msallisgis:5432` ★)" | Queries **`msallis-db:5433`** production instance ★ |
| §23.1 last paragraph | "★ 92+ containers active" | **100 containers** ★ |

#### §23.2 Shared Structural Pattern

| Location | Stale Value | Correct Value |
|---|---|---|
| Background storage paragraph | "`ms_allis_memory` ChromaDB (UUID: `79240788...`, ★ confirmed in **49**-collection inventory April 12; ★ total ChromaDB: **49** collections, **6,700,000+** vectors)" | **48-collection inventory; ~6,740,611 vectors** ★ |
| First-stage filtering | "`msallis:5433` ★ (5,416,521 entities)" | Mark GBIM count as **verify-current** ★ |

#### §23.4 Analytical Path

| Location | Stale Value | Correct Value |
|---|---|---|
| RAG context paragraph | "`allis-gis-rag` (port **8004** ★; queries spatial tables from `msallisgis:5432` ★ — 45 GB PostGIS, 548 tables, 993 ZCTA centroids)" | Queries **`msallis-db:5433`** (production, 16 GB, 294 tables) ★ |
| Synthesis paragraph | "`background_rag_store` writes to `ms_allis_memory` ChromaDB (★ 49 collections, 6,700,000+ total vectors)" | **48 collections, ~6,740,611 vectors** ★ |
| GBIM landowner paragraph | "`msallisgis:5432` ★ and `msallis:5433` ★" | **two-container split** ★ |

#### §23.5 Cross-Talk

| Location | Stale Value | Correct Value |
|---|---|---|
| Shared background store paragraph | "★ 49 collections, 6,700,000+ vectors as of April 12" | **48 collections, ~6,740,611 vectors** ★ |
| PostgreSQL as shared ground truth | "`msallisgis` (port **5432** ★, 45 GB PostGIS, 548 tables, 993 ZCTA centroids)" | **Two-container split** ★ |
| PostgreSQL as shared ground truth | "`msallis` (port **5433** ★, 5,416,521 GBIM entities)" | Mark GBIM count as **verify-current** ★ |
| EEG Delta PIA health signal | "pulse_count: 12,860 … as of April 12" | Remove hard-coded April 12 reading; note as **live metric** ★ |
| Unified health monitoring | "92+ active containers" | **100 containers** ★ |

#### §23.6 Influence on Behavior

- §23.6 diagnostics paragraph: "`msallisgis:5432` ★" → **two-container split** ★
- §23.6 EEG Delta reference: remove hard-coded April 12 reading ★

#### §23.7 Summary

Every quantitative statement in the summary paragraph requires updating:

| Stale | Correct |
|---|---|
| "21 active proxies, 22 registered" | Retain ✅ |
| "`msallisgis:5432` (45 GB PostGIS, 548 tables, 993 ZCTA centroids)" | **Two-container split** ★ |
| "`msallis:5433` (5,416,521 GBIM entities)" | Mark as **verify-current** ★ |
| "`ms_allis_memory` ChromaDB (49 collections, 6,700,000+ vectors)" | **48 collections, ~6,740,611 vectors** ★ |
| "EEG Delta band (port 8073) PIA signal (`pulse_count: 12,860`, …)" | Remove hard-coded reading; note as **live metric** ★ |
| "92+ active containers" (final line) | **100 containers** ★ |

#### Automated Commands Block (§ at chapter end)

| Command | Update needed |
|---|---|
| `# 1. Active container count (update §23.1 table if different from 92)` | Update expected to **100** ★ |
| `# 4. PostgreSQL msallisgis — table count and DB size` | Update expected host/port: **`-p 5433 -d msallis`** (production) + add forensic check at **5452** ★ |
| Footer star note | "92+ active containers"; "49 collections, 6,700,000+ vectors"; "msallisgis updated to 548 tables, 45 GB" | **100 containers; 48 collections, ~6,740,611 vectors; two-container split** ★ |

#### OI-36-A Note to Add

Add a paragraph or table row noting that **OI-36-A is now CLOSED at the Caddy perimeter layer** — `forward_auth` token enforcement is active before any request reaches main-brain port 8050. The bearer token note in §23.4 and §23.5 remains correct at the service level, but perimeter enforcement is now Caddy-first as of April 23, 2026 ★.

***

### Chapter 24 — `24-feedback-into-broader-layers.md`

**Last closed: April 12, 2026 — 11 days stale. Explicitly scoped to the 92-container rebuild stack.**

Chapter 24 has the most self-aware stack-scoping language of the three ("92-container rebuild stack"), but every quantitative baseline now requires updating to the April 23 production state.

#### Header / Metadata Block

| Location | Stale Value | Correct Value |
|---|---|---|
| `*Last updated:*` line | "92-container rebuild stack … Container count corrected to **92**" | **100 containers** ★ |
| Top revision note | "gisdb updated to **551 public tables**" | **two-container split** ★ |
| Top revision note | "ChromaDB updated to **49 collections, 6,722,589+ vectors**" | **48 collections, ~6,740,611 vectors** ★ |
| Top revision note | "local_resources confirmed **101** items" | **207 items** ★ |
| `> Stack scope note` | "92-container rebuild configuration … 105-container thesis stack" | Update container count to **100** ★; retain the thesis-stack cross-reference language as still valid |

#### Polymathmatic Geography Callout Block

| Location | Stale Value | Correct Value |
|---|---|---|
| P1 bullet | "ChromaDB (★★ **49 collections, 6,722,589+ total vectors**)" | **48 collections, ~6,740,611 vectors** ★ |
| P1 bullet | "`msallisgis` (port **5432**, **551 public tables**, 993 ZCTA centroids)" | **Two-container split** ★ |
| P3 bullet | "`allis-memory:8056`" | Retain; still accurate |
| P12 bullet | "`local_resources` (101 items, all 55 WV counties)" | **207 items** ★ |

#### ASCII Architecture Diagram (Figure 24.1)

| Stale Annotation | Correct Annotation |
|---|---|
| `★★ Updated April 12, 2026 — 92 containers Up (92-container rebuild stack)` | **100 containers Up** ★ |
| `PostgreSQL msallisgis (port 5432) — 993 ZCTA centroids, 551 public tables` | **Two-container split** ★ |
| `PostgreSQL msallis (port 5433) — 5,416,521 GBIM entities` | Mark GBIM count as **verify-current** ★ |
| `ChromaDB (127.0.0.1:8002→8000) — 49 collections, 6,722,589+ vectors` | **48 collections, ~6,740,611 vectors** ★ |
| `local_resources: 101 items, 55 WV cntys` | **207 items** ★ |
| `msallis_docs: 7,465 items (Apr 12)` | **verify current** ★ |
| `AAPCAppE pipeline (ingest-api + watcher)` | **Superseded** by dedicated AAACPE stack ★ |
| Figure 24.1 caption: "551 public tables, 993 ZCTA centroids … 49 collections, 6,722,589+ total vectors … 92-container rebuild stack" | **Two-container split; 48 collections, ~6,740,611 vectors; 100 containers** ★ |

#### Status Table

| Row | Stale Value | Correct Value |
|---|---|---|
| Stack configuration | "**92 containers Up**" | **100 containers Up** ★ |
| ChromaDB | "**49 collections, 6,722,589+ total vectors**" | **48 collections, ~6,740,611 vectors** ★ |
| msallisgis | "PostgreSQL at **127.0.0.1:5432** — **551 public tables**" | **Two-container split**: production `msallis-db:5433` (16 GB, 294 tables) + forensic `postgis-forensic:5452` (17 GB, 314 tables) ★ |
| msallis | "**5,416,521 GBIM entities**" | Mark as **verify-current** ★ |
| msallis_docs | "**7,465 items** as of April 12" | **verify current** ★ |
| local_resources | "**101 items, all 55 WV counties seeded**" | **207 items** ★ |
| mvw_gbim_landowner_spatial | "**20,593 rows**" | Mark as **verify-current** ★ |
| RAG example | Fayette County food pantry description | Retain — still valid ✅ |
| Gate enforcement | "Chroma collections ≥ 40 (49 found)" | Update to **≥ 40 (48 found)** ★; `local_resources` gate → **≥ 207** ★ |

#### §24.1 Overview

| Location | Stale Value | Correct Value |
|---|---|---|
| Long-term memory paragraph | "**49 confirmed collections** and **6,722,589+ total vectors**" | **48 collections, ~6,740,611 vectors** ★ |
| Long-term memory paragraph | "`msallisgis` at **127.0.0.1:5432** (551 public tables, 993 ZCTA centroids)" | **Two-container split** ★ |
| Long-term memory paragraph | "`local_resources` (101 items, all 55 WV counties)" | **207 items** ★ |
| Long-term memory paragraph | "AAPCAppE ingest pipeline (`allis-ingest-api` + `allis-ingest-watcher`)" | **Dedicated AAACPE stack** ★ |
| §24.1a Consciousness Pipeline | "`chromadb_context` … 49 collections, 6,722,589+ total vectors" | **48 collections, ~6,740,611 vectors** ★ |

#### §24.2 Introspective Records

- `getdatabasehealth` paragraph: "`msallisgis:5432`, 551 public tables, 993 ZCTA centroids" → **two-container split** ★
- System Verification Reports paragraph: "551 public tables … 49 collections, 6,722,589+ vectors" → **two-container split; 48 collections, ~6,740,611 vectors** ★
- §24.2a gate list: update Chroma gate to **48**; `local_resources` gate to **≥ 207** ★

#### §24.3 Long-Term Memory

| Location | Stale Value | Correct Value |
|---|---|---|
| Primary feedback collection | "confirmed in 49-collection inventory" | **48-collection inventory** ★ |
| PostgreSQL msallisgis | "`msallisgis:5432` (551 public tables, 993 ZCTA centroids)" | **Two-container split** ★ |
| Chroma collections list | "**49 collections** … **6,722,589+** … `local_resources` (**101 items**, all 55 WV counties seeded)" | **48 collections; ~6,740,611 vectors; 207 items** ★ |
| AAPCAppE pathway | "`allis-ingest-api` + `allis-ingest-watcher`" | **Dedicated AAACPE stack** ★ |
| `msallis_docs` item count | "7,465 items as of April 12" | **verify current** ★ |

#### §24.4 Global Settings

- §24.4a AU-02 v2: no data changes needed ✅
- §24.4b EEG: no change needed ✅
- §24.4c `allis-memory:8056`: no change needed ✅
- §24.4d Judge pipeline: no change needed ✅

#### §24.5 Cross-Path Effects

- All `msallisgis:5432` references → **two-container split** ★
- `local_resources` (101 items) → **207 items** ★
- `msallis_docs` (7,465 items) → **verify current** ★
- `⚠️ neuro_master status` callout: note still valid; retain as historical context ✅

#### §24.6 Logging / Audit

- "ChromaDB collections (49 collections, 6,722,589+ vectors)" → **48 collections, ~6,740,611 vectors** ★
- "`msallisgis:5432` — 551 public tables, 993 ZCTA centroids" → **two-container split** ★
- Gate enforcement logs paragraph: update Chroma gate to **48**, `local_resources` gate to **≥ 207** ★

#### §24.7 Summary

| Location | Stale Value | Correct Value |
|---|---|---|
| Bullet 1 (introspective) | "`msallisgis` (551 public tables, 993 ZCTA centroids)" | **Two-container split** ★ |
| Bullet 2 (long-term memory) | "ChromaDB (49 collections, 6,722,589+ vectors … `msallis_docs` 7,465 items, `local_resources` 101 items, all 55 WV counties)" | **48 collections, ~6,740,611 vectors; local_resources 207 items** ★ |
| AAPCAppE reference | "`allis-ingest-api` + `allis-ingest-watcher`" | **Dedicated AAACPE stack** ★ |
| Chapter header "92 containers" | All references | **100 containers** ★ |

***

### Chapter 25 — `25-consciousness-coordinator-and-services.md`

**Sealed: April 12, 2026 — 11 days stale. This is a formal SEAL document.**

Chapter 25 uses a sealed/closed format with a formal infrastructure state table. The seal is a historical record, so the strategy here is different: **do not alter the seal record itself** — instead, add a brief `§25.0a — Post-Seal Baseline Update (April 23, 2026)` section immediately after §25.0, noting the changes without rewriting the closed verification outputs.

#### Structural Correction — Add §25.0a

Add a new section between §25.0 and §25.1:

```
## §25.0a — Post-Seal Baseline Update (April 23, 2026)

The seal record in §25.1–§25.11 reflects the April 12, 2026 state at chapter close
and is preserved as-is. The following corrections apply the April 23, 2026 production
baseline and supersede the §25.1 table values for any forward references.
```

Followed by an update table:

| §25.1 Metric | Sealed Value | April 23, 2026 Baseline |
|---|---|---|
| Active containers | 92 | **100** ★ |
| ChromaDB collections | 49 | **48** ★ |
| Vector embeddings | 6,722,589+ | **~6,740,611** ★ |
| PostgreSQL gisdb tables | 551 (`msallisgis` public schema) | **Two-container split**: production `msallis-db:5433` (294 tables, 16 GB); forensic `postgis-forensic:5452` (314 tables, 17 GB) ★ |
| neuro_master processes | 131 | **verify current** ★ |

#### §25.2 Open Items Closure Register

| OI # | Correction |
|---|---|
| OI-36-A | Entry reads "allis-auth port 8055 — ✅ CLOSED". **Add note**: OI-36-A is now also closed at the Caddy perimeter layer — `forward_auth` token enforcement is active before any request reaches main-brain ★ |

#### §25.7 Port Map

| Row | Stale Value | Correction |
|---|---|---|
| `allis-chroma` host binding | `127.0.0.1:8001, 127.0.0.1:8002` | Retain ✅ — still correct |
| No `msallis-db` or `postgis-forensic` rows present | — | **Add note in §25.0a** that these two containers replaced the single `msallisgis:5432` instance ★ |

#### §25.10 Sprint Timeline

No changes required — this is a historical log. ✅

#### §25.11 Chapter 26 Pre-Conditions

| Item | Correction |
|---|---|
| "gisdb at 551 tables (up from 501 at chapter open)" | **Add note in §25.0a**: replaced by two-container split ★ |
| "Embedding model consistent … across all **49** collections" | **Add note in §25.0a**: **48** collections as of April 23 ★ |

***

### Universal Corrections Applying to All Three Chapters

| Correction | Ch. 23 | Ch. 24 | Ch. 25 |
|---|---|---|---|
| Container count → **100** ★ | Header, diagram, §23.1, §23.5, §23.7 | Header, table, §24.1–§24.7 | §25.0a (post-seal note) |
| ChromaDB → **48 collections** ★ | Everywhere | Everywhere | §25.0a |
| Total vectors → **~6,740,611** ★ | Everywhere | Everywhere | §25.0a |
| Two-container DB split replacing `msallisgis:5432` ★ | §23.1, §23.2, §23.4, §23.5, §23.7, diagram | §24.1–§24.7, diagram, table | §25.0a, §25.7 note |
| `local_resources` → **207 items** ★ | N/A | §24.1, §24.3, §24.5, §24.6, §24.7, table | N/A |
| `msallis_docs` → **verify current** ★ | §23.5 mention | §24.1, §24.3, §24.5, table | N/A |
| AAPCAppE → dedicated AAACPE stack ★ | §23.4, §23.5, status table | §24.1, §24.3, §24.7 | N/A |
| OI-36-A Caddy perimeter closure note ★ | Add §23.4/§23.5 | §24.2a gate list update | §25.2 OI-36-A row |
| EEG Delta hard-coded readings → **live metric note** ★ | §23.1, §23.5, §23.6, §23.7 | N/A | N/A |
| GBIM entity row counts → **verify-current** ★ | §23.2, §23.4, §23.5, §23.7 | §24.1, §24.2, §24.3, §24.4 | §25.0a |
