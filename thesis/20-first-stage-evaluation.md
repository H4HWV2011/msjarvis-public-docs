> **Why this matters for Polymathmatic Geography**
> This chapter explains the first gate Ms. Jarvis applies to every incoming record — a fast,
> inexpensive layer that decides what gets stored, what gets flagged, and what gets dropped before
> any deeper reasoning begins. It supports:
> - **P1 – Every where is entangled** by ensuring that even the fastest evaluation respects safety,
>   truth, and place-based constraints before allowing content to entangle with community memories.
> - **P3 – Power has a geometry** by making keep-or-discard decisions explicit, annotated, and
>   auditable rather than hiding them inside opaque pipelines.
> - **P5 – Design is a geographic act** by treating first-stage filtering as a design choice about
>   which Appalachian realities are admitted into memory and which are deferred or discarded.
> - **P12 – Intelligence with a ZIP code** by scoping relevance checks to role, domain, and
>   place-tagged records rather than treating all content as equally worthy of storage.
> - **P16 – Power accountable to place** by recording reason codes, confidence indicators, and
>   aggregated statistics so communities can audit how and why the system filtered their data.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies the first
> evaluation and filtering layer that protects downstream memory and reasoning from overload,
> redundancy, and unsafe content.

---

## Status as of February 2026

| Category | Details |
|---|---|
| **Implemented now** | `background_rag_store` confirmed operational in `jarvis-main-brain` (port **8050**): runs as a background task after every `/chat` response, performs a near-duplicate check via RAG server `/search` with `top_k=1`, and writes accepted interactions into `ms_jarvis_memory` Chroma collection with `bg_<ISO8601>` ids, `type: "background"` metadata, and `services: ["llm20production"]`. **`ms_jarvis_memory` is append-only in the current deployment**: deduplication is advisory — it affects the skip logic and downstream reuse, not the write path. Repeated identical messages produce distinct entries with separate timestamps. `truthverdict` from BBB (port **8016**) attached to every `UltimateResponse`, providing `valid`, `confidence`, and `principalreasons` signals. `/curator/background` endpoint on main brain (port **8050**) providing stable, auditable view of background store contents. BBB four-filter pipeline (`EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`, `ThreatDetection`) operational as pre-filter gate. Identity truth validators (`normalize_identity`, `TruthValidator`) applied on every response. Confirmed in 2026-02-15 case study: `bg_<ISO8601>` entries in `ms_jarvis_memory` verified via Python REPL and `/curator/background` query (see Chapter 9 §9.3.5 and Chapter 17 §17.6). |
| **Partially implemented / scaffolded** | Novelty/near-duplicate check influences legacy RAG storage and skip logic but does not currently prevent writes to `ms_jarvis_memory`; Chroma background store remains append-only. Track-level differentiation between meaning-focused and analytical path evaluators is present as a design pattern but not yet fully implemented as distinct threshold configurations in the current deployment. `truthverdict` is advisory in the current `ultimatechat` path — it does not hard-gate input processing. Aggregated first-stage statistics (counts and rates by role, track, and source) are logged but not yet exposed via a dedicated metrics endpoint. |
| **Future work / design intent only** | Hard-gate behavior on `truthverdict` for specific role or threat levels. Configurable per-track similarity thresholds that actually prevent writes for near-duplicate content. Persistent sampled-example store for borderline-case quality review. Automated introspective summaries reporting first-stage behavior across runs. Full deduplication at the write path for `ms_jarvis_memory`. |

> **Cross-reference:** The canonical description of the `ultimatechat` execution path — including
> exactly where `background_rag_store` is scheduled, where `truthverdict` is computed and
> attached, and where BBB output-guarding fires — is in **Chapter 17**. This chapter describes
> the purpose, logic, and observed behavior of the first-stage evaluation layer that those
> mechanisms implement.

---

# 20. First-Stage Evaluation and Immediate Filtering

This chapter describes the first evaluation stage applied to incoming records after they have been
routed into the container paths. In the current deployment, this stage is realized by a
combination of fast safety checks, background storage for semantic memory, truth-validation
modules, and basic structural heuristics. Its purpose is to make fast, inexpensive decisions
about which items warrant further attention and which can be safely ignored, while preserving
enough information to justify those decisions later.

---

## 20.1 Objectives of the First Stage

In the current deployment, the first stage satisfies three practical objectives.

**Reduce volume.** In the current deployment, the system quickly discards or downgrade low-value
items so that later stages — such as deeper RAG integration, graph updates, or I-container growth
— are not overwhelmed. Although `ms_jarvis_memory` is currently append-only and does not
deduplicate Chroma background entries at write time, the near-duplicate check in
`background_rag_store` centralizes routing so that downstream services can choose whether to
reuse or skip repeated content.

**Preserve opportunity.** In the current deployment, user conversations that pass safety checks
are queued for background handling and written into the `ms_jarvis_memory` semantic store
(confirmed running via `jarvis-chroma` at **127.0.0.1:8002**), where they can later contribute
to autonomous learning, clustering, or case-study analysis.

**Respect constraints.** In the current deployment, BBB (`jarvis-blood-brain-barrier`, port
**8016**) and truth-validation modules act as early gates that can veto or annotate content
before it is allowed to influence memory or downstream reasoning. The `truthverdict` attached to
every `UltimateResponse` is the concrete artifact of this constraint, even though it is advisory
rather than a hard gate in the current deployment.

The focus is on simple, explainable decisions rather than detailed analysis, so that this stage
can run on every incoming record without introducing substantial latency.

---

## 20.2 Inputs from the Routing Layer

In the current deployment, the inputs to this stage are normalized records produced by the
routing and container layers. For user-facing interactions, `jarvis-main-brain` on port **8050**
provides structured `UltimateRequest` objects (message, `userid`, role, `useallservices`), a
snapshot of services confirmed healthy by `discover_services()` at request time, and intermediate
signals such as BBB filtering outcomes, `llm20production` ensemble results, and web-research
context. For the canonical description of how these inputs are assembled, see **Chapter 17**.

For internal tasks, the container architecture supplies candidate knowledge entries from the
autonomous learner and Fifth DGM (where active; `jarvis-fifth-dgm`, port **4002**, confirmed
running), and metrics, analysis results, and diagnostics from verification scripts and monitoring
services. In both cases, records include identifiers, timestamps, role and domain tags, content
summaries, links to underlying memory or spatial elements, and track assignments.

---

## 20.3 Basic Keep-or-Discard Decision

In the current deployment, the keep-or-discard decision appears most concretely in two places.

**`background_rag_store`.** After every `/chat` response, in the current deployment
`jarvis-main-brain` schedules `background_rag_store` with the original message, response text,
and `servicesused`. The task performs a near-duplicate check via the RAG server's `/search`
endpoint with `top_k=1`. If the top result's similarity score exceeds a configured threshold, the
task logs a `rag_skip_duplicate` event. If the query is sufficiently novel, it calls the RAG
server's `/store` endpoint and writes the record into `ms_jarvis_memory` with a
`bg_<ISO8601_TIMESTAMP>` id, `type: "background"` metadata, and the `servicesused` list.
**`ms_jarvis_memory` is append-only in the current deployment**: the near-duplicate check is
advisory and affects the skip logic only, not the write path. Repeated identical test messages
produce distinct entries with separate timestamps and response variants.

**BBB and identity truth validators.** In the current deployment, BBB (`jarvis-blood-brain-barrier`,
port **8016**) marks records as disallowed or questionable via the `truthverdict` on
`UltimateResponse`, thereby preventing flagged content from being treated as ground truth by
downstream services even when the background write still occurs.

The keep-or-discard decision is based on relevance (whether the record is in scope for the
active role), novelty (near-duplicate check signal), and quality (non-empty, well-formed query
and response, free from gross formatting errors).

If the answer is negative, the record may be marked as discarded or low-value at this stage and
is not passed to deeper trusted stores such as identity specifications or curated graph layers.
Minimal metadata about the decision (reason code and timestamp) can still be recorded for audit
and analysis.

---

## 20.4 Signals Used in Evaluation

In the current deployment, the first-stage evaluator draws on several fast, inexpensive signals.

**Tag and keyword matches.** Domain tags, role indicators, and key phrases are compared against
allow-lists and deny-lists associated with the current track and global settings. Certain classes
of unsafe content trigger BBB / ethics modules before any storage occurs.

**Lightweight similarity and reuse checks.** In the current deployment, before writing new
material into the legacy RAG server, the pipeline performs small similarity lookups via `/search`
and examines the closest-match score. The Chroma background store `ms_jarvis_memory` remains
append-only; these checks influence legacy RAG storage behavior and downstream reuse only.

**Structural heuristics.** Simple checks confirm required fields are present and that basic size
limits and format constraints are met (maximum text length for background entries, presence of
user identifiers, minimum content length to avoid trivial noise).

Because these signals are computationally inexpensive, in the current deployment they are applied
to every record that enters the container paths, providing broad coverage without excessive
overhead.

---

## 20.5 Outcomes and Annotations

In the current deployment, each processed record is assigned an outcome and supporting
annotations.

**Kept for deeper storage or background memory.** The record is deemed relevant and structurally
sound. For chat interactions, in the current deployment this means the user message and model
response are written into the `ms_jarvis_memory` Chroma collection as a `background` item with
`bg_<ISO8601>` id and associated metadata, confirmed via `/curator/background` query (see
Chapter 9 §9.3.5). For internal tasks, it may be scheduled for insertion into the I-container,
graph database, or relational store where the corresponding APIs are active.

**Discarded or down-ranked as low value or redundant.** The record is similar to previously
stored items, falls outside the intended domain, fails safety checks, or lacks meaningful
content. In the current deployment, some such records remain in background memory but are not
promoted into trusted identity or graph layers.

**Deferred or flagged.** Records that trigger unusual `truthverdict` patterns, relate to
sensitive identity topics, or indicate configuration problems are routed to diagnostic tools or
human review.

Associated annotations include reason codes (short machine-readable flags such as
`OUT_OF_SCOPE`, `SAFETY_DENIED`, `MINIMAL_CONTENT`, or entries in `truthverdict`) and confidence
estimates reflecting the strength of the decision.

---

## 20.6 Interaction with Parallel Paths

In the current deployment, both the meaning-focused and analytical paths share the same
`background_rag_store` and BBB infrastructure, with the track assignment from the routing layer
determining which evaluator criteria apply.

**Meaning-focused path.** In the current deployment, this path may retain items that touch on
themes of care, identity, or community even if they are not technically dense, because they
contribute to psychological and community-context modules. Such items are written into background
memory and may later be referenced by `jarvis-psychology-services` (port **8019**, confirmed
running) or `psychological_rag_domain` (port **9006**, confirmed running).

**Analytical path.** In the current deployment, this path prioritizes items with clear technical
content, structured data, or explicit problem statements. The design intends that distinct
per-track threshold configurations will be implemented as the system matures; in the current
deployment, both paths use the same near-duplicate and BBB filter parameters.

Both evaluators attach outcomes, reason codes, and confidence indicators in a comparable format,
making it possible to compare behavior across paths and to adjust their criteria over time.

---

## 20.7 Recording First-Stage Decisions

In the current deployment, even when records are down-ranked or effectively discarded, the system
records information about first-stage decisions at multiple levels.

**Aggregated statistics.** In the current deployment, counts and rates of kept versus skipped
items are logged by role and source. A dedicated metrics endpoint exposing these breakdowns is
identified as near-term work.

**Sampled examples.** In the current deployment, the `/curator/background` endpoint on
`jarvis-main-brain` (port **8050**) provides a stable, auditable view of what has been retained,
enabling researchers to inspect both nominal and edge-case behaviors. A formal sampled-example
store for borderline-case quality review with privacy controls is identified as future work.

**Introspective summaries.** In the current deployment, verification scripts can report how many
items were written into `ms_jarvis_memory` during a test run, how often `truthverdict` flagged
issues, and how many background tasks were queued without error. Automated production of such
summaries on a scheduled basis is identified as future work.

---

## 20.8 Relationship to Truth and Safety Filters

In the current deployment, first-stage evaluation is closely linked to BBB and truth-validation
mechanisms.

**Blood–brain barrier (BBB), port 8016.** In the current deployment, `jarvis-blood-brain-barrier`
acts as a pre-filter for user-facing interactions, blocking or transforming content that violates
ethical or safety constraints before it can reach deeper storage or influence reasoning. Its
verdicts — `valid`, `confidence`, `principalreasons` — are attached as `truthverdict` on
`UltimateResponse` and are advisory in the current deployment rather than a hard gate on writes
to `ms_jarvis_memory`. Hard-gate behavior for specific role or threat levels is identified as
future work.

**Truth validators.** In the current deployment, `TruthValidator` and `normalize_identity` check
for hallucination patterns, identity confusion, and known factual constraints. When these modules
detect violations, they annotate the record with issues and prevent it from being treated as
trusted knowledge, even if the background record remains in `ms_jarvis_memory`. These filters
are domain-specific first-stage evaluators layered on top of the more generic structural and
similarity-based checks described earlier.

Together, in the current deployment, these filters define the minimum bar that content must clear
before it can become part of central, trusted memory or influence downstream processes.

---

## 20.9 Operational Validation

In the current deployment, operational validation of the first-stage evaluation focuses on two
aspects.

**Correctness of basic behavior.** Integration tests using `jarvis-main-brain` `/chat` endpoint
confirm that requests are accepted, processed through BBB and routing logic, and scheduled for
background handling without errors. Empirical tests on 2026-02-15 show that each `/chat` call
produces a full `UltimateResponse` (including `truthverdict` and `servicesused`), queues a
background task (log entries `rag-store-queued`), and results in a new `background` entry in
`ms_jarvis_memory` with a `bg_<ISO8601>` identifier and appropriate metadata. This was confirmed
via Python REPL inside the `jarvis-main-brain` container and via `/curator/background` query (see
Chapter 9 §9.3.5 and Chapter 17 §17.6).

**Effectiveness under realistic use.** In the current deployment, manual verification runs
demonstrate that repeated identical messages produce multiple background entries clustering
closely in embedding space but retaining distinct timestamps and response variants (confirming
append-only behavior). Truth and safety filters are invoked consistently, with `truthverdict`
fields reflecting ethics and identity assessments even for technical test messages. The
`/curator/background` endpoint provides a stable, auditable view of what has been retained,
enabling researchers to inspect both nominal and edge-case behaviors.

These operational checks do not exhaustively prove correctness but provide concrete evidence of
how the first-stage evaluation behaves in the live deployment as of mid-February 2026, including
where its behavior diverges from the earlier, more aggressively de-duplicating design.

---

## 20.10 Summary

In the current deployment, the first-stage evaluation and immediate filtering layer serves as the
system's initial gate against overload, redundancy, and unsafe content. It operates on normalized
records produced by routing and container structures, applying fast, explainable criteria based
on relevance, near-duplicate signals, structural quality, and domain-specific safety and truth
rules. Outcomes are recorded with reason codes and confidence indicators, enabling later
diagnostics and academic analysis.

The two most concrete artifacts of this stage in the current deployment are: the `truthverdict`
field on every `UltimateResponse` (computed by BBB at port **8016**), and the `bg_<ISO8601>`
entries in the `ms_jarvis_memory` Chroma collection (written by `background_rag_store` after
every `/chat` call). **`ms_jarvis_memory` is append-only** in the current deployment;
lightweight near-duplicate checks influence legacy RAG reuse and skip logic but do not prevent
writes. For the canonical description of exactly where in the execution sequence these artifacts
are produced, see **Chapter 17**.

Subsequent chapters build on this foundation to describe how retained items are integrated into
deeper storage layers, how patterns over time are identified, and how the system's behavior
evolves as its memories and models change.
