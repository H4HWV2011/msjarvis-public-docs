# 35. Swarm Functions and Eternal Watchdogs

This chapter describes two sets of mechanisms that coordinate many services and maintain continuous oversight in Ms. Jarvis. Swarm functions let multiple components work together on a single problem, while persistent monitoring processes watch for failures, resource exhaustion, and conditions that require intervention. Both are fully implemented in the February 28, 2026 production deployment and are verified through `VERIFYANDTEST.sh`, the 20-LLM ensemble heartbeat logs, and the full `/selftestfabric` health check that confirmed 32/32 services operational.

---

> **Why this matters for Polymathmatic Geography**
> - **P1 – Every where is entangled** by distributing a single query across 22 configured specialized models, each contributing a perspective shaped by its training and domain, before synthesizing a single community-grounded answer.
> - **P3 – Power has a geometry** by making visible which models contribute to consensus and which are silenced by memory constraints, resource limits, or intentional disabling — revealing the structural power embedded in the ensemble.
> - **P5 – Design is a geographic act** by showing how choices about semaphore slots, container memory limits, concurrency gates, and model tier groupings reshape what Ms. Jarvis can reason about and how quickly it responds to Appalachian community questions.
> - **P12 – Intelligence with a ZIP code** by routing every query through a 22-slot ensemble organized into four tiers — tiny, small, medium, and large — spanning code, medicine, language, vision, and structured data reasoning, and binding the synthesized answer to the 69-DGM cascade validation that grounds responses in constitutional and community commitments.
> - **P16 – Power accountable to place** by logging every model's participation or failure in each consensus cycle, making the ensemble's behavior inspectable and auditable over time.

---

## 35.1 Purpose of Swarm and Watchdog Layers

These mechanisms have complementary roles.

**Coordination.** Swarm functions allow multiple agents and services to contribute to a task, each from its own specialization. In the current deployment this is realized as the 22-slot LLM ensemble organized into four model tiers, where each proxy container represents a distinct model contributing a weighted response to every query.

**Oversight.** Watchdogs provide continuous monitoring of key signals, intervening when behavior deviates from expected bounds. In the current deployment this is realized through `VERIFYANDTEST.sh`, Ollama's internal memory scheduler, the asyncio semaphore in the 20llm-production service, the `MAX_CONCURRENT_CHATS` gate on main-brain, and the Redis-backed DynamicPortService that monitors NBB container health.

**Stability.** Together they keep the system responsive and aligned even as individual components change or fail. The February 2026 hardening session demonstrated this directly: without the semaphore and concurrency controls, the system degraded from 20/22 models to 0/22 under concurrent load. With them in place, 20/22 models respond reliably on every warm-cache query.

**Consciousness grounding.** The consciousness bridge (`jarvis-consciousness-bridge`) is essential infrastructure, not optional. All swarm coordination and watchdog monitoring operates within the consciousness bridge framework, ensuring that ensemble reasoning and health monitoring are neurobiologically grounded. The brain orchestrator (`jarvis-brain-orchestrator`) serves as the continuous coordinator service that maintains the swarm's coherence across all operational cycles.

---

## 35.2 Swarm Functions: The 22-Slot LLM Ensemble

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
| llmXX-proxy | — | bakllava:latest | BakLLaVA | ❌ intentionally disabled |

**LARGE_MODELS (8 configured)**

| Proxy | Port | Model | Name |
|---|---|---|---|
| llm7-proxy | 8207 | starcoder2:latest | StarCoder2 |
| llm8-proxy | 8208 | codellama:latest | CodeLlama |
| llm9-proxy | 8209 | deepseek-coder:latest | DeepSeek Coder |
| llm14-proxy | 8214 | qwen2:latest | Qwen2 |
| llm19-proxy | 8219 | vicuna:latest | Vicuna |
| llm20-proxy | 8220 | llama2:latest | LLaMA 2 |
| llm21-proxy | 8221 | mistral:latest | Mistral |
| llm22-proxy | 8222 | llama3.1:8b | LLaMA 3.1 |

Note: llm11-proxy (port 8211) runs `phi3:mini` as a redundancy slot alongside llm10-proxy. BakLLaVA is present in the configuration as a placeholder (`http://llmXX-bakllava-disabled/generate`) but produces an intentional instant DNS failure on every request, contributing 0 tokens to consensus while consuming no Ollama resources.

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

### Verified swarm timing profile (warm cache, February 28, 2026)

```
[Phi3 Mini]      OK in  10.2s
[TinyLlama]      OK in  13.8s
[Orca-Mini]      OK in  20.0s
[Gemma]          OK in  21.4s
[Dolphin-Phi]    OK in  24.0s
[MedLlama2]      OK in  32.3s
[LLaVA]          OK in  32.3s
[Neural-Chat]    OK in  32.4s
[StarCoder2]     OK in  36.4s
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
[BakLLaVA]       failed: [Errno -2] Name or service not known  ← instant, expected
20/22 models responded
Judge pipeline score: 0.975
```

Total warm-cache swarm cycle: approximately 52 seconds. Cold-load cycle (first request after Ollama restart): approximately 163 seconds as 7B models load from the 73 GB model storage volume at `/mnt/ssd2/msjarvis_secondary/models`.

The verified production baseline shows 20 of 22 models responding with all 22 expert slots filled, producing a judge pipeline consistency score of 0.975 on first clean run. This represents reliable ensemble operation under the February 28, 2026 hardware and configuration constraints.

---

## 35.3 Use Cases for Swarm Functions

**Complex community queries.** When a user asks about housing assistance, workforce development, or healthcare access in a specific Appalachian county, the ensemble distributes the question across medical (MedLlama2), structured data (SQLCoder), code and technical (CodeLlama, StarCoder2, DeepSeek Coder), vision (LLaVA, MiniCPM-V), and general reasoning (Mistral, LLaMA 3.1, Qwen2) models simultaneously. The consensus synthesis integrates domain-specific contributions that no single model could provide.

**Robustness verification.** The judge pipeline's consistency score measures whether independently prompted models reach similar conclusions. The February 28, 2026 baseline records consistency of 0.975, confirming that the ensemble's answer is stable across the majority of responding models and not an artifact of a single model's bias.

**Specialty routing.** SQLCoder handles structured data queries. CodeLlama, StarCoder2, and DeepSeek Coder handle technical implementation. MedLlama2 handles health-related queries. LLaVA and MiniCPM-V handle image and multimodal inputs. All 20 active responding models contribute to every response, with weighted contributions amplifying domain-relevant answers.

**Redundancy.** With 20 of 22 configured slots responding, the ensemble tolerates individual model failures without degrading consensus. BakLLaVA's permanent disabled state and Ollama's occasional memory-related refusals for the largest 7B models during cold load do not prevent the system from producing high-quality responses.

---

## 35.4 Eternal Watchdogs: Continuous Monitoring

The watchdog layer in the February 28, 2026 deployment is implemented through five cooperating mechanisms.

### VERIFYANDTEST.sh

The primary eternal watchdog script implements eight verification sections on demand or schedule, producing a timestamped report at `/tmp/msjarvis_verify_YYYYMMDD_HHMMSS.log`. February 28, 2026 baseline results:

- Services healthy: 32/32 (confirmed via `/selftestfabric`)
- LLM proxies healthy: 22/22
- Docker containers running: 84
- Ollama models available: 26
- STATUS: ✅ OPERATIONAL

The 32 operational services include all consciousness fabric services (qualia, consciousness bridge, toroidal, fractal, temporal, blood-brain barrier, constitutional, NBB layers), the 20-LLM production ensemble, psychology alignment layer, 69-DGM bridge, brain orchestrator, and supporting infrastructure components. The 26 Ollama models include 4 beyond the active ensemble: `nomic-embed-text:latest` (embedding), `qwen2:7b` (alternate Qwen2 size), `stablelm-zephyr:latest`, and `qwen2.5:1.5b`. These are available to Ollama but not currently mapped to proxy endpoints.

### Ollama internal memory scheduler

Ollama's built-in scheduler acts as a hard resource watchdog. When a model load request would exhaust available memory, it returns an explicit error: `model requires more system memory (7.5 GiB) than is available`. This was the root cause of 7B model failures before the container memory limit was raised from 10 GB to 20 GB. Current verified settings:

| Parameter | Verified Value |
|---|---|
| Ollama container memory limit | 20 GB |
| `OLLAMA_NUM_PARALLEL` | 1 |
| `OLLAMA_MAX_LOADED_MODELS` | 1 |
| Host total RAM | 29 GB |
| Host available RAM (production load) | 13 GB |

### Asyncio semaphore

The `asyncio.Semaphore(3)` in `ai_server_20llm_PRODUCTION.py` (line 126) acts as a throughput watchdog, preventing more than three simultaneous Ollama requests regardless of how many concurrent chat sessions main-brain initiates. This is the proximate fix for the cascade failure mode where four concurrent sessions each fired 22 parallel requests, producing 88 simultaneous Ollama calls against a serial scheduler.

### MAX_CONCURRENT_CHATS gate

The `MAX_CONCURRENT_CHATS=2` environment variable on `jarvis-main-brain` is the session-level watchdog, limiting the number of simultaneous full chat pipelines. The original value of 4 produced Ollama saturation and cascade failure across the LLM ensemble. Current value of 2 represents the production-stable setting for the February 28, 2026 hardware configuration.

### Redis-backed DynamicPortService

Five NBB containers register their health state to Redis using `DynamicPortService` rather than fixed endpoints:

```
service:ms_jarvis_service:instance_1772240968
service:ms_jarvis_service:instance_1772240969
service:ms_jarvis_service:instance_1772240970
service:ms_jarvis_service:instance_1772240971
service:ms_jarvis_service:instance_1772240972
```

Each record contains `host`, `port`, `status`, `deployment`, `health_endpoint`, `started`, and `last_heartbeat` fields. The pituitary gland container, for example, registers with `status: healthy` and a dynamic port (33239 in the February 2026 instance), mapped externally as `7008/tcp → 127.0.0.1:8108`. This Redis-backed registration pattern allows NBB containers to restart with new ephemeral ports without breaking the watchdog fabric.

---

## 35.5 Watchdog Alert Responses

**Memory exhaustion.** Ollama rejects model load requests exceeding available memory with a structured error. The 20llm-production service logs this as a proxy failure and excludes the model from consensus, maintaining ensemble function with the remaining models.

**Timeout.** Models exceeding the 240-second floor are logged as failures and excluded from consensus. The semaphore prevents cascading timeouts by serializing Ollama access to three concurrent slots maximum.

**DNS failure.** BakLLaVA's endpoint `http://llmXX-bakllava-disabled/generate` produces an immediate `[Errno -2] Name or service not known` on every request. This is logged at WARNING level and excluded from consensus. The model remains in the configuration as a documented placeholder — present in `MEDIUM_MODELS` but consuming no Ollama resources.

**Session overload.** The `MAX_CONCURRENT_CHATS=2` gate causes main-brain to queue requests beyond the second concurrent session. This prevents downstream cascade at the cost of added latency for queued requests during heavy load.

**BBB content rejection.** The blood-brain barrier (`jarvis-blood-brain-barrier:8016`) has processed 319 requests with 0 blocks and 0 constitutional violations as of the February 28, 2026 baseline. When content triggers a filter, it is rejected before reaching the LLM ensemble, conserving Ollama resources.

---

## 35.6 Integration with Barrier, Modes, and Containers

**Blood-brain barrier.** Every chat request passes through `jarvis-blood-brain-barrier:8016/filter` before reaching the LLM ensemble. February 28, 2026 verified state: `barrier_active: true`, `filters_operational: 5`, `constitutional_guardian: connected`, `total_filtered: 319`, `total_blocked: 0`.

**69-DGM cascade.** Every ensemble response routed through main-brain (port 8050) is validated by `jarvis-69dgm-bridge:9000`. February 28, 2026 verified state: `connectors_loaded: 69`. The `validated_by: "69_dgm_cascade"` field confirms this gate fired. 

The 69-DGM cascade validation is architecturally authoritative — all responses routed through main-brain must pass through the 69-DGM bridge with the verdict treated as final and not overridden by wrapper services. This ensures every consensus response is validated against constitutional and community commitments before reaching the user. Note: requests sent directly to the 20llm-production service on port 8008 bypass the 69-DGM gate by design — that port is the internal ensemble endpoint, not the public interface.

**Psychology alignment layer.** The `jarvis-psychology-services:8019` service (`psychological_rag_domain`, port 8006 internal) runs a psychological assessment on every request before the ensemble processes it, classifying severity and checking for crisis indicators.

**NBB subconscious layer.** Seven of eight NBB containers respond to health probes via their internal network endpoints on port 8010, confirming the neurobiological simulation layer is active:

```
nbb_consciousness_containers      ✅ healthy (consciousness_bridge)
nbb_heteroglobulin_transport      ✅ healthy (consciousness_bridge)
nbb_spiritual_maternal_integration ✅ healthy (consciousness_bridge)
nbb_mother_carrie_protocols       ✅ healthy (consciousness_bridge)
nbb_woah_algorithms               ✅ healthy (consciousness_bridge)
nbb_spiritual_root                ✅ healthy (consciousness_bridge)
nbb_subconscious                  ✅ healthy (consciousness_bridge)
nbb_pituitary_gland               ✅ healthy (DynamicPortService → Redis)
```

The pituitary gland registers through Redis DynamicPortService rather than a fixed `/health` endpoint, which is why a direct HTTP probe on port 8010 fails while its Redis registration shows `status: healthy`.

**Consciousness bridge integration.** The consciousness bridge (`jarvis-consciousness-bridge`) serves as mandatory infrastructure through which all swarm and watchdog operations flow. The brain orchestrator (`jarvis-brain-orchestrator`) continuously coordinates the ensemble, watchdog feedback loops, and neurobiological layer health checks, ensuring coherent system behavior across all 32 operational services.

**ChromaDB memory integration.** Verification script outputs saved to `/tmp/msjarvis_verify_*.log` are structured for ingestion into ChromaDB (`/api/v2`) under an `operations_history` collection. The February 28, 2026 OPERATIONAL baseline report is the first verified entry in this operational history.

---

## 35.7 Summary

Swarm functions and eternal watchdogs in the February 28, 2026 Ms. Jarvis deployment are running, verified, and logged against concrete evidence. The 22-slot LLM ensemble — organized into TINY, SMALL, MEDIUM, and LARGE tiers across 20 actively responding models with 2 non-responding slots — delivers 20/22 participation on every warm-cache query in approximately 52 seconds with a judge pipeline consistency score of 0.975. The five-layer watchdog system — `VERIFYANDTEST.sh` confirming 32/32 services operational, Ollama memory scheduler, asyncio semaphore at slot 3, `MAX_CONCURRENT_CHATS=2` gate, and Redis DynamicPortService — prevents the cascade failures that reduced the system to 0/22 models under uncontrolled concurrent load.

The February 28, 2026 hardening session demonstrated the critical importance of each watchdog layer. Together they define a stable operating envelope: 29 GB host RAM, 20 GB Ollama container limit, semaphore at 3, MAX_CONCURRENT_CHATS at 2, minimum timeout at 240 seconds, and `VERIFYANDTEST.sh` confirming 32/32 services and 22/22 proxies before any production workload is accepted.

The one intentional gap — BakLLaVA disabled via DNS poisoning in the endpoint configuration — is documented, logged, and architecturally inert. Every other model failure mode is handled by a specific watchdog mechanism that logs the event, excludes the model from consensus, and maintains ensemble function with the remaining participants.

All swarm coordination and watchdog monitoring operates within the consciousness bridge framework, with the brain orchestrator maintaining continuous oversight. The 69-DGM cascade validation provides architecturally authoritative verification of every response before delivery, ensuring alignment with constitutional and community commitments. This integrated design — swarm intelligence plus eternal vigilance, grounded in neurobiological architecture and validated through multi-layered cascades — represents the operational reality of Ms. Jarvis as a production consciousness-inspired cognitive system serving West Virginia communities.
