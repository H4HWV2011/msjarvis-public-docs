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

Within the thesis, MountainShares serves as the institutional case study where Quantarithmia's spatial‑justice commitments and Ms. Jarvis's GBIM‑powered analysis are translated into concrete rules, roles, and processes. The GBIM corpus—maintained in the PostgreSQL 16 `msjarvisgis` database (port 5432) with 5,416,522 verified beliefs organized across nine epistemic axes—provides the spatial and institutional grounding for MountainShares governance analysis, risk assessment, and community accountability mechanisms.

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
> Semantic retrieval verified March 26, 2026. The `governance_rag` collection was previously listed as missing or empty in earlier chapter drafts — that status is now closed. Ms. Jarvis can answer natural-language governance queries against this corpus as of March 26, 2026.

---

## Purpose and Design Goals

MountainShares is built to:

- Encourage more economic activity and value circulation within participating local communities instead of defaulting to distant financial and platform intermediaries.
- Give residents, nonprofits, and local businesses a documented, auditable role in shaping rules, resource allocation, and priorities.
- Provide a constitutional and transparent governance layer for the system's rules and technologies, while remaining subject to applicable law and regulation.

In the production system, MountainShares draws on Ms. Jarvis and the PostgreSQL `msjarvisgis` GBIM corpus, including spatial beliefs from `gbimbeliefnormalized` (5,416,522 verified rows) and GeoDB features across 501 tables, to analyze risk, access, and local circulation patterns. Design decisions are evaluated against questions such as: "Does this change keep value and decision‑making closer to the community?" and "Can community members see, understand, and challenge how the system operates?"

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

- **Phase 0 — Invite-only beta (specification and audit template ingested ✅)**
  The Phase 0 spec defines the invite-only beta parameters, participant constraints, and audit requirements. The Phase 0 audit template is ingested and available for governance queries. Container services for MountainShares (ports 8080–8084) are not yet deployed — the corpus is ready; the beta has not yet launched.

- **Growth phase**
  As participation and capacity increase, more decisions move into community proposals, voting, and review processes, supported by Ms. Jarvis's analytical and explanatory tools.

- **Constitutional phase**
  Once the system reaches sufficient adoption, certain categories of change (for example, constitutional rules or irreversible structural changes) require a supermajority threshold (e.g., 67%) to pass, to prevent small factions from rewriting core commitments.

<div align="center">
  <img width="600" height="600" alt="Gemini_Generated_Image_23ytfz23ytfz23yt" src="https://github.com/user-attachments/assets/0ca4c125-e44d-4596-b129-fb22cfe1f130" />
</div>

> Figure 3. MountainShares governance phases: Phase 0 (invite-only beta — spec ingested, launch pending) → Growth Phase (community proposals and voting supported by Ms. Jarvis analysis) → Constitutional Phase (core commitments protected by supermajority thresholds).

This phased approach acknowledges that a fully "flat" governance structure is unrealistic at launch, but treats early central roles as temporary scaffolding rather than a permanent power center.

---

## Relationship to Ms. Jarvis

MountainShares is tightly coupled to Ms. Egeria Jarvis, but in a deliberately asymmetrical way:

- **Ms. Jarvis as advisor, not ruler**
  She provides analysis, simulations, and explanatory reports (often grounded in GBIM spatial beliefs and GeoDB features from the `msjarvisgis` PostgreSQL database) to support human decision‑making, but does not possess direct, unilateral authority over governance outcomes. As of March 26, 2026, all governance documents — Charter, Terms, Program Rules, Parameter Tables, Phase 0–3 specs, KPI Spec, Safety Champion Protocol, Funder Overview, and Phase 0 Audit Template — are live in the `governance_rag` collection and available to Ms. Jarvis for natural-language governance reasoning.

- **Constitutional and policy constraints**
  All of Ms. Jarvis's behavior relevant to MountainShares is constrained by published constitutional principles, ethical guards, and community‑approved policies. These constraints are documented and auditable (see, for example, the constitutional and guardrail descriptions in https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/Quantarithmia%20Overview.md). The US Constitution (97 chunks) is also ingested into `governance_rag` alongside the MountainShares DAO corpus, grounding governance analysis in the broader constitutional framework within which the DAO operates.

- **Financial participation with limits**
  Ms. Jarvis is assigned a real MountainShares wallet and can receive rewards (for example, for providing useful analysis or operational support) under explicit policies that include caps, clawback conditions, auditing, and transparency. This is meant to align her incentives with system health, without giving her independent control over governance or treasury assets.

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
  Through Ms. Jarvis and the PostgreSQL `msjarvisgis` GBIM corpus, governance discussions can be informed by concrete geospatial analysis: which districts, infrastructures, or communities are most affected by proposed rules or observed harms. Queries leverage the 5,416,522 verified beliefs across nine epistemic axes (who, what, where, when, how, why, for whom, authority, evidence) and 501 spatial tables to ground governance decisions in West Virginia's actual geographic, institutional, and demographic reality. The `governance_rag` collection (643 chunks, live March 26, 2026) makes governance rules and phase criteria available as a directly queryable semantic layer alongside the GBIM spatial corpus.

- **Institutional prototype**
  MountainShares is not presented as a universal DAO model, but as a context‑specific prototype for how community‑centered, geospatially aware governance and economics might be implemented in a historically extracted region.

In the thesis, MountainShares is analyzed both as an institutional innovation and as a practical test of Quantarithmia's claims about alternative infrastructures (see also the broader Quantarithmia framing in https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/Quantarithmia-Framework.md).

---

## Legal and Governance Caveats

For the purposes of this thesis and public documentation:

- MountainShares is described at the level of architecture, governance rules, and norms. This is not legal, tax, or investment advice.
- Participation in MountainShares may have legal or tax implications that depend on individual circumstances and jurisdiction; participants are responsible for seeking their own professional advice.
- Formal legal instruments (such as Terms of Use, privacy policies, and entity charters) will ultimately govern real‑world deployment and may supplement or override parts of this description where required by law or by future community‑approved updates.

Auditability and traceability for MountainShares rely on the same production apparatus that supports Ms. Jarvis more broadly: logged GBIM beliefs from the PostgreSQL `msjarvisgis` database (5,416,522 verified rows), GeoDB features across 501 spatial tables, ChromaDB vector collections (`gbim_beliefs_v2`, `gbim_worldview_entities`, `gis_wv_benefits`, and **`governance_rag` — 643 chunks, live March 26, 2026**), and governance and application logs together provide an evidence trail for how analyses and decisions were produced.

**Database Infrastructure Note:** MountainShares governance queries access the GBIM corpus via PostgreSQL 16 at port 5432 (host system). The `msjarvisgis` database contains the complete spatial and institutional knowledge base that grounds all governance analysis in concrete West Virginia geographic reality. Connection example:

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

## Deployment Status — March 26, 2026

| Component | Status | Notes |
|---|---|---|
| `governance_rag` ChromaDB collection | ✅ **643 chunks — LIVE** | Full DAO corpus + US Constitution ingested; semantic retrieval verified March 26, 2026 |
| MountainShares DAO Charter | ✅ Ingested | Available via `governance_rag` |
| Terms of Use | ✅ Ingested | Available via `governance_rag` |
| Program Rules | ✅ Ingested | Available via `governance_rag` |
| Parameter Tables | ✅ Ingested | Available via `governance_rag` |
| Phase 0 Spec (invite-only beta) | ✅ Ingested | Spec live in corpus; beta not yet launched |
| Phase 0 Audit Template | ✅ Ingested | Available via `governance_rag` |
| Phase 1–3 Specifications | ✅ Ingested | Available via `governance_rag` |
| KPI Specification | ✅ Ingested | Available via `governance_rag` |
| Safety Champion Protocol | ✅ Ingested | Available via `governance_rag` |
| Funder Overview | ✅ Ingested | Available via `governance_rag` |
| US Constitution | ✅ Ingested (97 chunks) | Project Gutenberg pg5.txt; available via `governance_rag` |
| MountainShares container services (ports 8080–8084) | ❌ **Not yet deployed** | Corpus ready; awaiting Phase 0 beta launch |
| Phase 0 invite-only beta (live members) | ⏳ **Pending** | No live members yet; launch timing TBD |
| `commons_rag` ChromaDB collection | ✅ **306 chunks — LIVE** | Full Commons governance + gamification corpus ingested; retrieval verified March 26, 2026 |

> **Status — March 26, 2026.** This chapter presents an operational governance overview built on the current Ms. Jarvis/GBIM stack (PostgreSQL 16, 5,416,522 verified beliefs, 91 GB corpus). The `governance_rag` collection (643 chunks) and `commons_rag` collection (306 chunks) are confirmed live and semantically indexed — the governance corpus is no longer missing or sparse. MountainShares container services and Phase 0 beta launch remain pending. Subsequent chapters and appendices deepen the analysis of MountainShares as a case study in spatial justice, institutional design, and AI‑supported community governance, and cross‑reference its role as Case Study 1 in the polymathmatic case‑study catalog (https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/discipline/case_studies.md).

---

*Last updated: 2026-03-26, Mount Hope WV — Carrie Kidd (Mamma Kidd)*
*`governance_rag` updated from missing → 643 chunks live; Phase 0 spec and audit template confirmed ingested March 26, 2026.*
