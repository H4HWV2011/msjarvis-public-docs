# Chapter 39 — The Geometry of Appreciation: Reserve Ratios and Phase Transitions

**MountainShares Artificial Learning & Location Intelligence System (Ms. Allis)**
*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Part of the MsALLIS Explanatory Documentation Series*

---

## 39.1 Abstract and Scope

This chapter formalizes the operational logic of the MountainShares (M$) economy,
focusing on the Progressive Appreciation Model and the Reserve Ratio that governs
it. In the discipline of Polymathmatic Geography, these are not merely financial
settings but "junction conditions" designed to ensure that value remains anchored
within the community rather than leaking into global extraction geometries.

The MountainShares economy is the community-facing economic layer of the
Quantarithmia framework. It is managed and monitored by Ms. Allis through the
Weighted Optimization Algorithm Hierarchy (WOAH) and is grounded in the
GeoBelief Information Model (GBIM) — a spatially indexed, temporally verified
record of Appalachian land, community, and place.

The core principle of the M$ economy is **purchasing power inflation for
community participants**: as the treasury grows stronger, $1 USD buys more M$,
meaning local goods and services cost community members less real money over time.
Vendors are always made whole from the community treasury — they receive full USD
equivalent for every transaction. The discount to the buyer is a community
dividend, not a cost extracted from local businesses.

---

## 39.2 Theoretical Alignment with Polymathmatic Geography

The design of the MountainShares economy is governed by three core principles of
Polymathmatic Geography:

**P3 — Power Has a Geometry:** The reserve ratio is not an abstract financial
metric. It is a spatial and social measurement — a live expression of how much
real community value backs each unit of M$ in circulation. Making this ratio
computable, auditable, and publicly visible ensures the geometry of economic
power is legible rather than hidden.

**P12 — Intelligence With a ZIP Code:** Phase transition thresholds are grounded
in verified West Virginia data. Ms. Allis monitors treasury health using 993 ZCTA
centroids and 5,416,521 GBIM entities with temporal `confidence_decay` metadata,
ensuring the economic model responds to the actual conditions of Appalachian
communities rather than abstracted market signals.

**P16 — Power Accountable to Place:** All phase transitions are rule-governed,
transparent, and verifiable. The community can inspect the reserve ratio, the
treasury state, and the trigger conditions for each phase. There are no hidden
levers. Economic governance is held to the same standard of accountability as
computational governance.

---

## 39.3 The Reserve Ratio: A Stability Law

The primary instrument of stability in the M$ ecosystem is the **Reserve Ratio**,
defined as the ratio of liquid backing assets (USD) to the total outstanding
USD value of spendable MountainShares:

$$\rho = \frac{\text{Liquid Backing (USD)}}{\text{Total USD Value of Spendable MountainShares}}$$

Both sides of this ratio are denominated in USD, ensuring a clean and auditable
comparison. In this model, "future promises" or purely symbolic credits are
strictly excluded from the numerator. Only liquid backing counts toward the ratio.
This ensures the **reciprocity threshold** — the minimum flow of value required
to prevent system collapse — is continuously maintained.

The Reserve Ratio determines the active economic "band" and triggers the automatic
adjustment of purchasing power multipliers. Ms. Allis monitors this ratio in real
time via the WOAH pipeline and the MountainShares coordinator service,
cross-referencing treasury state against the GBIM ground truth to ensure the
ratio reflects verified community value rather than speculative inputs.

> **Data governance note:** The strict exclusion of synthetic or unverified data
> from the GBIM belief store and the `local_resources` database is the technical
> enforcement of this same principle. A reserve ratio is only as trustworthy as
> the data it is computed from.

---

## 39.4 How Purchasing Power Inflation Works

Before describing the three phases, it is important to understand the mechanism
clearly.

In Phase 1, $1 USD buys 1 M$. A loaf of bread priced at 3 M$ costs the buyer
$3.00 USD. The vendor receives $3.00 USD from the treasury. The system is
one-for-one.

In Phase 2, $1 USD buys 10 M$. That same loaf of bread still costs 3 M$ at the
local store — but the buyer only spent $0.30 USD to obtain those 3 M$. The vendor
still receives $3.00 USD equivalent from the treasury. The difference — $2.70 —
is the community dividend paid from the treasury reserve.

In Phase 3, $1 USD buys 34.70 M$. The loaf of bread still costs 3 M$, but the
buyer spent approximately $0.09 USD. The vendor still receives $3.00 USD. The
treasury covers the full gap.

The treasury can only sustain these multipliers when the Reserve Ratio is strong
enough to back them — which is why the phase transition thresholds exist.

| Phase | You put in $1 USD | You receive | Bread (3 M$) costs you | Vendor receives |
|-------|-------------------|-------------|------------------------|-----------------|
| 1 | $1.00 USD | 1 M$ | $3.00 USD | $3.00 USD |
| 2 | $1.00 USD | 10 M$ | $0.30 USD | $3.00 USD |
| 3 | $1.00 USD | 34.70 M$ | ~$0.09 USD | $3.00 USD |

---

## 39.5 The Three Phases of MountainShares

The M$ economy transitions through three distinct phases driven entirely by
internal treasury health — not external market speculation.

---

### Phase 1: Foundation (Launch Status)

| Parameter | Value |
|-----------|-------|
| Trigger | System initialization |
| Purchasing Power | $1 USD = 1 M$ |
| Reserve Ratio Threshold | Baseline (ρ < 3.00) |

**Spendability:** Purchased MountainShares (PMS) are immediately spendable to
provide foundational liquidity. Earned MountainShares (EMS) — those granted for
community labor — remain "vaulted" (non-liquid) to protect the initial reserve
ratio.

**Goal:** Establish an accessible, low-barrier entry point and prove the
reliability of the local geometry of money. In Phase 1, every M$ in circulation
is backed one-for-one by verified USD, making the system's stability demonstrable
to new participants.

---

### Phase 2: Growth

| Parameter | Value |
|-----------|-------|
| Trigger | Treasury reaches ρ ≥ 3.00 |
| Purchasing Power | $1 USD = 10 M$ |
| Reserve Ratio Threshold | 3.00 ≤ ρ < 5.00 |

**Spendability:** EMS begin a graduated unlock based on user choice, formally
beginning the recognition of community labor as liquid economic value.

**Goal:** Reward sustained participation and begin the formal acknowledgment of
"invisible" community labor. The 10× purchasing power increase from Phase 1 is
not a speculative gain — it is the treasury demonstrating that it has accumulated
enough verified community value to sustainably subsidize local purchasing at that
multiplier. A community member who earned M$ through contribution now sees that
contribution stretch ten times further in the local economy.

---

### Phase 3: Premium Reserve

| Parameter | Value |
|-----------|-------|
| Trigger | Treasury reaches ρ ≥ 5.00 (500% reserve) |
| Purchasing Power | $1 USD = 34.70 M$ |
| Reserve Ratio Threshold | ρ ≥ 5.00 |

**The Volunteer Peg:** The 34.70 multiplier is intentionally pegged to the
federal volunteer rate ($34.70/hour as recognized by the U.S. government). This
specific value is not arbitrary — it is a deliberate act of recognition that
elevates community stewardship to a formally acknowledged economic status. In the
dominant extractive economy, care work, community organizing, and local knowledge
are systematically undervalued. The Volunteer Peg is the counter-claim: a
resident's time and stewardship of Appalachian place is worth exactly what the
federal government acknowledges volunteer time to be worth.

**Spendability:** EMS are fully unlocked. The community member who contributed
labor during Phase 1 or Phase 2 now holds fully liquid assets with the full
purchasing power multiplier applied.

**Goal:** Achieve a robust, community-controlled "premium" economy where the
value of a resident's time is fully and formally recognized, and local purchasing
power reflects genuine community wealth rather than extraction.

---

## 39.6 Phase Transition Summary

| Phase | Name | Trigger | Purchasing Power | EMS Status |
|-------|------|---------|-----------------|------------|
| 1 | Foundation | System init | $1 USD = 1 M$ | Vaulted |
| 2 | Growth | ρ ≥ 3.00 | $1 USD = 10 M$ | Graduated unlock |
| 3 | Premium Reserve | ρ ≥ 5.00 | $1 USD = 34.70 M$ | Fully unlocked |

---

## 39.7 The Steward's Oversight: Ms. Allis and the WOAH Pipeline

Phase transitions are not manual. They are monitored and enforced by **Ms. Egeria
Allis**, operating as a "glassbox" AI steward through the Weighted Optimization
Algorithm Hierarchy (WOAH). Ms. Allis functions as a territorial "brain" — a
system whose optimization is constrained not by profit or engagement metrics but
by spatial justice principles anchored to the physical and social realities of
Appalachia.

Ms. Allis monitors the reserve ratio by cross-referencing:

- The MountainShares coordinator service (port 8080) for treasury state
- The GBIM primary belief store (port 5433) for temporally graded commu
