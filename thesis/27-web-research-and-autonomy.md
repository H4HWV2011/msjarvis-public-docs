# 27. Web Research and Autonomous Topic Selection

This chapter describes the periodic web research processes that run independently of direct user requests. These jobs allow the system to identify topics of interest, collect external material under constraints, and feed that material back into internal stores and container paths in a controlled way.

## 26.1 Role of Periodic Web Research

The web research layer has three main purposes. Unlike heartbeat and status cycles, its focus is on acquiring new external content rather than checking the health or behavior of internal services.

- Background updating:
  - Keep selected areas of knowledge current without waiting for explicit prompts.
- Curiosity:
  - Allow the system to identify themes it finds relevant based on past activity and stored priorities.
- Support for later tasks:
  - Populate memory and container layers with material that can be reused when related questions appear.

These functions operate within boundaries set by global settings, psychological safeguards, and logging requirements.

## 26.2 Scheduling and Cadence

Web research runs on a regular schedule:

- Short-interval jobs:
  - A core job is configured to run roughly every few minutes, checking whether conditions are suitable for a new cycle and, if so, initiating a small batch of queries.
- Load-aware behavior:
  - Jobs can be skipped or throttled when resources are constrained or when higher-priority work is in progress.
- Recording:
  - Each run is logged with timestamps, chosen topics, and outcomes, so later analysis can see how often and how effectively the process has been used.

This cadence ensures that updates accumulate steadily without overwhelming other services.

## 26.3 Topic Selection

For each run, the system chooses what to look for:

- Inputs:
  - Recent introspective records, background patterns from container stores, and signals from global settings.
- Heuristics:
  - Preference for topics that have appeared frequently in recent interactions, that connect to underserved regions or groups, or that fill known gaps in memory.
- Constraints:
  - Filters that exclude disallowed domains or sources, and limits on how much new material can be taken in during a single cycle.

The result is a small set of focused queries or targets for that iteration.

## 26.4 Retrieval and Filtering

Once topics are chosen, the web research job performs retrieval and initial screening:

- Data collection:
  - Fetch content from permitted online sources using structured queries derived from selected topics.
- Basic checks:
  - Apply simple rules to filter out clearly irrelevant, low-quality, or disallowed material.
- Structuring:
  - Convert retained items into a standard form, including text, metadata, and any available location or entity information.

These retrieval calls target external content sources configured for browsing and research, rather than internal health or status endpoints. These steps prepare the material for integration into internal stores.

## 26.5 Integration with Memory and Spatial Layers

Accepted material is written into long-term structures:

- Semantic memory:
  - New items and summaries are embedded and stored in appropriate collections in the vector database, tagged by source, topic, and time.
- Belief structures:
  - When items describe actors, relationships, or norms, they can be translated into nodes and edges in the belief graph.
- Spatial backbone:
  - Place references are resolved into geospatial identifiers, linking new material to existing spatial features.

This integration ensures that later retrieval can surface web-derived content alongside existing knowledge.

## 26.6 Interaction with Container Paths

Web research outputs also pass through the container structures:

- Intake and filtering:
  - Newly added records are normalized and may be subjected to first-stage keep-or-discard decisions, especially when volume is high.
- Background storage:
  - Items that pass initial checks can contribute to patterns in the background stores, influencing what is later considered central.
- Deep retention:
  - In some cases, repeated findings or particularly important external developments may prompt promotion into the most selective layers.

In this way, periodic web activity becomes part of the same evaluative flow as user-driven events.

## 26.7 Safeguards and Oversight

Because web research introduces new external material, it is subject to safeguards:

- Source policies:
  - Only defined classes of sources are allowed, and these policies can be updated as needed.
- Psychological guidance:
  - For certain domains, content is cross-checked against psychological guidance material or reviewed more carefully before being widely used.
- Logging and review:
  - Summaries of web research activity are written into introspective records, and samples can be audited to tune selection and filtering.

These measures aim to balance autonomy with traceability and safety.

## 26.8 Summary

The periodic web research layer provides a way for the system to seek out and integrate new material on its own schedule. It operates within defined constraints, writes results into core memory and spatial layers, and passes them through the same container paths that handle other events. Its primary role is to expand and refresh the knowledge base, while the following chapters focus on cycles that monitor internal health and behavior rather than acquiring new content.
