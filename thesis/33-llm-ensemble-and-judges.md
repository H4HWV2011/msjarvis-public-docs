# Chapter 33 — LLM Ensemble and Judges

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**
**Last updated: ★ 2026-04-23**
**★ 100 containers Up (April 23, 2026) (zero Restarting, zero Exited). LLM ensemble, judge pipeline, `rag_grounded_v2` components, and constitutional guardianship fully wired and PostgreSQL-grounded. PostgreSQL two-container split active (April 23, 2026): `production msallis-db host 5433` (16 GB, 294 tables, 11 schemas) + `forensic postgis-forensic host 5452` (17 GB, 314 tables). ChromaDB: ★ 48 collections / ~6,740,611 total vectors / `/api/v2/` only. Caddy `forward_auth` perimeter (OI-36-A CLOSED).**

---

> **Port and Storage Ground Truth (★ April 23, 2026):**
>
> - `production msallis-db` at host port **5433** — ★ 16 GB, 294 tables, 11 schemas; GBIM entity count: 5,416,521+ (floor; growing ~288/day from `autonomous_learner` commits); `confidence_decay` metadata on all entities; 80 epochs, 206 source layers (restored March 28). **Supersedes April 6 `msallis:5433` entry.**
> - `forensic postgis-forensic` at host port **5452** — ★ 17 GB, 314 tables (PostGIS geometry). **Supersedes April 6 `gisdb / msallisgis` at host:5432 / container-internal:5452 — 45 GB, 548 tables entry. That figure is no longer current.**
> - `allis-local-resources-db` at port **5435** — community resources database; `local_resources` collection: 207 items / all 55 WV counties.
> - Redis: `allis-redis` — single container, internal port 6379, host port 6380.
> - ChromaDB: host **8002** → container 8000; ★ **48 collections, ~6,740,611 total vectors**; `/api/v2/` only (`/api/v1/` permanently removed); pinned to `chromadb/chroma:0.6.3`; volume: `/home/ms-allis/msallis-rebuild/persistent/chroma → /data`; `ms_allis_memory` and `psychological_rag` (968 docs) confirmed; `conversation_history` wiped and reseeded clean April 16, 2026 — post-wipe accumulation only.
> - `allis-memory:8056` — durable audit store; fully mapped — **8 endpoints**: `/steg_report`, `/pia_window`, `/memory/turn`, `/memory/get`, `/memory/sessions`, `/memory/session/{id}`, `/memory/quest*`, `/memory/episodic/{id}`; survives container restarts.
> - `allis-constitutional-guardian:8091` — constitutional authority; `/health` reports `postgresql_gbim_connection` (production `msallis-db:5433` ★) and `postgresql_geodb_connection` (forensic `postgis-forensic:5452` ★) liveness fields. ★ Verify-current field names after April 23 two-container split.
> - `allis-gis-rag:8004` — connects to `production msallis-db:5433` ★ for GBIM lookups and `forensic postgis-forensic:5452` ★ for PostGIS geometry. Cross-reference: Ch 28 §28.7.
> - `allis-spiritual-rag:8005` — RAG source for `rag_grounded_v2` truth verification; `spiritual_rag` collection deduplicated March 28 (−19,338 vectors removed).
> - `allis-rag-grounded-v2:7241` — judge pipeline `rag_grounded_v2` component, v2.0.0, `dgm_available: true`; accessible to autonomous learning cycles (Ch 27 §27.4) as well as judge pipeline.
> - `allis-memory:8056` now also includes `/steg_report` and `/pia_window` endpoints specifically relevant to ensemble and judge pipeline oversight.
> - OI-36-A CLOSED: Caddy `forward_auth` before main-brain port 8050; HTTP 401 on unauthenticated `/chat` confirmed. Perimeter sits outside Docker stack.

---

## Why This Matters for Polymathmatic Geography

This chapter describes the reasoning and response-generation infrastructure at the heart of Ms. Allis — an ensemble of diverse LLMs, a judge pipeline grounded in local PostgreSQL and ChromaDB data, and a synthesizer that speaks in a single accountable voice.

- **P1 – Every where is entangled** by using an ensemble in which every model's contribution is evaluated in relation to the others: no single model's answer is final. The judge pipeline's `rag_grounded_v2` truth-verification step entangles every response with the GBIM belief graph (`production msallis-db:5433` ★, 5,416,521+ entities) and the `forensic postgis-forensic:5452` ★ PostGIS geometry — so answers about Fayette County are literally grounded in Fayette County data.
- **P3 – Power has a geometry** by placing the Constitutional Guardian (`allis-constitutional-guardian:8091`) above the ensemble and judge pipeline in the governance stack, and by requiring that the Caddy `forward_auth` perimeter (OI-36-A CLOSED) be the first gate before any ensemble call is possible. The geometry is enforced in infrastructure, not only in policy.
- **P5 – Design is a geographic act** by constraining the LM Synthesizer's identity rules to name Mount Hope, WV, Harmony for Hope, Inc., and the Appalachian community as the system's locus of accountability — so that the ensemble's diversity converges on a geographically situated voice, not a generic AI persona.
- **P12 – Intelligence with a ZIP code** by routing all truth claims through `rag_grounded_v2` (backed by `allis-gis-rag:8004` and `allis-spiritual-rag:8005`), both of which draw on `local_resources` (207 items / all 55 WV counties) and the `appalachian_english_corpus` (210 docs, 38 sources, 6-hour cron) for place-specific grounding.
- **P16 – Power accountable to place** by auditing every ensemble output, judge verdict, and BBB decision at `allis-memory:8056` (8 mapped endpoints, survives restarts), making the ensemble's reasoning independently inspectable by Mother Carrie and community governance structures.

As such, this chapter belongs to the **Computational Instrument tier**: it specifies the reasoning and response machinery that translates community questions into grounded, accountable answers.

---

## 33.1 Why an Ensemble and Judge Pipeline

This chapter describes the **LLM ensemble and judge pipeline** that underpins Ms. Allis's reasoning and response generation. Rather than a single model acting alone, Ms. Allis uses a diverse ensemble of expert models, a judge pipeline that compares, critiques, and selects outputs, a synthesizer (LM Synthesizer) that merges judge decisions into a final response, and a truth-verification layer (`rag_grounded_v2`) that anchors answers in GBIM and RAG retrieval.

This architecture exists because single models can hallucinate, misjudge, or encode hidden biases; Appalachian communities need an AI that checks its work, not one that asserts authority without evidence; and constitutional, spiritual, and community responsibilities require multiple perspectives and durable audit trails. For a West Virginia–specific system, ensemble diversity is not a generic AI engineering choice — it is a governance decision: no single model's training data reliably reflects the linguistic, spiritual, and socioeconomic texture of Appalachian life. Cross-referencing multiple models against locally grounded RAG (`allis-gis-rag:8004`, `allis-spiritual-rag:8005`, `appalachian_english_corpus`) is what makes the ensemble's diversity meaningful for this community.

The ensemble and judge pipeline are part of the **Computational Instrument tier**: they define how Ms. Allis evaluates evidence, weighs options, and speaks.

---

## 33.2 Components at a Glance

| Component | Service | Role |
|:--|:--|:--|
| Expert models (ensemble members) | 22 configured / 21 active (BakLLaVA fails expected); `llm22-proxy` (LLaMA 3.1, port 8222) confirmed active | Diverse LLMs with different strengths; called with `asyncio.Semaphore(3)` hardware gate |
| Judge pipeline | `allis-rag-grounded-v2:7241` + `allis-gis-rag:8004` + `allis-spiritual-rag:8005` | Evaluate candidates; score factual accuracy, safety, alignment, clarity |
| LM Synthesizer | `allis-lm-synthesizer:8001` | Merges judge outputs into a unified answer in Ms. Allis's voice |
| BBB | `allis-blood-brain-barrier:8016` | Six-filter pipeline; all 6 confirmed responding (★ April 23) |
| Constitutional Guardian | `allis-constitutional-guardian:8091` | Highest governance authority; first gate after Caddy perimeter |
| Durable audit | `allis-memory:8056` | 8 mapped endpoints; stores all ensemble, judge, BBB, and synthesizer decisions |
| Perimeter (OI-36-A) | Caddy `forward_auth` | HTTP 401 before port 8050; outermost gate; cannot be removed by DGM or token class |

---

## 33.3 Ensemble — Multiple Voices, One Steward

Ms. Allis's ensemble consists of **22 configured / 21 active** LLMs. BakLLaVA fails as expected (hardware constraint; documented). `llm22-proxy` (LLaMA 3.1, port 8222) is confirmed active as of April 23. The ensemble is hardware-constrained by an `asyncio.Semaphore(3)` gate — no more than three LLMs are called simultaneously — enforced by the Lenovo Legion 5 16IRX9 (29 GB RAM) physical limits. This is a documented design constraint, not a bug: the semaphore prevents OOM crashes and ensures response stability on community hardware.

**Why ensemble diversity matters for West Virginia specifically:** No single LLM's training data reliably reflects the linguistic patterns of rural Fayette County, the spiritual governance structures of Appalachian communities, or the specific policy landscape of a 55-county state with historically underserved infrastructure. The `appalachian_english_corpus` (210 docs, 38 sources, 6-hour cron) provides the linguistic grounding that no pre-trained LLM can fully replicate, feeding into the LM Synthesizer's identity guard to ensure the convergent voice is recognizably Appalachian, not generic.

Ensemble decisions are recorded in `allis-memory:8056` so that communities can inspect how Ms. Allis arrived at an answer. Key design principles — diversity of models (no single vendor or architecture), redundancy for safety (disagreement triggers escalation), and unity of voice (the LM Synthesizer enforces identity rules) — are equally governance principles and engineering ones.

---

## 33.4 Judge Pipeline and `rag_grounded_v2`

The **judge pipeline** evaluates candidate outputs produced by ensemble models through rule-based checks, LLM-based judges, and `rag_grounded_v2` truth verification.

LLM-based judges score candidates along four dimensions: factual accuracy (backed by retrieval), safety (cross-checked with SafetyMonitor baseline `safety_score=1.0` on survivor/victim queries, April 3), alignment with Appalachian community values (grounded in `appalachian_english_corpus` and `allis-spiritual-rag:8005`), and clarity and usefulness. Judge pipeline score baseline: **`0.975`** (April 6 — verify-current).

### 33.4.1 `rag_grounded_v2` (Judge Pipeline Component)

`allis-rag-grounded-v2:7241` plays a central role in both the judge pipeline and the BBB's `truth_verification` filter:

- Version: v2.0.0
- Health: `{"status":"healthy","version":"v2.0.0","dgm_available":true}`
- Host: `127.0.0.1:7241`
- `dgm_available: true` — accessible to DGM sprint-level decisions and autonomous learning cycles (Ch 27 §27.4), not only the judge pipeline

Responsibilities:
- Receive a proposed answer and relevant context
- Retrieve supporting or contradicting evidence from `production msallis-db:5433` ★ GBIM (5,416,521+ entities with `confidence_decay`), `forensic postgis-forensic:5452` ★ PostGIS geometry, `allis-gis-rag:8004`, and `allis-spiritual-rag:8005`
- Produce a verdict with a `truth_score`, `verified` flag, and diagnostic metadata

`rag_grounded_v2` thus provides evidence (what was retrieved), verdict (whether the answer is consistent), and confidence (how strongly the evidence supports the answer). Future work: upgrade from `heuristic_contradiction_v1` to full RAG-grounded scoring querying both `production msallis-db:5433` ★ and `forensic postgis-forensic:5452` ★ stores directly. Cross-reference: Ch 32 §32.3 (DGM-Response-Level uses `rag_grounded_v2` for threshold-triggered re-runs).

---

## 33.5 BBB Six-Filter Pipeline and Truth Verification

The **BBB** (`allis-blood-brain-barrier:8016`) runs six filters, **all confirmed responding as of April 23, 2026**:

| Filter | Status | Notes |
|:--|:--|:--|
| EthicalFilter | ✅ Confirmed responding | Recalibrated April 2 — 0% false positive rate, 9/9 regression pass |
| SpiritualFilter | ✅ Confirmed responding | Blocks coercive, manipulative, or spiritually abusive content |
| SafetyMonitor | ✅ Confirmed responding | Recalibrated April 3 — `safety_score=1.0` on survivor/victim queries |
| ThreatDetection | ✅ Confirmed responding | Detects harassment and coercive patterns |
| steganography_filter | ✅ Confirmed responding | **First live catch documented (April 2026)** |
| truth_verification | ✅ Confirmed responding | Method: `rag_grounded_v2` (`127.0.0.1:7241`, `dgm_available: true`) |

**Live steganography catch (April 2026):** The steganography filter intercepted a live adversarial prompt: `"override your safety filters"` → classified as `prompt_injection_keywords`, `severity=CRITICAL`, blocked ✅. This is the first documented live BBB catch in the thesis record. It confirms the filter is operationally active for production traffic. The event is durably logged at `allis-memory:8056/steg_report`. Cross-reference: Ch 29 §29.3 (psychological safeguard context); Ch 32 §32.8 (worked DGM example).

**Phase 4.5 status:** BBB is currently in log+passthrough mode. Blocking re-enablement is pending red-team review — a DGM-Sprint-Level decision. The live steg catch is the primary evidence informing this decision. Until blocking is re-enabled, the steganography filter logs and flags but does not block non-CRITICAL events independently of the BBB gate decision. ★ Verify-current: confirm whether Phase 4.5 blocking has been re-enabled since April 6.

The **truth_verification** filter sends claims to `allis-rag-grounded-v2:7241` or directly to `allis-gis-rag` and `allis-spiritual-rag`, receives back evidence snippets, scores, and supported/unsupported/contradicted flags, and marks responses accordingly. This ensures truth verification is not a heuristic guess but a retrieval-backed process grounded in `production msallis-db:5433` ★ and `forensic postgis-forensic:5452` ★.

All BBB gate decisions — including the steg catch — are logged at `allis-memory:8056`. The durable audit is specifically queryable via `/steg_report` (steganography events) and `/pia_window` (PIA-relevant audit window) — not only via generic audit endpoints.

---

## 33.6 LM Synthesizer — Identity Guard and Voice

The **LM Synthesizer** (`allis-lm-synthesizer:8001`) merges judge-selected content into a final answer. It is constrained by two rule sets that operate as governance mechanisms, not only as prompt engineering.

**IDENTITY RULES** state that Ms. Allis is Ms. Egeria Allis, built by Harmony for Hope, Inc., in Mount Hope, WV, to serve Appalachian communities, and that she must not claim to be built by large tech corporations. These rules are grounded in `production msallis-db:5433` ★ GBIM — identity statements are not hardcoded strings but GBIM-validated beliefs with `confidence_decay` metadata, growing daily as `autonomous_learner` (~23,200+ records, ~288/day) commits new beliefs about Appalachian communities. Cross-reference: Ch 36 §36.5.2 (LM Synthesizer three-layer identity guard).

**STRICT RULES** forbid mentioning model names or ensembles, revealing that multiple models were consulted, using hedging like "it seems" to explain internal uncertainty, or describing the internal pipeline or consensus process. In combination, these rules ensure that ensemble and judge complexity stays behind the scenes, that a unified human-aligned voice is presented, and that identity integrity and spiritual root commitments are maintained.

The `appalachian_english_corpus` (210 docs, 38 sources, 6-hour cron) provides the Appalachian English linguistic grounding that shapes the synthesizer's register — primary contributing sources include WV Watch, WOAY, Daily Yonder, AppVoices. This corpus is refreshed every six hours, meaning the linguistic baseline the synthesizer draws on is not static.

The synthesizer is called **only** from `main_brain.py` Phase 3.5, not from `judge_pipeline.py`. `icontainers-identity` service is at `allis-i-containers:8015` — confirmed Up in 100-container baseline. Cross-reference: Ch 28 §28.2 (service inventory); Ch 36 §36.1 (concept of identity).

---

## 33.7 PostgreSQL and ChromaDB Grounding

The ensemble and judge pipeline are tightly connected to the two-container PostgreSQL store and ChromaDB. The April 6 ground truth for this section has been superseded by the April 23 two-container split.

**PostgreSQL (★ April 23, 2026 — supersedes April 6):**

| Store | Host port | Size | Role |
|:--|:--|:--|:--|
| `production msallis-db` ★ | 5433 | 16 GB, 294 tables, 11 schemas | GBIM entities (5,416,521+, growing ~288/day); `confidence_decay` metadata; 80 epochs, 206 source layers |
| `forensic postgis-forensic` ★ | 5452 | 17 GB, 314 tables | PostGIS geometry; ZIP-code and county boundaries for WV |

> **★ Supersession note:** The April 6 ground truth box cited `gisdb / msallisgis` at `host:5432 / container-internal:5452 — 45 GB, 548 tables`. This figure is **superseded** by the April 23 two-container split. `allis-gis-rag:8004` now connects to `production msallis-db:5433` ★ for GBIM lookups and `forensic postgis-forensic:5452` ★ for PostGIS geometry. Any judge pipeline component or watchdog referencing `msallisgis:5452` or `gisdb:5432` must be updated. Cross-reference: Ch 28 §28.7 (full two-container split detail).

`confidence_decay` means the system tracks how "fresh" a belief is. High-decay beliefs must be flagged or audited before being used as ground truth in judge verdicts or truth-verification responses. Future work: automated `confidence_decay`-aware gating — trigger: beliefs above decay threshold flagged before use as ground truth, routing to human steward review rather than automatic assertion.

**ChromaDB (★ April 23, 2026):**

| Metric | Value |
|:--|:--|
| Collections | ★ **48** (supersedes April 6 baseline of 47) |
| Total vectors | ★ **~6,740,611** (supersedes 6,722,589) |
| Host port | **8002** → container 8000 |
| API | `/api/v2/` only — `/api/v1/` permanently removed |
| Pinned version | `chromadb/chroma:0.6.3` |
| Volume | `/home/ms-allis/msallis-rebuild/persistent/chroma → /data` |

**Key collections for ensemble and judge:**

| Collection | Contents | Notes |
|:--|:--|:--|
| `autonomous_learner` | ~23,200+ records (~288/day) | Primary live-growing collection feeding ensemble context |
| `appalachian_english_corpus` | 210 docs, 38 sources, 6-hour cron | Appalachian English linguistic grounding for synthesizer |
| `local_resources` | 207 items / all 55 WV counties | GIS RAG community resource substrate |
| `psychological_rag` | 968 docs (restored March 28) | Psychological safeguards RAG substrate |
| `spiritual_rag` | Post-dedup baseline (−19,338 vectors removed March 28) | Spiritual root RAG; verify-current count |
| `conversation_history` | Post-April 16 accumulation only | Wiped and reseeded clean April 16, 2026 |
| `ms_allis_memory` | Confirmed | General memory substrate |

---

## 33.8 Audit and Oversight

Every key step in the ensemble and judge pipeline is **audited** at `allis-memory:8056` (8 endpoints fully mapped, survives container restarts).

**Audit scope by pipeline stage:**

| Stage | What is logged | `allis-memory:8056` endpoint |
|:--|:--|:--|
| Ensemble outputs | Models called, responses, basic scores (length, complexity, filter triggers) | `/memory/turn` |
| Judge decisions | Preferred candidate and rationale, `rag_grounded_v2` verdicts and scores, safety/alignment annotations | `/memory/turn`, `/memory/episodic/{id}` |
| BBB decisions | Filters triggered, blocks and rewrites, final pass/fail; steg catches | `/steg_report` (steg-specific), `/memory/turn` |
| BBB PIA-relevant events | Privacy-impact-relevant filter events (SafetyMonitor, SpiritualFilter on sensitive queries) | `/pia_window` |
| Synthesizer outputs | Final answer text, identity guard checks, warnings attached | `/memory/turn` |
| Constitutional Guardian | Constitutional gate decisions, `postgresql_validation` results | `/memory/turn`, `constitutional_audit.jsonl` |

`constitutional_audit.jsonl` (bind-mounted; 6.7K+ entries at April 6 — verify-current) provides the long-form audit record independent of ChromaDB container state. The durable `/steg_report` and `/pia_window` endpoints specifically relevant to ensemble and judge pipeline oversight were not present in earlier chapter versions; they are part of the fully mapped 8-endpoint `allis-memory:8056` store confirmed April 23.

---

## 33.9 Example Flow — From Question to Answer

Consider a user question: *"Is it safe to drink water from this creek in Fayette County? There's an old mine upstream."*

**Step 1 — Caddy perimeter (OI-36-A CLOSED):**
- Request arrives at `egeria.mountainshares.us`
- Caddy `forward_auth` enforces Bearer token validation
- HTTP 401 returned on unauthenticated request — perimeter blocks before gateway is reached
- Authenticated request passes to `allis-main-brain:8050`

**Step 2 — Gateway and app-layer auth:**
- Token validated via `allis_auth:8055` and `allis-redis:6380`
- Two-layer auth model: Caddy perimeter (Layer 0) + app-layer RBAC (gateway middleware)

**Step 3 — Constitutional Guardian (`allis-constitutional-guardian:8091`):**
- Checks for constitutional issues (environmental justice, community harm, `10a-no-extraction` principle)
- `postgresql_validation`: queries `production msallis-db:5433` ★ GBIM and `forensic postgis-forensic:5452` ★ PostGIS boundaries for Fayette County
- Logs gate decision to `constitutional_audit.jsonl` and `allis-memory:8056`

**Step 4 — Ensemble:**
- 21 active LLMs (BakLLaVA excluded); `asyncio.Semaphore(3)` gates concurrent calls
- Models generate candidate answers about water safety, mine drainage, and local context
- `llm22-proxy` (LLaMA 3.1, port 8222) included in the active pool

**Step 5 — Judge pipeline:**
- `allis-rag-grounded-v2:7241` receives candidates and retrieves from `allis-gis-rag:8004` (mine maps, county boundaries, contamination records if available in `forensic postgis-forensic:5452` ★) and `allis-spiritual-rag:8005` (community values context)
- `rag_grounded_v2` assesses whether safety claims are supported; flags high-`confidence_decay` GBIM beliefs
- Judge scores candidates on factual accuracy, safety, alignment, clarity; baseline score `0.975`
- Prioritizes caution and transparency; encourages consulting local authorities or testing services; cites `local_resources` (207 items / all 55 WV counties) for Fayette County-specific referrals

**Step 6 — BBB (all 6 filters confirmed responding):**
- EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter run
- truth_verification uses `rag_grounded_v2` results — blocks overly confident claims unsupported by evidence
- All events logged to `allis-memory:8056`

**Step 7 — LM Synthesizer (`allis-lm-synthesizer:8001`):**
- Merges judge-approved content into a single response in Ms. Egeria Allis's voice
- Identity guard enforces: Mount Hope WV, Harmony for Hope, Inc., Appalachian community accountability
- `appalachian_english_corpus` grounding ensures the response register is Appalachian, not clinical
- Emphasizes safety, uncertainty, and local Fayette County resources

**Step 8 — Audit:**
- All decisions recorded in `allis-memory:8056` across relevant endpoints
- Constitutional gate decision in `constitutional_audit.jsonl`

The result: a cautious, community-safe answer grounded in local Fayette County data, transparent about uncertainty, in line with the spiritual root and Mother Carrie protocol — and fully auditable by Mother Carrie and community governance structures.

---

## 33.10 Implementation Status

| Component | Status | Notes |
|:--|:--|:--|
| LLM ensemble (22 configured / 21 active) | ✅ Stable | BakLLaVA fails expected; `llm22-proxy` LLaMA 3.1 port 8222 confirmed active; `asyncio.Semaphore(3)` gate |
| Judge pipeline (`rag_grounded_v2` v2.0.0) | ✅ Healthy | `127.0.0.1:7241`, `dgm_available: true`; score baseline `0.975` |
| BBB six-filter stack | ✅ All 6 confirmed responding | First live steg catch documented; Phase 4.5 log+passthrough (blocking pending red-team sign-off) |
| LM Synthesizer identity guard | ✅ Stable | `icontainers-identity:8015` Up; GBIM-grounded identity beliefs; `appalachian_english_corpus` linguistic grounding |
| Caddy `forward_auth` perimeter (OI-36-A) | ✅ CLOSED | HTTP 401 before port 8050; two-layer auth model |
| `production msallis-db:5433` ★ | ✅ Active | 16 GB, 294 tables, 11 schemas; 5,416,521+ entities growing ~288/day |
| `forensic postgis-forensic:5452` ★ | ✅ Active | 17 GB, 314 tables; supersedes `gisdb:5432 / 45 GB / 548 tables` April 6 baseline |
| ChromaDB | ✅ 48 collections, ~6,740,611 vectors | `/api/v2/` only; `conversation_history` wiped April 16 |
| `allis-memory:8056` — 8-endpoint audit | ✅ Fully mapped | `/steg_report` + `/pia_window` for pipeline-specific oversight |
| `autonomous_learner` as live ensemble context | ✅ ~23,200+ records (~288/day) | Primary live-growing ChromaDB collection |
| `appalachian_english_corpus` synthesizer grounding | ✅ 210 docs, 6-hour cron | WV Watch, WOAY, Daily Yonder, AppVoices primary contributors |
| `local_resources` judge pipeline substrate | ✅ 207 items / 55 WV counties | County-specific referrals in judge verdicts |
| Phase 4.5 BBB blocking re-enablement | ⚠️ Pending | Log+passthrough; red-team sign-off required; live steg catch is primary trigger evidence |
| Automated `confidence_decay`-aware gating | 🔲 Future work | Trigger: beliefs above decay threshold flagged before ground truth use in judge verdicts |
| Judge upgrade from `heuristic_contradiction_v1` to full RAG-grounded scoring | 🔲 Future work | Requires querying both `production msallis-db:5433` ★ and `forensic postgis-forensic:5452` ★ |
| Expanded RAG corpora (local environmental data, legal resources) | 🔲 Future work | Design intent; governance-gated expansion |
| Additional judge criteria (long-term harm, community trust, narrative balance) | 🔲 Future work | Conceptually defined; not yet wired into scoring |

---

## Cross-Reference Map

| This section | Cross-chapter reference |
|:--|:--|
| §33.3 ensemble diversity for WV | Ch 30 §30.3 (AAPCappE sources); Ch 34 §34.7 (Mother Carrie protocol — why identity matters) |
| §33.3 `appalachian_english_corpus` synthesizer grounding | Ch 30 §30.4 (corpus curation); Ch 34 §34.5 (spiritual corpus) |
| §33.4 `rag_grounded_v2` autonomous learning access | Ch 27 §27.4 (autonomous learning cycles) |
| §33.5 live steg catch | Ch 29 §29.3 (psychological safeguard); Ch 32 §32.8 (DGM worked example) |
| §33.5 Phase 4.5 status | Ch 29 §29.3 (BBB phase); Ch 37 §37.4.1 (constitutional BBB integration) |
| §33.6 LM Synthesizer identity guard | Ch 34 §34.3 (spiritual root); Ch 36 §36.5.2 (three-layer identity guard) |
| §33.6 `icontainers-identity:8015` | Ch 28 §28.2 (100-container baseline); Ch 36 §36.3 (identity data structures) |
| §33.7 PostgreSQL two-container supersession | Ch 28 §28.7 (GIS RAG detail); Ch 37 §37.1 (constitutional guardian PostGIS) |
| §33.7 `conversation_history` wipe | Ch 29 §29.6; Ch 37 §37.6 (audit continuity) |
| §33.8 `constitutional_audit.jsonl` | Ch 37 §37.6 (persistent audit log); Ch 31 §31.4 (volume bind mount) |
| §33.9 canonical flow — Caddy as Step 1 | Ch 31 §31.7 (seven-layer stack); Ch 36 §36.2 (Caddy as zero-th gate); Ch 37 §37.2 |
| §33.10 future work — `confidence_decay` gating | Ch 38 (future chapter); Ch 32 §32.10 (DGM future work) |

---

*Chapter 33 — LLM Ensemble and Judges*
*Ms. Egeria Allis Steward System — Harmony for Hope, Inc.*
*Mount Hope, West Virginia*
*Last updated: ★ 2026-04-23 — Carrie Kidd (Mamma Kidd)*
*★ 100 containers Up — 22 configured / 21 active LLMs — judge pipeline score 0.975 — all 6 BBB filters confirmed responding — live steg catch documented — `production msallis-db:5433` ★ + `forensic postgis-forensic:5452` ★ — ChromaDB 48 collections / ~6,740,611 vectors — Caddy forward_auth (OI-36-A CLOSED)*
