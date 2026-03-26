# 35. Swarm Functions and Eternal Watchdogs

Carrie Kidd (Mamma Kidd) — Oak Hill, WV
*Last updated: March 25, 2026 — VERIFYANDTEST.sh preflight gate updated to 24 PASS / 0 FAIL (March 22–25 sprint); StarCoder2 exclusion (OI-11) status confirmed unchanged; no regression failures introduced by bridge, WOAH, or RAG patches*

---

## Why This Matters for Polymathmatic Geography

This chapter describes two sets of mechanisms that coordinate many services and maintain continuous oversight in Ms. Jarvis, all grounded in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs). It supports:

- **P1 – Every where is entangled** by distributing a single query across 22 configured specialized models, each contributing a perspective shaped by its training and domain, before synthesizing a single community-grounded answer validated against PostgreSQL GBIM.
- **P3 – Power has a geometry** by making visible which models contribute to consensus and which are silenced by memory constraints, resource limits, or intentional disabling — revealing the structural power embedded in the ensemble.
- **P5 – Design is a geographic act** by showing how choices about semaphore slots, container memory limits, concurrency gates, and model tier groupings reshape what Ms. Jarvis can reason about and how quickly it responds to Appalachian community questions grounded in PostgreSQL GeoDB.
- **P12 – Intelligence with a ZIP code** by routing every query through a 22-slot ensemble organized into four tiers — tiny, small, medium, and large — spanning code, medicine, language, vision, and structured data reasoning, and binding the synthesized answer to the 69-DGM cascade validation that grounds responses in constitutional and community commitments validated against PostgreSQL.
- **P16 – Power accountable to place** by logging every model's participation or failure in each consensus cycle, making the ensemble's behavior inspectable and auditable over time with PostgreSQL-backed operational history.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the swarm coordination mechanisms (22-model ensemble with semaphore gating), eternal watchdog systems (VERIFYANDTEST.sh, Ollama scheduler, concurrency gates, Redis health registration), dual-BBB architecture, and their integration with PostgreSQL `msjarvisgis` for community accountability.

---

┌─────────────────────────────────────────────────────────────┐
│ Swarm Functions & Eternal Watchdogs Architecture │
│ (Production State: March 25, 2026) │
├─────────────────────────────────────────────────────────────┤
│ │
│ ┌────────────────────────────────────────────────┐ │
│ │ 22-Slot LLM Ensemble (Swarm Function) │ │
│ │ ────────────────────────────────────────── │ │
│ │ jarvis-20llm-production (port 8008) │ │
│ │ │ │
│ │ TINY_MODELS (2): │ │
│ │ - TinyLlama (8201), Gemma (8202) │ │
│ │ │ │
│ │ SMALL_MODELS (3): │ │
│ │ - Phi3 Mini (8210), Dolphin-Phi (8212) │ │
│ │ - Orca-Mini (8213) │ │
│ │ │ │
│ │ MEDIUM_MODELS (8 active, 1 disabled): │ │
│ │ - MedLlama2 (8203), MiniCPM-V (8204) │ │
│ │ - LLaVA (8205), SQLCoder (8206) │ │
│ │ - Zephyr (8215), Starling-LM (8216) │ │
│ │ - Neural-Chat (8217), OpenChat (8218) │ │
│ │ - BakLLaVA: DISABLED (name-check guard) │ │
│ │ │ │
│ │ LARGE_MODELS (8): │ │
│ │ - StarCoder2 (8207) ⚠️ OI-11 UNCHANGED │ │
│ │ - CodeLlama (8208), DeepSeek Coder (8209) │ │
│ │ - Qwen2 (8214), Vicuna (8219) │ │
│ │ - LLaMA 2 (8220), Mistral (8221) │ │
│ │ - LLaMA 3.1 (8222) │ │
│ │ │ │
│ │ Coordination: │ │
│ │ - asyncio.Semaphore(3) — max 3 concurrent │ │
│ │ - Timeout floor: 240 seconds │ │
│ │ - 21/22 contributing consensus │ │
│ │ (StarCoder2: HTTP 200, 0-char community) │ │
│ │ - Judge consistency: 0.975 │ │
│ │ - Warm cache: ~52s, Cold: ~163s │ │
│ └────────────────────────────────────────────────┘ │
│ ↓ │
│ ┌────────────────────────────────────────────────┐ │
│ │ Dual Blood-Brain Barrier Architecture │ │
│ │ ────────────────────────────────────── │ │
│ │ │ │
│ │ jarvis-blood-brain-barrier (8016) │ │
│ │ - PRIMARY — judge pipeline output guard │ │
│ │ - 6-filter input stack (Phase 1.4) │ │
│ │ - BBB output guard (Phase 4.5, │ │
│ │ log+passthrough — commit 18b8ddac) │ │
│ │ - Full verdict dict received Mar 18 │ │
│ │ - Steganography: zero_width_homoglyph_ │ │
│ │ structural_v1, confidence: 1.0 ✅ │ │
│ │ - fail-open on HTTP 500 │ │
│ │ │ │
│ │ nbb_blood_brain_barrier (8301) │ │
│ │ - NBB-INTERNAL — neurobiological variant │ │
│ │ - Running confirmed Mar 21 │ │
│ │ - Phase 1 / NBB subconscious pathway │ │
│ │ - Complements, does not replace, 8016 │ │
│ │ - NOT the judge pipeline output guard │ │
│ └────────────────────────────────────────────────┘ │
│ ↓ │
│ ┌────────────────────────────────────────────────┐ │
│ │ Five-Layer Watchdog System │ │
│ │ ────────────────────────────────────── │ │
│ │ 1. VERIFYANDTEST.sh / preflight_gate.sh │ │
│ │ - 32/32 services operational │ │
│ │ - 22/22 LLM proxies healthy │ │
│ │ - preflight: 24 PASS / 0 FAIL ✅ │ │
│ │ (March 22–25 sprint — no regression) │ │
│ │ - PostgreSQL connections verified │ │
│ │ - Timestamped logs → ChromaDB │ │
│ │ │ │
│ │ 2. Ollama Internal Memory Scheduler │ │
│ │ - 20 GB container limit │ │
│ │ - OLLAMA_NUM_PARALLEL=1 │ │
│ │ - OLLAMA_MAX_LOADED_MODELS=1 │ │
│ │ - Rejects loads exceeding memory │ │
│ │ │ │
│ │ 3. Asyncio Semaphore │ │
│ │ - Limits to 3 concurrent Ollama requests │ │
│ │ - Prevents cascade failure │ │
│ │ │ │
│ │ 4. MAX_CONCURRENT_CHATS Gate │ │
│ │ - Set to 2 (production stable) │ │
│ │ - Session-level throughput control │ │
│ │ │ │
│ │ 5. Redis DynamicPortService │ │
│ │ - NBB container health registration │ │
│ │ - 5 instances with heartbeats │ │
│ │ - Dynamic port assignment │ │
│ └────────────────────────────────────────────────┘ │
│ ↓ │
│ Integration Points (All PostgreSQL-Grounded) │
│ - BBB primary (8016): judge output guard │
│ - BBB NBB-internal (8301): subconscious pathway │
│ - 69-DGM cascade (19000→9000): 69 connectors │
│ - Psychology layer (8019): pre-ensemble assessment │
│ - NBB subconscious (7/8 healthy via consciousness bridge) │
│ - Consciousness bridge: mandatory infrastructure │
│ - Brain orchestrator: continuous coordination │
│ - PostgreSQL msjarvisgis (5432): ground truth validation │
│ - ChromaDB (8002 host): operational history ingestion │
│ │
│ Verified Performance Baseline (March 25, 2026) │
│ - Host RAM: 29 GB total, 13 GB available under load │
│ - Model storage: 73 GB at /mnt/ssd2/.../models │
│ - 21/22 models contributing consensus │
│ - Judge consistency: 0.975 │
│ - preflight_gate.sh: 24 PASS / 0 FAIL ✅ │
│ - STATUS: ✅ OPERATIONAL │
│ │
└─────────────────────────────────────────────────────────────┘

text

> **Figure 35.1.** Swarm functions and eternal watchdogs architecture (March 25, 2026): dual-BBB architecture with `jarvis-blood-brain-barrier` (port 8016) serving as primary judge pipeline output guard and `nbb_blood_brain_barrier` (port 8301) serving as the NBB-internal neurobiological variant; 22-slot LLM ensemble organized in 4 tiers with semaphore-gated coordination producing 21/22 consensus participation at 0.975 judge consistency; preflight gate confirmed at **24 PASS / 0 FAIL** throughout March 22–25 sprint; protected by 5-layer watchdog system; StarCoder2 exclusion (OI-11) status unchanged.

---

## Status as of March 25, 2026

| Category | Details |
|---|---|
| **Implemented and verified** | 22-slot LLM ensemble (`jarvis-20llm-production`, port 8008) with 21 actively contributing consensus models. Four-tier organization: TINY (2 models), SMALL (3 models), MEDIUM (8 active + 1 intentionally disabled via name-check guard), LARGE (8 models). `asyncio.Semaphore(3)` concurrency gate confirmed. `MAX_CONCURRENT_CHATS=2` session gate confirmed on `jarvis-main-brain`. Ollama container memory limit 20 GB, confirmed stable. 240-second timeout floor confirmed. BakLLaVA disabled via name-check guard. StarCoder2 (`llm7-proxy:8207`) returns HTTP 200 but 0-char on community queries; excluded from consensus (OI-11 — status unchanged, not addressed in March 22–25 sprint). **VERIFYANDTEST.sh / `preflight_gate.sh` confirmed at 24 PASS / 0 FAIL throughout the entire March 22–25 sprint. No regression failures were introduced by any of the bridge, WOAH, or RAG patches (Chapter 25 §25.9).** 32/32 services healthy, 22/22 LLM proxies HTTP 200, PostgreSQL connections verified. Redis DynamicPortService confirmed managing NBB container health registration with 5 instances heartbeating. **Dual-BBB architecture confirmed**: `jarvis-blood-brain-barrier` (port 8016) is the primary judge pipeline output guard (6-filter input stack Phase 1.4, verdict dict output guard Phase 4.5 — log+passthrough mode commit `18b8ddac`); `nbb_blood_brain_barrier` (port 8301) is the NBB-internal neurobiological variant. 69-DGM bridge (host port **19000** → internal 9000): 69 connectors loaded. Psychology alignment layer (port 8019) confirmed Phase 3 pre-ensemble assessment every request. NBB subconscious: 7/8 containers healthy via consciousness bridge. All services re-locked to `127.0.0.1` — zero `0.0.0.0` exposures. Five judge services compose-managed (`restart: unless-stopped`). PostgreSQL `msjarvisgis` at `127.0.0.1:5432` confirmed ground truth. ChromaDB host port **8002** confirmed. |
| **Partially implemented / scaffolded** | ChromaDB `operations_history` collection for VERIFYANDTEST.sh log ingestion designed but automated ingestion pipeline not yet active. PostgreSQL-backed aggregated ensemble metrics not yet exposed via dedicated analytics endpoint. Automated alerting based on VERIFYANDTEST.sh failure thresholds not yet implemented. StarCoder2 0-char exclusion logic in place but root cause not yet resolved via routing-layer fix (OI-11 unchanged). |
| **Future work / design intent only** | Automated ingestion of VERIFYANDTEST.sh logs into ChromaDB `operations_history`. PostgreSQL-backed time-series analytics dashboard for ensemble performance and judge consistency trends. Automated alerting when VERIFYANDTEST.sh detects service degradation. Dynamic model tier selection based on query complexity. Automated model weight tuning. StarCoder2 routing-layer fix (OI-11). |

Cross-reference: This chapter describes the swarm coordination and eternal watchdog systems. For the judge pipeline see Chapter 33. For the BBB primary pipeline (port 8016) see Chapter 16. For the NBB subconscious layer and NBB-internal BBB (port 8301) see Chapter 12. For the consciousness bridge and brain orchestrator see Chapter 12. For the canonical `ultimatechat` execution sequence see Chapter 17. For the March 18, 2026 security hardening see Chapter 40 §40-C. For the March 22–25 consciousness pipeline bridge patches see Chapter 25 §25.9.

---

## 35.1 Purpose of Swarm and Watchdog Layers

These mechanisms have complementary roles grounded in PostgreSQL `msjarvisgis`.

**Coordination.** Swarm functions allow multiple agents and services to contribute to a task, each from its own specialization. In the current deployment this is realized as the 22-slot LLM ensemble organized into four model tiers, where each proxy container represents a distinct model contributing a weighted response to every query with context sourced from PostgreSQL-backed RAG collections.

**Oversight.** Watchdogs provide continuous monitoring of key signals including PostgreSQL connection health, intervening when behavior deviates from expected bounds. In the current deployment this is realized through `VERIFYANDTEST.sh` (confirming four PostgreSQL database connections), Ollama's internal memory scheduler, the asyncio semaphore in the 20llm-production service, the `MAX_CONCURRENT_CHATS` gate on main-brain, and the Redis-backed DynamicPortService that monitors NBB container health.

**Stability.** Together they keep the system responsive and aligned even as individual components change or fail. The March 22–25 sprint demonstrated this directly: three consciousness pipeline bridge patches were applied (Chapter 25 §25.9) and the preflight gate remained at **24 PASS / 0 FAIL** throughout. No regression failures were introduced.

**Consciousness grounding.** The consciousness bridge (`jarvis-consciousness-bridge`) is essential infrastructure, not optional. All swarm coordination and watchdog monitoring operates within the consciousness bridge framework, ensuring that ensemble reasoning and health monitoring are neurobiologically grounded. The brain orchestrator (`jarvis-brain-orchestrator`) serves as the continuous coordinator service that maintains the swarm's coherence across all operational cycles.

---

## 35.2 Dual Blood-Brain Barrier Architecture

As of March 25, 2026, two BBB containers are confirmed running simultaneously. Their roles are distinct and complementary; they must not be conflated.

### jarvis-blood-brain-barrier (port 8016) — Primary, Judge Pipeline Output Guard

`jarvis-blood-brain-barrier` at `127.0.0.1:8016` is the primary, architecturally authoritative BBB. It serves two roles in the production pipeline:

- **Phase 1.4 — input stack**: All 6 filters active (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, SteganographyDetection [`zero_width_homoglyph_structural_v1`, `confidence: 1.0`], TruthVerification [`heuristic_contradiction_v1`]). Every request passes through this gate before reaching psychological assessment or LLM synthesis.
- **Phase 4.5 — output guard**: After the 22-model ensemble and 69-DGM cascade, `apply_output_guards_async` posts the full judge verdict dict to `jarvis-blood-brain-barrier:8016/output_guard`. **As of commit `18b8ddac` (March 22, 2026), Phase 4.5 is in log+passthrough mode** — all responses pass through and filter results are logged, but no response is blocked at this layer pending threshold recalibration (31% false-positive on maternal Appalachian voice). See Chapter 16 §16.9 and Chapter 38 §38.6.1.

Port 8016 is the BBB that receives the judge pipeline's verdict dict. It is the component referenced in Chapter 16, Chapter 29 (PIA framework), Chapter 41 (smoke tests), and all sprint regression baselines.

### nbb_blood_brain_barrier (port 8301) — NBB-Internal Neurobiological Variant

`nbb_blood_brain_barrier` at `127.0.0.1:8301` is the NBB-internal neurobiological variant of the BBB concept, confirmed running as of March 21, 2026. Its role is distinct from the primary BBB:

- Operates on the **Phase 1 / NBB subconscious pathway** — the neurobiological simulation layer managed by the consciousness bridge, not the main `ultimatechat` judge pipeline.
- Does **not** receive the judge pipeline verdict dict. It is not the component that sets `bbb_checked: true`.
- Does **not** replace or duplicate `jarvis-blood-brain-barrier:8016` — it complements it by extending the BBB gating concept into the NBB subconscious infrastructure.

┌──────────────────────────────────────────────────────┐
│ Dual-BBB Architecture: Role Disambiguation │
├──────────────────────────────────────────────────────┤
│ │
│ jarvis-blood-brain-barrier (8016) │
│ ───────────────────────────────── │
│ Role: PRIMARY — judge pipeline output guard │
│ Pipeline position: Phase 1.4 (input) + │
│ Phase 4.5 (output guard, │
│ log+passthrough — 18b8ddac) │
│ Receives: Full judge verdict dict (Mar 18) │
│ Sets: bbb_checked: true in UltimateResponse │
│ Steganography: zero_width_homoglyph_structural_v1 │
│ confidence: 1.0 ✅ confirmed Mar 21 │
│ Fail-open: yes (HTTP 500 → pipeline continues) │
│ Referenced in: Ch.16, Ch.29 PIA, Ch.41 smoke tests │
│ │
│ nbb_blood_brain_barrier (8301) │
│ ────────────────────────────── │
│ Role: NBB-INTERNAL — neurobiological variant │
│ Pipeline position: Phase 1 / NBB subconscious │
│ Receives: NBB subconscious layer traffic │
│ Sets: NBB-layer filtering metadata (not │
│ bbb_checked in main UltimateResponse) │
│ Running: confirmed Mar 21, 2026 │
│ Referenced in: Ch.12, NBB subconscious layer │
│ │
│ These two containers are complementary. │
│ Port 8016 ≠ Port 8301. Do not substitute. │
│ │
└──────────────────────────────────────────────────────┘

text

> **Figure 35.2.** Dual-BBB architecture role disambiguation. `jarvis-blood-brain-barrier:8016` is the primary judge pipeline output guard. `nbb_blood_brain_barrier:8301` is the NBB-internal neurobiological variant operating on the NBB subconscious pathway. Neither replaces the other.

**Operational note for VERIFYANDTEST.sh:** Health probes for the BBB should target both ports:

```bash
# Primary BBB — judge pipeline output guard
curl -s http://127.0.0.1:8016/health | python3 -m json.tool

# NBB-internal BBB — neurobiological variant
curl -s http://127.0.0.1:8301/health | python3 -m json.tool
```

A healthy system shows both returning `status: healthy`. A failure on 8016 is a critical regression requiring immediate investigation. A failure on 8301 is an NBB subconscious layer issue that should be investigated via `docker logs nbb_blood_brain_barrier`.

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
| llm7-proxy | 8207 | starcoder2:latest | ⚠️ OI-11 UNCHANGED | HTTP 200, 0-char on community queries; excluded from consensus. Not addressed in March 22–25 sprint. |
| llm8-proxy | 8208 | codellama:latest | ✅ active | |
| llm9-proxy | 8209 | deepseek-coder:latest | ✅ active | |
| llm14-proxy | 8214 | qwen2:latest | ✅ active | |
| llm19-proxy | 8219 | vicuna:latest | ✅ active | |
| llm20-proxy | 8220 | llama2:latest | ✅ active | |
| llm21-proxy | 8221 | mistral:latest | ✅ active | |
| llm22-proxy | 8222 | llama3.1:8b | ✅ active | |

**Note on BakLLaVA and StarCoder2 (OI-11):** BakLLaVA (`llm11-proxy:8211`) is permanently disabled via name-check guard. StarCoder2 (`llm7-proxy:8207`) passes VERIFYANDTEST.sh health checks (HTTP 200) but produces 0-character responses on community queries due to its code-specialization; it is excluded from consensus extraction but remains in the health-monitored pool. **OI-11 status is UNCHANGED as of March 25, 2026 — StarCoder2 was not addressed in the March 22–25 sprint.** Root cause (code-only model receiving community queries) and routing-layer fix remain future work.

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

[Phi3 Mini] OK in 10.2s
[TinyLlama] OK in 13.8s
[Orca-Mini] OK in 20.0s
[Gemma] OK in 21.4s
[Dolphin-Phi] OK in 24.0s
[MedLlama2] OK in 32.3s
[LLaVA] OK in 32.3s
[Neural-Chat] OK in 32.4s
[StarCoder2] OK in 36.4s ← HTTP 200 but 0-char on community queries (OI-11)
[LLaMA 2] OK in 36.2s
[LLaMA 3.1] OK in 36.3s
[Vicuna] OK in 36.2s
[DeepSeek Coder] OK in 37.5s
[SQLCoder] OK in 37.8s
[OpenChat] OK in 39.5s
[MiniCPM-V] OK in 45.7s
[Zephyr] OK in 48.6s
[Starling-LM] OK in 49.3s
[CodeLlama] OK in 50.0s
[Mistral] OK in 50.8s
[Qwen2] OK in 52.0s
[BakLLaVA] excluded: name-check guard ← instant, expected
21/22 models contributing consensus
Judge pipeline score: 0.975

text

Total warm-cache swarm cycle: approximately 52 seconds. Cold-load cycle: approximately 163 seconds.

---

## 35.4 Use Cases for Swarm Functions

**Complex community queries.** When a user asks about housing assistance, workforce development, or healthcare access in a specific Appalachian county grounded in PostgreSQL GBIM, the ensemble distributes the question across medical (MedLlama2), structured data (SQLCoder), code and technical (CodeLlama, DeepSeek Coder), vision (LLaVA, MiniCPM-V), and general reasoning (Mistral, LLaMA 3.1, Qwen2) models simultaneously.

**Robustness verification.** The judge pipeline's consistency score validated against PostgreSQL GBIM measures whether independently prompted models reach similar conclusions. The March 21, 2026 canonical integration test records `consensus_score: 0.975` on the capital of West Virginia query, confirming ensemble stability.

**Specialty routing.** SQLCoder handles structured data queries from PostgreSQL. CodeLlama and DeepSeek Coder handle technical implementation. MedLlama2 handles health-related queries. LLaVA and MiniCPM-V handle image and multimodal inputs.

**Redundancy.** With 21 of 22 configured slots contributing consensus, the ensemble tolerates individual model failures without degrading consensus. BakLLaVA's permanent disabled state, StarCoder2's 0-char exclusion (OI-11, unchanged), and Ollama's occasional memory-related refusals do not prevent the system from producing high-quality responses.

---

## 35.5 Eternal Watchdogs: Continuous Monitoring

The watchdog layer is implemented through five cooperating mechanisms including four PostgreSQL connection monitors.

### VERIFYANDTEST.sh and preflight_gate.sh

> **March 22–25 sprint result: preflight gate held at 24 PASS / 0 FAIL throughout the entire sprint. No regression failures were introduced by any of the bridge patches (Chroma health check reroute, WOAH network fix, gateway dict.lower() guard), WOAH container rebuild, or RAG endpoint correction. See Chapter 25 §25.9 for the full patch record.**

The primary eternal watchdog script implements eight verification sections on demand or schedule, producing a timestamped report at `/tmp/verify_YYYYMMDD_HHMMSS.log` with all PostgreSQL connection statuses.

**March 22–25, 2026 sprint preflight validation:**

preflight_gate.sh — Sprint Validation Log
─────────────────────────────────────────────────────────────
Sprint: March 22–25, 2026
Patches applied this sprint:
- Ch. 25 Patch 1: Chroma health check rerouted to
jarvis-chroma:8000/api/v2/heartbeat directly
- Ch. 25 Patch 2: WOAH container rebuilt as stdlib stub,
brought up on qualia-net
- Ch. 25 Patch 3A: RAG endpoint corrected /direct_rag → /query
- Ch. 25 Patch 3B: isinstance(str) guard on gateway .lower() calls

Preflight results throughout sprint:
March 22: 24 PASS / 0 FAIL ✅
March 23: 24 PASS / 0 FAIL ✅
March 24: 24 PASS / 0 FAIL ✅
March 25: 24 PASS / 0 FAIL ✅

Regression check: NONE — no regression failures observed.
─────────────────────────────────────────────────────────────

text

> **Note on gate count:** The preflight gate expanded from 20 PASS (March 22 pre-sprint baseline) to **24 PASS** as additional gate checks were added for consciousness pipeline services (Chroma reachability, WOAH status, RAG endpoint, bridge health) during the sprint. All 24 checks passed throughout.

**March 21, 2026 VERIFYANDTEST.sh baseline results (still current):**

- Services healthy: 32/32 (confirmed via `/selftestfabric`)
- LLM proxies healthy: 22/22 (HTTP 200; 21 contributing consensus)
- Docker containers running: 80+
- Ollama models available: 26
- PostgreSQL `msjarvis` (5433): ✅ CONNECTED — 5,416,521 GBIM entities
- PostgreSQL `gisdb` (5432): ✅ CONNECTED — PostGIS operational
- PostgreSQL `msjarvisgis` (5432): ✅ CONNECTED — 20,593 landowner beliefs
- PostgreSQL `jarvis-local-resources-db` (5435): ✅ CONNECTED
- Dual-BBB: `jarvis-blood-brain-barrier` (8016) ✅, `nbb_blood_brain_barrier` (8301) ✅
- STATUS: ✅ OPERATIONAL

### Ollama internal memory scheduler

Ollama's built-in scheduler acts as a hard resource watchdog. Current verified settings:

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

The `MAX_CONCURRENT_CHATS=2` environment variable on `jarvis-main-brain` is the session-level watchdog, limiting the number of simultaneous full chat pipelines. Current value of 2 represents the production-stable setting for the current hardware configuration.

### Redis-backed DynamicPortService

Five NBB containers register their health state to Redis (`jarvis-redis`, **host port 6380**, container-internal 6379) using `DynamicPortService` rather than fixed endpoints:

service:ms_jarvis_service:instance_1772240968
service:ms_jarvis_service:instance_1772240969
service:ms_jarvis_service:instance_1772240970
service:ms_jarvis_service:instance_1772240971
service:ms_jarvis_service:instance_1772240972

text

Each record contains `host`, `port`, `status`, `deployment`, `health_endpoint`, `started`, and `last_heartbeat` fields. Redis job state TTL is 30 minutes. Redis async status key is `'complete'` (not `'done'`).

---

## 35.6 Watchdog Alert Responses

**Memory exhaustion.** Ollama rejects model load requests exceeding available memory with a structured error. The 20llm-production service logs this as a proxy failure and excludes the model from consensus, maintaining ensemble function with the remaining models.

**Timeout.** Models exceeding the 240-second floor are logged as failures and excluded from consensus. The semaphore prevents cascading timeouts by serializing Ollama access to three concurrent slots maximum.

**BakLLaVA name-check guard.** BakLLaVA is permanently excluded via a name-check guard in the main-brain routing layer. The model name is detected before dispatch and the slot is bypassed with zero Ollama resource consumption.

**StarCoder2 0-char exclusion (OI-11 — UNCHANGED).** StarCoder2 (`llm7-proxy:8207`) passes VERIFYANDTEST.sh health checks (HTTP 200) but returns empty responses on community queries due to its code-specialization; it is excluded from consensus extraction. **OI-11 status is UNCHANGED as of March 25, 2026.** This was not addressed in the March 22–25 sprint. StarCoder2 remains in the health-monitored pool; future work will implement routing-layer fixes to dispatch code-specific queries to StarCoder2 and suppress community query dispatch.

**Session overload.** The `MAX_CONCURRENT_CHATS=2` gate causes main-brain to queue requests beyond the second concurrent session. Async jobs (`/chat/async`) use Redis (host port 6380, status key `'complete'`) for job state with 30-minute TTL.

**BBB content rejection (primary BBB — port 8016).** When content triggers a filter, it is rejected before reaching the LLM ensemble, conserving Ollama resources. `barrier_stats` counts are logged for PIA review (Chapter 29 §29.5).

**BBB output guard (Phase 4.5 — log+passthrough).** As of commit `18b8ddac` (March 22, 2026), Phase 4.5 is in log+passthrough mode. Filter results are logged but no response is blocked. The governance implication is documented in Chapter 38 §38.6.1. Output safety relies on Phase 1.4 input filter (blocking), judge pipeline `bbb_check_verdict` (live httpx POST), LM Synthesizer identity guard Layer 3, and `normalize_identity` persona enforcement.

**BBB output guard failure (port 8016).** If the BBB output guard returns HTTP 500, `apply_output_guards_async` fails open — the pipeline continues and delivers the response with `bbb_checked: false`. A pattern of `bbb_checked: false` entries in `ms_jarvis_memory` is a PIA review trigger.

**PostgreSQL connection loss.** VERIFYANDTEST.sh monitors all four PostgreSQL connection health states. Any `FAILED` status triggers immediate alerting and prevents ensemble operations that depend on PostgreSQL-sourced RAG context.

**0.0.0.0 exposure detection.** VERIFYANDTEST.sh includes a security watchdog check: `docker ps --format '{{.Names}} {{.Ports}}' | grep 0.0.0.0`. Any output from this check is a critical security regression. Expected output: empty (zero `0.0.0.0` exposures confirmed March 18, 2026, held throughout March 22–25 sprint).

**Consciousness pipeline service health (new — March 25, 2026).** Following the sprint patches (Chapter 25 §25.9), VERIFYANDTEST.sh and `preflight_gate.sh` now include consciousness pipeline service health as monitored gate items:

```bash
# Consciousness pipeline health checks (added as preflight gates during sprint):

# Chroma direct health (v2 API — rerouted per Patch 1):
curl -s http://127.0.0.1:8002/api/v2/heartbeat
# Expected: HTTP 200

# WOAH stdlib stub health:
curl -s http://jarvis-woah:7012/
# Expected: {"status": "ok", "service": "jarvis-woah", "port": 7012}

# RAG server endpoint health:
curl -s -o /dev/null -w "%{http_code}" \
  -X POST http://127.0.0.1:8003/query \
  -H "Content-Type: application/json" \
  -d '{"query": "test", "n_results": 1}'
# Expected: 200

# Consciousness bridge health:
curl -s http://127.0.0.1:8018/health
# Expected: {"status": "ok"} or similar
```

All four consciousness pipeline health gates were added to `preflight_gate.sh` during the sprint and are included in the 24 PASS count.

---

## 35.7 Integration with Barriers, Modes, and Containers

**Blood-brain barrier (primary — port 8016).** Every chat request passes through `jarvis-blood-brain-barrier:8016/filter` (Phase 1.4) before reaching the LLM ensemble. Phase 4.5 output guard is in log+passthrough mode (commit `18b8ddac`). This is the BBB referenced in all smoke tests in Chapter 41 and all PIA review procedures in Chapter 29.

**Blood-brain barrier (NBB-internal — port 8301).** `nbb_blood_brain_barrier:8301` operates on the NBB subconscious pathway. It is monitored by VERIFYANDTEST.sh and contributes to the NBB subconscious health report but does not participate in the main `ultimatechat` Phase 1.4 / Phase 4.5 pipeline.

**69-DGM cascade.** Every ensemble response routed through main-brain (port 8050) is validated by `jarvis-69dgm-bridge` at **host port 19000** (internal container port 9000) against PostgreSQL-grounded constitutional and community commitments.

**Psychology alignment layer.** The `jarvis-psychology-services:8019` service runs a psychological assessment on every request before the ensemble processes it.

**NBB subconscious layer.** Seven of eight NBB containers respond to health probes via their internal network endpoints, confirming the neurobiological simulation layer is active.

**Judge pipeline (compose-managed since March 18, 2026).** All five judge services (ports 7230–7233, 7239) are confirmed compose-managed with `restart: unless-stopped`. Judge verdicts are delivered as a full dict to `jarvis-blood-brain-barrier:8016/output_guard` at Phase 4.5.

**Consciousness bridge and brain orchestrator.** The consciousness bridge serves as mandatory infrastructure through which all swarm and watchdog operations flow. As of March 25, 2026, the consciousness bridge is confirmed OPERATIONAL following three sprint patches (Chapter 25 §25.9), and all four pipeline stages (Chroma CONNECTED, WOAH ACTIVE, RAG REACHABLE, Bridge OPERATIONAL) are monitored by the expanded preflight gate.

**ChromaDB memory integration.** ChromaDB host port is **8002** (`127.0.0.1:8002->8000/tcp`). Verification script outputs are structured for ingestion into the `operations_history` collection. Automated ingestion pipeline is designed but not yet active.

**PostgreSQL msjarvisgis integration.** PostgreSQL `msjarvisgis` at `127.0.0.1:5432` (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) serves as ground truth for BBB validation, 69-DGM cascade verification, RAG context sourcing, and VERIFYANDTEST.sh connection monitoring.

---

## 35.8 Open Items Related to Swarm and Watchdog Systems

| OI ID | Issue | Status |
|---|---|---|
| OI-11 | StarCoder2 exclusion — 0-char responses on community queries; routing-layer fix not yet implemented | ⚠️ **UNCHANGED** — not addressed in March 22–25 sprint |
| — | ChromaDB `operations_history` automated ingestion pipeline | ⚠️ OPEN — manual ingestion only |
| — | Automated alerting on VERIFYANDTEST.sh failure thresholds | ⚠️ OPEN — future work |
| — | Dynamic model tier selection based on query complexity | ⚠️ OPEN — future work |
| — | `jarvis-neurobiological-master` unreachable (consciousness pipeline) | ⚠️ OPEN — Chroma health check rerouted around it (Ch. 25 Patch 1); open item |
| — | RAG embedding end-to-end validation | ⚠️ IN PROGRESS — RAG REACHABLE; embedding roundtrip not yet fully validated |

---

## 35.9 Summary

Swarm functions and eternal watchdogs in the March 25, 2026 Ms. Jarvis deployment are running, verified, and logged against concrete evidence with PostgreSQL `msjarvisgis` as ground truth. The 22-slot LLM ensemble delivers 21/22 consensus participation on every warm-cache query with a judge pipeline consistency score of 0.975. **StarCoder2 (OI-11) remains excluded from consensus on community queries; this was not addressed in the March 22–25 sprint and its status is unchanged.**

**The March 22–25 sprint applied three consciousness pipeline bridge patches** (Chroma health check reroute, WOAH network fix + stdlib stub, gateway dict.lower() guard + RAG endpoint correction) and confirmed the consciousness pipeline OPERATIONAL (Chroma CONNECTED 200, WOAH ACTIVE stub, RAG REACHABLE, Bridge OPERATIONAL). **The preflight gate held at 24 PASS / 0 FAIL throughout the entire sprint with no regression failures introduced by any patch.** The gate expanded from 20 to 24 checks with the addition of consciousness pipeline health gates.

The dual-BBB architecture remains in place: `jarvis-blood-brain-barrier` (port 8016) is the primary judge pipeline output guard (Phase 4.5 in log+passthrough mode, commit `18b8ddac`); `nbb_blood_brain_barrier` (port 8301) is the NBB-internal neurobiological variant. Both are monitored by VERIFYANDTEST.sh. The five-layer watchdog system — VERIFYANDTEST.sh confirming 32/32 services operational plus four PostgreSQL connection health checks, Ollama memory scheduler, asyncio semaphore at slot 3, `MAX_CONCURRENT_CHATS=2` gate, and Redis DynamicPortService (host port 6380, async status key `'complete'`) — prevents cascade failures and protects the production system's stability under load.

---

*Last updated: March 25, 2026 by Carrie Kidd (Mamma Kidd), Oak Hill WV*
*Sprint validation: 24 PASS / 0 FAIL throughout March 22–25; OI-11 StarCoder2 exclusion unchanged; no regression from bridge/WOAH/RAG patches*

---

---

# 38. External Communication Channels and Authority Boundaries

Carrie Kidd (Mamma Kidd) · Mount Hope, WV
*Last updated: March 22, 2026*

---

> **Production context as of March 22, 2026:** This chapter has been updated from its earlier abstract form to reflect the concrete external communication and authority infrastructure verified in the live Ms. Jarvis stack. Key facts that were not present in the prior draft:
> - Public URL confirmed live: [https://egeria.mountainshares.us](https://egeria.mountainshares.us) — first public end-to-end chat response confirmed March 22, 2026 (21/21 LLMs responded, 106.5s, HTTP 200).
> - Token-based authority boundary tested March 22, 2026 — enforcement middleware not yet wired (OI-36-A / OI-36-B, tracked in Chapter 36).
> - BBB six-filter pipeline (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification) active at `127.0.0.1:8016` on all inbound and outbound paths.
> - Phase 4.5 BBB output in log+passthrough mode (commit `18b8ddac`, March 22, 2026) — was blocking 31% of community queries due to maternal Appalachian voice false positives; threshold recalibration is tracked future work.
> - All services bound exclusively to `127.0.0.1`. Zero `0.0.0.0` exposures. External traffic enters only through the unified gateway at port 8050 or through Cloudflare/reverse-proxy termination in front of `egeria.mountainshares.us`.
> - PostgreSQL: `msjarvis` port 5433 (5,416,521 GBIM entities); `gisdb` port 5432 (PostGIS); `jarvis-local-resources-db` port 5435.
> - Redis host port: 6380 (`127.0.0.1:6380->6379/tcp`). Redis async status key is `'complete'` (not `'done'`).
> - ChromaDB host port: 8002 (`127.0.0.1:8002->8000/tcp`).

This chapter describes how the system uses external communication channels — including the public web endpoint, email-class messaging, and hosting platforms — and how authority over these channels is constrained by governance, identity, and safeguard mechanisms. The focus is on roles, limits, and recording practices grounded in the verified production stack as of March 22, 2026.

---

## Why This Matters for Polymathmatic Geography

This chapter supports:

- **P1 – Every where is entangled** by ensuring that every outbound message or web-facing change can be traced back to GBIM beliefs, spatial records in PostgreSQL `gisdb` (port 5432), and the identity structures in Chapter 36.
- **P3 – Power has a geometry** by making authority over external channels explicit, bounded by roles and mode configuration rather than implicit in operational scripts.
- **P5 – Design is a geographic act** by treating the public URL [https://egeria.mountainshares.us](https://egeria.mountainshares.us) as a place — a community-facing surface that carries governance obligations toward Fayette County and West Virginia broadly.
- **P12 – Intelligence with a ZIP code** by keeping all inbound external traffic accountable to the BBB six-filter pipeline (port 8016) grounded in the spiritual, ethical, and community values of Appalachian communities.
- **P16 – Power accountable to place** by requiring that high-impact external actions be tied to registered identities (Chapter 36) under auditable rules backed by PostgreSQL `msjarvis` (port 5433).

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the governed external surface of Ms. Jarvis and the authority rules that constrain it.

---

## 38.1 Types of External Channels

Several kinds of external channels are relevant to the current deployment:

- **Public web endpoint** — [https://egeria.mountainshares.us](https://egeria.mountainshares.us), serving the Ms. Egeria Jarvis persona via the unified gateway at port 8050. Confirmed live March 22, 2026.
- **Messaging** — email accounts and similar mechanisms that can send and receive structured or unstructured text, used for reports, alerts, and outbound community communications.
- **Web and hosting interfaces** — connections to hosting, domain, and content delivery platforms used to publish or adjust web content or DNS configuration.
- **Cooperative and institutional platforms** — systems used by partner organizations (regional development authorities, nonprofits, universities) for coordination, registration, or record-keeping.

These channels extend the system's influence beyond its own infrastructure and therefore require clear authority boundaries enforced by token validation (Chapter 36), BBB filtering (Chapter 16), and mode constraints (Chapter 15).

---

## 38.2 The Public Endpoint: egeria.mountainshares.us

### 38.2.1 Confirmed Production State (March 22, 2026)

The public-facing URL [https://egeria.mountainshares.us](https://egeria.mountainshares.us) is the primary external communication surface for Ms. Jarvis as of March 22, 2026. Key verified facts:

- **First public end-to-end chat response:** confirmed March 22, 2026. Query: "What county is Mount Hope WV in?" Response: correct, delivered in authentic Ms. Egeria Jarvis maternal Appalachian voice. 21/21 LLMs responded. 106.5s end-to-end. HTTP 200.
- **Response identity verified:** No model names detected. No synthesis disclosure. No hedging language. Identity guard (Chapter 33 §33.5.1) confirmed working.
- All traffic enters through the unified gateway (`msjarvis_unified_gateway.py`, port 8050), then routes to `jarvis-main-brain` and the full pipeline.
- BBB input filter at `127.0.0.1:8016` (Phase 1.4) is active on all inbound traffic — six filters applied before any LLM call.
- BBB output guard at `127.0.0.1:8016` (Phase 4.5) is in log+passthrough mode (commit `18b8ddac`, March 22, 2026). See §38.6.1 for the governance implications.
- Pre-flight gate: **20 PASS 0 FAIL** (`scripts/preflight_gate.sh`, March 22, 2026 pre-sprint baseline) — all containers healthy before public exposure. Sprint expanded gate to **24 PASS / 0 FAIL** (see Chapter 35 §35.5).

### 38.2.2 Gateway and Port Architecture

All inbound external traffic is handled exclusively through the unified gateway:

External client → https://egeria.mountainshares.us
→ Cloudflare / reverse-proxy TLS termination
→ jarvis-main-brain (port 8050) / unified gateway
→ jarvis-semaphore (port 8030)
→ jarvis-20llm-production (port 8008) [21-LLM ensemble]
→ jarvis-judge-pipeline (port 7239) [4 judges parallel]
→ jarvis-lm-synthesizer (port 8001) [Phase 3.5 only]
→ BBB output guard (port 8016) [log+passthrough]
→ Response to client

text

All internal services are bound to `127.0.0.1`. Zero `0.0.0.0` exposures. No internal service port is reachable directly from outside the host.

---

## 38.3 Outbound Messages and Reports

Outbound communication is primarily used for reports, alerts, and community deliverables.

- **Generated messages** — the system can prepare messages summarizing analyses, status information, or proposals, based on internal records from PostgreSQL `msjarvis` (port 5433), ChromaDB collections (host port 8002), and current context. All outbound content passes through the LM Synthesizer identity guard (Chapter 33 §33.5.1) before delivery — no model names, no synthesis disclosure, no hedging language.
- **Sending conditions** — for higher-impact audiences or topics, sending requires that a registered identity with appropriate role explicitly approve the message content or trigger the send. Current production roles: `carrie_admin` (full authority) and `hayden_test` (scoped to non-administrative paths). See Chapter 36 §36.7 for the token registry.
- **Logging** — each message, including recipients, subject, and a reference to the content, is recorded in consciousness layer entries along with relevant mode and BBB filter state.

**Authority boundary note:** Token validation middleware is not yet wired into the gateway (OI-36-A, Chapter 36). Until OI-36-A is resolved, outbound high-impact actions should be confirmed via direct `carrie_admin` token verification through `jarvis_token_service.py` before execution.

---

## 38.4 Handling of Inbound Messages

Inbound messages — whether arriving via the public web endpoint, API calls, or future messaging integrations — are treated as external input and pass through the same protective structures as other outside content.

- **Ingestion** — messages are collected via the unified gateway (port 8050) and tagged with source, channel, and any available identity information (bearer token, if present).
- **BBB input filter** — all inbound content passes through the BBB six-filter pipeline at `127.0.0.1:8016` (Phase 1.4, ~0.6s) before it can influence memory, containers, or decision processes. The six filters are: EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, and truth_verification (current method: `heuristic_contradiction_v1` — see Chapter 33 §33.2.3 for honest limitations and the `rag_grounded_v2` upgrade path).
- **Phase 1.45 community memory** — after BBB input clearance, inbound content triggers a 384-dim semantic search of the `autonomous_learner` ChromaDB collection (21,181 records, growing ~288/day) via `all-minilm:latest`, prepending the top-5 community interaction records to the composite prompt sent to the 21-LLM ensemble.
- **Routing** — accepted messages are normalized and routed into appropriate consciousness layer paths or workflows, depending on content and intended purpose.

This keeps external messages from bypassing safeguards or overwhelming internal structures backed by PostgreSQL `msjarvis` (port 5433).

---

## 38.5 Hosting and DNS Interactions

Interfaces to hosting and domain-related platforms are handled conservatively.

- **Proposal over execution** — the system typically generates structured proposals for changes (updated content, configuration) that can be reviewed and applied by human operators before taking effect on live infrastructure.
- **Limited direct actions** — when direct calls to hosting or content delivery services are permitted, they are restricted to narrowly defined operations and subject to rate and scope limits. All calls are logged in consciousness layer entries.
- **Coupling to identity** — high-impact changes require that a `carrie_admin` token be active and that the request be tied to that role via `jarvis_token_service.py` (Chapter 36 §36.6). Until OI-36-A is resolved, this check must be performed manually rather than enforced automatically by the gateway middleware.
- **egeria.mountainshares.us DNS** — managed separately from the container stack. Changes to DNS or TLS configuration are human-operator actions, not automated pipeline actions in the current deployment.

---

## 38.6 Authority Boundaries and Modes

Authority over external channels is bounded by configuration, role, and context.

- **Role-based limits** — only `carrie_admin` tokens are authorized to initiate or approve external actions beyond simple reporting or low-risk updates. `hayden_test` tokens are scoped to non-administrative paths. See Chapter 36 §36.7 and §36.11 (OI-36-A, OI-36-B).
- **Mode-based limits** — in more restrictive modes, some channels may be disabled, restricted to read-only use, or limited to internal draft generation. The BBB operates fail-open on HTTP 500 (both Phase 1.4 input filter and Phase 4.5 output guard) — in the event of BBB unavailability, traffic passes through rather than being blocked. This is a deliberate design choice to maintain community access during infrastructure issues, with governance implications noted in §38.6.1.
- **Escalation paths** — when an action appears to exceed configured limits, it is paused and flagged for review rather than executed automatically. Judge pipeline verdicts of "fail" on any dimension (truth, consistency, alignment, ethics) trigger this path (Chapter 33 §33.9).

### 38.6.1 Phase 4.5 Log+Passthrough Mode — Governance Implication

As of March 22, 2026, the BBB output guard (Phase 4.5) is in log+passthrough mode (commit `18b8ddac`). This was applied because the output BBB was blocking 31% of community queries due to false positives on the maternal Appalachian voice used by Ms. Egeria Jarvis. Log+passthrough means:

- All responses still pass through `jarvis-blood-brain-barrier:8016/filter`.
- Filter results (all six dimensions) are logged in the consciousness layer `bbb_result` field on every `UltimateResponse`.
- No response is blocked by Phase 4.5 while in this mode — the filter output is for audit and calibration only.

**Governance implication:** The output BBB is not currently blocking harmful content at Phase 4.5. The input BBB (Phase 1.4) remains active and blocking. The judge pipeline BBB check (`bbb_check_verdict` in `judge_pipeline.py`, March 21, 2026) provides a second live filter against the consensus answer. Community-facing deployment with full Phase 4.5 enforcement requires threshold recalibration to eliminate false positives on Appalachian dialect — this is tracked as future work in Chapter 16 §16.9.

Until recalibration is complete, output safety relies on:

1. Phase 1.4 BBB input filter (active, blocking)
2. Judge pipeline BBB check via `bbb_check_verdict` (active, live httpx POST)
3. LM Synthesizer identity guard Layer 3 — meta-commentary prohibition (active)
4. `normalize_identity` persona enforcement (active)
5. Phase 4.5 BBB output — log+passthrough (active, non-blocking)

---

## 38.7 Recording, Audit, and Governance Links

External communications are tied back to governance structures.

- **Consciousness layer records** — each significant interaction with external channels writes entries to the judge-pipeline consciousness layer, including `consensus_score`, `judge_verdicts`, `bbb_checked`, and `bbb_result`. These are accessible via `/curator/background` and visible in `UltimateResponse` objects.
- **`autonomous_learner` growth** — every processed community interaction is stored in the `autonomous_learner` ChromaDB collection (21,181 records, growing ~288/day, host port 8002), building a local record of Appalachian community needs and interaction patterns over time.
- **Aggregated views** — summaries of external communications and infrastructure changes can be compiled from the consciousness layer for cooperative oversight bodies, regional development authorities (NRGRDA, New River Gorge RDA), and other stakeholders. High-consensus (> 0.9) judge-refined content signals readiness for publication (Chapter 33 §33.8).
- **Policy feedback** — patterns in external communication, such as frequent BBB false positives (as documented in Phase 4.5 above), motivate updates to policies, roles, and technical safeguards. The 31% false-positive finding directly caused the log+passthrough mode change and initiated the threshold recalibration work item.
- **Session contracts** — all significant external-facing changes (e.g., going live at `egeria.mountainshares.us`, auth boundary test results) are committed to `msjarvis-public-docs/docs/contract/SESSION-2026-03-22.md` (commit `d966351`) for audit continuity.

---

## 38.8 Open Items Related to External Communication Authority

### ⚠️ OI-38-A — Token Enforcement Not Active on Public Endpoint

**Status:** OPEN — March 22, 2026 (tracked also as OI-36-A in Chapter 36)

**Description:** [https://egeria.mountainshares.us](https://egeria.mountainshares.us) currently accepts unauthenticated requests with HTTP 200. Token validation middleware is not wired into the unified

