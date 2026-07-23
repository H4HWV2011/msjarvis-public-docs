# 37. Constitutional Principles Service

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 37.1 What This Service Does

The constitutional principles service is a **governance gate** that checks whether a proposed action fits the project’s constitutional commitments before it is allowed to gain authority.

Here, “constitutional” is concrete, not decorative. The service is rooted in:

- the **United States Constitution**;  
- the **West Virginia Constitution**.

These are used as reference frameworks for rights, limits, due process, and bounded authority. The service sits in the promotion path to help decide whether a candidate action may move from **internal proposal** to **approved system behavior**.

---

## 37.2 Live Service and Ports (July 2026)

As of the July 2026 evidence:

- The **constitutional guardian** is live on host port **8091**.  
- The **BBB** (blood–brain barrier) is live on host port **8016** and connected to the guardian.  
- The guardian exposes two review endpoints:  
  - `/constitutional-principles/review`  
  - `/constitutional/review`.

These endpoints accept structured payloads and return governance decisions. This chapter does **not** rely on any April 2026 container counts or database sizes; it reflects the as‑built July 2026 state only.

---

## 37.3 Constitutional Materials in the System

The constitutional principles service works alongside:

- internal corpora that store the **U.S.** and **West Virginia** constitutions;  
- related governance texts and commentary;  
- retrieval tools that can pull relevant passages for context.

The purpose is **not** to act as a court or replace lawyers. Instead, the service:

- brings constitutional ideas (rights, restraints, due process) into the decision pipeline;  
- helps flag actions that look like they would violate those commitments;  
- supports a place‑rooted understanding of lawful power in West Virginia communities.

---

## 37.4 The Guardian Payload Contract

Every request to the constitutional service must carry a **structured payload**. A typical contract includes:

- `actor_role` – who is acting (for example, system module, operator, automation).  
- `context` – in what situation (session, workflow, scenario).  
- `action_type` – what kind of action is proposed (promotion, disclosure, registration, memory write, etc.).  
- `content` – the substance of what is being promoted or done.  
- `metadata` – provenance, identifiers, and other details needed for review.

If this payload is **missing required fields** or structurally invalid, the guardian:

- rejects the request;  
- treats the action as **not constitutionally approved**;  
- causes the promotion path to **fail closed**.

Simply calling the endpoint is not enough; the payload must be complete and valid.

---

## 37.5 What the Guardian Checks

When a valid payload is sent to `/constitutional-principles/review` or `/constitutional/review`, the service checks questions such as:

- Is this actor allowed to attempt this action in this context?  
- Does the action respect consent and privacy (for example, no private disclosure without permission)?  
- Does it avoid obvious conflicts with constitutional rights or protections?  
- Is there any sign of bypassing required oversight or due process within the system’s own rules?

Examples:

- A **governed promotion payload** with proper consent and context can pass.  
- A **consent‑bypass** or **private‑disclosure** payload is expected to **fail closed**.  
- A payload that omits required consent fields is rejected at the schema level.

---

## 37.6 BBB and Guardian Together

The **BBB** and the **constitutional guardian** work together in the promotion path:

- BBB sits at a boundary between lower‑risk internal reasoning and higher‑authority consequences.  
- The guardian provides constitutional review within that boundary.  
- Both expose **health surfaces** so watchdogs and operators can confirm they are up and responding.

For rural operators, this means you can:

- check that BBB on port **8016** is healthy;  
- check that the guardian on port **8091** is healthy;  
- verify that promotion calls actually pass through these gates instead of bypassing them.

---

## 37.7 Valid vs. Invalid Promotion Payloads

From the July 2026 closure evidence:

- **Valid governed promotion payloads pass** constitutional review.  
- **Consent‑bypass or private‑disclosure payloads fail closed.**  
- **Missing required fields** are **rejected by schema validation** before approval.

In practice:

- a well‑formed request, with all required fields and consent markers, can be approved;  
- a request trying to expose private information without consent is blocked;  
- a request that forgets to include necessary context fields is treated as **invalid**, not “probably fine.”

---

## 37.8 Role in the Promotion Pipeline

The constitutional principles service is one part of a broader promotion gate. A typical path is:

1. **Sandbox reasoning** produces a candidate action or answer.  
2. Other judges/checks evaluate truth, coherence, safety, provenance, etc.  
3. A promotion request is constructed with a **guardian payload**.  
4. The request is sent through BBB and the **constitutional review endpoints**.  
5. Only if constitutional review **approves** (and other gates agree) can promotion proceed.

If the guardian response is a failure, or if the payload is malformed, the system:

- does **not** treat the action as approved;  
- fails closed and logs the problem.

---

## 37.9 Place-Aware Constitutional Orientation

Because Ms. Allis is rooted in **Mount Hope, West Virginia**, the constitutional service:

- names and respects both the **U.S. Constitution** and the **West Virginia Constitution**;  
- treats local state‑level rights and limits as part of its frame of reference;  
- avoids pretending that governance is the same everywhere.

The service still does **not** give legal advice or act as a lawyer. It is a **technical mechanism** to enforce internal rules that are themselves influenced by constitutional traditions.

---

## 37.10 What This Chapter Does Not Claim

Within this closure, Chapter 37 does **not** claim:

- perfect legal correctness;  
- that the system is a court or legal advisor;  
- that all constitutional questions are solved or provably encoded;  
- clinical or safety guarantees for downstream human decisions.

It only claims:

- a **live constitutional guardian** on port 8091;  
- a connected **BBB** on port 8016;  
- working review endpoints;  
- fail‑closed handling of malformed and consent‑bypass payloads;  
- explicit naming of the **United States** and **West Virginia** constitutions as reference frameworks.

---

## 37.11 Step-by-Step View for Rural Developers

In everyday terms, when something important is about to happen (for example, a promotion or disclosure that touches identity or public impact), the flow is:

1. Ms. Allis builds a **guardian payload** describing who is acting, what they want to do, in what context, and with what content.  
2. That payload is sent through the **BBB** to the **constitutional review endpoints**.  
3. The guardian checks that the payload is structurally valid and constitutionally acceptable under the project’s rules.  
4. If checks pass, the rest of the promotion gates may proceed.  
5. If checks fail, the action is **blocked** and the event is logged.

This keeps “what is allowed” tied to a concrete, inspectable service instead of being hidden inside model behavior.

---

## 37.12 Closing Statement

The Constitutional Principles Service makes **constitutional restraint** a real part of Ms. Allis’s promotion path. By running on live ports, requiring structured guardian payloads, failing closed on malformed or consent‑bypass requests, and explicitly naming the **U.S.** and **West Virginia** constitutions as reference points, it turns constitutional ideas into an operational gate.

For rural communities, this means the system’s big moves—especially around disclosure and authority—must pass through a **concrete constitutional checkpoint**, not just the good intentions of the developers.
