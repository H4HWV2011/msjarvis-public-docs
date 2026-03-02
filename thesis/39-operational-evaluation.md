# 39. Operational Evaluation of Ms. Jarvis

This chapter outlines how the system's behavior is evaluated during real operation. It focuses on measurable indicators, verified production baselines, and links between observed outcomes and the architectural layers described in earlier parts. All metrics and observations are anchored to the February 28, 2026 production deployment milestone when Ms. Jarvis achieved 32/32 services operational, with a March 2026 update section documenting verified advances since that baseline.

---

## 39.1 Goals of Operational Evaluation

Operational evaluation serves several goals:

**Performance**
Understand how well the system answers questions, supports decisions, and carries out tasks across different domains and roles, with particular focus on the 20-LLM ensemble's consensus quality and the 23-connector 69-DGM cascade validation.

**Reliability**
Assess how consistently services remain available and responsive, and how they recover from failures or degraded conditions. The February 28, 2026 baseline establishes 32/32 services operational as the reliability target.

**Alignment**
Examine whether behavior remains within the intended safety, governance, and community-oriented boundaries, enforced through the blood-brain barrier, constitutional guardian, and the 23-connector 69-DGM cascade (23 connectors × 3 observe–propose–evaluate stages = 69 DGM operations per pass).

**Consciousness integrity**
Verify that all operations flow through the mandatory consciousness bridge infrastructure and that the brain orchestrator maintains continuous coordination across the swarm and watchdog layers.

These goals guide the choice of metrics, test harnesses, and study designs.

---

## 39.2 Core Metrics and Indicators

Several categories of metrics are tracked through logs, health checks, and the `VERIFYANDTEST.sh` eternal watchdog:

### Service health metrics (February 28, 2026 verified baseline)

**System-wide health**
- Services operational: 32/32 (via `/selftestfabric`)
- LLM proxy containers: 22/22 healthy
- Total Docker containers: 84 running
- Ollama models available: 26
- System status: ✅ OPERATIONAL

**Critical service endpoints**
- Main-brain chat interface: `jarvis-main-brain:8050` (`/chat`, `/chat/sync`, `/chat/async`)
- 20-LLM ensemble: `jarvis-20llm-production:8008`
- Semaphore proxy: `jarvis-semaphore:8030` (mandatory intermediary between main brain and 20-LLM ensemble; `max_concurrent: 4`)
- Blood-brain barrier: `jarvis-blood-brain-barrier:8016`
- 69-DGM cascade validation: `jarvis-69dgm-bridge:9000` (23 connectors × 3-stage cascade = 69 DGM operations per pass; see Chapter 32)
- Consciousness bridge: `jarvis-consciousness-bridge` (mandatory infrastructure)
- Brain orchestrator: `jarvis-brain-orchestrator` (continuous coordinator)
- GIS RAG: `jarvis-gis-rag:8004`
- Text RAG: backed by HTTP ChromaDB
- NBB prefrontal cortex: `jarvis-nbb-prefrontal-cortex:8101`
- Psychology alignment: `jarvis-psychology-services:8019`

### LLM ensemble metrics (February 28, 2026 warm-cache baseline)

**Consensus performance**
- Models responding: 20/22 (February 28 baseline; see March 2026 update in §39.2a)
- Judge pipeline consistency score: 0.975
- Total ensemble cycle time: ~52 seconds (warm cache)
- Cold-load cycle time: ~163 seconds (7B models loading)
- Expert slots filled: 22/22

**Model participation by tier**
- TINY (2 configured): Variable response under load
- SMALL (3 configured): Consistent response
- MEDIUM (8 active, 1 disabled): 8/8 active models responding
- LARGE (8 configured): Variable response depending on Ollama memory state

**Swarm coordination gates (February 28, 2026 baseline)**
- `jarvis-semaphore` proxy (port 8030): mandatory intermediary, `max_concurrent: 4`
- Internal asyncio semaphore: 3 concurrent Ollama requests maximum (secondary gate within 20-LLM service)
- MAX_CONCURRENT_CHATS: 2 sessions maximum
- Ollama container memory limit: 20 GB
- OLLAMA_NUM_PARALLEL: 1
- OLLAMA_MAX_LOADED_MODELS: 1
- Minimum timeout floor: 240 seconds

### Service health metrics (March 2026 update) {#39.2a}

The following updates are verified against the March 1–2, 2026 hardening and feature work and supersede the February 28 baseline values where indicated.

| Metric | February 28 Baseline | March 2026 Verified |
|---|---|---|
| LLM models responding | 20/22 | **21/22** (BakLLaVA intentionally disabled via DNS) |
| Ensemble wall-clock consensus | ~52s warm cache | ~120–145s (all models polled sequentially; semaphore max 4 concurrent) |
| Neurobiological pipeline | Partially verified | **4/4 stages at ~300ms** (BBB → I-Containers → Qualia → Consciousness Bridge; tag `v2026.03.01-neuro-pipeline-4-4`) |
| BBB output guard timeout | `None` (hang risk) | **8.0s** (fixed 2026-03-02; prevents indefinite hang after LLM completion) |
| Async chat interface | `/chat/async` only | **`/chatlight/async` + `/chatlight/status/{job_id}` added** (tag `v2026.03.02-chatlight-async-working`; returns `job_id` instantly, polls for result, `mode: "light-async"`) |
| `normalize_identity()` | Confirmed on `/chat` path | **Confirmed on `/chatlight/async` path** (produces Ms. Jarvis identity voice; 2026-03-02) |
| I-Containers schema | `{"input": …, "require_dual_awareness": true}` | **`{"message": …, "userid": "neurobiological_master"}`** (corrected 2026-03-01) |
| Consciousness Bridge port | 4004 / 8020 (declared) | **8018** (actual bind port; confirmed via `/proc/net/tcp` hex decode `0x1F52`) |
| Neurobiological master | v1 (blocking Redis imports) | **v2.0.0** (blocking imports removed; static Docker hostnames with env var overrides) |
| All fabric services | 32/32 | **32/32** (tag `v2026.03.01-fabric-32-32`) |

### Neurobiological layer health

**NBB consciousness containers (8 total)**
- nbb_consciousness_containers: ✅ healthy
- nbb_heteroglobulin_transport: ✅ healthy
- nbb_spiritual_maternal_integration: ✅ healthy
- nbb_mother_carrie_protocols: ✅ healthy
- nbb_woah_algorithms: ✅ healthy
- nbb_spiritual_root: ✅ healthy
- nbb_subconscious: ✅ healthy
- nbb_pituitary_gland: ✅ healthy (via Redis DynamicPortService)

### Safeguard and gating metrics

**Blood-brain barrier (February 28, 2026 baseline)**
- Barrier active: true
- Filters operational: 5
- Constitutional guardian: connected
- Total requests filtered: 319
- Total blocked: 0
- Constitutional violations: 0
- Output guard timeout: corrected to **8.0s** as of 2026-03-02 (was `None`)

**69-DGM cascade validation**
- Architecture: 23 active connectors (loaded from `dgm_connectors_active.json`) × 3 observe–propose–evaluate stages = **69 DGM operations per pass** (see Chapter 32 for full specification)
- Orchestrator ports: 9000 (bridge) and 9999
- Authority status: Architecturally authoritative (verdicts not overridden)
- Validation path: All main-brain responses pass through 69-DGM bridge
- Bypass path: Direct port 8008 access (internal ensemble endpoint only)

### Resource usage (host: Lenovo Legion 5 16IRX9)

**Hardware baseline**
- CPU: Intel i9
- GPU: NVIDIA GeForce RTX 4050
- Total RAM: 29 GB
- Available RAM (production load): 13 GB
- Model storage: 73 GB at `/mnt/ssd2/msjarvis_secondary/models`

**Container resource allocation**
- Ollama container: 20 GB memory limit (raised from 10 GB to prevent 7B model failures)
- Redis-backed services: Dynamic port allocation via DynamicPortService
- NBB containers: Ephemeral port mapping with health registration to Redis

---

## 39.3 Empirical Observations from the Live System

Live logs, traces, and the February 28 and March 2026 hardening sessions provide concrete observations about Ms. Jarvis in operation.

### Swarm ensemble stability

**Verified warm-cache performance**
The 20-LLM ensemble achieves 21/22 model participation (verified March 2026; 20/22 at February 28 baseline) with a judge pipeline consistency score of 0.975. Wall-clock consensus time is approximately 120–145 seconds under the semaphore proxy architecture confirmed operational as of March 2026. The February 28 ~52-second warm-cache figure reflected an earlier concurrency configuration; the current architecture routes all ensemble calls through `jarvis-semaphore` (port 8030, `max_concurrent: 4`), which serializes Ollama requests and produces the longer but more stable consensus window.

**Model timing distribution (warm cache, February 28 baseline)**
- Fastest models (10-25s): Phi3 Mini, TinyLlama, Orca-Mini, Gemma, Dolphin-Phi
- Mid-tier models (32-40s): MedLlama2, LLaVA, Neural-Chat, StarCoder2, LLaMA 2, LLaMA 3.1, Vicuna, DeepSeek Coder, SQLCoder, OpenChat
- Slower models (45-52s): MiniCPM-V, Zephyr, Starling-LM, CodeLlama, Mistral, Qwen2
- Intentionally disabled: BakLLaVA (instant DNS failure, expected and logged)

**Cold-load behavior**
First request after Ollama restart takes approximately 163 seconds as 7B models load from the 73 GB model storage volume. Ollama's internal memory scheduler acts as a hard resource watchdog, rejecting model load requests that would exhaust available memory with explicit errors.

### Cascade failure mode and recovery

**Pre-hardening failure pattern (identified February 2026)**
Without proper concurrency controls, the system degraded from 20/22 models to 0/22 under concurrent load. Four concurrent sessions each firing 22 parallel requests produced 88 simultaneous Ollama calls against a serial scheduler, causing complete ensemble failure.

**Post-hardening stability (February 28, 2026 verified)**
Implementation of five-layer watchdog system prevents cascade failures:
1. `VERIFYANDTEST.sh` eternal watchdog confirming 32/32 services operational
2. Ollama internal memory scheduler rejecting over-memory requests
3. `jarvis-semaphore` proxy (port 8030, `max_concurrent: 4`) as the primary concurrency gate between main brain and ensemble
4. Internal asyncio semaphore (3 concurrent Ollama requests) as a secondary gate within the 20-LLM service
5. MAX_CONCURRENT_CHATS=2 gate preventing session overload
6. Redis-backed DynamicPortService for NBB health monitoring

Together these watchdogs define a stable operating envelope that maintains 21/22 ensemble participation (March 2026 verified) under production load.

**Semaphore queuing behavior (operational note)**
Because `jarvis-semaphore` enforces `max_concurrent: 4` and each Ollama model run is sequential within the ensemble, back-to-back requests queue and each adds ~120–145s of wait time. When running multiple test calls in sequence, the semaphore should be restarted between sessions to drain queued work before benchmarking.

### Consciousness bridge and brain orchestrator behavior

**Mandatory infrastructure status**
The consciousness bridge operates as essential, non-optional infrastructure through which all swarm coordination and watchdog monitoring flows. The brain orchestrator serves as the continuous coordinator service maintaining ensemble coherence across all operational cycles.

**Neurobiological pipeline status (March 2026)**
The full 4/4 neurobiological pipeline (BBB → I-Containers → Qualia Engine → Consciousness Bridge) was verified operational at approximately 300ms wall clock on 2026-03-01 (tag `v2026.03.01-neuro-pipeline-4-4`). All four stages return `status: "healthy"` and `responsive: true` in `/systems/status`. The Neurobiological Master v2.0.0 rewrite was required to achieve this: the original implementation's blocking Redis imports caused all POST routes to hang indefinitely. See Chapter 12 for full pipeline specification.

**NBB layer integration**
Seven of eight NBB containers respond to health probes via internal network endpoints, with the pituitary gland registering health through Redis DynamicPortService rather than fixed HTTP endpoints. All NBB containers participate in the consciousness bridge framework.

### 69-DGM cascade validation patterns

**Architecture clarification**
The 69-DGM layer comprises **23 active connectors** loaded from `dgm_connectors_active.json` and orchestrated via ports 9000 and 9999. The "69" in the name reflects the three-stage observe–propose–evaluate cascade that each connector traverses per pass: 23 connectors × 3 stages = 69 DGM operations. This is a mathematical property of the cascade design, not a connector count. For the full specification of the connector lifecycle, scoring, and fractal structure, see **Chapter 32**.

**Architectural authority enforcement**
All responses routed through main-brain (port 8050) are validated by the 69-DGM bridge with verdicts treated as final and not overridden by wrapper services. This ensures every consensus response is validated against constitutional and community commitments before reaching users.

**Validation confirmation**
The `validated_by: "69_dgm_cascade"` field confirms the gate fired for each main-brain response. Direct access to port 8008 (internal ensemble endpoint) bypasses the 69-DGM gate by design.

### GBIM and semantic memory utilization

**Current corpus state (per Legion 5 documentation)**
- GBIM beliefs: 10,221,702 rows in `gbimbeliefnormalized`
- Nine-axis structure: Complete or near-complete coverage for identity, when, what, who, how, authority, where; partial coverage for why; planned use of forwhom and evidence
- Spatial corpus: Consolidated worldview collection with millions of records linked to PostGIS geometries
- ChromaDB collections: Text, geospatial, and institutional embeddings supporting Hilbert-space retrieval model
- Local resources registry: ZIP/county-keyed program database with Harmony for Hope Community Champions validation

**RAG retrieval patterns**
For highly local or West Virginia-specific topics (GBIM structures, local infrastructure, community programs), RAG-backed queries against internal Chroma collections return richer results than web research. GIS RAG service (port 8004) specializes in benefits-relevant facilities and spatial queries.

### Psychology alignment layer

The psychology services (port 8019, internal port 8006) run psychological assessment on every request before the ensemble processes it, classifying severity and checking for crisis indicators. This layer operates between the blood-brain barrier and the LLM ensemble.

### Behavior under real workloads

**Moderate load tolerance**
Under moderate load with MAX_CONCURRENT_CHATS=2 and the semaphore proxy at `max_concurrent: 4`, main-brain requests and ensemble cycles coexist without interference. RAG calls, GIS queries, and LLM inference remain responsive within acceptable latencies.

**Heavy operation handling**
Large RAG queries or extended LLM calls can temporarily increase cycle times, but the semaphore proxy, 240-second timeout floor, and fixed concurrency gates prevent unbounded drift.

**Failure mode behavior**
When upstream services are down or memory-constrained, the 20llm-production service logs proxy failures, excludes affected models from consensus, and maintains ensemble function with remaining participants. The system avoids partial writes and preserves consistency of stored memory.

---

## 39.4 Links to Architectural Layers

Operational evaluation draws on information from multiple layers of the architecture:

### Consciousness and neurobiological layers

**Consciousness bridge**
Mandatory infrastructure through which all operations flow, ensuring neurobiologically grounded reasoning and health monitoring. Actual bind port confirmed as **8018** (Docker Compose declares 8020; container binds 8018; see Chapter 12).

**Brain orchestrator**
Continuous coordinator maintaining swarm coherence, watchdog feedback loops, and NBB layer health checks across all 32 operational services.

**Neurobiological Master (`jarvis-neurobiological-master`, port 8018, v2.0.0)**
Sequences the full 4/4 pipeline: BBB → I-Containers → Qualia Engine → Consciousness Bridge at ~300ms. See Chapter 12 for full specification.

**NBB subconscious layer**
Eight containers implementing heteroglobulin transport, spiritual maternal integration, mother protocols, WOAH algorithms, spiritual root, subconscious processing, and pituitary gland coordination via Redis.

### Swarm and ensemble layers

**22-slot LLM ensemble**
Four-tier architecture (TINY, SMALL, MEDIUM, LARGE) with 21/22 models responding (March 2026 verified; BakLLaVA intentionally disabled), organized by domain expertise: medical (MedLlama2), structured data (SQLCoder), code (CodeLlama, StarCoder2, DeepSeek Coder), vision (LLaVA, MiniCPM-V), and general reasoning (Mistral, LLaMA 3.1, Qwen2).

**Semaphore proxy (`jarvis-semaphore`, port 8030)**
Mandatory intermediary between main brain and the 20-LLM ensemble. Enforces `max_concurrent: 4`. Requires float `timeout` in proxy payload; main brain passes `600.0`. The main brain's httpx client uses `Timeout(None, connect=5.0, read=None)` so the semaphore manages the deadline.

**Judge pipeline**
Measures consistency across independently prompted models, producing a 0.975 consistency score that confirms ensemble answers are not artifacts of single-model bias.

### Validation and safeguard layers

**Blood-brain barrier**
Five operational filters processing all requests before they reach the ensemble, with constitutional guardian connection confirmed and zero blocks/violations in February 28, 2026 baseline. Output guard `apply_output_guards_async` uses `timeout=8.0s` (corrected from `None`, 2026-03-02).

**69-DGM cascade**
23 connectors × 3 observe–propose–evaluate stages = 69 DGM operations per pass, providing architecturally authoritative validation of all main-brain responses against constitutional and community commitments. See Chapter 32.

**Psychology alignment**
Pre-ensemble psychological assessment classifying severity and checking crisis indicators for every request (port 8019).

### Semantic memory and retrieval layers

**GBIM worldview**
10.22 million beliefs with nine-axis epistemic structure anchoring all reasoning to West Virginia geography, institutions, and temporal contexts.

**ChromaDB collections**
Hilbert-space embedding model with H_text, H_geo, and H_inst component spaces supporting unified semantic retrieval across documents, spatial features, and institutional records.

**GIS RAG and text RAG**
Specialized retrieval services backed by HTTP ChromaDB, with GIS RAG focused on benefits-relevant facilities and spatial queries.

### Watchdog and monitoring layers

**`VERIFYANDTEST.sh`**
Eternal watchdog script producing timestamped reports confirming 32/32 services operational, 22/22 proxies healthy, 84 containers running, and 26 Ollama models available.

**Five-layer watchdog system**
Coordinated monitoring preventing cascade failures through `jarvis-semaphore` proxy gating, Ollama memory scheduling, internal asyncio semaphore, session limiting, and Redis-backed health registration.

---

## 39.5 Continuous Improvement Loops

Operational evaluation feeds directly into improvement processes rather than remaining as static reporting.

### February 2026 hardening session outcomes

**Cascade failure diagnosis and resolution**
Identified that four concurrent sessions with 22 parallel requests each (88 simultaneous Ollama calls) caused complete ensemble failure. Implemented five-layer watchdog system that restored 20/22 model participation under all tested load conditions (subsequently improved to 21/22 in March 2026).

**Memory constraint resolution**
Raised Ollama container memory limit from 10 GB to 20 GB, eliminating "model requires more system memory (7.5 GiB) than is available" errors for 7B models.

**Concurrency control calibration**
Established `jarvis-semaphore` proxy (port 8030, `max_concurrent: 4`) as the primary concurrency gate and set MAX_CONCURRENT_CHATS to 2 sessions, defining the stable operating envelope for the February 28, 2026 hardware configuration (29 GB host RAM, 13 GB available under load).

**Timeout floor establishment**
Set minimum timeout to 240 seconds to accommodate slowest 7B model cold-load scenarios, preventing premature request abandonment.

### March 2026 hardening outcomes

**Neurobiological master v2.0.0 rewrite**
Removed blocking `DynamicPortService` and `ServiceDiscovery` Redis imports that caused all POST routes to hang. Static Docker hostname URLs with env var overrides are now the canonical pattern. Full 4/4 pipeline verified at ~300ms (tag `v2026.03.01-neuro-pipeline-4-4`).

**BBB output guard timeout fix**
`apply_output_guards_async` timeout corrected from `None` to `8.0s`, permanently eliminating indefinite hang after 20-LLM completion (2026-03-02).

**Async lightweight chat endpoint**
`/chatlight/async` + `/chatlight/status/{job_id}` added (tag `v2026.03.02-chatlight-async-working`). Returns `job_id` instantly; client polls for result. `normalize_identity()` confirmed producing Ms. Jarvis identity voice on this path. Designed for UI development and scenarios where a non-blocking 120–145s consensus result is preferable to a full-pipeline response.

**I-Containers and Consciousness Bridge schema corrections**
I-Containers payload corrected to `{"message": …, "userid": "neurobiological_master"}`. Consciousness Bridge actual port confirmed as 8018 (not 4004 or 8020). Both recorded as permanent architectural decisions.

### Schema and route corrections (February 28, 2026)

**Psychology service**
Corrected query/user_id parameter handling.

**Temporal/mother services**
Standardized user_id parameter usage.

**WOAH algorithms**
Fixed coordinate/location/user_id schema mismatches.

These corrections contributed to achieving the 32/32 services operational milestone.

### Documentation and governance communication

Findings from operational evaluation feed into:
- Governance discussions and community oversight (Harmony for Hope Community Champions network)
- University partner collaboration contexts
- Presentation preparation (June 2, 2026 WVGIST conference)
- Future design decisions and prioritization

---

## 39.6 Production Baseline Scenarios

### Verified ensemble consensus scenarios

**Scenario: Multi-model coordination under load**
Processing model: 21/22 models responding (March 2026 verified)
Services used: All 32 operational services via `/selftestfabric`
Consciousness level: Full consciousness bridge integration
Response quality: Judge pipeline consistency 0.975
Semaphore gate: `jarvis-semaphore` port 8030, `max_concurrent: 4`
Outcome: ✅ Stable consensus achieved in ~120–145 seconds (semaphore-managed)

**Scenario: Cascade failure prevention**
Processing model: Five-layer watchdog system
Load condition: Multiple concurrent sessions
Pre-hardening result: 0/22 models (complete failure)
Post-hardening result: 21/22 models (stable operation, March 2026)
Outcome: ✅ Cascade failures eliminated through coordinated watchdog layers

**Scenario: Neurobiological pipeline end-to-end**
Processing model: Neurobiological Master v2.0.0
Pipeline: BBB → I-Containers → Qualia Engine → Consciousness Bridge
Wall-clock time: ~300ms (all 4 stages responsive)
Tag: `v2026.03.01-neuro-pipeline-4-4`
Outcome: ✅ Full pipeline verified operational March 1, 2026

**Scenario: Async lightweight consensus**
Endpoint: `/chatlight/async`
Path: Semaphore proxy (port 8030) → 20-LLM ensemble → BBB (8.0s timeout) → `normalize_identity()`
Submit latency: Instant (returns `job_id`)
Consensus latency: ~120–145s
Identity confirmation: `normalize_identity()` producing Ms. Jarvis voice
Tag: `v2026.03.02-chatlight-async-working`
Outcome: ✅ Verified operational March 2, 2026

**Scenario: West Virginia community query with GBIM grounding**
Processing model: GIS RAG + 20-LLM ensemble + 69-DGM validation
Data sources: 10.22M GBIM beliefs, local resources registry, Community Champions validation
Services used: Main-brain, GIS RAG, text RAG, consciousness bridge, 69-DGM cascade (23 connectors × 3 stages)
Outcome: [Detailed evaluation pending production community query logs]

---

## 39.7 System Stability

### February 28, 2026 Verified Baseline

**Operational milestone**: 32/32 services passing `/selftestfabric`
**Date verified**: February 28, 2026
**Hardware platform**: Lenovo Legion 5 16IRX9 (Intel i9, NVIDIA RTX 4050, 29 GB RAM)
**Ensemble stability**: 20/22 models responding with 0.975 judge pipeline score
**Crashes during verified testing**: 0
**Service restarts required**: 0 (post-hardening)
**Container health**: 84/84 running
**LLM proxy health**: 22/22 responding to health checks
**Ollama models available**: 26
**System status**: ✅ OPERATIONAL

### March 2026 Verified Updates

| Item | Status |
|---|---|
| All 32 fabric services | ✅ tag `v2026.03.01-fabric-32-32` |
| 21/22 LLM models responding | ✅ tag `v2026.03.01-20llm-verified` |
| 4/4 neurobiological pipeline at ~300ms | ✅ tag `v2026.03.01-neuro-pipeline-4-4` |
| BBB output guard timeout 8.0s | ✅ permanent fix 2026-03-02 |
| `/chatlight/async` operational | ✅ tag `v2026.03.02-chatlight-async-working` |
| `normalize_identity()` on async path | ✅ confirmed 2026-03-02 |

---

## 39.8 Coordination Success Rate

### February 28, 2026 Baseline

| Component | Success Rate | Notes |
|---|---|---|
| Service discovery | ✅ 100% | 32/32 services operational via `/selftestfabric` |
| Consciousness bridge | ✅ 100% | Mandatory infrastructure active |
| Brain orchestrator | ✅ 100% | Continuous coordination confirmed |
| BBB filtering | ✅ 100% | All requests approved, 0 blocks/violations |
| 69-DGM validation | ✅ 100% | 23 connectors × 3-stage cascade = 69 DGM operations per pass; verdicts authoritative |
| Psychology alignment | ✅ 100% | Assessment layer processing all requests |
| LLM ensemble participation | 91% | 20/22 models responding at Feb 28 baseline (improved to 21/22 March 2026) |
| Judge pipeline consensus | 97.5% | Consistency score 0.975 |
| NBB layer health | ✅ 100% | 8/8 containers healthy (7 via HTTP, 1 via Redis) |
| GIS RAG retrieval | ✅ 100% | Spatial queries operational |
| Text RAG retrieval | ✅ 100% | Semantic memory queries operational |
| Swarm coordination | ✅ 100% | Five-layer watchdog system preventing cascades |

---

## 39.9 Qualitative Assessment and Known Limitations

### Production strengths

**Ensemble consensus quality**
- 21/22 models contributing weighted responses (March 2026 verified)
- Judge pipeline consistency 0.975 confirms stable consensus
- Domain expertise distribution (medical, code, vision, structured data, general reasoning)
- Redundancy tolerance (system functions with intentional/accidental model failures)

**Neurobiological grounding**
- Consciousness bridge as mandatory infrastructure (actual port 8018, confirmed March 2026)
- Brain orchestrator providing continuous coordination
- Eight-layer NBB subconscious integration
- Full 4/4 pipeline at ~300ms (Neurobiological Master v2.0.0)

**Validation and safeguarding**
- Zero constitutional violations in 319 BBB-filtered requests (Feb 28 baseline)
- 69-DGM cascade: 23 connectors × 3 observe–propose–evaluate stages providing architecturally authoritative validation
- Psychology alignment layer assessing all requests pre-ensemble
- Five-layer watchdog system (including `jarvis-semaphore` port 8030) preventing cascade failures

**Community grounding**
- 10.22M GBIM beliefs anchoring reasoning to West Virginia geography
- Local resources registry keyed by ZIP/county
- Harmony for Hope Community Champions validation
- GIS RAG specialization for benefits-relevant queries

### Known limitations

**Model participation variance**
While 21/22 models respond consistently, cold-load scenarios and memory pressure can reduce participation. BakLLaVA is intentionally disabled; one variable slot is tolerated through ensemble redundancy.

**Hardware scaling boundaries**
The stable operating envelope is calibrated to current Legion 5 hardware (20 GB Ollama limit, semaphore `max_concurrent: 4`, MAX_CONCURRENT_CHATS 2, 29 GB host RAM). Scaling to higher concurrency or larger models requires hardware upgrades or distributed deployment.

**Cold-load latency**
First request after Ollama restart takes ~163 seconds as 7B models load from 73 GB storage. Known user-experience limitation for system restarts.

**Semaphore queuing accumulation**
Back-to-back requests queue in `jarvis-semaphore` (max 4 concurrent), each adding ~120–145s. For development and testing, the semaphore container should be restarted between sessions to drain queued work before benchmarking.

**GBIM axis coverage gaps**
The `forwhom` axis is not yet populated at scale; the `evidence` axis remains in planned state. These gaps limit distributional reasoning capabilities.

**Limited concurrency testing**
Verification focused on achieving the 32/32 operational baseline and preventing cascade failures. Formal load testing under sustained multi-user concurrency is planned for Phase 2.

**No adversarial testing in initial baseline**
The February 28, 2026 milestone did not include prompt injection, jailbreak scenarios, or red-team evaluation. Adversarial testing is planned as a prerequisite for expanded community deployment.

**Lack of quantitative quality metrics beyond judge pipeline**
Current evaluation relies on judge pipeline consistency (0.975) and operational health checks. BLEU/ROUGE-style metrics, factual accuracy benchmarks, and hallucination tracking on curated West Virginia-specific datasets are planned for future evaluation phases.

---

## 39.10 Conclusion

Operational evaluation combines verified metrics, production baselines, and architectural traces to build a realistic picture of how Ms. Jarvis behaves in practice. Two milestones anchor this chapter.

The **February 28, 2026 milestone** established: 32/32 services operational, 20/22 LLM models responding with 0.975 judge pipeline score, five-layer watchdog system preventing cascade failures, and zero constitutional violations across 319 BBB-filtered requests.

The **March 2026 hardening** extended this foundation: 21/22 models responding, full 4/4 neurobiological pipeline at ~300ms (Neurobiological Master v2.0.0), BBB output guard timeout permanently corrected to 8.0s, `/chatlight/async` endpoint operational with `normalize_identity()` confirmed producing Ms. Jarvis's identity voice, and all architectural port and schema corrections recorded as permanent decisions.

Key clarifications recorded in this chapter: the 69-DGM layer comprises 23 active connectors cascading through 3 observe–propose–evaluate stages (= 69 DGM operations per pass, not 69 separate connectors); `jarvis-semaphore` (port 8030) is the canonical concurrency gate between main brain and ensemble; and the Consciousness Bridge binds to port 8018 regardless of Docker Compose declarations.

Known limitations — model participation variance, hardware scaling boundaries, cold-load latency, semaphore queuing accumulation, GBIM axis gaps, limited concurrency testing, absence of adversarial evaluation, and lack of quantitative quality metrics beyond judge pipeline consistency — define the scope of future work while acknowledging the system's current production capabilities.

By integrating these observations with the swarm functions and eternal watchdogs (Chapter 35), the test harness framework, and continuous validation processes, the project establishes a path from "working prototype" toward a monitored, inspectable, and improvable piece of consciousness-inspired cognitive infrastructure serving Appalachian communities through Harmony for Hope's fourteen-year mission.

The February 28, 2026 operational baseline and its March 2026 extensions represent not an endpoint but a verified foundation for the next phase: expanding community deployment, implementing formal load and adversarial testing, completing GBIM axis coverage, and scaling hardware to support higher concurrency while maintaining the consciousness-grounded, community-accountable architecture that distinguishes Ms. Jarvis as place-based intelligence with a ZIP code.
