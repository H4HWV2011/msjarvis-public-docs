> **Why this matters for Polymathmatic Geography**  
> This chapter shows how Ms. Jarvis “looks things up” on its own—under constraints—and folds that knowledge back into place‑based memory. It supports:  
> - **P1 – Every where is entangled** by letting external and internal sources about specific communities and regions accumulate together over time in shared Chroma+GeoDB structures.  
> - **P3 – Power has a geometry** by centralizing web and autonomous access behind gateways, learners, and filters whose flows and ports can be audited and redesigned.  
> - **P5 – Design is a geographic act** by embedding web research outputs directly into the same RAG and spatial backbones that serve Appalachian governance, benefits, and resilience questions.  
> - **P12 – Intelligence with a ZIP code** by steering curiosity through topics selected from West Virginia–relevant queues and knowledge‑gap maps rather than generic, placeless lists.  
> - **P16 – Power accountable to place** by making autonomous learning schedulable, loggable, and subject to the same constitutional and identity filters as user‑facing flows.  
> As such, this chapter belongs to the **Computational Instrument** tier: it describes how periodic web research and topic selection are implemented as controlled, observable processes that feed back into entangled, place‑aware memory.

# 27. Web Research and Autonomous Topic Selection

This chapter describes the periodic web‑research and autonomous learning processes that now run as first‑class services alongside user‑facing chat. These processes allow the system to identify topics of interest, collect both internal and external material under constraints, and feed that material back into internal stores in a controlled way. The basic pattern—scheduled retrieval via gateways, semantic storage, and filtered reuse—parallels retrieval‑augmented and tool‑using designs in the broader literature while being adapted to Ms. Jarvis’s WV‑first, GBIM‑anchored architecture.

---

## 27.0 Current Implementation (February 2026)

In the current deployment, autonomous web research is implemented by a dedicated learner service, identity‑aware topic suggestion, and supporting gateways and verification tools. These components are designed to operate on a repeating schedule and to integrate their outputs into long‑term semantic and spatial memory.

- **Optimized learner service with stable HTTP interface**  
  The autonomous learner runs as a FastAPI service (`jarvis-autonomous-learner`) on port **8425**, built around an ONNX sentence‑embedding model cached on the host and a configurable `learning_queue` of topics. It conducts research cycles, constructs embeddings for summarized sessions, and writes them into persistent Chroma collections (for example, `autonomous_learner`). Verification reports now confirm this service as “CONFIRMED OPERATIONAL,” with host mapping 127.0.0.1:8425 and a restart policy of `unless-stopped`.

- **RAG gateways and internal search**  
  Internal retrieval is provided by Chroma‑backed RAG services: the general RAG server on port **8003**, the Spiritual Root / GBIM RAG on **8005**, the WV‑entangled gateway on **8010**, and GIS RAG on **8004**. The learner queries collections such as `autonomous_learner`, `ms_jarvis_memory`, and `conversation_history` to relate new material to existing embeddings, perform semantic deduplication, and identify knowledge gaps.

- **Web research gateways and external search**  
  External web access is mediated by dedicated web‑research services. The learner issues JSON queries to these gateways to obtain structured results (`title`, `snippet`, `url`, `source`), keeping domain policies, rate limits, and geographic filters centralized and auditable. In high‑stakes ULTIMATE flows, the same gateway pattern is used under tighter constraints and in combination with Blood–Brain Barrier and multi‑model reasoning layers.

- **Semantic memory integration and ChromaDB**  
  Summarized research items are embedded at 384 dimensions and stored in long‑lived Chroma collections, including `autonomous_learner`, `conversation_history`, and `ms_jarvis_memory`. Counts from verification logs confirm that Chroma now holds at least five collections with dozens of items and is “actively growing,” with the ONNX embedding model cached persistently on `/mnt/spiritual_drive/msjarvis-rebuild/.cache/chroma`.

- **Topic planning and I‑container suggestions**  
  Topic planning is driven by a configurable `learning_queue` in the learner and augmented by identity‑driven suggestions. A new HTTP endpoint `GET /next-learning-topic` on the I‑containers service (port **8015**) queries Chroma for knowledge gaps across fifteen Appalachian community domains and returns a topic, source type (`knowledge_gap`, `reinforcement`, `fallback`), collection names, and collection counts. The autonomous learner successfully calls this endpoint over the internal network to select learning topics based on its own memory state.

- **Gating and control**  
  Environment variables, supervision policies, and verification scripts act as gating mechanisms for autonomous behavior. System‑wide verification reports summarize whether the autonomous learner, web research, and RAG servers are active; operators can pause learning by stopping the learner container or adjusting flags without modifying learning logic.

The remaining sections of this chapter describe the conceptual role of these processes and how they support the broader architecture.

---

## 27.1 Role of Periodic Web Research and Autonomous Learning

Periodic web research and autonomous learning serve three primary functions, distinct from heartbeat or status checks.

- **Background updating**  
  By running independently of direct user queries, the learner keeps selected areas of knowledge current. It periodically retrieves internal embeddings from collections such as `autonomous_learner` and `ms_jarvis_memory`, and augments them with freshly retrieved web content via the web‑research gateway. This allows the system’s knowledge base to evolve in response to changes in the outside world, rather than only when prompted by users.

- **Curiosity and topic exploration**  
  The learner’s `learning_queue`, the `/next-learning-topic` endpoint, and its embedding‑based summarization infrastructure allow the system to pursue topics of intrinsic interest and local importance, such as “large language model coordination systems” or Appalachian community resilience themes. Over time, this queue is extended by suggestions derived from I‑container interests, autonomous logs, governance priorities, and explicit human input.

- **Support for later tasks**  
  Items stored by the learner become part of the corpus available to RAG pipelines and orchestrated reasoning paths. When later questions arise in governance, spatial planning, or community advice, ULTIMATE and related services can retrieve both user‑driven and autonomously learned material. This increases the diversity and depth of the contexts used for planning and decision‑making, while preserving a clear boundary between automatically discovered knowledge and explicitly curated inputs.

These functions operate within bounds set by truth filters, Blood–Brain Barrier modules, role‑ and geography‑aware routing, and logging requirements, ensuring that autonomous knowledge acquisition remains subordinate to safety and governance constraints.

---

## 27.2 Scheduling, Cadence, and Logging

Autonomous learning and web research run on a regular, observable schedule.

- **Periodic cadence**  
  The learner is configured as a long‑lived service that executes a learning cycle at fixed or configurable intervals. Verification reports include fields indicating that `jarvis-autonomous-learner` is “CONFIRMED OPERATIONAL” and that the autonomous research and storage pipeline is active, forming part of a broader integration healthcheck.

- **Coordinated use of RAG and web services**  
  Within each cycle, the learner constructs embeddings for topic summaries, queries Chroma collections for related internal content, and calls web‑research gateways for external material. Per‑cycle resource use is bounded by explicit limits on the number of RAG and web calls per topic, preventing background learning from starving user‑facing services.

- **Logging and status reports**  
  Learner logs record embedding operations, Chroma insertions, topic selections, and web‑gateway calls. System‑wide verification scripts summarize autonomous activity with structured tables that list running containers (including `jarvis-autonomous-learner`, `jarvis-rag-server`, and `jarvis-web-research`), collection counts, and response times. These reports make autonomy visible as part of the system’s overall “vitals.”

This combination of rhythm, controlled retrieval, and explicit logging allows operators to monitor and adjust autonomous learning without instrumenting every internal operation.

---

## 27.3 Topic Selection

Each autonomous learning cycle starts by selecting one or more topics to investigate, guided by configuration, identity signals, and future entanglement structures.

- **Configured topic lists and embeddings**  
  The learner maintains an internal list of topics to study and uses a sentence‑embedding model to encode both raw texts and higher‑level session summaries. These embeddings structure internal memory and provide a basis for similarity calculations between candidate research items and the existing corpus.

- **Knowledge‑gap–driven selection**  
  The new `/next-learning-topic` endpoint on the I‑containers service queries Chroma (via `jarvis-chroma:8000`) to identify knowledge gaps across fifteen Appalachian community domains. The endpoint returns a topic, a `source_type` that distinguishes between filling gaps and reinforcing existing knowledge, and a set of relevant Chroma collection names. The autonomous learner calls this endpoint to pick topics that are informed by its own memory coverage rather than a static queue alone.

- **Hooks for entangled topic dynamics**  
  Historical variants of the learner code include scaffolding for a `topic_graph.json` and session embeddings that can be used to construct a graph of related topics. As in the entangled RAG design, the long‑term plan is to bias future topic selection toward neighbors of recently studied topics, turning autonomous learning into a structured walk through entangled regions of knowledge.

Topic selection therefore blends configured lists, memory‑driven knowledge‑gap suggestions, and entanglement‑ready structures, ensuring that autonomous learning reflects both prior design and current memory state.

---

## 27.4 Retrieval, Filtering, and Deduplication

Once topics are selected, each cycle performs retrieval and screening to convert raw search results into curated, semantically indexed knowledge.

- **Internal retrieval via Chroma**  
  The learner queries internal collections such as `autonomous_learner`, `ms_jarvis_memory`, and `conversation_history` through HTTP‑based Chroma clients. Retrieved items serve as prior context, help identify coverage gaps, and provide material for multi‑document summaries.

- **External retrieval via web gateways**  
  Web search is conducted through dedicated research gateways that return structured results. The learner translates topics into queries, obtains a bounded number of results per cycle, and respects centralized policies on domains and rate limits.

- **Summarization and structuring**  
  Internal and external items are combined into intermediate structures that may represent individual sources or aggregated views. The learner uses LLMs and embeddings to summarize and compress these materials into session‑level notes suited for storage and reuse.

- **Semantic deduplication and selective storage**  
  Before writing new entries to Chroma, the learner embeds candidate summaries and compares them with existing vectors. Near duplicates are dropped, with counters recording deduplicated items; genuinely new entries are stored with metadata including `topic`, `source_type`, `url` (if applicable), `collection`, and timestamps.

Through this pipeline, the learner transforms noisy, redundant search results into a compact, vectorized knowledge base that can be reused across future tasks.

---

## 27.5 Integration with Memory and Spatial Layers

Accepted items from autonomous learning cycles are folded into the same memory and spatial structures used by other components.

- **Semantic memory collections**  
  New items are written into collections such as `autonomous_learner` and `ms_jarvis_memory`, using the same embedding configuration as the rest of the system. These entries become available to RAG services on ports 8003, 8005, and 8010, and can appear in both autonomous and user‑driven retrieval flows.

- **Spatial integration and GIS export**  
  Existing scripts connect ChromaDB and GeoDB, allowing semantic entries to be exported as GeoJSON and spatial features to be embedded back into Chroma collections. Autonomous learning about spatial themes—such as infrastructure, flood risk, or service access—can therefore be tied to locations and later recovered through GIS RAG.

- **Belief and identity layers**  
  Over time, autonomously acquired material about actors, relationships, and norms can inform GBIM beliefs, governance reasoning, and identity formation. For instance, repeated autonomous learning about Fayette County service networks may be reflected in ULTIMATE reports, identity narratives, or spatial‑justice analyses.

Integrating autonomous learning into both semantic and spatial backbones ensures that background research enriches the same entangled memory stack that supports day‑to‑day stewardship.

---

## 27.6 Interaction with Container and Governance Paths

Autonomous outputs are subject to the same container and governance processes as user‑driven inputs.

- **I‑containers and subconscious RAG**  
  Newly learned items can be treated as candidates for subconscious storage and identity influence. The Fifth DGM service and WOAH algorithms can evaluate these items, deciding whether they remain in background collections, are promoted into I‑containers, or are filtered out.

- **Governance filters and role constraints**  
  Governance and ethics components can restrict topics or sources deemed sensitive, enforcing additional checks on autonomous learning in domains such as health, law, or vulnerable populations. Truth filters, constitutional guardians, and the Blood–Brain Barrier can be applied both to web research outputs and to the autonomous learner’s summaries before they are stored or used.

- **Background influence on future decisions**  
  Once admitted, autonomous items contribute to the contexts retrieved by ULTIMATE and related orchestrators. For example, if autonomous learning repeatedly surfaces new flood‑risk evidence for a region, later spatial or governance queries about that region will be answered against a richer, more current evidence set.

This integration makes autonomous learning a managed contributor to the broader evaluative and decision‑making apparatus, not a free‑floating process.

---

## 27.7 Safeguards and Oversight

Because web research introduces new external material, autonomous learning is equipped with multiple layers of safeguards and oversight.

- **Source restrictions and gateway policies**  
  Web‑research gateways define permitted domains, result limits, and geographic filters. Centralizing these policies ensures that external access can be tightened or adapted without redeploying the learner.

- **Environment‑based gating and operational control**  
  Environment variables and process supervisors provide simple mechanisms for enabling, disabling, or throttling autonomous learning. Verification scripts explicitly report whether autonomous services are active and whether the “complete flow” is working, giving operators a clear picture of autonomy at a glance.

- **Logging, verification, and system‑wide reports**  
  Logs from the learner, web gateways, and RAG servers are combined with periodic verification reports that list running containers, Chroma collection counts, GIS data health, and performance metrics. These reports can be archived to provide an audit trail for when autonomy was active, what it accessed, and how it interacted with other services.

These safeguards align autonomous learning with the program’s glassbox and spatial‑justice commitments, keeping curiosity accountable to place and governance.

---

## 27.8 Web Research in the ULTIMATE Path

Beyond background learning, web research participates directly in user‑driven, high‑stakes reasoning.

- **Position in the orchestration pipeline**  
  In ULTIMATE‑style flows, web research is typically invoked after initial filtering and before deep ensemble reasoning. The main brain may call web gateways alongside RAG services, then pass the resulting context to the 20‑LLM ensemble and judge stack, ensuring that external content is integrated deliberately rather than incidentally.

- **Latency and resource considerations**  
  Web research adds latency, particularly when reaching out to remote sources. Timeouts, bounded result counts, and careful scheduling help prevent web access from dominating response times. Verification scripts measure both chat and web‑research latencies, allowing operators to adjust settings and expectations.

- **Planned introspection and debugging**  
  Future versions of the web‑research gateways are intended to expose debug endpoints that show, for a given request, which internal and external sources were used, how they were ranked, and how context was assembled. Combined with autonomous learner and container logs, this will support detailed provenance tracing for complex answers.

In this way, web research functions as a shared, policy‑constrained capability that supports both autonomous and interactive reasoning.

---

## 27.9 Summary

Autonomous web research and topic selection provide Ms. Jarvis with a controlled form of curiosity: the ability to seek and structure knowledge on a schedule, under constraints, and with clear integration into long‑term memory and spatial layers. By centralizing external access through web‑research gateways, selecting topics via `/next-learning-topic` and identity‑aware queues, storing results in Chroma collections that are also linked to GIS data, and subjecting all autonomous outputs to the same container and governance paths as user‑driven inputs, the system balances the benefits of ongoing learning with the requirements of safety, accountability, and community oversight.
