# 35. Swarm Functions and Eternal Watchdogs

This chapter describes two sets of mechanisms that help coordinate many services and maintain continuous oversight. Swarm functions let multiple components work together on problems, while persistent monitoring processes watch for failures, policy violations, and other conditions that require intervention.

## 35.1 Purpose of Swarm and Watchdog Layers

These mechanisms have complementary roles:

- **Coordination**  
  Swarm functions allow multiple agents and services to contribute to a task, each from its own perspective or specialization.

- **Oversight**  
  Watchdogs provide continuous monitoring of key signals, intervening when behavior deviates from expected bounds.

- **Stability**  
  Together, they help keep the system responsive and aligned even as individual components change or fail.

They operate alongside, and partially independent of, the main request–response flows.

---

## 35.2 Swarm Functions and Collective Behavior

Swarm functions organize groups of components into structured collaborations:

- **Task decomposition**  
  Larger questions or objectives are broken into smaller sub-tasks that can be handled by different services or agents.

- **Parallel exploration**  
  Different agents explore alternative approaches or hypotheses in parallel, using varied prompts, tools, or data slices.

- **Aggregation**  
  Results are collected and compared, with combining logic that can highlight consensus, disagreements, and edge cases.

Swarm behavior is guided by the coordinator and constrained by barrier and mode settings to avoid uncontrolled proliferation of work.

---

## 35.3 Use Cases for Swarm Functions

Typical uses include:

- **Complex analyses**  
  When a task involves multiple domains (for example, spatial planning, governance considerations, and technical constraints), different services can contribute domain-specific views.

- **Robustness checks**  
  Multiple agents can independently examine a scenario to see whether they reach similar conclusions, improving confidence in the result.

- **Pattern discovery**  
  Swarms can search for recurring structures or anomalies across large sets of data, with individual agents specializing in different patterns.

These activities make use of the same memory, spatial, and container layers described in earlier parts.

---

## 35.4 Eternal Watchdogs and Continuous Monitoring

Watchdog processes provide ongoing oversight:

- **Health monitoring**  
  Periodic checks confirm that services are reachable, responsive, and behaving within expected resource limits.

- **Policy monitoring**  
  Logs and introspective records are scanned for signs of policy violations, such as repeated near-misses with safety constraints or unusual patterns of requests.

- **Signal monitoring**  
  Core metrics such as error rates, latency distributions, and barrier rejection statistics are tracked over time.

These processes are designed to run continuously or on frequent schedules, independent of individual user sessions.

---

## 35.5 Responses to Watchdog Alerts

When watchdogs detect concerning conditions, they can trigger several kinds of responses:

- **Automatic adjustments**  
  Switch to more restrictive modes, reduce concurrency, or temporarily disable certain routes or capabilities.

- **Escalation**  
  Flag issues for human review, especially when they involve potential harm, policy breaches, or surprising patterns in behavior.

- **Recovery actions**  
  Restart or reconfigure services, clear specific queues, or roll back to known-good configurations where appropriate.

All such actions are recorded in introspective entries for later analysis.

---

## 35.6 Integration with Barrier, Modes, and Containers

Swarm and watchdog mechanisms interact with other layers:

- **Barrier**  
  Watchdogs can tighten or relax barrier thresholds in response to observed trends, such as increased rates of problematic inputs from particular channels.

- **Global modes**  
  Swarm behavior and watchdog responses are constrained by active modes, with more conservative settings limiting the scope of both.

- **Container paths**  
  Events related to swarms and watchdog interventions are written into container and memory layers, becoming part of the system’s history and influencing future decisions.

This integration ensures that coordination and oversight are treated as first-class parts of the architecture.

---

## 35.7 Summary

Swarm functions and eternal watchdogs provide mechanisms for collective problem-solving and continuous oversight. By organizing groups of agents to work together and by maintaining persistent monitoring of health, policy, and risk signals, they help keep the system effective and aligned as it operates and evolves.

---

## Implementation Notes (Reality Alignment)

In the current deployment, the original host-level orchestrator units remain installed but no longer drive behavior. Their responsibilities have been decomposed into dedicated containerized services and standalone Python processes that can be monitored individually.

### Concrete watchdog processes

Several always-on or long-running Python programs act as practical eternal watchdogs alongside the container mesh:

- `ms_jarvis_ram_watchdog.py`  
  Monitors memory usage and related resource conditions on the host, ensuring that heavy workloads (for example, large RAG or LLM runs) do not silently exhaust RAM.

- `sanctuary_construction_monitor.py`  
  Tracks the overall construction and health of the sanctuary environment, including basic checks for missing or misconfigured services and files.

- `ms_jarvis_mother_carrie_protocols.py`  
  Encodes higher-level governance and “spiritual” safeguards, running as a persistent process that can influence how other components are allowed to operate.

- `memory_dgm_engine.py`  
  Runs as a long-lived background process on its own port, maintaining and updating deep generative memory structures; this engine both consumes system state and feeds back patterns that can be used for swarm-style reasoning and optimization.

These watchdogs run directly on the host and are visible in process listings and port/health audits, making their behavior inspectable.

### Swarm functions in practice

Swarm behavior today is primarily realized through:

- The `jarvis-llm-bridge` service, which orchestrates a multi-agent ensemble of models to produce synthesized responses for complex tasks. Multiple reasoning, specialist, and judge agents operate in parallel and their outputs are combined into a single answer.  
- Coordination between `jarvis-web-research`, RAG/Chroma access, and the LLM bridge, where different services contribute web evidence, internal semantic memory, and reasoning passes over the same query.  
- DGM and optimization components that propose variants of prompts, tool calls, or workflows, effectively exploring different “agents” or configurations as part of a small swarm.

These implementations give concrete form to the abstract swarm functions described earlier, using real services and ensembles that can be traced in logs.

### Monitoring and health observation

Watchdog behavior is implemented through a combination of:

- **Host-level watchdogs**  
  The Python processes listed above, which continuously observe aspects of host and system health and can emit logs or trigger safeguards.

- **Service-level health checks**  
  Key containers (main brain, BBB, web-research, RAG, Chroma, Neo4j, MySQL, Ollama, and others) expose health or status endpoints and/or container health checks that are regularly polled.

- **Scripted audits and test harnesses**  
  Shell scripts and automated tests execute standardized checks, including:
  - Container inventories and port scans.  
  - Health requests to core services.  
  - Basic data-plane queries against Chroma and other stores.

Together, these mechanisms turn “swarm functions” into observable multi-service coordination and “eternal watchdogs” into specific long-running processes and health-check routines that can be inspected, tested, and improved over time.
