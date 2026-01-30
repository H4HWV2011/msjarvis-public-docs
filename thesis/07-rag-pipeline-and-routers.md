# 7. RAG Pipeline and Routers

> **Why this matters for Polymathmatic Geography**  
> This chapter specifies how Ms. Jarvis’s language models are bound to *place‑aware, collection‑aware memory* instead of free‑floating text generation. It makes the Hilbert‑space and GBIM structures from earlier chapters operational by defining concrete services that retrieve from semantic memory, the spatial body, and the web. It supports:  
> - **P1 – Every where is entangled** by requiring that answers emerge from an entangled memory of governance texts, spatial layers, and research notes, rather than from an abstract model prior.  
> - **P3 – Power has a geometry** by letting retrieval paths expose which collections—and thus which institutional and spatial perspectives—shape a given answer.  
> - **P5 – Design is a geographic act** by treating routing rules, collection choices, and gateway boundaries as design decisions that change how the system “sees” and acts within a region.  
> - **P12 – Intelligence with a ZIP code** by privileging West Virginia and MountainShares‑specific collections in retrieval, and by coupling text RAG to a state‑scale GeoDB and GBIM worldview entities for spatial questions.  
> - **P16 – Power accountable to place** by making retrieval calls, filters, and sources visible at the API level so that communities and researchers can audit what informed a Steward response.  
> As such, this chapter belongs to the **Computational Instrument** tier: it defines the retrieval and routing machinery that connects Chroma‑backed semantic memory, the GBIM/GeoDB spatial body, and web research to the live outputs of Ms. Jarvis.

---

## 7.0 Overview and Scope

This chapter describes the retrieval‑augmented generation (RAG) infrastructure that binds Ms. Egeria Jarvis’s language models to the semantic and spatial memory systems defined in Chapters 2, 4, 5, and 6. In the current deployment, language models are no longer queried “from scratch”: they are constrained and informed by a text RAG service backed by ChromaDB, a GeoDB‑coupled GIS RAG endpoint for West Virginia features, and a web‑research gateway, all orchestrated by the main brain and blood–brain‑barrier services.

Within the overall architecture, the RAG layer is the primary bridge between relatively slow‑changing long‑term memory (Chroma collections and PostGIS/GeoDB) and fast, per‑query reasoning in the language models. It is also the place where the Hilbert‑space state metaphor from Chapter 4 becomes operational: each RAG call carves out a small, query‑conditioned subspace of the much larger semantic and spatial state space, and hands that subspace to the models as their working context. Finally, the RAG services provide concrete, inspectable interfaces where retrieval calls, filters, and source collections can be logged, audited, and tuned in service of the program’s glassbox and spatial‑justice commitments.

---

## 7.1 Alignment with GBIM, Hilbert Space, Semantic Memory, and GeoDB

The GeoBelief Information Model (GBIM) introduced in Chapter 2 defines how entities, places, and normative claims are represented across documents and spatial features. The RAG layer is the mechanism that actually retrieves those GBIM‑anchored fragments when a question is asked. GBIM identifiers and worldview entities are surfaced into Chroma as metadata (for example, in the `gbim_worldview_entities` collection) and into GIS‑RAG‑specific collections derived from the geospatial_features table; the RAG services are structured so they can increasingly filter and group results by these identifiers as metadata matures.

The Hilbert‑space state view from Chapter 4 treats the system’s overall knowledge and constraints as a very high‑dimensional state vector. RAG interactions can be understood as projections into lower‑dimensional subspaces that correspond to “what matters for this query, given this role and place.” For text, those projections are implemented as embedding‑based nearest‑neighbor searches in Chroma collections; for space, they are implemented as centroid‑based spatial filters over GeoDB‑derived features transformed into a common WGS84 coordinate system and, at GBIM scale, as neighborhood queries over `gbim_worldview_entities`.

Chapter 5 defines Chroma‑backed semantic memory as the substrate for governance texts, thesis fragments, research notes, and other curated materials, while Chapter 6 defines the GeoDB as the system’s spatial body composed of PostGIS layers and derived geospatial features. The text RAG server is the front‑door to semantic memory: it queries explicitly named Chroma collections, respects metadata filters such as source, county, or worldview, and returns scored snippets along with their provenance. The GIS RAG service plays the same role for the spatial body: it queries a geospatial Chroma collection built from the GeoDB’s geospatial_features or GBIM exports, and returns features with layer names, derived centroids, and high‑level attributes that can be rendered, reasoned about, or further filtered upstream.

---

## 7.2 Core RAG Components

At the implementation level, the RAG layer consists of three main services plus orchestration.

### 7.2.1 Text RAG Service (ChromaDB‑Backed)

The text RAG service exposes a structured HTTP API (for example, `/search`) that takes a query string, a `top_k` parameter, optional metadata filters (such as collection, source, county, worldview, or state), and optional `role` and `geography` hints. It issues similarity searches against one or more Chroma collections using sentence‑embedding models, and returns both a flat list of top results and a `results_by_source` mapping keyed by collection name. Each result item carries:

- The retrieved text snippet or document identifier.
- Collection and source names.
- Metadata fields (for example, dataset, worldview_id, county, layer).
- A similarity‑derived score.

From the Hilbert‑space perspective, each collection represents a finite subset of the component spaces \(H_{\text{text}}\), \(H_{\text{geo}}\), or \(H_{\text{inst}}\), and the RAG query selects a neighborhood around the embedded query vector. From the GBIM perspective, the same calls return belief fragments whose `belief_state` and provenance fields can be inspected and composed.

### 7.2.2 GIS RAG Service (GeoDB/GBIM‑Backed)

The GIS RAG service is a dedicated FastAPI application that serves geospatial retrieval, currently focused on West Virginia. It exposes a `/gis_rag` endpoint that accepts a natural‑language query and a `n_results` parameter and returns a list of hits. Internally, it queries a Chroma collection of geospatial features built from:

- The GeoDB’s `geospatial_features` table for regional deployments, and
- GBIM worldview exports (for example, a downsampled or task‑specific subset of `gbim_worldview_entities`) in more mature stacks.

Each indexed feature stores a short text description (including layer name, theme, and location) and metadata fields such as `layer_name`, `name`, `lat`, and `lon`. The latitude and longitude are derived by taking the centroid of the PostGIS geometry and transforming it into EPSG:4326, so that callers can apply geographic filters by bounding box, radius, county, or GBIM region.

The outputs of the GIS RAG service are designed to be composable with text RAG outputs: a hit is both a semantic object (a building, road, facility, boundary) and a spatial object (with coordinates, SRID, and possibly GBIM entity identifiers) that the main brain can reason about in the same Hilbert‑space frame.

### 7.2.3 Web Research Gateway

External web retrieval is handled by a dedicated gateway rather than allowing arbitrary outbound calls from each agent or service. This gateway exposes a `POST /search` endpoint that accepts a JSON body with a query string and limit on the number of results. It:

- Applies policy filters and rate limits to outbound web access.
- Normalizes results into a uniform structure with fields like `title`, `snippet`, `url`, `source`, and sometimes `published_at`.
- Logs queries and responses for audit and debugging.

This design ensures that the boundary between internal semantic memory, spatial memory, and the external web remains explicit, auditable, and subject to distinct governance rules.

### 7.2.4 Orchestration and Main Brain

The main brain does not typically call language models directly. Instead, it routes each job through an orchestration layer that decides whether to invoke the text RAG service, the GIS RAG service, the web gateway, or some combination, based on:

- The request type (for example, policy question, spatial query, system status).
- The active role (for example, researcher, governance support, community‑facing advisor).
- Any explicit or inferred geography (for example, county, ZIP, worldview region).

The same orchestration layer also composes the final context window for the models and sends candidate responses through downstream guardrail services such as the blood–brain barrier.

---

## 7.3 Retrieval Flows

This section sketches the typical flows for non‑spatial and spatial queries. In each case, the RAG layer is where abstract Hilbert‑space projections and GBIM entities become concrete calls and responses.

### 7.3.1 Non‑Spatial RAG Flow

A typical governance or thesis question (for example, about MountainShares rules or Ms. Jarvis architecture) progresses as follows:

1. **Query intake.**  
   A user or upstream component sends a request to the unified gateway or main brain. The main brain wraps it into an internal job structure containing the raw text, any structured fields (project, county, worldview), and role hints.

2. **Routing to text RAG and/or web.**  
   The orchestration logic decides whether to call the local text RAG service, the web gateway, or both. For most governance‑ and thesis‑style questions, it prefers Chroma‑backed collections (for example, governance, thesis, GBIM, or MountainShares collections) and only consults the web when the question clearly depends on external or time‑varying facts.

3. **Retrieval from ChromaDB.**  
   The text RAG service embeds the query, runs similarity search against the selected collections, and returns high‑scoring documents and their metadata. Collection selection and metadata filters act as an early constraint layer, narrowing the effective Hilbert‑space subspace from “all memory” to “things plausibly relevant to this query and role.”

4. **Context assembly.**  
   The orchestration layer merges the retrieved items into a context window alongside system prompts, role‑specific instructions, and any web‑research snippets. Source separation is preserved where possible, so governance texts, GBIM descriptions, and thesis excerpts remain distinguishable.

5. **Generation and guarding.**  
   One or more language models generate an answer conditioned on this assembled context. The main brain then routes the candidate answer through the blood–brain barrier service, which can rewrite, annotate, or reject outputs that violate constitutional, safety, or scope rules.

### 7.3.2 Spatial RAG Flow

Spatially explicit questions (for example, “roads in Fayette County,” “hospitals near Oak Hill,” or “which buildings lie in this floodplain?”) introduce the GIS RAG path:

1. **Spatial query intake.**  
   The main brain or a spatially aware client calls `/gis_rag` with a natural‑language query and `n_results`, and may additionally pass a center point, bounding box, county, or GBIM region identifier if known.

2. **Semantic and spatial retrieval.**  
   The GIS RAG service embeds the query and runs similarity search over the geospatial Chroma collection. Because each feature includes `lat`, `lon`, and layer/region metadata, the service or caller can then apply geometric filters (for example, restricting to features within a bounding box around Oak Hill or within Fayette County).

3. **Return of geospatial hits.**  
   The service returns a list of hits, each including a compact textual description, the source layer name, a feature label, and lat/lon coordinates. Upstream, these hits can be:
   - Shown directly in map or tabular form.
   - Used to fetch richer GBIM records or PostGIS geometries.
   - Combined with text RAG results to provide mixed semantic and spatial evidence to the language models.

In a more mature configuration, the same flow can be implemented over the full `gbim_worldview_entities` collection, allowing spatial RAG to see not just raw features but their attached GBIM belief states, graph edges, and provenance.

---

## 7.4 Routing, Roles, and Geography (Design vs. Implementation)

Routing is conceptually central to the RAG design. It is meant to be GBIM‑aware, role‑aware, and geography‑aware, but the current implementation is deliberately conservative and only partially realizes this vision.

### 7.4.1 Design Intent

On the design side:

- **Topic and intent routing.**  
  The system should distinguish between queries about governance, geospatial context, thesis theory, MountainShares economics, and infrastructure status, and route each toward appropriate services and collections. For example, governance queries should favor charters, policies, and DAO records; spatial‑justice queries should favor GBIM and GeoDB‑derived collections; infrastructure questions may emphasize logs or status traces.

- **Role‑aware routing.**  
  The active role (for example, researcher, governance engineer, community‑facing advisor) should determine which collections are even eligible. Internal or sensitive material (such as draft policies, experimental models, or raw logs) should only be surfaced for trusted roles, while community‑facing roles should be restricted to public documentation and appropriately filtered spatial layers.

- **Geography‑aware routing.**  
  Queries with explicit or implicit place references should steer retrieval toward collections that encode GBIM entities, `gbim_worldview_entities` records, and GeoDB/PostGIS features in the relevant region. This reinforces the program’s commitment to “intelligence with a ZIP code” by giving local data priority for local questions.

### 7.4.2 Current Implementation

On the implementation side as of early 2026:

- The text RAG API already exposes optional `role` and `geography` fields and uses them to choose which Chroma collections to query and to construct metadata filters. However, many collections are only partially annotated with role and geography metadata, so the behavior defaults to broader retrieval when metadata is missing.

- The GIS RAG service is currently focused on West Virginia, indexing layers such as building footprints, roads, hospitals, and census units from the GeoDB, with centroids transformed into WGS84. Its API is shaped so that GBIM worldview IDs, authority links, and beneficiary tags can be threaded through as metadata in future iterations.

- Routing decisions are implemented as explicit function calls and configuration in the orchestration layer rather than as learned classifiers. This keeps behavior legible and debuggable at the current scale and allows the thesis’s design constraints to be encoded as configuration instead of opaque model weights.

In practice, this means that the RAG layer already has the shape of a role‑ and geography‑sensitive interface, but strict enforcement of those constraints awaits fuller metadata coverage and policy tuning.

---

## 7.5 Context Construction and Structure

Even in the current deployment, how retrieved material is structured for the language model is a significant design choice. The RAG server and upstream services adopt several principles to keep context both usable and inspectable.

- **Source separation.**  
  The text RAG service returns a `results_by_source` dictionary keyed by collection name, and each item carries `collection`, `source`, and `metadata` fields. The GIS RAG service returns layer names and feature labels. Upstream logic uses these fields to keep, for example, governance documents distinct from research notes or spatial features, and to decide how each should be framed in prompts.

- **Relevance ordering and bounded size.**  
  Chroma returns distances, which the services convert into scores; flat results are sorted in descending score order. Clients specify `top_k` per collection or `n_results` per GIS query, and the RAG services enforce these limits, preventing over‑large contexts while still allowing multiple collections to contribute.

- **Role‑ and geography‑aware scaffolding.**  
  Where role and geography are known, upstream prompt builders can add headers or structure that make those constraints explicit (for example, “You are advising a community organization in Fayette County, WV; prioritize GBIM and GeoDB evidence for this region.”). This scaffolding helps the language models respect the same locality and accountability principles that the retrieval layer is designed to enforce.

The combination of collection‑aware grouping, explicit scores, and bounded retrieval gives the language model a context that is closer to an evidence set than an undifferentiated text blob. As metadata schemas mature, this same structure will support richer tracing from answers back to the specific documents, beliefs, and spatial features that informed them.

---

## 7.6 Constraints, Provenance, and Logging

Constitutional and ethical constraints in the present system interact with the RAG pipeline at several points.

- **Pre‑retrieval and retrieval‑time constraints.**  
  The RAG services’ collection selection and filter mechanisms already support limiting retrieval by collection, source, county, worldview, and state. The APIs include `role` and `geography` fields that will govern access‑level and spatial filters more tightly as metadata is filled in. For now, these features are used conservatively: when in doubt, retrieval may fall back to role‑agnostic and region‑agnostic behavior.

- **Decoding‑time guards.**  
  After retrieval and generation, the main brain routes candidate responses through a dedicated guardrail (blood–brain barrier) service that can refuse, rewrite, or annotate outputs that violate constitutional or safety principles. This decoding‑time guard operates over the final answer, regardless of which retrieval path produced it, and complements earlier filters.

- **Post‑hoc review and logging.**  
  The RAG server supports a `/store` or equivalent endpoint for background storage of queries and responses into a conversation‑history collection. Logs capture which services were called, which collections were queried, and sometimes which documents or features were returned. A fully structured, user‑facing explanation interface—where Ms. Jarvis can explicitly list the documents and spatial features relied upon—is marked as future work.

Together, these mechanisms move the system away from unconstrained text generation toward a constrained, accountable pipeline, while leaving room to tighten role‑ and geography‑specific policies as the underlying memory schemas stabilize.

---

## 7.7 Relation to Long‑Term Memory, GeoDB, and Entanglement

The RAG layer sits between relatively static long‑term memory and dynamic, per‑query reasoning, and it is the primary place where semantic and spatial representations are expected to meet.

- **Long‑term memory.**  
  ChromaDB collections hold embedded representations of governance documents, project‑specific knowledge, GBIM worldview entities, and other curated materials. Additional collections are reserved for institutional and narrative content associated with Ms. Jarvis’s roles and the MountainShares DAO.

- **Short‑term context.**  
  Each RAG call assembles a temporary context window from the retrieved items, sorted by relevance and grouped by collection or layer. This window serves as the immediate working memory for the language models and orchestration services as they construct an answer.

- **Coupled updates and future entanglement.**  
  The broader entanglement concept in later chapters envisions updates to semantic memory, spatial layers, and normative constraints as mutually influencing. The current RAG implementation does not fully realize this; instead, it provides a stable, inspectable interface that can later be extended with entanglement‑aware routing, access policies, and metadata propagation across collections.

In this way, the present RAG deployment should be understood as a working but intentionally conservative layer. It already anchors Ms. Jarvis’s outputs in named collections and explicit retrieval calls, including a concrete path from GeoDB and GBIM‑derived spatial features into generation, but it still relies on forthcoming work in metadata design, spatial integration, and explanation tooling to fully satisfy the program’s glassbox and spatial‑justice commitments.
