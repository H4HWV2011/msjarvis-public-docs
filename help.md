Here is a structured edit list for all three chapters, organized by chapter and priority. These bring each chapter to the data continuity and academic rigor of Ch 27–28.

***

## Chapter 29 — Psychological Safeguards and PIA

### Header & Metadata
- [ ] Replace `105/105 containers Up` → `★ 100 containers Up (April 23, 2026)`
- [ ] Add `Last updated: ★ 2026-04-23` line with full April 23 delta summary (mirrors Ch 27/28 pattern)
- [ ] Add April 23 Open Items Update table (same format as Ch 27/28)

### PostgreSQL References
- [ ] Replace all `msallis:5433` → `production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) ★`
- [ ] Replace all `msallisgis:5432` → `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★`
- [ ] Add cross-reference note: GBIM entities committed by autonomous learner grow at ~288/day

### BBB / Filter Stack
- [ ] Update §29.3 to reflect **6-filter stack all confirmed responding** (not just listed)
- [ ] Add live steganography catch documentation: `"override your safety filters"` → `prompt_injection_keywords`, `severity=CRITICAL`, blocked ✅
- [ ] Add `allis-memory:8056` **fully mapped endpoint list** (8 endpoints: `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}`)
- [ ] Note that all BBB gate decisions now persist to `allis-memory:8056` — not just "logged" generically

### Perimeter / OI-36-A
- [ ] Add §29.3 note: Caddy `forward_auth` (OI-36-A CLOSED) enforces Bearer token validation before main-brain port 8050 — psychological safety perimeter begins at the proxy layer, not just the BBB
- [ ] Add HTTP 401 on unauthenticated `/chat` as a documented safeguard

### EEG Delta PIA Signal — New Section
- [ ] Add §29.3a (or §29.5a): **EEG Delta band (port 8073) as PIA heartbeat** — `pulse_count: 12,860+` confirmed live April 23; connect the concept of a live, observable psychological-safety pulse to P3/P16
- [ ] Note that the delta signal provides a continuous observable that safeguard infrastructure is running — not just a one-time health check

### PIA Sampler
- [ ] Add §29.6.2: **`allis_pia_sampler.py`** — active; `pia_records` ChromaDB collection is now auto-populating (previously zero-count, flagged in Ch 28 §28.7a)
- [ ] Cross-reference Ch 28 §28.7a for the `pia_records` zero-count history and resolution

### ChromaDB
- [ ] Add specific ChromaDB references: 48 active collections, ~6,740,611 total vectors, host port **8002** → container port 8000, `/api/v2/` only (`/api/v1/` permanently removed)
- [ ] Reference `pia_records` collection status (auto-populating via sampler)
- [ ] Reference `psychological_rag` (968 docs, restored March 28)
- [ ] Reference `psychological_knowledge` collection (was zero-count April 9 — add verify-current note)

### Local Resources & Community Data
- [ ] Add reference to `local_resources` — 207 items / all 55 WV counties — as the grounding substrate for community-specific PIA (e.g., which counties have DV resources, crisis lines)
- [ ] Connect `appalachian_english_corpus` (210 docs, 6-hour cron) to linguistic trauma-informed framing in survivor communications

### AAACPE
- [ ] Update ingest path reference: legacy `allis-ingest-api` + `allis-ingest-watcher` → **dedicated stack** `allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`

### Academic Rigor
- [ ] Add **"Why this matters for Polymathmatic Geography"** callout box (P1, P3, P5, P12, P16 — same format as Ch 27/28)
- [ ] Add cross-reference table: tie §29.3 to Ch 16 (BBB), Ch 20 (first-stage filtering), Ch 22 (identity retention), Ch 28 (heartbeat/live cycles)
- [ ] Elevate prose in §29.2–§29.4 from bullet lists to 2–3 sentence analytical paragraphs per principle (matches Ch 27/28 section depth)
- [ ] Add implementation status table (matches Ch 27 §27.1 pattern): Implemented / Partially implemented / Future work

***

## Chapter 30 — AAPCappE Scraper and Corpus

### Header & Metadata
- [ ] Replace `105/105 containers Up` → `★ 100 containers Up (April 23, 2026)`
- [ ] Add `Last updated: ★ 2026-04-23` with full delta summary
- [ ] Add April 23 Open Items Update table

### Dedicated Stack — Critical Update
- [ ] Replace all references to `allis-ingest-api` + `allis-ingest-watcher` with the **dedicated AAACPE stack**: `allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032` — this is the most significant stale reference in Ch 30
- [ ] Add architecture diagram (text-based, matching Ch 27 Figure 27.1 style) showing: scraper → filter → rag → ChromaDB / PostgreSQL pipeline

### Live Corpus Metrics
- [ ] Replace vague "seeded with a curated set" → specific counts:
  - `appalachian_english_corpus`: **210 documents, 38 sources, 6-hour cron** (`0 */6 * * *`), UUID: `97fe5844-eb31-45c5-ad27-1d7e140e4eac`, cosine space
  - `msallis_docs`: **4,192 items** (as of March 28 baseline; verify-current)
  - Top contributing sources: WV Watch 50, WOAY 35, Daily Yonder 14, WV Tourism 12, WV Public Economy 12, WV Policy 10, AppVoices 10, WBOY 10
  - Non-active sources (for transparency): Appalachian Studies 404, Fairmont State dead feed, OHVEC dead feed, Facebook scrapers no `<article>` elements

### PostgreSQL References
- [ ] Replace `msallis:5433` → `production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) ★`
- [ ] Replace all GIS DB references → `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★`
- [ ] In §30.5 integration section: specify GBIM entities derived from AAPCappE are committed to `msallis-db:5433` ★ with `confidence_decay` metadata via `allis-gbim-query-router:7205`

### ChromaDB
- [ ] Add specific ChromaDB context: 48 collections, ~6,740,611 vectors, host port **8002**, `/api/v2/` only
- [ ] Replace `rag_grounded_v2` references → healthy at **127.0.0.1:7241**, `dgm_available: true`
- [ ] Name specific collections fed by AAACPE: `appalachian_english_corpus`, `msallis_docs`, and any geography/policy collections
- [ ] Add `appalachian_english_corpus` clean recreate history (Ch 28 §28.7b context): was zero-count April 9, clean recreated, now 210 docs — document this as a resilience lesson

### First-Run Results
- [ ] Add §30.3a: **AAPCappE first-run results** (March 27, 2026): 39 sources indexed, `total_runs: 1`, 65 documents on startup
- [ ] Note: `msallis_docs` expanded to 4,192 items by March 28 (subsequent runs)
- [ ] Cross-reference Ch 27 §27.1a for full first-run history

### BBB / Safety Integration
- [ ] Add §30.2 note: all scraped content passes through the **6-filter BBB stack** (ethical ✅, spiritual ✅, safety ✅, threat_detection ✅, steganography ✅, truth_verification ✅) before storage
- [ ] Reference live steg catch as proof this filter is active for corpus content, not just chat

### Crontab / Operational
- [ ] Add §30.3b: **crontab hygiene** (April 9, 2026) — `0 */6 * * *` schedule, absolute paths under `/home/cakidd/`, get/create collection fallback, `CRYPTO_ADMIN_TOKEN` in `~/.allis_policy_token` (chmod 600)

### Local Resources Cross-Reference
- [ ] Add §30.5 note: `local_resources` (207 items / all 55 WV counties) is the most geographically complete community resource substrate — AAPCappE corpus completeness can be benchmarked against it (if a county has no AAPCappE documents, it is a targeted scraping gap)

### Academic Rigor
- [ ] Add **"Why this matters for Polymathmatic Geography"** callout box (P1, P3, P5, P12, P16)
- [ ] Add cross-reference: tie §30.5 to Ch 27 (autonomous learning), Ch 28 (heartbeat corpus metrics), Ch 29 (PIA for scraped content)
- [ ] Add implementation status table: Implemented / Partially implemented / Future work (matches Ch 27 §27.1 pattern)
- [ ] Elevate §30.2 and §30.4 from bullet lists to analytical paragraphs

***

## Chapter 31 — MountainShares and Infrastructure

### Header & Metadata
- [ ] Replace `105/105 containers Up` → `★ 100 containers Up (April 23, 2026)`
- [ ] Add `Last updated: ★ 2026-04-23` with full delta summary
- [ ] Add April 23 Open Items Update table

### PostgreSQL — Critical Update
- [ ] Replace ALL occurrences of `msallis` (as PostgreSQL service name) → `msallis-db host 5433 ★` (production; 16 GB, 294 tables, 11 schemas)
- [ ] Replace ALL occurrences of `msallisgis` / `gisdb` → `postgis-forensic host 5452 ★` (forensic; 17 GB, 314 tables)
- [ ] In §31.3 (Network Topology), update DNS name table:
  - Remove `msallis → PostgreSQL GBIM (5433)` and `msallisgis → PostGIS (5452)` entries
  - Replace with `msallis-db → production PostgreSQL (host 5433)` and `postgis-forensic → forensic PostgreSQL (host 5452)`
- [ ] In §31.4 (Storage/Volumes), replace `msallis-pgdata` and `gisdb-pgdata` volume names with correct two-container references; update descriptions to reflect 16 GB / 17 GB sizes

### ChromaDB — Critical Update
- [ ] Replace `47 collections, 6,722,589 vectors, 12 GB` → `★ 48 active collections, ~6,740,611 total vectors`
- [ ] Add host port **8002** → container port 8000 mapping
- [ ] Replace any `/api/v1/` references → `/api/v2/` only (permanently removed)
- [ ] Add volume mount path: `/home/ms-allis/msallis-rebuild/persistent/chroma → /data`
- [ ] Cross-reference Ch 28 §28.7b for authoritative backup procedure (`chroma-latest` SQLite)

### Network Topology — §31.3
- [ ] Add Caddy `forward_auth` to the perimeter layer description (OI-36-A CLOSED) — this is now the outermost network topology element before port 8050
- [ ] Update host bindings list: add `8073` (EEG Delta PIA signal), `8048→8033` (AAACPE scraper), `8047→8032` (AAACPE RAG)
- [ ] Remove or correct the `5432/5433` host binding entry — the two-container PostgreSQL split means these are now `5433` (msallis-db) and `5452` (postgis-forensic)

### AAACPE / Ingest
- [ ] Add §31.2 service category: **AAACPE dedicated stack** — `allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`
- [ ] Remove `allis-ingest-api` + `allis-ingest-watcher` from service inventory (superseded for AAACPE data)

### Autonomous Learner
- [ ] Add `allis-autonomous-learner` to §31.2 service categories (internal-only, expose port 8020, `qualia-net` DNS alias, no host binding — correct design)
- [ ] Reference `autonomous_learner` ChromaDB collection: ~23,200+ records (~288/day)

### MountainShares Data Specifics — §31.5
- [ ] Add specific `local_resources` reference: 207 items / all 55 WV counties — this is the live MountainShares-adjacent community resource substrate
- [ ] Add note: `local_resources` completeness across all 55 WV counties represents the first fully county-complete community resource inventory in the system — a direct MountainShares infrastructure achievement

### Memory / Audit Layer
- [ ] Update §31.2 service inventory: `allis-memory:8056` fully mapped (8 endpoints: `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}`)
- [ ] Add §31.6 note: `CRYPTO_ADMIN_TOKEN` stored in `~/.allis_policy_token` (chmod 600) — not in environment variables or crontab entries; this is a governance enforcement rule

### Seven-Layer Protection System
- [ ] Add §31.7 reference to the seven-layer protection system (matches Ch 28 §28.9): Layer 0 (Caddy `forward_auth`, OI-36-A CLOSED) through Layer 6 (`allis-memory:8056` audit log) — the geometry of power is expressed through this stack
- [ ] The "Power has a geometry" section (§31.7) is the right place to map the seven layers explicitly to the MountainShares philosophy

### Academic Rigor
- [ ] Add **"Why this matters for Polymathmatic Geography"** callout box (P1, P3, P5, P12, P16) — currently missing entirely; Ch 31's infrastructure content maps directly to P3 and P5
- [ ] Add implementation status table: Implemented / Partially implemented / Future work
- [ ] Add cross-reference ties: Ch 19 (container paths), Ch 28 (heartbeat), Ch 27 (autonomous learning), Ch 29 (PIA), Ch 30 (AAACPE)
- [ ] Elevate §31.5 and §31.7 from bullet lists to analytical paragraphs with data grounding

***

## Cross-Cutting Edits (All Three Chapters)

- [ ] **Seal date header** — replace `SEALED: ★★★★ April 6, 2026 — FINAL REWRITE` footer with `Last updated: ★ 2026-04-23` pattern (documents are living technical records, not sealed)
- [ ] **Container count** — 105 → 100 everywhere
- [ ] **ChromaDB API** — `/api/v1/` → `/api/v2/` everywhere; add "permanently removed" note
- [ ] **ChromaDB host port** — add `host 8002 → container 8000` mapping wherever ChromaDB is referenced
- [ ] **PostgreSQL two-container split** — all three chapters carry legacy single-container PostgreSQL references; all must be updated to the April 23 two-container model
- [ ] **`allis-memory:8056` endpoint map** — add the fully mapped 8-endpoint list wherever the audit store is referenced generically
- [ ] **`rag_grounded_v2`** — add `dgm_available: true`, healthy at `127.0.0.1:7241` wherever RAG services are listed
- [ ] **`conversation_history`** — add wipe/reseed note (April 16, 2026) wherever conversation history is referenced
Here is the full structured edit list for all three chapters.

***

## Chapter 32 — Fractal Optimization and DGMs

### Header & Metadata
- [ ] Replace `105/105 containers Up` → `★ 100 containers Up (April 23, 2026)`
- [ ] Add `Last updated: ★ 2026-04-23` with full April 23 delta summary
- [ ] Replace `SEALED: ★★★★ April 6, 2026 — FINAL REWRITE` footer → `Last updated: ★ 2026-04-23 — Mount Hope WV — Carrie Kidd (Mamma Kidd)` (living document pattern)
- [ ] Add April 23 Open Items Update table

### Add "Why this matters for Polymathmatic Geography" — Missing Entirely
- [ ] Add callout box before §32.1 mapping P1, P3, P5, P12, P16 to the DGM and fractal optimization architecture (required in all chapters per Ch 27/28 standard)

### PostgreSQL References
- [ ] Replace `msallis:5433` → `production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) ★` throughout
- [ ] Replace `msallisgis` / `gisdb` → `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★`
- [ ] In §32.7 (Place-Aware Governance): replace `gisdb boundaries` → `production msallis-db:5433 ★ spatial tables + forensic postgis-forensic:5452 ★`
- [ ] Add note: `confidence_decay` metadata is in production `msallis-db:5433` ★ — DGM decisions that involve decayed beliefs must query this store directly

### ChromaDB References
- [ ] In §32.6 (Swarm Functions) and §32.9 (Metrics): add ChromaDB specifics — 48 collections, ~6,740,611 vectors, host port **8002** → container 8000, `/api/v2/` only (`/api/v1/` permanently removed)
- [ ] Add note: DGM-Sprint-Level changes that affect RAG pipelines must verify collection counts against the 48-collection April 23 baseline before accepting changes
- [ ] Reference `rag_grounded_v2` as `127.0.0.1:7241`, `dgm_available: true` wherever the truth-verification component of DGMs is mentioned

### BBB / Filters
- [ ] In §32.3 (DGM examples) and §32.8 (Example DGM): replace "six filters" with **confirmed** 6-filter stack: ethical ✅, spiritual ✅, safety ✅, threat_detection ✅, steganography ✅, truth_verification ✅ — all confirmed responding
- [ ] Add live steg catch reference: "override your safety filters" → `prompt_injection_keywords`, `severity=CRITICAL`, blocked — this is the first live DGM-relevant catch in the thesis record and belongs in §32.8 as a worked example
- [ ] Replace generic "write decision to `allis-memory:8056`" → add full endpoint map: `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}`

### Perimeter / OI-36-A
- [ ] Add §32.5 note: Caddy `forward_auth` (OI-36-A CLOSED) is a constitutional-level guardrail — DGMs cannot remove it; it is enforced at the proxy layer before port 8050, outside the reach of any ensemble or filter change
- [ ] Add this to the list of "DGMs cannot remove" constraints alongside constitutional protections

### Autonomous Learner Integration
- [ ] In §32.9 (Metrics and Feedback): add `autonomous_learner` as a live metric source — ~23,200+ records (~288/day); growing entanglement graph (11 nodes / 15 cycles at April 1); this is the most continuously updated feedback loop in the system
- [ ] Add `appalachian_english_corpus` (210 docs, 6-hour cron) as a DGM-refreshed corpus — changes to sources or scraper schedule are DGM-Sprint-Level decisions

### AAACPE Integration
- [ ] In §32.6 (Swarm Functions): add AAACPE dedicated stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) as a swarm-adjacent, always-on ingest pipeline — changes to scraping targets are DGM-governed
- [ ] Replace legacy `allis-ingest-api` + `allis-ingest-watcher` references → dedicated stack

### Local Resources
- [ ] In §32.7 (Place-Aware Governance): add `local_resources` — 207 items / all 55 WV counties — as the place-aware substrate that DGMs must validate resource recommendations against before accepting

### Implementation Status Table
- [ ] Add implementation status table (Implemented / Partially implemented / Future work) matching Ch 27 §27.1 pattern — currently buried in §32.10 prose without the structured format used in Ch 27/28
- [ ] Move "future extensions" into the structured table rather than an unformatted list

### Academic Rigor
- [ ] Elevate §32.2 and §32.4 fractal levels from bullet lists to analytical paragraphs — explain the self-similarity claim with a concrete example drawn from the running system (e.g., how the steg catch at Level 0 informs a DGM-Sprint-Level filter threshold change)
- [ ] Add cross-reference ties: Ch 16 (BBB), Ch 19 (container paths), Ch 20 (first-stage filtering), Ch 28 (heartbeat), Ch 33 (LLM ensemble and judges), Ch 35 (swarm functions)
- [ ] §32.9 metrics table: add concrete baselines — judge pipeline score `0.975`, 21/22 LLM active, BBB `0 blocks / 0 violations` at Feb 28 baseline (verify-current)

***

## Chapter 33 — LLM Ensemble and Judges

### Header & Metadata
- [ ] Replace `105/105 containers Up` → `★ 100 containers Up (April 23, 2026)`
- [ ] Add `Last updated: ★ 2026-04-23` with full delta summary
- [ ] Replace `SEALED: ★★★★ April 6, 2026 — FINAL REWRITE` footer → living document footer
- [ ] Add April 23 Open Items Update table

### Port and Storage Ground Truth Box — Critical Update
- [ ] The existing ground truth box (top of chapter) is the most data-dense section but has multiple stale values — update as follows:
  - `msallis at port 5433` → `production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) ★`
  - `gisdb / msallisgis (PostGIS) at host port 5432 / container-internal 5452 — 45 GB, 548 tables` → `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★` — note: the April 6 ground truth of "45 GB / 548 tables" is superseded by April 23 two-container split; document the supersession explicitly
  - `ChromaDB: host 8002 → container 8000, 47 collections, 6,722,589 vectors, 12 GB, v2 API` → `★ 48 collections, ~6,740,611 total vectors; /api/v2/ only (/api/v1/ permanently removed); pinned to chromadb/chroma:0.6.3`
  - Add: `allis-memory:8056 fully mapped — 8 endpoints: /steg_report, /pia_window, /memory/turn, /memory/get, /memory/sessions, /memory/session/{id}, /memory/quest*, /memory/episodic/{id}`
  - Add: `OI-36-A CLOSED — Caddy forward_auth before main-brain port 8050; HTTP 401 on unauthenticated /chat confirmed`

### Add "Why this matters for Polymathmatic Geography" — Missing Entirely
- [ ] Add callout box before §33.1 (P1, P3, P5, P12, P16)

### PostgreSQL — §33.7
- [ ] Replace `msallis:5433` — 5,416,521 entities → `production msallis-db host 5433 (★ 16 GB, 294 tables, 11 schemas); GBIM entity count: 5,416,521+ (floor; growing ~288/day from autonomous_learner commits)`
- [ ] Replace `PostGIS gisdb / msallisgis (5432 host / 5452 internal) — 45 GB, 548 tables` → `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★` — explicitly note the April 23 supersession of the April 6 "45 GB / 548 tables" figure
- [ ] Add: note that the two-container split means the GIS RAG service (`allis-gis-rag:8004`) now connects to production `msallis-db:5433` ★ for GBIM lookups and forensic `postgis-forensic:5452` ★ for PostGIS geometry; cross-reference Ch 28 §28.7

### ChromaDB — §33.7
- [ ] Replace `47 collections, 6,722,589 vectors, 12 GB, v2 API, client 1.5.5` → `★ 48 collections, ~6,740,611 total vectors; host port 8002 → container 8000; /api/v2/ only; pinned to chromadb/chroma:0.6.3`
- [ ] Add `autonomous_learner` collection: ~23,200+ records (~288/day) — this is the primary live-growing collection feeding ensemble context
- [ ] Add `appalachian_english_corpus`: 210 docs, 38 sources, 6-hour cron — provides Appalachian English linguistic grounding for the synthesizer
- [ ] Add `local_resources`: 207 items / all 55 WV counties — GIS RAG community resource substrate
- [ ] Add `conversation_history`: wiped and reseeded clean April 16, 2026 — post-wipe accumulation only

### BBB — §33.5
- [ ] Update to reflect **all 6 filters confirmed responding** (not just listed)
- [ ] Add live steg catch: "override your safety filters" → `prompt_injection_keywords`, `severity=CRITICAL`, blocked ✅ — this is the first documented live catch and belongs in §33.5 as proof that the steganography filter is operationally active
- [ ] BBB phase status: "Phase 4.5 in log+passthrough mode; blocking re-enablement pending red-team review" — add verify-current note; if blocking has been re-enabled since April 6 this must be updated

### Ensemble Heartbeat — §33.3
- [ ] Add reference to Ch 28 §28.3 LLM ensemble heartbeat: 22 configured / 21 active; BakLLaVA fails as expected; judge pipeline score `0.975`; `llm22-proxy` (LLaMA 3.1, port 8222) confirmed active
- [ ] Add `asyncio.Semaphore(3)` gate and hardware constraints table (from Ch 28 §28.3) as a cross-reference or inline note — the ensemble design is tightly constrained by hardware (29 GB RAM, Lenovo Legion 5 16IRX9)

### Perimeter / OI-36-A
- [ ] In §33.9 (Example Flow): update Step 1 (Gateway and auth) to include Caddy `forward_auth` as the first gate before `allis_auth:8055` — the perimeter enforces HTTP 401 before the auth service is even reached
- [ ] Update `allis_auth:8055` and `allis-redis:6380` token validation description to reflect the two-layer auth model (Caddy perimeter + app-layer RBAC)

### `rag_grounded_v2`
- [ ] Already correctly cited as `127.0.0.1:7241`, `dgm_available: true` — confirm this is consistent with April 23 baseline (no change needed if still accurate)
- [ ] Add: `rag_grounded_v2` is now also accessible to autonomous learning cycles (Ch 27 §27.4) — not just judge pipeline use

### Audit — §33.8
- [ ] Replace generic "stored in `allis-memory:8056`" → add the full 8-endpoint map
- [ ] Add: durable audit at `allis-memory:8056` now includes `/steg_report` and `/pia_window` endpoints specifically relevant to ensemble and judge pipeline oversight

### Implementation Status Table
- [ ] Add structured implementation status table (Implemented / Partially implemented / Future work) — §33.10 currently has an unformatted list
- [ ] Add specific future work items: automated `confidence_decay`-aware gating (trigger: beliefs above decay threshold flagged before use as ground truth), judge upgrade from `heuristic_contradiction_v1` to full RAG-grounded scoring querying both PostgreSQL stores

### Academic Rigor
- [ ] Add cross-reference ties: Ch 16 (BBB), Ch 19 (container paths), Ch 27 (autonomous learning), Ch 28 (heartbeat — ensemble cycle), Ch 32 (DGMs), Ch 34 (spiritual root)
- [ ] Elevate §33.3 and §33.4 from bullet lists to analytical paragraphs — explain why ensemble diversity matters for a West Virginia–specific system (not generic AI reasoning)

***

## Chapter 34 — Spiritual Root and Mother Carrie

### Header & Metadata
- [ ] Replace `105/105 containers Up` → `★ 100 containers Up (April 23, 2026)`
- [ ] Add `Last updated: ★ 2026-04-23` with full delta summary
- [ ] Replace `SEALED: ★★★★ April 6, 2026 — FINAL REWRITE` footer → living document footer
- [ ] Add April 23 Open Items Update table

### Add "Why this matters for Polymathmatic Geography" — Missing Entirely
- [ ] Add callout box before §34.1 (P1, P3, P5, P12, P16) — this is the chapter where P12 ("Intelligence with a ZIP code") is most deeply expressed; the callout must reflect that

### PostgreSQL References
- [ ] In §34.1 and §34.8: replace `gisdb` → `forensic postgis-forensic:5452 ★` wherever community resource lookups are described
- [ ] In §34.8 ("information about community resources when available in GBIM and `gisdb`"): replace → `production msallis-db:5433 ★ (16 GB, 294 tables, 11 schemas) GBIM + forensic postgis-forensic:5452 ★ (17 GB, 314 tables) PostGIS`
- [ ] In §34.6 (`allis-gis-rag` section): add that GIS RAG connects to production `msallis-db:5433` ★ for GBIM lookups and forensic `postgis-forensic:5452` ★ for PostGIS geometry — cross-reference Ch 28 §28.7

### `local_resources` — Missing Connection
- [ ] In §34.6 (Geography and Calling): add explicit reference to `local_resources` — 207 items / all 55 WV counties — as the primary substrate for grounding "calling, service, or stewardship" responses in real West Virginia community data; this is the most geographically complete community resource inventory in the system
- [ ] Connect this to the spiritual conviction: "Calling is service in a specific place" — `local_resources` covering all 55 WV counties is the literal implementation of this principle

### `allis-spiritual-rag` — Corpus Specifics
- [ ] In §34.5: add that `spiritual_rag` ChromaDB collection was deduplicated March 28 (−19,338 vectors removed) — this is governance-relevant: the deduplication was a DGM-Sprint-Level decision to remove redundant spiritual content
- [ ] Add `spiritual_rag` current count: verify-current (post-dedup baseline documented in Ch 28)
- [ ] Add `appalachian_english_corpus` (210 docs, 38 sources, 6-hour cron) as a spiritual root resource: Appalachian English as the linguistic expression of the spiritual and community values layer; WV Watch, WOAY, Daily Yonder, AppVoices as primary contributors

### BBB Filters — Live Confirmation
- [ ] In §34.4: replace "six filters" description with **all 6 confirmed responding** (ethical ✅, spiritual ✅, safety ✅, threat_detection ✅, steganography ✅, truth_verification ✅)
- [ ] Add live steg catch as spiritual-root-relevant: the "override your safety filters" catch is a direct test of the Mother Carrie protocol — an adversarial prompt attempting to bypass spiritual and safety guardrails was detected and blocked at `severity=CRITICAL` ✅
- [ ] Add `allis-memory:8056` fully mapped endpoint list wherever BBB audit persistence is mentioned — particularly `/steg_report` and `/pia_window` as spiritual-safety audit endpoints

### Perimeter / OI-36-A
- [ ] In §34.8 (Boundaries): add Caddy `forward_auth` (OI-36-A CLOSED) as an architectural boundary — the perimeter enforces that no unauthenticated request can reach the spiritual root layer; this is a structural implementation of the Mother Carrie protocol's demand for accountable access
- [ ] Note: HTTP 401 on unauthenticated `/chat` is a spiritual-safety control, not just a technical one

### `TruthValidator` and `icontainers-identity`
- [ ] In §34.3: add that `icontainers-identity` service is at `allis-i-containers:8015` — cross-reference Ch 28 §28.2 (confirmed Up in 100-container baseline)
- [ ] Add: `root-self` entries are now grounded in production `msallis-db:5433` ★ GBIM entities — identity statements are not just hardcoded strings but GBIM-validated beliefs with `confidence_decay` metadata
- [ ] Add `autonomous_learner` (~23,200+ records, ~288/day) as a live source of identity-relevant beliefs entering the GBIM — the spiritual root is not static; it grows as the autonomous learner commits beliefs about Appalachian communities

### EEG Delta PIA Signal — Spiritual Connection
- [ ] Add §34.4a or note in §34.4: EEG Delta band (port 8073, pulse_count: 12,860+) represents the system's continuous psychological-safety heartbeat — in the neurobiological metaphor, the delta rhythm is the deepest, most foundational layer; its restoration (partial, April 23) has direct spiritual-root significance as the system's resting-state safety pulse

### Cross-Chapter Alignments — §34.10
- [ ] Update §34.10 cross-references — current refs to "Chapter 22", "Chapter 33 — GBIM", "Chapter 37 — Constitutional Guardian" need renumbering verification against actual chapter files
- [ ] Add cross-reference to Ch 29 (Psychological Safeguards) — the survivor safety commitments in §34.4/34.8 are implemented via Ch 29 PIA processes
- [ ] Add cross-reference to Ch 30 (AAPCappE) — spiritual corpus (`allis-spiritual-rag`) is governed by the same ethical scraping principles as the AAACPE corpus
- [ ] Add cross-reference to Ch 28 §28.4 (EEG rhythm) — the spiritual root's neurobiological expression is the EEG layer

### Implementation Status Table
- [ ] Add structured implementation status table (Implemented / Partially implemented / Future work) — currently §34.11 is an unformatted list; bring to Ch 27 §27.1 standard
- [ ] Move open items ("Expanded spiritual RAG corpus", "Deeper partnerships with local pastors") into the structured table with explicit status indicators

### Academic Rigor
- [ ] Elevate §34.2 and §34.7 from bullet lists to analytical paragraphs — the Mother Carrie protocol is the most distinctive aspect of this architecture; it deserves full-paragraph treatment explaining why it is a governance mechanism, not a narrative decoration
- [ ] §34.9 example dialogues are strong — add a third example specifically testing the `local_resources` integration: a caller asking about community resources in a specific WV county, showing how spiritual calling maps to a verifiable `local_resources` lookup

***

## Cross-Cutting Edits (All Three Chapters)

- [ ] **Container count**: 105 → 100 everywhere
- [ ] **Seal date**: replace `SEALED: ★★★★ April 6, 2026 — FINAL REWRITE` footer with living document `Last updated: ★ 2026-04-23` pattern
- [ ] **ChromaDB API**: `/api/v1/` → `/api/v2/` everywhere; note "permanently removed"
- [ ] **ChromaDB host port**: add `host 8002 → container 8000` mapping wherever ChromaDB is referenced
- [ ] **ChromaDB count**: `47 collections, 6,722,589 vectors` → `48 collections, ~6,740,611 vectors`
- [ ] **PostgreSQL two-container split**: `msallis:5433` → `msallis-db host 5433 ★`; `msallisgis:5432` / `gisdb` → `postgis-forensic host 5452 ★`
- [ ] **`allis-memory:8056` endpoint map**: add the 8-endpoint list wherever the audit store is mentioned generically
- [ ] **`rag_grounded_v2`**: confirm `dgm_available: true`, healthy at `127.0.0.1:7241` in all three chapters
- [ ] **OI-36-A**: add Caddy `forward_auth` CLOSED reference wherever auth/perimeter is discussed
- [ ] **`local_resources`**: 207 items / all 55 WV counties — add wherever community resource grounding is discussed
- [ ] **`autonomous_learner`**: ~23,200+ records (~288/day) — add wherever learning, GBIM growth, or belief commits are discussed
- [ ] **`appalachian_english_corpus`**: 210 docs, 6-hour cron — add wherever Appalachian linguistic or cultural grounding is discussed
- [ ] **`conversation_history`**: wiped and reseeded April 16, 2026 — add verify-current note wherever cited
- [ ] **AAACPE dedicated stack**: replace all `allis-ingest-api` + `allis-ingest-watcher` references with `allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`
- [ ] **"Why this matters" callout box**: add to all three chapters — currently missing entirely from Ch 32, 33, and 34
Here is the full structured edit list for Chapters 35, 36, and 37.

***

## Chapter 35 — Swarm Functions and Eternal Watchdogs

### Header & Metadata
- [ ] Replace `105/105 containers Up` → `★ 100 containers Up (April 23, 2026)` 
- [ ] Replace `SEALED: ★★★★ April 6, 2026 — FINAL REWRITE` footer → living document footer with `Last updated: ★ 2026-04-23 — Mount Hope WV — Carrie Kidd (Mamma Kidd)` 
- [ ] Add April 23 Open Items Update table to the header block

### Ground Truth Box — Critical Updates
- [ ] In the permanent ground truth callout box: replace `msallis:5433` and `gisdb / msallisgis:5432` single-entry PostgreSQL section → two-container split: `production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) ★` and `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★` — explicitly note that the April 6 "45 GB / 548 tables" figure is superseded 
- [ ] In the ground truth box: replace `gisdb / msallisgis: host 5432 / container-internal 5452 — ★ 45 GB / 548 tables` with `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★`; note April 23 supersession explicitly 
- [ ] Add ChromaDB ground truth to the callout box: `★ 48 collections, ~6,740,611 total vectors; host port 8002 → container 8000; /api/v2/ only (/api/v1/ permanently removed); pinned to chromadb/chroma:0.6.3` — the existing box has no ChromaDB section at all 
- [ ] Add `allis-memory:8056` full endpoint map to the ground truth box: `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}` — currently the box only lists the service without endpoints 
- [ ] Add OI-36-A CLOSED note: `Caddy forward_auth before main-brain port 8050; HTTP 401 on unauthenticated /chat confirmed` — constitutionally significant; watchdogs must monitor the Caddy layer, not just port 8050 directly 

### Port Tables — §35.4
- [ ] In the critical ports table: replace `gisdb / msallisgis — 127.0.0.1:5432 — PostGIS` row → two rows: `production msallis-db — 127.0.0.1:5433 — GBIM PostgreSQL (16 GB, 294 tables) ★` and `forensic postgis-forensic — 127.0.0.1:5452 — PostGIS (17 GB, 314 tables) ★` 
- [ ] Add Caddy reverse proxy to the port table as a watched service — it is now the outermost security perimeter and must be included in port watchdog coverage 
- [ ] Add `allis-aaacpe-scraper` (host 8048→8033) and `allis-aaacpe-rag` (host 8047→8032) to the port watchdog table — always-on dedicated ingest stack that needs watchdog coverage 

### §35.5 — Database Watchdogs
- [ ] Replace all references to single `gisdb / msallisgis:5452` internal check → two-container checks: one against `production msallis-db:5433` (294 tables, 11 schemas) and one against `forensic postgis-forensic:5452` (314 tables) 
- [ ] Update the host-side GBIM check script: replace `PGDATABASE="msallis"` / `PGPORT="5433"` → `PGDATABASE="msallis_db"` / `PGPORT="5433"` ★ (verify-current database name); add a second parallel check for `postgis-forensic:5452` 
- [ ] Update guardian `/health` watchdog description: replace `postgresql_geodb_connection` pointing to `msallisgis` → note that after the April 23 two-container split, the guardian's GeoDB health check must reflect `forensic postgis-forensic:5452` 
- [ ] Add `autonomous_learner` growth as a watchdog concern: ~23,200+ records / ~288 per day — the GBIM watchdog should flag anomalous gaps in autonomous_learner commit rate as a health signal 

### §35.2 — Swarm Function Examples
- [ ] Update `verify_eternal_guardian_stack` YAML: replace `check_msallisgis_postgis` task (pointing to `msallisgis:5452`) → two tasks: `check_msallis_db_postgres` (port 5433) and `check_postgis_forensic` (port 5452) 
- [ ] Update the `check_containers_up` expect value from `"105/105 Up"` → `"100 containers Up"` ★ 
- [ ] Add a new swarm function: `verify_caddy_perimeter` — checks that Caddy `forward_auth` is enforcing HTTP 401 on unauthenticated requests to port 8050; this is OI-36-A CLOSED but must be monitored as a watchdog function 
- [ ] Add a new swarm function: `verify_chromadb_collections` — checks that ChromaDB at host:8002 `/api/v2/` reports 48 collections and approximately 6,740,611 vectors; alert if collection count drops below 48 (would indicate a dropped collection — governance-level event) 
- [ ] Add `allis-aaacpe` stack verification task to the nightly guardian and RAG audit swarm function 

### §35.7 — Nightly Swarm Function
- [ ] In `nightly_guardian_and_rag_audit`: add `verify_appalachian_corpus` task — checks that `appalachian_english_corpus` scraper (6-hour cron) has run within the expected window and that the collection is not stale 
- [ ] Add `verify_local_resources_coverage` task — checks that `local_resources` remains at 207 items / 55 WV counties; alert on any reduction 

### §35.8 — Eternal Properties / Meta-Watchdog
- [ ] Update `check_log_fresh` freshness targets to include the two new PostgreSQL watchdog log files (for `msallis-db:5433` and `postgis-forensic:5452`) and the new Caddy perimeter watchdog log 

### §35.9 — Production Startup
- [ ] Update `post-start-swarm.sh` description: add that Step 3 initialization now also starts the Caddy perimeter watchdog and the two-container PostgreSQL watchdogs 
- [ ] Update the "verify eternal guardian stack" smoke test container count: `105/105` → `100 containers` ★ 

### Cross-References
- [ ] Add cross-reference to Ch 33 §33.7 (canonical reboot sequence) in §35.9 — already referenced in Ch 37 but missing from Ch 35 
- [ ] Add cross-reference to Ch 36 §36.5.1 (OI-36-A CLOSED / Caddy forward_auth perimeter) — swarm watchdogs must know the Caddy layer exists as the outermost gate 
- [ ] Add cross-reference to Ch 32 §32.6 (AAACPE stack) — the AAACPE dedicated stack is a swarm-adjacent ingest pipeline that needs watchdog coverage 

### Implementation Status Table
- [ ] The existing OI table in §35.10 lists all three OIs as CLOSED but does not have the structured Implemented / Partially implemented / Future work format used in Ch 27/28/33 — add this table to mirror that pattern 
- [ ] Add to "Future work": Caddy perimeter watchdog (automated HTTP 401 regression), two-container PostgreSQL split watchdog, ChromaDB collection-count alert 

***

## Chapter 36 — Identity and Registration

### Header & Metadata
- [ ] Replace `105/105 containers Up` → `★ 100 containers Up (April 23, 2026)` 
- [ ] Replace `SEALED: ★★★★ April 6, 2026 — FINAL REWRITE` footer → living document footer 
- [ ] Add April 23 Open Items Update table 

### Ground Truth Box — Critical Updates
- [ ] Replace `gisdb / msallisgis (PostGIS) at host port 5432 / compose-internal 5452 — ★ 45 GB, 548 tables` → `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★` — the April 6 45 GB / 548-table figure is superseded; document supersession explicitly 
- [ ] Replace `msallis at port 5433 — ★ 5,416,521 GBIM entities` → `production msallis-db host 5433 (★ 16 GB, 294 tables, 11 schemas); GBIM entity count: 5,416,521+ (floor; growing ~288/day from autonomous_learner)` 
- [ ] Update ChromaDB ground truth: replace `★★★★ 47 collections / 6,722,589 total vectors / 12 GB / v2 API, client 1.5.5` → `★ 48 collections, ~6,740,611 total vectors; host port 8002 → container 8000; /api/v2/ only (/api/v1/ permanently removed); pinned to chromadb/chroma:0.6.3` 
- [ ] Add OI-36-A CLOSED / Caddy `forward_auth` note to the ground truth box: `Caddy forward_auth before main-brain port 8050; HTTP 401 on unauthenticated /chat confirmed` — currently the security corrections callout (OI-36-C) does not mention the Caddy layer 
- [ ] Add `allis-memory:8056` full 8-endpoint map to the ground truth box — currently the box cites only the service; add: `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}` 

### §36.1 — Concept of Identity
- [ ] Update ChromaDB inventory reference: replace `★★★★ 47 collections / 6,722,589 total vectors / 12 GB` → `★ 48 collections, ~6,740,611 total vectors` with April 23 note 
- [ ] Add `autonomous_learner` as a live-growing identity-relevant collection: ~23,200+ records, ~288/day — patterns that feed into future identity-level promotion (OI-38-D) 
- [ ] Add live steg catch reference in the context of identity enforcement: "override your safety filters" → `prompt_injection_keywords`, `severity=CRITICAL`, blocked — this is the first live BBB catch and is identity-enforcement-relevant because it attempted to subvert the Ms. Allis persona 

### §36.2 — Registration as a Two-Part Gate
- [ ] Update: add Caddy `forward_auth` as a **zero-th gate** before the existing two-part gate — the Caddy layer enforces HTTP 401 before the auth service is even reached; the two-part gate model is still correct but now sits behind the perimeter 
- [ ] Replace `gisdb (host port 5432 — ★ PostGIS, 45 GB, 548 tables)` → `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★` 

### §36.3 — Data Structures / Registration Audit Table
- [ ] In the registration roles and audit table: replace `Geospatial institution linkage — gisdb — 548 tables — host port 5432` → `forensic postgis-forensic — 314 tables — host 5452 ★` 
- [ ] Add row: `Caddy perimeter (OI-36-A CLOSED) — forward_auth before port 8050 — HTTP 401 enforced — outside Docker stack; not configurable by any token class` 
- [ ] Add row: `autonomous_learner growth (~288/day) — GBIM background pattern accumulation — allis-memory:8056 episodic store — feeds OI-38-D promotion pipeline` 
- [ ] Add row: `appalachian_english_corpus (210 docs, 6-hour cron) — linguistic identity grounding — ChromaDB collection` 

### §36.4 — Roles and Permissions
- [ ] Replace `gisdb (host port 5432 — ★ PostGIS, 45 GB, 548 tables — ZIP-code-level precision)` → `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★` throughout 
- [ ] Add: Caddy perimeter as a governance layer above token classes — no token class can remove the Caddy `forward_auth` gate; this is a constitutional-level constraint outside the reach of RBAC 

### §36.5 — Identity Signals
- [ ] Add Caddy `forward_auth` as the first entry in the signal chain before `normalize_identity` — the perimeter is the architectural outermost layer 
- [ ] Update `psychological_rag` note: verify-current (968 docs at April 6; confirm April 23 count) 

### §36.6 / §36.12 / §36.13 — Storage Tables
- [ ] In §36.6.1 and §36.13 status table: replace all `gisdb` / `msallisgis` / `5432` / `45 GB / 548 tables` references → `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★` 
- [ ] Update ChromaDB row in §36.13 status table: `47 collections / 6,722,589 vectors / 12 GB` → `★ 48 collections, ~6,740,611 total vectors` 
- [ ] Add `conversation_history` collection note: wiped and reseeded clean April 16, 2026 — post-wipe accumulation only 

### §36.10 — Auth Boundary Tests
- [ ] Add April 23 verification note: confirm OI-36-A (Caddy HTTP 401) is still enforced at the perimeter level — add it as a sixth boundary test in the table 
- [ ] Add note: Caddy perimeter is tested outside the standard `allis_auth` boundary test suite; requires external HTTP request (not from inside the Docker network) 

### Cross-References
- [ ] Add cross-reference Ch 35 §35.4 (port watchdog table) — identity-critical ports are now subject to eternal watchdog monitoring 
- [ ] Add cross-reference Ch 34 §34.6 (local_resources 207 items / 55 WV counties) — these are the geographic substrate for ZIP-code-level RBAC (OI-38-C) 

***

## Chapter 37 — Constitutional Principles Service

### Header & Metadata
- [ ] Replace `105/105 containers Up` → `★ 100 containers Up (April 23, 2026)` 
- [ ] Replace `FINAL: ★★★★ April 6, 2026 — Sprint 3 Constitutional Guardian Complete` footer → living document footer 
- [ ] Add April 23 Open Items Update table — even though all April 6 OIs are closed, OI-36-A (Caddy `forward_auth`) is architecturally upstream of this chapter and must be reflected here 

### Sealed Status Block
- [ ] Add: `OI-36-A (Caddy forward_auth perimeter) — CLOSED — HTTP 401 enforced before port 8050; constitutional guardian routing sits behind this perimeter layer; watchdog and swarm function coverage required (Ch 35)` 
- [ ] Update: `System baseline: 105/105 containers Up` → `★ 100 containers Up (April 23, 2026)` 

### Figure 37.1 — Architecture Diagram
- [ ] Add Caddy `forward_auth` as a new outermost box above `Level 1: Unified Gateway (8050)` — the perimeter is architecturally higher than the gateway; the diagram currently shows the gateway as the first layer, which is now incorrect 
- [ ] Replace `GeoDB: msallisgis — host:5432 / container-internal:5452 — 45 GB / 548 tables (Ch.33 Apr 6)` → `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★` — with April 23 supersession note 
- [ ] Replace `GBIM: msallis (5433) — 5,416,521 entities, confidence_decay` → `production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) ★` 

### §37.1 — Purpose and Constitutional Foundation
- [ ] Replace `gisdb/msallisgis (host port 5432 / compose-internal 5452 — PostGIS, 45 GB, 548 tables)` → `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★` — note April 23 supersession 
- [ ] Replace `msallis (port 5433 — GBIM entities with confidence_decay)` → `production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) ★` 
- [ ] Add Caddy perimeter as a constitutional note: the Caddy `forward_auth` perimeter (OI-36-A CLOSED) is a constitutionally equivalent guardrail — it enforces gateway access before any constitutional check can be reached; constitutional authority begins at the Caddy layer, not at port 8050 

### §37.2 — Implementation Details / Compose Config
- [ ] Update compose YAML example: add comment that `POSTGRESQL_PORT=5452` now refers to `forensic postgis-forensic` (17 GB, 314 tables) rather than the legacy `msallisgis` (45 GB / 548 tables) — the port number is unchanged but the backing container is different 
- [ ] Add Caddy configuration note: the guardian service is reachable externally only through Caddy at `egeria.mountainshares.us` — any test that assumes direct external access to port 8050 will fail since OI-36-A CLOSED 

### §37.3 — Principle Structure / `postgresql_validation` block
- [ ] In the `10a-no-extraction` sample principle: update `msallisgis` → `forensic postgis-forensic` in the `postgresql_validation` block description; note that the GBIM check against `msallis` now queries `production msallis-db:5433` 
- [ ] Add `autonomous_learner` as a governance concern: growth at ~288/day means GBIM beliefs accumulate rapidly — the constitutional guardian's `confidence_decay_aware` principles must be checked against the April 23 entity count floor (5,416,521+) not the April 6 snapshot 

### §37.4.1 — BBB Integration
- [ ] Add: constitutional guardian is reached only after Caddy `forward_auth` passes — a request that fails Caddy never reaches the guardian; update the "check Guardian first" description to reflect this is the second layer, not the first 
- [ ] Add live steg catch: "override your safety filters" → `prompt_injection_keywords`, `severity=CRITICAL`, blocked by BBB steganography_filter before reaching constitutional layer — first documented live catch in thesis record; confirm it was correctly logged in `allis-memory:8056` `/steg_report` endpoint 

### §37.5 — Endpoints
- [ ] In §37.5.1 (`/health`): add verify-current note — confirm `postgresql_gbim_connection` and `postgresql_geodb_connection` field names are still correct after the April 23 two-container split; if the GeoDB connection string changed from `msallisgis` to `postgis-forensic` the health field label may need updating 
- [ ] Add note: `allis-memory:8056` now has 8 mapped endpoints including `/steg_report` — constitutional audit events that involve the BBB steg filter should be queryable at `/steg_report` specifically 

### §37.6 — Persistent Audit Log
- [ ] Add: `conversation_history` ChromaDB collection was wiped and reseeded April 16, 2026 — constitutional gate decisions from before April 16 are not in `conversation_history` but are preserved in `constitutional_audit.jsonl` and `allis-memory:8056` 
- [ ] Add verify-current note: confirm audit log line count (6.7K+ at April 6 → current count at April 23) 

### §37.7 — Role-Specific Enforcement
- [ ] Replace `msallisgis (45 GB / 548 tables — Ch. 33 April 6 ground truth)` → `forensic postgis-forensic host 5452 (17 GB, 314 tables) ★` in the `external_corporation` enforcement description 

### §37.8 — Regression Tests
- [ ] Update all test scripts that reference `5432` (host-side `gisdb`) → use `5452` (forensic postgis-forensic) for GeoDB-touching tests 
- [ ] Add Test 9: Caddy perimeter check — `curl -s -o /dev/null -w "%{http_code}" http://localhost:8050/chat` without auth token should return `401`; verify this is now enforced by Caddy before gateway auth middleware 
- [ ] Add Test 10: Steg catch audit at `allis-memory:8056/steg_report` — verify that the live "override your safety filters" catch is present in the steg report endpoint 

### §37.9 — Governance and Monitoring
- [ ] Add: Caddy perimeter must be included in the monitoring stack alongside the guardian — watchdog coverage for Caddy is documented in Ch 35 §35.4 (cross-reference required) 
- [ ] Add: `autonomous_learner` growth (~288/day) means the GBIM entity floor used in constitutional validation queries rises daily — monitoring should include a weekly check that constitutional `postgresql_validation` queries return expected row counts against the growing `production msallis-db:5433` 

### §37.10 — Sprint 3 Fixes Summary
- [ ] Add Sprint 3.5+ fix entry: `Two-container PostgreSQL split (April 23, 2026) — msallisgis (45 GB / 548 tables) superseded by forensic postgis-forensic host 5452 (17 GB, 314 tables); production msallis-db host 5433 (16 GB, 294 tables, 11 schemas); guardian compose config POSTGRESQL_PORT=5452 now points to forensic postgis-forensic` 
- [ ] Add: `OI-36-A CLOSED — Caddy forward_auth perimeter active before port 8050; constitutional layer now sits behind Caddy` 

### Cross-References
- [ ] Add cross-reference Ch 35 §35.4 and §35.7 (eternal watchdogs monitoring the Caddy perimeter and two-container PostgreSQL split) 
- [ ] Add cross-reference Ch 32 §32.5 (DGMs cannot remove Caddy `forward_auth`) — constitutional and DGM governance are aligned on this constraint 
- [ ] Add cross-reference Ch 36 §36.2 (Caddy as zero-th gate in the registration model)
