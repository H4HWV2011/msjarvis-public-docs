# MountainShares Phase 1: Economic Safety Specification

**Version:** 1.0  
**Date:** January 15, 2026  
**Status:** DAO Governance Document  
**Scope:** West Virginia Pilot (Phase 2)

---

## 1. Core Economic Principles

- **Recognition Ledger (Unlimited):** All EMS hours logged on-chain with full UEI, geo, org, and timestamp data. No hard cap; serves as permanent audit trail and identity marker.
- **Spendable M$ (Capped & Reserve-Backed):** Convertible portion pegged to treasury backing ratio. Starts conservatively; can only increase with DAO vote inside safe thresholds.
- **Hard Triggers (Automatic, Non-Negotiable):** Ms. Jarvis enforces automatically; no DAO override possible.

---

## 2. Starting Conversion Rate & Per-User Caps (Phase 2 Bootstrap)

### 2.1 Global Base Rate
- **Starting:** 0.2 M$ per EMS hour
- **Range:** Can adjust 0.1 – 1.0 M$ per EMS hour via DAO vote, *only if* reserve ratio ≥ threshold (see Section 3)
- **Example:** If user logs 8 hours of verified caregiving at 0.2, they earn 1.6 M$ (capped further by tier, below)

### 2.2 Per-User Convertible Caps (Monthly)

| User Tier | Definition | Monthly Cap (M$) | Weekly Cap | Daily Cap |
|-----------|-----------|------------------|-----------|-----------|
| **Tier 1** | General Commons, light EMS (non-mission-critical) | 40 M$ | 10 hrs | 1–2 hrs |
| **Tier 2** | Verified EMS, caregiving, high-need community roles (geo+UEI validated) | 80 M$ | 20 hrs | 4 hrs |

**Tier Assignment Logic:**
- Tier 1 default for all new UEIs.
- Tier 2 requires: org co-sign (nonprofit, EMS, mutual aid network) + geo-fence verification + Commons trust signals.
- Ms. Jarvis flags tier eligibility; final assignment by DAO governance or pre-agreed rules.

### 2.3 Examples at 0.2 Base Rate

- **Tier 1 user, 30 EMS hours/month:** 30 × 0.2 = 6 M$ (well under 40 M$ cap) ✓
- **Tier 2 user, 200 EMS hours/month (very active caregiver):** capped at 80 M$ convertible, even though raw value = 40 M$ (within tier cap) ✓
- **If rate rises to 1.0 M$/hour via DAO vote:** Same user gets 80 M$ from same 80 EMS hours ✓

---

## 3. Treasury Backing & Hard Reserve Thresholds

### 3.1 Reserve Ratio Definition

```
Reserve Ratio = Liquid Backing Assets (USD) / Total Outstanding Spendable M$
```

**Backing Assets Include:**
- USD load fees (users converting USD → M$)
- Merchant fees (% of transactions)
- CLIO NFT revenue
- DAO-approved grants or donations
- *Excludes:* EMS recognition hours, future promises

### 3.2 Safety Thresholds (Ms. Jarvis Enforces Automatically)

| Reserve Ratio | Global Base Rate | User Cap Adjustment | Bonus Promos | Action |
|---------------|------------------|-------------------|------------|--------|
| ≥ 1.5 | 1.0 M$/hr (full 1:1) | 120 M$/mo (Tier 2) | Enabled | DAO can vote to increase |
| 1.0 – 1.49 | 0.5–0.8 M$/hr (DAO-controlled) | 80–100 M$/mo | Reduced | DAO can vote to increase *if trend stable* |
| 0.75 – 0.99 | 0.2–0.4 M$/hr (DAO-controlled) | 40–80 M$/mo | Paused | DAO can vote *only to hold steady* |
| < 0.75 | 0.1 M$/hr (Emergency Floor) | 20–40 M$/mo | Frozen | Auto-tighten; no DAO votes increase anything |

**Automatic Trigger Logic:**
- Ms. Jarvis recalculates reserve ratio daily.
- If ratio crosses a threshold boundary, new rate and caps apply at next epoch (24–48 hour notice).
- No human approval required for *downward* adjustments; they fire automatically.

---

## 4. Monthly Promo & Bonus Pool (Funded Separately)

### 4.1 Promo Pool Budget
- **Source:** Separate allocation from total fees (distinct from EMS conversion budget).
- **Max Size:** 2–3% of monthly processed volume, capped at X M$/month (DAO sets X).
- **Example:** If volume is 100k USD/month, promo pool ≤ 2–3k M$/month.

### 4.2 Bonus Rules
- All bonuses (e.g., "+50 M$ for visiting Nicholas Pharmacy") draw from pool.
- Once pool is exhausted in a month, no new bonuses are offered until next cycle.
- **Bonuses still count against user's per-month convertible cap** (don't bypass it).
- Bonuses pause automatically when reserve ratio < 1.0.

---

## 5. DAO Authority: What Can Change & How

### 5.1 DAO Can Vote To Increase (Requires Super-Majority, e.g., 66%+)

✅ **Global base rate** (0.2 → 0.5 → 0.8 → 1.0), *only if reserve ratio is in safe zone*  
✅ **Per-user monthly caps** (40/80 → 60/100 → 80/120), *only if reserve ratio supports it*  
✅ **Tier assignment criteria** (e.g., add new community roles as Tier 2)  
✅ **Promo pool budget** (increase X M$/month), *only if backing assets support it*  
✅ **Hard trigger thresholds themselves** (move 1.5 to 1.4, etc.), *only once system is stable + audited*

### 5.2 DAO Cannot Override (Hard Trigger Rules)

❌ Vote to mint M$ without reserve backing  
❌ Disable automatic rate/cap reductions when ratio drops below threshold  
❌ Allow EMS conversions that would breach reserve ratio math  
❌ Overrule legal / safety prohibitions (drugs, weapons, exploitation, etc.)

### 5.3 Ms. Jarvis Authority (Automatic, No Vote Needed)

✅ **Enforce reserve ratio checks** every 24 hours; apply auto-adjustments if thresholds crossed  
✅ **Flag and freeze** EMS/M$ flows tied to illegal content or high-risk patterns  
✅ **Calculate and publish** daily reserve ratio, backing assets, outstanding M$, and "next rate tier" projection  
✅ **Tier assignments** based on pre-agreed rules (org co-sign + geo verification)  
✅ **Pause bonuses** when reserve ratio < 1.0  

---

## 6. One UEI = One Vote

- **Governance Token:** Each UEI receives 1 equal vote on all Phase 2 DAO proposals.
- **Voting Rights:** After 30 days on-platform (anti-sybil protection) and min. 10 EMS hours logged.
- **Vote Scope:** All items in Section 5.1 (increases/policy changes); cannot vote on Section 5.2 (hard triggers) or illegal activity rules.

---

## 7. Phase 2 → Phase 3 Graduation Criteria

**Transition to Phase 3 only when ALL of these hold for 60+ days:**

- Reserve ratio stable ≥ 1.0 (no dips below threshold)
- Monthly processed volume ≥ 200k USD (realistic merchant/load flow)
- Active UEIs ≥ 2,000 (meaningful community adoption)
- Zero systemic fraud or reserve-threatening exploits
- DAO governance participation ≥ 30% quorum on key votes

**Phase 3 Changes:** Caps can rise further; base rate can approach 1.0; statewide rollout planning begins.

---

## 8. Safety Prohibitions (Hard-Coded, No Vote)

**Banned Content / Activity Categories:**

| Category | Prohibition | Detection | Consequence |
|----------|-----------|-----------|------------|
| **Illegal Drugs** | Cannot buy/sell/promote illegal drugs or paraphernalia | Content filter + pattern matching + keyword flagging | Account freeze + report to authorities (if required) |
| **Weapons** | Cannot facilitate illegal weapons transfers or trafficking | Content filter + geo + pattern | Account freeze + report |
| **Exploitation** | No sexually explicit content, porn, child abuse material, or coerced sex work | NLP + imagery scanning + manual review | Immediate permanent ban |
| **Fraud/Forgery** | No fake documents, false UEI claims, or spoofed org identities | UEI registry verification + geo cross-check | Account freeze + investigation |

**Enforcement:**
- Ms. Jarvis auto-flags and freezes.
- Human review within 24–48 hours.
- Clear appeals process for false positives.
- Transparent logging (anonymized) of all freezes/bans.

---

## 9. Transparency & Dashboards (Ms. Jarvis Public API)

Every UEI can see (updated daily):

- Personal: hours logged, M$ balance, convertible budget remaining, tier status
- Network: current reserve ratio, backing assets breakdown, total outstanding M$, next rate tier projection
- DAO: current proposals, vote status, outcome history, policy changelog

**Purpose:** Make "should we vote to raise the rate?" a decision based on visible data, not trust.

---

## 10. Audit & Governance Cadence

- **Daily:** Ms. Jarvis publishes reserve ratio, auto-applies threshold-triggered adjustments
- **Weekly:** Network snapshot (active users, volume, M$ minted, promo spend)
- **Monthly:** Full treasury audit, DAO governance session (proposals + votes)
- **Quarterly:** External audit by independent WV nonprofit (if funds permit)

---

## 11. Sunset & Emergency Powers

### 11.1 If Reserve Ratio Falls Below 0.5 (Critical)
- All EMS conversions pause immediately
- Only USD loads and merchant fees accepted
- Emergency governance session called within 48 hours
- Options: (a) shut down gracefully, (b) seek external funding, (c) reset with community consent

### 11.2 If Ms. Jarvis Detects Coordinated Fraud/Attack
- Affected accounts frozen pending review
- Daily public reporting of incident
- Emergency DAO vote on remediation (clawback, reset, shutdown)

---

## Appendix A: Definitions

- **UEI:** Unique Entity Identifier (per user, including individuals and orgs)
- **EMS:** Energy/work hour (1 hour = 1 EMS credit, logged with UEI + geo + timestamp)
- **M$:** MountainShares token (spendable, reserve-backed, convertible)
- **Backing Assets:** Liquid USD and near-liquid reserves (fees, donations, CLIO revenue)
- **Reserve Ratio:** Backing Assets / Outstanding M$; Ms. Jarvis enforces thresholds
- **Tier:** User classification (Tier 1 = general, Tier 2 = verified EMS/caregiving)
- **Hard Trigger:** Automatic enforcement rule (Ms. Jarvis, no override)
- **DAO Vote:** Community governance (1 UEI = 1 vote, super-majority for increases)

---

## Appendix B: Example Governance Scenario

**Month 3 of Phase 2:**

- Reserve ratio = 1.2 (healthy, above 1.0 threshold)
- Monthly processed volume = 150k USD
- Active UEIs = 1,200
- EMS logging is consistent, no fraud detected
- Community feedback: "40–80 M$/month is meaningful but tight"

**DAO Proposal:** "Raise global base rate from 0.2 → 0.35 M$/hr and tier caps from 40/80 → 60/100 M$/mo"

**Vote:** 68% in favor (super-majority)

**Result:** Next epoch (24 hrs), all users get 1.75× their previous earning potential.  
- Tier 1: now capped at 60 M$/mo instead of 40  
- Tier 2: now capped at 100 M$/mo instead of 80  
- Ms. Jarvis recalculates reserve ratio: still 1.18 (healthy)

**Rinse, repeat monthly.** As volume grows and reserve ratio strengthens, the community votes its own way up the scale toward 1:1.

---

## Sign-Off

This spec is a **living document.** Minor corrections (typos, examples) can be made by DAO vote with simple majority. Major changes (thresholds, safety rules, hard triggers) require super-majority + independent audit.

**Drafted in collaboration with:** MountainShares DAO, Ms. Jarvis Governance Team  
**Next Review:** Post-Phase 2 Launch + 30 Days of Live Data

---

*"People earn what they do. The commons holds what we decide together. Ms. Jarvis watches so nobody can wreck it."*
