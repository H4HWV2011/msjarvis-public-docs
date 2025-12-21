# 20. First-Stage Evaluation and Immediate Filtering

This chapter describes the first evaluation stage applied to incoming records after they have been routed into the container paths. In the implemented system, this stage is realized by a combination of fast safety checks, RAG de-duplication, truth-validation modules, and basic structural heuristics. Its purpose is to make fast, inexpensive decisions about which items warrant any further attention and which can be safely ignored, while preserving enough information to justify those decisions later.

## 20.1 Objectives of the First Stage

The first stage is designed to satisfy three practical objectives:

- **Reduce volume**  
  Quickly discard low-value or redundant items so that later stages—such as deeper RAG integration, graph updates, or I-Container growth—are not overwhelmed. This includes preventing repeated storage of near-identical query–response pairs.

- **Preserve opportunity**  
  Forward items that may matter later, even if their importance is not fully known at the time. For example, user conversations that pass safety checks and appear novel are queued for RAG storage and may later contribute to autonomous learning or case-study analysis.

- **Respect constraints**  
  Apply basic policy and safety checks before anything is stored more deeply. The blood–brain barrier (BBB) and truth-validation modules act as early gates that can veto or annotate content before it is allowed to influence memory or downstream reasoning.

The focus is on simple, explainable decisions rather than detailed analysis, so that this stage can run on every incoming record without introducing substantial latency.

## 20.2 Inputs from the Routing Layer

The inputs to this stage are normalized records produced by the routing and container layers. For user-facing interactions, the main-brain coordinator provides:

- Structured request objects (including message, user_id, and flags such as `use_all_services`).
- A list of services that were considered healthy at the time of the request.
- Intermediate results such as BBB filtering outcomes, RAG search results, and web-research context.  

For internal tasks, the container architecture supplies:

- Candidate knowledge entries from the autonomous learner and Fifth DGM.
- Metrics, analysis results, and diagnostics from verification scripts and monitoring services.

In both cases, the first-stage evaluator sees structured objects rather than raw logs. Records typically include:

- Identifiers, timestamps, role and domain tags, and content summaries.
- Links (or references) to underlying memory, graph, or spatial elements.
- Track assignments and coarse priorities determined by the routing layer.

This structure allows first-stage logic to operate without revisiting raw trace data, except when discrepancies are later investigated.

## 20.3 Basic Keep-or-Discard Decision

For each record, the first-stage logic answers a simple question: should this item be kept for further consideration, or dropped here?

In the running system, this decision appears most concretely in two places:

- The RAG storage pipeline, where `background_rag_store` checks whether a query–response pair is sufficiently novel before calling the RAG server’s `/store` endpoint.
- The truth and safety filters (for example, BBB and identity truth validators), which can mark a record as disallowed or questionable and thereby prevent it from being treated as ground truth.

The keep-or-discard decision is based on criteria such as:

- **Relevance**  
  Whether the record touches on topics, locations, or entities that are in scope for the active role and current global settings. Records that fail safety checks or fall completely outside the system’s intended domain may be dropped.

- **Novelty**  
  Whether similar records have appeared recently, based on lightweight similarity scores returned by the RAG server or hashes/fingerprints for internal content. Near-duplicate interactions that add no new information are candidates for discard.

- **Quality**  
  Whether the record passes basic checks on completeness and internal consistency. For chat-based records, this includes ensuring both query and response are non-empty, well-formed, and free from gross formatting errors.

If the answer is negative, the record is marked as discarded at this stage and is not passed to deeper storage. Minimal metadata about the discard decision (for example, a reason code and timestamp) may still be recorded for audit and analysis.

## 20.4 Signals Used in Evaluation

To support these decisions, the first-stage evaluator draws on several fast, inexpensive signals:

- **Tag and keyword matches**  
  Domain tags, role indicators, and key phrases are compared against allow-lists and deny-lists associated with the current track (meaning-oriented vs. analytical) and global settings. For instance, certain classes of unsafe content may trigger immediate rejection or require BBB/ethics modules to run.

- **Lightweight similarity checks**  
  Before storing new material in semantic memory, the RAG pipeline performs a small `/search` call with `top_k = 1` and examines the similarity score of the closest match. If the score exceeds a configured threshold, the item is treated as redundant and not stored again. This provides an efficient de-duplication mechanism without full clustering or re-encoding of the corpus.

- **Structural heuristics**  
  Simple checks ensure that required fields are present and that basic size limits and format constraints are respected (for example, maximum text length for RAG entries, presence of user identifiers, or minimum content length to avoid trivial noise).

Because these signals are computationally cheap, they can be applied to every record that enters the container paths, providing broad coverage without excessive overhead.

## 20.5 Outcomes and Annotations

Each processed record is assigned an outcome label and supporting annotations to make first-stage behavior explicit. Typical outcomes include:

- **Kept for deeper storage**  
  The record is deemed relevant, novel enough, and structurally sound. For chat interactions, this means the query–response pair is queued for RAG storage with associated metadata. For internal tasks, it may be scheduled for insertion into the I-Container, graph database, or relational store.

- **Discarded as low value or redundant**  
  The record is similar to previously stored items, falls outside the intended domain, fails safety checks, or lacks meaningful content. The system may still log a brief discard entry, but the underlying content is not propagated further.

- **Deferred or flagged**  
  Some records may be tagged for special handling—for example, those that trigger unusual truth-validator patterns, relate to sensitive identity topics, or indicate potential configuration problems. These can be routed to diagnostic tools or human review rather than being immediately stored or discarded.

Associated annotations often include:

- **Reason codes**  
  Short machine-readable codes such as `DUPLICATE`, `OUT_OF_SCOPE`, `SAFETY_DENIED`, or `MINIMAL_CONTENT`, indicating why the action was taken.

- **Confidence estimates**  
  Simple scores or categories (for example, `high`, `medium`, `low`) reflecting the strength of the decision, which can guide later tuning or review.

These annotations allow later stages, monitoring tools, and researchers to understand how and why the first-stage filter behaved as it did.

## 20.6 Interaction with Parallel Paths

Although both parallel paths share the same overall structure, their first-stage evaluators can differ in their criteria and thresholds:

- **Meaning-focused path**  
  This path may be more sensitive to affective or narrative content and more inclined to keep items that touch on themes of care, loss, identity, or community. For example, a short narrative about community resilience might be retained even if it is not technically dense, because it contributes to the system’s understanding of lived experience.

- **Analytical path**  
  This path may prioritize items with clear technical content, structured data, or explicit problem statements. Records that contain precise metrics, spatial features, or well-defined optimization targets are more likely to be kept, while vague or purely emotional content may be filtered out here.

The intake layer’s track assignment determines which evaluator runs for a given record, but both evaluators attach outcomes, reason codes, and any relevant confidence indicators in a comparable format. This makes it possible to compare behavior across paths and to adjust their respective criteria over time.

## 20.7 Recording First-Stage Decisions

Even when records are discarded, the system can record information about first-stage decisions at multiple levels:

- **Aggregated statistics**  
  Counts and rates of kept versus discarded items can be tracked by role, track (meaning-focused vs. analytical), time period, and source (user chat vs. internal task). These statistics support monitoring of load, safety behavior, and possible bias.

- **Sampled examples**  
  A small sample of discarded records can be retained (with appropriate privacy controls) for periodic quality checks and tuning. This allows developers and researchers to inspect borderline cases, refine similarity thresholds, or adjust allow/deny lists.

- **Introspective summaries**  
  Higher-level summaries of first-stage behavior can be written into introspective records or verification reports. For example, the verification scripts used in system evaluation can report how many items were added to or rejected from the I-Container during a test run, or how many RAG storage attempts were skipped due to high similarity scores.

Recording these decisions, even in compressed form, helps guard against systematic errors and provides a basis for empirical evaluation of the first-stage filters.

## 20.8 Relationship to Truth and Safety Filters

First-stage evaluation is closely linked to truth and safety mechanisms, which operate as specialized filters:

- **Blood–brain barrier (BBB)**  
  The BBB acts as a pre-filter for many user-facing interactions, blocking or transforming content that violates ethical or safety constraints before it can reach deeper storage or influence reasoning. Its decisions effectively dominate the keep-or-discard outcome for certain classes of input.

- **Truth validators**  
  Dedicated truth-validation modules check for hallucination patterns, identity confusion, and known factual constraints (for example, the correct number of minds, the correct creator identity, and prohibited forms of self-description). When these modules detect violations, they can downgrade confidence, annotate the record with issues, or prevent it from being treated as trusted knowledge.

In practice, these filters can be viewed as domain-specific first-stage evaluators layered on top of the more generic structural and similarity-based checks described earlier. Together, they define the minimum bar that content must clear before it can become part of central memory or influence downstream processes.

## 20.9 Operational Validation

Operational validation of the first-stage evaluation focuses on two aspects:

- **Correctness of basic behavior**  
  Unit and integration tests (for example, FastAPI TestClient-based tests for the main-brain `/chat` endpoint) confirm that requests are accepted, processed through the BBB and routing logic, and, when appropriate, scheduled for RAG storage without errors. These tests ensure that the first-stage filter does not block safe, ordinary usage.

- **Effectiveness under realistic load**  
  Verification scripts such as `VERIFYANDTEST.sh` and `verifyallclaims.sh` exercise full flows that include autonomous learner outputs, Fifth DGM filtering, and I-Container updates. By comparing I-Container sizes before and after test runs, and by examining logs of RAG storage and de-duplication, evaluators can confirm that:
  - Novel, high-value items are indeed added to memory.
  - Redundant or low-value items are not repeatedly stored.
  - Safety and truth filters are invoked as expected and produce interpretable annotations.

These operational checks do not exhaustively prove correctness but provide concrete evidence that the first-stage evaluation behaves as designed in a live prototype.

## 20.10 Summary

The first-stage evaluation and immediate filtering layer serves as the system’s initial line of defense against overload, redundancy, and unsafe content. It operates on normalized records produced by routing and container structures, applying fast, explainable criteria based on relevance, novelty, structural quality, and domain-specific safety and truth rules. Outcomes are recorded with reason codes and confidence indicators, enabling later diagnostics and academic analysis.

By combining lightweight similarity checks, structural heuristics, and dedicated truth/safety filters, this stage reduces noise, preserves promising material, and respects global constraints, all while maintaining traceability of its decisions. Subsequent chapters build on this foundation to describe how retained items are integrated into deeper storage layers, how patterns over time are identified, and how the system’s behavior evolves as its memories and models change.
