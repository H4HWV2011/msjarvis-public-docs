
This ratio governs whether buying-power expansion is permitted to activate at all. It is the primary top-of-dashboard metric in the KPI Specification v3.0. No conversion gate may open unless this ratio satisfies the applicable threshold and all formation/transition fees have been paid.

| Gate | Threshold | Additional Condition |
|---|---|---|
| Phase 2 buying-power expansion | ≥ **300%** | All Treasury Reserve-funded formation and transition fees fully paid |
| Phase 3 buying-power expansion | ≥ **500%** | Phase 2 conditions satisfied and sustained for 2+ consecutive quarters |
| Reversion to Phase 2 parameters | < **500%** | Automatic; no vote required |
| Reversion to Phase 1 parameters | < **300%** | Automatic; no vote required |

**How the Treasury Builds:**

1. **Purchase/load flows:** Users pay fiat → Stripe processes → USDC deposited to treasury → PMS minted to user (1:1)
2. **Fee revenue:** All transaction fees route per Parameter Tables Section 4.3:
   - 30% → H4H Operations
   - 30% → Treasury Reserve
   - 15% → Platform Development
   - 15% → Community Connectivity – Operations
   - 10% → Community Connectivity – Infrastructure
   - +0.55% supplemental treasury reserve on gross transaction volume
3. **Phase 1 PMS-only spending:** Only ATM withdrawals drain treasury USDC; internal spending recirculates
4. **ATM withdrawal processing:** $1.25 standard withdrawal fee; 500 PMS daily limit; processed by WITHDRAWALPROCESSORROLE under the DUNA's licensed rails
5. **Additional revenue:** CLIO NFT heritage revenue (50% creator / 30% platform / 20% treasury), DAO-approved grants, business verification flows

**What does NOT count as treasury backing:**
- EMS time credits (vaulted recognition, not circulating supply)
- Future promises or pledged donations not yet received
- Speculative asset valuations

### 4.2 Operational Phase Transitions and Safety Bands (Phase 1)

The Phase Management Controller enforces operational economic phases driven by the Operational Reserve Ratio. These bands govern continuity of service during Phase 1 and do not activate buying-power expansion — that is governed exclusively by the Treasury Reserve Solvency Ratio in Section 4.1 above.

| Operational Reserve Ratio | Active Band | EMS Status | PMS Spending | PMS Cash-Out | Promo Bonuses |
|---|---|---|---|---|---|
| **< 0.75** | Emergency Floor | Vaulted | **Restricted** — daily caps reduced to 20–40 PMS/user | **Paused** | Frozen |
| **0.75 – 0.99** | Phase 1 (Conservative) | Vaulted | Normal — monthly loading caps enforced | Active — $1.25 fee, 500 PMS daily limit | Paused |
| **1.0 – 1.24** | Phase 1 (Healthy) | Vaulted | Increased caps possible via DAO vote (max 750/1,500 PMS) | Active | Enabled |
| **≥ 1.25 sustained** | Phase 2 transition candidate | Per Treasury Reserve Solvency Ratio — see Section 4.1 | Full circulation | Active | Enabled |
| **≥ 1.50 sustained** | Phase 3 transition candidate | Per Treasury Reserve Solvency Ratio — see Section 4.1 | Full circulation | Active | Enabled |

> **Critical Distinction:** Reaching an operational reserve ratio of 1.25 or 1.50 does **not** itself activate EMS buying-power expansion. Activation requires the Treasury Reserve Solvency Ratio (Reserve ÷ Total EMS + M$) to meet the 300% or 500% threshold respectively, with all formation fees paid. The two metrics are separate and both must be satisfied.

**Automatic Trigger Logic:**
- Operational reserve ratio calculated as `Treasury USDC / Outstanding Spendable PMS`
- EMS time credits are **not counted in the denominator** — they are vaulted recognition
- Downward phase restrictions fire immediately when ratio drops; no DAO vote required
- Upward phase unlocks for operational bands auto-apply when ratio sustained for 60+ consecutive days
- EMS buying-power expansion activation follows the separate Treasury Reserve Solvency process

**Phase 2 & 3 User Control (when applicable thresholds are eventually met):**
- Users are **never forced** to cash out EMS
- Each user individually decides how much vaulted EMS to convert at the phase-adjusted rate
- Unconverted EMS remains vaulted
- Treasury pays USDC at the phase rate; converted EMS is burned
- Example: User has 100 EMS vaulted. Treasury Reserve Solvency Ratio reaches 300% and all fees are paid (Phase 2 gate opens). User chooses to convert 30 EMS → receives $300 USDC equivalent (30 × $10), pays the $1.25 withdrawal fee, 70 EMS remain vaulted for potential Phase 3 conversion.

**Ms. Allis daily monitoring:**
- Recalculates both reserve metrics every 24 hours
- If either metric crosses a threshold boundary, new rules apply at next epoch (24–48 hour notice)
- No human approval required for downward adjustments; they fire automatically
- Publishes reserve solvency ratio prominently on dashboard with green/amber/red bands

---

## 5. Monthly Promo & Bonus Pool

### 5.1 Promo Pool Budget
- **Source:** Allocated from fee revenue and treasury per Parameter Tables Section 4.2 (the promo pool is a separate allocation and is no longer drawn from the former Community Programs bucket, which is now dedicated to Community Connectivity).
- **Max Size:** 2–3% of monthly processed volume, capped at X PMS/month (DAO sets X per Parameter Tables).
- **Example:** If volume is 100k USD/month, promo pool ≤ 2–3k PMS/month.

### 5.2 Bonus Rules
- All bonuses draw from the pool.
- Once pool is exhausted in a month, no new bonuses are offered until next cycle.
- Bonuses are awarded as PMS (prepaid value), not EMS time credits — they count against monthly loading caps.
- Bonuses pause automatically when operational reserve ratio < 1.0.
- Quest completion rewards, seasonal campaign bonuses, and streak milestone rewards all draw from this pool.
- Data stewardship verification rewards are funded separately per the smart contract structure.

---

## 6. Time Bank Service Categories

All categories log time credits to the recognition ledger at stable baseline value. One hour of any category = one time credit. No Phase 1 EMS balance carries a vested conversion right.

| Category | Examples | Notes |
|---|---|---|
| **Mutual Aid** | Caregiving, supply donation, transportation, neighbor support | Tier 2 eligible with org co-sign; 1 EMS hr per verified hour |
| **Learning and Teaching** | Workshops, skill sessions, mentoring, learning modules | 1 EMS hr per verified hour |
| **Cultural Preservation** | Clio trail markers, oral history, heritage events, traditions | 1 EMS hr per verified hour |
| **Land and Mapping** | GIS validation, place record submission, parcel verification | 1 EMS hr per verified hour |
| **Data Stewardship** | Ground-truthing, contact collection (with consent), Ms. Allis verification ping responses, record updates | EMS awarded per verified activity; verification rewards funded separately from promo pool |
| **Community Connectivity** | Siting, deploying, maintaining, and monitoring free public internet nodes (Wi-Fi and LoRa mesh) | 1 EMS hr per verified hour; node operations funded by fee-allocation Bucket 4 |
| **Community Events** | Commons-hosted events, volunteer hours, local programs | 1 EMS hr per verified hour |
| **Governance Participation** | DAO votes, proposal review and feedback, governance sessions | 1 EMS hr per session |
| **Emergency Preparedness** | Prep activities during active NOAA alert periods, resilience drills | 1 EMS hr per verified hour; promo bonus when reserve permits |
| **Time Bank Goods Exchange** | Participant-produced items traded for time credits | **Labor-hour valuation only** — 1 hour of production labor = 1 EMS; material costs paid separately in USD; time-banking tax treatment under counsel review |
| **Marketplace Commerce** | Buying/selling goods and services at market prices using PMS | Transactions in PMS; no EMS earned unless service hours logged separately |

### 6.1 Goods Exchanges in the Time Bank

**1. Labor-Hour Valuation Only**
Goods are valued by hours of labor invested to create them, not market price. Example: 2 hours making a quilt = 2 time credits.

**2. Material Costs Paid Separately**
Recipients pay producers in USD for material costs only; time credits cover labor only.

**3. Participant-Produced Goods Preferred**
Goods must be made/grown/harvested by the participant. Reselling store-bought goods is not a qualifying time bank exchange.

**4. No Market-Value Haggling**
Participants document labor hours, not negotiate market value.

**5. Documentation Required**
All goods exchanges log to Ms. Allis with: producer UEI, recipient UEI, item description, documented labor hours, material cost if any, timestamp. The time-banking tax treatment of these exchanges is under counsel review.

| Item | Labor Hours | Material Cost | Time Credits Earned | Cash Payment |
|---|---|---|---|---|
| 1 jar homemade pickles | 1 hour | $2 | 1 EMS | Recipient pays $2 USD |
| Hand-sewn quilt | 20 hours | $40 | 20 EMS | Recipient pays $40 USD |
| Firewood (1 cord) | 4 hours | $0 | 4 EMS | None |
| Baked bread (2 loaves) | 1 hour | $3 | 1 EMS | Recipient pays $3 USD |

---

## 7. Data Stewardship and Ground Truthing

### 7.1 Ground Truthing Workflow

1. Community Champions collect contact information for local places, businesses, organizations, and services with explicit opt-in consent documented at collection time.
2. Ms. Allis runs automated verification pings every 6–12 months to each consenting record holder.
3. When the record holder responds and confirms or updates their data, they earn EMS time credits at stable baseline value.
4. Verification rewards are funded per the existing smart contract structure, separate from the promo pool.

### 7.2 Community Champion Role in Data Stewardship

| Phase | Primary Champion Focus |
|---|---|
| Phase 0 | Red-team security, governance document review |
| Phase 1 (early) | Ground truthing — contact collection, place record verification |
| Phase 1 (mature) | Community anchoring, onboarding, quest coordination, connectivity node stewardship |
| Phase 2+ | Governance leadership, regional stewardship, data quality oversight |

### 7.3 Data Stewardship KPIs

Ms. Allis tracks and publishes:
- % of active place records verified within the last 12 months
- Response rate to Ms. Allis verification pings (rolling 6-month)
- Total records collected, verified, and updated in current period
- Number of active participants with Data Keeper or Living Map badges

---

## 8. DAO Authority: What Can Change & How

### 8.1 DAO Can Vote To Change (Requires Super-Majority, 66%+)

- Prepaid loading caps (500/1,000 → 750/1,500 PMS/mo Tier 1/Tier 2), only if reserve ratio supports it
- Tier assignment criteria
- Promo pool budget, only if backing assets support it
- Operational phase transition thresholds, only once system is stable and audited
- Quest categories, seasonal campaigns, badge criteria, within reserve-ratio safety bands
- Champion role scope and focus per phase, through standard proposal lifecycle
- Fee revenue allocation percentages, subject to governance floors of 20% minimum for Treasury Reserve and 20% minimum for H4H Operations; requires 66% super-majority + Board ratification
- Benefits-Sensitive Account balance caps, subject to legal review + 66% super-majority
- **Treasury Reserve Solvency thresholds (300% Phase 2 / 500% Phase 3) require DUNA governance approval through formal proposal and quorum-verified vote; any proposed reduction requires additional legal review**

### 8.2 DAO Cannot Override (Hard Trigger Rules)

- Vote to mint PMS without 1:1 USDC reserve backing
- Disable automatic phase restrictions when operational reserve ratio drops below threshold
- Force users to convert vaulted EMS time credits to PMS prepaid value
- Override Benefits-Sensitive Account protections without supermajority + legal review
- Overrule legal / safety prohibitions (drugs, weapons, exploitation, etc.)
- Remove consent requirements from data stewardship workflows
- Alter smart-contracted fee rates outside the governance process defined in the Parameter Tables
- Reduce Treasury Reserve allocation below 20% or H4H Operations below 20%
- Bypass Phase Management Controller withdrawal limits or emergency pause mechanisms
- Activate EMS buying-power expansion before Treasury Reserve Solvency Ratio meets applicable threshold with all formation fees paid
- Divert Bucket 4/5 connectivity funds to private benefit, or meter or paywall a free public internet node

### 8.3 Ms. Allis & Phase Management Controller Authority (Automatic, No Vote Needed)

- Enforce reserve ratio checks every 24 hours; apply auto-phase-adjustments if thresholds crossed
- Calculate and publish daily operational reserve ratio and Treasury Reserve Solvency Ratio; display both with green/amber/red bands
- Flag and freeze accounts tied to illegal content or high-risk patterns
- Tier assignments based on pre-agreed rules (org co-sign + geo verification)
- Pause bonuses when operational reserve ratio < 1.0
- Run data stewardship verification pings every 6–12 months; award EMS for verified responses
- Surface plain-language notices to Benefits-Sensitive Account holders approaching thresholds
- Confirm EMS buying-power expansion gates are inactive in Phase 1 and surface reversion status if applicable
- Process ATM withdrawals via WITHDRAWALPROCESSORROLE under the DUNA's licensed rails (enforce $1.25 fee, 500 PMS daily limit)
- Enforce Phase 1 PMS-only spending rules (EMS vaulting); unlock Phase 2/3 user-choice conversion only when both operational and solvency thresholds are met

---

## 9. One UEI = One Vote

- **Governance Token:** Each UEI receives 1 equal vote on all DAO proposals.
- **Voting Rights:** After 30 days on-platform (anti-sybil) and minimum 10 EMS time credits logged (Bronze rank threshold).
- **Vote Scope:** All items in Section 8.1; cannot vote on Section 8.2 (hard triggers) or illegal activity rules.
- **Rank does not change vote weight.**

---

## 10. Phase 0 → Phase 1 → Phase 2 Graduation Criteria

### 10.1 Phase 0 → Phase 1 (Already Completed Before This Document)

Phase 0 graduated to Phase 1 when the Pre-Launch Audit Report was finalized, all critical and high security findings were remediated, Treasury Reserve solvency gating logic was validated, and founding governance documents were approved by the founding cohort.

### 10.2 Phase 1 → Phase 2 Graduation Criteria

**Transition to Phase 2 only when ALL of the following hold:**

- Operational reserve ratio stable ≥ 1.25 for 60+ consecutive days (no dips below threshold)
- **Treasury Reserve Solvency Ratio ≥ 300% of total EMS + M$ outstanding for 2+ consecutive quarters**
- **All Treasury Reserve-funded formation and transition fees (including KTS formation, DUNA structuring, money-services licensure and capitalization, legal counsel) fully paid from the reserve**
- Monthly processed volume ≥ 200k USD
- Active UEIs ≥ 2,000
- Zero systemic fraud or reserve-threatening exploits
- DAO governance participation ≥ 30% quorum on key votes
- Data stewardship layer active: ≥ 500 verified place records with ≥ 60% verified in last 12 months
- Benefits-Sensitive Account protections under benefits-counsel review (confirmation pending)
- Conflict-of-interest recusal documentation on file for all related-party approvals

**Phase 2 Changes (contingent on threshold conditions above being met):**

- **EMS unlocking:** Each user with vaulted EMS time credits receives a one-time opt-in prompt when Phase 2 activates. Users choose:
  - **Cash out now** at the Phase 2 rate (1 EMS = $10 USD equivalent)
  - **Continue vaulting** for potential Phase 3 conversion at the Independent Sector / Do Good Institute Value of Volunteer Time (BLS-derived) in effect on the Phase 3 activation date
  - **Partial conversion** — cash out X EMS hours, leave the rest vaulted
- **No forced conversion:** Phase 2 unlocking does not automatically convert all EMS to spendable PMS
- **Treasury impact:** Only EMS that users actively choose to convert is paid out from treasury USDC reserves
- **Reversion protection:** If the Treasury Reserve Solvency Ratio falls below 300% after Phase 2 activates, the system automatically reverts to Phase 1 parameters; no resident loses their principal EMS balance

### 10.3 Phase 2 → Phase 3 Graduation Criteria

**Transition to Phase 3 only when ALL of the following hold:**

- Operational reserve ratio stable ≥ 1.50 for 60+ consecutive days
- **Treasury Reserve Solvency Ratio ≥ 500% of total EMS + M$ outstanding for 2+ consecutive quarters**
- Monthly processed volume ≥ 500k USD
- Active UEIs ≥ 5,000
- Phase 2 EMS conversion opt-in rate ≥ 20%
- Zero systemic fraud or reserve-threatening exploits
- DAO governance participation ≥ 40% quorum on key votes

**Phase 3 Changes (contingent on threshold conditions above):**
- EMS buying-power advances to the Independent Sector / Do Good Institute Value of Volunteer Time (BLS-derived, not a federal or IRS rate) in effect on the Phase 3 activation date (1 EMS = the FVSR; 2026: $36.14)
- Users with remaining vaulted EMS receive a new opt-in prompt
- **Reversion protection:** If Treasury Reserve Solvency Ratio falls below 500%, system automatically reverts to Phase 2 parameters; if it falls below 300%, system reverts to Phase 1 parameters

---

## 11. Safety Prohibitions (Hard-Coded, No Vote)

| Category | Prohibition | Detection | Consequence |
|---|---|---|---|
| **Illegal Drugs** | Cannot buy/sell/promote illegal drugs or paraphernalia | Content filter + pattern matching + keyword flagging | Account freeze + report to authorities |
| **Weapons** | Cannot facilitate illegal weapons transfers or trafficking | Content filter + geo + pattern | Account freeze + report |
| **Exploitation** | No sexually explicit content, child abuse material, or coerced sex work | NLP + imagery scanning + manual review | Immediate permanent ban |
| **Fraud/Forgery** | No fake documents, false UEI claims, or spoofed org identities | UEI registry verification + geo cross-check | Account freeze + investigation |
| **Data Theft** | No unauthorized collection, export, or misuse of contact data or place records | Audit log anomaly detection | Account freeze + data remediation |
| **Benefits Fraud** | No misrepresentation of benefits status to manipulate account tier, cap, or protections | Cross-check + manual review trigger | Account freeze + investigation |
| **Connectivity Misuse** | No diversion of Bucket 4/5 connectivity funds to private benefit, and no metering or paywalling of free public internet nodes | Public spend ledger + node audit | Critical finding; immediate resolution required |
| **Structural Boundary Breach** | No mechanism that creates founder equity through H4H or community EMS | Audit + legal review | Critical finding; immediate resolution required |

---

## 12. Transparency & Dashboards (Ms. Allis Public API)

Every UEI can see (updated daily):

**Personal:**
- Time credits logged (EMS hours), prepaid balance (PMS), monthly loading budget remaining, tier status
- Current rank, time credits to next rank, active badges and badges in progress
- Data stewardship record count and verification ping history
- Benefits-Sensitive Account status and prepaid balance threshold proximity (private, participant-only)

**Network:**
- **Operational Reserve Ratio** (Treasury USDC / Outstanding Spendable PMS) — with 7/30/90-day trend
- **Treasury Reserve Solvency Ratio** (Reserve ÷ Total EMS + M$) — primary top-of-dashboard metric; green/amber/red bands
- EMS buying-power expansion status: Inactive / Conditionally Active / Reversion Active
- Phase 2 gate progress: % of way to 300% Treasury Reserve Solvency threshold
- Free public internet node status: nodes deployed, nodes online, uptime
- Active participant count, monthly EMS time credits logged, monthly PMS minted and spent
- Phase status and phase unlock criteria progress

**DAO:**
- Current proposals, vote status, outcome history, policy changelog
- Champion role scope for current phase
- Parameter Tables current values and last-changed date

---

## 13. Audit & Governance Cadence

- **Daily:** Ms. Allis publishes both reserve ratios; auto-applies phase-triggered adjustments; runs data confidence scoring
- **Weekly:** Network snapshot (active users, volume, PMS minted/spent, promo spend, data stewardship KPIs, connectivity node status, phase status, solvency ratio trend)
- **Monthly:** Full treasury audit (USDC reserves, PMS supply, EMS outstanding, reserve ratios, solvency threshold progress); DAO governance session
- **Quarterly:** External audit by independent WV nonprofit (if funds permit); Champion role scope review; conflict-of-interest recusal documentation review
- **Every 6–12 months:** Ms. Allis verification ping cycle for all consenting place records; KPI Specification review against live data

---

## 14. Sunset & Emergency Powers

### 14.1 If Operational Reserve Ratio Falls Below 0.5 (Critical)
- Phase Management Controller automatically pauses all PMS minting and ATM withdrawals
- Only USD loads via Stripe accepted (rebuilds treasury)
- Data stewardship verification ping cycles continue — funded separately
- Emergency governance session called within 48 hours
- Options: (a) shut down gracefully and return remaining reserves to users pro-rata, (b) seek external funding, (c) reset with community consent

### 14.2 If Ms. Allis Detects Coordinated Fraud or Attack
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

### 14.4 If Treasury Reserve Solvency Ratio Falls Below Threshold Post-Expansion
- System automatically reverts to prior-phase parameters
- Expanded buying-power schedules suspended immediately
- No resident loses principal EMS balance
- Reversion logged to durable audit trail with timestamp
- System returns to expanded parameters only after threshold is restored for 2 consecutive quarters

---

## Appendix A: Definitions

- **UEI:** Unique Entity Identifier (per user, including individuals and orgs)

- **EMS (Earned MountainShares) — Time Bank Credits:** Hours of community service logged to the MountainShares time bank recognition ledger. Community time-bank credits; tax and benefits treatment under counsel review (no MountainShares-specific private letter ruling). Vaulted in Phase 1. Subject to conditional, reserve-gated, participant-elected buying-power expansion that activates only when the Treasury Reserve Solvency Ratio ≥ 300% (Phase 2) or ≥ 500% (Phase 3), all formation fees are paid, and no reversion event is active. Confers no equity or ownership interest. Securities treatment under counsel review. Any appreciating founder-side instrument is documented separately on the KTS side only.

- **PMS (Personal MountainShares) — Prepaid Stored Value:** Digital prepaid account balance funded by participant USD deposits. Backed 1:1 by USDC in treasury. Spendable in The Commons; cash-out via ATM under the DUNA's licensed rails with $1.25 fee and 500 PMS daily limit.

- **Treasury Reserve Solvency Ratio:** Treasury Reserve ÷ (Total Outstanding EMS + Total Outstanding M$). Primary conversion-gate metric. Phase 2 threshold: ≥ 300%. Phase 3 threshold: ≥ 500%. Reversion triggers: < 300% (Phase 2 reverts) / < 500% (Phase 3 reverts).

- **Operational Reserve Ratio:** Treasury USDC Reserve ÷ Total Outstanding Spendable PMS. Governs day-to-day continuity of service. EMS not included in denominator.

- **Community Connectivity Nodes:** MountainShares free public internet nodes (Wi-Fi and LoRa community mesh) deployed at trailheads, civic sites, libraries, and community anchors across West Virginia. Funded by fee-allocation Bucket 4 (operations) and Bucket 5 (buildout); kept open to the public as a public good, never metered or paywalled.

- **Ms. Allis:** The AI enforcement and monitoring system operated by Carrie Ann Kidd / KTS at 704 Main Street. Enforces all hard triggers, calculates both reserve metrics daily, surfaces notices to Benefits-Sensitive Account holders, and publishes the public dashboard.

- **Phase Management Controller:** Smart contract enforcing phase-based rules including PMS-only spending in Phase 1, ATM withdrawal processing, emergency pause mechanisms, and automatic phase transitions.

- **WV Money Transmitter License (MTL) / FinCEN MSB Registration:** The state license and federal registration for money transmission; held by the MountainShares DAO / DUNA, not H4H.

- **FVSR (Volunteer Time Value Rate):** The Independent Sector / Do Good Institute Value of Volunteer Time — a BLS-derived rate published annually by Independent Sector and the Do Good Institute. Not a federal or IRS rate. The Phase 3 EMS buying-power rate is the FVSR in effect on the date the DAO formally activates Phase 3 — not the rate at document publication. The current rate (2026) is $36.14. If Phase 3 activates in a later year, the applicable rate is that year's published Independent Sector value.

---

## Appendix C: Participation Roles Cross-Reference

For a complete map of who participates and what they receive, see the Participation Map.

| Role | Economic Safety Relevance |
|---|---|
| **Commons User** | Subject to prepaid loading caps (Tier 1: 500 PMS/mo, Tier 2: 1,000 PMS/mo); earns unlimited EMS time credits at stable baseline value; Benefits-Sensitive Account protections available |
| **Phase 0 Participant** | Founding EMS time credits and badges carry forward at stable baseline value; Groundbreaker rank permanent |
| **Community Champion** | Primary ground-truthing, data stewardship, and connectivity node stewardship force in Phase 1; earns EMS time credits for current phase focus; role evolves through governance |
| **Safety Champion** | Ongoing post-Phase 0 safety review; monitors Phase Management Controller enforcement and both reserve metrics |
| **Merchant** | Pays 1.80% transaction fee; 30% routes to Treasury Reserve; receives PMS in prepaid account |
| **Ms. Allis** | Enforces all hard triggers; monitors both reserve metrics; surfaces conversion gate status; publishes phase unlock countdown |
| **Phase Management Controller** | Smart contract enforcing phase-based rules; processes ATM withdrawals under the DUNA's licensed rails; applies automatic phase transitions; enforces conversion gate conditions |
| **Stripe Payment Gateway** | Fiat-to-crypto onramp; processes USD deposits → USDC to treasury → PMS minted 1:1 |

---

*"People earn what they do. The commons holds what we decide together. Ms. Allis watches so nobody can wreck it."*

*MountainShares Phase 1: Economic Safety Specification — Version 3.2*
*Harmony for Hope, Inc. | MountainShares DAO / DUNA | 704 Main Street, Mount Hope, WV 25880*
*Draft — Subject to H4H board review, DAO governance, and legal counsel approval before reliance*

---

**End of MountainShares Phase 1: Economic Safety Specification v3.2**
