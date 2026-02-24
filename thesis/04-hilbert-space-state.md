# 4. Hilbert‑Space Model of Application State

This chapter introduces a Hilbert‑space formalization of Ms. Jarvis’s application state. The goal is to provide a mathematically coherent framework that unifies textual, geospatial, and institutional information into a single state space, while remaining compatible with practical embedding models, vector databases, and structured stores such as GBIM, GeoDB, and local_resources. This model serves as the backbone for later chapters on entanglement, retrieval, and identity‑aware context management.

## 4.1 Component Spaces

We begin by defining three primary real Hilbert spaces, each corresponding to a different facet of Ms. Jarvis’s knowledge and operational state:

- \(H_{\text{text}}\): the real inner‑product space associated with textual embeddings (documents, conversations, rules, code, public documentation, and thesis materials).
- \(H_{\text{geo}}\): the real inner‑product space associated with geospatial embeddings (parcels, infrastructure, service areas, and other GIS entities represented in GBIM and PostGIS).
- \(H_{\text{inst}}\): the real inner‑product space associated with institutional and behavioral embeddings (governance rules, DAO state, roles, trust‑related signals, and institutional records).

Each of these spaces is modeled as a finite‑ or countably infinite‑dimensional real Hilbert space with an inner product and the induced norm. That is, for each component \(H_{\bullet}\) there exists an inner product \(\langle \cdot,\cdot\rangle_{\bullet}\) such that the space is complete under the associated norm.

The joint application state space is then defined as the orthogonal direct sum

\[
H_{\text{App}} := H_{\text{text}} \oplus H_{\text{geo}} \oplus H_{\text{inst}}
\]

equipped with the canonical inner product

\[
\langle (x_1,y_1,z_1),(x_2,y_2,z_2)\rangle_{\text{App}} := \langle x_1,x_2\rangle_{\text{text}} + \langle y_1,y_2\rangle_{\text{geo}} + \langle z_1,z_2\rangle_{\text{inst}}.
\]

Here \(\langle\cdot,\cdot\rangle_{\text{text}}\), \(\langle\cdot,\cdot\rangle_{\text{geo}}\), and \(\langle\cdot,\cdot\rangle_{\text{inst}}\) are the inner products on the component spaces, and the induced norm is

\[
\lVert v\rVert_{\text{App}} := \sqrt{\langle v,v\rangle_{\text{App}}}.
\]

Elements of \(H_{\text{App}}\) represent application‑level “community states” that combine semantic content, spatial configuration, institutional constraints, and, via linked structures such as local_resources and entangled Chroma collections, the configuration of concrete programs and services. Beliefs, memories, resource neighborhoods, entangled retrieval neighborhoods, and working contexts in Ms. Jarvis are modeled as vectors, or as probability measures over subsets of \(H_{\text{App}}\). This provides a common geometric language for similarity, relevance, constraint application, and WV‑biased measurement across layers.

## 4.2 Domains and Embedding Maps

We formalize the mapping from raw data into the Hilbert‑space representation via embedding functions. Let

- \(D_{\text{text}}\) denote the domain of textual objects (documents, passages, prompts, chat turns, rules).
- \(D_{\text{geo}}\) denote the domain of geospatial objects (parcels, road segments, service areas, polygons, points, raster‑derived features).
- \(D_{\text{inst}}\) denote the domain of institutional objects (program eligibility rules, DAO states, organizational records, legal or policy fragments).

Define embedding maps

- \(E_{\text{text}} : D_{\text{text}} \to H_{\text{text}}\),
- \(E_{\text{geo}} : D_{\text{geo}} \to H_{\text{geo}}\),
- \(E_{\text{inst}} : D_{\text{inst}} \to H_{\text{inst}}\).

In concrete deployments, these maps are implemented by specific embedding models and preprocessing pipelines (for example, transformer‑based text encoders, spatial encoders that capture geometry and attributes, and encoders for institutional or policy text). Abstractly, they are treated as measurable maps into the corresponding spaces, respecting any normalization or scaling conventions imposed by the implementation.

Given a tuple \((d,g,i)\) consisting of a document, a geospatial feature, and an institutional configuration, the corresponding state vector is

\[
v(d,g,i) := \bigl(E_{\text{text}}(d),\,E_{\text{geo}}(g),\,E_{\text{inst}}(i)\bigr) \in H_{\text{App}}.
\]

In practice, some components of this tuple may be absent or “neutral” for a given task. The model accommodates such cases by embedding missing components as distinguished neutral vectors (for example, the zero vector) or by omitting them from the tuple and treating the state as supported on a lower‑dimensional subspace.

## 4.3 Belief States and Context Subspaces

A belief state for a given task (for example, advising on a MountainShares proposal, answering a spatial‑justice query, or finding programs for a specific household) is modeled as:

- a finite subset \(C \subset H_{\text{App}}\), together with
- non‑negative weights \(\{w_v\}_{v \in C}\) satisfying \(\sum_{v \in C} w_v = 1\).

This pair induces a finitely supported probability measure on \(H_{\text{App}}\). Intuitively, \(C\) collects a set of “active” vectors—retrieved documents, spatial features, institutional rules, or composite states—and the weights encode their relative importance or salience for the current task.

The associated context subspace is the closed linear span

\[
S(C) := \overline{\operatorname{span}(C)} \subseteq H_{\text{App}}.
\]

Intuitively, “being in a certain context” means that Ms. Jarvis restricts attention to the subspace \(S(C)\) and to operators that act on it. Operationally, this matches the idea that a particular task selects a local neighborhood of relevant embeddings and linked registry rows—for example, KB chunks about Christmas programs plus the local_resources entries for the user’s ZIP, as well as entangled GBIM/GeoDB features identified in a `wv_entangled_context` envelope—and that reasoning and generation are conditioned on that neighborhood rather than the full state space.

Context updates (for example, after user feedback, new retrievals, or background learning) correspond to modifications of the set \(C\) and its weights \(\{w_v\}\), and therefore to changes in the subspace \(S(C)\). This provides a clean way to speak about shifting attention, expanding or narrowing scope, and transitioning between tasks.

## 4.4 Motivation for a Hilbert‑Space View

### 4.4.1 Mathematical Structure

A real Hilbert space provides:

- An inner product \(\langle\cdot,\cdot\rangle\) inducing norms, distances, and angles.
- Orthogonal projections onto closed subspaces.
- Decompositions into orthogonal components, enabling structured factorization of state.

These features support precise definitions of similarity, orthogonality, and subspaces, which are useful for modeling topics, roles, constraint sets, and WV‑entanglement envelopes as geometric structures (for example, a governance subspace, a resource‑eligibility subspace, or a “Fayette County mental‑health access” direction). They also support the use of linear operators and spectral tools to describe system evolution—for instance, the impact of certain retrieval operators, constraint‑projection steps, or policy filters on the state vector.

### 4.4.2 Explainable Geometry

Distances and angles between embedding vectors can be interpreted as degrees of similarity or opposition between beliefs, contexts, documents, or resource neighborhoods. In particular, cosine similarity is the normalized inner product

\[
\cos(\theta) = \frac{\langle u,v\rangle}{\lVert u\rVert \cdot \lVert v\rVert},
\]

which is already widely used in embedding‑based retrieval. Framing retrieval, including WV‑biased, multi‑collection `/search` retrieval, geometrically makes the behavior of Ms. Jarvis more explainable to researchers, practitioners, and community partners than opaque model internals, especially when those retrievals are then resolved to concrete program rows keyed by county and ZIP.

Angles and projections can be used to reason about:

- Alignment or misalignment between two policy regimes.
- Overlap between resource neighborhoods for different households.
- How far a given context is from a governance or safety boundary.

This geometric intuition is helpful when communicating design and evaluation decisions to non‑technical stakeholders.

### 4.4.3 Compatibility with Existing Tools

Modern embedding models output high‑dimensional real vectors, and vector databases efficiently store and query these vectors. Treating embedding outputs as elements of a Hilbert space aligns the implementation with a coherent conceptual model of state and operators, while remaining fully compatible with standard similarity search, clustering, RAG pipelines, and the entangled `/search` path that sit alongside structured stores like GBIM and local_resources.

In particular:

- \(H_{\text{text}}\) and its inner product correspond directly to text‑embedding spaces used in vector stores.
- \(H_{\text{geo}}\) can be implemented using spatial encoders that respect geometry and attributes, while still being queried via cosine or other kernel similarities.
- \(H_{\text{inst}}\) aligns with embeddings of institutional texts, rules, and configurations, allowing similarity queries over policy and governance information.

The orthogonal direct sum structure simply packages these into a single, principled space without imposing any additional burden on implementation.

## 4.5 Query Projection and Retrieval

Let \(q\) be a natural‑language query associated with a task and (optionally) a geography, role, household context, and entanglement envelope. The system first computes a text embedding

\[
q_{\text{vec}} := E_{\text{text}}(q) \in H_{\text{text}}.
\]

In the simplest case, this is lifted into the joint space via

\[
\tilde{q} := (q_{\text{vec}}, 0, 0) \in H_{\text{App}}.
\]

If geospatial or institutional context is encoded directly in the query or its metadata, a more structured lifting may be used:

\[
\tilde{q} := \bigl(q_{\text{vec}},\,q_{\text{geo}},\,q_{\text{inst}}\bigr) \in H_{\text{App}},
\]

where \(q_{\text{geo}}\) and \(q_{\text{inst}}\) are derived from associated spatial and institutional descriptors (for example, “family in ZIP 25309 on SNAP and SSI” together with the user’s parcel centroid and benefit flags).

Given a finite collection \(C \subset H_{\text{App}}\), retrieval is implemented as selection of vectors \(v \in C\) that maximize a similarity functional such as cosine similarity,

\[
\operatorname{sim}(\tilde{q},v) := \frac{\langle \tilde{q},v\rangle_{\text{App}}}{\lVert\tilde{q}\rVert_{\text{App}}\cdot\lVert v\rVert_{\text{App}}},
\]

or another kernel compatible with the Hilbert structure. This similarity defines the “neighborhood” of \(\tilde{q}\) in which standard RAG operates. The top‑\(k\) neighbors form a finite set \(C_q\), and the span

\[
S(C_q) := \overline{\operatorname{span}(C_q)}
\]

serves as the immediate context subspace for answering \(q\). From there, Ms. Jarvis can further ground results by:

- Matching against structured tables (for example, using metadata to resolve from a retrieved Christmas‑Bureau PDF chunk to a specific local_resources row that encodes ZIP coverage, phone, email, and last‑verified timestamp).
- Projecting into role‑, geography‑, constraint‑, and entanglement‑compatible subspaces before generation or decision‑making.

This two‑step procedure—geometric neighborhood selection followed by structured grounding—makes it possible to reason transparently about why certain programs or documents were surfaced for a given query.

## 4.6 Entangled WV‑Biased Retrieval

The Hilbert‑space view becomes fully operational in Ms. Jarvis not only through standard RAG, but through a multi‑collection WV‑biased retrieval path activated by a structured entanglement envelope.

A dedicated `/search` endpoint takes a natural‑language query together with a `wv_entangled_context` object encoding active domains, principles, GBIM entities, and GeoDB features for the task. Conceptually, the `wv_entangled_context` identifies:

- A subset of GBIM entities (for example, schools, clinics, housing assets).
- A subset of GeoDB features (for example, specific roads, tracts, service areas).
- Relevant principles or constraints (for example, spatial justice, benefits access, program‑eligibility envelopes).

These selections can be represented as a set of vectors in \(H_{\text{geo}}\) and \(H_{\text{inst}}\), together with metadata about how they should influence retrieval and ranking.

Given such an envelope, the query lifting \(\tilde{q}\) is adjusted so that:

- Its geospatial component \(q_{\text{geo}}\) is biased toward the entangled GBIM/GeoDB features (for example, by averaging or otherwise aggregating their embeddings).
- Its institutional component \(q_{\text{inst}}\) encodes the relevant program types, eligibility regimes, and governance principles.

Retrieval then proceeds as in Section 4.5, but over a union of collections (for example, Chroma collections for different document sets, local_resources indices, GBIM‑linked embeddings) and with similarity measures that incorporate the entangled components. The result is a WV‑biased neighborhood \(C_q\) in \(H_{\text{App}}\) that:

- Favors documents and resources connected to the specified places, programs, and principles.
- Still respects the geometric structure of the embedding spaces.
- Can be grounded into concrete program entries, maps, and explanations for users.

The same Hilbert‑space formalism thus unifies standard semantic retrieval and the more specialized, entangled WV‑biased retrieval path, providing a single mathematical language for analyzing, auditing, and improving Ms. Jarvis’s behavior across different layers of the system.
