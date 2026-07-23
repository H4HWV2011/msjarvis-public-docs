# 19. Container Architecture and Routing

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 19.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis is actually wired as a set of containers, ports, and networks, not just as an idea on a whiteboard. It shows how reasoning, safeguards, time and state services, and commons‑facing gateways are stitched together on one host.

It supports:

- **P1 – Every where is entangled** by showing that memory, safeguards, time, and sandbox reasoning are connected services, even though they live in separate containers.  
- **P3 – Power has a geometry** by locating authority in network attachments, host ports, and routing paths instead of vague “intelligence.”  
- **P5 – Design is a geographic act** by treating Docker networks and host bindings as a map of where state is allowed to travel.  
- **P12 – Intelligence with a ZIP code** by tying container routing to West‑Virginia–grounded GBIM and Chroma services.  
- **P16 – Power accountable to place** by keeping the routes between sandbox, BBB, guardian, and promotion visible and auditable.

This chapter belongs to the **Computational Instrument** tier. It documents the as‑built container topology and host route map that carry Ms. Allis’s work.

---

## 19.2 High‑Level Container Topology

On the running host, Ms. Allis is deployed as a large Docker Compose stack. At the time of this chapter:

- A single `docker-compose.yml` file defines **165 services**.  
- There are **no duplicate published host ports**, so each exposed port has a unique mapping.  
- Critical governance, memory, sandbox, Hilbert, and Chroma services are up and reachable through health endpoints.

For rural developers, that means you can SSH into the box, run a single `docker compose ps` command, and see the whole working nervous system: which containers are up, which ports are bound to `127.0.0.1`, and which networks tie them together.

---

## 19.3 Core Governance and Time Services

Several governance and time services anchor the architecture:

- **Blood–Brain Barrier (BBB):**  
  - Service: `jarvis-blood-brain-barrier`  
  - Host port: `127.0.0.1:8016->8016/tcp`  
  - Network: `qualia-net`  
  - Role: core constitutional filter and post‑quantum signature verifier on both input and output.

- **Constitutional guardian:**  
  - Service: `jarvis-constitutional-guardian`  
  - Host port: `127.0.0.1:8091->8091/tcp`  
  - Network: `qualia-net`  
  - Role: audit and guardrail service for higher‑level policy checks.

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

These services are what make the rest of the stack more than just a pile of models. They give the system a notion of **time, state, and law**, all exposed through real container ports.

---

## 19.4 Memory and Vector Services

The stack includes a dedicated vector store for memory and retrieval:

- **Chroma:**  
  - Service: `jarvis-chroma`  
  - Host port: `127.0.0.1:8002->8000/tcp`  
  - Network: `qualia-net`  
  - Role: main vector database for memories, safety rules, GBIM embeddings, and automated learner sinks.

Chroma is the backing store for many of the “hippocampus” and “learning pathway” metaphors from other chapters. In practice, it is just another container on `qualia-net` with a health endpoint and a port, but its collections carry most of the learned and constitutional content.

---

## 19.5 Internal Sandbox Service

The internal sandbox is a first‑class service in the container graph:

- **Internal sandbox:**  
  - Service: `ms-allis-internal-sandbox`  
  - Host port: `127.0.0.1:8042->8042/tcp`  
  - Networks: `jarvis_ch14_bridge_net`, `msjarvis-rebuild_default`, `qualia-net`  
  - Health: responds 200 with `status: healthy`, `service: ms_allis_internal_sandbox`, `version: 1.2.0`, and `bbb_enforced: true`.

The sandbox’s job is to host **reversible deliberation**. It can think, compare, and stage hypotheses, but it has no direct authority to write to production tables or emit committed actions. That authority only arrives later, after BBB review and bridge promotion.

The probe output confirms that:

- a dedicated sandbox route is present;  
- the sandbox can see the **consciousness bridge** dependency;  
- sandbox status reports connectivity to EEG bands, pituitary, I‑containers, qualia orchestrator, judge-truth, and guardian.

For a rural developer, the main command is simple:

```text
curl http://127.0.0.1:8042/health
```

If that returns healthy with `bbb_enforced: true`, the sandbox is up and fenced.

---

## 19.6 Consciousness Bridge Visibility

The sandbox’s health overlay shows that it can see the consciousness bridge:

- `consciousness_bridge: true` in `services_alive`  
- `consciousness_bridge_url: "http://jarvis-consciousness-bridge:8018"`  
- A separate health check reports the bridge itself at port 8010 with capabilities like multi‑agent processing, memory integration, and synthesis.

This proves that:

- sandbox outputs that pass review can be promoted across a named bridge;  
- the bridge is a real container with its own health endpoint, not just a drawing.

The chapter does not claim that the bridge bypasses BBB. Promotion always routes through safeguards first; the bridge is where **approved** state gets integrated into higher‑level behavior.

---

## 19.7 Commons and Gateway Layer

Earlier runs of the gate blocked until a **commons gateway** container was restored. Once the gateway container is running, the routing picture is:

- Commons‑facing traffic enters through the gateway stack rather than bare model endpoints.  
- The gateway routes into the unified chat/gateway service, which then fans out into sandbox, BBB, and downstream services.  
- Host‑published ports for commons access remain bound to `127.0.0.1`, with outer exposure handled by a tunnel or reverse proxy.

This keeps public entry points separated from internal container ports, so a mis‑configured firewall cannot accidentally expose raw judges or sandbox services.

---

## 19.8 Routing Map: Step‑by‑Step for Rural Developers

A typical routed request follows a pattern like this:

1. **Entry through gateway.**  
   A request arrives at the commons gateway, is authenticated, and is passed to the internal chat/gateway service.

2. **Dispatch to sandbox.**  
   For reasoning work, the gateway sends the job to `ms-allis-internal-sandbox` on port 8042.

3. **Sandbox deliberation.**  
   The sandbox coordinates with EEG, pituitary, I‑containers, and retrieval to form candidate conclusions. Everything remains internal and reversible at this stage.

4. **Return and classification.**  
   The sandbox returns either a validated candidate or a non‑validated provisional result. Executive coordination routes only validated candidates further.

5. **BBB review.**  
   The candidate is sent through `jarvis-blood-brain-barrier` at 8016, where filters, judges, and signatures are checked.

6. **Guardian review.**  
   The constitutional guardian at 8091 may perform additional policy checks, especially on consequential actions.

7. **Bridge promotion.**  
   Approved candidates cross the consciousness bridge (internal URL at port 8018, host‑visible at 8010) and become part of active response or memory flows.

8. **Response and logging.**  
   The final result travels back through the gateway, and all steps are logged along the way.

Every major hop in that list corresponds to a real container and port, and every governance step has a live health endpoint you can call from the host.

---

## 19.9 What This Chapter Does Not Claim

Within this gate, Chapter 19 stays within a bounded scope:

- It does **not** claim perfect uptime. Containers will restart, pull new images, and occasionally fail health checks.  
- It does **not** claim that every historical container in the 165‑service stack is still needed. Some are legacy or experimental.  
- It does **not** claim that all ports are public APIs; many are bound to `127.0.0.1` for local routing only.  
- It does **not** claim that routing can never drift; compose files and host bindings can change over time.  
- It does **not** claim Kubernetes or a cloud‑native orchestrator; this is a Docker Compose deployment on one host.

The point of this chapter is to document the **current**, inspectable architecture, not to promise it will never evolve.

---

## 19.10 How to Inspect the Architecture Yourself

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

- Inspect networks:

  ```text
  docker network inspect qualia-net
  ```

Those commands give you the same evidence the gate used: which containers are present, which ports are mapped, and which networks tie the stack together.

---

## 19.11 Closing Statement

Chapter 19 records the container architecture and routing as they actually run today: 165 Compose‑managed services, unique host‑published ports, live BBB, guardian, sandbox, Hilbert, and Chroma services, and a sandbox that can see its consciousness bridge.

For a geographer‑turned‑developer, this is the map of Ms. Allis’s body: not imagined, but inspectable—one container, port, and Docker network at a time.
