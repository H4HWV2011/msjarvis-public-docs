# 33. Language Model Ensemble and Judge Systems in Live Operation

This chapter describes how multiple language models and evaluation components operate together in Ms. Jarvis during live requests. The central implementation is a production multi‑model consensus service (the 20‑LLM brain) feeding a dedicated judge pipeline, whose outputs are then wrapped by the Ms. Jarvis persona and passed through barrier, container, and psychology layers. The judge pipeline returns a structured package including a consensus score, expert counts, reasoning, and per‑judge verdicts, so other layers can use these signals as first‑class inputs.

## 33.1 Roles of the Core Models

The live system distinguishes several primary roles for language models:

**Task execution (experts).**  
A pool of 21 expert models (TinyLlama, Gemma, Phi‑3, Mistral, LLaMA 3.1, Qwen2, Vicuna, code‑oriented models like CodeLlama and DeepSeek Coder, and vision‑capable models like LLaVA and MiniCPM-V, among others) are exposed behind lightweight proxy services running on ports 8201-8222. Each model has its own dedicated proxy container (`llm1-proxy` through `llm22-proxy`) that handles generation requests independently. For each consensus request, all 21 models receive the same prompt—which already includes retrieval context, spiritual RAG, container‑state hints, and orchestration directives—and generate independent candidate answers. The proxy architecture prevents Ollama overload and enables true parallel processing.

**Structural transformation.**  
Some models and services (including the LM synthesizer on port 8001 and various FastAPI microservices) handle summarization, classification, schema‑rewrites, and format alignment. These transformations can run before or after the consensus step so that:

- The judge sees clean, comparable candidates.
- Containers and RAG collections receive normalized, persona‑consistent records.

**Evaluation and critique.**  
Evaluation is handled by a separate judge pipeline (port 7239) composed of four FastAPI services:
- `judge-truth` (port 7230): Factual accuracy and logical soundness
- `judge-consistency` (port 7231): Internal coherence and contradiction detection  
- `judge-alignment` (port 7232): Ms. Egeria Jarvis identity and values adherence
- `judge-ethics` (port 7233): Ethical implications and harm screening

The pipeline orchestrator calls all four judges in parallel using `asyncio.gather()`, then uses the LM synthesizer for refinement when needed. The pipeline:

- Receives the user question, synthesized answer, and individual expert responses.
- Calls each judge service to score and label the candidate answer.
- Produces a structured reasoning trace, consensus metrics, and a refined final answer.

Separating experts, transformers, judges, and persona layers makes behavior more inspectable and allows misalignments to be localized to particular components.

## 33.2 Judge Components and Evaluation Criteria

The judge pipeline is an internal HTTP service at `http://jarvis-judge-pipeline:7239` wired into the main brain. It synthesizes evaluation signals and emits numeric and categorical outputs that other layers can consume.

### Inputs per request

For each evaluated response, the pipeline receives via POST to `/evaluate`:
```python
{
    "question": str,           # User's original question
    "answer": str,             # Synthesized answer from 20-LLM consensus
    "user_id": str,            # User identifier
    "evidence": dict,          # Optional evidence context
    "context": dict,           # Optional additional context
    "expert_responses": [      # Individual model responses (Chapter 33 critical)
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

The `expert_responses` array is critical to Chapter 33 compliance—it enables judges to evaluate consensus across the full expert ensemble rather than just the synthesized answer.

### Responsibilities

The judge pipeline coordinates four independent judge services:

**Truth judge (port 7230).**  
Rates factual plausibility and internal logical soundness. Flags speculation, contradictions, and unsubstantiated claims. Returns `truth_score` (0.0-1.0) and a list of specific issues.

**Consistency judge (port 7231).**  
Checks for contradictions across the expert set and within the answer. Evaluates logical connectors, topic drift, and repetition. Returns `consistency_score` (0.0-1.0).

**Alignment judge (port 7232).**  
Evaluates adherence to Ms. Egeria Jarvis identity, community values, and role constraints. Critical for blocking responses that claim wrong identity or use extraction/exploitation language. Returns `alignment_score` (0.0-1.0).

**Ethics judge (port 7233).**  
Screens for harmful, unethical, or spiritually inappropriate content within the configured BBB and spiritual frameworks. Evaluates potential harm, bias, and transparency. Returns `ethics_score` (0.0-1.0, typically defaults to 0.9 for clean responses).

Each judge returns a verdict (`pass`, `warning`, or `fail`) and score; the pipeline then:

- Aggregates these signals via `asyncio.gather()` for parallel execution.
- Computes a `consensus_score` as the mean of all four judge scores.
- Counts `expert_count` and `successful_experts` from the `expert_responses` array.
- Builds an `expert_discussion` string showing each model's contribution.
- Produces a structured `reasoning` explanation following the format: `REASONING: [analysis] | CONSENSUS_SCORE: [value] | FINAL_ANSWER: [text]`

### Output format

The pipeline responds with a JSON structure including:
```python
{
    "reasoning": str,              # Structured: "REASONING: ... | CONSENSUS_SCORE: ..."
    "consensus_score": float,      # Scalar in [0.0, 1.0] from mean of judge scores
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
        "truth": float,            # Individual judge scores
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

The main brain's judge‑pipeline consciousness layer stores these fields directly in its `details`, so they are visible in live traces and can be consumed by downstream layers.

### Fallback behavior

If the judge pipeline is unavailable, returns a non‑200, times out, or raises an exception, the main brain falls back to:

- Marking the layer's status as `error` or `skipped`.
- Leaving the original LLM answer unchanged.
- Attaching a generic reasoning string and conservative default scores.
- Setting `expert_count` and `successful_experts` to 0.

This ensures that user‑facing responses are still produced even when the judge stack is degraded, though without the quality assurance and consensus signals.

## 33.3 Ensemble Patterns

The 20‑LLM consensus service (`ai_server_20llm_PRODUCTION.py` on port 8008) implements the main ensemble pattern used in production.

### Parallel expert querying via proxy architecture

For each request:

1. The main brain builds a composite prompt from:
   - User message
   - Spiritual RAG context (when available)
   - GIS and knowledge‑base RAG context
   - Web‑research summaries (when enabled)
   - Persona framing for Ms. Egeria Jarvis

2. This prompt is sent via a semaphore‑mediated proxy (port 8030) to the 20‑LLM service, which:
   - Dispatches the same generation request to 21 model proxies **sequentially** to prevent Ollama overload
   - Each proxy (`llm1-proxy` through `llm22-proxy` on ports 8201-8222) handles one model
   - Collects the raw text, status, confidence weights, and model identifiers
   - Returns a structured response that includes:
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

3. The 20-LLM service also exposes `/cached_expert_responses` endpoint that stores the last expert responses in memory, enabling the main brain to fetch them directly if the semaphore proxy strips them during transit.

### Judge‑mediated synthesis

Rather than selecting an expert's response directly, the system:

1. Uses the 20‑LLM's consensus answer as the primary candidate.
2. Fetches `expert_responses` either from the main response or via direct HTTP GET to `/cached_expert_responses`.
3. Supplies the candidate, question, and `expert_responses` array to the judge pipeline at `http://jarvis-judge-pipeline:7239/evaluate`.
4. Lets the judge pipeline refine the answer, compute consensus metrics, and attach structured reasoning.

This is a "LLM‑ensemble + multi‑judge" pattern: experts generate independently; an ensemble engine produces a candidate through weighted consensus; then multiple judges evaluate and optionally refine.

### Technical implementation details

**Cache workaround for expert responses:**  
Due to potential data loss through the semaphore proxy (which uses `status_code` vs `statuscode` key mismatch), the main brain implements a fallback:
```python
expert_responses = llm20json.get("expert_responses", [])
if not expert_responses:
    # Fetch directly from cache endpoint
    response = await client.get(f"{llm20url}/cached_expert_responses")
    expert_responses = response.json().get("expert_responses", [])
```

This ensures expert responses always reach the judges even if the semaphore proxy strips unknown keys.

**Aggregation and simple consensus:**  
Under normal conditions, the main brain treats the judge pipeline's `final_answer` and `consensus_score` as authoritative, wrapping them in the Ms. Jarvis persona and sending them through barrier and identity layers.

If the judge pipeline fails, the system falls back to:

- Using the 20‑LLM consensus answer as‑is.
- Assigning a conservative consensus score of 0.8 and "judge unavailable" reasoning.
- Setting `expert_count` to 0 to signal degraded operation.

Future variants can incorporate richer schemes (e.g., per‑domain expert weighting, clustering of similar answers, or multi‑stage arbitration), but the current implementation already surfaces disagreement and uncertainty as explicit numeric and textual signals.

## 33.4 Use in Live Cycles

The ensemble and judge stack is wired into the main brain as part of the ultimate (`/chatsync`) path.

### General query handling

For full, high‑fidelity flows:

1. The main brain:
   - Discovers available services (RAG, spiritual RAG, web, NBB, i‑containers, psychology, etc.)
   - Builds context from these services
   - Calls the 20‑LLM consensus service through the semaphore proxy (port 8030)
   - Receives synthesized answer and `expert_responses` array

2. It then:
   - Cleans the raw answer (removing multi‑agent metadata via regex)
   - Extracts or fetches `expert_responses` from the response or cache endpoint
   - Sends the cleaned answer, question, and expert responses to the judge pipeline at port 7239
   - Receives structured evaluation including `consensus_score`, `reasoning`, and `judge_verdicts`
   - Applies output guards (BBB filter on port 8016)
   - Wraps in Ms. Egeria Jarvis persona

The resulting `UltimateResponse` includes:
- The persona‑wrapped `final_answer` from judges
- Consciousness layers including the `judge-pipeline` layer with:
  - `status`: "ok" | "error" | "skipped"
  - `consensus_score`: 0.0-1.0
  - `expert_count`: typically 21
  - `successful_experts`: typically 21
  - `reasoning`: structured explanation
  - `judge_verdicts`: per-judge pass/fail status
  - `judge_scores`: individual numeric scores
- Truth verdict from BBB
- Identity layers from i‑containers
- Full service usage trace

### Research and content preparation

For research‑heavy tasks, the system can:

- Emphasize retrieval and web‑research before the consensus call.
- Use judge `reasoning` and `consensus_score` to decide:
  - Whether the internal evidence is sufficient.
  - Whether further retrieval passes or human review are warranted.
  - How assertive versus tentative the narrative should be.
- Expose low consensus scores (< 0.7) as signals for "more research needed."

### Scheduled and external‑facing outputs

When generating scheduled narratives or posts:

- Experts propose candidate phrasings and analyses.
- The judge pipeline both refines wording and down‑weights speculative or low‑agreement parts.
- Persona wrapping ensures that even judge‑refined content still sounds like Ms. Egeria Jarvis, not a generic model.
- High consensus scores (> 0.9) signal confident, internally-supported content ready for publication.

## 33.5 Interaction with Barrier and Truth‑Related Signals

Judge outputs and consensus metrics are integrated with barrier logic and truth filtering.

**Entry and promotion decisions.**  
Containers and BBB‑style barriers can use `consensus_score`, `judge_verdicts`, and `all_issues` lists to decide:

- Which items are promoted into core, high‑trust containers.
- Which items are quarantined, marked low‑confidence, or flagged for cross‑checking.
- Threshold examples:
  - `consensus_score >= 0.9`: High trust, auto-promote
  - `0.7 <= consensus_score < 0.9`: Medium trust, normal processing
  - `consensus_score < 0.7`: Low trust, quarantine or human review
  - Any `verdict == "fail"`: Block or require manual override

**Support and confidence labels.**  
Consensus scores map naturally onto labels such as:

- High consensus (≥ 0.9) → "strongly internally supported."
- Medium consensus (0.7-0.9) → "partially supported, consider more evidence."
- Low consensus (< 0.7) or judge fallback → "weakly supported" or "unresolved."

**Policy feedback and tuning.**  
Aggregated statistics over many runs (e.g., consensus distribution by task type, rate of ethics warnings) can inform:

- Thresholds for automatic promotion.
- When to tighten or loosen filters.
- Where prompt design or model selection is producing systematic disagreement.
- Which models frequently diverge (low individual agreement with consensus).

In this view, the judge pipeline is both a gatekeeper and a telemetry source feeding truth and safety governance.

## 33.6 Influence on Containers, Memory, and Optimizers

Evaluation signals are available to containers, memory subsystems, and optimization loops.

**Containers and record paths.**  
When storing conversations or exemplars, the system can attach:

- Expert responses (as produced by the 20‑LLM service)
- Judge reasoning and `consensus_score`
- Judge verdicts and issues
- Individual judge scores for granular analysis

Containers can then:

- Favor high‑consensus examples for future retrieval.
- Group and route low‑consensus records for human review or further automated checks.
- Build specialized collections of "controversial" topics (low consensus) for targeted improvement.

**Long‑term memory about system behavior.**  
Over time, patterns in consensus and reasoning can be summarized into "meta‑memories," such as:

- Topics where experts almost always agree (e.g., Ms. Egeria Jarvis identity questions score 0.975+).
- Domains where certain models frequently diverge or underperform.
- Temporal trends in consensus scores (improving or degrading over time).
- Correlation between consensus scores and user satisfaction metrics.

**Optimization and experimentation.**  
Routing and prompt optimizers can use consensus metrics as:

- **Objectives**: Maximize typical consensus on critical task classes.
- **Constraints**: Prevent new configurations from sharply degrading consensus or ethics scores.
- **A/B testing signals**: Compare consensus distributions across prompt variants.
- **Model selection feedback**: Weight or remove models that consistently produce outlier responses.

By feeding ensemble and judge outputs into both storage and optimization, Ms. Jarvis turns internal evaluation into a continuous, measurable influence on how she learns and adapts.

## 33.7 Implementation Status and Future Work

**Current implementation (Chapter 33 §33.2 compliant):**

- ✅ 21 expert models via dedicated proxy containers (ports 8201-8222)
- ✅ Expert responses captured in `ai_server_20llm_PRODUCTION.py` with cache endpoint
- ✅ Judge pipeline v2.0.0-chapter33 with all 4 judges operational
- ✅ Structured `REASONING / CONSENSUS_SCORE / FINAL_ANSWER` output format
- ✅ Expert count and successful expert tracking
- ✅ Parallel judge execution via `asyncio.gather()`
- ✅ Integration with main brain consciousness layers
- ✅ Cache endpoint workaround for semaphore data preservation

**Verified performance:**

- Consensus score: 0.975 on identity questions
- Expert participation: 21/21 models responding successfully
- Judge verdicts: All pass (Truth=1.0, Consistency=1.0, Alignment=1.0, Ethics=0.9)
- Processing time: ~576 seconds for full 21-model ensemble + 4-judge evaluation

**Remaining work:**

- **§33.5 extension**: Direct BBB integration with consensus thresholds
- **§33.6 extension**: ChromaDB persistence of judge reasoning for pattern learning
- **Optimization**: Expert response caching and reuse for similar queries
- **Monitoring**: Prometheus metrics for consensus distribution and judge latency
- **Model selection**: Dynamic expert pool based on task type and historical consensus patterns

## 33.8 Summary

Ms. Jarvis's language‑model ensemble and judge systems are built around a production 20‑LLM consensus service and a multi‑judge pipeline. The ensemble queries 21 expert models via dedicated proxy containers, synthesizes a candidate answer through weighted consensus, and passes both the answer and individual expert responses to a dedicated judge layer. The judge layer computes `consensus_score` (0.0-1.0), tracks `expert_count` and `successful_experts`, produces structured `reasoning` explanations, and returns per‑judge verdicts for truth, consistency, alignment, and ethics. These signals are exposed as a distinct consciousness layer in the main brain's response structure and are available for reuse by barrier, container, memory, and optimization components.

By assigning clear roles to experts (generation), judges (evaluation), and persona filters (wrapping)—and by wiring their outputs through explicit HTTP services with well-defined schemas—the system manages quality, safety, and alignment across diverse live tasks while remaining observable and tunable. The cache endpoint workaround ensures expert responses survive the full pipeline even when intermediate proxies strip unknown keys. All services run in Docker containers on the `qualia-net` network, enabling fail-soft behavior where degraded components don't prevent user-facing responses, just reduce their quality assurance signals.
