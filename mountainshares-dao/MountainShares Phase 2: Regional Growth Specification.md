# MountainShares Phase 2: Regional Growth Specification

> **Disciplinary Context: Appalachian Economic Commons**
> This document instantiates Polymathmatic Geography principles P1, P9, P16, and related axioms for the Appalachian economic commons:
> - **P1 – Every where is entangled / Leakage and enclosure:** Sections 1–3 and 7–11 treat regional expansion, statewide reserve architecture, and the 300% treasury band as a single coupled system, explicitly tying minting ceilings and merchant network growth to real backing assets and graduated community trust.
> - **P9 – Transparency and traceability:** Sections 3, 4, 9, and 10 define public reserve-ratio calculations at the 300% band, statewide dashboards, and governance cadences so that every treasury position is observable and reconstructable over time.
> - **P16 – Power accountable to place:** Sections 2, 3, 5–7, and 11 bound DAO, Ms. Allis, and H4H authority inside hard economic and legal constraints at regional scale, ensuring that decisions about rates, caps, statewide rollout, and new region eligibility answer to local solvency and community safety.
> - **Anti-leakage and closed-loop spending:** The reserve-ratio-driven 300% band (Section 3) and the Stage 3 full-commerce unlock (Section 2) operationalize anti-leakage design at expanded geographic scale while keeping the closed loop anchored in verified backing assets.
> - **Bounty and corrective programs:** Regional promo-pool rules (Section 5) and example governance scenarios (Appendix B) show how expansion bonuses and parameter changes remain bounded by safety math rather than becoming unconstrained growth incentives.

**Version:** 2.0
**Date:** June 17, 2026
**Status:** DAO Governance Document — Structural Rewrite
**Scope:** West Virginia Statewide Expansion (Phase 2)
**Related documents:** [Phase 0 Specification](MountainShares%20Phase%200%3A%20Invite-Only%20Beta%20Specification.md), [Phase 1 Specification](MountainShares%20Phase%201%3A%20Economic%20Safety%20Specification.md), [Phase 3 Specification](MountainShares%20Phase%203%3A%20Surplus%20Distribution%20Specification.md), [Program Rules](MountainShares%20Program%20Rules(Draft).md), [Program Rules – Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md), [DAO Governance Charter](MountainShares%20DAO%20Governance%20Charter.md), [KPI Specification v3.0](MountainShares%20KPI%20Specification.md), [FA-001 Fee Amendment](../contract/H4H/Fee%20Amendment%20-%20FA001.md)

> **Entity Status Notice:** Kidd's Technical Services ("KTS") is not yet a registered West Virginia LLC and has no EIN. References to "KTS" in this document mean Carrie Ann Kidd personally, operating under that trade name. Formation of the WV LLC is the gating step before founder equity, ALLIS IP holding, and KTS-side capitalization instruments take legal effect. No Phase 2 mechanism creates a founder equity path through H4H or community EMS.

> **Server Location Notice:** The operational server cluster and Ms. Allis / ALLIS node for H4H and MountainShares Commons is located at **704 Main Street, Mount Hope, West Virginia 25880** (Fayette County Community Arts Center).

> **EMS Appreciation — Governing Rule:** Community EMS maintains stable baseline exchange value. Buying-power expansion schedules are **inactive** unless and until the Treasury Reserve achieves the applicable solvency threshold (300% of total EMS + M$ outstanding at Phase 2; 500% at Phase 3), all Treasury Reserve-funded transition and formation costs have been paid, and no reversion event has occurred. If the reserve metric falls below the applicable threshold, the system automatically reverts to prior-phase specifications to maintain continuity of service. No resident holds a vested appreciation right prior to threshold clearance. Community EMS is non-appreciating in the securities-law sense — it does not function as an investment contract and carries no present appreciation claim a resident can realize. Any appreciating founder-side instrument exists exclusively on the KTS side under separate, counsel-reviewed documentation.

---

## Structural Framework

This specification operates within the three-box entity structure governing MountainShares. All Phase 2 design choices must preserve the walls between these entities.

| Entity | Role | Phase 2 Relevance |
|---|---|---|
| Harmony for Hope, Inc. (H4H) | 501(c)(3) charitable anchor; program sponsor; legal operator | Holds all regulatory licenses and compliance obligations at statewide scale; files Regulatory Compliance Draw Requests; submits Annual Regulatory Compliance Budget; receives 30% of fee revenue for operations |
| MountainShares Commons / DUNA | Community-owned mutual-credit ledger and governance layer | EMS recognition ledger, UEIs, PMS prepaid system, statewide county activation, DAO governance, Tier 3 Regional Champions |
| Kidd's Technical Services (KTS) | To-be-formed for-profit LLC/PBC; founder-owned commercial engine | Ms. Allis / ALLIS deployment at 704 Main Street; founder-side rights documented separately; no equity path through EMS or H4H |

No Phase 2 mechanism may create a path by which founder value is realized through H4H or community EMS. Any such path found in operation is a Critical finding requiring immediate resolution.

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 1.0 | March 16, 2026 | Initial release — Phase 2 framework, 300% reserve band, statewide rollout, Stage 3 full-commerce unlock, regional governance expansion, Regulatory Compliance Reserve Draw mechanism |
| 2.0 | June 17, 2026 | **STRUCTURAL REWRITE:** Added dual reserve metric framework (Operational Reserve Ratio / Treasury Reserve Solvency Ratio); corrected EMS appreciation framing to reserve-gated, deferred, conditional — not present floating value; added reversion trigger language throughout; added three-box structural framework; corrected server location to 704 Main Street; added KTS entity status notice; aligned with FA-001, KPI Specification v3.0, and H4H Canonical Facts Sheet |

---

## 1. Foundation: What Phase 1 Built

Phase 2 does not start from zero. It starts from a proven, community-validated foundation built during Phase 1 at 704 Main Street and across Fayette County.

**What Phase 1 produced:**
- A fully operational reserve-backed M$ economy with a tested safety threshold system enforced by Ms. Allis
- A mature recognition ledger with thousands of verified UEIs, geo-tagged EMS hours, and real merchant transaction history
- A statewide merchant network capable of supporting Stage 3 full-commerce activity
- A graduated Champion corps ready to shift from data stewardship to regional governance leadership
- A reserve ratio that has held stable at ≥ 1.25 operational and ≥ 300% Treasury Reserve Solvency for 60+ consecutive days, meeting all Phase 2 graduation criteria
- A verified data stewardship layer with ≥ 500 active place records at ≥ 60% recency
- A DAO with demonstrated quorum and a governance track record
- Benefits-Sensitive Account protections reviewed by legal counsel and confirmed compliant
- Confirmed buying-power expansion gate logic: Phase 2 gate opened only after Treasury Reserve Solvency Ratio met 300% threshold with all formation fees paid
- All KTS formation and H4H/DUNA transition costs paid from the Treasury Reserve before Phase 2 activation

All EMS hours, ranks, and badges from Phase 0 and Phase 1 carry forward permanently at stable baseline value. Groundbreaker and Phase 1 founding badges are locked. The founding governance record is permanently anchored in the Phase 0 Pre-Launch Audit Report.

---

## 2. Core Economic Principles at the 300% Band

Phase 2 is defined by two governing thresholds operating simultaneously.

### 2.1 Dual Reserve Metric Framework

**Operational Reserve Ratio** governs day-to-day continuity of service, per-user caps, and Phase 2 commerce feature unlock:

~~~
Operational Reserve Ratio = Treasury USDC Reserve / Total Outstanding Spendable PMS (M$)
~~~

**Treasury Reserve Solvency Ratio** governs EMS buying-power expansion and is the primary appreciation gate:

~~~
Treasury Reserve Solvency Ratio = Treasury Reserve / (Total Outstanding EMS + Total Outstanding M$)
~~~

Both metrics are calculated daily by Ms. Allis, published on the dashboard with green/amber/red bands, and enforced by the Phase Management Controller. A reader — including a funder, auditor, or regulator — can see on the face of the dashboard whether any appreciation gate is open or closed.

### 2.2 EMS Appreciation Status in Phase 2

Phase 2 buying-power expansion activated because the Treasury Reserve Solvency Ratio reached 300% of total EMS + M$ outstanding **and** all Treasury Reserve-funded formation and transition costs were paid. That activation condition is documented in the Phase 1 → Phase 2 graduation record.

The Phase 2 appreciation schedule (1 EMS = $10 USD equivalent, user-controlled opt-in) is therefore **conditionally active** — not permanently vested. If the Treasury Reserve Solvency Ratio falls below 300%, the system automatically reverts to Phase 1 parameters:

- Expanded buying-power schedules suspend immediately
- No resident loses their principal EMS balance
- Reversion is logged to the durable audit trail
- The system returns to Phase 2 expansion parameters only after the 300% threshold is restored for two consecutive quarters

Phase 3 buying-power expansion (1 EMS = $the Federal Volunteer Service Rate (FVSR) in effect on the Phase 3 activation date) activates only when the Treasury Reserve Solvency Ratio reaches and sustains 500%.

Community EMS remains non-appreciating in the securities-law sense at all times — it does not function as an investment contract and carries no present appreciation claim that is vested or guaranteed. Any founder-side appreciating instrument exists exclusively on the KTS side under separate documentation.

### 2.3 Three-Stage Platform Arc

- **Stage 1** (barter/trade): Phase 0 and Phase 1 early
- **Stage 2** (discovery/TikTok-style): Phase 1 mature and Phase 2 entry; operational reserve ratio ≥ 1.5
- **Stage 3** (full commerce/Amazon-style): Phase 2 confirmed; operational reserve ratio ≥ 3.0 for 30+ consecutive days

### 2.4 Legal Operability as a Treasury Priority

The commons cannot function without H4H maintaining its legal and regulatory standing. Treasury reserve funds are available, through the governed and transparent process defined in Section 7A, to cover verified regulatory compliance costs that are prerequisites to MountainShares operating legally at Phase 2 scale and beyond. This is legal infrastructure, not discretionary spending.

---

## 3. EMS Conversion Rates and Per-User Caps (Phase 2)

### 3.1 Phase 2 EMS Buying-Power Expansion (Conditionally Active)

EMS buying-power expansion is conditionally active in Phase 2 at a 10× rate (1 EMS = $10 USD equivalent), subject to the reversion conditions in Section 2.2. No resident holds a vested right to this expanded buying power — conversion is user-initiated, optional, and incremental. The treasury pays USDC only for EMS that users actively choose to convert; vaulted EMS remains off-balance-sheet recognition until conversion.

All EMS not yet converted continues to vault. If Phase 3 conditions are met (500% Treasury Reserve Solvency), vaulted EMS may be converted at the Federal Volunteer Service Rate (FVSR) in effect on the Phase 3 activation date×.

### 3.2 Global Base Rate at Phase 2 Scale

- **Floor:** 0.5 M$ per EMS hour (Phase 2 minimum; lower rates belong to Phase 1 recovery scenarios only)
- **Ceiling:** 2.0 M$ per EMS hour (unlocked only at ≥ 300% operational reserve ratio, via DAO vote)
- **Range:** 0.5 – 2.0 M$ per EMS hour, governed by the Phase 2 Safety Threshold Table in Section 3.4

All current rates and caps are maintained in the [Program Rules – Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md).

### 3.3 Per-User Convertible Caps (Monthly, Phase 2)

| User Tier | Definition | Monthly Cap (M$) | Weekly Cap | Daily Cap |
|---|---|---|---|---|
| **Tier 1** | General Commons participants | 80 M$ | 20 hrs | 3–4 hrs |
| **Tier 2** | Verified EMS, caregiving, high-need community roles (geo+UEI validated) | 160 M$ | 40 hrs | 8 hrs |
| **Tier 3** | Regional Champion, governance leadership, data stewardship anchor (DAO-confirmed) | 240 M$ | 60 hrs | 12 hrs |

**Tier 3 is new in Phase 2.** Tier 3 assignment requires: Phase 1 Champion history + DAO confirmation vote + Ms. Allis geo-activity verification across ≥ 2 counties.

### 3.4 Benefits-Sensitive Account Protections (Phase 2)

All Phase 1 Benefits-Sensitive Account protections carry forward unchanged. EMS conversion in Phase 2 is participant-timed and incremental, allowing benefits-sensitive participants to manage eligibility impact. Phase 2 adds:

- **Statewide legal review:** Before any new county activates, Benefits-Sensitive Account thresholds are reviewed against that county's predominant benefits mix.
- **County-level cap variation:** Ms. Allis may apply county-specific Benefits-Sensitive caps where legal counsel determines the statewide threshold is insufficient for a specific program mix. County-level variations are published in the Parameter Tables and reviewed quarterly.
- **No forced conversion at Phase 2 activation:** Participants who vaulted EMS in Phase 1 are never automatically converted; each participant controls their own conversion timing.
- **No forced disclosure:** Participation in The Commons does not require disclosure of benefit status at any tier.

### 3.5 Phase 2 Safety Threshold Table (Ms. Allis Enforces Automatically)

| Operational Reserve Ratio | Treasury Reserve Solvency Ratio | Global Base Rate | Tier 1 Cap | Tier 2 Cap | Tier 3 Cap | Stage 3 Commerce | EMS Buying-Power Status | Action |
|---|---|---|---|---|---|---|---|---|
| ≥ 3.0 (300%) | ≥ 300% (P2 active) | 1.5–2.0 M$/hr (DAO vote) | 80 M$/mo | 160 M$/mo | 240 M$/mo | Fully unlocked | Conditionally active — 1 EMS = $10 | DAO may vote to increase rate toward 2.0 |
| 2.0 – 2.99 | ≥ 300% | 1.0–1.5 M$/hr (DAO-controlled) | 80 M$/mo | 120 M$/mo | 180 M$/mo | Unlocked (monitored) | Conditionally active | DAO can vote to hold or increase if trend stable |
| 1.5 – 1.99 | ≥ 300% | 0.5–1.0 M$/hr (DAO-controlled) | 80 M$/mo | 100 M$/mo | 140 M$/mo | Stage 2 only | Conditionally active | DAO can vote to hold steady; Stage 3 gated |
| < 1.5 | Any | Phase 1 thresholds reactivate | Phase 1 caps | Phase 1 caps | Tier 3 paused | Stage 2 only | Suspended pending recovery | Auto-revert to Phase 1 safety rules; Tier 3 suspended |
| Any | < 300% | Phase 1 thresholds reactivate | Phase 1 caps | Phase 1 caps | Tier 3 paused | Stage 2 only | **Reverted to Phase 1 — buying-power expansion suspended** | Automatic reversion; no vote required |

**Automatic Trigger Logic:**
- Ms. Allis recalculates both reserve metrics daily.
- If operational reserve ratio drops below 1.5, Phase 2 Tier 3 suspends automatically and Phase 1 thresholds reactivate.
- If operational reserve ratio drops below 0.75, Phase 1 emergency floor fires.
- Stage 3 commerce features lock automatically if operational reserve ratio drops below 2.0 for 7 consecutive days.
- **If Treasury Reserve Solvency Ratio drops below 300%, buying-power expansion reverts to Phase 1 immediately — no DAO vote required.**
- Regulatory Compliance Reserve Draws (Section 7A) are calculated against both reserve ratios after draw, not before. No draw may fire if it would push either metric below its applicable phase floor.

---

## 4. Treasury Backing and Hard Reserve Thresholds (Phase 2)

### 4.1 Reserve Metrics Definition

**Operational Reserve Ratio:**

~~~
Operational Reserve Ratio = Liquid Backing Assets (USD) / Total Outstanding Spendable M$
~~~

**Treasury Reserve Solvency Ratio:**

~~~
Treasury Reserve Solvency Ratio = Treasury Reserve / (Total Outstanding EMS + Total Outstanding M$)
~~~

**Backing Assets Include:**
- USD load fees (users converting USD → M$)
- Merchant transaction fees (1.80% of eligible M$ transactions)
- Internal transfer fees (0.25%)
- ATM/refund fees ($1.25 flat per cash-out transaction)
- CLIO NFT revenue
- DAO-approved grants or donations
- Regional activation revenue and Stage 3 commerce transaction fees

**Excludes:** EMS recognition hours (vaulted, not circulating supply), future promises, unfunded projections, speculative asset valuations.

> **Fee Revenue Allocation:** All collected fees are allocated per [Program Rules – Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md) Section 4.3:
>
> | Bucket | Allocation | Purpose |
> |---|---|---|
> | 1 | 30% | Harmony for Hope, Inc. (H4H Operations) |
> | 2 | 30% | Treasury Reserve |
> | 3 | 15% | Platform Development |
> | 4 | 15% | Community Programs |
> | 5 | 10% | Community Projects |
> | — | +0.55% | Supplemental Treasury Reserve (on gross transaction volume) |

### 4.2 Treasury Reserve Draw Authority

Two draw categories exist in Phase 2:

**Category A — Automatic Safety Draws:** Ms. Allis draws from the Treasury Reserve automatically to maintain reserve ratio thresholds, fund verified EMS conversions within approved caps, and execute approved promo pool disbursements. These require no DAO vote.

**Category B — Regulatory Compliance Reserve Draws:** H4H may draw from the Treasury Reserve for documented, verified regulatory compliance costs that are prerequisites to MountainShares operating legally at Phase 2 scale. Governed by Section 7A.

No other draws from the Treasury Reserve are authorized. The DAO may not vote to authorize draws for general operating expenses, speculative investments, or purposes not listed in this document.

---

## 5. Monthly and Regional Promo and Bonus Pool (Phase 2)

### 5.1 Promo Pool Budget
- **Source:** Allocated from fees and treasury per the smart contract structure and [Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md) Section 4.2.
- **Max Size:** 3–5% of monthly processed volume, capped at Y M$/month (DAO sets Y per Parameter Tables).
- **Regional Targeting:** DAO may designate a portion of the promo pool for county-specific activation campaigns — new-county bonuses that draw from the regional pool, not from local budgets.

### 5.2 Bonus Rules (Phase 2)
- All bonuses draw from the pool and still count against per-user monthly caps.
- Once pool is exhausted in a month, no new bonuses are offered until next cycle.
- Bonuses pause automatically when operational reserve ratio < 2.0.
- Regional activation bonuses (for first-time UEIs in newly activated counties) are a new Phase 2 bonus category.
- Stage 3 commerce launch bonuses (merchant onboarding incentives, first-transaction bonuses) draw from the pool subject to the same reserve-ratio rules.

---

## 6. EMS Earning Categories (Phase 2 Additions)

All Phase 1 EMS categories carry forward unchanged. EMS earned in all categories remains non-appreciating in the securities-law sense — no present appreciation claim, no investment contract, no vested conversion right. Phase 2 adds the following:

| Category | Examples | Notes |
|---|---|---|
| **Regional Governance** | Multi-county DAO coordination, statewide proposal development, inter-county data reconciliation | Tier 3 eligible with DAO co-sign |
| **Merchant Onboarding** | Recruiting, training, and onboarding new merchants in newly activated counties | 1 EMS hr per verified onboarding session |
| **Stage 3 Commerce Support** | Full-commerce transaction facilitation, buyer/seller dispute resolution, marketplace quality review | 1 EMS hr per verified session |
| **County Activation Leadership** | Leading ground-truthing campaigns in newly activated counties | Promo bonus when reserve permits |

---

## 7. DAO Authority at Phase 2 Scale

### 7.1 DAO Can Vote To Change (Requires Super-Majority, 66%+)

All Phase 1 DAO authorities carry forward. Phase 2 adds:

- County activation sequence (add or reorder counties), subject to Ms. Allis pre-conditions
- Tier 3 assignment criteria (expand or restrict Regional Champion eligibility)
- Stage 3 commerce feature rollout pace (accelerate or defer), only if both reserve metrics support it
- Regional promo pool regional targeting (county-specific allocation rules)
- Annual Regulatory Compliance Budget (approve H4H's submitted annual budget per Section 7A.5)
- Phase 2 → Phase 3 graduation readiness vote (advisory; binding graduation criteria remain in Section 11)
- **Treasury Reserve Solvency Ratio thresholds (300% Phase 2 / 500% Phase 3)** require DUNA governance approval through formal proposal and quorum-verified vote; any proposed reduction requires additional legal review

### 7.2 DAO Cannot Override (Phase 2 Hard Triggers)

All Phase 1 hard trigger rules carry forward unchanged. Phase 2 adds:

- Vote to activate a new county without Ms. Allis pre-condition verification
- Override Stage 3 commerce lock when operational reserve ratio < 2.0
- Suspend Tier 3 rotation requirements
- Override county-specific Benefits-Sensitive Account thresholds set by legal review
- Authorize Treasury Reserve draws for any purpose not listed in Section 4.2
- Block or delay a Regulatory Compliance Reserve Draw that has met all conditions in Section 7A
- Override automatic reversion of buying-power expansion when Treasury Reserve Solvency Ratio falls below 300%
- Force any participant to convert vaulted EMS

---

## 7A. Regulatory Compliance Reserve Draw (H4H Operational Authority)

### 7A.1 Purpose and Scope

Harmony for Hope, Inc. (H4H) is the founding legal entity and operational steward of the MountainShares commons. The commons cannot function without H4H maintaining its legal and regulatory standing. At Phase 2 scale — statewide merchant transactions, a live M$ economy, and a growing participant base — H4H is subject to West Virginia financial regulation, federal financial oversight requirements, nonprofit compliance obligations, and potentially federal or state licensing requirements for money transmission or related activities.

These obligations are not optional and they are not predictable on a fee-revenue schedule. Some arise on short notice. Some front-load at phase transitions before fee revenue volume is sufficient to cover them from the H4H operational allocation alone. All of them, if unmet, can halt the entire commons system.

**Known regulatory landscape as of 2026:**

- **WV Money Transmitter License (WV Division of Financial Institutions):** Initial application fee of $1,000; surety bond requirement of $300,000 (annual bond premium typically $1,500–$9,000 depending on H4H's financial standing); minimum net worth requirement of $50,000; annual renewal fee of $250 plus $20 per additional location. This license may be required before Phase 2 statewide transaction volume is legally permissible.
- **FinCEN Money Services Business (MSB) Registration:** Federal registration via Form 107 through BSA E-Filing. No federal filing fee; legal counsel costs to structure and file correctly typically $2,000–$5,000.
- **WV SB887 / HB5179 (2026 Legislative Session):** Active West Virginia legislation specifically addressing money transmission and virtual currency. H4H must monitor this legislation actively and flag compliance requirements to the DAO as soon as they are known.
- **IRS Nonprofit Annual Compliance (Form 990):** Filing is free; late penalties run $20/day up to $11,000 for organizations under approximately $1.1M gross receipts.
- **State and Federal Legal Counsel:** Full MTL application legal support typically costs $5,000–$25,000. FinCEN registration support typically $2,000–$5,000.

### 7A.2 Eligible Expenditures

Regulatory Compliance Reserve Draws are authorized **only** for the following categories:

| Category | Examples | Verification Required |
|---|---|---|
| **Federal Program Registration and Compliance** | IRS Form filings, federal nonprofit compliance, FinCEN MSB registration legal costs | Filed document + date + fee receipt or legal invoice specifying compliance scope |
| **State Legal Entity Maintenance** | WV Secretary of State annual fees, registered agent fees, state nonprofit filings, state regulatory registrations required to operate a payment or credit system in WV | Filed document + date + fee receipt |
| **Payment and Financial Regulation** | WV MTL application and renewal fees, surety bond premiums, FinCEN registration costs, state MSB registration fees, legal counsel costs directly tied to regulatory compliance review | Regulatory filing or legal invoice specifying compliance scope |
| **Legislative Compliance Response** | Costs arising directly from new WV or federal legislation (including SB887 and any successor legislation) imposing new licensing, registration, or structural requirements | Legislative text citation + regulatory filing or legal invoice |
| **Federal and State Audit or Examination Fees** | Costs imposed by a regulator as a condition of examination — not voluntary audits | Regulatory demand document + fee receipt |
| **Legal Counsel for Regulatory Navigation** | Attorney fees specifically for regulatory compliance, licensing, or legal structure maintenance | Legal invoice specifying regulatory compliance scope; general retainer costs not eligible |
| **Formal Dispute Resolution Required by Law** | Filing fees for legally mandated dispute processes involving the DAO, the commons, or H4H's operational status | Court or agency filing document + fee receipt |
| **Participant Protection Legal Costs** | Legal costs specifically incurred to defend or maintain Benefits-Sensitive Account protections, participant data protections, or other participant-protective legal mechanisms | Legal invoice specifying participant protection scope |

### 7A.3 What Is NOT Eligible

Regulatory Compliance Reserve Draws may **not** be used for:
- H4H general operating expenses (staff salaries, rent, utilities, equipment)
- Voluntary legal consultations not tied to a specific regulatory requirement
- Marketing, outreach, or community engagement costs
- Technology development or platform infrastructure costs
- Grant writing or fundraising costs
- Any cost that can be funded through H4H's 30% operational allocation without material harm to H4H's ability to maintain the commons infrastructure

### 7A.4 Draw Process and Governance

**Step 1 — Request:**
H4H files a Regulatory Compliance Draw Request with the DAO, including: category of expenditure, specific regulatory body or legislation driving the cost, amount requested, supporting documentation, and attestation that the cost cannot be funded from the current H4H operational allocation without material harm.

**Step 2 — Ms. Allis Verification:**
Ms. Allis verifies: the requested amount does not reduce either reserve metric below its applicable phase floor after draw; the request category matches Section 7A.2; the request is not a duplicate of a previously approved draw. Ms. Allis publishes the verification result publicly within 24 hours.

**Step 3 — DAO Notification and Comment Window:**
- For draws ≤ $10,000: 72-hour community comment window; H4H may proceed if no objection vote passes within the window
- For draws > $10,000 and ≤ $50,000: 7-day community comment window + simple majority DAO confirmation vote required before draw fires
- For draws > $50,000: 14-day community comment window + 66% super-majority DAO vote required

> **Note on the $50,000 threshold:** The full WV Money Transmitter License process — application fee, first-year surety bond premium, and legal counsel — could approach $30,000–$40,000 in a single initial engagement. This is expected. The $50,000 super-majority threshold is a safeguard for very large draws, not a barrier to necessary licensing.

**Step 4 — Draw and Public Record:**
Upon approval, Ms. Allis executes the draw from the Treasury Reserve. The draw is recorded permanently in the public governance ledger with: amount, category, regulatory requirement, date, and DAO confirmation status. H4H must provide proof of payment within 30 days of draw; proof is published in the governance ledger.

### 7A.5 Annual Regulatory Compliance Budget

H4H shall submit an Annual Regulatory Compliance Budget to the DAO each year:
- Submitted no later than 60 days before the start of each calendar year
- Itemized by expenditure category and estimated amount
- Includes known recurring costs and projected one-time costs
- Subject to simple majority DAO approval vote

If the annual budget is approved, individual draws within the approved categories and amounts may proceed through the 72-hour comment window regardless of size, provided Ms. Allis verification passes.

### 7A.6 Reserve Floor Protection

No draw may reduce either reserve metric below its applicable phase floor. If a draw would breach any floor, Ms. Allis automatically defers it to the deferral queue. **Deferral is not denial.** A deferred draw executes automatically as soon as the treasury can accommodate it without breaching the floor, subject to the original DAO approval remaining valid (expires after 180 days).

If a legally required compliance cost is deferred, H4H must notify the relevant regulatory body in writing and document that notification in the governance ledger. If deferral would result in a lapse of a legally required license, H4H must call an emergency governance session within 48 hours.

### 7A.7 Relationship to the Fee Revenue Allocation

The Regulatory Compliance Reserve Draw does not replace or reduce H4H's 30% operational allocation from fee revenue. Both mechanisms exist simultaneously: the 30% allocation funds recurring operating costs; the Reserve Draw backstops costs that are front-loaded, irregular, volume-independent, or time-critical.

### 7A.8 Transparency Commitment

H4H commits to: publishing all draw requests publicly at submission; publishing Ms. Allis verification results within 24 hours; publishing proof of payment within 30 days; including a full annual draw summary in the year-end governance report; flagging all known or anticipated regulatory requirements to the DAO no later than 90 days before a compliance deadline.

---

## 8. Statewide Rollout Protocol

### 8.1 County Activation Sequence

Statewide expansion is not a single launch event. Counties activate in a governed sequence:

1. **Anchor counties** (Fayette, Nicholas, Raleigh) activate first — founding geographic base of the system.
2. **Adjacent counties** activate when anchor counties hold ≥ 2.0 operational reserve ratio for 30+ consecutive days AND the anchor data stewardship layer has ≥ 75% record recency in those counties.
3. **Full statewide** opens when ≥ 10 counties are active and system-wide operational reserve ratio is ≥ 3.0 for 30+ consecutive days.

### 8.2 New County Activation Requirements

Before a new county activates, Ms. Allis verifies:
- ≥ 3 active Merchants in the county OR ≥ 1 active Merchant and ≥ 50 UEIs in the county
- At least 1 Community Champion with geo-verified presence in the county
- Benefits-Sensitive Account thresholds reviewed for county-specific benefit program mix
- No outstanding systemic fraud or reserve-threatening incidents in adjacent counties
- No outstanding deferred Regulatory Compliance Reserve Draws that, if fired simultaneously with county activation costs, would breach the 3.0 operational reserve floor
- Treasury Reserve Solvency Ratio confirms Phase 2 gate remains open (≥ 300%)
- DAO vote confirming readiness (simple majority)

### 8.3 Regional Data Stewardship at Scale

- Each newly activated county requires a minimum of 25 verified place records before first M$ transactions are enabled in that county.
- Ms. Allis runs county-level data confidence scoring in addition to network-wide scoring.
- Regional Champions (Tier 3) are the primary ground-truthing force in newly activated counties.
- County activation is gated on data quality, not only on financial metrics.

---

## 9. One UEI = One Vote (Phase 2)

The one-UEI one-vote principle is unchanged. Phase 2 adds:

- **County-scoped proposals:** For proposals affecting a single county, only UEIs with verified presence in that county may vote. Network-wide proposals remain open to all eligible UEIs.
- **Tier 3 governance advisory role:** Regional Champions (Tier 3) may submit governance proposals without a co-sponsor. All other tiers still require 2+ co-signers.
- **Voting rights threshold unchanged:** 30 days on-platform + minimum 10 EMS hours (Bronze rank).
- **Regulatory Compliance Draw votes:** All eligible UEIs may participate in comment windows and confirmation votes.

---

## 10. Transparency and Dashboards (Phase 2)

All Phase 1 dashboard features carry forward. Phase 2 adds:

**County-level:**
- Per-county operational reserve ratio contribution, active UEI count, merchant transaction volume
- Per-county data stewardship KPIs: % records verified in last 12 months, records collected, ping response rate
- County activation status and pre-condition checklist (publicly visible)

**Regional:**
- Statewide operational reserve ratio, backing assets, total outstanding M$, and 300% band proximity indicator
- **Treasury Reserve Solvency Ratio** prominently displayed with Phase 2 (300%) and Phase 3 (500%) threshold markers
- EMS buying-power expansion status: Active (P2) / Reverted / Pending P3
- Stage 3 commerce unlock status and days at current ratio
- Phase 2 → Phase 3 graduation criteria checklist with current status (publicly visible)

**Regulatory Compliance:**
- All pending and completed Regulatory Compliance Draw Requests (amount, category, status)
- Approved annual Regulatory Compliance Budget (current year) and year-to-date draw total
- Any active legislative or regulatory developments flagged by H4H

---

## 11. Phase 2 → Phase 3 Graduation Criteria

**Transition to Phase 3 only when ALL of the following hold for 90+ consecutive days:**

- Operational reserve ratio stable ≥ 3.0 (no dips below 2.5 in the 90-day window)
- **Treasury Reserve Solvency Ratio ≥ 500% of total EMS + M$ outstanding for 2+ consecutive quarters**
- Monthly processed volume ≥ 2M USD statewide
- Active UEIs ≥ 10,000 across ≥ 10 active counties
- Stage 3 full-commerce features active and operating without systemic incidents
- Zero systemic fraud or reserve-threatening exploits
- DAO governance participation ≥ 40% quorum on key votes
- Data stewardship layer: ≥ 5,000 verified place records statewide, ≥ 65% verified in last 12 months
- Benefits-Sensitive Account protections reviewed statewide by legal counsel and confirmed compliant
- All required WV and federal regulatory registrations and licenses confirmed current and in good standing
- No deferred compliance draws in an unresolved state
- DAO advisory vote on Phase 3 readiness passes (simple majority; advisory only — binding criteria above govern)

**Phase 3 Changes:** Treasury surplus distribution protocol activates; 500% Treasury Reserve Solvency Ratio becomes the new maintenance floor; community dividend engine becomes operational; EMS appreciation schedule advances to the Federal Volunteer Service Rate (FVSR) in effect on the Phase 3 activation date× for vaulted EMS not yet converted. See Phase 3 Specification.

---

## 12. Safety Prohibitions (Phase 2)

All Phase 1 safety prohibitions carry forward unchanged at statewide scale. Phase 2 adds:

| Category | Prohibition | Detection | Consequence |
|---|---|---|---|
| **County Spoofing** | No false geo-claims to access county-specific promo campaigns or activation bonuses | Geo cross-check + UEI history | Account freeze + investigation |
| **Tier Manipulation** | No falsification of multi-county Champion presence to qualify for Tier 3 | Geo audit + org co-sign verification | Tier demotion + account review |
| **Merchant Shell Activity** | No fake merchants created to generate transaction volume toward graduation criteria | Transaction pattern analysis + site verification | Account freeze + report |
| **Compliance Draw Fraud** | No falsification of regulatory documents or invoices to obtain a Regulatory Compliance Reserve Draw | Document verification + external regulatory cross-check | Permanent H4H governance suspension + legal referral |
| **Structural Boundary Breach** | No mechanism that creates founder equity through H4H or community EMS | Audit + legal review | Critical finding; immediate resolution required |

---

## 13. Audit and Governance Cadence (Phase 2)

All Phase 1 audit cadences carry forward. Phase 2 adds or adjusts:

- **Weekly:** County-level network snapshots added to standard weekly report; both reserve metrics published
- **Monthly:** Per-county treasury audit included in full treasury audit; county activation pre-condition review; Regulatory Compliance Draw status report; Treasury Reserve Solvency Ratio trend analysis
- **Quarterly:** Statewide external audit (goal: independent WV nonprofit or university partner); Tier 3 multi-county presence verification; county-specific Benefits-Sensitive Account review; review of any active or pending regulatory or legislative developments affecting the commons; EMS vaulted/converted balance reconciliation
- **Annually:** H4H submits Annual Regulatory Compliance Budget to DAO no later than 60 days before calendar year start
- **At each county activation:** Pre-activation Ms. Allis verification report published publicly before DAO vote

---

## 14. Sunset and Emergency Powers (Phase 2)

All Phase 1 emergency powers carry forward. Phase 2 adds:

### 14.1 If Operational Reserve Ratio Falls Below 1.5
- Tier 3 suspends automatically; Phase 1 thresholds reactivate
- Stage 3 commerce features lock automatically
- No new county activations until ratio recovers to ≥ 2.0 for 30+ consecutive days
- All pending Regulatory Compliance Reserve Draws are reviewed; draws that would breach the 3.0 floor are automatically deferred per Section 7A.6
- Emergency governance session called within 48 hours

### 14.2 If Treasury Reserve Solvency Ratio Falls Below 300% (Reversion Event)
- Buying-power expansion reverts to Phase 1 parameters immediately
- Expanded buying-power schedules suspend; no resident loses principal EMS balance
- Reversion logged to durable audit trail with timestamp, current ratio, and triggering metric
- Plain-language notice published to all participants
- System returns to Phase 2 expansion parameters only after 300% threshold is restored for two consecutive quarters

### 14.3 If a County-Level Fraud Event Occurs
- Affected county's transactions freeze pending review
- Network-wide activity continues in unaffected counties
- Affected county's Champions placed on administrative hold pending investigation
- County reactivation requires DAO vote + Ms. Allis pre-condition re-verification

### 14.4 If a Regulatory Compliance Deadline Cannot Be Met Due to Reserve Constraints
- H4H calls an emergency governance session within 48 hours of identifying the conflict
- Ms. Allis publishes a plain-language explanation to all participants
- DAO considers options: temporary minting reduction to accelerate reserve growth; emergency fundraising; phased draw; or governed operational pause in the affected jurisdiction
- H4H notifies the relevant regulatory body in writing; documentation filed in the governance ledger

---

## Appendix A: Definitions (Phase 2)

All Phase 1 definitions carry forward. Phase 2 adds or amends:

- **300% Reserve Band:** The treasury position at which the operational reserve ratio ≥ 3.0; the Phase 2 operational target and Stage 3 unlock gate.
- **Treasury Reserve Solvency Ratio (Phase 2 Gate):** Treasury Reserve ÷ (Total Outstanding EMS + Total Outstanding M$). Phase 2 activation threshold: ≥ 300% with all formation fees paid. Reversion trigger: < 300%.
- **Treasury Reserve Solvency Ratio (Phase 3 Gate):** ≥ 500%. Reversion trigger: < 500% (reverts to Phase 2 parameters); < 300% (reverts to Phase 1 parameters).
- **EMS Buying-Power Expansion (Phase 2, Conditionally Active):** 1 EMS = $10 USD equivalent; user-initiated, optional, incremental. Active only while Treasury Reserve Solvency Ratio ≥ 300%. Not vested — subject to reversion.
- **Tier 3:** Regional Champion tier; requires multi-county geo-verified presence and DAO confirmation; highest earning tier in Phase 2; suspends automatically if operational reserve ratio < 1.5.
- **County Activation:** Formal process by which a new county joins the MountainShares network, gated on data stewardship, merchant presence, regulatory compliance standing, and DAO vote.
- **Stage 3 Full Commerce:** Amazon-style full-commerce feature set of The Commons platform, unlocked when operational reserve ratio ≥ 3.0 for 30+ consecutive days.
- **Regulatory Compliance Reserve Draw:** Governed, transparent, bounded draw from the Treasury Reserve for documented and verified regulatory compliance costs; governed by Section 7A.
- **Deferral Queue:** Ms. Allis-managed queue of approved but reserve-floor-constrained draws that fire automatically when the treasury can accommodate them without breaching the applicable floor.
- **WV Money Transmitter License (MTL):** State license required by the West Virginia Division of Financial Institutions; initial application fee $1,000; $300,000 surety bond; $50,000 minimum net worth; $250 annual renewal.
- **FinCEN MSB Registration:** Federal Money Services Business registration via Form 107 through BSA E-Filing; no federal fee.

---

## Appendix B: Example Governance Scenario

**Month 4 of Phase 2 — Regulatory Compliance Draw:**

- Operational reserve ratio = 2.6; Treasury Reserve Solvency Ratio = 310% (Phase 2 gate open)
- H4H files a Regulatory Compliance Draw Request for WV MTL initial application: $1,000 application fee + $6,500 first-year surety bond premium + $12,000 legal counsel = **$19,500 total**
- Category: Payment and Financial Regulation
- Supporting documentation: WV DFI application form, bond quote, legal engagement letter specifying MTL application scope
- Ms. Allis verifies: $19,500 draw would leave operational reserve ratio at 2.58 — below the 3.0 Phase 2 operational floor
- **Ms. Allis defers the draw to the deferral queue.** Operational reserve ratio must reach 3.0 before the draw can fire.
- Ms. Allis publishes plain-language notice: "H4H has an approved regulatory compliance draw of $19,500 for WV Money Transmitter License. The draw is queued and will fire automatically when the operational reserve ratio reaches 3.0. Current ratio: 2.6. Estimated days to threshold at current growth rate: 38 days."
- H4H notifies WV DFI that the application will be filed within 45 days and documents this in the governance ledger.
- **Day 39:** Operational reserve ratio reaches 3.0. Ms. Allis fires the draw automatically. MTL application filed. Public governance ledger updated.

**Month 6 of Phase 2 — County Activation:**

- Operational reserve ratio = 3.1; Treasury Reserve Solvency Ratio = 320% (Phase 2 gate open)
- Ms. Allis pre-condition verification for Summers County: passed (all metrics confirmed including Benefits-Sensitive cap review and solvency ratio confirmation)
- DAO vote: 74% in favor
- Summers County activates. New-county activation bonuses drawn from regional promo pool.

---

## Appendix C: Participation Roles Cross-Reference (Phase 2)

For a complete map of who participates in The Commons and MountainShares, see the [Participation Map](../the%20commons/Participation%20Map.md).

| Role | Phase 2 Relevance |
|---|---|
| **Commons User** | Subject to Phase 2 per-user caps; eligible for Stage 3 full-commerce features; controls own EMS conversion timing |
| **Phase 0 / Phase 1 Participant** | All founding EMS hours and badges carry forward permanently at stable baseline value |
| **Community Champion (Tier 2)** | Primary local anchor; transitions toward merchant onboarding in Phase 2 early |
| **Regional Champion (Tier 3)** | New Phase 2 role; multi-county governance and data stewardship leadership |
| **Safety Champion** | Ongoing post-Phase 1 safety review; monitors both reserve metrics; feeds into quarterly audit cycle at statewide scale |
| **Merchant** | Stage 3 commerce features expand available transaction types; fee structure unchanged; 30% of fees to Treasury Reserve |
| **Harmony for Hope, Inc. (H4H)** | Maintains all regulatory and legal standing required for commons operation; files Regulatory Compliance Draw Requests per Section 7A; submits Annual Regulatory Compliance Budget; flags emerging legislative and regulatory developments to the DAO; operates Ms. Allis / ALLIS node at 704 Main Street |
| **Ms. Allis** | Enforces all hard triggers at statewide scale; monitors both reserve metrics daily; runs county activation pre-condition verification; manages deferral queue; publishes county-level and compliance dashboards; surfaces EMS appreciation gate status |
| **Phase Management Controller** | Smart contract enforcing phase-based rules; processes ATM withdrawals; applies automatic phase transitions including reversion events; enforces both appreciation gate conditions |

---

*"The commons grows county by county, hand by hand. Ms. Allis watches the math so the growth stays honest. H4H holds the legal door open so the growth stays possible."*

*MountainShares Phase 2: Regional Growth Specification — Version 2.0*
*Harmony for Hope, Inc. | 704 Main Street, Mount Hope, WV 25880*
*Draft — Subject to H4H board review and legal counsel approval before reliance*

---

**End of MountainShares Phase 2: Regional Growth Specification v2.0**
