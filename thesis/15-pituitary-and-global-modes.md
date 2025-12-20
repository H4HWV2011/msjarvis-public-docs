# 15. Pituitary and Global Modes

This chapter describes the layer that controls global settings and modes across the system. The design borrows the idea of a central regulator that sends signals influencing many subsystems at once, implemented here as configuration state, constitutional and supervisory services, and routing policies that shape how agents, retrieval, and generation behave under different conditions.

## 15.1 Purpose and Scope

Global controls in Ms. Jarvis are realized as a set of always‑on governance and modulation services rather than static configuration files. The core components are:

- **Constitutional Guardian**  
  A dedicated constraint engine and API that enforces high‑level prohibitions (e.g., no PII collection without consent, no integration with surveillance infrastructure), logs violations, and exposes audit and status endpoints under `/constitutional/*`.

- **Pituitary emotional‑depth service**  
  A microservice that wraps a `pituitary_gland` module and exposes `/process` to add emotional depth to payloads and `/health` for monitoring, intended to modulate global affective tone.

- **WOAH / DGM supervisory services**  
  Services that estimate multi‑scale complexity (`fractal_dgm_woah`), maintain and increment global WOAH weights, and expose optimization endpoints for self‑improving behavior.

These controls are treated as dynamic state that can evolve over time, and their status and effects are surfaced through unified gateway endpoints with explicit `system_transparency_mode` descriptions.

## 15.2 Types of Global Settings

The global layer manages several categories of settings and constraints, grounded in concrete artifacts:

- **Safety and constitutional constraints**  
  - A `ConstitutionalPrinciple` enum defines principles such as `NO_PII`, `NO_SURVEILLANCE_INTEGRATION`, `NO_FINANCIAL_SURVEILLANCE`, `WATCHDOG_VISIBLE`, `DECISIONS_LOGGED`, and `COMMUNITY_VETO`, implemented in `ConstitutionalConstraint` objects that inspect request payloads and log violations.  
  - The Constitutional API exposes `/constitutional/status`, `/constitutional/principles`, `/constitutional/audit`, and `/constitutional/transparency`, reporting constraint counts, detailed principle descriptions, a hashed audit trail, and governance summaries.

- **WOAH weights and fractal dimensions**  
  - `config/woah_weights.json` specifies weights over dimensions such as safety, truthfulness, helpfulness, local_context, and spiritual_alignment, and fractal layers like session, daily, and weekly, representing global emphasis profiles.  
  - Analysis services compute WOAH‑weighted complexity across gamma, beta, theta, and delta bands and interpret the result as “initializing,” “agents coordinating,” or “full DGM integration,” effectively labeling global cognitive state for given message sequences.

- **Roles, personas, and orchestration modes**  
  - The LLM bridge defines a 20‑model ensemble with per‑model `role` tags (e.g., `quick_general`, `reasoning`, `medical`, `vision`, `code`, `multilingual`), allowing orchestration layers to reason about which kinds of capabilities they are invoking.  
  - DGM orchestrators maintain explicit mode fields such as `{"mode": "emergent_passthrough"}` and return responses labeled with `mode="dgm_complete_integration"`, making global orchestration state explicit in the API.

- **System‑wide transparency modes**  
  Unified gateway endpoints advertise per‑subsystem `system_transparency_mode` strings describing the configuration of storage, RAG, qualia, WOAH, and GIS services (for example, indicating direct DB access, depth of analysis, or “no hidden loops”), which function as human‑readable global mode descriptors.

Each of these settings has a defined meaning and is either stored in structured config (e.g., JSON/YAML) or exposed via documented HTTP endpoints whose outputs can be queried and versioned.

## 15.3 Implementation and Storage

The global control state is implemented through a combination of configuration files, long‑running services, and code‑level flags:

- **Structured configuration and persistence**  
  - `config/settings.py` encapsulates application and database configuration (Facebook API, Neo4j, Redis, Chroma path) via Pydantic models, with environment‑based overrides and automatic creation of the Chroma path, providing a typed, persistent backing for global connectivity and storage settings.  
  - `config/woah_weights.json`, `constitutional_principles.yml`, and `constitutional_principles.md` encode numeric weights and textual principles that guide behavior, and are updated or read by services like `woah_optimizer.py` and the Constitutional API.

- **Derived flags and in‑memory state**  
  - Services such as the unified status and orchestrators derive simple flags like `woah_processed`, `darwin_processed`, `blood_brain_barrier` active, and current DGM mode, and include them in JSON responses to higher‑level gateways.  
  - Redis is used by some status components to track orchestrator state under keys like `jarvis:state`, contributing to short natural‑language or JSON summaries of the system’s current focus that can be consumed by higher‑level agents.

- **Change logs and audits**  
  - The Constitutional Guardian logs every violation event with timestamps, associated principles, violation descriptions, and maintains a SHA‑256 hash over the log as `audit_integrity`, giving an integrity‑checked audit trail of blocked actions.  
  - Scripts such as `VERIFY_AND_TEST.sh`, `verify_full_integration.sh`, and `verify_all_claims.sh` define operational verification routines that can be invoked to assert that the deployed system is consistent with intended configurations and documentation.

Services that need to obey global controls either read this state on startup and periodically (e.g., via health/status calls) or rely on orchestrators and gateways that aggregate the relevant flags and present them as part of higher‑level responses.

## 15.4 Influence on Agents and Retrieval

Global settings materially influence how agents are selected, how retrieval operates, and how deep reasoning is allowed to proceed:

- **Layered orchestration pipelines**  
  - `unified_app_coordinated_real.py` orchestrates a chain of services—main AI (port 8000), Darwin–Gödel Machine (7003), WOAH algorithms (7012), Mamma Kidd spiritual model (4003), and an orchestrator (33881)—tracking which layers have processed the request in `layers_processed` and exposing flags like `darwin_godel_active` and `woah_active`.  
  - `unified_app_final.py` routes through the main AI and Mamma Kidd, then an orchestrator, and returns a response explicitly labeled with the `mamma_kidd` personality, demonstrating role‑shaped final outputs.

- **Safety gating before retrieval and reasoning**  
  - The blood–brain barrier service and associated filters and judges enforce safety before deeper reasoning or retrieval occurs, blocking or rephrasing queries and returning structured reasons, which are logged and surfaced up to the main brain.  
  - The Constitutional Guardian is designed to validate request payloads against surveillance‑ and PII‑related constraints, and its audit output can be used to examine whether specific retrieval or reasoning steps were blocked by constitutional rules.

- **Mode‑dependent depth and routing**  
  - DGM orchestrators such as `master_chat_orchestrator_v9_dgm_complete.py` explicitly annotate responses with `dgm_orchestration` information (e.g., `{"mode": "emergent_passthrough"}`) and a final `mode` field set to `"dgm_complete_integration"`, which can be consumed by downstream introspective and control layers.  
  - Unified gateways control which services are invoked and how their outputs are merged, and their endpoints report `system_transparency_mode` texts describing whether, for example, full audit, high‑depth analysis, or minimal direct DB access modes are active for RAG and GIS subsystems.

These mechanisms ensure that identical underlying capabilities are deployed differently depending on global modes, governance constraints, and orchestration choices.

## 15.5 Interaction with Optimization and Self‑Improvement

Optimization and self‑improving components treat global controls both as constraints and as parameters to tune:

- **WOAH optimization and versioning**  
  - `woah_optimizer.py` implements a simple, long‑running process that repeatedly loads `woah_weights.json`, increments its `version`, and writes it back, serving as a scaffold for future logic that will adjust these weights according to system performance metrics stored in Redis or logs.  
  - `ms_jarvis_fractal_dgm_woah.py` uses WOAH weights to compute a `weighted_complexity` and an improvement factor, and assigns interpretive labels to the system’s complexity state (e.g., “High – WOAH harmonics active”), which can be used to gate when more aggressive self‑improvement actions are permitted.

- **DGM supervisory and orchestration modes**  
  - `dgm_supervisor_woah_simple.py` exposes `/optimize_woah`, returning a structured object indicating that WOAH weights and hierarchies have been optimized, even though the current implementation is a stub; this endpoint represents an explicit control surface for exploration bounds and hierarchical tuning.  
  - `master_chat_orchestrator_v9_dgm_complete.py` labels its main chat endpoint as “EMERGENT PASSTHROUGH MODE,” and returns structured metadata, including `dgm_orchestration`, `woah_optimization`, and `biological_processing`, enabling external processes to analyze and potentially adjust the orchestrator’s operating mode.

- **Deployment gates and verification**  
  Shell scripts such as `verify_full_integration.sh` and `VERIFY_AND_TEST.sh` provide system‑level checks that can be integrated into deployment pipelines to ensure that the state of safety filters, constitutional services, and orchestrators is acceptable before enabling new modes or self‑improvement behaviors in production.

By tying optimization routines to centrally visible state—weights, modes, and constraint outputs—the system can adjust how ambitious or conservative it is without editing the code of each individual agent.

## 15.6 Relationship to Introspection and Memory

Global modes are both informed by and reflected in the system’s introspective and memory layers:

- **Introspective awareness of modes**  
  Consciousness coordination logs already include fields describing which GBIM services and consciousness layers are active, and reference scores and discrepancies between mesh status and integrated beliefs, providing evidence that introspective summaries can incorporate mode‑like metadata about system configuration.

- **Consolidated memory annotated with configuration**  
  Consolidation pipelines that route through coordinated and final unified apps can include fields such as `woah_active`, `darwin_godel_active`, and the specific pipeline layers traversed, so that long‑term memory entries implicitly record which global mechanisms were engaged when a particular episode occurred.

- **Feedback loops into global settings**  
  Because the Constitutional Guardian maintains a detailed audit trail and WOAH/DGM analyzers report complexity and integration measures, higher‑level optimization or governance processes can examine these records to motivate adjustments—tightening constraints, altering role emphasis, or changing orchestrator modes when certain patterns of violations or instabilities are observed.

This creates a cycle in which high‑level state affects behavior, and observed behavior, recorded in introspective and consolidated structures, informs subsequent changes to that state.

## 15.7 Governance and Change Management

Because global settings have wide impact, the repository includes both formal mechanisms and design patterns for governance and change management:

- **Constitutional enforcement and auditing**  
  - The Constitutional Guardian’s `validate` and `get_audit_trail` methods provide a programmatic way to assess requests against enumerated principles and to obtain an integrity‑checked log of decisions, including principle names, descriptions, and specific violation tags.  
  - The Constitutional API and unified gateway expose `/constitutional/audit`, `/constitutional/principles`, and `/constitutional/status`, enabling external tools and governance bodies to inspect constraints and violation histories over HTTP.

- **Administrative audit surfaces**  
  The unified gateway’s `/admin/audit` endpoint reports service counts, log paths, and descriptive fields like “No Blackbox; Consciousness/Biometric/GIS Integrated,” establishing an admin‑facing account of which subsystems are online and how they are composed.

- **Verification and testing scripts**  
  Top‑level scripts such as `VERIFY_AND_TEST.sh`, `verify_full_integration.sh`, and `verify_all_claims.sh` formalize the process of checking microservice health, integration status, and documentation alignment, and can be treated as deployment gates that must pass before changes to modes or global weights are accepted.

These practices support a governance model in which global controls are not altered ad hoc but are mediated by explicit APIs, logs with integrity checks, and repeatable verification procedures.

## 15.8 Summary

The pituitary and global modes layer in Ms. Jarvis is instantiated as a set of concrete services and configurations: a Constitutional Guardian with PII and surveillance constraints and an audit trail; a pituitary emotional‑depth wrapper service; WOAH/DGM analyzers and supervisors that compute and adjust complexity‑related weights; and orchestrators that explicitly encode modes in their responses. Unified gateways and status endpoints surface these elements via descriptive `system_transparency_mode` strings and admin/audit routes, tying low‑level configuration and constraints to high‑level, human‑interpretable modes. Later work on executive control and container design can build directly on this foundation by treating guardian decisions, WOAH weights, DGM modes, and orchestrator health as first‑class inputs to higher‑level routing, scheduling, and policy adaptation.
