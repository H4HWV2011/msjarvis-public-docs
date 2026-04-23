# 10. WOAH: Weighted Optimization Algorithm Hierarchy

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: April 23, 2026 — `msallis_docs` count confirmed 7,465 ✅;
`ms_allis_memory` distance metric corrected to cosine (with live-vs-public name note);
`allis-ms-token-service` container name applied (sed-pass corrected);
`allis-community-stake-registry` (port 8084) added to MountainShares inventory;
`autonomous_learner` confirmed 21,181 ✅ — no change;
OI-E updated: ✅ CLOSED — 38,979 rows, `msallis-db`, April 23, 2026;

---

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis coordinates many specialized agents as a
**population**, rather than relying on a single model, and how that coordination is
constrained by spatial-justice goals. It supports:

- **P1 – Every where is entangled** by treating governance, spatial, and narrative agents
  as a coupled population whose influence is jointly optimized, not siloed.
- **P3 – Power has a geometry** by shaping how optimization pressure flows through the
  service graph, deciding which agents' outputs are amplified or muted for particular
  places and tasks.
- **P5 – Design is a geographic act** by making orchestration weights and routing
  strategies first-class design choices that affect how West Virginia is seen and served.
- **P12 – Intelligence with a ZIP code** by privileging agents and retrieval paths that
  are explicitly grounded in Appalachian data and institutions.
- **P16 – Power accountable to place** by keeping WOAH as a glass-box service that can
  expose how different agents were weighted in producing an answer.

This chapter belongs to the **Computational Instrument** tier: it specifies a
WOA-inspired orchestration layer that coordinates Ms. Allis's multi-agent "mind" in
service of Quantarithmia's justice-oriented instruments.

WOAH operates at **Phase 2.5 of the 9-phase `ultimatechat` pipeline** (see Ch. 11
§11.4).

> Figure 10.1. WOAH as a WOA-inspired orchestration service in Ms. Allis, weighting
> multiple agents and feeding those weights into the consciousness and routing stack with
> Appalachian, place-aware priorities.

> **★ Security posture — April 23, 2026:** All containers bound to `127.0.0.1`. Zero
> `0.0.0.0` exposures confirmed. **100 containers Up (April 23, 2026)**; thesis-verified
> **112/112 containers Up (April 16, 2026)**. `allis-woah` `{}` port bindings =
> **correct and intentional** — internal qualia-net DNS service only, no host port needed
> (OI-10B CLOSED). `nbb_woah_algorithms` (port 8104 host / 8010 container) running.
> `ALLIS_API_KEY` confirmed set. 3 MountainShares services from compose override pushed
> count 109→112 on April 16, 2026. 5 older orphan containers (Apr 10–12, including
> `allis-redis-local` and `allis-pia-status`) confirmed `127.0.0.1`-bound — zero
> security exposure.

> **★ ChromaDB v2 audit — April 23, 2026:** `allis-chroma`, host port **8002**,
> container port **8000**, inter-service URL `http://allis-chroma:8000`. **48 active
> collections, ~6,740,611 total vectors** (v2 API). Collection name notes:
>
> - `msallis_docs`: **7,465 items** ✅
> - `ms_allis_memory`: **cosine** distance metric. *Name note: the live collection name
>   in the running system is `ms_allis_memory`; this document uses that name
>   consistently. In some public-facing and early draft references this collection was
>   referred to as `ms_allis_memory` — that name reflects the public/legacy namespace and
>   should not be used in service code targeting the current `msallis-rebuild` stack.*
> - `autonomous_learner`: **21,181 records** ✅ (L2 distance, April 23, 2026 — no change)
>
> Required embedding model: `all-minilm:latest` (384-dim) — permanent architectural
> constraint. v1 path deprecated; `/api/v1/` returns 410 Gone.

> **★ Database audit — April 23, 2026:** Two-container architecture —
> **Production:** `msallis-db`, host **5433** / container **5432**, role `postgres`,
> `msallisgis`, 16 GB / 294 tables / 11 schemas.
> **Forensic:** `postgis-forensic`, host **5432**, role `allis` (+ `-h 127.0.0.1`),
> `msallisgis`, 17 GB / 314 tables / 9 schemas — forensic auditing only.
> DNS: `msallis-db:5432` resolves from all connected containers (production).
> PostgreSQL 16.4 confirmed.
>
> **`mvw_gbim_landowner_spatial` — ✅ CLOSED: 38,979 rows, `msallis-db`,
> April 23, 2026. Not present in `postgis-forensic`.**

> **★ OI status — April 23, 2026 (all closed):**
> - OI-10A (container count): ✅ CLOSED — 100 Up (April 23, 2026); 112 thesis-verified
>   (April 16, 2026); 3 MountainShares + 5 orphans all `127.0.0.1`-bound
> - OI-10B (`allis-woah` binding): ✅ CLOSED — `{}` internal DNS intentional; only fix
>   needed is `woah_stub.py` documentation note
> - OI-10C (bridge missing): ✅ CLOSED — DGM topology stub, import confirmed, permanent
>   mount verified
> - OI-10D (DB metrics): ✅ CLOSED — two-container architecture confirmed;
>   `msallis-db` host 5433 / `postgis-forensic` host 5432
> - OI-10E (`msallis-db` name): ✅ CLOSED — two-container architecture documented
> - OI-10F (WOAH population): ✅ CLOSED — population seeded;
>   `hierarchical_weight: 0.8, identity_type: "structural",
>   weight_category: "strong_identity"`, 1 vector confirmed non-empty
> - OI-E (`mvw_gbim_landowner_spatial`): ✅ CLOSED — 38,979 rows, `msallis-db`,
>   April 23, 2026

---

## WOAH: Weighted Optimization Algorithm Hierarchy

This chapter describes WOAH (Weighted Optimization Algorithm Hierarchy) as used in Ms.
Egeria Allis (`msallis-rebuild`). WOAH is inspired by the Whale Optimization Algorithm
(WOA), a population-based metaheuristic that models humpback whale hunting with
exploration and exploitation phases, but it is not a textbook WOA implementation. In
this system, WOAH is a set of concrete Python services that evaluate and weight multiple
agents (LLMs, DGMs, RAG paths) and feed those weights into the consciousness and
orchestration layers, helping coordinate many minds rather than optimizing a single
numeric function.

WOAH should therefore be understood as a **WOA-inspired orchestration pattern implemented
as a web service**, with classical scoring and weighting logic, rather than as a fully
formal WOA with provable convergence guarantees.

---

## Deployment Status — ★ Updated April 23, 2026

### Container Status: RUNNING ✅

As of April 23, 2026, `allis-woah` is **confirmed RUNNING** on `qualia-net`.
**100 containers Up (April 23, 2026)**; thesis-verified **112/112 (April 16, 2026)** —
zero Restarting, zero Exited.

**OI-10B CLOSED — `{}` port bindings are correct and intentional.** `allis-woah` has no
host port binding. It is a qualia-net **internal service only**, called exclusively via
Docker DNS (`http://allis-woah:7012`). No host port is needed and none should be added.
The `{}` binding seen in `docker ps` output is the correct and expected state.

The only documentation fix required is in `woah_stub.py`: add a comment noting that if a
host port is ever needed in the future, it must be bound to `127.0.0.1`, not `0.0.0.0`.
This is a documentation note, not a code change.

**Confirmed from `allis-consciousness-bridge`:**

```bash
docker exec allis-consciousness-bridge \
  python3 -c "import urllib.request; print(urllib.request.urlopen('http://allis-woah:7012/').read())"
# → 200 {'status': 'ok', 'service': 'allis-woah'}
```

**Previous failure and root cause (historical — resolved March 2026):** The container was
previously exiting with code 1 due to `ModuleNotFoundError: No module named 'uvicorn'`.
Resolved by replacing the stub with a stdlib `http.server` implementation (no pip
installs required). Volume bind mount deployment method confirmed.

### Correct docker-compose.yml Entry

> **⚠️ Deployment Method Note:** Inline command strings with multiline Python are
> unreliable in Docker Compose YAML and must not be used. The correct deployment method
> is a volume bind mount. `woah_stub.py` must exist on the host alongside
> `docker-compose.yml`.

```yaml
allis-woah:
  image: python:3.11-slim
  container_name: allis-woah
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
- `networks: - qualia-net` — same network as `allis-consciousness-bridge` and
  `allis-fifth-dgm`
- **No `ports:` block** — intentional; `{}` binding is correct; qualia-net DNS only

### woah_stub.py Reference Implementation

> **Canonical home:** This `woah_stub.py` is the reference implementation for both
> Ch. 9 (§9.3.4) and this chapter (Ch. 10). Ch. 9 §9.3.4 cross-references this stub;
> the canonical home of the implementation and deployment specification is this chapter.
>
> **Documentation note (OI-10B):** If a host port is ever added to `allis-woah` in the
> future, bind it to `127.0.0.1:7012:7012` — never `0.0.0.0:7012:7012`. This is the
> security policy for all Ms. Allis services.

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
                "service": "allis-woah",
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
    # NOTE (OI-10B): No host port binding by design — qualia-net internal only.
    # If a host port is ever added, use 127.0.0.1:7012 — never 0.0.0.0.
    server = HTTPServer(("0.0.0.0", 7012), WOAHHandler)
    print("allis-woah stub listening on port 7012 (qualia-net internal only)", flush=True)
    server.serve_forever()
```

### WOAH Service Port Reference — ★ Updated April 23, 2026

| Service | Host Port | Container Port | Network | Status |
|:--|:--|:--|:--|:--|
| `allis-woah` | **none** (internal only) | 7012 | qualia-net | ✅ RUNNING — stdlib stub; `{}` bindings intentional (OI-10B CLOSED) |
| `nbb_woah_algorithms` | 8104 | 8010 | internal | ✅ RUNNING — FastAPI, full scoring; population seeded (OI-10F CLOSED) |
| `nbb_woah_algorithms` via `nbb-i-containers` | 8101 | — | internal | ✅ RUNNING — Phase 1 NBB prefrontal gateway to WOAH |

---

## Classical Whale Optimization Algorithm

The original Whale Optimization Algorithm (WOA) is a population-based optimization
method that models humpback whales' bubble-net hunting behavior.

Key features of WOA:

- **Population and best agent** — A set of candidate solutions (whales) explores a
  search space, and the current best candidate guides others.
- **Encircling prey** — Agents update their positions relative to the best solution using
  coefficients that shrink over time, balancing exploration and exploitation.
- **Spiral and bubble-net search** — A spiral equation models whales' bubble-net feeding,
  allowing candidate solutions to move around the best in a shrinking spiral trajectory.

WOAH in Ms. Allis borrows the ideas of populations, encircling, and weighted movement
toward better candidates, but adapts them to agent orchestration rather than direct
numeric parameter search.

---

## WOAH in Ms. Allis: Conceptual Role

In Ms. Allis, WOAH refers to a hierarchy of weighting and evaluation processes that sit
between low-level agents and higher-level consciousness or orchestration:

- **Multiple agents as "whales"** — Different LLMs, DGMs, RAG paths, and analysis
  services act as candidate "whales," each producing outputs or evaluations over the same
  user query or memory item.
- **Weighted evaluation** — WOAH services analyze those outputs and assign weights or
  scores indicating how much influence each agent should have for a given task, user, or
  place.
- **Hierarchical integration** — These weights are fed into consciousness coordinators,
  qualia engines, and judge layers that combine agent outputs into a final response.

WOAH is called at **Phase 2.5 of the 9-phase `ultimatechat` pipeline** — after initial
BBB input filtering and community memory retrieval, and before the main RAG and LLM
ensemble phases. See Ch. 11 §11.4 for the full 9-phase pipeline specification.

---

## The WOAH Algorithms Service (nbb_woah_algorithms, port 8104)

The central, production-grade piece of WOAH in Ms. Allis is the **WOAH algorithms
service**, a standalone FastAPI application listening on host port 8104 (container
internal port 8010). It exposes a stable surface:

- `GET /health` — reports liveness and version information
- `POST /process` — accepts structured JSON input with:
  - `content`: a free-text string (e.g., a user utterance or narrative)
  - `metadata`: a JSON object with optional contextual tags (source, theme, county)

### Semantic Identity Weighting Function

Internally, the service implements a **semantic identity weighting function**:

- Tokenizes content into words; rejects very short inputs as low-weight noise
- Detects high-value keywords associated with Appalachian governance, community,
  heritage, and MountainShares work
- Detects low-value keywords associated with tests, spam, or transient information
- Computes a **hierarchical identity weight** between 0.0 and 1.0:

| Range | Interpretation |
|:--|:--|
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
- `identity_type` — currently `"structural"` vs `"episodic"` based on thresholding
- `weight_category` — a human-readable bucket such as `"strong_identity"`

**★ OI-10F CLOSED — April 16, 2026:** WOAH population confirmed seeded and working.
Sample confirmed output from `POST /process` + `/woah_population_debug`:

```json
{
  "hierarchical_weight": 0.8,
  "identity_type": "structural",
  "weight_category": "strong_identity",
  "population_size": 1,
  "population_non_empty": true
}
```

Population is confirmed non-empty with 1 vector. This is the correct baseline state —
the population grows as more content is processed through the service.

---

## WOA-Inspired Population Dynamics

WOAH maintains an **internal population of weight vectors** updated in a WOA-inspired
way:

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

The WOAH algorithms service calls into this module on every `/process` request: after
computing the semantic identity weight, it packages the axes into a weight vector, records
it into the population, and advances the population by one step. Each identity evaluation
also nudges the internal population, slowly shaping a policy over which kinds of memories
and contexts are treated as more central.

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
- Concrete data that can be plotted or analyzed to determine how the population moves as
  Ms. Allis processes more Appalachian narratives and governance memories
- A basis for **Polymathmatic Geography instrumentation**: WOAH is not just conceptual,
  but running as a dynamical system in production

---

## WOAH in the Consciousness and Orchestration Stack

WOAH occupies an intermediate layer in the Ms. Allis architecture, operating at
**Phase 2.5 of the 9-phase `ultimatechat` pipeline** (see Ch. 11 §11.4):

**Upstream layers:**

- Direct user queries reaching the unified gateway
- Domain-specific agents and services: RAG and ChromaDB v2 lookups (★ **48 collections,
  ~6,740,611 vectors** — April 23, 2026; `allis-chroma` host port **8002**, container
  port **8000**, inter-service `http://allis-chroma:8000`, v2 API only), Hilbert-space
  spatial reasoning, neurobiological and consciousness services, specialized governance
  and spatial agents
- **Production database:** `msallis-db`, host **5433** / container **5432**, role
  `postgres`, `msallisgis`, 16 GB / 294 tables / 11 schemas.
  **Forensic database:** `postgis-forensic`, host **5432**, role `allis`,
  `msallisgis`, 17 GB / 314 tables / 9 schemas — forensic auditing only.
  GBIM entity store: ChromaDB `gbim_worldview_entities` (5,416,521 vectors, L2 distance).
  DNS: `msallis-db:5432` resolves from all connected containers (production).
  PostgreSQL 16.4 confirmed.
  **`mvw_gbim_landowner_spatial` — ✅ CLOSED: 38,979 rows, `msallis-db`, April 23, 2026.**
- GIS-RAG v0.4.0 (port 8004) — **204 WV GIS dataset services** auto-discovered, 0 import
  failures, Redis catalogue live (`gis:catalogue` = 204 entries). Live PostGIS features
  flowing: 7,357 WV bridges confirmed. Spatial query routing: `is_spatial_query()` →
  `/query/spatial` → GIS context injected into LLM prompt. Non-spatial queries → normal
  RAG path.
- **MountainShares service inventory (April 23, 2026):**
  - `allis-ms-token-service` ✅ healthy, port **8088**
  - `allis-community-stake-registry` ✅ port **8084** — community stake registry;
    tracks on-chain/off-chain stake assignments for WV community governance participants
  - `ms_mountainshares_analytics`: `{"status":"healthy","total_records":0}` — tables
    exist, schema complete, DB connected, ready to receive real participation data.
    `ms_participation`, `ms_user_profile` confirmed connected.
  - MountainShares coordinator healthy on qualia-net (172.18.0.50); DNS resolves
    `msallis-db` → 172.18.0.x (production).
- `GISDatasetService` dispatcher: 204 services registered, 0 failures, Redis
  `gis:catalogue` 204 entries, `gis:service_count` 204.

**WOAH layer (Phase 2.5):**

- Called when the system needs to decide:
  - Whether a new memory should be treated as structural or episodic
  - How important a given narrative is to the user's autobiographical profile
  - How to weight this memory in downstream decisions about storage and promotion into
    long-term containers
- The WOA-inspired population module updates its policy with each evaluation
- `nbb_pituitary_gland` (port 8108) modulates WOAH weight thresholds upstream —
  pituitary state feeds into WOAH governance context

**Downstream layers:**

- The Fifth DGM (`allis-fifth-dgm`, port 4002) tracks how many inputs have been
  evaluated by WOAH, how many were accepted into subconscious or I-containers, and
  timestamps of the most recent WOAH evaluations
- Consciousness coordinators and bridges (including `allis-consciousness-bridge`,
  internal port 8020 — `{"8020/tcp":null}`, no host binding) record when WOAH was used
  as one of the services in an end-to-end pipeline
- WOAH's identity weights influence which memories are promoted, how they are indexed,
  and how strongly they shape future responses
- Identity-promoted items stored to ChromaDB use `all-minilm:latest` (384-dim) — the
  mandatory embedding model for all 48 active collections. `nomic-embed-text` (768-dim)
  is incompatible with existing collections.
- `nbb_mother_carrie_protocols` (port 8107, 5 protocols, `MOTHER_CARRIE_KIDD` anchor)
  receives warmth signals downstream of WOAH identity weighting

### Collection Distance Metric Reference (April 23, 2026)

| Collection | Distance Metric | Notes |
|:--|:--|:--|
| `msallis_docs` | L2 | 7,465 items ✅ |
| `ms_allis_memory` | **cosine** | Live name in `msallis-rebuild` stack; legacy public-facing name was `ms_allis_memory` — do not use in service code |
| `autonomous_learner` | L2 | 21,181 records ✅ |
| `gbim_worldview_entities` | L2 | 5,416,521 vectors |
| `fifth_dgm_subconscious` | L2 | Active subconscious write target |

### Service Integration: allis-woah vs nbb_woah_algorithms

```text
nbb_pituitary_gland (127.0.0.1:8108)
│  [upstream governance — modulates WOAH thresholds]
│
allis-consciousness-bridge (internal 8020/tcp, no host binding)
│
├──→ allis-woah (qualia-net internal, port 7012 — NO HOST PORT, {} binding intentional)
│     GET /  → health check → 200 {'status': 'ok', 'service': 'allis-woah'}
│     POST /process → stub response:
│       {status: ok,
│        content: "WOAH stub reasoning complete",
│        confidence: 0.8}
│     [OI-10B CLOSED — DNS-only, no host port by design]
│
└──→ nbb_woah_algorithms (127.0.0.1:8104 host / 8010 container)
      POST /process → full semantic identity scoring
                    + WOA population dynamics
                    → hierarchical_weight: 0.8
                    → identity_type: "structural"
                    → weight_category: "strong_identity"
                    [OI-10F CLOSED — population seeded, 1 vector confirmed]
      GET /woah_population_debug → population state
      GET /health → liveness + version
```

**Calling `allis-woah` from other containers (qualia-net DNS — the only correct
method):**

```python
import httpx

# Health check — use Docker DNS name, not host port
resp = httpx.get("http://allis-woah:7012/")
# {"status": "ok", "service": "allis-woah", "port": 7012}

# Process call
resp = httpx.post(
    "http://allis-woah:7012/process",
    json={"content": "community resource query", "context": {}}
)
# {"status": "ok", "content": "WOAH stub reasoning complete", "confidence": 0.8}
```

> **⚠️ Do NOT use a host port to call `allis-woah`.** There is no host port binding.
> Any code attempting `http://127.0.0.1:7012` or `http://localhost:7012` from inside a
> container will fail. The only valid address is `http://allis-woah:7012` from any
> container on `qualia-net`.

**Calling `nbb_woah_algorithms` from host (full scoring):**

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

**Full scoring response schema:**

```json
{
  "content": "MountainShares cooperative economic development in Fayette County",
  "metadata": {"source": "governance", "county": "Fayette"},
  "hierarchical_weight": 0.87,
  "self_relevance": 0.91,
  "temporal_importance": 0.78,
  "novelty": 0.65,
  "stability": 0.82,
  "composite_weight": 0.83,
  "identity_type": "structural",
  "weight_category": "strong_identity"
}
```

**Any Ms. Allis service can query the GIS catalogue via Redis for spatial context
injection:**

```python
import redis
r = redis.Redis(host='allis-redis', port=6379, decode_responses=True)

# All 204 WV GIS tables instantly available to any service
catalogue = r.hgetall('gis:catalogue')
# → {'bridges': 'gis_bridges', '911centers_wvdem_032819_utm83': 'gis_911centers_...', ...}

# Check service count
count = r.get('gis:service_count')  # → "204"
```

---

## Confirmed Operational State — ★ Updated April 23, 2026

| Check | Result |
|:--|:--|
| `allis-woah` container status | ✅ RUNNING |
| `allis-woah` port binding | ✅ `{}` — **intentional, correct** — qualia-net internal DNS only (OI-10B CLOSED) |
| DNS from `allis-consciousness-bridge` → `allis-woah` | ✅ 200 `{'status': 'ok', 'service': 'allis-woah'}` |
| Deployment method | Volume bind mount `./woah_stub.py:/woah_stub.py` — NOT inline command |
| Network: qualia-net membership | ✅ Confirmed |
| `GET /` health | ✅ 200 OK |
| `POST /process` stub response | ✅ `{status: ok, content: "WOAH stub reasoning complete", confidence: 0.8}` |
| `nbb_woah_algorithms` (port 8104) | ✅ RUNNING — full FastAPI scoring service |
| WOAH population seeded | ✅ `hierarchical_weight: 0.8, identity_type: "structural", weight_category: "strong_identity"` — 1 vector confirmed non-empty (OI-10F CLOSED) |
| Fifth DGM WOAH evaluation cycles | ✅ Recording successful WOAH evaluations |
| `allis-consciousness-bridge` ChromaDB v2 | ✅ `/api/v2/heartbeat` → 200 |
| All ports bound to `127.0.0.1` | ✅ Confirmed April 23, 2026 |
| `0.0.0.0` exposures remaining | ✅ Zero |
| `_auth()` on sensitive routes | ✅ Confirmed on all 4 routes |
| Total containers Up (working run) | ✅ **100 (April 23, 2026)** |
| Total containers Up (thesis-verified) | ✅ **112/112 (April 16, 2026)** — zero Restarting, zero Exited |
| Container count change (April 16) | 109 → 112: 3 MountainShares from compose override (OI-10A CLOSED) |
| Orphan containers (5 older) | ✅ All `127.0.0.1`-bound; `allis-redis-local` + `allis-pia-status` confirmed required |
| ChromaDB v2 collections | ✅ **48 collections, ~6,740,611 vectors** — `allis-chroma` host port 8002, v2 API |
| `msallis_docs` count | ✅ **7,465 items** |
| `ms_allis_memory` distance metric | ✅ **cosine** (live name; legacy public name `ms_allis_memory` — see collection table) |
| `autonomous_learner` count | ✅ **21,181 records** (L2, April 23, 2026) |
| Production DB (`msallis-db`) | ✅ host 5433 / container 5432 — `msallisgis` 16 GB / 294 tables / 11 schemas |
| Forensic DB (`postgis-forensic`) | ✅ host 5432 — `msallisgis` 17 GB / 314 tables / 9 schemas — forensic only |
| `mvw_gbim_landowner_spatial` | ✅ **CLOSED: 38,979 rows, `msallis-db`, April 23, 2026** |
| PostgreSQL version | ✅ 16.4 (version: 160004) |
| `ms_mountainshares_analytics` | ✅ `{"status":"healthy","total_records":0}` — correct, tables ready |
| `ms_participation` + `ms_user_profile` | ✅ Connected |
| `allis-ms-token-service` | ✅ Healthy, port **8088** |
| `allis-community-stake-registry` | ✅ port **8084** — community stake registry added April 23, 2026 |
| MountainShares coordinator | ✅ Healthy on qualia-net |
| GISDatasetService dispatcher | ✅ 204 services registered, 0 failures |
| Redis `gis:catalogue` | ✅ 204 entries |
| Redis `gis:service_count` | ✅ 204 |
| GIS-RAG v0.4.0 (port 8004) | ✅ Running; 7,357 WV bridges live; spatial query routing active |
| Spatial query routing | ✅ `is_spatial_query()` → `/query/spatial` → GIS context injected |
| Non-spatial query routing | ✅ Normal RAG path — community resources path confirmed |
| `allis-hilbert-state` embed | ✅ dim=384 len=384 returning correctly |
| `allis-rag-server` | ✅ `/query` returning 200 OK |
| LM Synthesizer output | ✅ 255–637 chars generated successfully |
| All 3 Chroma collections (core) | ✅ `ms_allis_memory`, `local_resources`, `conversation_history` confirmed |
| Inner compose file | ✅ 86 containers, 1,799 lines |
| GPU pipeline end-to-end | ✅ 93.98s / real 1m34s (within 99–115s spec) |
| Consensus score | ✅ 0.95 — high agreement across models |
| Truth score / verdict | ✅ 1.0 / pass — RAG grounding working |
| RAG results (Fayette County) | ✅ 3 records returned from Chroma |
| Fast path (27 services, no LLM proxies) | ✅ 9–14 seconds clean |
| Full path (57 services, all 22 proxies) | ✅ 60–90 seconds, completes, valid responses |
| `fast_brain` / `brain` split | ✅ Implemented and running — not future work |

**DNS resolution note (historical — OI-10B CLOSED):** The DNS failure from
`allis-consciousness-bridge` to `allis-woah` was previously reported as a potential
network misconfiguration. Confirmed **false diagnosis** — the failure was caused entirely
by `allis-woah` exiting at startup (exit code 1). Docker's embedded DNS cannot resolve a
container that is not running. No changes to `qualia-net` topology, DNS configuration, or
bridge network settings were needed or made. `{}` port bindings on `allis-woah` are
correct and intentional.

---

## Relationship to Classical WOA and Limitations

The relationship between WOAH and classical WOA is honest but partial:

**Conceptual borrowing:**

- Maintaining a **population** of candidates (here, weight vectors)
- Moving candidates toward a current best vector
- Using **encircling** and **spiral**-style updates to balance exploitation with limited
  exploration

**Implementation reality:**

- `allis-woah` (qualia-net internal port 7012, **no host port** — OI-10B): stdlib
  `http.server` stub — provides health and stub `/process` response; no scoring logic
- `nbb_woah_algorithms` (port 8104): full FastAPI service with heuristic semantic identity
  scoring and WOA-inspired population dynamics; population seeded and confirmed non-empty
  (OI-10F)
- The semantic identity scoring is **heuristic and rule-based**, not learned
- The population updates apply WOA-style formulas to a small, in-memory population,
  without claims of formal convergence or optimality
- The population is primarily used as an **instrument** for understanding how the system
  is weighting identity, not as the sole driver of routing decisions

This thesis presents WOAH as a **WOA-inspired orchestration pattern and identity-weighting
instrument**, not as a mathematically complete, fully validated optimization algorithm.

---

## WOAH as a Computational Instrument for Place-Accountable Intelligence

From a Polymathmatic Geography perspective, WOAH functions as a **computational
instrument** that connects algorithmic behavior to specific places and communities:

- By privileging Appalachian keyphrases and MountainShares themes in its semantic
  identity function, WOAH encodes a **place-specific prior** about what counts as core
  identity work.
- By decomposing identity into axes like `self_relevance`, `temporal_importance`, and
  `stability`, it offers a vocabulary for **geographic narrative structure** — which
  memories persist, which are fleeting, and how they are tied to particular counties or
  projects.
- By maintaining a population of weight vectors and exposing it via
  `/woah_population_debug`, it makes **power accountable to place**: researchers can see
  whether the optimization dynamics are drifting toward or away from the values and
  geographies the system claims to serve.
- By weighting items ingested into ChromaDB v2 collections (all using `all-minilm:latest`
  384-dim — ★ **48 collections, ~6,740,611 vectors** — April 23, 2026), WOAH directly
  shapes which Appalachian narratives persist in the long-term semantic memory of
  `autonomous_learner` (21,181 items, L2, April 23, 2026) and `governance_rag`
  (643 chunks including the US Constitution).
- By feeding identity weights downstream into the `nbb_pituitary_gland` (port 8108)
  feedback loop — via `judge_to_pituitary_bridge.py` verdicts and WOAH process scores —
  the system implements a closed-loop, place-grounded governance mechanism.
- The **204 GIS dataset services** auto-discovered by `GISDatasetService` and published
  to the Redis catalogue (`gis:catalogue`) mean every WOAH-weighted identity evaluation
  can now be enriched with live PostGIS spatial context (7,357 WV bridges; 993 ZCTA
  centroids; 1,115,588 address points). A narrative about "bridges near Oak Hill" or
  "911 centers in Fayette County" carries not just semantic weight but actual geographic
  geometry.
- The `fast_brain` / `brain` architecture split (9 sub-2GB models at <20s vs full 21-LLM
  fabric at 60–90s) means WOAH's identity weights can route low-stakes queries through
  the fast path and high-stakes governance queries through the full ensemble —
  **optimization pressure flows to where it matters geographically**.
- `allis-community-stake-registry` (port **8084**) complements this by tracking
  community stake assignments — making MountainShares governance participation a
  first-class signal that flows into WOAH identity weighting alongside spatial and
  narrative cues.

WOAH belongs in the **Computational Instrument** tier:

- It is not just a low-level library, but a first-class service whose weights shape the
  flow of information and influence
- It is explicitly designed to be **inspectable and tunable**, so that West Virginia
  communities and collaborators can see and adjust how their stories are being weighted
- It demonstrates how WOA-style ideas can be repurposed from pure numeric optimization
  into **place-grounded orchestration of many minds**, aligned with Quantarithmia's
  justice-oriented instruments

> **Status — ★ April 23, 2026:** Both WOAH services are RUNNING. `allis-woah` is
> confirmed operational on qualia-net using the stdlib stub deployed via volume bind
> mount — `{}` port bindings are **correct and intentional** (OI-10B CLOSED).
> `nbb_woah_algorithms` (port 8104) implements the full heuristic semantic identity
> function, WOA-inspired population dynamics, and `/woah_population_debug` — population
> confirmed seeded with `hierarchical_weight: 0.8, identity_type: "structural",
> weight_category: "strong_identity"` (OI-10F CLOSED). **100 containers Up
> (April 23, 2026)**; thesis-verified **112/112 (April 16, 2026)**. Zero `0.0.0.0`
> exposures. ChromaDB v2: 48 collections, ~6,740,611 vectors (`allis-chroma` host
> port 8002, inter-service `http://allis-chroma:8000`, v2 API only). Production DB:
> `msallis-db` host 5433 / `msallisgis` 16 GB / 294 tables; forensic:
> `postgis-forensic` host 5432 / 17 GB / 314 tables. OI-E CLOSED:
> `mvw_gbim_landowner_spatial` — 38,979 rows, `msallis-db`, April 23, 2026. 204 GIS
> datasets live in Redis catalogue. MountainShares inventory: `allis-ms-token-service`
> (8088) ✅ + `allis-community-stake-registry` (8084) ✅ + coordinator + analytics
> healthy. `msallis_docs` 7,465 ✅. `ms_allis_memory` cosine ✅ (live name;
> legacy public name `ms_allis_memory`). `autonomous_learner` 21,181 ✅. GPU pipeline
> 93.98s / 1m34s. All OI items CLOSED. Chapter 10 CLOSED.

---

*Last updated: April 23, 2026 — Carrie Kidd (Mamma Kidd), Mount Hope WV*
*Namespace: `msallis-rebuild`. Container prefix: `allis-`.*

*★ March 27, 2026: Port reference table — security hardening note added; `woah_stub.py`
block — canonical-home sentence added; pipeline phase number added throughout — WOAH
operates at Phase 2.5; DNS false-diagnosis note confirmed.*

*★ March 28, 2026: Security remediation complete — 96/96 containers Up; `allis-i-containers`
(8015) + `allis-memory` (8056) → `127.0.0.1`; `_auth()` 4 routes confirmed;
`ALLIS_API_KEY` set. ChromaDB full audit: 40 collections, 6,675,442 vectors.
`spiritual_rag` deduped; `psychological_rag` restored. Full scoring response JSON schema
added. `autonomous_learner` + `governance_rag` collection references added.*

*★ April 16, 2026 — CHAPTER CLOSED: All 6 OI items closed. Container count 96 → 109 →
112 (3 MountainShares + 5 orphans confirmed safe). `allis-woah` `{}` binding confirmed
intentional — OI-10B CLOSED. WOAH population seeded — OI-10F CLOSED. DB forensics: both
DBs confirmed at correct ports; OI-10D, OI-10E CLOSED. MountainShares analytics healthy.
GISDatasetService dispatcher: 204 services. GIS-RAG v0.4.0: 7,357 WV bridges live.
`fast_brain`/`brain` split confirmed. GPU pipeline 93.98s / 1m34s; consensus 0.95; truth
score 1.0/pass. `nbb_pituitary_gland` (8108) and `nbb_mother_carrie_protocols` (8107)
integrated. Chapter 10 CLOSED.*

*★★ April 23, 2026: ``msjarvis-rebuild` narrative name applied; `msjarvis` count confirmed 7,465 ✅; 
`ms_jarvis_memory` corrected to cosine metric with live-vs-public name prose note added; `jarvis-ms-token-service`
name applied (sed-pass corrected); `jarvis-community-stake-registry` (port 8084) added to
MountainShares inventory throughout; `autonomous_learner` confirmed 21,181 ✅;
OI-E CLOSED: `mvw_gbim_landowner_spatial` 38,979 rows, `msjarvis-db`, April 23, 2026;
two-container database architecture (`msjarvis-db` host 5433 / `postgis-forensic` host
5432) applied; `jarvis-chroma` inter-service URL `http://jarvis-chroma:8000` applied;
container counts date-stamped (100 Up April 23, 2026; 112 thesis-verified April 16,
2026).*
