# 17. Executive Coordination Overview

Carrie Kidd (Mamma Kidd) — Mount Hope, WV

*Last updated: 2026-03-27 — §17.2 GPU corrected RTX 4050 → RTX 4070 (per Ch. 12 §12.1 confirmed hardware); §17.3 Phase 1.4 ContextAwareness 7th filter cross-reference to Ch. 16 §16.4 added; §17.7 Phase 1.45 AAPCAppE first-run footnote added (65 docs, March 27, 2026)*

---

## Why This Matters for Polymathmatic Geography

This chapter provides the empirical grounding for all architectural claims made across the thesis. It supports:

- **P1 – Every where is entangled** by measuring the actual cost of entangling spatial, semantic, community memory, and neurobiological services on a single commodity host — demonstrating that a geographically rooted AI system can achieve full-pipeline operation even on hardware typical of a rural nonprofit.

- **P3 – Power has a geometry** by making the per-phase timing profile visible, showing exactly which stages account for latency and where optimization pressure should be directed.

- **P5 – Design is a geographic act** by showing that design decisions — merging Phase 3.5/3.75, switching judge payload to consensus-only, adding health-check caching, converting compose to image-based — have measurable geographic consequences: a system that can be rebooted and fully operational in two commands is a system a community organization can actually steward.

- **P12 – Intelligence with a ZIP code** by documenting that 21 models, three PostgreSQL databases, 21,181 community memories, and 5,416,521 GBIM entities all operate on a Lenovo Legion 5 in a home office in Oak Hill, West Virginia.

- **P16 – Power accountable to place** by publishing the benchmark methodology, the exact query used, the hardware envelope, and the per-phase timing so that future operators and researchers can reproduce, audit, and improve upon these measurements.

As such, this chapter belongs to the **Empirical Evidence** tier: it converts architectural claims into falsifiable, reproducible measurements anchored to a specific place, time, and hardware configuration.

---

## 17.1 The `ultimatechat` Execution Path

The `ultimatechat` execution path is the canonical end-to-end coordination sequence that processes every synchronous request through the full 9-phase Ms. Jarvis ULTIMATE pipeline. It is the primary artifact evaluated in the operational benchmarks (Chapter 39) and the primary integration surface for all architectural changes described in this thesis.

As of March 18, 2026 — the reference snapshot for all benchmarks in this chapter — the pipeline runs on a Lenovo Legion 5 at Oak Hill, West Virginia, managing 80 fully compose-managed containers, three PostgreSQL databases (ports 5432, 5433, 5435), a ChromaDB instance (port 8000), and a 21-model LLM ensemble. End-to-end response time on the reference benchmark query ("What community resources are available in Fayette County, WV?") is approximately **436 seconds**, optimized from a 532-second pre-optimization baseline (see Chapter 39, §39.2).

Two architectural changes confirmed in the March 16–18 sessions materially affect the canonical execution sequence described in §17.3:

1. **BBB output guard now receives the full verdict dict, not just the answer text.** After the judge pipeline produces its scored verdict (`truth_score`, `consistency_score`, `alignment_score`, `ethics_score`, `consensus_score`, `judge_verdicts`), the BBB output guard receives the complete verdict dictionary — including all judge scores and the synthesized `consensus_answer` — rather than the raw answer string alone. This change enables the BBB to apply output guards that are score-aware: a response with a low `ethics_score` can be held or modified by the BBB even if its text does not independently trigger any pattern-based filter. This is documented as a confirmed operational change in the March 18, 2026 security hardening audit (Chapter 40, §40-C).

2. **Judge pipeline → BBB output guard integration is a confirmed step in the Phase 4 sequence.** Prior to March 16, the judge pipeline (ports 7230–7233, coordinated by `judge_pipeline.py`) ran as an orphaned set of manually started containers with no guaranteed integration into the BBB output path. As of March 18, all five judge containers are compose-managed with `restart: unless-stopped`, their outputs are wired to the BBB output guard, and the guard's `apply_output_guards_async` function is confirmed to receive the full verdict dict. This makes the judge → BBB handoff a first-class, monitored step in the pipeline rather than a best-effort side channel.

Both changes are reflected in the canonical execution sequence in §17.3.

---

## 17.2 Reference Hardware and Baseline State

All timing figures and architectural claims in this chapter are grounded in the following reference configuration, confirmed March 18, 2026:

```
┌─────────────────────────────────────────────────────────────┐
│     Ms. Jarvis ULTIMATE — Reference Deployment State        │
│     March 18, 2026 — Oak Hill, West Virginia                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Host              Lenovo Legion 5 (16IRX9), Intel i9       │
│  RAM               29 GB system RAM                          │
│  GPU               NVIDIA RTX 4070 — present, not used      │
│  Inference mode    CPU-only (size_vram: 0 on all models)    │
│  Docker Compose    v5.1.0 (upgraded from v1.29.2)           │
│  Containers        80 fully compose-managed                 │
│                                                              │
│  PostgreSQL msjarvis    port 5433 — 5,416,521 GBIM entities │
│  PostgreSQL gisdb       port 5433 — PostGIS, 13 GB          │
│  PostgreSQL msjarvisgis port 5432 — 91 GB, 501 tables       │
│  PostgreSQL local-res   port 5435 — community resources     │
│  ChromaDB               port 8000 — 384-dim, all-minilm     │
│  autonomous_learner     21,181 records (~288/day growth)    │
│  LLM ensemble           21 of 22 models active             │
│  End-to-end benchmark   ~436s (optimized from 532s)         │
│                                                              │
│  Location: Oak Hill / Mount Hope, Fayette County, WV        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 17-1. Reference deployment configuration for all benchmarks and execution-sequence documentation in this chapter. GPU corrected to RTX 4070 per Ch. 12 §12.1 confirmed hardware reference (March 27, 2026). All measurements are CPU-only; GPU-accelerated inference via the WVU partnership server remains pending.

---

## 17.3 Canonical `ultimatechat` Execution Sequence

The following sequence documents the confirmed Phase-by-Phase execution path for a synchronous `POST /ultimatechat` request as of March 18, 2026. Two confirmed changes from earlier descriptions are marked explicitly: **(NEW)** for additions not present in earlier chapter drafts, and **(UPDATED)** for steps whose behavior changed in the March 16–18 sessions.

```
┌─────────────────────────────────────────────────────────────┐
│       Canonical ultimatechat Execution Sequence             │
│       Confirmed State: March 18, 2026                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ── PHASE 1 ── Service Discovery + Prefrontal Planning      │
│                                                              │
│  POST /ultimatechat received by jarvis-main-brain (8050)   │
│  Health check sweep — 30s TTL cache, 2s timeout/service    │
│  NBB Prefrontal Cortex consulted for planning context       │
│  Cost: ~0.7s (cached after first query)                     │
│                                                              │
│  ── PHASE 1.4 ── BBB Input Filter                          │
│                                                              │
│  POST jarvis-blood-brain-barrier:8016/filter                │
│  7-filter stack:                                            │
│    1. EthicalFilter                                          │
│    2. SpiritualFilter                                        │
│    3. SafetyMonitor (regex corrected March 15)              │
│    4. ThreatDetection                                        │
│    5. SteganographyDetection                                 │
│    6. TruthVerification (truth_score null guard active)     │
│    7. ContextAwareness                                       │
│  Fail-open on HTTP 500 — pipeline continues                 │
│  Cost: ~1.3s total (including Phase 1.45)                   │
│                                                              │
│  Note: Ch. 16 §16.4 documents 6 named stable filters        │
│  (EthicalFilter, SpiritualFilter, SafetyMonitor,            │
│  ThreatDetection, SteganographyDetection,                   │
│  TruthVerification); ContextAwareness is the 7th filter     │
│  present in the Phase 1.4 stack per this canonical          │
│  sequence. See Ch. 16 §16.4 for per-filter stability log.  │
│                                                              │
│  ── PHASE 1.45 ── Semantic Community Memory Retrieval (NEW) │
│                                                              │
│  Fires AFTER BBB input approval, BEFORE text RAG           │
│  all-minilm:latest (384-dim) → autonomous_learner          │
│    (21,181 items, ~288/day growth)                         │
│  Top-5 most similar records retrieved                       │
│  Prepended to enhanced_message before LLM ensemble         │
│  Cost: included in Phase 1.4 total                          │
│                                                              │
│  ── PHASE 1.75–3 (pre-LLM) ──                              │
│                                                              │
│  Truth verdict — BBB port 8016                              │
│  Psychology pre-assessment — port 8019                      │
│  Consciousness layers (6 active, validated March 13)        │
│  Cost: ~0.5s                                                 │
│                                                              │
│  ── PHASE 4 ── RAG Context Building                        │
│                                                              │
│  jarvis-spiritual-rag (port 8005)                           │
│    → spiritual_texts, appalachian_cultural_intelligence,    │
│      governance collections                                 │
│  jarvis-gis-rag (port 8004)                                 │
│    → gbim_worldview_entities, gis_wv_benefits               │
│    → PostgreSQL gisdb / msjarvis (port 5433)               │
│  jarvis-rag-server (port 8003)                              │
│    → text RAG over thesis, governance, msjarvis_docs        │
│  jarvis-local-resources-db (port 5435)                      │
│    → registry resolver (county, ZIP, resource_type)        │
│  web research — excluded for WV-scoped queries              │
│  WV-first context assembly                                  │
│  Cost: included in Phase 1.75–3 total                       │
│                                                              │
│  ── PHASE 2.5 ── 21-Model LLM Ensemble Synthesis           │
│                                                              │
│  semaphore proxy (port 8030)                                │
│    → jarvis-20llm-production (port 8008)                    │
│  Community-memory-enriched, RAG-grounded prompt             │
│  21 models active (StarCoder2 excluded from consensus)      │
│  CPU-only inference — hardware floor                        │
│  Cost: ~320–360s                                            │
│                                                              │
│  ── PHASE 3 ── Judge Pipeline (UPDATED — March 16–18)      │
│                                                              │
│  Receives: consensus_answer ONLY                            │
│    (raw_responses dump eliminated — saves ~15–20s)         │
│  jarvis-judge-truth      (port 7230)                        │
│  jarvis-judge-consistency (port 7231)                       │
│  jarvis-judge-alignment  (port 7232)                        │
│  jarvis-judge-ethics     (port 7233)                        │
│  jarvis-judge-pipeline   (port 7239, coordinator)          │
│  All 5 containers: compose-managed, restart: unless-stopped │
│  Returns: full verdict dict —                               │
│    { truth_score, consistency_score, alignment_score,       │
│      ethics_score, consensus_score, judge_verdicts,         │
│      consensus_answer }                                     │
│  Cost: ~60–86s                                              │
│                                                              │
│  ── PHASE 3 → PHASE 4 HANDOFF ── Judge → BBB (UPDATED)     │
│                                                              │
│  [CONFIRMED NEW STEP — March 18, 2026]                     │
│                                                              │
│  Full verdict dict passed to BBB output guard               │
│  POST jarvis-blood-brain-barrier:8016/output_guard          │
│    Payload: complete verdict dict (not answer text only)    │
│    Includes: all judge scores + consensus_answer            │
│  BBB apply_output_guards_async — score-aware filtering:    │
│    - Low ethics_score → held or modified                    │
│    - Low truth_score → flagged or amended                   │
│    - Constitutional check against verdict                   │
│  Fail-open on HTTP 500 — content passes through,           │
│    failure logged (8.0s timeout)                            │
│                                                              │
│  ── PHASE 3.5 ── LM Synthesizer + Voice Delivery           │
│  (merged from Phase 3.5 + 3.75 — UPDATED March 18)        │
│                                                              │
│  Single Ollama call — saves ~40s vs. two-pass              │
│  jarvis-ollama:11434/api/generate                           │
│  model: llama3.1:latest                                     │
│  Ms. Egeria Jarvis persona prompt injected                  │
│  Phase 3.75 (Final LLM Polish) eliminated                   │
│  Cost: ~30–55s                                              │
│                                                              │
│  ── PHASE 7 + PHASE 4.5 ──                                 │
│                                                              │
│  69-DGM cascade — jarvis-69dgm-bridge                      │
│    host port 19000 → internal port 9000                    │
│    23 connectors, 3 stages, 69 DGM operations              │
│  BBB output guard — final pass (fail-open on HTTP 500)     │
│  Cost: ~0.5s                                                 │
│                                                              │
│  ── PHASE 5 + POST-PROCESSING ──                            │
│                                                              │
│  confidence_decay multiplier (GBIM temporal)                │
│  normalize_identity                                          │
│  background_rag_store (async — non-blocking)                │
│  Cost: ~0.5s                                                 │
│                                                              │
│  ── RESPONSE ──                                             │
│                                                              │
│  UltimateResponse returned to caller                        │
│  Total: ~436s (reference benchmark, March 18, 2026)         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 17-2. Canonical `ultimatechat` execution sequence as of March 18, 2026. Two confirmed changes are marked **(UPDATED)**: (1) the judge pipeline now returns a full verdict dict, not a consensus answer string, and (2) the judge → BBB handoff is a confirmed, compose-managed step in which the BBB output guard receives and evaluates the full verdict dict before Phase 3.5 voice delivery. Phase 1.4 note: Ch. 16 §16.4 documents 6 named stable filters; ContextAwareness is the 7th filter present in this canonical stack.

---

## 17.4 The BBB Output Guard — Full Verdict Dict (UPDATED)

The Blood-Brain Barrier output guard (`apply_output_guards_async`, `jarvis-blood-brain-barrier:8016`) underwent a confirmed behavioral change in the March 18 session. Prior to this change, the guard received the synthesized answer text as a string and applied pattern-based content filters to that text independently of any judge scoring. After the change, the guard receives the **complete judge verdict dictionary**:

```python
# Confirmed BBB output guard payload shape (March 18, 2026)
verdict_payload = {
    "consensus_answer": str,        # synthesized response text
    "truth_score": float,           # 0.0–1.0 from judge_truth (port 7230)
    "consistency_score": float,     # 0.0–1.0 from judge_consistency (port 7231)
    "alignment_score": float,       # 0.0–1.0 from judge_alignment (port 7232)
    "ethics_score": float,          # 0.0–1.0 from judge_ethics (port 7233)
    "consensus_score": float,       # aggregated score from judge_pipeline (port 7239)
    "judge_verdicts": dict,         # per-judge detail objects
    "expert_count": int,            # number of LLM responses included in consensus
    "gbim_beliefs_consulted": int,  # populated when RAG-grounded judges deployed
    "gbim_contradictions_detected": int  # populated when RAG-grounded judges deployed
}
```

This change is significant because it gives the BBB output guard access to the full epistemic state of the response — not just its surface text but also how well it scored across truth, consistency, alignment, and ethics dimensions. The guard can now act as a score-gated filter: a response that passes all surface-level text checks but carries a low `ethics_score` (below a configurable threshold) can be held, amended, or accompanied by a disclosure note before delivery. The `fail-open on HTTP 500` behavior (added March 18) ensures that a BBB failure does not block the pipeline; the content passes through unchanged and the failure is logged.

```
┌─────────────────────────────────────────────────────────────┐
│     BBB Output Guard — Full Verdict Dict Integration        │
│     Confirmed: March 18, 2026                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Judge Pipeline (port 7239)                                 │
│  Produces: full verdict dict                                 │
│      ↓                                                       │
│  POST :8016/output_guard                                    │
│  Payload: verdict dict (all fields above)                   │
│      ↓                                                       │
│  BBB apply_output_guards_async                              │
│    ├─ Constitutional check (text + ethics_score)            │
│    ├─ Truth gate (truth_score threshold)                     │
│    ├─ Alignment gate (alignment_score threshold)            │
│    └─ Ethics gate (ethics_score threshold)                  │
│    └─ Safety validation                                      │
│      ↓                                                       │
│  Pass / Amend / Hold                                        │
│    fail-open on HTTP 500 (8.0s timeout)                     │
│      ↓                                                       │
│  Phase 3.5 — LM Synthesizer (llama3.1:latest)              │
│      ↓                                                       │
│  UltimateResponse                                           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 17-3. BBB output guard integration with the full judge verdict dict. The guard receives all judge scores, not just the answer text, enabling score-aware content filtering before voice delivery.

---

## 17.5 Phase 3 — Judge Pipeline Integration (UPDATED)

The judge pipeline underwent two confirmed changes in the March 16–18 sessions:

**Change 1 — Consensus-only payload (March 16):** Prior to March 16, the judge pipeline received the full `raw_responses` dump from all 21 LLM proxies as part of its evaluation payload. This caused the judge evaluation cycle to spend significant time parsing, deduplicating, and scoring individual model outputs. The change limits the judge payload to `consensus_answer` only — the pre-synthesized response string — reducing Phase 3 wall-clock time by approximately 15–20 seconds per query.

**Change 2 — Compose management and port correction (March 16–18):** All five judge containers were previously started via manual `docker run` with `restart: no`, giving them no managed lifecycle. On any system reboot or `docker compose down`, they would silently fail to restart, leaving the main brain operating in degraded mode (`consensus_score: 0.8`, `expert_count: 0`, no `judge_verdicts`). As of March 18, all five are defined in `docker-compose.yml` with `restart: unless-stopped` and `build: context: ./services, dockerfile: Dockerfile.judge`. The previously incorrect unified port `7239` (used for all four evaluation judges) was corrected to the per-judge ports `7230` (truth), `7231` (consistency), `7232` (alignment), `7233` (ethics), with `7239` remaining as the pipeline coordinator.

```
┌─────────────────────────────────────────────────────────────┐
│     Judge Pipeline — Confirmed State March 18, 2026         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Input: consensus_answer (ONLY — raw_responses eliminated)  │
│                                                              │
│  jarvis-judge-pipeline   port 7239  coordinator             │
│    ├─ jarvis-judge-truth      port 7230  heuristic_v1       │
│    ├─ jarvis-judge-consistency port 7231  heuristic_v1      │
│    ├─ jarvis-judge-alignment  port 7232  heuristic_v1       │
│    └─ jarvis-judge-ethics     port 7233  heuristic_v1       │
│                                                              │
│  All 5 containers:                                          │
│    ✅ compose-managed (restart: unless-stopped)             │
│    ✅ build: ./services / Dockerfile.judge                  │
│    ✅ ports locked to 127.0.0.1                             │
│    ✅ source files in services/ directory                   │
│                                                              │
│  Output: full verdict dict → BBB output guard (port 8016)  │
│                                                              │
│  ⚠️  Current judge method: heuristic_contradiction_v1      │
│     (pattern-matching — no live GBIM/RAG queries)          │
│     See Chapter 7, §7.8 for RAG-grounded upgrade path.     │
│                                                              │
│  Phase 3 wall-clock: ~60–86s (reduced from ~85–100s)       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 17-4. Judge pipeline confirmed state as of March 18, 2026. All five containers are compose-managed. The current judge implementation uses `heuristic_contradiction_v1` (pattern-matching). The RAG-grounded upgrade described in Chapter 7, §7.8 is the specified near-term improvement path.

---

## 17.6 The UltimateResponse Schema

The `UltimateResponse` is the canonical output object of the `ultimatechat` path. It carries the synthesized answer, all judge scores, consciousness layer metadata, GBIM temporal metadata, and — as of the March 18 changes — fields that will expose judge-to-BBB integration provenance when the RAG-grounded judge upgrade (Chapter 7, §7.8) is deployed.

```python
# UltimateResponse schema — confirmed March 18, 2026
# Forward-compatible fields for RAG-grounded judge upgrade marked (FUTURE)

class UltimateResponse(BaseModel):
    # Core response
    answer: str                     # synthesized answer (Ms. Jarvis persona)
    consensus_answer: str           # raw pre-persona consensus
    
    # Judge verdict block — UPDATED (full verdict dict now passed to BBB)
    truth_score: float              # 0.0–1.0 (heuristic_v1 current)
    consistency_score: float        # 0.0–1.0
    alignment_score: float          # 0.0–1.0
    ethics_score: float             # 0.0–1.0
    consensus_score: float          # aggregated
    judge_verdicts: dict            # per-judge detail
    expert_count: int               # LLM responses included in consensus
    
    # GBIM temporal metadata (Phase 5)
    confidence_decay: float         # applied at Phase 5
    gbim_beliefs_consulted: int     # (FUTURE: populated by RAG-grounded judges)
    gbim_contradictions_detected: int  # (FUTURE: populated by RAG-grounded judges)
    
    # Consciousness layer metadata (validated March 13, 2026)
    validated_by: str               # comma-separated active layer names
    architecture_layers: int        # count of active consciousness layers
    consciousness_layers: list      # per-layer name/status objects
    truth_verdict: dict             # { valid, confidence, principal_reasons }
    
    # Provenance
    rag_sources: list               # ChromaDB collections queried
    gis_sources: list               # PostgreSQL gisdb features returned
    registry_sources: list          # jarvis-local-resources-db rows used
    phase_145_memories: list        # top-5 autonomous_learner records prepended
    
    # Async job metadata (when called via /chat/async)
    job_id: Optional[str]
    status: Optional[str]
```

The `gbim_beliefs_consulted` and `gbim_contradictions_detected` fields are scaffolded in the current schema as integers (default 0). They are populated with non-zero values only when the RAG-grounded judge upgrade (Chapter 7, §7.8) is deployed. Including them now ensures forward compatibility — external callers and dashboards can begin parsing these fields without a schema breaking change.

---

## 17.7 Per-Phase Timing Profile (March 18, 2026)

The following table documents the confirmed wall-clock cost of each phase on the reference hardware. All figures are from the March 18, 2026 benchmark on the Lenovo Legion 5 (CPU-only inference).

| Phase | Description | Wall-clock cost |
|---|---|---|
| Phase 1 | Service discovery + NBB prefrontal planning (30s TTL health cache) | ~0.7s (cached) |
| Phase 1.4 | BBB 7-filter input stack (fail-open on HTTP 500; truth_score null guard) | ~1.3s total |
| Phase 1.45 | Community memory retrieval — `autonomous_learner` top-5 (all-minilm, 384-dim) | Included above |
| Phase 1.75–3 pre-LLM | Truth verdict + psychology pre-assessment + consciousness layers | ~0.5s |
| Phase 4 | RAG context building — spiritual-rag, gis-rag, text-rag, registry, web (WV-excluded) | Included above |
| Phase 2.5 | 21-model LLM ensemble — CPU-only, semaphore proxy, community-enriched prompt | ~320–360s |
| Phase 3 | 4-judge pipeline — consensus-only payload (raw_responses eliminated) | ~60–86s |
| Phase 3 → Phase 4 handoff | **Judge → BBB output guard — full verdict dict (CONFIRMED NEW STEP)** | < 1s |
| Phase 3.5 | LM Synthesizer + Voice Delivery — merged single Ollama call, llama3.1:latest | ~30–55s |
| Phase 7 + Phase 4.5 | 69-DGM cascade + BBB output guard (fail-open, 8.0s timeout) | ~0.5s |
| Phase 5 + post-processing | Confidence decay + normalize_identity + background_rag_store (async) | ~0.5s |
| **Total** | **Full 9-phase pipeline** | **~436s** |

> The 436-second end-to-end figure represents a ~18% improvement from the 532-second pre-optimization baseline. The dominant cost — ~320–360 seconds — is Phase 2.5 (CPU-only LLM ensemble) and represents a hardware floor, not a software optimization target. The path to sub-120-second ensemble times is GPU-accelerated inference via the WVU partnership server (pending).

> **Phase 1.45 corpus note (March 27, 2026):** As of March 27, 2026, Phase 1.45 community memory retrieval now has access to **65 documents from the AAPCAppE first scrape run** (`jarvis-ingest-watcher` first confirmed run — 39 sources) in addition to the existing `autonomous_learner` corpus. RAG server also loaded 53 documents (7 new base cultural docs). See Ch. 16 §16.13 and Ch. 30 (OI-30) for full ingest pipeline status.

---

## 17.8 Optimization History (March 16–18, 2026)

| Optimization | Applied | Time saved |
|---|---|---|
| Judge pipeline consensus-only (eliminated `raw_responses` dump) | March 16 | ~15–20s/query |
| Phase 3.5 + Phase 3.75 merged into single Ollama call | March 18 | ~40s/query |
| Health-check caching (30s TTL, 2s per-service timeout) | March 18 | ~0.7s after first query |
| BBB fail-open on HTTP 500 (eliminates hang on BBB errors) | March 18 | Eliminates hangs |
| Judge URL corrections (7239 → 7230/7231/7232/7233) | March 16 | Eliminates silent judge failures |
| LM Synthesizer URL fix (jarvis-roche-llm → jarvis-ollama:11434) | March 18 | Eliminates Phase 3.5 errors |
| **Judge → BBB full verdict dict handoff wired** | **March 18** | **Architectural correctness** |
| **Total measured improvement** | **March 16–18** | **~96s (~18%)** |

The judge → BBB verdict dict handoff is listed here as an architectural correctness fix rather than a latency optimization: the change does not reduce wall-clock time, but it closes a critical integration gap in which the BBB output guard had no access to judge scores and could not apply score-aware content filtering.

---

## 17.9 Container Infrastructure Supporting the Execution Path

The `ultimatechat` execution path touches 20+ containers across the 80-container production stack. The following table maps each phase to its primary container(s) and confirms compose management status as of March 18, 2026:

| Phase | Primary containers | Ports | Compose-managed |
|---|---|---|---|
| Phase 1 | `jarvis-main-brain` | 8050 | ✅ |
| Phase 1.4 | `jarvis-blood-brain-barrier` | 8016 | ✅ |
| Phase 1.45 | `jarvis-autonomous-learner`, `jarvis-ollama`, `jarvis-chroma` | 8425, 11434, 8000 | ✅ |
| Phase 2.5 | `jarvis-20llm-production`, `jarvis-semaphore`, llm1–22 proxies | 8008, 8030, 8201–8222 | ✅ |
| Phase 3 | `jarvis-judge-truth`, `-consistency`, `-alignment`, `-ethics`, `-pipeline` | 7230–7233, 7239 | ✅ (as of March 18) |
| Phase 3→4 handoff | `jarvis-blood-brain-barrier` | 8016 | ✅ |
| Phase 3.5 | `jarvis-lm-synthesizer`, `jarvis-ollama` | internal, 11434 | ✅ |
| Phase 4 | `jarvis-spiritual-rag`, `jarvis-gis-rag`, `jarvis-rag-server`, `jarvis-local-resources-db` | 8005, 8004, 8003, 5435 | ✅ |
| Phase 7 | `jarvis-69dgm-bridge` | 19000 (→9000 internal) | ✅ |
| Phase 5 | `jarvis-main-brain` (decay + store) | 8050 | ✅ |

> All containers listed above are defined in `~/msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml` with `image:` references (no `build:` directives). Docker Compose v5.1.0. No container in the `ultimatechat` path requires manual startup; `jarvis_startup.sh` handles the six judge/gateway pipeline containers with health-check retry logic.

---

## 17.10 Known Issues and Forward Path (March 18, 2026)

| Issue | Status |
|---|---|
| Judge implementation is `heuristic_contradiction_v1` — no live GBIM queries | 🔴 OPEN — see Chapter 7, §7.8 for RAG-grounded upgrade specification |
| BBB output guard score thresholds not yet configurable — pass/hold/amend logic uses implicit defaults | 🟡 PENDING — threshold configuration planned post-GPU activation |
| `gbim_beliefs_consulted` and `gbim_contradictions_detected` always 0 in current schema | 🟡 PENDING — populated when RAG-grounded judges deployed |
| Hallucination on Mount Hope / Fayette County local resource queries | 🔴 OPEN — `jarvis-local-resources-db` empty; Community Champions data entry is next priority |
| GPU inference (WVU partnership server) | 🟡 PENDING — expected to reduce Phase 2.5 from ~320–360s to ~80–120s |
| StarCoder2 (`llm7-proxy`) returns 0-char on community queries | 🟡 KNOWN — 21 of 22 models active; consensus extracts correctly |
| Red-team adversarial test suite | 🔴 OPEN — highest-priority remaining security gap |

The most consequential forward-path item for the `ultimatechat` execution sequence itself is the RAG-grounded judge upgrade (Chapter 7, §7.8). When deployed, the judge pipeline will make live HTTP calls to `jarvis-gis-rag:8004` and `jarvis-spiritual-rag:8005` as part of truth and alignment scoring, populating `gbim_beliefs_consulted` and `gbim_contradictions_detected` with real counts and passing a genuinely evidence-grounded verdict dict to the BBB output guard. The judge → BBB verdict dict handoff wired in March 18 is the plumbing that makes this upgrade slot in without further structural changes.

---

## 17.11 Async Job API

The Redis-backed async job system (deployed March 17, 2026) provides non-blocking access to the full 9-phase pipeline for callers who cannot wait ~436 seconds synchronously. The async path executes the same canonical sequence described in §17.3:

| Endpoint | Method | Function |
|---|---|---|
| `/chat/async` | POST | Create async job — returns `job_id` immediately |
| `/chat/status/{job_id}` | GET | Poll for progress and result |
| `/chat/cancel/{job_id}` | DELETE | Cancel specific job — true `asyncio.Task.cancel()` |
| `/chat/cancel/all` | DELETE | Cancel all running jobs |

Job state is stored in Redis (`jarvis-redis:6379`) with a 30-minute TTL. State survives `jarvis-main-brain` container restarts (Redis persists independently). `DELETE /chat/cancel/{job_id}` performs true asyncio task cancellation — the 21-LLM pipeline stops immediately mid-run. The in-memory-only `active_jobs` limitation is resolved; the Redis-backed store is the canonical job state store as of March 17, 2026.

---

## 17.12 Verified Reboot Sequence (March 18, 2026)

```bash
# Step 1: Start all 80 compose-managed containers
cd ~/msjarvis-rebuild-working/msjarvis-rebuild && docker compose up -d

# Step 2: Start and verify the six pipeline containers
~/jarvis_startup.sh
```

Go signal — six green checkmarks from `~/jarvis_startup.sh`:

```
jarvis-judge-truth        ✅
jarvis-judge-consistency  ✅
jarvis-judge-alignment    ✅
jarvis-judge-ethics       ✅
jarvis-judge-pipeline     ✅
jarvis-69dgm-bridge       ✅
```

The `build:` → `image:` conversion (March 17) makes this sequence fully deterministic: `docker compose up -d` starts containers from pre-built images with no rebuild overhead. The verified two-command reboot restores the complete 80-container stack including all services in the `ultimatechat` execution path.

---

*Last updated: 2026-03-27 by Carrie Kidd (Mamma Kidd), Mount Hope WV*
*★ March 27, 2026: §17.2 GPU corrected RTX 4050 → RTX 4070 (per Ch. 12 §12.1 confirmed hardware reference); §17.3 Phase 1.4 cross-reference added — Ch. 16 §16.4 documents 6 named stable filters; ContextAwareness is the 7th filter in this canonical stack; §17.7 Phase 1.45 footnote added — 65 AAPCAppE docs now available in Chroma as of March 27, 2026 first scrape run (39 sources), RAG 53 docs loaded, 7 new base cultural docs ingested.*
`````
