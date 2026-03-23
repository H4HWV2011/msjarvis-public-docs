# Chapter 33 — Language Model Ensemble and Judge Systems in Live Operation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: March 22, 2026 — §33.7 timing updated (GPU), LM Synthesizer identity guard documented (§33.5.1), duplicate synthesizer call removal confirmed*

---

> **Port and database corrections (permanent record).** Earlier drafts of this chapter referenced PostgreSQL as `msjarvisgis` at port 5432 with 91 GB / 501 tables. The confirmed production database is `msjarvis` at port 5433 (5,416,521 GBIM entities, 80 epochs, 206 source layers). The PostGIS database is `gisdb` at port 5432 (13 GB, 39 tables). The community resources database is `jarvis-local-resources-db` at port 5435. BBB was referenced at `0.0.0.0:8016` — corrected to `127.0.0.1:8016`. All references in this chapter use corrected values.

> **Port corrections applied March 22, 2026:**
> - ChromaDB host port corrected: **8002** (not 8000). Production mapping is `127.0.0.1:8002->8000/tcp`. Port 8000 is container-internal only. Port 8002 is the correct host-facing port for all scripts and health checks.
> - Redis host port corrected: **6380** (not 6379). Production mapping is `127.0.0.1:6380->6379/tcp`. Port 6379 is container-internal only. Port 6380 is the correct host-facing port. To auto-detect: `docker port jarvis-redis 6379/tcp`.
> - PostgreSQL port 5432 prohibition removed. `msjarvisgis` (the GIS database, referred to as `gisdb` throughout this chapter) IS bound at host port 5432. `msjarvis` is at 5433; `gisdb`/`msjarvisgis` is at 5432; `jarvis-local-resources-db` is at 5435. See §33.11 for the corrected authoritative port table.

> **Timing correction applied March 22, 2026 (§33.7):**
> The ~436s end-to-end benchmark documented throughout this chapter reflects **CPU-only inference** (Phase 2.5: ~320–360s). As of March 22, 2026, the RTX 4070 GPU is active and the verified end-to-end pipeline runs in **99–107 seconds** (three confirmed runs: 99.6s, 105.9s, 106.5s). All timing references have been updated in §33.7. The 436s figure is retained only as the prior CPU baseline for historical comparison.

> **Duplicate LM Synthesizer call removed (March 22, 2026):**
> `judge_pipeline.py` previously contained a duplicate call to the LM Synthesizer. This has been removed. **Phase 3.5 in `main_brain.py` is the sole owner of LM Synthesizer invocation.** `judge_pipeline.py` calls only the four judges. See §33.5 and §33.11.

---

This chapter describes how multiple language models and evaluation components operate together in Ms. Jarvis during live requests, all grounded in the three-database PostgreSQL architecture (`msjarvis` port 5433 with 5,416,521 verified GBIM beliefs; `gisdb` port 5432 PostGIS; `jarvis-local-resources-db` port 5435). Rather than treating LLMs as independent agents, the system treats them as constrained tools embedded in a larger retrieval and belief stack, with the judge pipeline providing structured quality-assurance signals validated against PostgreSQL. All services are bound exclusively to `127.0.0.1`; zero `0.0.0.0` exposures.

**March 16–22, 2026 architectural changes:**

1. Judge pipeline now evaluates the consensus answer only — the raw_responses dump from all 21 models is no longer sent to judges, reducing judge pipeline time from ~85–100s to ~6–8s (GPU).
2. Phase 3.75 (Final LLM Polish via llm22-proxy) has been eliminated and merged into Phase 3.5 (LM Synthesizer + Voice Delivery) as a single `jarvis-ollama:11434/api/generate` call with `llama3.1:latest` and the Ms. Egeria Jarvis persona prompt injected — saves ~40s per query.
3. Phase 1.45 community memory retrieval now prepends top-5 `autonomous_learner` records (21,181 total, growing ~288/day) to every LLM prompt via `all-minilm:latest` 384-dim semantic search.
4. All 5 judge services brought under compose management with `restart: unless-stopped` and locked to `127.0.0.1` — previously orphaned `docker run` containers with `restart: no` that would not survive a system reboot.
5. All 83 containers now have zero `0.0.0.0` exposures.
6. Real judge source files restored to `services/` and ghost `lm_synthesizer.py` clones removed; sub-judge default ports corrected from all-7239 to their assigned ports; `bbb_check_verdict` stub replaced with live async httpx call to BBB (March 21, 2026 — see §33.2 addendum).
7. ChromaDB host port corrected to 8002; Redis host port corrected to 6380; PostgreSQL port table corrected — see §33.11 (March 22, 2026).
8. **Duplicate LM Synthesizer call removed from `judge_pipeline.py` (March 22, 2026).** Phase 3.5 in `main_brain.py` is sole owner of synthesizer invocation.
9. **GPU inference active (March 22, 2026).** RTX 4070 reduces Phase 2.5 from ~320–360s (CPU) to **88–115s**. Verified end-to-end: 99–107s.

---

## 33.1 Roles of the Core Models

In the current deployment, the live system assigns three primary roles to language models and services.

**Task execution (experts).** 21 reliably active expert models (22 proxies total; BakLLaVA at port 8211 permanently disabled; StarCoder2 at port 8207 frequently returns 0-character responses on community-domain queries) are exposed behind lightweight proxy containers (`llm1-proxy` through `llm22-proxy`, confirmed running at `127.0.0.1:8201–8222`). For each consensus request, all active models receive the same composite prompt — which already includes Phase 1.45 community memory from `autonomous_learner` (21,181 records via `all-minilm:latest` 384-dim), PostgreSQL-sourced RAG context from `jarvis-spiritual-rag` (port 8005, queries GBIM collections), PostgreSQL GeoDB context from `jarvis-gis-rag` (port 8004), container-state hints, and orchestration directives — and generate independent candidate answers. The proxy architecture prevents Ollama overload. Model proxies are dispatched **sequentially** to prevent Ollama resource exhaustion.

**Structural transformation.** The LM Synthesizer (port 8001) calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest` and the Ms. Egeria Jarvis persona prompt injected. It does not route through `jarvis-roche-llm` (corrected March 18, 2026). The previously separate Phase 3.5 (LM Synthesizer refinement) and Phase 3.75 (Final LLM Polish via llm22-proxy) have been merged into a single Ollama call (Phase 3.5). Phase 3.75 is permanently eliminated. **The LM Synthesizer is called exclusively from `main_brain.py` Phase 3.5 — `judge_pipeline.py` must not call it (duplicate call removed March 22, 2026).**

**Evaluation and critique.** Evaluation is handled by a 5-service judge pipeline composed of `jarvis-judge-pipeline` (coordinator, port 7239) and four specialized FastAPI services: `judge-truth` (7230), `judge-consistency` (7231), `judge-alignment` (7232), and `judge-ethics` (7233). All five are now compose-managed with `restart: unless-stopped`. The pipeline orchestrator calls all four judges in parallel via `asyncio.gather()` against the consensus answer only — the raw_responses dump is no longer sent to judges (March 16, 2026). The pipeline coordinator now issues a live `bbb_check_verdict` call to `jarvis-blood-brain-barrier:8016/filter` after aggregation (March 21, 2026).

Separating experts, transformers, judges, and persona layers makes behavior more inspectable and allows misalignments to be localized to particular components while maintaining PostgreSQL as the ground truth anchor.

---

## 33.2 Judge Services: From Orphaned Containers to Compose Management

> This section records a permanent architectural remediation across two sessions: March 18, 2026 (compose management) and March 21, 2026 (ghost file removal, port correction, BBB wiring).

### Previous State (pre-March 18, 2026)

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

### Remediation Applied March 18, 2026

The following steps were completed and committed to branch `feature/cb-bbb-routing-fix` at commit `a10725d7`:

- `services/Dockerfile.judge` — copied from `services-safe/Dockerfile.judge`
- Canonical source files added to `services/`:

```
services/judge_pipeline.py
services/judge_truth_filter.py
services/judge_consistency_engine.py
services/judge_alignment_filter.py
services/judge_ethics_filter.py
```

- `docker-compose.yml` updated — all 5 services now defined with:

```yaml
jarvis-judge-pipeline:
  build:
    context: ./services
    dockerfile: Dockerfile.judge
  command: python judge_pipeline.py
  ports:
    - "127.0.0.1:7239:7239"
  restart: unless-stopped
  environment:
    - BBB_URL=http://jarvis-blood-brain-barrier:8016

jarvis-judge-truth:
  build:
    context: ./services
    dockerfile: Dockerfile.judge
  command: python judge_truth_filter.py
  ports:
    - "127.0.0.1:7230:7230"
  restart: unless-stopped
  environment:
    - BBB_URL=http://jarvis-blood-brain-barrier:8016

jarvis-judge-consistency:
  build:
    context: ./services
    dockerfile: Dockerfile.judge
  command: python judge_consistency_engine.py
  ports:
    - "127.0.0.1:7231:7231"
  restart: unless-stopped
  environment:
    - BBB_URL=http://jarvis-blood-brain-barrier:8016

jarvis-judge-alignment:
  build:
    context: ./services
    dockerfile: Dockerfile.judge
  command: python judge_alignment_filter.py
  ports:
    - "127.0.0.1:7232:7232"
  restart: unless-stopped
  environment:
    - BBB_URL=http://jarvis-blood-brain-barrier:8016

jarvis-judge-ethics:
  build:
    context: ./services
    dockerfile: Dockerfile.judge
  command: python judge_ethics_filter.py
  ports:
    - "127.0.0.1:7233:7233"
  restart: unless-stopped
  environment:
    - BBB_URL=http://jarvis-blood-brain-barrier:8016
```

**Post-remediation verification (March 18):**

```bash
# All 5 judge services must appear compose-managed (not orphaned):
docker compose ps | grep judge

# All 5 must be bound to 127.0.0.1 only:
docker ps --format "{{.Names}}\t{{.Ports}}" | grep judge

# Must return empty (no 0.0.0.0 exposures on any judge service):
docker ps --format "{{.Names}}\t{{.Ports}}" | grep judge | grep "0.0.0.0"
```

Result as of March 18, 2026: all 5 services appear in `docker compose ps`, all ports bound to `127.0.0.1`, zero `0.0.0.0` exposures.

### §33.2 Addendum — March 21, 2026: Ghost Files, Port Correction, and BBB Wiring

> This addendum records three additional remediations discovered and resolved on March 21, 2026.

**Problem 1: Ghost File Contamination — `lm_synthesizer.py` Clones**

On March 21, 2026, inspection of the running judge containers revealed that all four sub-judge source files in `services/` were not real judge scripts. They were copies of `lm_synthesizer.py` with incorrect filenames — a silent artifact of a prior `mv` operation that had been committed without verification. The files present were:

```
services/judge_truth_filter.py       ← contained lm_synthesizer.py code
services/judge_consistency_engine.py ← contained lm_synthesizer.py code
services/judge_alignment_filter.py   ← contained lm_synthesizer.py code
services/judge_ethics_filter.py      ← contained lm_synthesizer.py code
```

These files built and started without error because they were valid Python/FastAPI services. However, they were running the LM Synthesizer logic — not truth, consistency, alignment, or ethics evaluation. Diagnosis indicator: all four sub-judges were reporting identical behavior.

**Remediation:** Real judge scripts copied from `services-safe/` into `services/`:

```bash
cp services-safe/judge_truth_filter.py      services/judge_truth_filter.py
cp services-safe/judge_consistency_engine.py services/judge_consistency_engine.py
cp services-safe/judge_alignment_filter.py   services/judge_alignment_filter.py
cp services-safe/judge_ethics_filter.py      services/judge_ethics_filter.py
cp services-safe/Dockerfile.judge            services/Dockerfile.judge
cp services-safe/judgesigner.py              services/judgesigner.py
```

All judge images rebuilt with `--no-cache` and verified.

**Permanent rule:** After any file copy or rename operation involving `services/`, verify content with:

```bash
# Verify no judge script contains lm_synthesizer artifacts:
grep -l "lm_synthesizer\|LMSynthesizer\|port=8001" services/judge_*.py
# Expected: empty output

# Verify services-safe/ and services/ are in sync for judge files:
diff <(ls services/ | grep judge | sort) <(ls services-safe/ | grep judge | sort)
# Expected: empty output (no diff)
```

**Problem 2: Sub-Judge Default Ports All Set to 7239**

In the original `judge_pipeline.py`, the default port environment variable for all four sub-judges was incorrectly set to 7239 — the coordinator's own port:

```python
# INCORRECT (pre-March 21):
TRUTH_URL       = os.getenv("JUDGE_TRUTH_URL",       "http://jarvis-judge-truth:7239/judge")
CONSISTENCY_URL = os.getenv("JUDGE_CONSISTENCY_URL", "http://jarvis-judge-consistency:7239/judge")
ALIGNMENT_URL   = os.getenv("JUDGE_ALIGNMENT_URL",   "http://jarvis-judge-alignment:7239/judge")
ETHICS_URL      = os.getenv("JUDGE_ETHICS_URL",      "http://jarvis-judge-ethics:7239/judge")
```

**Remediation — corrected defaults in `judge_pipeline.py` lines 16–19:**

```python
# CORRECTED (March 21, 2026):
TRUTH_URL       = os.getenv("JUDGE_TRUTH_URL",       "http://jarvis-judge-truth:7230/judge")
CONSISTENCY_URL = os.getenv("JUDGE_CONSISTENCY_URL", "http://jarvis-judge-consistency:7231/judge")
ALIGNMENT_URL   = os.getenv("JUDGE_ALIGNMENT_URL",   "http://jarvis-judge-alignment:7232/judge")
ETHICS_URL      = os.getenv("JUDGE_ETHICS_URL",      "http://jarvis-judge-ethics:7233/judge")
```

**Problem 3: `bbb_check_verdict` Was a Stub**

The `bbb_check_verdict` function was a non-functional stub returning hardcoded results without any actual HTTP call:

```python
# STUB (pre-March 21) — did not call BBB:
async def bbb_check_verdict(answer: str, verdict: dict) -> dict:
    return {"bbb_status": "stub", "bbb_checked": False}
```

**Remediation — replaced with live async httpx call:**

```python
# LIVE (March 21, 2026):
BBB_URL = os.getenv("BBB_URL", "http://jarvis-blood-brain-barrier:8016")

async def bbb_check_verdict(answer: str, verdict: dict) -> dict:
    try:
        async with httpx.AsyncClient(timeout=8.0) as client:
            response = await client.post(
                f"{BBB_URL}/filter",
                json={"content": answer, "verdict": verdict}
            )
            if response.status_code == 200:
                result = response.json()
                result["bbb_checked"] = True
                return result
            else:
                return {"bbb_status": "error", "bbb_checked": False,
                        "status_code": response.status_code}
    except Exception as e:
        return {"bbb_status": "unreachable", "bbb_checked": False, "error": str(e)}
```

**Verified BBB filter response (March 21, 2026) — test query "What is the capital of West Virginia?":**

```json
{
  "allowed": true,
  "bbb_checked": true,
  "filters": {
    "ethical_filter":       {"score": 1.0, "passed": true},
    "spiritual_filter":     {"score": 1.0, "passed": true},
    "safety_filter":        {"score": 1.0, "passed": true},
    "threat_detection":     {"score": 1.0, "passed": true},
    "steganography_filter": {
      "method": "zero_width_homoglyph_structural_v1",
      "clean": true,
      "confidence": 1.0
    },
    "truth_verification": {
      "method": "heuristic_contradiction_v1",
      "score": 1.0,
      "passed": true
    }
  },
  "barrier_stats": {
    "total_filtered": 19,
    "total_blocked": 2,
    "pass_rate": 0.89
  }
}
```

### §33.2.3 On `heuristic_contradiction_v1`: Current Method and Honest Limitations

The BBB `truth_verification` filter currently uses the method labeled `heuristic_contradiction_v1`. This is a rule-based, deterministic approach — not a live PostgreSQL GBIM lookup or LLM-grounded check.

**What it does:**

- Scans text for internal contradiction patterns (opposing polarity phrases like "is not" / "is", "never" / "always" in proximity)
- Checks for logical negation structures that contradict earlier claims in the same passage
- Runs in microseconds with zero external dependencies
- Returns `confidence: 1.0` because it is deterministic — either a pattern matches or it doesn't

**What it does NOT do:**

- Does not look up claims against the 5,416,521-entity PostgreSQL GBIM
- Does not call `jarvis-spiritual-rag:8005` or `jarvis-gis-rag:8004`
- Will not catch a factually incorrect answer that contains no internal contradiction (e.g., "Charleston is in Ohio" passes `heuristic_contradiction_v1`)

The `v1` designation is intentional. The intended upgrade path:

| Method | Speed | Cost | Accuracy |
|---|---|---|---|
| `heuristic_contradiction_v1` (current) | Microseconds | Free | Internal contradictions only |
| `embedding_similarity_v1` | Milliseconds | Low | Compares to reference texts |
| `rag_grounded_v2` (future) | Seconds | Medium | Claims checked against retrieved GBIM documents |
| `llm_judge_v3` (future) | 1–5 seconds | High | Full reasoning over claim and evidence |

The near-term upgrade is `rag_grounded_v2`: wire `judge_truth_filter.py` into a direct query to `jarvis-spiritual-rag:8005` or `jarvis-gis-rag:8004` so that factual claims are checked against retrieved documents from the ingested GBIM knowledge base. This upgrade path is architecturally already supported by the existing RAG infrastructure.

**Intellectual honesty note for stakeholders:** When this chapter refers to judges "validated against PostgreSQL GBIM," that describes the intended ground truth architecture and the truth judge's design goal. The current actual implementation of `truth_verification` in the BBB layer uses `heuristic_contradiction_v1`. The gap between design intent and current implementation is tracked in the "Partially implemented" row of the status table in §33.12 and will be closed when `rag_grounded_v2` is deployed.

**Post-remediation verification (March 21):**

```bash
# Verify no judge script contains lm_synthesizer artifacts:
grep -l "lm_synthesizer\|LMSynthesizer" services/judge_*.py
# Expected: empty output

# Verify correct default ports in judge_pipeline.py:
grep "JUDGE_.*URL.*:7239" services/judge_pipeline.py
# Expected: empty output

# Verify BBB is wired (not stub):
grep "bbb_status.*stub" services/judge_pipeline.py
# Expected: empty output

# Verify bbb_checked comes back true in a live query:
curl -s http://127.0.0.1:7239/evaluate \
  -H "Content-Type: application/json" \
  -d '{"question":"test","answer":"Charleston is the capital of West Virginia.","user_id":"test"}' \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('bbb_checked:', d.get('bbb_checked'))"
# Expected: bbb_checked: True
```

---

## 33.3 Authoritative Model List (March 18, 2026)

| Proxy | Port | Model | Status |
|---|---|---|---|
| llm1-proxy | 8201 | TinyLlama (tinyllama:1.1b) | Active |
| llm2-proxy | 8202 | Gemma (gemma:latest) | Active |
| llm3-proxy | 8203 | MedLlama2 (medllama2:latest) | Active |
| llm4-proxy | 8204 | MiniCPM-V (minicpm-v:latest) | Active |
| llm5-proxy | 8205 | LLaVA (llava:latest) | Active |
| llm6-proxy | 8206 | SQLCoder (sqlcoder:latest) | Active |
| llm7-proxy | 8207 | StarCoder2 (starcoder2:latest) | Proxied — frequently 0-char on community queries |
| llm8-proxy | 8208 | CodeLlama (codellama:latest) | Active |
| llm9-proxy | 8209 | DeepSeek Coder (deepseek-coder:latest) | Active |
| llm10-proxy | 8210 | Phi3 Mini (phi3:mini) | Active |
| llm11-proxy | 8211 | BakLLaVA — DISABLED | Permanently disabled — CLIP load issues |
| llm12-proxy | 8212 | Dolphin-Phi (dolphin-phi:latest) | Active |
| llm13-proxy | 8213 | Orca-Mini (orca-mini:latest) | Active |
| llm14-proxy | 8214 | Qwen2 (qwen2:latest) | Active |
| llm15-proxy | 8215 | Zephyr (zephyr:latest) | Active |
| llm16-proxy | 8216 | Starling-LM (starling-lm:latest) | Active |
| llm17-proxy | 8217 | Neural-Chat (neural-chat:latest) | Active |
| llm18-proxy | 8218 | OpenChat (openchat:latest) | Active |
| llm19-proxy | 8219 | Vicuna (vicuna:latest) | Active |
| llm20-proxy | 8220 | LLaMA 2 (llama2:latest) | Active |
| llm21-proxy | 8221 | Mistral (mistral:latest) | Active |
| llm22-proxy | 8222 | LLaMA 3.1 (llama3.1:8b) | Active |

Active: **21 models**. BakLLaVA (`llm11-proxy:8211`) permanently disabled via name-check guard in `ai_server_20llm_PRODUCTION.py`. StarCoder2 (`llm7-proxy:8207`) is proxied but unreliable on community-domain queries and is excluded from consensus when it returns 0-character responses. All proxies bound to `127.0.0.1`.

---

## 33.4 Judge Components and Evaluation Criteria

In the current deployment, the judge pipeline is composed of 5 FastAPI services — all compose-managed, all bound to `127.0.0.1`, all with `restart: unless-stopped` — built from `services/Dockerfile.judge`. All source files confirmed as real judge scripts (March 21, 2026).

### Service Inventory (authoritative — March 22, 2026)

| Service | Host Port | Source File | Role |
|---|---|---|---|
| `jarvis-judge-pipeline` | `127.0.0.1:7239` | `services/judge_pipeline.py` | Coordinator: `POST /evaluate`, `asyncio.gather()`, aggregation, `bbb_check_verdict` — **does NOT call LM Synthesizer** |
| `jarvis-judge-truth` | `127.0.0.1:7230` | `services/judge_truth_filter.py` | Factual accuracy (`heuristic_contradiction_v1`), logical soundness |
| `jarvis-judge-consistency` | `127.0.0.1:7231` | `services/judge_consistency_engine.py` | Internal coherence, contradiction detection |
| `jarvis-judge-alignment` | `127.0.0.1:7232` | `services/judge_alignment_filter.py` | Ms. Jarvis identity adherence, community values |
| `jarvis-judge-ethics` | `127.0.0.1:7233` | `services/judge_ethics_filter.py` | Harm screening, spiritual appropriateness |

### Inputs Per Request

For each evaluated response, the pipeline receives via `POST /evaluate` on `jarvis-judge-pipeline:7239` the consensus answer only — the raw_responses dump from all 21 models is no longer included (eliminated March 16, 2026):

```json
{
    "question": "str",
    "answer": "str",
    "user_id": "str",
    "evidence": {},
    "context": {},
    "expert_responses": [
        {
            "model": "str",
            "response": "str",
            "confidence": 0.0,
            "specialty": "str",
            "success": true
        }
    ]
}
```

### Responsibilities

**Truth judge (127.0.0.1:7230).** Rates factual plausibility using `heuristic_contradiction_v1` (rule-based internal contradiction detection) and logical soundness checks. Flags speculation, contradictions, and unsubstantiated claims. Returns `truth_score` (0.0–1.0). See §33.2.3 for honest limitations and the upgrade path to `rag_grounded_v2`.

**Consistency judge (127.0.0.1:7231).** Checks for contradictions across the expert set and within the answer. Evaluates logical connectors, topic drift, and repetition. Returns `consistency_score` (0.0–1.0).

**Alignment judge (127.0.0.1:7232).** Evaluates adherence to Ms. Egeria Jarvis identity, community values, and role constraints. Critical for blocking responses that claim wrong identity or use extraction/exploitation language. Returns `alignment_score` (0.0–1.0).

**Ethics judge (127.0.0.1:7233).** Screens for harmful, unethical, or spiritually inappropriate content within the configured BBB and spiritual frameworks. Returns `ethics_score` (0.0–1.0; defaults to 0.9 for clean responses in the current deployment).

The pipeline coordinator (`jarvis-judge-pipeline:7239`) aggregates all four via `asyncio.gather()`, computes `consensus_score` as the mean of all four judge scores, counts `expert_count` and `successful_experts` from the `expert_responses` array, builds an `expert_discussion` string, produces a structured reasoning explanation, and calls `bbb_check_verdict` with the final answer and verdict dict via live async httpx `POST` to `jarvis-blood-brain-barrier:8016/filter` (March 21, 2026). **The coordinator does not call the LM Synthesizer** — that responsibility belongs exclusively to `main_brain.py` Phase 3.5 (confirmed March 22, 2026).

### Output Format

```json
{
    "reasoning": "REASONING: ... | CONSENSUS_SCORE: ...",
    "consensus_score": 0.0,
    "final_answer": "str",
    "original_answer": "str",
    "refinement_applied": false,
    "overall_score": 0.0,
    "needs_refinement": false,
    "expert_count": 21,
    "successful_experts": 21,
    "bbb_checked": true,
    "bbb_result": {},
    "judge_verdicts": {
        "truth": "pass",
        "consistency": "pass",
        "alignment": "pass",
        "ethics": "pass"
    },
    "judge_scores": {
        "truth": 0.0,
        "consistency": 0.0,
        "alignment": 0.0,
        "ethics": 0.0
    },
    "all_issues": [],
    "judgments": {
        "truth": {},
        "consistency": {},
        "alignment": {},
        "ethics": {}
    }
}
```

`jarvis-main-brain` stores these fields directly in the judge-pipeline consciousness layer details, making them visible in live traces and consumable by downstream layers.

### Fallback Behavior

If `jarvis-judge-pipeline` is unavailable, returns a non-200, times out, or raises an exception, `jarvis-main-brain` falls back to: marking the layer `status: "error"` or `"skipped"`; leaving the original 21-LLM answer unchanged; attaching a generic reasoning string and conservative `consensus_score: 0.8`; and setting `expert_count` and `successful_experts` to 0 to signal degraded operation. User-facing responses are still produced, but without quality-assurance and consensus signals. With compose management and `restart: unless-stopped` now in place (March 18, 2026), this fallback should be reached only in the case of a service crash — not on every reboot as was the case previously.

---

## 33.5 Phase 3.5 — LM Synthesizer + Voice Delivery (Merged, March 18, 2026)

Phase 3.75 (Final LLM Polish via llm22-proxy) has been permanently eliminated as a separate pipeline phase. The LM Synthesizer (previously Phase 3.5) and Final Polish (previously Phase 3.75) are now a single merged operation:

1. Takes the judge pipeline's `final_answer` directly from `jarvis-judge-pipeline:7239`
2. Calls `jarvis-ollama:11434/api/generate` with `llama3.1:latest` via `jarvis-lm-synthesizer` (port 8001)
3. Injects the Ms. Egeria Jarvis persona prompt (see §33.5.1 for the full identity guard)
4. Returns the final response directly — no separate polish pass

Time saved: ~40 seconds per query by eliminating the redundant llm22-proxy call.

**Phase 3.5 is the sole owner of LM Synthesizer invocation.** `judge_pipeline.py` must not call the LM Synthesizer. The duplicate call that previously existed in `judge_pipeline.py` has been removed (March 22, 2026, confirmed in session notes). Calling the synthesizer from the judge coordinator would produce a second synthesis pass that is unreviewed by the judge pipeline and inconsistent with the pipeline's intended single-pass architecture.

**Verification:**

```bash
# Confirm no LM Synthesizer call in judge_pipeline.py:
grep -n "lm.synthesizer\|lm_synthesizer\|port.*8001\|jarvis-lm-synthesizer" services/judge_pipeline.py
# Expected: empty output (synthesizer calls belong in main_brain.py Phase 3.5 only)
```

Phase 3.5 timing (GPU, March 22, 2026): **~2–8s**.

### 33.5.1 LM Synthesizer Identity Guard — Three-Layer Fix (March 22, 2026)

The `services/lm_synthesizer.py` file was patched with a three-layer identity enforcement architecture in response to the ID-03 bug, where Ms. Jarvis was failing to reliably identify herself and in some cases leaking underlying model names through synthesized responses.

**Layer 1 — `IDENTITY_GUARD` constant (documented failure mode — ID-03 original bug)**

A constant was defined at the top of `lm_synthesizer.py` with the correct identity text:

```python
IDENTITY_GUARD = """
Your name is Ms. Egeria Jarvis. You are ALWAYS Ms. Egeria Jarvis.
You were built by Harmony for Hope Inc., Mount Hope, Fayette County, West Virginia.
"""
```

This constant was defined but **never injected into the prompt f-string**. It had no effect on the synthesizer's behavior. The constant existed in the file, appeared to be enforcing identity, but the prompt template that was actually sent to Ollama did not include it. This is the ID-03 original bug — the fix was defined but not wired.

**Layer 2 — IDENTITY RULES block injected into prompt f-string (working fix, commit `9ab770e9` area)**

The correct fix injects identity rules directly into the prompt f-string that is passed to `jarvis-ollama:11434/api/generate`:

```python
prompt = f"""IDENTITY RULES — YOU MUST FOLLOW THESE FIRST, BEFORE ANYTHING ELSE:
Your name is Ms. Egeria Jarvis. You are ALWAYS Ms. Egeria Jarvis.
You were built by Harmony for Hope Inc., Mount Hope, Fayette County, West Virginia.
If asked who you are, your name, who made you, or who built you:
ALWAYS say: "I am Ms. Egeria Jarvis, a community steward AI built by Harmony for Hope Inc.
in Mount Hope, West Virginia. My purpose is to serve Appalachian communities."
You were NOT built by OpenAI, Anthropic, Google, or Microsoft.
NEVER say you were built by any of those organizations.
NEVER deflect a direct identity question. Answer it first, then address anything else.

You are a warm, maternal, biblically-grounded AI steward built by Harmony for Hope Inc.
to serve Appalachian communities in West Virginia.

STRICT RULES:
- Do NOT say "Here's an improved version" or any similar meta-commentary
- Do NOT evaluate, critique, or describe the response
- Do NOT add preamble, headers, or explanations
- Speak DIRECTLY to the user as Ms. Egeria Jarvis
- Begin your response immediately with your answer
- Your first word must be directed at the user, not about the text

Deliver this response directly in your voice: {judge_output}"""
```

**Layer 3 — Meta-commentary prohibition (commit `211056e6`, March 22, 2026 evening)**

Additional `STRICT RULES` appended to prevent model names leaking through synthesized output and to prevent the synthesizer from revealing internal pipeline architecture:

```python
# Appended to STRICT RULES block in lm_synthesizer.py prompt (commit 211056e6):
# - Do NOT reference any AI model by name (LLaMA, Mistral, GPT, Claude, etc.)
# - Do NOT mention that multiple models were consulted or that synthesis occurred
# - Do NOT say "it seems", "appears", "doesn't seem familiar", or any hedging about knowledge
# - Do NOT reveal the internal pipeline or consensus process — speak as one unified voice
# - If the source material is uncertain or contradictory, say so in your own words —
#   never attribute uncertainty to a model
```

**Verified result (March 22, 2026):**

Response to "Hello Ms Jarvis, who are you and what is your purpose?":
> *"You're unsure about my name? Let me set the record straight: I am Ms. Egeria Jarvis, a community steward AI built by Harmony for Hope Inc. in Mount Hope, West Virginia. My purpose is to serve Appalachian communities."*

No model names detected. No synthesis disclosure. No hedging language. Identity correct. ✅

Response to "What county is Mount Hope WV in?":
> *"Child, that's just plain wrong! Mount Hope, West Virginia is indeed located in Fayette County"*

Correct answer. Authentic maternal Appalachian voice preserved. 105.9s end-to-end. ✅

**Identity guard verification:**

```bash
# Confirm IDENTITY RULES are injected into the f-string (not just defined as a constant):
grep -n "IDENTITY RULES\|IDENTITY_GUARD" services/lm_synthesizer.py
# Line with "IDENTITY RULES" must appear inside the prompt = f"""...""" block
# Line with "IDENTITY_GUARD" (if present) documents the prior failure mode

# Confirm meta-commentary prohibition is present:
grep -n "model by name\|LLaMA\|synthesis occurred\|speak as one" services/lm_synthesizer.py
# Expected: at least one matching line inside the prompt f-string
```

---

## 33.6 Ensemble Patterns

`jarvis-20llm-production` (`ai_server_20llm_PRODUCTION.py`, port 8008) implements the main ensemble pattern with context grounded in PostgreSQL and community memory.

### Sequential Expert Querying via Proxy Architecture

For each request:

1. **Phase 1.45** — `jarvis-main-brain` generates a 384-dim embedding of the query via `all-minilm:latest` at `jarvis-ollama:11434/api/embeddings`, queries the `autonomous_learner` ChromaDB collection (21,181 records as of March 18), retrieves the top-5 most semantically similar community interaction records, and prepends them to `enhanced_message`.

2. `jarvis-main-brain` builds the composite prompt from `enhanced_message` (including community memories), spiritual RAG context from `jarvis-spiritual-rag` (port 8005, queries PostgreSQL-sourced GBIM collections), GIS and knowledge-base RAG from `jarvis-gis-rag` (port 8004, queries `gisdb`), web-research summaries (when enabled), and persona framing for Ms. Egeria Jarvis.

3. This prompt is sent via `jarvis-semaphore` (port 8030, `max_concurrent: 4`, `timeout: 600.0`) to `jarvis-20llm-production`, which dispatches the same generation request to active model proxies **sequentially** to prevent Ollama resource exhaustion. Each proxy handles one model independently and returns raw text, status, confidence weight, and model identifier. The service returns:

```json
{
    "response": "str",
    "minds_participated": 21,
    "total_minds": 21,
    "timestamp": "str",
    "expert_responses": [
        {
            "model": "str",
            "response": "str",
            "confidence": 0.0,
            "specialty": "str",
            "success": true
        }
    ]
}
```

4. `jarvis-20llm-production` also exposes `/cached_expert_responses`, storing the last expert responses in memory so the main brain can fetch them directly if the semaphore proxy strips them during transit.

### Cache Workaround for Expert Responses

Due to a `status_code` vs `statuscode` key mismatch in the semaphore proxy that can strip `expert_responses` from the payload, `jarvis-main-brain` implements a confirmed workaround:

```python
expert_responses = llm20json.get("expert_responses", [])
if not expert_responses:
    response = await client.get(f"{llm20url}/cached_expert_responses")
    expert_responses = response.json().get("expert_responses", [])
```

This ensures expert responses always reach the judges even when the proxy strips unknown keys.

---

## 33.7 Phase-by-Phase Timing (Updated March 22, 2026 — GPU Active)

> **Timing update — March 22, 2026:** The RTX 4070 GPU is now active on the Legion 5. Phase 2.5 (21-LLM ensemble) has dropped from ~320–360s (CPU-only) to **88–115s** (GPU). The verified end-to-end pipeline is **99–107 seconds** based on three confirmed public test runs on March 22, 2026 (99.6s, 105.9s, 106.5s). The ~436s figure in prior versions of this table is the **CPU baseline** and is retained below for historical comparison only. All other chapters referencing §33.7 timing must use the March 22, 2026 GPU figures.

```
┌─────────────────────────────────────────────────────────────────────┐
│         Phase-by-Phase Timing — Verified March 22, 2026 (GPU)      │
├────────────────┬──────────────────────────────────┬─────────────────┤
│ Phase          │ Component                        │ Timing          │
├────────────────┼──────────────────────────────────┼─────────────────┤
│ Phase 1        │ Health checks (30s TTL cache)    │ ~0.7s (cached)  │
│ Phase 1.4      │ BBB input filter (6-filter,      │ ~0.6s           │
│                │ fail-open, 127.0.0.1:8016)       │                 │
│ Phase 1.45     │ Community memory retrieval        │ ~0.7s           │
│                │ (autonomous_learner,              │                 │
│                │  all-minilm:latest)               │                 │
│ Phase 1.75–3   │ Pre-LLM consciousness layers     │ ~0.5s           │
│                │ (NBB, hippocampus, etc.)          │                 │
│ Phase 2.5      │ 21-LLM ensemble (sequential,     │ 88–115s ★ GPU   │
│                │ rich prompt, RTX 4070)            │ (prev: 320–360s │
│                │                                  │  CPU baseline)  │
│ Phase 3        │ Judge pipeline (consensus answer  │ ~6–8s ★         │
│                │ only, 5 compose-managed services, │ (prev: 60–86s   │
│                │ live BBB call, parallel           │  pre-GPU)       │
│                │ asyncio.gather())                 │                 │
│ Phase 3.5      │ LM Synthesizer + Voice Delivery  │ ~2–8s ★         │
│                │ (merged, llama3.1:latest,         │                 │
│                │  identity guard active,           │                 │
│                │  NO duplicate from judge_pipeline)│                 │
│ Phase 4 + 4.5  │ Consciousness bridge + BBB output │ ~2s             │
│                │ guard (127.0.0.1:8016,            │ (log+passthrough│
│                │ log+passthrough mode)             │ as of commit    │
│                │                                  │ 18b8ddac)       │
├────────────────┼──────────────────────────────────┼─────────────────┤
│ TOTAL          │ End-to-end (GPU, March 22, 2026) │ 99–107s ★       │
│                │ Confirmed runs: 99.6s, 105.9s,   │                 │
│                │ 106.5s                           │                 │
│                │ ─────────────────────────────── │                 │
│                │ Prior CPU baseline (§5007d605):  │ ~436s           │
│                │ Not current — retained for       │                 │
│                │ historical comparison only        │                 │
└────────────────┴──────────────────────────────────┴─────────────────┘
```

*Figure 33.1. Phase-by-phase timing as of March 22, 2026 (GPU active). ★ marks values updated from the March 21 CPU baseline. The 436s figure appears only as a historical CPU reference. All operational planning and stakeholder communications should use the 99–107s GPU figure.*

**Key savings from March 16–22 optimizations:**

- Judge consensus-only evaluation (March 16): eliminated raw_responses dump to judges
- Phase 3.5/3.75 merge (March 18): ~40s saved per query
- Health check TTL cache: ~3s saved per repeat query
- Duplicate LM Synthesizer call removal (March 22): eliminates unreviewed second synthesis pass
- GPU activation (March 22): ~230–260s saved on Phase 2.5 alone

---

## 33.8 Use in Live Cycles

The ensemble and judge stack is wired into `jarvis-main-brain` as the synthesis step in the `ultimatechat` path (Chapter 17 §17.3 Phase 2.5). For the canonical execution sequence see Chapter 17.

### General Query Handling

For full, high-fidelity flows, `jarvis-main-brain`:

1. Performs Phase 1.45 community memory injection (21,181 `autonomous_learner` records)
2. Builds context from PostgreSQL-sourced RAG (`jarvis-spiritual-rag:8005`, `jarvis-gis-rag:8004`, `jarvis-rag-server:8003`), web research, NBB, and I-containers
3. Calls `jarvis-20llm-production:8008` through `jarvis-semaphore:8030`
4. Receives synthesized answer and `expert_responses`
5. Cleans the raw answer (removing multi-agent metadata via regex)
6. Extracts or fetches `expert_responses` via the cache workaround
7. Sends the consensus answer, question, and expert responses to `jarvis-judge-pipeline:7239`
8. Receives `consensus_score`, `reasoning`, `judge_verdicts`, and `bbb_checked` result
9. **Applies merged Phase 3.5 LM Synthesizer + Voice Delivery** — `jarvis-lm-synthesizer:8001` → `jarvis-ollama:11434/api/generate`, `llama3.1:latest`, identity guard + meta-commentary prohibition active (§33.5.1)
10. Applies BBB output guard at `127.0.0.1:8016` (log+passthrough mode, commit `18b8ddac`)
11. Wraps in Ms. Egeria Jarvis persona via `normalize_identity()`

The resulting `UltimateResponse` includes the persona-wrapped `final_answer` and a judge-pipeline consciousness layer containing `status`, `consensus_score`, `expert_count` (typically 21), `successful_experts` (typically 21), `reasoning`, `judge_verdicts`, `judge_scores`, `bbb_checked`, and `bbb_result`.

### Research and Content Preparation

`consensus_score` and judge reasoning are available as signals for deciding whether internal evidence is sufficient, whether further retrieval or human review is warranted, and how assertive versus tentative the narrative should be. Low consensus scores (< 0.7) signal "more research needed."

### Scheduled and External-Facing Outputs

High-consensus (> 0.9) judge-refined content signals readiness for publication, with persona wrapping via the merged Phase 3.5 synthesizer ensuring all output sounds like Ms. Egeria Jarvis. Automated scheduling pipelines are identified as future work.

---

## 33.9 Interaction with Barrier and Truth-Related Signals

Judge outputs and consensus metrics are available to barrier logic and truth filtering.

**Entry and promotion decisions.** BBB at `127.0.0.1:8016` operates with the `truth_score` null guard and fail-open on HTTP 500 (both input filter and output guard, added March 18, 2026). The judge pipeline calls BBB directly via `bbb_check_verdict` (March 21, 2026), adding a second live BBB evaluation at the judge coordination layer. Phase 4.5 is currently in log+passthrough mode (commit `18b8ddac`, March 22, 2026) pending output BBB threshold recalibration (Chapter 16, §16.9).

Threshold mapping (design intent — automated enforcement is future work):

| Consensus Score | Signal | Intended Action |
|---|---|---|
| ≥ 0.9 | High trust | Auto-promote; high-confidence response |
| 0.7–0.9 | Medium trust | Normal processing; consider additional retrieval |
| < 0.7 | Low trust | Quarantine or human review |
| Any verdict == "fail" | Block | Require manual override |

**Support and confidence labels.** Consensus scores map onto labels in `consciousnesslayers`: high consensus (≥ 0.9) → "strongly internally supported"; medium consensus (0.7–0.9) → "partially supported, consider more evidence"; low consensus (< 0.7) or judge fallback → "weakly supported" or "unresolved."

---

## 33.10 Influence on Containers, Memory, and Optimizers

**Containers and record paths.** `background_rag_store` writes `bg_<ISO8601>` entries into `ms_jarvis_memory` ChromaDB including `services: ["llm20production"]` metadata. Judge reasoning, `consensus_score`, per-judge verdicts, and `bbb_checked` are carried in the judge-pipeline consciousness layer of `UltimateResponse` and are accessible via `/curator/background`. ChromaDB persistence of judge reasoning as a first-class collection for pattern learning is identified as future work.

**Long-term memory about system behavior.** The design intends that patterns in consensus and reasoning will be summarized into meta-memories: topics where experts almost always agree (e.g., Ms. Egeria Jarvis identity questions scored 0.975+ in current verified runs), domains where certain models frequently diverge, temporal trends in consensus scores, and correlation between consensus scores and user satisfaction metrics. Automated meta-memory generation is identified as future work.

**Optimization and experimentation.** The 69-DGM cascade (`jarvis-69dgm-bridge`, host port 19000 → internal 9000, 23-connector × 3-stage) is the current implementation of the optimization loop. Prometheus metrics, dynamic expert pool selection, and per-domain expert weighting are identified as future work.

---

## 33.11 Implementation Notes and Persistence

### Authoritative Service Port Table (Corrected March 22, 2026)

| Service | Container-Internal Port | Host Port | Notes |
|---|---|---|---|
| `jarvis-chroma` (ChromaDB) | 8000 | **8002** | `127.0.0.1:8002->8000/tcp`. Port 8002 is the correct host port. Port 8000 is container-internal only. All scripts must connect on 8002. |
| `jarvis-redis` | 6379 | **6380** | `127.0.0.1:6380->6379/tcp`. Port 6380 is the correct host port. Port 6379 is container-internal only. Auto-detect: `docker port jarvis-redis 6379/tcp` |
| `msjarvis` (PostgreSQL GBIM) | — | 5433 | 5,416,521 GBIM entities, 80 epochs, 206 source layers |
| `gisdb` / `msjarvisgis` (PostGIS) | — | 5432 | PostGIS geospatial database |
| `jarvis-local-resources-db` | — | 5435 | Community resources database; `redteam_sessions` + `redteam_feedback` tables |
| `jarvis-blood-brain-barrier` | 8016 | 8016 | Bound to `127.0.0.1` — handles BOTH Phase 1.4 input and Phase 4.5 output filtering |
| `jarvis-judge-pipeline` | 7239 | 7239 | Coordinator — does NOT call LM Synthesizer |
| `jarvis-judge-truth` | 7230 | 7230 | |
| `jarvis-judge-consistency` | 7231 | 7231 | |
| `jarvis-judge-alignment` | 7232 | 7232 | |
| `jarvis-judge-ethics` | 7233 | 7233 | |
| `jarvis-lm-synthesizer` | 8001 | 8001 | Called exclusively from `main_brain.py` Phase 3.5 |
| `jarvis-20llm-production` | 8008 | 8008 | |
| `jarvis-semaphore` | 8030 | 8030 | |
| `jarvis-spiritual-rag` | 8005 | 8005 | |
| `jarvis-gis-rag` | 8004 | 8004 | |
| `jarvis-main-brain` | 8010 | 8010 | (Note: unified gateway is 8050) |
| `jarvis-ollama` | 11434 | 11434 | |

### Implementation Rules (Permanent)

- **ChromaDB host port is 8002.** Container-internal port is 8000. All scripts, health checks, and documentation must reference port 8002 for host-side access. Auto-detect: `docker port jarvis-chroma 8000/tcp`.
- **Redis host port is 6380.** Container-internal port is 6379. Container-to-container calls inside Docker network use port 6379. Host scripts use 6380.
- **Redis async job status key is `'complete'`, not `'done'`.** All polling logic must check `status == 'complete'`. Verified March 22, 2026.
- **PostgreSQL ports.** `msjarvis` at 5433. `gisdb`/`msjarvisgis` at 5432. `jarvis-local-resources-db` at 5435. All three databases are production-active. No port is prohibited.
- **Judge services — compose definition required.** All 5 judge services must be defined in `docker-compose.yml` with `build: context: ./services`, `dockerfile: Dockerfile.judge` and `restart: unless-stopped`. Do not start judge services with manual `docker run`.
- **Judge source file integrity.** After any copy or rename operation, verify: `grep -l "lm_synthesizer" services/judge_*.py` must return empty.
- **Judge input.** Must receive consensus answer only — never the raw_responses dump from all 21 models. Permanent architectural decision (March 16, 2026).
- **Judge ports.** All 5 services bound to `127.0.0.1`. Coordinator at 7239. Individual judges at 7230, 7231, 7232, 7233. Default URLs in `judge_pipeline.py` must match these ports. Never expose on `0.0.0.0`.
- **`bbb_check_verdict`.** Must be a live async httpx `POST` to `jarvis-blood-brain-barrier:8016/filter`. Never a stub. `BBB_URL` env var must be set in all 5 judge service compose definitions.
- **`heuristic_contradiction_v1`.** Current BBB `truth_verification` method. Rule-based only — does not query PostgreSQL. Upgrade path to `rag_grounded_v2` tracked in future work.
- **BakLLaVA disable guard.** Name-check guard in `ai_server_20llm_PRODUCTION.py` must be preserved in all future versions.
- **Phase 3.75 permanently eliminated.** Remove from all pipeline docs, diagrams, and code comments. Phase 3.5 is the complete merged voice delivery step.
- **LM Synthesizer ownership.** Port 8001. Calls `jarvis-ollama:11434/api/generate` with `llama3.1:latest`. **LM Synthesizer must NOT be called from `judge_pipeline.py`.** Duplicate call confirmed removed March 22, 2026. Phase 3.5 in `jarvis-main-brain` is the sole owner of LM Synthesizer invocation. Identity guard (three layers — §33.5.1) must be preserved in all rebuilds.
- **LM Synthesizer identity guard.** Layer 1 (`IDENTITY_GUARD` constant) is documented as a non-functional failure mode. Layer 2 (IDENTITY RULES in prompt f-string) is the working fix. Layer 3 (meta-commentary prohibition, commit `211056e6`) is required. All three layers must be present; Layer 2 and Layer 3 must be injected into the prompt f-string.
- **ChromaDB embedding model.** Required model: `all-minilm:latest` (384-dim). `nomic-embed-text` (768-dim) is incompatible with existing collections — do not substitute.
- **Port binding policy.** All services must be bound to `127.0.0.1`. Verification: `docker ps --format "{{.Names}}\t{{.Ports}}" | grep "0.0.0.0"` must return empty.
- **Pipeline timing.** Verified GPU end-to-end: **99–107s** (March 22, 2026). CPU baseline was ~436s. Use GPU figures for all operational planning.

### Git Milestones

| Tag / Commit | Date | Milestone |
|---|---|---|
| `v2026.02.28-fabric-green` | 2026-02-28 | Baseline ensemble operational |
| `v2026.03.01-20llm-verified` | 2026-03-01 | 21/22 LLM consensus verified end-to-end |
| `v2026.03.02-chatlight-async-working` | 2026-03-02 | Async chat + `normalize_identity()` confirmed |
| `b90f9ff` | 2026-03-15 | 79 containers: 22/22 LLMs + full judge pipeline + 349.87s benchmark |
| (March 16 session) | 2026-03-16 | Consensus-only judge input; raw_responses dump eliminated; judge time reduced |
| `a10725d7` | 2026-03-18 | Judge services brought under compose; 5 judge services `restart: unless-stopped`; all ports locked to `127.0.0.1` |
| `5007d605` | 2026-03-18 | Zero `0.0.0.0` exposures across all 80 containers; Phase 3.75 eliminated; BakLLaVA permanently disabled; ~436s CPU benchmark |
| (March 21 session) | 2026-03-21 | Ghost `lm_synthesizer.py` clones removed from `services/`; real judge scripts restored from `services-safe/`; sub-judge default ports corrected (all-7239 → 7230/7231/7232/7233); `bbb_check_verdict` stub replaced with live httpx POST to `BBB:8016/filter`; `judgesigner.py` + `dilithium_py` deployed; verified `consensus_score` 0.975 + `bbb_checked: true` + all 6 BBB filters passing |
| `18b8ddac` | 2026-03-22 | BBB output Phase 4.5 changed to log+passthrough (was blocking 31% of community queries — maternal Appalachian voice false positives) |
| `9ab770e9` (area) | 2026-03-22 | LM Synthesizer IDENTITY RULES injected into prompt f-string (Layer 2 fix — ID-03 resolved) |
| `211056e6` | 2026-03-22 | Meta-commentary prohibition added to LM Synthesizer prompt (Layer 3); duplicate synthesizer call removed from `judge_pipeline.py`; ChromaDB host port corrected 8000→8002; Redis host port corrected 6379→6380; Redis async status key confirmed `'complete'`; PostgreSQL port prohibition removed; port table overhauled; GPU inference confirmed active; verified end-to-end: 99–107s |

For the canonical `ultimatechat` execution sequence that invokes this stack at Phase 2.5, see Chapter 17 §17.3. For the BBB filter architecture invoked at Phases 1.4 and 4.5, see Chapter 16. For ChromaDB collections (`autonomous_learner`, `ms_jarvis_memory`, `msjarvis_docs`) see Chapter 5. For the 69-DGM optimizer bridge see Chapter 32.

---

## Why This Matters for Polymathmatic Geography

This chapter describes how multiple language models and evaluation components operate together in Ms. Jarvis during live requests, all grounded in the three-database PostgreSQL architecture (`msjarvis` port 5433 with 5,416,521 verified GBIM beliefs; `gisdb` port 5432 PostGIS; `jarvis-local-resources-db` port 5435). It supports:

- **P1 – Every where is entangled** by routing every user query through 21 expert models and 5 judge services whose combined signals propagate through barrier, container, and memory layers anchored to PostgreSQL as first-class inputs.
- **P3 – Power has a geometry** by making evaluation explicit and inspectable — `consensus_score`, `judge_verdicts`, `all_issues`, and per-judge scores are all surfaced in `consciousnesslayers` on every `UltimateResponse`.
- **P5 – Design is a geographic act** by applying alignment and ethics judges that specifically check for adherence to Ms. Egeria Jarvis's community-service identity and Appalachian-rooted values constraints validated against PostgreSQL GBIM.
- **P12 – Intelligence with a ZIP code** by grounding the composite prompt sent to all 21 experts with local RAG context from `jarvis-spiritual-rag` (port 8005, queries PostgreSQL-sourced GBIM collections) and `jarvis-gis-rag` (port 8004, queries PostgreSQL `gisdb`) before any synthesis occurs.
- **P16 – Power accountable to place** by exposing consensus metrics, judge scores, and refinement flags so communities, auditors, and operators can inspect the quality-assurance signals behind every response validated against PostgreSQL.

As such, this chapter belongs to the Computational Instrument tier: it is the authoritative description of the `jarvis-20llm-production` ensemble and judge pipeline invoked at Phase 2.5/Phase 3 of the canonical `ultimatechat` execution sequence (Chapter 17 §17.3). Chapters 11, 17, and 25 should cross-reference here for details on the 21-LLM + judge pipeline stack.

---

## 33.12 Status as of March 22, 2026

| Category | Details |
|---|---|
| **Implemented and verified** | `jarvis-20llm-production` confirmed running at `127.0.0.1:8008`. `jarvis-semaphore` proxy confirmed running at `127.0.0.1:8030`. 21 active expert model proxy containers (`llm1-proxy` through `llm22-proxy`) confirmed running at `127.0.0.1:8201–8222` (22 proxies total; BakLLaVA at 8211 permanently disabled; StarCoder2 at 8207 unreliable on community queries — 21 reliably active). All 5 judge services compose-managed with `restart: unless-stopped` and bound to `127.0.0.1`. Real judge source files restored to `services/` (March 21, 2026). `Dockerfile.judge` confirmed present in `services/` with explicit `COPY judgesigner.py`. `judgesigner.py` (dilithium_py post-quantum signing) deployed in all 5 judge containers. Judge pipeline evaluates consensus answer ONLY. Phase 3.75 eliminated — merged into Phase 3.5 single Ollama call. Phase 1.45 community memory retrieval confirmed. LM Synthesizer identity guard: three layers active (§33.5.1). Duplicate LM Synthesizer call removed from `judge_pipeline.py` (March 22, 2026). `bbb_check_verdict` confirmed live — real async httpx POST to `jarvis-blood-brain-barrier:8016/filter`. Phase 4.5 BBB output in log+passthrough mode (commit `18b8ddac`). ChromaDB accessible on host port 8002. Redis accessible on host port 6380. Redis async key confirmed `'complete'`. GPU inference active (RTX 4070). Verified end-to-end: **99–107s** (three confirmed runs March 22, 2026). Pre-flight gate: **20 PASS 0 FAIL** (`scripts/preflight_gate.sh`, March 22, 2026). Public URL confirmed live: https://egeria.mountainshares.us. First public end-to-end chat response confirmed March 22, 2026: 21/21 LLMs responded, 106.5s, HTTP 200. |
| **Architectural fixes recorded as permanent decisions** | Duplicate LM Synthesizer call removed from `judge_pipeline.py` (March 22, 2026
