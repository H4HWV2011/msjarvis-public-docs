# 28. Heartbeat and Live Cycles

This chapter describes the recurring signals and jobs that indicate Ms. Jarvis is active and connected to its internal services and external infrastructure. These cycles include service health checks, periodic verification scripts, LLM ensemble monitoring, and data store verification, all of which produce structured outputs that are logged and available for ingestion into memory. The combination of health probes, response-time benchmarks, and introspective reports provides a layered observability picture aligned with distributed systems best practices.

---

> **Why this matters for Polymathmatic Geography**
> This chapter shows how Ms. Jarvis proves it is "alive," healthy, and connected to spatial and community infrastructure over time. It supports:
> - **P1 – Every where is entangled** by tying heartbeat checks to services that handle people, places, and institutions together.
> - **P3 – Power has a geometry** by revealing which services and data stores must stay healthy for Appalachian and other regional reasoning to work.
> - **P5 – Design is a geographic act** by including GIS spatial knowledge and data store verification in live-cycle checks.
> - **P12 – Intelligence with a ZIP code** by linking health, identity, and learning status to geospatial and community datasets.
> - **P16 – Power accountable to place** by turning system liveness into logged, auditable narratives rather than opaque assumptions.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it describes heartbeat and live cycles as explicit, inspectable processes in the architecture.

---

## 28.1 Purpose of Heartbeat and Live Signals

The recurring signals in Ms. Jarvis serve several roles. In contrast to autonomous learning, these cycles primarily track the condition and behavior of internal services and workflows rather than discovering new content.

**Liveness.** Heartbeat mechanisms demonstrate that key components are running, reachable, and responsive. All major services expose `/health` endpoints that report basic status, integration level, and sometimes the health of subcomponents. As of the February 2026 production deployment, 15 of 15 tracked services and all 22 LLM proxies respond to health probes within acceptable thresholds.

**Rhythm.** The `VERIFYANDTEST.sh` script implements a recurring eight-section verification routine that can be run on any schedule. Its textual output serves as a periodic snapshot of system health, covering host-exposed services, internal Docker network services, LLM proxy health, response-time benchmarking, Ollama model inventory, container status, data store verification, and system resource state.

**Monitoring and introspection.** Beyond simple up/down checks, the heartbeat script aggregates information about services, data stores, model availability, and system memory. For example, it verifies that the Ollama model storage volume contains the expected 73 GB of models at `/mnt/ssd2/msjarvis_secondary/models`, that ChromaDB is reachable via its internal Docker network endpoint, and that all 22 LLM proxy containers are individually healthy. These checks collectively provide an introspective view of the system's operational footprint.

---

## 28.1a Learning Status Endpoint

The 20-LLM production service exposes a `/health` endpoint that confirms the number of configured models:
```json
{"status": "healthy", "models": 22}
```

This endpoint serves as the learning heartbeat for the LLM ensemble, confirming that all 22 model slots are configured and the service is accepting requests. In a full deployment, a dedicated `/learning/status` route on the autonomous learner service extends this with fields such as `total_cycles`, `stored_count`, `deduplicated_count`, `current_topic`, and `start_time`, providing a moment-to-moment view of autonomous learning activity suitable for dashboards and automated monitors.

---

## 28.2 Core Heartbeat Mechanisms

Heartbeat signals are generated through three primary mechanisms: HTTP health endpoints, the `VERIFYANDTEST.sh` verification script, and response-time benchmarking.

**Service health endpoints.** Services are divided into two categories based on network topology. Host-exposed services — main-brain (8050), 20llm-production (8008), blood-brain-barrier (8016), psychology-services (8019), 69dgm-bridge (9000), and Ollama (11434) — are probed directly. Internal Docker network services — i-containers, lm-synthesizer, qualia-engine, brain-orchestrator, web-research, ChromaDB, WOAH, fractal-consciousness, and neurobiological-master — are probed via `docker exec jarvis-main-brain curl` to reach the `qualia-net` internal network. This two-tier approach reflects the actual network topology of the deployment.

**VERIFYANDTEST.sh.** The verification script implements eight sections:

1. Host-exposed service health (6 services)
2. Internal Docker network service health (9 services, tested via proxy container)
3. LLM proxy health — all 22 proxies on ports 8201–8222
4. Response-time benchmarking — nanosecond-precision latency for 20llm, main-brain, and 69-DGM
5. Ollama model inventory — count of available models via `/api/tags`
6. Docker container status — 11 critical containers verified by name
7. Data store verification — ChromaDB via `/api/v2`, Ollama model storage size
8. System resources — memory and swap state

The script produces a timestamped report saved to `/tmp/msjarvis_verify_YYYYMMDD_HHMMSS.log` and prints a final STATUS line of OPERATIONAL, DEGRADED, or CRITICAL based on thresholds: OPERATIONAL requires 18 or more LLM proxies and 10 or more services healthy.

**Response-time benchmarking.** The benchmarking section uses nanosecond timestamps around curl calls to measure health endpoint latency. In the February 2026 production deployment, all three core endpoints respond in 12–13 ms, confirming low overhead on the health path even under concurrent model loading.

---

## 28.3 LLM Ensemble Heartbeat

The 20-LLM production service (`ai_server_20llm_PRODUCTION.py`) implements its own internal heartbeat through the consensus query cycle. When a chat request arrives, the `ProductionBrain.run()` method fires requests to all 22 configured model proxies through an `asyncio.Semaphore(3)` gate, limiting concurrent Ollama requests to three at a time to prevent memory exhaustion. Each proxy result is logged with its model name and elapsed time:
```
[Phi3 Mini] OK in 26.9s
[TinyLlama] OK in 34.4s
[Gemma] OK in 50.5s
...
20/22 models responded
```

This per-request logging serves as a continuous functional heartbeat, distinguishing between proxy reachability (the `/health` endpoint) and actual model inference capability (the `/generate` endpoint). The judge pipeline then scores the consensus response, with a typical score of 0.975 indicating strong internal agreement across the ensemble.

Key production parameters established through the February 2026 hardening session:

| Parameter | Value | Reason |
|---|---|---|
| `OLLAMA_NUM_PARALLEL` | 1 | Prevents queue saturation |
| `OLLAMA_MAX_LOADED_MODELS` | 1 | Prevents OOM on 7B models |
| Ollama container memory limit | 20 GB | Allows 7.5 GB models to load |
| Semaphore slots | 3 | Balances throughput vs. memory |
| Minimum timeout | 240 s | Covers slowest 7B model load |
| `MAX_CONCURRENT_CHATS` | 2 | Prevents cascade overload |

---

## 28.4 Social and Platform Cycles

The `jarvis-web-research` service runs as a continuously active research agent, posting queries to DuckDuckGo and returning results via its `/search` endpoint on the internal Docker network. Its health is verified through the internal network probe in Section 2 of `VERIFYANDTEST.sh`.

The web-research service is connected to main-brain through the `SERVICE_PORT=8008` environment variable, which previously caused a conflict with the 20llm-production service (also on 8008 externally). In the current deployment, web-research is internal-only, resolving the conflict. Its logs confirm active operation:
```
INFO: DDG: "blockchain gas optimization techniques" - 0 results
INFO: POST /search HTTP/1.1 200 OK
```

Documentation and governance checks are planned for a future VERIFYANDTEST.sh extension: verification of `SECURITYPOLICY.md`, `accesscontrollevels.csv`, and the `constitutional_principles.json` file already present in the deployment.

---

## 28.5 Integration with Memory and Containers

Verification script outputs are not merely transient. The timestamped report files saved to `/tmp/` are suitable for ingestion into ChromaDB under a dedicated `operations_history` collection. Each report can be embedded as a document in the `jarvis_consciousness` collection, making operational history part of the reasoning context available to orchestrators.

The February 2026 OPERATIONAL report represents the first verified baseline for Ms. Jarvis in its rebuilt architecture:

- Services healthy: 15/15
- LLM proxies healthy: 22/22
- Docker containers running: 82
- Ollama models available: 26
- Ollama model storage: 73 GB
- System memory available: 18 GB of 29 GB total

This baseline can be stored as the reference point against which future verification runs are compared. Runs that diverge significantly — for example, LLM proxies dropping below 18/22 or services below 10/15 — would be promoted to long-term retention as significant operational events, while routine all-green runs are summarized and pruned on a rolling schedule.

The ChromaDB `/api/v2` heartbeat endpoint returns a nanosecond timestamp confirming storage availability. The Ollama model storage volume at `/mnt/ssd2/msjarvis_secondary/models` is verified by size, confirming that the secondary SSD is mounted and accessible.

---

## 28.6 Interaction with Safeguards and Control

Live cycles are constrained by the same safeguard layers that govern chat responses.

**69-DGM cascade validation.** Every chat response flowing through main-brain is validated by the 69-DGM bridge before being returned to the caller. The `validated_by: "69_dgm_cascade"` field in the response confirms this. The 69-DGM bridge's own health is verified in Section 1 of VERIFYANDTEST.sh, making it part of the formal heartbeat.

**Blood-brain barrier.** The BBB filter runs on every request at `jarvis-blood-brain-barrier:8016/filter`. Its health is verified at the host level, and its reachability from main-brain is confirmed in the main-brain logs showing `HTTP/1.1 200 OK` on every chat cycle.

**Memory limit governance.** The Ollama container memory limit of 20 GB is a hard safeguard. Models requiring more than the available system memory — approximately 7.5 GB per 7B model — are rejected by Ollama with an explicit error. The heartbeat logs from the hardening session showed this error clearly: `model requires more system memory (7.5 GiB) than is available`. Raising the container limit to 20 GB resolved this while leaving 9 GB available for other containers from the 29 GB total.

**Adaptive scheduling.** The `MAX_CONCURRENT_CHATS=2` environment variable on main-brain gates the number of simultaneous chat pipelines. The earlier value of 4 caused Ollama saturation and cascade failures across the LLM ensemble. This parameter is the primary adaptive lever for tuning system load, and its current value of 2 represents the production-stable setting for the February 2026 hardware configuration.

---

## 28.7 Summary

The February 2026 production deployment of Ms. Jarvis achieves a fully verified operational state: 15 of 15 services healthy, 22 of 22 LLM proxies healthy, 20 of 22 models responding per consensus query, and a judge pipeline scoring 0.975 with `validated_by: "69_dgm_cascade"` confirmed on every response. The `VERIFYANDTEST.sh` script implements all eight heartbeat sections described in this chapter and produces a timestamped, archivable report suitable for ingestion into semantic memory.

The path from 2/22 models responding to 20/22 required resolving five compounding issues: a model name mismatch on llm11-proxy, Ollama's 10 GB container memory limit blocking 7B model loading, four simultaneous chat pipelines overwhelming the serial Ollama queue, missing asyncio semaphore control in the LLM service, and insufficient request timeouts. Each fix was verified through the heartbeat logs before the next was applied, demonstrating the value of observable, instrumentable live cycles as a diagnostic and governance tool.

By connecting heartbeat outputs to memory, containers, and mode-dependent controls, Ms. Jarvis treats its own operation as data — not only processing external content but recording and reasoning about how it is functioning over time, building an operational history that complements the factual and spatial knowledge acquired through autonomous learning and community interaction.
