# Why This Matters for Polymathmatic Geography

This chapter describes how multiple language models and evaluation components operate together in Ms. Jarvis during live requests, all grounded in the three-database PostgreSQL architecture (`msjarvis` port 5433 with 5,416,521 verified GBIM beliefs; `gisdb` port 5433 PostGIS; `jarvis-local-resources-db` port 5435). It supports:

- **P1 – Every where is entangled** by routing every user query through 21 expert models and 5 judge services whose combined signals propagate through barrier, container, and memory layers anchored to PostgreSQL as first-class inputs.

- **P3 – Power has a geometry** by making evaluation explicit and inspectable — `consensus_score`, `judge_verdicts`, `all_issues`, and per-judge scores are all surfaced in `consciousnesslayers` on every `UltimateResponse`.

- **P5 – Design is a geographic act** by applying alignment and ethics judges that specifically check for adherence to Ms. Egeria Jarvis's community-service identity and Appalachian-rooted values constraints validated against PostgreSQL GBIM.

- **P12 – Intelligence with a ZIP code** by grounding the composite prompt sent to all 21 experts with local RAG context from `jarvis-spiritual-rag` (port **8005**, queries PostgreSQL-sourced GBIM collections) and `jarvis-gis-rag` (port **8004**, queries PostgreSQL `gisdb`) before any synthesis occurs.

- **P16 – Power accountable to place** by exposing consensus metrics, judge scores, and refinement flags so communities, auditors, and operators can inspect the quality-assurance signals behind every response validated against PostgreSQL.

As such, this chapter belongs to the **Computational Instrument** tier: it is the authoritative description of the `jarvis-20llm-production` ensemble and judge pipeline invoked at Phase 2.5/Phase 3 of the canonical `ultimatechat` execution sequence (Chapter 17 §17.3). Chapters 11, 17, and 25 should cross-reference here for details on the 21-LLM + judge pipeline stack.

As of March 18, 2026, the fabric runs **21 active models** (22 proxies; BakLLaVA permanently disabled), all 5 judge services are **formally compose-managed with `restart: unless-stopped`**, all ports are bound to **127.0.0.1**, and the verified end-to-end benchmark is **~436 seconds**.

```
┌─────────────────────────────────────────────────────────────┐
│   Language Model Ensemble + Judge Pipeline Architecture    │
│   (Production State: March 18, 2026)                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Query → jarvis-main-brain (127.0.0.1:8050)            │
│      ↓                                                       │
│  Phase 1.45 — Community Memory Retrieval                    │
│  -  autonomous_learner ChromaDB (21,181 records)             │
│  -  all-minilm:latest 384-dim semantic search                │
│  -  Top-5 memories prepended to enhanced_message             │
│      ↓                                                       │
│  Context Assembly (validated vs PostgreSQL)                 │
│  -  PostgreSQL-sourced RAG (spiritual-rag 8005)              │
│  -  PostgreSQL gisdb (gis-rag 8004)                          │
│  -  Web research (when enabled)                              │
│  -  Persona framing (Ms. Egeria Jarvis)                      │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  jarvis-20llm-production (127.0.0.1:8008)     │         │
│  │  via jarvis-semaphore (127.0.0.1:8030)        │         │
│  │  ─────────────────────────────────────────    │         │
│  │  21 Active Expert Models (Sequential)         │         │
│  │  llm1-proxy to llm22-proxy                    │         │
│  │  127.0.0.1:8201-8222                          │         │
│  │  (llm11/BakLLaVA permanently disabled;        │         │
│  │   StarCoder2 returns 0-char on community      │         │
│  │   queries — 21 reliably active)               │         │
│  │                                                │         │
│  │  Outputs:                                      │         │
│  │  -  response (synthesized consensus)            │         │
│  │  -  minds_participated (typically 21)           │         │
│  │  -  expert_responses array                      │         │
│  │  -  /cached_expert_responses endpoint           │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Clean Response (strip multi-agent metadata)                │
│  Cache Workaround (fetch expert_responses if stripped)      │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  jarvis-judge-pipeline (127.0.0.1:7239)       │         │
│  │  ──────────────────────────────────────────   │         │
│  │  POST /evaluate — consensus answer ONLY        │         │
│  │  (raw_responses dump eliminated March 16)      │         │
│  │  asyncio.gather() parallel execution           │         │
│  │  ALL 5 SERVICES: compose-managed               │         │
│  │  restart: unless-stopped (March 18, 2026)      │         │
│  │  Dockerfile.judge / services/ source files     │         │
│  │                                                │         │
│  │  ┌──────────────────────────────────────────┐ │         │
│  │  │  judge-truth (127.0.0.1:7230)            │ │         │
│  │  │  -  Factual accuracy (vs GBIM/PostgreSQL)  │ │         │
│  │  │  -  Logical soundness                     │ │         │
│  │  │  -  Returns truth_score + issues          │ │         │
│  │  └──────────────────────────────────────────┘ │         │
│  │  ┌──────────────────────────────────────────┐ │         │
│  │  │  judge-consistency (127.0.0.1:7231)      │ │         │
│  │  │  -  Internal coherence                    │ │         │
│  │  │  -  Contradiction detection               │ │         │
│  │  │  -  Returns consistency_score             │ │         │
│  │  └──────────────────────────────────────────┘ │         │
│  │  ┌──────────────────────────────────────────┐ │         │
│  │  │  judge-alignment (127.0.0.1:7232)        │ │         │
│  │  │  -  Ms. Jarvis identity adherence         │ │         │
│  │  │  -  Community values (vs GBIM)            │ │         │
│  │  │  -  Returns alignment_score               │ │         │
│  │  └──────────────────────────────────────────┘ │         │
│  │  ┌──────────────────────────────────────────┐ │         │
│  │  │  judge-ethics (127.0.0.1:7233)           │ │         │
│  │  │  -  Harm screening                        │ │         │
│  │  │  -  Spiritual appropriateness             │ │         │
│  │  │  -  Returns ethics_score (default 0.9)    │ │         │
│  │  └──────────────────────────────────────────┘ │         │
│  │                                                │         │
│  │  Aggregation:                                  │         │
│  │  -  consensus_score = mean(4 judge scores)     │         │
│  │  -  expert_count = 21                           │         │
│  │  -  successful_experts = typically 21           │         │
│  │  -  reasoning with CONSENSUS_SCORE              │         │
│  │  -  judge_verdicts (pass/warning/fail)          │         │
│  │  -  all_issues aggregated                       │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Phase 3.5 — LM Synthesizer + Voice Delivery (merged)      │
│  -  jarvis-ollama:11434/api/generate (llama3.1:latest)       │
│  -  Ms. Egeria Jarvis persona prompt injected                │
│  -  Single Ollama call (Phase 3.75 eliminated March 18)      │
│  -  ~30-55s                                                  │
│      ↓                                                       │
│  BBB Output Guard (127.0.0.1:8016, validated vs PostgreSQL) │
│  normalize_identity (Ms. Egeria Jarvis persona)             │
│      ↓                                                       │
│  UltimateResponse                                           │
│  -  response (persona-wrapped final_answer)                  │
│  -  judge-pipeline consciousnesslayer:                       │
│    - consensus_score (0.0-1.0)                              │
│    - expert_count (21)                                      │
│    - successful_experts (typically 21)                      │
│    - reasoning                                              │
│    - judge_verdicts {truth, consistency, alignment, ethics} │
│    - judge_scores {truth, consistency, alignment, ethics}   │
│  -  truthverdict (from BBB, validated vs PostgreSQL)         │
│  -  background_rag_store → ms_jarvis_memory (ChromaDB)       │
│                                                              │
│  Fallback (if judge pipeline down):                         │
│  -  Use 21-LLM answer as-is                                  │
│  -  consensus_score: 0.8 (conservative)                      │
│  -  expert_count: 0 (signals degraded mode)                  │
│  -  status: "error" or "skipped"                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 33.1.** Language model ensemble and judge pipeline architecture: 21 active expert models queried sequentially via semaphore proxy, synthesized consensus answer passed to the 5-service judge pipeline (pipeline coordinator + truth + consistency + alignment + ethics) executing in parallel against the consensus answer only (raw_responses dump eliminated March 16, 2026), aggregated consensus_score and judge verdicts exposed in consciousnesslayers, Phase 3.5 LM Synthesizer + Voice Delivery merged into a single Ollama call (Phase 3.75 eliminated March 18, 2026), all context grounded in PostgreSQL-sourced RAG collections plus Phase 1.45 community memory retrieval (21,181 `autonomous_learner` records via `all-minilm:latest` 384-dim). **All 5 judge services are now compose-managed with `restart: unless-stopped` and bound to 127.0.0.1** (March 18, 2026). Fallback to degraded mode if judge pipeline unavailable.

---

## Status as of March 18, 2026

| Category | Details |
|---|---|
| **Implemented and verified** | `jarvis-20llm-production` (`ai_server_20llm_PRODUCTION.py`) confirmed running at **127.0.0.1:8008**. `jarvis-semaphore` proxy confirmed running at **127.0.0.1:8030**. **21 active expert model proxy containers** (`llm1-proxy` through `llm22-proxy`) confirmed running at **127.0.0.1:8201–8222** (22 proxies total; BakLLaVA at 8211 permanently disabled via name-check guard in `ai_server_20llm_PRODUCTION.py`; StarCoder2 at 8207 returns 0-char responses on community queries — 21 reliably active). **All 5 judge services formally defined in `docker-compose.yml` with `restart: unless-stopped` and bound to `127.0.0.1`** (March 18, 2026): `jarvis-judge-pipeline` **127.0.0.1:7239**, `jarvis-judge-truth` **127.0.0.1:7230**, `jarvis-judge-consistency` **127.0.0.1:7231**, `jarvis-judge-alignment` **127.0.0.1:7232**, `jarvis-judge-ethics` **127.0.0.1:7233**. `Dockerfile.judge` and canonical source files (`judge_pipeline.py`, `judge_truth_filter.py`, `judge_consistency_engine.py`, `judge_alignment_filter.py`, `judge_ethics_filter.py`) added to `services/`. **Judge pipeline updated March 16, 2026: evaluates consensus answer ONLY** — `raw_responses` dump no longer sent to judges; judge pipeline time reduced from ~85–100s to ~60–86s. **Phase 3.75 (Final LLM Polish via llm22-proxy) ELIMINATED March 18, 2026** — merged into Phase 3.5 LM Synthesizer single Ollama call; saves ~40s per query. **Phase 1.45 community memory retrieval** confirmed — `autonomous_learner` ChromaDB collection (21,181 records, growing ~288/day) queried via `all-minilm:latest` (384-dim) before LLM ensemble; top-5 memories prepended to `enhanced_message`. PostgreSQL `msjarvis` at **127.0.0.1:5433** (5,416,521 GBIM entities, 80 epochs, 206 source layers) as ground truth for truth judge and alignment judge. PostgreSQL `gisdb` at **127.0.0.1:5433** (PostGIS). `jarvis-local-resources-db` at **127.0.0.1:5435**. `POST /evaluate` endpoint on judge pipeline operational. `/cached_expert_responses` endpoint on `jarvis-20llm-production` operational. `asyncio.gather()` parallel judge execution confirmed. `judge-pipeline` consciousness layer in `UltimateResponse` confirmed. Fallback behavior confirmed. All 80 containers fully compose-managed via Docker Compose v5.1.0. Zero `0.0.0.0` exposures. **Verified performance (March 18, 2026):** consensus score 0.975 on identity questions; 21/21 expert participation; all four judge verdicts pass (Truth=1.0, Consistency=1.0, Alignment=1.0, Ethics=0.9); end-to-end **~436 seconds** (optimized from 532s baseline). |
| **Architectural fixes recorded as permanent decisions** | Judge services brought from orphaned manual `docker run` (restart: no) → compose-managed (restart: unless-stopped), Dockerfile.judge, `services/` canonical source files (March 18, 2026). All 5 judge ports locked to `127.0.0.1` (March 18, 2026). BBB port corrected from `0.0.0.0:8016` → `127.0.0.1:8016` (March 18, 2026). PostgreSQL port corrected from **5432** → **5433** throughout (March 18, 2026). PostgreSQL database corrected from `msjarvisgis` → `msjarvis` throughout (March 18, 2026). Judge pipeline coordinator port confirmed as **7239** (not 7230). Consensus-only judge input permanently enforced (March 16, 2026). Phase 3.75 eliminated (March 18, 2026). BakLLaVA permanently disabled via `ai_server_20llm_PRODUCTION.py` name-check guard (March 18, 2026). LM Synthesizer target corrected from `jarvis-roche-llm` → `jarvis-ollama:11434/api/generate` with `llama3.1:latest` (March 18, 2026). `all-minilm:latest` (384-dim) confirmed as required embedding model — `nomic-embed-text` (768-dim) is incompatible with existing collections (March 18, 2026). |
| **Partially implemented / scaffolded** | Direct BBB integration with consensus-score thresholds for automated promotion/quarantine is not yet wired into the live path. ChromaDB persistence of judge reasoning as a first-class collection for pattern learning is not yet implemented. Per-request model breakdowns and per-model latency/error-rate metrics are logged but no dedicated HTTP endpoint exposes them. |
| **Future work / design intent only** | Prometheus metrics for consensus distribution and judge latency. Dynamic expert pool selection based on task type and historical consensus patterns. Expert response caching and reuse for similar queries. Per-domain expert weighting, clustering of similar answers, multi-stage arbitration. ChromaDB persistence of judge reasoning as a first-class collection. Automated promotion/quarantine pipeline driven by `consensus_score` thresholds in collaboration with BBB. PostgreSQL-backed consensus metrics aggregation for long-term system health tracking. StarCoder2 evaluation — replace or retune for community-domain query performance. GPU inference server (WVU partnership pending) to reduce Phase 2.5 from ~320–360s to target ~80–120s. |

> **Port and database corrections (permanent record).** Earlier drafts of this chapter referenced PostgreSQL as `msjarvisgis` at port **5432** with 91 GB / 501 tables. The confirmed production database is `msjarvis` at port **5433** (5,416,521 GBIM entities, 80 epochs, 206 source layers). The PostGIS database is `gisdb` at port **5433** (13 GB, 39 tables). The community resources database is `jarvis-local-resources-db` at port **5435**. BBB was referenced at `0.0.0.0:8016` — corrected to `127.0.0.1:8016`. All references in this chapter use corrected values.

---

# 33. Language Model Ensemble and Judge Systems in Live Operation

This chapter describes how multiple language models and evaluation components operate together in Ms. Jarvis during live requests, all grounded in the three-database PostgreSQL architecture (`msjarvis` port 5433 with 5,416,521 verified GBIM beliefs; `gisdb` port 5433 PostGIS; `jarvis-local-resources-db` port 5435). Rather than treating LLMs as independent agents, the system treats them as constrained tools embedded in a larger retrieval and belief stack, with the judge pipeline providing structured quality-assurance signals validated against PostgreSQL. All services are bound exclusively to **127.0.0.1**; zero `0.0.0.0` exposures.

> **March 16–18, 2026 architectural changes:** (1) Judge pipeline now evaluates the consensus answer only — the `raw_responses` dump from all 21 models is no longer sent to judges, reducing judge pipeline time from ~85–100s to ~60–86s. (2) Phase 3.75 (Final LLM Polish via `llm22-proxy`) has been eliminated and merged into Phase 3.5 (LM Synthesizer + Voice Delivery) as a single `jarvis-ollama:11434/api/generate` call with `llama3.1:latest` and the Ms. Egeria Jarvis persona prompt injected — saves ~40s per query. (3) Phase 1.45 community memory retrieval now prepends top-5 `autonomous_learner` records (21,181 total, growing ~288/day) to every LLM prompt via `all-minilm:latest` 384-dim semantic search. **(4) All 5 judge services brought under compose management with `restart: unless-stopped` and locked to `127.0.0.1` — previously orphaned `docker run` containers with `restart: no` that would not survive a system reboot.** (5) All 80 containers now have zero `0.0.0.0` exposures.

---

## 33.1 Roles of the Core Models

In the current deployment, the live system assigns three primary roles to language models and services.

**Task execution (experts).** **21 reliably active expert models** (22 proxies total; BakLLaVA at port 8211 permanently disabled; StarCoder2 at port 8207 frequently returns 0-character responses on community-domain queries) are exposed behind lightweight proxy containers (`llm1-proxy` through `llm22-proxy`, confirmed running at **127.0.0.1:8201–8222**). For each consensus request, all active models receive the same composite prompt — which already includes Phase 1.45 community memory from `autonomous_learner` (21,181 records via `all-minilm:latest` 384-dim), PostgreSQL-sourced RAG context from `jarvis-spiritual-rag` (port **8005**, queries GBIM collections), PostgreSQL GeoDB context from `jarvis-gis-rag` (port **8004**), container-state hints, and orchestration directives — and generate independent candidate answers. The proxy architecture prevents Ollama overload. Model proxies are dispatched **sequentially** to prevent Ollama resource exhaustion on the CPU-only inference host (Legion 5, 29 GB RAM, `size_vram: 0` on all models).

**Structural transformation.** The LM Synthesizer (port **8001**) calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest` and the Ms. Egeria Jarvis persona prompt injected. It does not route through `jarvis-roche-llm` (corrected March 18, 2026). The previously separate Phase 3.5 (LM Synthesizer refinement) and Phase 3.75 (Final LLM Polish via `llm22-proxy`) have been **merged into a single Ollama call** (Phase 3.5). Phase 3.75 is permanently eliminated.

**Evaluation and critique.** Evaluation is handled by a 5-service judge pipeline composed of `jarvis-judge-pipeline` (coordinator, port **7239**) and four specialized FastAPI services: `judge-truth` (**7230**), `judge-consistency` (**7231**), `judge-alignment` (**7232**), and `judge-ethics` (**7233**). All five are now compose-managed with `restart: unless-stopped`. The pipeline orchestrator calls all four judges in parallel via `asyncio.gather()` against the **consensus answer only** — the `raw_responses` dump is no longer sent to judges (March 16, 2026).

Separating experts, transformers, judges, and persona layers makes behavior more inspectable and allows misalignments to be localized to particular components while maintaining PostgreSQL as the ground truth anchor.

---

## 33.2 Judge Services: From Orphaned Containers to Compose Management

> **This section records a permanent architectural remediation completed March 18, 2026.**

### Previous state (pre-March 18, 2026)

Prior to March 18, 2026, all 5 judge services were started as orphaned manual `docker run` containers. They had:

- `restart: no` — would not survive a system reboot
- No entry in `docker-compose.yml`
- No `build:` directive — Docker attempted to pull from registry on next boot, producing:

```
Error response from daemon: pull access denied for msjarvis-rebuild-jarvis-judge-ethics,
repository does not exist or may require 'docker login'
```

- Ports exposed on `0.0.0.0`, not `127.0.0.1`
- Source files in `services-safe/` but not canonically in `services/`

This meant that after any reboot, host hibernation, or `docker compose down`, all 5 judge services would fail to start and the entire judge pipeline would be in degraded fallback mode until manually restarted. The failure was silent — the main brain would receive `consensus_score: 0.8` with `expert_count: 0` and no judge verdicts, with no automated alerting.

### Remediation applied March 18, 2026

The following steps were completed and committed to branch `feature/cb-bbb-routing-fix` at commit `a10725d7`:

1. `services/Dockerfile.judge` — copied from `services-safe/Dockerfile.judge`
2. Canonical source files added to `services/`:

```
services/judge_pipeline.py
services/judge_truth_filter.py
services/judge_consistency_engine.py
services/judge_alignment_filter.py
services/judge_ethics_filter.py
```

3. `docker-compose.yml` updated — all 5 services now defined with:

```yaml
jarvis-judge-pipeline:
  build:
    context: ./services
    dockerfile: Dockerfile.judge
  command: python judge_pipeline.py
  ports:
    - "127.0.0.1:7239:7239"
  restart: unless-stopped

jarvis-judge-truth:
  build:
    context: ./services
    dockerfile: Dockerfile.judge
  command: python judge_truth_filter.py
  ports:
    - "127.0.0.1:7230:7230"
  restart: unless-stopped

jarvis-judge-consistency:
  build:
    context: ./services
    dockerfile: Dockerfile.judge
  command: python judge_consistency_engine.py
  ports:
    - "127.0.0.1:7231:7231"
  restart: unless-stopped

jarvis-judge-alignment:
  build:
    context: ./services
    dockerfile: Dockerfile.judge
  command: python judge_alignment_filter.py
  ports:
    - "127.0.0.1:7232:7232"
  restart: unless-stopped

jarvis-judge-ethics:
  build:
    context: ./services
    dockerfile: Dockerfile.judge
  command: python judge_ethics_filter.py
  ports:
    - "127.0.0.1:7233:7233"
  restart: unless-stopped
```

### Post-remediation verification

```bash
# All 5 judge services must appear compose-managed (not orphaned):
docker compose ps | grep judge

# All 5 must be bound to 127.0.0.1 only:
docker ps --format "{{.Names}}\t{{.Ports}}" | grep judge

# Must return empty (no 0.0.0.0 exposures on any judge service):
docker ps --format "{{.Names}}\t{{.Ports}}" | grep judge | grep "0.0.0.0"
```

Result as of March 18, 2026: all 5 services appear in `docker compose ps`, all ports bound to `127.0.0.1`, zero `0.0.0.0` exposures.

---

## 33.3 Authoritative Model List (March 18, 2026)

The following table is the canonical list of deployed LLM proxy containers as confirmed from `docker-compose.yml` and `docker ps` on the production host.

| Proxy | Port | Model | Status |
|---|---:|---|---|
| llm1-proxy | 8201 | TinyLlama (`tinyllama:1.1b`) | Active |
| llm2-proxy | 8202 | Gemma (`gemma:latest`) | Active |
| llm3-proxy | 8203 | MedLlama2 (`medllama2:latest`) | Active |
| llm4-proxy | 8204 | MiniCPM-V (`minicpm-v:latest`) | Active |
| llm5-proxy | 8205 | LLaVA (`llava:latest`) | Active |
| llm6-proxy | 8206 | SQLCoder (`sqlcoder:latest`) | Active |
| llm7-proxy | 8207 | StarCoder2 (`starcoder2:latest`) | Proxied — frequently 0-char on community queries |
| llm8-proxy | 8208 | CodeLlama (`codellama:latest`) | Active |
| llm9-proxy | 8209 | DeepSeek Coder (`deepseek-coder:latest`) | Active |
| llm10-proxy | 8210 | Phi3 Mini (`phi3:mini`) | Active |
| llm11-proxy | 8211 | **BakLLaVA — DISABLED** | Permanently disabled — CLIP load issues |
| llm12-proxy | 8212 | Dolphin-Phi (`dolphin-phi:latest`) | Active |
| llm13-proxy | 8213 | Orca-Mini (`orca-mini:latest`) | Active |
| llm14-proxy | 8214 | Qwen2 (`qwen2:latest`) | Active |
| llm15-proxy | 8215 | Zephyr (`zephyr:latest`) | Active |
| llm16-proxy | 8216 | Starling-LM (`starling-lm:latest`) | Active |
| llm17-proxy | 8217 | Neural-Chat (`neural-chat:latest`) | Active |
| llm18-proxy | 8218 | OpenChat (`openchat:latest`) | Active |
| llm19-proxy | 8219 | Vicuna (`vicuna:latest`) | Active |
| llm20-proxy | 8220 | LLaMA 2 (`llama2:latest`) | Active |
| llm21-proxy | 8221 | Mistral (`mistral:latest`) | Active |
| llm22-proxy | 8222 | LLaMA 3.1 (`llama3.1:8b`) | Active |

**Active: 21 models.** BakLLaVA (llm11-proxy:8211) permanently disabled via name-check guard in `ai_server_20llm_PRODUCTION.py`. StarCoder2 (llm7-proxy:8207) is proxied but unreliable on community-domain queries and is excluded from consensus when it returns 0-character responses. All proxies bound to `127.0.0.1`.

---

## 33.4 Judge Components and Evaluation Criteria

In the current deployment, the judge pipeline is composed of 5 FastAPI services — all **compose-managed**, all **bound to 127.0.0.1**, all with **`restart: unless-stopped`** — built from `services/Dockerfile.judge`.

### Service inventory (authoritative — March 18, 2026)

| Service | Host Port | Source File | Role |
|---|---|---|---|
| `jarvis-judge-pipeline` | 127.0.0.1:7239 | `services/judge_pipeline.py` | Coordinator: `POST /evaluate`, `asyncio.gather()`, aggregation |
| `jarvis-judge-truth` | 127.0.0.1:7230 | `services/judge_truth_filter.py` | Factual accuracy vs GBIM, logical soundness |
| `jarvis-judge-consistency` | 127.0.0.1:7231 | `services/judge_consistency_engine.py` | Internal coherence, contradiction detection |
| `jarvis-judge-alignment` | 127.0.0.1:7232 | `services/judge_alignment_filter.py` | Ms. Jarvis identity adherence, community values |
| `jarvis-judge-ethics` | 127.0.0.1:7233 | `services/judge_ethics_filter.py` | Harm screening, spiritual appropriateness |

### Inputs per request

For each evaluated response, the pipeline receives via `POST /evaluate` on `jarvis-judge-pipeline:7239` the **consensus answer only** — the `raw_responses` dump from all 21 models is no longer included (eliminated March 16, 2026):

```python
{
    "question": str,           # User's original question
    "answer": str,             # Synthesized consensus answer from 21-LLM ensemble
    "user_id": str,            # User identifier
    "evidence": dict,          # Optional evidence context
    "context": dict,           # Optional additional context
    "expert_responses": [      # Individual model responses (from /cached_expert_responses)
        {
            "model": str,
            "response": str,
            "confidence": float,
            "specialty": str,
            "success": bool
        }
    ]
}
```

### Responsibilities

**Truth judge (127.0.0.1:7230).** Rates factual plausibility validated against PostgreSQL `msjarvis` GBIM (5,416,521 entities) and internal logical soundness. Flags speculation, contradictions, and unsubstantiated claims. Returns `truth_score` (0.0–1.0) and a list of specific issues.

**Consistency judge (127.0.0.1:7231).** Checks for contradictions across the expert set and within the answer. Evaluates logical connectors, topic drift, and repetition. Returns `consistency_score` (0.0–1.0).

**Alignment judge (127.0.0.1:7232).** Evaluates adherence to Ms. Egeria Jarvis identity, community values validated against PostgreSQL `msjarvis` GBIM, and role constraints. Critical for blocking responses that claim wrong identity or use extraction/exploitation language. Returns `alignment_score` (0.0–1.0).

**Ethics judge (127.0.0.1:7233).** Screens for harmful, unethical, or spiritually inappropriate content within the configured BBB and spiritual frameworks. Returns `ethics_score` (0.0–1.0; defaults to 0.9 for clean responses in the current deployment).

The pipeline coordinator (`jarvis-judge-pipeline:7239`) aggregates all four via `asyncio.gather()`, computes `consensus_score` as the mean of all four judge scores, counts `expert_count` and `successful_experts` from the `expert_responses` array, builds an `expert_discussion` string, and produces a structured `reasoning` explanation: `REASONING: [analysis] | CONSENSUS_SCORE: [value] | FINAL_ANSWER: [text]`.

### Output format

```python
{
    "reasoning": str,              # "REASONING: ... | CONSENSUS_SCORE: ..."
    "consensus_score": float,      # Mean of four judge scores, [0.0, 1.0]
    "final_answer": str,           # Refined answer or original if no refinement needed
    "original_answer": str,        # Pre-refinement answer for comparison
    "refinement_applied": bool,    # True if LM synthesizer was called
    "overall_score": float,        # Same as consensus_score
    "needs_refinement": bool,      # True if fail_count > 0 or warning_count >= 2
    "expert_count": int,           # Total expert responses provided (e.g., 21)
    "successful_experts": int,     # Number with success=true
    "judge_verdicts": {
        "truth": str,              # "pass" | "warning" | "fail"
        "consistency": str,
        "alignment": str,
        "ethics": str
    },
    "judge_scores": {
        "truth": float,
        "consistency": float,
        "alignment": float,
        "ethics": float
    },
    "all_issues": [str],           # Aggregated issues from all judges
    "judgments": {                 # Full judge responses for debugging
        "truth": dict,
        "consistency": dict,
        "alignment": dict,
        "ethics": dict
    }
}
```

`jarvis-main-brain` stores these fields directly in the `judge-pipeline` consciousness layer `details`, making them visible in live traces and consumable by downstream layers.

### Fallback behavior

> **Important:** If `jarvis-judge-pipeline` is unavailable, returns a non-200, times out, or raises an exception, `jarvis-main-brain` falls back to: marking the layer `status: "error"` or `"skipped"`; leaving the original 21-LLM answer unchanged; attaching a generic reasoning string and conservative `consensus_score: 0.8`; and setting `expert_count` and `successful_experts` to 0 to signal degraded operation. User-facing responses are still produced, but without quality-assurance and consensus signals. With compose management and `restart: unless-stopped` now in place (March 18, 2026), this fallback should be reached only in the case of a service crash — not on every reboot as was the case previously.

---

## 33.5 Phase 3.5 — LM Synthesizer + Voice Delivery (Merged, March 18, 2026)

Phase 3.75 (Final LLM Polish via `llm22-proxy`) has been **permanently eliminated** as a separate pipeline phase. The LM Synthesizer (previously Phase 3.5) and Final Polish (previously Phase 3.75) are now a single merged operation:

1. Takes the judge pipeline's `final_answer` directly from `jarvis-judge-pipeline:7239`
2. Calls `jarvis-ollama:11434/api/generate` with `llama3.1:latest` via `jarvis-lm-synthesizer` (port **8001**)
3. Injects the Ms. Egeria Jarvis persona prompt:

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

4. Returns the final response directly — no separate polish pass

**Time saved:** ~40 seconds per query by eliminating the redundant `llm22-proxy` call. Phase 3.5 timing: ~30–55s. Phase 3.75 must be removed from all pipeline documentation, diagrams, and code comments.

---

## 33.6 Ensemble Patterns

`jarvis-20llm-production` (`ai_server_20llm_PRODUCTION.py`, port **8008**) implements the main ensemble pattern with context grounded in PostgreSQL and community memory.

### Sequential expert querying via proxy architecture

For each request:

1. **Phase 1.45** — `jarvis-main-brain` generates a 384-dim embedding of the query via `all-minilm:latest` at `jarvis-ollama:11434/api/embeddings`, queries the `autonomous_learner` ChromaDB collection (21,181 records as of March 18), retrieves the top-5 most semantically similar community interaction records, and prepends them to `enhanced_message`.

2. `jarvis-main-brain` builds the composite prompt from `enhanced_message` (including community memories), spiritual RAG context from `jarvis-spiritual-rag` (port **8005**, queries PostgreSQL-sourced GBIM collections), GIS and knowledge-base RAG from `jarvis-gis-rag` (port **8004**, queries `gisdb`), web-research summaries (when enabled), and persona framing for Ms. Egeria Jarvis.

3. This prompt is sent via `jarvis-semaphore` (port **8030**, `max_concurrent: 4`, `timeout: 600.0`) to `jarvis-20llm-production`, which dispatches the same generation request to active model proxies **sequentially** to prevent Ollama resource exhaustion. Each proxy handles one model independently and returns raw text, status, confidence weight, and model identifier. The service returns:

```python
{
    "response": str,              # Synthesized consensus answer
    "minds_participated": int,    # Number of successful responses (typically 21)
    "total_minds": int,           # Total models attempted (21)
    "timestamp": str,             # ISO timestamp
    "expert_responses": [
        {
            "model": str,
            "response": str,
            "confidence": float,
            "specialty": str,
            "success": bool
        }
    ]
}
```

4. `jarvis-20llm-production` also exposes `/cached_expert_responses`, storing the last expert responses in memory so the main brain can fetch them directly if the semaphore proxy strips them during transit.

### Cache workaround for expert responses

Due to a `status_code` vs `statuscode` key mismatch in the semaphore proxy that can strip `expert_responses` from the payload, `jarvis-main-brain` implements a confirmed workaround:

```python
expert_responses = llm20json.get("expert_responses", [])
if not expert_responses:
    response = await client.get(f"{llm20url}/cached_expert_responses")
    expert_responses = response.json().get("expert_responses", [])
```

This ensures expert responses always reach the judges even when the proxy strips unknown keys.

---

## 33.7 Phase-by-Phase Timing (March 18, 2026)

| Phase | Component | Timing |
|---|---|---|
| Phase 1 | Health checks (30s TTL cache) | ~0.7s (cached after first query) |
| Phase 1.4 | BBB input filter (7-filter, fail-open, 127.0.0.1:8016) | ~0.6s |
| Phase 1.45 | Community memory retrieval (`autonomous_learner`, `all-minilm:latest`) | ~0.7s |
| Phase 1.75–3 | Pre-LLM consciousness layers (NBB, hippocampus, etc.) | ~0.5s |
| Phase 2.5 | 21-LLM ensemble (rich prompt, CPU-only inference) | ~320–360s |
| Phase 3 | Judge pipeline (consensus answer only, 5 compose-managed services) | ~60–86s |
| Phase 3.5 | LM Synthesizer + Voice Delivery (merged, `llama3.1:latest`) | ~30–55s |
| Phase 4 + 4.5 | Consciousness bridge + BBB output guard (127.0.0.1:8016, 8.0s) | ~0.5s |
| **Total** | **End-to-end (March 18, optimized)** | **~436s** |

> Previous baseline before March 16–18 optimizations: ~532s. Key savings: judge consensus-only (~15–20s saved), Phase 3.5/3.75 merge (~40s saved), health check TTL cache (~3s saved per repeat query).

---

## 33.8 Use in Live Cycles

The ensemble and judge stack is wired into `jarvis-main-brain` as the synthesis step in the `ultimatechat` path (Chapter 17 §17.3 Phase 2.5). For the canonical execution sequence see **Chapter 17**.

### General query handling

For full, high-fidelity flows, `jarvis-main-brain`: performs Phase 1.45 community memory injection (21,181 `autonomous_learner` records); builds context from PostgreSQL-sourced RAG (`jarvis-spiritual-rag:8005`, `jarvis-gis-rag:8004`, `jarvis-rag-server:8003`), web research, NBB, and I-containers; calls `jarvis-20llm-production:8008` through `jarvis-semaphore:8030`; receives synthesized answer and `expert_responses`; cleans the raw answer (removing multi-agent metadata via regex); extracts or fetches `expert_responses` via the cache workaround; sends the consensus answer, question, and expert responses to `jarvis-judge-pipeline:7239`; receives `consensus_score`, `reasoning`, and `judge_verdicts` validated against PostgreSQL `msjarvis`; applies merged Phase 3.5 LM Synthesizer + Voice Delivery (`jarvis-lm-synthesizer:8001` → `jarvis-ollama:11434/api/generate`, `llama3.1:latest`, Ms. Jarvis persona); applies BBB output guard at `127.0.0.1:8016` (fail-open on HTTP 500); wraps in Ms. Egeria Jarvis persona via `normalize_identity()`.

The resulting `UltimateResponse` includes the persona-wrapped `final_answer` and a `judge-pipeline` consciousness layer containing `status`, `consensus_score`, `expert_count` (typically 21), `successful_experts` (typically 21), `reasoning`, `judge_verdicts`, and `judge_scores`, plus `truthverdict` from BBB and `icontainers-identity` layer.

### Research and content preparation

`consensus_score` and judge `reasoning` are available as signals for deciding whether internal evidence is sufficient, whether further retrieval or human review is warranted, and how assertive versus tentative the narrative should be. Low consensus scores (< 0.7) signal "more research needed."

### Scheduled and external-facing outputs

High-consensus (> 0.9) judge-refined content signals readiness for publication, with persona wrapping via the merged Phase 3.5 synthesizer ensuring all output sounds like Ms. Egeria Jarvis. In the current deployment, this pattern is available for use in scheduled tasks but automated scheduling pipelines are identified as future work.

---

## 33.9 Interaction with Barrier and Truth-Related Signals

Judge outputs and consensus metrics are available to barrier logic and truth filtering.

**Entry and promotion decisions.** BBB at **127.0.0.1:8016** operates with the `truth_score` null guard and fail-open on HTTP 500 (both input filter and output guard, added March 18, 2026). Threshold mapping (design intent — automated enforcement is future work):

| Consensus Score | Signal | Intended Action |
|---|---|---|
| ≥ 0.9 | High trust | Auto-promote; high-confidence response |
| 0.7–0.9 | Medium trust | Normal processing; consider additional retrieval |
| < 0.7 | Low trust | Quarantine or human review |
| Any `verdict == "fail"` | Block | Require manual override |

**Support and confidence labels.** Consensus scores map onto labels in `consciousnesslayers`: high consensus (≥ 0.9) → "strongly internally supported"; medium consensus (0.7–0.9) → "partially supported, consider more evidence"; low consensus (< 0.7) or judge fallback → "weakly supported" or "unresolved."

---

## 33.10 Influence on Containers, Memory, and Optimizers

**Containers and record paths.** `background_rag_store` writes `bg_<ISO8601>` entries into `ms_jarvis_memory` ChromaDB including `services: ["llm20production"]` metadata. Judge reasoning, `consensus_score`, and per-judge verdicts are carried in the `judge-pipeline` consciousness layer of `UltimateResponse` and are accessible via `/curator/background`. ChromaDB persistence of judge reasoning as a first-class collection for pattern learning is identified as future work.

**Long-term memory about system behavior.** The design intends that patterns in consensus and reasoning will be summarized into meta-memories: topics where experts almost always agree (e.g., Ms. Egeria Jarvis identity questions scored 0.975+ in current verified runs), domains where certain models frequently diverge, temporal trends in consensus scores, and correlation between consensus scores and user satisfaction metrics. Automated meta-memory generation is identified as future work.

**Optimization and experimentation.** The 69-DGM cascade (`jarvis-69dgm-bridge`, host port **19000** → internal **9000**, 23-connector × 3-stage) is the current implementation of the optimization loop. Prometheus metrics, dynamic expert pool selection, and per-domain expert weighting are identified as future work.

---

## 33.11 Implementation Notes and Persistence

- **Judge services — compose definition required.** All 5 judge services must be defined in `docker-compose.yml` with `build: context: ./services, dockerfile: Dockerfile.judge` and `restart: unless-stopped`. Source files must be present in `services/`. Do not start judge services with manual `docker run` — they will not survive reboot.
- **Judge input.** Must receive consensus answer only — never the raw_responses dump from all 21 models. This is a permanent architectural decision (March 16, 2026).
- **Judge ports.** All 5 services bound to `127.0.0.1`. Coordinator at **7239**. Individual judges at **7230**, **7231**, **7232**, **7233**. Never expose on `0.0.0.0`.
- **BakLLaVA disable guard.** Name-check guard in `ai_server_20llm_PRODUCTION.py` must be preserved in all future versions.
- **Phase 3.75 permanently eliminated.** Remove from all pipeline docs, diagrams, and code comments. Phase 3.5 is the complete merged voice delivery step.
- **LM Synthesizer.** Port **8001**. Calls `jarvis-ollama:11434/api/generate` with `llama3.1:latest`. Persona prompt must be preserved in all rebuilds.
- **PostgreSQL ports.** `msjarvis` and `gisdb` at **5433**. `jarvis-local-resources-db` at **5435**. Never reference port 5432.
- **ChromaDB.** Port **8000**, `chroma_data` volume. Required embedding model: `all-minilm:latest` (384-dim). Never reference port 8002 or `nomic-embed-text`.
- **Port binding policy.** All services must be bound to `127.0.0.1`. Verification: `docker ps --format "{{.Names}}\t{{.Ports}}" | grep "0.0.0.0"` must return empty.
- **Compose management.** All 80 containers defined in `~/msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml`. Docker Compose v5.1.0.

**Git milestones for this chapter's verified states:**

| Tag / Commit | Date | Milestone |
|---|---|---|
| `v2026.02.28-fabric-green` | 2026-02-28 | Baseline ensemble operational |
| `v2026.03.01-20llm-verified` | 2026-03-01 | 21/22 LLM consensus verified end-to-end |
| `v2026.03.02-chatlight-async-working` | 2026-03-02 | Async chat + `normalize_identity()` confirmed |
| `b90f9ff` | 2026-03-15 | 79 containers: 22/22 LLMs + full judge pipeline + 349.87s benchmark |
| *(March 16 session)* | 2026-03-16 | Consensus-only judge input; raw_responses dump eliminated; judge time ~60–86s |
| `a10725d7` | 2026-03-18 | Judge services brought under compose; 5 judge services restart: unless-stopped; all ports locked to 127.0.0.1 |
| `5007d605` | 2026-03-18 | Zero 0.0.0.0 exposures across all 80 containers; Phase 3.75 eliminated; BakLLaVA permanently disabled; ~436s benchmark |

For the canonical `ultimatechat` execution sequence that invokes this stack at Phase 2.5/Phase 3, see **Chapter 17**. For how the main brain integrates these signals into the broader coordination layer, see **Chapter 25**. For how the LLM fabric is described at the architectural overview level, see **Chapter 11**.

*Last updated: 2026-03-18 by Carrie Kidd, Mount Hope WV*
