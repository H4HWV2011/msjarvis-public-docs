# 2. The Geometric Belief Model and GBIM Architecture

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

---

## Why This Matters for Polymathmatic Geography

This chapter provides the theoretical foundation for understanding how Ms. Jarvis represents knowledge, belief, and uncertainty — and why those representations are structured the way they are. It supports:

- **P1 – Every where is entangled** by establishing that belief is not stored as isolated facts but as multi-axis geometric structures in which spatial, temporal, institutional, and normative dimensions are co-present and mutually constraining — so that a single GBIM belief about a hospital in Fayette County is simultaneously a claim about what exists, where it is, when it was verified, who has authority over it, and what its implications are for program routing.

- **P3 – Power has a geometry** by showing that the GBIM axis structure — particularly `who`, `where`, `under_whose_authority`, and `for_whom` — is designed to make institutional power over place explicit and queryable, not buried in unstructured text. The landowner belief layer (Section 2.6.4, field note March 20, 2026) is the direct realization of this principle at parcel scale.

- **P5 – Design is a geographic act** by treating the nine-axis GBIM schema, the worldview structure, the collection inventory, and the ChromaDB configuration not as neutral technical choices but as geographic and political decisions that determine which facts are computable, which relationships are traversable, and which forms of institutional accountability are operationally enforceable.

- **P12 – Intelligence with a ZIP code** by grounding the Hilbert-space model in a concrete PostgreSQL corpus — msjarvis (port 5433), msjarvisgis (port 5432), and their ChromaDB mirrors — so that the abstract framework of quantum-geometric belief representation is always already indexed to real West Virginia places, programs, and populations.

- **P16 – Power accountable to place** by designing the belief structure so that institutional actors — government agencies, corporate landowners, utility companies — are represented as first-class GBIM entities with explicit `under_whose_authority` and `who` axis entries, making them queryable and auditable in a way that individual residential actors deliberately are not.

The theoretical framework in this chapter is not a preamble to the system — it is the system's operating logic, expressed at the level of schema, routing, and collection design rather than at the level of code.

Accordingly, this chapter belongs to the **Theoretical Foundation** tier: it establishes the geometric belief model, the nine-axis GBIM schema, the Hilbert-space representation of uncertainty, the worldview structure, and the ChromaDB collection inventory that together constitute the epistemic architecture of Ms. Egeria Jarvis.

---

## 2.1 Purpose and Scope

This chapter establishes the theoretical framework underlying the **GeoBelief Information Model (GBIM)** — the core representational system that allows Ms. Egeria Jarvis to hold, update, route, and reason over structured beliefs about West Virginia's physical world, institutional landscape, and programmatic infrastructure.

GBIM is not a database schema in the conventional sense. It is a multi-axis geometric representation of belief that treats each claim about the world as a structured object with nine dimensions, each encoding a distinct aspect of the claim's meaning, provenance, authority, and applicability. This nine-axis structure is what allows beliefs derived from a WV assessor parcel record, a federal hazard dataset, a community organization's program flyer, and a peer-reviewed paper on Appalachian poverty to coexist in a single corpus and be meaningfully compared, combined, and routed.

The chapter is organized as follows:

- **Section 2.2** introduces the nine-axis belief schema and explains the role of each axis.
- **Section 2.3** presents the Hilbert-space model of belief and uncertainty that motivates the GBIM design.
- **Section 2.4** describes the worldview structure (`eq1` and related worldviews) and its role in routing and filtering.
- **Section 2.5** describes the PostgreSQL GBIM corpus — its current scale, table structure, and production status as of March 2026.
- **Section 2.6** presents the ChromaDB collection inventory — the vector-backed memory layer that makes GBIM beliefs semantically retrievable — updated through March 26, 2026.
- **Section 2.7** addresses the relationship between GBIM, the GeoDB spatial body (Chapter 6), the RAG pipeline (Chapter 7), and the local resource registry.
- **Section 2.8** is an intellectual honesty correction (March 21, 2026): it documents the gap between GBIM's designed role as the ground truth for judge verification and the current actual implementation of the truth and alignment judges, which use heuristic pattern-matching, not live PostgreSQL queries.
- **Section 2.9** documents the ethical architecture of the belief corpus — specifically the exclusion of individual residential owner names and the full accountability metadata required for institutional actors.

---

## 2.2 The Nine-Axis Belief Schema

Every belief in the GBIM corpus is a structured object with nine named axes. Each axis is stored as a JSONB field in `gbimbeliefnormalized`, allowing flexible, typed, and queryable representation of the full semantic content of the belief.
