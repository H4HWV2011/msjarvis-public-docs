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
