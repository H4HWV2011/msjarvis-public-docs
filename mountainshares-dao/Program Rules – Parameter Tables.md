# Program Rules – Parameter Tables (Phase 1 – WV Pilot)

> **Disciplinary Context: Appalachian Economic Commons**  
> This document instantiates Polymathmatic Geography principles P1, P9, P16, and related axioms for the Appalachian economic commons:  
> - **P1 – Every where is entangled / Leakage and enclosure:** Sections 1–7 treat EMS→M$ rates, caps, fees, reserve bands, and governance thresholds as one integrated instrument that shapes how value circulates and where leakage or enclosure pressures arise. See https://github.com/H4HWV2011/msAllis-public-docs/blob/main/docs/Polymathmatical-Geography.md  
> - **P9 – Transparency and traceability:** The tabular parameters for conversion, reserve bands, internal buying power, fees, and limits make the "knobs" of the system inspectable, so communities can see exactly how rules translate into numeric constraints.  
> - **P16 – Power accountable to place:** Governance thresholds, band‑based permissions, and benefits‑sensitive limits tie parameter changes and risk controls to explicit conditions in the West Virginia pilot, ensuring that institutional power responds to local reserves, usage, and sensitivity to benefits.  
> - **Anti‑leakage and closed‑loop spending:** Conversion caps, reserve‑ratio bands, internal phase schedules, and promo‑pool limits collectively aim to keep value recirculating in the closed loop rather than spilling out via over‑minting or unbounded cash‑outs.  
> - **Bounty and corrective programs:** Promo‑pool parameters and governance thresholds encode how targeted bonuses or "bounty‑like" incentives can be safely activated or throttled in response to reserve bands and community decisions.

> **DRAFT – LIVE PARAMETERS SUBJECT TO CHANGE**
>
> This document presents the **current operational parameters** for Phase 1 of the MountainShares Program
> (West Virginia pilot). It is incorporated by reference into `Program Rules.md` and the Phase 1 Economic
> Safety Specification. In case of conflict, the Phase 1 Specification and Terms and Conditions control.

---

## 1. Phase 1 EMS → M$ Conversion Parameters

### 1.1 Global Base Rate

| Parameter             | Value                 | Notes                                           |
|-----------------------|-----------------------|------------------------------------------------|
| Initial base rate     | 0.20 M$ / EMS hour    | Applied to eligible EMS in Phase 1             |
| Minimum base rate     | 0.10 M$ / EMS hour    | Emergency floor in low reserve band            |
| Maximum base rate     | 1.00 M$ / EMS hour    | Upper bound in safe zone                       |
| Adjustment frequency  | Epoch-based (e.g. 24–48 hours) | Governed by reserve ratio and DAO rules |

### 1.2 Per‑User Convertible Caps (Spendable M$ per Month)

| Tier  | Description                                        | Monthly Cap (M$) | Weekly Guidance (hrs at 1.0 M$/hr) | Daily Guidance (hrs at 1.0 M$/hr) |
|-------|----------------------------------------------------|------------------|------------------------------------|-----------------------------------|
| Tier 1| General commons participants                       | 40               | ≈ 10                               | ≈ 1–2                             |
| Tier 2| Verified EMS (e.g., caregiving, high‑need roles)   | 80               | ≈ 20                               | ≈ 4                               |

> **Note:** Weekly/daily values are guidelines derived from the current base rate and may be applied as
> separate hard caps where specified in the Economic Safety Specification.

---

## 2. Reserve Ratio Bands and Automatic Adjustments

### 2.1 Reserve Ratio

Reserve Ratio = Liquid Backing Assets (USD) / Total Outstanding Spendable M$

### 2.2 Band Table (Illustrative Phase 1 Values)

| Band ID | Reserve Ratio Range | Base Rate Range (M$/EMS hr) | Typical Tier 2 Cap (M$/mo) | Promo State | Governance Permissions                 |
|---------|---------------------|------------------------------|----------------------------|------------|----------------------------------------|
| A       | ≥ 1.50              | 1.00                         | up to 120                  | Enabled    | May propose limited increases          |
| B       | 1.00 – 1.49         | 0.50 – 0.80                  | 80 – 100                   | Reduced    | May adjust upward if trend stable      |
| C       | 0.75 – 0.99         | 0.20 – 0.40                  | 40 – 80                    | Paused     | May hold steady only                   |
| D       | < 0.75              | 0.10                         | 20 – 40                    | Frozen     | No increases; automatic tightening     |

Ms. Allis recalculates the reserve ratio daily and applies the appropriate band at the next epoch.

---

## 3. Internal Phase Schedules (In‑Network Buying Power)

> Internal buying power is used for in‑network redemption accounting only and does not establish any
> external price, redemption right, or investment return.

| Phase   | Internal Schedule (1 M$ ≈ USD) | Activation Conditions (High‑Level)                          |
|---------|---------------------------------|-------------------------------------------------------------|
| Phase 1 | 1.00                            | Default launch phase                                        |
| Phase 2 | 10.00                           | Reserve ratio and adoption thresholds met (see Phase 1 Spec)|
| Phase 3 | 34.70                           | Aspirational; high reserve / safety conditions only         |

---

## 4. Fees and Promo Pool

### 4.1 Standard Fees

| Fee Type             | Current Rate           | Applies To                                   |
|----------------------|------------------------|----------------------------------------------|
| Load fee             | 2.85% of fiat load     | USD → PMS loads                              |
| Internal transfer fee| 0.25%                  | Eligible User‑to‑User transfers              |
| Merchant fee         | 1.80%                  | Eligible purchases at accepting Merchants    |
| ATM / refund fee     | 1.25 USD (flat)        | PMS cash‑out transactions (where enabled)    |

### 4.2 Promo / Bonus Pool

| Parameter                    | Value / Range                             | Notes                                      |
|-----------------------------|-------------------------------------------|-------------------------------------------|
| Promo pool source           | % of monthly processed volume             | Allocated from fees / treasury            |
| Promo pool target range     | 2% – 3% of monthly volume (illustrative)  | Exact % set by DAO within safety limits   |
| Monthly promo cap (M$)      | X (to be set per region)                  | Hard cap to prevent overspend             |
| Promo state per reserve band| Enabled / Reduced / Paused / Frozen       | As per reserve ratio band table           |

### 4.3 Fee Revenue Allocation

All collected fee revenue (load fees, internal transfer fees, merchant fees, and ATM/refund fees) is
allocated across five designated purposes according to the following fixed split. This structure ensures
that every dollar of fee income serves a defined function within the MountainShares ecosystem and the
broader Appalachian economic commons.

#### 4.3.1 Allocation Table

| Bucket | Allocation | Recipient / Purpose                     | Description                                                                                      |
|--------|------------|-----------------------------------------|--------------------------------------------------------------------------------------------------|
| 1      | 30%        | Harmony for Hope, Inc. (H4H Operations) | Covers nonprofit administration, staffing, compliance, legal, and program delivery costs         |
| 2      | 30%        | Treasury Reserve                        | Grows the MountainShares backing reserve; supports phase transition thresholds and liquidity     |
| 3      | 15%        | Platform Development                    | Funds ongoing development of The Commons app, Ms. Allis infrastructure, and technical systems  |
| 4      | 15%        | Community Programs                      | Supports structured programs: education, mutual aid, time-banking, cultural preservation, etc.  |
| 5      | 10%        | Community Projects                      | Funds member-initiated or DAO-approved local projects within the West Virginia commons           |
| —      | +0.55%     | Treasury Reserve (Supplemental)         | An additional 0.55% of gross transaction volume accrues directly to the Treasury Reserve        |

> **Total standard split: 100% of collected fee revenue.**  
> The +0.55% supplemental treasury reserve is assessed separately on gross transaction volume (not fee
> revenue) and is in addition to the 30% Treasury Reserve bucket above.

#### 4.3.2 Treasury Reserve Funding Sources

The Treasury Reserve (Bucket 2) is funded by the following streams:

- **30% of all collected fee revenue** (load fees, transfer fees, merchant fees, ATM fees)
- **+0.55% supplemental reserve assessment** on gross transaction volume
- **Merchant fees (1.80%)** — the merchant fee is a primary treasury-building mechanism; the 30% treasury
  share of this fee is routed to the reserve automatically at settlement
- **ATM / refund fee ($1.25 flat)** — the full $1.25 per cash-out transaction contributes to the treasury
  reserve pool via the standard 30% allocation, reinforcing reserve stability every time a PMS cash-out
  occurs

> **Design intent:** The combination of the 30% fee-revenue split and the +0.55% supplemental assessment
> creates a compounding reserve-growth mechanism. As transaction volume grows, the treasury grows
> proportionally, supporting the Phase 2 (125% reserve ratio) and Phase 3 (150% reserve ratio) thresholds
> defined in the Terms and Conditions and Phase 1 Economic Safety Specification.

#### 4.3.3 Governance and Adjustability

These allocation percentages are **Program Rules parameters** and may be adjusted through the DAO
governance process defined in the MountainShares DAO Governance Charter, subject to:

- A minimum Treasury Reserve allocation of 20% (floor, not subject to ordinary DAO vote)
- A minimum H4H Operations allocation of 20% (floor, required for nonprofit sustainability)
- Any changes requiring a super-majority (66%) DAO vote and Board of Directors ratification
- Changes disclosed to Users per Section 10.3 of the Terms and Conditions (minimum 30 days notice)

---

## 5. PMS Load and Cash‑Out Limits (Phase 1 Baseline)

> Exact figures to be set in consultation with payment partners and compliance.

| Limit Type                      | Tier / KYC Level        | Value (Placeholder)           |
|---------------------------------|-------------------------|-------------------------------|
| Min load per transaction        | All                     | e.g., 10 USD                  |
| Max load per transaction        | Basic / Advanced / High | e.g., 200 / 1,000 / 5,000     |
| Max total load per month        | By KYC tier             | To be defined                 |
| Max PMS cash‑out per transaction| By KYC tier             | To be defined                 |
| Max PMS cash‑out per month      | By KYC tier             | To be defined                 |

Benefits‑Sensitive Accounts have PMS cash‑out disabled by default regardless of general limits.

---

## 6. Benefits‑Sensitive Account Thresholds (Illustrative)

| Parameter                     | Value (Placeholder) | Description                                       |
|-------------------------------|---------------------|---------------------------------------------------|
| Balance warning threshold     | e.g., 200 M$        | UI warns user to check impact on benefits         |
| Hard soft‑cap (throttle point)| e.g., 400 M$        | EMS earning slows or pauses above this level      |
| PMS load allowed              | No (by default)     | Exceptions documented case‑by‑case                |

---

## 7. Governance Thresholds (Phase 1 / Early Phase 2)

| Parameter               | Value (Placeholder)     | Description                                           |
|-------------------------|-------------------------|-------------------------------------------------------|
| Governance eligibility  | 10 EMS hours + 30 days  | To obtain 1 UEI vote (per DAO spec)                  |
| Quorum for key proposals| 30% of eligible UEIs    | For rate/cap changes, phase transitions               |
| Super‑majority threshold| 66%                     | For "constitutional" or high‑impact changes           |

All numeric values above are subject to revision via governance, within the bounds of the Terms and Economic Safety Specification.
