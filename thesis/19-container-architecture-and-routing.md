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

### Container Topology (December 11, 2025)

#### ✅ VALIDATED: Port Audit Complete

Complete inventory of 19 Docker containers and port mappings.

#### Core Orchestration Layer

| Container         | Image                          | Port Mapping | Status        | Role                                                                 |
|-------------------|--------------------------------|--------------|---------------|----------------------------------------------------------------------|
| jarvis-main-brain | msjarvis-main-brain:latest     | 8051→8050    | ✅ Operational | External API entry point; health check sweep; service orchestration |

#### Coordination Services (ULTIMATE Path)

| Container                  | Image                          | Port Mapping | Status        | Role                                               |
|----------------------------|--------------------------------|--------------|---------------|----------------------------------------------------|
| jarvis-blood-brain-barrier | msjarvis-bbb:latest           | 8016→8016    | ✅ Operational | Content filter; context cleaning; safety enforcement |
| jarvis-llm-bridge          | msjarvis-llm-bridge:latest    | 18006→8006   | ✅ Operational | 22‑agent ensemble coordination; response synthesis |
| jarvis-web-research        | msjarvis-web-research:latest  | 18009→8009   | ✅ Operational | Context enhancement; external knowledge retrieval  |

#### Consciousness & Coordination Services (Not Invoked)

| Container                  | Image                                  | Port Mapping | Status        | Role                               |
|----------------------------|----------------------------------------|--------------|---------------|------------------------------------|
| jarvis-qualia-engine       | msjarvis-qualia-engine:latest         | 18117→8017   | 🔄 Not invoked | Introspective state; qualia layer  |
| jarvis-swarm-intelligence  | msjarvis-swarm:latest                 | 18221→8021   | 🔄 Not invoked | Swarm coordination; multi-agent    |
| jarvis-consciousness-bridge| msjarvis-consciousness-bridge:latest  | 18220→8020   | 🔄 Not invoked | Inter-service consciousness sync   |
| jarvis-unified-gateway     | msjarvis-unified-gateway:latest       | 18001→8001   | 🔄 Not invoked | External communication authority   |

#### Memory & Learning Services

| Container                  | Image                               | Port Mapping | Status        | Role                              |
|----------------------------|-------------------------------------|--------------|---------------|-----------------------------------|
| jarvis-autonomous-learner  | msjarvis-autonomous-learner:latest | 18053→8053   | 🔄 Unknown     | Autonomous learning; self-improve |
| jarvis-neurobiological-master | msjarvis-neuro-master:latest    | 18118→8018   | 🔄 Unknown     | Neurobiological coordination      |
| jarvis-i-containers        | msjarvis-i-containers:latest        | 18115→8015   | 🔄 Unknown     | Container orchestration           |
| jarvis-fifth-dgm           | msjarvis-fifth-dgm:latest           | 14002→4002   | 🔄 Unknown     | Darwin–Gödel machine; optimization |

#### Data Persistence & Semantics

| Container                 | Image                   | Port Mapping | Status     | Role                               |
|---------------------------|-------------------------|--------------|------------|------------------------------------|
| jarvis-chroma             | msjarvis-chroma:0.4.24 | 8000→8000    | ✅ Running | Primary semantic memory (ChromaDB) |
| services-chroma-1         | chromadb/chroma:latest | 8010→8010    | ✅ Running | Services stack ChromaDB instance   |
| msjarvis-rebuild-chroma-1 | chromadb/chroma:latest | 8002→8000    | ✅ Running | Rebuild / development instance     |

#### External Access Points

Only two ports are exposed to the host (localhost):

- **8051**: External API endpoint (`jarvis-main-brain`).  
- **11434**: Ollama LLM backend (local model access).

All other services communicate internally via Docker’s bridge network and DNS, using container names for service discovery.

#### Databases & Infrastructure

| Container        | Image                | Port Mapping | Status     | Role                                              |
|------------------|----------------------|--------------|------------|---------------------------------------------------|
| services-neo4j-1 | neo4j:5.13-community | 7474, 7687   | ✅ Running | Graph database; GBIM spatial and identity graphs  |
| services-mysql-1 | mysql:8.2            | 3307→3306    | ✅ Running | Relational data; user management; audit logs      |
| services-ipfs-1  | ipfs/kubo:latest     | 5001         | ✅ Running | Distributed storage; content-addressed artifacts  |

#### LLM Backend

| Container     | Image                | Port Mapping  | Status     | Role                         |
|---------------|----------------------|---------------|------------|------------------------------|
| jarvis-ollama | ollama/ollama:latest | 11434→11434   | ✅ Running | Local LLM execution backend  |

#### Service Health Status (December 11, 2025)

**Operational**: 8/23 (34.8%)

- ✅ `jarvis-main-brain`  
- ✅ `jarvis-blood-brain-barrier`  
- ✅ `jarvis-llm-bridge`  
- ✅ `jarvis-web-research`  
- ✅ `jarvis-chroma` (main)  
- ✅ `services-chroma-1`  
- ✅ `services-neo4j-1`  
- ✅ `services-mysql-1`  
- ✅ `jarvis-ollama`  

**Non‑responsive**: 15/23 (65.2%)

- 🔄 `jarvis-qualia-engine`  
- 🔄 `jarvis-swarm-intelligence`  
- 🔄 `jarvis-consciousness-bridge`  
- 🔄 `jarvis-unified-gateway`  
- 🔄 `jarvis-autonomous-learner`  
- 🔄 `jarvis-neurobiological-master`  
- 🔄 `jarvis-i-containers`  
- 🔄 `jarvis-fifth-dgm`  
- 🔄 + 7 others pending detailed profiling  

#### Future Work: Service Repair

Priority for bringing non-responsive services online:

1. `jarvis-qualia-engine` (introspection for better reasoning).  
2. `jarvis-swarm-intelligence` (distributed consensus).  
3. `jarvis-consciousness-bridge` (system coherence).  
4. `jarvis-fifth-dgm` (self-improvement capability).  
5. Remaining services, after profiling resource requirements.

#### Narrative Summary

The container architecture described in this chapter now has a concrete, validated topology: `jarvis-main-brain` on port 8051 fronts BBB, web_research, and llm_bridge, backed by ChromaDB, Neo4j, MySQL, IPFS, and Ollama. This layout provides the operational substrate for receiving, normalizing, and routing events into deeper evaluative paths, and sets the stage for future work on repairing and activating the higher-order consciousness and swarm services so they can participate in the same routing fabric.
