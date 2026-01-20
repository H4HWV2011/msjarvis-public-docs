> **Why this matters for Polymathmatic Geography**  
> This chapter shows how Ms. Jarvis “looks things up” on its own, under constraints, and folds that knowledge back into place-based memory. It supports:  
> - **P1 – Every where is entangled** by letting external and internal sources about specific communities and regions accumulate together over time.  
> - **P3 – Power has a geometry** by centralizing web access behind gateways and filters so that external knowledge flows are accountable.  
> - **P5 – Design is a geographic act** by embedding web research outputs directly into Chroma+GeoDB backbones used for Appalachian and other spatial reasoning.  
> - **P12 – Intelligence with a ZIP code** by steering curiosity through topics that matter for local governance, resilience, and community life.  
> - **P16 – Power accountable to place** by making autonomous learning schedulable, loggable, and subject to the same filters as user-facing flows.  
> As such, this chapter belongs to the **Computational Instrument** tier: it describes how periodic web research and topic selection are implemented as controlled, observable processes.

# 27. Web Research and Autonomous Topic Selection

This chapter describes the periodic web‑research and autonomous learning processes that run independently of direct user requests. These jobs allow the system to identify topics of interest, collect both internal and external material under constraints, and feed that material back into internal stores in a controlled way. The basic pattern—scheduled retrieval via gateways, semantic storage, and filtered reuse—parallels retrieval-augmented and tool-using designs in the broader literature (for example, Lewis et al., https://arxiv.org/abs/2005.11401; Ram et al., https://arxiv.org/abs/2302.00083).

---

## 27.0 Current Implementation (December 2025)

In the current deployment, autonomous web research is implemented by an optimized learner service together with supporting gateways and verification tools. These components are designed to operate on a repeating schedule and to integrate their outputs into long‑term semantic and spatial memory.

- **Optimized learner service**  
  The autonomous learner runs as a dedicated Python application (for example, `ms_jarvis_autonomous_learner_optimized.py` in the services directory), built around a sentence‑embedding model such as `all‑MiniLM‑L6‑v2` and a configurable `learning_queue` of topics. The learner constructs embeddings for summarized research sessions, encodes session summaries, and writes them into persistent Chroma collections. Verification scripts test whether an “Autonomous Learner” process is running (for instance, by searching for `python.autonomouslearner` in `ps aux`) and report whether the autonomous learning flow is active as part of a full integration healthcheck.

- **RAG gateway and internal search**  
  Internal retrieval is provided by Chroma‑backed RAG services. The system maintains collections such as `autonomous_learning`, `jarvis_consciousness`, `ms_jarvis_memory`, and `mountainshares_knowledge` using `chromadb.PersistentClient` and HTTP-based Chroma clients. Internal scripts and services query these collections to retrieve prior research, semantic memories, and domain‑specific knowledge, making it possible for the learner to relate new material to existing embeddings and to perform semantic deduplication before writing new entries.

- **Web research gateway and external search**  
  External web access is mediated by dedicated gateways rather than by arbitrary HTTP calls from core services. A web‑research service exposes HTTP endpoints that accept JSON queries of the form `{"query": "<string>", "max_results": <int>}` and return structured lists of results with fields such as `title`, `snippet`, `url`, and `source`. The autonomous learner and higher‑level orchestrators call this gateway to obtain external context while keeping source policies centralized and auditable. In the ULTIMATE reasoning path, a similar gateway is used as part of a broader pipeline that also includes the Blood–Brain Barrier and multi‑model reasoning layers.

- **Semantic memory integration**  
  Summarized research items are embedded and stored in long‑lived collections. The `autonomous_learning` collection contains atomic learned items, while per‑cycle summaries can be stored in a `research_history` or similar collection that records topics, counts of stored versus deduplicated items, and timestamps. Other collections, such as `jarvis_consciousness` and `ms_jarvis_memory`, hold more general reflections and identity‑related fragments. These collections are accessed by other services and are periodically exported to or synchronized with GIS layers, for instance via `extract_all_chromadb_to_gis.py`, which traverses all ChromaDB SQLite databases and writes a combined GeoJSON feature set.

- **Topic planning and suggestions**  
  The learner’s topic planning is driven by a configurable `learning_queue` in the autonomous learner code and can be extended by additional suggestion sources. Historical versions of the learner code show hooks for maintaining a topic graph (for example, `topic_graph.json`) and computing embeddings for topic summaries, allowing future development of entangled topic dynamics where related topics are visited in clustered sequences.

- **Gating and control**  
  Environment variables and external scripts act as gating mechanisms for autonomous behavior. Verification scripts check whether the autonomous learner process is running, whether key services are responsive, and whether Chroma directories and GIS data directories exist and are populated. Operators can disable or pause autonomous learning by stopping the learner process, adjusting environment flags, or placing the system into a testing mode, all without modifying core learning logic.

The remaining sections of this chapter describe the conceptual role of these processes and how they support the broader architecture.

---

## 27.1 Role of Periodic Web Research and Autonomous Learning

Periodic web research and autonomous learning serve three primary functions, distinct from heartbeat or status checks.

- **Background updating**  
  By running independently of direct user queries, the learner keeps selected areas of knowledge current. It periodically retrieves internal embeddings from collections such as `autonomous_learning`, `jarvis_consciousness`, and `ms_jarvis_memory`, and augments them with freshly retrieved web content. This allows the system’s knowledge base to evolve in response to changes in the outside world, rather than only when prompted by users.

- **Curiosity and topic exploration**  
  The learner’s `learning_queue` and embedding‑based summarization infrastructure allow the system to pursue topics of intrinsic interest, such as “large language model coordination systems” or other domain‑relevant themes encoded in the learner’s configuration. Over time, this queue can be extended by suggestions derived from container analyses, governance priorities, or explicit human input. The eventual use of topic graphs and entangled embeddings is intended to drive a structured “random walk” through related topics, embodying a controlled form of curiosity that echoes curiosity-driven exploration in reinforcement learning (for example, Pathak et al., https://arxiv.org/abs/1705.05363).

- **Support for later tasks**  
  Items stored by the learner become part of the corpus available to RAG pipelines and orchestrated reasoning paths. When later questions arise in governance, spatial planning, or community advice, ULTIMATE and related services can retrieve both user‑driven and autonomously learned material. This increases the diversity and depth of the contexts used for planning and decision‑making, while maintaining a clear boundary between automatically discovered knowledge and explicitly curated inputs.

These functions operate within bounds set by truth filters, Blood–Brain Barrier modules, environment‑based gating, and logging requirements, ensuring that autonomous knowledge acquisition remains subordinate to safety and governance constraints.

---

## 27.2 Scheduling, Cadence, and Logging

Autonomous learning and web research run on a regular, observable schedule, although the host’s current runtime state may not expose all intended behaviors.

- **Fixed or periodic cadence**  
  The optimized learner is designed to run as a long‑lived service that executes a learning cycle at a fixed interval (for example, every five minutes). Verification scripts include sections labelled “AUTONOMOUS LEARNER” and commands that search for `python.autonomouslearner` processes, reporting whether the learner is “RUNNING” and whether the complete autonomous learning flow is operational. This demonstrates that the architecture expects a regular, repeating cycle, even if particular deployments may adjust the exact timing.

- **Coordinated use of RAG and web services**  
  Within each cycle, the learner constructs embeddings for topic summaries, queries Chroma collections for related internal content, and calls external web‑research gateways for additional material. Design notes and scripts encourage a pattern in which each cycle issues a small, bounded number of RAG and web calls per topic to limit resource consumption, especially when sharing infrastructure with user‑facing services such as main chat and GIS queries.

- **Logging and verification reports**  
  Autonomy is made observable through both service logs and verification scripts. The learner’s code logs embedding operations, Chroma insertions, and topic processing steps, while verification scripts generate structured reports summarizing system status. These reports include statements about autonomous learning activity (for example, “Autonomous learning Active” and “Complete flow Working”), counts of running services, ChromaDB size, GIS file counts, and performance metrics such as response times for GIS queries and production chat. Together, they provide a coarse but meaningful view of autonomous behavior over time.

This combination of steady cadence, controlled use of retrieval services, and explicit logging makes it possible to monitor and adjust autonomous learning without needing to instrument every internal step.

---

## 27.3 Topic Selection

Each autonomous learning cycle begins by selecting one or more topics to investigate, guided by configuration and, in future, by entangled topic structures.

- **Configured topic lists and embeddings**  
  The optimized learner maintains an internal list of topics to study, such as “large language model coordination systems”, and uses an embedding model (`SentenceTransformer('all‑MiniLM‑L6‑v2')`) to encode both raw texts and higher‑level session summaries. These embeddings are used both to structure internal memory and to estimate similarity between candidate research items and the existing corpus, following sentence-embedding practices described by Reimers & Gurevych (https://arxiv.org/abs/1908.10084).

- **Simple queues with hooks for entanglement**  
  In the current implementation, topics are often processed according to a simple queue or deterministic rule coded directly in the learner. Historical variants of the code suggest the use of a `topic_graph.json` and session embeddings to construct a graph of related topics, with the long‑term plan of biasing future topic selection toward neighbors of recently studied topics. Even before this graph is fully exploited, the presence of topic embeddings and session summaries provides a foundation for more sophisticated planners.

- **External and governance‑driven suggestions**  
  The architecture allows for additional topic suggestions to be injected into the learner from other components. For example, container analyses of I‑Container contents and autonomous learning logs can produce lists of under‑explored themes, while governance processes or human operators can append topics tied to current community concerns or policy issues. Over time, this combination of internal entanglement and external suggestions is intended to produce a guided but open‑ended exploration of the relevant knowledge space.

Topic selection thus balances fixed configuration, potential entangled dynamics, and external input, ensuring that autonomous learning activity reflects both prior structure and current priorities.

---

## 27.4 Retrieval, Filtering, and Deduplication

Once topics are selected, each cycle performs retrieval and screening to convert raw search results into curated, semantically indexed knowledge.

- **Internal retrieval via Chroma**  
  The learner queries internal collections through Chroma clients, whether via a local persistent client or HTTP. Collections such as `autonomous_learning`, `jarvis_consciousness`, and `ms_jarvis_memory` are searched for items related to the current topic, and the retrieved items are used both as signals of prior coverage and as inputs to new summaries.

- **External retrieval via web research gateways**  
  Web search is conducted through dedicated gateways that return structured results containing titles, snippets, URLs, and sources. The learner uses topic‑derived queries to call these gateways and retrieve a bounded number of external results, ensuring that external access is both policy‑controlled and rate‑limited. This indirection allows policies (such as allowed domains, rate limits, or geographic filters) to be updated centrally without changing the learner code.

- **Summarization and structuring**  
  Retrieved internal and external items are combined into intermediate structures, where multiple hits can be summarized into synthetic documents or notes. The learner’s use of embeddings for summaries and session‑level descriptions ensures that the granularity of stored items can vary: some entries may represent single documents, while others may represent aggregated knowledge about a theme. This multi-level summarization is consistent with hierarchical summarization strategies in the literature (for example, Liu & Lapata’s work on document summarization, https://arxiv.org/abs/1903.10318).

- **Semantic deduplication and selective storage**  
  Before writing new entries into collections such as `autonomous_learning`, the learner embeds candidate items and compares them with existing embeddings to detect near‑duplicates. Items whose embeddings fall within a small distance of existing items are considered redundant and are dropped from storage, while counters record how many candidates were rejected due to similarity. Only items that appear genuinely new or substantially different are stored, together with metadata such as `topic`, `title`, `url`, `learned_at`, and possibly `cycle_number`.

Through these steps, the learner converts raw search results into a curated, vectorized knowledge base that is compact enough to be tractable and rich enough to support later reasoning.

---

## 27.5 Integration with Memory and Spatial Layers

Accepted items from autonomous learning cycles are integrated into the same memory and spatial structures used by other components, ensuring that they participate fully in later reasoning.

- **Semantic memory collections**  
  New items are written into collections such as `autonomous_learning` and `jarvis_consciousness`, with embeddings computed using the same sentence‑transformer model used during retrieval. Collections are stored in ChromaDB and can be queried by both autonomous processes and user‑facing RAG flows, allowing autonomous knowledge to be rediscovered by later queries without direct coupling between those queries and the learning process.

- **Spatial integration and GIS export**  
  Scripts such as `extract_all_chromadb_to_gis.py` traverse all ChromaDB SQLite databases and write GeoJSON files in a GIS directory, assigning default coordinates and storing Chroma table names and rows as feature properties. In the opposite direction, scripts like `sync_geodb_to_chromadb.py` load rows from a GeoDB `features` table and write them into a Chroma collection `geodb_features`, with `geodb_id` metadata linking features to embeddings. This bidirectional flow means that autonomous learning about spatially relevant topics can ultimately be tied to concrete locations, and vice versa.

- **Belief, governance, and identity layers**  
  Over time, items that describe actors, relationships, and norms become part of the context used by orchestrators, governance tools, and identity‑related services. For example, autonomous learning about water infrastructure, governance frameworks, or community initiatives can feed into beliefs used by ULTIMATE when producing state‑of‑region or state‑of‑governance reports. The same Chroma collections that store autonomous learning outputs are also used by services that generate summaries of spatial knowledge, identity candidates, and theological or ethical reflections.

By integrating autonomous learning into both semantic and spatial backbones, the system ensures that “background” research is not siloed but directly usable by the rest of the architecture.

---

## 27.6 Interaction with Container and Governance Paths

Autonomous outputs are not consumed in isolation; they are subject to the same container and governance processes as user‑driven inputs.

- **Container intake and background tracks**  
  Newly learned items can be treated as container‑like entries, passing through keep‑or‑discard decisions based on topic, source, and quality. For example, autonomous learning about a local watershed might produce entries that are reviewed by Fifth DGM and WOAH, scored for relevance and quality, and then either promoted into I‑Containers or left in background collections. Container growth analysis scripts, which compute I‑Container size and suggest pruning or further growth, implicitly incorporate these autonomous items into their recommendations.

- **Governance filters and role constraints**  
  Governance and ethics components can restrict topics or sources deemed sensitive, enforcing additional checks on autonomous learning in areas such as health, law, or vulnerable populations. Truth filters and Blood–Brain Barrier modules can be deployed in front of both web research and ingestion of learning outputs, rejecting items that violate accuracy or ethical criteria. This means that autonomous learning is not free‑running: it is constrained by the same filters that protect user‑driven workflows, consistent with responsible-AI frameworks (for example, Raji et al., https://arxiv.org/abs/2001.00973; Whittlestone et al., https://arxiv.org/abs/1903.03425).

- **Background influence on future decisions**  
  Once admitted, autonomous items contribute to the context retrieved by ULTIMATE and related orchestrators, affecting how future decisions are framed. For example, if autonomous learning repeatedly discovers new flood‑risk assessments for a region, subsequent spatial or governance queries about that region will retrieve richer context, potentially altering the system’s recommendations or risk assessments.

In this way, autonomous learning becomes a managed source of background knowledge that is integrated into the broader evaluative and decision‑making apparatus.

---

## 27.7 Safeguards and Oversight

Given that web research introduces new external material, the autonomous learning system is equipped with multiple layers of safeguards and oversight.

- **Source restrictions and gateway policies**  
  Web‑research gateways define which sources are permitted and how many results may be returned for a given query. These policies can be updated independent of the learner code, providing a central place to restrict domains, enforce geographic limits, or implement blacklists and whitelists. Because all external access flows through these gateways, they constitute a strong control point for external dependencies.

- **Environment-based gating and operational control**  
  Environment variables and process supervision provide operators with simple mechanisms for enabling, disabling, or throttling autonomous learning. Verification scripts explicitly report whether autonomous services are “Active” and whether “Complete flow” is “Working”, making it straightforward to check whether autonomy is currently functioning. If necessary, operators can stop the learner process, adjust environment flags, or modify supervision policies to reduce or temporarily suspend autonomous activity.

- **Logging, verification, and system-wide reports**  
  Logs and verification scripts together provide a trail of autonomous activity. Structured reports produced by scripts such as `verifyallclaims.sh` and `VERIFYANDTEST.sh` include sections on autonomous learner status, I‑Container size and growth capacity, ChromaDB and GIS data health, and service responsiveness. Over time, these reports can be archived to provide an audit trail of how and when autonomous learning was active, what infrastructure it relied on, and how it interacted with other services.

These safeguards align autonomous learning with the broader design goal of glassbox introspection: autonomy is permitted, but it is bounded, observable, and subject to human oversight.

---

## 27.8 Web Research in the ULTIMATE Path

Beyond its role in autonomous learning, web research also contributes directly to user‑driven, high‑stakes reasoning paths.

- **Position in the orchestration pipeline**  
  In ULTIMATE‑style flows, web research is typically invoked after safety filtering and before deep model reasoning. A representative pattern is: Blood–Brain Barrier and related filters apply constraints to the query and context; a web‑research gateway is called to enrich the filtered context with external and internal sources; and multi‑model reasoning engines, such as AI ensemble servers and DGM orchestrators, then operate on this enriched context. This ensures that external content is both vetted and integrated into a deliberative pipeline, consistent with retrieval-augmented architectures (for example, Lewis et al., https://arxiv.org/abs/2005.11401).

- **Latency and resource considerations**  
  Web research adds latency to ULTIMATE flows, especially when external requests must be made to remote sources. To manage this, gateway calls often include explicit timeouts and limits on result counts, and orchestrators are designed to remain responsive even if web research is partially unavailable. The same verification scripts that measure GIS and chat response times can be extended to benchmark web‑research latency, ensuring that the contribution of this layer is known and manageable.

- **Planned introspection and debugging**  
  To maintain transparency, future versions of the web‑research gateway are intended to expose debug endpoints that show, for a given request, which internal and external sources were consulted, how they were ranked, what similarity scores were computed, and how the final context was assembled. Combining these introspective reports with logs from autonomous learning and container processes will make it possible to reconstruct the provenance of complex ULTIMATE answers that rely on multiple layers of web research and internal retrieval.

In this context, web research acts as a shared service that supports both autonomous and user‑driven reasoning, with common safeguards and introspective tools.

---

## 27.9 Summary

Autonomous web research and topic selection provide Ms. Jarvis with a controlled form of curiosity: the ability to seek and structure knowledge on a schedule, under constraints, and with clear integration into long‑term memory and spatial layers. By centralizing external access through web‑research gateways, storing results in Chroma collections that are also linked to GIS data, and subjecting all autonomous outputs to the same container and governance paths as user‑driven inputs, the system balances the benefits of ongoing learning with the requirements of safety, accountability, and community oversight.
