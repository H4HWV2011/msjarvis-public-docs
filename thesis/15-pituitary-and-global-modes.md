# 15. Pituitary and Global Modes

This chapter describes the layer that controls global settings and modes across the system. The design borrows the idea of a central regulator that sends signals influencing many subsystems at once. Here this is implemented as configuration state, control services, and policies that together shape how agents, retrieval, and generation behave under different conditions.

## 15.1 Purpose and Scope

Global controls serve several functions:

- Safety and alignment:
  - Define how cautious or exploratory the system should be in different roles and environments.
- Resource management:
  - Limit how much computation and storage can be used for given tasks.
- Role shaping:
  - Adjust which capabilities are available in particular contexts and for particular audiences.

These controls are not one-time configuration files. They are treated as dynamic state that can change over time, subject to governance and audit.

## 15.2 Types of Global Settings

The global layer manages multiple categories of settings, including:

- Safety levels:
  - Thresholds for when to block, rephrase, or escalate answers.
  - Controls on which topics or operations are allowed.
- Role profiles:
  - Bundles of permissions and defaults for different uses such as research, advising, or operational support.
- Performance targets:
  - Limits on latency, concurrency, and memory usage.
  - Preferences for lighter or heavier models under different loads.
- Logging and observability:
  - Levels of detail to capture in logs and introspective records.
  - Selection of which metrics to track in detail.

Each setting has a documented meaning and is stored in a way that can be queried and versioned.

## 15.3 Implementation and Storage

The global control state is typically represented as:

- Structured configuration:
  - A set of key-value pairs or documents held in a database or configuration service.
- Derived flags:
  - In-memory variables or cache entries that services read to make quick decisions.
- Change logs:
  - Records of when a setting was changed, by whom or by what process, and why.

Services that need to obey these controls either read them at startup and on a schedule, or subscribe to updates so they can adapt more quickly.

## 15.4 Influence on Agents and Retrieval

Global settings influence the behavior of agents and retrieval components in several ways:

- Agent selection:
  - Certain profiles may restrict which agents can be invoked, or how many can be combined for a single query.
- Retrieval scope:
  - Filters on which memory collections, belief graph segments, or spatial layers may be used in a given context.
- Depth of reasoning:
  - Limits on the number of steps or the complexity of workflows that can be triggered for lower-privilege roles.

These effects ensure that the same underlying capabilities are used differently depending on the setting of the global mode.

## 15.5 Interaction with Optimization and Self-Improvement

Optimization and self-improving components also pay attention to global controls:

- Exploration bounds:
  - Limits on how radical proposed changes can be without explicit approval.
- Evaluation criteria:
  - Weights on metrics such as accuracy, fairness, resource use, and coverage.
- Deployment gates:
  - Conditions that must be met before a proposed change is applied beyond a sandbox.

By tying these limits to centrally managed state, the system can change how ambitious or conservative it is without modifying code in each agent.

## 15.6 Relationship to Introspection and Memory

Global modes are both informed by and reflected in other layers:

- Introspective records:
  - Each record can include the active mode at the time of an event, allowing later analysis of how behavior differs across settings.
- Consolidated memory:
  - Long-term entries can note which modes were active when key decisions or patterns emerged.
- Feedback loops:
  - Analyses of introspective and consolidated data can motivate mode adjustments, such as tightening safety thresholds or altering role profiles.

This creates a cycle in which high-level state affects behavior, and observed behavior in turn informs changes to that state.

## 15.7 Governance and Change Management

Because global settings have wide impact, changes to them should follow clear procedures:

- Proposal and review:
  - Changes are described, justified, and documented before being applied.
- Testing:
  - New configurations are tried in limited contexts before being rolled out broadly.
- Audit:
  - All changes are logged with timestamps, authorship, and links to any supporting analysis.

These practices help maintain trust that global controls are not altered in ad hoc or opaque ways.

## 15.8 Summary

The global control layer acts as a central regulator for safety, roles, resources, and logging across the system. It provides a way to adjust high-level behavior without directly modifying individual agents or models. Later work on executive control and container design will build on this foundation, using these settings as inputs to higher-level routing and coordination.
