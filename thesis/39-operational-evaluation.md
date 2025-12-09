# 39. Operational Evaluation of Ms. Jarvis

This chapter outlines how the system’s behavior is evaluated during real operation. It focuses on measurable indicators, case-based studies, and links between observed outcomes and the architectural layers described in earlier parts.

## 39.1 Goals of Operational Evaluation

Operational evaluation serves several goals:

- **Performance**  
  Understand how well the system answers questions, supports decisions, and carries out tasks across different domains and roles.

- **Reliability**  
  Assess how consistently services remain available and responsive, and how they recover from failures or degraded conditions.

- **Alignment**  
  Examine whether behavior remains within the intended safety, governance, and community-oriented boundaries.

These goals guide the choice of metrics and study designs.

## 39.2 Core Metrics and Indicators

Several categories of metrics are tracked or can be reconstructed from logs and traces:

- **Service metrics**  
  - Uptime, latency distributions, and error rates for key services and routes:
    - ULTIMATE API on `8051`.
    - RAG gateway on `8103`.
    - Web-research gateway on `8009`.
    - Autonomous learner on `8053`.  
  - Resource usage (CPU, memory, disk I/O) for containers hosting Ollama, RAG, web-research, and the learner.

- **Interaction metrics**  
  - Patterns in request types (ad hoc questions, spatial/RAG queries, autonomous learning cycles).  
  - Completion rates and typical latencies for end-to-end flows (e.g., question → RAG → LLM → answer).

- **Safeguard and gating metrics**  
  - Counts of failures to reach Chroma via the RAG gateway.  
  - Periods where environment-variable gating disables or throttles the autonomous learner.  
  - Barrier or policy-triggered rejections in outward-facing flows.

These indicators provide a quantitative view of day-to-day operation and highlight where behavior diverges from design expectations.

## 39.3 Empirical Observations from the Live System

Live logs and traces from the December 2025 deployment provide several concrete observations:

- **Autonomous learner cadence and stability**  
  - The optimized learner on `8053` consistently executes cycles on a five-minute cadence, with log entries such as “Cycle complete – Next in 5 minutes” appearing regularly over multi-hour windows.  
  - Under normal conditions, this cadence is stable; deviations (e.g., missing cycles) correlate with upstream failures (RAG or web-research) or deliberate gating.

- **RAG vs. web hit patterns**  
  - For many topics, RAG (`8103 /search`) returns internal results even when web-research (`8009 /search`) returns zero or very few hits, especially for highly local or project-specific content.  
  - Web-research is most useful for broad, general topics or current events; for tightly local or Ms. Jarvis–specific topics, internal RAG dominates.  
  - The learner logs both counts, making it possible to estimate per-topic RAG/web hit rates and to detect topics that should be reframed or rescheduled.

- **Chroma connection architecture**  
  - All live Chroma access is mediated via the RAG gateway on port `8103`; the older direct client pattern (for example, assuming a Chroma server on `8002`) is no longer used in active services.  
  - When Chroma is unavailable (e.g., at startup or during maintenance), the autonomous learner logs connection failures, skips semantic writes, and continues its cycle using whatever information is available, then recovers cleanly once RAG/Chroma return.

- **Behavior under real workloads**  
  - Under moderate load, ULTIMATE and the learner coexist without noticeable interference: RAG and web-research calls complete within acceptable latencies, and LLM inference remains responsive.  
  - Heavy operations (e.g., large RAG queries or extended LLM calls) can temporarily increase cycle times, but timeouts and the fixed five-minute cadence prevent unbounded drift.  
  - When upstream services are down (web, RAG, or Ollama), the learner and ULTIMATE surface clear error messages and avoid partial writes, preserving consistency of stored memory.

These observations anchor the evaluation in actual behavior rather than purely theoretical expectations.

### Case F‑2025‑Legacy‑Orchestrators

On 2025‑11‑28 at approximately 10:10 EST, two historical orchestrator units, `jarvis-qualia-coordinator.service` and `msjarvis.service`, failed to start under systemd on the primary host. Systemd recorded repeated start attempts followed by failure for both units, while the newer port-scoped services (such as the RAG gateway, web-research, and the autonomous learner) continued to define live behavior.

This incident confirmed that the legacy orchestrators were no longer part of the operational control path and should be treated explicitly in the documentation as retired scaffolding. As a result, the thesis and architecture roadmap mark these units as disabled, describe their former responsibilities as decomposed across dedicated services, and emphasize that monitoring and evaluation now target the newer mesh rather than the historical multi-consciousness service.

## 39.4 Links to Architectural Layers

Evaluation draws on information from multiple layers:

- **Introspective and learner logs**  
  - Provide detailed traces of cycles, topic selections, RAG and web hit counts, and success/failure outcomes.

- **Semantic memory and Chroma via RAG**  
  - Show which collections are receiving new items from autonomous learning and how often, including the balance between internal RAG-derived content and web-derived content.

- **Safeguard and watchdog mechanisms**  
  - Record when environment-based gating is used to pause the learner, when external services are unreachable, and when the system falls back to degraded modes.

This multi-layer view supports richer explanations of successes and failures and ties them back to specific architectural choices (such as centralizing Chroma access through RAG).

## 39.5 Continuous Improvement Loops

Operational evaluation is tied back into improvement processes:

- **Threshold and timeout tuning**  
  - Metrics and case findings motivate adjustments to timeouts for RAG, web, and LLM calls, as well as thresholds for semantic deduplication and daily learning limits.

- **Workflow and routing updates**  
  - Observed weaknesses (for example, topics that consistently produce zero web hits or repeated Chroma failures at startup) lead to revised topic selection heuristics, better error handling, or updated startup ordering.

- **Documentation and communication**  
  - Findings are summarized in records that feed into governance discussions, provide context for collaborators (e.g., university partners), and guide future design choices.

These loops connect evaluation to ongoing refinement rather than treating it as a one-time exercise.

## 39.6 Summary

Operational evaluation combines metrics, case studies, and architectural traces to build a picture of how the system behaves in practice. Empirical observations from the live deployment—such as the five-minute learner cadence, RAG versus web hit patterns, centralized Chroma access via the RAG gateway, and behavior under real workloads—ground the evaluation in reality. By linking these observations to specific layers and mechanisms, the system gains a foundation for informed adjustments and for broader discussions about performance, reliability, and alignment.
