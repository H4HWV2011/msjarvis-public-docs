# MountainShares Phase 0: Invite-Only Beta Specification

> **Disciplinary Context: Appalachian Economic Commons**
> This document instantiates Polymathmatic Geography principles P1, P9, P16, and related axioms for the Appalachian economic commons:
> - **P1 – Every where is entangled / Leakage and enclosure:** Phase 0 is the first moment the closed-loop system touches real place — real wallets, real UEIs, real EMS hours logged against real people and geographies in West Virginia. Every design choice here shapes leakage and enclosure patterns in Phase 1 and beyond. See https://github.com/H4HWV2011/msAllis-public-docs/blob/main/docs/Polymathmatical-Geography.md
> - **P9 – Transparency and traceability:** All Phase 0 activity — wallets issued, EMS hours logged, red-team findings, security incidents, and parameter changes — is logged in the recognition ledger and auditable. Nothing in Phase 0 is invisible.
> - **P16 – Power accountable to place:** Phase 0 is governed by Harmony for Hope's board and designated system monitors under documented authority. Community Champions earn governance standing through logged hours, not invitation status alone.
> - **Anti-leakage and closed-loop spending:** Phase 0 deliberately restricts EMS-to-spendable-M$ conversion and prohibits external cash-out to protect the closed loop before the treasury is sufficiently backed. PMS loads may be enabled for select participants on a case-by-case basis under system monitor approval.
> - **Bounty and corrective programs:** Red-team and security testing in Phase 0 is the first structured bounty program — logged, rewarded with EMS, and used to harden the system before public launch.

**Version:** 2.0
**Date:** June 17, 2026
**Status:** DAO Governance Document — Structural Rewrite
**Scope:** West Virginia Pilot — Invite-Only Beta
**Incorporated by reference into:** MountainShares DAO Governance Charter (Section 7.2), MountainShares Phase 1 Economic Safety Specification, MountainShares Program Rules

> **Entity Status Notice:** Kidd's Technical Services ("KTS") is not yet a registered West Virginia LLC and has no EIN. References to "KTS" in this document mean Carrie Ann Kidd personally, operating under that trade name. Formation of the WV LLC is the gating step before founder equity, ALLIS IP holding, and KTS-side capitalization instruments take legal effect.

> **Server Location Notice:** The operational server cluster and Ms. Allis / ALLIS node for H4H and MountainShares Commons is located at **704 Main Street, Mount Hope, West Virginia 25880** (Fayette County Community Arts Center).

> **EMS Appreciation Notice:** Community EMS maintains stable baseline exchange value throughout Phase 0 and Phase 1. Buying-power expansion schedules are **inactive** unless and until the Treasury Reserve achieves the applicable solvency threshold (300% of total EMS + M$ outstanding at Phase 2; 500% at Phase 3), all Treasury Reserve-funded transition and formation costs have been paid, and no reversion event has occurred. If the reserve metric falls below the applicable threshold, the system automatically reverts to prior-phase specifications to maintain continuity of service. No resident holds a vested appreciation right prior to threshold clearance. Phase 0 EMS hours are baseline mutual-credit units only — they carry no present appreciation right, no conversion right to fiat, and no equity interest of any kind.

---

## Structural Framework

This specification operates within the three-box entity structure governing MountainShares. All Phase 0 design choices must preserve the walls between these entities.

| Entity | Role | Phase 0 Relevance |
|---|---|---|
| Harmony for Hope, Inc. (H4H) | 501(c)(3) charitable anchor; program sponsor | Holds governance authority during Phase 0; authorizes Phase 1 launch |
| MountainShares Commons / DUNA | Community-owned mutual-credit ledger and governance layer | EMS ledger, UEIs, Community Champions, voting eligibility |
| Kidd's Technical Services (KTS) | To-be-formed for-profit LLC/PBC; founder-owned commercial engine | Ms. Allis / ALLIS deployment at 704 Main Street; founder-side rights documented separately |

No Phase 0 mechanism may create a path by which founder value is realized through H4H or community EMS. Any such path found in testing is a **Critical** security finding requiring resolution before Phase 1 launch.

---

## 1. Purpose and Scope

Phase 0 is the **invite-only beta period** that precedes public launch of MountainShares and The Commons. Its purposes are:

- Issue and test real wallets, UEIs, and EMS recognition against production or near-production infrastructure at 704 Main Street.
- Identify and harden security vulnerabilities, reserve-ratio logic errors, fraud vectors, and UX friction points before public participants are exposed.
- Build the first cohort of Community Champions who understand the system deeply and can serve as stewards, captains, and red-team elders as the community grows.
- Accumulate real EMS hours in the recognition ledger that count toward Phase 1 governance eligibility.
- Validate Ms. Allis enforcement behavior — reserve ratio calculations, Treasury Reserve solvency gating, tier assignments, hard trigger logic, and dashboard accuracy — in a live environment before public launch.
- Confirm that EMS buying-power expansion gates are inactive at Phase 0 and Phase 1 and that the reversion trigger logic functions correctly.

Phase 0 does **not** constitute public availability of MountainShares. No public marketing, open registration, or general solicitation occurs during Phase 0.

---

## 2. Phase 0 Participants

### 2.1 Who Is Invited

Phase 0 participants are selected by Harmony for Hope and designated system monitors. Invitation categories include:

- **Security and red-team participants** — developers, systems testers, and security researchers invited to probe treasury logic, EMS logging, reserve ratio enforcement, Treasury Reserve solvency gating, smart contract surfaces, and Ms. Allis behavior.
- **Community anchor participants** — local trusted community members, nonprofit partners, and local business representatives in the Mount Hope area invited to test real-world UX, onboarding flows, and EMS earning activities.
- **Internal team participants** — Harmony for Hope staff, KTS technical contributors (currently Carrie Ann Kidd personally), and governance document reviewers.

### 2.2 What Phase 0 Participants Receive

Upon invitation and acceptance:

- A **MountainShares wallet** tied to a unique **UEI** (Unique Entity Identifier).
- Authenticated access to The Commons app and the Ms. Allis chatbot UI via secure, non-public links at the 704 Main Street ALLIS node.
- Access to Phase 0 documentation, testing guides, and red-team scope documents.
- EMS hours logged in the **recognition ledger** for qualifying Phase 0 activities (see Section 4).

Phase 0 EMS hours are baseline mutual-credit units. They carry no present appreciation right, no conversion right, no equity interest, and no cash value.

### 2.3 Community Champions

Phase 0 security and red-team participants may be designated as **Community Champions** under Section 2.5.4 of the DAO Governance Charter. This designation:

- Recognizes their foundational role in hardening the system.
- Gives them founding governance eligibility (1 UEI = 1 vote) once standard eligibility criteria are met (30 days account age + 10 EMS hours).
- Does **not** grant extra voting weight, override capability, or exemption from hard safety triggers.
- Does **not** create any financial right, equity interest, expectation of profit, or claim against KTS, H4H, or the DUNA.

---

## 3. Economic Rules During Phase 0

Phase 0 operates under the most conservative economic parameters in the MountainShares lifecycle. These restrictions exist because the Treasury Reserve solvency conditions for any buying-power expansion have not been met and will not be met during Phase 0.

### 3.1 Recognition Ledger — Active

All qualifying Phase 0 activity is logged in the **unlimited recognition ledger** with full UEI, geo, org, and timestamp metadata. These hours are permanent and carry forward into Phase 1 and beyond. They represent baseline mutual-credit units only.

### 3.2 EMS Value and Appreciation Status

Community EMS during Phase 0 is **non-appreciating**. The system's buying-power expansion schedule is inactive at this stage. Specifically:

- **Phase 2 buying-power expansion** requires Treasury Reserve ≥ 300% of total EMS + M$ outstanding, with all Treasury Reserve-funded formation and transition fees fully paid. That condition is not met in Phase 0.
- **Phase 3 buying-power expansion** requires Treasury Reserve ≥ 500% of total EMS + M$ outstanding. That condition is not met in Phase 0.
- If the reserve metric ever falls below the applicable threshold in a later phase, the system automatically reverts to prior-phase specifications. No resident loses their principal EMS balance on reversion; buying-power expansion is simply suspended.

No participant in Phase 0 holds or accumulates any vested appreciation right. EMS earned in Phase 0 enters Phase 1 at stable baseline exchange value.

### 3.3 Spendable M$ — Severely Restricted

| Parameter | Phase 0 Value | Notes |
|---|---|---|
| EMS → M$ conversion | **Disabled by default** | No spendable M$ issued from EMS during Phase 0 except by explicit system monitor authorization for testing purposes |
| PMS loads (USD → M$) | **Restricted — by invitation only** | Enabled only for specific test scenarios; all loads are monitored |
| Per-user spendable cap | **Test amounts only** | Not the Phase 1 production caps; set per test scenario |
| Cash-out / ATM | **Disabled** | No fiat conversion of any kind during Phase 0 |
| Benefits-Sensitive Accounts | **All accounts treated as benefits-sensitive by default** | Maximum protection during beta |

### 3.4 Hard Triggers — Fully Active

Ms. Allis enforces **all hard economic safety triggers** during Phase 0, including reserve ratio monitoring, automatic cap tightening, fraud flagging, Treasury Reserve solvency gate enforcement, and safety prohibitions. These cannot be disabled for testing purposes. Testing of hard trigger behavior is conducted by **observing trigger responses**, not by disabling them.

### 3.5 No External Cash Value

Phase 0 MountainShares — whether EMS hours in the recognition ledger or any test spendable M$ — carry **no external cash value** and no right to redemption. Phase 0 EMS hours count toward governance eligibility and rank only.

---

## 4. Earning EMS in Phase 0

### 4.1 Qualifying Phase 0 Activities

EMS hours may be logged for the following Phase 0 activities:

| Activity Category | Description | Verification Method |
|---|---|---|
| **Red-team and security testing** | Structured testing of treasury logic, reserve ratio enforcement, Treasury Reserve solvency gating, reversion trigger logic, EMS logging, fraud vectors, smart contract surfaces, Ms. Allis enforcement behavior | Logged findings submitted via designated channels; system monitor attestation |
| **UX and onboarding testing** | Testing wallet creation, UEI issuance, Commons app flows, and Ms. Allis chatbot interactions | Session logs + tester attestation |
| **Governance document review** | Structured review and feedback on Program Rules, DAO Charter, Phase 1 Spec, Terms and Conditions | Written feedback submitted via designated channels |
| **Community anchor activities** | Real qualifying commons activities (caregiving, mapping, cultural work, education) performed during Phase 0 by community anchor participants | Standard Phase 1 verification methods (partner attestation, geo-fence, task confirmation) |
| **Incident response participation** | Participation in post-incident reviews, playbook development, and corrective action documentation | System monitor attestation |

### 4.2 EMS Rate During Phase 0

- **Recognition rate:** 1 EMS hour per 1 documented qualifying hour — same as Phase 1.
- **Conversion to spendable M$:** Disabled by default during Phase 0 (see Section 3.3).
- All EMS logged in Phase 0 carries forward to Phase 1 at stable baseline exchange value and counts toward voting eligibility, role eligibility, and rank progression.
- No Phase 0 EMS balance carries a vested appreciation right or conversion right to fiat.

---

## 5. Red-Team Scope and Responsible Disclosure

### 5.1 What Community Champions May Test

Red-team participants are authorized to attempt to identify vulnerabilities in:

- Reserve ratio calculation and reporting logic.
- Treasury Reserve solvency ratio calculation (Reserve ÷ (Total EMS + M$)).
- EMS buying-power expansion gate logic — confirming gates are inactive below thresholds.
- Reversion trigger logic — confirming automatic reversion when reserve falls below applicable floor.
- EMS logging accuracy and tamper-resistance.
- Per-user cap enforcement and bypass vectors.
- Promo pool logic and bonus rule exploitation.
- UEI identity and anti-sybil mechanisms.
- Ms. Allis enforcement behavior and hard trigger logic.
- Three-box structural boundary — any path that could route founder value through H4H or EMS.
- Privacy and access control surfaces.
- Smart contract logic on Arbitrum One.
- IPFS record integrity.
- Conflict-of-interest recusal documentation completeness.

### 5.2 What Is Out of Scope

- Attacks against real user data beyond authorized test accounts.
- Disabling or circumventing hard safety triggers (observing trigger behavior is in scope; disabling is not).
- Testing against production systems without system monitor authorization.
- Social engineering of Harmony for Hope staff or community participants.
- Any action that would create or imply a founder equity right through H4H or EMS systems.

### 5.3 Responsible Disclosure Process

All findings must be reported through the designated security disclosure channel defined in [SECURITY-OVERVIEW.md](../security/SECURITY-OVERVIEW.md) and [CONTRIBUTING.md](../security/CONTRIBUTING.md).

- **Critical findings** (reserve ratio bypass, uncapped minting, hard trigger disable, structural-boundary breach, appreciation-gate bypass): report within 24 hours; system monitors respond within 24 hours.
- **High findings**: report within 72 hours; response within 72 hours.
- **Medium/low findings**: report in weekly batch; response within 7 days.

All findings are logged, credited as EMS hours, and incorporated into the pre-launch hardening audit.

---

## 6. Phase 0 → Phase 1 Graduation Criteria

Phase 0 ends and Phase 1 public launch may begin **only when ALL of the following are satisfied:**

| Criterion | Requirement |
|---|---|
| **Security audit complete** | All critical and high findings resolved or formally accepted with documented mitigation |
| **Hard trigger validation** | Ms. Allis reserve ratio enforcement, cap tightening, and hard trigger logic independently verified across all reserve bands |
| **Treasury Reserve solvency gating validated** | Buying-power expansion gates confirmed inactive; reversion trigger logic confirmed operational |
| **Three-box structural boundary confirmed** | No founder equity path through H4H or EMS; structural separation confirmed in writing |
| **EMS logging integrity** | Recognition ledger accuracy and tamper-resistance confirmed; all Phase 0 balances recorded at stable baseline value |
| **Legal review** | Terms and Conditions, Program Rules, FA-001 Fee Amendment, FTIS-001, and Phase 1 Economic Safety Specification reviewed by qualified legal counsel and approved for production |
| **Governance documents** | DAO Governance Charter, Phase 1 Spec, Program Rules, KPI Specification v3.0, and Parameter Tables finalized and published |
| **Harmony for Hope board authorization** | Formal board vote authorizing Phase 1 public launch |
| **Minimum Phase 0 cohort** | At least 10 Community Champions with logged EMS hours and verified findings on record |
| **KTS entity status documented** | KTS formation status confirmed in writing (formed or not-yet-formed) and reflected accurately in all live documents |
| **Treasury Reserve-funded costs confirmed** | All Treasury Reserve-funded formation and procurement costs itemized and confirmed paid before any Phase 2 appreciation gate can be evaluated |
| **Treasury baseline published** | Documented starting treasury balance, total EMS + M$ outstanding, and Treasury Reserve solvency ratio published before first public user is onboarded |
| **Conflict-of-interest documentation on file** | Recusal documentation complete for all related-party approvals |

---

## 7. Governance During Phase 0

Phase 0 is **not a DAO-governed period.** Harmony for Hope's Board of Directors and designated system monitors hold all governance authority during Phase 0.

- DAO voting is not active during Phase 0.
- System monitors may adjust parameters, issue invitations, revoke access, and respond to incidents under documented authority.
- Any parameter change that affects EMS appreciation gate thresholds, reserve solvency ratio floors, or reversion trigger conditions requires board-level approval and conflict-of-interest recusal documentation before taking effect.
- All Phase 0 decisions are logged and will be published as part of the pre-launch audit trail available to Phase 1 participants.
- Community Champions may submit structured feedback and recommendations, which system monitors are expected to consider and respond to in writing.

---

## 8. Transparency and Audit

Consistent with P9 (Transparency and traceability):

- All Phase 0 wallets issued, EMS hours logged, findings submitted, and parameter changes made are recorded.
- A **Phase 0 Pre-Launch Audit Report** will be published before Phase 1 opens, summarizing: wallets issued, EMS hours logged, findings by severity, resolutions, any parameters adjusted as a result of testing, Treasury Reserve solvency ratio at Phase 0 close, and EMS buying-power expansion status at Phase 1 launch.
- The audit report becomes part of the permanent governance record and is available to all Phase 1 participants.
- The template for this report is maintained at [MountainShares Phase 0 Pre-Launch Audit Report Template.md](MountainShares%20Phase%200%20Pre-Launch%20Audit%20Report%20Template.md).

---

## 9. Relationship to Other Documents

| Document | Relationship |
|---|---|
| [DAO Governance Charter](MountainShares%20DAO%20Governance%20Charter.md) | Phase 0 defined in Section 7.2; Community Champions defined in Section 2.5.4 |
| [Phase 1 Economic Safety Specification](MountainShares%20Phase%201%3A%20Economic%20Safety%20Specification.md) | Phase 0 graduation criteria must be met before Phase 1 activates |
| [Program Rules (Draft)](MountainShares%20Program%20Rules(Draft).md) | Phase 0 EMS earning rules incorporated by reference from Section 4 |
| [KPI Specification v3.0](MountainShares%20KPI%20Specification.md) | Phase 0 does not count toward Phase 1 KPI targets; KPI measurement begins at Phase 1 public launch; Treasury Reserve Solvency KPI tracked from Phase 0 close |
| [FA-001 Fee Amendment](../contract/H4H/Fee%20Amendment%20-%20FA001.md) | Establishes three-box structure, 704 Main Street correction, KTS entity status, and Treasury Reserve formation-cost funding |
| [Security Overview](../security/SECURITY-OVERVIEW.md) | Responsible disclosure process and security architecture |
| [Terms and Conditions](Terms%20and%20Conditions.md) | Phase 0 participants bound by Terms; no public offering during Phase 0 |
| [Pre-Launch Audit Report Template](MountainShares%20Phase%200%20Pre-Launch%20Audit%20Report%20Template.md) | Companion document; completed before Phase 1 launch |

---

*"The commons is built before it is opened. Phase 0 is the building."*

*MountainShares Phase 0: Invite-Only Beta Specification — Version 2.0*
*Harmony for Hope, Inc. | 704 Main Street, Mount Hope, WV 25880*
*Draft — Subject to H4H board review and legal counsel approval before reliance*
