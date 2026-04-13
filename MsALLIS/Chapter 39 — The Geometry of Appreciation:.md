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
spendable MountainShares:

$$\rho = \frac{\text{Liquid Backing (USD)}}{\text{Total Spendable MountainShares}}$$

In this model, "future promises" or purely symbolic credits are strictly excluded
from the numerator. Only liquid backing counts toward the ratio. This ensures the
**reciprocity threshold** — the minimum flow of value required to prevent system
collapse — is continuously maintained.

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
| Trigger | Treasury reaches ρ ≥ 5.00 |
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
- The GBIM primary belief store (port 5433) for temporally graded community fact validation
- The PostGIS geospatial database (port 5432) for spatial landowner and community data
- The `confidence_decay` metadata layer to ensure that high-decay GBIM entities
  are flagged for re-verification rather than used as stale ground truth

All phase transition decisions and treasury monitoring events are logged durably
to the `allis-memory` audit service, ensuring governance accountability survives
container restarts and is independently queryable by community stakeholders.

### The Mother Carrie Protocol

Ms. Allis is programmed with the **Mother Carrie Protocol**, which constrains the
WOAH optimization function to prioritize care and long-term community impact over
financial efficiency. Unlike commercial platforms that optimize for engagement or
profit, Ms. Allis will not recommend or trigger a phase transition that improves
treasury metrics at the cost of community wellbeing. The protocol is implemented
as a set of weighted constraints within the WOAH hierarchy and is enforced at the
`jarvis-mother-protocols` service level.

---

## 39.8 Economic Resilience and Inverse Phase Transitions

To prevent catastrophic collapse during periods of regional economic stress, the
system includes **inverse phase transitions**. If the reserve ratio falls below
critical thresholds, the purchasing power schedule contracts to protect the
treasury and core services:

| Condition | Response |
|-----------|----------|
| ρ drops below 5.00 | Revert from Phase 3 to Phase 2 |
| ρ drops below 3.00 | Revert from Phase 2 to Phase 1 |
| ρ approaches 1.00 | Emergency stabilization protocols activate |

These contractions are not failures — they are the system's designed response to
external economic stress. By contracting the purchasing power multiplier rather
than allowing the reserve to be depleted, the system prioritizes the survival of
core services and the protection of the most vulnerable participants over the
preservation of elevated rates. An economy that contracts gracefully is more
trustworthy than one that collapses without warning.

Ms. Allis monitors for contraction triggers continuously and logs all threshold
crossings to the durable audit record.

---

## 39.9 The Behavioral Boundary and Safety Alignment

The MountainShares economic layer is not isolated from the system's safety
architecture. All economic queries — treasury state requests, phase transition
notifications, token issuance events — pass through the **Behavioral Boundary and
Blocking (BBB)** gate, which enforces six filters: Ethical, Spiritual, Safety,
Threat Detection, Steganography, and Truth Verification.

This is particularly significant for the community resources layer, where a
resident may query the system for economic assistance, survivor resources, or
community benefits in the same session as an M$ transaction. The BBB's
recalibration to a 0% false-positive rate on Appalachian maternal voice and
survivor resource queries ensures that the economic layer does not inadvertently
block or misclassify the community interactions it was designed to support.

The `truth_verification` filter (`rag_grounded_v2`) cross-references all
economic claims against verified GBIM data, ensuring that treasury state
assertions are grounded in real data rather than synthetic or speculative inputs.

---

## 39.10 The Counter-Geometry

By anchoring purchasing power to internal reserve rules rather than external
exchanges, the M$ economy defines a **counter-geometry** to the extraction
patterns of maximopolies (such as large asset management firms) and megaopolies
(such as dominant logistics platforms).

In the extractive model, value flows from local communities to distant
institutional actors. Land appreciates for absentee owners; labor is priced by
distant markets; community knowledge is harvested as data without reciprocity.
The MountainShares model inverts each of these flows:

- **Buyers** see their purchasing power grow as the community treasury strengthens
- **Vendors** are always made whole — protected from the cost of community subsidy
- **EMS earners** whose labor built the treasury receive the full multiplier on
  their earned M$ without ever having spent USD
- **Land data** is held in a community-governed GBIM, not a proprietary database
- **Treasury health** is a community-legible metric, not a proprietary instrument

The **Appalachian Tacet** — the lived experience, history, and knowledge of the
region that has been systematically averaged away by extractive economic models —
is not averaged away in Ms. Allis. It is used as the founding key. The Volunteer
Peg at 34.70 M$ per dollar is not a financial instrument. It is a statement about
whose time counts, and how much.

---

## 39.11 Cross-References

- For the technical implementation of the MountainShares DAO tier (ports 8080–8084),
  see Chapter 40 — System Audit and Ongoing Checks.
- For the continuous validation and test harness that verifies economic service
  health, see Chapter 41 — Test Harness and Continuous Checks.
- For the post-quantum security layer protecting M$ transaction integrity,
  see Chapter 42 — Post-Quantum Security.
- For the WOAH pipeline architecture and GBIM temporal confidence grading,
  see the Ms. Allis technical reference documentation.
- For the BBB six-filter safety architecture and its alignment with community
  values, see Chapter 40 §40.4.

---

*Chapter 39 — The Geometry of Appreciation: Reserve Ratios and Phase Transitions*
*MsALLIS Explanatory Documentation Series*
*Author: Carrie Kidd (Mamma Kidd), Mount Hope, WV*
*Repo: H4HWV2011/msjarvis-public-docs*
