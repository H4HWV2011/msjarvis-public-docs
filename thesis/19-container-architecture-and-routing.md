# 17. Container Architecture and Routing

This chapter describes the high-level layout of the structures that receive activity from earlier layers and route it into deeper evaluation paths. The goal is to separate the flow of events into clear stages, so that each stage has a well-defined role in deciding what is ignored, what is kept for background consideration, and what becomes part of a more central store.

## 17.1 Position in the Overall System

The container layer sits above retrieval, optimization, and global control and below external interfaces and scheduling. Its main responsibilities are to:

- Accept events coming from many sources, including question-handling flows, scheduled jobs, and self-improving processes.
- Normalize these events into a common format that can be evaluated in a consistent way.
- Dispatch normalized items into successive evaluation stages, while obeying system-wide constraints.

Earlier parts of the work have described how information is retrieved, evaluated, and stored. This part focuses on how those elements are wrapped in container structures that manage their entry into higher-level evaluative paths.

## 17.2 Types of Incoming Events

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

## 17.3 Normalization into Container Records

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

## 17.4 First-Level Routing Decisions

Once a record is normalized, the intake layer applies initial routing logic:

- Eligibility checks:
  - Confirm that the record is allowed to enter the container paths under current global settings.
- Priority assignment:
  - Assign a simple priority level that will influence ordering and resource allocation.
- Track assignment:
  - Decide whether the record should be sent to one or both of the parallel paths that follow.

At this stage, routing focuses on structural compatibility and basic policy, leaving more detailed judgments to later chapters.

## 17.5 Parallel Paths

The architecture uses two parallel paths that share the same structural pattern:

- One path emphasizes questions of meaning, care, and affect, and is used when events are framed in those terms.
- The other path emphasizes general analysis and technical reasoning, and is used for more conventional problem-solving tasks.

The intake layer decides, based on metadata and simple classifiers, whether a record is best handled by one path, the other, or both. Each path then applies its own evaluation criteria while maintaining the same overall sequence of stages.

## 17.6 Outputs of the Routing Layer

After routing, the main outputs are:

- Records marked for immediate evaluation in the next stage.
- Records held back or dropped according to policy.
- Logs and introspective entries describing which path was chosen and why.

These outputs ensure that downstream stages receive appropriately prepared inputs and that the choices made at the routing step can be examined later if needed.

## 17.7 Summary

The container architecture described here provides a structured way to receive, normalize, and route events into deeper evaluative paths. It establishes the context in which later chapters will describe how items are filtered, retained, and woven into longer-term structures in each parallel path.
