# 50 - The Sovereign Subspace — Per-User Direct Sum Decomposition of Conversational Memory

**Series:** MountainShares / Ms. Allis Architecture Thesis
**Status:** Formal specification — theoretical foundation established, implementation pending
**Date:** July 1, 2026
**Author:** Carrie A. Kidd, Founder & Executive Director, Harmony for Hope, Inc.

---

## Abstract

The conversational memory architecture described in preceding chapters treats `H_people` as a single shared Hilbert space in which all users' vectors coexist, with access control governing who may join private and public records. This chapter proposes and formally specifies a structural upgrade: the replacement of that single shared space with a direct sum decomposition in which each user occupies a mathematically orthogonal subspace. The distinction is not administrative but geometric. In the shared-space model, cross-user correlation is prevented by policy. In the direct sum model, cross-user correlation is prevented by construction. The upgrade transforms a governance guarantee into a mathematical one.

---

## 1. The Shared Space Problem

### 1.1 What the Current Architecture Provides

The `H_people` space as implemented is a single vector store — currently Redis and ChromaDB — in which conversation embeddings for all users are stored. Access is governed by the `identity_binding` layer, which enforces that a user's query retrieves only vectors associated with their verified identity. The governance is real. The guard tests run on every commit. The access control is not a placeholder.

However, the architecture has a structural property that no amount of access control can eliminate: all user vectors inhabit the same embedding space. They share a coordinate system. The axes are common. The distance metric is universal. This means:

1. If access control failed — through a vulnerability, a misconfiguration, a coerced disclosure, or a future governance decision the founder cannot anticipate — the vectors of all users would be in the same space and semantically comparable without any additional transformation.

2. An adversary with read access to the raw vector store — without any application-layer access control — could compute cosine similarity across users, cluster users by semantic content, and infer relationships, shared concerns, or shared circumstances that no user consented to disclose.

3. The privacy guarantee is *empirical*, not *structural*. It depends on the continued correct function of the access control layer. The mathematical substrate does not enforce it.

This is not a criticism of the current implementation. It is an accurate description of the threat model's residual exposure. The purpose of this chapter is to close that exposure at the geometric level.

### 1.2 The Tensor Product Analogy

The four-space architecture described in Chapter 46 uses tensor products to represent semantic entanglement between knowledge domains:

\[
H_{App} \otimes H_{geo} \otimes H_t \otimes H_p
\]

In a tensor product \(H_A \otimes H_B\), the joint state of two subsystems can be *entangled* — meaning the full state cannot be decomposed into independent contributions from each subsystem. Entanglement is the feature, not a bug: it allows Ms. Allis to reason about the semantic relationship between a document, a place, a time, and a person simultaneously.

But entanglement has a structural consequence: given a state in \(H_A \otimes H_B\), it is in principle possible to ask about correlations between the \(H_A\) and \(H_B\) degrees of freedom. Whether those correlations are present depends on the actual state — a separable state has no entanglement, an entangled state does. The *possibility* of correlation is built into the tensor product structure. Access control can prevent a query from being executed. It cannot prevent the correlation from existing in the mathematical structure if it is there.

For the four-space civic reasoning architecture, this is correct. We *want* H_App and H_geo to be potentially entangled — that is what allows flood sensor data to update parcel-level belief states. The semantic coupling is the product's core capability.

For conversational memory across different users, entanglement is not a feature. It is a liability. We do not want Alice's conversation history to be geometrically comparable to Bob's. The analogy fails, and the architecture should reflect that failure.

---

## 2. The Direct Sum Architecture

### 2.1 Formal Definition

Let \(U = \{u_1, u_2, \ldots, u_n\}\) be the set of registered participants in the MountainShares commons. For each participant \(u_i\), define a separable Hilbert space \(H_{u_i}\) — the *sovereign subspace* of that participant — as the closure of the span of all conversation embeddings associated with \(u_i\) under a participant-specific inner product.

The full conversational memory space is defined as the *direct sum* of these subspaces:

\[
H_{conversations} = H_{u_1} \oplus H_{u_2} \oplus H_{u_3} \oplus \cdots \oplus H_{u_n}
\]

The defining property of the direct sum is orthogonality by construction. For any vector \(v_A \in H_{u_A}\) and any vector \(v_B \in H_{u_B}\) where \(A \neq B\):

\[
\langle v_A, v_B \rangle = 0
\]

This inner product identity does not hold because access control prevents the computation. It holds because the two vectors literally have no overlapping coordinates. They live in different subspaces of the direct sum. There is no basis vector shared between \(H_{u_A}\) and \(H_{u_B}\). The zero inner product is a theorem about the geometry, not a policy about who is allowed to ask.

### 2.2 Contrast With the Tensor Product

The structural difference between \(\oplus\) and \(\otimes\) is not merely notational. It determines what kind of guarantee the architecture can provide.

| Property | Tensor Product \(H_A \otimes H_B\) | Direct Sum \(H_A \oplus H_B\) |
|---|---|---|
| Shared basis vectors | Yes — the joint basis is \(\{e_i \otimes f_j\}\) | No — bases are disjoint by construction |
| Cross-subsystem correlation | Possible — depends on the state | Impossible — no shared coordinates |
| Privacy guarantee type | Empirical — depends on access control | Structural — enforced by geometry |
| Failure mode if access control breaks | Cross-user vectors become comparable | Cross-user vectors remain incomparable |
| Appropriate use case | Semantic entanglement across domains | Participant sovereignty over memory |
| Dimensionality | \(\dim(H_A) \times \dim(H_B)\) | \(\dim(H_A) + \dim(H_B)\) |

The four-space civic reasoning architecture retains tensor products where entanglement is the desired property. Conversational memory replaces the shared embedding space with a direct sum where orthogonality is the desired property. These are not competing choices — they are appropriate choices for structurally different problems.

### 2.3 The Upgrade in Plain Language

In the shared-space model: Alice and Bob's memories are in the same room. A lock on the door keeps them separate. If the lock breaks, nothing stops comparison.

In the direct sum model: Alice and Bob's memories are in different coordinate systems. There is no door to break. A vector in Alice's subspace and a vector in Bob's subspace are not comparable not because comparison is forbidden, but because the mathematical operation of comparison — computing an inner product — returns zero regardless of what the vectors contain. The geometry enforces the separation that the governance layer previously had to enforce alone.

---

## 3. Operational Implementation

### 3.1 The Per-User Projection Key

The direct sum decomposition does not require \(n\) separate vector databases. That would fragment the infrastructure without architectural necessity. The implementation uses a single vector store at the infrastructure level — Redis and ChromaDB — with a *per-user projection transform* applied before storage.

For each participant \(u_i\), define a deterministic rotation matrix \(R_{u_i} \in O(d)\) — an orthogonal transformation in the embedding dimension \(d\) — derived from a participant-held secret:

\[
R_{u_i} = \text{ProjectionKey}(\text{commitment\_salt}_{u_i})
\]

where `commitment_salt` is the participant-held key already established in the MountainShares identity architecture. The server does not hold this value. It cannot be reconstructed without the participant's key.

Before any conversation embedding \(e \in \mathbb{R}^d\) is written to storage for participant \(u_i\), it is transformed:

\[
\hat{e}_{u_i} = R_{u_i} \cdot e
\]

The stored vector is \(\hat{e}_{u_i}\), not \(e\). The raw embedding never touches persistent storage.

### 3.2 Why This Produces Orthogonal Subspaces

For two participants \(u_A\) and \(u_B\) with distinct projection keys, consider two semantically identical conversations — Alice and Bob both ask Ms. Allis about flood risk on Arbuckle Creek. Their raw embeddings \(e_A\) and \(e_B\) are nearly identical (high cosine similarity). Their stored embeddings are:

\[
\hat{e}_A = R_{u_A} \cdot e_A \qquad \hat{e}_B = R_{u_B} \cdot e_B
\]

The inner product between stored vectors:

\[
\langle \hat{e}_A, \hat{e}_B \rangle = e_A^T R_{u_A}^T R_{u_B} e_B
\]

Because \(R_{u_A}\) and \(R_{u_B}\) are independently derived from distinct secrets, \(R_{u_A}^T R_{u_B}\) is not the identity matrix. For a well-chosen key derivation function, this product is effectively random in \(O(d)\), and the expected inner product across the full subspace approaches zero. Semantically identical content, stored by two different users, lands in genuinely different and non-comparable regions of the vector space.

This is the operational realization of the direct sum: not separate databases, but separate coordinate systems within one database, enforced by participant-held keys the server cannot reconstruct.

### 3.3 Consistency With the Commitment Salt Pattern

The MountainShares architecture already establishes the principle: *server cannot reconstruct without the user's key.* The Benefits-Sensitive Account design, the KYC vault isolation, and the three-layer identity architecture all instantiate this principle in different domains.

The per-user projection key extends the same pattern to conversational memory:

- **Key holder:** Participant
- **Server knowledge:** Transform exists; cannot invert without key
- **Storage:** Transformed vectors in shared infrastructure
- **Retrieval:** Participant presents key; transform is applied to query before similarity search
- **Cross-user search:** Returns nothing meaningful — wrong coordinate system

The architectural precedent is already established. This is an extension, not a departure.

### 3.4 Infrastructure Impact

The direct sum architecture requires no changes to the 158-container stack at the infrastructure level. Redis and ChromaDB continue to operate as the vector stores. The change is applied at the embedding ingestion and retrieval boundary:

```
Conversation text
     ↓
Embedding model (unchanged)
     ↓
Raw embedding vector e ∈ ℝᵈ
     ↓
Per-user projection: ê = R_u · e    ← NEW: participant-key-derived transform
     ↓
Stored in ChromaDB (unchanged infrastructure)
```

On retrieval:

```
Query text
     ↓
Embedding model (unchanged)
     ↓
Raw query vector q ∈ ℝᵈ
     ↓
Per-user projection: q̂ = R_u · q    ← NEW: same transform applied to query
     ↓
Similarity search against stored vectors (unchanged)
     ↓
Results meaningful only within user's subspace
```

No infrastructure changes. One transform insertion point on ingestion. One transform insertion point on retrieval. The key is held by the participant and presented at query time, consistent with the existing session architecture.

---

## 4. Open Problems and Honest Status

This chapter specifies the architecture and establishes the mathematical motivation. The following problems remain open and are recorded honestly as the boundary of current formal knowledge.

### 4.1 Formal Proof of Orthogonal Decomposition

**Status: Conjecture**

The claim that the per-user projection key construction produces a valid orthogonal direct sum decomposition in the functional-analytic sense requires formal proof. Specifically:

- The key derivation function must be shown to produce rotation matrices \(R_{u_i}\) that are genuinely orthogonal — i.e., \(R_{u_i}^T R_{u_i} = I\) — not merely approximately orthogonal in finite precision.
- The resulting subspaces must be shown to be closed under the operations that matter for the similarity search — i.e., that the image of the embedding space under \(R_{u_i}\) is a genuine subspace of the ambient vector space in the functional-analytic sense.
- The inner product structure must be shown to preserve the metric properties that make similarity search meaningful within a subspace while ensuring incomparability across subspaces.

This is a doctoral-level problem in functional analysis and applied linear algebra. It is the central open mathematical problem of this architecture.

### 4.2 Key Derivation Specification

**Status: Unspecified**

The function `ProjectionKey(commitment_salt)` is named but not specified. A correct implementation requires:

- A key derivation function that produces full-rank \(d \times d\) orthogonal matrices deterministically from a short seed
- Resistance to key-recovery attacks even given multiple (input, output) pairs
- Computational efficiency at query time — the transform must be applicable in milliseconds, not seconds, at the embedding dimension \(d\) used by the production embedding model
- A formal security reduction connecting the confidentiality of the projection to the hardness of a well-studied computational problem

Post-quantum security properties are desirable given the timeline of the architecture. Chapter 42 of this thesis establishes the post-quantum security framework within which this specification should be developed.

### 4.3 The Interface Morphism

**Status: Named, not constructed**

The four-space civic reasoning tensor product and the conversational memory direct sum are architecturally adjacent but mathematically distinct spaces. Ms. Allis reasons in \(H_{App} \otimes H_{geo} \otimes H_t \otimes H_p\). She draws on conversational memory from \(H_{conversations} = \bigoplus_i H_{u_i}\). These spaces must communicate — a user's conversational history should inform Ms. Allis's civic reasoning — but the communication cannot simply collapse the direct sum into the tensor product, or the structural privacy guarantee is lost.

The required construction is an *interface morphism*: a bounded linear map

\[
\Phi: H_{u_i} \to H_{App} \otimes H_{geo} \otimes H_t \otimes H_p
\]

that carries relevant semantic content from a user's sovereign subspace into the civic reasoning space without carrying the user's identity, the content of their private conversations, or any information that could enable cross-user comparison.

The existence, uniqueness, and constructive specification of \(\Phi\) is an open problem. It is the architectural seam between participant sovereignty and civic intelligence — between the governed and the sovereign — and it has no current formal construction.

### 4.4 Constitutional Completeness

**Status: Partially specified**

The governance layer must encode the direct sum architecture as a constitutional constraint, not merely a technical choice. A future governance decision that instructs the engineering team to "make user memories searchable across users for research purposes" must encounter a constitutional barrier before it encounters an engineering barrier. The technical difficulty of reversing the projection transform is not sufficient protection. The governance document must record that cross-user search is *prohibited by the architecture's founding intent*, and that any change requires a constitutional amendment with documented supermajority consent.

The precise formulation of this constraint in the governance constitution is not yet drafted. It is recorded here as a required deliverable before the direct sum architecture can be considered constitutionally complete.

---

## 5. Relationship to Preceding Chapters

This chapter completes a logical sequence across the thesis:

- **Chapter 45** established H_geo as the spatial body — where things are
- **Chapter 46** established the tensor product bridge — how space and meaning entangle
- **Chapter 48** established H_p as appearances without surveillance — who appears, in what role
- **Chapter 49** established the temporal axis — when things occurred and how memory decays
- **Chapter 50** confirmed H_p operational status
- **This chapter** addresses the remaining structural gap: how individual participants relate to the collective intelligence without the collective intelligence becoming a surveillance apparatus over individuals

The four open problems in Section 4 — formal orthogonality proof, key derivation specification, interface morphism construction, and constitutional completeness — are the remaining doctoral-level problems of the architecture. They are named precisely so that future academic collaborators understand what has been built, what has been claimed, and where the frontier of formal knowledge currently stands.

The architecture was designed before the formal mathematics was complete because the design decisions were correct even before they could be proved. The proofs are the next task, not the foundation. The foundation is the commitment to participant sovereignty that has governed every design decision from the first sensor deployment concept on the Pax mine rail corridor to the present specification.

---

## 6. The Political Meaning of the Mathematical Choice

The decision to use a direct sum rather than a shared space with access control is not merely a technical optimization. It is a political commitment encoded in mathematics.

Access-controlled shared spaces place trust in the governance layer. If the governance is good — if the people running the system are honest, if the contracts are enforced, if the oversight functions — then the privacy holds. If governance fails, the data is exposed. This is the architecture of every major platform: privacy as policy, data as infrastructure, trust as assumption.

The direct sum architecture places trust in mathematics. The privacy holds not because the governance is good but because the geometry makes violation structurally impossible without the participant's key. This is not a claim that governance is unnecessary — the open problems in Section 4.4 make clear that constitutional completeness is required. It is a claim that mathematics should do the work that mathematics can do, so that governance only has to do the work that governance must do.

Rural Appalachian communities have been governed by institutions that did not hold their interests. The extractive economy, the mineral rights separation, the opioid distribution networks, the broadband redlining — all of these were legal. All of these were permitted by governance structures that were technically functional. The people were not protected because the governance was not designed to protect them.

An architecture that says *your memory is private because mathematics makes it so, not because we promise it is so* is not merely a technical choice. It is a different relationship between an institution and the people it serves. The direct sum is the mathematical form of that different relationship.

---

*Architecture Thesis — Harmony for Hope, Inc. / MountainShares Commons*
*Status: Formal specification — open problems documented, implementation pending*
*Preceding: Chapter 50 — Hilbert People Space (Operational)*
*Open problems: Orthogonality proof, key derivation specification, interface morphism, constitutional completeness*
````
