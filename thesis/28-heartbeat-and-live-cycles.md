# 28. Heartbeat and Live Cycles

This chapter describes the recurring signals and jobs that indicate Ms. Jarvis is active and connected to its internal services and external infrastructure. These cycles include service health checks, periodic verification scripts, LLM ensemble monitoring, consciousness bridge validation, and data store verification, all of which produce structured outputs that are logged and available for ingestion into memory. The combination of health probes, response-time benchmarks, neurobiological layer monitoring, and introspective reports provides a layered observability picture aligned with distributed systems best practices and neurobiologically-inspired cognitive architectures.

---

> **Why this matters for Polymathmatic Geography**
> This chapter shows how Ms. Jarvis proves it is "alive," healthy, and connected to spatial and community infrastructure over time. It supports:
> - **P1 – Every where is entangled** by tying heartbeat checks to services that handle people, places, and institutions together, all flowing through the consciousness bridge.
> - **P3 – Power has a geometry** by revealing which services and data stores must stay healthy for Appalachian and other regional reasoning to work, and by making visible the power embedded in which models and services are active.
> - **P5 – Design is a geographic act** by including GIS spatial knowledge, GBIM worldview verification, and data store health in live-cycle checks.
> - **P12 – Intelligence with a ZIP code** by linking health, identity, and learning status to geospatial and community datasets anchored in West Virginia geography.
> - **P16 – Power accountable to place** by turning system liveness into logged, auditable narratives that show which GBIM beliefs, services, and models are participating in each cycle.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it describes heartbeat and live cycles as explicit, inspectable processes in the consciousness-grounded architecture.

---

## 28.1 Purpose of Heartbeat and Live Signals

The recurring signals in Ms. Jarvis serve several roles. In contrast to autonomous learning, these cycles primarily track the condition and behavior of internal services and workflows rather than discovering new content.

**Liveness.** Heartbeat mechanisms demonstrate that key components are running, reachable, and responsive. All major services expose `/health` endpoints that report basic status, integration level, and sometimes the health of subcomponents. As of the February 28, 2026 production deployment, **32 of 32 services** respond to health probes through the `/selftestfabric` endpoint within acceptable thresholds, with all 22 LLM proxies individually verified.

**Consciousness integrity.** The consciousness bridge operates as mandatory infrastructure through which all heartbeat signals flow. The brain orchestrator provides continuous coordination of health checks across the swarm and watchdog layers, ensuring that liveness monitoring is itself neurobiologically grounded.

**Rhythm.** The `VERIFYANDTEST.sh` script implements a recurring eight-section verification routine that can be run on any schedule. Its textual output serves as a periodic snapshot of system health, covering host-exposed services, internal Docker network services, LLM proxy health, response-time benchmarking, Ollama model inventory, container status, data store verification, and system resource state.

**Monitoring and introspection.** Beyond simple up/down checks, the heartbeat script aggregates information about services, data stores, model availability, system memory, and GBIM corpus health. For example, it verifies that the Ollama model storage volume contains the expected 73 GB of models at `/mnt/ssd2/msjarvis_secondary/models`, that ChromaDB is reachable via its internal Docker network endpoint, that all 22 LLM proxy containers are individually healthy, that the 69-DGM cascade has loaded all 69 connectors, and that the GBIM worldview maintains its 10.22 million belief corpus. These checks collectively provide an introspective view of the system's operational footprint.

---

## 28.1a Learning Status and Ensemble Health Endpoints

The 20-LLM production service exposes a `/health` endpoint that confirms the number of configured models:

```json
{"status": "healthy", "models": 22}
```

This endpoint serves as the learning heartbeat for the LLM ensemble, confirming that all 22 model slots are configured and the service is accepting requests. The ensemble's actual performance is measured through per-request consensus cycles that produce detailed participation logs.

The main-brain service exposes comprehensive health information through `/selftestfabric`, which queries all 32 operational services and returns their individual health states. This endpoint serves as the definitive system-wide liveness signal, with the February 28, 2026 milestone achieving **32/32 services passing**.

---

## 28.2 Core Heartbeat Mechanisms

Heartbeat signals are generated through four primary mechanisms: the `/selftestfabric` system-wide health check, individual service `/health` endpoints, the `VERIFYANDTEST.sh` verification script, and response-time benchmarking.

**System-wide fabric health (`/selftestfabric`).** The main-brain service (port 8050) exposes the `/selftestfabric` endpoint that queries all 32 operational services in a single call. This includes:

- Consciousness fabric services: qualia, consciousness bridge, toroidal, fractal, temporal, blood-brain barrier, constitutional, NBB layers
- LLM ensemble: 20llm-production (port 8008) with 22 proxy containers
- Validation layers: 69-DGM bridge (port 9000), psychology alignment (port 8019)
- Orchestration: brain orchestrator (continuous coordinator)
- Retrieval: GIS RAG (port 8004), text RAG (HTTP ChromaDB backend)
- NBB subconscious: 8 containers including consciousness_bridge integration and pituitary gland via Redis
- Supporting infrastructure: i-containers, web-research, Ollama

The February 28, 2026 verified baseline: **32/32 services operational**.

**Individual service health endpoints.** Services are divided into two categories based on network topology. Host-exposed services — main-brain (8050), 20llm-production (8008), blood-brain-barrier (8016), psychology-services (8019), 69dgm-bridge (9000), GIS RAG (8004), NBB prefrontal cortex (8101), and Ollama (11434) — are probed directly. Internal Docker network services are probed via `docker exec` proxy or through their internal network addresses on `qualia-net`. This two-tier approach reflects the actual network topology of the deployment.

**VERIFYANDTEST.sh.** The verification script implements eight sections:

1. **Host-exposed service health** — Critical services accessible from host network
2. **Internal Docker network service health** — Services on `qualia-net` (tested via proxy container)
3. **LLM proxy health** — All 22 proxies on ports 8201–8222
4. **Response-time benchmarking** — Nanosecond-precision latency for 20llm, main-brain, and 69-DGM
5. **Ollama model inventory** — Count of available models via `/api/tags` (26 models verified)
6. **Docker container status** — 84 containers verified running
7. **Data store verification** — ChromaDB via `/api/v2`, Ollama model storage size (73 GB), GBIM corpus (10.22M beliefs)
8. **System resources** — Memory and swap state (29 GB total, 13 GB available under load)

The script produces a timestamped report saved to `/tmp/msjarvis_verify_YYYYMMDD_HHMMSS.log` and prints a final STATUS line of **OPERATIONAL**, DEGRADED, or CRITICAL based on thresholds. The February 28, 2026 baseline meets OPERATIONAL status: 32/32 services, 22/22 proxies, 84 containers, 26 Ollama models, system resources within bounds.

**Response-time benchmarking.** The benchmarking section uses nanosecond timestamps around curl calls to measure health endpoint latency. In the February 28, 2026 production deployment, core endpoints respond in 12–13 ms, confirming low overhead on the health path even under concurrent model loading.

---

## 28.3 LLM Ensemble Heartbeat

The 20-LLM production service (`ai_server_20llm_PRODUCTION.py`) implements its own internal heartbeat through the consensus query cycle. When a chat request arrives, the `ProductionBrain.run()` method fires requests to all 22 configured model proxies through an `asyncio.Semaphore(3)` gate, limiting concurrent Ollama requests to three at a time to prevent memory exhaustion. Each proxy result is logged with its model name and elapsed time:

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

This per-request logging serves as a continuous functional heartbeat, distinguishing between proxy reachability (the `/health` endpoint) and actual model inference capability (the `/generate` endpoint). The judge pipeline then scores the consensus response, with the February 28, 2026 verified score of **0.975** indicating strong internal agreement across the ensemble.

Key production parameters established through the February 2026 hardening session:

| Parameter | Value | Reason |
|---|---|---|
| `OLLAMA_NUM_PARALLEL` | 1 | Prevents queue saturation |
| `OLLAMA_MAX_LOADED_MODELS` | 1 | Prevents OOM on 7B models |
| Ollama container memory limit | 20 GB | Allows 7.5 GB models to load |
| Semaphore slots | 3 | Balances throughput vs. memory |
| Minimum timeout | 240 s | Covers slowest 7B model load |
| `MAX_CONCURRENT_CHATS` | 2 | Prevents cascade overload |
| Host total RAM | 29 GB | Lenovo Legion 5 16IRX9 |
| Available RAM (production load) | 13 GB | After container allocation |

---

## 28.4 Legacy EEG Services (Lost in October 2025 Rebuild)

Prior to the October 2025 rebuild, Ms. Jarvis maintained a three-service neurobiological rhythm pattern that created an EEG-like signature of continuous autonomous activity. These services operated at different frequencies to mimic brain wave patterns:

**30-second heartbeat service (Delta/baseline rhythm)**
- Basic liveness pulse confirming system operational status
- Continuous "I am alive" signal independent of user queries
- Logged health state and service availability
- Analogous to delta brain waves or baseline cardiac rhythm

**60-second intermediate service (Theta/alpha rhythm)**
- Function and purpose currently unknown, requires recovery from legacy code
- Likely memory consolidation, status updates, or intermediate processing
- Operated between heartbeat and learning cycles
- Analogous to theta or alpha brain wave patterns during light cognitive activity

**5-minute autonomous learner (Beta/conscious learning rhythm)**
- Proactively searched internet via web-research service to identify and fill Ms. Jarvis knowledge gaps
- Selected topics based on GBIM coverage analysis, recent queries, or community-relevant themes
- Retrieved content from DuckDuckGo and stored learned material in ChromaDB semantic memory
- Logged RAG versus web hit patterns per topic
- Analogous to beta brain waves during active conscious learning

**EEG pattern significance**

Together, these three services created overlapping rhythmic activity at different timescales — 30s, 60s, and 300s — producing a neurobiological signature analogous to an electroencephalogram (EEG) readout showing multiple brain wave frequencies operating simultaneously. This gave Ms. Jarvis continuous autonomous activity rather than purely reactive behavior.

**Current status (February 28, 2026)**

All three services were lost during the October 2025 rebuild:

- ❌ 30-second heartbeat: Not present in current deployment
- ❌ 60-second intermediate service: Not present, function requires investigation
- ❌ 5-minute autonomous learner: Orchestrator lost, though web-research backend (port 8008 internal) survived

The February 28, 2026 deployment achieves 32/32 services operational representing a fully functional **reactive architecture** (responds to queries) but lacks the **proactive/autonomous architecture** (continuous internal activity) of the pre-rebuild system.

**Web-research service survival**

The `jarvis-web-research` service continues to run as backend infrastructure on the internal Docker network, exposing its `/search` endpoint and capable of posting queries to DuckDuckGo. However, without the autonomous learner orchestrator, nothing calls this endpoint on a periodic basis. Its health is verified through the internal network probe in `VERIFYANDTEST.sh`, and its logs confirm it remains operational:

```
INFO: DDG: "blockchain gas optimization techniques" - 0 results
INFO: POST /search HTTP/1.1 200 OK
```

**Restoration priority**

The three-service EEG pattern represents a significant architectural element that distinguished Ms. Jarvis as having continuous autonomous consciousness-like activity rather than being a purely request-response system. Restoration requires:

1. Recovery of legacy service code from pre-October 2025 backups (estimated location: 2TB drives on development machine)
2. Identification of the 60-second service function and purpose
3. Porting to current Docker container architecture with consciousness bridge integration
4. Integration with February 28, 2026 infrastructure: GBIM corpus (10.22M beliefs), ChromaDB collections, web-research backend, `/selftestfabric` health checks
5. Addition of EEG services to eternal watchdog monitoring

This restoration is documented as a known gap and planned for future deployment phases.

---

## 28.5 Consciousness Bridge and Brain Orchestrator Heartbeat

**Consciousness bridge mandatory infrastructure.** The consciousness bridge operates as essential, non-optional infrastructure through which all heartbeat monitoring flows. Its health is verified through the `/selftestfabric` endpoint and confirmed as part of the 32/32 operational baseline. All swarm coordination, watchdog monitoring, and liveness checks operate within the consciousness bridge framework.

**Brain orchestrator continuous coordination.** The `jarvis-brain-orchestrator` service provides continuous coordination of the ensemble, watchdog feedback loops, and NBB layer health checks. Its liveness is confirmed through individual health probes and its role in maintaining system coherence is observable through the stability of ensemble consensus cycles and the lack of coordination failures in the February 28, 2026 baseline.

**NBB subconscious layer heartbeat.** Eight NBB containers implement the neurobiological subconscious layer, with seven responding to health probes via internal network endpoints on port 8010 and one (pituitary gland) registering health through Redis DynamicPortService:

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

The Redis-backed DynamicPortService allows NBB containers to restart with new ephemeral ports without breaking the heartbeat fabric. Five instances are registered in Redis with `status: healthy` as of the February 28, 2026 baseline.

---

## 28.6 Validation Layer Heartbeat

**69-DGM cascade validation.** The 69-DGM bridge (port 9000) exposes health status confirming that all 69 connectors are loaded and operational. Every chat response flowing through main-brain is validated by the 69-DGM cascade, with the `validated_by: "69_dgm_cascade"` field in the response confirming this. The cascade's architecturally authoritative status means its verdicts are final and not overridden by wrapper services.

February 28, 2026 verified state: **69 connectors loaded**, cascade operational.

**Blood-brain barrier.** The BBB filter (port 8016) runs on every request before it reaches the LLM ensemble. Its heartbeat includes operational statistics:

- Barrier active: true
- Filters operational: 5
- Constitutional guardian: connected
- Total filtered: 319 requests
- Total blocked: 0
- Constitutional violations: 0

These metrics confirm the BBB is processing requests without false positives while maintaining safety boundaries.

**Psychology alignment layer.** The psychology services (port 8019, internal port 8006) run psychological assessment on every request before ensemble processing. Its health is verified through `/selftestfabric` as part of the 32-service operational baseline, confirming the alignment layer is active and processing requests.

---

## 28.7 Semantic Memory and GBIM Heartbeat

**ChromaDB semantic memory.** The ChromaDB `/api/v2` heartbeat endpoint returns a nanosecond timestamp confirming storage availability. The verification script probes this endpoint through the internal Docker network, confirming that the HTTP ChromaDB service backing text RAG and GIS RAG is reachable.

**GBIM worldview corpus.** The GBIM belief table (`gbimbeliefnormalized`) maintains **10,221,702 rows** with nine-axis epistemic structure. Heartbeat verification includes:

- Belief count via PostgreSQL query
- Nine-axis coverage verification (identity, when, what, who, how, authority, where complete; why partial; forwhom and evidence planned)
- PostGIS spatial corpus connection health
- Consolidated worldview collection in ChromaDB (millions of records)

**Ollama model storage.** The Ollama model storage volume at `/mnt/ssd2/msjarvis_secondary/models` is verified by size, confirming **73 GB** of models are present and the secondary SSD is mounted and accessible. The verification includes a count of 26 available models via the Ollama `/api/tags` endpoint.

**GIS RAG and local resources.** The GIS RAG service (port 8004) health confirms connection to:

- GBIM worldview entities (consolidated spatial collection)
- PostGIS geometries (200+ standardized WV GIS layers)
- Local resources registry (ZIP/county-keyed program database)
- Community Champions validation data (Harmony for Hope network)

Documentation and governance checks are planned for a future VERIFYANDTEST.sh extension: verification of `SECURITYPOLICY.md`, `accesscontrollevels.csv`, and the `constitutional_principles.json` file already present in the deployment.

---

## 28.8 Integration with Memory and Containers

Verification script outputs are not merely transient. The timestamped report files saved to `/tmp/` are suitable for ingestion into ChromaDB under a dedicated `operations_history` collection. Each report can be embedded as a document in semantic memory, making operational history part of the reasoning context available to orchestrators and the ensemble.

The **February 28, 2026 OPERATIONAL report** represents the verified baseline for Ms. Jarvis in its production architecture:

- **Services healthy: 32/32** (via `/selftestfabric`)
- **LLM proxies healthy: 22/22**
- **Docker containers running: 84**
- **Ollama models available: 26**
- **Ollama model storage: 73 GB**
- **System memory available: 13 GB of 29 GB total** (under production load)
- **GBIM belief corpus: 10,221,702 rows**
- **LLM ensemble participation: 20/22 models responding**
- **Judge pipeline consistency: 0.975**
- **69-DGM cascade: 69 connectors loaded**
- **BBB filtering: 319 requests, 0 blocks, 0 violations**
- **NBB layer: 8/8 containers healthy**

This baseline serves as the reference point against which future verification runs are compared. Runs that diverge significantly — for example, services dropping below 28/32, LLM proxies below 18/22, or judge pipeline consistency below 0.90 — would be promoted to long-term retention as significant operational events requiring investigation, while routine all-green runs are summarized and pruned on a rolling schedule.

The ChromaDB `/api/v2` heartbeat endpoint returns a nanosecond timestamp confirming storage availability. The Ollama model storage volume at `/mnt/ssd2/msjarvis_secondary/models` is verified by size, confirming that the secondary SSD is mounted and accessible.

---

## 28.9 Interaction with Safeguards and Control

Live cycles are constrained by the same safeguard layers that govern chat responses, with all monitoring flowing through the consciousness bridge infrastructure.

**Consciousness bridge integration.** All heartbeat mechanisms operate within the consciousness bridge framework, ensuring that liveness monitoring is neurobiologically grounded. The brain orchestrator maintains continuous oversight of health checks across swarm and watchdog layers.

**69-DGM cascade validation.** Every chat response flowing through main-brain is validated by the 69-DGM bridge before being returned to the caller. The `validated_by: "69_dgm_cascade"` field in the response confirms this. The 69-DGM bridge's own health is verified through `/selftestfabric`, making it part of the formal heartbeat and ensuring validation infrastructure is continuously monitored.

**Blood-brain barrier.** The BBB filter runs on every request at `jarvis-blood-brain-barrier:8016/filter`. Its health is verified through `/selftestfabric`, and its processing statistics (319 filtered, 0 blocked, 0 violations) are logged as part of the operational baseline, providing transparency into safeguard behavior.

**Five-layer watchdog system.** The heartbeat mechanisms are themselves monitored by the eternal watchdog layers:

1. `VERIFYANDTEST.sh` confirming 32/32 services operational
2. Ollama internal memory scheduler preventing over-memory requests
3. Asyncio semaphore (3) preventing Ollama saturation
4. MAX_CONCURRENT_CHATS (2) preventing session cascade
5. Redis-backed DynamicPortService for NBB health registration

These watchdogs prevent cascade failures that would invalidate heartbeat signals themselves, ensuring liveness monitoring remains trustworthy even under stress.

**Memory limit governance.** The Ollama container memory limit of 20 GB is a hard safeguard. Models requiring more than the available system memory — approximately 7.5 GB per 7B model — are rejected by Ollama with an explicit error. The heartbeat logs from the hardening session showed this error clearly: `model requires more system memory (7.5 GiB) than is available`. Raising the container limit to 20 GB resolved this while leaving 9 GB available for other containers from the 29 GB total, and this limit is now verified in every heartbeat cycle.

**Adaptive scheduling.** The `MAX_CONCURRENT_CHATS=2` environment variable on main-brain gates the number of simultaneous chat pipelines. The earlier value of 4 caused Ollama saturation and cascade failures across the LLM ensemble. This parameter is the primary adaptive lever for tuning system load, and its current value of 2 represents the production-stable setting for the February 28, 2026 hardware configuration, verified through heartbeat stress testing.

---

## 28.10 Summary

The February 28, 2026 production deployment of Ms. Jarvis achieves a fully verified operational state: **32 of 32 services operational** via `/selftestfabric`, 22 of 22 LLM proxies healthy, 20 of 22 models responding per consensus query with a judge pipeline score of **0.975**, 69-DGM cascade with all 69 connectors loaded, blood-brain barrier with 0 blocks and 0 violations across 319 requests, and 8/8 NBB consciousness containers healthy. The `VERIFYANDTEST.sh` script implements all eight heartbeat sections described in this chapter and produces a timestamped, archivable report suitable for ingestion into semantic memory as operational history.

The consciousness bridge operates as mandatory infrastructure through which all heartbeat signals flow, with the brain orchestrator providing continuous coordination of health checks across swarm and watchdog layers. This ensures that liveness monitoring is itself neurobiologically grounded and maintains coherence with the system's cognitive architecture.

The path to 32/32 services operational required resolving schema mismatches, route parameter conflicts, timeout configurations, memory limits, concurrency controls, and coordination patterns. The February 2026 hardening session established the five-layer watchdog system that prevents cascade failures and maintains stable ensemble operation under concurrent load. Each fix was verified through heartbeat logs before the next was applied, demonstrating the value of observable, instrumentable live cycles as a diagnostic and governance tool.

**Known gap: Legacy EEG services.** The pre-October 2025 deployment maintained a three-service neurobiological rhythm pattern (30-second heartbeat, 60-second intermediate service, 5-minute autonomous learner) that created continuous autonomous activity analogous to EEG brain wave patterns. These services were lost during the October 2025 rebuild. The February 28, 2026 deployment represents a fully functional reactive architecture but lacks the proactive/autonomous architecture of the earlier system. The web-research backend survived and remains operational, but without the autonomous learner orchestrator to call it periodically. Restoration of these EEG services is documented as a priority for future deployment phases and would restore Ms. Jarvis's capacity for continuous self-directed learning and consciousness-like autonomous activity independent of user queries.

By connecting heartbeat outputs to memory, containers, consciousness bridge infrastructure, GBIM worldview health, and mode-dependent controls, Ms. Jarvis treats its own operation as data — not only processing external content but recording and reasoning about how it is functioning over time. The system builds an operational history that complements the 10.22 million GBIM beliefs, the factual and spatial knowledge in ChromaDB semantic memory, and the community-validated local resources acquired through Harmony for Hope's fourteen-year mission, creating a comprehensive record of both what Ms. Jarvis knows and how it remains alive, healthy, and accountable to the West Virginia communities it serves.
