> **Why this matters for Polymathmatic Geography**
> This chapter describes how multiple language models and evaluation components operate together
> in Ms. Jarvis during live requests. It supports:
> - **P1 – Every where is entangled** by routing every user query through 21 expert models and
>   4 judge services whose combined signals propagate through barrier, container, and memory
>   layers as first-class inputs.
> - **P3 – Power has a geometry** by making evaluation explicit and inspectable — `consensus_score`,
>   `judge_verdicts`, `all_issues`, and per-judge scores are all surfaced in `consciousnesslayers`
>   on every `UltimateResponse`.
> - **P5 – Design is a geographic act** by applying alignment and ethics judges that specifically
>   check for adherence to Ms. Egeria Jarvis's community-service identity and Appalachian-rooted
>   values constraints.
> - **P12 – Intelligence with a ZIP code** by grounding the composite prompt sent to all 21
>   experts with local RAG context from `jarvis-spiritual-rag` (port **8005**) and
>   `jarvis-gis-rag` (port **8004**) before any synthesis occurs.
> - **P16 – Power accountable to place** by exposing consensus metrics, judge scores, and
>   refinement flags so communities, auditors, and operators can inspect the quality-assurance
>   signals behind every response.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it is the authoritative
> description of the `llm20production` ensemble and judge pipeline invoked at Step 7 of the
> canonical `ultimatechat` execution sequence (Chapter 17 §17.3). Chapters 11, 17, and 25
> should cross-reference here for details on the 20-LLM + judge pipeline stack.

---

## Status as of February 2026

| Category | Details |
|---|---|
| **Implemented now** | `jarvis-20llm-production` (`ai_server_20llm_PRODUCTION.py`) confirmed running at **127.0.0.1:8008** (`docker compose ps`). `jarvis-semaphore` proxy confirmed running at **127.0.0.1:8030**. 21 expert model proxy containers (`llm1-proxy` through `llm22-proxy`) confirmed running at **127.0.0.1:8201–8222**. Judge pipeline (`jarvis-judge-pipeline`) confirmed running at internal **7239** with all 4 judges: `judge-truth` **7230**, `judge-consistency` **7231**, `judge-alignment` **7232**, `judge-ethics` **7233**. `POST /evaluate` endpoint on judge pipeline operational. `/cached_expert_responses` endpoint on `jarvis-20llm-production` operational (cache workaround for semaphore key-mismatch). `asyncio.gather()` parallel judge execution confirmed. `judge-pipeline` consciousness layer in `UltimateResponse` confirmed, storing `consensus_score`, `expert_count`, `successful_experts`, `reasoning`, `judge_verdicts`, `judge_scores`. Fallback behavior confirmed: if judge pipeline unavailable, main brain marks layer `status: "error"` or `"skipped"`, uses 20-LLM answer as-is, assigns `consensus_score: 0.8`, sets `expert_count: 0` to signal degraded operation. Verified performance on reference host (Legion 5): consensus score 0.975 on identity questions; 21/21 expert participation; all four judge verdicts pass (Truth=1.0, Consistency=1.0, Alignment=1.0, Ethics=0.9); end-to-end processing time ~576 seconds for full 21-model + 4-judge evaluation. |
| **Partially implemented / scaffolded** | Direct BBB integration with consensus-score thresholds (§33.5 extension): BBB at **8016** currently provides input truth filtering and output guarding independently; automated promotion/quarantine decisions driven by `consensus_score` thresholds are not yet wired into the live path. ChromaDB persistence of judge reasoning for pattern learning (§33.6 extension): judge outputs are surfaced in `consciousnesslayers` on `UltimateResponse` and visible via `/curator/background` logs, but are not yet written into a dedicated Chroma collection for long-term meta-memory. |
| **Future work / design intent only** | Prometheus metrics for consensus distribution and judge latency. Dynamic expert pool selection based on task type and historical consensus patterns. Expert response caching and reuse for similar queries. Per-domain expert weighting, clustering of similar answers, multi-stage arbitration. ChromaDB persistence of judge reasoning as a first-class collection for pattern learning and optimization feedback. Automated promotion/quarantine pipeline driven by `consensus_score` thresholds in collaboration with BBB. |

> **Cross-reference:** This chapter is the authoritative description of what `llm20production`
> does internally. When **Chapter 11** (LLM Fabric) or **Chapter 17** (Executive Coordination,
> §17.3 Step 4) say "see Chapter 33 for details on the 20-LLM + judge pipeline stack that
> `llm20production` uses," they are pointing here. **Chapter 25** (Consciousness Coordinator)
> §25.7 also cross-references here for ensemble and judge detail. For the canonical
> `ultimatechat` execution sequence that invokes this stack, see **Chapter 17**.

---

# 33. Language Model Ensemble and Judge Systems in Live Operation

This chapter describes how multiple language models and evaluation components operate together in
Ms. Jarvis during live requests. In the current deployment, the central implementation is
`jarvis-20llm-production` (port **8008**) — a production 21-model consensus service — feeding
`jarvis-judge-pipeline` (internal port **7239**), whose structured outputs are then wrapped by
the Ms. Jarvis persona and passed through BBB and identity layers. The judge pipeline returns a
structured package including a `consensus_score`, `expert_count`, `reasoning`, and per-judge
verdicts, so other layers can use these signals as first-class inputs.

---

## 33.1 Roles of the Core Models

In the current deployment, the live system assigns three primary roles to language models and
services.

**Task execution (experts).** In the current deployment, 21 expert models (TinyLlama, Gemma,
Phi-3, Mistral, LLaMA 3.1, Qwen2, Vicuna, CodeLlama, DeepSeek Coder, LLaVA, MiniCPM-V, and
others) are exposed behind lightweight proxy containers (`llm1-proxy` through `llm22-proxy`,
confirmed running at **127.0.0.1:8201–8222**). For each consensus request, all 21 models receive
the same composite prompt — which already includes RAG context, spiritual RAG, container-state
hints, and orchestration directives — and generate independent candidate answers. The proxy
architecture prevents Ollama overload. In the current deployment, model proxies are dispatched
**sequentially** rather than in true parallel to prevent Ollama resource exhaustion.

**Structural transformation.** In the current deployment, the LM synthesizer (port **8001**)
and various FastAPI microservices handle summarization, classification, schema-rewrites, and
format alignment, running before or after the consensus step so that the judge sees clean,
comparable candidates and RAG collections receive normalized, persona-consistent records.

**Evaluation and critique.** In the current deployment, evaluation is handled by
`jarvis-judge-pipeline` at internal port **7239**, composed of four confirmed running FastAPI
services: `judge-truth` (**7230**) for factual accuracy and logical soundness, `judge-consistency`
(**7231**) for internal coherence and contradiction detection, `judge-alignment` (**7232**) for
Ms. Egeria Jarvis identity and values adherence, and `judge-ethics` (**7233**) for ethical
implications and harm screening. The pipeline orchestrator calls all four judges in parallel via
`asyncio.gather()`, then uses the LM synthesizer for refinement when needed.

Separating experts, transformers, judges, and persona layers makes behavior more inspectable and
allows misalignments to be localized to particular components.

---

## 33.2 Judge Components and Evaluation Criteria

In the current deployment, the judge pipeline is an internal HTTP service at
`http://jarvis-judge-pipeline:7239` wired into `jarvis-main-brain`. It synthesizes evaluation
signals and emits numeric and categorical outputs that other layers can consume.

### Inputs per request

For each evaluated response, the pipeline receives via `POST /evaluate`:
```python
{
    "question": str,           # User's original question
    "answer": str,             # Synthesized answer from 20-LLM consensus
    "user_id": str,            # User identifier
    "evidence": dict,          # Optional evidence context
    "context": dict,           # Optional additional context
    "expert_responses": [      # Individual model responses
        {
            "model": str,       # Model name (e.g., "mistral", "llama3")
            "response": str,    # Model's raw response text
            "confidence": float, # Weight/confidence score (0.0-1.0)
            "specialty": str,   # Model's specialty area
            "success": bool     # Whether model returned valid response
        }
    ]
}
```

The `expert_responses` array is critical: it enables judges to evaluate consensus across the
full expert ensemble rather than just the synthesized answer.

### Responsibilities

In the current deployment, the four judge services operate as follows.

**Truth judge (port 7230).** Rates factual plausibility and internal logical soundness. Flags
speculation, contradictions, and unsubstantiated claims. Returns `truth_score` (0.0–1.0) and a
list of specific issues.

**Consistency judge (port 7231).** Checks for contradictions across the expert set and within
the answer. Evaluates logical connectors, topic drift, and repetition. Returns
`consistency_score` (0.0–1.0).

**Alignment judge (port 7232).** Evaluates adherence to Ms. Egeria Jarvis identity, community
values, and role constraints. Critical for blocking responses that claim wrong identity or use
extraction/exploitation language. Returns `alignment_score` (0.0–1.0).

**Ethics judge (port 7233).** Screens for harmful, unethical, or spiritually inappropriate
content within the configured BBB and spiritual frameworks. Returns `ethics_score` (0.0–1.0;
defaults to 0.9 for clean responses in the current deployment).

In the current deployment, the pipeline aggregates all four via `asyncio.gather()`, computes
`consensus_score` as the mean of all four judge scores, counts `expert_count` and
`successful_experts` from the `expert_responses` array, builds an `expert_discussion` string,
and produces a structured `reasoning` explanation: `REASONING: [analysis] | CONSENSUS_SCORE:
[value] | FINAL_ANSWER: [text]`.

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

In the current deployment, `jarvis-main-brain` stores these fields directly in the
`judge-pipeline` consciousness layer `details`, making them visible in live traces and consumable
by downstream layers.

### Fallback behavior

> **Important:** If `jarvis-judge-pipeline` is unavailable, returns a non-200, times out, or
> raises an exception, in the current deployment `jarvis-main-brain` falls back to: marking the
> layer `status: "error"` or `"skipped"`; leaving the original 20-LLM answer unchanged;
> attaching a generic reasoning string and conservative `consensus_score: 0.8`; and setting
> `expert_count` and `successful_experts` to 0 to signal degraded operation. User-facing
> responses are still produced, but without quality-assurance and consensus signals.

---

## 33.3 Ensemble Patterns

In the current deployment, `jarvis-20llm-production` (`ai_server_20llm_PRODUCTION.py`, port
**8008**) implements the main ensemble pattern.

### Sequential expert querying via proxy architecture

For each request in the current deployment:

1. `jarvis-main-brain` builds a composite prompt from the user message, spiritual RAG context
   from `jarvis-spiritual-rag` (port **8005**, when available), GIS and knowledge-base RAG
   context from `jarvis-gis-rag` (port **8004**, when available), web-research summaries (when
   enabled), and persona framing for Ms. Egeria Jarvis.

2. This prompt is sent via `jarvis-semaphore` (port **8030**) to `jarvis-20llm-production`,
   which dispatches the same generation request to 21 model proxies **sequentially** to prevent
   Ollama overload. Each proxy (`llm1-proxy` through `llm22-proxy`, ports **8201–8222**) handles
   one model independently and returns raw text, status, confidence weight, and model identifier.
   The service returns:
```python
{
    "response": str,              # Synthesized consensus answer
    "minds_participated": int,    # Number of successful responses
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

3. In the current deployment, `jarvis-20llm-production` also exposes `/cached_expert_responses`,
   storing the last expert responses in memory so the main brain can fetch them directly if the
   semaphore proxy strips them during transit.

### Judge-mediated synthesis

In the current deployment, rather than selecting an expert's response directly, the system uses
the 20-LLM's consensus answer as the primary candidate, fetches `expert_responses` either from
the main response or via `GET /cached_expert_responses`, supplies the candidate, question, and
`expert_responses` array to `jarvis-judge-pipeline` at `http://jarvis-judge-pipeline:7239/evaluate`,
and lets the judge pipeline refine the answer, compute consensus metrics, and attach structured
reasoning. This is the "LLM-ensemble + multi-judge" pattern: experts generate independently;
an ensemble engine produces a candidate; multiple judges evaluate and optionally refine.

### Cache workaround for expert responses

In the current deployment, due to a `status_code` vs `statuscode` key mismatch in the semaphore
proxy that can strip `expert_responses` from the payload, `jarvis-main-brain` implements a
confirmed workaround:
```python
expert_responses = llm20json.get("expert_responses", [])
if not expert_responses:
    response = await client.get(f"{llm20url}/cached_expert_responses")
    expert_responses = response.json().get("expert_responses", [])
```

This ensures expert responses always reach the judges even when the proxy strips unknown keys.

---

## 33.4 Use in Live Cycles

In the current deployment, the ensemble and judge stack is wired into `jarvis-main-brain` as
the synthesis step in the `ultimatechat` path (Chapter 17 §17.3 Step 4). For the canonical
execution sequence see **Chapter 17**.

### General query handling

For full, high-fidelity flows in the current deployment, `jarvis-main-brain`: discovers
available services via `discover_services()`; builds context from RAG, web research, NBB, and
I-containers; calls `jarvis-20llm-production` through `jarvis-semaphore` (port **8030**);
receives synthesized answer and `expert_responses`; cleans the raw answer (removing multi-agent
metadata via regex); extracts or fetches `expert_responses` via the cache workaround; sends the
cleaned answer, question, and expert responses to `jarvis-judge-pipeline` at internal port
**7239**; receives `consensus_score`, `reasoning`, and `judge_verdicts`; applies BBB output
guard at **0.0.0.0:8016**; wraps in Ms. Egeria Jarvis persona via `normalize_identity`.

The resulting `UltimateResponse` in the current deployment includes the persona-wrapped
`final_answer` from judges, and a `judge-pipeline` consciousness layer containing `status`,
`consensus_score`, `expert_count` (typically 21), `successful_experts` (typically 21),
`reasoning`, `judge_verdicts`, and `judge_scores`, plus `truthverdict` from BBB and
`icontainers-identity` layer.

### Research and content preparation

In the current deployment, for research-heavy tasks, `consensus_score` and judge `reasoning`
are available as signals for deciding whether internal evidence is sufficient, whether further
retrieval or human review is warranted, and how assertive versus tentative the narrative should
be. Low consensus scores (< 0.7) signal "more research needed."

### Scheduled and external-facing outputs

The design intends that high-consensus (> 0.9) judge-refined content signals readiness for
publication, with persona wrapping ensuring all output sounds like Ms. Egeria Jarvis rather than
a generic model. In the current deployment, this pattern is available for use in scheduled tasks
but automated scheduling pipelines are identified as future work.

---

## 33.5 Interaction with Barrier and Truth-Related Signals

In the current deployment, judge outputs and consensus metrics are available to barrier logic
and truth filtering, though direct BBB integration with consensus thresholds is identified as
future work.

**Entry and promotion decisions.** The design intends that BBB-style barriers will use
`consensus_score`, `judge_verdicts`, and `all_issues` to automate promotion/quarantine decisions.
In the current deployment, BBB at **0.0.0.0:8016** operates independently as an input truth
filter and output guard; the following threshold mapping describes the intended logic:
`consensus_score >= 0.9` → high trust, auto-promote; `0.7 <= consensus_score < 0.9` → medium
trust, normal processing; `consensus_score < 0.7` → low trust, quarantine or human review;
any `verdict == "fail"` → block or require manual override. Automated enforcement of these
thresholds at the BBB level is identified as future work (§33.7 §33.5 extension).

**Support and confidence labels.** In the current deployment, consensus scores map onto labels
surfaced in `consciousnesslayers`: high consensus (≥ 0.9) → "strongly internally supported";
medium consensus (0.7–0.9) → "partially supported, consider more evidence"; low consensus
(< 0.7) or judge fallback → "weakly supported" or "unresolved."

**Policy feedback and tuning.** The design intends that aggregated statistics over many runs
(consensus distribution by task type, rate of ethics warnings) will inform threshold tuning,
filter tightening, and model selection. In the current deployment, these statistics are visible
in `consciousnesslayers` logs and `ms_jarvis_memory` entries but are not yet aggregated via a
dedicated analytics pipeline.

---

## 33.6 Influence on Containers, Memory, and Optimizers

In the current deployment, evaluation signals are surfaced in `consciousnesslayers` and
available for manual inspection, with automated persistence into Chroma and optimization
pipelines identified as future work.

**Containers and record paths.** In the current deployment, `background_rag_store` writes
`bg_<ISO8601>` entries into `ms_jarvis_memory` including `services: ["llm20production"]`
metadata (Chapter 17 §17.6, Chapter 20). Judge reasoning, `consensus_score`, and per-judge
verdicts are carried in the `judge-pipeline` consciousness layer of `UltimateResponse` and are
accessible via `/curator/background`. ChromaDB persistence of judge reasoning as a first-class
collection for pattern learning is identified as future work (§33.7 §33.6 extension).

**Long-term memory about system behavior.** The design intends that patterns in consensus and
reasoning will be summarized into meta-memories over time: topics where experts almost always
agree (e.g., Ms. Egeria Jarvis identity questions scored 0.975+ in current verified runs),
domains where certain models frequently diverge, temporal trends in consensus scores, and
correlation between consensus scores and user satisfaction metrics. In the current deployment,
this pattern recognition is manual; automated meta-memory generation is identified as future work.

**Optimization and experimentation.** The design intends that routing and prompt optimizers will
use consensus metrics as objectives (maximize consensus on critical task classes), constraints
(prevent configurations from degrading consensus or ethics scores), A/B testing signals, and
model-selection feedback. In the current deployment, these optimization loops are not yet
implemented; they are identified as future work.

---

## 33.7 Implementation Status and Future Work

**Confirmed implemented in the current deployment:**

21 expert models via dedicated proxy containers (ports **8201–8222**, confirmed running).
`ai_server_20llm_PRODUCTION.py` with `/cached_expert_responses` endpoint. Judge pipeline
v2.0.0-chapter33 with all 4 judges operational (7230–7233, confirmed). Structured
`REASONING / CONSENSUS_SCORE / FINAL_ANSWER` output format. Expert count and successful-expert
tracking. Parallel judge execution via `asyncio.gather()`. Integration with main brain
`consciousnesslayers`. Cache endpoint workaround for semaphore data preservation.

**Verified performance on reference host (Legion 5, local Docker, 2026-02-15 deployment):**
Consensus score 0.975 on identity questions. Expert participation 21/21. Judge verdicts all pass
(Truth=1.0, Consistency=1.0, Alignment=1.0, Ethics=0.9). End-to-end processing time
approximately 576 seconds for full 21-model ensemble + 4-judge evaluation.

**Future work:**

Direct BBB integration with consensus-score thresholds for automated promotion/quarantine
(§33.5 extension). ChromaDB persistence of judge reasoning for pattern learning (§33.6
extension). Expert response caching and reuse for similar queries. Prometheus metrics for
consensus distribution and judge latency. Dynamic expert pool based on task type and historical
consensus patterns.

---

## 33.8 Summary

In the current deployment, Ms. Jarvis's language-model ensemble and judge systems are built
around `jarvis-20llm-production` (port **8008**) with 21 expert model proxies (ports
**8201–8222**) and `jarvis-judge-pipeline` (internal port **7239**) with four judge services
(7230–7233). The ensemble queries all 21 experts sequentially via `jarvis-semaphore` (port
**8030**), synthesizes a candidate answer, and passes both the answer and `expert_responses` to
the judge pipeline. The judge layer computes `consensus_score` (0.0–1.0), tracks `expert_count`
and `successful_experts`, produces structured `reasoning`, and returns per-judge verdicts for
truth, consistency, alignment, and ethics. These signals are exposed as a `judge-pipeline`
consciousness layer in every `UltimateResponse` and are available for reuse by barrier,
container, memory, and optimization components.

**If the judge pipeline is down**, `jarvis-main-brain` falls back to the 20-LLM answer
unchanged, marks the layer degraded, and sets `expert_count: 0` — user-facing responses are
still produced, but without quality-assurance signals.

For the canonical `ultimatechat` execution sequence that invokes this stack at Step 4 (Step 7
in the full 11-step sequence), see **Chapter 17**. For how the main brain integrates these
signals into the broader coordination layer see **Chapter 25**. For how LLM fabric is described
at the architectural overview level see **Chapter 11**.
