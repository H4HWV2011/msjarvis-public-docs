# 3. MountainShares DAO — Governance Architecture, Perimeter, and Live Topology

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 9, 2026*

---

## 3.1 Why This Matters for Polymathmatic Geography

This chapter describes the MountainShares DAO governance layer — the constitutional, computational, and perimeter architecture that governs how community proposals, token stake, and resource allocation decisions flow through Ms. Allis.

It supports:

- **P3 – Power has a geometry** by making institutional decision‑making pathways explicit, auditable, and spatially grounded. DAO proposals do not float free of geography; they are evaluated against a semantic and relational substrate that encodes West Virginia counties, GBIM entities, and verified local resources.

- **P5 – Design is a geographic act** by treating every governance schema decision — what proposals are valid, which constitutional constraints apply, which token holders have stake, which promotion gates must pass — as a deliberate choice about how power is distributed across Appalachian communities rather than concentrated in abstract administrative categories.

- **P12 – Intelligence with a ZIP code** by binding DAO deliberations to county‑level infrastructure questions grounded in local resource registries, address points, and GBIM worldview entities, so that governance decisions are answerable to specific places and people rather than to abstract token economics alone.

- **P16 – Power accountable to place** by requiring that all external DAO traffic pass through a hardened perimeter and all internal DAO reasoning pass through sandbox gates, so that no governance route is reachable without a valid token and no proposal reaches voting or action without passing truth, constitutional, privacy, and system‑safety checks.

The DAO is therefore not a standalone web application. It is the community governance edge of a larger governed organism. Proposals, votes, token stake, and resource allocation decisions are evaluated against constitutional constraints, grounded in spatial and semantic memory, modulated by a systemic regulator, and protected by both an external perimeter and an internal sandbox promotion architecture.

In plain language, MountainShares DAO is the part of Ms. Allis that lets communities in West Virginia — and similar rural regions — make and track decisions about shared resources together, with every decision tied back to real counties, real infrastructure, and real people rather than abstract dashboards.

---

## 3.2 Purpose and Scope

The MountainShares DAO is the community governance layer of the Ms. Allis organism. It is a governed edge of a larger distributed system — one in which proposals, votes, token stake, and resource allocation decisions must originate from validated sandbox reasoning and must move through explicit promotion gates before they can affect real‑world governance outcomes.

This chapter documents:

- The live MountainShares service topology.
- The Caddy/auth perimeter layer that governs all external access, including the DAO tier.
- The systemic regulator above the DAO layer.
- Impersonation detection and constitutional alignment at the DAO boundary.
- The gates that ensure DAO proposals are derived from sandboxed reasoning and constitutionally filtered before they are eligible to affect voting, proposals, or governance actions.
- The distinction between sandbox hypothesis, corroborated conclusion, approved governance memory, and actionable state.

DAO governance inputs are documented as sandboxed and constitutionally filtered rather than as direct AI outputs. Where earlier descriptions implied “the system outputs a proposal and the DAO acts,” the accurate sequence is: the system reasons in a sandbox, proposals are formed as governed candidate states, gates evaluate those candidates, and only promoted conclusions may influence governance processes.

---

## 3.3 Live MountainShares Service Topology

The MountainShares governance tier consists of several services that together implement community‑facing coordination, proposal evaluation, stake registry, and token management. They are part of the larger Ms. Allis service graph and operate under a governed promotion architecture.

```text
┌─────────────────────────────────────────────────────────────┐
│                 MountainShares Governance Services          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Coordinator UI          — proposals, votes, stake views    │
│  Governance API          — evaluates and records proposals  │
│  Community Stake Registry — maps tokens to stake records    │
│  Token Service           — issues and validates tokens      │
│                                                             │
│  All services are behind the Caddy/auth perimeter and fed   │
│  by sandboxed reasoning, not direct model output.           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Host‑visible governance services sit downstream of the main inference and routing layer. No external client reaches them directly; all external access is mediated by perimeter and auth components, and all internal reasoning that feeds them is mediated by sandbox and gate components.

For a rural community, that means the screens they see — the coordinator UI showing proposals, votes, and stake — are backed by services that never act on unreviewed, unconstrained suggestions. Every governance artifact has passed through structured reasoning and gatekeeping before it appears.

---

## 3.4 Constitutional and Token Architecture

MountainShares DAO operates under a layered constitutional framework and a token‑based stake registry. That framework applies both to external requests and to internal reasoning about governance.

Constitutionally:

- Federal and state constitutional texts provide a legal and normative frame.
- A DAO charter defines community governance rules.
- GBIM worldview entities encode an equity‑oriented interpretive base.

Token stake:

- Tokens represent community stake and governance rights.
- A stake registry maps token holders to verifiable stake records in relational and GBIM substrates.
- A token service issues and validates tokens behind the perimeter.

Token and constitutional architecture govern how proposals are allowed to exist and move, not just how they are seen from outside. A proposal’s path from sandbox hypothesis to actionable state is constrained by authority levels, gates, and constitutional checks.

For example, a county‑level proposal to reallocate a small emergency fund toward flood mitigation will only be admitted into the governance process if the token holder has valid stake, the proposal’s content is consistent with the DAO charter and constitutional obligations, and the supporting evidence has been evaluated in the sandbox.

---

## 3.5 External Perimeter — Cloud, Gateway, and Auth Layer

All external DAO traffic passes through a hardened perimeter before reaching any governance or inference service.

```text
Internet
   │
   ▼
External proxy / tunnel
   │
   ▼
Caddy gateway (TLS termination, token enforcement)
   │
   ▼
Auth service (token validation)
   │
   ▼
Main inference and routing layer
   │
   ▼
MountainShares DAO services
```

Enforcement properties:

- No unauthenticated DAO access — requests must carry valid tokens.
- No direct container exposure — services bind to loopback; public endpoints are mediated through the gateway.
- Single entry path — external clients see only the gateway; all downstream calls originate from authenticated internal routes.

This perimeter is part of the governance architecture, not merely network plumbing. It ensures that external actors cannot bypass governance or pretend to be internal services, and that rural communities using a simple web interface still benefit from rigorous boundary protection.

---

## 3.6 Impersonation Detection and Constitutional Alignment at the DAO Boundary

Impersonation detection protocols protect the constitutional integrity of the DAO boundary. They operate at the same boundary as the external perimeter and the blood‑brain barrier.

Their function is to detect and block attempts to impersonate:

- System identity (internal services, governance components).
- Community identity (token holders, stake records, GBIM entities).
- Constitutional authority (DAO charter, state or federal constitutional texts).

These protocols act on content before it enters governance flows. Inputs that fail impersonation checks or constitutional alignment are rejected at the boundary rather than passed downstream to DAO services or recorded as proposals.

In practice, this means that neither a misconfigured script nor a malicious external client can easily pose as “the county’s coordinator” or “a legitimate stakeholder” in order to push a proposal through.

---

## 3.7 Sandbox‑Origin Governance Inputs

MountainShares DAO recommendations and governance proposals originate from validated sandbox reasoning, not from raw model output.

The sequence is:

- Initial deliberation about a governance question occurs in an internal reasoning sandbox.
- Candidate proposals are produced as sandbox hypotheses, not as immediate DAO artifacts.
- Evidence, context, semantic retrieval, and GBIM queries contribute to sandbox reasoning.
- Judges evaluate the sandbox state for truth, coherence, ethics, and alignment.
- Constitutional and privacy gates evaluate the state for legal, disclosure, and harm constraints.

Only after passing this combination of evaluations can a candidate proposal be promoted to a DAO‑visible recommendation or governance artifact.

The mental model is:

> DAO proposals are promoted from sandbox reasoning under gates, not emitted directly from a model.

For a rural leader looking at the MountainShares interface, this guarantees that the “recommended options” presented on screen have been through rigorous internal reasoning and review, rather than being unfiltered suggestions.

---

## 3.8 Blood‑Brain Barrier and DGM Gates for Governance Actions

Downstream from sandbox reasoning, the blood‑brain barrier (BBB) and Darwin–Gödel Machine (DGM) gates govern whether proposals can affect voting, governance actions, or persistent state.

Promotion between state spaces can be described as:

\[
S_{\mathrm{raw}} \rightarrow S_{\mathrm{sandbox}} \rightarrow S_{\mathrm{validated}} \rightarrow S_{\mathrm{memory}} \rightarrow S_{\mathrm{action}}
\]

For DAO governance:

- \(S_{\mathrm{raw}}\) includes external inputs, initial retrievals, and unconstrained model outputs.
- \(S_{\mathrm{sandbox}}\) includes internal reasoning states and candidate proposals.
- \(S_{\mathrm{validated}}\) includes proposals that passed truth and coherence checks.
- \(S_{\mathrm{memory}}\) includes recorded governance artifacts and approved decisions.
- \(S_{\mathrm{action}}\) includes proposals that have been enacted as real governance actions.

A promotion operator

\[
T_{\mathrm{promote}} : S_{\mathrm{sandbox}} \rightharpoonup S_{\mathrm{validated}}
\]

is defined only for states that satisfy a combined gate:

\[
G(x) = G_{\mathrm{constitutional}}(x) \land G_{\mathrm{provenance}}(x) \land G_{\mathrm{coherence}}(x) \land G_{\mathrm{privacy}}(x) \land G_{\mathrm{security}}(x) \land G_{\mathrm{domain}}(x)
\]

For MountainShares:

- BBB implements constitutional and safety gates.
- DGMs implement evolutionary and structural gates for self‑modification.
- DAO governance logic implements community and charter gates.

DAO recommendations and governance proposals pass BBB and constitutional checks, as well as relevant DGM gates, before they can influence voting, proposals, or governance actions. Any state that fails the required gates remains a sandbox hypothesis, is rejected, or is routed for human review; it does not become a live governance artifact.

---

## 3.9 Authority Levels in Governance State Transitions

Authority‑level language helps distinguish governance states. A simple illustrative chain is:

\[
a_0 \preceq a_1 \preceq a_2 \preceq a_3 \preceq a_4 \preceq a_5
\]

with example interpretations:

- \(a_0\): untrusted input.
- \(a_1\): observed signal.
- \(a_2\): sandbox hypothesis.
- \(a_3\): corroborated conclusion.
- \(a_4\): approved governance memory.
- \(a_5\): actionable governance state.

For MountainShares:

- External suggestions and raw model ideas sit at lower authority levels.
- Sandbox hypotheses occupy a mid‑authority level.
- Corroborated conclusions rise further.
- Approved governance memory includes recorded proposals and decisions that passed gates.
- Actionable governance state denotes proposals that have been enacted or can be executed.

The key principle is:

\[
(v, a_2) \neq (v, a_4) \neq (v, a_5)
\]

even when the semantic content \(v\) appears unchanged.

A DAO recommendation visible in a human‑facing coordinator is not automatically actionable. It is a state with authority attached. Voting, enactment, and system effects respect authority levels and gate requirements.

---

## 3.10 Commons‑Level Governance and Anonymized Aggregation

MountainShares DAO sometimes reasons at the level of community or commons rather than individual. In those cases, governance logic operates on anonymized or aggregated representations, not on raw personal traces.

At the algebraic level, per‑person subspaces can be seen as sovereign identity spaces; commons‑level state is formed from projections and aggregations:

\[
H_{\mathrm{commons}} = \mathcal{A}\left(\{\Pi_{\mathrm{approved},u}(H_u)\}_{u \in U}\right)
\]

In prose:

- Individual conversational or identity‑bearing state lives in separate, protected spaces.
- Governance‑relevant features are projected, approved, and anonymized before aggregation.
- Commons‑level governance reasoning sees aggregated patterns, distributions, and needs, not raw individual traces.

Commons‑level governance reasoning uses anonymized or aggregated representations derived from approved projections. DAO logic does not treat raw personal traces as governance inputs. Identity protection and non‑surveillance commitments apply equally at the DAO layer and the GBIM layer.

In a rural context, that means the DAO can reason about “which neighborhoods are being underserved” or “which counties are facing repeated infrastructure failure” without exposing or surveilling the personal histories of individual residents.

---

## 3.11 Coordinator, Stake Registry, and Token Service Roles

The coordinator, stake registry, and token service roles operate with governed inputs and authority levels.

Coordinator:

- Presents proposals, votes, and stake views.
- Surfaces sandbox‑origin recommendations that have passed promotion gates.
- Visualizes authority states and status (for example, proposal awaiting gate, approved, enacted).

Stake registry:

- Maps tokens to stake records and verifies governance rights.
- Provides structured authority backing for identity‑linked governance participation.

Token service:

- Issues and validates tokens.
- Operates behind the perimeter and under impersonation detection and constitutional constraints.

None of these services operate on unconstrained model output. All of them consume promoted states whose origin is sandbox reasoning and whose path is governed by gates.

From a user’s perspective, the coordinator UI becomes a trustworthy window into governed state, not a direct feed from a model. The stake and token services ensure that participation is tied to real, verifiable community roles.

---

## 3.12 Systemic Regulator and Governance Modes

A systemic regulator sits above the DAO layer and modulates governance behavior:

- Warmth (community‑care orientation).
- Urgency (response and escalation sensitivity).
- Mode (baseline, elevated, crisis, consolidation, creative, rest).

At the DAO level, this regulator:

- Shapes how strongly certain governance topics are weighted (for example, essential services during a crisis).
- Modulates gate thresholds and human‑review triggers.
- Influences how quickly sandbox hypotheses move toward gate evaluation.

Regulatory modulation does not bypass gates. It scales processes, not authority. Decisions about governance inputs still originate in sandbox reasoning and move through the promotion architecture.

For a rural leader, this means the system can lean toward quicker attention to urgent local issues — like flood damage or clinic closure — while still respecting constitutional and safety boundaries.

---

## 3.13 Canonical Port and Service Table (Narrative)

MountainShares DAO services and their host bindings can be summarized narratively:

- Coordinator UI runs on an internal host port and is published through the perimeter gateway.
- Governance API binds to loopback and is reached only through authenticated internal calls from the gateway and inference layer.
- Community stake registry operates on a dedicated internal port and is never directly exposed.
- Token service binds internally, with issuance and validation mediated by auth and impersonation detection.
- Perimeter and auth components occupy the only publicly reachable ports, terminating TLS and enforcing token presence.
- Regulator and BBB components sit behind these layers, reachable only by trusted internal services.

This narrative port and service description emphasizes that:

- All external reaches go through the perimeter.
- All governance inputs go through sandbox and gates.
- Host and container ports are distinguished to avoid confusion, with no direct container exposure.

---

## 3.14 Production Status Summary

As of this draft:

- Compose validation and service wiring confirm that the MountainShares DAO tier is reachable only through the perimeter and auth layer.
- Gate checks for BBB, constitutional alignment, privacy, and coherence are integrated into the path from sandbox reasoning to DAO‑visible recommendations.
- Governance‑critical services — coordinator, governance API, stake registry, token service — are tied to the promotion architecture and operate on promoted, gated state.
- Sandbox integration is verified: DAO proposals originate from sandbox reasoning rather than direct model output.
- Known warnings and non‑critical service issues are tracked but do not affect gate exit codes or the integrity of governance flows.

MountainShares DAO is thus operating as a governed community edge of Ms. Allis, with proposals, votes, and stake grounded in spatial and semantic memory, accountable to constitutional and community constraints, and shielded by both external perimeter enforcement and internal sandbox promotion gates.

---

*Chapter 3 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*  
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*  
*See LICENSE for terms.*
