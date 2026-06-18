# MountainShares Funder Overview
*Harmony for Hope, Inc. – West Virginia Pilot*

**Version:** 2.0
**Date:** June 17, 2026
**Status:** Funder-Facing Overview — Structural Rewrite
**Scope:** West Virginia statewide — Phase 1 operational, Phase 2 and Phase 3 forward-looking
**Related documents:** [MountainShares Program Rules](MountainShares%20Program%20Rules(Draft).md), [Program Rules – Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md), [Phase 1 Specification](MountainShares%20Phase%201%3A%20Economic%20Safety%20Specification.md), [Phase 2 Specification](MountainShares%20Phase%202%3A%20Regional%20Growth%20Specification.md), [Phase 3 Specification](MountainShares%20Phase%203%3A%20Surplus%20Distribution%20Specification.md), [Complete System Overview](MountainShares%3A%20Complete%20System%20Overview%20and%20Benefits.md), [DAO Governance Charter](MountainShares%20DAO%20Governance%20Charter.md)

> **Entity Status Notice:** Kidd's Technical Services ("KTS") is not yet a registered West Virginia LLC and has no EIN. References to "KTS" in this document mean Carrie Ann Kidd personally, operating under that trade name. Formation of the WV LLC is the gating step before founder equity, ALLIS IP holding, and KTS-side capitalization instruments take legal effect. No part of the MountainShares community system creates a founder equity path through H4H or community EMS.

> **Server Location Notice:** The operational server cluster and Ms. Allis / ALLIS node for H4H and MountainShares Commons is located at **704 Main Street, Mount Hope, West Virginia 25880** (Fayette County Community Arts Center).

> **EMS Appreciation — Governing Rule:** Community EMS maintains stable baseline exchange value. Phase-based buying-power expansion rates are **inactive** unless and until the Treasury Reserve achieves the applicable solvency threshold (300% at Phase 2; 500% at Phase 3), all Treasury Reserve-funded transition and formation costs have been paid, and no reversion event has occurred. The system reverts automatically to prior-phase specifications if thresholds are not maintained. No resident holds a vested appreciation right prior to threshold clearance. Community EMS is non-appreciating in the securities-law sense at all times. Any appreciating founder-side instrument exists exclusively on the KTS side under separate, counsel-reviewed documentation.

---

## 1. Organizational Structure and Roles

### 1.1 The Three-Box Structure

MountainShares operates inside a three-box entity structure that is the legal and economic firewall keeping charitable, community, and founder interests properly separated. This structure is not cosmetic — it defines who holds what rights, who bears what obligations, and who receives what flows under which conditions.

| Entity | Legal Form | Role | Key Constraint |
|---|---|---|---|
| **Harmony for Hope, Inc. (H4H)** | 501(c)(3) nonprofit | Charitable anchor; program sponsor; legal operator | Cannot be a path for founder equity; must operate within IRS nonprofit rules |
| **MountainShares Commons / DUNA** | Decentralized community entity | Community-owned ledger, governance, and EMS/M$ system | Community EMS is non-appreciating; no surplus distributed before 500% treasury floor |
| **Kidd's Technical Services (KTS)** | To-be-formed WV LLC/PBC | Founder commercial engine; ALLIS IP holder | Not yet formed; no EIN; founder rights do not activate until formation and registration |

No mechanism in this structure creates a path by which founder value is realized through H4H or community EMS. Any such path found in operation is a Critical finding requiring immediate resolution.

### 1.2 Harmony for Hope, Inc.

Harmony for Hope, Inc. ("H4H") is a 501(c)(3) nonprofit organization based in Mount Hope, West Virginia, and the program sponsor and legal operator of MountainShares and The Commons ecosystem for the West Virginia pilot.

H4H is responsible for:

- **Program stewardship and compliance:** Owning and operating MountainShares as a charitable, community-benefit initiative. Ensuring compliance with Applicable Law, payment-provider terms, and nonprofit obligations, including IRS rules for 501(c)(3) organizations. Approving and updating Program Rules, Phase Specifications, and DAO governance frameworks through the Board of Directors.

- **Treasury and reserve management:** Acting as fiduciary steward of MountainShares treasury reserves. Overseeing fee revenue allocation across treasury reserves, organizational operations, infrastructure, and community programs. Ensuring that reserve-ratio safety rules and phase thresholds are implemented and respected in practice.

- **Program operations and partnerships:** Managing relationships with local merchants, nonprofits, and public entities participating in MountainShares and The Commons. Coordinating on-the-ground programs, events, and outreach connecting the digital system to real community needs across West Virginia. Serving as the primary point of contact for funders, regulators, and institutional partners.

- **Annual Regulatory Compliance Budget:** Filing an Annual Regulatory Compliance Budget with the DAO each year. Budget covers legal, regulatory, compliance, and KTS-related transition costs. Individual draws from the Treasury Reserve for approved budget items follow the governance process defined in Section 7A of the applicable Phase Specification.

H4H is not a bank, credit union, or investment advisor. It operates MountainShares as a community rewards and prepaid-value program within a closed loop, under nonprofit governance and legal constraints.

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

### 1.4 MountainShares DAO and Ms. Allis

MountainShares includes a DAO-style governance layer and a transparent AI assistant, Ms. Allis, both operating under H4H's legal framework.

**MountainShares Commons / DUNA:**
- Provides community governance over adjustable parameters: EMS→M$ base rates, per-user caps, promo pool sizes, phase transition advisory votes, and certain program thresholds
- Operates on a "one UEI = one vote" principle once minimum participation criteria are met, with super-majority and super-super-majority thresholds for structural or high-impact changes
- Is explicitly constrained: cannot override hard triggers, reserve-ratio safety bands, or legal/compliance requirements. Hard triggers are automatic and non-overridable by any vote at any threshold.

**Ms. Allis (AI tooling layer):**
- Acts as a "glass-box" AI advisor and operations assistant: monitoring reserve ratios and phase thresholds; calculating EMS recognition and vaulting status; suggesting parameter adjustments within allowed bands; flagging anomalies, abuse patterns, or safety issues for human review
- Operates at 704 Main Street, Mount Hope, WV 25880
- Has no independent legal status, cannot own assets, and cannot overrule H4H, the DAO, or applicable law

H4H remains the final authority for legal, fiduciary, and mission-aligned decisions, while the DAO and Ms. Allis provide participatory and analytical capabilities inside that framework.

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
| 4 | 15% | Community Programs — education, mutual aid, time-banking, cultural preservation, and structured programming |
| 5 | 10% | Community Projects — member-initiated or DAO-approved local projects within the West Virginia commons |
| — | +0.55% | Treasury Reserve (Supplemental) — assessed separately on gross transaction volume |

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

As MountainShares activity increases, the treasury grows. This compounding mechanism is central to the system's long-term sustainability and the path to Phase 2 and Phase 3 threshold clearance without requiring continuous external grant injections.

---

## 3. EMS, PMS, Reserve Architecture, and Phases

### 3.1 The Two Reserve Metrics

MountainShares monitors two distinct reserve ratios daily. Both are calculated and published by Ms. Allis. Both have automatic enforcement by the Phase Management Controller.

**Operational Reserve Ratio** — governs day-to-day transaction safety, per-user caps, and commerce features:

~~~
Operational Reserve Ratio = Treasury USDC Reserve / Total Outstanding Spendable PMS (M$)
~~~

**Treasury Reserve Solvency Ratio** — governs EMS buying-power expansion and is the primary phase gate:

~~~
Treasury Reserve Solvency Ratio = Treasury Reserve / (Total Outstanding EMS + Total Outstanding M$)
~~~

These two ratios answer different safety questions. The Operational Reserve Ratio asks: *Can the system safely handle current spendable volume?* The Treasury Reserve Solvency Ratio asks: *Is the treasury strong enough to support a higher recognition-conversion schedule without structural risk?*

### 3.2 Recognition vs. Spendable Layers

MountainShares draws a clear distinction between:
- An **unlimited recognition ledger** where all EMS are recorded (1 EMS hour per verified hour of community contribution, with UEI, geo, and timestamp metadata)
- A **capped spendable layer** where some EMS hours are converted into spendable M$ under base-rate and per-user cap rules, governed by reserve-ratio bands

This architecture lets the system recognize the full scope of community contribution — even when treasury conditions require tight caps on spendable conversions — and use the recognition ledger for governance, Phase 3 dividend eligibility (Participation Weight), and historical community record.

### 3.3 Vaulting and Unlocking

EMS credits flow through stages:
1. Participant performs verified community work
2. Work is logged into the EMS recognition ledger
3. Program rules determine how much EMS may be converted into spendable M$ in the current epoch
4. Conversion is subject to phase rules, reserve conditions, per-user caps, and benefits-sensitive protections
5. Unconverted EMS remains vaulted — visible on dashboards, auditable, but not circulating

No participant is ever automatically converted. Each participant controls their own conversion timing. This is a hard guarantee — the Phase Management Controller cannot force conversion.

### 3.4 Phase-Gated EMS Buying-Power Schedule

| Phase | EMS Buying-Power Rate | Treasury Reserve Solvency Gate | Reversion Trigger |
|---|---|---|---|
| **Phase 1 – Launch** | 1 EMS = $1.00 USD equivalent | Default | N/A |
| **Phase 2 – Regional Growth** | 1 EMS = $10.00 USD equivalent | ≥ 300% for 2+ consecutive quarters; all formation fees paid | Ratio drops below 300% → automatic reversion to Phase 1 |
| **Phase 3 – Surplus Distribution** | 1 EMS = **FVSR** in effect on Phase 3 activation date | ≥ 500% for 2+ consecutive quarters; all prior-phase transition costs paid | Ratio drops below 500% → reversion to Phase 2; below 300% → reversion to Phase 1 |

> **Federal Volunteer Service Rate (FVSR):** The IRS-published standard rate for valuing volunteer services, updated annually. The Phase 3 EMS buying-power rate is the FVSR in effect on the date the DAO formally activates Phase 3 — not the rate at document publication. The current rate (2026) is **$36.14**. If Phase 3 activates in a later year, the applicable rate is that year's published FVSR. Ms. Allis surfaces the current FVSR on the dashboard each calendar year.

All reversion events are automatic, non-overridable by governance, logged to the durable audit trail, and communicated in plain language to all participants within 24 hours.

### 3.5 Phase Transition Conditions (High-Level)

| Criterion | Phase 1 → Phase 2 | Phase 2 → Phase 3 |
|---|---|---|
| Treasury Reserve Solvency Ratio | ≥ 300% for 2+ quarters | ≥ 500% for 2+ quarters |
| Operational Reserve Ratio | ≥ 1.25 stable for 60+ days | ≥ 3.0 stable for 90+ days |
| Active UEIs | ≥ 500 across ≥ 3 counties | ≥ 10,000 across ≥ 10 counties |
| Monthly processed volume | To be defined | ≥ $2M USD statewide |
| Prior-phase transition fees paid | Yes — required before Phase 2 rate activates | Yes — required before Phase 3 FVSR rate activates |
| Regulatory standing | All WV and federal registrations current | All current; no unresolved deferred compliance draws |

---

## 4. Phase 3 Community Dividend — Funder Summary

The most distinctive long-horizon benefit of MountainShares is the Phase 3 community surplus distribution. Funders should understand it correctly to represent it accurately.

### 4.1 What It Is

The Phase 3 community dividend is a distribution of **real surplus above the permanent 500% treasury floor** after the floor has been maintained through a 7-year active accumulation period. It is:

- Not a speculative return
- Not a token yield product
- Not a founder extraction mechanism
- Not guaranteed — it activates only if and when all threshold conditions are satisfied and the treasury generates genuine surplus above the floor

It is a community distribution from genuine surplus, made to the people who actually built the commons.

### 4.2 How Eligibility Is Determined

Eligibility and distribution share are based entirely on **Participation Weight (PW)** — a score reflecting actual presence and community contribution over the 7-year accumulation window, not on financial stake:

~~~
Participation Weight (PW) = Verified Months Active × Activity Multiplier
~~~

| Tier | Verified Active Months | Multiplier |
|---|---|---|
| Minimum | 1–6 months | 1.0× |
| Regular | 7–24 months | 1.25× |
| Sustained | 25–60 months | 1.5× |
| Founding Deep | 61–84 months (≥ 5 years continuous) | 2.0× |

This design ensures the people who showed up consistently — especially those who contributed during early, harder phases — receive a proportionally larger share of the surplus they helped create.

### 4.3 Benefits-Sensitive Design in Phase 3

Phase 3 adds specific protections for participants who receive means-tested public benefits:
- 60-day advance notice before any distribution event fires
- Projected allocation information provided before distribution
- Strong advisement to consult a benefits counselor before electing USD cash-out
- **EMS Recognition Bonus election** — an irrevocable per-event option to receive distribution as permanent recognition hours rather than M$ or USD, specifically designed for participants who need to avoid financial instrument receipts for benefits eligibility purposes

### 4.4 Why It Matters to Funders

The Phase 3 dividend inverts the Central Appalachian extraction model. Wealth generated within the commons stays within the commons — and eventually returns to the community members who kept it alive. For grant funders focused on wealth-building, asset development, or community economic sovereignty, Phase 3 is the structural answer to "what does this system actually build?"

---

## 5. Founder's Technical Investment and Capacity Evidence

KTS (Carrie Ann Kidd personally, pending LLC formation) has made a substantial founder's capital contribution to MountainShares and Ms. Allis:

- **6,067.5 hours** of senior geospatial, AI, and systems architecture work from March 23, 2025 through May 14, 2026
- Valued at **$150/hour**, totaling a documented capital contribution of **$910,125**
- Detailed timesheets, monthly roll-ups, and milestone logs are available to support grant audits and due diligence
- Infrastructure is not hypothetical — the Ms. Allis node and server cluster are physically operational at 704 Main Street, Mount Hope, WV 25880

For funders, this contribution:
- Demonstrates significant **pre-award investment** and real technical capacity
- Provides **in-kind match documentation** for eligible grant programs accepting such match
- Reduces technical risk — core infrastructure already exists and has been tested rather than being conceptual
- Is treated as founder's capital into a commons system; no charitable deduction is claimed for the value of time, and no expectation of profit distributions from H4H is created by this contribution

---

## 6. Use of Program Revenues

Program revenues and related funds allocated to H4H in connection with MountainShares are intended to support:

- **H4H operations and staff** — organizational backbone for community programming and technical stewardship
- **704 Main Street / Fayette County Community Arts Center** — historic rehabilitation, cultural programming, ongoing maintenance, and Ms. Allis / ALLIS node operations
- **Oakvale Area Outreach Team** — staffing, daily operations, and project-based outreach work
- **Mount Hope Historic Walking Trail and Coalfield Chronicles Trail** — expansion, wayfinding, interpretation, and associated programming
- **In-house IT, GIS, and infrastructure maintenance** — MountainShares, Ms. Allis, GBIM, and The Commons platform

These allocations describe charitable and programmatic uses of revenue. They do not create any right to profit or distributions for participants or funders.

---

## 7. Governance and Automatic Constraints (Funder Summary)

Funders should understand the difference between what the community can govern and what is locked by design.

### 7.1 What Governance Can Adjust

- Earning rates within approved ranges
- Per-user and per-tier caps within safety bands
- Promo pool targeting
- County activation sequencing
- Program category definitions
- Annual Regulatory Compliance Budget approval
- Certain allocation mechanics (subject to floors and super-majority thresholds)

### 7.2 What Governance Cannot Override

- Hard safety triggers — enforced automatically, non-overridable at any threshold
- Reserve-based phase reversion — automatic, no vote required
- Permanent Phase 3 500% treasury floor — cannot be lowered or distributed from
- Benefits-Sensitive Account core protections
- The three-box structural separation between H4H, commons, and KTS
- Founder equity path prohibition through H4H or community EMS

This constraint architecture is specifically designed to protect funders, participants, and charitable assets from governance capture, extraction, or well-intentioned but structurally unsound decisions. It is a feature, not a limitation.

---

## 8. Summary for Funders

MountainShares is a community-governed, nonprofit-operated rewards and prepaid-value system that:

- Keeps value and decision-making rooted in West Virginia communities, beginning with Mount Hope
- Uses explicit safety math — two distinct reserve metrics, automatic reversion cascades, and non-overridable hard triggers — to balance community recognition with conservative financial commitments
- Channels program revenue to H4H operations, treasury reserves, infrastructure, and local projects rather than to outside investors
- Leverages a substantial, documented founder's technical investment ($910,125) and a transparent AI assistant (Ms. Allis) to deliver glass-box governance and operations
- Provides a clear, reservation-tested path toward Phase 2 ($10 EMS buying power) and Phase 3 (FVSR) buying-power expansion — conditional, deferred, and reversion-protected, not speculative
- Ends with a Phase 3 community surplus distribution designed to return genuine wealth to the people who built the commons — weighted by participation, protected for benefits-sensitive residents, and impossible to activate before the treasury is structurally strong enough to sustain it

For funders, this overview provides a coherent picture of who operates MountainShares, how it is financed and safeguarded, how EMS and PMS behave across phases, how the entity structure prevents extraction, and how the system supports long-term community stewardship rather than speculative or extractive models.

---

## Appendix A: Definitions

- **PMS / M$:** Purchased MountainShares; spendable network balance issued when USD is loaded into the system.
- **EMS:** Earned MountainShares; recognition credits for verified community contribution.
- **Operational Reserve Ratio:** Treasury USDC Reserve ÷ Total Outstanding Spendable PMS (M$). Governs day-to-day transaction safety and commerce features.
- **Treasury Reserve Solvency Ratio:** Treasury Reserve ÷ (Total Outstanding EMS + Total Outstanding M$). Governs EMS buying-power expansion and is the primary phase gate.
- **FVSR (Federal Volunteer Service Rate):** The IRS-published standard rate for valuing volunteer services, updated annually. The Phase 3 EMS rate is the FVSR in effect on Phase 3 activation — not at document publication. Current 2026 rate: $36.14.
- **UEI:** Unique Economic Identity; each participant's persistent identity in the system and governance structure.
- **Participation Weight (PW):** Phase 3 dividend allocation score — Verified Months Active × Activity Multiplier.
- **Benefits-Sensitive Account (BSA):** Enhanced-protection account for participants receiving or potentially receiving means-tested public benefits.
- **EMS Recognition Bonus:** Phase 3 optional distribution form — permanent recognition hours instead of M$ or USD. Irrevocable per event. Not income or assets.
- **Hard Trigger:** Automatic system rule enforced by Ms. Allis and the Phase Management Controller. Non-overridable by any governance vote at any threshold.
- **Reversion Cascade:** Automatic return to prior-phase buying-power rules when reserve thresholds fall below the applicable floor.
- **Structural Boundary Breach:** Any mechanism that creates founder equity through H4H, community EMS, or the community surplus pool.
- **Three-Box Structure:** Entity wall separating H4H (charitable anchor), MountainShares Commons/DUNA (community ledger), and KTS (founder commercial engine).

---

*MountainShares Funder Overview — Version 2.0*
*Harmony for Hope, Inc. | 704 Main Street, Mount Hope, WV 25880*
*Draft — Subject to H4H board review and legal counsel approval before reliance*

---

**End of MountainShares Funder Overview v2.0**
