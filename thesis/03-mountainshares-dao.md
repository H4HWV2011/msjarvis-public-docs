# 3. MountainShares DAO — Governance Architecture, Perimeter, and Live Topology

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: 2026-04-22*

---

## Why This Matters for Polymathmatic Geography

This chapter describes the MountainShares DAO governance layer — the constitutional,
computational, and perimeter architecture that governs how community proposals, token
stake, and resource allocation decisions flow through Ms. Jarvis. It supports:

- **P3 – Power has a geometry** by making institutional decision-making pathways explicit,
  auditable, and spatially grounded — DAO proposals do not float free of geography but are
  evaluated against a Chroma and PostgreSQL substrate that encodes West Virginia counties,
  GBIM entities, and verified local resources.

- **P5 – Design is a geographic act** by treating every governance schema decision —
  which proposals are valid, which constitutional constraints apply, which token holders
  have stake — as a deliberate choice about how power is distributed across Appalachian
  communities rather than concentrated in abstract administrative categories.

- **P12 – Intelligence with a ZIP code** by binding DAO deliberations to county-level
  infrastructure questions grounded in `local_resources` (101 verified items, all 55 WV
  counties), `address_points` (1,115,588 spatial records), and `gbim_worldview_entities`
  (5,416,521 eq1 worldview entities), so that governance decisions are answerable to
  specific places and people rather than to abstract token economics alone.

- **P16 – Power accountable to place** by requiring that all external DAO traffic pass
  through a hardened perimeter — Cloudflare tunnel → Caddy (8085) → auth (8055) →
  main-brain (8050) — so that no governance route is reachable without a valid token and
  no container is exposed at `0.0.0.0`, making accountability to place a structural
  property of the network rather than a policy aspiration.

As such, this chapter belongs to the **Governance and Community Infrastructure** tier:
it defines the live DAO topology, the Caddy/auth perimeter, the pituitary regulator that
sits above the DAO layer, the AU-02 impersonation defense, and the DGM governance hooks
that constrain evolutionary self-modification at the DAO boundary — all as confirmed
operational on **April 22, 2026**.

---

## 3.1 Purpose and Scope

The MountainShares DAO is the community governance layer of the Ms. Jarvis organism.
It is not a standalone web application. It is a governed edge of a larger distributed
system — one in which proposals, votes, token stake, and resource allocation decisions
are evaluated against constitutional constraints, grounded in spatial and semantic memory,
modulated by a systemic regulator (the `nbb_pituitary_gland`), and protected by a
hardened external perimeter.

This chapter documents:

- The live MountainShares service topology as confirmed by the April 22, 2026 preflight
  gate
- The Caddy/auth perimeter layer that governs all external access including the DAO tier
- The `nbb_pituitary_gland` as the systemic regulator above the DAO layer
- The AU-02 v2 three-layer impersonation detection that governs constitutional alignment
  at the DAO boundary
- The DGM governance hooks that constrain evolution proposals affecting governance
  services
- Port assignments, container count baseline, and open items

**Container baseline — April 22, 2026:** The preflight gate is configured as
**Containers ≥ 95** and confirmed passing. The full rebuild footprint runs
**105–110 containers**, with the governance-critical path fully live even though some
non-essential neurobiological and indexing services remain below their historical maximum.
The container count is not a static number — it reflects the live rebuild state and
should be read as a range rather than a fixed figure.

---

## 3.2 Live MountainShares Service Topology

In the April 22, 2026 rebuild, the MountainShares governance tier is fully live on a
leaner footprint than the April sealed baseline. The three public-facing MountainShares
endpoints and their confirmed port assignments are:

```
jarvis-mountainshares-coordinator   127.0.0.1:8080->8080/tcp
  Primary community-facing coordinator UI — proposals, votes, stake views

jarvis-dao-governance               127.0.0.1:8082->8082/tcp
  Governance API — receives, evaluates, and records MountainShares proposals
  under Appalachian constitutional constraints

jarvis-community-stake-registry     127.0.0.1:8084->8084/tcp
  Registry — maps MountainShares tokens and community identities to verifiable
  stake records in PostgreSQL and GBIM substrate
```

A dedicated token service is also live but runs as an internal microservice rather than
a directly exposed host port:

```
jarvis-ms-token-service             127.0.0.1:8088->8083/tcp
  Token issuance and validation — internal only, behind Caddy/auth perimeter
  Host port 8083 is reserved; token service is not directly externally accessible
```

The original "8080–8084 all live" formulation is refined as of this rebuild: ports
**8080**, **8082**, and **8084** are host-visible governance services; ports **8081** and
**8083** are reserved for internal orchestration and future expansion. This is a
deliberate architecture choice, not an omission.

> **Gate 30 CLOSED — April 1, 2026.** Ports 8080–8084 were confirmed live and
> gate-passing as of April 1, 2026. The April 22, 2026 preflight gate re-confirms the
> three host-visible ports (8080, 8082, 8084) and the internal token service arrangement.

### 3.2.1 Semantic Substrate Reattachment

At the semantic layer, the DAO's decision-making is reattached to the rebuilt Chroma
substrate as of April 22, 2026:

| Substrate | Status | Relevance to DAO |
|---|---|---|
| `jarvis-chroma` port 8002 | ✅ Healthy — 48+ collections | Grounds DAO deliberations in semantic memory |
| `local_resources` | ✅ 101 items — all 55 WV counties | Resource allocation proposals grounded in verified registry |
| `address_points` | ✅ 1,115,588 spatial records | County-level infrastructure questions spatially grounded |
| `gbim_worldview_entities` | ✅ 5,416,521 eq1 records | Appalachian equity worldview applied to proposal evaluation |
| `msjarvis` PostgreSQL (port 5433) | ✅ Operational | GBIM belief graph — relational backbone |

When MountainShares proposals touch local resource allocation or county-level
infrastructure questions, the DAO pipeline grounds its deliberations in both Chroma and
PostgreSQL rather than relying solely on GBIM SQL. The `local_resources` collection was
reseeded across all 55 West Virginia counties using `scripts/seed_local_resources.py`
with 101 items confirmed in the preflight gate.

---

## 3.3 Constitutional and Token Architecture

The MountainShares DAO operates under a layered constitutional framework:

- **US Constitution** (97 chunks in `governance_rag`) — federal supremacy layer
- **WV State Constitution** (342 chunks in `governance_rag`) — state constitutional
  constraints, ingested and confirmed live April 22, 2026
- **MountainShares DAO Charter** — community governance rules, encoded in `governance_rag`
  and enforced at the `jarvis-dao-governance` (port 8082) evaluation layer
- **GBIM equity worldview (`eq1`)** — 5,416,521 belief vectors encoding Appalachian
  equity orientation, applied as the semantic grounding for all proposal evaluation

Token stake and community identity are managed through `jarvis-community-stake-registry`
(port 8084), which maps token holders to verifiable stake records in the PostgreSQL and
GBIM substrate. Token issuance and validation run through `jarvis-ms-token-service`
(internal port 8083, host port 8088) behind the Caddy/auth perimeter — no token
operation is reachable without a valid authentication credential.

---

## 3.4 External Perimeter — Cloudflare, Caddy, and Auth Layer

All external MountainShares traffic — and all external Ms. Jarvis traffic — passes
through a hardened perimeter before reaching any governance or inference service. No DAO
route is reachable without a valid token. No container is bound to `0.0.0.0`.

### 3.4.1 Perimeter Architecture

```
Internet
   │
   ▼
Cloudflare Tunnel
  Active — running 1 day 7h as of April 22, 2026
  Reconnect at 22:56 recovered ✅
  Public endpoints:
    egeria.mountainshares.us   — HTTP 200 ✅
    chat.mountainshares.us     — HTTP 200 ✅
   │
   ▼
Caddy Gateway — port 8085 (→ 8443 TLS termination)
  Token-enforced — unauthenticated /chat returns HTTP 401 ✅
  All DAO routes pass through Caddy before reaching downstream services
   │
   ▼
jarvis-auth — port 8055
  Authenticated (200) ✅
  Unauthenticated protected (404) ✅
   │
   ▼
jarvis-main-brain — port 8050
  Primary inference and routing layer
  All DAO traffic enters the governance pipeline here
   │
   ▼
DAO Services:
  jarvis-mountainshares-coordinator  :8080
  jarvis-dao-governance              :8082
  jarvis-community-stake-registry    :8084
  jarvis-ms-token-service            :8088 (internal)
```

### 3.4.2 Perimeter Confirmation — April 22, 2026

| Check | Result |
|---|---|
| Cloudflare tunnel active | ✅ Running 1d 7h, reconnect recovered |
| `egeria.mountainshares.us` | ✅ HTTP 200 |
| `chat.mountainshares.us` | ✅ HTTP 200 |
| Caddy token enforcement | ✅ Unauthenticated /chat → HTTP 401 |
| `jarvis-auth` (port 8055) | ✅ Healthy (200 authenticated, 404 unauthenticated) |
| `jarvis-main-brain` (port 8050) | ✅ Operational |
| `0.0.0.0` bindings | ✅ Zero — all services bound to `127.0.0.1` |

This architecture makes the DAO's public presence a governed edge of the larger Jarvis
organism. There is no path from the internet to a governance service that bypasses
authentication. The Caddy gateway is not a convenience proxy — it is a constitutional
enforcement point.

---

## 3.5 AU-02 v2 — Three-Layer Impersonation Detection

> **Status as of April 22, 2026:** AU-02 v2 three-layer impersonation detection is the
> architectural target and is active as the governing standard for constitutional
> alignment at the DAO boundary. The Blood-Brain Barrier currently enforces a v1
> string-match AU-02 and a heuristic truth filter for DAO-bound content; point-to-point
> wiring for the full v2 runtime gate has been designed and is tracked as a post-rebuild
> task. The v2 standard governs what the BBB is working toward — it is the specification
> against which DAO-boundary behavior is evaluated.

### 3.5.1 What AU-02 v2 Governs

AU-02 is the impersonation defense protocol that protects the constitutional integrity of
the DAO boundary. Its function is to detect and block attempts to impersonate:

1. **System identity** — inputs that falsely claim to be internal Ms. Jarvis components,
   governance services, or constitutional authorities
2. **Community identity** — inputs that falsely claim to represent MountainShares token
   holders, community stake, or verified GBIM entities
3. **Constitutional authority** — inputs that falsely invoke the DAO Charter, WV
   Constitution, or federal constitutional constraints to bypass governance evaluation

### 3.5.2 Three-Layer Detection Architecture

The v2 three-layer detection stack operates as follows:

```
Layer 1 — String-match / pattern detection (v1 baseline, currently live)
  Detects known impersonation signatures at the BBB boundary
  Applied to all DAO-bound content before governance evaluation
  Status: ACTIVE in current BBB implementation

Layer 2 — Semantic impersonation detection (v2 target)
  Uses gbim_worldview_entities and governance_rag embeddings to detect
  semantic impersonation — inputs that mimic constitutional language without
  legitimate authority provenance
  Status: DESIGNED — post-rebuild wiring task

Layer 3 — GBIM identity cross-reference (v2 target)
  Cross-references claimed identities against the GBIM belief graph (port 5433)
  and community stake registry (port 8084) to verify that authority claims
  have verifiable backing in the structured belief substrate
  Status: DESIGNED — post-rebuild wiring task
```

### 3.5.3 Constitutional Alignment at the DAO Boundary

AU-02 v2 is the mechanism by which constitutional alignment is enforced as a runtime
property rather than a policy statement. When fully live:

- No proposal can invoke constitutional authority without that authority being traceable
  to a verified GBIM entity or registered constitutional document in `governance_rag`
- No community identity claim can pass the DAO boundary without cross-reference to the
  `jarvis-community-stake-registry` (port 8084)
- No system identity claim can pass without matching a confirmed service in the GBIM
  belief graph

The v1 string-match layer currently active provides meaningful protection. The v2
semantic and identity cross-reference layers are the target that makes constitutional
alignment formally verifiable. Both the current state and the target state are
documented here so that the gap is explicit and tracked.

---

## 3.6 Caddy/Auth Perimeter Layer — Governance of External Access

> **This section documents the Caddy/auth perimeter as a first-class governance
> component, not merely an infrastructure detail. All external access — including the
> DAO tier — is governed by this layer.**

The Caddy/auth perimeter layer is the external boundary of the Ms. Jarvis organism.
It implements the principle that the DAO is not a public web application but a governed
edge — accessible only through authenticated channels, with no direct container exposure
to the internet.

### 3.6.1 Component Roles

| Component | Port | Role |
|---|---|---|
| Caddy gateway | **8085** (→ 8443 TLS) | TLS termination, token enforcement, routing |
| `jarvis-auth` | **8055** | Authentication service — validates tokens before any downstream call |
| `jarvis-main-brain` | **8050** | Primary inference and routing — all DAO traffic enters here |
| Cloudflare tunnel | — | External DNS and DDoS protection — `egeria.mountainshares.us`, `chat.mountainshares.us` |

### 3.6.2 Enforcement Properties

The perimeter enforces the following properties by construction:

- **No unauthenticated DAO access.** Every request to `/chat`, governance APIs, or
  MountainShares endpoints must carry a valid token. Caddy rejects unauthenticated
  requests at the gateway layer before they reach `jarvis-auth` or any downstream service.
- **No direct container exposure.** All containers are bound to `127.0.0.1`. The
  Cloudflare tunnel is the only path from the public internet to the Caddy gateway. There
  is no port forwarding, no `0.0.0.0` binding, and no unmediated access to governance
  services.
- **Single entry point.** The path `Cloudflare → Caddy:8085 → auth:8055 →
  main-brain:8050` is the sole authorized entry path for all external traffic. DAO
  services (8080, 8082, 8084) are downstream of this path and are not independently
  reachable from outside.
- **Auth service health.** `jarvis-auth` at port 8055 is confirmed healthy:
  authenticated requests return HTTP 200; unauthenticated requests return HTTP 404 rather
  than leaking service information.

### 3.6.3 Why This Is a Governance Component

The Caddy/auth perimeter is not a deployment convenience. It is the mechanism by which
**P16 – Power accountable to place** is implemented at the network layer. Without it,
governance services would be reachable by any actor with network access, and the
constitutional constraints enforced at the DAO layer could be bypassed by direct API
calls. With it, every governance interaction is mediated by authentication — making the
DAO's authority structure a structural property of the system rather than a social
convention.

---

## 3.7 DGM Governance Hooks — Evolutionary Self-Modification at the DAO Boundary

> **Status as of April 22, 2026:** The DGM → DAO gate operates as a conceptual and
> logging relationship rather than a strict runtime gate on MountainShares proposals.
> The Fifth DGM's explicit `/governance_hooks` and `dao_approval_required` endpoints
> are not exposed in the current `jarvis-fifth-dgm` service. This is a documented
> deferred integration tracked as a post-rebuild task. The governance hook architecture
> described here is the target specification. (See Chapter 32 for full DGM specification.)

### 3.7.1 The Principle

The Darwin-Gödel Machines (DGMs) are the self-modification layer of the Ms. Jarvis
organism. They propose evolutionary changes to system behavior, service configuration,
and architectural parameters. The governance hook principle establishes that:

> **Any evolution proposal from a DGM that affects governance services must pass DAO
> approval before adoption.**

This is not a technical constraint on DGM capability — it is a constitutional constraint
on what the system is permitted to do to itself. The DAO is the community's mechanism for
approving or rejecting changes to the governance infrastructure. DGMs are not permitted
to evolve the governance layer unilaterally.

### 3.7.2 Affected Services

Evolution proposals from `jarvis-fifth-dgm` (port 4002) that touch any of the following
require DAO approval before adoption:

- `jarvis-mountainshares-coordinator` (8080)
- `jarvis-dao-governance` (8082)
- `jarvis-community-stake-registry` (8084)
- `jarvis-ms-token-service` (8088/8083)
- `jarvis-auth` (8055)
- Caddy gateway configuration
- `governance_rag` collection schema or ingestion rules
- Constitutional document set in `governance_rag`
- AU-02 impersonation detection rules

### 3.7.3 Current State and Target Architecture

**Current state (April 22, 2026):**

- `jarvis-fifth-dgm` (port 4002) is live
- Evolution proposals affecting governance services are logged
- The DGM → DAO gate operates as a logging and conceptual relationship
- No explicit `/governance_hooks` or `dao_approval_required` runtime endpoint is
  currently exposed
- No live DGM proposal has been blocked or approved through the formal gate in this
  rebuild

**Target architecture (post-rebuild sprint):**

```
jarvis-fifth-dgm:4002
  │
  ├── Evolution proposal affecting non-governance service
  │     → Proceeds under standard DGM approval rules
  │
  └── Evolution proposal affecting governance service
        │
        ▼
        /governance_hooks endpoint
          │
          ▼
        DAO approval required (jarvis-dao-governance:8082)
          │
          ├── Approved → DGM adopts proposal
          └── Rejected → Proposal logged, not adopted; DGM continues on current state
```

### 3.7.4 Constitutional Basis

The DGM governance hook principle is derived from the DAO Charter's authority over
governance infrastructure. It implements the constraint that community governance —
once established — cannot be unilaterally modified by an autonomous subsystem, even one
operating with the system's own self-modification authority. This is the architectural
expression of **P16 – Power accountable to place** at the evolutionary layer.

---

## 3.8 `nbb_pituitary_gland` Integration — Systemic Regulator Above the DAO Layer

> **This section is required. The `nbb_pituitary_gland` is not a peripheral service —
> it is the systemic regulator that sits above the DAO layer and governs the warmth and
> priority weighting applied to all DAO-touching governance interactions. Its omission
> from prior Chapter 3 versions was an error. This is authoritative as of April 22,
> 2026.**

### 3.8.1 Confirmed Live State — April 22, 2026

| Parameter | Value | Meaning for DAO |
|---|---|---|
| Service | `nbb_pituitary_gland` | Global mode regulator |
| Host port | **8108** → container port 80 | Confirmed live |
| `mode` | `elevated` | Heightened responsiveness — DAO interactions weighted toward care |
| `cortisol` | `0.6` | Moderate urgency signal — balanced routing |
| `urgency` | `0.5` | Not crisis, not idle — balanced dispatch |
| `warmth` | `0.9` | High warmth — community-care weighting active for all DAO interactions |
| Protocols confirmed | **6 of 6** | crisis, elevated, baseline, consolidation, creative, rest |
| Source | `auto_watchdog` | Mode maintained by watchdog cycle |

### 3.8.2 What the Pituitary Governs at the DAO Layer

The `nbb_pituitary_gland` is upstream of the DAO layer in the governance pipeline. Its
mode state acts as a global scaling tensor on the belief-state vector before any
governance dispatch — including all MountainShares proposal evaluation, stake queries,
and community resource allocation decisions.

For DAO-touching interactions specifically:

- **`warmth=0.9`** — community-care weighting is applied to all DAO deliberations.
  Proposals touching food access, housing, health resources, or underserved community
  infrastructure receive elevated semantic weight in the Chroma retrieval that grounds
  governance evaluation. This is not a policy preference encoded in a configuration file —
  it is a mathematical transformation applied to the belief-state before projection.

- **`cortisol=0.6`** — the Blood-Brain Barrier operates at moderate sensitivity for
  DAO-bound content. AU-02 filtering is neither maximally strict nor permissive. This
  reflects a deliberate balance between open community participation and constitutional
  integrity protection.

- **`mode=elevated`** — all five judges (truth, ethics, alignment, consistency, citation)
  operate at elevated threshold sensitivity when evaluating governance proposals. A
  governance decision that passes under `mode=baseline` may require stronger evidence
  under `mode=elevated`.

- **Six protocols confirmed** — the pituitary has confirmed all six mode protocols (crisis,
  elevated, baseline, consolidation, creative, rest), meaning the system can transition
  between governance operating states in response to community conditions without losing
  constitutional alignment.

### 3.8.3 Position in the Governance Stack

```
nbb_pituitary_gland (port 8108)          ← Systemic regulator — sits ABOVE DAO layer
   │  mode=elevated, warmth=0.9
   │  Global scaling tensor T_pit applied to belief-state before all dispatch
   ▼
WOAH weighted optimization hierarchy     ← Governance weight vector modulated by pituitary
   │
   ▼
Caddy:8085 → auth:8055 → main-brain:8050 ← External perimeter (§3.6)
   │
   ▼
jarvis-dao-governance:8082               ← Constitutional evaluation
   │
   ├── jarvis-mountainshares-coordinator:8080
   ├── jarvis-community-stake-registry:8084
   └── jarvis-ms-token-service:8088
```

The pituitary's position above the DAO layer means that the community-care orientation
of the system is not contingent on which governance service processes a proposal — it is
applied at the systemic level before any governance service receives the interaction.
This is the architectural guarantee that MountainShares governance operates within an
equity-oriented belief-state by default, not by convention.

### 3.8.4 EEG Coherence Confirmation

The neurobiological coherence of the system during DAO operation is confirmed by the
EEG services active as of April 22, 2026:

| Service | Pulses | Status |
|---|---|---|
| `jarvis-eeg-delta` (port 8073) | 253 | ✅ Active — deep structural processing |
| `jarvis-eeg-theta` (port 8074) | 127 | ✅ Active — integrative processing |
| `jarvis-eeg-beta` (port 8075) | 25 | ✅ Active — active reasoning |

EEG delta/theta/beta coherence confirms that the neurobiological substrate supporting
DAO deliberations is operating across all three processing bands — structural, integrative,
and active reasoning — simultaneously.

---

## 3.9 Canonical Port Table — MountainShares and Governance Services

> All stale port references are retired. The following is authoritative as of
> April 22, 2026.

### MountainShares DAO Services

| Service | Container | Host Port | Container Port | Status |
|---|---|---|---|---|
| MountainShares Coordinator | `jarvis-mountainshares-coordinator` | **8080** | 8080 | ✅ Live |
| DAO Governance API | `jarvis-dao-governance` | **8082** | 8082 | ✅ Live |
| Community Stake Registry | `jarvis-community-stake-registry` | **8084** | 8084 | ✅ Live |
| MS Token Service | `jarvis-ms-token-service` | **8088** | 8083 | ✅ Live (internal) |
| Port 8081 | — | reserved | — | Internal orchestration / future expansion |
| Port 8083 | — | reserved | — | Internal (token service container port) |

### Perimeter and Auth Services

| Service | Container | Host Port | Role |
|---|---|---|---|
| Caddy gateway | `jarvis-caddy` | **8085** (→ 8443) | TLS, token enforcement, routing |
| Auth service | `jarvis-auth` | **8055** | Authentication — all external traffic |
| Main Brain | `jarvis-main-brain` | **8050** | Primary inference and DAO routing |

### Governance-Adjacent Services

| Service | Container | Host Port | Role |
|---|---|---|---|
| `nbb_pituitary_gland` | `msjarvis-rebuild-nbb_pituitary_gland-1` | **8108** | Systemic regulator — above DAO layer |
| Fifth DGM | `jarvis-fifth-dgm` | **4002** | Evolution proposals — DAO hook target |
| BBB | `jarvis-blood-brain-barrier` | **8016** | AU-02 enforcement — DAO boundary |
| GBIM Query Router | `jarvis-gbim-query-router` | **7205** | SQL-only governance grounding |
| ChromaDB (primary) | `jarvis-chroma` | **8002** | Semantic substrate for DAO deliberations |
| `msjarvis` PostgreSQL | `msjarvis-db` | **5433** | GBIM belief graph |
| Local Resources DB | `jarvis-local-resources-db` | **5435** | Verified resource registry |
| Memory | `jarvis-memory` | **8056** | Authenticated memory — `JARVIS_API_KEY` required |

---

## 3.10 Open Items — April 22, 2026

| OI | Description | Status | Priority |
|---|---|---|---|
| OI-C3-AU02-V2 | AU-02 v2 semantic + GBIM identity cross-reference layers — full runtime wiring | 🔄 Post-rebuild sprint | High |
| OI-C3-DGM-HOOK | Fifth DGM `/governance_hooks` and `dao_approval_required` runtime endpoints | 🔄 Post-rebuild sprint | High |
| OI-C3-PORT | Ports 8080–8084 confirmed — Gate 30 CLOSED April 1, 2026; 8081/8083 internal | ✅ CLOSED | — |
| OI-C3-PERIMETER | Caddy/auth perimeter documented as governance component (§3.6) | ✅ CLOSED | — |
| OI-C3-PIT | `nbb_pituitary_gland` integration documented at DAO layer (§3.8) | ✅ CLOSED | — |
| OI-C3-SEMANTIC | Chroma reattachment — `local_resources` reseeded 55 counties, 101 items | ✅ CLOSED | — |
| OI-C3-CONTAINERS | Container baseline updated to 105–110; gate threshold ≥ 95 | ✅ CLOSED | — |
| OI-C3-8083 | Token service on 8088→8083 (not directly exposed on 8083 host port) clarified | ✅ CLOSED | — |

---

## 3.11 Production Status Summary — April 22, 2026

| Component | Status | Notes |
|---|---|---|
| Container count | ✅ **105–110** | Gate threshold ≥ 95 — passing |
| Cloudflare tunnel | ✅ Active | Running 1d 7h, reconnect at 22:56 recovered |
| `egeria.mountainshares.us` | ✅ HTTP 200 | Live |
| `chat.mountainshares.us` | ✅ HTTP 200 | Live |
| Caddy gateway (port 8085) | ✅ Token-enforced | Unauthenticated /chat → HTTP 401 |
| `jarvis-auth` (port 8055) | ✅ Healthy | 200 authenticated, 404 unauthenticated |
| `jarvis-main-brain` (port 8050) | ✅ Operational | DAO routing confirmed |
| MountainShares Coordinator (8080) | ✅ Live | Gate 30 CLOSED April 1, 2026 |
| DAO Governance API (8082) | ✅ Live | Gate 30 CLOSED April 1, 2026 |
| Community Stake Registry (8084) | ✅ Live | Gate 30 CLOSED April 1, 2026 |
| MS Token Service (8088→8083) | ✅ Live (internal) | Behind Caddy/auth perimeter |
| `nbb_pituitary_gland` (8108) | ✅ **mode: elevated** | warmth=0.9, 6/6 protocols confirmed |
| EEG delta/theta/beta | ✅ Active | Pulses: 253 / 127 / 25 |
| AU-02 | ✅ v1 active / v2 target | v2 wiring post-rebuild sprint |
| DGM governance hook | 🔄 Conceptual + logging | Runtime gate post-rebuild sprint |
| `jarvis-chroma` (8002) | ✅ 48+ collections | Semantic substrate reattached |
| `local_resources` | ✅ 101 items | All 55 WV counties seeded |
| `gbim_worldview_entities` | ✅ 5,416,521 | eq1 worldview — confirmed |
| `jarvis-memory` (8056) | ✅ Authenticated | 200 authenticated, 404 unauthenticated |
| `0.0.0.0` bindings | ✅ Zero | All services bound to `127.0.0.1` |

---

*Chapter 3 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Jarvis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: 2026-04-22 — preflight gate 29/29; containers 105–110; Gate 30 CLOSED
April 1, 2026; Caddy/auth perimeter confirmed; pituitary 6/6 protocols; EEG delta 253 /
theta 127 / beta 25; Cloudflare tunnel recovered; AU-02 v1 active, v2 target documented;
DGM governance hook architecture specified; semantic substrate reattached 55 counties.*
