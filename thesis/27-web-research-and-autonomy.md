# 27. Web Research and Autonomous Topic Selection

This chapter describes the periodic web research and autonomous learning processes that run independently of direct user requests. These jobs allow the system to identify topics of interest, collect both internal and external material under constraints, and feed that material back into internal stores in a controlled way.

## 27.0 Current Implementation (December 2025)

The current implementation of autonomous web research is provided by the optimized learner service and a dedicated web research gateway, working together on a fixed cadence.

- **Optimized learner service (8053)**  
  - `ms_jarvis_autonomous_learner_optimized` runs as a FastAPI application on port `8053` and executes an autonomous learning cycle every five minutes.  
  - Each cycle selects a topic, calls the RAG gateway and the web research gateway, summarizes results, performs semantic deduplication, and writes unique items into Chroma collections.

- **RAG gateway (8103)**  
  - A minimal HTTP service on port `8103` exposes a `/search` endpoint over the Chroma-backed semantic store.  
  - The autonomous learner uses this endpoint to retrieve internal knowledge related to the current topic (documents, prior analyses, and other stored materials).

- **Web research gateway (8009)**  
  - A separate HTTP service on port `8009` exposes a `/search` endpoint that accepts JSON requests of the form `{"query": "<string>", "max_results": <int>}`.  
  - The gateway returns results as an object with `count`, the original `query`, and a `results` list containing fields such as `title`, `snippet`, `url`, and `source`.  
  - The optimized learner uses this gateway rather than direct arbitrary web access, so policies and filters can be centralized.

- **Semantic memory integration**  
  - Summarized research items are stored in the `autonomous_learning` collection, with embeddings and metadata including `topic`, `title`, `url`, `learned_at`, and `cycle_number`.  
  - Per-cycle summaries are stored in the `research_history` collection, capturing the `topic`, counts of items stored and deduplicated, and a timestamp for that learning cycle.

- **Topic planning and suggestions**  
  - The learner maintains a configured `learning_queue` of topics and can augment this with suggestions from a `learning_suggestions` collection.  
  - Other components can populate `learning_suggestions` so that external signals or human inputs influence the autonomous topic planner.

- **Gating and control**  
  - Environment variables (for example, flags for enabling the learner, controlling concurrency, or limiting daily activity) act as the current gating mechanism, determining whether the five-minute loop is active and how aggressively it runs.  
  - This provides practical control over autonomy without requiring a fully realized “consciousness” or mode controller.

The remaining sections of this chapter describe the conceptual role of these processes; the implementation above is the concrete realization currently running in the system.

## 27.1 Role of Periodic Web Research and Autonomous Learning

The web research and autonomous learning layer has three main purposes. Unlike heartbeat and status cycles, its focus is on acquiring and structuring knowledge rather than checking the health of internal services.

- **Background updating**  
  Keep selected areas of knowledge current without waiting for explicit prompts, by periodically refreshing topics via both RAG and web search.

- **Curiosity**  
  Allow the system to identify themes it finds relevant based on past activity, stored priorities, and topic suggestions, then pursue them on its own.

- **Support for later tasks**  
  Populate semantic memory with material that can be reused when related questions appear, giving ULTIMATE and other services richer context.

These functions operate within boundaries set by global settings, environment-based gating, psychological safeguards, and logging requirements.

## 27.2 Scheduling, Cadence, and Logging

Autonomous learning and web research run on a regular, log-visible schedule:

- **Fixed cadence**  
  - A core loop in `ms_jarvis_autonomous_learner_optimized` runs every 300 seconds (five minutes), controlled by an internal timer.  
  - If environment variables indicate the learner should be paused or throttled, the loop can skip work for that cycle.

- **Dual RAG + web behavior**  
  - Each cycle makes at most one RAG call and one web-research call for the selected topic, minimizing resource contention.  
  - If either service is unavailable, the learner logs the error and still completes the cycle with whatever information is available.

- **Stats logging**  
  - Each cycle logs timestamps, selected topic, number of RAG results, number of web results, number of items stored, and number of items deduplicated.  
  - Summary lines (for example, “Cycle complete – Next in 5 minutes”) provide a clear heartbeat in the log, making it easy to see that the loop is healthy over time.

This cadence ensures that updates accumulate steadily without overwhelming other services and that behavior is transparent in the logs.

## 27.3 Topic Selection

For each run, the system chooses what to learn about:

- **Inputs**  
  - The configured `learning_queue` of topics.  
  - Optional additional suggestions from `learning_suggestions` and, in the future, the entanglement topic graph.

- **Current behavior**  
  - The learner currently steps through `learning_queue` in a simple, deterministic order, with hooks in place to support more advanced planners.  
  - A placeholder entanglement update is applied at the end of each cycle, maintaining a `topic_graph.json` structure that will eventually influence topic choice.

- **Planned behavior**  
  - Once neighbor-biased selection is enabled, the learner will use the topic graph to bias toward related topics, effectively creating an entangled random walk through the topic space while still honoring gating and resource constraints.

The result is a small set of focused queries or targets for each cycle, chosen under control of both configuration and emerging entanglement logic.

## 27.4 Retrieval, Filtering, and Deduplication

Once a topic is chosen, the autonomous learner performs retrieval and screening:

- **RAG retrieval**  
  - Calls the RAG gateway on `8103 /search` to retrieve internal content (documents, notes, prior learning outputs) relevant to the topic.

- **Web retrieval**  
  - Calls the web-research service on `8009 /search` to gather external content from permitted sources, using a concise query derived from the topic.

- **Summarization and structuring**  
  - Combines RAG and web results into an intermediate structure.  
  - Uses a summarization step to condense multiple hits into unified items with consistent fields and metadata.

- **Semantic deduplication**  
  - Embeds candidate items and compares them against existing entries in the target collections.  
  - Drops items that are too similar to existing content, incrementing deduplication counters.  
  - Stores only genuinely new items in `autonomous_learning`, and records per-cycle stats in `research_history`.

These steps ensure that the learner grows memory in a controlled way, avoiding redundant clutter while keeping a clear audit trail of what was considered and what was kept.

## 27.5 Integration with Memory and Spatial Layers

Accepted material is written into long-term structures:

- **Semantic memory**  
  - New items and summaries are embedded and stored in appropriate Chroma collections, tagged by source (RAG or web), topic, and time.  
  - Items with clear spatial references may be linked to specific `geodb_*` collections and GeoDB feature IDs.

- **Belief and reasoning layers**  
  - When items describe actors, relationships, or norms, they become part of the broader semantic context that ULTIMATE and other services can retrieve.  
  - Over time, repeated patterns in these items can motivate more explicit belief structures or governance rules in higher-level components.

- **Spatial backbone**  
  - Place references are resolved into geospatial identifiers where possible, linking new material to existing spatial features in the GeoDB layer.

This integration ensures that later retrieval can surface autonomous-learning content alongside manually ingested and RAG-stored knowledge.

## 27.6 Interaction with Container and Governance Paths

Autonomous learning outputs also interact with container-like structures and safeguards:

- **Intake and filtering**  
  - Newly added records are normalized and may be subjected to first-stage keep-or-discard decisions based on topic, source, or size.

- **Background influence**  
  - Items that survive initial filters contribute to the background of available context, influencing how future answers are framed and what evidence is cited.

- **Governance and ethics**  
  - Topics and sources can be constrained by environment variables and configuration, ensuring that certain domains are treated with extra caution or excluded entirely.

In this way, periodic autonomous activity becomes part of the same evaluative flow as user-driven events, but with explicit external controls.

## 27.7 Safeguards and Oversight

Because web research introduces new external material, it is subject to safeguards:

- **Source policies**  
  - Only defined classes of sources are allowed by the web-research gateway, and these policies can be tightened without changing the learner.

- **Gating via environment variables**  
  - Single environment flags can enable or disable the entire autonomous learner, providing an immediate “off switch” if needed.  
  - Additional variables can cap daily cycles or switch the learner into a “RAG-only” mode if external web access should be paused.

- **Logging and review**  
  - Summaries of autonomous learning activity are written into logs and semantic memory, allowing later inspection of what was learned, from where, and when.

These measures aim to balance autonomy with traceability and safety.

## 27.8 Summary

The autonomous learning and web research layer provides a way for the system to seek out and integrate new material on its own schedule. It operates within defined constraints, writes results into core memory and spatial layers, and uses environment-variable gating instead of unconstrained autonomy. Its primary role is to expand and refresh the knowledge base, while the following chapter focuses on cycles that monitor internal health and behavior rather than acquiring new content.

---

### Chapter 27: Web Research and Autonomy - UPDATE

**File**: `thesis/27-web-research-and-autonomy.md`

**Add operational role section**:

```markdown
## Operational Role (December 11, 2025)

### ✅ VALIDATED: Web Research in ULTIMATE Path

web_research consistently appears in services_used for all heavy reasoning tasks.

### Coordination Position
BBB (filter) → web_research (enhance) → llm_bridge (synthesize)

### Function (Inferred from Traces)

Based on request-response patterns, web_research appears to:
1. Receive filtered query + context from BBB
2. Perform semantic search or knowledge retrieval
3. Return enhanced context + source citations
4. Pass results to llm_bridge for synthesis

### Processing Time Budget

**Estimated latency for agi-arch-1** (195s total):
- Health check: ~4s
- BBB: ~1s
- **web_research: ~60s** (30%)
- llm_bridge: ~120s
- Aggregation: ~10s

web_research accounts for ~30% of total latency, suggesting moderate complexity search/retrieval operation.

### Outstanding Questions (Require Code Inspection)

❓ Does it perform **live web scraping** or **cached knowledge retrieval**?  
❓ What **APIs/sources** does it access (Wikipedia? ArXiv? proprietary)?  
❓ How does it **rank/select** relevant context?  
❓ What **semantic similarity threshold** triggers context inclusion?  
❓ How many prior **search results** are included per query?  
❓ Does it **deduplicate** or **synthesize** multiple sources?  

### Implementation Status Badge

✅ **OPERATIONAL** (consistently invoked) | 🔄 **PARTIAL** (internal mechanics unknown)

### Future Work: Debug Endpoint

**Proposed endpoint**: `GET /web_research/debug/sources?job_id={job_id}`

**Response format**:
```json
{
  "job_id": "uuid",
  "query": "Explain Ms. Jarvis architecture",
  "sources_retrieved": [
    {
      "rank": 1,
      "source": "internal_thesis_docs/19-container-architecture-and-routing.md",
      "similarity_score": 0.94,
      "snippet": "Container Topology shows 19 Docker containers..."
    },
    {
      "rank": 2,
      "source": "github_readme_msjarvis",
      "similarity_score": 0.87,
      "snippet": "Ms. Jarvis uses 22-agent LLM ensemble..."
    },
    {
      "rank": 3,
      "source": "web_search_result_url",
      "similarity_score": 0.76,
      "snippet": "Multi-agent systems coordinate through..."
    }
  ],
  "total_sources": 3,
  "context_size_tokens": 1250,
  "retrieval_time_ms": 58000
}
Conclusion

web_research is a critical enabler of ULTIMATE's reasoning capability, providing context that allows llm_bridge to synthesize more informed responses. Full understanding of its operation requires code inspection and debug endpoint implementation.

