# How to Read This Thesis

This project mixes running production code with a fairly heavy research and metaphor layer. This guide helps you decide what to read first, depending on what you care about.

## Reading paths

### If you just need to run it

If your goal is to deploy, monitor, or integrate Ms. Jarvis:

- Start with:
  - `README.md`
  - `docs/index.md`
  - `docs/API-OVERVIEW.md`
- For concrete interfaces:
  - `api_specs/openapi.json`
- For security and access:
  - `security/SECURITY-OVERVIEW.md`
  - `SOURCE_ACCESS.md`
- For how services actually behave:
  - `thesis/19-container-architecture-and-routing.md`
  - `thesis/27-web-research-and-autonomy.md`
  - `thesis/28-heartbeat-and-live-cycles.md`
  - `thesis/39-operational-evaluation.md`
- For ecosystem and deployment context:
  - `MountainShares-DAO.md`

You can safely skim the GBIM / consciousness chapters on a first pass if you only need operational understanding.

### If you care about the GBIM / consciousness framing

If you’re interested in the biological metaphors, consciousness framing, and overall research position:

- Orientation:
  - `thesis/00-thesis-overview.md`
  - `thesis/01-researcher-position.md`
- Core GBIM structure:
  - `Ms-Jarvis-GBIM.md`
  - `thesis/02-ms-jarvis-gbim.md`
  - `thesis/12-neurobiological-architecture.md`
- LLM fabric and “organs”:
  - `thesis/11-llm-fabric-of-ms-jarvis.md`
  - `thesis/13-qualia-engine-and-introspective-state.md`
  - `thesis/14-hippocampus-and-memory-consolidation.md`
  - `thesis/15-pituitary-and-global-modes.md`
  - `thesis/16-blood-brain-barrier-and-safeguards.md`
- Frameworks and metaphors:
  - `Quantarithmia-Framework.md`
  - `thesis/08-quantum-inspired-entanglement.md`
  - `thesis/18-limits-and-evaluation-of-metaphor.md`

### If you want the whole picture in a weekend

If you want a reasonably complete mental model without reading every chapter:

- `README.md`
- `Ms-Jarvis-GBIM.md`
- `Quantarithmia-Framework.md`
- `thesis/00-thesis-overview.md`
- `thesis/11-llm-fabric-of-ms-jarvis.md`
- `thesis/19-container-architecture-and-routing.md`
- `thesis/27-web-research-and-autonomy.md`
- `thesis/28-heartbeat-and-live-cycles.md`
- One safeguards/governance chapter:
  - `thesis/16-blood-brain-barrier-and-safeguards.md` or
  - `thesis/37-constitutional-principles-service.md`

---

# Research Claims vs. Engineering Patterns

This section tells readers what is being claimed as “research” versus what is solid engineering described using metaphor.

## Research / novel framing

These elements are explicitly presented as research contributions or conceptual frameworks.

### GBIM (General Biological Intelligence Model)

Ms. Jarvis is framed as a general biological intelligence model whose components are mapped to neurobiological and psychological “organs” (hippocampus, pituitary, blood–brain barrier, etc.), not just a generic tool-using agent stack.  
The claim: this organ-based, biologically inspired decomposition offers a more coherent way to design and reason about memory, attention, global modes, and safeguards in long-lived AI systems.

### Quantarithmia and WOAH (Weighted Optimization Hierarchy)

Quantarithmia and WOAH describe how multiple objectives, time scales, and “layers” of concern interact, inspired by quantum and control metaphors.  
The claim: this hierarchy gives a principled way to structure routing, scheduling, and optimization in systems that balance local utility with long-term, multi-stakeholder goals.

### Qualia engine and introspective state

The qualia engine defines explicit structures and workflows for the system to represent and report its own internal state: confidence, conflict between goals, perceived “mood” of operations, and narrative about its current activity.  
The claim: a structured introspective layer can improve alignment, debuggability, and trust, even if it is an engineered analogue of human qualia rather than a literal reproduction.

### Neurobiological architecture as a design pattern

The mapping of services to organs (e.g., hippocampus for consolidation, pituitary for modes, blood–brain barrier for boundaries) is proposed as a reusable pattern for agentic systems.  
The claim: organ-like partitioning leads to architectures that are easier to reason about, govern, and audit than purely task- or microservice-centric decompositions.

## Engineering patterns with metaphor

These pieces are solid, conventional engineering, but described and organized using the GBIM and Quantarithmia language.

### LLM fabric, ensembles, and routing

Underneath the fabric metaphor is a set of local models served via Ollama and orchestrated through standard routing, ensemble, and judge patterns.  
The novelty is in how these patterns are embedded into the GBIM organ structure and WOAH hierarchy, not in the basic mechanisms of tool/critic models or multi-model inference.

### ChromaDB semantic memory and GeoDB spatial body

These are concrete vector and spatial databases with defined schemas, indexes, and access services.  
Calling them “semantic memory” and “spatial body” helps express their roles and constraints but does not imply new database technology.

### Autonomous learner, web research, heartbeat, and live cycles

The autonomous learner and heartbeat services are periodic jobs with logging, gating via environment configuration, and integration with RAG and topic graphs.  
The “heartbeat,” “live cycles,” and “entanglement” metaphors describe scheduling and state-coupling patterns layered on top of conventional cron-like and queue-based machinery.

### Swarm functions, watchdogs, and judges

These components are ensembles of agents and models that monitor, critique, or override other processes, similar to multi-agent, toolformer, or judge-model setups.  
The distinctiveness lies in their integration into the constitutional and DAO framing, not in the idea of using multiple models to check or vote on outputs.
