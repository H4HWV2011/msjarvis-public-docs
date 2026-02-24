> **Why this matters for Polymathmatic Geography**
> This chapter describes how the three-stage structure outlined in earlier chapters is
> instantiated in two parallel paths with different emphases. It supports:
> - **P1 – Every where is entangled** by routing both experiential and technical perspectives
>   through a shared Chroma background store and unified orchestration layer.
> - **P3 – Power has a geometry** by making the asymmetry between the two paths explicit: the
>   analytical path is fully wired into `ultimatechat` while meaning-oriented modules are
>   partially present and not yet all plugged in.
> - **P5 – Design is a geographic act** by encoding how Appalachian questions are handled
>   differently depending on whether they enter the analytical or meaning-oriented track.
> - **P12 – Intelligence with a ZIP code** by grounding both tracks in West Virginia–specific
>   memory, identity constraints, and community context.
> - **P16 – Power accountable to place** by exposing which modules were active for each request
>   via `consciousnesslayers`, `identitylayers`, and `truthverdict` in every `UltimateResponse`.
>
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies how the
> two parallel processing paths are implemented, what is actually wired into the live
> `ultimatechat` entrypoint, and what remains present as services but not yet plugged in.

---

## Status as of February 2026

| Category | Details |
|---|---|
| **Implemented now — analytical path (always runs in `ultimatechat`)** | `jarvis-20llm-production` at **127.0.0.1:8008** (confirmed running) as primary synthesis fabric; `jarvis-semaphore` proxy at **127.0.0.1:8030**; `llm1-proxy` through `llm22-proxy` at **127.0.0.1:8201–8222** (all confirmed). Judge services confirmed running: truth 7230, consistency 7231, alignment 7232, ethics 7233. `jarvis-gis-rag` at **127.0.0.1:8004** (confirmed). `jarvis-spiritual-rag` at **127.0.0.1:8005** (confirmed; earlier plan listed 8103). `jarvis-blood-brain-barrier` at **0.0.0.0:8016** (confirmed). `TruthValidator` and `normalize_identity` applied to every response. `background_rag_store` into `ms_jarvis_memory` after every `/chat` call. `truthverdict` attached to every `UltimateResponse`. For the canonical execution sequence see **Chapter 17**. |
| **Implemented now — meaning-oriented services (confirmed running but not all wired into `ultimatechat`)** | `jarvis-i-containers` at **8015** (confirmed); `icontainers-identity` layer confirmed `status: "active"` in 2026-02-15 `UltimateResponse` (Chapter 9 §9.3.5). `jarvis-qualia-engine` at **8017** (confirmed). `jarvis-neurobiological-master` at **8018** (confirmed). `jarvis-fifth-dgm` at **4002** (confirmed). `nbb-i-containers` at **127.0.0.1:8101** (confirmed). `jarvis-psychology-services` at **127.0.0.1:8019** (confirmed). `psychological_rag_domain` at **127.0.0.1:9006** (confirmed). `jarvis-temporal-consciousness` at **7007** (confirmed). `jarvis-mother-protocols` at **4000** (confirmed). `nbb_woah_algorithms` at **127.0.0.1:8104** (confirmed). |
| **Partially implemented / scaffolded** | Meaning-oriented modules listed above are running as services and are invoked in specific workflows and integration tests, but are **not currently wired into the primary `/chat` path** in `jarvis-main-brain`. The `consciousnesslayers` array in `UltimateResponse` records which meaning-oriented layers fired; in the 2026-02-15 case study only `prefrontal-planner` and `icontainers-identity` were active, with `nbb-prefrontal-cortex` skipped. MountainShares and Appalachian-wisdom integration modules are registered in the service registry but not confirmed as active in the current `ultimatechat` path. Cross-path routing that sends requests to the meaning-oriented track based on role flags or content type is partially implemented. |
| **Future work / design intent only** | Full wiring of all meaning-oriented modules into the `ultimatechat` entrypoint. Configurable per-track thresholds and routing rules. Automated cross-path analytics comparing meaning-oriented and analytical module usage. Dynamic track selection based on content classification. |

> **Critical routing note — asymmetry of the two paths:** As of February 2026, the `ultimatechat`
> entrypoint in `jarvis-main-brain` (port **8050**) **always runs the analytical path** —
> ensemble synthesis via `llm20production` plus judge pipeline, BBB truth filter, RAG context,
> and `background_rag_store`. Meaning-oriented modules are **partly present as confirmed running
> services** but are **not all plugged into the primary `/chat` path**. This asymmetry is a
> deliberate staged integration strategy, not a design gap. Chapters that describe both paths as
> equally live in `ultimatechat` should be corrected to reflect this. For the canonical execution
> sequence see **Chapter 17**.

---

# 23. Dual Tracks for Meaning-Oriented and Analytical Processing

This chapter describes how the three-stage structure outlined in earlier chapters is instantiated
in two parallel paths with different emphases. Both paths share the same overall pattern — intake
and normalization, first-stage filtering, background storage, and identity-focused retention —
but they differ in the kinds of services they invoke, what they prioritize, and how their outputs
are interpreted. In the current deployment, these two paths are **not symmetrically live** inside
the `ultimatechat` entrypoint: the analytical path always runs; the meaning-oriented path is
partly present as confirmed running services but not yet fully wired into every `/chat` call.

---

## 23.1 Rationale for Two Parallel Paths

The architecture exposes two conceptually distinct families of services.

**The meaning-oriented family** includes neurobiological and consciousness-related components:
Qualia Engine (`jarvis-qualia-engine`, port **8017**, confirmed running), I-Containers
(`jarvis-i-containers`, port **8015**, confirmed running), Neurobiological Master
(`jarvis-neurobiological-master`, port **8018**, confirmed running), Mother Protocols
(`jarvis-mother-protocols`, port **4000**, confirmed running), temporal consciousness
(`jarvis-temporal-consciousness`, port **7007**, confirmed running), NBB I-Containers
(`nbb-i-containers`, **127.0.0.1:8101**, confirmed running), psychology services
(`jarvis-psychology-services`, **127.0.0.1:8019**, confirmed running), and psychological RAG
domain (`psychological_rag_domain`, **127.0.0.1:9006**, confirmed running). In the current
deployment, a subset of these services respond with healthy status codes and are invoked in
specific workflows and integration tests, but **not all are wired into the primary `ultimatechat`
path**.

**The analytical family** includes RAG servers, GIS and GBIM bridges, GeoDB core services, truth
and BBB verification modules, and the LLM ensemble stack. In the current deployment, this is the
path that always runs in `ultimatechat`: `llm20production` synthesis via `jarvis-20llm-production`
(port **8008**, confirmed), judge pipeline (7230–7233, confirmed), `jarvis-spiritual-rag` (port
**8005**, confirmed), `jarvis-gis-rag` (port **8004**, confirmed), and `jarvis-blood-brain-barrier`
(port **8016**, confirmed). For the full sequence see **Chapter 17**.

Separating these concerns into two parallel paths allows the system to treat contexts involving
care, community, and personal meaning differently from contexts requiring focused technical
reasoning. At the same time, both paths operate within a shared container and orchestration
framework, making it possible to align their outputs and allow information to flow between them.

---

## 23.2 Shared Structural Pattern

In the current deployment, each path follows the same three-stage pattern.

**Intake and normalization.** Requests enter through `jarvis-main-brain` (port **8050**), where
they are parsed into `UltimateRequest` objects containing message, `userid`, role, and
`useallservices` flag. This normalized representation is shared across both tracks.

**First-stage filtering.** Fast, inexpensive filters apply safety, truth, and structural checks.
For both tracks, in the current deployment this includes BBB-based ethical filtering at port
**8016**, `TruthValidator`, `normalize_identity`, and simple structural heuristics in the main
brain. `ms_jarvis_memory` is append-only in the current deployment; near-duplicate checks
influence legacy RAG reuse but do not prevent writes. See **Chapter 20** for full detail.

**Background storage and identity-focused retention.** Both tracks feed into `ms_jarvis_memory`
via `background_rag_store`. Every successful `/chat` call produces a `bg_<ISO8601>` entry with
concatenated `USER:`/`EGERIA:` text and metadata including `userid`, `timestamp`, `type:
"background"`, and `services`. Over time, patterns detected in each track inform curated
identity-level updates. See **Chapters 20 and 22**.

---

## 23.3 Meaning-Oriented Path

**What is confirmed running.** In the current deployment, the following meaning-oriented services
are confirmed running: `jarvis-i-containers` (port **8015**), `jarvis-qualia-engine` (port
**8017**), `jarvis-neurobiological-master` (port **8018**), `jarvis-mother-protocols` (port
**4000**), `jarvis-temporal-consciousness` (port **7007**), `nbb-i-containers`
(**127.0.0.1:8101**), `jarvis-psychology-services` (**127.0.0.1:8019**), and
`psychological_rag_domain` (**127.0.0.1:9006**).

**What is wired into `ultimatechat`.** In the current deployment, of the meaning-oriented modules,
only `icontainers-identity` is confirmed active in the primary `/chat` path. The 2026-02-15
`UltimateResponse` showed `icontainers-identity` with `status: "active"` producing a real
`root-self` ego entry, and `nbb-prefrontal-cortex` with `status: "skipped"` and reason
`"nbbprefrontalcortex not configured"` (Chapter 9 §9.3.5). This contrast documents the asymmetry
precisely: one meaning-oriented layer was active, another was skipped, and the full
Neurobiological Master pipeline (BBB → I-containers → Qualia → consciousness bridge, Chapter 12)
was not invoked as part of that request.

**What the path provides when invoked.** When meaning-oriented modules are called — either in
the Neurobiological Master's own `integrated_processing()` flow or in specific workflows —
they contribute `consciousnesslayers` entries describing emotional resonance, spiritual filter,
maternal wisdom, subconscious processing, and `identitylayers` with ego boundary state. The
psychological RAG domain provides `psychological_assessment`, `therapeutic_guidance`,
`emotional_support`, and `evidence_based_approaches`. The design intends that these will be
fully integrated into the `ultimatechat` path as the system matures.

---

## 23.4 Analytical Path

**What always runs in `ultimatechat`.** In the current deployment, the analytical path is the
primary, always-active path for every `/chat` call through `jarvis-main-brain`.

RAG context is gathered from `jarvis-spiritual-rag` (port **8005**) and `jarvis-web-research`
(internal Docker network). Synthesis runs through `jarvis-20llm-production` (port **8008**) as
the production LLM ensemble fabric, confirmed by `servicesused: ["llm20production"]` in
`UltimateResponse`. The judge pipeline (truth 7230, consistency 7231, alignment 7232, ethics 7233)
evaluates ensemble output; if judge services are down, the main brain falls back to the 20-LLM
answer and marks consensus metrics as degraded (see **Chapter 33**). BBB at port **8016**
provides both input truth filtering and output guarding. `normalize_identity` and `TruthValidator`
enforce identity constraints. `background_rag_store` writes to `ms_jarvis_memory`. For the full
canonical sequence see **Chapter 17**.

GIS verification (`jarvis-gis-rag`, port **8004**), truth filters for registration and BBB
verification, and database health endpoints provide structured analytical grounding for spatial,
governance, and data-integrity questions.

---

## 23.5 Cross-Talk and Shared Anchors

In the current deployment, the two paths share several concrete integration points.

**Shared background store.** Both tracks write into `ms_jarvis_memory` via `background_rag_store`.
Background entries are distinguished by their `services` metadata and content, not by separate
collections. Similarity queries against `ms_jarvis_memory` return clusters of related items,
showing how both paths contribute to a common memory substrate.

**Shared identity infrastructure.** Both paths use the same `normalize_identity`, `TruthValidator`,
and `icontainers-identity` layer. The `truthverdict`, `consciousnesslayers`, and `identitylayers`
fields on `UltimateResponse` record the combined output of both path families for each request.

**Unified health monitoring.** In the current deployment, health and fabric self-test endpoints
report on both families of services, listing Qualia Engine, I-Containers, NBB adapters, the
ensemble LLM fabric, RAG, and others. This makes it possible to monitor whether one path is
lagging or failing.

**Linked orchestration.** The design intends that unified orchestrators will construct responses
containing both AI/technical analysis and spiritual/meaning analysis in a single composite reply.
In the current deployment, this integration is partial: the analytical response is always present,
meaning-oriented `consciousnesslayers` are present when their services are wired in, and the
`identitylayers` ego entry is confirmed active.

---

## 23.6 Influence on Behavior and Explanation

In the current deployment, the existence of two paths — one always-active, one partially wired —
affects how the system behaves and explains itself.

**Response composition.** For a given `/chat` request, in the current deployment the main brain
returns a composite `UltimateResponse` containing `response` (from `llm20production`),
`truthverdict` (from BBB), `consciousnesslayers` (always including `prefrontal-planner`; including
`icontainers-identity` when active), and `identitylayers` (including `root-self` ego entry when
`icontainers-identity` fires). Meaning-oriented fields such as `psychological_assessment` or
`mountainsharescontext` appear when those modules are explicitly invoked, not on every call.

**Framing and narrative.** In the current deployment, introspective reports and explanatory text
can reference both tracks, explaining which analytical modules (ensemble LLMs, GIS, truth
filters) and which meaning-oriented modules (psychology, maternal guidance, I-containers) were
active for a given request. The `consciousnesslayers` skipped/active distinction (Chapter 9
§9.3.5) provides auditors with precise evidence of which modules fired.

**Diagnostics and balance.** Because services in both tracks are registered and health-monitored,
diagnostic tools can show which path is being exercised more heavily for particular topics or
regions. In the current deployment, logs and `ms_jarvis_memory` contents reveal that the
analytical path dominates ordinary `/chat` calls, with meaning-oriented layers contributing
where specifically wired.

---

## 23.7 Summary

In the current deployment, the dual-track design is **asymmetric at the `ultimatechat` entrypoint**.
The analytical path — ensemble synthesis via `llm20production`, judge pipeline, BBB filtering,
RAG context, and `background_rag_store` — runs on every `/chat` call and is the current
production path. Meaning-oriented modules are confirmed running as services (Qualia Engine,
I-Containers, Neurobiological Master, psychology services, Mother Protocols, temporal
consciousness) and are active in specific workflows and integration tests, but are **not all
plugged into the primary `/chat` path** as of February 2026.

Both paths share the same intake framework, feed into `ms_jarvis_memory`, and contribute to the
compact identity layer governed by `normalize_identity` and `TruthValidator`. The
`consciousnesslayers` and `identitylayers` fields on `UltimateResponse` provide transparent,
per-request evidence of which layers from each path were active. The design intends that future
work will fully wire meaning-oriented modules into the `ultimatechat` entrypoint. For the
canonical execution sequence, see **Chapter 17**. For the Neurobiological Master's own meaning-
oriented pipeline, see **Chapter 12**.
