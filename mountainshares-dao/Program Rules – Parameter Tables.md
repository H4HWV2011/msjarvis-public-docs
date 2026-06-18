# Program Rules – Parameter Tables

> **Disciplinary Context: Appalachian Economic Commons**
> This document instantiates Polymathmatic Geography principles P1, P9, P16, and related axioms for the Appalachian economic commons:
> - **P1 – Every where is entangled / Leakage and enclosure:** Sections 1–7 treat EMS→M$ rates, caps, fees, reserve bands, and governance thresholds as one integrated instrument that shapes how value circulates and where leakage or enclosure pressures arise.
> - **P9 – Transparency and traceability:** The tabular parameters for conversion, reserve bands, internal buying power, fees, and limits make the "knobs" of the system inspectable, so communities can see exactly how rules translate into numeric constraints.
> - **P16 – Power accountable to place:** Governance thresholds, band-based permissions, and benefits-sensitive limits tie parameter changes and risk controls to explicit conditions in the West Virginia pilot, ensuring that institutional power responds to local reserves, usage, and sensitivity to benefits.
> - **Anti-leakage and closed-loop spending:** Conversion caps, reserve-ratio bands, internal phase schedules, and promo-pool limits collectively aim to keep value recirculating in the closed loop rather than spilling out via over-minting or unbounded cash-outs.
> - **Bounty and corrective programs:** Promo-pool parameters and governance thresholds encode how targeted bonuses or "bounty-like" incentives can be safely activated or throttled in response to reserve bands and community decisions.

**Version:** 3.0
**Date:** June 17, 2026
**Status:** DAO Governance Document — Structural Rewrite (securities framing + money-services relocation)
**Scope:** West Virginia Statewide (Phase 1 baseline; Phase 2 and Phase 3 parameters included)
**Related documents:** Phase 1 Specification, Phase 2 Specification, Phase 3 Specification, Program Rules, DAO Governance Charter, KPI Specification v3.0, H4H Canonical Facts Sheet, EMS Securities Treatment — Counsel Prep, Money-Services Entity Relocation Map

> **DRAFT – LIVE PARAMETERS SUBJECT TO CHANGE**
> This document presents the current operational parameters for MountainShares across all active phases (West Virginia pilot). It is incorporated by reference into `Program Rules.md` and each Phase Specification. In case of conflict, the applicable Phase Specification and Terms and Conditions control.

> **Entity Status Notice:** Kidd's Technical Services ("KTS") is not yet a registered West Virginia LLC and has no EIN. References to "KTS" in this document mean Carrie Ann Kidd personally, operating under that trade name. Formation of the WV LLC is the gating step before founder equity, ALLIS IP holding, and KTS-side capitalization instruments take legal effect. No parameter in this document creates a founder equity path through H4H or community EMS.

> **Server Location Notice:** The operational server cluster and Ms. Allis / ALLIS node for H4H and MountainShares Commons is located at **704 Main Street, Mount Hope, West Virginia 25880** (Fayette County Community Arts Center).

> **Money-Services Notice:** The **MountainShares DAO / DUNA is the licensee of record** for money transmission (WV Money Transmitter License) and FinCEN Money Services Business registration; it holds the surety bond, runs the BSA/AML program, and receives the money-services Treasury Reserve draw. **Harmony for Hope, Inc. is not the money transmitter.** This structure is contingent on counsel confirming a license is required and that the WV Division of Financial Institutions will license the DUNA directly; otherwise a separate DUNA-controlled licensed entity substitutes for "DUNA."

> **EMS Conversion — Governing Rule:** Community EMS maintains a stable baseline exchange value. Phase-based buying-power expansion rates are **inactive** unless and until the Treasury Reserve achieves the applicable solvency threshold (300% at Phase 2; 500% at Phase 3), all Treasury Reserve-funded transition and formation costs have been paid, and no reversion event has occurred. These rates are conditional, revocable, and not vested, and are realized only through participant-elected conversion; no resident holds a vested or guaranteed right to any buying-power rate. EMS confers no equity, ownership, membership interest, or profit-sharing interest in H4H, the DUNA, KTS, or any entity. **The securities-law treatment of EMS, M$, and the phase-based conversion mechanism is under review by securities counsel; this document makes no representation as to whether any of these is or is not a security or investment contract.** Any appreciating founder-side instrument exists exclusively on the KTS side under separate, counsel-reviewed documentation.

---

## Structural Framework

This document operates within the three-box entity structure governing MountainShares.

| Entity | Role | Parameter Relevance |
|---|---|---|
| Harmony for Hope, Inc. (H4H) | 501(c)(3) charitable anchor; program sponsor | Receives 30% of fee revenue (Bucket 1); maintains **its own** nonprofit compliance (Form 990, WV SOS annual report, registered agent, charitable registration). **Not the money transmitter.** |
| MountainShares Commons / DUNA | Community-owned mutual-credit ledger and governance layer **and licensed money-services function** | EMS→M$ rates, per-user caps, reserve band table, promo pool, governance thresholds; **licensee of record for WV MTL + FinCEN MSB; receives the money-services Treasury Reserve draw (Stream M)** |
| Kidd's Technical Services (KTS) | To-be-formed for-profit LLC/PBC; founder-owned commercial engine | Ms. Allis / ALLIS deployment at 704 Main Street; founder-side rights documented separately; no equity path through EMS or H4H; holds no money-services license |

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 1.0 | March 16, 2026 | Initial release — Phase 1 parameter tables, reserve bands, fee structure, governance thresholds |
| 2.0 | June 17, 2026 | **STRUCTURAL REWRITE:** Added three-box structural framework; added Phase 2 and Phase 3 parameter tables; replaced hardcoded Phase 3 rate ($34.70 / $36.14) with Federal Volunteer Service Rate (FVSR) defined term; corrected dual reserve metric framework; added reversion cascade language; added KTS entity status notice; corrected server location to 704 Main Street |
| 3.0 | June 17, 2026 | **STRUCTURAL REWRITE:** Removed all "non-appreciating in the securities-law sense" assertions (own-the-appreciation decision; securities treatment placed under counsel review with no self-certified legal conclusion); relocated money-services licensing from H4H to the **MountainShares DAO / DUNA** as licensee of record; reframed Section 8 compliance draws into Stream N (H4H nonprofit) and Stream M (DUNA money-services); softened the EMS Recognition Bonus income/asset claim to benefits-counsel review; aligned with Phase 2 v3.0, Phase 3 v3.0, EMS Securities Treatment — Counsel Prep, and Money-Services Entity Relocation Map |

---

## 1. EMS → M$ Conversion Parameters (All Phases)

### 1.1 Global Base Rate by Phase

| Phase | Global Base Rate Floor | Global Base Rate Ceiling | Activation Condition |
|---|---|---|---|
| **Phase 1** | 0.10 M$ / EMS hour | 1.00 M$ / EMS hour | Default launch phase |
| **Phase 2** | 0.50 M$ / EMS hour | 2.00 M$ / EMS hour | Operational Reserve Ratio ≥ 3.0 for 30+ consecutive days |
| **Phase 3** | 1.00 M$ / EMS hour | 3.00 M$ / EMS hour | Operational Reserve Ratio ≥ 5.0 for 30+ consecutive days; Treasury Reserve Solvency Ratio ≥ 500% |

Ms. Allis recalculates the reserve ratio daily and applies the appropriate band at the next epoch. The ceiling rate in each phase is unlocked only via DAO vote at the applicable reserve threshold — it is not automatic.

### 1.2 Per-User Convertible Caps (Spendable M$ per Month)

#### Phase 1

| Tier | Description | Monthly Cap (M$) | Weekly Guidance | Daily Guidance |
|---|---|---|---|---|
| **Tier 1** | General commons participants | 40 M$ | ≈ 10 hrs | ≈ 1–2 hrs |
| **Tier 2** | Verified EMS (caregiving, high-need roles; geo+UEI validated) | 80 M$ | ≈ 20 hrs | ≈ 4 hrs |

#### Phase 2

| Tier | Description | Monthly Cap (M$) | Weekly Guidance | Daily Guidance |
|---|---|---|---|---|
| **Tier 1** | General commons participants | 80 M$ | 20 hrs | 3–4 hrs |
| **Tier 2** | Verified EMS, caregiving, high-need community roles (geo+UEI validated) | 160 M$ | 40 hrs | 8 hrs |
| **Tier 3** | Regional Champion, governance leadership, data stewardship anchor (DAO-confirmed) | 240 M$ | 60 hrs | 12 hrs |

#### Phase 3

| Tier | Description | Monthly Cap (M$) | Weekly Guidance | Daily Guidance |
|---|---|---|---|---|
| **Tier 1** | General commons participants | 120 M$ | 30 hrs | 6 hrs |
| **Tier 2** | Verified EMS, caregiving, high-need community roles (geo+UEI validated) | 240 M$ | 60 hrs | 12 hrs |
| **Tier 3** | Regional Champion, governance leadership, data stewardship anchor (DAO-confirmed) | 360 M$ | 90 hrs | 18 hrs |

> Weekly and daily values are guidelines derived from the current base rate ceiling and may be applied as separate hard caps where specified in the applicable Phase Specification.

---

## 2. Reserve Ratio Bands and Automatic Adjustments

### 2.1 Reserve Metrics

**Operational Reserve Ratio** governs day-to-day continuity of service, per-user caps, and phase commerce feature unlocks:

```
Operational Reserve Ratio = Treasury USDC Reserve / Total Outstanding Spendable PMS (M$)
```

**Treasury Reserve Solvency Ratio** governs EMS buying-power expansion and is the primary conversion gate:

```
Treasury Reserve Solvency Ratio = Treasury Reserve / (Total Outstanding EMS + Total Outstanding M$)
```

Both metrics are calculated daily by Ms. Allis, published on the dashboard with green/amber/red bands, and enforced by the Phase Management Controller.

### 2.2 Phase 1 Band Table

| Band | Operational Reserve Ratio | Base Rate Range (M$/EMS hr) | Tier 2 Cap (M$/mo) | Promo State | Governance Permissions |
|---|---|---|---|---|---|
| **A** | ≥ 1.50 | 1.00 | up to 120 | Enabled | May propose limited increases |
| **B** | 1.00 – 1.49 | 0.50 – 0.80 | 80 – 100 | Reduced | May adjust upward if trend stable |
| **C** | 0.75 – 0.99 | 0.20 – 0.40 | 40 – 80 | Paused | May hold steady only |
| **D** | < 0.75 | 0.10 | 20 – 40 | Frozen | No increases; automatic tightening |

### 2.3 Phase 2 Band Table

| Operational Reserve Ratio | Treasury Reserve Solvency Ratio | Global Base Rate | Tier 1 Cap | Tier 2 Cap | Tier 3 Cap | Stage 3 Commerce | EMS Buying-Power Status | Action |
|---|---|---|---|---|---|---|---|---|
| ≥ 3.0 | ≥ 300% | 1.5–2.0 M$/hr (DAO vote) | 80 M$/mo | 160 M$/mo | 240 M$/mo | Fully unlocked | Conditionally active — 1 EMS = $10 | DAO may vote to increase rate toward 2.0 |
| 2.0 – 2.99 | ≥ 300% | 1.0–1.5 M$/hr | 80 M$/mo | 120 M$/mo | 180 M$/mo | Unlocked (monitored) | Conditionally active | DAO can vote to hold or increase if trend stable |
| 1.5 – 1.99 | ≥ 300% | 0.5–1.0 M$/hr | 80 M$/mo | 100 M$/mo | 140 M$/mo | Stage 2 only | Conditionally active | DAO can vote to hold steady; Stage 3 gated |
| < 1.5 | Any | Phase 1 thresholds reactivate | Phase 1 caps | Phase 1 caps | Tier 3 paused | Stage 2 only | Suspended | Auto-revert to Phase 1 safety rules |
| Any | < 300% | Phase 1 thresholds reactivate | Phase 1 caps | Phase 1 caps | Tier 3 paused | Stage 2 only | **Reverted to Phase 1** | Automatic reversion; no vote required |

### 2.4 Phase 3 Band Table

| Operational Reserve Ratio | Treasury Reserve Solvency Ratio | Global Base Rate | Dividend Clock | EMS Buying-Power Status | Compliance Draws | Action |
|---|---|---|---|---|---|---|
| ≥ 5.0 | ≥ 500% | 2.0–3.0 M$/hr (DAO vote) | Running | Conditionally active — 1 EMS = FVSR | Available per Phase 3 §7A | DAO may vote to increase rate toward 3.0; surplus accumulates |
| 4.0 – 4.99 | ≥ 500% | 1.5–2.0 M$/hr | Paused | Conditionally active | Queued per deferral rules | No new distributions; DAO notified |
| 3.0 – 3.99 | ≥ 500% | Phase 2 rates reactivate | Paused + alert | Conditionally active (P2 rate) | Queued per deferral rules | Phase 2 thresholds govern; emergency review |
| < 3.0 | Any | Phase 1/2 recovery rules | Paused + emergency | Phase 2 or P1 reversion | Emergency session required | Full emergency protocol |
| Any | < 500% | Phase 2 rates reactivate | Paused | **Reverted to Phase 2** | Queued | Automatic reversion; no vote required |
| Any | < 300% | Phase 1 rates reactivate | Paused + emergency | **Reverted to Phase 1** | Emergency session required | Automatic reversion; full emergency protocol |

---

## 3. EMS Buying-Power Expansion Schedule (Phase-Gated)

> The schedules below are reserve-gated, deferred, conditional, and subject to automatic reversion. No resident holds a vested conversion right prior to threshold clearance, and EMS confers no equity or ownership interest. The securities-law treatment of EMS and the phase-based conversion schedule is under review by securities counsel; this document makes no representation as to whether it is or is not a security or investment contract.

| Phase | EMS Buying-Power Rate | Activation Gate | Reversion Trigger |
|---|---|---|---|
| **Phase 1** | 1 EMS = $1.00 USD equivalent (baseline) | Default | N/A |
| **Phase 2** | 1 EMS = $10.00 USD equivalent (10×) | Treasury Reserve Solvency Ratio ≥ 300% + all formation fees paid | Ratio drops below 300% → automatic reversion to Phase 1 rate |
| **Phase 3** | 1 EMS = **FVSR** (Federal Volunteer Service Rate in effect on Phase 3 activation date) | Treasury Reserve Solvency Ratio ≥ 500% + all prior-phase transition costs paid | Ratio drops below 500% → automatic reversion to Phase 2 rate; below 300% → automatic reversion to Phase 1 rate |

> **Federal Volunteer Service Rate (FVSR):** The IRS-published standard rate for valuing volunteer services, updated annually. The Phase 3 EMS buying-power rate is the FVSR in effect on the date the DAO formally activates Phase 3 — not the rate at document publication. The current rate (2026) is **$36.14**. If Phase 3 activates in a later year, the applicable rate is that year's published FVSR. The FVSR is published annually by the IRS and is publicly verifiable at no cost. Ms. Allis surfaces the current FVSR on the dashboard each calendar year. The DAO does not vote on the FVSR — it is an external, IRS-determined figure.

**Reversion cascade (automatic, no DAO vote required):**
- If Treasury Reserve Solvency Ratio falls below 500%: Phase 3 buying-power expansion reverts to Phase 2 rate ($10) immediately
- If Treasury Reserve Solvency Ratio falls below 300%: all buying-power expansion reverts to Phase 1 baseline ($1) immediately
- No resident loses their principal EMS balance in any reversion scenario
- The system re-advances to the higher rate only after the applicable threshold is restored for two consecutive quarters
- Each reversion is logged to the durable audit trail with timestamp, triggering metric, and applicable restored parameters

---

## 4. Fees and Promo Pool

### 4.1 Standard Fees

| Fee Type | Current Rate | Applies To |
|---|---|---|
| Load fee | 2.85% of fiat load | USD → PMS loads |
| Internal transfer fee | 0.25% | Eligible user-to-user transfers |
| Merchant fee | 1.80% | Eligible purchases at accepting merchants |
| ATM / refund fee | $1.25 USD (flat) | PMS cash-out transactions (where enabled, under the DUNA's licensed rails) |

### 4.2 Promo / Bonus Pool

| Parameter | Value / Range | Notes |
|---|---|---|
| Promo pool source | % of monthly processed volume | Allocated from fees / treasury |
| Promo pool target range | 2% – 5% of monthly volume | Phase 2 and Phase 3 upper bound raised to 5%; exact % set by DAO within safety limits |
| Monthly promo cap (M$) | Set by DAO per region | Hard cap to prevent overspend |
| Promo state per reserve band | Enabled / Reduced / Paused / Frozen | As per applicable phase band table (Sections 2.2, 2.3, 2.4) |

Bonuses pause automatically:
- Phase 1: when Operational Reserve Ratio < 0.75
- Phase 2: when Operational Reserve Ratio < 2.0
- Phase 3: when Operational Reserve Ratio < 4.0 or Treasury Reserve Solvency Ratio < 500%

### 4.3 Fee Revenue Allocation

All collected fee revenue (load fees, internal transfer fees, merchant fees, and ATM/refund fees) is allocated across five designated purposes according to the following fixed split. Every dollar of fee income serves a defined function within the MountainShares ecosystem and the broader Appalachian economic commons.

#### 4.3.1 Allocation Table

| Bucket | Allocation | Recipient / Purpose | Description |
|---|---|---|---|
| 1 | 30% | Harmony for Hope, Inc. (H4H Operations) | Covers nonprofit administration, staffing, compliance, legal, and program delivery costs |
| 2 | 30% | Treasury Reserve | Grows the MountainShares backing reserve; supports phase transition thresholds and liquidity |
| 3 | 15% | Platform Development | Funds ongoing development of The Commons app, Ms. Allis infrastructure, and technical systems |
| 4 | 15% | Community Programs | Supports structured programs: education, mutual aid, time-banking, cultural preservation, etc. |
| 5 | 10% | Community Projects | Funds member-initiated or DAO-approved local projects within the West Virginia commons |
| — | +0.55% | Treasury Reserve (Supplemental) | An additional 0.55% of gross transaction volume accrues directly to the Treasury Reserve |

> **Total standard split: 100% of collected fee revenue.**
> The +0.55% supplemental treasury reserve is assessed separately on gross transaction volume (not fee revenue) and is in addition to the 30% Treasury Reserve bucket above.

#### 4.3.2 Treasury Reserve Funding Sources

The Treasury Reserve (Bucket 2) is funded by the following streams:

- **30% of all collected fee revenue** (load fees, transfer fees, merchant fees, ATM fees)
- **+0.55% supplemental reserve assessment** on gross transaction volume
- **Merchant fees (1.80%)** — the merchant fee is a primary treasury-building mechanism; the 30% treasury share of this fee is routed to the reserve automatically at settlement
- **ATM / refund fee ($1.25 flat)** — the full $1.25 per cash-out transaction contributes to the treasury reserve pool via the standard 30% allocation

> **Design intent:** The combination of the 30% fee-revenue split and the +0.55% supplemental assessment creates a compounding reserve-growth mechanism. As transaction volume grows, the treasury grows proportionally, supporting the Phase 2 (300% Treasury Reserve Solvency Ratio) and Phase 3 (500% Treasury Reserve Solvency Ratio) thresholds defined in the applicable Phase Specifications.

#### 4.3.3 Governance and Adjustability

These allocation percentages are Program Rules parameters and may be adjusted through the DAO governance process defined in the MountainShares DAO Governance Charter, subject to:

- A minimum Treasury Reserve allocation of 20% (floor, not subject to ordinary DAO vote)
- A minimum H4H Operations allocation of 20% (floor, required for nonprofit sustainability)
- Any changes requiring a super-majority (66%) DAO vote and Board of Directors ratification
- Changes disclosed to Users per Section 10.3 of the Terms and Conditions (minimum 30 days notice)

---

## 5. PMS Load and Cash-Out Limits

> Exact figures to be set in consultation with payment partners and compliance counsel. The KYC tier structure below is the governing framework; numeric values are placeholders pending regulatory guidance. Cash-out is operated under the DUNA's licensed money-services rails.

| Limit Type | Tier / KYC Level | Phase 1 Value | Phase 2 Value | Phase 3 Value |
|---|---|---|---|---|
| Min load per transaction | All | $10 USD | $10 USD | $10 USD |
| Max load per transaction | Basic / Advanced / High | $200 / $1,000 / $5,000 | $500 / $2,500 / $10,000 | $1,000 / $5,000 / $25,000 |
| Max total load per month | By KYC tier | To be defined | To be defined | To be defined |
| Max PMS cash-out per transaction | By KYC tier | To be defined | To be defined | To be defined |
| Max PMS cash-out per month | By KYC tier | To be defined | To be defined | To be defined |

**Benefits-Sensitive Accounts:** PMS cash-out is disabled by default regardless of general limits. Exceptions are documented case-by-case. Phase 3 adds a 60-day advance notice requirement and EMS Recognition Bonus election option before any distribution event.

---

## 6. Benefits-Sensitive Account Thresholds

| Parameter | Phase 1 | Phase 2 | Phase 3 | Description |
|---|---|---|---|---|
| Balance warning threshold | 200 M$ | 400 M$ | 600 M$ | UI warns user to check impact on benefits |
| Hard soft-cap (throttle point) | 400 M$ | 800 M$ | 1,200 M$ | EMS earning slows or pauses above this level |
| PMS load allowed | No (default) | No (default) | No (default) | Exceptions documented case-by-case |
| EMS conversion timing | Participant-controlled | Participant-controlled | Participant-controlled; 60-day advance notice before distribution events |
| Distribution form | N/A | N/A | M$ credit (default); USD cash-out (optional); EMS Recognition Bonus (optional, irrevocable per event) |

> County-level variations may apply where legal counsel determines the statewide threshold is insufficient for a specific county benefit program mix. County-level variations are published in this table and reviewed quarterly. Because the phase-based conversion rates increase realizable value, whether a vaulted-but-convertible balance is a countable resource or income for benefits purposes is under benefits-counsel review and should be confirmed before reliance.

---

## 7. Governance Thresholds

| Parameter | Phase 1 | Phase 2 | Phase 3 | Description |
|---|---|---|---|---|
| Governance eligibility | 10 EMS hours + 30 days | 10 EMS hours + 30 days | 10 EMS hours + 30 days | To obtain 1 UEI vote (per DAO Governance Charter) |
| Quorum for key proposals | 30% of eligible UEIs | 35% of eligible UEIs | 40% of eligible UEIs | For rate/cap changes, phase transitions |
| Simple majority | 50%+1 | 50%+1 | 50%+1 | Standard DAO confirmation votes |
| Super-majority threshold | 66% | 66% | 66% | For structural or high-impact changes |
| Super-super-majority | N/A | N/A | 75% | Phase 3 only: surplus retention, phase initiation, distribution interval extension |
| County-scoped proposals | N/A | Active UEIs in that county only | Active UEIs in that county only | Only UEIs with verified presence in a county vote on single-county proposals |
| Tier 3 proposal submission | N/A | No co-sponsor required | No co-sponsor required | All other tiers require 2+ co-signers |
| Hard trigger overrides | Not permitted at any threshold | Not permitted at any threshold | Not permitted at any threshold | Hard triggers are automatic and non-overridable by any vote |

> All numeric values above are subject to revision via governance, within the bounds of the applicable Phase Specification and Terms and Conditions.

---

## 8. Compliance Draw Thresholds (Two Streams, All Phases)

> Compliance funding runs in two streams. **Stream N — H4H Nonprofit Compliance:** Form 990, WV SOS annual report, registered agent, charitable registration; funded from H4H's 30% operational allocation; exception draws only. **Stream M — DUNA Money-Services Licensing:** WV MTL, surety bond, FinCEN MSB, BSA/AML program; the **MountainShares DAO / DUNA is the licensee of record and the applicant**, funded from the Treasury Reserve to the DUNA. The draw-size governance thresholds below apply to both streams. The reserve floor against which draws are calculated changes by phase (3.0 at Phase 2; 5.0 at Phase 3). Full draw process and eligible expenditure categories are defined in Section 7A of each Phase Specification.

| Draw Amount | Comment Window | Approval Required | Reserve Floor Check |
|---|---|---|---|
| ≤ $10,000 | 72-hour community comment window | No vote required if no objection passes | Ms. Allis verifies floor is maintained after draw |
| $10,001 – $50,000 | 7-day community comment window | Simple majority DAO confirmation vote | Ms. Allis verifies floor is maintained after draw |
| > $50,000 | 14-day community comment window | 66% super-majority DAO vote | Ms. Allis verifies floor is maintained after draw |
| Any — floor breach | N/A — draw deferred automatically | Deferred to deferral queue | Ms. Allis queues draw; fires automatically when floor is maintainable |

> Annual Budget Pre-Approval: If the DUNA's Annual Money-Services Compliance Budget (Stream M) is DAO-approved, individual draws within approved categories and amounts may proceed through the 72-hour window regardless of size, provided Ms. Allis verification passes. H4H's Stream N nonprofit compliance is funded from its 30% operational allocation.

---

## 9. Phase Graduation Criteria (Summary)

> Full binding criteria are defined in each Phase Specification. This table is a navigation aid only.

| Criterion | Phase 1 → Phase 2 | Phase 2 → Phase 3 |
|---|---|---|
| Operational Reserve Ratio | ≥ 1.25 stable for 60+ consecutive days | ≥ 3.0 stable for 90+ consecutive days |
| Treasury Reserve Solvency Ratio | ≥ 300% for 2+ consecutive quarters | ≥ 500% for 2+ consecutive quarters |
| Prior-phase formation fees paid | Yes — required before Phase 2 EMS rate activates | Yes — required before Phase 3 FVSR rate activates |
| Active UEIs | ≥ 500 across ≥ 3 counties | ≥ 10,000 across ≥ 10 counties |
| Monthly processed volume | To be defined | ≥ $2M USD statewide |
| Data stewardship layer | ≥ 500 place records at ≥ 60% recency | ≥ 5,000 place records at ≥ 65% recency |
| Stage 3 commerce | N/A | Active and operating without systemic incidents |
| DAO governance quorum | ≥ 30% on key votes | ≥ 40% on key votes |
| Regulatory standing | DUNA money-services registrations current; H4H nonprofit standing current | DUNA money-services registrations current; H4H nonprofit standing current; no deferred compliance draws unresolved |
| DAO advisory vote | Simple majority (advisory) | Simple majority (advisory; binding criteria above govern) |

---

## Appendix A: Definitions

- **Operational Reserve Ratio:** Treasury USDC Reserve ÷ Total Outstanding Spendable PMS (M$). Governs day-to-day continuity of service, per-user caps, and phase commerce feature unlock.
- **Treasury Reserve Solvency Ratio:** Treasury Reserve ÷ (Total Outstanding EMS + Total Outstanding M$). Governs EMS buying-power expansion and is the primary conversion gate.
- **Federal Volunteer Service Rate (FVSR):** The IRS-published standard rate for valuing volunteer services, updated annually. The Phase 3 EMS buying-power rate is the FVSR in effect on the date the DAO formally activates Phase 3 — not the rate at document publication. The current rate (2026) is $36.14. If Phase 3 activates in a later year, the applicable rate is that year's published FVSR. Ms. Allis surfaces the current FVSR on the dashboard each calendar year.
- **EMS Buying-Power Expansion:** The conditional, reserve-gated schedule by which 1 EMS hour carries increasing USD-equivalent buying power as the commons matures through phases. Conditional, revocable, and not vested; subject to automatic reversion cascade. Securities treatment under counsel review.
- **Reversion Cascade:** The automatic, no-vote-required process by which EMS buying-power expansion reverts to a prior phase's rate when the Treasury Reserve Solvency Ratio falls below the applicable phase threshold.
- **Compliance Draw:** Governed, transparent, bounded draw for documented and verified compliance costs; Stream N (H4H nonprofit) or Stream M (DUNA money-services); governed by Section 7A of each Phase Specification.
- **Deferral Queue:** Ms. Allis-managed queue of approved but reserve-floor-constrained Compliance Draws that fire automatically when the treasury can accommodate them without breaching the applicable floor.
- **Benefits-Sensitive Account (BSA):** A participant account flagged for enhanced protections due to the participant's receipt of means-tested benefits. PMS cash-out disabled by default; conversion timing participant-controlled; Phase 3 adds advance notice and EMS Recognition Bonus election option.
- **EMS Recognition Bonus:** An optional Phase 3 distribution form in which a participant elects to convert their dividend into permanent EMS recognition hours rather than M$ or USD. Irrevocable once elected for a given distribution event; income/asset treatment under benefits-counsel review.
- **Hard Trigger:** A system rule enforced automatically by Ms. Allis and the Phase Management Controller that cannot be overridden by any DAO vote at any threshold. Hard triggers protect the structural integrity of the commons.
- **Stage 3 Full Commerce:** Amazon-style full-commerce feature set of The Commons platform, unlocked when Operational Reserve Ratio ≥ 3.0 for 30+ consecutive days. Locks automatically if ratio drops below 2.0 for 7 consecutive days.
- **WV Money Transmitter License (MTL) / FinCEN MSB Registration:** The state license and federal registration for money transmission; held by the MountainShares DAO / DUNA, not H4H.

---

*Program Rules – Parameter Tables — Version 3.0*
*Harmony for Hope, Inc. | MountainShares DAO / DUNA | 704 Main Street, Mount Hope, WV 25880*
*Draft — Subject to H4H board review, DAO governance, and legal counsel approval before reliance*

---

**End of Program Rules – Parameter Tables v3.0**
