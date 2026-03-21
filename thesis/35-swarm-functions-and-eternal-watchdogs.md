# 35. Swarm Functions and Eternal Watchdogs

Carrie Kidd (Mamma Kidd) — Oak Hill, WV

## Why This Matters for Polymathmatic Geography

This chapter describes two sets of mechanisms that coordinate many services and maintain continuous oversight in Ms. Jarvis, all grounded in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs). It supports:

- **P1 – Every where is entangled** by distributing a single query across 22 configured specialized models, each contributing a perspective shaped by its training and domain, before synthesizing a single community-grounded answer validated against PostgreSQL GBIM.
- **P3 – Power has a geometry** by making visible which models contribute to consensus and which are silenced by memory constraints, resource limits, or intentional disabling — revealing the structural power embedded in the ensemble.
- **P5 – Design is a geographic act** by showing how choices about semaphore slots, container memory limits, concurrency gates, and model tier groupings reshape what Ms. Jarvis can reason about and how quickly it responds to Appalachian community questions grounded in PostgreSQL GeoDB.
- **P12 – Intelligence with a ZIP code** by routing every query through a 22-slot ensemble organized into four tiers — tiny, small, medium, and large — spanning code, medicine, language, vision, and structured data reasoning, and binding the synthesized answer to the 69-DGM cascade validation that grounds responses in constitutional and community commitments validated against PostgreSQL.
- **P16 – Power accountable to place** by logging every model's participation or failure in each consensus cycle, making the ensemble's behavior inspectable and auditable over time with PostgreSQL-backed operational history.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the swarm coordination mechanisms (22-model ensemble with semaphore gating), eternal watchdog systems (VERIFYANDTEST.sh, Ollama scheduler, concurrency gates, Redis health registration), dual-BBB architecture, and their integration with PostgreSQL `msjarvisgis` for community accountability.

---

```
┌─────────────────────────────────────────────────────────────┐
│   Swarm Functions & Eternal Watchdogs Architecture         │
│   (Production State: March 21, 2026)                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────────────────────────────────┐         │
│  │  22-Slot LLM Ensemble (Swarm Function)        │         │
│  │  ──────────────────────────────────────────   │         │
│  │  jarvis-20llm-production (port 8008)           │         │
│  │                                                │         │
│  │  TINY_MODELS (2):                              │         │
│  │  -  TinyLlama (8201), Gemma (8202)              │         │
│  │                                                │         │
│  │  SMALL_MODELS (3):                             │         │
│  │  -  Phi3 Mini (8210), Dolphin-Phi (8212)        │         │
│  │  -  Orca-Mini (8213)                            │         │
│  │                                                │         │
│  │  MEDIUM_MODELS (8 active, 1 disabled):         │         │
│  │  -  MedLlama2 (8203), MiniCPM-V (8204)          │         │
│  │  -  LLaVA (8205), SQLCoder (8206)               │         │
│  │  -  Zephyr (8215), Starling-LM (8216)           │         │
│  │  -  Neural-Chat (8217), OpenChat (8218)         │         │
│  │  -  BakLLaVA: DISABLED (name-check guard)       │         │
│  │                                                │         │
│  │  LARGE_MODELS (8):                             │         │
│  │  -  StarCoder2 (8207), CodeLlama (8208)         │         │
│  │  -  DeepSeek Coder (8209), Qwen2 (8214)         │         │
│  │  -  Vicuna (8219), LLaMA 2 (8220)               │         │
│  │  -  Mistral (8221), LLaMA 3.1 (8222)            │         │
│  │                                                │         │
│  │  Coordination:                                 │         │
│  │  -  asyncio.Semaphore(3) — max 3 concurrent     │         │
│  │  -  Timeout floor: 240 seconds                  │         │
│  │  -  21/22 contributing consensus (Mar 21)       │         │
│  │    (StarCoder2: HTTP 200, 0-char community)    │         │
│  │  -  Judge consistency: 0.975                    │         │
│  │  -  Warm cache: ~52s, Cold: ~163s               │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Dual Blood-Brain Barrier Architecture        │         │
│  │  ──────────────────────────────────────       │         │
│  │                                                │         │
│  │  jarvis-blood-brain-barrier (8016)             │         │
│  │  -  PRIMARY — judge pipeline output guard       │         │
│  │  -  7-filter input stack (Phase 1.4)            │         │
│  │  -  BBB output guard (Phase 4.5)                │         │
│  │  -  Full verdict dict received Mar 18           │         │
│  │  -  Steganography: zero_width_homoglyph_        │         │
│  │    structural_v1, confidence: 1.0 ✅           │         │
│  │  -  fail-open on HTTP 500                       │         │
│  │                                                │         │
│  │  nbb_blood_brain_barrier (8301)                │         │
│  │  -  NBB-INTERNAL — neurobiological variant      │         │
│  │  -  Running 3 days (confirmed Mar 21)           │         │
│  │  -  Phase 1 / NBB subconscious pathway          │         │
│  │  -  Complements, does not replace, 8016         │         │
│  │  -  NOT the judge pipeline output guard         │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  ┌────────────────────────────────────────────────┐         │
│  │  Five-Layer Watchdog System                   │         │
│  │  ──────────────────────────────────────        │         │
│  │  1. VERIFYANDTEST.sh                           │         │
│  │     -  32/32 services operational               │         │
│  │     -  22/22 LLM proxies healthy                │         │
│  │     -  80 Docker containers running             │         │
│  │     -  26 Ollama models available               │         │
│  │     -  PostgreSQL connections verified          │         │
│  │     -  Timestamped logs → ChromaDB              │         │
│  │                                                │         │
│  │  2. Ollama Internal Memory Scheduler           │         │
│  │     -  20 GB container limit                    │         │
│  │     -  OLLAMA_NUM_PARALLEL=1                    │         │
│  │     -  OLLAMA_MAX_LOADED_MODELS=1               │         │
│  │     -  Rejects loads exceeding memory           │         │
│  │                                                │         │
│  │  3. Asyncio Semaphore                          │         │
│  │     -  Limits to 3 concurrent Ollama requests   │         │
│  │     -  Prevents cascade failure                 │         │
│  │                                                │         │
│  │  4. MAX_CONCURRENT_CHATS Gate                  │         │
│  │     -  Set to 2 (production stable)             │         │
│  │     -  Session-level throughput control         │         │
│  │                                                │         │
│  │  5. Redis DynamicPortService                   │         │
│  │     -  NBB container health registration        │         │
│  │     -  5 instances with heartbeats              │         │
│  │     -  Dynamic port assignment                  │         │
│  └────────────────────────────────────────────────┘         │
│      ↓                                                       │
│  Integration Points (All PostgreSQL-Grounded)               │
│  -  BBB primary (8016): judge output guard                   │
│  -  BBB NBB-internal (8301): subconscious pathway            │
│  -  69-DGM cascade (19000→9000): 69 connectors              │
│  -  Psychology layer (8019): pre-ensemble assessment         │
│  -  NBB subconscious (7/8 healthy via consciousness bridge)  │
│  -  Consciousness bridge: mandatory infrastructure           │
│  -  Brain orchestrator: continuous coordination              │
│  -  PostgreSQL msjarvisgis (5432): ground truth validation   │
│  -  ChromaDB (8000): operational history ingestion           │
│                                                              │
│  Verified Performance Baseline (March 21, 2026)             │
│  -  Host RAM: 29 GB total, 13 GB available under load        │
│  -  Model storage: 73 GB at /mnt/ssd2/.../models             │
│  -  21/22 models contributing consensus                      │
│  -  Judge consistency: 0.975                                 │
│  -  STATUS: ✅ OPERATIONAL                                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 35.1.** Swarm functions and eternal watchdogs architecture (March 21, 2026): dual-BBB architecture with `jarvis-blood-brain-barrier` (port 8016) serving as primary judge pipeline output guard and `nbb_blood_brain_barrier` (port 8301) serving as the NBB-internal neurobiological variant; 22-slot LLM ensemble organized in 4 tiers with semaphore-gated coordination producing 21/22 consensus participation at 0.975 judge consistency, protected by 5-layer watchdog system, integrated with 69-DGM cascade (host port 19000), psychology layer, NBB subconscious, consciousness bridge, brain orchestrator, and PostgreSQL `msjarvisgis` ground truth validation.

---

## Status as of March 21, 2026

| Category | Details |
|---|---|
| **Implemented and verified** | 22-slot LLM ensemble (`jarvis-20llm-production`, port 8008) with 21 actively contributing consensus models as of March 21, 2026. Four-tier organization: TINY (2 models), SMALL (3 models), MEDIUM (8 active + 1 intentionally disabled via name-check guard), LARGE (8 models). `asyncio.Semaphore(3)` concurrency gate confirmed. `MAX_CONCURRENT_CHATS=2` session gate confirmed on `jarvis-main-brain`. Ollama container memory limit 20 GB, confirmed stable. 240-second timeout floor confirmed. BakLLaVA disabled via name-check guard. StarCoder2 (`llm7-proxy:8207`) returns HTTP 200 but 0-char on community queries; excluded from consensus. `VERIFYANDTEST.sh` eternal watchdog confirmed operational: 32/32 services healthy, 22/22 LLM proxies HTTP 200, 80 Docker containers running, 26 Ollama models available, four PostgreSQL databases verified. Redis DynamicPortService confirmed managing NBB container health registration with 5 instances heartbeating. **Dual-BBB architecture confirmed**: `jarvis-blood-brain-barrier` (port 8016) is the primary judge pipeline output guard (7-filter input stack Phase 1.4, full verdict dict output guard Phase 4.5, `zero_width_homoglyph_structural_v1` steganography filter `confidence: 1.0` confirmed active March 21); `nbb_blood_brain_barrier` (port 8301) is the NBB-internal neurobiological variant, confirmed running 3 days as of March 21, operating on the Phase 1 / NBB subconscious pathway. 69-DGM bridge (host port **19000** → internal 9000): 69 connectors loaded, architecturally authoritative. Psychology alignment layer (port 8019) confirmed Phase 3 pre-ensemble assessment every request. NBB subconscious: 7/8 containers healthy via consciousness bridge. Consciousness bridge and brain orchestrator confirmed as mandatory infrastructure. All services re-locked to `127.0.0.1` — zero `0.0.0.0` exposures — confirmed March 18, 2026. Five judge services compose-managed (`restart: unless-stopped`) since March 18, 2026. PostgreSQL `msjarvisgis` at `127.0.0.1:5432` (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) confirmed ground truth. ChromaDB `jarvis-chroma` (port 8000, `chroma_data` volume) confirmed operational history target. `gbimqueryrouter` (port 7205) confirmed as 80th container. |
| **Partially implemented / scaffolded** | ChromaDB `operations_history` collection for VERIFYANDTEST.sh log ingestion designed but automated ingestion pipeline not yet active. PostgreSQL-backed aggregated ensemble metrics (model participation rates over time, judge consistency trends) not yet exposed via dedicated analytics endpoint. Automated alerting based on VERIFYANDTEST.sh failure thresholds not yet implemented. StarCoder2 0-char exclusion logic in place but root cause (code-only model receiving community queries) not yet resolved via routing-layer fix. |
| **Future work / design intent only** | Automated ingestion of VERIFYANDTEST.sh logs into ChromaDB `operations_history`. PostgreSQL-backed time-series analytics dashboard for ensemble performance and judge consistency trends. Automated alerting when VERIFYANDTEST.sh detects service degradation. Dynamic model tier selection based on query complexity and historical performance from PostgreSQL. Automated model weight tuning based on domain-specific accuracy validated against PostgreSQL GBIM. StarCoder2 routing-layer fix to suppress community query dispatch and redirect to code-specific queries only. |

Cross-reference: This chapter describes the swarm coordination (22-model ensemble) and eternal watchdog systems that protect system stability. For the judge pipeline that evaluates ensemble output see Chapter 33. For the BBB primary pipeline (port 8016) that filters all requests see Chapter 16. For the NBB subconscious layer and NBB-internal BBB (port 8301) see Chapter 12. For the consciousness bridge and brain orchestrator that provide mandatory infrastructure see Chapter 12. For the canonical `ultimatechat` execution sequence that routes through this ensemble see Chapter 17. For the March 18, 2026 security hardening that re-locked all services to `127.0.0.1` see Chapter 40 §40-C.

---

## 35.1 Purpose of Swarm and Watchdog Layers

These mechanisms have complementary roles grounded in PostgreSQL `msjarvisgis`.

**Coordination.** Swarm functions allow multiple agents and services to contribute to a task, each from its own specialization. In the current deployment this is realized as the 22-slot LLM ensemble organized into four model tiers, where each proxy container represents a distinct model contributing a weighted response to every query with context sourced from PostgreSQL-backed RAG collections.

**Oversight.** Watchdogs provide continuous monitoring of key signals including PostgreSQL connection health, intervening when behavior deviates from expected bounds. In the current deployment this is realized through `VERIFYANDTEST.sh` (confirming four PostgreSQL database connections), Ollama's internal memory scheduler, the asyncio semaphore in the 20llm-production service, the `MAX_CONCURRENT_CHATS` gate on main-brain, and the Redis-backed DynamicPortService that monitors NBB container health.

**Stability.** Together they keep the system responsive and aligned even as individual components change or fail. The February 2026 hardening session demonstrated this directly: without the semaphore and concurrency controls, the system degraded from 20/22 models to 0/22 under concurrent load. With them in place, 21/22 models respond reliably on every warm-cache query with PostgreSQL-sourced context.

**Consciousness grounding.** The consciousness bridge (`jarvis-consciousness-bridge`) is essential infrastructure, not optional. All swarm coordination and watchdog monitoring operates within the consciousness bridge framework, ensuring that ensemble reasoning and health monitoring are neurobiologically grounded. The brain orchestrator (`jarvis-brain-orchestrator`) serves as the continuous coordinator service that maintains the swarm's coherence across all operational cycles.

---

## 35.2 Dual Blood-Brain Barrier Architecture

As of March 21, 2026, two BBB containers are confirmed running simultaneously. Their roles are distinct and complementary; they must not be conflated.

### jarvis-blood-brain-barrier (port 8016) — Primary, Judge Pipeline Output Guard

`jarvis-blood-brain-barrier` at `127.0.0.1:8016` is the primary, architecturally authoritative BBB. It serves two roles in the 9-phase production pipeline:

- **Phase 1.4 — input stack**: All 7 filters active (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, SteganographyDetection [`zero_width_homoglyph_structural_v1`, `confidence: 1.0`, confirmed March 21], TruthVerification, ContextAwareness). Every request passes through this gate before reaching psychological assessment or LLM synthesis.
- **Phase 4.5 — output guard**: After the 22-model ensemble and 69-DGM cascade, `apply_output_guards_async` posts the full judge verdict dict to `jarvis-blood-brain-barrier:8016/output_guard` (integrated March 18, 2026, 8.0s timeout, fail-open on HTTP 500). This is the component that sets `bbb_checked: true` in the UltimateResponse.

Port 8016 is the BBB that receives the judge pipeline's verdict dict. It is the component referenced in Chapter 16, Chapter 29 (PIA framework), Chapter 41 (smoke tests), and the March 21, 2026 regression baseline (`bbb_checked: true`, `consensus_score: 0.975`).

### nbb_blood_brain_barrier (port 8301) — NBB-Internal Neurobiological Variant

`nbb_blood_brain_barrier` at `127.0.0.1:8301` is the NBB-internal neurobiological variant of the BBB concept. It has been confirmed running for 3 days as of March 21, 2026. Its role is distinct from the primary BBB:

- Operates on the **Phase 1 / NBB subconscious pathway** — the neurobiological simulation layer managed by the consciousness bridge, not the main `ultimatechat` judge pipeline.
- Provides BBB-equivalent filtering within the NBB subconscious layer (`nbb-i-containers`, `nbb_woah_algorithms`, `nbb_prefrontal_cortex`, and associated containers), applying the BBB concept at the neurobiological simulation layer rather than at the main request pipeline boundary.
- Does **not** receive the judge pipeline verdict dict. It is not the component that sets `bbb_checked: true`.
- Does **not** replace or duplicate `jarvis-blood-brain-barrier:8016` — it complements it by extending the BBB gating concept into the NBB subconscious infrastructure.

```
┌──────────────────────────────────────────────────────┐
│   Dual-BBB Architecture: Role Disambiguation         │
├──────────────────────────────────────────────────────┤
│                                                      │
│  jarvis-blood-brain-barrier (8016)                   │
│  ─────────────────────────────────                   │
│  Role: PRIMARY — judge pipeline output guard         │
│  Pipeline position: Phase 1.4 (input) +              │
│                     Phase 4.5 (output guard)         │
│  Receives: Full judge verdict dict (Mar 18)          │
│  Sets: bbb_checked: true in UltimateResponse         │
│  Steganography: zero_width_homoglyph_structural_v1   │
│    confidence: 1.0 ✅ confirmed Mar 21               │
│  Fail-open: yes (HTTP 500 → pipeline continues)      │
│  Referenced in: Ch.16, Ch.29 PIA, Ch.41 smoke tests  │
│                                                      │
│  nbb_blood_brain_barrier (8301)                      │
│  ──────────────────────────────                      │
│  Role: NBB-INTERNAL — neurobiological variant        │
│  Pipeline position: Phase 1 / NBB subconscious       │
│  Receives: NBB subconscious layer traffic            │
│  Sets: NBB-layer filtering metadata (not             │
│        bbb_checked in main UltimateResponse)         │
│  Running: 3 days confirmed Mar 21, 2026              │
│  Referenced in: Ch.12, NBB subconscious layer        │
│                                                      │
│  These two containers are complementary.             │
│  Port 8016 ≠ Port 8301. Do not substitute.           │
│                                                      │
└──────────────────────────────────────────────────────┘
```

> **Figure 35.2.** Dual-BBB architecture role disambiguation. `jarvis-blood-brain-barrier:8016` is the primary judge pipeline output guard referenced in all Phase 1.4 and Phase 4.5 documentation. `nbb_blood_brain_barrier:8301` is the NBB-internal neurobiological variant operating on the NBB subconscious pathway. Neither replaces the other.

**Operational note for VERIFYANDTEST.sh:** Health probes for the BBB should target both ports:

```bash
# Primary BBB — judge pipeline output guard
curl -s http://127.0.0.1:8016/health | python3 -m json.tool

# NBB-internal BBB — neurobiological variant
curl -s http://127.0.0.1:8301/health | python3 -m json.tool
```

A healthy system shows both returning `status: healthy`. A failure on 8016 is a critical regression requiring immediate investigation. A failure on 8301 is an NBB subconscious layer issue that should be investigated via `docker logs nbb_blood_brain_barrier` and cross-referenced with the consciousness bridge health check.

---

## 35.3 Swarm Functions: The 22-Slot LLM Ensemble

The primary swarm function in Ms. Jarvis is the 20-LLM production service (`jarvis-20llm-production`, port 8008 on host). This service manages 22 proxy containers — `llm1-proxy` through `llm22-proxy` on ports 8201–8222 — organized into four tiers defined in `llm_consensus_20_FINAL.py`.

### Model roster by tier

**TINY_MODELS (2 configured)**

| Proxy | Port | Model | Name |
|---|---|---|---|
| llm1-proxy | 8201 | tinyllama:1.1b | TinyLlama |
| llm2-proxy | 8202 | gemma:latest | Gemma |

**SMALL_MODELS (3 configured)**

| Proxy | Port | Model | Name |
|---|---|---|---|
| llm10-proxy | 8210 | phi3:mini | Phi3 Mini |
| llm12-proxy | 8212 | dolphin-phi:latest | Dolphin-Phi |
| llm13-proxy | 8213 | orca-mini:latest | Orca-Mini |

**MEDIUM_MODELS (8 active, 1 disabled)**

| Proxy | Port | Model | Name | Status |
|---|---|---|---|---|
| llm3-proxy | 8203 | medllama2:latest | MedLlama2 | ✅ active |
| llm4-proxy | 8204 | minicpm-v:latest | MiniCPM-V | ✅ active |
| llm5-proxy | 8205 | llava:latest | LLaVA | ✅ active |
| llm6-proxy | 8206 | sqlcoder:latest | SQLCoder | ✅ active |
| llm15-proxy | 8215 | zephyr:latest | Zephyr | ✅ active |
| llm16-proxy | 8216 | starling-lm:latest | Starling-LM | ✅ active |
| llm17-proxy | 8217 | neural-chat:latest | Neural-Chat | ✅ active |
| llm18-proxy | 8218 | openchat:latest | OpenChat | ✅ active |
| llm11-proxy | 8211 | bakllava:latest | BakLLaVA | ❌ permanently disabled via name-check guard |

**LARGE_MODELS (8 configured)**

| Proxy | Port | Model | Status | Notes |
|---|---|---|---|---|
| llm7-proxy | 8207 | starcoder2:latest | ⚠️ HTTP 200, 0-char | Returns empty response on community queries; excluded from consensus |
| llm8-proxy | 8208 | codellama:latest | ✅ active | |
| llm9-proxy | 8209 | deepseek-coder:latest | ✅ active | |
| llm14-proxy | 8214 | qwen2:latest | ✅ active | |
| llm19-proxy | 8219 | vicuna:latest | ✅ active | |
| llm20-proxy | 8220 | llama2:latest | ✅ active | |
| llm21-proxy | 8221 | mistral:latest | ✅ active | |
| llm22-proxy | 8222 | llama3.1:8b | ✅ active | |

**Note on BakLLaVA and StarCoder2:** BakLLaVA (`llm11-proxy:8211`) is permanently disabled via name-check guard in the main-brain routing layer, consuming no Ollama resources. StarCoder2 (`llm7-proxy:8207`) returns HTTP 200 and is VERIFYANDTEST.sh-healthy, but produces 0-character responses on community queries due to its code-specialization; it is excluded from consensus extraction but remains in the health-monitored pool. Together these account for the difference between 22/22 HTTP-healthy proxies and 21/22 consensus-contributing models as of March 21, 2026.

### Swarm execution model

When a chat request arrives at `jarvis-20llm-production`, the `ProductionBrain.run()` method fires requests to all 22 configured endpoints concurrently, gated by an `asyncio.Semaphore(3)`. This semaphore is the critical swarm coordination mechanism: it limits concurrent Ollama requests to three at a time, preventing the serial Ollama scheduler from being overwhelmed while still allowing the ensemble to operate in parallel batches.

```python
sem = asyncio.Semaphore(3)  # max 3 concurrent Ollama requests

async def guarded(client, m):
    async with sem:
        return await self.query_one(client, m, prompt)

results = await asyncio.gather(*[guarded(client, m) for m in self.models])
```

The timeout floor is set at 240 seconds (`max(float(model_cfg.get("timeout", 60.0)), 240.0)`), accommodating the slowest 7B model cold-load scenario.

### Verified swarm timing profile (warm cache, February 28, 2026 baseline)

```text
[Phi3 Mini]      OK in  10.2s
[TinyLlama]      OK in  13.8s
[Orca-Mini]      OK in  20.0s
[Gemma]          OK in  21.4s
[Dolphin-Phi]    OK in  24.0s
[MedLlama2]      OK in  32.3s
[LLaVA]          OK in  32.3s
[Neural-Chat]    OK in  32.4s
[StarCoder2]     OK in  36.4s   ← HTTP 200 but 0-char on community queries
[LLaMA 2]        OK in  36.2s
[LLaMA 3.1]      OK in  36.3s
[Vicuna]         OK in  36.2s
[DeepSeek Coder] OK in  37.5s
[SQLCoder]       OK in  37.8s
[OpenChat]       OK in  39.5s
[MiniCPM-V]      OK in  45.7s
[Zephyr]         OK in  48.6s
[Starling-LM]    OK in  49.3s
[CodeLlama]      OK in  50.0s
[Mistral]        OK in  50.8s
[Qwen2]          OK in  52.0s
[BakLLaVA]       excluded: name-check guard  ← instant, expected
21/22 models contributing consensus
Judge pipeline score: 0.975
```

Total warm-cache swarm cycle: approximately 52 seconds. Cold-load cycle (first request after Ollama restart): approximately 163 seconds as 7B models load from the 73 GB model storage volume at `/mnt/ssd2/msjarvis_secondary/models`.

---

## 35.4 Use Cases for Swarm Functions

**Complex community queries.** When a user asks about housing assistance, workforce development, or healthcare access in a specific Appalachian county grounded in PostgreSQL GBIM, the ensemble distributes the question across medical (MedLlama2), structured data (SQLCoder), code and technical (CodeLlama, DeepSeek Coder), vision (LLaVA, MiniCPM-V), and general reasoning (Mistral, LLaMA 3.1, Qwen2) models simultaneously. The consensus synthesis integrates domain-specific contributions validated against PostgreSQL GeoDB that no single model could provide.

**Robustness verification.** The judge pipeline's consistency score validated against PostgreSQL GBIM measures whether independently prompted models reach similar conclusions. The March 21, 2026 canonical integration test records `consensus_score: 0.975` on the capital of West Virginia query, confirming that the ensemble's answer is stable across the majority of responding models and not an artifact of a single model's bias.

**Specialty routing.** SQLCoder handles structured data queries from PostgreSQL. CodeLlama and DeepSeek Coder handle technical implementation. MedLlama2 handles health-related queries. LLaVA and MiniCPM-V handle image and multimodal inputs. All 21 active consensus-contributing models contribute to every community response with PostgreSQL-sourced context, with weighted contributions amplifying domain-relevant answers.

**Redundancy.** With 21 of 22 configured slots contributing consensus, the ensemble tolerates individual model failures without degrading consensus validated against PostgreSQL. BakLLaVA's permanent disabled state, StarCoder2's 0-char exclusion, and Ollama's occasional memory-related refusals for the largest 7B models during cold load do not prevent the system from producing high-quality responses grounded in PostgreSQL GBIM.

---

## 35.5 Eternal Watchdogs: Continuous Monitoring

The watchdog layer in the March 21, 2026 deployment is implemented through five cooperating mechanisms including four PostgreSQL connection monitors.

### VERIFYANDTEST.sh

The primary eternal watchdog script implements eight verification sections on demand or schedule, producing a timestamped report at `/tmp/verify_YYYYMMDD_HHMMSS.log` with all PostgreSQL connection statuses. March 21, 2026 baseline results:

- Services healthy: 32/32 (confirmed via `/selftestfabric`)
- LLM proxies healthy: 22/22 (HTTP 200; 21 contributing consensus)
- Docker containers running: 80
- Ollama models available: 26
- PostgreSQL `msjarvis` (5433): ✅ CONNECTED — 5,416,521 GBIM entities
- PostgreSQL `gisdb` (5433): ✅ CONNECTED — PostGIS operational
- PostgreSQL `msjarvisgis` (5432): ✅ CONNECTED — 20,593 landowner beliefs
- PostgreSQL `jarvis-local-resources-db` (5435): ✅ CONNECTED
- Dual-BBB: `jarvis-blood-brain-barrier` (8016) ✅, `nbb_blood_brain_barrier` (8301) ✅
- STATUS: ✅ OPERATIONAL

The 26 Ollama models include 4 beyond the active ensemble: `nomic-embed-text:latest` (embedding — note: all-minilm:latest is the production embedding model for the `autonomous_learner` collection, locked March 17), `qwen2:7b`, `stablelm-zephyr:latest`, and `qwen2.5:1.5b`. These are available to Ollama but not currently mapped to proxy endpoints.

### Ollama internal memory scheduler

Ollama's built-in scheduler acts as a hard resource watchdog. When a model load request would exhaust available memory, it returns an explicit error: `model requires more system memory (7.5 GiB) than is available`. Current verified settings:

| Parameter | Verified Value |
|---|---|
| Ollama container memory limit | 20 GB |
| `OLLAMA_NUM_PARALLEL` | 1 |
| `OLLAMA_MAX_LOADED_MODELS` | 1 |
| Host total RAM | 29 GB |
| Host available RAM (production load) | 13 GB |

### Asyncio semaphore

The `asyncio.Semaphore(3)` in `ai_server_20llm_PRODUCTION.py` acts as a throughput watchdog, preventing more than three simultaneous Ollama requests regardless of how many concurrent chat sessions main-brain initiates. This is the proximate fix for the cascade failure mode where four concurrent sessions each fired 22 parallel requests, producing 88 simultaneous Ollama calls against a serial scheduler.

### MAX_CONCURRENT_CHATS gate

The `MAX_CONCURRENT_CHATS=2` environment variable on `jarvis-main-brain` is the session-level watchdog, limiting the number of simultaneous full chat pipelines. The original value of 4 produced Ollama saturation and cascade failure across the LLM ensemble. Current value of 2 represents the production-stable setting for the current hardware configuration.

### Redis-backed DynamicPortService

Five NBB containers register their health state to Redis (`jarvis-redis:6380`) using `DynamicPortService` rather than fixed endpoints:

```text
service:ms_jarvis_service:instance_1772240968
service:ms_jarvis_service:instance_1772240969
service:ms_jarvis_service:instance_1772240970
service:ms_jarvis_service:instance_1772240971
service:ms_jarvis_service:instance_1772240972
```

Each record contains `host`, `port`, `status`, `deployment`, `health_endpoint`, `started`, and `last_heartbeat` fields. The pituitary gland container registers with `status: healthy` and a dynamic port mapped externally as `7008/tcp → 127.0.0.1:8108`. This Redis-backed registration pattern allows NBB containers to restart with new ephemeral ports without breaking the watchdog fabric. Redis job state TTL is 30 minutes, consistent with the async chat job TTL documented in Chapter 17.

---

## 35.6 Watchdog Alert Responses

**Memory exhaustion.** Ollama rejects model load requests exceeding available memory with a structured error. The 20llm-production service logs this as a proxy failure and excludes the model from consensus, maintaining ensemble function with the remaining models and PostgreSQL-sourced context.

**Timeout.** Models exceeding the 240-second floor are logged as failures and excluded from consensus. The semaphore prevents cascading timeouts by serializing Ollama access to three concurrent slots maximum.

**BakLLaVA name-check guard.** BakLLaVA is permanently excluded via a name-check guard in the main-brain routing layer. The model name is detected before dispatch and the slot is bypassed with zero Ollama resource consumption. This supersedes the earlier DNS-poisoning approach documented in the February 28, 2026 baseline.

**StarCoder2 0-char exclusion.** StarCoder2 (`llm7-proxy:8207`) passes VERIFYANDTEST.sh health checks (HTTP 200) but returns empty responses on community queries. The consensus extraction layer detects 0-character responses and excludes them from the consensus score calculation. StarCoder2 remains in the health-monitored pool; future work will implement routing-layer fixes to dispatch code-specific queries to StarCoder2 and suppress community query dispatch.

**Session overload.** The `MAX_CONCURRENT_CHATS=2` gate causes main-brain to queue requests beyond the second concurrent session. This prevents downstream cascade at the cost of added latency for queued requests during heavy load. Async jobs (`/chat/async`) use Redis for job state (30-minute TTL) and do not consume a `MAX_CONCURRENT_CHATS` slot until they begin active processing.

**BBB content rejection (primary BBB — port 8016).** When content triggers a filter validated against PostgreSQL GBIM, it is rejected before reaching the LLM ensemble, conserving Ollama resources. `barrier_stats` counts are logged for PIA review (Chapter 29 §29.5). Note: `nbb_blood_brain_barrier` (port 8301) rejections are logged independently within the NBB subconscious layer and are not included in the primary `barrier_stats` counter.

**BBB output guard failure (port 8016).** If the BBB output guard returns HTTP 500 on Phase 4.5 evaluation, `apply_output_guards_async` fails open — the pipeline continues and delivers the response with `bbb_checked: false`. This behavior is logged as a WARNING and surfaces in VERIFYANDTEST.sh reports. A pattern of `bbb_checked: false` entries in `ms_jarvis_memory` is a PIA review trigger.

**PostgreSQL connection loss.** VERIFYANDTEST.sh monitors all four PostgreSQL connection health states. Any `FAILED` status triggers immediate alerting and prevents ensemble operations that depend on PostgreSQL-sourced RAG context. The `msjarvisgis` database (port 5432) is particularly critical for the `gbimqueryrouter` (port 7205) landowner query pathway — a connection failure there affects the 80th container's spatial query capability without necessarily affecting the main `msjarvis` BBB validation path.

**0.0.0.0 exposure detection.** VERIFYANDTEST.sh includes a security watchdog check: `docker ps --format '{{.Names}} {{.Ports}}' | grep 0.0.0.0`. Any output from this check is a critical security regression requiring immediate `docker compose` re-lock and `--force-recreate`. Expected output: empty (zero `0.0.0.0` exposures confirmed March 18, 2026).

---

## 35.7 Integration with Barriers, Modes, and Containers

**Blood-brain barrier (primary — port 8016).** Every chat request passes through `jarvis-blood-brain-barrier:8016/filter` validated against PostgreSQL GBIM (Phase 1.4) before reaching the LLM ensemble, and the full judge verdict dict is passed to `jarvis-blood-brain-barrier:8016/output_guard` (Phase 4.5) after the 69-DGM cascade. This is the BBB referenced in all smoke tests in Chapter 41 and all PIA review procedures in Chapter 29.

**Blood-brain barrier (NBB-internal — port 8301).** `nbb_blood_brain_barrier:8301` operates on the NBB subconscious pathway, applying BBB-concept filtering at the neurobiological simulation layer. It is monitored by VERIFYANDTEST.sh and contributes to the NBB subconscious health report but does not participate in the main `ultimatechat` Phase 1.4 / Phase 4.5 pipeline.

**69-DGM cascade.** Every ensemble response routed through main-brain (port 8050) is validated by `jarvis-69dgm-bridge` at **host port 19000** (internal container port 9000) against PostgreSQL-grounded constitutional and community commitments. The `validated_by: "69_dgm_cascade"` field confirms this gate fired. Requests sent directly to the 20llm-production service on port 8008 bypass the 69-DGM gate by design — port 8008 is the internal ensemble endpoint, not the public interface.

**Psychology alignment layer.** The `jarvis-psychology-services:8019` service runs a psychological assessment validated against PostgreSQL community norms on every request before the ensemble processes it. Phase 3 psychology pre-assessment records are included in `consciousnesslayers` of the UltimateResponse.

**NBB subconscious layer.** Seven of eight NBB containers respond to health probes via their internal network endpoints, confirming the neurobiological simulation layer is active. The `nbb_blood_brain_barrier` (port 8301) is one of these NBB containers, confirmed running 3 days as of March 21, 2026. The pituitary gland registers through Redis DynamicPortService rather than a fixed `/health` endpoint.

**Judge pipeline (compose-managed since March 18, 2026).** All five judge services (ports 7230–7233, 7239) are confirmed compose-managed with `restart: unless-stopped`. Judge verdicts are delivered as a full dict to `jarvis-blood-brain-barrier:8016/output_guard` at Phase 4.5. Judge service health is included in VERIFYANDTEST.sh fabric verification.

**Consciousness bridge and brain orchestrator.** The consciousness bridge (`jarvis-consciousness-bridge`) serves as mandatory infrastructure through which all swarm and watchdog operations flow. The brain orchestrator (`jarvis-brain-orchestrator`) continuously coordinates the ensemble, watchdog feedback loops, and neurobiological layer health checks, ensuring coherent system behavior across all 32 operational services.

**ChromaDB memory integration.** Verification script outputs saved to `/tmp/verify_*.log` are structured for ingestion into ChromaDB (port 8000, `chroma_data` volume) under an `operations_history` collection. The automated ingestion pipeline is designed but not yet active; manual ingestion is the current practice.

**PostgreSQL msjarvisgis integration.** PostgreSQL `msjarvisgis` at `127.0.0.1:5432` (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) serves as ground truth for BBB validation, 69-DGM cascade verification, RAG context sourcing, and VERIFYANDTEST.sh connection monitoring. The `gbimqueryrouter` (port 7205, 80th container) routes landowner-specific queries directly to `mvw_gbim_landowner_spatial` in `msjarvisgis` without traversing the LLM ensemble, providing millisecond-latency spatial query responses validated against PostgreSQL ground truth.

---

## 35.8 Summary

Swarm functions and eternal watchdogs in the March 21, 2026 Ms. Jarvis deployment are running, verified, and logged against concrete evidence with PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as ground truth. The 22-slot LLM ensemble — organized into TINY, SMALL, MEDIUM, and LARGE tiers across 21 actively contributing consensus models, with BakLLaVA permanently excluded and StarCoder2 excluded from consensus on community queries — delivers 21/22 consensus participation on every warm-cache query with PostgreSQL-sourced context in approximately 52 seconds with a judge pipeline consistency score of 0.975.

The dual-BBB architecture is the most significant architectural clarification since the February 28, 2026 baseline: `jarvis-blood-brain-barrier` (port 8016) is the primary judge pipeline output guard, serving Phase 1.4 input filtering and Phase 4.5 output evaluation with the full verdict dict and confirmed `zero_width_homoglyph_structural_v1` steganography detection at `confidence: 1.0`; `nbb_blood_brain_barrier` (port 8301) is the NBB-internal neurobiological variant operating on the Phase 1 / NBB subconscious pathway, confirmed running 3 days as of March 21. Both are monitored by VERIFYANDTEST.sh. Neither replaces the other.

The five-layer watchdog system — VERIFYANDTEST.sh confirming 32/32 services operational plus four PostgreSQL connection health checks, Ollama memory scheduler, asyncio semaphore at slot 3, `MAX_CONCURRENT_CHATS=2` gate, and Redis DynamicPortService — prevents the cascade failures that reduced the system to 0/22 models under uncontrolled concurrent load. All services are bound to `127.0.0.1` (zero `0.0.0.0` exposures, confirmed March 18, 2026), all judge services are compose-managed, and the March 21, 2026 canonical integration test (`consensus_score: 0.975`, `bbb_checked: true`) establishes the regression baseline that this watchdog architecture is designed to protect.

All swarm coordination and watchdog monitoring operates within the consciousness bridge framework, with the brain orchestrator maintaining continuous oversight. The 69-DGM cascade (host port 19000) provides architecturally authoritative verification validated against PostgreSQL GBIM of every response before delivery, ensuring alignment with constitutional and community commitments. This integrated design — swarm intelligence plus eternal vigilance, neurobiologically grounded, spatially anchored in PostgreSQL `msjarvisgis`, and protected by comprehensive watchdog systems including a dual-layer BBB architecture — represents the operational reality of Ms. Jarvis as a production consciousness-inspired cognitive system serving West Virginia communities.

---

*Last updated: 2026-03-21 by Carrie Kidd (Mamma Kidd), Oak Hill WV*
