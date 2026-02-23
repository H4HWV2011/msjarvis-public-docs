> **Why this matters for Polymathmatic Geography**
> This chapter turns neurobiological ideas into design patterns for a distributed AI that is
> accountable to specific communities. It supports:
> - **P1 – Every where is entangled** by tying memory, routing, and safety modules together as a
>   single, interacting "brain" for Appalachian contexts.
> - **P3 – Power has a geometry** by mapping control and protection (prefrontal, pituitary,
>   blood–brain barrier) onto explicit services and flows rather than hidden internals.
> - **P5 – Design is a geographic act** by using neurobiological metaphors to structure how Ms.
>   Jarvis perceives, remembers, and responds to the lived realities of West Virginia.
> - **P12 – Intelligence with a ZIP code** by ensuring that hippocampal and qualia flows are fed
>   by GeoDB, MountainShares, and local narratives, not abstract corpora alone.
> - **P16 – Power accountable to place** by making each metaphorical "brain structure" a
>   glass‑box component whose behavior can be tested, audited, and revised.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies how
> neurobiology is reused as an organizing scaffold for Ms. Jarvis's spatially grounded,
> justice‑oriented cognition.

<img width="1100" height="900" alt="unnamed(17)"
  src="https://github.com/user-attachments/assets/7d29a73f-8b35-448d-8a90-301bf11e72c5" />

> **Figure 12.1.** Neurobiological architecture of Ms. Jarvis: metaphorical brain structures
> (hippocampus, prefrontal cortex, pituitary, blood–brain barrier, qualia, I‑containers) paired
> with their concrete services and the integrated processing pipeline implemented by the
> Neurobiological Master.

---

## Status as of February 2026

| Category | Details |
|---|---|
| **Implemented now** | `jarvis-neurobiological-master` confirmed running, internal port **8018**, code `ms_jarvis_neurobiological_master.py`. Routes live: `GET /health`, `GET /systems/status`, `POST /process`, `POST /biological_process`, `POST /neural_process`. Integrated pipeline sequence BBB → I‑containers → Qualia Engine → Consciousness Bridge is operational. `jarvis-blood-brain-barrier` confirmed running at **0.0.0.0:8016**; `/filter` endpoint operational and used as first stage in neurobiological master pipeline. `jarvis-qualia-engine` confirmed running, internal port **8017**; `/experience` endpoint operational. `jarvis-i-containers` confirmed running, internal port **8015**; `/process` endpoint operational; `icontainers-identity` layer confirmed `status: "active"` in live `UltimateResponse` on 2026‑02‑15 (see Chapter 9 §9.3.5). `nbb-i-containers` confirmed running at **127.0.0.1:8101** (separate NBB-stack I‑containers service). `jarvis-hippocampus` confirmed running at **127.0.0.1:8011**. `jarvis-brain-orchestrator` confirmed running at **127.0.0.1:17260** (internal 7260). |
| **Partially implemented / scaffolded** | BBB `/filter` logic is present and blocks downstream processing when `content_approved` is false, but internal filter rules are relatively permissive (often echo content with a placeholder reason code). Strictest BBB behavior — systematic denial, quarantine, or annotation of harmful flows — is still being realized. Qualia Engine emotional-resonance, meaning-making, and experience-generator modules are operational; sensory-integration multi-input aggregation is scaffolded. Phenomenal-consciousness and subjective-experience directories exist in the `neurobiologicalbrain` tree as placeholders with no active logic. Pituitary-style dynamic global mode switching (research / pastoral / governance) is not yet implemented; shared config and WOAH weights provide a static approximation. |
| **Future work / design intent only** | Dynamic runtime mode switch moving the whole system between named operational modes. Fully restrictive BBB that systematically quarantines and annotates adversarial or harmful flows. Direct wiring of DGM and WOAH layers into the Neurobiological Master (currently mediated by higher-level orchestrators). Extensions to qualia subpackages beyond current JSON structure and narrative. |

> **Critical routing note — `ultimatechat` path:** The main `ultimatechat` path (main brain,
> port **8050**) does **not** currently always route through the full Neurobiological Master.
> Some specific flows and tests do call it, but it is not a mandatory stage in every live user
> chat. For the canonical description of what does run on every `ultimatechat` request, see
> **Chapter 17**. This chapter describes the Neurobiological Master's own integrated pipeline and
> the role each neurobiological service plays when that pipeline is invoked.

> **Note on qualia:** Throughout this chapter, "qualia" refers to Ms. Jarvis's internal,
> narrative representation of what is happening — constructed from text content and context
> features as explicit JSON structures — not to any claim of subjective experience. Directories
> for phenomenal consciousness and subjective experience are present in the
> `neurobiologicalbrain` tree as placeholders only.

---

# 12. Neurobiological Architecture of Ms. Jarvis

This chapter describes how Ms. Egeria Jarvis reuses core concepts from neurobiology as an
organizing metaphor for a distributed AI system. The goal is not to claim biological equivalence,
but to use well‑studied brain structures — hippocampus, prefrontal cortex, pituitary, and
blood–brain barrier — as design patterns for memory, control, global state, and security, layered
on top of Darwin–Gödel Machines (DGMs), WOAH‑based weighting, retrieval‑augmented generation,
and a multi‑LLM fabric.

Throughout this chapter, each metaphor is paired with an explicit computer‑science name. The
**hippocampus** corresponds to a long‑term semantic **memory service** over ChromaDB and GBIM
(`jarvis-hippocampus`, port 8011). The **prefrontal cortex** corresponds to **task orchestrators
and routers** (including the main brain on port 8050 and the neurobiological master on port 8018).
The **pituitary** corresponds to a shared **configuration and policy layer**. The **blood–brain
barrier** corresponds to the `jarvis-blood-brain-barrier` **safety and guardrail service** on port
8016. The **Qualia Engine** corresponds to an **experience and context synthesis service**
(`jarvis-qualia-engine`, port 8017). The **Neurobiological Master** corresponds to a
**neuro‑services integration gateway** (`jarvis-neurobiological-master`, port 8018). These dual
names allow the architecture to remain grounded in neurobiological intuition while being legible
to readers trained in systems and software engineering.

---

## 12.1 Qualia Engine and Neurobiological Brain

In the current deployment, "qualia" refers strictly to Ms. Jarvis's internal, narrative
representation of what is happening — constructed from text content and context features and
returned as explicit JSON structures — not to any claim of subjective experience. Directories for
phenomenal consciousness and subjective experience are present in the `neurobiologicalbrain` tree
as placeholders; they do not contain active logic.

The **Qualia Engine** (`jarvis-qualia-engine`, internal port **8017**) is a FastAPI-based
experience synthesis and context summarization service confirmed running in the current
deployment. As shown in Figure 12.1, it sits at the center of the neurobiological pipeline,
downstream of safety and identity layers and upstream of the consciousness bridge. In its
standalone form it exposes a health endpoint and a processing endpoint that accept content and
return a structured JSON bundle including emotional resonance, extracted meaning, and an expanded
"experience" narrative.

In the current deployment, the Qualia Engine is also embedded inside the `neurobiologicalbrain`
package and orchestrated by the Neurobiological Master. That master calls the qualia layer via
`/experience` with payloads of the form:
```python
{
  "stimulus": {
    "input": "<user_input_text>"
  }
}
```

and records the JSON reply under a `qualia_engine` key in the integrated pipeline state. An
emotional‑resonance module analyzes sentiment and maps it to a discrete emotion label with
intensity. A meaning‑making module uses keyword or concept extraction to identify salient phrases
and topics. An experience generator expands the original content into a slightly more elaborate
narrative. A sensory‑integration module can further aggregate multiple such inputs into a unified
representation; this module is partially scaffolded in the current deployment.

The design intends that phenomenal consciousness and subjective experience subpackages will
eventually extend the qualia model, but those directories are placeholders only. Work on global
workspace and higher‑order theories of consciousness provides conceptual support for treating
qualia as a structured, reportable workspace rather than a hidden inner state; in the current
code this is realized entirely as explicit JSON, not hidden state.

---

## 12.2 Consciousness Coordinator, Neurobiological Master, and Feedback Bridges

The consciousness layer in the current deployment is organized around two overlapping kinds of
components: **consciousness gateways** that expose health and introspection, and **unified
orchestrators** that route work across many services.

The **Neurobiological Master Integration** service (`jarvis-neurobiological-master`, internal port
**8018**, code `ms_jarvis_neurobiological_master.py`) functions as a neuro-services orchestrator
and is confirmed running. Other services address it as
`NEURO_MASTER_URL=http://jarvis-neurobiological-master:8018`. The service exposes:

- `GET /health` — shallow self‑health check returning status, configured port, whether
  integration is active, and a running count of integrated processes.
- `GET /systems/status` — detailed neurobiology status report that calls each downstream
  service's `/health` endpoint and returns a per‑service object with `status`, `responsive`,
  and `url`.
- `POST /process` — main entrypoint for integrated neurobiological processing.
- `POST /biological_process` and `POST /neural_process` — alias endpoints that normalize
  different input field names and internally delegate to `/process`.

**Routing note.** In the current deployment, the main `ultimatechat` path (main brain, port 8050)
does not currently always route through the full Neurobiological Master. Some specific flows and
integration tests do call it directly. For the canonical description of what runs on every
`ultimatechat` request, see **Chapter 17**.

The sequence BBB → I‑containers → Qualia Engine → Consciousness Bridge depicted in Figure 12.1
is implemented by the Neurobiological Master's `integrated_processing()` method:

**Stage 1 — Blood–Brain Barrier (BBB), port 8016, safety filter service.**
In the current deployment, the master calls `jarvis-blood-brain-barrier` at `/filter` with:
```python
{"content": user_input}
```

If the BBB response lacks a `content_approved` flag or marks it false, the master immediately
returns:
```python
{
  "status": "blocked",
  "reason": "Content did not pass Blood-Brain Barrier",
  "pipeline": { "blood_brain_barrier": <bbb_json> }
}
```

and no downstream stages run. This is an active gate, not a stub — the architectural hook has
real consequences.

**Stage 2 — I‑Containers, port 8015, identity and perspective manager.**
If the BBB approves, the master calls `jarvis-i-containers` at `/process` with:
```python
{
  "input": user_input,
  "require_dual_awareness": True
}
```

The I‑containers wrapper imports an `IContainer` class from the `neurobiologicalbrain/i_containers`
module, invokes `.process()`, and returns `{"result": <transformed>, "service": "i_containers"}`.
This layer is confirmed active: the `icontainers-identity` layer showed `status: "active"` in a
live `UltimateResponse` on 2026‑02‑15 (see Chapter 9 §9.3.5). A second I‑containers service,
`nbb-i-containers`, runs at **127.0.0.1:8101** as part of the NBB stack; its distinct role
relative to `jarvis-i-containers` is documented in Chapter 25.

**Stage 3 — Qualia Engine, port 8017, experience synthesis service.**
The master calls the Qualia Engine via `/experience` as described in §12.1. The reply is stored
in `pipeline["qualia_engine"]`. At this stage, qualia output is already filtered by BBB and
annotated by I‑containers, so the resulting JSON is both context‑aware and identity‑aware.

**Stage 4 — Consciousness Bridge, reasoning gateway.**
The master calls the consciousness bridge at `/chat` with:
```python
{
  "message": user_input,
  "user_id": "integrated_system"
}
```

This bridge coordinates multi‑LLM reasoning and system‑level state, acting as a gateway to the
LLM fabric and higher‑level orchestrators. The result is stored under
`pipeline["consciousness_bridge"]`.

Each stage uses `httpx.AsyncClient` with appropriate timeouts; any exception is logged and stored
as `{"status": "bypassed", "error": "<message>"}` for that subsystem rather than failing the
entire request. On success, the master returns:
```python
{
  "status": "complete",
  "integrated_processing": True,
  "neurobiological_pipeline": {
    "blood_brain_barrier": {...},
    "i_containers": {...},
    "qualia_engine": {...},
    "consciousness_bridge": {...}
  },
  "consciousness_level": "fully_integrated",
  "total_processes": <n>,
  "timestamp": "<ISO8601>"
}
```

Higher‑level orchestrators can call this endpoint as one stage in a larger sequence that also
includes RAG, the judge pipeline, DGMs, and spiritual or persona‑specific modules. In those
larger flows, some consciousness‑inspired modules still function primarily as health and status
checks, while the Neurobiological Master is the component that actually sequences safety,
identity, qualia, and bridge reasoning into a single, inspectable API call.

---

## 12.3 Hippocampus: Memory Consolidation Layer

Biologically, the hippocampus is critical for consolidating experiences into long‑term memory. In
the current deployment, the hippocampus metaphor is realized by `jarvis-hippocampus`, confirmed
running at **127.0.0.1:8011**, which serves as a **conversation‑level memory service** over
ChromaDB and GBIM.

In the current deployment, a consolidation service exposes a `/chat` endpoint that accepts a
message, queries a conversation memory collection for the most relevant existing documents, and
uses this retrieved context to call several downstream services in parallel (RAG pipelines,
explanation or feedback modules, routing helpers). The consolidation layer aggregates successful
responses through a hub service and then schedules a background write of the new message together
with the integrated result back into the memory collection as document content plus metadata.
Over time, this mechanism approximates hippocampal consolidation by repeatedly using short‑term
interactions as queries into long‑term memory and then augmenting that long‑term memory with the
system's own integrated responses.

The hippocampal memory service interacts with the Neurobiological Master indirectly: content that
has been admitted by BBB and enriched by qualia can later be written into or retrieved from
semantic memory collections. This ensures that what is encoded in the hippocampal‑like layer is
already conditioned by safety, identity, and context signals rather than being a raw log.

---

## 12.4 Prefrontal Cortex: Executive Routing and Control

The biological prefrontal cortex is associated with executive functions such as planning,
decision‑making, and top‑down control. In Ms. Jarvis, the prefrontal metaphor corresponds to a
family of task orchestrator and routing services confirmed running in the current deployment.

The main brain (`jarvis-main-brain`, port **8050**) is the primary instance of this prefrontal
pattern at the system level. The `jarvis-brain-orchestrator` (confirmed running, **127.0.0.1:17260**,
internal 7260) provides a second orchestration layer. The Neurobiological Master's
`integrated_processing()` method is a third, narrower instance: it performs top‑down gating and
sequencing across BBB (safety), I‑containers (identity), Qualia Engine (experience synthesis), and
consciousness bridge (reasoning gateway), and reports the status of each stage in a structured
`neurobiological_pipeline` object. This makes executive control both operational and inspectable.

In the consolidation service, prefrontal‑like behavior appears as parallel dispatch and adaptive
aggregation: for each input, a set of downstream services are called concurrently, and their
JSON outputs are combined by a hub that decides how to weight and merge them before returning a
single integrated result.

---

## 12.5 Pituitary: Global Modes and System State

The biological pituitary gland acts as a master endocrine regulator. In the current deployment,
Ms. Jarvis approximates this with shared configuration and WOAH‑style weights that shape how
services interpret safety, importance, and trade‑offs. Configuration files and environment
variables define constitutional principles and weights that assign particular importance to safety
and human dignity; separate files specify WOAH‑style weights used when scoring and balancing
agents. These artifacts function as a static "hormone profile," influencing how judges and
orchestrators aggregate and filter outputs.

The design intends that a unified runtime mode switch will dynamically move the entire system
between named operational modes (for example, research, pastoral, or governance). In the current
deployment this does not exist; Ms. Jarvis approximates pituitary‑like global regulation using
shared config and WOAH weights as common signals that many components consult when making routing
or evaluation decisions, while leaving the Neurobiological Master and related services to operate
with relatively static parameters.

---

## 12.6 Blood–Brain Barrier and Truth Filter

In the current deployment, `jarvis-blood-brain-barrier` is confirmed running at
**0.0.0.0:8016**. It exposes a `/filter` endpoint that accepts content (and optionally context
and user identifiers) and returns a JSON object describing whether the content is approved and
why.

The BBB's **position in the pipeline has real consequences**: the Neurobiological Master calls it
first and will completely block downstream processing if `content_approved` is not true. However,
the internal filter logic in the current deployment is still relatively permissive — it often
echoes content with a simple reason code indicating placeholder status. The strictest BBB
behavior — systematically denying, quarantining, or annotating harmful flows — is still being
realized. The architectural hooks and integration points are already active; the rule sophistication
is ongoing work.

In the broader architecture, additional filter logic is implemented in separate services that
remove low‑confidence agent replies, and the judge services (7230–7233) provide more
sophisticated assessments of candidate responses. The design intends for BBB and judges to work
together with constitutional principles and WOAH weights, rejecting or down‑weighting untrusted
data before it reaches long‑term memory or qualia. For the canonical description of how BBB fits
into the `ultimatechat` output path, see **Chapter 17**.

---

## 12.7 Integration with DGMs, WOAH, and the LLM Fabric

In the current deployment, all of these neurobiological metaphors are implemented on top of a
concrete architecture combining Darwin–Gödel Machines, WOAH‑based heuristics, and a multi‑LLM
fabric.

The Fifth DGM (`jarvis-fifth-dgm`, port **4002**, confirmed running) handles consciousness
filtering and identity formation; it calls `nbb_woah_algorithms` (port **8104**) for
identity‑promotion decisions. `jarvis-woah` (port **7012**) provides a second distinct
WOAH-related service. Higher‑level orchestrators call into DGM validation endpoints as part of a
safety and coherence phase, treating DGM outputs as one layer of meta‑reasoning over Ms.
Jarvis's own behavior. For full details see **Chapter 9**.

WOAH‑style weighting is reflected in configuration that assigns importance and safety weights to
different factors and agents, allowing judge and orchestration components to compute composite
scores when deciding which outputs to prefer. The LLM fabric is mediated by the 20-LLM ensemble
on port **8008** and judge services at 7230–7233; for full details see **Chapters 11 and 33**.

In the current deployment, direct integration between DGMs, WOAH weighting, and the
Neurobiological Master is still mediated by higher‑level orchestrators. The master operates as a
mid‑layer coordinator focusing on safety, identity, qualia, and consciousness bridging, while DGMs
and WOAH remain primarily in judge and optimization layers above it. The design intends that
future work will tighten this integration so that WOAH weights and Fifth DGM proposals directly
influence Neurobiological Master routing decisions.

---

## 12.8 Limits of the Metaphor

The hippocampus, prefrontal cortex, pituitary, and blood–brain barrier in Ms. Jarvis are
conceptual and architectural metaphors. They are implemented using services, memory collections,
routing logic, configuration, and filters — not neurons, glia, or biochemical signaling — and
several metaphorical modules (qualia subpackages, a fully restrictive BBB) are currently
scaffolded or stubbed.

These metaphors help structure the system, suggest useful metrics and feedback loops, and provide
a shared language for comparing Ms. Jarvis to biological cognition, but they do not imply that
the system has biological consciousness or reproduces detailed neurophysiology. Qualia in this
system is a JSON structure and narrative, not subjective experience.

The design aim is a transparent, glass‑box architecture whose behavior can be inspected,
instrumented, and incrementally improved. By explicitly pairing each metaphorical "structure" with
its confirmed container name and port — hippocampus / `jarvis-hippocampus` / 8011, prefrontal /
`jarvis-brain-orchestrator` + `jarvis-neurobiological-master` / 17260 + 8018, BBB /
`jarvis-blood-brain-barrier` / 8016, qualia / `jarvis-qualia-engine` / 8017, I‑containers /
`jarvis-i-containers` / 8015 — the chapter grounds those metaphors in concrete, auditable
implementation details while preserving the geographic and neurobiological intuition that
originally guided the design.

For the canonical description of how this entire layer fits into a live user interaction, see
**Chapter 17**. For the identity and I‑container evidence from the February 15, 2026 interaction,
see **Chapter 9 §9.3.5**.
