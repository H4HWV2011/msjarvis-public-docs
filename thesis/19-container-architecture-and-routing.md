# 19. Container Architecture and Routing

This chapter describes the high-level layout of the container-based structures that receive activity from earlier layers and route it into deeper evaluation paths. The goal is to separate the flow of events into clear stages, so that each stage has a well-defined role in deciding what is ignored, what is kept for background consideration, and what becomes part of a more central store. In the implemented system, these responsibilities are realized by a set of Dockerized services that cooperate via HTTP and shared data stores.

## 19.1 Position in the Overall System

The container layer sits between external interfaces and the lower-level retrieval, optimization, and global control mechanisms. It is visible both in the main-brain service that handles `/chat` requests and in the autonomous learning and Fifth DGM pipelines that generate and refine internal content. Its main responsibilities are to:

- Accept events coming from many sources, including question-handling flows, scheduled jobs, and self-improving processes.
- Normalize these events into a common format that can be evaluated and stored in a consistent way.
- Dispatch normalized items into successive evaluation stages, while obeying system-wide constraints such as safety filters, resource limits, and service health.

Earlier parts of the work have described how information is retrieved, evaluated, and stored. This chapter focuses on how those elements are wrapped in container structures—both conceptual and literal Docker containers—that manage their entry into higher-level evaluative paths and long-term memory.

## 19.2 Types of Incoming Events

In practice, the intake layer receives several broad categories of events that must be handled in a unified way:

- **Direct interactions**  
  User queries and responses that have already passed through initial retrieval and constraint checks via the `jarvis-main-brain` `/chat` pipeline. These include synchronous requests and asynchronous jobs that are tracked via job IDs and status records.

- **Internal tasks**  
  Results from scheduled analyses, background maintenance jobs, and optimization routines. Examples include outputs from the autonomous learner, Fifth DGM optimization steps, and WOAH evaluations, which generate candidate content for the I-Container and other long-term structures.

- **External signals**  
  Notifications or status changes from connected systems such as messaging platforms, web front ends, or external data sources. These may arrive via dedicated services or be polled and converted into internal events.

- **Structural changes**  
  Updates to memory, belief graphs, or spatial layers that may require special attention. For instance, a new GBIM graph edge, a significant Chroma embedding insertion, or an update to access-control metadata can trigger container-level processing and validation.

Each event is accompanied by metadata such as timestamps, role identifiers, user or agent IDs, and source information. Container logic uses this metadata to make routing decisions, enforce policy, and maintain traceability.

## 19.3 Normalization into Container Records

Before events are passed to deeper stages, they are normalized into container records with a common structure. This normalization is implemented in several places:

- In the `Ms. Jarvis ULTIMATE` main-brain, where incoming `/chat` requests are converted into structured request models and then into RAG storage records.
- In the autonomous learning and Fifth DGM flows, where internal discoveries are wrapped into I-Container entries.

A typical normalized record includes:

- **Core fields**  
  A unique identifier, creation and update timestamps, origin (for example, `user_chat`, `autonomous_learner`, or `external_signal`), and a reference to the initiating service or job.

- **Context**  
  Active role or profile, relevant geographic or institutional context, and tags describing the domain (such as `governance`, `infrastructure`, or `community_culture`). For chat records, this includes the user_id and any declared mode (for example, ultimate vs. simpler paths).

- **Content summary**  
  Key text, numerical values, or structured data extracted from the event. For chat interactions, this is typically a truncated version of the query and response plus any derived summaries. For internal tasks, it may include candidate knowledge statements, metrics, or optimization results.

- **Links**  
  References to memory items (Chroma embeddings, GBIM graph nodes/edges, relational records), spatial features (GIS entities), and introspective entries (job logs, verification reports). These links make it possible to traverse from a container record back into underlying stores.

- **Control information**  
  Flags indicating initial assessments such as urgency, sensitivity, safety status (for example, BBB-approved or denied), expected resource cost, and whether the item is considered high-value for long-term retention.

This normalization step allows subsequent stages—such as I-Container growth, truth filtering, or consolidation—to apply uniform logic regardless of where the event originated.

## 19.4 First-Level Routing Decisions

Once a record is normalized, the intake layer applies initial routing logic. In the running system, this logic appears in:

- The main-brain’s decision to send a request through BBB, RAG, web-research, and LLM ensembles, and then to queue RAG storage with specific metadata.
- The autonomous learner and Fifth DGM scripts that decide when to push new candidate items into the I-Container and when to leave them as transient results.

The first-level routing includes:

- **Eligibility checks**  
  Confirming that the record is allowed to enter container paths under current global settings. This includes safety checks (such as BBB and truth validators), role-based constraints, and checks for service availability via health probes.

- **Priority assignment**  
  Assigning a simple priority or track indicator that influences ordering and resource allocation. For example, user-facing requests may be processed before low-priority background maintenance items, and safety-relevant events may be escalated for additional scrutiny.

- **Track assignment**  
  Deciding whether the record should be sent to specific container subsystems such as the I-Container, psychological RAG domains, GBIM graph updates, or audit logs. The same record may feed multiple tracks—for instance, both memory and introspective audit—depending on its control flags.

At this stage, routing focuses on structural compatibility, basic policy, and safety, leaving deeper judgments (such as long-term importance or thematic clustering) to later stages.

## 19.5 Parallel Paths

The architecture supports multiple parallel paths that share a common structural pattern: intake → normalization → gating → storage or discard. Conceptually, two broad tracks can be distinguished:

- **Affective and care-oriented paths**  
  Used when events are framed in terms of meaning, care, or psychological support. These may involve specialized RAG domains, therapeutic or community-oriented analysis, and services that emphasize ethical interpretation and human impact.

- **Analytical and technical paths**  
  Used for more conventional problem-solving tasks, such as infrastructure planning, spatial reasoning, and optimization over data. These paths emphasize quantitative reasoning, model-based analysis, and technical verification.

The intake layer uses metadata, simple classifiers, and explicit flags to decide whether a record is best handled by one path, the other, or both. Each path then applies its own evaluation criteria and modules but retains the same overarching sequence of stages: initial safety, context integration, analysis, and optional storage into long-term structures.

In concrete terms, these paths are supported by distinct services and RAG domains (for example, psychological RAG vs. general knowledge RAG), as well as by specialized orchestration scripts that test different flows (such as the full autonomous learning + Fifth DGM + I-Container route).

## 19.6 Outputs of the Routing Layer

After routing, the container layer produces several types of outputs that feed later stages and support evaluation:

- **Records marked for immediate evaluation**  
  Items that pass eligibility checks and have sufficient priority are forwarded to downstream evaluators (for example, ensemble LLM reasoning, truth validators, or optimization routines). Their container records carry all necessary context and links.

- **Records held back or dropped**  
  Events may be held back (queued, delayed, or rate-limited) or dropped entirely based on policy. Reasons include safety denials, low priority under heavy load, redundancy detected by RAG similarity checks, or failure of essential services.

- **Introspective logs and verification entries**  
  The system records which paths were chosen, which services were invoked, and what the outcomes were. Scripts such as `VERIFYANDTEST.sh` and `verifyallclaims.sh` generate structured summaries of service health, I-Container growth, autonomous learning cycles, and ChromaDB status. These introspective outputs make the behavior of the routing layer auditable and support both debugging and research.

Together, these outputs ensure that downstream stages receive appropriately prepared inputs and that routing choices can be reconstructed and analyzed when necessary.

## 19.7 Conceptual Summary

Conceptually, the container architecture provides a structured way to receive, normalize, and direct events into deeper evaluative paths. It defines how diverse inputs—user interactions, internal learning results, external signals, and structural changes—enter the system’s evaluative core. By enforcing clear stages and control flags, it supports disciplined decision-making about what is ignored, what is kept for background consideration, and what is integrated into central memory and belief structures.

The remaining sections of this chapter ground this abstraction in an observed deployment topology, focusing on Docker containers, port mappings, and service roles as they existed during the December 2025 evaluation period.

---

## 19.8 Operational Container Topology (December 11, 2025)

This section summarizes one observed deployment topology, to ground the abstract container architecture in a concrete set of services. It should be read as an empirical snapshot rather than as a permanent or exhaustive design. The topology is derived from the `docker-compose.yml` configuration, runtime `docker ps` output, and verification scripts.

### Core Orchestration Layer

| Container         | Port Mapping | Role                                                                      |
|------------------|-------------:|---------------------------------------------------------------------------|
| jarvis-main-brain| 8051→8050    | External API entry point; health-check sweep; service orchestration; RAG queueing |

The `jarvis-main-brain` container hosts the `Ms. Jarvis ULTIMATE` main-brain FastAPI application. It exposes `/health`, `/chat`, and asynchronous job endpoints, performs health-based service discovery, and coordinates downstream services according to the executive coordination pattern described in Chapter 17.

### Coordination Services (ULTIMATE Path)

| Container                   | Port Mapping | Role                                                          |
|-----------------------------|-------------:|---------------------------------------------------------------|
| jarvis-blood-brain-barrier | 8016→8016    | Content filter; context cleaning; ethical and safety enforcement |
| jarvis-llm-bridge          | 18006→8006   | Multi-model ensemble coordination; response synthesis         |
| jarvis-web-research        | 18009→8009   | External knowledge retrieval; web-based context enhancement   |

These services implement the intake and early-routing behavior described earlier: the main-brain calls the blood–brain barrier for gating, invokes web_research and RAG for context, and uses llm_bridge as the primary LLM fabric for synthesis. Their outputs are normalized and incorporated into container records that can be stored, audited, or further processed.

### Memory, Learning, and Optimization Services

| Container                     | Port Mapping | Role                                              |
|------------------------------|-------------:|---------------------------------------------------|
| jarvis-autonomous-learner    | 18053→8053   | Autonomous learning; self-generated tasks and content |
| jarvis-i-containers          | 18115→8015   | Container orchestration; storage of curated knowledge items |
| jarvis-fifth-dgm             | 14002→4002   | Darwin–Gödel–style optimization and filtering     |
| jarvis-neurobiological-master| 18118→8018   | Higher-level coordination among neurobiological modules |

These components participate in internal flows where the autonomous learner proposes new content, Fifth DGM evaluates and filters it, and successful items are integrated into the I-Container. Verification scripts demonstrate a complete flow:

1. Measuring initial I-Container size via an HTTP endpoint on port 4002.
2. Adding high-value test items through Fifth DGM routes.
3. Allowing WOAH and other evaluators to score the items.
4. Measuring I-Container size again to confirm growth.
5. Running analysis tools that inspect I-Container contents, keywords, and topics to assess growth stage and recommendations.

This flow illustrates how internal tasks and structural changes enter the container layer and how normalization and routing support long-term storage.

### Data Persistence and Semantics

| Container                  | Port Mapping | Role                                        |
|---------------------------|-------------:|---------------------------------------------|
| jarvis-chroma             | 8000→8000    | Primary semantic memory (ChromaDB instance) |
| services-chroma-1         | 8010→8010    | Additional or legacy ChromaDB instance      |
| msjarvis-rebuild-chroma-1 | 8002→8000    | Rebuild / development ChromaDB instance     |
| services-neo4j-1          | 7474, 7687   | GBIM graph database                         |
| services-mysql-1          | 3307→3306    | Relational data store; user and audit records |

Verification scripts confirm that ChromaDB directories exist, that collections (such as `msjarvismemories`) can be opened and counted, and that Neo4j and MySQL instances are reachable on the expected ports. Container records link into these stores via IDs, foreign keys, and Chroma document IDs, enabling cross-layer navigation from events to semantic and structural representations.

### Service Registry, Dynamic Ports, and Discovery

In addition to static ports defined in `docker-compose.yml`, the system uses a service registry and Redis-based dynamic port allocation for some components. Scripts such as `verifyallclaims.sh` check:

- Existence and contents of `serviceregistry.json`, which lists services with names and ports.
- Redis keys of the form `service:<name>` that map to dynamically assigned ports.
- Health of registered services by iterating over the registry and issuing `GET /health` checks.

This registry layer supports the container architecture by allowing certain services (for example, multiple AIs or RAG domains) to join and leave dynamically while remaining discoverable by orchestrators and container logic.

### External Access Points and LLM Backend

Only a small subset of ports are exposed to the host:

- **8051** – External API endpoint (mapped to `jarvis-main-brain` on 8050).
- **11434** – Ollama LLM backend (local model serving, typically in `jarvis-ollama`).

All other services communicate over the Docker bridge network using container names and internal ports for discovery. The llm_bridge service connects to the Ollama backend to run ensembles of local models, while the main-brain and other orchestration components treat llm_bridge as a black box for LLM inference.

---

## 19.9 Observed Routing Behavior in Verification Scripts

Several shell scripts provide concrete evidence of how the container architecture behaves in practice:

- **VERIFYANDTEST.sh**  
  Checks RAG, web UI, and selected services, confirming that containerized components are reachable and that semantic memory is populated.

- **verifyallclaims.sh**  
  Exercises a complete autonomous learning and I-Container flow, testing:
  - Current I-Container size and growth capacity.
  - Service registry and dynamic port integration via Redis.
  - Health of key services (Fifth DGM, WOAH, I-Containers, Consciousness Bridge, Autonomous Learner, Web Research, LLM Bridge, Qualia Engine, Swarm Intelligence).
  - I-Container analysis tools that report size, status, keywords, and suggested topics.

- **VERIFY CHROMADB sections**  
  Confirm that ChromaDB directories exist, that collections can be queried, and that embedding counts match expectations, tying container records back to semantic memory.

These scripts demonstrate that the container architecture is not merely conceptual: it is instrumented and testable, with observable behaviors that align with the intake–normalization–routing pattern described in this chapter.

## 19.10 Summary

The container architecture and routing layer described here provide the structural glue between external interfaces, executive coordination, autonomous learning, and long-term memory. Through a combination of Dockerized services, service registry mechanisms, and structured normalization of events into container records, the system can:

- Receive and categorize diverse inputs from users, internal processes, and external signals.
- Apply safety filters, eligibility checks, and basic policy decisions at the intake stage.
- Route normalized records into parallel paths for affective and analytical evaluation.
- Feed curated content into long-term stores such as the I-Container, ChromaDB, GBIM graphs, and relational databases.

By grounding the abstract design in a concrete December 2025 topology and associated verification scripts, this chapter demonstrates that the container architecture is both implemented and empirically observable. Subsequent chapters will build on this foundation to describe how filtered and routed items are further evaluated, consolidated, and woven into longer-term cognitive and memory structures.
