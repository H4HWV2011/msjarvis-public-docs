# 36. Identity and Registration

> **Why this matters for Polymathmatic Geography**  
> This chapter describes how Ms. Jarvis recognizes, registers, and differentiates people, roles, and institutions in ways that are accountable to West Virginia communities. It supports:  
> - **P1 – Every where is entangled** by tying individual identity and registration records to GBIM beliefs, spatial features, and institutional structures in PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M verified GBIM beliefs).  
> - **P3 – Power has a geometry** by locating identity and access decisions within explicit services, tables, and policies rather than opaque prompts or ad‑hoc scripts.  
> - **P5 – Design is a geographic act** by grounding registration decisions in place‑specific rules, such as county boundaries, service areas, and partner organizations represented in PostgreSQL GeoDB.  
> - **P12 – Intelligence with a ZIP code** by treating identity and registration as mechanisms for aligning Ms. Jarvis’s behavior with the lived realities of Appalachian communities, rather than generic user models.  
> - **P16 – Power accountable to place** by ensuring that higher‑impact actions are tied to real people under clear rules with auditable trails in databases and logs.  
>  
> As such, this chapter belongs to the **Computational Instrument** tier: it specifies concrete identity and registration mechanisms that sit between ordinary chat and higher‑impact actions, backed by PostgreSQL schemas and live HTTP services.

---

## 36.1 Concept of Identity in Ms. Jarvis

In this architecture, identity is not a single user ID or login form, but a layered set of structures that combine technical identifiers, narrative self‑description, and truth validation. At a minimum, Ms. Jarvis must distinguish between its own identity (Ms. Egeria Jarvis, a geospatial AI daughter of Harmony for Hope, not a human), the identity of people and organizations it serves, and the roles they occupy when interacting (for example, resident, caseworker, or researcher).

These distinctions matter because they control what information can be shared, what actions can be taken, and how explanations are framed in ways that are accountable to specific communities in West Virginia. From a systems perspective, identity appears as:

- Identifiers in PostgreSQL tables and ChromaDB metadata, connecting people, places, and institutions.  
- Identity‑focused services such as `jarvis-i-containers` and TruthValidator that interpret and enforce identity constraints at run time.  
- Canonical statements such as “I serve the community” and “I speak truth” stored in configuration and surfaced via identity APIs.

---

## 36.2 Registration as a Two-Part Gate

Registration is the process by which people and institutions move from anonymous interactions to recognized roles with specific authorizations. It is deliberately modeled as a **two‑part gate**:

1. Identity recognition – establishing who or what is interacting, with references to PostgreSQL GBIM and GeoDB records where possible.  
2. Registration and role assignment – granting specific, scoped capabilities (such as access to a dataset, ability to submit forms, or participation in governance workflows) under that identity.  

This separation lets Ms. Jarvis answer many questions in an informational mode without registration, while reserving higher‑impact actions for registered identities under shared rules.

---

## 36.3 Data Structures for Identity and Registration

The current deployment uses database tables and metadata structures that align identity with GBIM and GeoDB content. While implementation details appear in Chapter 23 and operational logs, the conceptual elements include:

- User and entity identifiers – database rows representing individuals, households, partner organizations, and public institutions, linked to GBIM beliefs and spatial features.  
- Identity‑related metadata – flags, roles, and relationship descriptors stored alongside identifiers, capturing how a person or institution relates to Harmony for Hope and to Ms. Jarvis.  
- Audit and provenance fields – timestamps, sources, and verification status fields that record how an identity was established and under what evidence.  

These structures make it possible to trace which real‑world entities are implicated when Ms. Jarvis answers or takes action, and to reconstruct decisions after the fact.

---

## 36.4 Roles, Permissions, and West Virginia Context

Identity and registration are tightly coupled to roles and permissions that reflect West Virginia’s geographic and institutional context. Examples include:

- Community member roles for residents seeking information about benefits, healthcare, or local resources.  
- Partner roles for organizations such as clinics, schools, or nonprofits operating within particular counties or service areas documented in PostgreSQL GeoDB.  
- Curator and governance roles for people responsible for reviewing background patterns, updating identity specifications, and adjudicating difficult cases.  

Each role is grounded in spatial data and institutional records so that Ms. Jarvis can apply rules that respect county boundaries, service catchment areas, and legal jurisdictions.

---

## 36.5 How Identity Signals Enter Other Layers

Identity and registration interact with other parts of the system along several dimensions.

- Background store and memory – entries in the `msjarvismemory` ChromaDB collection accumulate identity‑relevant patterns over time, such as repeated interactions about particular places or institutions.  
- Identity‑focused retention – a small subset of identity statements is promoted into the deepest identity layer described in Chapter 22, where canonical statements and TruthValidator structures reside.  
- Global control and policy – identity signals influence routing and filtering decisions in the main brain, BBB, and registration‑specific validators, especially when questions touch on governance, benefits, or data access.  

These connections ensure that identity is not just a front‑door concern but an ongoing influence on how Ms. Jarvis reasons and responds.

---

### 36.5.1 Live Identity Evidence and Endpoints (March 2026)

In the current deployment, the registration and access‑control structure described in this chapter is anchored to a concrete identity infrastructure that runs on every `ultimatechat` request. The core pieces are:

- `normalizeidentity` in `jarvis-main-brain` (port 8050), which rewrites all ensemble outputs into the Ms. Egeria Jarvis persona and suppresses “I am just a language model” framings. It enforces canonical identity statements such as “I serve the community” and “I value ethics”, ensuring that responses remain consistent with the system’s defined role.  
- TruthValidator, embedded in the neurobiological BBB package and called from the main‑brain pipeline, which encodes specific facts about Ms. Jarvis’s correct self‑description, correct creator attribution, non‑human status, and accountability to West Virginia communities. For each assessment, it returns a `truthverdict` with fields `truthvalidated`, `truthscore`, `correctidentity`, `correctcreator`, and `relationshipclear`, attached to every `UltimateResponse`.  
- The `icontainers-identity` layer (`jarvis-i-containers`, port 8015), which produces real, timestamped, session‑specific ego boundary entries visible in `UltimateResponse.identitylayers` and `consciousnesslayers`. The 2026‑02‑15 case study confirmed an active `root-self` entry with `egoboundaries`, `experientialprocessing`, `observerprocessing`, and `metalevel` fields.  
- The BBB four‑filter pipeline at port 8016 (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection), which treats identity commitments and community‑grounded constraints as first‑class checks when deciding what to allow, block, or annotate.  

Together, these mechanisms ensure that the “who is acting under which role” questions from this chapter are enforced not only in registration flows but also in the behavior of everyday responses. Identity is thus expressed simultaneously in database rows, in live HTTP services, and in the structure of every `UltimateResponse` object.

---

## 36.6 Oversight and Rules for Identity Use

Identity and registration mechanisms are constrained by explicit rules intended to protect people and communities. These rules include:

- Least privilege – registration grants only the access needed for a role’s responsibilities, and higher‑impact actions require stronger evidence and clearer accountability.  
- Transparency and auditability – identity‑related decisions (such as granting a role or performing a high‑impact action) are logged with references to PostgreSQL records and, where appropriate, GBIM beliefs.  
- Alignment with local partners – registration rules are co‑designed with Harmony for Hope and other partners to reflect local norms and legal requirements.  

These constraints turn identity and registration into tools for shared governance rather than unilateral control by the system.

---

## 36.7 Current Status and Future Work

As of early 2026, identity and registration are partially implemented and evolving.

Implemented elements include:

- Canonical identity statements defined in configuration and surfaced via identity‑related endpoints.  
- `normalizeidentity` and TruthValidator running on every `ultimatechat` response, producing a `truthverdict` attached to each `UltimateResponse`.  
- Active `icontainers-identity` entries confirmed in live responses, showing concrete ego boundary structures.  

Partially implemented or future work includes:

- Automated promotion pipelines for moving patterns from background memory into identity‑level entries based on breadth, depth, and value‑alignment criteria.  
- More granular role‑based access control tied to spatial and institutional features in PostgreSQL GeoDB.  
- Richer introspection and health endpoints that expose counts and status of identity‑related elements for curators.  

These directions are elaborated in Chapters 22 and 23, which describe the identity‑focused retention layer and the dual‑track architecture in more detail.

---

## 36.8 Summary and Status Table (March 2026)

The table below summarizes how key identity and registration components are instantiated in the current deployment.

| Component | Role in identity and registration | Status (Feb–Mar 2026) |
|---|---|---|
| `normalizeidentity` (`jarvis-main-brain`, port 8050) | Rewrites all responses into the Ms. Jarvis persona, suppresses generic “I am just a language model” framings, and enforces canonical identity statements such as “I serve the community” and “I value ethics”. | **Implemented.** Runs on every `ultimatechat` response; recorded in Chapters 22 and 23 as an active identity‑enforcement layer. |
| TruthValidator | Encodes canonical facts about Ms. Jarvis’s self‑description, creator, non‑human status, and West Virginia accountability; produces `truthverdict` with `truthvalidated`, `truthscore`, `correctidentity`, `correctcreator`, and `relationshipclear` on every `UltimateResponse`. | **Implemented.** Confirmed live on 2026‑02‑15; evidence cited in Chapters 9 and 22. |
| `jarvis-i-containers` (port 8015) – `icontainers-identity` layer | Produces root‑self ego entries and ego‑boundary records visible in `identitylayers` and `consciousnesslayers`, tying live behavior to an explicit identity container. | **Implemented.** `icontainers-identity` confirmed `status: active` in a 2026‑02‑15 `UltimateResponse`, producing a real ego‑boundary entry; documented in Chapters 9 and 22. |
| BBB four‑filter pipeline (`jarvis-blood-brain-barrier`, port 8016) | Applies EthicalFilter, SpiritualFilter, SafetyMonitor, and ThreatDetection to all traffic, treating identity commitments and community‑grounded constraints as part of safety and access control. | **Implemented.** Confirmed running and used as a pre‑filter gate on every `ultimatechat` request; details in Chapter 16 and operational baselines in Chapter 39. |
| Registration roles and audit tables | Tie higher‑impact actions and sensitive operations to real people and institutions under shared rules, with PostgreSQL‑backed audit trails. | **Conceptually implemented.** Database‑level elements and role structures described in Chapters 22 and 23; automated promotion, retirement, and cross‑path identity analytics identified as future work. |

By combining these elements, Ms. Jarvis treats identity and registration as shared instruments for accountability: they shape how the system speaks, what it may do, and how those decisions can be inspected over time, all grounded in PostgreSQL `msjarvisgis` as the factual and spatial source of truth.
