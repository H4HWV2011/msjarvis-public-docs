# MountainShares DAO Governance Charter

> **DRAFT – GOVERNANCE CHARTER**
>
> This Charter describes the intended governance structure and processes for the MountainShares DAO.
> It is a non‑binding design document for community review and legal vetting. In any conflict with
> the MountainShares Terms and Conditions or applicable law, those higher‑level instruments control.

---

## 1. Purpose and Scope

The MountainShares DAO exists to:

- Steward the rules and parameters of the MountainShares Program in alignment with the mission of Harmony for Hope, Inc.  
- Keep value, voice, and decision‑making rooted in Appalachian communities, beginning with the West Virginia pilot.  
- Provide structured, transparent community input into key economic, technical, and cultural decisions.

The DAO is **not** a bank, investment club, or vehicle for distributing profits. It does not create equity or ownership interests in any entity.

---

## 2. Governance Roles

### 2.1 Harmony for Hope, Inc. (H4H)

- Holds fiduciary, legal, and regulatory responsibility.  
- Can veto or override DAO decisions where necessary to comply with law, funding conditions, or core safety obligations.  
- Appoints and oversees staff who implement DAO‑approved program changes.

### 2.2 DAO Participants (UEI‑Based Members)

- Each Unique Ecosystem Identifier (UEI) can become an eligible voting participant once contribution and tenure thresholds are met.  
- DAO participants submit proposals, deliberate, and vote on matters within the DAO’s scope.

### 2.3 System Monitors (Early‑Phase)

- Designated individuals or small teams with limited authority to:
  - Apply urgent safety fixes.  
  - Respond to clear abuse or exploits.  
  - Execute technical changes already approved in principle by governance.  
- Operate under explicit mandates and reporting requirements; subject to periodic review and sunsetting.

### 2.4 Ms. Egeria Jarvis (AI Advisor)

- Functions as a “glass‑box” advisory and enforcement layer.  
- Monitors reserve ratios, flags anomalies, enforces hard triggers, and surfaces analytics.  
- Cannot unilaterally change rules, mint tokens, or override H4H’s legal responsibilities.

---

## 3. Membership and Voting

### 3.1 Eligibility for Voting Participation

Initial eligibility (subject to refinement):

- Account age: minimum 30 days since UEI creation.  
- Contribution: minimum 10 EMS hours recorded in the recognition ledger.  
- Good standing: no unresolved sanctions for abuse, fraud, or major policy violations.

### 3.2 One‑UEI‑One‑Vote Principle

- Each eligible UEI has exactly one vote in general DAO proposals.  
- Identity aggregation or splitting is discouraged and may be mitigated through sybil‑resistance measures (e.g., tiered KYC for higher‑impact roles).

### 3.3 Classes of Proposals

- **Operational Parameter Proposals**  
  - Adjustments to base rates, caps, and promo budgets within safety bands.  

- **Policy and Program Proposals**  
  - Changes to Program Rules categories, qualification criteria, and gamification mechanics.  

- **Constitutional Proposals**  
  - Changes to the Economic Safety Specification, DAO Charter, or other core documents.  
  - Require higher quorum and super‑majority thresholds.

---

## 4. Proposal Lifecycle

### 4.1 Submission

- Any eligible voting member may submit a proposal within defined categories.  
- Proposals must include:
  - Clear title and category.  
  - Rationale and expected impact.  
  - Concrete parameter changes or policy text where applicable.

### 4.2 Review and Screening

- System monitors and/or a governance working group may perform initial screening to:
  - Check for conflicts with law, Terms, or hard triggers.  
  - Consolidate duplicative proposals.  
  - Provide non‑binding impact assessments (e.g., reserve ratio implications).

### 4.3 Discussion and Amendment

- Proposals enter a discussion period (for example, 7–21 days):  
  - Comments and suggested amendments are recorded.  
  - Proposers may revise based on community feedback.

### 4.4 Voting

- After discussion, proposals are opened for a defined voting window (for example, 5–14 days).  
- Voting methods:
  - Simple majority for low‑impact operational changes.  
  - Super‑majority (e.g., 66% in favor) for constitutional or high‑impact changes.  
- Quorum thresholds (e.g., 30% of eligible voters) must be met for validity.

### 4.5 Implementation

- If approved and not vetoed by H4H for legal/safety reasons:
  - Ms. Jarvis and designated operators apply the changes at the next epoch or defined activation date.  
  - Implementation details (contracts touched, parameters updated) are documented in a change log.

---

## 5. Decision‑Making Scope and Limits

### 5.1 DAO Scope (Can Decide)

- Adjusting EMS → M$ base rate within defined bounds.  
- Adjusting per‑user caps and promo budgets within reserve‑safe ranges.  
- Recognizing new categories of qualifying work and Tier 2 roles.  
- Setting or updating game‑layer parameters (quests, ranks, value interactions).  
- Recommending regional expansion and branch parameterization.

### 5.2 Out‑of‑Scope (Cannot Decide)

- Actions that violate Applicable Law or regulatory guidance.  
- Minting beyond reserve‑ratio‑compliant levels.  
- Disabling or weakening hard safety triggers and emergency protections.  
- Using treasury assets for private benefit or unrelated purposes.  
- Overriding H4H’s fiduciary and legal obligations.

In any such case, H4H may decline to implement and must provide a public explanation.

---

## 6. Transparency and Accountability

### 6.1 Public Records

- Governance proposals, discussions, and vote outcomes are published in a public repository (e.g., this GitHub repo and on‑chain logs where feasible).  
- Parameter changes include:
  - Before/after values.  
  - Effective dates.  
  - References to the authorizing proposal.

### 6.2 Reporting

- Periodic governance reports summarize:
  - Key decisions.  
  - Participation metrics (turnout, quorum, diversity of participation).  
  - Any vetoes by H4H and associated rationale.

### 6.3 Conflict of Interest

- DAO participants and monitors are encouraged to declare material conflicts (e.g., business ties to proposals).  
- H4H Board and staff are subject to formal Conflict of Interest policies maintained separately in `legal/`.

---

## 7. Evolution of the DAO

### 7.1 Early‑Phase Monitors and Guardrails

- During early phases, monitors retain limited emergency powers and implementation discretion.  
- The intent is to gradually reduce reliance on monitors as:
  - Participation grows.  
  - Systems are audited and hardened.  
  - Community capacity for governance increases.

### 7.2 Charter Amendments

- Amendments to this Charter are treated as **constitutional proposals** and require:
  - Higher quorum (e.g., 40% of eligible voters).  
  - Higher approval threshold (e.g., 66% super‑majority).  
  - Review and non‑objection by H4H’s Board.

---

*End of `Governance Charter.md`*
