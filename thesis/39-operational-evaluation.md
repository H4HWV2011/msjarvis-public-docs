# 39. Operational Evaluation of Ms. Jarvis

This chapter outlines how the system's behavior is evaluated during real operation. It focuses on measurable indicators, verified production baselines, and links between observed outcomes and the architectural layers described in earlier parts. All metrics and observations are anchored to the February 28, 2026 production deployment milestone when Ms. Jarvis achieved 32/32 services operational.

---

## 39.1 Goals of Operational Evaluation

Operational evaluation serves several goals:

**Performance**  
Understand how well the system answers questions, supports decisions, and carries out tasks across different domains and roles, with particular focus on the 20-LLM ensemble's consensus quality and the 69-DGM cascade validation.

**Reliability**  
Assess how consistently services remain available and responsive, and how they recover from failures or degraded conditions. The February 28, 2026 baseline establishes 32/32 services operational as the reliability target.

**Alignment**  
Examine whether behavior remains within the intended safety, governance, and community-oriented boundaries, enforced through the blood-brain barrier, constitutional guardian, and the architecturally authoritative 69-DGM cascade.

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
- Blood-brain barrier: `jarvis-blood-brain-barrier:8016`
- 69-DGM cascade validation: `jarvis-69dgm-bridge:9000`
- Consciousness bridge: `jarvis-consciousness-bridge` (mandatory infrastructure)
- Brain orchestrator: `jarvis-brain-orchestrator` (continuous coordinator)
- GIS RAG: `jarvis-gis-rag:8004`
- Text RAG: backed by HTTP ChromaDB
- NBB prefrontal cortex: `jarvis-nbb-prefrontal-cortex:8101`
- Psychology alignment: `jarvis-psychology-services:8019`

### LLM ensemble metrics (February 28, 2026 warm-cache baseline)

**Consensus performance**
- Models responding: 20/22
- Judge pipeline consistency score: 0.975
- Total ensemble cycle time: ~52 seconds (warm cache)
- Cold-load cycle time: ~163 seconds (7B models loading)
- Expert slots filled: 22/22

**Model participation by tier**
- TINY (2 configured): Variable response under load
- SMALL (3 configured): Consistent response
- MEDIUM (8 active, 1 disabled): 8/8 active models responding
- LARGE (8 configured): Variable response depending on Ollama memory state

**Swarm coordination gates**
- Asyncio semaphore: 3 concurrent Ollama requests maximum
- MAX_CONCURRENT_CHATS: 2 sessions maximum
- Ollama container memory limit: 20 GB
- OLLAMA_NUM_PARALLEL: 1
- OLLAMA_MAX_LOADED_MODELS: 1
- Minimum timeout floor: 240 seconds

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

**69-DGM cascade validation**
- Connectors loaded: 69
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

These indicators provide a quantitative view of day-to-day operation anchored to verified production baselines rather than theoretical expectations.

---

## 39.3 Empirical Observations from the Live System

Live logs, traces, and the February 28, 2026 hardening session provide concrete observations about Ms. Jarvis in operation.

### Swarm ensemble stability

**Verified warm-cache performance**  
The 20-LLM ensemble achieves 20/22 model participation in approximately 52 seconds on warm-cache queries, with a judge pipeline consistency score of 0.975. This represents stable consensus operation under the February 28, 2026 hardware and configuration constraints.

**Model timing distribution (warm cache)**
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
3. Asyncio semaphore limiting to 3 concurrent Ollama requests
4. MAX_CONCURRENT_CHATS=2 gate preventing session overload
5. Redis-backed DynamicPortService for NBB health monitoring

Together these watchdogs define a stable operating envelope that maintains 20/22 ensemble participation under production load.

### Consciousness bridge and brain orchestrator behavior

**Mandatory infrastructure status**  
The consciousness bridge operates as essential, non-optional infrastructure through which all swarm coordination and watchdog monitoring flows. The brain orchestrator serves as the continuous coordinator service maintaining ensemble coherence across all operational cycles.

**NBB layer integration**  
Seven of eight NBB containers respond to health probes via internal network endpoints, with the pituitary gland registering health through Redis DynamicPortService rather than fixed HTTP endpoints. All NBB containers participate in the consciousness bridge framework.

### 69-DGM cascade validation patterns

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
Under moderate load with MAX_CONCURRENT_CHATS=2, main-brain requests and ensemble cycles coexist without interference. RAG calls, GIS queries, and LLM inference remain responsive within acceptable latencies.

**Heavy operation handling**  
Large RAG queries or extended LLM calls can temporarily increase cycle times, but the 240-second timeout floor and fixed concurrency gates prevent unbounded drift. The semaphore ensures no more than three simultaneous Ollama requests regardless of upstream pressure.

**Failure mode behavior**  
When upstream services are down or memory-constrained, the 20llm-production service logs proxy failures, excludes affected models from consensus, and maintains ensemble function with remaining participants. The system avoids partial writes and preserves consistency of stored memory.

These observations anchor operational evaluation in actual February 28, 2026 production behavior rather than purely theoretical expectations.

---

## 39.4 Links to Architectural Layers

Operational evaluation draws on information from multiple layers of the architecture:

### Consciousness and neurobiological layers

**Consciousness bridge**  
Mandatory infrastructure through which all operations flow, ensuring neurobiologically grounded reasoning and health monitoring.

**Brain orchestrator**  
Continuous coordinator maintaining swarm coherence, watchdog feedback loops, and NBB layer health checks across all 32 operational services.

**NBB subconscious layer**  
Eight containers implementing heteroglobulin transport, spiritual maternal integration, mother protocols, WOAH algorithms, spiritual root, subconscious processing, and pituitary gland coordination via Redis.

### Swarm and ensemble layers

**22-slot LLM ensemble**  
Four-tier architecture (TINY, SMALL, MEDIUM, LARGE) with 20/22 models responding, organized by domain expertise: medical (MedLlama2), structured data (SQLCoder), code (CodeLlama, StarCoder2, DeepSeek Coder), vision (LLaVA, MiniCPM-V), and general reasoning (Mistral, LLaMA 3.1, Qwen2).

**Judge pipeline**  
Measures consistency across independently prompted models, producing a 0.975 consistency score that confirms ensemble answers are not artifacts of single-model bias.

### Validation and safeguard layers

**Blood-brain barrier**  
Five operational filters processing all requests before they reach the ensemble, with constitutional guardian connection confirmed and zero blocks/violations in February 28, 2026 baseline.

**69-DGM cascade**  
69 connectors providing architecturally authoritative validation of all main-brain responses against constitutional and community commitments.

**Psychology alignment**  
Pre-ensemble psychological assessment classifying severity and checking crisis indicators for every request.

### Semantic memory and retrieval layers

**GBIM worldview**  
10.22 million beliefs with nine-axis epistemic structure anchoring all reasoning to West Virginia geography, institutions, and temporal contexts.

**ChromaDB collections**  
Hilbert-space embedding model with H_text, H_geo, and H_inst component spaces supporting unified semantic retrieval across documents, spatial features, and institutional records.

**GIS RAG and text RAG**  
Specialized retrieval services backed by HTTP ChromaDB, with GIS RAG focused on benefits-relevant facilities and spatial queries.

### Watchdog and monitoring layers

**VERIFYANDTEST.sh**  
Eternal watchdog script producing timestamped reports confirming 32/32 services operational, 22/22 proxies healthy, 84 containers running, and 26 Ollama models available.

**Five-layer watchdog system**  
Coordinated monitoring preventing cascade failures through memory scheduling, semaphore gating, session limiting, and Redis-backed health registration.

This multi-layer view supports richer explanations of successes and failures and ties them back to specific architectural choices verified in the February 28, 2026 production deployment.

---

## 39.5 Continuous Improvement Loops

Operational evaluation feeds directly into improvement processes rather than remaining as static reporting.

### February 2026 hardening session outcomes

**Cascade failure diagnosis and resolution**  
Identified that four concurrent sessions with 22 parallel requests each (88 simultaneous Ollama calls) caused complete ensemble failure. Implemented five-layer watchdog system that restored 20/22 model participation under all tested load conditions.

**Memory constraint resolution**  
Raised Ollama container memory limit from 10 GB to 20 GB, eliminating "model requires more system memory (7.5 GiB) than is available" errors for 7B models.

**Concurrency control calibration**  
Set asyncio semaphore to 3 concurrent Ollama requests and MAX_CONCURRENT_CHATS to 2 sessions, defining the stable operating envelope for the February 28, 2026 hardware configuration (29 GB host RAM, 13 GB available under load).

**Timeout floor establishment**  
Set minimum timeout to 240 seconds to accommodate slowest 7B model cold-load scenarios, preventing premature request abandonment.

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

These loops connect observation to action, ensuring that operational evaluation drives continuous refinement of Ms. Jarvis as community infrastructure serving Boone, Fayette, Kanawha, Raleigh, and Mercer counties.

---

## 39.6 Production Baseline Scenarios

Comprehensive reasoning tasks anchored to the February 28, 2026 operational baseline:

### Verified ensemble consensus scenarios

**Scenario: Multi-model coordination under load**  
Processing model: 20/22 models responding  
Services used: All 32 operational services via `/selftestfabric`  
Consciousness level: Full consciousness bridge integration  
Response quality: Judge pipeline consistency 0.975  
Outcome: ✅ Stable consensus achieved in ~52 seconds (warm cache)

**Scenario: Cascade failure prevention**  
Processing model: Five-layer watchdog system  
Load condition: Multiple concurrent sessions  
Pre-hardening result: 0/22 models (complete failure)  
Post-hardening result: 20/22 models (stable operation)  
Outcome: ✅ Cascade failures eliminated through coordinated watchdog layers

**Scenario: West Virginia community query with GBIM grounding**  
Processing model: GIS RAG + 20-LLM ensemble + 69-DGM validation  
Data sources: 10.22M GBIM beliefs, local resources registry, Community Champions validation  
Services used: Main-brain, GIS RAG, text RAG, consciousness bridge, 69-DGM cascade  
Consciousness level: Full neurobiological layer integration  
Outcome: [Detailed evaluation pending production community query logs]

### Planned evaluation scenarios

**Scenario: Extended reasoning with ChromaDB memory**  
Processing model: Hilbert-space retrieval across H_text, H_geo, H_inst  
Collections accessed: GBIM worldview entities, consolidated spatial corpus, institutional embeddings  
Expected services: Full 32-service fabric  
Status: [Planned for Phase 2 evaluation]

**Scenario: Benefits routing with ZIP/county grounding**  
Processing model: Local resources registry + spatial RAG + ensemble consensus  
Community validation: Harmony for Hope Champions (Crystal Colyer, Cece Thompson, Brittney Bartlet, et al.)  
Geographic scope: Kanawha and Fayette Counties  
Status: [Planned for production community deployment]

---

## 39.7 System Stability (February 28, 2026 Verified Baseline)

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

**Watchdog system verification**:
- `VERIFYANDTEST.sh`: Reporting 32/32 services operational
- Ollama memory scheduler: Preventing over-memory requests
- Asyncio semaphore (3): Preventing Ollama saturation
- MAX_CONCURRENT_CHATS (2): Preventing session cascade
- Redis DynamicPortService: NBB health registration operational

**Safeguard system verification**:
- Blood-brain barrier: 319 requests filtered, 0 blocked, 0 violations
- 69-DGM cascade: 69 connectors loaded, architecturally authoritative
- Constitutional guardian: Connected and operational
- Psychology alignment: Assessment layer active

---

## 39.8 Coordination Success Rate (February 28, 2026 Baseline)

| Component | Success Rate | Notes |
|---|---|---|
| Service discovery | ✅ 100% | 32/32 services operational via `/selftestfabric` |
| Consciousness bridge | ✅ 100% | Mandatory infrastructure active |
| Brain orchestrator | ✅ 100% | Continuous coordination confirmed |
| BBB filtering | ✅ 100% | All requests approved, 0 blocks/violations |
| 69-DGM validation | ✅ 100% | 69 connectors loaded, verdicts authoritative |
| Psychology alignment | ✅ 100% | Assessment layer processing all requests |
| LLM ensemble participation | 91% | 20/22 models responding (2 expected failures) |
| Judge pipeline consensus | 97.5% | Consistency score 0.975 |
| NBB layer health | ✅ 100% | 8/8 containers healthy (7 via HTTP, 1 via Redis) |
| GIS RAG retrieval | ✅ 100% | Spatial queries operational |
| Text RAG retrieval | ✅ 100% | Semantic memory queries operational |
| Swarm coordination | ✅ 100% | Five-layer watchdog system preventing cascades |

These results represent the verified production baseline as of February 28, 2026, with all measured components performing within design specifications.

---

## 39.9 Qualitative Assessment and Known Limitations

### Production strengths (February 28, 2026 baseline)

**Ensemble consensus quality**  
- 20/22 models contributing weighted responses
- Judge pipeline consistency 0.975 confirms stable consensus
- Domain expertise distribution (medical, code, vision, structured data, general reasoning)
- Redundancy tolerance (system functions with 2 intentional/accidental model failures)

**Neurobiological grounding**  
- Consciousness bridge as mandatory infrastructure
- Brain orchestrator providing continuous coordination
- Eight-layer NBB subconscious integration
- All operations flowing through consciousness framework

**Validation and safeguarding**  
- Zero constitutional violations in 319 BBB-filtered requests
- 69-DGM cascade providing architecturally authoritative validation
- Psychology alignment layer assessing all requests pre-ensemble
- Five-layer watchdog system preventing cascade failures

**Community grounding**  
- 10.22M GBIM beliefs anchoring reasoning to West Virginia geography
- Local resources registry keyed by ZIP/county
- Harmony for Hope Community Champions validation
- GIS RAG specialization for benefits-relevant queries

### Known limitations

**Model participation variance**  
While 20/22 models respond consistently on warm-cache queries, cold-load scenarios and memory pressure can reduce participation. The two non-responding slots (one intentionally disabled, one variable) are tolerated through ensemble redundancy but represent known capacity constraints.

**Hardware scaling boundaries**  
The February 28, 2026 stable operating envelope (20 GB Ollama limit, semaphore 3, MAX_CONCURRENT_CHATS 2, 29 GB host RAM) is calibrated to current Legion 5 hardware. Scaling to higher concurrency or larger models requires hardware upgrades or distributed deployment.

**Cold-load latency**  
First request after Ollama restart takes ~163 seconds as 7B models load from 73 GB storage. This represents a known user-experience limitation for system restarts.

**GBIM axis coverage gaps**  
While identity, when, what, who, how, authority, and where axes have complete or near-complete coverage, the forwhom axis is not yet populated at scale and evidence axis remains in planned state. These gaps limit distributional reasoning capabilities.

**Limited concurrency testing**  
February 28, 2026 verification focused on achieving 32/32 operational baseline and preventing cascade failures. Formal load testing under sustained multi-user concurrency is planned for Phase 2.

**No adversarial testing in initial baseline**  
The February 28, 2026 milestone did not include prompt injection, jailbreak scenarios, or red-team evaluation. Adversarial testing is planned as a prerequisite for expanded community deployment.

**Lack of quantitative quality metrics beyond judge pipeline**  
Current evaluation relies on judge pipeline consistency (0.975) and operational health checks. BLEU/ROUGE-style metrics, factual accuracy benchmarks, and hallucination tracking on curated West Virginia-specific datasets are planned for future evaluation phases.

---

## 39.10 Conclusion

Operational evaluation combines verified metrics, production baselines, and architectural traces to build a realistic picture of how Ms. Jarvis behaves in practice. The February 28, 2026 milestone—32/32 services operational, 20/22 LLM models responding with 0.975 judge pipeline score, five-layer watchdog system preventing cascade failures, and zero constitutional violations across 319 BBB-filtered requests—establishes a concrete foundation for ongoing evaluation and improvement.

Empirical observations ground the thesis in observed behavior rather than theoretical aspiration: the swarm ensemble's 52-second warm-cache cycles, the consciousness bridge's mandatory infrastructure role, the brain orchestrator's continuous coordination, the 69-DGM cascade's architectural authority, the GBIM corpus's 10.22 million beliefs anchoring reasoning to West Virginia geography, and the five-layer watchdog system's prevention of cascade failures under concurrent load.

Known limitations—model participation variance, hardware scaling boundaries, cold-load latency, GBIM axis gaps, limited concurrency testing, absence of adversarial evaluation, and lack of quantitative quality metrics beyond judge pipeline consistency—define the scope of future work while acknowledging the system's current production capabilities.

By integrating these observations with the swarm functions and eternal watchdogs (Chapter 35), the test harness framework, and continuous validation processes, the project establishes a path from "working prototype" toward a monitored, inspectable, and improvable piece of consciousness-inspired cognitive infrastructure serving Appalachian communities through Harmony for Hope's fourteen-year mission.

The February 28, 2026 operational baseline represents not an endpoint but a verified foundation for the next phase of development: expanding community deployment, implementing formal load and adversarial testing, completing GBIM axis coverage, and scaling hardware to support higher concurrency while maintaining the consciousness-grounded, community-accountable architecture that distinguishes Ms. Jarvis as place-based intelligence with a ZIP code.
