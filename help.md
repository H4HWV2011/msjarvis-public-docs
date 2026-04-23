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
