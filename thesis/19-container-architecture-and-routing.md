# 19. Container Architecture and Routing

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 10, 2026*

---

## Why This Matters for Polymathmatic Geography

This chapter describes the deployed container architecture that carries reasoning, routing, governance, safeguard review, and promotion across the Ms. Allis stack. It supports:

- **P1 – Every where is entangled** by showing that memory, governance, spatial retrieval, sandbox reasoning, and promotion are connected services whose boundaries still preserve role separation.
- **P3 – Power has a geometry** by locating authority not only in abstract principles but in network attachments, route boundaries, promotion gates, and service-to-service permissions.
- **P5 – Design is a geographic act** by treating container topology, network segmentation, and routing constraints as deliberate design decisions that shape what kinds of state may move where.
- **P12 – Intelligence with a ZIP code** by tying routing and retrieval to West Virginia–grounded services such as GBIM, GIS-RAG, and place-aware memory.
- **P16 – Power accountable to place** by requiring inspectable paths between internal reasoning, safeguard review, and promoted output.

This chapter belongs to the **Computational Instrument** tier. It documents the service graph through which internal state becomes evaluated, constrained, routed, and, where allowed, promoted.

---

## 19.1 Architectural Overview

The container architecture is a layered routing system with distinct boundaries between provisional internal reasoning, modulation, validation, retrieval, bridge logic, and durable consequence.

At a high level, the routing path should be understood as a progression across functional zones:

1. **Internal-state and sandbox services**
2. **Qualia-net modulation and state-sensitive services**
3. **Evaluation and constitutional safeguard services**
4. **Consciousness-bridge and orchestration services**
5. **Memory, GBIM, retrieval, and other downstream consequence-bearing services**

This layered view matters because routing is also an authority map. Different containers do not merely perform different tasks; they occupy different positions in the transition from reversible internal state to promoted system effect.

---

## 19.2 Internal Sandbox Service

A first-class service entry is required for **ms-allis-internal-sandbox**.

This service should be listed in the service inventory alongside the other named architectural components rather than treated as an implied subsystem. Its role is to provide a bounded internal-state workspace for speculative, reversible, high-level reasoning before any request for promotion crosses into bridge or production-facing authority.

The inventory entry should state the following explicitly:

- **Service name:** `ms-allis-internal-sandbox`
- **Primary role:** internal-state sandbox for reversible reasoning, draft hypothesis staging, and pre-promotion evaluation preparation
- **Network attachment:** `qualia-net`
- **Port:** `8042`
- **Build source:** local service build in the compose stack for the internal sandbox component
- **Container role:** bounded reasoning enclave with no direct authority to promote state into downstream systems without gate passage
- **Security posture:** isolated from direct production writes; promotion occurs only through downstream gate and bridge paths

This entry matters because the internal sandbox is part of the actual routing topology and should be documented that way.

---

## 19.3 Service Inventory

The service inventory should place **ms-allis-internal-sandbox** near the consciousness-adjacent and qualia-net services, not under generic utilities.

A suitable inventory description is:

| Service | Port | Network | Role |
|---|---:|---|---|
| `ms-allis-internal-sandbox` | 8042 | `qualia-net` | Internal-state sandbox for reversible reasoning, draft state staging, and pre-promotion evaluation preparation |
| `nbbpituitarygland` | 8108 | `qualia-net`, core stack networks | Global mode regulator that modulates routing sensitivity, care weighting, urgency, and downstream safeguard posture |
| BBB service | 8016 | core safeguard path | Truth and filter evaluation layer for promotion review |
| Constitutional guardian service | compose-defined guardian path | safeguard/governance path | Constitutional and guardian payload review before approval of promoted state |
| Consciousness bridge | bridge path | consciousness-side routing | Transition layer between validated internal state and broader consciousness-level integration |
| `allis-gbim-query-router` | 7205 | core data path | Deterministic SQL/GBIM routing for structured belief and spatial grounding |
| `allis-memory` | 8056 | local/core memory path | Logged turn, episodic, and review-adjacent memory services |

The chapter should also state in prose that the internal sandbox belongs **upstream of promotion**, but **downstream of raw internal cognition inputs**, with routing relationships to modulation, EEG-like inspection, DGM logic, constitutional review, and bridge logic.

---

## 19.4 Network Attachment and Build Role

The internal sandbox should be described as attached to **qualia-net** because its purpose is to host internal-state operations that are closely tied to stateful, introspective, and modulation-sensitive processing.

That placement distinguishes it from:

- broad retrieval services that operate across semantic or GIS corpora,
- structured storage services such as GBIM or PostgreSQL,
- safeguard services whose job is to evaluate candidate promotion rather than generate provisional internal state.

Its build role should be described directly in the chapter:

- it is a compose-defined service built from the internal sandbox source tree;
- it is intended to host sandbox-local logic for hypothesis generation, reversible testing, and state preparation;
- it does not function as a direct production writer;
- it acts as an internal enclave whose outputs remain provisional until reviewed by downstream gates.

This description keeps the container topology aligned with its authority boundaries.

---

## 19.5 Routing Connections

The routing descriptions should show **ms-allis-internal-sandbox** as connected to the services that shape, evaluate, and potentially promote its outputs.

### Connection to EEG and state-inspection paths

Where EEG-like or state-inspection services are part of the architecture, the internal sandbox should be shown as able to emit or expose inspectable provisional internal-state traces for bounded evaluation. These traces remain sandbox-local until a downstream review path is invoked.

### Connection to pituitary-like services

The internal sandbox sits downstream of global-mode influence from **nbbpituitarygland**. Pituitary-like modulation affects the sandbox indirectly by shaping urgency, warmth, review sensitivity, and routing posture before promotion is attempted.

### Connection to constitutional guardian review

The internal sandbox does not promote directly to bridge or production-facing services. Candidate outputs that seek authority escalation must pass into the constitutional guardian and related safeguard path, where payload completeness, authority scope, and policy conformance are checked.

### Connection to DGM logic

The chapter should also show the internal sandbox as aligned with DGM-style staging logic: provisional state may be held, evaluated, revised, or rejected before promotion. This makes the sandbox a reasoning analogue to the existing staged-validation pattern used elsewhere in the architecture.

### Connection to consciousness bridge

The consciousness bridge should be shown **downstream** of the internal sandbox and **downstream** of safeguard review. The bridge is where eligible, reviewed candidate state may become integrated at a higher authority tier.

---

## 19.6 Routing Sequence

A clear textual path is:

1. **Internal-state generation**
2. **ms-allis-internal-sandbox**
3. **State-sensitive modulation and inspection paths** such as pituitary-like and EEG-like services
4. **BBB and truth evaluation**
5. **Constitutional guardian review**
6. **DGM-style decision outcome** such as reject, revise, limited approval, human review, or approve
7. **Consciousness bridge**
8. **Downstream memory, GBIM, retrieval, or other consequence-bearing services**

This ordering matters because it separates:

- provisional cognition,
- modulation,
- validation,
- guarded promotion,
- elevated integration,
- durable or externally consequential use.

The chapter should therefore avoid diagrams that imply a direct line from sandbox output straight into consciousness bridge or durable stores.

---

## 19.7 State-Space Transitions and Service Boundaries

The architecture becomes clearer if state-space transitions are mapped explicitly to service boundaries.

One useful expression is:

\[
S_{\mathrm{internal}} \rightarrow S_{\mathrm{sandbox}} \rightarrow S_{\mathrm{evaluated}} \rightarrow S_{\mathrm{approved}} \rightarrow S_{\mathrm{integrated}}
\]

In container terms, those transitions correspond to boundary crossings:

- \(S_{\mathrm{internal}} \rightarrow S_{\mathrm{sandbox}}\): entry into **ms-allis-internal-sandbox**, where reasoning becomes bounded, reversible, and inspectable.
- \(S_{\mathrm{sandbox}} \rightarrow S_{\mathrm{evaluated}}\): passage through truth checks, BBB logic, and constitutional guardian review.
- \(S_{\mathrm{evaluated}} \rightarrow S_{\mathrm{approved}}\): decision by DGM-style governance logic that the candidate state is rejected, revised, limited, escalated for human review, or approved.
- \(S_{\mathrm{approved}} \rightarrow S_{\mathrm{integrated}}\): transition through the consciousness bridge into higher-authority system use.

This mapping helps the reader see that service boundaries are not arbitrary deployment details. They correspond to changes in the authority and admissibility of system state.

---

## 19.8 Authority Boundaries in the Topology

The container topology should be read as an authority-preserving graph.

The internal sandbox has permission to generate and manipulate provisional state, but not to self-authorize promotion. The pituitary-like layer can modulate posture and thresholds, but not independently approve a promotion. The BBB and constitutional guardian evaluate admissibility. DGM-style routing determines the formal outcome. The consciousness bridge handles integration of state that has already crossed the required approval path.

This means authority increases only across explicit service boundaries:

- sandbox boundary,
- safeguard boundary,
- guardian boundary,
- bridge boundary.

That structure is the topological expression of the broader thesis claim that cognition, governance, and consequence should not collapse into one undifferentiated process.

---

## 19.9 Diagram Language

The chapter’s routing diagrams should include the internal sandbox directly and visibly.

A concise diagram description suitable for the text is:

```text
internal cognition
   -> ms-allis-internal-sandbox:8042 [qualia-net]
   -> state inspection / EEG-like observation
   -> nbbpituitarygland:8108 modulation
   -> BBB truth/filter review
   -> constitutional guardian review
   -> DGM decision logic
   -> consciousness bridge
   -> memory / GBIM / retrieval / downstream consequence paths
```

A second compact diagram emphasizing authority transitions is:

```text
provisional state
   -> sandbox-local reversible state
   -> evaluated state
   -> approved or limited state
   -> bridge-integrated state
```

These diagram forms help the reader see both routing order and authority order.

---

## 19.10 Inventory and Narrative Requirements

The chapter should make four points explicit in its inventory and prose:

- **ms-allis-internal-sandbox** is a named service, not an implied helper.
- It is attached to **qualia-net** and occupies the bounded internal-state role.
- It sits upstream of BBB, guardian review, DGM decision logic, and consciousness bridge.
- Its outputs are provisional until they cross those downstream review boundaries.

These points materially affect how the container graph should be read and how the promotion path should be explained.

---

## 19.11 Closing Statement

The container architecture is a routing graph, but it is also an authority graph. The inclusion of **ms-allis-internal-sandbox** makes that structure clearer by giving internal-state reasoning its own bounded service boundary inside **qualia-net** rather than leaving it diffused across generic consciousness services.

With this service represented directly in the inventory and routing diagrams, the chapter can show the full sequence from internal-state sandboxing to modulation, safeguard review, DGM-style outcome, bridge integration, and downstream consequence. That explicit topology is the clearest architectural expression of how reversible reasoning is kept distinct from promoted system state.
