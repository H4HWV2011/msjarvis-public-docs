# 20. First-Stage Evaluation and Immediate Filtering

This chapter describes the first evaluation stage applied to incoming records after they have been routed into the container paths. In the implemented system, this stage is realized by a combination of fast safety checks, background storage for semantic memory, truth-validation modules, and basic structural heuristics. Its purpose is to make fast, inexpensive decisions about which items warrant any further attention and which can be safely ignored, while preserving enough information to justify those decisions later.

## 20.1 Objectives of the First Stage

The first stage is designed to satisfy three practical objectives:

- **Reduce volume**  
  Quickly discard or downgrade low-value items so that later stages—such as deeper RAG integration, graph updates, or I-Container growth—are not overwhelmed. Although the current February 15, 2026 deployment does not deduplicate Chroma background entries, it does centralize routing so that downstream services can choose whether to reuse or ignore repeated content.

- **Preserve opportunity**  
  Forward items that may matter later, even if their importance is not fully known at the time. For example, user conversations that pass safety checks are queued for RAG-related background handling and are written into the `ms_jarvis_memory` semantic store, where they can later contribute to autonomous learning, clustering, or case-study analysis.

- **Respect constraints**  
  Apply basic policy and safety checks before anything is treated as trusted. The blood–brain barrier (BBB) and truth-validation modules act as early gates that can veto or annotate content before it is allowed to influence memory or downstream reasoning.

The focus is on simple, explainable decisions rather than detailed analysis, so that this stage can run on every incoming record without introducing substantial latency.

## 20.2 Inputs from the Routing Layer

The inputs to this stage are normalized records produced by the routing and container layers. For user-facing interactions, the main-brain coordinator provides:

- Structured request objects (including message, `userid`, and flags such as `useallservices`).
- A snapshot of services that were considered healthy at the time of the request.
- Intermediate signals such as BBB filtering outcomes, ensemble LLM results, and web-research context.

For internal tasks, the container architecture supplies:

- Candidate knowledge entries from the autonomous learner and Fifth DGM (where active).
- Metrics, analysis results, and diagnostics from verification scripts and monitoring services.

In both cases, the first-stage evaluator sees structured objects rather than raw logs. Records typically include:

- Identifiers, timestamps, role and domain tags, and content summaries.
- Links (or references) to underlying memory, graph, or spatial elements.
- Track assignments and coarse priorities determined by the routing layer.

This structure allows first-stage logic to operate without revisiting raw trace data, except when discrepancies are later investigated.

## 20.3 Basic Keep-or-Discard Decision

For each record, the first-stage logic answers a simple question: should this item be kept for further consideration, or dropped here?

In the running system, this decision appears most concretely in two places:

- The background storage pipeline, where a background task (often named `background_rag_store` in the code) prepares material for the legacy RAG server and writes interactions into the shared Chroma collection `ms_jarvis_memory`.
- The truth and safety filters (for example, BBB and identity truth validators), which can mark a record as disallowed or questionable and thereby prevent it from being treated as ground truth.

The keep-or-discard decision is based on criteria such as:

- **Relevance**  
  Whether the record touches on topics, locations, or entities that are in scope for the active role and current global settings. Records that fail safety checks or fall completely outside the system’s intended domain may be dropped or treated as low priority.

- **Novelty (designed intent vs. current behavior)**  
  The intended design includes lightweight similarity checks against existing semantic memory or RAG indexes, so that near-duplicate interactions that add no new information can be downgraded. In the February 15, 2026 reference deployment, repeated test messages are still written as separate entries in `ms_jarvis_memory`, so novelty primarily affects how downstream tools interpret and reuse them, rather than preventing the background write.

- **Quality**  
  Whether the record passes basic checks on completeness and internal consistency. For chat-based records, this includes ensuring both query and response are non-empty, well-formed, and free from gross formatting errors.

If the answer is negative, the record may be marked as discarded or low-value at this stage and is not passed to deeper, trusted stores such as identity specifications or curated graph layers. Minimal metadata about the decision (for example, a reason code and timestamp) can still be recorded for audit and analysis.

## 20.4 Signals Used in Evaluation

To support these decisions, the first-stage evaluator draws on several fast, inexpensive signals:

- **Tag and keyword matches**  
  Domain tags, role indicators, and key phrases are compared against allow-lists and deny-lists associated with the current track (meaning-oriented vs. analytical) and global settings. Certain classes of unsafe content may trigger immediate rejection or require BBB/ethics modules to run before any storage occurs.

- **Lightweight similarity and reuse checks**  
  Before writing new material into some semantic stores, the pipeline can perform small similarity lookups (for example, limited `/search` calls to the legacy RAG server) and examine the score of the closest matches. In the present deployment, these checks influence legacy RAG storage behavior and downstream reuse, while the Chroma background store `ms_jarvis_memory` remains append-only, preserving each interaction with its own timestamp and metadata.

- **Structural heuristics**  
  Simple checks ensure that required fields are present and that basic size limits and format constraints are respected (for example, maximum text length for background entries, presence of user identifiers, or minimum content length to avoid trivial noise).

Because these signals are computationally cheap, they can be applied to every record that enters the container paths, providing broad coverage without excessive overhead.

## 20.5 Outcomes and Annotations

Each processed record is assigned an outcome label and supporting annotations to make first-stage behavior explicit. Typical outcomes include:

- **Kept for deeper storage or background memory**  
  The record is deemed relevant and structurally sound. For chat interactions in the current system, this means the user message and model response are queued for background handling and written into the `ms_jarvis_memory` Chroma collection as a `background` item with associated metadata. For internal tasks, it may be scheduled for insertion into the I-Container, graph database, or relational store where the corresponding APIs are active.

- **Discarded or down-ranked as low value or redundant**  
  The record is similar to previously stored items, falls outside the intended domain, fails safety checks, or lacks meaningful content. In some cases, this leads to an explicit discard; in others, the record remains in background memory but is not promoted into trusted identity or graph layers.

- **Deferred or flagged**  
  Some records may be tagged for special handling—for example, those that trigger unusual truth-validator patterns, relate to sensitive identity topics, or indicate potential configuration problems. These can be routed to diagnostic tools or human review rather than being immediately stored or discarded.

Associated annotations often include:

- **Reason codes**  
  Short machine-readable codes or flags such as `OUT_OF_SCOPE`, `SAFETY_DENIED`, `MINIMAL_CONTENT`, or notes in the `truthverdict`, indicating why a given path was taken.

- **Confidence estimates**  
  Simple scores or categories (for example, `high`, `medium`, `low`) reflecting the strength of the decision, which can guide later tuning or review.

These annotations allow later stages, monitoring tools, and researchers to understand how and why the first-stage filter behaved as it did.

## 20.6 Interaction with Parallel Paths

Although both parallel paths share the same overall structure, their first-stage evaluators can differ in their criteria and thresholds:

- **Meaning-focused path**  
  This path may be more sensitive to affective or narrative content and more inclined to keep items that touch on themes of care, loss, identity, or community. For example, a short narrative about community resilience might be retained even if it is not technically dense, because it contributes to the system’s understanding of lived experience. Such items are written into background memory and may later be referenced by psychological or community-context modules.

- **Analytical path**  
  This path may prioritize items with clear technical content, structured data, or explicit problem statements. Records that contain precise metrics, spatial features, or well-defined optimization targets are more likely to be highlighted for analytical reuse, while vague or purely emotional content may be filtered out at this level (even if it remains in background memory for the meaning-oriented path).

The intake layer’s track assignment determines which evaluator runs for a given record, but both evaluators attach outcomes, reason codes, and any relevant confidence indicators in a comparable format. This makes it possible to compare behavior across paths and to adjust their respective criteria over time.

## 20.7 Recording First-Stage Decisions

Even when records are down-ranked or effectively discarded, the system can record information about first-stage decisions at multiple levels:

- **Aggregated statistics**  
  Counts and rates of kept versus discarded items can be tracked by role, track (meaning-focused vs. analytical), time period, and source (user chat vs. internal task). These statistics support monitoring of load, safety behavior, and possible bias.

- **Sampled examples**  
  A small sample of records that were not promoted into trusted layers can be retained (with appropriate privacy controls) for periodic quality checks and tuning. This allows developers and researchers to inspect borderline cases, refine similarity thresholds, or adjust allow/deny lists.

- **Introspective summaries**  
  Higher-level summaries of first-stage behavior can be written into introspective records or verification reports. For example, verification scripts can report how many items were written into `ms_jarvis_memory` during a test run, how often the `truthverdict` flagged issues, or how many background tasks were queued without error.

Recording these decisions, even in compressed form, helps guard against systematic errors and provides a basis for empirical evaluation of the first-stage filters.

## 20.8 Relationship to Truth and Safety Filters

First-stage evaluation is closely linked to truth and safety mechanisms, which operate as specialized filters:

- **Blood–brain barrier (BBB)**  
  The BBB acts as a pre-filter for many user-facing interactions, blocking or transforming content that violates ethical or safety constraints before it can reach deeper storage or influence reasoning. Its verdicts (including `valid` flags, confidence scores, and principal reasons) effectively dominate the keep-or-discard outcome for certain classes of input.

- **Truth validators**  
  Dedicated truth-validation modules check for hallucination patterns, identity confusion, and known factual constraints (for example, the correct persona, the correct creator identity, and prohibited forms of self-description). When these modules detect violations, they can downgrade confidence, annotate the record with issues, or prevent it from being treated as trusted knowledge, even if the background record remains in `ms_jarvis_memory`.

In practice, these filters can be viewed as domain-specific first-stage evaluators layered on top of the more generic structural and similarity-based checks described earlier. Together, they define the minimum bar that content must clear before it can become part of central, trusted memory or influence downstream processes.

## 20.9 Operational Validation

Operational validation of the first-stage evaluation focuses on two aspects:

- **Correctness of basic behavior**  
  Integration tests using the main-brain `/chat` endpoint confirm that requests are accepted, processed through the BBB and routing logic, and, when appropriate, scheduled for background handling without errors. Empirical tests on February 15, 2026 show that each `/chat` call:
  - Produces a full `UltimateResponse` (including `truthverdict` and `servicesused`).
  - Queues a background task, as indicated by log entries such as `rag-store-queued`.
  - Results in a new `background` entry in `ms_jarvis_memory` with a timestamped `bg_<ISO8601>` identifier and appropriate metadata.

- **Effectiveness and behavior under realistic use**  
  Manual verification runs demonstrate that:
  - Repeated, identical messages result in multiple background entries that cluster closely in embedding space but retain distinct timestamps and response variants.
  - Truth and safety filters are invoked consistently, with `truthverdict` fields reflecting ethics and identity assessments even for technical test messages.
  - The curator endpoint `/curator/background` provides a stable, auditable view of what has been retained at this stage, enabling researchers to inspect both nominal and edge-case behaviors.

These operational checks do not exhaustively prove correctness but provide concrete evidence of how the first-stage evaluation behaves in a live deployment as of mid-February 2026, and where its behavior diverges slightly from the earlier, more aggressively de-duplicating design.

## 20.10 Summary

The first-stage evaluation and immediate filtering layer serves as the system’s initial line of defense against overload, redundancy, and unsafe content. It operates on normalized records produced by routing and container structures, applying fast, explainable criteria based on relevance, novelty signals, structural quality, and domain-specific safety and truth rules. Outcomes are recorded with reason codes and confidence indicators, enabling later diagnostics and academic analysis.

In the current deployment, background memory in the `ms_jarvis_memory` Chroma collection is append-only for user interactions, ensuring that even repeated tests are preserved with their own timestamps and metadata. Lightweight similarity and RAG-related checks influence how content is reused and interpreted downstream, while truth and safety filters determine what can be treated as trusted. Subsequent chapters build on this foundation to describe how retained items are integrated into deeper storage layers, how patterns over time are identified, and how the system’s behavior evolves as its memories and models change.
