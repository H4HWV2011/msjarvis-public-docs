# MountainShares Phase 0: Invite-Only Beta Specification

> **Disciplinary Context: Appalachian Economic Commons**
> This document instantiates Polymathmatic Geography principles P1, P9, P16, and related axioms for the Appalachian economic commons:
> - **P1 – Every where is entangled / Leakage and enclosure:** Phase 0 is the first moment the closed-loop system touches real place — real wallets, real UEIs, real EMS hours logged against real people and geographies in West Virginia. Every design choice here shapes leakage and enclosure patterns in Phase 1 and beyond. See https://github.com/H4HWV2011/msAllis-public-docs/blob/main/docs/Polymathmatical-Geography.md
> - **P9 – Transparency and traceability:** All Phase 0 activity — wallets issued, EMS hours logged, red-team findings, security incidents, and parameter changes — is logged in the recognition ledger and auditable. Nothing in Phase 0 is invisible.
> - **P16 – Power accountable to place:** Phase 0 is governed by Harmony for Hope's board and designated system monitors under documented authority. Community Champions earn governance standing through logged hours, not invitation status alone.
> - **Anti-leakage and closed-loop spending:** Phase 0 deliberately restricts EMS-to-spendable-M$ conversion and prohibits external cash-out to protect the closed loop before the treasury is sufficiently backed. PMS loads may be enabled for select participants on a case-by-case basis under system monitor approval.
> - **Bounty and corrective programs:** Red-team and security testing in Phase 0 is the first structured bounty program — logged, rewarded with EMS, and used to harden the system before public launch.

**Version:** 1.0 (Draft)
**Date:** March 12, 2026
**Status:** DAO Governance Document — Pre-Launch Draft
**Scope:** West Virginia Pilot — Invite-Only Beta
**Incorporated by reference into:** MountainShares DAO Governance Charter (Section 7.2), MountainShares Phase 1 Economic Safety Specification, MountainShares Program Rules

---

## 1. Purpose and Scope

Phase 0 is the **invite-only beta period** that precedes public launch of MountainShares and The Commons. Its purposes are:

- Issue and test real wallets, UEIs, and EMS recognition against production or near-production infrastructure.
- Identify and harden security vulnerabilities, reserve-ratio logic errors, fraud vectors, and UX friction points before public participants are exposed.
- Build the first cohort of Community Champions who understand the system deeply and can serve as stewards, captains, and red-team elders as the community grows.
- Accumulate real EMS hours in the recognition ledger that count toward Phase 1 governance eligibility.
- Validate Ms. Allis enforcement behavior — reserve ratio calculations, tier assignments, hard trigger logic, and dashboard accuracy — in a live environment before public launch.

Phase 0 does **not** constitute public availability of MountainShares. No public marketing, open registration, or general solicitation occurs during Phase 0.

---

## 2. Phase 0 Participants

### 2.1 Who Is Invited

Phase 0 participants are selected by Harmony for Hope and designated system monitors. Invitation categories include:

- **Security and red-team participants** — developers, systems testers, and security researchers invited to probe treasury logic, EMS logging, reserve ratio enforcement, smart contract surfaces, and Ms. Allis behavior.
- **Community anchor participants** — local trusted community members, nonprofit partners, and local business representatives in the Mount Hope area invited to test real-world UX, onboarding flows, and EMS earning activities.
- **Internal team participants** — Harmony for Hope staff, KTS technical contributors, and governance document reviewers.

### 2.2 What Phase 0 Participants Receive

Upon invitation and acceptance:

- A **MountainShares wallet** tied to a unique **UEI** (Unique Entity Identifier).
- Authenticated access to The Commons app and the Ms. Allis chatbot UI via secure, non-public links.
- Access to Phase 0 documentation, testing guides, and red-team scope documents.
- EMS hours logged in the **recognition ledger** for qualifying Phase 0 activities (see Section 4).

### 2.3 Community Champions

Phase 0 security and red-team participants may be designated as **Community Champions** under Section 2.5.4 of the DAO Governance Charter. This designation:

- Recognizes their foundational role in hardening the system.
- Gives them founding governance eligibility (1 UEI = 1 vote) once standard eligibility criteria are met (30 days account age + 10 EMS hours).
- Does **not** grant extra voting weight, override capability, or exemption from hard safety triggers.
- Does **not** create any financial right, equity interest, or expectation of profit.

---

## 3. Economic Rules During Phase 0

Phase 0 operates under the most conservative economic parameters in the MountainShares lifecycle.

### 3.1 Recognition Ledger — Active

All qualifying Phase 0 activity is logged in the **unlimited recognition ledger** with full UEI, geo, org, and timestamp metadata. These hours are permanent and carry forward into Phase 1 and beyond.

### 3.2 Spendable M$ — Severely Restricted

| Parameter | Phase 0 Value | Notes |
|-----------|--------------|-------|
| EMS → M$ conversion | **Disabled by default** | No spendable M$ issued from EMS during Phase 0 except by explicit system monitor authorization for testing purposes |
| PMS loads (USD → M$) | **Restricted — by invitation only** | Enabled only for specific test scenarios; all loads are monitored |
| Per-user spendable cap | **Test amounts only** | Not the Phase 1 production caps; set per test scenario |
| Cash-out / ATM | **Disabled** | No fiat conversion of any kind during Phase 0 |
| Benefits-Sensitive Accounts | **All accounts treated as benefits-sensitive by default** | Maximum protection during beta |

### 3.3 Hard Triggers — Fully Active

Ms. Allis enforces **all hard economic safety triggers** during Phase 0, including reserve ratio monitoring, automatic cap tightening, fraud flagging, and safety prohibitions. These cannot be disabled for testing purposes. Testing of hard trigger behavior is conducted by **observing trigger responses**, not by disabling them.

### 3.4 No External Cash Value

Phase 0 MountainShares — whether EMS hours in the recognition ledger or any test spendable M$ — carry **no external cash value** and no right to redemption. Phase 0 EMS hours count toward governance eligibility and rank only.

---

## 4. Earning EMS in Phase 0

### 4.1 Qualifying Phase 0 Activities

EMS hours may be logged for the following Phase 0 activities:

| Activity Category | Description | Verification Method |
|-------------------|-------------|-------------------|
| **Red-team and security testing** | Structured testing of treasury logic, reserve ratio enforcement, EMS logging, fraud vectors, smart contract surfaces, Ms. Allis enforcement behavior | Logged findings submitted via designated channels; system monitor attestation |
| **UX and onboarding testing** | Testing wallet creation, UEI issuance, Commons app flows, and Ms. Allis chatbot interactions | Session logs + tester attestation |
| **Governance document review** | Structured review and feedback on Program Rules, DAO Charter, Phase 1 Spec, Terms and Conditions | Written feedback submitted via designated channels |
| **Community anchor activities** | Real qualifying commons activities (caregiving, mapping, cultural work, education) performed during Phase 0 by community anchor participants | Standard Phase 1 verification methods (partner attestation, geo-fence, task confirmation) |
| **Incident response participation** | Participation in post-incident reviews, playbook development, and corrective action documentation | System monitor attestation |

### 4.2 EMS Rate During Phase 0

- **Recognition rate:** 1 EMS hour per 1 documented qualifying hour — same as Phase 1.
- **Conversion to spendable M$:** Disabled by default during Phase 0 (see Section 3.2).
- All EMS logged in Phase 0 carries forward to Phase 1 and counts toward voting eligibility, role eligibility, and rank progression.

---

## 5. Red-Team Scope and Responsible Disclosure

### 5.1 What Community Champions May Test

Red-team participants are authorized to attempt to identify vulnerabilities in:

- Reserve ratio calculation and reporting logic.
- EMS logging accuracy and tamper-resistance.
- Per-user cap enforcement and bypass vectors.
- Promo pool logic and bonus rule exploitation.
- UEI identity and anti-sybil mechanisms.
- Ms. Allis enforcement behavior and hard trigger logic.
- Privacy and access control surfaces.
- Smart contract logic on Arbitrum One.
- IPFS record integrity.

### 5.2 What Is Out of Scope

- Attacks against real user data beyond authorized test accounts.
- Disabling or circumventing hard safety triggers (observing trigger behavior is in scope; disabling is not).
- Testing against production systems without system monitor authorization.
- Social engineering of Harmony for Hope staff or community participants.

### 5.3 Responsible Disclosure Process

All findings must be reported through the designated security disclosure channel defined in [SECURITY-OVERVIEW.md](../security/SECURITY-OVERVIEW.md) and [CONTRIBUTING.md](../security/CONTRIBUTING.md).

- **Critical findings** (reserve ratio bypass, uncapped minting, hard trigger disable): report within 24 hours; system monitors respond within 24 hours.
- **High findings**: report within 72 hours; response within 72 hours.
- **Medium/low findings**: report in weekly batch; response within 7 days.

All findings are logged, credited as EMS hours, and incorporated into the pre-launch hardening audit.

---

## 6. Phase 0 → Phase 1 Graduation Criteria

Phase 0 ends and Phase 1 public launch may begin **only when ALL of the following are satisfied:**

| Criterion | Requirement |
|-----------|-------------|
| **Security audit complete** | All critical and high findings resolved or formally accepted with documented mitigation |
| **Hard trigger validation** | Ms. Allis reserve ratio enforcement, cap tightening, and hard trigger logic independently verified across all reserve bands |
| **EMS logging integrity** | Recognition ledger accuracy and tamper-resistance confirmed |
| **Legal review** | Terms and Conditions, Program Rules, and Phase 1 Economic Safety Specification reviewed by qualified legal counsel and approved for production |
| **Governance documents** | DAO Governance Charter, Phase 1 Spec, Program Rules, KPI Specification, and Parameter Tables finalized and published |
| **Harmony for Hope board authorization** | Formal board vote authorizing Phase 1 public launch |
| **Minimum Phase 0 cohort** | At least 10 Community Champions with logged EMS hours and verified findings on record |
| **Treasury baseline** | Documented starting treasury balance and reserve ratio published before first public user is onboarded |

---

## 7. Governance During Phase 0

Phase 0 is **not a DAO-governed period.** Harmony for Hope's Board of Directors and designated system monitors hold all governance authority during Phase 0.

- DAO voting is not active during Phase 0.
- System monitors may adjust parameters, issue invitations, revoke access, and respond to incidents under documented authority.
- All Phase 0 decisions are logged and will be published as part of the pre-launch audit trail available to Phase 1 participants.
- Community Champions may submit structured feedback and recommendations, which system monitors are expected to consider and respond to in writing.

---

## 8. Transparency and Audit

Consistent with P9 (Transparency and traceability):

- All Phase 0 wallets issued, EMS hours logged, findings submitted, and parameter changes made are recorded.
- A **Phase 0 Pre-Launch Audit Report** will be published before Phase 1 opens, summarizing: wallets issued, EMS hours logged, findings by severity, resolutions, and any parameters adjusted as a result of testing.
- The audit report becomes part of the permanent governance record and is available to all Phase 1 participants.
- The template for this report is maintained at [MountainShares Phase 0 Pre-Launch Audit Report Template.md](MountainShares%20Phase%200%20Pre-Launch%20Audit%20Report%20Template.md).

---

## 9. Relationship to Other Documents

| Document | Relationship |
|----------|--------------|
| [DAO Governance Charter](MountainShares%20DAO%20Governance%20Charter.md) | Phase 0 defined in Section 7.2; Community Champions defined in Section 2.5.4 |
| [Phase 1 Economic Safety Specification](MountainShares%20Phase%201%3A%20Economic%20Safety%20Specification.md) | Phase 0 graduation criteria must be met before Phase 1 activates |
| [Program Rules (Draft)](MountainShares%20Program%20Rules(Draft).md) | Phase 0 EMS earning rules incorporated by reference from Section 4 |
| [KPI Specification](MountainShares%20KPI%20Specification.md) | Phase 0 does not count toward Phase 1 KPI targets; KPI measurement begins at Phase 1 public launch |
| [Security Overview](../security/SECURITY-OVERVIEW.md) | Responsible disclosure process and security architecture |
| [Terms and Conditions](Terms%20and%20Conditions.md) | Phase 0 participants bound by Terms; no public offering during Phase 0 |
| [Pre-Launch Audit Report Template](MountainShares%20Phase%200%20Pre-Launch%20Audit%20Report%20Template.md) | Companion document; completed before Phase 1 launch |

---

*"The commons is built before it is opened. Phase 0 is the building."*
