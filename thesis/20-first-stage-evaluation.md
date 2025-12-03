# 20. First-Stage Evaluation and Immediate Filtering

This chapter describes the first evaluation stage applied to incoming records after they have been routed into the container paths. The purpose of this stage is to make fast, inexpensive decisions about which items are worth any further attention and which can be safely ignored, while preserving enough information to justify those decisions later.

## 18.1 Objectives of the First Stage

The first stage is designed to:

- Reduce volume:
  - Quickly discard low-value or redundant items so that later stages are not overwhelmed.
- Preserve opportunity:
  - Forward items that may matter later, even if their importance is not yet clear.
- Respect constraints:
  - Apply basic policy and safety checks before anything is stored more deeply.

The focus is on simple, explainable decisions rather than on detailed analysis.

## 18.2 Inputs from the Routing Layer

The inputs to this stage are normalized records produced by the container intake:

- Each record includes identifiers, timestamps, role and domain tags, and content summaries.
- Links to underlying memory, graph, or spatial elements may already be present.
- The routing layer may have assigned a track (meaning-oriented, analytical, or both) and a coarse priority.

The first-stage evaluator treats these records as structured objects and does not need to revisit raw logs unless a discrepancy is detected later.

## 18.3 Basic Keep-or-Discard Decision

For each record, the first-stage logic answers a simple question: should this item be kept for further consideration, or dropped here?

The decision is based on criteria such as:

- Relevance:
  - Whether the record touches on topics, locations, or entities that are in scope for the active role and current global settings.
- Novelty:
  - Whether similar records have appeared recently, based on hashes or similarity scores.
- Quality:
  - Whether the record passes basic checks on completeness and internal consistency.

If the answer is negative, the record is marked as discarded and not passed to deeper storage. Minimal metadata about the discard decision may still be recorded for audit purposes.

## 18.4 Signals Used in Evaluation

The evaluator can use several fast signals to support its judgment:

- Tag and keyword matches:
  - Comparing tags and key phrases against allow-lists and deny-lists for the current track.
- Lightweight similarity checks:
  - Comparing compact fingerprints of the record against recent items to spot near-duplicates.
- Structural heuristics:
  - Ensuring required fields are present and that basic size and format constraints are met.

These signals are chosen to be inexpensive enough to apply to every incoming record.

## 18.5 Outcomes and Annotations

Each processed record is assigned an outcome label and supporting annotations, such as:

- Outcome:
  - Kept for deeper storage.
  - Discarded as low value.
  - Deferred or flagged for special handling.
- Reason codes:
  - Short codes indicating why a decision was made (for example, “duplicate”, “out-of-scope”, “minimal-content”).
- Confidence estimates:
  - Simple scores indicating how strong the decision is, which can guide later review.

These annotations allow later stages and diagnostic tools to understand how the first-stage filter behaved.

## 18.6 Interaction with Parallel Paths

Although both parallel paths share the same overall structure, their first-stage evaluators can differ in their criteria:

- Meaning-focused path:
  - May be more sensitive to affective or narrative content, and more inclined to keep items that touch on themes of care, loss, or community.
- Analytical path:
  - May prioritize items with clear technical content, structured data, or explicit problem statements.

The intake layer’s track assignment determines which evaluator runs, but both evaluators record their decisions in a comparably structured way.

## 18.7 Recording First-Stage Decisions

Even when records are discarded, the system can record:

- Aggregated statistics:
  - Counts and rates of kept versus discarded items by role, track, and time period.
- Sampled examples:
  - A small sample of discarded records for quality checks and tuning.
- Links to introspective entries:
  - When appropriate, high-level summaries of first-stage behavior may be written into introspective records for later analysis.

These records help tune the criteria over time and guard against systematic bias.

## 18.8 Summary

The first-stage evaluation acts as a fast filter that decides which incoming records deserve further attention in each path. It reduces noise, preserves promising material, and applies basic policy checks, while keeping enough information to justify and refine its behavior. Subsequent chapters describe how the remaining items are handled in deeper storage and how patterns over time are identified.
