# 10. WOAH: Weighted Optimization Algorithm Hierarchy

Carrie Kidd (Mamma Kidd) — Mount Hope, WV

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Jarvis coordinates many specialized agents as a **population**, rather than relying on a single model, and how that coordination is constrained by spatial-justice goals. It supports:

- **P1 – Every where is entangled** by treating governance, spatial, and narrative agents as a coupled population whose influence is jointly optimized, not siloed.
- **P3 – Power has a geometry** by shaping how optimization pressure flows through the service graph, deciding which agents' outputs are amplified or muted for particular places and tasks.
- **P5 – Design is a geographic act** by making orchestration weights and routing strategies first-class design choices that affect how West Virginia is seen and served.
- **P12 – Intelligence with a ZIP code** by privileging agents and retrieval paths that are explicitly grounded in Appalachian data and institutions.
- **P16 – Power accountable to place** by keeping WOAH as a glass-box service that can, in principle, expose how different agents were weighted in producing an answer.

This chapter belongs to the **Computational Instrument** tier: it specifies a WOA-inspired orchestration layer that coordinates Ms. Jarvis's multi-agent "mind" in service of Quantarithmia's justice-oriented instruments.

> Figure 10.1. WOAH as a WOA-inspired orchestration service in Ms. Jarvis, weighting multiple agents and feeding those weights into the consciousness and routing stack with Appalachian, place-aware priorities.

---

# WOAH: Weighted Optimization Algorithm Hierarchy

This chapter describes WOAH (Weighted Optimization Algorithm Hierarchy) as used in Ms. Egeria Jarvis. WOAH is inspired by the Whale Optimization Algorithm (WOA), a population-based metaheuristic that models humpback whale hunting with exploration and exploitation phases, but it is not a textbook WOA implementation. In this system, WOAH is a set of concrete Python services that evaluate and weight multiple agents (LLMs, DGMs, RAG paths) and feed those weights into the consciousness and orchestration layers, helping coordinate many minds rather than optimizing a single numeric function.

WOAH should therefore be understood as a WOA-inspired orchestration pattern implemented as a web service, with classical scoring and weighting logic, rather than as a fully formal WOA with provable convergence guarantees.

---

## Deployment Status (March 25, 2026)

### Container Status: RUNNING ✅

As of March 25, 2026, `jarvis-woah` (port 7012) is **confirmed RUNNING** on `qualia-net` (IP `172.18.0.x`).

**Previous failure and root cause:** The container was previously exiting with code 1 due to `ModuleNotFoundError: No module named 'uvicorn'`. The original stub attempted to import uvicorn and FastAPI, which are not present in the `python:3.11-slim` base image. This caused the container to exit immediately at startup.

**Resolution:** The stub was replaced with a `woah_stub.py` implementation using Python's stdlib `http.server` module, requiring no external dependencies. The file is mounted via a volume bind mount in `docker-compose.yml` and executed directly.

**Network fix:** `jarvis-woah` is confirmed on `qualia-net`. The DNS resolution failure that was previously observed from `jarvis-consciousness-bridge` was caused by the container not starting (exit code 1), not by any network misconfiguration. Once the container starts successfully, DNS resolution via `qualia-net` resolves correctly. No changes to network configuration were required.

### Correct docker-compose.yml Entry

> **⚠️ Deployment Method Note:** Inline command strings with multiline Python are unreliable in Docker Compose YAML and must not be used. The correct deployment method is a volume bind mount. The stub file `woah_stub.py` must exist on the host alongside `docker-compose.yml`.

```yaml
jarvis-woah:
  image: python:3.11-slim
  container_name: jarvis-woah
  volumes:
    - ./woah_stub.py:/woah_stub.py
  command: ["python3", "/woah_stub.py"]
  networks:
    - qualia-net
```

Key points:
- `image: python:3.11-slim` — no pip installs required; stdlib only
- `volumes: - ./woah_stub.py:/woah_stub.py` — bind mount, not inline command
- `command: ["python3", "/woah_stub.py"]` — exec form, not shell form
- `networks: - qualia-net` — same network as `jarvis-consciousness-bridge` and `jarvis-fifth-dgm`

### woah_stub.py Reference Implementation

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class WOAHHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "status": "ok",
                "service": "jarvis-woah",
                "port": 7012
            }).encode())

    def do_POST(self):
        if self.path == "/process":
            content_length = int(self.headers.get("Content-Length", 0))
            self.rfile.read(content_length)  # consume body
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "status": "ok",
                "content": "WOAH stub reasoning complete",
                "confidence": 0.8
            }).encode())

    def log_message(self, format, *args):
        pass  # suppress access logs

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 7012), WOAHHandler)
    print("jarvis-woah stub listening on port 7012", flush=True)
    server.serve_forever()
```

### WOAH Service Port Reference (March 25, 2026)

| Service | Host Port | Container Port | Network | Status |
|---|---|---|---|---|
| `jarvis-woah` | 7012 | 7012 | qualia-net | ✅ RUNNING — stdlib stub |
| `nbb_woah_algorithms` | 8104 | 8010 | internal | ✅ RUNNING — FastAPI, full scoring |

---

## Classical Whale Optimization Algorithm

The original Whale Optimization Algorithm (WOA) is a population-based optimization method that models humpback whales' bubble-net hunting behavior.

Key features of WOA:

- **Population and best agent** — A set of candidate solutions (whales) explores a search space, and the current best candidate guides others.
- **Encircling prey** — Agents update their positions relative to the best solution using coefficients that shrink over time, balancing exploration and exploitation.
- **Spiral and bubble-net search** — A spiral equation models whales' bubble-net feeding, allowing candidate solutions to move around the best in a shrinking spiral trajectory.

WOAH in Ms. Jarvis borrows the ideas of populations, encircling, and weighted movement toward better candidates, but adapts them to agent orchestration rather than direct numeric parameter search.

---

## WOAH in Ms. Jarvis: Conceptual Role

In Ms. Jarvis, WOAH refers to a hierarchy of weighting and evaluation processes that sit between low-level agents and higher-level consciousness or orchestration:

- **Multiple agents as "whales"** — Different LLMs, DGMs, RAG paths, and analysis services act as candidate "whales," each producing outputs or evaluations over the same user query or memory item.
- **Weighted evaluation** — WOAH services analyze those outputs and assign weights or scores indicating how much influence each agent should have for a given task, user, or place.
- **Hierarchical integration** — These weights are fed into consciousness coordinators, qualia engines, and judge layers that combine agent outputs into a final response.

---

## The WOAH Algorithms Service (nbb_woah_algorithms, port 8104)

The central, production-grade piece of WOAH in Ms. Jarvis is the **WOAH algorithms service**, a standalone FastAPI application listening on host port 8104 (container internal port 8010). It exposes a stable surface:

- `GET /health` — reports liveness and version information
- `POST /process` — accepts structured JSON input with:
  - `content`: a free-text string (e.g., a user utterance or narrative)
  - `metadata`: a JSON object with optional contextual tags (source, theme, county)

### Semantic Identity Weighting Function

Internally, the service implements a **semantic identity weighting function**:

- Tokenizes content into words; rejects very short inputs as low-weight noise
- Detects high-value keywords associated with Appalachian governance, community, heritage, and MountainShares work
- Detects low-value keywords associated with tests, spam, or transient information
- Computes a **hierarchical identity weight** between 0.0 and 1.0:

| Range | Interpretation |
|---|---|
| 0.9–1.0 | Core identity |
| 0.75–0.89 | Strong identity |
| 0.5–0.74 | Moderate interest |
| 0.25–0.49 | Low interest |
| 0.0–0.24 | Very low interest or test content |

On top of this scalar, the service performs a **decomposition** into:

- `self_relevance`
- `temporal_importance`
- `novelty`
- `stability`

and derives:

- `composite_weight` — a weighted combination of these axes
- `identity_type` — currently "structural" vs "episodic" based on thresholding
- `weight_category` — a human-readable bucket such as `strong_identity`

The `POST /process` response includes all of these values alongside the original content and metadata.

---

## WOA-Inspired Population Dynamics

WOAH maintains an **internal population of weight vectors** updated in a WOA-inspired way:

- A small in-memory population of candidates, each a vector over:
  - `hierarchical_weight`
  - `self_relevance`
  - `temporal_importance`
  - `novelty`
  - `stability`

- An update policy that:
  - Records each new weight vector coming out of `POST /process`
  - Periodically runs WOA-style update steps using:
    - An **encircling** update that pulls candidates toward the current best vector
    - A **spiral** update that moves candidates around the best in a contracting spiral
  - Iterates over a bounded number of steps

The WOAH algorithms service calls into this module on every `/process` request: after computing the semantic identity weight, it packages the axes into a weight vector, records it into the population, and advances the population by one step. Each identity evaluation also nudges the internal population, slowly shaping a policy over which kinds of memories and contexts are treated as more central.

---

## The `/woah_population_debug` Endpoint

To make the population **visible and accountable**, the WOAH algorithms service exposes:

- `GET /woah_population_debug` — returns the current internal population:

```json
{
  "population": [
    {
      "hierarchical_weight": 0.21508379888268156,
      "self_relevance": 0.21508379888268156,
      "temporal_importance": 0.21508379888268156,
      "novelty": 0.13966480446927373,
      "stability": 0.21508379888268156
    }
  ]
}
```

This endpoint provides:
- A **glass-box view** into the evolving WOA-style policy
- Concrete data that can be plotted or analyzed to determine how the population moves as Ms. Jarvis processes more Appalachian narratives and governance memories
- A basis for **Polymathmatic Geography instrumentation**: WOAH is not just conceptual, but running as a dynamical system in production

---

## WOAH in the Consciousness and Orchestration Stack

WOAH occupies an intermediate layer in the Ms. Jarvis architecture:

**Upstream layers:**
- Direct user queries reaching the unified gateway
- Domain-specific agents and services: RAG and ChromaDB lookups, Hilbert-space spatial reasoning, neurobiological and consciousness services, specialized governance and spatial agents

**WOAH layer:**
- Called when the system needs to decide:
  - Whether a new memory should be treated as structural or episodic
  - How important a given narrative is to the user's autobiographical profile
  - How to weight this memory in downstream decisions about storage and promotion into long-term containers
- The WOA-inspired population module updates its policy with each evaluation

**Downstream layers:**
- The Fifth DGM (port 4002) tracks how many inputs have been evaluated by WOAH, how many were accepted into subconscious or I-containers, and timestamps of the most recent WOAH evaluations
- Consciousness coordinators and bridges (including `jarvis-consciousness-bridge`, port 8020) record when WOAH was used as one of the services in an end-to-end pipeline
- WOAH's identity weights influence which memories are promoted, how they are indexed, and how strongly they shape future responses

### Service Integration: jarvis-woah vs nbb_woah_algorithms

jarvis-consciousness-bridge (port 8020)
│
├──→ jarvis-woah (port 7012, qualia-net)
│ GET / → health check
│ POST /process → stub response:
│ {status: ok,
│ content: "WOAH stub reasoning complete",
│ confidence: 0.8}
│
└──→ (internal) nbb_woah_algorithms (port 8104 host / 8010 container)
POST /process → full semantic identity scoring
+ WOA population dynamics
GET /woah_population_debug → population state

text

**Calling jarvis-woah from other containers (qualia-net):**

```python
import httpx

# Health check
resp = httpx.get("http://jarvis-woah:7012/")
# {"status": "ok", "service": "jarvis-woah", "port": 7012}

# Process call
resp = httpx.post(
    "http://jarvis-woah:7012/process",
    json={"content": "community resource query", "context": {}}
)
# {"status": "ok", "content": "WOAH stub reasoning complete", "confidence": 0.8}
```

**Calling nbb_woah_algorithms from host (full scoring):**

```python
import httpx

resp = httpx.post(
    "http://127.0.0.1:8104/process",
    json={
        "content": "MountainShares cooperative economic development in Fayette County",
        "metadata": {"source": "governance", "county": "Fayette"}
    }
)
# Returns: hierarchical_weight, self_relevance, temporal_importance,
#          novelty, stability, composite_weight, identity_type, weight_category
```

---

## Confirmed Operational State (March 25, 2026)

| Check | Result |
|---|---|
| `jarvis-woah` container status | ✅ RUNNING (was: Exiting 1) |
| Root cause of previous failure | `ModuleNotFoundError: No module named 'uvicorn'` — resolved by stdlib stub |
| Deployment method | Volume bind mount `./woah_stub.py:/woah_stub.py` — NOT inline command string |
| Network: qualia-net membership | ✅ Confirmed — IP `172.18.0.x` |
| DNS from `jarvis-consciousness-bridge` | ✅ Resolves correctly once container is running |
| `GET /` health | ✅ 200 OK |
| `POST /process` stub response | ✅ `{status: ok, content: "WOAH stub reasoning complete", confidence: 0.8}` |
| `nbb_woah_algorithms` (port 8104) | ✅ RUNNING — full FastAPI scoring service |
| Fifth DGM WOAH evaluation cycles | ✅ Recording successful WOAH evaluations |
| `jarvis-consciousness-bridge` ChromaDB v2 call | ✅ `/api/v2/heartbeat` → 200 |

**DNS resolution note:** The DNS failure from `jarvis-consciousness-bridge` to `jarvis-woah` was previously reported as a potential network misconfiguration. This has been confirmed as a **false diagnosis** — the failure was caused entirely by `jarvis-woah` exiting at startup (exit code 1). Docker's embedded DNS cannot resolve a container that is not running. No changes to `qualia-net` topology, DNS configuration, or bridge network settings were needed or made.

---

## Relationship to Classical WOA and Limitations

The relationship between WOAH and classical WOA is honest but partial:

**Conceptual borrowing:**
- Maintaining a **population** of candidates (here, weight vectors)
- Moving candidates toward a current best vector
- Using **encircling** and **spiral**-style updates to balance exploitation with limited exploration

**Implementation reality:**
- `jarvis-woah` (port 7012): stdlib `http.server` stub — provides health and stub `/process` response; no scoring logic
- `nbb_woah_algorithms` (port 8104): full FastAPI service with heuristic semantic identity scoring and WOA-inspired population dynamics
- The semantic identity scoring is **heuristic and rule-based**, not learned
- The population updates apply WOA-style formulas to a small, in-memory population, without claims of formal convergence or optimality
- The population is primarily used as an **instrument** for understanding how the system is weighting identity, not as the sole driver of routing decisions

This thesis presents WOAH as a **WOA-inspired orchestration pattern and identity-weighting instrument**, not as a mathematically complete, fully validated optimization algorithm.

---

## WOAH as a Computational Instrument for Place-Accountable Intelligence

From a Polymathmatic Geography perspective, WOAH functions as a **computational instrument** that connects algorithmic behavior to specific places and communities:

- By privileging Appalachian keyphrases and MountainShares themes in its semantic identity function, WOAH encodes a **place-specific prior** about what counts as core identity work.
- By decomposing identity into axes like `self_relevance`, `temporal_importance`, and `stability`, it offers a vocabulary for **geographic narrative structure** — which memories persist, which are fleeting, and how they are tied to particular counties or projects.
- By maintaining a population of weight vectors and exposing it via `/woah_population_debug`, it makes **power accountable to place**: researchers can see whether the optimization dynamics are drifting toward or away from the values and geographies the system claims to serve.

WOAH belongs in the **Computational Instrument** tier:
- It is not just a low-level library, but a first-class service whose weights shape the flow of information and influence
- It is explicitly designed to be **inspectable and tunable**, so that West Virginia communities and collaborators can see and adjust how their stories are being weighted
- It demonstrates how WOA-style ideas can be repurposed from pure numeric optimization into **place-grounded orchestration of many minds**, aligned with Quantarithmia's justice-oriented instruments

> **Status (March 25, 2026):** Both WOAH services are RUNNING. `jarvis-woah` (port 7012) is confirmed operational on qualia-net using the stdlib `http.server` stub deployed via volume bind mount. `nbb_woah_algorithms` (port 8104) implements the full heuristic semantic identity function, WOA-inspired population dynamics over weight vectors, and the `/woah_population_debug` endpoint for inspecting the internal population. Both services are actively integrated with the Fifth DGM consciousness metrics and the consciousness bridge pipeline. The stub's optimization theory, formal evaluation, and broader orchestration influence remain evolving areas of work.

