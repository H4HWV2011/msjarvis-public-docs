# The Ms. Jarvis Steward System  

**Where:** Mount Hope, West Virginia  
**What:** A live AI Steward System, not a demo  
**When:** Running in production as of January 2026  

---

## 1. What is Ms. Jarvis?

Ms. Jarvis is a **transparent AI helper** for communities.  
It does not replace people, leaders, or laws. Instead, it:

- Helps organize local data and stories.  
- Builds clear, checked‑again explanations and maps.  
- Shows where power, money, and risk are moving through a place.

All of this is tied to real locations in West Virginia: parcels, buildings, roads, and public data.

Ms. Jarvis is part of a bigger research project called **Polymathmatic Geography**, which studies places where land, law, computers, money, stories, and faith are already tangled together.

---

## 2. The three big questions we are testing

**Q1. Trust and clarity**  
Do residents, partners, and auditors feel that Ms. Jarvis is easier to understand and trust than a black‑box AI or a hard‑to‑follow government process?

**Q2. Seeing extraction**  
Can the system make hidden patterns of “taking without giving back” visible on the map, so that local people can act on them?

**Q3. Stronger local safety nets**  
Does the MountainShares program keep more value circulating in the community and make people feel safer, without turning into an unregulated bank?

These are the questions we are measuring in pilots and ongoing use.

---

## 3. How the system works in 8 steps

The picture of the Ms. Jarvis architecture shows this loop. In plain words:

1. **A question comes in**  
   A resident or partner asks something like:  
   *“Where is food access most fragile in our county?”*

2. **Secure front door**  
   The request comes through a secure web gateway.  
   The system checks who is asking and logs the request.

3. **Steward orchestration**  
   A central “traffic director” checks what rules and limits apply.  
   It decides which tools and data are allowed for this question.

4. **Geospatial grounding (GBIM)**  
   The system looks up the places involved: parcels, stores, roads, census units, and so on.  
   Everything is tied to the map, not just loose text.

5. **Semantic memory (Hilbert‑space)**  
   It then pulls in related documents and notes: research, past answers, policies, and local history that matter for the question.

6. **LLM ensemble reasoning**  
   Several language models look at the combined map data and text.  
   A routing layer picks the right models for the job and combines their answers.

7. **Governance checks**  
   Before anything goes back to a person, the system checks the draft answer against clear rules and “do not cross” lines.  
   Some answers get flagged for human review.

8. **Stewarded output**  
   The final result goes back as a short narrative, an annotated map, or a data table that people can actually use.

---

## 4. What is already running today

- **Scale of code:** More than 51,000 Python modules across 175 services.  
- **Core database:** PostgreSQL + PostGIS, holding millions of records for parcels, buildings, census blocks, and infrastructure.  
- **Semantic memory:** Over 6 million spatial records from West Virginia GIS layers indexed for fast search.  
- **Models:** A mix of local and remote language models, coordinated by a routing and judging layer.  
- **Access:** A locked‑down gateway that logs requests for audit and safety.

This is a live stack in daily use, not a slide deck.

---

## 5. What makes Ms. Jarvis different

Most AI systems:

- Hide how they reach a conclusion.  
- Are trained on global data, with little sense of place.  
- Ask you to “trust the model” without showing receipts.

Ms. Jarvis is built to be different:

- **Place‑based:** Every answer is tied back to real locations in West Virginia.  
- **Traceable:** People can see which data, sources, and rules fed into a given response.  
- **Constrained:** There are written rules about what the system may and may not do.  
- **Supporting, not replacing:** It is meant to support community decisions, not make them on its own.

---

## 6. The three layers of the research program

You can think of the work in three nested layers:

1. **Polymathmatic Geography (the field)**  
   The overall way of studying places where land, law, money, technology, stories, and faith are tangled together.

2. **Quantarithmia (the theory)**  
   A set of ideas and measures for understanding big financial actors (“maximopolies”), big platforms (“megaopolies”), and fairer local alternatives.

3. **Ms. Jarvis and MountainShares (the tools in the world)**  
   The actual running system and local economic program that put the ideas to the test in West Virginia.

The thesis asks: *Do these ideas still make sense when they touch the ground?*

---

## 7. Risks we are watching and guardrails we use

**Main risks:**

- People might treat Ms. Jarvis as if it were a person, a bank, or a government office.  
- The models might quietly learn patterns that favor already powerful actors.  
- Local commons and conversations could be captured by a small group.  
- Sacred places, cemeteries, or family histories could be treated as “just data.”

**Current guardrails:**

- Written **non‑goals**: Ms. Jarvis is *not* a person, a bank, a regulator, or an investment scheme.  
- **Glass‑box design**: logs, data sources, and rules are visible and reviewable.  
- **Charters and policies**: MountainShares and The Commons have clear rules, roles, and audit paths.  
- **Human review** on sensitive questions and flagged answers.

---

## 8. Who this handout is for

- **Defense committees and reviewers** – to see that the work is both theoretical and very practical.  
- **Funders** – to understand what is already built, what questions we are testing, and where new support would go.  
- **Community partners** – to see that the system is designed to be accountable to place and people.  
- **Policy makers and regulators** – to see an example of AI that is designed around transparency and limits from day one.

---

## 9. Where to learn more

- **Full overview:** `thesis/00-overview.md`  
- **Field card for the discipline:** `discipline/Polymathmatic-Geography-Field-Card.md`  
- **Architecture figure:** Section 2.6 in `thesis/00-overview.md`  
- **Governance details:** MountainShares DAO and The Commons documents in this repository
