# The Commons Gamification: The Daily Life Game

> **Disciplinary Context: Appalachian Economic Commons**
> This document instantiates Polymathmatic Geography principles P1, P9, and P16:
> - **P1 – Every where is entangled:** Every quest, badge, and streak is tied to a specific place, activity, and community in West Virginia — not abstract engagement metrics. See https://github.com/H4HWV2011/msAllis-public-docs/blob/main/docs/Polymathmatical-Geography.md
> - **P9 – Transparency and traceability:** All value interactions, quest completions, and streak milestones are logged to the recognition ledger with UEI, geo, and timestamp. The game is visible and auditable.
> - **P16 – Power accountable to place:** Quest categories, seasonal campaigns, and regional challenges are proposed and governed by community participants — not designed by distant platform teams and imposed on the community.

**Version:** 1.1 (Draft)
**Date:** March 12, 2026
**Status:** Design Document
**Scope:** The Commons App — West Virginia Pilot (Phase 0 through Phase 3)
**Related documents:** [MountainShares Gamification: The Contribution Game](../mountainshares-dao/MountainShares%20Gamification%3A%20The%20Contribution%20Game.md), [Program Rules](../mountainshares-dao/MountainShares%20Program%20Rules(Draft).md), [KPI Specification](../mountainshares-dao/MountainShares%20KPI%20Specification.md), [Phase 1 Economic Safety Specification](../mountainshares-dao/MountainShares%20Phase%201%3A%20Economic%20Safety%20Specification.md)

---

## 1. Purpose

The Commons game is the **daily game.** It is light, social, place-specific, and immediately rewarding. It answers the question: *what can I do today that matters in my community and earns recognition for it?*

The Commons game is the on-ramp to MountainShares. Every qualifying quest completion, streak, and value interaction feeds EMS hours into the recognition ledger — building rank and governance standing in the MountainShares contribution game without participants needing to think about governance at all.

The Commons game is designed for everyone: the elder who wants to share a recipe and earn a few M$, the teenager scanning trail markers after school, the small business owner rewarding loyal local customers, the mutual aid organizer tracking volunteer hours, and the ground-truther walking door-to-door to verify local data. It should feel like community life, not like a financial product.

---

## 2. Three-Stage Platform Arc

The Commons is not built all at once. It grows with the community and the economy.

| Stage | Model | Feel | Phase |
|-------|-------|------|-------|
| **Stage 1: Marketplace** | Barter & trade / Facebook Marketplace | Hyperlocal, neighbor-to-neighbor, community board — people trading, offering, and requesting within their holler and town | Phase 1 (early) |
| **Stage 2: Discovery** | TikTok-style content and quest discovery | Short-form local content, viral community moments, quests as content — trust spreading outward through stories | Phase 1 (mature) |
| **Stage 3: Full Commerce** | Amazon-style local marketplace | Full merchant catalog, search, inventory, fulfillment — M$ circulating at scale, closed-loop economy fully alive | Phase 2+ |

Features, quests, badges, and leaderboards are designed to grow with the platform arc. Stage 1 emphasizes discovery and human connection. Stage 2 amplifies through content. Stage 3 locks in the economic loop.

---

## 3. The Currency: Value Interactions

The basic unit is a **value interaction** — a concrete, verified action that the community has decided matters.

- Help a neighbor.
- Attend a workshop.
- Scan a trail marker.
- Buy local with M$.
- Map something.
- Teach someone.
- Verify a local record.
- Respond to a Ms. Allis data ping.
- Show up.

Value interactions stack into quests, streaks, and seasonal campaigns. They log EMS hours to the recognition ledger automatically when they qualify as commons work. They draw from the promo pool for bonus M$ rewards when the reserve ratio permits.

---

## 4. Quest Categories

Quests are structured challenges with defined completion conditions, time windows, and rewards. They are proposed by community participants, approved through governance within safety bands, and funded from the promo pool.

| Category | Examples | EMS Earning |
|----------|---------|------------|
| **Local Commerce** | Visit a participating merchant; make a purchase with M$; refer a new merchant; list an item for barter | Merchant visit logged; M$ transaction recorded |
| **Mutual Aid** | Fulfill a help request; donate supplies; provide transportation; check on a neighbor | 1 EMS hr per verified hour of aid |
| **Learning and Teaching** | Attend a workshop; teach a skill session; complete a learning module; mentor a participant | 1 EMS hr per verified hour |
| **Cultural Preservation** | Scan a Clio trail marker; contribute an oral history; attend a heritage event; document a tradition | 1 EMS hr per verified hour |
| **Land and Mapping** | Complete a GIS data validation; map a local asset; submit a place record; verify a parcel | 1 EMS hr per verified hour |
| **Data Stewardship** | Collect contact information (with consent) for local places and people; respond to a Ms. Allis verification ping to confirm data is current; update an outdated record | 1 EMS hr per verified hour; EMS awarded to record-holder for responding to verification ping |
| **Community Events** | Attend a Commons-hosted event; volunteer at a community gathering; organize a local program | 1 EMS hr per verified hour |
| **Governance Participation** | Vote in a DAO proposal; attend a governance session; review a proposal and submit feedback | 1 EMS hr per session |
| **Emergency Preparedness** | Complete an emergency prep activity during an active NOAA alert period; participate in a resilience drill | 1 EMS hr per verified activity; promo bonus when reserve permits |

---

## 5. Data Stewardship — Ground Truthing Detail

Data stewardship is one of the most important and underrecognized commons activities. Rural data decays fast — businesses close, phone numbers change, addresses shift. The Commons maintains a **living, verified data layer** by using the community to keep it current.

### How It Works

1. **Collection:** Community Champions (and eventually any participant) collect contact information — email and SMS — for local places, businesses, organizations, and services, with **explicit consent** documented at collection time.
2. **Verification cycles:** Ms. Allis runs automated verification pings every **6–12 months** to each consenting record holder, asking them to confirm or update their record.
3. **Response = EMS:** When the record holder responds and confirms or updates their data, they earn EMS hours. The record is marked verified with a new timestamp.
4. **Confidence scoring:** Ms. Allis maintains a data confidence score on each record based on verification recency, response history, and cross-source consistency.
5. **Champion role evolution:** Ground truthing is the primary Champion focus in Phase 1 early. As the data layer matures, Champion focus shifts — but the verification cycle continues automatically through Ms. Allis pings.

### Consent Requirements

- Contact information may only be collected with **explicit opt-in** at the time of collection.
- Record holders may opt out of future verification pings at any time.
- Collection workflow must document: collector UEI, collection date, consent method, and contact type.
- Privacy Policy and Terms govern all contact data handling.

---

## 6. Quest Structure

### 6.1 Daily Quests
Small, repeatable. Reset every 24 hours.
- "Log at least one value interaction today."
- "Visit a local merchant."
- "Check in to The Commons."

### 6.2 Weekly Quests
Moderate effort. Reset every 7 days.
- "Complete 3 mutual aid hours this week."
- "Attend one community event."
- "Make 2 purchases at local merchants using M$."
- "Verify or update 5 local records."

### 6.3 Seasonal Campaigns
Large, community-wide. Proposed and governed by the community. Examples:
- **Spring Trail Mapping Drive** — document new points of interest along the Coalfield Chronicles Trail
- **Winter Mutual Aid Month** — log caregiving and neighbor-support hours through the cold season
- **Harvest Heritage Week** — food preservation, oral history collection, and cultural documentation
- **Back to School Commons** — education and mentoring hours during the school year opening
- **Data Accuracy Drive** — ground-truthing sprint targeting a specific county or category of records

### 6.4 Regional Quests
Proposed by Captains for their specific geographic area. Approved through governance.
- "Oakvale Outreach Challenge — log 100 mutual aid hours in the Oakvale corridor this month."
- "Mount Hope Trail Completion Badge — scan all QR markers on the Historic Walking Trail."
- "Nicholas County Data Sprint — verify 50 local asset records with documented consent."

---

## 7. Streaks

Streaks reward consistent participation over time. They are visible on the participant’s Commons profile.

| Streak | Trigger | Milestone Rewards |
|--------|---------|------------------|
| **Daily Contributor** | Log at least 1 qualifying activity per day | Streak counter visible; badge milestones at 7, 30, 90, 365 days |
| **Weekly Presence** | At least 1 value interaction per week | Maintained rank stability; weekly streak badge |
| **Monthly Anchor** | Complete at least 1 quest per month for 6 consecutive months | EMS hour bonus credited to recognition ledger |
| **Seasonal Champion** | Complete all quests in a seasonal campaign | Seasonal badge + promo M$ bonus from pool (reserve-ratio gated) |
| **Verification Streak** | Respond to 3 consecutive Ms. Allis verification cycles | Verification Veteran badge |

---

## 8. Visual Badge System — The Commons Layer

Badges in The Commons follow the same visual design language as the MountainShares contribution game. See [MountainShares Gamification: The Contribution Game](../mountainshares-dao/MountainShares%20Gamification%3A%20The%20Contribution%20Game.md) Section 5 for the full design principles.

### Phase 0 Founding Badges (Iron/Charcoal — Permanent)

| Badge | Visual | Earned By |
|-------|--------|-----------|
| **Commons Founder** | Mountain silhouette, double-ring | Phase 0 participant, 1+ EMS hour |
| **Red-Team Pioneer** | Shield with lightning bolt | 1+ verified security finding |
| **Critical Path** | Shield with red core | Critical/high severity finding |
| **Charter Witness** | Open scroll | 3+ governance docs reviewed |
| **First Cartographer** | Compass rose | GIS/mapping/trail work in Phase 0 |
| **Safety Champion Founder** | Shield + institutional pillar | Institution-linked Safety Champion |
| **Incident Architect** | Forge hammer | Post-incident review participation |
| **Groundbreaker** | Pickaxe breaking ground, double-ring | 10 EMS hrs + 30 days, Phase 0 only |

### Phase 1 Activity Badges (Earth Tones)

**Data Stewardship**

| Badge | Visual | Earned By |
|-------|--------|-----------|
| **Ground Truthing** | Magnifying glass over map pin | First data verification or contact collection |
| **Data Keeper** | Map pin + checkmark | 25 records verified or updated |
| **Living Map** | Topographic lines, glowing | 100 records verified or updated |
| **Verification Veteran** | Calendar + checkmark | Responded to 3+ Ms. Allis verification cycles |

**Commons Life**

| Badge | Visual | Earned By |
|-------|--------|-----------|
| **Neighbor** | Two hands | First mutual aid interaction |
| **Mutual Aid Hundred** | Flame with "100" | 100 mutual aid EMS hours |
| **Knowledge Spark** | Open book, spark | First education/teaching hour |
| **Knowledge Keeper** | Stacked books | 100 education EMS hours |
| **Memory Keeper** | Quill + mountain | First cultural preservation hour |
| **Land Memory** | Topographic hexagon | 50 GIS/mapping/cultural hours |
| **Trail Walker** | Boot print on trail | All Mount Hope Trail QR markers scanned |
| **Coalfield Chronicler** | Mine lamp | 10+ Coalfield Chronicles Trail markers |
| **First Steps** | Storefront + M$ coin | First merchant purchase with M$ |
| **Local First** | Storefront, clay | 10 merchant purchases with M$ |
| **Commons Regular** | Sunrise over holler | 30-day active streak |
| **Emergency Ready** | Storm cloud + hand | Emergency preparedness activity during active NOAA alert |
| **Story Holder** | Feather + mountain | Verified oral history or place narrative contributed |
| **Market Maker** | Two-arrow exchange, storefront | First sale or trade to another participant inside The Commons |

### Phase 2 Commerce and Discovery Badges (Copper/Amber)

| Badge | Visual | Earned By |
|-------|--------|-----------|
| **Marketplace Pioneer** | Storefront, amber glow | First Phase 2 marketplace transaction |
| **Local Merchant** | Scale/balance, copper | Merchant reaches 100 M$ in transactions |
| **Barter Master** | Two-arrow exchange, amber | Completes 10 barter/trade exchanges |
| **Commons Curator** | Shelves with items | Lists 10+ items in marketplace |
| **Discovery Engine** | Play button over mountain | First content post that drives a verified value interaction |
| **Content Keeper** | Camera + mountain | 10 Commons content pieces that earn engagement |

### Phase 3 Legacy Badges (Gold/River-Glass)

| Badge | Visual | Earned By |
|-------|--------|-----------|
| **River Glass** | River-polished stone, iridescent | 1,000+ EMS hours across 10+ categories |
| **Appalachian Roots** | Full mountain range, gold | 3+ years active, hours in every category |
| **Living Economy** | Closed-loop river symbol | M$ transactions completing a documented local economic loop |
| **Founding Legacy** | Pickaxe + gold tree overlay | Groundbreaker (Phase 0) who reaches Champion rank |

---

## 9. Leaderboards

The Commons has **community-visible leaderboards** that celebrate local contribution. All leaderboards are opt-in — participants choose to appear by UEI handle or remain anonymous.

| Leaderboard | Scope | Reset |
|-------------|-------|-------|
| **Most value interactions this week** | Neighborhood / regional | Weekly |
| **Top contributors by category** | Mutual aid, learning, cultural preservation, data stewardship | Monthly |
| **Quest completion leaders** | Current seasonal campaign | Per campaign |
| **Merchant of the month** | Most M$ received by a local business | Monthly |
| **Streak leaders** | Longest active daily contributor streaks | Live |
| **Regional Commons builders** | Most EMS hours in a defined geographic area | Quarterly |
| **Top data stewards** | Most records verified/updated | Monthly |

---

## 10. How The Commons Game Feeds MountainShares

Every qualifying Commons activity automatically logs EMS hours to the recognition ledger.

| Commons Action | MountainShares Effect |
|---------------|----------------------|
| Complete a caregiving quest | +EMS hours → recognition ledger → rank progression |
| Respond to Ms. Allis verification ping | +EMS hours → Data Keeper progress |
| Hit a 30-day streak | Commons Regular badge earned; EMS milestone logged |
| Finish a seasonal campaign | EMS hours logged; promo M$ from pool (reserve-ratio gated) |
| Reach 100 EMS hours | Silver rank unlocked → Steward eligibility opens |
| Complete governance participation quest | EMS logged + DAO vote counted toward Governance Voice badge |
| List and sell item in marketplace | Market Maker badge; M$ transaction logged |

---

## 11. What The Commons Game Does NOT Do

- Quest rewards and streak bonuses **do not bypass per-user spendable M$ caps** — all bonus M$ draws from the promo pool and counts against monthly limits per the Economic Safety Specification.
- Promo pool bonuses **pause automatically** when the reserve ratio falls below 1.0. Participants are notified by Ms. Allis with a plain-language explanation.
- No Commons quest, badge, leaderboard position, or streak changes vote weight or creates financial rights.
- Discovery badges and seasonal achievements are recognition only — they do not create equity, ownership, or expectation of financial return.
- Benefits-Sensitive Account participants are protected: Commons participation is fully supported, but EMS earning throttles and balance caps defined in Program Rules apply.

---

## 12. Ms. Allis in The Commons Game

Ms. Allis is the game layer’s guide and narrator. She is present throughout The Commons app experience.

- Surfaces available quests, active campaigns, and streak status through the chatbot UI
- Notifies participants of new badge achievements in plain, warm language
- Answers questions about how Commons activities translate to EMS hours and rank
- Runs data stewardship verification pings every 6–12 months and awards EMS for responses
- Flags when promo pool is low or bonuses are paused, with a plain explanation of why
- Surfaces local leaderboard context and celebrates community milestones
- Connects participants to relevant quests based on their location, history, and interests
- Reminds Benefits-Sensitive Account holders of relevant protections when approaching thresholds

Ms. Allis does not manipulate engagement or maximize time-on-platform. Her role is to help participants find meaningful activities in their community, understand what they’ve earned, and connect their daily actions to the larger commons they’re building.

---

## 13. Governance of the Game Layer

The Commons game layer is not static. Quest categories, seasonal campaigns, streak mechanics, badge criteria, and promo pool allocations are all governed through the MountainShares DAO within safety bands.

- **Any eligible participant** can propose a new quest, badge, or seasonal campaign.
- **Captains** can propose regional quests for their geographic area.
- **System monitors** screen proposals for conflicts with reserve ratio safety, legal constraints, and benefits-sensitive protections.
- **DAO votes** approve or reject game layer changes through the standard proposal lifecycle defined in the Governance Charter.
- **Ms. Allis** surfaces the impact of proposed game layer changes on reserve ratio projections and KPI trends to inform governance decisions.

The game belongs to the community. Its design evolves through the same democratic process as every other parameter in MountainShares.

---

*"Every scan, every hour, every visit, every ping answered — the commons sees it, remembers it, and builds on it."*
