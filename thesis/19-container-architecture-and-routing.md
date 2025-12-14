# 19. Container Architecture and Routing

This chapter describes the high-level layout of the structures that receive activity from earlier layers and route it into deeper evaluation paths. The goal is to separate the flow of events into clear stages, so that each stage has a well-defined role in deciding what is ignored, what is kept for background consideration, and what becomes part of a more central store.

## 19.1 Position in the Overall System

The container layer sits above retrieval, optimization, and global control and below external interfaces and scheduling. Its main responsibilities are to:

- Accept events coming from many sources, including question-handling flows, scheduled jobs, and self-improving processes.
- Normalize these events into a common format that can be evaluated in a consistent way.
- Dispatch normalized items into successive evaluation stages, while obeying system-wide constraints.

Earlier parts of the work have described how information is retrieved, evaluated, and stored. This part focuses on how those elements are wrapped in container structures that manage their entry into higher-level evaluative paths.

## 19.2 Types of Incoming Events

The intake layer receives several broad categories of events:

- Direct interactions:
  - User queries and responses that have already passed through retrieval and constraint checks.
- Internal tasks:
  - Results from scheduled analyses, background maintenance jobs, and optimization routines.
- External signals:
  - Notifications or status changes from connected systems such as messaging platforms or data sources.
- Structural changes:
  - Updates to memory, beliefs, or spatial layers that may require special attention.

Each event is accompanied by metadata such as timestamps, role information, and identifiers, which the containers use to make routing decisions.

## 19.3 Normalization into Container Records

Before events are passed to deeper stages, they are normalized into container records with a common structure. A typical record includes:

- Core fields:
  - A unique identifier, timestamps, and origin.
- Context:
  - Active role or profile, relevant locations, and any tags describing the domain.
- Content summary:
  - Key text, numerical values, or structured data extracted from the event.
- Links:
  - References to memory items, graph entities, spatial features, or introspective entries.
- Control information:
  - Flags indicating initial assessments such as urgency, sensitivity, or resource cost.

This normalization step allows subsequent stages to apply uniform logic, regardless of where the event originated.

## 19.4 First-Level Routing Decisions

Once a record is normalized, the intake layer applies initial routing logic:

- Eligibility checks:
  - Confirm that the record is allowed to enter the container paths under current global settings.
- Priority assignment:
  - Assign a simple priority level that will influence ordering and resource allocation.
- Track assignment:
  - Decide whether the record should be sent to one or both of the parallel paths that follow.

At this stage, routing focuses on structural compatibility and basic policy, leaving more detailed judgments to later chapters.

## 19.5 Parallel Paths

The architecture uses two parallel paths that share the same structural pattern:

- One path emphasizes questions of meaning, care, and affect, and is used when events are framed in those terms.
- The other path emphasizes general analysis and technical reasoning, and is used for more conventional problem-solving tasks.

The intake layer decides, based on metadata and simple classifiers, whether a record is best handled by one path, the other, or both. Each path then applies its own evaluation criteria while maintaining the same overall sequence of stages.

## 19.6 Outputs of the Routing Layer

After routing, the main outputs are:

- Records marked for immediate evaluation in the next stage.
- Records held back or dropped according to policy.
- Logs and introspective entries describing which path was chosen and why.

These outputs ensure that downstream stages receive appropriately prepared inputs and that the choices made at the routing step can be examined later if needed.

## 19.7 Summary

The container architecture provides a structured way to receive, normalize, and direct events into deeper evaluative paths. It defines how diverse inputs enter the system’s evaluative core, setting the stage for later chapters that describe how these items are filtered, retained, and woven into longer-term structures.

---

## 19.8 Operational Container Topology (December 11, 2025)

This section summarizes one observed deployment topology, to ground the abstract container architecture in a concrete set of services. It should be read as an empirical snapshot rather than a permanent design.

### Core Orchestration Layer

| Container         | Port Mapping | Role                                                                 |
|-------------------|-------------:|----------------------------------------------------------------------|
| jarvis-main-brain | 8051→8050    | External API entry point; health-check sweep; service orchestration |

### Coordination Services (ULTIMATE Path)

| Container                  | Port Mapping | Role                                                |
|---------------------------|-------------:|-----------------------------------------------------|
| jarvis-blood-brain-barrier| 8016→8016    | Content filter; context cleaning; safety enforcement|
| jarvis-llm-bridge         | 18006→8006   | Multi-agent ensemble coordination; response synthesis|
| jarvis-web-research       | 18009→8009   | Context enhancement; external knowledge retrieval   |

These services implement the intake and early-routing behavior described above, turning raw requests into normalized, filtered records before deeper evaluation.

### Memory, Learning, and Optimization Services

| Container                    | Port Mapping | Role                              |
|-----------------------------|-------------:|-----------------------------------|
| jarvis-autonomous-learner   | 18053→8053   | Autonomous learning; self-improve |
| jarvis-i-containers         | 18115→8015   | Container orchestration           |
| jarvis-fifth-dgm            | 14002→4002   | Darwin–Gödel–style optimization   |
| jarvis-neurobiological-master| 18118→8018  | Neurobiological coordination      |

These components generate internal tasks and structural changes that enter the container layer as events, and they depend on consistent routing and normalization to feed their outputs back into memory and belief structures.

### Data Persistence and Semantics

| Container                 | Port Mapping | Role                                |
|--------------------------|-------------:|-------------------------------------|
| jarvis-chroma            | 8000→8000    | Primary semantic memory (ChromaDB)  |
| services-chroma-1        | 8010→8010    | Additional ChromaDB instance        |
| msjarvis-rebuild-chroma-1| 8002→8000    | Rebuild / development instance      |
| services-neo4j-1         | 7474, 7687   | GBIM graph database                 |
| services-mysql-1         | 3307→3306    | Relational data; user/audit records |

These stores provide the long-term structures that container records link to via IDs and metadata.

### External Access Points and LLM Backend

Only two ports are exposed to the host:

- **8051** – External API endpoint (`jarvis-main-brain`).  
- **11434** – Ollama LLM backend (local model serving).

Internally, a `jarvis-ollama` container on port `11434` hosts the local language models used by `llm_bridge`, ULTIMATE, and other services. All other services communicate over the Docker bridge network using container names for discovery.

> Status: The container architecture is operational and matches the conceptual intake–normalization–routing pattern described in this chapter. Some higher-order services (for example, qualia and swarm coordination) exist but are not yet fully integrated into the live routing fabric; their activation and repair are treated as future work.
