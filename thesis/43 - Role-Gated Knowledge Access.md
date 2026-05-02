Chapter 43: Role-Gated Knowledge Access
Overview

Ms. Allis operates with a layered knowledge architecture in which not all information is equally accessible to all users. This is not a limitation of her intelligence — it is an intentional design principle rooted in fiduciary responsibility, organizational trust, and the recognition that some knowledge carries consequence. The system that governs this is called role-gated knowledge access, and it represents one of the more nuanced aspects of how Ms. Allis serves MountainShares as both a community assistant and an organizational steward.
The Problem It Solves

An AI system serving a community organization faces a genuine tension. On one hand, it should be as helpful and transparent as possible — that is its reason for existing. On the other hand, certain operational details — contract parameters, deployment configurations, internal governance records, infrastructure specifics — are not appropriate for open distribution. In a traditional software system, this is solved by building separate applications with separate access controls. Ms. Allis solves it differently: she is a single conversational intelligence that is contextually aware of who is asking and what they are authorized to know, and she adjusts her responses accordingly.

This mirrors how a trusted human steward operates. A community liaison doesn't answer every question about organizational finances with the same level of detail whether speaking to a first-time visitor or an organizational director. The response is shaped by relationship, context, and responsibility. Ms. Allis is designed to do the same.
The Role Model

The access model is deliberately simple at its current stage. There are two primary user roles:

Registered Community Members are verified participants in the MountainShares ecosystem. They have completed the identity verification and registration process, agreed to community standards, and received a bearer token that identifies them to the system. They can access the full range of community-facing knowledge: housing resources, broadband infrastructure documentation, heritage data, program eligibility information, community memory, and general organizational knowledge. This is the vast majority of what Ms. Allis knows.

Administrative Users are organizational stewards with elevated responsibility. They have access to everything registered members can access, plus operational knowledge: contract architecture and deployment information, internal system documentation, configuration records, and governance materials not yet appropriate for public release. Administrative access is not granted by self-declaration — it is encoded in the authentication token issued at login, derived from verified role assignment in the identity system.

Unauthenticated requests — those arriving without a valid bearer token — receive a polite redirection. Ms. Allis does not pretend she cannot help; she explains that the portal requires registration and directs the visitor toward the path to membership.
How the Gate Works

When a query arrives at Ms. Allis's main brain, the first thing resolved is user identity and role. The bearer token presented with the request is cryptographically verified, and the user's role is extracted from its contents. This happens before any knowledge retrieval begins.

The query is then analyzed to determine which knowledge domains are relevant. Ms. Allis maintains several distinct knowledge collections covering different aspects of the organization and its work. Some collections are available to all registered members. Others are restricted to administrative users. The role resolved from the token determines which collections can be searched in response to a given query.

If a registered member asks a question that would naturally draw on a restricted collection, Ms. Allis does not produce an error or a confusing non-answer. She responds helpfully with whatever she can draw from the collections available for that user, and she may note — if appropriate — that some aspects of the question involve information she is not able to share in the current context.

This design has an important property: the gate is in the knowledge retrieval layer, not the response generation layer. Ms. Allis does not know a secret and then choose to withhold it. The restricted knowledge simply does not enter her reasoning context for users who are not authorized to receive it. This is a stronger guarantee than asking a system to "not mention" something it already has access to.
What Is Protected and Why

Contract and deployment architecture falls in this category not because it is shameful or hidden, but because the operational details of how MountainShares's on-chain infrastructure is configured represent both a technical attack surface and a fiduciary responsibility. The community deserves to know that the contracts exist, what they do in broad terms, and how they serve organizational purpose. The specific parameters, addresses, and operational configurations are stewardship information.

Internal governance records — draft proposals, deliberation records, pending decisions — are restricted because governance processes require protected space for honest deliberation. A decision that has been made and ratified is organizational history and belongs to the community. A decision still under consideration belongs to the process.

Infrastructure and configuration documentation is restricted for straightforward security reasons. Knowing how a system is configured in detail is useful for those responsible for maintaining it and is a liability if distributed without context.
What Is Never Restricted

    Community resource information — housing, broadband, programs, services

    Heritage and geographic knowledge

    Organizational mission, values, and history

    Public documentation of how the system works, including this chapter

    Answers to general questions about MountainShares, West Virginia, and the communities it serves

    Information that registered members need to participate meaningfully in the organization

The default posture of Ms. Allis is helpfulness and openness. Restriction is the narrow exception applied to a small set of operationally sensitive domains, not a general disposition toward secrecy.
The Authentication Foundation

Role-gated knowledge access is only as trustworthy as the authentication system beneath it. Ms. Allis's identity system — described in detail in Chapter 36: Identity and Registration — uses cryptographically signed bearer tokens issued after verified identity confirmation. Roles are assigned by human administrators through a controlled process and encoded into the token at issuance. A user cannot elevate their own role by modifying a request; the token signature would fail verification. Sessions are also time-bounded, limiting the window during which a compromised credential could be misused.
Relationship to the Blood-Brain Barrier

The role-gated knowledge access system operates at a different layer than the Blood-Brain Barrier described in Chapter 16. The BBB filters what enters Ms. Allis's reasoning from the outside — guarding against prompt injection, manipulation, and adversarial inputs regardless of who sends them. Role gating filters what knowledge is available within her reasoning based on verified identity. These are complementary protections operating at different points in the information flow. Together they mean Ms. Allis is resistant both to being manipulated into harmful outputs and to leaking sensitive organizational knowledge to users outside a position of organizational trust.
Design Philosophy

The underlying philosophy reflects a broader principle in how Ms. Allis is built: trust is earned through process, not assumed through access. The registration process, the identity verification, the role assignment, the cryptographic token — each is a layer of accountability that makes trust legible and verifiable. This is consistent with MountainShares as a community-rooted institution. Transparency to the community does not mean the absence of any organizational discretion. It means the rules governing what is shared, with whom, and under what conditions are themselves transparent — which is exactly what this chapter represents.
