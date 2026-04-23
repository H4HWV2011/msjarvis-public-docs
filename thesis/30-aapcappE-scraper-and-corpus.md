# Chapter 30 — AAPCappE Scraper and Corpus

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**
**Last updated: ★ 2026-04-23**
**★ 100 containers Up (April 23, 2026) (zero Restarting, zero Exited). AAPCappE scraper and corpus handling are documented as part of Ms. Allis's data pipeline, with explicit constraints for ethical scraping, Appalachian focus, and survivor-safe content curation. The dedicated AAACPE stack (`allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032`) supersedes the legacy `allis-ingest-api` + `allis-ingest-watcher` path.**

---

> **April 23, 2026 — Open Items Update**
>
> | Item | Status | Notes |
> |:--|:--|:--|
> | Container baseline | ★ 100 Up (April 23, 2026) | Supersedes 105/105 April 6 baseline |
> | Dedicated AAACPE stack | ✅ ACTIVE | `allis-aaacpe-scraper:8048→8033` + `allis-aaacpe-rag:8047→8032` — supersedes legacy `allis-ingest-api` + `allis-ingest-watcher` |
> | PostgreSQL two-container split | ★ ACTIVE | `production msallis-db host 5433` (16 GB, 294 tables, 11 schemas) + `forensic postgis-forensic host 5452` (17 GB, 314 tables) |
> | ChromaDB | ★ 48 collections, ~6,740,611 total vectors | `/api/v2/` only; `/api/v1/` permanently removed; host port 8002 → container 8000; pinned to `chromadb/chroma:0.6.3` |
> | `appalachian_english_corpus` | ★ 210 docs, 38 sources, 6-hour cron | UUID: `97fe5844-eb31-45c5-ad27-1d7e140e4eac`, cosine space; was zero-count April 9, clean recreated |
> | `msallis_docs` | ★ 4,192 items (March 28 baseline) | Verify-current |
> | Caddy `forward_auth` (OI-36-A) | ✅ CLOSED | HTTP 401 enforced before port 8050 — corpus traffic gates at proxy perimeter |
> | BBB six-filter stack | ✅ All 6 confirmed responding | Live steg catch documented: `"override your safety filters"` → `prompt_injection_keywords`, `severity=CRITICAL`, blocked ✅ |
> | Crontab hygiene (April 9) | ✅ Documented | `0 */6 * * *`, absolute paths, `CRYPTO_ADMIN_TOKEN` in `~/.allis_policy_token` (chmod 600) |
> | `local_resources` | ★ 207 items / all 55 WV counties | Geographic completeness benchmark for corpus coverage gaps |

---

## Why This Matters for Polymathmatic Geography

This chapter describes the dedicated data ingest pipeline that gives Ms. Allis grounded, Appalachian-specific knowledge — not generic web content, but public information selected and filtered for community stewardship.

- **P1 – Every where is entangled** by recognizing that a health story from McDowell County is entangled with infrastructure policy from Charleston, linguistic patterns from rural Fayette, and governance decisions from Morgantown. The AAPCappE corpus captures these entanglements by indexing content from 38 sources across Appalachian media, policy, and community outlets — and benchmarks geographic completeness against `local_resources` (207 items / all 55 WV counties).
- **P3 – Power has a geometry** by making the scraper architecture explicitly auditable — every URL scraped, every BBB filter gate, every GBIM entity commit is logged. The power to define what Ms. Allis knows about Appalachia is not held by a vendor or algorithm; it is held by a governed pipeline with documented inclusion/exclusion criteria and DGM oversight.
- **P5 – Design is a geographic act** by treating corpus scope as a design decision with geographic consequences. Non-active sources (Appalachian Studies 404, dead feeds, Facebook scrapers without `<article>` elements) are documented rather than silently excluded — making coverage gaps visible as governance information.
- **P12 – Intelligence with a ZIP code** by grounding the corpus in West Virginia–specific sources (WV Watch, WOAY, WV Policy, WV Tourism, WV Public Economy, AppVoices) and validating GBIM entity commits against `production msallis-db:5433` ★ spatial tables with `confidence_decay` metadata, so that place-specific claims carry epistemic accountability.
- **P16 – Power accountable to place** by routing all scraped content through the six-filter BBB stack before storage, logging every filter gate event at `allis-memory:8056`, and subjecting corpus changes to DGM-Sprint-Level governance — so the community can inspect what goes into the system and why.

As such, this chapter belongs to the **Computational Instrument tier**: it specifies the always-on, six-hour-cycle ingest infrastructure that continuously refreshes Ms. Allis's knowledge of Appalachian public life.

---

## 30.1 Purpose of AAPCappE in Ms. Allis

The **AAPCappE scraper and corpus** are designed to collect public, ethically accessible data relevant to Appalachian communities, policy and governance, and poverty, health, environment, and infrastructure — and to provide Ms. Allis with better context for answering questions, evidence for `rag_grounded_v2` (healthy at `127.0.0.1:7241`, `dgm_available: true`) and judge pipeline decisions, and material for identifying structural patterns in Appalachian life.

AAPCappE is **not** a generic web crawler and **not** a surveillance tool. It is a focused, purpose-built pipeline for Appalachian public content that is explicitly allowed for research and stewardship use. The dedicated stack — `allis-aaacpe-scraper:8048→8033` and `allis-aaacpe-rag:8047→8032` — is always on, running a six-hour cron cycle (`0 */6 * * *`). This supersedes the legacy `allis-ingest-api` + `allis-ingest-watcher` path, which is no longer the AAACPE data route.

---

## 30.2 Ethical Scraping Principles

AAPCappE is built on five ethical constraints that are encoded in scraper configuration, corpus filters, and downstream RAG and GBIM ingestion rules — not stated only as policy.

**Respect for robots.txt and site policies** means the scraper does not access sites that disallow bots or research use. Non-cooperative sources are listed explicitly in the non-active source inventory (see §30.3a) rather than silently dropped, making exclusion decisions auditable.

**No scraping behind logins or paywalls** means personal data and gated content are avoided. The scraper targets `<article>` elements and structured public HTML; sources that do not expose parseable article elements (such as certain Facebook pages and dead feeds) are documented as non-active.

**Rate-limiting and politeness** means the scraper uses backoffs and maximum request limits to avoid harming site performance. Crontab scheduling (`0 */6 * * *`) spaces runs six hours apart, and absolute paths under `/home/cakidd/` prevent accidental duplicate execution.

**Transparency and traceability** means URLs scraped, timestamps, and parsing decisions are logged for auditing. The `CRYPTO_ADMIN_TOKEN` is stored in `~/.allis_policy_token` (chmod 600) — not in environment variables or crontab entries — enforcing a governance rule that credentials are never exposed in process listings.

**Survivor safety and spiritual sensitivity** means the scraper avoids personal trauma narratives not clearly intended for public analysis, and content that could re-identify or retraumatize individuals. All scraped content passes through the **six-filter BBB stack** (ethical ✅, spiritual ✅, safety ✅, threat_detection ✅, steganography ✅, truth_verification ✅) before storage — confirmed by the live steg catch ("override your safety filters" → `prompt_injection_keywords`, `severity=CRITICAL`, blocked ✅), which proves the filter is active for corpus content, not just chat. Cross-reference: Ch 29 §29.3 (live steg catch documentation).

---

## 30.3 Dedicated Stack Architecture

The AAACPE dedicated stack consists of two always-on services:

```
┌─────────────────────────────────────────────────────────────┐
│   AAACPE Dedicated Stack Architecture                       │
│   ★ Active as of April 23, 2026                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────────────────────────────┐          │
│  │  allis-aaacpe-scraper                        │          │
│  │  Host: 8048 → Container: 8033                │          │
│  │  Schedule: 0 */6 * * * (6-hour cron)         │          │
│  │  Paths: absolute, under /home/cakidd/        │          │
│  │  Auth: CRYPTO_ADMIN_TOKEN in                 │          │
│  │    ~/.allis_policy_token (chmod 600)          │          │
│  │  Outputs: cleaned text + metadata            │          │
│  │    (title, date, author, source tag)         │          │
│  └──────────────────────────────────────────────┘          │
│      ↓ scraped content                                      │
│  ┌──────────────────────────────────────────────┐          │
│  │  BBB Six-Filter Gate                         │          │
│  │  (allis-blood-brain-barrier:8016)            │          │
│  │  EthicalFilter ✅ · SpiritualFilter ✅       │          │
│  │  SafetyMonitor ✅ · ThreatDetection ✅       │          │
│  │  steganography_filter ✅ · truth_verification ✅        │
│  └──────────────────────────────────────────────┘          │
│      ↓ filtered content                                     │
│  ┌──────────────────────────────────────────────┐          │
│  │  allis-aaacpe-rag                            │          │
│  │  Host: 8047 → Container: 8032                │          │
│  │  Indexes into ChromaDB collections           │          │
│  │  GBIM entities → production msallis-db:5433  │          │
│  │    with confidence_decay metadata            │          │
│  │  via allis-gbim-query-router:7205            │          │
│  └──────────────────────────────────────────────┘          │
│      ↓                   ↓                                  │
│  ChromaDB               production msallis-db:5433 ★       │
│  host 8002→8000         16 GB, 294 tables, 11 schemas      │
│  48 collections         forensic postgis-forensic:5452 ★   │
│  ~6,740,611 vectors     17 GB, 314 tables (PostGIS)        │
│  /api/v2/ only                                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Figure 30.1.** AAACPE dedicated stack (★ April 23, 2026): scraper → BBB six-filter gate → RAG indexer → ChromaDB (48 collections, ~6,740,611 vectors, `/api/v2/` only) + PostgreSQL (`production msallis-db:5433` ★ 16 GB for GBIM; `forensic postgis-forensic:5452` ★ 17 GB for PostGIS geometry). Legacy `allis-ingest-api` + `allis-ingest-watcher` path is superseded.

### 30.3a AAPCappE First-Run Results (March 27, 2026)

On first run (March 27, 2026), the scraper indexed 39 sources and produced 65 documents on startup (`total_runs: 1`). By March 28, subsequent runs had expanded `msallis_docs` to 4,192 items. Cross-reference: Ch 27 §27.1a (full first-run history).

**Active sources (primary contributors as of March 28 baseline):**

| Source | Documents contributed |
|:--|:--|
| WV Watch | 50 |
| WOAY | 35 |
| Daily Yonder | 14 |
| WV Tourism | 12 |
| WV Public Economy | 12 |
| WV Policy | 10 |
| AppVoices | 10 |
| WBOY | 10 |
| Additional sources | Remainder to 4,192 |

**Non-active sources (documented for governance transparency):**

| Source | Reason |
|:--|:--|
| Appalachian Studies | HTTP 404 — dead endpoint |
| Fairmont State | Dead feed |
| OHVEC | Dead feed |
| Facebook scrapers | No `<article>` elements parseable |

Non-active sources are documented rather than silently excluded. If any source becomes active or resolvable, re-inclusion is a DGM-Sprint-Level decision.

### 30.3b Crontab Hygiene (April 9, 2026)

Crontab governance rules confirmed April 9, 2026:

- Schedule: `0 */6 * * *` — six-hour cycle
- All paths: absolute, under `/home/cakidd/`
- `get/create collection` fallback — if a collection is missing at run time, the scraper creates it rather than failing silently
- `CRYPTO_ADMIN_TOKEN` stored in `~/.allis_policy_token` (chmod 600) — never in environment variables or crontab entries
- Crontab entries do not contain credentials inline

---

## 30.4 Corpus Curation and Filtering

The AAPCappE corpus is not a raw dump. Documents are tagged by geography (county, ZIP code where identifiable), topic (health, environment, economy, governance), and source type (government, nonprofit, news, community narrative). They are filtered for relevance to Appalachian communities and appropriateness for Ms. Allis's roles as steward, not voyeur.

Content that is clearly personally identifying, sensitive in a way not intended for public analysis, or potentially retraumatizing without strong public-interest justification is either excluded entirely or abstracted into high-level GBIM statements without direct quotation. These decisions are logged and subject to DGM governance — they are not made ad hoc.

**Geographic completeness benchmark:** `local_resources` (207 items / all 55 WV counties) is the most geographically complete community resource substrate in the system. AAPCappE corpus completeness can be benchmarked against it: if a county has no AAPCappE documents, that is a targeted scraping gap and a governance-visible coverage failure. Cross-reference: Ch 34 §34.6 (`local_resources` as geographic substrate).

Corpus management includes versioning (track corpus versions over time, allow rollback and differential analysis) and documentation (describe included domains and topics, specify inclusion and exclusion criteria). The `appalachian_english_corpus` collection resilience lesson is documented here: the collection was zero-count April 9, 2026, was clean-recreated (UUID: `97fe5844-eb31-45c5-ad27-1d7e140e4eac`, cosine space), and now holds 210 docs from 38 sources on a six-hour cron. Cross-reference: Ch 28 §28.7b (clean recreate procedure and backup discipline).

---

## 30.5 Integration with RAG and GBIM

AAPCappE corpus content feeds into ChromaDB RAG collections and GBIM entities, creating the knowledge substrate that Ms. Allis draws on when responding to community questions.

**ChromaDB collections fed by AAPCappE (★ April 23, 2026):**

| Collection | Content | Notes |
|:--|:--|:--|
| `appalachian_english_corpus` | 210 docs, 38 sources, 6-hour cron | Linguistic and cultural grounding; cosine space; UUID `97fe5844-eb31-45c5-ad27-1d7e140e4eac` |
| `msallis_docs` | 4,192 items (March 28 baseline; verify-current) | Primary Appalachian policy and news corpus |
| Geography/policy collections | Various | Exposed via `allis-gis-rag:8004` for geographic queries |

ChromaDB inventory: ★ **48 collections, ~6,740,611 total vectors**; host port **8002** → container port 8000; `/api/v2/` only (`/api/v1/` permanently removed); pinned to `chromadb/chroma:0.6.3`. `conversation_history` collection was wiped and reseeded clean April 16, 2026 — post-wipe accumulation only.

**GBIM integration via `production msallis-db:5433` ★:**

Derived facts — for example, "Fayette County has X% broadband coverage" — may be stored as GBIM entities with `confidence_decay` metadata, linked to specific counties, ZIP codes, or institutions. GBIM entity commits route through `allis-gbim-query-router:7205`. The GBIM entity floor grows at approximately 288 per day from `autonomous_learner` commits (~23,200+ records as of April 23); AAPCappE-sourced entities add to this floor. `confidence_decay_aware` principles in the Constitutional Guardian (`allis-constitutional-guardian:8091`) cross-check decay metadata before treating any AAPCappE-sourced belief as confirmed ground truth for enforcement decisions.

**PostGIS integration via `forensic postgis-forensic:5452` ★:**

Geographic claims from the corpus (county boundaries, ZIP-code-level service coverage) are validated against `forensic postgis-forensic:5452` ★ (17 GB, 314 tables). The April 6 baseline of `gisdb / msallisgis` at `host:5432 / container-internal:5452 — 45 GB, 548 tables` is superseded by the April 23 two-container split. Cross-reference: Ch 28 §28.7 (GIS RAG two-container split detail).

**RAG services receiving AAPCappE content:**

- `allis-gis-rag:8004` — geographic and policy content
- `allis-spiritual-rag:8005` — community values and spiritual/cultural content
- `rag_grounded_v2` — healthy at `127.0.0.1:7241`, `dgm_available: true` — truth-verification endpoint for judge pipeline

---

## 30.6 Governance and Oversight

AAPCappE is governed by the same oversight structures as the rest of Ms. Allis, applied specifically to the ingest pipeline.

**Constitutional Guardian** (`allis-constitutional-guardian:8091`) ensures scraping and corpus use are consistent with privacy protections, community sovereignty (`10a-no-extraction` principle), and general welfare principles. The guardian's `postgresql_validation` blocks cross-check `production msallis-db:5433` ★ GBIM entities and `forensic postgis-forensic:5452` ★ PostGIS boundaries before allowing corpus-derived facts to influence enforcement decisions.

**Caddy `forward_auth` perimeter (OI-36-A CLOSED):** Corpus-adjacent API endpoints (including `allis-aaacpe-rag:8047`) are accessible only through authenticated routes. The Caddy layer enforces HTTP 401 before requests reach the ingest stack — an unauthenticated corpus update request is blocked at the proxy perimeter. Cross-reference: Ch 36 §36.2 (Caddy as zero-th gate); Ch 37 §37.2 (constitutional guardian behind Caddy).

**Spiritual root and survivor safety:** SpiritualFilter and SafetyMonitor (SafetyMonitor recalibrated April 3 — `safety_score=1.0` on survivor/victim queries) flag corpus content that contradicts safety commitments or leans on harmful narratives. The live steg catch confirms that the `steganography_filter` is active for corpus traffic. All BBB gate events are logged at `allis-memory:8056`.

**Dynamic Governance Mechanisms (DGMs)** (Ch. 32) govern changes to scraping targets, filter adjustments, and domain additions or removals. Adding a new source to the scraper schedule is a DGM-Sprint-Level decision — it cannot be done unilaterally. DGMs also govern the `appalachian_english_corpus` schedule (currently `0 */6 * * *`); changing the cron interval is a governed change.

Community input channels allow local partners to provide feedback on which feeds are helpful or feel extractive, and to request exclusion of certain content types. All such changes are logged, tied to DGMs, and visible in system governance documents.

---

## 30.7 Implementation Status

| Component | Status | Notes |
|:--|:--|:--|
| `allis-aaacpe-scraper` (host 8048→8033) | ✅ Implemented — dedicated stack active | Supersedes legacy `allis-ingest-api` |
| `allis-aaacpe-rag` (host 8047→8032) | ✅ Implemented — dedicated stack active | Supersedes legacy `allis-ingest-watcher` |
| `appalachian_english_corpus` | ✅ 210 docs, 38 sources, 6-hour cron | Clean-recreated post zero-count April 9; UUID `97fe5844-eb31-45c5-ad27-1d7e140e4eac` |
| `msallis_docs` | ✅ 4,192 items (March 28 baseline) | Verify-current |
| Crontab hygiene | ✅ Documented (April 9, 2026) | `0 */6 * * *`, absolute paths, credential governance |
| BBB six-filter gate on corpus content | ✅ All 6 confirmed responding | Live steg catch proves filter active for corpus, not just chat |
| GBIM integration (`production msallis-db:5433` ★) | ✅ Via `allis-gbim-query-router:7205` | `confidence_decay` metadata on all entity commits |
| PostGIS integration (`forensic postgis-forensic:5452` ★) | ✅ Supersedes legacy `gisdb:5432` | April 23 two-container split; 17 GB, 314 tables |
| `rag_grounded_v2` integration | ✅ `127.0.0.1:7241`, `dgm_available: true` | Truth-verification endpoint for judge pipeline |
| Geographic coverage benchmark vs `local_resources` | ⚠️ Partially implemented | 207 items / 55 WV counties as benchmark; per-county gap analysis not yet automated |
| Corpus browser / user-facing source transparency | 🔲 Future work | Design intent; no UI built yet |
| Robust survivor-focused filters for trauma-heavy historical content | 🔲 Future work | Current SafetyMonitor covers live queries; corpus-specific trauma triage is future work |
| Automated PIA reminders for corpus expansion changes | 🔲 Future work | DGM-Sprint-Level trigger defined; automation not yet wired |
| Per-county AAPCappE coverage gap alert | 🔲 Future work | Benchmark against `local_resources` defined; automated alert not yet built |

---

## Cross-Reference Map

| This section | Cross-chapter reference |
|:--|:--|
| §30.2 ethical scraping / BBB gate | Ch 29 §29.3 (live steg catch); Ch 16 (BBB architecture); Ch 20 (first-stage filtering) |
| §30.3a first-run results | Ch 27 §27.1a (first-run history) |
| §30.3b crontab hygiene | Ch 28 §28.7b (backup and cron discipline) |
| §30.4 `appalachian_english_corpus` clean recreate | Ch 28 §28.7b (clean recreate procedure) |
| §30.4 `local_resources` coverage benchmark | Ch 34 §34.6 (geographic substrate); Ch 31 §31.5 (MountainShares community data) |
| §30.5 ChromaDB `conversation_history` wipe | Ch 29 §29.6; Ch 33 §33.7 |
| §30.5 GBIM integration | Ch 27 §27.4 (autonomous learning); Ch 33 §33.7 (ensemble ground truth) |
| §30.5 PostGIS two-container split | Ch 28 §28.7 (GIS RAG detail); Ch 37 §37.1 (constitutional guardian PostGIS) |
| §30.6 Constitutional Guardian | Ch 37 §37.3 (`10a-no-extraction` principle); Ch 37 §37.4.1 (Caddy before guardian) |
| §30.6 Caddy perimeter (OI-36-A) | Ch 36 §36.2 (Caddy as zero-th gate); Ch 35 §35.4 (watchdog coverage) |
| §30.6 DGM governance | Ch 32 §32.6 (swarm functions and corpus scope) |
| §30.6 survivor safety | Ch 29 (psychological safeguards); Ch 34 §34.4 (Mother Carrie protocol) |

---

*Chapter 30 — AAPCappE Scraper and Corpus*
*Ms. Egeria Allis Steward System — Harmony for Hope, Inc.*
*Mount Hope, West Virginia*
*Last updated: ★ 2026-04-23 — Carrie Kidd (Mamma Kidd)*
*★ 100 containers Up — dedicated AAACPE stack active — `appalachian_english_corpus` 210 docs / 6-hour cron — BBB six-filter gate confirmed on corpus traffic — `production msallis-db:5433` ★ + `forensic postgis-forensic:5452` ★*
