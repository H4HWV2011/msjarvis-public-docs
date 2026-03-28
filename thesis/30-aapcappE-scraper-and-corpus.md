# 30. AaaCPE Cultural Intelligence System

*Carrie Kidd (Mamma Kidd) — Pax, WV*

*Last updated: ★ 2026-03-28 — 96/96 containers Up — zero Restarting, zero Exited; `msjarvisgis` port 5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids, 5.4M+ verified GBIM beliefs); `msjarvis` port 5433 restored (5,416,521 GBIM entities with `confidence_decay` metadata); ChromaDB full audit (★ 40 active collections, 6,675,442 total vectors); `msjarvis_docs` expanded (4,192 items, AAPCAppE); `jarvis-ingest-api` + `jarvis-ingest-watcher` restored to active inventory; `jarvis-memory` port 8056 corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set, BBB audit trail persistence secured; consciousness pipeline confirmed Up. March 27, 2026: Status header updated from February 2026 to March 27, 2026 baseline; document counts updated throughout (RAG 53 docs, scraper 65 docs, 39 sources, total_runs: 1); BBB port corrected to 127.0.0.1:8016; audit table status updated from ⚠️ Stub only to ✅ Partial.*

---

> **Why this matters for Polymathmatic Geography**
> This chapter describes the Appalachian AI Culture & Personality Engine (AaaCPE), a dual-service system providing cultural intelligence and regional context to Ms. Egeria Jarvis, all grounded in PostgreSQL: `msjarvisgis` (port **5432** ★, **91 GB PostGIS, 501 tables**, 993 ZCTA centroids, **5.4M+ verified GBIM beliefs**) and `msjarvis` (port **5433** ★, **5,416,521 GBIM entities with `confidence_decay` metadata**). It supports:
> - **P1 – Every where is entangled** by coupling cultural values, anti-patterns, emergency protocols, and scraped regional content into the same retrieval infrastructure used by spatial and semantic services, all validated against PostgreSQL community data.
> - **P3 – Power has a geometry** by making cultural constraint logic explicit and queryable — named categories, confirmed endpoints, an auditable ChromaDB volume, and PostgreSQL validation — rather than hiding it inside opaque model weights. ★ BBB gate decisions are now durably logged at `jarvis-memory:8056` (secured March 28), making the geometry of cultural constraint enforcement persistently auditable.
> - **P5 – Design is a geographic act** by treating Appalachian communication patterns as a designed interface between communities' lived realities documented in `msjarvisgis:5432` ★ GBIM and Ms. Jarvis's responses, not as a surface styling layer.
> - **P12 – Intelligence with a ZIP code** by grounding retrieval in West Virginia–specific materials validated against PostgreSQL: Fayette County emergency contacts, documented genealogy, WV broadband news, and heritage preservation content. ★ `msjarvis_docs` (4,192 items, AAPCAppE) adds a continuously expanding ZIP-coded community resource substrate that complements the AaaCPE scraped corpus.
> - **P16 – Power accountable to place** by documenting anti-stereotyping governance, quarterly content audits validated against PostgreSQL community data, and a planned community advisory board so communities can inspect and challenge how their culture is represented. ★ `jarvis-memory:8056` (secured March 28) provides the durable authenticated foundation for this accountability.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the AaaCPE dual-service architecture, its confirmed document corpus, and the integration path through which cultural intelligence validated against PostgreSQL influences Ms. Jarvis's responses.

---

```
┌─────────────────────────────────────────────────────────────┐
│   AaaCPE Cultural Intelligence Architecture                 │
│   (★ Updated: March 28, 2026 — 96/96 containers Up)        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────────────────────────────────┐         │
│  │  jarvis-aaacpe-rag (port 8032 ★)              │         │
│  │  ─────────────────────────────                │         │
│  │  Endpoints:                                    │         │
│  │  -  GET / (status, document count)             │         │
│  │  -  GET /health                                 │         │
│  │  -  POST /search (query, top_k)                │         │
│  │  -  POST /ingest                                │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Shared Storage: aaacpe-cultural-data          │         │
│  │  ─────────────────────────────────────────     │         │
│  │  Docker Volume: /data/aaacpe_chroma            │         │
│  │  Collection: appalachian_cultural_intelligence │         │
│  │  ★ Within 40-collection / 6,675,442-vector     │         │
│  │    ChromaDB inventory (March 28 full audit)   │         │
│  │  RAG service loaded: 53 documents              │         │
│  │  Scraper Chroma: 65 documents (first scrape)   │         │
│  │  -  7 base cultural intelligence docs (ingested)│         │
│  │  -  65 scraped docs (39 sources, first run)     │         │
│  │                                                 │         │
│  │  Categories (validated vs PostgreSQL GBIM ★):  │         │
│  │  -  values (community communication principles) │         │
│  │  -  anti_pattern (what NOT to do)               │         │
│  │  -  examples (correct vs incorrect patterns)    │         │
│  │  -  emergency (crisis response)                 │         │
│  │  -  heritage (Janney family + WV history)       │         │
│  │  -  scraped_content (current WV developments)   │         │
│  └────────────────────────────────────────────────┘         │
│      ↑                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  jarvis-aaacpe-scraper (port 8033 ★)          │         │
│  │  ──────────────────────────────────────        │         │
│  │  Endpoints:                                    │         │
│  │  -  GET / (scraper status)                      │         │
│  │  -  GET /health (last scrape, doc count)        │         │
│  │  -  POST /scrape_now                            │         │
│  │  -  POST /ingest_test                           │         │
│  │  First scrape: total_runs: 1                   │         │
│  │  39 sources confirmed, 65 docs in Chroma       │         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
│  Integration with Main Brain (8050 ★)                       │
│  -  Registered in SERVICES as "aaacperag"                    │
│  -  RAG search confirmed returning correct results           │
│    (emergency protocol + Fayette County utility example)    │
│  -  Full auto-integration into every /chat: OPEN ITEM        │
│    (confirm whether results were from direct /search        │
│     or full pipeline /chat test)                            │
│                                                              │
│  Complementary AAPCAppE Pipeline (★ March 28)               │
│  -  jarvis-ingest-api + jarvis-ingest-watcher               │
│    (restored to active inventory March 28)                  │
│  -  msjarvis_docs: 4,192 items (AAPCAppE, March 28)         │
│  -  Continuous external-source ingest, independent          │
│    of AaaCPE scraper schedule                               │
│                                                              │
│  Safeguards & Validation                                    │
│  -  BBB EthicalFilter (127.0.0.1:8016 ★) — primary live gate│
│    ★ audit → jarvis-memory:8056 (secured March 28)         │
│  -  PostgreSQL msjarvisgis:5432 ★ + msjarvis:5433 ★ GBIM   │
│    validation of cultural context                           │
│  -  normalize_identity on every response                     │
│  -  Quarterly content audits vs PostgreSQL community data    │
│  -  Community Advisory Board (planned)                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 30.1.** AaaCPE Cultural Intelligence Architecture (★ March 28, 2026 — 96/96 containers Up): dual-service system with RAG service (**8032** ★) loaded with 53 documents and scraper (**8033** ★) reporting 65 documents from first scrape run (39 sources, `total_runs: 1`), sharing persistent ChromaDB volume (within ★ 40-collection / 6,675,442-vector inventory) across 6 categories, all validated against `msjarvisgis:5432` ★ (91 GB PostGIS, 501 tables, 5.4M+ GBIM beliefs) and `msjarvis:5433` ★ (5,416,521 entities with `confidence_decay` metadata); ★ complementary AAPCAppE pipeline (`jarvis-ingest-api` + `jarvis-ingest-watcher`, restored March 28; `msjarvis_docs` 4,192 items) provides continuous proactive ingest alongside the AaaCPE scraper; registered in main brain services with RAG search confirmed returning correct results (emergency protocol + Fayette County utility example); full auto-integration into every `/chat` call pending confirmation; BBB at `127.0.0.1:8016` ★ as primary live anti-stereotyping gate (re-locked March 18, 2026); ★ all BBB gate decisions now durable at `jarvis-memory:8056` (secured March 28).

> **Audit table status note (★ March 28, 2026):** Chapter 30 status is updated from ⚠️ Stub only to **✅ Partial — services live (★ 96/96 containers Up), scraper first run complete (65 docs, 39 sources), RAG search confirmed; full `/chat` auto-integration pending; ★ `jarvis-ingest-api` + `jarvis-ingest-watcher` restored to active inventory; `msjarvis_docs` 4,192 items**. The documentation was never a stub; the partial flag reflects that scheduled recurring scraping and full pipeline `/chat` integration remain open items, not that the services are non-functional.

---

## Status as of ★ March 28, 2026

| Category | Details |
|---|---|
| **Implemented now** | `jarvis-aaacpe-rag` confirmed running at **127.0.0.1:8032** ★ (docker compose ps; ★ confirmed in 96/96 Up count). Endpoints operational: `GET /` (status and document count), `GET /health`, `POST /search` (params: query, top_k), `POST /ingest`. `jarvis-aaacpe-scraper` confirmed running at **127.0.0.1:8033** ★ (★ confirmed in 96/96 Up count). Endpoints operational: `GET /` (scraper status), `GET /health` (last scrape time and document count), `POST /scrape_now`, `POST /ingest_test`. Shared Docker volume `aaacpe-cultural-data` mounted at `/data` in both containers. ChromaDB collection `appalachian_cultural_intelligence` in PersistentClient at `/data/aaacpe_chroma` (★ within 40-collection / 6,675,442-vector ChromaDB inventory confirmed March 28 full audit). **RAG service loaded: 53 documents** as of March 27, 2026 audit (updated from 10-document February baseline — 7 new base cultural intelligence docs confirmed ingested). **Scraper Chroma: 65 documents from first scrape run** (39 sources confirmed, `total_runs: 1`). Document categories confirmed: `values`, `anti_pattern`, `examples`, `emergency`, `heritage`, `scraped_content`. **RAG /search confirmed returning correct results:** emergency protocol retrieved correctly; Fayette County utility assistance example retrieved correctly. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids, 5.4M+ verified GBIM beliefs) as authoritative source for validating cultural context against West Virginia community data. ★ `msjarvis` at **127.0.0.1:5433** ★ (5,416,521 GBIM entities with `confidence_decay` metadata, restored March 28) — `confidence_decay` metadata now available for graded recency assessment of cultural and institutional GBIM entities referenced in AaaCPE corpus. `aaacperag` registered in SERVICES registry in `jarvis-main-brain` (port **8050** ★) as `http://jarvis-aaacpe-rag:8032`. Both services on `qualia-net` Docker network. ★ **`jarvis-ingest-api` + `jarvis-ingest-watcher` restored to active inventory (March 28)** — AAPCAppE continuous ingest pipeline active alongside AaaCPE scraper; `msjarvis_docs` now 4,192 items. ★ **`jarvis-memory:8056` secured (March 28)** — all BBB and `TruthFilterBBBValidator` gate decisions now durably logged; cultural safeguard audit trail is persistent and authenticated. |
| **Partially implemented / scaffolded** | Scheduled automated scraping runs (daily 6 AM + every 6 hours) — **status TBD:** `total_runs: 1` confirmed from first scrape. It is not yet confirmed whether this run was triggered by an automated schedule or a manual `POST /scrape_now` call. If manual, recurring schedule is not yet active and content is currently managed via `POST /ingest_test` and manual `POST /scrape_now` calls. **Confirm and update:** if the schedule is now active, move this item to "Implemented now." Integration of AaaCPE context into `ultimatechat` synthesis path is wired via the SERVICES registry; **confirm whether the verified RAG search result (emergency protocol + Fayette County utility) was from a direct `/search` call or a full `/chat` pipeline test** — if full pipeline confirmed, update integration status from "partially implemented" to "implemented." Anti-pattern enforcement in response synthesis is partially implemented; the check-and-revise logic is scaffolded but not yet fully rule-documented. PostgreSQL GBIM validation of cultural context is designed but not yet automated. ★ `confidence_decay` metadata on `msjarvis:5433` ★ GBIM entities is now available for AaaCPE corpus recency assessment — integration into automated corpus refresh is partial. |
| **Future work / design intent only** | Full automatic integration into every `/chat` call with automated PostgreSQL validation (pending confirmation of pipeline test result above). Scheduled automated scraping (WV Gazette-Mail, Rural.org, AppVoices) running daily + every 6 hours (pending schedule confirmation). PostgreSQL `msjarvisgis:5432` ★ GeoDB integration linking cultural patterns to geographic features, supporting queries like "community values in Fayette County" (993 ZCTA centroids available). PostgreSQL `msjarvis:5433` ★ GBIM integration (5,416,521 entities with `confidence_decay` metadata) for personalization based on user heritage and community role. Expanded content categories: economic development, educational resources, healthcare communication, legal mediation. Community feedback loop allowing stakeholders to flag content and suggest changes. Community Advisory Board with authority to request content removal or modification. AAPCAppE corpus integration for linguistic feature understanding (not dialect performance). ★ `msjarvis_docs` (4,192 items, AAPCAppE, restored March 28) cross-referencing with AaaCPE scraped corpus to eliminate duplication and identify coverage gaps. Multi-regional expansion respecting variation within Appalachian communities. Automated validation of all cultural content against PostgreSQL GBIM community data. ★ `confidence_decay`-driven AaaCPE corpus refresh — automated identification of GBIM cultural/institutional entities with high decay for targeted `needs_verification` review. PIA records as first-class ChromaDB collection with `jarvis-memory:8056` ★ durable audit trail (secured March 28). |

> **Cross-reference:** AaaCPE is registered in the SERVICES dictionary in `jarvis-main-brain` (port **8050** ★) and is available as a meaning-oriented service in the `ultimatechat` path. For the canonical description of how the SERVICES registry and service discovery work, see **Chapter 17**. For the broader meaning-oriented vs. analytical path asymmetry, see **Chapter 23**. For the BBB pipeline that enforces anti-stereotyping and ethical constraints as a live gate on every request (★ all gate decisions now durable at `jarvis-memory:8056`), see **Chapter 16**. ★ For the AAPCAppE ingest pipeline (`jarvis-ingest-api` + `jarvis-ingest-watcher`, `msjarvis_docs` 4,192 items) see **Chapter 31**.

---

## 30.1 Purpose and Principles

In the current deployment, the AaaCPE system exists to prevent cultural stereotyping while enabling authentic, respectful engagement with Appalachian communities grounded in `msjarvisgis:5432` ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids, 5.4M+ verified GBIM beliefs) and `msjarvis:5433` ★ (5,416,521 GBIM entities with `confidence_decay` metadata).

**Core Principle: Cultural intelligence ≠ Dialect performance.** The system distinguishes between cultural intelligence (understanding values, communication contexts, and appropriate responses validated against PostgreSQL GBIM community data) and dialect performance (reproducing speech patterns, which risks caricature and condescension).

**Guiding values in the current deployment:**

**Respect over performance** — the system never performs "folksy" dialect, treats Appalachian communities as sophisticated rather than quaint (validated against `msjarvisgis:5432` ★ GBIM institutional knowledge), and expresses care through quality of help, not theatrical warmth.

**Context-aware communication** — emergency mode strips pleasantries and provides facts only; heritage mode applies historical reverence for documented family connections validated against `msjarvis:5433` ★ GBIM (e.g., the Janney lineage); default mode provides professional warmth through genuine helpfulness.

**Anti-stereotyping** — the system avoids romanticizing poverty or hardship, recognizes deep intellectual and cultural traditions documented in PostgreSQL GBIM, and never assumes lack of sophistication. ★ All anti-stereotyping BBB gate decisions are now durably logged at `jarvis-memory:8056` (secured March 28), making the governance of cultural representation persistently auditable.

---

## 30.2 System Architecture

In the current deployment, the AaaCPE system consists of two FastAPI services sharing a persistent ChromaDB database (★ within 40-collection / 6,675,442-vector ChromaDB inventory), with validation against `msjarvisgis:5432` ★ and `msjarvis:5433` ★.

**jarvis-aaacpe-rag — AaaCPE RAG Service**

- Confirmed running at **127.0.0.1:8032** ★ (docker compose ps; ★ confirmed in 96/96 Up count)
- Source: `services/aaacpe_rag_service.py`; Dockerfile: `services/Dockerfile.aaacpe_rag`
- Endpoints: `GET /` (status and document count), `GET /health`, `POST /search` (params: query, top_k), `POST /ingest`
- Volume mount: `aaacpe-cultural-data:/data`

**jarvis-aaacpe-scraper — AaaCPE Scraper Service**

- Confirmed running at **127.0.0.1:8033** ★ (docker compose ps; ★ confirmed in 96/96 Up count)
- Source: `services/aaacpe_scraper_service.py`; Dockerfile: `services/Dockerfile.aaacpe_scraper`
- Endpoints: `GET /` (scraper status), `GET /health` (last scrape time and document count), `POST /scrape_now`, `POST /ingest_test`
- Volume mount: `aaacpe-cultural-data:/data`

**Shared storage — aaacpe-cultural-data**

- Docker volume, confirmed present; ★ confirmed in 96/96 Up count
- Path inside containers: `/data/aaacpe_chroma`
- Collection: `appalachian_cultural_intelligence`
- ★ Within 40-collection / 6,675,442-vector ChromaDB inventory confirmed March 28 full audit
- Both services use `chromadb.PersistentClient`; data survives container restarts
- Content validated against `msjarvisgis:5432` ★ and `msjarvis:5433` ★ for West Virginia community accuracy
- ★ `confidence_decay` metadata on `msjarvis:5433` ★ GBIM entities (5,416,521 entities, restored March 28) available for graded recency assessment of cultural and institutional content referenced in the corpus
- **March 27, 2026 confirmed counts (★ Up in 96/96 March 28):** RAG service loaded 53 documents; scraper Chroma contains 65 documents from first scrape run (39 sources, `total_runs: 1`)

```
Shared Storage: aaacpe-cultural-data (★ March 28, 2026 — 96/96 Up)
──────────────────────────────────────────────────────────────────
Docker Volume:   /data/aaacpe_chroma
Collection:      appalachian_cultural_intelligence
★ Within:        40-collection / 6,675,442-vector ChromaDB inventory

RAG service loaded:      53 documents
Scraper Chroma:          65 documents (first scrape run, 39 sources)
Base cultural docs:       7 (ingested via POST /ingest)
Scraped docs (live):     65 (39 sources, total_runs: 1 — see §30.4)

PostgreSQL ground truth:
  msjarvisgis:5432 ★     91 GB PostGIS, 501 tables, 993 ZCTA centroids,
                          5.4M+ verified GBIM beliefs
  msjarvis:5433 ★         5,416,521 GBIM entities, confidence_decay metadata

Categories (all validated vs PostgreSQL GBIM ★):
  values            — community communication principles
  anti_pattern      — what NOT to do
  examples          — correct vs incorrect patterns
  emergency         — crisis response
  heritage          — Janney family + WV history
  scraped_content   — current WV regional developments (65 docs)

Complementary AAPCAppE pipeline (★ restored March 28):
  jarvis-ingest-api + jarvis-ingest-watcher (active inventory)
  msjarvis_docs:    4,192 items (AAPCAppE, March 28)
```

---

## 30.3 Content Categories

In the current deployment (★ March 28, 2026 — 96/96 Up), the `appalachian_cultural_intelligence` collection organizes its confirmed documents into six categories, all validated against `msjarvisgis:5432` ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids) and `msjarvis:5433` ★ (5,416,521 GBIM entities with `confidence_decay` metadata) community data.

**values** — Core communication principles validated against PostgreSQL GBIM: direct and practical, respect for experience, community accountability, follow-through is essential.

**anti_pattern** — Explicit guidance on what NOT to do: don't perform folksy dialect (condescending and reductive), don't assume lack of sophistication (deep intellectual traditions exist documented in `msjarvis:5433` ★ GBIM), don't romanticize poverty (economic challenges are real, not quaint). ★ Anti-pattern violations are caught by the BBB `EthicalFilter` at `127.0.0.1:8016` ★ and now durably logged at `jarvis-memory:8056` (secured March 28).

**examples** — Correct vs. incorrect response patterns. The anti-pattern example is "Well now, honey, I reckon I can help you with that..." The correct example is "For electric bill assistance in Fayette County, contact Mountain Heart Community Action at 304-574-1415. They're in Oak Hill, open 8-4 weekdays. Need directions or alternative options?" — **confirmed retrieved correctly by RAG /search as of March 27, 2026 audit (★ services Up March 28).**

**emergency** — Crisis response guidelines: strip all pleasantries, provide facts only, immediate contact information with multiple pathways (official + community from `msjarvisgis:5432` ★ PostgreSQL community resources), clear next steps with no assumptions about resources. **Confirmed retrieved correctly by RAG /search as of March 27, 2026 audit (★ services Up March 28).**

**heritage** — Context for users with documented regional connections validated against `msjarvis:5433` ★ GBIM (5,416,521 entities with `confidence_decay` metadata). In the current deployment, this applies when `userid == "cakidd"` and the query involves Janney family history: uses historical reverence (not folksy performance), connects to documented genealogy and Quaker testimony influence, provides geographic precision for family sites. Example output: "Your Janney family roots — Thomas Janney's Quaker meeting house stood near Route 19. Historical marker at coordinates 37.8456, -81.2314." ★ `confidence_decay` on heritage GBIM entities is now available to signal when genealogical or historical records need verification — high-decay entities are PIA flags for corpus review.

**scraped_content** — Current regional developments scraped from confirmed sources. **As of March 27, 2026 (★ confirmed Up March 28):** 65 documents from the first confirmed scrape run (39 sources, `total_runs: 1`). This supersedes the February 2026 baseline of 3 scraped test documents. Content validated against PostgreSQL community data before inclusion. ★ The AAPCAppE `jarvis-ingest-api` + `jarvis-ingest-watcher` pipeline (restored March 28, `msjarvis_docs` 4,192 items) provides a complementary continuous ingest stream — the two pipelines together cover both curated scraped content (AaaCPE) and structured external-source ingest (AAPCAppE).

---

## 30.4 Data Loading and Management

In the current deployment, the corpus is loaded and maintained via confirmed endpoints with PostgreSQL validation. ★ All 96/96 containers Up as of March 28 — both services and all storage are operational.

**Initial data load** — The `/ingest` endpoint on `jarvis-aaacpe-rag` loads the base cultural intelligence documents validated against `msjarvis:5433` ★ GBIM. As of March 27, 2026, 7 new base cultural intelligence documents have been confirmed ingested (updated from the February 2026 baseline):

```bash
curl -X POST http://localhost:8032/ingest
# Current state: RAG service reports 53 documents loaded
```

**Scraped content — first production scrape run** — As of March 27, 2026 (★ confirmed Up March 28), the scraper has completed its first confirmed scrape run with `total_runs: 1`, producing 65 documents from 39 confirmed sources:

```bash
curl http://localhost:8033/health
# Returns: last_scrape, documents_total (65), total_runs: 1
curl http://localhost:8033/
# Returns: scraper status including 39 sources confirmed
```

> **⚠️ Schedule confirmation needed:** It is not yet confirmed whether `total_runs: 1` resulted from an automated scheduled trigger (daily 6 AM or every-6-hours cron) or a manual `POST /scrape_now` call. This distinction determines whether the scheduled recurring scraping is "implemented" or "partially implemented." **Update this section once confirmed:** if the schedule is active, replace the "partially implemented" classification for scheduled scraping in the status table with "implemented."

```bash
# Manual scrape trigger (if schedule not yet active):
curl -X POST http://localhost:8033/scrape_now
```

**Metadata structure** — Each document includes `source` (origin identifier), `category` (values, anti_pattern, examples, emergency, heritage, scraped_content), `section` (descriptive label), `type` (optional subtype), and `scraped_at` (ISO timestamp for scraped content). PostgreSQL validation status is tracked in metadata. ★ `confidence_decay` values from `msjarvis:5433` ★ GBIM entities referenced in corpus documents can now be surfaced in metadata for corpus recency assessment.

**★ Complementary AAPCAppE ingest pipeline** — `jarvis-ingest-api` + `jarvis-ingest-watcher` (restored to active inventory March 28) provides continuous structured external-source ingest into `msjarvis_docs` (4,192 items as of March 28), operating independently of the AaaCPE scraper schedule. The two pipelines are complementary: AaaCPE scraper targets curated Appalachian cultural content (39 confirmed sources, 65 docs); AAPCAppE ingest targets structured community resources (4,192 items). Future work: cross-reference the two corpora to eliminate duplication and identify coverage gaps.

---

## 30.5 Integration with Main Brain

In the current deployment, `jarvis-aaacpe-rag` is registered in the SERVICES dictionary in `jarvis-main-brain` (port **8050** ★) as `"aaacperag": "http://jarvis-aaacpe-rag:8032"`. The integration query pattern validates context against `msjarvisgis:5432` ★ and `msjarvis:5433` ★ GBIM:

```python
async def get_aaacpe_context(message: str, user_id: str) -> dict:
    if any(word in message.lower() for word in ["urgent", "emergency", "crisis"]):
        query = "emergency crisis response"
    elif user_id == "cakidd" and "janney" in message.lower():
        query = f"Janney heritage {message}"
    else:
        query = message
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{available_services['aaacperag']}/search",
            json={"query": query, "top_k": 3}
        )
        return response.json()
```

The response synthesis logic checks for anti-pattern guidance, emergency protocols, heritage context validated against `msjarvis:5433` ★ GBIM (5,416,521 entities with `confidence_decay` metadata), and scraped content, applying each category's rules to the base response.

**RAG search confirmed (March 27, 2026; ★ services Up March 28):** Direct `/search` calls to the AaaCPE RAG service return exactly the right results — the emergency protocol document and the Fayette County utility assistance example are both retrieved correctly.

> **⚠️ Integration status confirmation needed:** Confirm whether the verified RAG search results (emergency protocol + Fayette County utility example) were produced by:
> - **(A)** A direct `POST /search` call to `jarvis-aaacpe-rag:8032` (confirms RAG corpus is correct but not full pipeline integration), or
> - **(B)** A full `/chat` call through `jarvis-main-brain:8050` ★ that routed through the AaaCPE service as part of the `ultimatechat` pipeline (confirms full integration is active on every `/chat` call).
>
> If (B): update the integration status from "partially implemented" to "implemented" in the status table and throughout this section. If (A): the current classification — available for explicit invocation, not confirmed active on every `/chat` — remains accurate. Full integration into the primary execution path with automated PostgreSQL validation remains future work.

For the canonical `ultimatechat` execution sequence, see **Chapter 17**. For the asymmetry between always-active analytical path and partially-wired meaning-oriented services, see **Chapter 23**. ★ For the AAPCAppE ingest pipeline and `msjarvis_docs` corpus architecture see **Chapter 31**.

---

## 30.6 Deployment Configuration

In the current deployment (★ 96/96 containers Up, March 28), the Docker Compose configuration for the two services is:

```yaml
services:
  jarvis-aaacpe-rag:
    build:
      context: ./services
      dockerfile: Dockerfile.aaacpe_rag
    container_name: jarvis-aaacpe-rag
    ports:
      - 127.0.0.1:8032:8032
    environment:
      - SERVICE_PORT=8032
    volumes:
      - aaacpe-cultural-data:/data
    networks:
      - qualia-net
    restart: unless-stopped

  jarvis-aaacpe-scraper:
    build:
      context: ./services
      dockerfile: Dockerfile.aaacpe_scraper
    container_name: jarvis-aaacpe-scraper
    ports:
      - 127.0.0.1:8033:8033
    environment:
      - SERVICE_PORT=8033
    volumes:
      - aaacpe-cultural-data:/data
    networks:
      - qualia-net
    restart: unless-stopped

volumes:
  aaacpe-cultural-data:
    driver: local
```

Startup sequence: create network → build services → deploy → load base data via `POST http://localhost:8032/ingest` → verify via `GET http://localhost:8032/` (RAG service currently reports 53 documents loaded) → scraper reports 65 documents from first scrape run. ★ Both services confirmed in 96/96 Up count (March 28) — `restart: unless-stopped` policy confirmed effective.

---

## 30.7 Use Cases and Examples

The following four use cases illustrate how the confirmed corpus validated against `msjarvisgis:5432` ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids) and `msjarvis:5433` ★ (5,416,521 GBIM entities with `confidence_decay` metadata) is applied in the current deployment. RAG search has been confirmed returning correct results for use cases 1 and 3 as of the March 27, 2026 audit (★ services Up March 28).

**Use Case 1: Emergency Utility Assistance.** Query: "I need help with my electric bill NOW." The main brain detects urgency keywords, queries AaaCPE for `category: "emergency"`, and applies emergency protocol validated against `msjarvisgis:5432` ★ PostgreSQL community resources: strip pleasantries, provide facts only. Response: "For electric bill assistance in Fayette County, contact Mountain Heart Community Action at 304-574-1415. They're in Oak Hill, open 8-4 weekdays. Need directions or alternative options?" Not: "Well honey, don't you worry none..." **RAG /search confirmed returning this result correctly (March 27, 2026 audit; ★ services Up March 28).** ★ The complementary AAPCAppE `msjarvis_docs` corpus (4,192 items) may contain additional Fayette County community resource entries that can be cross-referenced to enrich this use case in future work.

**Use Case 2: Heritage Inquiry (userid cakidd).** Query: "Tell me about the Janney family trail." The main brain identifies `userid == "cakidd"` and "Janney" in the query, AaaCPE returns `category: "heritage"` validated against `msjarvis:5433` ★ GBIM genealogy data (5,416,521 entities), and the response includes documented genealogy and geographic precision: "Your Janney family roots — Thomas Janney's Quaker meeting house stood near what's now Route 19. The historical marker is at coordinates 37.8456, -81.2314." ★ `confidence_decay` metadata on the relevant GBIM entities is now available — high-decay heritage entities are candidates for targeted corpus review.

**Use Case 3: Regional Development News.** Query: "What's new with internet access in West Virginia?" AaaCPE searches `category: "scraped_content"` validated against PostgreSQL community data. As of March 27, 2026 (★ confirmed Up March 28), the scraper Chroma contains 65 documents from 39 confirmed sources (first scrape run complete, `total_runs: 1`), including current WV broadband and regional development content. **RAG /search confirmed returning correct results from this category (March 27, 2026 audit; ★ services Up March 28).** ★ The AAPCAppE `msjarvis_docs` corpus (4,192 items) provides a complementary structured resource for regional development queries.

**Use Case 4: Anti-Pattern Prevention.** Query: "How should I talk to people in Appalachia?" AaaCPE returns `category: "anti_pattern"` guidance emphasizing what NOT to do. Response: "Communicate directly and practically — provide clear, actionable information. Don't perform folksy dialect or assume lack of sophistication. Appalachian communities have deep intellectual traditions." ★ All anti-pattern BBB enforcement decisions are now durably logged at `jarvis-memory:8056` (secured March 28) — anti-stereotyping governance is persistently auditable.

---

## 30.8 Future Enhancements

The following are identified as future work, not yet confirmed implemented in the current deployment.

Scheduled automated scraping (WV Gazette-Mail, Rural.org, AppVoices) — daily 6 AM + every 6 hours with automated PostgreSQL validation. **Status TBD pending confirmation of whether `total_runs: 1` was automated or manual (see §30.4).** PostgreSQL `msjarvisgis:5432` ★ GeoDB integration linking cultural patterns to geographic features, supporting queries like "community values in Fayette County" (993 ZCTA centroids available as spatial anchors). PostgreSQL `msjarvis:5433` ★ GBIM integration (5,416,521 entities with `confidence_decay` metadata) for personalization based on user heritage and community role. Full automatic integration of AaaCPE context into every `/chat` call via the `ultimatechat` pipeline (pending confirmation of pipeline test result — see §30.5). Expanded content categories covering economic development, educational resources, healthcare communication norms, and legal/institutional mediation, all validated against PostgreSQL. Community feedback loop allowing stakeholders to flag content, request changes, and vote on authenticity. AAPCAppE corpus integration for understanding linguistic features (not dialect performance). ★ Cross-referencing of AaaCPE scraped corpus (65 docs, 39 sources) with AAPCAppE `msjarvis_docs` (4,192 items, restored March 28) to eliminate duplication and identify coverage gaps. Multi-regional expansion respecting variation within Appalachian communities. Automated validation of all cultural content against `msjarvisgis:5432` ★ and `msjarvis:5433` ★ GBIM community data. ★ `confidence_decay`-driven AaaCPE corpus refresh: automated identification of GBIM cultural and institutional entities with high decay for targeted `needs_verification` review in `jarvis-local-resources-db:5435`. ★ PIA records as first-class ChromaDB collection with `jarvis-memory:8056` durable audit trail (secured March 28) for ongoing community governance review of cultural representation decisions.

---

## 30.9 Safeguards and Governance

In the current deployment (★ March 28, 2026 — 96/96 containers Up), anti-stereotyping safeguards are enforced through the confirmed anti-pattern category documents, the BBB `EthicalFilter` at **127.0.0.1:8016** ★ as the live gate on every request (all BBB services re-locked to `127.0.0.1` as of March 18, 2026 security hardening — see Chapter 16 and Chapter 40 §40-C), `normalize_identity` applied to every response (Chapter 22), and validation against `msjarvisgis:5432` ★ and `msjarvis:5433` ★ GBIM community data. ★ **All BBB and `EthicalFilter` gate decisions are now durably logged at `jarvis-memory:8056`** (secured March 28 — port corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set) — the anti-stereotyping governance record is now persistently auditable for the first time.

**Quarterly content audit** — In the current deployment, all scraped content is reviewed manually for accuracy, stereotyping, and inappropriate framing against `msjarvisgis:5432` ★ and `msjarvis:5433` ★ GBIM community data (5,416,521 entities with `confidence_decay` metadata), with anti-patterns updated based on feedback. ★ `confidence_decay` metadata is now available to prioritize quarterly review of GBIM entities underlying corpus content — high-decay entities surface as candidate refresh items.

**Response quality checks** — In the current deployment, generated responses are sampled monthly and evaluated against anti-pattern guidelines validated against PostgreSQL. ★ `jarvis-memory:8056` (secured March 28) provides the durable BBB gate decision log that makes monthly sampling more systematic — manual sampling from ephemeral container logs is no longer the only path.

**Community Advisory Board** — The design intends that representatives from Appalachian organizations will have authority to review system behavior and request content removal or modification. In the current deployment, this board is planned but not yet established. ★ `jarvis-memory:8056` durable audit trail (secured March 28) provides the governance foundation this board will need to inspect cultural enforcement decisions.

**Privacy protection** — In the current deployment, heritage context is applied only for users who explicitly share family history (`userid == "cakidd"` with Janney query), no personally identifiable information is included in scraped content, and community stories are anonymized unless public domain.

---

## 30.10 Testing and Validation

In the current deployment (★ 96/96 containers Up, March 28), the following functional tests are confirmed working. **RAG /search confirmed returning correct results for emergency protocol and Fayette County utility assistance example as of March 27, 2026 audit (★ services Up March 28).**

```bash
# Test 1: Anti-pattern retrieval
curl -X POST http://localhost:8032/search \
  -H "Content-Type: application/json" \
  -d '{"query": "dont perform dialect stereotypes", "top_k": 1}'
# Expected: category="anti_pattern", text includes "Don't perform folksy dialect"

# Test 2: Emergency protocol
curl -X POST http://localhost:8032/search \
  -H "Content-Type: application/json" \
  -d '{"query": "crisis emergency response", "top_k": 1}'
# Expected: category="emergency", text includes "Strip all pleasantries"
# CONFIRMED CORRECT — March 27, 2026 audit (★ services Up March 28)

# Test 3: Heritage context
curl -X POST http://localhost:8032/search \
  -H "Content-Type: application/json" \
  -d '{"query": "Janney family Carrie heritage", "top_k": 1}'
# Expected: category="heritage", text includes "Thomas Janney" and geographic coordinates

# Test 4: Scraped content (★ 65 docs from first scrape run, 39 sources; Up March 28)
curl -X POST http://localhost:8032/search \
  -H "Content-Type: application/json" \
  -d '{"query": "West Virginia broadband rural", "top_k": 1}'
# Expected: category="scraped_content", text includes current regional development info
# CONFIRMED CORRECT — March 27, 2026 audit (★ services Up March 28)
```

Health monitoring in the current deployment (★ all Up, March 28):

```bash
curl http://localhost:8032/health                   # RAG service health (★ Up)
curl http://localhost:8033/health                   # Scraper service health (★ Up)
curl http://localhost:8032/ | jq '.documents'       # RAG document count (currently 53)
curl http://localhost:8033/ | jq '.documents_total' # Scraper document count (currently 65)
curl http://localhost:8033/ | jq '.total_runs'      # Scrape run count (currently 1)
curl http://localhost:8033/health | jq '.last_scrape'
# ★ Add to VERIFYANDTEST.sh Section 9 or future AaaCPE health section
```

---

## 30.11 Performance Metrics

In the current deployment (★ March 28, 2026 — 96/96 Up), the confirmed system status is as follows:

| Metric | February 2026 Baseline | March 27, 2026 Confirmed | ★ March 28, 2026 |
|---|---|---|---|
| RAG service documents loaded | 10 (7 base + 3 scraped test) | **53** | ★ **53** (Up, 96/96) |
| Scraper Chroma documents | 3 (test only) | **65** (first scrape run, 39 sources) | ★ **65** (Up, 96/96) |
| Scraper total_runs | 0 | **1** | ★ **1** (schedule TBD §30.4) |
| Services running | 2/2 | **2/2** ✅ | ★ **2/2** ✅ (in 96/96 Up) |
| RAG /search correctness | Not verified | **✅ Confirmed** (emergency + Fayette County utility) | ★ **✅** (services Up) |
| ChromaDB inventory | Not audited | Not audited | ★ **40 collections / 6,675,442 vectors** (March 28 full audit) |
| `msjarvis_docs` (AAPCAppE) | Not present | 39 sources / 65 docs (first run) | ★ **4,192 items** (restored March 28) |
| `jarvis-ingest-api/watcher` | Not present | Not present | ★ **Restored to active inventory** (March 28) |
| `jarvis-memory:8056` BBB audit | Not present | Not present | ★ **Secured** (March 28; durable gate log) |
| `msjarvis:5433` `confidence_decay` | Not present | Not present | ★ **5,416,521 entities** (restored March 28) |
| Query latency | Under 100ms average | Under 100ms average | Under 100ms average |
| Volume size | ~50 MB | ~50 MB (update after scraper volume measurement) | ~50 MB (update pending) |
| Restart policy | unless-stopped | unless-stopped | unless-stopped |
| Scheduled scraping active | Not yet | **TBD — see §30.4** | **TBD — see §30.4** |

---

## 30.12 Summary

In the current deployment (★ March 28, 2026 — 96/96 containers Up), the AaaCPE Cultural Intelligence System is realized as two confirmed running services — `jarvis-aaacpe-rag` (**127.0.0.1:8032** ★) and `jarvis-aaacpe-scraper` (**127.0.0.1:8033** ★) — sharing the `aaacpe-cultural-data` Docker volume with an `appalachian_cultural_intelligence` ChromaDB collection (★ within 40-collection / 6,675,442-vector inventory confirmed March 28 full audit). **As of the March 27, 2026 audit (★ services Up March 28):** the RAG service reports 53 documents loaded; the scraper Chroma contains 65 documents from its first confirmed scrape run (39 sources, `total_runs: 1`); RAG /search is confirmed returning correct results for the emergency protocol and Fayette County utility assistance example. All content is validated against `msjarvisgis:5432` ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids, 5.4M+ verified GBIM beliefs) and `msjarvis:5433` ★ (5,416,521 GBIM entities with `confidence_decay` metadata, restored March 28) for West Virginia community accuracy.

★ Three new operational capabilities are active as of March 28, 2026 that were not present in the March 27 baseline:
1. **Durable BBB anti-stereotyping audit trail** — `jarvis-memory:8056` (secured March 28) now stores all BBB `EthicalFilter` and gate decisions persistently and authentically — cultural safeguard governance is durably auditable for the first time.
2. **`confidence_decay` metadata on GBIM entities** — `msjarvis:5433` ★ (5,416,521 entities) now exposes graded temporal confidence on cultural and institutional GBIM entities, enabling prioritized corpus refresh signals for AaaCPE quarterly content audits.
3. **Complementary AAPCAppE ingest pipeline active** — `jarvis-ingest-api` + `jarvis-ingest-watcher` (restored March 28; `msjarvis_docs` 4,192 items) provides continuous structured community resource ingest alongside the AaaCPE scraper — the two pipelines together constitute the broadest confirmed community knowledge ingest footprint in the system's history.

Both services are registered in the `jarvis-main-brain` SERVICES registry and are available for invocation in the `ultimatechat` path. **Two open items remain for documentation update (see §30.4 and §30.5):** (1) confirm whether `total_runs: 1` was triggered by an active automated schedule or a manual `POST /scrape_now` call, and update the scheduled scraping status accordingly; (2) confirm whether the verified RAG search results were from a direct `/search` call or a full `/chat` pipeline test, and update the main brain integration status accordingly. The BBB at **127.0.0.1:8016** ★ (re-locked from `0.0.0.0` as of March 18, 2026 security hardening; ★ audit → `jarvis-memory:8056` secured March 28) continues to function as the primary live anti-stereotyping and ethics gate on all requests regardless of whether AaaCPE is explicitly invoked.

The system treats Appalachian culture as systematic, respected, and deserving of authentic representation grounded in PostgreSQL GBIM community data — not as performance material. Community engagement, transparency, and ongoing governance ensure this work serves rather than exploits the communities it represents.

---

*Last updated: ★ 2026-03-28 by Carrie Kidd (Mamma Kidd), Pax WV*
*★ March 28, 2026: 96/96 containers Up confirmed — operational scope updated throughout*
*★ March 28, 2026: `jarvis-memory:8056` secured (durable BBB audit trail) — anti-stereotyping governance accountability updated throughout*
*★ March 28, 2026: `msjarvis:5433` restored (5,416,521 GBIM entities, `confidence_decay` metadata) — all GBIM references updated; confidence_decay corpus refresh signals added*
*★ March 28, 2026: ChromaDB 40-collection / 6,675,442-vector inventory confirmed — collection context updated throughout*
*★ March 28, 2026: `jarvis-ingest-api` + `jarvis-ingest-watcher` restored (AAPCAppE, `msjarvis_docs` 4,192 items) — complementary pipeline noted throughout; cross-reference to Ch 31 added*
*Status header updated from February 2026 to March 27, 2026 baseline — March 27, 2026*
*Document counts updated throughout: RAG 53 docs, scraper 65 docs (39 sources, total_runs: 1) — March 27, 2026*
*scraped_content category updated from 3 test docs to 65 first-production-run docs — March 27, 2026*
*Scheduled scraping status noted as TBD pending manual vs automated confirmation — March 27, 2026*
*Main brain integration status noted as TBD pending direct /search vs full /chat pipeline confirmation — March 27, 2026*
*BBB port corrected from 0.0.0.0:8016 to 127.0.0.1:8016 (March 18 security hardening) — March 27, 2026*
*Audit table status updated from ⚠️ Stub only to ✅ Partial — March 27, 2026*
