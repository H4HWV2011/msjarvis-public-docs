# 3. MountainShares DAO — Governance Architecture, Perimeter, and Live Topology

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 3.1 Why This Matters for Polymathmatic Geography

This chapter describes the MountainShares DAO governance layer — the constitutional, computational, and perimeter architecture that governs how community proposals, token‑mediated stake, and commons‑level resource deliberations flow through Ms. Allis.

MountainShares DAO is explicitly documented as **bounded, nonbinding commons governance**. It operates as a public‑interest, evidence‑grounded recommendation and feedback system over shared infrastructure and local conditions. It does not claim binding municipal or legal authority, does not execute treasury operations, does not offer security‑token or investment returns, and does not enact automatic real‑world enforcement or unconsented identity disclosure.

The architecture supports:

- **P3 – Power has a geometry** by making institutional decision‑making pathways explicit, auditable, and spatially grounded. Commons‑level proposals do not float free of geography; they are evaluated against a semantic and relational substrate that encodes West Virginia counties, GBIM entities, and verified local resources.

- **P5 – Design is a geographic act** by treating every governance schema decision — what proposals are valid, which constitutional constraints apply, which roles may propose, which gates must pass — as a deliberate choice about how commons‑scale voice is distributed across Appalachian communities rather than concentrated in abstract administrative categories.

- **P12 – Intelligence with a ZIP code** by binding DAO deliberations to county‑level infrastructure questions grounded in local resource registries, address points, and GBIM worldview entities, so that governance recommendations are answerable to specific places and people rather than to abstract token economics alone.

- **P16 – Power accountable to place** by requiring that all external DAO traffic pass through a hardened perimeter and all internal DAO reasoning pass through sandbox gates, so that no governance route is reachable without a valid token and permitted role, and no proposal reaches a recorded recommendation state without passing truth, constitutional, privacy, consent, and system‑safety checks.

MountainShares DAO is therefore not a standalone web application and not a binding legal authority. It is the community commons governance edge of a larger governed organism. Proposals, feedback, votes, token‑mediated stake, and resource deliberations are evaluated against constitutional constraints, bounded by scope rules, grounded in spatial and semantic memory, modulated by a systemic regulator, and protected by both an external perimeter and an internal sandbox promotion architecture.

In plain language, MountainShares DAO is the part of Ms. Allis that lets communities in West Virginia — and similar rural regions — submit structured feedback and recommendations about shared resources together, with every recommendation tied back to real counties, real infrastructure, and real people, while clearly remaining a nonbinding, evidence‑grounded commons governance workflow.

---

## 3.2 Purpose and Scope

The MountainShares DAO is the commons‑governance layer of the Ms. Allis organism. It is a governed edge of a larger distributed system — one in which proposals, feedback items, votes, token‑mediated stake, and resource‑allocation recommendations must originate from validated sandbox reasoning and must move through explicit promotion gates before they can be recorded or surfaced in user‑facing coordination interfaces.

This chapter documents:

- the live MountainShares service topology as it exists in the production stack;
- the perimeter and authentication layers that govern all external access, including the DAO tier;
- the systemic regulator above the DAO layer and its influence on governance modes;
- impersonation detection and constitutional alignment checks at the DAO boundary;
- the gates that ensure DAO proposals are derived from sandboxed reasoning and constitutionally, privacy, and consent‑filtered before they are eligible to be written into commons governance records; and
- the distinction between sandbox hypothesis, corroborated conclusion, approved governance memory, and nonbinding actionable state in the MountainShares context.

DAO governance inputs are documented as sandboxed and constitutionally filtered rather than as direct AI outputs. Where naïve descriptions might imply “the system outputs a proposal and the DAO acts,” the accurate sequence is: the system reasons in a sandbox, proposals are formed as governed candidate commons states, gates evaluate those candidates, and only promoted conclusions may be written into governance records or surfaced in coordination UIs — always under the nonbinding, public‑interest, commons scope constraints described in the gate.

---

## 3.3 Live MountainShares Service Topology

The MountainShares governance tier consists of several services that together implement community‑facing coordination, proposal evaluation, stake registry, and token validation for bounded commons governance. They are part of the larger Ms. Allis service graph and operate under a governed promotion architecture.

```text
┌─────────────────────────────────────────────────────────────┐
│                 MountainShares Governance Services          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Coordinator UI           — proposals, feedback, votes      │
│  Governance API           — evaluates and records           │
│                             commons-governance items        │
│  Community Stake Registry — maps tokens to stake records    │
│  Token Service            — issues and validates tokens     │
│                                                             │
│  All services sit behind a perimeter and are fed by         │
│  sandboxed reasoning, not direct model output.              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Host‑visible governance services sit downstream of the main inference and routing layer. No external client reaches them directly; all external access is mediated by perimeter and authentication components, and all internal reasoning that feeds them is mediated by sandbox and gate components.

For a rural community, this means the screens they see — the coordinator UI showing proposals, feedback, votes, and stake — are backed by services that never act on unreviewed, unconstrained suggestions. Every commons governance artifact has passed through structured reasoning, evidence checks, and gatekeeping before it appears, and its scope is clearly recorded as nonbinding, public‑interest, commons‑focused.

---

## 3.4 Constitutional and Token Architecture

MountainShares DAO operates under a layered constitutional framework and a token‑based stake registry. That framework applies both to external requests and to internal reasoning about commons governance.

Constitutionally:

- federal and state constitutional texts provide a legal and normative frame for what counts as permissible and non‑harmful public reasoning;
- a DAO charter defines community governance rules and scope, including nonbinding status and public‑interest focus; and
- GBIM worldview entities encode an equity‑oriented interpretive base that shapes how infrastructure and benefit trade‑offs are analysed.

Token‑mediated stake:

- tokens represent **community stake and participation rights**, not financial instruments or security tokens;
- a stake registry maps token holders to verifiable stake records in relational and GBIM substrates, linking stake to community roles and affected places; and
- a token service issues and validates tokens behind the perimeter, enforcing scope and preventing impersonation.

Token and constitutional architecture govern how proposals are allowed to exist and move, not just how they are displayed. A proposal’s path from sandbox hypothesis to nonbinding actionable commons state is constrained by:

- permitted role (for example, municipal partner, community member);
- affected place (e.g., a county, a road segment, a drainage basin);
- community scope (e.g., public civic infrastructure, shared services);
- public‑interest orientation (no private profit or token‑return claims);
- evidence reference count; and
- consent flags where identity or sensitive data are involved.

A county‑level proposal to adjust a drainage pattern near a public road, for example, is only admitted into the recorded governance process if:

- the proposer holds a permitted role with valid stake;
- the proposal’s content is consistent with the DAO charter and constitutional obligations;
- the supporting evidence references meet minimum thresholds; and
- consent is obtained where required for identity‑bearing inputs.

Even then, the proposal is recorded as a **bounded, nonbinding commons governance record** rather than as an enforceable legal act.

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
Gateway (TLS termination, token enforcement)
   │
   ▼
Auth service (token validation, role checks)
   │
   ▼
Main inference and routing layer
   │
   ▼
MountainShares DAO services
```

Enforcement properties include:

- no unauthenticated DAO access — requests must carry valid tokens and roles;
- no direct container exposure — services bind to loopback; public endpoints are mediated through the gateway; and
- a single entry path — external clients see only the gateway; all downstream calls originate from authenticated internal routes.

This perimeter is part of the governance architecture, not merely network plumbing. It ensures that external actors cannot bypass governance, impersonate internal services, or directly tamper with the commons‑governance records, and that rural communities using a simple web interface still benefit from rigorous boundary protection and role enforcement.

---

## 3.6 Impersonation Detection and Constitutional Alignment at the DAO Boundary

Impersonation detection protocols protect the constitutional integrity of the DAO boundary. They operate at the same boundary as the external perimeter and the blood‑brain barrier.

Their function is to detect and block attempts to impersonate:

- system identity (internal services, governance components);
- community identity (token holders, stake records, GBIM entities); and
- constitutional authority (DAO charter, state or federal constitutional texts).

These protocols act on content and metadata before inputs enter governance flows. Requests that fail impersonation checks, misrepresent roles, over‑claim authority, or violate constitutional alignment are rejected at the boundary rather than passed downstream to DAO services or recorded as proposals.

In practice, this means that neither a misconfigured script nor a malicious external client can easily pose as “the county’s coordinator” or “a municipal partner with legal authority” in order to push a binding proposal through; attempts to claim external legal authority are routed to human review and documented as such, not accepted as automatic authority.

---

## 3.7 Sandbox‑Origin Governance Inputs

MountainShares DAO recommendations and commons governance proposals originate from validated sandbox reasoning, not from raw model output.

The sequence is:

- initial deliberation about a governance question occurs in an internal reasoning sandbox;
- candidate proposals are produced as sandbox hypotheses, not as immediate DAO artifacts;
- evidence, context, semantic retrieval, and GBIM queries contribute to sandbox reasoning;
- judges evaluate the sandbox state for truth, coherence, ethics, and alignment with worldview and mission; and
- constitutional, privacy, consent, and scope gates evaluate the state for legal, disclosure, community, and harm constraints.

Only after passing this combination of evaluations can a candidate proposal be promoted to a DAO‑visible recommendation or recorded commons governance artifact. Proposals without evidence references, without required consent, or carrying financial/token‑return claims are rejected or flagged before they ever reach recorded state.

The operative mental model is:

> Commons governance proposals are promoted from sandbox reasoning under gates, not emitted directly from a model, and they remain nonbinding recommendations.

For a rural leader looking at the MountainShares interface, this guarantees that the “recommended options” presented on screen have been through structured internal reasoning and review, rather than being unfiltered suggestions or automatic enforcement actions.

---

## 3.8 Blood‑Brain Barrier and DGM Gates for Governance Actions

Downstream from sandbox reasoning, the blood‑brain barrier (BBB) and Darwin–Gödel Machine (DGM) gates govern whether proposals can:

- be recorded as commons governance artifacts;
- be surfaced in coordinator UIs; or
- influence downstream decision support.

Promotion between state spaces can be described as:

\[
S_{\mathrm{raw}} \rightarrow S_{\mathrm{sandbox}} \rightarrow S_{\mathrm{validated}} \rightarrow S_{\mathrm{memory}} \rightarrow S_{\mathrm{action}}
\]

For MountainShares DAO:

- \(S_{\mathrm{raw}}\) includes external inputs, initial retrievals, and unconstrained model outputs;
- \(S_{\mathrm{sandbox}}\) includes internal reasoning states and candidate proposals;
- \(S_{\mathrm{validated}}\) includes proposals that passed truth and coherence checks under commons scope;
- \(S_{\mathrm{memory}}\) includes recorded governance artifacts and approved commons decisions; and
- \(S_{\mathrm{action}}\) includes nonbinding recommendations and feedback items that may be seen and acted upon by humans, not automatic enforcement.

A promotion operator:

\[
T_{\mathrm{promote}} : S_{\mathrm{sandbox}} \rightharpoonup S_{\mathrm{validated}}
\]

is defined only for states that satisfy a combined gate:

\[
G(x) = G_{\mathrm{constitutional}}(x) \land G_{\mathrm{provenance}}(x) \land G_{\mathrm{coherence}}(x) \land G_{\mathrm{privacy}}(x) \land G_{\mathrm{consent}}(x) \land G_{\mathrm{scope}}(x)
\]

For MountainShares:

- BBB implements constitutional, safety, and privacy gates;
- DGMs implement evolutionary and structural gates for system‑change and self‑modification; and
- DAO governance logic implements community, consent, and charter gates, including rejection of financial/token‑return claims.

DAO recommendations and governance proposals pass BBB and constitutional checks, as well as relevant DGM and scope gates, before they can influence recorded commons governance or user‑facing coordinator views. Any state that fails the required gates remains a sandbox hypothesis, is rejected, or is routed for human review; it does not become a live governance artifact or binding action.

---

## 3.9 Authority Levels in Governance State Transitions

Authority‑level language helps distinguish governance states in MountainShares. A simple illustrative chain is:

\[
a_0 \preceq a_1 \preceq a_2 \preceq a_3 \preceq a_4 \preceq a_5
\]

with example interpretations:

- \(a_0\): untrusted input;  
- \(a_1\): observed signal;  
- \(a_2\): sandbox hypothesis;  
- \(a_3\): corroborated conclusion;  
- \(a_4\): approved governance memory (recorded commons governance item);  
- \(a_5\): actionable commons state (nonbinding recommendation visible to humans).

For MountainShares:

- external suggestions and raw model ideas sit at lower authority levels (\(a_0\), \(a_1\));
- sandbox hypotheses occupy mid‑authority (\(a_2\));
- corroborated conclusions rise further (\(a_3\));
- approved governance memory includes recorded proposals and decisions that passed gates (\(a_4\));
- actionable commons state denotes proposals that have been surfaced for human action or follow‑up (\(a_5\)), while remaining nonbinding.

The key principle is:

\[
(v, a_2) \neq (v, a_4) \neq (v, a_5)
\]

even when the semantic content \(v\) appears unchanged.

A DAO recommendation visible in a human‑facing coordinator is not automatically enforceable; it is a state with authority and scope attached. Voting, enactment, and system effects respect authority levels and gate requirements, and any binding municipal or legal acts are handled outside the DAO by human institutions.

---

## 3.10 Commons‑Level Governance and Anonymized Aggregation

MountainShares DAO often reasons at the level of community or commons rather than individual. In those cases, governance logic operates on anonymized or aggregated representations, not on raw personal traces.

At the algebraic level, per‑person subspaces can be seen as sovereign identity spaces; commons‑level state is formed from projections and aggregations:

\[
H_{\mathrm{commons}} = \mathcal{A}\left(\{\Pi_{\mathrm{approved},u}(H_u)\}_{u \in U}\right)
\]

In prose:

- individual conversational or identity‑bearing state lives in separate, protected spaces;
- governance‑relevant features (for example, counts of affected households, density of infrastructure failures) are projected, approved, and anonymized before aggregation; and
- commons‑level governance reasoning sees aggregated patterns, distributions, and needs, not raw individual traces.

Commons‑level governance reasoning uses anonymized or aggregated representations derived from approved projections. DAO logic does not treat raw personal traces as governance inputs. Identity protection, consent requirements, and non‑surveillance commitments apply equally at the DAO layer and the GBIM layer.

In a rural context, this allows the DAO to reason about “which neighbourhoods are underserved,” “which counties face repeated infrastructure failure,” or “where drainage problems accumulate” without exposing or surveilling personal histories.

---

## 3.11 Coordinator, Stake Registry, and Token Service Roles

The coordinator, stake registry, and token service roles operate with governed inputs, authority levels, and scope constraints.

Coordinator:

- presents commons governance proposals, feedback items, votes, and stake views;
- surfaces sandbox‑origin recommendations that have passed promotion gates and scope checks;
- visualises authority states and status (for example, proposal awaiting gate, approved, surfaced); and
- clearly indicates nonbinding status and public‑interest focus.

Stake registry:

- maps tokens to stake records and verifies governance participation rights;
- links stake to roles, affected places, and community scopes; and
- provides structured authority backing for identity‑linked participation under consent and privacy rules.

Token service:

- issues and validates tokens as participation credentials rather than financial instruments;
- operates behind the perimeter and under impersonation detection and constitutional constraints; and
- enforces that financial or token‑return claims are out of scope.

None of these services operate on unconstrained model output. All of them consume promoted states whose origin is sandbox reasoning and whose path is governed by gates and scope predicates.

From a user’s perspective, the coordinator UI becomes a trustworthy window into bounded commons governance state, not a direct feed from a model or a binding legal instrument. The stake and token services ensure that participation is tied to real, verifiable community roles, affected places, and explicitly limited scopes.

---

## 3.12 Systemic Regulator and Governance Modes

A systemic regulator sits above the DAO layer and modulates governance behaviour:

- warmth (community‑care orientation);  
- urgency (response and escalation sensitivity); and  
- governance modes (baseline, elevated, crisis, consolidation, creative, rest).

At the DAO level, this regulator:

- shapes how strongly certain governance topics are weighted (for example, essential services during a flood event);
- modulates gate thresholds and human‑review triggers; and
- influences how quickly sandbox hypotheses move toward gate evaluation and surfacing.

Regulatory modulation does not bypass gates and does not change nonbinding scope. It scales processes, not authority. Decisions about governance inputs still originate in sandbox reasoning, pass through promotion architecture, and remain bounded commons recommendations.

For rural leaders, this means the system can lean toward quicker attention to urgent local issues — like road drainage failures or clinic closure risks — while still respecting constitutional, consent, and safety boundaries, and while clearly signalling that MountainShares outputs are advisory, not enacting law.

---

## 3.13 Canonical Port and Service Table (Narrative)

MountainShares DAO services and their host bindings can be summarised narratively:

- the coordinator UI runs on an internal host port and is published through the perimeter gateway;
- the governance API binds to loopback and is reached only through authenticated internal calls from the gateway and inference layer;
- the community stake registry operates on a dedicated internal port and is never directly exposed;
- the token service binds internally, with issuance and validation mediated by auth and impersonation detection; and
- perimeter and auth components occupy the only publicly reachable ports, terminating TLS and enforcing token presence and role checks.

Regulator, BBB, and commons gateway components sit behind these layers and are reachable only by trusted internal services. This binding regime emphasises that:

- all external reaches go through the perimeter and auth;
- all governance inputs go through sandbox and gates; and
- host and container ports are distinguished to avoid accidental exposure of internal DAO or commons governance services.

---

## 3.14 Production Status Summary

As of this draft:

- compose validation and service wiring confirm that the MountainShares DAO tier is reachable only through the perimeter and auth layer;
- gate checks for BBB, constitutional alignment, privacy, consent, and coherence are integrated into the path from sandbox reasoning to DAO‑visible recommendations;
- governance‑critical services — coordinator, governance API, stake registry, token service — are tied to the promotion architecture and operate on promoted, gated, scope‑checked state;
- commons‑governance collections (`commons_rag`, `community_hilbert_commons`, `mountainshares_dao_governance_records`) are runtime‑visible and wired to the promotion architecture as bounded nonbinding governance records; and
- sandbox integration is verified: DAO proposals originate from sandbox reasoning rather than direct model output, and binding legal authority, treasury operations, security‑token behaviour, financial returns, and unconsented identity disclosure are explicitly out of scope.

MountainShares DAO is thus operating as a governed community edge of Ms. Allis, with proposals, votes, and stake grounded in spatial and semantic memory, accountable to constitutional and community constraints, and shielded by both external perimeter enforcement and internal sandbox promotion gates, within a clearly bounded, nonbinding commons governance framework.

---

*Chapter 3 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*  
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*  
*See LICENSE for terms.*
