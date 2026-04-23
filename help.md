Here is the complete edit list for Chapters 26, 27, and 28.

***

## Edit List — Chapters 26, 27, and 28

All corrections apply the April 23, 2026 authoritative baseline. The stale closed dates are: Ch. 26 — April 10, 2026 (13 days); Ch. 27 — April 10, 2026 (13 days); Ch. 28 — April 9, 2026 (14 days).

***

### Chapter 26 — `26-temporal-toroidal-semaphore-structure.md`

**Last updated: April 10, 2026 — 13 days stale**

Chapter 26 carries two distinct numerical baselines that are now stale: the container count ("105 containers Up") which was itself a correction from 96 at chapter open, and all ChromaDB/PostgreSQL figures. Additionally this chapter uses "AAPCAppE" (`allis-ingest-api` + `allis-ingest-watcher`) which has been superseded.

#### Header / Metadata Block

| Location | Stale Value | Correct Value |
|---|---|---|
| `*Last updated:*` star note | "**105 containers Up** (updated from 96)" | **100 containers** ★ |
| `*Last updated:*` star note | "**49** ChromaDB collections / **6,722,589+ vectors**" | **48 collections, ~6,740,611 vectors** ★ |
| March 28 baseline note | "`msallisgis:5432` confirmed (**91 GB PostGIS, 501 tables**, 993 ZCTA centroids)" | **Two-container split** ★ |

#### Opening Paragraph (§26.0 preamble)

| Stale Value | Correct Value |
|---|---|
| "★★★ confirmed OPERATIONAL … **105 containers Up**" | **100 containers** ★ |
| "ChromaDB-backed semantic memory (★★★ **49 collections, 6,722,589+ vectors**)" | **48 collections, ~6,740,611 vectors** ★ |
| "`msallisgis:5432` ★ **91 GB PostGIS, 501 tables**, 993 ZCTA centroids" | **Two-container split** ★ |
| "`msallis:5433` ★ **5,416,521 entities**" | Mark GBIM count as **verify-current** ★ |
| "autonomous learning (★★ **68 Chroma items**, 11 entanglement nodes confirmed April 1)" | Mark as **verify-current** (growing collection) ★ |

#### §26.1 Temporal Structure

**Short-term section:**
- "★★★ With **105 containers Up**" → **100 containers** ★
- "EEG beta rhythm (5-minute cadence; ★★ confirmed operational April 1 — **68 Chroma items**, 15 cycles, 11 entanglement nodes)" → Mark item count and cycle telemetry as **verify-current** ★

**Medium-term section:**
- "ChromaDB (★★★ **49 collections, 6,722,589+ vectors**) via the ★★★ correct host port **8002**" → **48 collections, ~6,740,611 vectors** ★
- "`msallisgis:5432` ★" → **Two-container split** ★
- "AAPCAppE (`allis-ingest-api` + `allis-ingest-watcher`) … `msallis_docs` (4,192 items)" → **Dedicated AAACPE stack** (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`); `msallis_docs` item count → **verify current** ★
- "`appalachian_english_corpus` scraper adds a second always-on medium-term ingest: **210 documents**" → Mark as **verify-current** (growing) ★

**Long-term section:**
- "ChromaDB (★★★ **49 active collections, 6,722,589+ total vectors**)" → **48 collections, ~6,740,611 vectors** ★
- "`msallis_docs` (★ **4,192 items**)" → **verify current** ★
- "`appalachian_english_corpus` (★★★ **210 docs**, live)" → **verify-current** ★
- "`autonomous_learner` (★★ **68 items** confirmed live, growing)" → **verify-current** ★
- "per-request pipelines (★★★ **105 containers Up**)" → **100 containers** ★
- "`msallis:5433` ★ GBIM (5,416,521 entities)" → mark as **verify-current** ★

#### §26.2 Toroidal Structure

**Cyclic passes section:**
- "★★★ As of April 10, 2026: **105 containers Up**" → **100 containers** ★

**Recurrent sweeps section:**
- "`msallisgis:5432` ★ (501 tables, 993 ZCTA centroids)" → **Two-container split** ★
- `msallis:5433` ★ GBIM entities → mark as **verify-current** ★

**AAPCAppE / appalachian_english_corpus section:**
- "AAPCAppE pipeline … flow into `msallis_docs` (**4,192 items**)" → **Dedicated AAACPE stack**; item count → **verify current** ★
- "`appalachian_english_corpus` (**210 docs**, growing)" → **verify-current** ★

**AU-02 v2 section:**
- "`msallis:5433` ★ GBIM entities, AU-02 v2 incorporates … entanglement node density … (★★ **11 nodes** in 15 cycles, April 1)" → Mark telemetry as **verify-current** ★
- "`msallis:5433` ★ GBIM entities (**5,416,521 beliefs**)" → **verify-current** ★

#### §26.3 Semaphore Structure

**LLM fabric section:**
- "★★★ With **105 containers Up**" → **100 containers** ★

**Mode flags section:**
- "(★★★ **105 containers Up**, all NBB/bridge/consciousness open items closed, **49 ChromaDB collections, 6,722,589+ vectors**" → **100 containers; 48 collections, ~6,740,611 vectors** ★

#### §26.4 Interaction Between the Three Views

| Location | Stale Value | Correct Value |
|---|---|---|
| Temporal–gate paragraph | "AAPCAppE continuous ingest … ★★★ 49 collections, 6,722,589+ vectors; `msallis:5433` ★ 5,416,521 GBIM" | **AAACPE stack; 48 collections, ~6,740,611 vectors; verify-current GBIM** ★ |
| Temporal–gate paragraph | "★★★ With **105 containers Up**" | **100 containers** ★ |
| Toroidal loops paragraph | "`msallis_docs` (★ **4,192 items**), `appalachian_english_corpus` (★★★ **210 docs**, growing)" | **verify-current** ★ |
| Toroidal loops paragraph | "`msallisgis:5432` ★" | **Two-container split** ★ |
| `autonomous_learner` (★★ **68 items** and growing) | **verify-current** ★ |
| Final summary paragraph | "★★★ The April 10, 2026 state — **105 containers Up** … **49 ChromaDB collections, 6,722,589+ vectors**" | **100 containers; 48 collections, ~6,740,611 vectors** ★ |

#### §26.5 Implications

| Location | Stale Value | Correct Value |
|---|---|---|
| Scheduling paragraph | "AAPCAppE continuous ingest (`allis-ingest-api` + `allis-ingest-watcher`) … 6-hour cron" | **AAACPE stack** ★ |
| Scheduling paragraph | "With **105 containers Up**" | **100 containers** ★ |
| Community control surfaces paragraph | "★★★ The April 10, 2026 state — all consciousness open items closed, **105 containers Up**" | **100 containers** ★ |

#### Footer Star Notes

| Stale Value | Correct Value |
|---|---|
| "★★★ April 10, 2026 … **105 containers**, 49 collections, 6,722,589+ vectors" | **100 containers; 48 collections, ~6,740,611 vectors** ★ |
| "★ March 28, 2026: `msallisgis:5432` confirmed (**91 GB PostGIS, 501 tables**, 993 ZCTA centroids)" | **Two-container split** ★ |

#### OI-36-A Note to Add

Chapter 26 does not currently mention OI-36-A closure at the Caddy perimeter layer. Add a brief note in §26.3 (Semaphore Structure), in the "Mode and flag-based routing" subsection or as a new bullet: **OI-36-A is now closed at the Caddy `forward_auth` perimeter layer** — bearer token enforcement operates before any request reaches main-brain port 8050. This is a new semaphore layer added at the perimeter since the chapter's April 10 close date ★.

***

### Chapter 27 — `27-web-research-and-autonomy.md`

**Last updated: April 10, 2026 — 13 days stale. Chapter 27's internal baseline is notably inconsistent: the header says "107 containers Up" while Chapter 26 sealed at "105 Up." This reflects two different snapshots on April 9–10. The April 23 baseline is 100 containers.**

#### Header / Metadata Block

| Location | Stale Value | Correct Value |
|---|---|---|
| `*Last updated:*` note | "container count updated to **107 Up** (was 96)" | **100 containers** ★ |
| `*Last updated:*` note | "ChromaDB inventory updated to **49 collections / 6,722,683 vectors**" | **48 collections, ~6,740,611 vectors** ★ |
| Correction table row | "Container count: 96 Up → **107 Up**" | **100 containers** ★ |
| Correction table row | "ChromaDB: **49 collections, 6,722,683 vectors**" | **48 collections, ~6,740,611 vectors** ★ |

#### Polymathmatic Geography Callout Block

| Location | Stale Value | Correct Value |
|---|---|---|
| P1 bullet | "ChromaDB (★★★ **49 collections, 6,722,683 total vectors**)" | **48 collections, ~6,740,611 vectors** ★ |
| P1 bullet | "`msallisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids)" | **Two-container split** ★ |
| P1 bullet | "`msallis` (port **5433** ★, **5,416,521 GBIM entities**)" | Mark as **verify-current** ★ |
| P5 bullet | "`msallisgis:5432` ★, 91 GB PostGIS, 501 tables, 993 ZCTA centroids" | **Two-container split** ★ |
| P12 bullet | "`msallis_docs` (**4,192 items**)" | **verify current** ★ |
| P12 bullet | "`appalachian_english_corpus` live at **210 documents**" | **verify-current** ★ |

#### ASCII Architecture Diagram (Figure 27.1)

| Stale Annotation | Correct Annotation |
|---|---|
| `★★★ Updated April 10, 2026 — 107 containers Up` | **100 containers Up** ★ |
| `49 collections / 6,722,683 vecs` | **48 collections, ~6,740,611 vectors** ★ |
| `AAPCAppE ingest ★ / allis-ingest-api + ingest-watcher ★` | **AAACPE stack** (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) ★ |
| `appalachian_english_corpus: 210 docs / cron 0 */6 * * *` | Mark as **verify-current (growing)** ★ |
| `msallis_docs (4,192 items AAPCAppE)` | **verify current; AAACPE** ★ |
| `★★★ 49 total, 6,722,683 vectors` | **48 collections, ~6,740,611 vectors** ★ |
| `PostgreSQL msallisgis:5432 ★` | **Two-container split** ★ |
| Figure 27.1 caption: "★★★ 49 collections, 6,722,683 total vectors … AAPCAppE … 107 containers Up" | **48 collections, ~6,740,611 vectors; AAACPE stack; 100 containers** ★ |

#### Status Table

| Row | Stale Value | Correct Value |
|---|---|---|
| Implemented now — container count | "★★★ **107 containers Up**" | **100 containers** ★ |
| Implemented now — ChromaDB | "★★★ **49 active collections, 6,722,683 total vectors**" | **48 collections, ~6,740,611 vectors** ★ |
| Implemented now — `appalachian_english_corpus` | "**210 documents** seeded … 6-hour cron active" | Mark as **verify-current (growing)** ★ |
| Implemented now — `msallis_docs` | "**4,192 items**" | **verify current** ★ |
| Implemented now — AAPCAppE | "`allis-ingest-api` + `allis-ingest-watcher`" | **AAACPE stack** ★ |
| Future work — judge upgrade | "`msallisgis:5432` ★ and `msallis:5433` ★" | **Two-container split** ★ |

#### §27.1 Role of Periodic Web Research

- Background updating paragraph: "AAPCAppE ingest pipeline (`allis-ingest-api` + `allis-ingest-watcher` …)" → **AAACPE stack** ★
- Background updating paragraph: "`appalachian_english_corpus` (**210 documents**, 38 sources) is live" → **verify-current** ★
- `appalachian_english_corpus` curiosity paragraph: "(**210 documents**, top contributors …)" → **verify-current (210 at chapter seal; growing)** ★
- `msallis_docs` item count throughout: "**4,192 items**" → **verify current** ★

#### §27.2 Scheduling, Cadence, and Logging

- "As of March 14 baseline, the `autonomous_learner` ChromaDB collection contains **21,181 records growing ≈288/day**" → Mark as **verify-current** ★ (collection is confirmed growing)
- ChromaDB queries paragraph: "**host port 8002** (container port 8000; **49 collections, 6,722,683 total vectors**)" → **48 collections, ~6,740,611 vectors** ★

#### §27.3 Topic Selection

- "ChromaDB (via ★★★ host port **8002**; **49 collections, 6,722,683 vectors**)" → **48 collections, ~6,740,611 vectors** ★
- "`msallisgis:5432` ★, 501 tables, 993 ZCTA centroids" → **Two-container split** ★
- `appalachian_english_corpus` paragraph: "(**210 documents**, 38 sources, self-refreshing every 6 hours)" → **verify-current** ★

#### §27.4 Retrieval, Filtering, and Deduplication

- Internal retrieval paragraph: "`msallis_docs` (★ **4,192 items**, AAPCAppE)" → **AAACPE stack; verify current item count** ★
- External retrieval paragraph: "AAPCAppE scraper … runs every 6 hours via cron" → **AAACPE stack** ★

#### §27.5 Integration with Memory and Spatial Layers

- PostgreSQL write paragraph: "`msallisgis` ★ (**91 GB PostGIS, 501 tables**, 993 ZCTA centroids)" → **Two-container split** ★
- Spatial integration paragraph: "ChromaDB (★★★ host port **8002**; **49 collections, 6,722,683 vectors**)" → **48 collections, ~6,740,611 vectors** ★

#### §27.6 Interaction with Container and Governance Paths

- "ChromaDB (★★★ **49 collections, 6,722,683 vectors**)" → **48 collections, ~6,740,611 vectors** ★

#### §27.7 Safeguards and Oversight

- "★★★ As of April 10, 2026: **107 containers Up**" → **100 containers** ★
- Logging paragraph: "`appalachian_english_corpus` at **210 docs** and growing every 6 hours; `msallis_docs` at **4,192 items**" → **verify-current** ★

#### §27.8 Web Research in the ULTIMATE Path

- "`msallisgis:5432` ★ and `msallis:5433` ★ (5,416,521 beliefs)" → **Two-container split; verify-current GBIM** ★
- Latency paragraph: "With **107 containers Up**" → **100 containers** ★

#### §27.9 Summary

| Location | Stale Value | Correct Value |
|---|---|---|
| Opening sentence | "`msallisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids)" | **Two-container split** ★ |
| Opening sentence | "`msallis` (port **5433** ★, **5,416,521 GBIM entities**)" | **verify-current** ★ |
| Opening sentence | "ChromaDB (★★★ **49 active collections, 6,722,683 total vectors**)" | **48 collections, ~6,740,611 vectors** ★ |
| Second paragraph | "★★★ **confirmed 6-filter BBB stack** … `allis-memory:8056`" | Retain ✅ |
| Milestones paragraph | "`appalachian_english_corpus` live … (**210 documents**, 38 sources)" | **verify-current** ★ |
| Final paragraph | "96/96 Up" | **100 containers** ★ — also update to note this was superseded |

#### Footer Star Notes

| Stale Value | Correct Value |
|---|---|
| "★★★ April 9–10, 2026 … **107 containers Up**; ChromaDB at host:8002→container:8000 corrected" | **100 containers** ★ |
| "★ March 28 … 96/96 Up; `msallisgis:5432` ★ confirmed (**91 GB PostGIS, 501 tables**, 993 ZCTA centroids)" | **Two-container split** ★ |

***

### Chapter 28 — `28-heartbeat-and-live-cycles.md`

**Last updated: April 9, 2026 — 14 days stale. Chapter 28 has the oldest close date of the three and carries multiple stale container counts (96 Up throughout, with "96/96 Up" as the highest confirmed baseline) along with stale ChromaDB and PostgreSQL figures. Additionally, the `msallisgis:5432` single-database references are pervasive.**

#### Header / Metadata Block

| Location | Stale Value | Correct Value |
|---|---|---|
| `*Last updated:*` note | No container update note for April 23 | **Add: April 23, 2026 — 100 containers Up (supersedes 96/96 Apr 1 baseline)** ★ |
| March 28 note | "`msallisgis` port 5432 confirmed (**91 GB PostGIS, 501 tables**, 993 ZCTA centroids)" | **Two-container split** ★ |

#### Why This Matters Callout Block

| Location | Stale Value | Correct Value |
|---|---|---|
| P5 bullet | "`msallisgis:5432`, 91 GB PostGIS, 501 tables, 993 ZCTA centroids … `msallis:5433`, 5,416,521 entities" | **Two-container split; GBIM verify-current** ★ |
| P12 bullet | "`msallis_docs` (**4,192 items**, AAPCAppE)" | **AAACPE stack; verify current item count** ★ |
| P12 bullet | "`autonomous_learner` collection (**68 items**, April 1, 2026)" | Mark as **verify-current (growing)** ★ |

#### §28.1 Purpose of Heartbeat and Live Signals

| Location | Stale Value | Correct Value |
|---|---|---|
| Liveness paragraph | "★★★ As of April 9 … ChromaDB collection count corrected to **49**" | Still accurate ✅ — retain |
| Liveness paragraph | "★ As of March 28, 2026 … **96/96 containers Up**" | Add note: **superseded by 100 containers (April 23)** ★ |
| Pinned baseline note | "★★ The **April 1, 2026 state** (96/96 Up re-confirmed … **68 Chroma items** / 15 cycles / 11 entanglement nodes) is the current verified operational milestone" | Add: **Superseded by April 23, 2026 baseline: 100 containers Up** ★ |
| Monitoring paragraph | "It verifies ChromaDB reachability via **127.0.0.1:8000** (★★★ **49 collections** … **6,732,980** total vectors per `chroma-latest` backup)" | Update vector count to **~6,740,611** ★ |

#### §28.1a Learning Status

- Learner live telemetry block (15 cycles / 68 items / 11 nodes): These are confirmed historical baselines (April 1, 2026). Add a note that these are **floor values** and the collection is growing ★
- Section 12 probe comment: "Baseline: ≥ **68** as of April 1, 2026" → Update gate to **≥ 68 (floor — verify current count)** ★

#### §28.2 Core Heartbeat Mechanisms

| Location | Stale Value | Correct Value |
|---|---|---|
| `/selftestfabric` list | "★★ **96/96 Up** (April 1, 2026)" | **100 containers Up** ★ |
| Individual service endpoints | No changes needed — port list is still accurate ✅ |
| VERIFYANDTEST.sh Section 7 | "ChromaDB at **127.0.0.1:8000** (★★★ **49 collections**, **6,732,980** total vectors)" | Update vector count to **~6,740,611** ★ |
| VERIFYANDTEST.sh Section 7 | "`msallisgis` — 501 tables, 993 ZCTA centroids" | **Two-container split** ★ |
| VERIFYANDTEST.sh Section 6 | "★★ **96/96 Up** (April 1, 2026)" | **100 containers** ★ |
| Section 9 planned extension | "★★★ **49 collections** as of April 9; per-collection counts; zero-count flag check" | Retain — still accurate ✅ |
| Divergence thresholds | "ChromaDB collections below **45**" | Update to **below 44** (reflecting 48-collection current baseline) ★ |

#### §28.3 LLM Ensemble Heartbeat

- The ensemble table (OLLAMA_NUM_PARALLEL, semaphore slots, etc.) — no changes needed ✅
- "LLaMA 3.1 confirmed active April 1, 2026" — retain as historical note ✅

#### §28.4 EEG Rhythm Services

- Beta learner restored paragraph: "★★ Operationally restored April 1, 2026" — retain as accurate ✅
- Telemetry in EEG status table: "**68 Chroma items** confirmed live (April 1, ~3:37 PM EDT); 15 cycles / 15 stored; 0 deduplicated; 11 entanglement nodes" → Add note: **floor values as of April 1 — collection actively growing** ★
- AAPCAppE row in EEG table: "`allis-ingest-api` + `allis-ingest-watcher`" → **AAACPE stack** ★

#### §28.7 Semantic Memory and GBIM Heartbeat

| Location | Stale Value | Correct Value |
|---|---|---|
| §28.7a collection table — `appalachian_english_corpus` | "⚠️ Zero count — **flagged for reseed in Ch 29**" | **Resolved in Ch 27 (210 docs, AAACPE clean recreate April 9)** ✅ — update status row ★ |
| §28.7a collection table — `msallis_docs` (second row, unknown count) | "Unknown count — flagged for verification in Ch 29" | **Resolved — 4,192 items as of April 9** ✅ ★ |
| §28.7b backup inventory table | "`chroma-latest`: **49 collections, 6,732,980**" | Update vector count to **~6,740,611** ★ |
| GBIM cross-database paragraph | "`msallisgis` (port **5432**, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids)" | **Two-container split** ★ |
| GIS RAG health paragraph | "connection to `msallis:5433`, `msallisgis:5432`" | **Two-container split** ★ |

#### §28.8 Integration with Memory and Containers — Operational Baseline Table

This table is a historical log with explicit dates. Add a new `★★★ Apr 23, 2026` column rather than modifying historical values:

| New Column Entry | Value |
|---|---|
| Services healthy | **100 containers Up** ★ |
| LLM proxies | 21/22 (unchanged) |
| Docker containers | **100 Up** ★ |
| ChromaDB collections | **48 collections, ~6,740,611 vectors** ★ |
| `msallisgis` | **Two-container split** ★ |
| `autonomous_learner` | **≥ 68 items (growing); verify current** ★ |
| AAPCAppE | **AAACPE stack** ★ |
| `appalachian_english_corpus` | **Resolved — 210 docs, growing** ★ |

Update the divergence threshold note to reflect:
- ChromaDB collections gate → **below 44** ★
- `autonomous_learner` gate → **decreasing from last verified baseline (floor: 68)** ✅ retain

#### §28.9 Interaction with Safeguards

- Seven-layer protection table — **Layer 0** entry: "★★ Up (March 22; confirmed active April 1)" → Note: **OI-36-A now also closed at Caddy `forward_auth` perimeter layer — token enforcement active before main-brain** ★
- "★★ With **96/96 Up**" → **100 containers** ★ (in narrative referencing container count)

#### §28.10 Summary

| Location | Stale Value | Correct Value |
|---|---|---|
| Opening statement | "★★ **April 1, 2026 production deployment … 96/96 containers Up**" | Add: **Superseded by April 23, 2026 baseline: 100 containers Up** ★ |
| April 9 corrections paragraph | "ChromaDB collection count is **49** … backup `chroma-latest` (**49 collections, 6,732,980 vectors**)" | Update vector count to **~6,740,611** ★ |
| AAPCAppE reference | "`allis-ingest-api`/`allis-ingest-watcher`" | **AAACPE stack** ★ |
| EEG status | "beta rhythm … operationally restored" | Retain ✅ |

#### Footer Star Notes

| Stale Value | Correct Value |
|---|---|
| "★★★ April 9, 2026: Collection count corrected to 49 … 6,732,980 vectors" | Add new footer star: **April 23, 2026: 100 containers Up; 48 collections, ~6,740,611 vectors; two-container PostgreSQL split; AAACPE stack** ★ |
| "★ March 28, 2026: `msallisgis` port 5432 confirmed (**91 GB PostGIS, 501 tables**, 993 ZCTA centroids)" | **Two-container split** ★ |

***

### Universal Corrections — Chapters 26, 27, and 28

| Correction | Ch. 26 | Ch. 27 | Ch. 28 |
|---|---|---|---|
| Container count → **100** ★ | §26.0–§26.5, header, footer | Header, diagram, status table, §27.7–§27.9, footer | §28.1, §28.2, §28.9, §28.10, new baseline column |
| ChromaDB → **48 collections** ★ | §26.1–§26.4, header, footer | Header, diagram, table, §27.2–§27.9 | §28.1, §28.2, §28.7b, §28.8, §28.10 |
| Total vectors → **~6,740,611** ★ | §26.1–§26.4, header | §27.2–§27.9, figure | §28.1, §28.2, §28.7b, §28.8, §28.10 |
| Two-container DB split ★ | §26.1, §26.2, §26.4, preamble, footer | P1/P5 callout, §27.3, §27.5, §27.8, §27.9 | §28.2, §28.7, §28.8, §28.9, §28.10 |
| AAPCAppE → AAACPE stack ★ | §26.1, §26.4, §26.5 | §27.1, §27.4, §27.7, diagram, §27.9 | §28.4 EEG table, §28.8, §28.10 |
| `msallis_docs` → **verify current** ★ | §26.1 medium-term | §27.1, §27.4, §27.7, diagram, table | §28.7a resolved row |
| `appalachian_english_corpus` → **verify-current (growing)** ★ | §26.1–§26.4 | §27.1, §27.3, §27.7, diagram, §27.9 | §28.7a status update |
| GBIM entity counts → **verify-current** ★ | §26.1–§26.4 | Callout, §27.3, §27.8, §27.9 | §28.1, §28.7, §28.8 |
| `autonomous_learner` telemetry → **floor/verify-current** ★ | §26.1 | §27.2 | §28.1a, §28.4 EEG table |
| OI-36-A Caddy perimeter closure note ★ | New note in §26.3 | N/A | §28.9 Layer 0 table |
| `appalachian_english_corpus` zero-count resolution ★ | N/A | N/A | §28.7a status row update |
| Ch. 27 container count inconsistency (107 vs 105) ★ | N/A | All "107" refs → **100** | N/A |Now I have all three chapters plus the authoritative help.md baseline. Here is the full edit list for all three chapters.

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
