> **Why this matters for Polymathmatic Geography**
> This chapter describes how multiple language models and evaluation components operate together in Ms. Jarvis during live requests, all grounded in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs). It supports:
> - **P1 – Every where is entangled** by routing every user query through 21 expert models and 4 judge services whose combined signals propagate through barrier, container, and memory layers anchored to PostgreSQL as first-class inputs.
> - **P3 – Power has a geometry** by making evaluation explicit and inspectable — `consensus_score`, `judge_verdicts`, `all_issues`, and per-judge scores are all surfaced in `consciousnesslayers` on every `UltimateResponse`.
> - **P5 – Design is a geographic act** by applying alignment and ethics judges that specifically check for adherence to Ms. Egeria Jarvis's community-service identity and Appalachian-rooted values constraints validated against PostgreSQL GBIM.
> - **P12 – Intelligence with a ZIP code** by grounding the composite prompt sent to all 21 experts with local RAG context from `jarvis-spiritual-rag` (port **8005**, queries PostgreSQL-sourced GBIM collections) and `jarvis-gis-rag` (port **8004**, queries PostgreSQL GeoDB) before any synthesis occurs.
> - **P16 – Power accountable to place** by exposing consensus metrics, judge scores, and refinement flags so communities, auditors, and operators can inspect the quality-assurance signals behind every response validated against PostgreSQL.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it is the authoritative description of the `llm20production` ensemble and judge pipeline invoked at Step 7 of the canonical `ultimatechat` execution sequence (Chapter 17 §17.3). Chapters 11, 17, and 25 should cross-reference here for details on the 21-LLM + judge pipeline stack.

```
┌─────────────────────────────────────────────────────────────┐
│   Language Model Ensemble + Judge Pipeline Architecture    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Query → jarvis-main-brain (8050)                      │
│      ↓                                                       │
│  Phase 1.45 — Community Memory Retrieval                    │
│  -  autonomous_learner ChromaDB (21,181 records)             │
│  -  all-minilm:latest 384-dim semantic search                │
│  -  Top-5 memories prepended to enhanced_message             │
│      ↓                                                       │
│  Context Assembly (validated vs PostgreSQL)                 │
│  -  PostgreSQL-sourced RAG (spiritual-rag 8005)              │
│  -  PostgreSQL GeoDB (gis-rag 8004)                          │
│  -  Web research (when enabled)                              │
│  -  Persona framing (Ms. Egeria Jarvis)                      │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  jarvis-20llm-production (port 8008)          │         │
│  │  via jarvis-semaphore (port 8030)             │         │
│  │  ─────────────────────────────────────────    │         │
│  │  21 Active Expert Models (Sequential)         │         │
│  │  llm1-proxy to llm22-proxy (8201-8222)        │         │
│  │  (22 proxies; StarCoder2 returns 0-char       │         │
│  │   on community queries — 21 reliably active)  │         │
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
│  │  jarvis-judge-pipeline (internal)             │         │
│  │  ──────────────────────────────────────────   │         │
│  │  POST /evaluate — consensus answer ONLY        │         │
│  │  (raw_responses dump eliminated March 16)      │         │
│  │  asyncio.gather() parallel execution           │         │
│  │                                                │         │
│  │  ┌──────────────────────────────────────────┐ │         │
│  │  │  judge-truth (7230)                      │ │         │
│  │  │  -  Factual accuracy (vs Postgres GBIM)   │ │         │
│  │  │  -  Logical soundness                     │ │         │
│  │  │  -  Returns truth_score + issues          │ │         │
│  │  └──────────────────────────────────────────┘ │         │
│  │  ┌──────────────────────────────────────────┐ │         │
│  │  │  judge-consistency (7231)                │ │         │
│  │  │  -  Internal coherence                    │ │         │
│  │  │  -  Contradiction detection               │ │         │
│  │  │  -  Returns consistency_score             │ │         │
│  │  └──────────────────────────────────────────┘ │         │
│  │  ┌──────────────────────────────────────────┐ │         │
│  │  │  judge-alignment (7232)                  │ │         │
│  │  │  -  Ms. Jarvis identity adherence         │ │         │
│  │  │  -  Community values (vs Postgres GBIM)   │ │         │
│  │  │  -  Returns alignment_score               │ │         │
│  │  └──────────────────────────────────────────┘ │         │
│  │  ┌──────────────────────────────────────────┐ │         │
│  │  │  judge-ethics (7233)                     │ │         │
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
│  BBB Output Guard (8016, validated vs PostgreSQL)           │
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

> **Figure 33.1.** Language model ensemble and judge pipeline architecture: 21 active expert models queried sequentially via semaphore proxy, synthesized consensus answer passed to 4-judge pipeline (truth, consistency, alignment, ethics) executing in parallel against the consensus answer only (raw_responses dump eliminated March 16, 2026), aggregated consensus_score and judge verdicts exposed in consciousnesslayers, Phase 3.5 LM Synthesizer + Voice Delivery merged into a single Ollama call (Phase 3.75 eliminated March 18, 2026), all context grounded in PostgreSQL-sourced RAG collections plus Phase 1.45 community memory retrieval (21,181 `autonomous_learner` records via `all-minilm:latest` 384-dim), with fallback to degraded mode if judge pipeline unavailable.

---

## Status as of March 18, 2026

| Category | Details |
|---|---|
| **Implemented now** | `jarvis-20llm-production` (`ai_server_20llm_PRODUCTION.py`) confirmed running at **127.0.0.1:8008**. `jarvis-semaphore` proxy confirmed running at **127.0.0.1:8030**. **21 active expert model proxy containers** (`llm1-proxy` through `llm22-proxy`) confirmed running at **127.0.0.1:8201–8222** (22 proxies total; StarCoder2 at 8207 returns 0-char responses on community queries — 21 reliably active). Judge pipeline (`jarvis-judge-pipeline`) confirmed running at internal ports **7230–7233** (corrected from erroneous 7239, March 16, 2026) with all 4 judges: `judge-truth` **7230**, `judge-consistency` **7231**, `judge-alignment` **7232**, `judge-ethics` **7233**. **Judge pipeline updated March 16, 2026: evaluates consensus answer ONLY** — `raw_responses` dump from all 21 models no longer sent to judges; judge pipeline time reduced from ~85–100s to ~60–86s. **Phase 3.75 (Final LLM Polish via llm22-proxy) ELIMINATED March 18, 2026** — merged into Phase 3.5 LM Synthesizer single Ollama call with Ms. Jarvis persona injection; saves ~40s per query. **Phase 1.45 community memory retrieval added March 17, 2026** — `autonomous_learner` ChromaDB collection (21,181 records, growing ~288/day) queried via `all-minilm:latest` (384-dim) before LLM ensemble; top-5 memories prepended to `enhanced_message`. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as ground truth for truth judge validation and alignment judge community values checking. `POST /evaluate` endpoint on judge pipeline operational. `/cached_expert_responses` endpoint on `jarvis-20llm-production` operational. `asyncio.gather()` parallel judge execution confirmed. `judge-pipeline` consciousness layer in `UltimateResponse` confirmed. Fallback behavior confirmed: if judge pipeline unavailable, main brain marks layer `status: "error"` or `"skipped"`, uses 21-LLM answer as-is, assigns `consensus_score: 0.8`, sets `expert_count: 0` to signal degraded operation. All 79 containers fully compose-managed via Docker Compose v5.1.0; all `build:` directives converted to `image:` references. **Verified performance (March 18, 2026):** consensus score 0.975 on identity questions; 21/21 expert participation; all four judge verdicts pass (Truth=1.0, Consistency=1.0, Alignment=1.0, Ethics=0.9); end-to-end processing time **~436 seconds** (optimized from 532s baseline) for full pipeline including Phase 1.45 community memory, 21-model ensemble, consensus-only judge pipeline, and merged Phase 3.5 voice delivery. |
| **Partially implemented / scaffolded** | Direct BBB integration with consensus-score thresholds (§33.5 extension): BBB at **8016** currently provides input truth filtering (with `truth_score` null guard and fail-open on HTTP 500) and output guarding independently validated against PostgreSQL; automated promotion/quarantine decisions driven by `consensus_score` thresholds are not yet wired into the live path. ChromaDB persistence of judge reasoning for pattern learning (§33.6 extension): judge outputs are surfaced in `consciousnesslayers` on `UltimateResponse` and visible via `/curator/background` logs, but are not yet written into a dedicated ChromaDB collection for long-term meta-memory. |
| **Future work / design intent only** | Prometheus metrics for consensus distribution and judge latency. Dynamic expert pool selection based on task type and historical consensus patterns. Expert response caching and reuse for similar queries. Per-domain expert weighting, clustering of similar answers, multi-stage arbitration. ChromaDB persistence of judge reasoning as a first-class collection for pattern learning and optimization feedback. Automated promotion/quarantine pipeline driven by `consensus_score` thresholds in collaboration with BBB validated against PostgreSQL. PostgreSQL-backed consensus metrics aggregation for long-term system health tracking. StarCoder2 evaluation — replace or retune for community-domain query performance. GPU inference server (WVU partnership pending) to reduce Phase 2.5 LLM ensemble from ~320–360s to target ~80–120s. |

> **Cross-reference:** This chapter is the authoritative description of what `llm20production` does internally. When **Chapter 11** (LLM Fabric) or **Chapter 17** (Executive Coordination, §17.3 Step 4) say "see Chapter 33 for details on the 21-LLM + judge pipeline stack that `llm20production` uses," they are pointing here. **Chapter 25** (Consciousness Coordinator) §25.7 also cross-references here for ensemble and judge detail. For the canonical `ultimatechat` execution sequence that invokes this stack, see **Chapter 17**.

---

# 33. Language Model Ensemble and Judge Systems in Live Operation

This chapter describes how multiple language models and evaluation components operate together in Ms. Jarvis during live requests, all grounded in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs). In the current deployment, the central implementation is `jarvis-20llm-production` (port **8008**) — a production 21-active-model consensus service — feeding `jarvis-judge-pipeline` (internal ports **7230–7233**, corrected March 16, 2026), whose structured outputs validated against PostgreSQL are then wrapped by the Ms. Jarvis persona via the merged Phase 3.5 LM Synthesizer + Voice Delivery and passed through BBB and identity layers. The judge pipeline returns a structured package including a `consensus_score`, `expert_count`, `reasoning`, and per-judge verdicts validated against PostgreSQL, so other layers can use these signals as first-class inputs.

> **March 16–18, 2026 architectural changes:** (1) Judge pipeline now evaluates the consensus answer only — the `raw_responses` dump from all 21 models is no longer sent to judges, reducing judge pipeline time from ~85–100s to ~60–86s. (2) Phase 3.75 (Final LLM Polish via `llm22-proxy`) has been eliminated and merged into Phase 3.5 (LM Synthesizer + Voice Delivery) as a single `jarvis-ollama:11434/api/generate` call with `llama3.1:latest` and the Ms. Egeria Jarvis persona prompt injected — saves ~40s per query. (3) Phase 1.45 community memory retrieval now prepends top-5 `autonomous_learner` records (21,181 total, growing ~288/day) to every LLM prompt via `all-minilm:latest` 384-dim semantic search. (4) All 22 proxy ports corrected from erroneous 7239 to proper per-judge ports (7230–7233).

---

## 33.1 Roles of the Core Models

In the current deployment, the live system assigns three primary roles to language models and services, all operating on context grounded in PostgreSQL `msjarvisgis`.

**Task execution (experts).** In the current deployment, **21 reliably active expert models** (22 proxies total; StarCoder2 at port 8207 frequently returns 0-character responses on community-domain queries) are exposed behind lightweight proxy containers (`llm1-proxy` through `llm22-proxy`, confirmed running at **127.0.0.1:8201–8222**). For each consensus request, all 21 models receive the same composite prompt — which already includes Phase 1.45 community memory from `autonomous_learner` (21,181 records via `all-minilm:latest` 384-dim), PostgreSQL-sourced RAG context from `jarvis-spiritual-rag` (port **8005**, queries GBIM collections), PostgreSQL GeoDB context from `jarvis-gis-rag` (port **8004**), container-state hints, and orchestration directives — and generate independent candidate answers. The proxy architecture prevents Ollama overload. In the current deployment, model proxies are dispatched **sequentially** rather than in true parallel to prevent Ollama resource exhaustion on the CPU-only inference host (Legion 5, 29 GB RAM, `size_vram: 0` on all models).

**Structural transformation.** In the current deployment, the LM synthesizer calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest` and the Ms. Egeria Jarvis persona prompt injected — it does not route through `jarvis-roche-llm` (fixed March 18, 2026). The previously separate Phase 3.5 (LM Synthesizer refinement) and Phase 3.75 (Final LLM Polish via `llm22-proxy`) have been **merged into a single Ollama call** (Phase 3.5). Phase 3.75 is eliminated.

**Evaluation and critique.** In the current deployment, evaluation is handled by `jarvis-judge-pipeline` composed of four confirmed running FastAPI services: `judge-truth` (**7230**), `judge-consistency` (**7231**), `judge-alignment` (**7232**), and `judge-ethics` (**7233**). The pipeline orchestrator calls all four judges in parallel via `asyncio.gather()` against the **consensus answer only** — the `raw_responses` dump is no longer sent to judges (March 16, 2026).

Separating experts, transformers, judges, and persona layers makes behavior more inspectable and allows misalignments to be localized to particular components while maintaining PostgreSQL as the ground truth anchor.

---

## 33.2 Authoritative Model List (March 18, 2026)

The following table is the canonical list of deployed LLM proxy containers as confirmed from `docker-compose.yml` and `docker ps` on the production host (cakidd-Legion-5-16IRX9).

| Proxy | Port | Model | Status |
|---|---:|---|---|
| llm1-proxy | 8201 | TinyLlama (`tinyllama:latest`) | Active |
| llm2-proxy | 8202 | Gemma (`gemma:2b`) | Active |
| llm3-proxy | 8203 | MedLlama2 (`medllama2:latest`) | Active |
| llm4-proxy | 8204 | MiniCPM-V (`minicpm-v:latest`) | Active |
| llm5-proxy | 8205 | LLaVA (`llava:latest`) | Active |
| llm6-proxy | 8206 | SQLCoder (`sqlcoder:latest`) | Active |
| llm7-proxy | 8207 | StarCoder2 (`starcoder2:latest`) | Proxied — frequently 0-char on community queries |
| llm8-proxy | 8208 | CodeLlama (`codellama:latest`) | Active |
| llm9-proxy | 8209 | DeepSeek Coder (`deepseek-coder:latest`) | Active |
| llm10-proxy | 8210 | Phi3 Mini (`phi3:mini`) | Active |
| llm11-proxy | 8211 | (assigned — verify against `llm_consensus_20_FINAL.py`) | Active |
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
| llm22-proxy | 8222 | LLaMA 3.1 (`llama3:latest`) | Active |

> **Note:** Earlier documentation referred to 22 models. The authoritative active count is **21** — 22 proxies are defined and running, but StarCoder2 (llm7-proxy, port 8207) frequently returns 0-character responses on community-domain queries. Consensus is extracted correctly from the 21 reliably responding models. The LM Synthesizer now calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest` — it does not route through `jarvis-roche-llm` (corrected March 18, 2026). All inference is CPU-only; GPU inference (WVU partnership) is pending.

---

## 33.3 Judge Components and Evaluation Criteria

In the current deployment, the judge pipeline is composed of four FastAPI services at ports **7230–7233**, wired into `jarvis-main-brain`. It synthesizes evaluation signals validated against PostgreSQL `msjarvisgis` and emits numeric and categorical outputs that other layers can consume.

### Inputs per request (March 18, 2026)

For each evaluated response, the pipeline receives via `POST /evaluate` the **consensus answer only** — the `raw_responses` dump from all 21 models is no longer included (eliminated March 16, 2026 to reduce judge pipeline time from ~85–100s to ~60–86s):

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

**Truth judge (port 7230).** Rates factual plausibility validated against PostgreSQL GBIM and internal logical soundness. Flags speculation, contradictions, and unsubstantiated claims. Returns `truth_score` (0.0–1.0) and a list of specific issues.

**Consistency judge (port 7231).** Checks for contradictions across the expert set and within the answer. Evaluates logical connectors, topic drift, and repetition. Returns `consistency_score` (0.0–1.0).

**Alignment judge (port 7232).** Evaluates adherence to Ms. Egeria Jarvis identity, community values validated against PostgreSQL GBIM, and role constraints. Critical for blocking responses that claim wrong identity or use extraction/exploitation language. Returns `alignment_score` (0.0–1.0).

**Ethics judge (port 7233).** Screens for harmful, unethical, or spiritually inappropriate content within the configured BBB and spiritual frameworks. Returns `ethics_score` (0.0–1.0; defaults to 0.9 for clean responses in the current deployment).

In the current deployment, the pipeline aggregates all four via `asyncio.gather()`, computes `consensus_score` as the mean of all four judge scores, counts `expert_count` and `successful_experts` from the `expert_responses` array, builds an `expert_discussion` string, and produces a structured `reasoning` explanation: `REASONING: [analysis] | CONSENSUS_SCORE: [value] | FINAL_ANSWER: [text]`.

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

In the current deployment, `jarvis-main-brain` stores these fields directly in the `judge-pipeline` consciousness layer `details`, making them visible in live traces and consumable by downstream layers.

### Fallback behavior

> **Important:** If `jarvis-judge-pipeline` is unavailable, returns a non-200, times out, or raises an exception, in the current deployment `jarvis-main-brain` falls back to: marking the layer `status: "error"` or `"skipped"`; leaving the original 21-LLM answer unchanged; attaching a generic reasoning string and conservative `consensus_score: 0.8`; and setting `expert_count` and `successful_experts` to 0 to signal degraded operation. User-facing responses are still produced, but without quality-assurance and consensus signals validated against PostgreSQL.

---

## 33.4 Phase 3.5 — LM Synthesizer + Voice Delivery (Merged, March 18, 2026)

Phase 3.75 (Final LLM Polish via `llm22-proxy`) has been **eliminated** as a separate pipeline phase. The LM Synthesizer (previously Phase 3.5) and Final Polish (previously Phase 3.75) are now a single merged operation:

1. Takes the judge pipeline's `final_answer` directly
2. Calls `jarvis-ollama:11434/api/generate` with `llama3.1:latest`
3. Injects the Ms. Egeria Jarvis persona prompt — warm, maternal, Appalachian voice, no meta-commentary
4. Returns the final response directly without a separate polish pass

**Time saved:** ~40 seconds per query by eliminating the redundant `llm22-proxy` call. Phase 3.5 timing: ~30–55s. Phase 3.75 should be removed from all pipeline documentation and diagrams.

---

## 33.5 Ensemble Patterns

In the current deployment, `jarvis-20llm-production` (`ai_server_20llm_PRODUCTION.py`, port **8008**) implements the main ensemble pattern with context grounded in PostgreSQL `msjarvisgis` and community memory from `autonomous_learner`.

### Sequential expert querying via proxy architecture

For each request in the current deployment:

1. **Phase 1.45** — `jarvis-main-brain` generates a 384-dim embedding of the query via `all-minilm:latest` at `jarvis-ollama:11434/api/embeddings`, queries the `autonomous_learner` ChromaDB collection (21,181 records as of March 18), retrieves the top-5 most semantically similar community interaction records, and prepends them to `enhanced_message`.

2. `jarvis-main-brain` then builds the composite prompt from `enhanced_message` (now including community memories), spiritual RAG context from `jarvis-spiritual-rag` (port **8005**, queries PostgreSQL-sourced GBIM collections), GIS and knowledge-base RAG context from `jarvis-gis-rag` (port **8004**, queries PostgreSQL GeoDB), web-research summaries (when enabled), and persona framing for Ms. Egeria Jarvis.

3. This prompt is sent via `jarvis-semaphore` (port **8030**) to `jarvis-20llm-production`, which dispatches the same generation request to 21 model proxies **sequentially** to prevent Ollama overload. Each proxy (`llm1-proxy` through `llm22-proxy`, ports **8201–8222**) handles one model independently and returns raw text, status, confidence weight, and model identifier. The service returns:

```python
{
    "response": str,              # Synthesized consensus answer
    "minds_participated": int,    # Number of successful responses (typically 21)
    "total_minds": int,           # Total models attempted (21)
    "timestamp": str,             # ISO timestamp
    "expert_responses": [         # Individual model responses
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

4. In the current deployment, `jarvis-20llm-production` also exposes `/cached_expert_responses`, storing the last expert responses in memory so the main brain can fetch them directly if the semaphore proxy strips them during transit.

### Judge-mediated synthesis (consensus answer only)

In the current deployment, the system uses the 21-LLM's consensus answer as the primary candidate, fetches `expert_responses` either from the main response or via `GET /cached_expert_responses`, supplies the **consensus answer** (not the full `raw_responses` dump), question, and `expert_responses` array to `jarvis-judge-pipeline` at `http://jarvis-judge-pipeline:7239/evaluate`, and lets the judge pipeline validated against PostgreSQL refine the answer, compute consensus metrics, and attach structured reasoning. This change (March 16, 2026) reduced judge pipeline time from ~85–100s to ~60–86s.

### Cache workaround for expert responses

In the current deployment, due to a `status_code` vs `statuscode` key mismatch in the semaphore proxy that can strip `expert_responses` from the payload, `jarvis-main-brain` implements a confirmed workaround:

```python
expert_responses = llm20json.get("expert_responses", [])
if not expert_responses:
    response = await client.get(f"{llm20url}/cached_expert_responses")
    expert_responses = response.json().get("expert_responses", [])
```

This ensures expert responses always reach the judges even when the proxy strips unknown keys.

---

## 33.6 Phase-by-Phase Timing (March 18, 2026)

| Phase | Component | Timing |
|---|---|---|
| Phase 1 | Health checks (30s TTL cache) | ~0.7s (cached after first query) |
| Phase 1.4 | BBB input filter (7-filter + fail-open) | ~0.6s |
| Phase 1.45 | Community memory retrieval (`autonomous_learner`, `all-minilm:latest`) | ~0.7s |
| Phase 1.75–3 | Pre-LLM consciousness layers (NBB, hippocampus, etc.) | ~0.5s |
| Phase 2.5 | 21-LLM ensemble (rich prompt, CPU-only inference) | ~320–360s |
| Phase 3 | Judge pipeline (consensus answer only) | ~60–86s |
| Phase 3.5 | LM Synthesizer + Voice Delivery (merged, `llama3.1:latest`) | ~30–55s |
| Phase 4 + 4.5 | Consciousness bridge + BBB output guard | ~0.5s |
| **Total** | **End-to-end (March 18, optimized)** | **~436s** |

> Previous baseline before March 16–18 optimizations: ~532s. Key savings: judge consensus-only (~15–20s saved), Phase 3.5/3.75 merge (~40s saved), health check TTL cache (~3s saved per repeat query).

---

## 33.7 Use in Live Cycles

In the current deployment, the ensemble and judge stack with PostgreSQL-grounded context is wired into `jarvis-main-brain` as the synthesis step in the `ultimatechat` path (Chapter 17 §17.3 Step 4). For the canonical execution sequence see **Chapter 17**.

### General query handling

For full, high-fidelity flows in the current deployment, `jarvis-main-brain`: discovers available services via `discover_services()` including PostgreSQL at port 5432; performs Phase 1.45 community memory injection (21,181 `autonomous_learner` records); builds context from PostgreSQL-sourced RAG, web research, NBB, and I-containers; calls `jarvis-20llm-production` through `jarvis-semaphore` (port **8030**); receives synthesized answer and `expert_responses`; cleans the raw answer (removing multi-agent metadata via regex); extracts or fetches `expert_responses` via the cache workaround; sends the consensus answer, question, and expert responses to `jarvis-judge-pipeline` (ports 7230–7233); receives `consensus_score`, `reasoning`, and `judge_verdicts` validated against PostgreSQL; applies merged Phase 3.5 LM Synthesizer + Voice Delivery (`jarvis-ollama:11434/api/generate`, `llama3.1:latest`, Ms. Jarvis persona); applies BBB output guard at **0.0.0.0:8016** (fail-open on HTTP 500); wraps in Ms. Egeria Jarvis persona via `normalize_identity`.

The resulting `UltimateResponse` in the current deployment includes the persona-wrapped `final_answer` from the merged Phase 3.5 synthesizer, and a `judge-pipeline` consciousness layer containing `status`, `consensus_score`, `expert_count` (typically 21), `successful_experts` (typically 21), `reasoning`, `judge_verdicts`, and `judge_scores`, plus `truthverdict` from BBB validated against PostgreSQL and `icontainers-identity` layer.

### Research and content preparation

In the current deployment, for research-heavy tasks, `consensus_score` and judge `reasoning` validated against PostgreSQL are available as signals for deciding whether internal evidence is sufficient, whether further retrieval or human review is warranted, and how assertive versus tentative the narrative should be. Low consensus scores (< 0.7) signal "more research needed."

### Scheduled and external-facing outputs

The design intends that high-consensus (> 0.9) judge-refined content validated against PostgreSQL signals readiness for publication, with persona wrapping via the merged Phase 3.5 synthesizer ensuring all output sounds like Ms. Egeria Jarvis rather than a generic model. In the current deployment, this pattern is available for use in scheduled tasks but automated scheduling pipelines are identified as future work.

---

## 33.8 Interaction with Barrier and Truth-Related Signals

In the current deployment, judge outputs and consensus metrics validated against PostgreSQL `msjarvisgis` are available to barrier logic and truth filtering, though direct BBB integration with consensus thresholds is identified as future work.

**Entry and promotion decisions.** The design intends that BBB-style barriers will use `consensus_score`, `judge_verdicts` validated against PostgreSQL, and `all_issues` to automate promotion/quarantine decisions. In the current deployment, BBB at **0.0.0.0:8016** operates with the `truth_score` null guard and fail-open on HTTP 500 (both input filter and output guard, added March 18, 2026). The following threshold mapping describes the intended logic: `consensus_score >= 0.9` → high trust, auto-promote to PostgreSQL; `0.7 <= consensus_score < 0.9` → medium trust, normal processing; `consensus_score < 0.7` → low trust, quarantine or human review; any `verdict == "fail"` → block or require manual override. Automated enforcement of these thresholds at the BBB level is identified as future work.

**Support and confidence labels.** In the current deployment, consensus scores validated against PostgreSQL map onto labels surfaced in `consciousnesslayers`: high consensus (≥ 0.9) → "strongly internally supported"; medium consensus (0.7–0.9) → "partially supported, consider more evidence"; low consensus (< 0.7) or judge fallback → "weakly supported" or "unresolved."

**Policy feedback and tuning.** The design intends that aggregated statistics over many runs (consensus distribution by task type, rate of ethics warnings) will inform threshold tuning, filter tightening, and model selection, all tracked against PostgreSQL ground truth. In the current deployment, these statistics are visible in `consciousnesslayers` logs and `ms_jarvis_memory` entries but are not yet aggregated via a dedicated analytics pipeline backed by PostgreSQL.

---

## 33.9 Influence on Containers, Memory, and Optimizers

In the current deployment, evaluation signals validated against PostgreSQL `msjarvisgis` are surfaced in `consciousnesslayers` and available for manual inspection, with automated persistence into ChromaDB and PostgreSQL and optimization pipelines identified as future work.

**Containers and record paths.** In the current deployment, `background_rag_store` writes `bg_<ISO8601>` entries into `ms_jarvis_memory` ChromaDB including `services: ["llm20production"]` metadata (Chapter 17 §17.6, Chapter 20). Judge reasoning, `consensus_score`, and per-judge verdicts validated against PostgreSQL are carried in the `judge-pipeline` consciousness layer of `UltimateResponse` and are accessible via `/curator/background`. ChromaDB persistence of judge reasoning as a first-class collection for pattern learning with PostgreSQL validation is identified as future work.

**Long-term memory about system behavior.** The design intends that patterns in consensus and reasoning validated against PostgreSQL will be summarized into meta-memories over time: topics where experts almost always agree (e.g., Ms. Egeria Jarvis identity questions scored 0.975+ in current verified runs), domains where certain models frequently diverge, temporal trends in consensus scores, and correlation between consensus scores and user satisfaction metrics. In the current deployment, this pattern recognition is manual; automated meta-memory generation backed by PostgreSQL is identified as future work.

**Optimization and experimentation.** The design intends that routing and prompt optimizers will use consensus metrics validated against PostgreSQL as objectives (maximize consensus on critical task classes), constraints (prevent configurations from degrading consensus or ethics scores), A/B testing signals, and model-selection feedback. The 69-DGM cascade (`jarvis-69dgm-bridge`, port 9000, 23-connector × 3-stage) is the current implementation of this optimization loop. Prometheus metrics, dynamic expert pool selection, and per-domain expert weighting are identified as future work.

---

## 33.10 Implementation Status and Future Work

**Confirmed implemented as of March 18, 2026:**

21 reliably active expert models via dedicated proxy containers (ports **8201–8222**, confirmed running). `ai_server_20llm_PRODUCTION.py` with `/cached_expert_responses` endpoint. Judge pipeline with all 4 judges operational (7230–7233, corrected March 16) validating against PostgreSQL `msjarvisgis`. **Consensus answer only sent to judges** (March 16 — reduces judge time to ~60–86s). **Phase 3.75 eliminated; Phase 3.5 LM Synthesizer + Voice Delivery merged** into single Ollama call (March 18 — saves ~40s). **Phase 1.45 community memory retrieval** (21,181 `autonomous_learner` records, `all-minilm:latest` 384-dim, March 17). Structured `REASONING / CONSENSUS_SCORE / FINAL_ANSWER` output format. Expert count and successful-expert tracking. Parallel judge execution via `asyncio.gather()`. Integration with main brain `consciousnesslayers`. Cache endpoint workaround for semaphore data preservation. PostgreSQL `msjarvisgis` at port 5432 as ground truth for truth judge and alignment judge validation. BBB `truth_score` null guard and fail-open on HTTP 500 (March 18). All 79 containers compose-managed via Docker Compose v5.1.0; `build:` → `image:` conversion complete.

**Verified performance (March 18, 2026, Legion 5 reference host):**
Consensus score 0.975 on identity questions. Expert participation 21/21. Judge verdicts all pass (Truth=1.0, Consistency=1.0, Alignment=1.0, Ethics=0.9). End-to-end processing time **~436 seconds** (optimized from 532s baseline). Judge pipeline time ~60–86s (reduced from ~85–100s by consensus-only evaluation). Phase 3.5 merged voice delivery ~30–55s.

**Future work:**

Direct BBB integration with consensus-score thresholds for automated promotion/quarantine validated against PostgreSQL. ChromaDB persistence of judge reasoning for pattern learning with PostgreSQL validation. Expert response caching and reuse for similar queries. Prometheus metrics for consensus distribution and judge latency backed by PostgreSQL. Dynamic expert pool based on task type and historical consensus patterns. PostgreSQL-backed consensus metrics aggregation for long-term system health tracking. StarCoder2 evaluation — replace or retune for community-domain query performance. GPU inference server (WVU partnership pending) to reduce Phase 2.5 from ~320–360s to target ~80–120s.

---

## 33.11 Summary

In the current deployment, Ms. Jarvis's language-model ensemble and judge systems are built around `jarvis-20llm-production` (port **8008**) with **21 reliably active expert model proxies** (22 proxies at ports **8201–8222**; StarCoder2 at 8207 unreliable on community queries) and `jarvis-judge-pipeline` with four judge services (7230–7233, corrected March 16, 2026) validating against PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs). The ensemble queries all 21 experts sequentially via `jarvis-semaphore` (port **8030**) with a composite prompt enriched by Phase 1.45 community memory (21,181 `autonomous_learner` records, `all-minilm:latest` 384-dim) and PostgreSQL-sourced RAG context. The judge layer receives the **consensus answer only** (not the full raw_responses dump), computes `consensus_score` validated against PostgreSQL, tracks `expert_count` and `successful_experts`, produces structured `reasoning`, and returns per-judge verdicts for truth, consistency, alignment, and ethics in ~60–86s. The merged Phase 3.5 LM Synthesizer + Voice Delivery (single `jarvis-ollama:11434/api/generate` call with `llama3.1:latest` and Ms. Jarvis persona, ~30–55s) replaces the previous separate Phase 3.5 + Phase 3.75 pattern. These signals are exposed as a `judge-pipeline` consciousness layer in every `UltimateResponse` and are available for reuse by barrier, container, memory, and optimization components anchored to PostgreSQL. End-to-end benchmark: **~436 seconds** (optimized from 532s baseline).

**If the judge pipeline is down**, `jarvis-main-brain` falls back to the 21-LLM answer unchanged, marks the layer degraded, and sets `expert_count: 0` — user-facing responses are still produced, but without quality-assurance signals validated against PostgreSQL.

For the canonical `ultimatechat` execution sequence that invokes this stack at Phase 2.5/Phase 3, see **Chapter 17**. For how the main brain integrates these signals into the broader coordination layer see **Chapter 25**. For how LLM fabric is described at the architectural overview level see **Chapter 11**.

*Last updated: 2026-03-18 by Carrie Kidd, Mount Hope WV*
