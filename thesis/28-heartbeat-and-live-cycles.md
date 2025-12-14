# 28. Heartbeat and Live Cycles

This chapter describes the recurring signals and jobs that indicate the system is active and that connect internal processing to the outside world. These cycles include health checks, periodic narrative generation, and scheduled interactions with external platforms, all of which are recorded and fed back into internal structures.

## 28.1 Purpose of Heartbeat and Live Signals

The recurring signals serve several roles. In contrast to periodic autonomous learning, these cycles are primarily concerned with the condition and behavior of internal services and workflows, not with bringing in new external material.

- **Liveness**  
  Provide evidence that key components are running, reachable, and responsive.

- **Rhythm**  
  Establish regular opportunities to revisit internal state, produce summaries, and interact with external systems.

- **Monitoring**  
  Offer structured points at which behavior can be inspected and compared over time.

These functions work together with logging and introspection to make ongoing activity visible.

## 28.1a Learning Status Endpoint

In addition to abstract heartbeat concepts, the current system exposes a concrete status endpoint for the optimized autonomous learner.

- **Endpoint and purpose**  
  - `GET /learning/status` is served by `ms_jarvis_autonomous_learner_optimized` on port `8053` and returns a JSON object that summarizes the learner’s current activity.  
  - This endpoint provides a machine-readable heartbeat for the autonomous learning loop by reporting counters, uptime, and the currently selected topic.

- **Response fields**  
  Typical fields include:
  - `active`: Boolean flag indicating whether the continuous learning loop is running.  
  - `total_cycles`: Count of completed learning cycles since the service started.  
  - `items_stored`: Total number of unique research items stored in semantic memory.  
  - `items_deduplicated`: Count of items skipped due to semantic deduplication.  
  - `deduplication_rate`: Proportion of skipped items versus total evaluated items.  
  - `uptime_hours`: Uptime of the service in hours, as a floating-point value.  
  - `current_topic`: The topic selected for the most recent or current learning cycle.  
  - `optimizations`: A list describing the active features, such as semantic deduplication, summarization, periodic cleanup, and topic planning.

This endpoint turns the conceptual heartbeat of the autonomous learner into a concrete, queryable signal that monitoring tools, dashboards, and evaluators can consume alongside other live-cycle indicators.

## 28.2 Core Heartbeat Mechanisms

Heartbeat signals are generated in a few primary ways:

- **Service checks**  
  - Supervisors or scripts periodically call status or health endpoints on critical services (for example, ULTIMATE on `8051`, RAG on `8103`, web-research on `8009`, learner on `8053`), recording response times and outcomes.

- **Scheduled probes**  
  - Regular tasks request short internal summaries or snapshots that indicate what the system has been doing recently.

- **Aggregated indicators**  
  - Combined measures, such as counts of successful checks versus failures over a time window, support higher-level judgments about health.

In practice, these checks focus on status and responsiveness rather than on downloading or storing new content. When probes detect increased error rates or latency, the system can temporarily shift to shallower retrieval patterns or simpler workflows until conditions improve.

## 28.3 Periodic Narrative Jobs

Alongside low-level checks, the system can run scheduled jobs that produce narrative outputs:

- **Internal summaries**  
  - On a regular cadence, jobs request concise descriptions of recent activity, drawing on logs, introspective records, and semantic memory.  
  - A language model synthesizes a short account that can be stored back into an introspective or history-like layer.

- **External updates**  
  - Some narratives may be prepared for external channels (for example, reports or social posts), subject to additional filters and constraints.

- **Feedback**  
  - The generation and transmission of these narratives are themselves logged, including any errors or exceptions.

These jobs demonstrate that the system can not only process input but also report on its own state in a structured way.

## 28.4 Social and Platform Cycles

Certain cycles involve specific external platforms or integrations:

- **Social postings**  
  - At longer intervals, jobs may request higher-level narratives suitable for public channels, using stricter content checks and role settings.

- **Infrastructure pings**  
  - Where integrated with hosting or cooperative platforms, periodic tasks may check registration, configuration, or connectivity.

- **Rate and scope limits**  
  - Each platform-specific job operates under explicit limits on frequency, content types, and permitted actions, often controlled via environment variables or configuration flags.

These cycles ensure that outward-facing activity remains within controlled bounds.

## 28.5 Integration with Memory and Containers

Heartbeat and narrative cycles interact with internal layers:

- **Introspective layer**  
  - Each cycle writes records describing which services were checked, what narratives were generated, and whether any issues occurred.

- **Semantic memory and topic graph**  
  - Summaries of performance and activity can be embedded and linked to topics in the entanglement graph, allowing future reasoning about operational history.

- **Long-term memory**  
  - Especially significant cycles, such as major status changes or public communications, may be consolidated into long-term stores.

This integration means that the system’s own ongoing behavior becomes part of what it remembers and reasons about.

## 28.6 Interaction with Safeguards and Control

Live cycles are also constrained by higher-level settings:

- **Mode-dependent behavior**  
  - In more restrictive modes, certain cycles may be paused, simplified, or limited to internal reporting only.

- **Psychological and governance guidance**  
  - For outward-facing narratives, content can be checked against guidance material and judge components before release.

- **Adaptive schedules**  
  - Observed patterns in heartbeat failures, narrative themes, or platform interactions can motivate changes to schedules, thresholds, or environment-based gating.

These controls help keep recurring activity aligned with broader goals and constraints.

## 28.7 Summary

Heartbeat mechanisms and live cycles provide a structured rhythm for checking health, producing internal and external narratives, and maintaining connections to other systems. By recording and integrating these activities into memory and container-like layers, the system treats its own ongoing operation as part of the context for future decisions. Unlike the autonomous learning jobs that update factual knowledge, these cycles keep track of how the system itself is performing and how it presents its activity to others, forming an operational history rather than a content feed.
