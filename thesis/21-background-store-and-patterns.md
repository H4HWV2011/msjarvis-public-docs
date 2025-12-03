# 21. Background Store and Ongoing Review

This chapter describes the second stage in the container paths, where items that passed the initial filter are held for longer periods and revisited over time. The aim is to move from one-off decisions toward recognition of stable patterns, without yet committing material to the most selective layer.

## 19.1 Purpose of the Background Store

The background store serves several roles:

- Retention:
  - Hold items that were judged potentially important but not yet central.
- Aggregation:
  - Group related items so that recurring themes become visible.
- Preparation:
  - Provide a pool of candidates from which identity-level entries and long-term memory updates can be drawn.

It acts as an intermediate space between fast filtering and deep storage.

## 19.2 Structure of Stored Items

Items in this store build on the records produced by earlier stages, with added fields for longer-term management:

- Grouping identifiers:
  - Keys that tie related items together, such as shared topics, locations, or entities.
- Counters and scores:
  - Simple metrics tracking how often similar items appear and how they have been evaluated.
- Aging information:
  - Timestamps and derived measures indicating how long items have been present and how recently they were updated.
- Links to later decisions:
  - Pointers to any downstream entries that have been created based on a given background item.

This structure allows the system to treat the store as both a set of individual records and a collection of evolving clusters.

## 19.3 Ingestion from the First Stage

When an item is accepted by the first-stage filter, it enters the background store with initial values:

- Its core fields are copied or referenced.
- Grouping keys are computed from tags, entities, and other metadata.
- Counters are initialized, and age begins from the time of entry.
- An initial status is set, indicating that the item has not yet been promoted or discarded.

At this point, the item is eligible for later review but does not yet change long-term structures.

## 19.4 Periodic Review Processes

The store is revisited by periodic processes that:

- Scan:
  - Select items or groups based on age, frequency, or other criteria.
- Update:
  - Adjust counters and scores in light of new related items.
- Classify:
  - Mark groups as emerging patterns, stable themes, or fading topics.

These review jobs can run on schedules tuned to available resources and desired responsiveness.

## 19.5 Pattern Detection

As more items accumulate, the system can detect patterns such as:

- Repeated questions about particular places, institutions, or issues.
- Recurring combinations of roles, topics, and outcomes.
- Clusters of events that tend to trigger specific constraints or evaluations.

Simple techniques such as counting, bucketing, and lightweight clustering can be used here without requiring heavy-weight analysis.

## 19.6 Promotion and Deletion Decisions

Based on observed patterns, the background store supports two main decisions:

- Promotion:
  - Select items or aggregates that should influence deeper layers, such as identity-focused storage or long-term memory.
- Deletion or compression:
  - Remove or further summarize items that no longer contribute useful information.

Criteria for promotion can include stability of a pattern, breadth of impact, and alignment with stated goals. Criteria for deletion can include redundancy, age without further reference, and clear lack of relevance.

## 19.7 Interaction with Parallel Paths

Both parallel paths maintain their own background stores, which may apply different thresholds and groupings:

- Meaning-oriented path:
  - May focus on themes related to community experience, emotional tone, or recurring narratives.
- Analytical path:
  - May emphasize technical topics, procedural issues, or repeated data structures.

Despite these differences, both stores produce similarly structured outputs so that later layers can combine information across paths when needed.

## 19.8 Links to Other Layers

The background store connects to other parts of the system in several ways:

- Introspective layer:
  - Summaries of emerging and stable patterns can be written into introspective records, providing context for current behavior.
- Consolidation layer:
  - Promotion decisions can trigger updates to vector collections in ChromaDB, belief structures in the GBIM graph, and spatial links in the PostGIS-backed geodatabase, which are then available to the retrieval pipeline.
- Global control:
  - Observed patterns can inform adjustments to settings, such as emphasis on particular regions, topics, or roles.

Through these links, what accumulates quietly in the background can, over time, influence both specific decisions and overall behavior.

## 19.9 Summary

The background store provides a place where items that have passed initial screening can accumulate, interact, and be revisited. It allows the system to recognize patterns and decide which material is worth elevating to more central storage, while keeping the process structured and inspectable. Later chapters build on this foundation to describe how the most selective layer is defined and how the two parallel paths differ in what they ultimately retain.
