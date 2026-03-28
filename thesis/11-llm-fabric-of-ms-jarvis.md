# 11. The LLM Fabric of Ms. Jarvis

Carrie Kidd (Mamma Kidd) — Mount Hope, WV

## Why This Matters for Polymathmatic Geography

This chapter shows how Ms. Jarvis's "thinking" is implemented as an organized fabric of local language models and services rather than a single opaque model instance. It supports:

- **P1 – Every where is entangled** by embedding LLMs inside a retrieval, entanglement, and spatial stack (ChromaDB port 8000 `chroma_data` volume, PostgreSQL `msjarvis` port 5433 with 5,416,521 verified GBIM beliefs, `gisdb` port 5433 PostGIS, `jarvis-local-resources-db` port 5435, WV-entangled RAG, autonomous learner collections) that keeps reasoning tied to concrete places, institutions, and learning histories.

- **P3 – Power has a geometry** by routing questions through specific models, memories, and services whose connections — ports, proxies, ensembles, judges, and DGMs — have explicit topologies that can be inspected, tuned, or redesigned.

- **P5 – Design is a geographic act** by treating model choice, ensemble wiring, timeout and backlog settings, and service topology as design decisions that change how Appalachian realities are seen, narrated, and optimized over time.

- **P12 – Intelligence with a ZIP code** by grounding LLM calls in West Virginia-specific semantic and geospatial memory from PostgreSQL `msjarvis` (port 5433, 5,416,521 GBIM entities, 80 epochs, 206 source layers), including GBIM-derived ChromaDB collections, WV-entangled search, autonomous learner outputs, and I-container identity, rather than generic, placeless prompts.

- **P16 – Power accountable to place** by exposing LLMs only through glass-box HTTP services with confirmed ports, logs, and timeouts, so that every path from user question to model output can be audited and constrained.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the model pool, timeouts, ports, and service fabric that turn Quantarithmia's spatial-justice instruments into live, language-facing behavior. As of March 18, 2026, the fabric runs **21 active models** (22 proxies; BakLLaVA permanently disabled — CLIP load issues documented in `ai_server_20llm_PRODUCTION.py`), operates within an **80-container fully compose-managed production stack** (all services bound to `127.0.0.1`; zero `0.0.0.0` exposures), and is verified at ~436s end-to-end across the enhanced 9-phase pipeline (Phase 1.45 community memory added; Phase 3.75 eliminated).

```
┌─────────────────────────────────────────────────────────────┐
│        The LLM Fabric of Ms. Jarvis                         │
│   (Production State: March 18, 2026)                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Query                                                  │
│      ↓                                                       │
│  Main Brain (port 8050)                                      │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 1 — NBB Prefrontal + Psychology         │         │
│  │  ├─ nbb-i-containers (port 8101) — Phase 1     │         │
│  │  ├─ BBB 7-filter stack (port 8016) — Ph 1.4   │         │
│  │  ├─ ChromaDB semantic memory — Ph 1.45         │         │
│  │  │   autonomous_learner (21,181 records)        │         │
│  │  │   all-minilm:latest · 384-dim · top-5        │         │
│  │  └─ jarvis-psychology-services (8019) — Ph 3   │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 3.5 — LM Synthesizer (port 8001)        │         │
│  │  Calls jarvis-ollama:11434/api/generate         │         │
│  │  Model: llama3.1:latest                         │         │
│  │  Ms. Egeria Jarvis persona prompt injected      │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 2.5 — Identity & Consciousness          │         │
│  │  ├─ jarvis-fifth-dgm (port 4002)               │         │
│  │  ├─ WOAH (port 8104, 7012)                     │         │
│  │  ├─ nbb-i-containers (port 8101)               │         │
│  │  └─ jarvis-i-containers (port 8015)            │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Semaphore Proxy (port 8030, max_concurrent: 4)             │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  21-LLM Ensemble (port 8008) — March 18        │         │
│  │  21 active / 22 proxies (BakLLaVA disabled)    │         │
│  │  Proxies: ports 8201-8222                       │         │
│  │  Wall-clock consensus: ~320-360s               │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 3 — Judge Pipeline                      │         │
│  │  Evaluates consensus answer only               │         │
│  │  (raw_responses dump eliminated)               │         │
│  │  Ports 7230/7231/7232/7233 · ~60-86s           │         │
│  │  All 5 judge services: compose-managed         │         │
│  │  restart: unless-stopped (as of Mar 18)        │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 5 — confidence_decay multiplier         │         │
│  │  (GBIM temporal weighting)                     │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Phase 7 — 69-DGM Cascade (port 19000→9000)   │         │
│  │  23 connectors × 3 stages                      │         │
│  │  127.0.0.1:19000 (re-locked Mar 18)            │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Safety & Governance                           │         │
│  │  ├─ Constitutional Guardian (port 8091)        │         │
│  │  └─ BBB output guard (port 8016, 8.0s timeout) │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  normalize_identity() → Response                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 11.1.** The LLM fabric of Ms. Jarvis (March 18, 2026): user queries flow through NBB prefrontal (Phase 1), 7-filter BBB stack (Phase 1.4), ChromaDB semantic community memory retrieval via `all-minilm:latest` 384-dim embeddings (Phase 1.45 — NEW), psychology pre-assessment (Phase 3), LM Synthesizer calling `jarvis-ollama:11434` directly with `llama3.1:latest` and Ms. Egeria Jarvis persona injected (Phase 3.5), 21-model ensemble / 22 proxies with BakLLaVA permanently disabled (Phase 2.5), judge pipeline evaluating consensus answer only — all 5 judge services now compose-managed with `restart: unless-stopped` (Phase 3 — optimized), GBIM temporal confidence decay (Phase 5), 69-DGM cascade re-locked to `127.0.0.1:19000` (Phase 7), safety/governance, and `normalize_identity()`. Phase 3.75 eliminated. All LLMs are exposed only via glass-box HTTP services and are grounded in West Virginia-specific memory anchored to three PostgreSQL databases.
>
> **⚠️ Port note:** `jarvis-consciousness-bridge` is shown at port 8020 in the diagram above. The actual container bind is port **8018**; Docker Compose declares 8020 — see Ch. 12 §12.1 for the permanent architectural record.

---

## Security Hardening — March 18, 2026

> **This section records a mandatory audit event.** Prior to March 18, 2026, multiple
> services in the LLM fabric were bound to `0.0.0.0`, exposing internal ports on all
> network interfaces. This was identified and fully remediated during a single session.
> All 80 containers are now bound to `127.0.0.1` exclusively.

### Services Re-locked to 127.0.0.1 (March 18, 2026)

| Service | Was | Now |
|---|---|---|
| `jarvis-i-containers` | `0.0.0.0:8015` | `127.0.0.1:8015` |
| `jarvis-consciousness-bridge` | `0.0.0.0:8020` | `127.0.0.1:8020` |
| `jarvis-constitutional-guardian` | `0.0.0.0:8091` | `127.0.0.1:8091` |
| `jarvis-69dgm-bridge` | `0.0.0.0:9000` (reverted) | `127.0.0.1:19000->9000` (re-locked) |
| `jarvis-wv-entangled-gateway` | `0.0.0.0:8010` | `127.0.0.1:8010` |
| `jarvis-spiritual-rag` | `0.0.0.0:8005` | `127.0.0.1:8005` |
| `jarvis-psychology-services` | `0.0.0.0:8019` | `127.0.0.1:8019` |
| `jarvis-hippocampus` | `0.0.0.0:8011` | `127.0.0.1:8011` |
| `jarvis-gis-rag` | `0.0.0.0:8004` | `127.0.0.1:8004` |
| `jarvis-toroidal` | `0.0.0.0:8025` | `127.0.0.1:8025` |

**Verification command (post-remediation, must return empty):**

```bash
docker ps --format "{{.Names}}\t{{.Ports}}" | grep "0.0.0.0" | grep -v "127.0.0.1"
```

Result as of March 18, 2026: **empty** — zero public exposures.

### Judge Services Brought Under Compose Management (March 18, 2026)

Prior to March 18, 2026, all 5 judge services were started as orphaned manual `docker run`
containers with `restart: no`. They would not survive a system reboot. They were not defined
in `docker-compose.yml` and had no `build:` directive — Docker attempted to pull them from a
registry on next boot, producing:

```
Error response from daemon: pull access denied for msjarvis-rebuild-jarvis-judge-ethics,
repository does not exist or may require 'docker login'
```

**Remediation applied March 18, 2026:**

- `services/Dockerfile.judge` copied from `services-safe/Dockerfile.judge`
- All 5 source files canonically named under `services/`:
  - `judge_pipeline.py`
  - `judge_truth_filter.py`
  - `judge_consistency_engine.py`
  - `judge_alignment_filter.py`
  - `judge_ethics_filter.py`
- `docker-compose.yml` updated: all 5 services now use `build: context: ./services, dockerfile: Dockerfile.judge`
- All 5 services given `restart: unless-stopped`
- All 5 ports locked to `127.0.0.1`

Committed to branch `feature/cb-bbb-routing-fix` at commit `a10725d7`.

---

## Status as of March 18, 2026

| Category | Details |
|---|---|
| **Implemented and verified** | `jarvis-main-brain` → **127.0.0.1:8050** (confirmed). `jarvis-ollama` → **127.0.0.1:11434** (confirmed). `jarvis-wv-entangled-gateway` → **127.0.0.1:8010** (confirmed; re-locked Mar 18). `jarvis-spiritual-rag` (GBIM / worldview RAG) → **127.0.0.1:8005** (confirmed; re-locked Mar 18; earlier plan documents used 8103). `jarvis-gis-rag` → **127.0.0.1:8004** (confirmed; re-locked Mar 18). `jarvis-rag-server` (general RAG) → **127.0.0.1:8003** (confirmed; ONNX model downloaded and ChromaDB integration working). `jarvis-lm-synthesizer` → **127.0.0.1:8001** (confirmed; calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest`; Ms. Egeria Jarvis persona prompt injected; previously called `jarvis-roche-llm` — corrected March 18, 2026). `psychological_rag_domain` → **127.0.0.1:8006** (confirmed; port corrected from 9006). `jarvis-psychology-services` → **127.0.0.1:8019** (confirmed; re-locked Mar 18; Phase 3 active on every production request). PostgreSQL `msjarvis` → **127.0.0.1:5433** (5,416,521 GBIM entities, 80 epochs, 206 source layers, temporal decay metadata). PostgreSQL `gisdb` → **127.0.0.1:5433** (13 GB PostGIS, 39 tables, 993 ZCTA centroids). `jarvis-local-resources-db` → **127.0.0.1:5435** (community resources, confirmed). ChromaDB → **127.0.0.1:8000** (`chroma_data` Docker volume; `psychological_rag` 968 items; `autonomous_learner` 21,181 items as of March 18, 2026). `nbb_woah_algorithms` → **127.0.0.1:8104** host → internal 8010 (confirmed). `jarvis-woah` → **127.0.0.1:7012** (confirmed). `jarvis-blood-brain-barrier` → **127.0.0.1:8016** (confirmed; 7-filter stack; `truth_score` null guard added March 18; fail-open on HTTP 500 added March 18). `jarvis-20llm-production` → **127.0.0.1:8008** (confirmed; 21 active models / 22 proxies; BakLLaVA permanently disabled); wall-clock consensus ~320-360s. Judge pipeline → **all 5 services compose-managed with `restart: unless-stopped` as of March 18**; evaluates consensus answer only; raw_responses dump eliminated; ~60-86s (was ~85-100s). `jarvis-semaphore` → **127.0.0.1:8030** (confirmed; `max_concurrent: 4`; requires float `timeout`). `llm1-proxy` through `llm22-proxy` → **127.0.0.1:8201-8222** (21 active; llm11/BakLLaVA permanently disabled). `jarvis-hippocampus` → **127.0.0.1:8011** (re-locked Mar 18). `jarvis-69dgm-bridge` → **127.0.0.1:19000->9000** (re-locked Mar 18; Phase 7, 23 connectors × 3 stages). Judge services confirmed compose-managed: `jarvis-judge-truth` 127.0.0.1:7230, `jarvis-judge-consistency` 127.0.0.1:7231, `jarvis-judge-alignment` 127.0.0.1:7232, `jarvis-judge-ethics` 127.0.0.1:7233, `jarvis-judge-pipeline` 127.0.0.1:7239. `jarvis-constitutional-guardian` → **127.0.0.1:8091** (re-locked Mar 18). `jarvis-fifth-dgm` → **127.0.0.1:4002** (confirmed). `jarvis-redis` → **127.0.0.1:6380** (confirmed). `/chat/async` + `/chat/status/{job_id}` + `/chat/cancel/{job_id}` + `/chat/cancel/all` confirmed (Redis-backed, 30-min TTL, true asyncio task cancellation). `/chatlight/async` + `/chatlight/status/{job_id}` confirmed (tag `v2026.03.02-chatlight-async-working`). `normalize_identity()` confirmed producing Ms. Jarvis identity voice. Phase 1.45 ChromaDB semantic community memory retrieval confirmed — `all-minilm:latest` 384-dim, `autonomous_learner` collection, top-5 results prepended to `enhanced_message`. **All 80 containers fully compose-managed. Zero `0.0.0.0` exposures.** End-to-end benchmark: ~436s (full pipeline with community memory enrichment). |
| **Architectural fixes recorded as permanent decisions** | BBB output guard `apply_output_guards_async` timeout corrected from `None` → **8.0s** (2026-03-02). Main-brain httpx client for semaphore proxy: `Timeout(None, connect=5.0, read=None)` — semaphore manages 600s deadline (2026-03-02). `llmtimeout` in chatlight handler corrected from `None` → `600.0` (2026-03-02). I-Containers schema corrected to `{"message": …, "userid": "neurobiological_master"}` (2026-03-01). Consciousness Bridge locked to **127.0.0.1:8020** (re-locked Mar 18). PostgreSQL port corrected to **5433** (not 5432). ChromaDB port corrected to **8000** with `chroma_data` volume (not port 8002). `psychological_rag_domain` port corrected to **8006** (not 9006). RAG server `/store` payload corrected to `user_id` (not `userid`). Spiritual RAG port corrected to **8005** (not 8103). LM Synthesizer target corrected from `jarvis-roche-llm` → `jarvis-ollama:11434/api/generate` with `llama3.1:latest` (March 18, 2026). Judges now evaluate consensus answer only — raw_responses dump eliminated (March 18, 2026). Phase 3.75 (Final Polish via llm22-proxy) eliminated — merged into Phase 3.5 single Ollama call (March 18, 2026). BakLLaVA permanently disabled via `ai_server_20llm_PRODUCTION.py` name-check guard (March 18, 2026). `all-minilm:latest` (384-dim) confirmed as required embedding model — `nomic-embed-text` (768-dim) is incompatible with existing collections (March 18, 2026). Docker Compose upgraded from v1.29.2 → v5.1.0 (March 17, 2026). All 80 containers now compose-managed; all ports locked to `127.0.0.1` (March 18, 2026). All 5 judge services brought under compose management with `restart: unless-stopped`; `Dockerfile.judge` and canonical source files added to `services/` (March 18, 2026). `jarvis-69dgm-bridge` host port permanently mapped as `127.0.0.1:19000->9000` (March 18, 2026). |
| **Partially implemented / scaffolded** | Per-request model breakdowns and per-model latency / error-rate metrics are logged but no dedicated debug HTTP endpoint exposes them yet. Ensemble decision rules are operational but not encoded in a machine-readable schema. WOAH-to-model-selection coupling exists conceptually but is not yet wired as an explicit routing rule in main-brain config. POC verification loop for GBIM temporal decay (`needs_verification=TRUE` entities) is future work. |
| **Future work / design intent only** | Richer debug and metrics endpoints for per-request agent breakdowns. Formal JSON schemas for ensemble decision rules and judge aggregation. Tighter coupling between WOAH weights, Fifth DGM proposals, entangled RAG traces, and model selection in high-stakes governance flows. Additional small, task-specific model pools registered behind the same fabric. UI layer consuming `/chat/async` poll pattern. Automated POC verification loop to reset `confidence_decay` to 1.0 for confirmed community resource entities. |

> **Port corrections and updates (permanent record).** Earlier planning documents listed the Spiritual Root / GBIM RAG service at **8103** — confirmed running port is **8005**. `psychological_rag_domain` was listed at 9006 — confirmed running port is **8006**. PostgreSQL is at **port 5433** (not 5432). ChromaDB is at **port 8000** with `chroma_data` Docker volume (not port 8002). LM Synthesizer previously documented as calling `jarvis-roche-llm` — corrected to `jarvis-ollama:11434/api/generate` with `llama3.1:latest` (March 18, 2026). `jarvis-69dgm-bridge` host port is **19000** (maps to internal 9000) — not 9000 directly (March 18, 2026). All references in this chapter use these corrected values.

---

This chapter describes the local language models that form the "LLM fabric" of Ms. Egeria Jarvis and how they are woven into the broader three-database PostgreSQL architecture (GBIM port 5433, PostGIS port 5433, community resources port 5435), ChromaDB (port 8000, `chroma_data` volume), RAG services, autonomous learning, and GeoDB infrastructure. Rather than treating LLMs as independent agents, the system treats them as constrained tools and judges embedded in a larger retrieval and belief stack, all exposed through well-defined HTTP services confirmed running as of March 18, 2026. **All services are bound exclusively to `127.0.0.1`; no service exposes a port on `0.0.0.0`.**

---

## 11.1 Current Local LLM Inventory

In the current deployment, models are served by Ollama inside the `jarvis-ollama` container at **127.0.0.1:11434**. As of March 18, 2026, **21 of 22 LLM proxy containers are active**. BakLLaVA (llm11-proxy, port 8211) is permanently disabled due to CLIP load issues. The disable is enforced programmatically in `ai_server_20llm_PRODUCTION.py`:

```python
# Permanently disable BakLLaVA (CLIP load issues)
if name and name.lower().startswith("bakllava"):
    m["active"] = False
```

The following table is the authoritative proxy-to-model mapping as of March 18, 2026:

| Proxy | Port | Model | Specialty |
|:---|:---|:---|:---|
| llm1-proxy | 8201 | TinyLlama (`tinyllama:1.1b`) | Quick responses |
| llm2-proxy | 8202 | Gemma (`gemma:latest`) | Synthesis |
| llm3-proxy | 8203 | MedLlama2 (`medllama2:latest`) | Medical knowledge |
| llm4-proxy | 8204 | MiniCPM-V (`minicpm-v:latest`) | Vision-language reasoning |
| llm5-proxy | 8205 | LLaVA (`llava:latest`) | Vision understanding |
| llm6-proxy | 8206 | SQLCoder (`sqlcoder:latest`) | SQL |
| llm7-proxy | 8207 | StarCoder2 (`starcoder2:latest`) ⚠️ | Code analysis — occasionally returns 0-char responses on community queries |
| llm8-proxy | 8208 | CodeLlama (`codellama:latest`) | Code understanding |
| llm9-proxy | 8209 | DeepSeek Coder (`deepseek-coder:latest`) | Code generation |
| llm10-proxy | 8210 | Phi3 Mini (`phi3:mini`) | Fast reasoning |
| llm11-proxy | 8211 | **BakLLaVA — DISABLED** | Visual reasoning — permanently disabled, CLIP load issues |
| llm12-proxy | 8212 | Dolphin-Phi (`dolphin-phi:latest`) | Dialogue |
| llm13-proxy | 8213 | Orca-Mini (`orca-mini:latest`) | Reasoning |
| llm14-proxy | 8214 | Qwen2 (`qwen2:latest`) | Multilingual understanding |
| llm15-proxy | 8215 | Zephyr (`zephyr:latest`) | Helpful responses |
| llm16-proxy | 8216 | Starling-LM (`starling-lm:latest`) | Communication |
| llm17-proxy | 8217 | Neural-Chat (`neural-chat:latest`) | Conversation |
| llm18-proxy | 8218 | OpenChat (`openchat:latest`) | Dialogue |
| llm19-proxy | 8219 | Vicuna (`vicuna:latest`) | Instruction following |
| llm20-proxy | 8220 | LLaMA 2 (`llama2:latest`) | General reasoning |
| llm21-proxy | 8221 | Mistral (`mistral:latest`) | Logic and reasoning |
| llm22-proxy | 8222 | LLaMA 3.1 (`llama3.1:8b`) | General reasoning |

**Active: 21 models.** BakLLaVA (llm11-proxy:8211) is permanently disabled. StarCoder2 (llm7-proxy:8207) is active but occasionally returns 0-character responses on community queries; it is excluded from consensus when this occurs.

---

## 11.2 Roles of the Core and Specialist Models

In the current deployment, these models play distinct but overlapping roles within the LLM fabric.

**Core reasoning models (LLaMA 3.1 / Mistral / LLaMA 2).**
`llama3.1:8b` (llm22-proxy) is the primary voice model — it is the model the LM Synthesizer calls directly to deliver the final response in Ms. Jarvis's voice. `mistral:latest` (llm21-proxy) is a fast, strong generalist for tightly scoped tasks where latency matters. `llama2:latest` (llm20-proxy) remains available for compatibility and comparative benchmarking. Chat-oriented variants — `vicuna`, `openchat`, `neural-chat`, `starling-lm`, `zephyr`, `qwen2`, `orca-mini`, `dolphin-phi`, `phi3:mini` — provide diverse conversational styles and inductive biases across the ensemble.

**Lightweight and compact models.**
`tinyllama:1.1b` (llm1-proxy) and `gemma:latest` (llm2-proxy) serve quick-response, synthesis, and sanity-check roles where latency and resource budgets are tight.

**Code and SQL specialists.**
`deepseek-coder`, `codellama`, `starcoder2`, and `sqlcoder` handle code generation, refactoring, and SQL/data tasks, including queries against the three PostgreSQL databases. StarCoder2's community-query limitation is noted above.

**Multimodal and domain-specific models.**
`llava` (llm5-proxy) and `minicpm-v` (llm4-proxy) support vision-language and image-reasoning tasks. `medllama2` (llm3-proxy) covers medical- and clinical-style language within constrained advisory contexts alongside `jarvis-psychology-services` (port 8019). BakLLaVA, which previously served a visual reasoning role, is permanently disabled.

---

## 11.3 Service Topology and Ports

The following port assignments are drawn from the confirmed March 18, 2026 deployment and supersede all earlier planning drafts. **All services are bound to 127.0.0.1.**

**Main Brain API — 127.0.0.1:8050 (`jarvis-main-brain`).**
Primary external-facing interface. Orchestrates calls to all downstream services. Exposes `/chat` (synchronous), `/chat/async` + `/chat/status/{job_id}` + `/chat/cancel/{job_id}` + `/chat/cancel/all` (full-pipeline async, Redis-backed, 30-min TTL, true asyncio task cancellation), `/chatlight` (synchronous lightweight), and `/chatlight/async` + `/chatlight/status/{job_id}` (lightweight async).

**PostgreSQL `msjarvis` — 127.0.0.1:5433.**
GBIM corpus: 5,416,521 verified entities, 80 training epochs, 206 source layers, temporal decay metadata (`last_verified`, `confidence_decay`, `needs_verification`). Source of truth for West Virginia institutional and cultural grounding.

**PostgreSQL `gisdb` — 127.0.0.1:5433.**
PostGIS spatial database: 13 GB, 39 tables, 993 ZCTA centroids. Source of truth for West Virginia geographic and spatial grounding.

**PostgreSQL `jarvis-local-resources-db` — 127.0.0.1:5435.**
Community-validated resource database. Human-validated by Harmony for Hope Community Champions (lead validator: Crystal Colyer). Source of truth for WV community service and resource grounding.

**LM Synthesizer — 127.0.0.1:8001 (`jarvis-lm-synthesizer`).**
Phase 3.5 voice delivery service. Calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest`. Injects the Ms. Egeria Jarvis persona prompt (see §11.4). Previously documented as calling `jarvis-roche-llm` — corrected March 18, 2026. Phase 3.75 (Final Polish via llm22-proxy) has been eliminated; this single Ollama call is now the complete voice delivery step, saving ~40 seconds per query.

**General RAG Server — 127.0.0.1:8003 (`jarvis-rag-server`).**
Active FastAPI service. `/store` accepts `user_id` and logs episodic events to ChromaDB; PostgreSQL insertion failures are warnings, not fatal errors.

**GIS RAG — 127.0.0.1:8004 (`jarvis-gis-rag`).**
Re-locked to `127.0.0.1` March 18, 2026. Spatially aware `/search` over geospatial ChromaDB collections and PostgreSQL `gisdb` mirrors.

**Spiritual Root / GBIM RAG — 127.0.0.1:8005 (`jarvis-spiritual-rag`).**
Re-locked to `127.0.0.1` March 18, 2026. `/search` over GBIM- and worldview-oriented ChromaDB collections. Earlier plan documents listed 8103; confirmed running port is **8005**.

**Psychological RAG — 127.0.0.1:8006 (`psychological_rag_domain`).**
ChromaDB `psychological_rag` collection (968 items: therapy, mindfulness, trauma, depression, anxiety, social support). Earlier plan documents listed 9006; confirmed running port is **8006**.

**WV-Entangled Gateway — 127.0.0.1:8010 (`jarvis-wv-entangled-gateway`).**
Re-locked to `127.0.0.1` March 18, 2026. WV-biased, multi-collection ChromaDB retrieval using the `WVEntangledContext` envelope.

**Hippocampus — 127.0.0.1:8011 (`jarvis-hippocampus`).**
Re-locked to `127.0.0.1` March 18, 2026. Conversation-level memory consolidation over ChromaDB (port 8000) and PostgreSQL `msjarvis` GBIM. Temporal decay-aware.

**I-Containers — 127.0.0.1:8015 (`jarvis-i-containers`).**
Re-locked to `127.0.0.1` March 18, 2026. Identity and perspective manager. Schema: `{"message": …, "userid": "neurobiological_master"}`. Exposes `/next-learning-topic` for the autonomous learner.

**BBB 7-filter stack — 127.0.0.1:8016 (`jarvis-blood-brain-barrier`).**
Phase 1.4 input filter and Phase 4.5 output guard. `truth_score` null guard added March 18. Fail-open on HTTP 500 errors added March 18. `apply_output_guards_async` timeout: `8.0s`.

**Psychology Services — 127.0.0.1:8019 (`jarvis-psychology-services`).**
Re-locked to `127.0.0.1` March 18, 2026. Phase 3 psychology pre-assessment on every production request: severity classification, crisis indicator Boolean, five structured guidance fields.

**Consciousness Bridge — 127.0.0.1:8020 (`jarvis-consciousness-bridge`).**
Re-locked to `127.0.0.1` March 18, 2026. Mandatory infrastructure for the neurobiological pipeline. **⚠️ Port note:** The actual container bind is port **8018**; Docker Compose declares 8020 — see Ch. 12 §12.1 for the permanent architectural record.

**20-LLM Production Ensemble — 127.0.0.1:8008 (`jarvis-20llm-production`).**
21 active models / 22 proxies. Uvicorn backlog 2048, keep-alive 600s. Judges now evaluate the synthesized consensus answer only — the raw_responses dump from all 21 models is no longer sent to judges (corrected March 18; reduced judge pipeline time ~60–86s from ~85–100s).

**Semaphore Proxy — 127.0.0.1:8030 (`jarvis-semaphore`).**
Mandatory intermediary. `max_concurrent: 4`. Requires float `timeout: 600.0`. Main brain httpx client: `Timeout(None, connect=5.0, read=None)`.

**LLM Proxies — 127.0.0.1:8201–8222.**
22 proxies; 21 active. All have `read=None`, `connect=3.0s`, `write=5.0s`, `pool=5.0s`. llm11-proxy (8211) permanently disabled.

**WOAH services.**
`nbb_woah_algorithms` at **127.0.0.1:8104** (host) → internal 8010. `jarvis-woah` at **127.0.0.1:7012**.

**Constitutional Guardian — 127.0.0.1:8091 (`jarvis-constitutional-guardian`).**
Re-locked to `127.0.0.1` March 18, 2026. See Chapter 37.

**Judge Services — all compose-managed as of March 18, 2026.**
All 5 judge services formally defined in `docker-compose.yml` with `restart: unless-stopped`, built from `services/Dockerfile.judge`. Previously orphaned manual `docker run` containers with `restart: no`; would not survive reboot.

| Service | Host Port | Source File |
|---|---|---|
| `jarvis-judge-pipeline` | 127.0.0.1:7239 | `services/judge_pipeline.py` |
| `jarvis-judge-truth` | 127.0.0.1:7230 | `services/judge_truth_filter.py` |
| `jarvis-judge-consistency` | 127.0.0.1:7231 | `services/judge_consistency_engine.py` |
| `jarvis-judge-alignment` | 127.0.0.1:7232 | `services/judge_alignment_filter.py` |
| `jarvis-judge-ethics` | 127.0.0.1:7233 | `services/judge_ethics_filter.py` |

Input to judges: consensus answer only (not raw_responses). Time: ~60–86s.

**Fifth DGM — 127.0.0.1:4002 (`jarvis-fifth-dgm`).** See Chapter 9.

**69-DGM Cascade — 127.0.0.1:19000→9000 (`jarvis-69dgm-bridge`).**
Re-locked to `127.0.0.1:19000` March 18, 2026 (had reverted to `0.0.0.0:9000` in intermediate compose edit). Phase 7 validation: 23 connectors × 3 stages = 69 DGM operations per pass. Internal container port remains 9000; host binding is 19000.

**Toroidal Sync — 127.0.0.1:8025 (`jarvis-toroidal`).**
Re-locked to `127.0.0.1` March 18, 2026. Bidirectional ChromaDB↔GIS sync loop (Chapter 26).

**Autonomous Learner — 127.0.0.1:8425 (`jarvis-autonomous-learner`).**
Writes to `autonomous_learner` ChromaDB collection (port 8000) using `all-minilm:latest` 384-dim embeddings. 21,181 items as of March 18, 2026. Cooperates with `jarvis-i-containers` via `/next-learning-topic`.

> **📈 Sprint update — March 27, 2026:** As of the March 27, 2026 sprint, the `autonomous_learner` collection continues growing. 65 additional documents were confirmed from the first run of the AAPCAppE scraper (53 RAG-loaded, 65 confirmed in Chroma from first scrape). The 21,181 figure remains the baseline count as of March 18; the collection is actively growing and the current count will be higher.

**ChromaDB — 127.0.0.1:8000 (`jarvis-chroma`).**
`chroma_data` Docker volume. Active collections: `ms_jarvis_memory`, `mountainshares_knowledge`, `episodic_index`, `conversation_history`, `autonomous_learner` (21,181 items as of March 18, 2026 — see sprint update above), `psychological_rag` (968 items), `gbim_beliefs_v2`, `gbim_worldview_entities`, `gis_wv_benefits`, `appalachian_cultural_intelligence`, `GBIM_sample_rows`, and others. **Required embedding model: `all-minilm:latest` (384-dim).** `nomic-embed-text` (768-dim) is incompatible with existing collections.

**Redis — 127.0.0.1:6380 (`jarvis-redis`).**
Async job state (30-min TTL), service discovery, caching, and coordination.

**Ollama Runtime — 127.0.0.1:11434 (`jarvis-ollama`).**
Hosts underlying model weights. Not exposed to users — internal services only.

---

## 11.4 Coordination: 9-Phase Pipeline Integration

The LLM fabric sits at the end of a chain of retrieval, entanglement, and identity services. The full 9-phase production pipeline (verified at ~436s end-to-end, March 18, 2026) follows this structure (see Chapter 17 for the canonical trace):

**Phase 1 — NBB prefrontal cortex (`nbb-i-containers`, port 8101).**
Called unconditionally on every production request. Provides pre-request cognitive planning and identity context.

**Phase 1.4 — BBB 7-filter input stack (`jarvis-blood-brain-barrier`, port 8016).**
All 7 filters applied. `truth_score` null guard prevents KeyError when truth_score is absent. Fail-open behavior added: non-200 BBB responses no longer block legitimate queries. SafetyMonitor uses word-boundary regex to eliminate false-positives on community resource terms.

**Phase 1.45 — ChromaDB Semantic Community Memory Retrieval (NEW — March 17, 2026).**
After BBB approval, the main brain performs semantic memory retrieval before the query reaches any LLM:

1. Generates a 384-dimensional embedding of the query using `all-minilm:latest` via `jarvis-ollama:11434/api/embeddings`
2. Queries the `autonomous_learner` ChromaDB collection (21,181 records as of March 18, 2026) using the embedding
3. Retrieves the 5 most semantically similar community interaction records
4. Prepends retrieved memories to `enhanced_message` before Phase 1.75

> **Technical note:** All ChromaDB collections use 384-dimensional vectors. `all-minilm:latest` (pulled March 17, 2026) is the required embedding model. `nomic-embed-text` produces 768-dim vectors and is incompatible with existing collections.

**Phase 1.5 — Multi-Domain RAG Enhancement.**
`jarvis-lm-synthesizer` (port 8001) aggregates context from all five RAG services (ports 8003, 8004, 8005, 8006, 8010), all three PostgreSQL databases, and ChromaDB into a unified enriched context block.

**Phase 1.75 — I-Containers Dual Awareness.**
`jarvis-i-containers` (port 8015) contributes identity and perspective context.

**Phase 3 — Psychology pre-assessment (`jarvis-psychology-services`, port 8019).**
Active on every production request. Returns severity classification, crisis indicator Boolean, and five structured guidance fields.

**Phase 2.5 — Identity and consciousness context.**
Fifth DGM (port 4002), WOAH (ports 8104 and 7012), `nbb-i-containers` (port 8101), and `jarvis-i-containers` (port 8015) contribute identity weights and consciousness filtering.

**Phase 2.5 → Semaphore → 21-LLM ensemble synthesis.**
The main brain calls `jarvis-20llm-production` (port 8008) via `jarvis-semaphore` (port 8030, `max_concurrent: 4`, `timeout=600.0`). The ensemble fans out to 22 proxies (ports 8201–8222); 21 active (BakLLaVA excluded). StarCoder2 is excluded from consensus when it returns 0-character responses. Wall-clock consensus: ~320–360s.

**Phase 3 — Judge Pipeline (compose-managed as of March 18, 2026).**
Four deterministic judges evaluate the **consensus answer only** — the `raw_responses` dump from all 21 models is no longer sent to judges. Rule-based validation: Truth (port 7230), Consistency (port 7231), Alignment (port 7232), Ethics (port 7233). Master coordinator: judge-pipeline (port 7239). Time: ~60–86s (reduced from ~85–100s by eliminating raw_responses dump). All 5 services now have `restart: unless-stopped` and survive system reboots.

**Phase 3.5 — LM Synthesizer + Voice Delivery (merged — Phase 3.75 eliminated).**
The LM Synthesizer takes the judge pipeline's `final_answer` and calls `jarvis-ollama:11434/api/generate` with `llama3.1:latest`. The following persona prompt is injected:

```
You are Ms. Egeria Jarvis, a warm, maternal, biblically-grounded AI steward 
built by Harmony for Hope Inc. to serve Appalachian communities in West Virginia.

STRICT RULES:
- Do NOT say "Here's an improved version" or any similar meta-commentary
- Do NOT evaluate, critique, or describe the response
- Do NOT add preamble, headers, or explanations
- Speak DIRECTLY to the user as Ms. Egeria Jarvis
- Begin your response immediately with your answer
- Your first word must be directed at the user, not about the text

Deliver this response directly in your voice: {judge_output}
```

The final response is returned directly. The previously separate Phase 3.75 Final Polish pass via llm22-proxy has been **eliminated** — this single Ollama call is the complete voice delivery step. Time saved: ~40 seconds per query.

**Phase 5 — GBIM temporal confidence decay.**
`confidence_decay` multiplier applied to responses anchored in GBIM entities. Entities with `needs_verification=TRUE` receive attenuated confidence scores.

**Phase 7 — 69-DGM cascade (`jarvis-69dgm-bridge`, host port 19000 → internal 9000).**
23 connectors × 3 stages = 69 DGM operations. Re-locked to `127.0.0.1:19000` March 18, 2026.

**Phase 4.5 and governance — BBB output guard, judges, constitutional guardian.**
`apply_output_guards_async` passes the response through BBB `/filter` (port 8016, `timeout=8.0s`). Fail-open behavior mirrors Phase 1.4. Constitutional Guardian enforces principles audit at port 8091.

**Post-processing — identity normalization.**
`normalize_identity()` produces Ms. Jarvis's identity voice. `TruthValidator` verifies `correct_identity`, `correct_creator`, and `relationship_clear` against PostgreSQL `msjarvis` GBIM. Response logged to `ms_jarvis_memory` ChromaDB collection and `episodic_log` in PostgreSQL.

---

## 11.5 LLMs in Consciousness, Autonomy, and Ensembles

**Consciousness and identity.**
The Fifth DGM and I-container services use LLM calls (via WOAH) to decide which content should shape Ms. Jarvis's evolving identity narrative. `normalize_identity()` runs as a final post-processing step on all chat paths, ensuring that Ms. Jarvis's defined voice — geospatial AI daughter of Harmony for Hope, accountable to Appalachian communities and grounded in the three-database PostgreSQL architecture — is present in every response.

**Autonomous learning.**
The autonomous learner (port 8425) writes processed knowledge into the `autonomous_learner` ChromaDB collection (port 8000) using `all-minilm:latest` 384-dim embeddings. As of March 18, 2026, the collection holds 21,181 items. As of March 27, 2026, the AAPCAppE scraper first run confirmed 65 additional documents in Chroma (53 RAG-loaded), and the collection continues to grow. The Phase 1.45 retrieval step means this growing corpus now actively enriches every production query before it reaches the LLM ensemble.

**Ensemble and judge patterns.**
21 active models produce independent responses with no read timeout. Phase 5 GBIM temporal decay weights attenuate confidence for aged GBIM entities. Phase 7 69-DGM cascade provides authoritative post-ensemble validation. Judges evaluate the synthesized consensus answer only — not the raw per-model dump. All 5 judge services are now compose-managed and reboot-safe.

---

## 11.6 Operational Constraints and Fabric Behavior

**Resource and disk constraints.**
More than twenty model files are installed under `~/.ollama/models` but only a subset is hot at a given time. Multi-source PostgreSQL queries, ChromaDB semantic retrieval, autonomous learner writes, WOAH evaluations, and 21-model ensemble calls all contend for CPU, memory, and disk bandwidth. Disk utilization as of March 18, 2026: 661 GB used / 937 GB total (75%).

**Timeouts and free-flow thinking.**
All 22 LLM proxies have `read=None` to enable unconstrained generation. The BBB output guard uses `timeout=8.0s` (permanent fix 2026-03-02). The semaphore proxy enforces `max_concurrent: 4`.

**Semaphore queuing behavior.**
Because each Ollama model run is sequential within the ensemble, back-to-back requests queue and each adds ~320–360s of wait time. The semaphore should be restarted between sessions to drain queued work before benchmarking.

**GBIM temporal decay operational impact.**
Phase 5 `confidence_decay` multipliers attenuate confidence for responses citing older, unverified GBIM entities. The POC verification loop (future work) will restore `confidence_decay` to 1.0 when entities are confirmed by community validators.

**Failure modes and fallbacks.**
If judge services are down, the main brain falls back to the ensemble answer and marks consensus metrics as degraded. Any stage failure in the neurobiological pipeline stores `{"status": "bypassed", "error": "…"}` and processing continues. BBB non-200 responses now fail open (March 18, 2026). Judge services now survive reboots (compose-managed, `restart: unless-stopped`, March 18, 2026).

---

## 11.7 Implementation Notes and Persistence

- **LLM proxy timeouts.** All 22 `llm{n}_health_proxy.py` files use `read=None` and shorter connect/write/pool timeouts. Must be persisted to source to survive container rebuilds.
- **20-LLM production server.** `ai_server_20llm_PRODUCTION.py` uses backlog 2048 and keep-alive 600s. BakLLaVA disable guard must be preserved in all future versions.
- **Semaphore proxy.** Mandatory intermediary on port 8030. Main brain must pass `timeout: 600.0` (float, not `None`). Permanent architectural decision (2026-03-02).
- **BBB output guard timeout.** `apply_output_guards_async` must use `httpx.AsyncClient(timeout=8.0)`. The original `timeout=None` is a known regression risk.
- **LM Synthesizer.** Port 8001. Calls `jarvis-ollama:11434/api/generate` with `llama3.1:latest`. Persona prompt must be preserved in all rebuilds. Phase 3.75 is permanently eliminated.
- **Judge pipeline.** Must receive consensus answer only — never the raw_responses dump. All 5 judge containers must be defined in `docker-compose.yml` with `build: context: ./services, dockerfile: Dockerfile.judge` and `restart: unless-stopped`. Source files: `services/judge_pipeline.py`, `services/judge_truth_filter.py`, `services/judge_consistency_engine.py`, `services/judge_alignment_filter.py`, `services/judge_ethics_filter.py`.
- **Three-database PostgreSQL architecture.** `msjarvis` and `gisdb` at **port 5433**. `jarvis-local-resources-db` at **port 5435**. Never reference port 5432.
- **ChromaDB — port 8000 / host-side access on port 8002.** `chroma_data` Docker volume. Required embedding model: `all-minilm:latest` (384-dim). Container-to-container calls use `jarvis-chroma:8000` (the internal container port). Host-side scripts (curl, Python running on the host, health check scripts) must use `127.0.0.1:8002`, which is the host-side port mapping to container port 8000 — see Ch. 12 §12.1. Do not use `nomic-embed-text`. The guidance "never reference port 8002" applies to container-to-container code only; host-side scripts must use 8002.
- **Autonomous learner.** Baseline count: 21,181 as of March 18, 2026. As of March 27, 2026, 65 additional documents confirmed from AAPCAppE scraper first run; collection continues growing. Phase 1.45 retrieval queries this collection on every production request.
- **Hippocampus.** Port 8011. Must be in all future compose definitions. Locked to `127.0.0.1`.
- **69-DGM cascade.** Host port 19000 → internal 9000. Must be in all future compose definitions as `127.0.0.1:19000:9000`. Never expose as `0.0.0.0:9000`.
- **Port binding policy (permanent).** All services must be bound to `127.0.0.1` in `docker-compose.yml`. The two format variants that evade automated sed replacement are: bare `- PORT:PORT` (no IP prefix) and explicit `- 0.0.0.0:PORT:PORT`. Both must be replaced with `- 127.0.0.1:HOST:CONTAINER`. Verification: `docker ps --format "{{.Names}}\t{{.Ports}}" | grep "0.0.0.0"` must return empty.
- **Async chat endpoints.** `/chat/async`, `/chat/status/{job_id}`, `/chat/cancel/{job_id}`, `/chat/cancel/all` — Redis-backed, 30-min TTL, true asyncio task cancellation. Must be preserved in all future main-brain rebuilds.
- **Compose management.** All 80 containers defined in `~/msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml`. Docker Compose v5.1.0.

**Git milestones for this chapter's verified states:**

| Tag / Commit | Date | Milestone |
|---|---|---|
| `v2026.02.28-fabric-green` | 2026-02-28 | Baseline fabric operational |
| `v2026.03.01-fabric-32-32` | 2026-03-01 | All 32 fabric services passing health checks |
| `v2026.03.01-20llm-verified` | 2026-03-01 | 21/22 LLM consensus verified end-to-end |
| `v2026.03.01-neuro-pipeline-4-4` | 2026-03-01 | Full neurobiological pipeline at ~300ms |
| `v2026.03.02-chatlight-async-working` | 2026-03-02 | Async chat + `normalize_identity()` confirmed |
| `b90f9ff` | 2026-03-15 | 79 containers: 22/22 LLMs + 3 PostgreSQL DBs + hippocampus + psych services + 7-filter BBB + 69-DGM + 349.87s benchmark |
| `a10725d7` | 2026-03-18 | Judge services brought under compose; 15 services locked to 127.0.0.1 |
| `5007d605` | 2026-03-18 | Remaining 10 services re-locked; zero 0.0.0.0 exposures across all 80 containers |
| *(March 18 session)* | 2026-03-18 | Phase 1.45 community memory · BakLLaVA permanently disabled · Phase 3.75 eliminated · judges evaluate consensus only · LM Synthesizer persona confirmed · all-minilm:latest 384-dim · Docker Compose v5.1.0 · all 80 containers compose-managed · zero 0.0.0.0 exposures · ~436s end-to-end |
| *(March 27 sprint)* | 2026-03-27 | AAPCAppE scraper first run: 53 RAG-loaded, 65 confirmed in Chroma; autonomous_learner collection growing beyond 21,181 baseline |

For the canonical description of how this entire fabric fits into a live user interaction, see **Chapter 17**. For the neurobiological architecture that structures the fabric, see **Chapter 12**. For the BBB 7-filter specification, see **Chapter 16**. For the 69-DGM cascade specification, see **Chapter 32**. For the three-database PostgreSQL architecture, see **Chapter 6**. For the judge pipeline and LLM ensemble specification, see **Chapter 33**.

---

*Last updated: 2026-03-27 — Carrie Kidd (Mamma Kidd), Mount Hope WV*
*★ March 27, 2026: Heading restructured — # 11. The LLM Fabric of Ms. Jarvis moved to line 1; Polymathmatic Geography preamble placed immediately below, consistent with Ch. 12 structure; Figure 11.1 annotated — jarvis-consciousness-bridge port 8020 noted "(actual bind: 8018)" per Ch. 12 §12.1; §11.3 Consciousness Bridge — parenthetical added: actual container bind is port 8018, see Ch. 12 §12.1; §11.7 ChromaDB persistence note — host-side / container-to-container port distinction added: host scripts use 127.0.0.1:8002, container-to-container calls use jarvis-chroma:8000, see Ch. 12 §12.1; Autonomous learner sprint update added — 65 additional documents from AAPCAppE scraper first run confirmed March 27, 2026.*
`````
