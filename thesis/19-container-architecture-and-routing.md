# 19. Container Architecture and Routing

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: August 17, 2026*

---

## 19.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis is actually wired as a set of containers, ports, and networks, not just as an idea on a whiteboard. It shows how reasoning, safeguards, time and state services, and commons-facing gateways are stitched together on one host.

It supports:

- **P1 – Every where is entangled** by showing that memory, safeguards, time, and sandbox reasoning are connected services, even though they live in separate containers.  
- **P3 – Power has a geometry** by locating authority in network attachments, host ports, and routing paths instead of vague “intelligence.”  
- **P5 – Design is a geographic act** by treating Docker networks and host bindings as a map of where state is allowed to travel.  
- **P12 – Intelligence with a ZIP code** by tying container routing to West-Virginia-grounded GBIM and Chroma services.  
- **P16 – Power accountable to place** by keeping the routes between sandbox, BBB, guardian, Master, EEG producers, and promotion visible and auditable.

This chapter belongs to the **Computational Instrument** tier. It documents the as-built container topology and host route map that carry Ms. Allis’s work.

---

## 19.2 High-Level Container Topology

On the running host, Ms. Allis is deployed as a large Docker Compose stack. At the time of this chapter:

- A single `docker-compose.yml` file defines **165 services**.  
- There are **no duplicate published host ports**, so each exposed port has a unique mapping.  
- Critical governance, memory, sandbox, Hilbert, Chroma, Neurobiological Master, BBB, and Guardian services are up and reachable through health endpoints.  
- Internal service-to-service routing for the Master, BBB, Guardian, I-Containers, Qualia, EEG producers, and related neurobiological services uses the `qualia-net` Docker network.

For rural developers, that means you can SSH into the box, run a single `docker compose ps` command, and see the whole working nervous system: which containers are up, which ports are bound to `127.0.0.1`, and which networks tie them together.

---

## 19.3 Core Governance and Time Services

Several governance and time services anchor the architecture:

- **Blood-Brain Barrier (BBB):**  
  - Service: `jarvis-blood-brain-barrier`  
  - Host port: `127.0.0.1:8016->8016/tcp`  
  - Network: `qualia-net`  
  - Live image: `jarvis-blood-brain-barrier:guardian-failclosed-canary-20260817`  
  - Restart policy: `unless-stopped`  
  - Work directory: `/app/services`  
  - Role: core local content filter, safety boundary, and fail-closed gate for explicitly Guardian-governed operations.  
  - Health route: `GET /health`  
  - Filter route: `POST /filter`  
  - Rollback image: `jarvis-blood-brain-barrier:asbuilt-20260728`

- **Constitutional guardian:**  
  - Service: `jarvis-constitutional-guardian`  
  - Host port: `127.0.0.1:8091->8091/tcp`  
  - Network: `qualia-net`  
  - Role: audit and guardrail service for higher-level policy checks and explicit governed data operationalization.  
  - Health route: `GET /health`

- **Hilbert time (H_t):**  
  - Service: `jarvis-hilbert-time`  
  - Host port: `127.0.0.1:18094->8092/tcp`  
  - Network: `qualia-net`  
  - Role: time service with Redis tiers for ephemeral/staged time and Postgres for historical time.

- **Hilbert state (H_state):**  
  - Service: `jarvis-hilbert-state`  
  - Host port: `127.0.0.1:18092->8081/tcp`  
  - Networks: `hilbert-net`, `qualia-net`  
  - Role: state snapshots and transitions, available to other services over an internal API.

These services are what make the rest of the stack more than just a pile of models. They give the system a notion of **time, state, safety, and law**, all exposed through real container ports.

---

## 19.4 Neurobiological Master and EEG Routing

The Neurobiological Master is the live integration service for the neurobiological pipeline and compatible EEG rhythm telemetry.

- **Neurobiological Master:**  
  - Service: `jarvis-neurobiological-master`  
  - Internal port: `8018/tcp`  
  - Network: `qualia-net`  
  - Live image: `msjarvis-neurobiological-master:eeg-compat-canary-20260817`  
  - Restart policy: `unless-stopped`  
  - Work directory: `/app/services`  
  - Runtime configuration includes:
    - `OLLAMA_HOST=http://jarvis-ollama:11434`
    - `SERVICE_PORT=8018`
    - `SERVICE_REDIS_HOST=jarvis-redis`
    - `SERVICE_REDIS_PORT=6379`
  - Rollback image: `msjarvis-neurobiological-master:integration-canary-20260817`

The Master exposes the following internal routes:

| Route | Method | Role |
|---|---|---|
| `/health` | `GET` | Confirms Master health, service port, integration state, and current process count |
| `/biological_process` | `POST` | Runs the established neurobiological processing pipeline |
| `/eeg_pulse` | `POST` | Accepts compatible EEG rhythm telemetry |
| `/eeg_pulse/status` | `GET` | Reports the latest process-local accepted pulse per observed rhythm |

The Master is reached from peer services on `qualia-net` through the Docker service name:

```text
http://jarvis-neurobiological-master:8018
```

This service-name route is the current internal network contract. Containers on `qualia-net` do not need to discover a changing container IP address.

### EEG producer route

EEG producers send telemetry to the Neurobiological Master:

```text
POST http://jarvis-neurobiological-master:8018/eeg_pulse
```

They do not post to an old missing EEG status endpoint, a BBB endpoint, or a consciousness-bridge endpoint.

A compatible pulse contains a rhythm, pulse value, timestamp, and optional payload:

```json
{
  "rhythm": "delta",
  "pulse": 2755,
  "timestamp": "2026-08-17T19:54:06.779391",
  "payload": {
    "service_states": {
      "gateway": "UP"
    }
  }
}
```

The Master accepts a compatible pulse with HTTP 202:

```json
{
  "status": "accepted",
  "rhythm": "delta",
  "pulse": 2755
}
```

HTTP 202 means that the Master accepted the telemetry event for the compatibility interface. It does not mean that the event has clinical significance, created durable EEG storage, crossed a promotion boundary, or received constitutional authorization.

### EEG status behavior

The Master exposes current EEG compatibility status through:

```text
GET http://jarvis-neurobiological-master:8018/eeg_pulse/status
```

This endpoint reports the latest accepted record for each observed rhythm during the current Master process lifetime. It is an in-memory, process-local status surface.

A representative response is:

```json
{
  "status": "ok",
  "rhythms": {
    "delta": {
      "rhythm": "delta",
      "pulse": 2755,
      "timestamp": "2026-08-17T19:54:06.779391",
      "received_at": "2026-08-17T19:54:06.791874"
    },
    "theta": {
      "rhythm": "theta",
      "pulse": 1525,
      "timestamp": "2026-08-17T19:54:21.339804",
      "received_at": "2026-08-17T19:54:21.350838"
    },
    "beta": {
      "rhythm": "beta",
      "pulse": 273,
      "timestamp": "2026-08-17T19:49:35.287623",
      "received_at": "2026-08-17T19:49:35.296678"
    }
  }
}
```

The status resets when the Master process or container restarts unless a separate durable telemetry store is introduced. It is not a clinical EEG record, medical system, or persistent telemetry ledger.

Production observation confirmed accepted Delta, Theta, and Beta rhythm traffic, with each rhythm accepted through `POST /eeg_pulse` using HTTP 202.

---

## 19.5 Memory and Vector Services

The stack includes a dedicated vector store for memory and retrieval:

- **Chroma:**  
  - Service: `jarvis-chroma`  
  - Host port: `127.0.0.1:8002->8000/tcp`  
  - Network: `qualia-net`  
  - Role: main vector database for memories, safety rules, GBIM embeddings, and automated learner sinks.

Chroma is the backing store for many of the “hippocampus” and “learning pathway” metaphors from other chapters. In practice, it is another container on `qualia-net` with a health endpoint and a port, but its collections carry much of the learned and constitutional content.

---

## 19.6 Internal Sandbox Service

The internal sandbox is a first-class service in the container graph:

- **Internal sandbox:**  
  - Service: `ms-allis-internal-sandbox`  
  - Host port: `127.0.0.1:8042->8042/tcp`  
  - Networks: `jarvis_ch14_bridge_net`, `msjarvis-rebuild_default`, `qualia-net`  
  - Health: responds 200 with `status: healthy`, `service: ms_allis_internal_sandbox`, `version: 1.2.0`, and `bbb_enforced: true`.

The sandbox’s job is to host **reversible deliberation**. It can think, compare, and stage hypotheses, but it has no direct authority to write to production tables or emit committed actions. That authority only arrives later, after BBB review and bridge promotion.

The probe output confirms that:

- a dedicated sandbox route is present;  
- the sandbox can see the **consciousness bridge** dependency;  
- sandbox status reports connectivity to EEG bands, pituitary, I-containers, qualia orchestrator, judge-truth, and guardian.

For a rural developer, the main command is simple:

```text
curl http://127.0.0.1:8042/health
```

If that returns healthy with `bbb_enforced: true`, the sandbox is up and fenced.

---

## 19.7 Consciousness Bridge Visibility

The sandbox’s health overlay shows that it can see the consciousness bridge:

- `consciousness_bridge: true` in `services_alive`  
- `consciousness_bridge_url: "http://jarvis-consciousness-bridge:8018"`  
- A separate health check reports the bridge itself at port 8010 with capabilities like multi-agent processing, memory integration, and synthesis.

This proves that:

- sandbox outputs that pass review can be promoted across a named bridge;  
- the bridge is a real container with its own health endpoint, not just a drawing.

The chapter does not claim that the bridge bypasses BBB. Promotion routes through safeguards first; the bridge is where **approved** state gets integrated into higher-level behavior.

The Neurobiological Master’s internal pipeline uses peer services on `qualia-net`, including BBB, I-Containers, Qualia, and consciousness-bridge-related integration. The verified Master pipeline continued through these components after the EEG compatibility and BBB fail-closed deployments.

---

## 19.8 Commons and Gateway Layer

Earlier runs of the gate blocked until a **commons gateway** container was restored. Once the gateway container is running, the routing picture is:

- Commons-facing traffic enters through the gateway stack rather than bare model endpoints.  
- The gateway routes into the unified chat/gateway service, which then fans out into sandbox, BBB, and downstream services.  
- Host-published ports for commons access remain bound to `127.0.0.1`, with outer exposure handled by a tunnel or reverse proxy.

This keeps public entry points separated from internal container ports, so a misconfigured firewall cannot accidentally expose raw judges, sandbox services, EEG compatibility interfaces, or Guardian routes.

---

## 19.9 Routing Map: Step-by-Step for Rural Developers

A typical routed request follows a pattern like this:

1. **Entry through gateway.**  
   A request arrives at the commons gateway, is authenticated, and is passed to the internal chat/gateway service.

2. **Dispatch to sandbox.**  
   For reasoning work, the gateway sends the job to `ms-allis-internal-sandbox` on port 8042.

3. **Sandbox deliberation.**  
   The sandbox coordinates with EEG, pituitary, I-containers, and retrieval to form candidate conclusions. Everything remains internal and reversible at this stage.

4. **Return and classification.**  
   The sandbox returns either a validated candidate or a non-validated provisional result. Executive coordination routes only validated candidates further.

5. **BBB review.**  
   The candidate is sent through `jarvis-blood-brain-barrier` at port 8016, where local ethical, spiritual, safety, and threat safeguards are applied.

6. **Guardian review where applicable.**  
   The Constitutional Guardian at port 8091 is a separate high-assurance authority path for explicit `user-data-operationalization`. Ordinary BBB content filtering is not falsely represented as a Guardian authorization. Guardian-governed failures deny rather than allow.

7. **Neurobiological processing where routed.**  
   The Neurobiological Master receives compatible requests at `jarvis-neurobiological-master:8018`. Its `/biological_process` route coordinates the BBB, I-Containers, Qualia, and related integration services.

8. **EEG rhythm telemetry where present.**  
   Delta, Theta, and Beta producers post compatible rhythm pulses to `jarvis-neurobiological-master:8018/eeg_pulse`. The Master accepts them with HTTP 202 and retains the latest observed pulse for each rhythm in process-local memory.

9. **Bridge promotion.**  
   Approved candidates cross the consciousness bridge and become part of active response or memory flows according to the relevant safeguards and promotion rules.

10. **Response and logging.**  
    The final result travels back through the gateway, and all steps are logged along the way.

Every major hop in that list corresponds to a real container and port, and every governance or health step has a live endpoint that can be called from the host or from an authorized peer container.

---

## 19.10 As-Built Deployment and Rollback State

The August 17, 2026 deployments established explicit image and rollback relationships for the Master and BBB.

| Service | Live image | Rollback image | Network | Restart policy |
|---|---|---|---|---|
| Neurobiological Master | `msjarvis-neurobiological-master:eeg-compat-canary-20260817` | `msjarvis-neurobiological-master:integration-canary-20260817` | `qualia-net` | `unless-stopped` |
| Blood-Brain Barrier | `jarvis-blood-brain-barrier:guardian-failclosed-canary-20260817` | `jarvis-blood-brain-barrier:asbuilt-20260728` | `qualia-net` | `unless-stopped` |

Both services run from `/app/services`.

The Master promotion was validated with:

- `GET /health` returning HTTP 200;
- `POST /biological_process` returning HTTP 200;
- `POST /eeg_pulse` returning HTTP 202;
- `GET /eeg_pulse/status` returning HTTP 200.

The BBB promotion was validated with:

- `GET /health` returning HTTP 200;
- generic `POST /filter` traffic passing local BBB safeguards while recording Guardian as `not_applicable`;
- explicitly Guardian-governed traffic without credentials being denied;
- invalid Guardian credentials resulting in preserved HTTP 401 denial rather than fail-open approval.

After BBB promotion, the Master pipeline was tested again and completed successfully with BBB approval, I-Containers present, Qualia processing completed, and the existing bridge fallback status preserved.

These rollback images are retained so the host can return to the immediately preceding known image if a later deployment validation fails. A rollback is an operational recovery action, not evidence that the current production image is unhealthy.

---

## 19.11 What This Chapter Does Not Claim

Within this gate, Chapter 19 stays within a bounded scope:

- It does **not** claim perfect uptime. Containers will restart, pull new images, and occasionally fail health checks.  
- It does **not** claim that every historical container in the 165-service stack is still needed. Some are legacy or experimental.  
- It does **not** claim that all ports are public APIs; many are bound to `127.0.0.1` or remain available only on internal Docker networks.  
- It does **not** claim that routing can never drift; compose files, images, service names, and host bindings can change over time.  
- It does **not** claim Kubernetes or a cloud-native orchestrator; this is a Docker Compose deployment on one host.  
- It does **not** claim that EEG pulse acceptance is clinical interpretation, durable telemetry retention, or a new route around BBB and promotion controls.  
- It does **not** claim that the Guardian authority path is active for ordinary traffic; governed data operationalization remains intentionally unavailable and fail closed until separately authorized.

The point of this chapter is to document the **current**, inspectable architecture, not to promise it will never evolve.

---

## 19.12 How to Inspect the Architecture Yourself

For rural developers who want to see this with their own eyes:

- List services and ports:

  ```text
  docker compose ps
  ```

- Check critical health endpoints from the host:

  ```text
  curl http://127.0.0.1:8016/health    # BBB
  curl http://127.0.0.1:8091/health    # guardian
  curl http://127.0.0.1:8002/health    # Chroma
  curl http://127.0.0.1:18094/health   # Hilbert time
  curl http://127.0.0.1:18092/health   # Hilbert state
  curl http://127.0.0.1:8042/health    # sandbox
  ```

- Inspect the Master through an authorized peer container on `qualia-net`:

  ```text
  GET http://jarvis-neurobiological-master:8018/health
  GET http://jarvis-neurobiological-master:8018/eeg_pulse/status
  ```

- Inspect the BBB through an authorized peer container on `qualia-net`:

  ```text
  GET http://jarvis-blood-brain-barrier:8016/health
  ```

- Inspect networks:

  ```text
  docker network inspect qualia-net
  ```

Those commands give you the same evidence the gate used: which containers are present, which ports are mapped, which images are live, and which networks tie the stack together.

---

## 19.13 Closing Statement

Chapter 19 records the container architecture and routing as they actually run today: Compose-managed services, unique host-published ports, live BBB, Guardian, Master, sandbox, Hilbert, and Chroma services, and a sandbox that can see its consciousness bridge.

The Neurobiological Master now provides a live EEG compatibility interface on `qualia-net`. Delta, Theta, and Beta producers post pulses to the Master at `/eeg_pulse`; the Master accepts compatible telemetry with HTTP 202 and reports the latest process-local state at `/eeg_pulse/status`. This interface preserves rather than replaces the established Master pipeline through BBB, I-Containers, Qualia, and bridge integration.

For a geographer-turned-developer, this is the map of Ms. Allis’s body: not imagined, but inspectable—one container, port, Docker network, health route, and governed routing path at a time.
