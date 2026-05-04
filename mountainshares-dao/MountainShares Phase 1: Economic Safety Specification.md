# MountainShares Phase 1: Economic Safety Specification

> **Disciplinary Context: Appalachian Economic Commons**
> This document instantiates Polymathmatic Geography principles P1, P9, P16, and related axioms for the Appalachian economic commons:
> - **P1 – Every where is entangled / Leakage and enclosure:** Sections 1–3 and 7–11 treat recognition, time credits, prepaid value, reserve ratios, and phase transitions as a single coupled system, explicitly tying minting and circulation to backing assets and regional program realities. See [https://github.com/H4HWV2011/msallis-public-docs/blob/main/docs/Polymathmatical-Geography.md](https://github.com/H4HWV2011/msallis-public-docs/blob/main/docs/Polymathmatical-Geography.md)
> - **P9 – Transparency and traceability:** Sections 3, 4, 9, and 10 define public reserve-ratio calculations, dashboards, audits, and governance cadences so that money creation, caps, and emergency actions are observable and reconstructable over time.
> - **P16 – Power accountable to place:** Sections 2, 3, 5–7, and 11 bound DAO, Ms. allis, and H4H authority inside hard economic and legal constraints, ensuring that decisions about rates, caps, and shutdowns answer to local solvency and community safety rather than abstract speculation.
> - **Anti-leakage and closed-loop spending:** The separation of the time bank recognition ledger from capped, reserve-backed prepaid value (Section 1) and the reserve-ratio-driven phase transition table (Section 4) operationalize anti-leakage design and keep the closed loop anchored in real backing assets.
> - **Bounty and corrective programs:** Promo-pool rules (Section 5) and example governance scenarios (Appendix B) show how targeted bonuses and parameter changes can be treated as bounded "bounties" aligned with safety math rather than unconstrained giveaways.

**Version:** 2.0  
**Date:** May 4, 2026  
**Status:** DAO Governance Document  
**Scope:** West Virginia Pilot (Phase 1)  
**Related documents:** [Phase 0 Specification](MountainShares%20Phase%200%3A%20Invite-Only%20Beta%20Specification.md), [Program Rules](MountainShares%20Program%20Rules(Draft).md), [Program Rules – Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md), [DAO Governance Charter](MountainShares%20DAO%20Governance%20Charter.md), [MountainShares Gamification: The Contribution Game](MountainShares%20Gamification%3A%20The%20Contribution%20Game.md), [The Commons Gamification: The Daily Life Game](../the%20commons/The%20Commons%20Gamification%3A%20The%20Daily%20Life%20Game.md), [Participation Map](../the%20commons/Participation%20Map.md), [KPI Specification](MountainShares%20KPI%20Specification.md)

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | January 15, 2026 | Initial release |
| 1.1 | March 12, 2026 | Added Phase 0 foundation section; integrated gamification layer (EMS earning categories, Data Stewardship, badge system cross-references); added three-stage platform arc context; added Community Champion role and ground-truthing provisions; added Benefits-Sensitive Account protections; added data stewardship KPIs; cross-referenced Parameter Tables, Participation Map, and both gamification docs throughout |
| 1.1 (corrected) | March 12, 2026 | Removed fabricated fee split percentages (60/20/15/5); fee allocation is governed by existing smart contract structure and Parameter Tables, not invented here |
| 1.2 | March 13, 2026 | Added cross-references to Parameter Tables Section 4.3 (Fee Revenue Allocation: 30% H4H / 30% Treasury Reserve / 15% Platform Development / 15% Community Programs / 10% Community Projects + 0.55% supplemental treasury reserve on gross volume); updated Appendix C Merchant row accordingly |
| 2.0 | May 4, 2026 | **MAJOR REVISION:** Restructured as community time bank with prepaid stored-value system; separated EMS (time credits, vaulted) from PMS (prepaid value, spendable); replaced variable base-rate model with phase-based treasury triggers; added user-choice framework for Phase 2/3 EMS conversion; clarified treasury mechanics (USDC reserves, Stripe gateway, ATM withdrawal as redemption path); enhanced Benefits-Sensitive Account protections with time banking legal framework; added goods exchange rules (labor-hour vs. market-price tracks); updated all definitions and examples to match deployed smart contract architecture |

---

## 1. Foundation: What Phase 0 Built

Phase 1 does not start from zero. It starts from a tested, red-teamed foundation built during Phase 0 (Invite-Only Beta).

**MountainShares operates as a community time bank with a digital prepaid account system.** Like traditional time banks, MountainShares values **one hour of community service = one hour of community service**, regardless of the type of work performed. All participants exchange time and skill through a shared ledger of recognition hours (EMS time credits), which may later convert to stored value (PMS prepaid balances) usable for local goods and services.

**What Phase 0 produced:**
- A working **time bank recognition ledger** with real UEIs, real EMS time credits, and real geo-tagged activity
- A red-teamed **prepaid stored-value wallet system** (PMS) with documented security findings and remediations
- A cohort of Groundbreaker-rank participants who carry founding badges, founding **time credits**, and governance eligibility into Phase 1
- A Phase 0 Pre-Launch Audit Report that serves as the permanent founding governance record
- A tested Ms. allis system with reserve ratio enforcement, Phase Management Controller integration, and chatbot interface
- Validated data stewardship workflows, including ground-truthing consent processes and initial contact record collection
- Deployed smart contract infrastructure: Backbone Contract, Phase Management Controller, Treasury Monitor, Business Registry, and Stripe Payment Gateway integration

All **time credits (EMS hours)** logged during Phase 0 carry forward permanently. Groundbreaker rank is locked — it cannot be earned after Phase 1 opens. Founding badges are permanent and visible on UEI profiles forever.

Phase 1 inherits everything Phase 0 built and opens it to the community.

---

## 2. Core Economic Principles

**Time Bank Foundation:**
- MountainShares is a **community time bank** where participants exchange hours of service using accumulated time credits (EMS) as the unit of account.
- All time is valued equally: one hour of caregiving = one hour of data stewardship = one hour of cultural preservation = one hour of governance participation.
- Time credits (EMS) are **recognition of service rendered to the community**, not wages, income, or compensation for employment.
- Prepaid stored value (PMS) represents a **digital prepaid account** funded by participant deposits (similar to prepaid debit cards), not a bank account or savings instrument.

**Two Parallel Systems:**

- **Time Bank Recognition Ledger (Unlimited):** All EMS time credits logged on-chain with full UEI, geo, org, and timestamp data. No hard cap; serves as permanent audit trail, rank engine, and identity marker. **These are non-taxable time credits in the community time bank**, not countable income for benefits purposes.

- **Prepaid Stored Value (Capped & Reserve-Backed):** PMS represents **prepaid account balances** that participants can use to purchase goods and services in The Commons or withdraw as cash (subject to fees and limits). PMS is backed 1:1 by USDC reserves held in treasury contracts. Participants load PMS by depositing USD via Stripe Payment Gateway.

**Hard Triggers (Automatic, Non-Negotiable):** Phase Management Controller and Ms. allis enforce automatically; no DAO override possible for safety constraints.

**Two games, one system:** The Commons daily game and the MountainShares contribution game share the same UEI, the same **time bank recognition ledger**, and the same **time credits (EMS)**. Every qualifying Commons activity feeds rank, governance standing, and badge progression in MountainShares automatically.

**Three-stage platform arc:** The Commons grows from a barter/trade and Facebook Marketplace feel (Phase 1 early) through TikTok-style discovery (Phase 1 mature) to an Amazon-style full commerce layer (Phase 2+). Economic safety parameters must support each stage. See [The Commons Gamification](../the%20commons/The%20Commons%20Gamification%3A%20The%20Daily%20Life%20Game.md) Section 2 for the full arc.

---

## 3. Time Credits vs. Prepaid Stored Value: The Two-Ledger System

### 3.1 Understanding the Distinction

MountainShares operates two parallel systems that participants access through a unified interface:

| System | How Acquired | Phase 1 Status | Legal Character | Cash-Out |
|---|---|---|---|---|
| **EMS (Earned MountainShares) — Time Bank Credits** | Logged for verified community service hours (caregiving, learning, land/mapping, cultural preservation, data stewardship, governance, emergency prep, commerce/trade) | **Vaulted and locked** — visible on time bank recognition ledger but not convertible to prepaid value | **Non-taxable time credits in a community time bank** — not wages, not income, not countable assets for benefits purposes | **No** — time credits remain vaulted until Phase 2+ when user opts in to convert |
| **PMS (Personal MountainShares) — Prepaid Stored Value** | Purchased with USD via Stripe Payment Gateway; minted 1:1 at time of deposit | **Spendable immediately** in The Commons | **Prepaid stored-value account balance** (similar to prepaid debit card balance) — not a bank account, not a savings account | **Yes** — via ATM withdrawal with $2.50 fee, 500 PMS daily limit |

### 3.2 Phase 1 Economic Flow (Time Bank Model)

**Time credit earning:**
- User performs 8 hours of verified caregiving → 8 EMS time credits logged to recognition ledger
- **These are reciprocal community service hours, not income**
- Time credits remain vaulted (visible but not spendable) until Phase 2+

**Prepaid account loading:**
- User deposits $100 USD via Stripe Payment Gateway
- Treasury receives ~98 USDC (net of Stripe processing fees)
- User receives 100 PMS **prepaid stored value** (minted 1:1)

**Prepaid spending in The Commons:**
- User spends 50 PMS at Nicholas Pharmacy
- Pharmacy receives 50 PMS in their prepaid account (spendable or withdrawable)
- Transaction fee (1.80%) collected: 0.9 PMS
- Fee split: 30% to Treasury Reserve (0.27 PMS equivalent USDC), 30% to H4H Operations, 15% to Platform Development, 15% to Community Programs, 10% to Community Projects

**Cash-out (ATM withdrawal):**
- User requests $25 cash-out via ATM withdrawal
- 25 PMS deducted from prepaid balance
- $2.50 withdrawal fee deducted
- Treasury pays $22.50 USDC to user's linked bank account
- Phase Management Controller's WITHDRAWALPROCESSORROLE processes transaction
- 500 PMS daily withdrawal limit enforced

**Result:**
- **Time credits (EMS)** accrue on the recognition ledger as non-taxable community service hours
- **Prepaid balances (PMS)** hold stored value in digital prepaid accounts
- Treasury holds USDC reserves backing prepaid balances 1:1
- Time credits do not convert to prepaid value until Phase 2+ when user actively chooses to opt in

### 3.3 Per-User Prepaid Loading Caps (Monthly)

To protect system stability and benefits eligibility, prepaid account loading is capped:

| User Tier | Definition | Monthly PMS Loading Cap | Purpose |
|-----------|-----------|------------------|---------|
| **Tier 1** | General Commons participants | 500 PMS/month | Standard cap for most users |
| **Tier 2** | Verified community roles (caregivers, mutual aid workers, nonprofit staff with org co-sign + geo validation) | 1,000 PMS/month | Higher cap for high-need community roles |

**Tier Assignment Logic:**
- Tier 1 default for all new UEIs
- Tier 2 requires: org co-sign (nonprofit, EMS, mutual aid network) + geo-fence verification + Commons trust signals
- Ms. allis flags tier eligibility; final assignment by DAO governance or pre-agreed rules

**Important:** These caps apply to **loading PMS via USD deposits**, not to earning EMS time credits. Users can log unlimited EMS hours; time credits are vaulted and do not count against prepaid caps.

All current caps are maintained in the [Program Rules – Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md), which is the authoritative live reference for any value that may change through governance.

### 3.4 Benefits-Sensitive Account Protections

Participants receiving means-tested public benefits (SNAP, Medicaid, SSI, WV WORKS, etc.) are protected by default. MountainShares is structured as a **community time bank** to minimize benefits conflicts:

**Time Bank Legal Protections:**
- **Time credits (EMS) are not countable income:** Hours of community service logged to the time bank recognition ledger represent **reciprocal non-monetary exchanges**, similar to traditional time banks where "one hour for one hour" exchanges are non-taxable.
- **Prepaid stored value (PMS) is not a bank account:** PMS balances are held in **prepaid stored-value accounts** (similar to prepaid debit cards), not savings or checking accounts. Participants load funds they already own into the prepaid system.
- **No benefits cliff from time bank participation:** Logging time credits to the recognition ledger does not create countable income or assets under IRS time banking precedent.

**Additional Protections for Benefits-Sensitive Accounts:**
- **Hard prepaid balance cap:** PMS prepaid balance may not exceed a threshold set to protect benefits eligibility (DAO-governed, defaults to conservative level at Phase 1 launch; see [Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md) Section 6)
- **Throttled prepaid loading:** Participants cannot load additional USD into prepaid accounts if balance approaches cap
- **No forced disclosure:** Participation in The Commons does not require disclosure of benefit status; protection is opt-in and participant-controlled
- **Ms. allis proactive notice:** When a Benefits-Sensitive Account participant approaches a threshold, Ms. allis provides a plain-language notice and suggests they consult with a benefits counselor before loading additional funds or converting time credits
- **Time credits remain vaulted by default:** Participants can log unlimited time credits (EMS) without converting to prepaid value (PMS), avoiding any asset-count concerns

**Why Time Bank Structure Protects Benefits:**

Traditional time banks have established legal precedent that **time credit exchanges are non-taxable and non-countable** because:

1. **Reciprocal service, not employment:** Time credits represent community members helping each other, not wages paid by an employer
2. **Equal value per hour:** All service hours are valued the same (1 hour = 1 credit), unlike market-wage bartering where values are negotiated
3. **Community purpose:** Time banks exist to build social capital and community resilience, not generate taxable income
4. **IRS precedent:** Time dollar exchanges have received IRS private letter rulings confirming tax-exempt status

MountainShares extends this model digitally:
- **Time credits (EMS)** log hours of community service with full auditability
- **Prepaid value (PMS)** represents participant-deposited funds in stored-value accounts, not earnings from time credits
- **Phase 2+ conversion** allows participants to **optionally** convert vaulted time credits to prepaid value at appreciation rates — this is when countable income may arise, and participants can choose timing and amount to manage benefits impact

**Bottom line:** Logging time credits and spending prepaid value should not jeopardize benefits eligibility, but participants should consult benefits counselors before converting time credits in Phase 2+.

**Legal Review Before Launch:**
- **Time bank classification:** Legal counsel reviews MountainShares' structure as a community time bank and confirms alignment with IRS private letter ruling precedent on tax-exempt time dollar exchanges.
- **Prepaid account classification:** Legal counsel confirms PMS prepaid accounts are not "bank accounts" or "savings accounts" for benefits eligibility purposes.
- **Benefits counselor partnership:** H4H establishes referral partnerships with WV benefits counselors who can advise participants on MountainShares participation impact.

---

## 4. Treasury Backing & Phase-Based Safety Triggers

### 4.1 Reserve Ratio and Treasury Management

The reserve ratio is calculated as:

```
Reserve Ratio = Treasury USDC Reserve / Total Outstanding Spendable PMS
```

**How the Treasury Builds:**

1. **Purchase/load flows:** Users pay fiat → Stripe Payment Gateway processes → USDC deposited to treasury → PMS minted to user (1:1 USD equivalent)

2. **Fee revenue:** All transaction fees route through the multi-party USDC distribution system per [Parameter Tables Section 4.3](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md):
   - 30% → H4H Operations
   - 30% → Treasury Reserve (primary reserve accumulation mechanism)
   - 15% → Platform Development
   - 15% → Community Programs
   - 10% → Community Projects
   - +0.55% supplemental treasury reserve on gross transaction volume

3. **Phase 1 PMS-only spending:** Users spend PMS in The Commons; EMS remains vaulted. PMS spending circulates prepaid value within the system but does not drain reserves—only **cash-out/ATM withdrawals** reduce treasury USDC.

4. **ATM withdrawal processing:** Phase Management Controller enforces a **$2.50 standard withdrawal fee** and **500 PMS daily withdrawal limits**. Withdrawals are processed by the `WITHDRAWALPROCESSORROLE` and deduct from treasury USDC at the current phase-adjusted rate.

5. **Additional revenue sources:**
   - CLIO NFT heritage revenue (50% creator, 30% platform, 20% treasury)
   - DAO-approved grants or donations
   - Business verification and employee reward vault transaction flows

**What does NOT count as treasury backing:**
- EMS time credits (vaulted recognition, not circulating supply)
- Future promises or pledged donations not yet received
- Speculative asset valuations

**The merchant fee (1.80%)** and the **ATM flat fee ($2.50)** are primary Treasury Reserve-building mechanisms: 30% of each routes directly to the reserve at settlement, and the +0.55% supplemental assessment on gross volume compounds reserve growth independently of fee collection. See [Parameter Tables Section 4.3](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md) for governance floors, adjustability rules, and the full allocation rationale.

### 4.2 Treasury-Triggered Phase Transitions and Safety Bands

The **Phase Management Controller** enforces three economic phases driven by treasury health. Ms. allis monitors the reserve ratio daily and auto-adjusts spending/withdrawal rules.

| Reserve Ratio | Active Phase | EMS Status | PMS Spending | PMS Cash-Out | User Choice | Promo Bonuses |
|---|---|---|---|---|---|---|
| **< 0.75** | Emergency Floor | Vaulted | **Restricted** — daily spending caps reduced to 20-40 PMS/user | **Paused** — ATM withdrawals halted | N/A | Frozen |
| **0.75 – 0.99** | Phase 1 (Conservative) | Vaulted | **Normal** — monthly loading caps enforced (500/1,000 PMS Tier 1/Tier 2) | **Active** — $2.50 fee, 500 PMS daily limit | N/A | Paused when ratio < 1.0 |
| **1.0 – 1.24** | Phase 1 (Healthy) | Vaulted | **Increased caps possible** via DAO vote (up to 750/1,500 PMS max) | **Active** | N/A | Enabled |
| **≥ 1.25** | **Phase 2 Unlocked** | **User choice: cash out OR continue vaulting** | Full circulation | **Active** | **Users choose how much EMS to unlock at 10× appreciation (1 EMS = $10)** | Enabled |
| **≥ 1.50** | **Phase 3 Unlocked** | **User choice at 34.7× appreciation** | Full circulation | **Active** | **Users choose how much EMS to unlock at 34.7× (1 EMS = $34.70)** | Enabled |

**Automatic Trigger Logic (Phase Management Controller enforces):**
- Reserve ratio calculated as `Treasury USDC / Outstanding Spendable PMS`
- EMS time credits are **not counted in the denominator** — they're vaulted recognition, not circulating supply
- Phase transitions happen **automatically when reserve ratio crosses thresholds for 60+ consecutive days** (per Phase 0→1→2 graduation criteria, Section 10.2)
- No DAO vote required for **downward** phase restrictions; they fire immediately if ratio falls
- **Upward** phase unlocks require DAO vote **only if thresholds are manually lowered**; otherwise auto-unlock when ratio sustained

**Phase 2 & 3 User Control:**
- Users are **never forced** to cash out EMS when phases unlock
- Each user **individually decides** how much of their vaulted EMS to convert at the phase-adjusted rate
- Unconverted EMS remains vaulted and continues appreciating if higher phases unlock
- Treasury pays USDC at the phase rate; converted EMS is burned
- Example: User has 100 EMS hours vaulted. Phase 2 unlocks (reserve ratio ≥ 1.25). User chooses to cash out 30 EMS → receives $300 USDC (30 × $10), pays $2.50 withdrawal fee, 70 EMS remain vaulted for potential Phase 3 appreciation.

**Ms. allis daily monitoring:**
- Recalculates reserve ratio every 24 hours
- If ratio crosses a threshold boundary, new phase rules apply at next epoch (24–48 hour notice to all participants)
- No human approval required for *downward* adjustments; they fire automatically
- Publishes next-phase projection and days-until-transition countdown on public dashboard

---

## 5. Monthly Promo & Bonus Pool

### 5.1 Promo Pool Budget
- **Source:** Allocated from Community Programs bucket (15% of fee revenue) per the smart contract structure and [Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md) Section 4.2.
- **Max Size:** 2–3% of monthly processed volume, capped at X PMS/month (DAO sets X per Parameter Tables).
- **Example:** If volume is 100k USD/month, promo pool ≤ 2–3k PMS/month.

### 5.2 Bonus Rules
- All bonuses (e.g., "+50 PMS for visiting Nicholas Pharmacy") draw from the pool.
- Once pool is exhausted in a month, no new bonuses are offered until next cycle.
- **Bonuses are awarded as PMS (prepaid value), not EMS time credits** — they count against monthly loading caps.
- Bonuses pause automatically when reserve ratio < 1.0.
- Quest completion rewards, seasonal campaign bonuses, and streak milestone rewards all draw from this pool.
- Data stewardship verification rewards are funded separately per the smart contract structure — they do not draw from the promo pool.

---

## 6. Time Bank Service Categories

The following categories are recognized as qualifying **time credit (EMS) earning activities** in the MountainShares community time bank. All activities log time credits to the recognition ledger with UEI, geo, org, and timestamp. **One hour of any category = one time credit**, valued equally across all service types. Full earning rules are defined in the [Program Rules](MountainShares%20Program%20Rules(Draft).md).

| Category | Examples | Notes |
|----------|---------|-------|
| **Mutual Aid** | Caregiving, supply donation, transportation, neighbor support | Tier 2 eligible with org co-sign; 1 EMS hr per verified hour |
| **Learning and Teaching** | Workshops, skill sessions, mentoring, learning modules | 1 EMS hr per verified hour |
| **Cultural Preservation** | Clio trail markers, oral history, heritage events, traditions | 1 EMS hr per verified hour |
| **Land and Mapping** | GIS validation, place record submission, parcel verification | 1 EMS hr per verified hour |
| **Data Stewardship** | Ground-truthing, contact collection (with consent), Ms. allis verification ping responses, record updates | EMS awarded per verified activity and per ping response; verification rewards are **funded separately from the promo pool** per the existing smart contract fee structure |
| **Community Events** | Commons-hosted events, volunteer hours, local programs | 1 EMS hr per verified hour |
| **Governance Participation** | DAO votes, proposal review and feedback, governance sessions | 1 EMS hr per session |
| **Emergency Preparedness** | Prep activities during active NOAA alert periods, resilience drills | 1 EMS hr per verified hour; promo bonus when reserve permits |
| **Time Bank Goods Exchange** | Participant-produced items (canned goods, quilts, firewood, baked goods) traded for time credits | **Labor-hour valuation only** — 1 hour of production labor = 1 EMS; recipient pays material costs in USD separately; non-taxable per IRS time banking precedent (see Section 6.1) |
| **Marketplace Commerce** | Buying/selling goods and services at market prices using prepaid value (PMS) | Transactions denominated in PMS (USD equivalent); operates like a local marketplace; **no EMS earned** unless service hours are separately logged |

For the full quest structure, streak system, seasonal campaign design, and badge system tied to these categories, see [The Commons Gamification: The Daily Life Game](../the%20commons/The%20Commons%20Gamification%3A%20The%20Daily%20Life%20Game.md).

### 6.1 Goods Exchanges in the Time Bank

MountainShares time bank members may exchange **participant-produced goods** for time credits under the following conditions, aligned with IRS private letter ruling guidance:

**1. Labor-Hour Valuation Only**
- Goods are valued by the **hours of labor invested to create them**, not market price
- Example: "I spent 2 hours making this quilt" = 2 time credits
- Counter-example (not allowed): "This quilt would sell for $200 at the craft fair" = 200 time credits ❌

**2. Material Costs Paid Separately**
- If goods required purchased materials (fabric, jars, seeds, etc.), the **recipient pays the producer in USD for material costs only**
- Time credits cover **labor only**
- Example: Producer logs 1 EMS hour for canning pickles; recipient pays $2 USD cash for vinegar/salt/jar costs

**3. Participant-Produced Goods Preferred**
- Goods should be **made/grown/harvested by the participant** (homemade bread, garden vegetables, hand-sewn items, home repairs using participant's labor)
- Reselling store-bought goods is **not a qualifying time bank exchange**

**4. No Market-Value Haggling**
- Participants **do not negotiate market value** — they document labor hours invested
- "One hour equals one time credit" principle applies to goods just as it does to services

**5. Documentation Required**
- Goods exchanges log to Ms. allis with: producer UEI, recipient UEI, item description, **documented labor hours**, material cost (if any), timestamp
- Example entry: "Sarah logged 1 EMS hour — canned 3 jars of pickles (1 hour labor); traded to John for 1 time credit; John paid $1.50 USD material cost"

**Common Goods Exchange Examples:**

| Item | Labor Hours | Material Cost | Time Credits Earned | Cash Payment |
|---|---|---|---|---|
| 1 jar homemade pickles | 1 hour (growing, harvesting, canning) | $2 (vinegar, salt, jar) | 1 EMS | Recipient pays $2 USD to producer |
| Hand-sewn quilt | 20 hours (cutting, sewing, quilting) | $40 (fabric, batting, thread) | 20 EMS | Recipient pays $40 USD to producer |
| Firewood (1 cord) | 4 hours (cutting, splitting, stacking) | $0 (from participant's land) | 4 EMS | No cash payment |
| Baked bread (2 loaves) | 1 hour (mixing, kneading, baking) | $3 (flour, yeast) | 1 EMS | Recipient pays $3 USD to producer |

**What This Means for Benefits-Sensitive Accounts:**
- Trading participant-produced goods for time credits (EMS) remains **non-taxable** under IRS time banking precedent
- Cash payments for materials are **reimbursements, not income** — recipient is paying the actual cost the producer incurred
- Time credits earned from goods exchanges remain vaulted (non-countable) until participant opts to convert to prepaid value (PMS) in Phase 2+

---

## 7. Data Stewardship and Ground Truthing

Data accuracy is a core commons value and a recognized time credit-earning activity. Rural data decays fast — businesses close, phone numbers change, services disappear. The Commons maintains a living, verified data layer through community participation.

### 7.1 Ground Truthing Workflow

1. Community Champions (and eligible participants) collect contact information — email and SMS — for local places, businesses, organizations, and services.
2. **Explicit opt-in consent** is required and documented at collection time (collector UEI, collection date, consent method, contact type).
3. Ms. allis runs automated verification pings every **6–12 months** to each consenting record holder.
4. When the record holder **responds and confirms or updates** their data, they earn EMS time credits. The record is marked verified with a new timestamp and confidence score.
5. Verification rewards are funded per the existing smart contract structure, separate from the promo pool.

### 7.2 Community Champion Role in Data Stewardship

Community Champions are the primary ground-truthing force in Phase 1 early. Their role is **fluid by design** — it evolves as the program matures:

| Phase | Primary Champion Focus |
|-------|----------------------|
| Phase 0 | Red-team security, governance document review |
| Phase 1 (early) | Ground truthing — contact collection, place record verification |
| Phase 1 (mature) | Community anchoring, onboarding, quest coordination |
| Phase 2+ | Governance leadership, regional stewardship, data quality oversight |

Champion responsibilities in any given period are defined through governance. EMS time credits are earned for the current phase focus; the recognition ledger preserves the full history.

### 7.3 Data Stewardship KPIs

Ms. allis tracks and publishes the following data quality indicators as part of the weekly network snapshot:

- % of active place records verified within the last 12 months
- Response rate to Ms. allis verification pings (rolling 6-month)
- Total records collected, verified, and updated in current period
- Number of active participants with Data Keeper or Living Map badges

Full KPI definitions are in the [KPI Specification](MountainShares%20KPI%20Specification.md).

---

## 8. DAO Authority: What Can Change & How

### 8.1 DAO Can Vote To Change (Requires Super-Majority, e.g., 66%+)

✅ **Prepaid loading caps** (500/1,000 → 750/1,500 PMS/mo Tier 1/Tier 2), *only if reserve ratio supports it*  
✅ **Tier assignment criteria** (e.g., add new community roles as Tier 2)  
✅ **Promo pool budget** (increase X PMS/month), *only if backing assets support it*  
✅ **Phase transition thresholds** (move 1.25 to 1.20, etc.), *only once system is stable + audited*  
✅ **Quest categories, seasonal campaigns, badge criteria**, *within reserve-ratio safety bands*  
✅ **Champion role scope and focus per phase**, *through standard proposal lifecycle*  
✅ **Fee revenue allocation percentages** ([Parameter Tables Section 4.3](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md)), *subject to governance floors of 20% minimum for Treasury Reserve and 20% minimum for H4H Operations; requires 66% super-majority + Board ratification*  
✅ **Benefits-Sensitive Account balance caps**, *subject to legal review + 66% super-majority*

### 8.2 DAO Cannot Override (Hard Trigger Rules)

❌ Vote to mint PMS without 1:1 USDC reserve backing  
❌ Disable automatic phase restrictions when reserve ratio drops below threshold  
❌ Force users to convert vaulted EMS time credits to PMS prepaid value  
❌ Override Benefits-Sensitive Account protections without supermajority + legal review  
❌ Overrule legal / safety prohibitions (drugs, weapons, exploitation, etc.)  
❌ Remove consent requirements from data stewardship workflows  
❌ Alter smart-contracted fee rates outside the governance process defined in the Parameter Tables  
❌ Reduce Treasury Reserve allocation below 20% or H4H Operations below 20% (governance floors per [Parameter Tables Section 4.3.3](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md))  
❌ Bypass Phase Management Controller withdrawal limits or emergency pause mechanisms

### 8.3 Ms. allis & Phase Management Controller Authority (Automatic, No Vote Needed)

✅ Enforce reserve ratio checks every 24 hours; apply auto-phase-adjustments if thresholds crossed  
✅ Flag and freeze accounts tied to illegal content or high-risk patterns  
✅ Calculate and publish daily reserve ratio, backing assets, outstanding PMS, and next-phase projection  
✅ Tier assignments based on pre-agreed rules (org co-sign + geo verification)  
✅ Pause bonuses when reserve ratio < 1.0  
✅ Run data stewardship verification pings every 6–12 months; award EMS for verified responses  
✅ Maintain data confidence scores on all place records  
✅ Surface plain-language notices to Benefits-Sensitive Account holders approaching thresholds  
✅ Surface badge progress, quest availability, and streak status through the Commons app  
✅ Process ATM withdrawals via WITHDRAWALPROCESSORROLE (enforce $2.50 fee, 500 PMS daily limit)  
✅ Enforce Phase 1 PMS-only spending rules (EMS vaulting); unlock Phase 2/3 user-choice conversion when reserve thresholds met

---

## 9. One UEI = One Vote

- **Governance Token:** Each UEI receives 1 equal vote on all DAO proposals.
- **Voting Rights:** After 30 days on-platform (anti-sybil) and minimum 10 EMS time credits logged (Bronze rank threshold).
- **Vote Scope:** All items in Section 8.1 (increases/policy changes); cannot vote on Section 8.2 (hard triggers) or illegal activity rules.
- **Rank does not change vote weight.** A Champion and a Bronze participant each get one vote.

---

## 10. Phase 0 → Phase 1 → Phase 2 Graduation Criteria

### 10.1 Phase 0 → Phase 1 (Already Completed Before This Document)

Phase 0 graduated to Phase 1 when the Pre-Launch Audit Report was finalized, all critical and high security findings were remediated, and founding governance documents were approved by the founding cohort.

### 10.2 Phase 1 → Phase 2 Graduation Criteria

**Transition to Phase 2 only when ALL of the following hold for 60+ consecutive days:**

- Reserve ratio stable ≥ 1.25 (no dips below threshold)
- Monthly processed volume ≥ 200k USD (realistic merchant/load flow)
- Active UEIs ≥ 2,000 (meaningful community adoption)
- Zero systemic fraud or reserve-threatening exploits
- DAO governance participation ≥ 30% quorum on key votes
- Data stewardship layer active: ≥ 500 verified place records with ≥ 60% verified in last 12 months
- Benefits-Sensitive Account protections reviewed by legal counsel and confirmed compliant

**Phase 2 Changes:**

- **EMS unlocking**: Each user with vaulted EMS time credits receives a one-time opt-in prompt when Phase 2 activates. Users choose:
  - **Cash out now** at 10× appreciation (1 EMS = $10 USD equivalent)
  - **Continue vaulting** for potential Phase 3 appreciation (34.7×)
  - **Partial conversion** — cash out X EMS hours, leave the rest vaulted

- **No forced conversion**: Phase 2 unlocking does **not** automatically convert all EMS to spendable PMS or force withdrawals

- **Treasury impact**: Only EMS that users **actively choose to convert** is paid out from treasury USDC reserves. Vaulted EMS remains off-balance-sheet recognition.

- **Prepaid loading caps**: Tier caps can rise further via DAO vote (e.g., 750/1,500 → 1,000/2,000 PMS/mo)

- **Platform arc progression**: Stage 2 (Discovery/TikTok-feel) and Stage 3 (Full Commerce/Amazon-style) features unlock

- **Statewide rollout planning** begins

### 10.3 Phase 2 → Phase 3 Graduation Criteria

**Transition to Phase 3 only when ALL of the following hold for 60+ consecutive days:**

- Reserve ratio stable ≥ 1.50 (no dips below threshold)
- Monthly processed volume ≥ 500k USD
- Active UEIs ≥ 5,000
- Phase 2 EMS conversion opt-in rate ≥ 20% (demonstrates user understanding and adoption)
- Zero systemic fraud or reserve-threatening exploits
- DAO governance participation ≥ 40% quorum on key votes

**Phase 3 Changes:**
- **EMS appreciation jumps to 34.7×** (1 EMS = $34.70 USD equivalent)
- Users with remaining vaulted EMS receive new opt-in prompt for Phase 3 conversion
- Stage 3 platform features (Full Commerce/Amazon-style) fully activated
- Regional expansion beyond West Virginia pilot may begin

---

## 11. Safety Prohibitions (Hard-Coded, No Vote)

**Banned Content / Activity Categories:**

| Category | Prohibition | Detection | Consequence |
|----------|-----------|-----------|------------|
| **Illegal Drugs** | Cannot buy/sell/promote illegal drugs or paraphernalia | Content filter + pattern matching + keyword flagging | Account freeze + report to authorities (if required) |
| **Weapons** | Cannot facilitate illegal weapons transfers or trafficking | Content filter + geo + pattern | Account freeze + report |
| **Exploitation** | No sexually explicit content, porn, child abuse material, or coerced sex work | NLP + imagery scanning + manual review | Immediate permanent ban |
| **Fraud/Forgery** | No fake documents, false UEI claims, or spoofed org identities | UEI registry verification + geo cross-check | Account freeze + investigation |
| **Data Theft** | No unauthorized collection, export, or misuse of contact data or place records | Audit log anomaly detection | Account freeze + data remediation |
| **Benefits Fraud** | No misrepresentation of benefits status to manipulate account tier, cap, or throttle protections | Cross-check + manual review trigger | Account freeze + investigation |

**Enforcement:**
- Ms. allis auto-flags and freezes.
- Human review within 24–48 hours.
- Clear appeals process for false positives.
- Transparent logging (anonymized) of all freezes/bans.

---

## 12. Transparency & Dashboards (Ms. allis Public API)

Every UEI can see (updated daily):

**Personal:**
- **Time credits logged** (EMS hours in time bank recognition ledger), **prepaid balance** (PMS in stored-value account), monthly loading budget remaining, tier status
- Current rank, time credits to next rank, active badges and badges in progress
- Data stewardship record count and verification ping history
- Benefits-Sensitive Account status and prepaid balance threshold proximity (private, participant-only)

**Network:**
- Current reserve ratio, treasury USDC backing, total outstanding PMS, next phase projection and days-until-transition countdown
- Data stewardship KPIs: % records verified in last 12 months, ping response rate
- Active participant count, monthly EMS time credits logged, monthly PMS minted and spent
- Phase status: current phase, reserve ratio trend (7/30/90-day), phase unlock criteria progress

**DAO:**
- Current proposals, vote status, outcome history, policy changelog
- Champion role scope for current phase
- [Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md) current values and last-changed date

**Purpose:** Make "should we vote to raise caps?" a decision based on visible data, not trust.

---

## 13. Audit & Governance Cadence

- **Daily:** Ms. allis publishes reserve ratio, auto-applies phase-triggered adjustments, runs data confidence scoring
- **Weekly:** Network snapshot (active users, volume, PMS minted/spent, promo spend, data stewardship KPIs, phase status)
- **Monthly:** Full treasury audit (USDC reserves, PMS supply, reserve ratio verification), DAO governance session (proposals + votes)
- **Quarterly:** External audit by independent WV nonprofit (if funds permit); Champion role scope review through governance
- **Every 6–12 months:** Ms. allis verification ping cycle for all consenting place records

---

## 14. Sunset & Emergency Powers

### 14.1 If Reserve Ratio Falls Below 0.5 (Critical)
- Phase Management Controller automatically pauses all PMS minting and ATM withdrawals
- Only USD loads via Stripe accepted (rebuilds treasury)
- Data stewardship verification ping cycles continue — funded separately from main reserve
- Emergency governance session called within 48 hours
- Options: (a) shut down gracefully and return remaining reserves to users pro-rata, (b) seek external funding, (c) reset with community consent

### 14.2 If Ms. allis Detects Coordinated Fraud or Attack
- Affected accounts frozen pending review
- Daily public reporting of incident (anonymized)
- Emergency DAO vote on remediation (clawback, reset, shutdown)
- Contact data and place records locked from export during active incident
- Phase Management Controller may pause withdrawals if attack threatens treasury

### 14.3 If Data Stewardship Breach Occurs
- Contact data collection paused immediately
- Affected record holders notified per Privacy Policy obligations
- Incident logged publicly (anonymized)
- Data stewardship verification paused until breach is remediated and reviewed

---

## Appendix A: Definitions

- **UEI:** Unique Entity Identifier (per user, including individuals and orgs)

- **EMS (Earned MountainShares) — Time Bank Credits:** Hours of community service logged to the MountainShares time bank recognition ledger. Represent reciprocal non-monetary exchanges where one hour of service = one time credit, regardless of service type. **Non-taxable per IRS time banking precedent** — not wages, not income, not countable assets for benefits purposes. Vaulted in Phase 1 (visible but not convertible to prepaid value). Unlock for user-choice conversion in Phase 2+ at appreciation multipliers (10× Phase 2, 34.7× Phase 3). Do not count toward reserve ratio until user opts to convert.

**Result:** Users maintain full control over timing and amount of EMS conversion. Treasury only pays out USDC for EMS that users actively choose to convert. Vaulted EMS continues appreciating if Phase 3 unlocks. Benefits-sensitive participants can defer conversion or convert in small amounts to manage eligibility impact.

---

## Appendix C: Participation Roles Cross-Reference

For a complete map of who participates in The Commons and MountainShares, what documents govern them, what they do, what they receive, and what they are not — see the [Participation Map](../the%20commons/Participation%20Map.md).

Key roles relevant to this specification:

| Role | Economic Safety Relevance |
|------|--------------------------|
| **Commons User** | Subject to prepaid loading caps (Tier 1: 500 PMS/mo, Tier 2: 1,000 PMS/mo); earns unlimited time credits (EMS) at 1 hour = 1 credit; Benefits-Sensitive Account protections available via opt-in |
| **Phase 0 Participant** | Founding EMS time credits and badges carry forward; Groundbreaker rank permanent; time credits remain vaulted until Phase 2+ user-choice conversion |
| **Community Champion** | Primary ground-truthing and data stewardship force in Phase 1 early; role evolves through governance per Section 7.2; earns EMS time credits for current phase focus |
| **Safety Champion** | Ongoing post-Phase 0 safety review; feeds into quarterly audit cycle; monitors Phase Management Controller enforcement and emergency pause scenarios |
| **Merchant** | Pays 1.80% transaction fee per [Parameter Tables Section 4.1](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md); 30% of that fee routes to Treasury Reserve at settlement per fee revenue allocation ([Parameter Tables Section 4.3](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md)); merchant fees are a primary reserve-building mechanism. Receives PMS in prepaid account (spendable or withdrawable via ATM). |
| **Ms. allis** | Enforces all hard triggers; runs verification pings every 6–12 months; maintains reserve ratio calculations and confidence scores; surfaces Benefits-Sensitive Account threshold notices; publishes phase unlock countdown and next-phase projections |
| **Phase Management Controller** | Smart contract enforcing phase-based rules: PMS-only spending in Phase 1, ATM withdrawal processing via WITHDRAWALPROCESSORROLE ($2.50 fee, 500 PMS daily limit), automatic phase unlock when reserve thresholds met for 60+ days, emergency pause mechanisms |
| **Stripe Payment Gateway** | Fiat-to-crypto onramp; processes USD deposits → USDC to treasury → PMS minted 1:1 to user prepaid account |

---

*"People earn what they do. The commons holds what we decide together. Ms. allis watches so nobody can wreck it."*

---

**End of MountainShares Phase 1: Economic Safety Specification v2.0**
