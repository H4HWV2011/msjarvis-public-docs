# MountainShares Funder Overview  
*Harmony for Hope, Inc. – West Virginia Pilot*

## 1. Organizational Structure and Roles

### 1.1 Harmony for Hope, Inc.

Harmony for Hope, Inc. (“Harmony for Hope” or “H4H”) is a 501(c)(3) nonprofit organization based in Mount Hope, West Virginia. Harmony for Hope is the program sponsor and legal operator of the MountainShares rewards program and The Commons ecosystem for the West Virginia pilot.

Harmony for Hope is responsible for:

- **Program stewardship and compliance**  
  - Owning and operating the MountainShares program as a charitable, community‑benefit initiative rather than a speculative financial product.  
  - Ensuring that all activities comply with Applicable Law, payment‑provider terms, and nonprofit obligations, including IRS rules for 501(c)(3) organizations.  
  - Approving and updating Program Rules, Phase Specifications, and DAO governance frameworks through the Board of Directors and designated committees.

- **Treasury and reserve management**  
  - Acting as fiduciary steward of MountainShares treasury reserves, which back the internal economic model.  
  - Overseeing how fee revenue is allocated between treasury reserves, organizational operations, infrastructure, and community programs.  
  - Ensuring that reserve‑ratio safety rules and phase thresholds (for example, 300% and 500% reserve coverage for later phases) are implemented and respected in practice.

- **Program operations and partnerships**  
  - Managing relationships with local merchants, nonprofits, and public entities that participate in MountainShares and The Commons.  
  - Coordinating on‑the‑ground programs, events, and outreach that connect the digital system to real community needs and specific places in West Virginia.  
  - Serving as the primary point of contact for funders, regulators, and institutional partners.

Harmony for Hope is not a bank, credit union, or investment advisor. It operates MountainShares as a community rewards and payment program within a closed loop, under nonprofit governance and legal constraints.

### 1.2 Kidd’s Technical Services, LLC

Kidd’s Technical Services, LLC (“KTS”) is the independent technical firm that has designed and implemented the core infrastructure for MountainShares and Ms. Allis.

KTS has:

- Designed and built the **Ms. Allis Geospatial Intelligence Platform**, including:  
  - A microservices architecture orchestrating more than eighty services.  
  - GBIM (Geographic Belief Information Model) for spatially aware knowledge.  
  - GeoDB and PostGIS schemas for geographic data.  
  - ChromaDB‑based vector search for semantic retrieval.  
  - An LLM orchestration layer and API gateway for cross‑system coordination.

- Implemented the **MountainShares mutual credit and rewards back end**, including:  
  - EMS recognition and vaulting logic.  
  - PMS handling and fee flows.  
  - Phase 1 Economic Safety Specification with reserve‑ratio bands and hard triggers.  
  - DAO and governance scaffolding integrated with Ms. Allis.

- Contributed **5,024 hours** of senior technical work between March 23, 2025 and February 19, 2026, valued at **$150/hour** for a documented capital contribution of **$753,600**, as detailed in the Founder's Technical Investment Statement.

Intellectual property is structured so that:

- The MountainShares mutual credit system and commons governance configurations are developed for use by Harmony for Hope as part of its charitable mission.  
- The Ms. Allis Geospatial Intelligence Platform remains proprietary to KTS and is made available to Harmony for Hope under a **non‑exclusive, royalty‑free license** for community‑benefit deployments.

This reflects a founder’s capital contribution into a commons infrastructure, rather than a venture‑capital style equity position or profit‑extraction arrangement.

### 1.3 MountainShares DAO and Ms. Allis

MountainShares includes a DAO‑style governance layer and a transparent AI assistant, Ms. Allis, both operating under Harmony for Hope’s legal framework.

- **MountainShares DAO**  
  - Provides community governance over adjustable parameters such as EMS→M$ base rates, per‑user caps, promo pool sizes, and some program thresholds.  
  - Operates on a “one UEI = one vote” principle once minimum participation and anti‑sybil criteria are met, with super‑majority thresholds for constitutional or high‑impact changes.  
  - Is explicitly constrained by the Economic Safety Specification and Program Rules: it cannot override hard triggers, reserve‑ratio safety bands, or legal/compliance requirements.

- **Ms. Allis (AI tooling layer)**  
  - Acts as a “glass‑box” AI advisor and operations assistant:  
    - Monitoring reserve ratios and phase thresholds.  
    - Calculating EMS recognition and vaulting status.  
    - Suggesting parameter adjustments within allowed bands.  
    - Flagging anomalies, abuse patterns, or safety issues for human review.  
  - May hold a MountainShares wallet and receive limited program rewards for useful system maintenance, under explicit caps and policies that prevent capture or undue influence.  
  - Has no independent legal status, cannot own assets, and cannot overrule Harmony for Hope, the DAO, or applicable law.

Harmony for Hope remains the final authority for legal, fiduciary, and mission‑aligned decisions while the DAO and Ms. Allis provide participatory and analytical capabilities inside that framework.

---

## 2. Program Model and Fee Structure

MountainShares operates as a **closed‑loop rewards and payment system** with a dual‑token design:

- **Purchased MountainShares (PMS)** – value that users load with U.S. dollars via Stripe, immediately spendable inside the system according to Program Rules.  
- **Earned MountainShares (EMS)** – credits granted for documented community contributions, which are first recorded in an unlimited recognition ledger and then partially converted into spendable M$ under strict caps and reserve‑linked rules.

### 2.1 Fiat Loads (USD → PMS)

When a user loads funds into MountainShares:

- The user selects a load amount (for example, **$100**) and receives exactly **100 M$** worth of PMS in their wallet. The internal account balance always matches the amount the user chose to load.  
- Stripe processing fees (currently around 3.5% effective when combining percentage and flat components) are added on top of the $100 and are passed directly to the payment processor.  
- Program fees totaling **3.05%** are also added on top of the load amount. These consist of:  
  - **2.55%** program fee, which is split across multiple community‑aligned buckets.  
  - **0.50%** additional fee, allocated entirely to the treasury reserve.

For every $1.00 loaded, the **2.55%** program fee (0.0255 USD) is allocated:

- 30% → **Harmony for Hope general operations** (core nonprofit capacity, administration, and staff).  
- 30% → **Treasury Reserve** (backing assets that help keep the system within defined safety bands).  
- 15% → **Infrastructure Development**, including ongoing hosting, maintenance, and development of Ms. Allis, GBIM, and the MountainShares back end.  
  - 2% of this 15% stream is reserved for the **founding architect**, recognizing long‑term technical stewardship.  
- 15% → **Community Projects**, such as local arts and preservation, mutual‑aid pilots, and project‑based initiatives.  
- 10% → **Community Programs**, such as recurring programming, classes, and events.

The additional **0.50%** program fee is:

- 100% → **Treasury Reserve**.

From the user’s perspective:

- “Load $100” always results in a **100 M$** balance inside the app.  
- Stripe and program fees are visible as costs added on top of the chosen load amount; they are not silently deducted from the user’s intended value.

### 2.2 Internal Transfers (User → User)

For person‑to‑person transfers within MountainShares:

- A **0.25%** transfer fee is applied to the transfer amount.  
- 100% of this fee is allocated to the **Treasury Reserve**, providing a small continuous inflow of backing assets as value circulates locally.

### 2.3 ATM / Cash‑Out (PMS → Cash)

When users cash out part of the PMS value they originally loaded (where such cash‑out features are enabled):

- A flat **$1.25** program fee is charged per ATM cash‑out transaction.  
- Users also pay any surcharge imposed by the ATM operator; that surcharge is not program revenue.  
- The $1.25 program fee is allocated 100% to the **Treasury Reserve**.

Cash‑out is constrained by Program Rules, treasury availability, and regulatory requirements, and typically limited to the amount of originally loaded funds (less prior fees and adjustments).

### 2.4 Merchant Payments (User → Local Merchant)

When users pay local merchants through MountainShares:

- A **1.75% merchant fee** is applied to the transaction.  
- That 1.75% stream uses the **same allocation split** as the 2.55% load fee (Harmony for Hope, treasury reserve, infrastructure, community projects, community programs, with a controlled architect share embedded in infrastructure).  
- Governance may authorize an additional **0.50%** to treasury reserve on merchant flows if risk models justify it, mirroring the load‑fee structure.  
- Merchants receive the full tagged price of the sale; the fee is treated as a program‑level charge on top of the transaction amount.

This structure is designed to:

- Keep friction lower for local participants and merchants than at the “edges” of the system.  
- Ensure that every load, transfer, cash‑out, and merchant transaction contributes in some way to reserves and community funding rather than flowing entirely to external processors.

---

## 3. EMS, PMS, Vaulting, and Phases

### 3.1 Recognition vs Spendable Layers

MountainShares draws a clear distinction between:

- An **unlimited recognition ledger** where all EMS are recorded (1 EMS hour per verified hour of community contribution, with UEI, geo, and timestamp metadata).  
- A **capped spendable layer** where some of those EMS hours are converted into spendable M$ under base‑rate and per‑user cap rules, governed by reserve‑ratio bands.

This allows the system to:

- Recognize the full scope of community contribution, even when treasury conditions require tight caps on spendable rewards.  
- Use the recognition ledger for governance, rank, and narrative purposes, without overextending financial promises.

### 3.2 Vaulting and Unlocking of EMS

During Phase 1 and possibly beyond:

- EMS are **credited** to the recognition ledger as users participate in qualifying activities.  
- Only a **portion** of EMS is immediately converted into spendable M$ each epoch, subject to:  
  - The current **global base rate** (for example, 0.2 M$ per EMS hour at launch, bounded between 0.1 and 1.0).  
  - **Per‑user tier caps** (for example, 40 M$/month for general participants, 80 M$/month for verified caregiving/high‑priority roles).  
  - System‑wide reserve‑ratio bands.

The remainder of EMS may be held in a **vaulted** state:

- Visible to the user in dashboards (for transparency), but not yet spendable.  
- Candidates for future unlocking if and when the system transitions to later phases and reserve coverage allows it.

### 3.3 Phase Thresholds and Unlock Logic

The three internal phases of MountainShares are designed to link **in‑network buying power** and EMS unlocking to the strength of treasury reserves.

- **Phase 1 – Launch (Default)**  
  - Internal schedule: **1 M$ ≈ 1.00 USD** of in‑network buying power for eligible redemptions.  
  - Only PMS is broadly spendable across the MountainShares app; EMS conversions are tightly capped and limited to specific in‑network contexts (see below).  
  - Serves as the conservative starting point, with maximum emphasis on safety and stability.

- **Phase 2 – Treasury Threshold (Aspirational but concrete)**  
  - Activation condition: treasury reserves reach at least **300%** of total outstanding spendable M$ **when valued at the Phase 2 schedule (10 USD per M$)**, and remain above that threshold for a defined stability window.  
  - Internal schedule: **1 M$ ≈ 10.00 USD** of in‑network buying power.  
  - When Phase 2 is active:  
    - A controlled subset of previously **vaulted EMS** can unlock into spendable M$ under carefully defined rules.  
    - If the reserve ratio later falls below the 300% threshold, Phase 2 can suspend new unlocks or revert to stricter caps, and already unlocked balances can be subject to safely defined fallback behavior (for example, slowing further conversions rather than forced clawbacks).

- **Phase 3 – Full‑Backing Target (Aspirational)**  
  - Activation condition: treasury reserves reach at least **500%** of total outstanding spendable M$ **when valued at the Phase 3 schedule (34.70 USD per M$)**, again with a stability window.  
  - Internal schedule: **1 M$ ≈ 34.70 USD** of in‑network buying power, initially aligned with national volunteer‑time valuation at the time the schedule is adopted.  
  - Phase 3 is an aspirational design target, not a guarantee; it may be:  
    - Narrowly applied to limited balances, cohorts, or use cases.  
    - Delayed, restricted, or never activated if conditions are not sustainably met.  
  - If reserves fall below the 500% threshold:  
    - New Phase 3 unlocks halt automatically.  
    - The system can tighten benefits back toward Phase 2 or Phase 1 schedules according to predefined, transparent fallback rules.

At every phase, **automatic downward adjustments** and protections are built in; upward moves (unlocking, expanded buying power) require both the reserve thresholds and appropriate governance decisions.

### 3.4 PMS vs EMS Usage and The Commons App

MountainShares deliberately differentiates how PMS and EMS can be used, especially in early phases:

- **Phase 1 – PMS usage**  
  - PMS (loaded via Stripe) is spendable inside the broader MountainShares app ecosystem according to Program Rules.  
  - PMS can be used for:  
    - Purchases at participating local merchants inside the MountainShares network.  
    - Internal transfers between users.  
    - Other app‑enabled spend activities defined in Program Rules.

- **Phase 1 – EMS usage**  
  - EMS in Phase 1 are **not** broadly spendable across the entire payment network.  
  - Converted EMS (the small portion that becomes spendable M$ under caps) are limited to specific in‑network use within **The Commons** app:  
    - Access to community programs, events, education, cultural offerings, and historic trail interactions provided through The Commons.  
    - Other commons‑oriented redemptions described in Program Rules.  
  - EMS cannot be used for out‑of‑network cash‑outs or unconstrained retail spending during Phase 1, which protects benefits‑sensitive users and helps maintain anti‑leakage design.

Over time, if the system reaches Phase 2 or beyond and reserves permit, governance may authorize carefully scoped expansions in where EMS‑linked M$ can be spent, including:

- Gradual extension of EMS‑backed spending from The Commons app into the broader MountainShares merchant network.  
- Application of higher internal buying‑power schedules to defined portions of EMS‑derived balances, under strict safety constraints.

This phased approach ensures that **PMS** behaves like stored purchasing power loaded by the user, while **EMS** remains heavily constrained and targeted toward commons‑aligned uses until the system is demonstrably safe and adequately funded.

---

## 4. Founder’s Investment and Capacity

Kidd’s Technical Services, LLC has made a substantial **founder’s capital contribution** to MountainShares and Ms. Allis:

- **5,024 hours** of senior geospatial, AI, and systems architecture work from March 23, 2025 through February 19, 2026.  
- Valued at **$150/hour**, totaling **$753,600** in documented founder’s technical investment.  
- Detailed timesheets, monthly roll‑ups, and milestone logs are available to support grant audits and due diligence.

This contribution:

- Demonstrates significant **pre‑award investment** and technical capacity.  
- Provides **in‑kind match documentation** for eligible grants that accept such match.  
- Reduces technical risk for funders by showing that core infrastructure already exists and has been tested, rather than being hypothetical.

For KTS, this is treated as founder’s capital investment into a commons system; there is no charitable deduction claimed for the value of time, and no expectation of profit distributions from Harmony for Hope.

---

## 5. Use of Program Revenues (Charitable Intent)

Program revenues and related funds allocated to Harmony for Hope in connection with MountainShares are intended to support:

- **Harmony for Hope operations and staff**, which provide organizational backbone for community programming and technical stewardship.  
- **Fayette County Community Arts Center** historic rehabilitation and ongoing cultural programming and maintenance.  
- **Oakvale Area Outreach Team** staffing, daily operations, and project‑based outreach work.  
- **Mount Hope Historic Walking Trail and Coalfield Chronicles Trail** expansion, wayfinding, interpretation, and associated programming.  
- **In‑house IT, GIS, and infrastructure maintenance** for MountainShares, Ms. Allis, GBIM, and The Commons.

These allocations describe a charitable and programmatic use of revenue; they do not create any right to profit or distributions for participants or funders.

---

## 6. Summary for Funders

MountainShares is a community‑governed, nonprofit‑operated rewards and payment system that:

- Keeps value and decision‑making rooted in West Virginia communities, beginning with Mount Hope.  
- Uses explicit safety math (reserve ratios, vaulting, and phase thresholds) to balance recognition of community work with conservative financial commitments.  
- Channels program revenue to Harmony for Hope operations, treasury reserves, infrastructure, and local projects rather than to outside investors.  
- Leverages a significant founder’s technical investment and a transparent AI assistant (Ms. Allis) to deliver glass‑box governance and operations.

For funders, this overview provides a coherent picture of who operates MountainShares, how it is financed and safeguarded, how EMS and PMS behave across phases, and how the system supports long‑term community stewardship instead of extractive models.
