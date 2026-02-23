## Why this matters for Polymathmatic Geography

This chapter specifies how Ms. Jarvis’s language models are bound to *place‑aware, collection‑aware, and registry‑aware memory* instead of free‑floating text generation. It makes the Hilbert‑space, GBIM structures, Chroma‑backed semantic memory, and the verified local resource registry from earlier chapters operational by defining concrete services that retrieve from semantic memory, the spatial body, the web, and structured program tables. In the current deployment, this design is realized as a production RAG stack that delivers West Virginia benefits intelligence through a 21‑model consciousness bridge anchored in ChromaDB, GBIM‑derived entities, GIS‑aware collections, and a WV‑first routing policy. It supports:  
- **P1 – Every where is entangled** by requiring that answers emerge from an entangled memory of governance texts, spatial layers, research notes, belief structures, and local resource registries, rather than from an abstract model prior.  
- **P3 – Power has a geometry** by letting retrieval paths expose which collections—and thus which institutional, spatial, and programmatic perspectives—shape a given answer, including WV‑specific benefits facilities in `gis_wv_benefits`, spatial entities derived from GBIM and GeoDB, and benefits‑focused resource collections.  
- **P5 – Design is a geographic act** by treating routing rules, collection choices, registry lookups, and gateway boundaries as design decisions that change how the system “sees” and acts within a region.  
- **P12 – Intelligence with a ZIP code** by privileging West Virginia‑specific collections in retrieval, and by coupling text RAG both to a state‑scale GeoDB/GBIM spatial body for spatial questions and to a ZIP‑ and county‑aware `local_resources` registry for concrete program referrals, including flows for Oak Hill, Beckley, and broader Fayette/Raleigh County.  
- **P16 – Power accountable to place** by making retrieval calls, filters, scores, registry lookups, and sources visible at the API and logging layer so that communities and researchers can audit what informed a Steward response.  

As such, this chapter belongs to the **Computational Instrument** tier: it defines the retrieval and routing machinery that connects Chroma‑backed semantic memory, the GBIM/GeoDB spatial body, the verified local resource registry, and web research to the live outputs of Ms. Jarvis.

---

## 7.0 Overview and Scope

This chapter describes the retrieval‑augmented generation (RAG) infrastructure that binds Ms. Egeria Jarvis’s language models to the semantic and spatial memory systems defined in earlier chapters. In the current deployment, language models are no longer queried “from scratch”: they are constrained and informed by:

- a text RAG service backed by a shared HTTP‑exposed ChromaDB instance,  
- a GeoDB‑coupled GIS RAG path for West Virginia features built on GBIM‑derived spatial entities and `gis_wv_benefits`,  
- a web‑research gateway, and  
- a resolver path into the `local_resources` registry for programmatic help,

all orchestrated by the main brain and blood–brain‑barrier services.

At runtime, queries enter through a unified HTTP gateway (for example, `POST /chat/sync` on a front‑door port) and are routed by the main brain into a RAG layer that spans Chroma collections, GIS features, and verified local‑resource rows. In production as of February 2026, the full pipeline

```text
Unified Gateway → Main Brain → RAG (text + GIS + registry, WV‑first) → 21‑LLM ensemble → Blood–Brain Barrier
```

is live and serving West Virginia benefits and geography questions. For WV‑scoped queries, the main brain treats West Virginia RAG as mandatory and suppresses generic web context when a county or WV role/profile is present, so that out‑of‑state material cannot quietly override in‑state evidence.

A typical benefits query such as:

```bash
curl -X POST http://127.0.0.1:8050/chat/sync \
  -H "Content-Type: application/json" \
  -H "X-API-Key: super-secret-key" \
  -d '{"message":"Oak Hill WV county benefits","county":"Fayette","role":"community","profile":"auto"}'
```

triggers retrieval from ChromaDB (including WV‑relevant collections such as governance, thesis, and `gis_wv_benefits`), optional GIS RAG over GBIM‑derived spatial entities, synthesis by the 21‑model `llm20_production` ensemble, and post‑filtering by the guardrail service, with WV RAG, GIS context, and `local_resources` treated as authoritative when they conflict with external web information.

Within the overall architecture, the RAG layer is the primary bridge between relatively slow‑changing long‑term memory (Chroma collections, PostGIS/GeoDB, and structured registries like `local_resources`) and fast, per‑query reasoning in the language models. It is also the place where the Hilbert‑space state metaphor becomes operational: each RAG call carves out a small, query‑conditioned subspace of the much larger semantic, spatial, institutional, and program state space, and hands that subspace to the models as their working context. Finally, the retrieval services provide concrete, inspectable interfaces where retrieval calls, filters, and source collections can be logged, audited, and tuned in service of the program’s glassbox and spatial‑justice commitments.

![Ms. Jarvis RAG Pipeline Architecture](https://github.com/user-attachments/assets/bfc8d3b1-90aa-478a-bb8d-85e9b98640d0)

Figure 7‑1. Retrieval‑augmented generation (RAG) pipeline overview linking the unified gateway, main‑brain orchestration, and ensemble‑guarded outputs. Author’s diagram, 2026.

---

## 7.1 Alignment with GBIM, Hilbert Space, Semantic Memory, GeoDB, and Registries

The GeoBelief Information Model (GBIM) defines how entities, places, and normative claims are represented across documents and spatial features. The RAG layer is the mechanism that actually retrieves those GBIM‑anchored fragments when a question is asked. GBIM worldview entities and other beliefs are surfaced into Chroma as metadata‑rich records, and the RAG services are structured so they can filter, group, and boost results by these identifiers as metadata coverage matures.

The Hilbert‑space state view treats the system’s overall knowledge and constraints as a very high‑dimensional state vector. RAG interactions can be understood as projections into lower‑dimensional subspaces that correspond to “what matters for this query, given this role and place.” For text, those projections are implemented as embedding‑based nearest‑neighbor searches in Chroma collections. For space, they are implemented as centroid‑based spatial filters over GeoDB‑derived features and as neighborhood queries over GBIM‑linked spatial entities. For concrete help‑seeking and program questions, retrieved resource documents and metadata are further resolved into rows of the `local_resources` table keyed by ZIP, county, and program type, which are themselves part of the structured Hilbert‑space state.

Chroma‑backed semantic memory (Chapter 5) is the substrate for governance texts, thesis fragments, research notes, GBIM worldview entities, and resource guides, while GeoDB and GBIM (Chapter 6) define the spatial body composed of PostGIS layers and exported worldview entities. The text RAG server is the front‑door to semantic memory: it queries explicitly named Chroma collections, respects metadata filters such as source, county, dataset, or worldview, and returns scored snippets along with their provenance. The GIS RAG service plays the parallel role for the spatial body: it queries geospatial collections such as GBIM‑derived spatial entities and `gis_wv_benefits`, and returns entities with dataset names, centroids, and core attributes that can be rendered, reasoned about, or further filtered upstream. For local‑resource questions, a dedicated resolver component uses RAG outputs and structured hints (such as county, ZIP, `resource_type`, and `local_resource_id`) to look up matching rows in `local_resources`, ensuring that final recommendations rest on explicit, versioned program records rather than unstructured text alone.

In the February 2026 deployment, this alignment is implemented concretely:

- Chroma collections like GBIM‑derived spatial indexes, general semantic collections (governance, thesis, research), and `gis_wv_benefits` for West Virginia‑specific benefits facilities are configured at embedding dimension 384 and accessed over a shared HTTP Chroma service.  
- GIS RAG queries can reference metadata such as `worldview_id`, `county`, `dataset`, and `gbim_entity` to tie vector results back to GBIM and GeoDB.  
- Resource‑related collections tag documents with `local_resource_id`, allowing RAG hits to be resolved to `local_resources` rows for facilities in Oak Hill, Beckley, and surrounding ZIP codes.

---

## 7.2 Core RAG and Search Components

At the implementation level, the retrieval layer now consists of four main retrieval services, a registry resolver, and orchestration:

![The Ms. Jarvis RAG Pipeline](https://github.com/user-attachments/assets/b32e580e-1673-4db1-94ec-abde0bc441d5)

Figure 7‑2. Core retrieval components composing the Ms. Jarvis RAG layer. Author’s diagram, 2026.

- A text RAG service backed by ChromaDB.  
- A GIS RAG path that treats geospatial features and GBIM‑linked entities as semantic objects with coordinates.  
- A web‑research gateway for external information.  
- A local resource registry resolver wired to `local_resources`.  
- A main brain + orchestrator that routes requests and assembles context for the 21‑model `llm20_production` ensemble, with WV‑first rules for state‑scoped queries.

### 7.2.1 Text RAG Service (ChromaDB‑Backed)

The text RAG service exposes a structured HTTP API (used internally by `/chat/light` and `/chat/sync`) that takes a query string, a `top_k` parameter, optional metadata filters (such as collection, source, county, dataset, or worldview), and optional role and geography hints. It issues similarity searches against one or more Chroma collections using a 384‑dimensional sentence‑embedding model, and returns both a flat list of top results and a `results_by_source` mapping keyed by collection name. Each result item carries:

- The retrieved text snippet or document identifier.  
- Collection and source names.  
- Metadata fields (for example, dataset, `worldview_id`, county, `local_resource_id`).  
- A similarity‑derived score.

From the Hilbert‑space perspective, each collection represents a finite subset of the component spaces \(H_{\text{text}}, H_{\text{geo}}, H_{\text{inst}}\), and the RAG query selects a neighborhood around the embedded query vector. From the GBIM perspective, the same calls return belief fragments whose provenance and `worldview_id` can be inspected and composed.

In production, typical text RAG behavior is exercised through the unified chat endpoints, for example:

```bash
curl -X POST http://127.0.0.1:8050/chat/light \
  -H "Content-Type: application/json" \
  -H "X-API-Key: super-secret-key" \
  -d '{"message":"Raleigh County WV benefits summary","role":"community"}'
```

which yields fast, Chroma‑conditioned responses about SNAP, Medicaid, and related programs, with WV collections and benefits‑specific facilities preferred when the query or caller indicates a West Virginia context.

### 7.2.2 GIS RAG Service (GeoDB/GBIM‑Backed)

The GIS RAG service is a dedicated geospatial retrieval path that serves West Virginia‑focused spatial questions. Logically, it exposes an endpoint (for example, `/gis_rag`) that accepts a natural‑language query and an `n_results` parameter and returns a list of spatial hits. Internally, it queries:

- a consolidated GBIM‑derived spatial collection that embeds worldview entities and their spatial metadata, and  
- the `gis_wv_benefits` collection, which stores semantic descriptions and metadata for benefits‑related facilities such as Oak Hill hubs and Beckley DHHR offices.

Each indexed entity stores a short text description and metadata fields such as `worldview_id`, `dataset`, `county`, `gbim_entity`, `centroid_x`, and `centroid_y`. The centroids in SRID 26917 are also transformed to EPSG:4326 for map display and simple geographic filtering.

For example, benefits facilities are added and queried via code analogous to:

```python
import chromadb

client = chromadb.HttpClient(host="jarvis-chroma", port=8000)
col = client.get_or_create_collection("gis_wv_benefits")

col.add(
    documents=[
        "Oak Hill WV FAYETTE County SNAP WIC Medicaid hub (New River Health District)",
        "Beckley WV DHHR benefits office social services hub",
        "New River Health Oak Hill clinic medical assistance"
    ],
    metadatas=[
        {"worldview_id": "wv_benefits_2026", "county": "Fayette", "gbim_entity": "oak_hill_fayette_corrected"},
        {"worldview_id": "wv_benefits_2026", "county": "Raleigh", "gbim_entity": "beckley_dhhr"},
        {"worldview_id": "wv_benefits_2026", "county": "Fayette", "gbim_entity": "new_river_health"}
    ],
    ids=["gbim001", "gbim002", "gbim003"]
)
```

GIS RAG outputs are designed to be composable with text RAG outputs: each hit is both a semantic object (a facility, boundary, or infrastructure feature) and a spatial object (with coordinates, SRID, and GBIM identifiers) that the main brain can reason about in the same Hilbert‑space frame.

### 7.2.3 Web Research Gateway

External web retrieval is handled by a dedicated gateway rather than allowing arbitrary outbound calls from each agent or service. This gateway exposes an HTTP endpoint that accepts a JSON body with a query string and a limit on the number of results. It:

- Applies policy filters and rate limits to outbound web access.  
- Normalizes results into a uniform structure with fields like `title`, `snippet`, `url`, `source`, and sometimes `published_at`.  
- Logs queries and responses for audit and debugging.

In the WV‑first design, the main brain only admits web context into the ultimate context window for non‑WV or clearly extra‑state questions. When a query is WV‑scoped (for example, has a West Virginia county or uses a WV benefits profile/role), web context is deliberately excluded so that external search results cannot override the in‑state RAG, GIS, and registry evidence.

### 7.2.4 Local Resource Registry Resolver

The local resource resolver is a thin service or module that sits alongside text and GIS RAG. It does not perform embedding search itself. Instead, it:

- Accepts structured hints such as `county`, `zip`, and `resource_type`, plus optional keys such as `local_resource_id` coming from RAG metadata.  
- Queries the `local_resources` Postgres table for rows that match these constraints and have an acceptable `verification_status`.  
- Returns normalized program records with fields like `name`, `description`, `contact_phone`, `contact_email`, `url`, `zip_coverage`, `last_verified_at`, and internal IDs.

In help‑seeking flows, the main brain uses RAG primarily to interpret the question and surface relevant resource descriptions, then delegates final program selection to this resolver so that recommendations are grounded in a maintained, auditable registry rather than in unstructured text alone.

### 7.2.5 Orchestration and Main Brain

The main brain does not typically call language models directly. Instead, it routes each job through an orchestration layer that decides whether to invoke the text RAG service, the GIS RAG service, the web gateway, the local resource resolver, or some combination, based on:

- The request type (for example, policy question, spatial query, resource lookup, system status).  
- The active role (for example, researcher, governance engineer, community‑facing advisor).  
- Any explicit or inferred geography (for example, county, ZIP, worldview region).

The same orchestration layer composes the final context window for the models and sends candidate responses through downstream guardrail services such as the blood–brain barrier.

In production, orchestration calls into a 21‑model ensemble service (`llm20_production`), which sequentially queries a set of model proxies and aggregates their outputs:

```text
llm20_production:
  🌟 Processing 21 models sequentially via proxies...
  ✅ Complete: 21/21 responded
```

For WV‑scoped queries, the main brain:

- Treats WV RAG (text + GIS + registry) as mandatory input.  
- Builds a WV‑first context window from RAG, GIS, and registry material, excluding `web_context`.  
- Prepends a strong grounding instruction that explicitly tells the ensemble to treat WV RAG, GIS context, and `local_resources` as authoritative for West Virginia and to ignore conflicting out‑of‑state information unless the user clearly asks about another state.

Ensemble outputs are then filtered by the blood–brain‑barrier and returned via `/chat/sync` or `/chat/light`.

---

## 7.3 Retrieval Flows

This section sketches the typical flows for non‑spatial, spatial, and resource‑oriented queries. In each case, the retrieval layer is where abstract Hilbert‑space projections and GBIM entities become concrete calls and responses.

### 7.3.1 Non‑Spatial RAG Flow

A typical governance or thesis question (for example, about MountainShares rules or Ms. Jarvis architecture) progresses as follows:

**Query intake.**  
A user or upstream component sends a request to the unified gateway or main brain. The main brain wraps it into an internal job structure containing the raw text, any structured fields (project, county, worldview), and role hints.

**Routing to text RAG and/or web.**  
The orchestration logic decides whether to call the local text RAG service, the web gateway, or both. For most governance‑ and thesis‑style questions, it prefers Chroma‑backed collections (for example, governance, thesis, GBIM, or MountainShares collections) and only consults the web when the question clearly depends on external or time‑varying facts.

**Retrieval from ChromaDB.**  
The text RAG service embeds the query, runs similarity search against the selected collections, and returns high‑scoring documents and their metadata. Collection selection and metadata filters act as an early constraint layer, narrowing the effective Hilbert‑space subspace from “all memory” to “things plausibly relevant to this query and role.”

**Context assembly.**  
The orchestration layer merges the retrieved items into a context window alongside system prompts, role‑specific instructions, and any web‑research snippets (if allowed). Source separation is preserved where possible, so governance texts, GBIM descriptions, and thesis excerpts remain distinguishable.

**Generation and guarding.**  
One or more language models generate an answer conditioned on this assembled context. The main brain then routes the candidate answer through the blood–brain barrier service, which can rewrite, annotate, or reject outputs that violate constitutional, safety, or scope rules.

### 7.3.2 Spatial RAG Flow

![Ms. Jarvis Production RAG Architecture](https://github.com/user-attachments/assets/e65c5ec6-3c72-430e-85cc-de94fd341aa8)

Figure 7‑3. Comparison of semantic (embedding‑based) and spatial (geographic‑filter) retrieval operations. Author’s figure, 2026.

Spatially explicit questions (for example, “roads in Fayette County,” “hospitals near Oak Hill,” or “which buildings lie in this floodplain?”) introduce the GIS RAG path:

**Spatial query intake.**  
The main brain or a spatially aware client calls the GIS RAG endpoint with a natural‑language query and `n_results`, and may additionally pass a center point, bounding box, county, or GBIM region identifier if known.

**Semantic and spatial retrieval.**  
The GIS RAG service embeds the query and runs similarity search over geospatial Chroma collections such as GBIM‑derived spatial entities and, for benefits queries, `gis_wv_benefits`. Because each entity includes centroids and region metadata, the service or caller can then apply geometric or administrative filters (for example, restricting to features within a bounding box around Oak Hill or within Fayette County).

**Return of geospatial hits.**  
The service returns a list of hits, each including a compact textual description, the source dataset or layer name, a feature label, metadata (`worldview_id`, `dataset`, `county`, `gbim_entity`), and coordinates. Upstream, these hits can be:

- Shown directly in map or tabular form.  
- Used to fetch richer GBIM records or PostGIS geometries.  
- Combined with text RAG results and registry entries to provide mixed semantic and spatial evidence to the language models.

In more fully integrated configurations, this flow is implemented entirely over a GBIM‑anchored spatial collection, so that spatial RAG can see both features and their GBIM belief states and edges.

### 7.3.3 Resource‑Oriented RAG Flow

Help‑seeking or resource questions (for example, “What Christmas help is available in Oak Hill this year?” or “Where can a grandmother in ZIP 25840 get utility assistance?”) combine semantic retrieval with structured registry lookups:

**Resource query intake.**  
The main brain receives the question and identifies it as a resource‑oriented request, extracting any available location hints (ZIP, county, town) and population signals (for example, “grandmother,” “teacher,” “family with kids”).

**Interpretation via text and spatial RAG.**  
Text RAG and/or GIS RAG can be used to interpret ambiguous language and, where appropriate, retrieve resource guides, flyers, benefits facilities, or prior notes related to the apparent need category (such as seasonal assistance or utility help). These hits may carry `local_resource_id` and `county` metadata linking them to structured registry entries.

**Resolution via local resource resolver.**  
The local resource resolver queries `local_resources` using structured hints (ZIP, county, `resource_type`) and any concrete IDs, returning candidate program rows that are currently verified or recently verified.

**Context assembly and generation.**  
The orchestration layer builds a context that includes both unstructured descriptions (for narrative framing) and structured fields from `local_resources` (for factual details such as phones, emails, deadlines, and coverage). Language models generate answers that explicitly reference the structured fields, and post‑processing may attach program names and contacts in a form suitable for copying or downstream display.

In all cases, the intent is that referrals are anchored in `local_resources` entries whose lifecycle (creation, update, verification, deprecation) is under explicit community governance, rather than in opaque semantic similarity alone.

---

## 7.4 Routing, Roles, Geography, and WV‑First Policy

Routing is conceptually central to the RAG design. It is meant to be GBIM‑aware, role‑aware, geography‑aware, registry‑aware, and, in the current deployment, explicitly WV‑first for West Virginia–scoped questions.

### 7.4.1 Design Intent

On the design side:

**Topic and intent routing.**  
The system should distinguish between queries about governance, geospatial context, thesis theory, MountainShares economics, resource and referral questions, and infrastructure status, and route each toward appropriate services and collections. Governance queries should favor charters, policies, and DAO records; spatial‑justice queries should favor GBIM and GeoDB‑derived collections; resource questions should favor `local_resources` plus WV‑resource collections.

**Role‑aware routing.**  
The active role (for example, researcher, governance engineer, community‑facing advisor) should determine which collections and registries are even eligible. Internal or sensitive material should only be surfaced for trusted roles, while community‑facing roles should be restricted to public documentation, approved spatial layers, and public‑facing slices of `local_resources`.

**Geography‑aware routing and WV‑first behavior.**  
Queries with explicit or implicit place references should steer retrieval toward collections that encode GBIM entities, GBIM‑derived spatial entities, GeoDB/PostGIS features, and `local_resources` rows in the relevant region. For West Virginia, the design goes further: whenever a query is WV‑scoped (for example, includes a WV county or uses a WV benefits profile/role), the system should:

- Treat WV RAG, GIS, and registry context as the authoritative sources.  
- Exclude web context from the final assembled context window.  
- Require models to ignore conflicting out‑of‑state content unless the user explicitly requests another state.

### 7.4.2 Current Implementation

![Intelligence with a ZIP Code](https://github.com/user-attachments/assets/6bb444a3-49e2-4770-b099-435678693603)

Figure 7‑4. Geography‑aware routing and data prioritization in the Ms. Jarvis retrieval layer for Fayette and Raleigh Counties, West Virginia. Author’s map, 2026.

As of early 2026:

- The text RAG API exposes optional `role` and `geography` fields and uses them to choose which Chroma collections to query and how to construct metadata filters. Many collections are only partially annotated, so behavior defaults to broader retrieval when metadata is missing, but WV‑specific benefits and governance collections are explicitly favored for WV benefits flows.  
- The GIS RAG service is focused on West Virginia, indexing GBIM‑ and GeoDB‑derived layers and benefits facilities (`gis_wv_benefits`), with centroids standardized to SRID 26917 and transformed to WGS84 when needed.  
- The local resource resolver is wired to the `local_resources` table and can be called explicitly when a flow is tagged as resource‑oriented; integration with role‑ and geography‑aware routing is being expanded as registries and policies are hardened.  
- Routing decisions are implemented as explicit function calls and configuration in the orchestration layer rather than as learned classifiers, keeping behavior legible and debuggable.  
- In the main brain’s ultimate path, context assembly computes a WV‑scoped flag based on county and role, builds `context_block` from `[rag_context, gis_context, registry_context]` for WV queries (dropping `web_context`), and injects a strong WV grounding instruction that tells the ensemble to treat WV RAG, GIS context, and `local_resources` as authoritative and to treat conflicting web or generic information as out‑of‑state and ignorable.

In practice, the retrieval layer already has the shape of a role‑, geography‑, and registry‑sensitive interface, with WV‑first behavior in place for benefits flows.

---

## 7.5 Context Construction and Structure

How retrieved material is structured for the language model is itself a significant design choice. The retrieval servers adopt several principles to keep context both usable and inspectable.

**Source separation.**  
The text RAG service returns a `results_by_source` dictionary keyed by collection name, and each item carries `collection`, `source`, and `metadata` fields. The GIS RAG service returns dataset names and feature labels with spatial metadata. The local resource resolver returns normalized rows from `local_resources` with clearly typed fields. Upstream logic uses these to keep, for example, governance documents distinct from research notes, spatial features distinct from narrative descriptions, and program registries distinct from unstructured flyers.

**Relevance ordering and bounded size.**  
Chroma returns distances, which the services convert into scores; flat results are sorted in descending score order. Clients specify `top_k` per collection or `n_results` per GIS query, and the services enforce these limits, preventing over‑large contexts while still allowing multiple collections to contribute. For registry lookups, the resolver limits results by geography and `resource_type`, and upstream logic may cap the number of programs presented at once.

**Role‑, geography‑, and WV‑aware scaffolding.**  
Where role and geography are known, upstream prompt builders can add headers or structure that make those constraints explicit (for example, “You are advising a community organization in Fayette County, WV; prioritize GBIM, GeoDB, Chroma RAG, and `local_resources` evidence for this region.”). For WV‑scoped queries, the ultimate prompt spells out that WV RAG and GIS context are authoritative, that web snippets are absent, and that any registry entries included represent current, community‑governed knowledge of local programs.

![RAG Pipeline Overview Diagram](https://github.com/user-attachments/assets/aa80b5d0-e6d8-4f45-a65c-5c9362f141c9)

Figure 7‑5. Structure of contextual input assembled for language‑model reasoning by the retrieval orchestration layer. Author’s diagram, 2026.

The combination of collection‑aware grouping, explicit scores, registry‑based fields, bounded retrieval, WV‑first context assembly for WV queries, and explicit grounding instructions gives the language model a context that is closer to an evidence set than an undifferentiated text blob. As metadata schemas mature, this same structure will support richer tracing from answers back to the specific documents, beliefs, spatial features, and registry entries that informed them.

---

## 7.6 Constraints, Provenance, and Logging

Constitutional and ethical constraints in the present system interact with the retrieval pipeline at several points.

**Pre‑retrieval and retrieval‑time constraints.**  
Collection selection and filter mechanisms already support limiting retrieval by collection, source, county, dataset, worldview, and state. The APIs include `role` and `geography` fields that will govern access‑level and spatial filters more tightly as metadata is filled in. For WV‑scoped queries, context assembly enforces a hard separation between WV evidence (RAG + GIS + registries) and generic web content by excluding `web_context` outright from the ultimate prompt.

**Decoding‑time guards.**  
After retrieval and generation, the main brain routes candidate responses through the blood–brain barrier service, which can refuse, rewrite, or annotate outputs that violate constitutional or safety principles. This decoding‑time guard operates over the final answer, regardless of which retrieval path produced it, and complements earlier filters. In WV‑scoped flows, the guardrail is applied after the WV‑first context and instructions have already constrained the ensemble’s behavior.

![Provenance and Logging RAG Pipeline](https://github.com/user-attachments/assets/73553e5a-e192-4878-86b3-5be580d6cc4a)

Figure 7‑6. Provenance and guardrail flow ensuring accountable generation in the Ms. Jarvis retrieval pipeline. Author’s figure, 2026.

**Post‑hoc review and logging.**  
The retrieval server supports background storage of queries and responses into a conversation‑history collection. Logs capture which services were called, which collections were queried, which filters and scores were applied, which registries were accessed, and which documents or features were returned. A fully structured, user‑facing explanation interface—where Ms. Jarvis can explicitly list the documents, spatial features, and registry entries relied upon—is marked as future work.

Together, these mechanisms move the system away from unconstrained text generation toward a constrained, accountable pipeline, while leaving room to tighten role‑, geography‑, registry‑, and WV‑specific policies as the underlying memory schemas stabilize.

---

## 7.7 Relation to Long‑Term Memory, GeoDB, Registries, and Entanglement

The retrieval layer sits between relatively static long‑term memory and dynamic, per‑query reasoning, and it is the primary place where semantic, spatial, and institutional representations are expected to meet.

**Long‑term memory.**  
ChromaDB collections hold embedded representations of governance documents, project‑specific knowledge, GBIM worldview entities, West Virginia benefits facilities, and other curated materials, configured at 384 dimensions. Structured tables such as `local_resources` hold normalized, versioned records that are not embedded directly but are addressable via RAG‑inferred keys, geography, and explicit `local_resource_id` metadata in Chroma. GBIM and GeoDB tables encode belief graphs and spatial bodies that can be reached via `entity_id`, `source_table`, and `source_pk` fields returned in Chroma metadata.

**Short‑term context.**  
Each retrieval call assembles a temporary context window from the retrieved items, sorted by relevance and grouped by collection, layer, and registry. This window serves as the immediate working memory for the language models and orchestration services as they construct an answer. For WV‑scoped queries, this window is explicitly WV‑first: it is assembled from West Virginia RAG, GIS, and registry material, with web content excluded and a grounding instruction that spells out how to handle conflicts.

**Coupled updates and future entanglement.**  
The broader entanglement concept envisions updates to semantic memory, spatial layers, registries like `local_resources`, GBIM belief structures, and normative constraints as mutually influencing. The current implementation does not fully realize this; instead, it provides a stable, inspectable interface that can later be extended with richer entanglement‑aware routing, access policies, and metadata propagation across collections and registries, including automated updates when WV program verification or worldview changes occur.

In this way, the present retrieval deployment should be understood as a working but intentionally conservative layer. It already anchors Ms. Jarvis’s outputs in named collections, explicit retrieval calls, and structured registry lookups—including a concrete WV‑first path from GBIM/GeoDB spatial features and from `local_resources` program records into generation—but it still relies on forthcoming work in metadata design, spatial integration, registry governance, and explanation tooling to fully satisfy the program’s glassbox and spatial‑justice commitments.
