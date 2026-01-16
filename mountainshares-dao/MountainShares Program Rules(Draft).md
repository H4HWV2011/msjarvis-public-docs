# MountainShares Program Rules

> **DRAFT – NOT FINAL PROGRAM RULES**
>
> This document describes draft operational rules for the MountainShares Program.  
> It is provided for internal design, governance discussion, and legal review only.  
> It does not create enforceable rights or obligations and must be reviewed and  
> approved by qualified legal counsel before any production use.

---

## 1. Scope and Structure

### 1.1 Relationship to Other Documents

These Program Rules are **incorporated by reference** into the MountainShares Rewards Program Terms and Conditions (“Terms”). In the event of any conflict between these Program Rules and the Terms, the Terms control.

These Rules are intended to be read together with:

- **MountainShares Rewards Program – Terms and Conditions** (legal framing).  
- **MountainShares Phase 1: Economic Safety Specification** (reserve ratios, caps, hard triggers).  
- **MountainShares DAO Governance Overview** (roles, voting, AI constraints).  
- **MountainShares Complete Systems Overview** (architecture, benefits, three‑phase model).

The Terms define the legal nature of MountainShares (PMS/EMS), disclaimers, and user relationships.  
The Program Rules define **changeable operational parameters** (rates, caps, thresholds, limits, and categories) within the bounds set by those higher‑level documents.

### 1.2 Governance of Program Rules

Program Rules may be updated through:

- Decisions of the Harmony for Hope Board of Directors.  
- Recommendations or votes adopted through the MountainShares DAO, where applicable.  
- Legal, compliance, risk‑management, or safety interventions required by Applicable Law.

Changes are implemented and communicated in accordance with the “Governance, Changes, and Termination” sections of the Terms and the DAO specification.

---

## 2. Eligibility and Account Types

### 2.1 Geographic Scope

- Phase 1 deployment is limited to Users and Merchants whose primary residence or operations are located within the State of West Virginia, unless expressly authorized in writing by Harmony for Hope.  
- Additional regions (for example, broader AppalachianShares or other branches) may be added in later phases as separate governed regions with their own parameter sets.

### 2.2 User Eligibility (Phase 1 Baseline)

Baseline eligibility criteria include, at minimum:

- Minimum age: 18 years (or as permitted by applicable law and policy).  
- Residency: Primary residence address in West Virginia.  
- Identity verification: KYC and other checks as required by risk tier, partner requirements, and Applicable Law.

Specific thresholds and procedures are documented in Program Rules updates and partner integration documents.

### 2.3 Account Types

- **Standard User Account**  
  Default account type for individuals participating in the Program.

- **Merchant / Organization Account**  
  For approved local businesses, nonprofits, and public entities that accept and spend MountainShares within The Commons ecosystem.

- **Benefits‑Sensitive Account**  
  For Users who receive or may receive means‑tested public benefits.  
  Additional protections, caps, and restrictions apply, as described in Section 8 of the Terms and Section 8 of these Rules.

---

## 3. Currency Types and Units

### 3.1 Purchased MountainShares (PMS)

- PMS are issued when Users load fiat currency (such as U.S. dollars) into The Commons via approved payment channels (for example, Stripe).  
- PMS are fully spendable within the network, subject to limits and fee schedules defined in these Rules.  
- PMS are issued at a nominal internal rate of 1 M$ per 1 USD loaded, less applicable fees, solely for use within the Program.

### 3.2 Earned MountainShares (EMS)

- EMS are credited as rewards for documented and verified community contributions (for example, volunteering, mutual aid, education, cultural work, historic preservation).  
- EMS are first recorded in an **unlimited recognition ledger** and then converted into spendable M$ subject to the Phase 1 Economic Safety Specification (base rates, per‑user caps, and reserve‑ratio‑gated limits).  
- EMS are generally **not redeemable for fiat** and are intended for in‑network use only.

### 3.3 Units and Denomination

- The base unit is **one (1) MountainShare**, denoted as **M$** in internal documents.  
- Internal valuations per phase (for in‑network buying power) are set out in Section 5 and in the Economic Safety Specification.

---

## 4. Earning Rules (EMS)

### 4.1 Qualifying Activities

Qualifying activities for EMS earning in Phase 1 may include, but are not limited to:

- Community care and caregiving.  
- Mutual aid, peer support, and informal social care.  
- Cultural preservation, arts, and Appalachian heritage work.  
- Education, learning, teaching, mentoring, and skill‑sharing.  
- Asset mapping, GIS work, data validation, and local knowledge capture.  
- Participation in approved community events, historic trail activities, and Commons‑hosted programs.

Each category is governed by:

- **Verification methods**, such as time‑tracking, partner attestations, task confirmations, or digital checkpoints.  
- **Eligible roles**, such as organizer, facilitator, participant, documenter, or researcher.

Detailed activity lists and verification procedures are maintained in partner agreements and operational guidelines.

### 4.2 Base Earning Rates (Phase 1)

Phase 1 adopts the following high‑level earning structure, consistent with the Economic Safety Specification:

- **Recognition rate:** 1 EMS hour per 1 documented qualifying hour of work.  
- **Conversion to spendable M$:**  
  - Global base rate: starts at 0.2 M$ per EMS hour.  
  - Base rate may be adjusted within the allowed range (0.1–1.0 M$ per EMS hour) when reserve‑ratio conditions and governance criteria are met.

The precise base rate in effect at any time is published via Ms. Jarvis dashboards and API, and may vary over time in response to reserve conditions and governance decisions.

### 4.3 Per‑User Caps and Global Caps

Per‑user caps for **converted, spendable M$** (illustrative Phase 1 starting point):

- **Tier 1 (general users):**  
  - Approximate monthly cap: 40 M$.  
- **Tier 2 (verified caregiving / high‑priority roles):**  
  - Approximate monthly cap: 80 M$.

Weekly and daily caps may be applied in hours relative to the current base rate to smooth issuance across the month.

Global caps:

- Program Rules may define a maximum aggregate amount of EMS convertible to spendable M$ per region per month, calculated to preserve the reserve ratio thresholds in the Economic Safety Specification.

All caps are parameterized and may be adjusted by governance within the safety bands defined in the Economic Safety Specification.

### 4.4 Vaulting and Unlocking

- A portion of EMS may be credited but **vaulted** (visible but not immediately spendable) during Phase 1.  
- Unlocking of vaulted EMS may be tied to:
  - Phase transitions (e.g., Phase 1 → Phase 2).  
  - Governance decisions within allowed bounds.  
  - User tiers, ranks, or verified roles.  
  - Treasury and reserve conditions.

Vaulting and unlocking rules are applied transparently and are subject to audit through Ms. Jarvis reporting and IPFS‑based records.

---

## 5. Phase Mechanics and Internal Buying Power

### 5.1 Internal Phase Definitions

Program Rules reference the three internal phases as defined in the Economic Safety Specification and Terms:

- **Phase 1 – Launch**  
  Internal schedule defines 1 M$ as having an internal 1.00 USD equivalent buying power for eligible in‑network redemptions.

- **Phase 2 – Treasury Threshold**  
  Internal schedule defines 1 M$ as having an internal 10.00 USD equivalent buying power for eligible in‑network redemptions.

- **Phase 3 – Aspirational Full Backing**  
  Internal schedule defines 1 M$ as having an internal 34.70 USD equivalent buying power for eligible in‑network redemptions, initially aligned with prevailing national estimates of volunteer time value when adopted.

These internal values are used solely for in‑network redemption capacity and accounting. They do not establish any external price, redemption right, or profit expectation.

### 5.2 Phase Transition Conditions

Transitions between phases occur only when internal conditions specified in the Economic Safety Specification are met and verified, including:

- Minimum and sustained **reserve ratio** thresholds and stability windows.  
- Minimum levels of monthly processed volume.  
- Minimum active UEI counts and community participation thresholds.  
- Absence of unresolved systemic fraud or reserve‑threatening exploits.  
- Sufficient governance participation and quorum on relevant proposals.

Program Rules record the current threshold values and effective dates for each region. If there is any difference between this document and the Economic Safety Specification, the Economic Safety Specification controls.

### 5.3 Parameter Ranges and Governance Control

For each phase, Program Rules specify:

- Permissible ranges for:
  - Global base earning rate (EMS → M$).  
  - Per‑user and per‑tier caps.  
  - Promo and bonus pool percentages.

- Which parameters may be adjusted by:
  - Automatic mechanisms (hard triggers enforced by Ms. Jarvis).  
  - Governance proposals and DAO votes.  
  - Harmony for Hope risk and compliance overrides (for safety and legal reasons).

Automatic **downward** adjustments in response to reserve ratio declines cannot be disabled or delayed by governance.

---

## 6. PMS Load, Use, and Cash Conversion

### 6.1 Fiat Load Limits (Illustrative Phase 1 Baseline)

Specific values are defined per integration, but may include:

- Minimum load per transaction: defined to avoid trivial micro‑loads.  
- Maximum load per transaction and per day/week/month, tied to KYC level and risk tier.  
- Additional limits for newly created accounts during ramp‑up periods.

### 6.2 PMS Fee Schedule

Program Rules maintain the current fee schedule, consistent with the Terms, for example:

- Load fee on fiat → PMS conversions (currently 2.85%).  
- Internal transfer fee on eligible User‑to‑User transfers (currently 0.25%).  
- Merchant fee on eligible purchases (currently 1.80%).  
- ATM or fiat refund fee per PMS cash‑out transaction (currently 1.25 USD), where such features are enabled.

Fee revenue supports treasury growth, platform operations, compliance, and community programs. Any changes to fee levels are documented with effective dates and communicated in accordance with the Terms.

### 6.3 PMS Cash Conversion

- PMS may be eligible for conversion back to fiat up to the amount originally loaded (less fees and adjustments), subject to operational, liquidity, and regulatory constraints.  
- Program Rules define maximum cash‑out amounts per transaction, per day, and per month.  
- PMS cash conversion is disabled by default for Benefits‑Sensitive Accounts, except under defined, exceptional conditions consistent with Applicable Law and benefits regulations.

Requests for PMS conversion do not guarantee conversion will be completed and are handled subject to treasury availability, partner policies, and Applicable Law.

---

## 7. Spending and Transfers

### 7.1 Permitted Uses

MountainShares may be used, subject to the Terms and Program Rules, to:

- Purchase eligible goods and services from approved Merchants.  
- Participate in events, education, cultural programming, and historic trail activities listed in The Commons.  
- Conduct documented in‑platform sales or exchanges between Users where such functionality is explicitly enabled.

### 7.2 Prohibited and Restricted Uses

Program Rules identify categories that are prohibited or subject to additional restrictions, consistent with the Terms, including:

- Illicit or illegal goods and services.  
- Certain regulated categories (for example, gambling, unlicensed financial services) unless explicitly authorized.  
- Uses that jeopardize regulatory status or public assistance safety.

Ms. Jarvis and Harmony for Hope may monitor, flag, and restrict transactions in these categories, with logging and review procedures set out in governance documents.

### 7.3 Internal Transfers

- Internal User‑to‑User transfers are subject to:
  - Eligibility of sender and receiver accounts.  
  - Specific EMS transfer limitations, especially for Benefits‑Sensitive Accounts.  
  - Transaction minimums, maximums, and rate limits.

Program Rules specify conditions under which transfers may be paused, reversed, or blocked due to suspected fraud, non‑compliance, or safety concerns.

---

## 8. Benefits‑Sensitive Account Rules

### 8.1 Designation and Eligibility

- Users who receive or may receive means‑tested public benefits may self‑designate their account as a Benefits‑Sensitive Account.  
- Harmony for Hope may also designate accounts as Benefits‑Sensitive where permitted by law and with appropriate notice, based on information voluntarily provided or via partner agencies.

### 8.2 Special Protections

Program Rules define the protections that apply to Benefits‑Sensitive Accounts, which may include:

- PMS cash‑out disabled by default.  
- Balance caps and EMS earning throttles intended to reduce the risk of benefits impact.  
- Warnings and educational prompts when balances or usage patterns approach known thresholds of concern.

Numeric thresholds and specific behaviors triggering prompts or throttles are documented here and updated as regulations or best practices evolve.

### 8.3 Reporting and Disclaimers

- Users remain responsible for understanding and complying with benefits reporting requirements.  
- Program Rules may reference external resources (benefits planners, legal aid, informational materials) but do not alter agency authority.  
- No guarantee is made that participation will have no impact on any benefits.

---

## 9. Gamification, Ranks, and Value Interactions

### 9.1 Ranks and Roles

Program Rules define rank tiers (for example, Bronze, Silver, Gold, Champion) and roles (for example, steward, elder) that may be used to:

- Recognize contribution levels.  
- Gate certain governance privileges (consistent with the DAO specification).  
- Adjust non‑monetary aspects of the user experience.

Rank is earned via documented time and contribution, not via financial stake.

### 9.2 Quests and Value Interactions

- “Value interactions” are concrete actions such as fulfilled help requests, event attendance, successful mappings, or other documented contributions.  
- Program Rules specify which interactions are counted and whether they carry EMS rewards, badges, or other recognition.  
- Quests and streaks may be defined to encourage participation in priority activities, consistent with reserve‑ratio limits and per‑user caps.

### 9.3 Governance‑Sensitive Game Parameters

Program Rules identify which gamification parameters (e.g., quest rewards, streak bonuses, rank thresholds) may be adjusted by governance, and within what safe ranges, to prevent exploitation or over‑incentivization.

---

## 10. Regional and Branch‑Level Parameters

### 10.1 Regional Overrides

- MountainShares may be deployed in multiple regions (e.g., MountainShares WV, AppalachianShares, CoastalShares).  
- Each region may adopt region‑specific parameter values (e.g., caps, activity categories) within the global safety and legal framework.  
- Program Rules identify which parameters are global and which may be overridden at the regional level.

### 10.2 Inter‑Region Interchange

If inter‑region interchange is enabled:

- Program Rules define permitted exchange mechanisms, caps, and internal rates for cross‑region flows.  
- Safeguards are specified to avoid risk contagion between regions (for example, limits on net flows, separate reserves, or circuit‑breaker conditions).

---

## 11. Change Management and Versioning

### 11.1 Version Control

Each revision of these Program Rules includes:

- A version number (e.g., v1.0.0).  
- An effective date.  
- A brief changelog summarizing key modifications.

### 11.2 Notice Procedures

Material changes to Program Rules are communicated via:

- Updates within The Commons application or official Harmony for Hope websites.  
- In‑app notifications or alerts.  
- Email notices, where appropriate, to the primary email on file.

Notice periods follow the standards set out in the Terms, except where immediate changes are required for legal, security, or operational safety reasons.

### 11.3 Alignment with Higher‑Level Documents

Program Rules must remain consistent with:

- MountainShares Rewards Program Terms and Conditions.  
- MountainShares Phase 1 (and later) Economic Safety Specifications.  
- MountainShares DAO governance framework and Harmony for Hope’s legal and fiduciary obligations.

Any change that would conflict with those documents is not effective until the higher‑level documents are amended through their own defined processes.

---
