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

A 500% reserve requirement means the system could sustain an 80% run on the
treasury and still honor every M$ in circulation at full face value. This is more
conservative than most central banks and is the architectural answer to the
question: *is this system survivable?*

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

## 39.11 The Appalachian Premium: External Markets Funding Local Resilience

The MountainShares Commons is designed to accept both M$ and USD — from local
participants and from anyone online, anywhere in the world. This dual-currency
architecture creates a structural funding mechanism for the treasury that does not
depend on regional economic conditions alone.

Provenance-based pricing is a documented and functioning market reality. Consumers
in distant markets demonstrably pay premium prices for goods with authentic
regional identity — Vermont maple syrup, Kentucky bourbon, Appalachian ginseng,
mountain crafts. West Virginia carries exactly that kind of authentic story, and
the Commons provides the verified provenance layer that makes it legible and
trustworthy to outside buyers.

The economic model this creates is straightforward:

| Who | What they pay | What they get | What goes to the treasury |
|-----|--------------|---------------|--------------------------|
| WV buyer using M$ | ~$0.09 USD equivalent (Phase 3) | Local bread, goods, services | Treasury covers the gap |
| Outside buyer using USD | $8.00 USD (Appalachian premium) | Authentic provenance product | Full USD premium strengthens ρ |
| WV vendor | $3.00 USD guaranteed | Full USD equivalent always | Protected — never absorbs the subsidy |

Outside USD premium purchases actively strengthen the reserve ratio. A single
sustained stream of provenance-premium online transactions can move the treasury
toward Phase 2 or Phase 3 thresholds without requiring every WV resident to
participate. The extraction economy harvests Appalachian culture as data. The
Commons harvests it as treasury.

---

## 39.12 The Threshold of Sufficiency: An Honest Assessment

Phase 3 requires a 500% reserve ratio — $5 in liquid backing for every $1 of
spendable M$ in circulation. To contextualize what treasury volume is needed to
sustain this, it is useful to compare against an existing global payment network.

Mastercard operates approximately 3.158 billion active cards globally and
processed over $10.63 trillion in transaction volume in 2025. **0.01% of
Mastercard's global cardholder base is 315,800 people.** That is less than the
population of a mid-sized American city, spread across the entire global network
— statistically invisible to Mastercard, but sufficient to sustain a 500%-backed
community economy at Phase 3 purchasing power.

As a global online commons accepting both M$ and USD, that threshold is
realistically achievable through multiple convergent paths:

- Diaspora Appalachians — people who left WV but maintain regional identity —
  number in the millions and represent a natural first adoption wave
- A single viral moment, academic citation, or press story could deliver
  315,800 participants within weeks
- Provenance-premium online sales to buyers in Michigan, California, or New York
  contribute USD directly to the treasury without requiring those buyers to
  hold or use M$ at all

**This section would be incomplete without the honest counterweights.**

The bootstrap problem is real. Getting to ρ ≥ 3.00 — the Phase 2 threshold —
is where most community currencies in history have failed. The gap between a
functioning system and a trusted system takes time, relationships, and sustained
participation that no amount of technical elegance can shortcut.

An online commons requires logistics infrastructure — shipping, fulfillment,
returns, dispute resolution — that is expensive, unglamorous, and orthogonal to
the computational architecture described in this documentation series.

Provenance trust requires marketing and certification that technology alone does
not provide. A buyer in Michigan paying a premium for an Appalachian product
needs a reason to believe the provenance claim is real — and building that trust
is a human and institutional problem, not a software problem.

Regulatory questions around M$ as a currency instrument are not yet resolved.
Depending on implementation, M$ may attract scrutiny under money transmission,
securities, or consumer protection frameworks. These questions are outside the
scope of this documentation but are not outside the scope of responsible
deployment.

**Why these hard truths strengthen rather than weaken the thesis:**

Every one of the known failure modes of community currencies has a direct
architectural response in this system. The 500% reserve requirement exists
*because* community currencies are vulnerable to runs. The inverse phase
transitions exist *because* external economic shocks are real. The vaulted EMS
mechanism exists *because* premature liquidity destroys reserve ratios. The
Mother Carrie Protocol exists *because* optimization without care constraints
produces outcomes that harm the vulnerable.

MountainShares does not need to displace Mastercard. It does not need to capture
a significant market share, attract venture capital, or achieve viral growth. It
needs **315,800 people** who believe that a loaf of bread from West Virginia is
worth buying, and that the person who baked it deserves to be paid fairly.

That is not an unrealistic number. It is a threshold of sufficiency — the minimum
sustainable footprint for a system designed not to grow without limit, but to
**survive with integrity**.

---

## 39.13 Cross-References

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
