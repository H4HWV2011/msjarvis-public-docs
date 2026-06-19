# MountainShares Funder Overview
*Harmony for Hope, Inc. – West Virginia Pilot*

**Version:** 2.1
**Date:** June 19, 2026
**Status:** Funder-Facing Overview — Structural Rewrite
**Scope:** West Virginia statewide — Phase 1 operational, Phase 2 and Phase 3 forward-looking
**Related documents:** [MountainShares Program Rules](MountainShares%20Program%20Rules(Draft).md), [Program Rules – Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md), [Phase 1 Specification](MountainShares%20Phase%201%3A%20Economic%20Safety%20Specification.md), [Phase 2 Specification](MountainShares%20Phase%202%3A%20Regional%20Growth%20Specification.md), [Phase 3 Specification](MountainShares%20Phase%203%3A%20Surplus%20Distribution%20Specification.md), [Complete System Overview](MountainShares%3A%20Complete%20System%20Overview%20and%20Benefits.md), [DAO Governance Charter](MountainShares%20DAO%20Governance%20Charter.md)

> **Entity Status Notice:** Kidd's Technical Services ("KTS") is not yet a registered West Virginia LLC and has no EIN. References to "KTS" in this document mean Carrie Ann Kidd personally, operating under that trade name. Formation of the WV LLC is the gating step before founder equity, ALLIS IP holding, and KTS-side capitalization instruments take legal effect. No part of the MountainShares community system creates a founder equity path through H4H or community EMS.

> **Server Location Notice:** The operational server cluster and Ms. Allis / ALLIS node for H4H and MountainShares Commons is located at **704 Main Street, Mount Hope, West Virginia 25880** (Fayette County Community Arts Center).

> **EMS Appreciation — Governing Rule:** Community EMS maintains stable baseline exchange value. Phase-based buying-power expansion rates are **inactive** unless and until the Treasury Reserve achieves the applicable solvency threshold (300% at Phase 2; 500% at Phase 3), all Treasury Reserve-funded transition and formation costs have been paid, and no reversion event has occurred. The system reverts automatically to prior-phase specifications if thresholds are not maintained. No resident holds a vested appreciation right prior to threshold clearance. Community EMS holders do not receive equity, ownership, or profit-participation rights in H4H or KTS. Securities-law treatment of EMS is under review by securities counsel; this document makes no representation as to whether EMS is or is not a security. Any appreciating founder-side instrument exists exclusively on the KTS side under separate, counsel-reviewed documentation.

> **Money-Services Notice:** The MountainShares DAO/DUNA — not H4H — is the licensee of record for money-services activities associated with MountainShares, including the West Virginia Money Transmitter License (WV MTL), the FinCEN MSB registration, the required surety bond, BSA/AML compliance program obligations, and the cash-out rails. H4H is the charitable program sponsor and legal operator of MountainShares but is not the money transmitter. All payment flows, fund custody, and regulatory money-services obligations run through the MountainShares DAO/DUNA as licensee. Users and counterparties should direct money-services inquiries to the DAO/DUNA compliance function.

---

## 1. Organizational Structure and Roles

### 1.1 The Three-Box Structure

MountainShares operates inside a three-box entity structure that is the legal and economic firewall keeping charitable, community, and founder interests properly separated. This structure is not cosmetic — it defines who holds what rights, who bears what obligations, and who receives what flows under which conditions.

| Entity | Legal Form | Role | Key Constraint |
|---|---|---|---|
| **Harmony for Hope, Inc. (H4H)** | 501(c)(3) nonprofit | Charitable anchor; program sponsor; legal operator | Cannot be a path for founder equity; must operate within IRS nonprofit rules; not the money transmitter |
| **MountainShares Commons / DUNA** | Decentralized Unincorporated Nonprofit Association | Community-owned ledger, governance, EMS/M$ system; money-services licensee of record (WV MTL, FinCEN MSB, surety bond, BSA/AML, cash-out rails) | Community EMS holders receive no equity, ownership, or profit-participation rights; securities-law treatment under review by securities counsel |
| **Kidd's Technical Services (KTS)** | To-be-formed WV LLC/PBC | Founder commercial engine; ALLIS IP holder | Not yet formed; no EIN; founder rights do not activate until formation and registration |

No mechanism in this structure creates a path by which founder value is realized through H4H or community EMS. Any such path found in operation is a Critical finding requiring immediate resolution.

### 1.2 Harmony for Hope, Inc.

Harmony for Hope, Inc. ("H4H") was established in 2011 and received 501(c)(3) status effective March 16, 2017. H4H is a 501(c)(3) nonprofit organization based in Mount Hope, West Virginia, and the program sponsor and legal operator of MountainShares and The Commons ecosystem for the West Virginia pilot. H4H is not the money transmitter for MountainShares; that role belongs to the MountainShares DAO/DUNA as licensee of record.

H4H is responsible for:

- **Program stewardship and compliance:** Owning and operating MountainShares as a charitable, community-benefit initiative. Ensuring compliance with Applicable Law, payment-provider terms, and nonprofit obligations, including IRS rules for 501(c)(3) organizations. Approving and updating Program Rules, Phase Specifications, and DAO governance frameworks through the Board of Directors.

- **Treasury and reserve management:** Acting as fiduciary steward of MountainShares treasury reserves. Overseeing fee revenue allocation across treasury reserves, organizational operations, infrastructure, and community connectivity programs. Ensuring that reserve-ratio safety rules and phase thresholds are implemented and respected in practice.

- **Program operations and partnerships:** Managing relationships with local merchants, nonprofits, and public entities participating in MountainShares and The Commons. Coordinating on-the-ground programs, events, and outreach connecting the digital system to real community needs across West Virginia. Serving as the primary point of contact for funders, regulators, and institutional partners.

- **Annual Regulatory Compliance Budget:** Filing an Annual Regulatory Compliance Budget with the DAO each year. Budget covers legal, regulatory, compliance, and KTS-related transition costs. Individual draws from the Treasury Reserve for approved budget items follow the governance process defined in Section 7A of the applicable Phase Specification.

H4H is not a bank, credit union, investment advisor, or money transmitter. It operates MountainShares as a community rewards and prepaid-value program within a closed loop, under nonprofit governance and legal constraints. Any employee benefits, tax treatment, or related claims associated with MountainShares participation are under benefits-counsel review; no MountainShares-specific Private Letter Ruling (PLR) has been obtained.

### 1.3 Kidd's Technical Services (KTS)

Kidd's Technical Services ("KTS") is the technical firm that has designed and implemented the core infrastructure for MountainShares and Ms. Allis. KTS is currently not yet a registered West Virginia LLC and has no EIN. All present obligations and rights held under the KTS name belong to Carrie Ann Kidd personally until the LLC is formed.

KTS has:

- Designed and built the **Ms. Allis Geospatial Intelligence Platform**, including a microservices architecture orchestrating 80+ services, the Geographic Belief Information Model (GBIM) for spatially aware knowledge, GeoDB and PostGIS schemas, ChromaDB-based vector search, and the LLM orchestration layer and API gateway
- Implemented the **MountainShares mutual-credit and rewards back end**, including EMS recognition and vaulting logic, PMS handling and fee flows, Phase Safety Specifications with reserve-ratio bands and hard triggers, and DAO and governance scaffolding integrated with Ms. Allis
- Contributed **6,067.5 hours** of senior technical work between March 23, 2025 and May 14, 2026, valued at $150/hour for a documented capital contribution of **$910,125**, as detailed in the Founder's Technical Investment Statement

IP structure:
- The MountainShares mutual-credit system and commons governance configurations are developed for use by H4H as part of its charitable mission
- The Ms. Allis / ALLIS Geospatial Intelligence Platform remains proprietary to KTS and is made available to H4H under a **non-exclusive, royalty-free license** for community-benefit deployments at 704 Main Street, Mount Hope, WV 25880

This is a founder's capital contribution into a commons infrastructure, not a venture-capital equity position or profit-extraction arrangement. Founder-side rights are documented separately from this document, require KTS LLC formation before activation, and are entirely outside H4H charitable assets and community EMS.

### 1.4 MountainShares DAO/DUNA and Ms. Allis

MountainShares includes a DAO-style governance layer organized as a Decentralized Unincorporated Nonprofit Association (DUNA) and a transparent AI assistant, Ms. Allis, both operating under H4H's legal framework.

**MountainShares Commons / DUNA:**
- Is the **licensee of record** for money-services activities: WV Money Transmitter License, FinCEN MSB registration, required surety bond, BSA/AML compliance program, and cash-out rails
- Provides community governance over adjustable parameters: EMS→M$ base rates, per-user caps, promo pool sizes, phase transition advisory votes, and certain program thresholds
- Operates on a "one UEI = one vote" principle once minimum participation criteria are met, with super-majority and super-super-majority thresholds for structural or high-impact changes
- Is explicitly constrained: cannot override hard triggers, reserve-ratio safety bands, or legal/compliance requirements. Hard triggers are automatic and non-overridable by any vote at any threshold.

**Ms. Allis (AI tooling layer):**
- Acts as a "glass-box" AI advisor and operations assistant: monitoring reserve ratios and phase thresholds; calculating EMS recognition and vaulting status; suggesting parameter adjustments within allowed bands; flagging anomalies, abuse patterns, or safety issues for human review
- Operates at 704 Main Street, Mount Hope, WV 25880
- Has no independent legal status, cannot own assets, and cannot overrule H4H, the DAO, or applicable law

H4H remains the final authority for legal, fiduciary, and mission-aligned decisions, while the DAO/DUNA and Ms. Allis provide participatory and analytical capabilities inside that framework.

---

## 2. Program Model and Fee Structure

MountainShares operates as a **closed-loop rewards and prepaid-value system** with a two-layer design:

- **Purchased MountainShares (PMS / M$):** Value that users load with USD via approved payment channels, immediately spendable inside the system subject to Program Rules
- **Earned MountainShares (EMS):** Credits granted for documented community contributions, recorded first in an unlimited recognition ledger, then partially converted into spendable M$ under strict caps and reserve-linked rules

### 2.1 Fee Overview

All fee parameters are governed by FA-001 (Fee Amendment No. 1, effective June 2026) and the Program Rules – Parameter Tables. The governing values are:

| Fee Type | Current Rate | Primary Purpose |
|---|---|---|
| Load fee | 2.85% of fiat load | Operations, treasury, platform, community |
| Internal transfer fee | 0.25% | Treasury Reserve (100%) |
| Merchant fee | 1.80% | Treasury building through commerce |
| ATM / refund fee | $1.25 flat per transaction | Treasury Reserve |
| Supplemental treasury assessment | +0.55% of gross transaction volume | Treasury Reserve (supplemental, assessed on volume not fee revenue) |

### 2.2 Fee Revenue Allocation

All collected fee revenue is allocated per the following fixed split:

| Bucket | Allocation | Recipient / Purpose |
|---|---|---|
| 1 | 30% | Harmony for Hope, Inc. (H4H Operations) — nonprofit administration, staffing, compliance, legal, program delivery |
| 2 | 30% | Treasury Reserve — grows backing reserve; supports phase transition thresholds and liquidity |
| 3 | 15% | Platform Development — ongoing development of The Commons app, Ms. Allis infrastructure, technical systems |
| 4 | 15% | Community Connectivity – Operations — public-good connectivity programs (always available, never paywalled) |
| 5 | 10% | Community Connectivity – Infrastructure — public-good connectivity infrastructure (always available, never paywalled) |
| — | +0.55% | Treasury Reserve (Supplemental) — assessed separately on gross transaction volume |

> **Community Connectivity Note:** Buckets 4 and 5 together represent 25% of fee revenue and are dedicated to public-good community connectivity. These programs and the infrastructure supporting them are permanently available to all community members and are never paywalled. Education, mutual aid, and cultural preservation activities remain as EMS-earning activities for participants and as eligible programming categories, but are not separately enumerated as fee-revenue buckets.

Governance floors that cannot be reduced by ordinary DAO vote:
- Minimum Treasury Reserve allocation: 20%
- Minimum H4H Operations allocation: 20%

Any reduction in either floor requires a 66% super-majority DAO vote, Board of Directors ratification, and minimum 30 days notice to users.

### 2.3 How Loads Work (User Experience)

From the user's perspective: "Load $100" always results in a **100 M$ balance** inside the app. Load fee and any payment processor fee are visible costs added on top of the chosen load amount; they are not silently deducted from the user's intended value.

### 2.4 Why This Fee Structure Matters to Funders

Every transaction type contributes to both operations and reserve growth:
- Load fees fund operations and build reserves simultaneously
- Transfer fees flow 100% to the Treasury Reserve
- Merchant fees are the primary treasury-building mechanism as commerce scales
- The +0.55% supplemental assessment creates continuous compounding reserve growth proportional to volume
- Community Connectivity buckets (25% combined) ensure permanent, publicly accessible programming without cost barriers

As MountainShares activity increases, the treasury grows. This compounding mechanism is central to the system's long-term sustainability and the path to Phase 2 and Phase 3 threshold clearance without requiring continuous external grant injections.

---

## 3. EMS, PMS, Reserve Architecture, and Phases

### 3.1 The Two Reserve Metrics

MountainShares monitors two distinct reserve ratios daily. Both are calculated and published by Ms. Allis. Both have automatic enforcement by the Phase Management Controller.

**Operational Reserve Ratio** — governs day-to-day transaction safety, per-user caps, and commerce features:
