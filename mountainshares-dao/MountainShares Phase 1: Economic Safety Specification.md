# MountainShares Phase 1: Economic Safety Specification

> **Disciplinary Context: Appalachian Economic Commons**
> This document instantiates Polymathmatic Geography principles P1, P9, P16, and related axioms for the Appalachian economic commons:
> - **P1 – Every where is entangled / Leakage and enclosure:** Sections 1–3 and 7–11 treat recognition, spendable M$, reserve ratios, and phase transitions as a single coupled system, explicitly tying minting and circulation to backing assets and regional program realities. See https://github.com/H4HWV2011/msjarvis-public-docs/blob/main/docs/Polymathmatical-Geography.md
> - **P9 – Transparency and traceability:** Sections 3, 4, 9, and 10 define public reserve-ratio calculations, dashboards, audits, and governance cadences so that money creation, caps, and emergency actions are observable and reconstructable over time.
> - **P16 – Power accountable to place:** Sections 2, 3, 5–7, and 11 bound DAO, Ms. Jarvis, and H4H authority inside hard economic and legal constraints, ensuring that decisions about rates, caps, and shutdowns answer to local solvency and community safety rather than abstract speculation.
> - **Anti-leakage and closed-loop spending:** The separation of the recognition ledger from capped, reserve-backed M$ (Section 1) and the reserve-ratio-driven adjustment table (Section 3) operationalize anti-leakage design and keep the closed loop anchored in real backing assets.
> - **Bounty and corrective programs:** Promo-pool rules (Section 4) and example governance scenarios (Appendix B) show how targeted bonuses and parameter changes can be treated as bounded "bounties" aligned with safety math rather than unconstrained giveaways.

**Version:** 1.2
**Date:** March 13, 2026
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

---

## 1. Foundation: What Phase 0 Built

Phase 1 does not start from zero. It starts from a tested, red-teamed foundation built during Phase 0 (Invite-Only Beta).

**What Phase 0 produced:**
- A working recognition ledger with real UEIs, real EMS hours, and real geo-tagged activity
- A red-teamed wallet and M$ system with documented security findings and remediations
- A cohort of Groundbreaker-rank participants who carry founding badges, founding EMS hours, and governance eligibility into Phase 1
- A Phase 0 Pre-Launch Audit Report that serves as the permanent founding governance record
- A tested Ms. Jarvis system with reserve ratio enforcement, safety trigger logic, and chatbot integration
- Validated data stewardship workflows, including ground-truthing consent processes and initial contact record collection

All EMS hours logged during Phase 0 carry forward permanently. Groundbreaker rank is locked — it cannot be earned after Phase 1 opens. Founding badges are permanent and visible on UEI profiles forever.

Phase 1 inherits everything Phase 0 built and opens it to the community.

---

## 2. Core Economic Principles

- **Recognition Ledger (Unlimited):** All EMS hours logged on-chain with full UEI, geo, org, and timestamp data. No hard cap; serves as permanent audit trail, rank engine, and identity marker.
- **Spendable M$ (Capped & Reserve-Backed):** Convertible portion pegged to treasury backing ratio. Starts conservatively; can only increase with DAO vote inside safe thresholds.
- **Hard Triggers (Automatic, Non-Negotiable):** Ms. Jarvis enforces automatically; no DAO override possible.
- **Two games, one system:** The Commons daily game and the MountainShares contribution game share the same UEI, the same recognition ledger, and the same EMS hours. Every qualifying Commons activity feeds rank, governance standing, and badge progression in MountainShares automatically.
- **Three-stage platform arc:** The Commons grows from a barter/trade and Facebook Marketplace feel (Phase 1 early) through TikTok-style discovery (Phase 1 mature) to an Amazon-style full commerce layer (Phase 2+). Economic safety parameters must support each stage. See [The Commons Gamification](../the%20commons/The%20Commons%20Gamification%3A%20The%20Daily%20Life%20Game.md) Section 2 for the full arc.

---

## 3. Starting Conversion Rate & Per-User Caps (Phase 1 Bootstrap)

### 3.1 Global Base Rate
- **Starting:** 0.2 M$ per EMS hour
- **Range:** Can adjust 0.1 – 1.0 M$ per EMS hour via DAO vote, *only if* reserve ratio ≥ threshold (see Section 4)
- **Example:** If a user logs 8 hours of verified caregiving at 0.2, they earn 1.6 M$ (capped further by tier, below)

All current rates and caps are maintained in the [Program Rules – Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md), which is the authoritative live reference for any value that may change through governance.

### 3.2 Per-User Convertible Caps (Monthly)

| User Tier | Definition | Monthly Cap (M$) | Weekly Cap | Daily Cap |
|-----------|-----------|------------------|-----------|-----------|
| **Tier 1** | General Commons, light EMS (non-mission-critical) | 40 M$ | 10 hrs | 1–2 hrs |
| **Tier 2** | Verified EMS, caregiving, high-need community roles (geo+UEI validated) | 80 M$ | 20 hrs | 4 hrs |

**Tier Assignment Logic:**
- Tier 1 default for all new UEIs.
- Tier 2 requires: org co-sign (nonprofit, EMS, mutual aid network) + geo-fence verification + Commons trust signals.
- Ms. Jarvis flags tier eligibility; final assignment by DAO governance or pre-agreed rules.

### 3.3 Benefits-Sensitive Account Protections

Participants receiving means-tested public benefits (SNAP, Medicaid, SSI, WV WORKS, etc.) are protected by default. Benefits-Sensitive Accounts have:

- **Hard balance cap:** M$ wallet balance may not exceed a threshold set to protect benefits eligibility (DAO-governed, defaults to conservative level at Phase 1 launch; see [Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md) Section 6)
- **Throttled earning rate:** EMS-to-M$ conversion throttles automatically if balance approaches cap
- **No forced disclosure:** Participation in The Commons does not require disclosure of benefit status; protection is opt-in and participant-controlled
- **Ms. Jarvis proactive notice:** When a Benefits-Sensitive Account participant approaches a threshold, Ms. Jarvis provides a plain-language notice and suggests they consult with a benefits counselor before converting additional EMS
- **Non-countable recognition hours:** EMS hours on the recognition ledger are not M$ balances and are not designed to be treated as income or assets for benefits purposes; legal counsel reviews this classification before Phase 1 launch

### 3.4 Examples at 0.2 Base Rate

- **Tier 1 user, 30 EMS hours/month:** 30 × 0.2 = 6 M$ (well under 40 M$ cap) ✓
- **Tier 2 user, 200 EMS hours/month (very active caregiver):** capped at 80 M$ convertible ✓
- **If rate rises to 1.0 M$/hour via DAO vote:** Same user gets 80 M$ from same 80 EMS hours ✓

---

## 4. Treasury Backing & Hard Reserve Thresholds

### 4.1 Reserve Ratio Definition

```
Reserve Ratio = Liquid Backing Assets (USD) / Total Outstanding Spendable M$
```

**Backing Assets Include:**
- USD load fees (users converting USD → M$)
- Merchant transaction fees (1.80% of eligible M$ transactions)
- Internal transfer fees (0.25%)
- ATM/refund fees ($1.25 flat per cash-out transaction)
- CLIO NFT revenue
- DAO-approved grants or donations
- *Excludes:* EMS recognition hours, future promises

> **Fee Revenue Allocation:** All collected fees are allocated across five designated purposes per the
> fixed split defined in [Program Rules – Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md)
> **Section 4.3**:
>
> | Bucket | Allocation | Purpose |
> |--------|------------|---------|
> | 1 | 30% | Harmony for Hope, Inc. (H4H Operations) |
> | 2 | 30% | Treasury Reserve |
> | 3 | 15% | Platform Development |
> | 4 | 15% | Community Programs |
> | 5 | 10% | Community Projects |
> | — | +0.55% | Supplemental Treasury Reserve (on gross transaction volume) |
>
> The **merchant fee (1.80%)** and the **ATM flat fee ($1.25)** are primary Treasury Reserve-building
> mechanisms: 30% of each routes directly to the reserve at settlement, and the +0.55% supplemental
> assessment on gross volume compounds reserve growth independently of fee collection.
> See Parameter Tables Section 4.3 for governance floors, adjustability rules, and the full allocation
> rationale.

### 4.2 Safety Thresholds (Ms. Jarvis Enforces Automatically)

| Reserve Ratio | Global Base Rate | User Cap Adjustment | Bonus Promos | Action |
|---------------|------------------|-------------------|------------|--------|
| ≥ 1.5 | 1.0 M$/hr (full 1:1) | 120 M$/mo (Tier 2) | Enabled | DAO can vote to increase |
| 1.0 – 1.49 | 0.5–0.8 M$/hr (DAO-controlled) | 80–100 M$/mo | Reduced | DAO can vote to increase *if trend stable* |
| 0.75 – 0.99 | 0.2–0.4 M$/hr (DAO-controlled) | 40–80 M$/mo | Paused | DAO can vote *only to hold steady* |
| < 0.75 | 0.1 M$/hr (Emergency Floor) | 20–40 M$/mo | Frozen | Auto-tighten; no DAO votes increase anything |

**Automatic Trigger Logic:**
- Ms. Jarvis recalculates reserve ratio daily.
- If ratio crosses a threshold boundary, new rate and caps apply at next epoch (24–48 hour notice to all participants).
- No human approval required for *downward* adjustments; they fire automatically.
- Promo pool bonuses pause automatically when reserve ratio < 1.0. Ms. Jarvis notifies participants in plain language.

---

## 5. Monthly Promo & Bonus Pool

### 5.1 Promo Pool Budget
- **Source:** Allocated from fees and treasury per the smart contract structure and [Parameter Tables](Program%20Rules%20%E2%80%93%20Parameter%20Tables.md) Section 4.2.
- **Max Size:** 2–3% of monthly processed volume, capped at X M$/month (DAO sets X per Parameter Tables).
- **Example:** If volume is 100k USD/month, promo pool ≤ 2–3k M$/month.

### 5.2 Bonus Rules
- All bonuses (e.g., "+50 M$ for visiting Nicholas Pharmacy") draw from the pool.
- Once pool is exhausted in a month, no new bonuses are offered until next cycle.
- **Bonuses still count against the user’s per-month convertible cap** — they do not bypass it.
- Bonuses pause automatically when reserve ratio < 1.0.
- Quest completion rewards, seasonal campaign bonuses, and streak milestone rewards all draw from this pool.
- Data stewardship verification rewards are funded separately per the smart contract structure — they do not draw from the promo pool.

---

## 6. EMS Earning Categories

The following categories are recognized as qualifying EMS-earning activities in Phase 1. All activities log EMS hours to the recognition ledger with UEI, geo, org, and timestamp. Full earning rules are defined in the [Program Rules](MountainShares%20Program%20Rules(Draft).md).

| Category | Examples | Notes |
|----------|---------|-------|
| **Mutual Aid** | Caregiving, supply donation, transportation, neighbor support | Tier 2 eligible with org co-sign |
| **Learning and Teaching** | Workshops, skill sessions, mentoring, learning modules | 1 EMS hr per verified hour |
| **Cultural Preservation** | Clio trail markers, oral history, heritage events, traditions | 1 EMS hr per verified hour |
| **Land and Mapping** | GIS validation, place record submission, parcel verification | 1 EMS hr per verified hour |
| **Data Stewardship** | Ground-truthing, contact collection (with consent), Ms. Jarvis verification ping responses, record updates | EMS awarded per verified activity and per ping response; funded per smart contract structure |
| **Community Events** | Commons-hosted events, volunteer hours, local programs | 1 EMS hr per verified hour |
| **Governance Participation** | DAO votes, proposal review and feedback, governance sessions | 1 EMS hr per session |
| **Emergency Preparedness** | Prep activities during active NOAA alert periods, resilience drills | Promo bonus when reserve permits |
| **Commerce and Trade** | Marketplace listings, barter exchanges, merchant transactions | M$ transaction logged; EMS for verified service hours |

For the full quest structure, streak system, seasonal campaign design, and badge system tied to these categories, see [The Commons Gamification: The Daily Life Game](../the%20commons/The%20Commons%20Gamification%3A%20The%20Daily%20Life%20Game.md).

---

## 7. Data Stewardship and Ground Truthing

Data accuracy is a core commons value and a recognized EMS-earning activity. Rural data decays fast — businesses close, phone numbers change, services disappear. The Commons maintains a living, verified data layer through community participation.

### 7.1 Ground Truthing Workflow

1. Community Champions (and eligible participants) collect contact information — email and SMS — for local places, businesses, organizations, and services.
2. **Explicit opt-in consent** is required and documented at collection time (collector UEI, collection date, consent method, contact type).
3. Ms. Jarvis runs automated verification pings every **6–12 months** to each consenting record holder.
4. When the record holder **responds and confirms or updates** their data, they earn EMS hours. The record is marked verified with a new timestamp and confidence score.
5. Verification rewards are funded per the existing smart contract structure, separate from the promo pool.

### 7.2 Community Champion Role in Data Stewardship

Community Champions are the primary ground-truthing force in Phase 1 early. Their role is **fluid by design** — it evolves as the program matures:

| Phase | Primary Champion Focus |
|-------|----------------------|
| Phase 0 | Red-team security, governance document review |
| Phase 1 (early) | Ground truthing — contact collection, place record verification |
| Phase 1 (mature) | Community anchoring, onboarding, quest coordination |
| Phase 2+ | Governance leadership, regional stewardship, data quality oversight |

Champion responsibilities in any given period are defined through governance. EMS hours are earned for the current phase focus; the recognition ledger preserves the full history.

### 7.3 Data Stewardship KPIs

Ms. Jarvis tracks and publishes the following data quality indicators as part of the weekly network snapshot:

- % of active place records verified within the last 12 months
- Response rate to Ms. Jarvis verification pings (rolling 6-month)
- Total records collected, verified, and updated in current period
- Number of active participants with Data Keeper or Living Map badges

Full KPI definitions are in the [KPI Specification](MountainShares%20KPI%20Specification.md).

---

## 8. DAO Authority: What Can Change & How

### 8.1 DAO Can Vote To Change (Requires Super-Majority, e.g., 66%+)

✅ **Global base rate** (0.2 → 0.5 → 0.8 → 1.0), *only if reserve ratio is in safe zone*
✅ **Per-user monthly caps** (40/80 → 60/100 → 80/120), *only if reserve ratio supports it*
✅ **Tier assignment criteria** (e.g., add new community roles as Tier 2)
✅ **Promo pool budget** (increase X M$/month), *only if backing assets support it*
✅ **Hard trigger thresholds themselves** (move 1.5 to 1.4, etc.), *only once system is stable + audited*
✅ **Quest categories, seasonal campaigns, badge criteria**, *within reserve-ratio safety bands*
✅ **Champion role scope and focus per phase**, *through standard proposal lifecycle*
✅ **Fee revenue allocation percentages** (Parameter Tables Section 4.3), *subject to governance floors of 20% minimum for Treasury Reserve and 20% minimum for H4H Operations; requires 66% super-majority + Board ratification*

### 8.2 DAO Cannot Override (Hard Trigger Rules)

❌ Vote to mint M$ without reserve backing
❌ Disable automatic rate/cap reductions when ratio drops below threshold
❌ Allow EMS conversions that would breach reserve ratio math
❌ Override Benefits-Sensitive Account protections without supermajority + legal review
❌ Overrule legal / safety prohibitions (drugs, weapons, exploitation, etc.)
❌ Remove consent requirements from data stewardship workflows
❌ Alter smart-contracted fee rates outside the governance process defined in the Parameter Tables
❌ Reduce Treasury Reserve allocation below 20% or H4H Operations below 20% (governance floors per Parameter Tables Section 4.3.3)

### 8.3 Ms. Jarvis Authority (Automatic, No Vote Needed)

✅ Enforce reserve ratio checks every 24 hours; apply auto-adjustments if thresholds crossed
✅ Flag and freeze EMS/M$ flows tied to illegal content or high-risk patterns
✅ Calculate and publish daily reserve ratio, backing assets, outstanding M$, and next-rate-tier projection
✅ Tier assignments based on pre-agreed rules (org co-sign + geo verification)
✅ Pause bonuses when reserve ratio < 1.0
✅ Run data stewardship verification pings every 6–12 months; award EMS for verified responses
✅ Maintain data confidence scores on all place records
✅ Surface plain-language notices to Benefits-Sensitive Account holders approaching thresholds
✅ Surface badge progress, quest availability, and streak status through the Commons app

---

## 9. One UEI = One Vote

- **Governance Token:** Each UEI receives 1 equal vote on all DAO proposals.
- **Voting Rights:** After 30 days on-platform (anti-sybil) and minimum 10 EMS hours logged (Bronze rank threshold).
- **Vote Scope:** All items in Section 8.1 (increases/policy changes); cannot vote on Section 8.2 (hard triggers) or illegal activity rules.
- **Rank does not change vote weight.** A Champion and a Bronze participant each get one vote.

---

## 10. Phase 0 → Phase 1 → Phase 2 Graduation Criteria

### 10.1 Phase 0 → Phase 1 (Already Completed Before This Document)

Phase 0 graduated to Phase 1 when the Pre-Launch Audit Report was finalized, all critical and high security findings were remediated, and founding governance documents were approved by the founding cohort.

### 10.2 Phase 1 → Phase 2 Graduation Criteria

**Transition to Phase 2 only when ALL of the following hold for 60+ consecutive days:**

- Reserve ratio stable ≥ 1.0 (no dips below threshold)
- Monthly processed volume ≥ 200k USD (realistic merchant/load flow)
- Active UEIs ≥ 2,000 (meaningful community adoption)
- Zero systemic fraud or reserve-threatening exploits
- DAO governance participation ≥ 30% quorum on key votes
- Data stewardship layer active: ≥ 500 verified place records with ≥ 60% verified in last 12 months
- Benefits-Sensitive Account protections reviewed by legal counsel and confirmed compliant

**Phase 2 Changes:** Caps can rise further; base rate can approach 1.0; Stage 2 (Discovery/TikTok-feel) and Stage 3 (Full Commerce/Amazon-style) platform features unlock; statewide rollout planning begins.

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
| **Benefits Fraud** | No misrepresentation of benefits status to manipulate account tier or cap | Cross-check + manual review trigger | Account freeze + investigation |

**Enforcement:**
- Ms. Jarvis auto-flags and freezes.
- Human review within 24–48 hours.
- Clear appeals process for false positives.
- Transparent logging (anonymized) of all freezes/bans.

---

## 12. Transparency & Dashboards (Ms. Jarvis Public API)

Every UEI can see (updated daily):

**Personal:**
- Hours logged, M$ balance, convertible budget remaining, tier status
- Current rank, EMS hours to next rank, active badges and badges in progress
- Data stewardship record count and verification ping history
- Benefits-Sensitive Account status and threshold proximity (private, participant-only)

**Network:**
- Current reserve ratio, backing assets breakdown, total outstanding M$, next rate tier projection
- Data stewardship KPIs: % records verified in last 12 months, ping response rate
- Active participant count, monthly EMS hours logged, monthly M$ minted and spent

**DAO:**
- Current proposals, vote status, outcome history, policy changelog
- Champion role scope for current phase
- Parameter Tables current values and last-changed date

**Purpose:** Make “should we vote to raise the rate?” a decision based on visible data, not trust.

---

## 13. Audit & Governance Cadence

- **Daily:** Ms. Jarvis publishes reserve ratio, auto-applies threshold-triggered adjustments, runs data confidence scoring
- **Weekly:** Network snapshot (active users, volume, M$ minted, promo spend, data stewardship KPIs)
- **Monthly:** Full treasury audit, DAO governance session (proposals + votes)
- **Quarterly:** External audit by independent WV nonprofit (if funds permit); Champion role scope review through governance
- **Every 6–12 months:** Ms. Jarvis verification ping cycle for all consenting place records

---

## 14. Sunset & Emergency Powers

### 14.1 If Reserve Ratio Falls Below 0.5 (Critical)
- All EMS conversions pause immediately
- Only USD loads and merchant fees accepted
- Data stewardship verification ping cycles continue — funded separately from main reserve
- Emergency governance session called within 48 hours
- Options: (a) shut down gracefully, (b) seek external funding, (c) reset with community consent

### 14.2 If Ms. Jarvis Detects Coordinated Fraud or Attack
- Affected accounts frozen pending review
- Daily public reporting of incident (anonymized)
- Emergency DAO vote on remediation (clawback, reset, shutdown)
- Contact data and place records locked from export during active incident

### 14.3 If Data Stewardship Breach Occurs
- Contact data collection paused immediately
- Affected record holders notified per Privacy Policy obligations
- Incident logged publicly (anonymized)
- Data stewardship verification paused until breach is remediated and reviewed

---

## Appendix A: Definitions

- **UEI:** Unique Entity Identifier (per user, including individuals and orgs)
- **EMS:** Earned Merit Score hour — 1 hour of qualifying community work logged with UEI + geo + timestamp
- **M$:** MountainShares token (spendable, reserve-backed, convertible)
- **Backing Assets:** Liquid USD and near-liquid reserves (fees, donations, CLIO revenue)
- **Reserve Ratio:** Backing Assets / Outstanding M$; Ms. Jarvis enforces thresholds
- **Tier:** User classification (Tier 1 = general, Tier 2 = verified EMS/caregiving)
- **Hard Trigger:** Automatic enforcement rule (Ms. Jarvis, no override)
- **DAO Vote:** Community governance (1 UEI = 1 vote, super-majority for increases)
- **Benefits-Sensitive Account:** Account flagged (by participant opt-in) as belonging to a means-tested benefits recipient; subject to additional cap and throttle protections per Parameter Tables Section 6
- **Ground Truthing:** The activity of collecting, verifying, and updating local place and contact records with documented consent
- **Verification Ping:** An automated Ms. Jarvis outreach (email or SMS) to a consenting record holder asking them to confirm or update their data; responding earns EMS hours
- **Confidence Score:** Ms. Jarvis’s per-record quality rating based on verification recency, response history, and cross-source consistency
- **Three-Stage Platform Arc:** The Commons’ growth path from Stage 1 (Marketplace/barter) → Stage 2 (Discovery/TikTok-feel) → Stage 3 (Full Commerce/Amazon-style)
- **Fee Revenue Allocation:** The 30/30/15/15/10 split of all collected fee revenue across H4H Operations, Treasury Reserve, Platform Development, Community Programs, and Community Projects, plus the +0.55% supplemental treasury reserve on gross volume; fully defined in Parameter Tables Section 4.3

---

## Appendix B: Example Governance Scenario

**Month 3 of Phase 1:**

- Reserve ratio = 1.2 (healthy, above 1.0 threshold)
- Monthly processed volume = 150k USD
- Active UEIs = 1,200
- EMS logging consistent, no fraud detected
- Data stewardship: 200 records collected, 75% verified in last 12 months
- Community feedback: "40–80 M$/month is meaningful but tight"

**DAO Proposal:** "Raise global base rate from 0.2 → 0.35 M$/hr and tier caps from 40/80 → 60/100 M$/mo"

**Vote:** 68% in favor (super-majority)

**Result:** Next epoch (24 hrs), all users get 1.75× their previous earning potential.
- Tier 1: now capped at 60 M$/mo instead of 40
- Tier 2: now capped at 100 M$/mo instead of 80
- Ms. Jarvis recalculates reserve ratio: still 1.18 (healthy)

**Rinse, repeat monthly.** As volume grows and the reserve ratio strengthens, the community votes its own way up the scale toward 1:1. As the data layer matures and Champion focus shifts, governance updates the Champion role scope. As Phase 2 graduation criteria approach, the community sees it in the dashboard before the vote happens.

---

## Appendix C: Participation Roles Cross-Reference

For a complete map of who participates in The Commons and MountainShares, what documents govern them, what they do, what they receive, and what they are not — see the [Participation Map](../the%20commons/Participation%20Map.md).

Key roles relevant to this specification:

| Role | Economic Safety Relevance |
|------|--------------------------|
| **Commons User** | Subject to per-user caps, tier assignment, Benefits-Sensitive Account protections |
| **Phase 0 Participant** | Founding EMS hours and badges carry forward; Groundbreaker rank permanent |
| **Community Champion** | Primary ground-truthing and data stewardship force in Phase 1 early; role evolves through governance |
| **Safety Champion** | Ongoing post-Phase 0 safety review; feeds into quarterly audit cycle |
| **Merchant** | Pays 1.80% transaction fee per Parameter Tables Section 4.1; 30% of that fee routes to Treasury Reserve at settlement per the fee revenue allocation (Parameter Tables Section 4.3); merchant fees are a primary reserve-building mechanism |
| **Ms. Jarvis** | Enforces all hard triggers; runs verification pings; maintains reserve ratio and confidence scores |

---

*“People earn what they do. The commons holds what we decide together. Ms. Jarvis watches so nobody can wreck it.”*
