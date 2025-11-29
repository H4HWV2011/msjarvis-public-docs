# 31. Fractal Optimization and the 69 DGM Connectors

This chapter describes the layer of self-improving components that sit between services and propose changes to how they operate. These components are based on the Darwin–Gödel Machine concept introduced earlier, but here they are deployed as many small, attached optimizers that together form a fractal pattern across the architecture.

## 31.1 Role of Per-Service Optimizers

Each optimizer is attached to a specific service or narrow cluster of services:

- Local focus:
  - Rather than trying to redesign the entire system at once, each unit concentrates on improving one part of the workflow, such as a router, a retrieval pattern, or a particular analysis job.
- Connector function:
  - By learning better ways to pass information between its attached service and neighboring components, each unit acts as a connector that can refine flows across boundaries.
  - Examples include optimizers attached to retrieval routes, live-cycle jobs, and integration routines such as the cooperative and web platform connectors described in the preceding chapter.
- Archive of variants:
  - Over time, each optimizer builds up a small collection of candidate configurations or workflows for its area, along with basic performance information.

This distributed arrangement allows many parts of the system to be explored in parallel.

## 31.2 Three-Stage Improvement Cycle

Each optimizer follows a recurring three-stage cycle:

- Observation:
  - Collect traces of how its attached service has been performing, including inputs, outputs, timings, and evaluator scores.
- Proposal:
  - Generate candidate changes to configuration, prompting, tool use, or workflow structure, based on observed patterns and a library of known modification strategies.
- Evaluation:
  - Test the proposed changes on suitable tasks or replayed examples, measuring effects on accuracy, resource use, and any relevant safety or alignment scores.

The cycle repeats over time, aiming to produce small, well-understood improvements rather than large, opaque changes.

## 31.3 Metrics and Constraints

Improvement proposals are evaluated against a set of metrics and constraints:

- Performance metrics:
  - Task-specific measures such as correctness, coverage, or latency.
- Stability metrics:
  - Indicators of variance or brittleness across similar inputs, helping to avoid improvements that only work in narrow cases.
- Safety metrics:
  - Scores from judge components that look for policy violations, risky language, or undesirable side effects.

A proposal is only considered for adoption if it improves relevant performance metrics without degrading stability or safety beyond allowed bounds.

## 31.4 Relationship to Fractal Structure

The collection of optimizers has a fractal character:

- Repetition across scales:
  - Similar three-stage cycles operate at many points in the system, from small routing tweaks to higher-level workflow adjustments.
- Nested influence:
  - Changes in one area can prompt further adjustments in neighboring areas, creating patterns of refinement that recur at different levels of abstraction.
- Diversity of variants:
  - Over time, each optimizer maintains an internal archive of candidate configurations, some of which may be less effective locally but useful as stepping stones for later changes.

This arrangement supports open-ended exploration while keeping each step bounded and interpretable.

## 31.5 Integration with Containers and Memory

Outputs from the optimizers are integrated through existing structures:

- Container paths:
  - Proposed changes and their evaluation results are recorded as events that pass through intake and background stages, where they can be grouped, rated, and, when appropriate, promoted.
- Long-term memory:
  - Stable improvements, such as better prompting patterns or more effective routing rules, can be written into semantic memory and belief structures as design knowledge.
- Introspective records:
  - Each cycle writes entries describing what was tried, how it was evaluated, and whether it was adopted, supporting later audit.

This ensures that self-improvement attempts are treated as part of the system’s history rather than as hidden side effects.

## 31.6 Interaction with Global Control and Barrier

Higher-level controls shape how and when optimizers can act:

- Mode dependency:
  - In more conservative modes, optimizers may be limited to proposing changes for offline evaluation or to narrow slices of functionality.
- Barrier checks:
  - Proposals that would alter how external sources are used or how outputs reach outside systems must pass through the same safeguard layer as other infrastructure-related actions.
- Coordination:
  - The central coordinating component can schedule optimization cycles, prioritize certain services, or temporarily suspend particular units when needed.

These mechanisms keep self-improvement aligned with broader goals and constraints.

## 31.7 Summary

The fractal optimization layer consists of many small, service-attached Darwin–Gödel-style components that observe behavior, propose changes, and evaluate their effects. By distributing this process across a network of connectors and tying it into container, memory, and control structures, the system can explore improvements in a structured, traceable way rather than through monolithic updates.
