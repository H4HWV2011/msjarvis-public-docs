## Why this matters for Polymathmatic Geography  
This chapter explains how Ms. Jarvis's "containers" receive, sort, and route the flows of experience that later become memory and decision support. It supports:  
- **P1 – Every where is entangled** by treating events from people, places, and institutions as a shared stream that must be carefully routed into PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs) and ChromaDB memory.
- **P3 – Power has a geometry** by making explicit which services, ports, and stores stand between communities' data and long-term inference in PostgreSQL.
- **P5 – Design is a geographic act** by encoding how Appalachian events move through Ms. Jarvis and into PostgreSQL spatial, semantic, and commons-oriented stores.
- **P12 – Intelligence with a ZIP code** by prioritizing spatial, governance, and commons contexts from PostgreSQL GeoDB in the way container records are tagged and stored.
- **P16 – Power accountable to place** by using auditable container flows and verification scripts so communities can see where their data goes in PostgreSQL `msjarvisgis` and ChromaDB.

As such, this chapter belongs to the **Computational Instrument** tier: it describes the container and routing structures that turn raw events into traceable, place-aware memory anchored in PostgreSQL.
```
┌─────────────────────────────────────────────────────────────┐
│   Container Architecture and Routing Flow                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Incoming Events                                            │
│  • User queries (/chat)                                     │
│  • Internal tasks (autonomous learner, Fifth DGM)           │
│  • External signals                                         │
│  • Structural changes (GBIM updates)                        │
│      ↓                                                       │
│  Normalization Layer                                        │
│  • Core fields (ID, timestamps, origin)                     │
│  • Context (role, geography, tags)                          │
│  • Content summary                                          │
│  • Links (PostgreSQL GBIM, ChromaDB, GIS)                   │
│  • Control flags (safety, urgency, sensitivity)             │
│      ↓                                                       │
│  First-Level Routing                                        │
│  • Eligibility checks (BBB, truth validators)               │
│  • Priority assignment                                      │
│  • Track assignment                                         │
│      ↓                                                       │
│  ┌──────────────────────┬──────────────────────┐            │
│  │  Affective/Care Path │  Analytical/Tech Path│            │
│  │  • Psychological RAG │  • GIS/Spatial       │            │
│  │  • Community support │  • Infrastructure    │            │
│  │  • Ethical interpret │  • Optimization      │            │
│  └──────────────────────┴──────────────────────┘            │
│      ↓                        ↓                             │
│  Container Records                                          │
│  • Marked for evaluation                                   │
│  • Held back or dropped                                    │
│  • Introspective logs                                      │
│      ↓                                                       │
│  Long-Term Storage                                          │
│  • PostgreSQL msjarvisgis (port 5432)                       │
│  •   GBIM beliefs (5.4M+ verified)                          │
│  •   GeoDB spatial (501 tables, 91 GB)                      │
│  • ChromaDB (port 8002)                                     │
│  •   Semantic collections                                   │
│  • I-Containers (port 8015)                                 │
│  • Audit logs                                               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 19.1.** Container architecture and routing flow: incoming events from multiple sources are normalized, evaluated through first-level routing, distributed across parallel evaluation paths, and stored in PostgreSQL `msjarvisgis` (port 5432, 5.4M+ GBIM beliefs) and ChromaDB long-term memory with full audit trails.

---

# 19. Container Architecture and Routing

This chapter describes the high-level layout of the container-based structures that receive activity from earlier layers and route it into deeper evaluation paths anchored in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs). The goal is to separate the flow of events into clear stages, so that each stage has a well-defined role in deciding what is ignored, what is kept for background consideration, and what becomes part of PostgreSQL or ChromaDB central stores. In the implemented system, these responsibilities are realized by a set of Dockerized services that cooperate via HTTP and shared data stores. Conceptually, this reflects microservice and modular-control patterns as described by Lewis & Fowler and modular coordination work such as Goyal et al.

---

## 19.1 Position in the Overall System

The container layer sits between external interfaces and the lower-level retrieval, optimization, and global control mechanisms. It is visible both in the main-brain service that handles `/chat` requests and in the autonomous learning and Fifth DGM pipelines that generate and refine internal content. Its main responsibilities are to:

- Accept events coming from many sources, including question-handling flows, scheduled jobs, and self-improving processes.
- Normalize these events into a common format that can be evaluated and stored consistently in PostgreSQL `msjarvisgis` and ChromaDB.
- Dispatch normalized items into successive evaluation stages, while obeying system-wide constraints such as safety filters, resource limits, and service health.

Earlier parts of the work have described how information is retrieved from PostgreSQL GBIM, evaluated, and stored. This chapter focuses on how those elements are wrapped in container structures—both conceptual and literal Docker containers—that manage their entry into higher-level evaluative paths and PostgreSQL long-term memory.

---

## 19.2 Types of Incoming Events

In practice, the intake layer receives several broad categories of events that must be handled in a unified way:

- **Direct interactions**  
  User queries and responses that have already passed through initial retrieval from PostgreSQL-sourced RAG and constraint checks via the `jarvis-main-brain` `/chat` pipeline. These include synchronous requests and asynchronous jobs that are tracked via job IDs and status records.

- **Internal tasks**  
  Results from scheduled analyses, background maintenance jobs, and optimization routines. Examples include outputs from the autonomous learner, Fifth DGM optimization steps, and WOAH evaluations, which generate candidate content for the I-Container and other long-term structures.

- **External signals**  
  Notifications or status changes from connected systems such as messaging platforms, web front ends, or external data sources. These may arrive via dedicated services or be polled and converted into internal events.

- **Structural changes**  
  Updates to PostgreSQL `msjarvisgis` memory, GBIM belief graphs, or spatial layers that may require special attention. For instance, a new GBIM graph edge in PostgreSQL, a significant ChromaDB embedding insertion, or an update to access-control metadata can trigger container-level processing and validation.

Each event is accompanied by metadata such as timestamps, role identifiers, user or agent IDs, and source information. Container logic uses this metadata to make routing decisions, enforce policy, and maintain traceability back to PostgreSQL sources.

---

## 19.3 Normalization into Container Records

Before events are passed to deeper stages, they are normalized into container records with a common structure. This normalization is implemented in several places:

- In the `Ms. Jarvis ULTIMATE` main-brain, where incoming `/chat` requests are converted into structured request models and then into RAG storage records in ChromaDB backed by PostgreSQL GBIM queries.
- In the autonomous learning and Fifth DGM flows, where internal discoveries are wrapped into I-Container entries.

A typical normalized record includes:

- **Core fields**  
  A unique identifier, creation and update timestamps, origin (for example, `user_chat`, `autonomous_learner`, or `external_signal`), and a reference to the initiating service or job.

- **Context**  
  Active role or profile, relevant geographic or institutional context from PostgreSQL GeoDB, and tags describing the domain (such as `governance`, `infrastructure`, or `community_culture`). For chat records, this includes the user_id and any declared mode (for example, ultimate vs. simpler paths).

- **Content summary**  
  Key text, numerical values, or structured data extracted from the event. For chat interactions, this is typically a truncated version of the query and response plus any derived summaries. For internal tasks, it may include candidate knowledge statements, metrics, or optimization results.

- **Links**  
  References to memory items (ChromaDB embeddings, PostgreSQL GBIM graph nodes/edges at port 5432, relational records), spatial features (PostgreSQL GeoDB entities), and introspective entries (job logs, verification reports). These links make it possible to traverse from a container record back into PostgreSQL underlying stores.

- **Control information**  
  Flags indicating initial assessments such as urgency, sensitivity, safety status (for example, BBB-approved or denied), expected resource cost, and whether the item is considered high-value for long-term retention in PostgreSQL `msjarvisgis`.

This normalization step allows subsequent stages—such as I-Container growth, truth filtering against PostgreSQL GBIM, or consolidation—to apply uniform logic regardless of where the event originated. The overall pattern parallels retrieval and routing architectures in tool-using and agentic LLM systems, as surveyed in Ram et al., Schick et al., and Trivedi et al.

---

## 19.4 First-Level Routing Decisions

Once a record is normalized, the intake layer applies initial routing logic. In the running system, this logic appears in:

- The main-brain's decision to send a request through BBB, PostgreSQL-sourced RAG, web-research, and LLM ensembles, and then to queue RAG storage with specific metadata.
- The autonomous learner and Fifth DGM scripts that decide when to push new candidate items into the I-Container and when to leave them as transient results.

The first-level routing includes:

- **Eligibility checks**  
  Confirming that the record is allowed to enter container paths under current global settings. This includes safety checks (such as BBB and truth validators against PostgreSQL GBIM ground truth), role-based constraints, and checks for service availability via health probes.

- **Priority assignment**  
  Assigning a simple priority or track indicator that influences ordering and resource allocation. For example, user-facing requests may be processed before low-priority background maintenance items, and safety-relevant events may be escalated for additional scrutiny.

- **Track assignment**  
  Deciding whether the record should be sent to specific container subsystems such as the I-Container, psychological RAG domains, PostgreSQL GBIM graph updates, or audit logs. The same record may feed multiple tracks—for instance, both ChromaDB memory and PostgreSQL introspective audit—depending on its control flags.

At this stage, routing focuses on structural compatibility, basic policy, and safety, leaving deeper judgments (such as long-term importance or thematic clustering) to later stages.

---

## 19.5 Parallel Paths

The architecture supports multiple parallel paths that share a common structural pattern: intake → normalization → gating → storage in PostgreSQL or ChromaDB or discard. Conceptually, two broad tracks can be distinguished:

- **Affective and care-oriented paths**  
  Used when events are framed in terms of meaning, care, or psychological support. These may involve specialized RAG domains, therapeutic or community-oriented analysis, and services that emphasize ethical interpretation and human impact.

- **Analytical and technical paths**  
  Used for more conventional problem-solving tasks, such as infrastructure planning using PostgreSQL GeoDB, spatial reasoning, and optimization over data. These paths emphasize quantitative reasoning, model-based analysis, and technical verification against PostgreSQL GBIM ground truth.

The intake layer uses metadata, simple classifiers, and explicit flags to decide whether a record is best handled by one path, the other, or both. Each path then applies its own evaluation criteria and modules but retains the same overarching sequence of stages: initial safety, context integration from PostgreSQL GBIM, analysis, and optional storage into PostgreSQL long-term structures. Similar dual-track designs—separating meaning-focused and analysis-focused flows—appear in broader discussions of interpretability and explanation, such as Doshi-Velez & Kim and Lipton.

In concrete terms, these paths are supported by distinct services and RAG domains (for example, psychological RAG vs. general knowledge RAG sourced from PostgreSQL GBIM), as well as by specialized orchestration scripts that test different flows (such as the full autonomous learning + Fifth DGM + I-Container route).

---

## 19.6 Outputs of the Routing Layer

After routing, the container layer produces several types of outputs that feed later stages and support evaluation:

- **Records marked for immediate evaluation**  
  Items that pass eligibility checks and have sufficient priority are forwarded to downstream evaluators (for example, ensemble LLM reasoning, truth validators against PostgreSQL GBIM, or optimization routines). Their container records carry all necessary context and links to PostgreSQL tables.

- **Records held back or dropped**  
  Events may be held back (queued, delayed, or rate-limited) or dropped entirely based on policy. Reasons include safety denials, low priority under heavy load, redundancy detected by RAG similarity checks against ChromaDB, or failure of essential services.

- **Introspective logs and verification entries**  
  The system records which paths were chosen, which services were invoked, what PostgreSQL queries were executed, and what the outcomes were. Scripts such as `VERIFYANDTEST.sh` and `verifyallclaims.sh` generate structured summaries of service health, I-Container growth, autonomous learning cycles, ChromaDB status, and PostgreSQL connection health. These introspective outputs make the behavior of the routing layer auditable and support both debugging and research, consistent with AI auditing approaches described by Raji et al. and ISO/IEC 42001 guidance.

Together, these outputs ensure that downstream stages receive appropriately prepared inputs and that routing choices can be reconstructed and analyzed when necessary, with full traceability back to PostgreSQL `msjarvisgis` sources.

---

## 19.7 Conceptual Summary

Conceptually, the container architecture provides a structured way to receive, normalize, and direct events into deeper evaluative paths anchored in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs). It defines how diverse inputs—user interactions, internal learning results, external signals, and structural changes—enter the system's evaluative core. By enforcing clear stages and control flags, it supports disciplined decision-making about what is ignored, what is kept for background consideration, and what is integrated into PostgreSQL central memory and GBIM belief structures.

The remaining sections of this chapter ground this abstraction in an observed deployment topology, focusing on Docker containers, port mappings, and service roles as they existed during the December 2025 evaluation period.

---

## 19.8 Operational Container Topology (December 11, 2025)

This section summarizes one observed deployment topology, to ground the abstract container architecture in a concrete set of services. It should be read as an empirical snapshot rather than as a permanent or exhaustive design. The topology is derived from the `docker-compose.yml` configuration, runtime `docker ps` output, and verification scripts.

### Core Orchestration Layer

| Container          | Port Mapping | Role                                                                      |
|-------------------|-------------:|---------------------------------------------------------------------------|
| jarvis-main-brain | 8051→8050    | External API entry point; health-check sweep; service orchestration; RAG queueing to ChromaDB backed by PostgreSQL GBIM |

The `jarvis-main-brain` container hosts the `Ms. Jarvis ULTIMATE` main-brain FastAPI application. It exposes `/health`, `/chat`, and asynchronous job endpoints, performs health-based service discovery, and coordinates downstream services including PostgreSQL queries according to the executive coordination pattern described in Chapter 17.

### Coordination Services (ULTIMATE Path)

| Container                    | Port Mapping | Role                                                                |
|-----------------------------|-------------:|---------------------------------------------------------------------|
| jarvis-blood-brain-barrier  | 8016→8016    | Content filter; context cleaning; ethical and safety enforcement    |
| jarvis-llm-bridge           | 18006→8006   | Multi-model ensemble coordination; response synthesis               |
| jarvis-web-research         | 18009→8009   | External knowledge retrieval; web-based context enhancement         |

These services implement the intake and early-routing behavior described earlier: the main-brain calls the blood–brain barrier for gating, invokes web_research and PostgreSQL-sourced RAG for context, and uses llm_bridge as the primary LLM fabric for synthesis. Their outputs are normalized and incorporated into container records that can be stored in PostgreSQL `msjarvisgis`, audited, or further processed.

### Memory, Learning, and Optimization Services

| Container                      | Port Mapping | Role                                                    |
|-------------------------------|-------------:|---------------------------------------------------------|
| jarvis-autonomous-learner     | 18053→8053   | Autonomous learning; self-generated tasks and content   |
| jarvis-i-containers           | 18115→8015   | Container orchestration; storage of curated knowledge items |
| jarvis-fifth-dgm              | 14002→4002   | Darwin–Gödel–style optimization and filtering           |
| jarvis-neurobiological-master | 18118→8018   | Higher-level coordination among neurobiological modules |

These components participate in internal flows where the autonomous learner proposes new content, Fifth DGM evaluates and filters it, and successful items are integrated into the I-Container. Verification scripts demonstrate a complete flow:

1. Measuring initial I-Container size via an HTTP endpoint on port 4002.
2. Adding high-value test items through Fifth DGM routes.
3. Allowing WOAH and other evaluators to score the items.
4. Measuring I-Container size again to confirm growth.
5. Running analysis tools that inspect I-Container contents, keywords, and topics to assess growth stage and recommendations.

This flow illustrates how internal tasks and structural changes enter the container layer and how normalization and routing support long-term storage in PostgreSQL and ChromaDB. Related ideas about background world models and pattern libraries are explored in Battaglia et al.'s work on relational inductive biases and graph networks.

### Data Persistence and Semantics

| Container                   | Port Mapping | Role                                        |
|----------------------------|-------------:|---------------------------------------------|
| jarvis-chroma              | 8000→8000    | Primary semantic memory (ChromaDB instance) |
| services-chroma-1          | 8010→8010    | Additional or legacy ChromaDB instance      |
| msjarvis-rebuild-chroma-1  | 8002→8000    | Rebuild / development ChromaDB instance     |
| postgresql-msjarvisgis     | 5432→5432    | PostgreSQL 16: GBIM beliefs (5.4M+), GeoDB (501 tables, 91 GB) |
| services-neo4j-1           | 7474, 7687   | GBIM graph database (legacy)                |
| services-mysql-1           | 3307→3306    | Relational data store; user and audit records (legacy) |

Verification scripts confirm that ChromaDB directories exist, that collections (such as `msjarvismemories`) can be opened and counted, that PostgreSQL `msjarvisgis` at port 5432 is reachable with 5.4M+ verified GBIM beliefs in `gbimbeliefnormalized`, and that Neo4j and MySQL instances are reachable on the expected ports. Container records link into these stores via IDs, foreign keys, PostgreSQL table references, and ChromaDB document IDs, enabling cross-layer navigation from events to semantic and structural representations in PostgreSQL. The use of graph and memory structures echoes broader patterns in relational inductive biases and pattern abstraction (for example, Battaglia et al.; Lake et al.'s Omniglot work).

### Service Registry, Dynamic Ports, and Discovery

In addition to static ports defined in `docker-compose.yml`, the system uses a service registry and Redis-based dynamic port allocation for some components. Scripts such as `verifyallclaims.sh` check:

- Existence and contents of `serviceregistry.json`, which lists services with names and ports.
- Redis keys of the form `service:<name>` that map to dynamically assigned ports.
- Health of registered services by iterating over the registry and issuing `GET /health` checks.

This registry layer supports the container architecture by allowing certain services (for example, multiple AIs or RAG domains) to join and leave dynamically while remaining discoverable by orchestrators and container logic. Similar concerns about monitoring, liveness, and controllers appear in cloud-native design discussions by Brewer and in controller patterns documented by Burns et al.

### External Access Points and LLM Backend

Only a small subset of ports are exposed to the host:

- **8051** – External API endpoint (mapped to `jarvis-main-brain` on 8050).
- **11434** – Ollama LLM backend (local model serving, typically in `jarvis-ollama`).
- **5432** – PostgreSQL `msjarvisgis` (GBIM and GeoDB source of truth).

All other services communicate over the Docker bridge network using container names and internal ports for discovery. The llm_bridge service connects to the Ollama backend to run ensembles of local models, while the main-brain and other orchestration components treat llm_bridge as a black box for LLM inference. This design fits into broader trends toward mixture-of-experts and agentic ensembles, such as Du et al.'s GLaM, Liu et al.'s AgentBench, and Shen et al.'s Mixture-of-Agents framework.

---

## 19.9 Observed Routing Behavior in Verification Scripts

Several shell scripts provide concrete evidence of how the container architecture behaves in practice:

- **VERIFYANDTEST.sh**  
  Checks RAG, web UI, and selected services, confirming that containerized components are reachable, that PostgreSQL `msjarvisgis` is accessible at port 5432, and that semantic memory is populated.

- **verifyallclaims.sh**  
  Exercises a complete autonomous learning and I-Container flow, testing:
  - Current I-Container size and growth capacity.
  - Service registry and dynamic port integration via Redis.
  - Health of key services (Fifth DGM, WOAH, I-Containers, Consciousness Bridge, Autonomous Learner, Web Research, LLM Bridge, Qualia Engine, Swarm Intelligence).
  - PostgreSQL `msjarvisgis` connection health and GBIM belief counts.
  - I-Container analysis tools that report size, status, keywords, and suggested topics.

- **VERIFY CHROMADB sections**  
  Confirm that ChromaDB directories exist, that collections can be queried, that embedding counts match expectations, and that PostgreSQL-sourced GBIM collections are properly synchronized, tying container records back to semantic memory and PostgreSQL ground truth.

These scripts demonstrate that the container architecture is not merely conceptual: it is instrumented and testable, with observable behaviors that align with the intake–normalization–routing pattern described in this chapter and anchored in PostgreSQL `msjarvisgis`. They also mirror best practices for health checks and monitoring in distributed systems as discussed by Brewer and Burns et al.

---

## 19.10 Summary

The container architecture and routing layer described here provide the structural glue between external interfaces, executive coordination, autonomous learning, and PostgreSQL long-term memory. Through a combination of Dockerized services, service registry mechanisms, and structured normalization of events into container records, the system can:

- Receive and categorize diverse inputs from users, internal processes, and external signals.
- Apply safety filters, eligibility checks against PostgreSQL GBIM truth, and basic policy decisions at the intake stage.
- Route normalized records into parallel paths for affective and analytical evaluation.
- Feed curated content into PostgreSQL long-term stores such as the I-Container, ChromaDB (backed by PostgreSQL GBIM), GBIM graphs in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified beliefs), and relational databases.

By grounding the abstract design in a concrete December 2025 topology and associated verification scripts, this chapter demonstrates that the container architecture is both implemented and empirically observable, with all memory and routing flows ultimately anchored to PostgreSQL `msjarvisgis` at port 5432. Subsequent chapters will build on this foundation to describe how filtered and routed items are further evaluated, consolidated, and woven into longer-term cognitive and memory structures in PostgreSQL.
