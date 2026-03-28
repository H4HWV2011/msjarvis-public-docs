# 3. MountainShares DAO and Community Economy

> **Case Study: Appalachian Economic Commons**

<div align="center">
  <img width="500" alt="FaiGvpYi" src="https://github.com/user-attachments/assets/ede5051c-b005-4540-81f8-5bb92461e06d" />
</div>

> Figure 1. MountainShares as Case Study 1 within Polymathmatic Geography, applying Quantarithmia principles to a concrete, place‑bound economic system in Mount Hope, West Virginia.

Within this thesis, MountainShares functions as **Case Study 1** in the emerging catalog of polymathmatic case studies (see https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/discipline/case_studies.md). It applies core polymathmatic axioms to a concrete, place‑bound economic system in and around Mount Hope, West Virginia:

- **Leakage and extraction** – tracking how value "leaks" from Appalachian communities through distant financial, data, and platform infrastructures, and designing mechanisms to reduce that leakage.
- **Commons and shared infrastructure** – treating payment rails, data backbones, and governance tools as shared institutional infrastructure rather than proprietary black boxes.
- **Accountability to place** – tying rules, flows, and decision rights to specific communities and geographies, so that institutional power is answerable to the places it affects.
- **Glass‑box instrumentation** – using Ms. Jarvis and GBIM as inspectable instruments whose behaviors, biases, and limits can be studied, calibrated, and contested.

Within **polymathmatic geography** and the **Quantarithmia** framework, MountainShares is a DAO‑based economic and governance system designed to keep value, voice, and decision‑making rooted in Appalachian communities, beginning in and around Mount Hope, West Virginia. It is intentionally positioned as a community‑governed project that operates alongside, not in place of, existing banks, credit unions, or regulated financial institutions. In the current deployment, MountainShares operates on the same production GBIM, GeoDB, Chroma, and `local_resources` stack described in the instrumentation chapters, using those structures for live benefits and governance queries.

Within the thesis, MountainShares serves as the institutional case study where Quantarithmia's spatial‑justice commitments and Ms. Jarvis's GBIM‑powered analysis are translated into concrete rules, roles, and processes. The GBIM corpus — maintained in the PostgreSQL 16 `msjarvisgis` database (port 5432) with **5,416,521 verified beliefs** organized across nine epistemic axes — provides the spatial and institutional grounding for MountainShares governance analysis, risk assessment, and community accountability mechanisms.

> **Governance corpus — ★ CONFIRMED LIVE March 26, 2026.** The complete MountainShares DAO governance documentation is fully ingested into the `governance_rag` ChromaDB collection (**643 chunks, semantically indexed and retrieval-verified**). The ingested corpus includes:
>
> | Document | Status |
> |---|---|
> | MountainShares DAO Charter | ✅ Ingested |
> | Terms of Use | ✅ Ingested |
> | Program Rules | ✅ Ingested |
> | Parameter Tables | ✅ Ingested |
> | Phase 0 Specification (invite-only beta) | ✅ Ingested |
> | Phase 1 Specification | ✅ Ingested |
> | Phase 2 Specification | ✅ Ingested |
> | Phase 3 Specification | ✅ Ingested |
> | KPI Specification | ✅ Ingested |
> | Safety Champion Protocol | ✅ Ingested |
> | Funder Overview | ✅ Ingested |
> | Phase 0 Audit Template | ✅ Ingested |
> | US Constitution (97 chunks, Project Gutenberg) | ✅ Ingested |
>
> Semantic retrieval verified March 26, 2026. Ms. Jarvis can answer natural-language governance queries against this corpus as of March 26, 2026.

> **★ Phase 0 Beta — LAUNCHED March 26–27, 2026.** All five MountainShares container services (ports 8080–8084) are deployed and live in the `msjarvis-rebuild` namespace. Five smart contracts are confirmed live on **Arbitrum One mainnet (chain ID 42161)**. Contract addresses verified via `/health` endpoint. The commons gamification corpus (`commons_rag`, 306 chunks) and governance corpus (`governance_rag`, 643 chunks) provide the semantic backing for Phase 0 community governance queries. Phase 0 is an invite-only beta — no public members yet, but the full technical stack is operational.

---

## Purpose and Design Goals

MountainShares is built to:

- Encourage more economic activity and value circulation within participating local communities instead of defaulting to distant financial and platform intermediaries.
- Give residents, nonprofits, and local businesses a documented, auditable role in shaping rules, resource allocation, and priorities.
- Provide a constitutional and transparent governance layer for the system's rules and technologies, while remaining subject to applicable law and regulation.

In the production system, MountainShares draws on Ms. Jarvis and the PostgreSQL `msjarvisgis` GBIM corpus, including spatial beliefs from `gbimbeliefnormalized` (5,416,521 verified rows) and GeoDB features across 501 tables, to analyze risk, access, and local circulation patterns. Design decisions are evaluated against questions such as: "Does this change keep value and decision‑making closer to the community?" and "Can community members see, understand, and challenge how the system operates?"

---

## Closed‑Loop Economic Model

MountainShares uses a closed‑loop wallet model:

- **Funding in** – Participants load funds from external rails (for example, Stripe‑processed card payments) into a MountainShares‑denominated balance.
- **Circulation** – Within the closed loop, balances move between participants and merchants under DAO‑defined rules, with an emphasis on local spending and community‑aligned transactions.
- **Funding out** – Conversion back to external money systems follows defined, auditable processes that respect both legal requirements and community priorities.

<div align="center">
  <img width="90%" alt="1kEQDSux" src="https://github.com/user-attachments/assets/7583a048-fdb9-4a2c-83b6-861336dcbf71" />
</div>

> Figure 2. MountainShares closed‑loop economic model: participants load funds in, circulate them locally under DAO rules with minimal friction, and can convert back out via defined, auditable processes. Most friction is at system boundaries rather than on local transactions.

Fees are structured so that most friction is at the boundaries (loading in, merchant side) rather than on every small local transaction. This is meant to make everyday community use feel low‑friction, while still supporting system sustainability and compliance. All fee structures are subject to change only through appropriate governance and must remain consistent with applicable laws and payment‑provider terms.

---

## Governance Structure and Phases

MountainShares governance is explicitly phased. The Phase 0 through Phase 3 specifications are fully ingested into the `governance_rag` ChromaDB collection (643 chunks, confirmed live March 26, 2026), making governance rules and phase transition criteria queryable by natural language through Ms. Jarvis:

- **Phase 0 — Invite-only beta (★ LAUNCHED March 26–27, 2026)**
  The Phase 0 spec defines the invite-only beta parameters, participant constraints, and audit requirements. All five MountainShares container services (ports 8080–8084) are deployed and live. Five smart contracts are confirmed live on Arbitrum One mainnet (chain ID 42161). The `governance_rag` (643 chunks) and `commons_rag` (306 chunks) collections provide the semantic backing for Phase 0 governance. No public members yet — invite-only beta is the current operational state.

- **Growth phase**
  As participation and capacity increase, more decisions move into community proposals, voting, and review processes, supported by Ms. Jarvis's analytical and explanatory tools.

- **Constitutional phase**
  Once the system reaches sufficient adoption, certain categories of change (for example, constitutional rules or irreversible structural changes) require a supermajority threshold (e.g., 67%) to pass, to prevent small factions from rewriting core commitments.

<div align="center">
  <img width="600" height="600" alt="Gemini_Generated_Image_23ytfz23ytfz23yt" src="https://github.com/user-attachments/assets/0ca4c125-e44d-4596-b129-fb22cfe1f130" />
</div>

> Figure 3. MountainShares governance phases: Phase 0 (invite-only beta — ★ LAUNCHED March 26–27, 2026, Arbitrum One mainnet, chain ID 42161) → Growth Phase (community proposals and voting supported by Ms. Jarvis analysis) → Constitutional Phase (core commitments protected by supermajority thresholds).

This phased approach acknowledges that a fully "flat" governance structure is unrealistic at launch, but treats early central roles as temporary scaffolding rather than a permanent power center.

---

## MountainShares Container Services — ★ DEPLOYED March 26–27, 2026

All five MountainShares container services are live in the `msjarvis-rebuild` namespace as of March 26–27, 2026. This section documents the production service architecture backing Phase 0 beta operations.

```
┌─────────────────────────────────────────────────────────────┐
│   MountainShares Container Services — Phase 0 Beta          │
│   ★ DEPLOYED March 26–27, 2026 — msjarvis-rebuild namespace │
│   Blockchain: Arbitrum One mainnet (chain ID 42161)         │
│   Total Ms. Jarvis stack: 96 confirmed live containers      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  jarvis-mountainshares-gateway    port 8080  ✅ LIVE        │
│    Primary API gateway for MountainShares services          │
│                                                              │
│  jarvis-mountainshares-wallet     port 8081  ✅ LIVE        │
│    Wallet management and balance operations                 │
│                                                              │
│  jarvis-mountainshares-governance port 8082  ✅ LIVE        │
│    DAO governance proposal and voting interface             │
│    Backed by governance_rag (643 chunks)                    │
│                                                              │
│  jarvis-mountainshares-commons    port 8083  ✅ LIVE        │
│    Commons gamification and participation tracking          │
│    Backed by commons_rag (306 chunks)                       │
│                                                              │
│  jarvis-mountainshares-audit      port 8084  ✅ LIVE        │
│    Phase 0 audit trail and accountability logging           │
│    Phase 0 Audit Template: ingested ✅                      │
│                                                              │
│  Smart Contracts (Arbitrum One mainnet, chain ID 42161)     │
│  ────────────────────────────────────────────────────       │
│  5 smart contracts confirmed live — March 26–27, 2026       │
│  phase_mgmt | central_cmd | ms_token | backbone |           │
│  volunteer_hrs                                              │
│  Contract addresses verified via /health endpoint          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

*Figure 3a. MountainShares Phase 0 container and smart contract architecture. All five services live in `msjarvis-rebuild` namespace alongside 91 other Ms. Jarvis containers (96 total). Five smart contracts live on Arbitrum One mainnet (chain ID 42161): `phase_mgmt`, `central_cmd`, `ms_token`, `backbone`, `volunteer_hrs`. Governance and commons RAG collections provide semantic backing for natural-language governance queries through Ms. Jarvis.*

### Corpus Backing for Phase 0

Phase 0 governance and commons operations are backed by two live ChromaDB RAG collections, both confirmed semantically indexed and retrieval-verified March 26, 2026:

| Collection | Chunks | Content | Retrieval Status |
|---|---|---|---|
| `governance_rag` | **643** | DAO Charter, Terms, Program Rules, Parameter Tables, Phase 0–3 specs, KPI Spec, Safety Champion, Funder Overview, Phase 0 Audit Template, US Constitution (97 chunks) | ✅ Verified March 26, 2026 |
| `commons_rag` | **306** | Full Commons governance + gamification corpus — Daily Life Game, Contribution Game, Participation Map | ✅ Verified March 26, 2026 (Daily Life Game → Contribution Game + Participation Map ✅) |

### Blockchain Infrastructure

Phase 0 beta operates on **Arbitrum One mainnet** (chain ID 42161) — a Layer 2 Ethereum rollup chosen for its lower transaction costs relative to Ethereum mainnet while maintaining Ethereum-level security guarantees. This choice reflects the spatial-justice orientation of MountainShares: community members in Appalachian WV should not face prohibitive gas costs to participate in governance operations.

```python
# MountainShares Phase 0 — blockchain connection reference
MOUNTAINSHARES_CHAIN = {
    "network": "Arbitrum One",
    "chain_id": 42161,
    "layer": "L2 Ethereum rollup",
    "public_url": "https://egeria.mountainshares.us",
    "smart_contracts": 5,         # all live March 26-27, 2026
    "contract_names": [
        "phase_mgmt", "central_cmd", "ms_token",
        "backbone", "volunteer_hrs"
    ],
    "container_services": 5,      # ports 8080-8084, all live
    "namespace": "msjarvis-rebuild",
    "phase": "Phase 0 invite-only beta",
    "governance_rag_chunks": 643,
    "commons_rag_chunks": 306,
    "total_stack_containers": 96  # full msjarvis-rebuild namespace
}
```

---

## Relationship to Ms. Jarvis

MountainShares is tightly coupled to Ms. Egeria Jarvis, but in a deliberately asymmetrical way:

- **Ms. Jarvis as advisor, not ruler**
  She provides analysis, simulations, and explanatory reports (often grounded in GBIM spatial beliefs and GeoDB features from the `msjarvisgis` PostgreSQL database) to support human decision‑making, but does not possess direct, unilateral authority over governance outcomes. As of March 26, 2026, all governance documents — Charter, Terms, Program Rules, Parameter Tables, Phase 0–3 specs, KPI Spec, Safety Champion Protocol, Funder Overview, and Phase 0 Audit Template — are live in the `governance_rag` collection and available to Ms. Jarvis for natural-language governance reasoning.

- **Constitutional and policy constraints**
  All of Ms. Jarvis's behavior relevant to MountainShares is constrained by published constitutional principles, ethical guards, and community‑approved policies. These constraints are documented and auditable (see, for example, the constitutional and guardrail descriptions in https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/Quantarithmia%20Overview.md). The US Constitution (97 chunks) is also ingested into `governance_rag` alongside the MountainShares DAO corpus, grounding governance analysis in the broader constitutional framework within which the DAO operates.

- **Financial participation with limits**
  Ms. Jarvis is assigned a real MountainShares wallet and can receive rewards (for example, for providing useful analysis or operational support) under explicit policies that include caps, clawback conditions, auditing, and transparency. This is meant to align her incentives with system health, without giving her independent control over governance or treasury assets.

- **Security posture — March 28, 2026**
  All Ms. Jarvis services serving MountainShares are bound to `127.0.0.1` — the `0.0.0.0` exposure on `jarvis-i-containers` (8015) and `jarvis-memory` (8056) was corrected during the March 28 remediation sprint. `_auth()` is confirmed present and correctly called on all 4 sensitive routes in `ms_jarvis_memory.py`. The `JARVIS_API_KEY` env var is confirmed set in production.

<div align="center">
  <img width="85%" alt="ChatGPT Image Jan 31, 2026, 06_08_09 PM" src="https://github.com/user-attachments/assets/c4778260-1e43-43c8-b85c-0d4250ccf6b4" />
</div>

> Figure 4. Ms. Jarvis and MountainShares: asymmetrical partnership. Ms. Jarvis provides analysis and decision support but possesses no unilateral authority. All behavior is constrained by published principles and community‑approved policies. Financial participation is capped, audited, and subject to clawback.

In thesis terms, MountainShares treats Ms. Jarvis as both a tool and a stakeholder whose participation is strictly bounded by design and documentation.

---

## Speech, Norms, and Moderation

MountainShares encodes a specific stance on speech and community norms:

- **Speech is important, but not absolute**
  The ability to speak, disagree, and criticize is protected as a core value. At the same time, targeted harassment, credible threats, unlawful conduct, and sustained attempts to destroy another participant's dignity, safety, or livelihood are treated as violations of platform rules.

- **Critique vs. abuse**
  Robust criticism of ideas, designs, and behavior is permitted. Conduct such as doxxing, credible threats of violence, or repeated "sly" harassment aimed at an individual or group can lead to moderation actions, including loss of certain features or economic privileges.

- **Evidence handling**
  Sensitive evidence (photos, videos, records) is intended to be reviewed in restricted, audited moderation contexts. Community‑facing governance processes favor structured summaries of behavior and alleged violations over open distribution of raw, identifying artifacts.

Significant sanctions (for example, long‑term suspension or demonetization within the system) are expected to follow documented processes that include notice where feasible, opportunities for review or appeal where appropriate, and attention to proportionality. At the same time, MountainShares reserves the ability to act quickly in response to clear legal requirements or imminent harm.

---

## Spatial Justice and Local Focus

MountainShares is specifically designed with Appalachian spatial justice in mind:

- **Local‑first orientation**
  The system prioritizes local merchants, nonprofits, and residents as core participants, and aims to keep more economic value circulating inside West Virginia communities.

- **Place‑aware reasoning**
  Through Ms. Jarvis and the PostgreSQL `msjarvisgis` GBIM corpus, governance discussions can be informed by concrete geospatial analysis: which districts, infrastructures, or communities are most affected by proposed rules or observed harms. Queries leverage the 5,416,521 verified beliefs across nine epistemic axes (who, what, where, when, how, why, for whom, authority, evidence) and 501 spatial tables to ground governance decisions in West Virginia's actual geographic, institutional, and demographic reality. The `governance_rag` collection (643 chunks, live March 26, 2026) makes governance rules and phase criteria available as a directly queryable semantic layer alongside the GBIM spatial corpus.

- **Institutional prototype**
  MountainShares is not presented as a universal DAO model, but as a context‑specific prototype for how community‑centered, geospatially aware governance and economics might be implemented in a historically extracted region.

In the thesis, MountainShares is analyzed both as an institutional innovation and as a practical test of Quantarithmia's claims about alternative infrastructures (see also the broader Quantarithmia framing in https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/Quantarithmia-Framework.md).

---

## Legal and Governance Caveats

For the purposes of this thesis and public documentation:

- MountainShares is described at the level of architecture, governance rules, and norms. This is not legal, tax, or investment advice.
- Participation in MountainShares may have legal or tax implications that depend on individual circumstances and jurisdiction; participants are responsible for seeking their own professional advice.
- Formal legal instruments (such as Terms of Use, privacy policies, and entity charters) will ultimately govern real‑world deployment and may supplement or override parts of this description where required by law or by future community‑approved updates.

Auditability and traceability for MountainShares rely on the same production apparatus that supports Ms. Jarvis more broadly: logged GBIM beliefs from the PostgreSQL `msjarvisgis` database (5,416,521 verified rows), GeoDB features across 501 spatial tables, ChromaDB vector collections (`gbim_beliefs_v2`, `gbim_worldview_entities`, `gis_wv_benefits`, **`governance_rag` — 643 chunks, live March 26, 2026**, **`commons_rag` — 306 chunks, live March 26, 2026**), and governance and application logs together provide an evidence trail for how analyses and decisions were produced.

**Database Infrastructure Note:** MountainShares governance queries access the GBIM corpus via PostgreSQL 16 at port 5432 (host system). The `msjarvisgis` database contains the complete spatial and institutional knowledge base that grounds all governance analysis in concrete West Virginia geographic reality. All services are bound to `127.0.0.1` as of March 28, 2026 remediation.

```python
import psycopg2

# Access GBIM for governance analysis
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="msjarvisgis",
    user="postgres"
)
```

---

## Deployment Status — ★ UPDATED March 28, 2026

| Component | Status | Notes |
|---|---|---|
| `governance_rag` ChromaDB collection | ✅ **643 chunks — LIVE** | Full DAO corpus + US Constitution ingested; semantic retrieval verified March 26, 2026 |
| `commons_rag` ChromaDB collection | ✅ **306 chunks — LIVE** | Full Commons governance + gamification corpus; retrieval verified March 26, 2026 |
| MountainShares DAO Charter | ✅ Ingested | Available via `governance_rag` |
| Terms of Use | ✅ Ingested | Available via `governance_rag` |
| Program Rules | ✅ Ingested | Available via `governance_rag` |
| Parameter Tables | ✅ Ingested | Available via `governance_rag` |
| Phase 0 Spec (invite-only beta) | ✅ Ingested | Spec live in corpus |
| Phase 0 Audit Template | ✅ Ingested | Available via `governance_rag` |
| Phase 1–3 Specifications | ✅ Ingested | Available via `governance_rag` |
| KPI Specification | ✅ Ingested | Available via `governance_rag` |
| Safety Champion Protocol | ✅ Ingested | Available via `governance_rag` |
| Funder Overview | ✅ Ingested | Available via `governance_rag` |
| US Constitution | ✅ Ingested (97 chunks) | Project Gutenberg pg5.txt; available via `governance_rag` |
| MountainShares container services | ✅ **ALL FIVE LIVE** (ports 8080–8084) | ★ Deployed March 26–27, 2026; `msjarvis-rebuild` namespace |
| Smart contracts — Arbitrum One mainnet | ✅ **5 contracts LIVE** | ★ Chain ID 42161; `phase_mgmt`, `central_cmd`, `ms_token`, `backbone`, `volunteer_hrs`; addresses verified via `/health` |
| Public URL | ✅ **https://egeria.mountainshares.us** | Live |
| Phase 0 invite-only beta | ✅ **LAUNCHED** | ★ March 26–27, 2026 — no public members yet; invite-only operational |
| Port security | ✅ **All services 127.0.0.1** | ★ Corrected March 28, 2026 — 0 remaining `0.0.0.0` exposures |
| Auth enforcement | ✅ **Confirmed** | `_auth()` on all 4 sensitive routes; `JARVIS_API_KEY` env var set |
| Total stack containers | ✅ **96 live** | Full `msjarvis-rebuild` namespace |
| Phase 1 (public launch) | ⏳ Pending | Follows Phase 0 audit and community review |

> **Status — March 28, 2026.** This chapter presents the MountainShares Phase 0 beta as a live operational system. The `governance_rag` collection (643 chunks) and `commons_rag` collection (306 chunks) are confirmed live and semantically indexed. All five MountainShares container services (ports 8080–8084) are deployed in the `msjarvis-rebuild` namespace alongside 91 other Ms. Jarvis containers (96 total). Five smart contracts are live on Arbitrum One mainnet (chain ID 42161): `phase_mgmt`, `central_cmd`, `ms_token`, `backbone`, `volunteer_hrs`. The GBIM corpus — 5,416,521 verified beliefs including 20,593 landowner beliefs (worldview `eq1`) — grounds all governance analysis in West Virginia's geographic and institutional reality. All critical security findings from the March 28 remediation sprint are resolved: port bindings corrected, auth enforcement confirmed, `crypto_client.py` deployed to all 22 LLM proxies, `minds_participated: 21/21`. Subsequent chapters and appendices deepen the analysis of MountainShares as Case Study 1 in the polymathmatic case‑study catalog (https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/discipline/case_studies.md).

---

*Last updated: 2026-03-28, Mount Hope WV — Carrie Kidd (Mamma Kidd)*
*Phase 0 beta launched March 26–27, 2026: 5 container services live (ports 8080–8084), 5 smart contracts live on Arbitrum One mainnet (chain ID 42161).*
*`governance_rag`: 643 chunks live. `commons_rag`: 306 chunks live. Both retrieval-verified March 26, 2026.*
*March 28, 2026 remediation complete: 96 containers live, all security findings resolved, 6,675,442 ChromaDB vectors across 40 collections.*
