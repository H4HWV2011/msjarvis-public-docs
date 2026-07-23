# 27. Web Research and Autonomy

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 27.1 Autonomy in Ms. Allis

In Ms. Allis, **autonomy** means the ability to go out, gather information, and form candidate conclusions under guardrails. It does **not** mean that whatever is found on the web becomes truth or guidance automatically.

The system can:

- decide what to search for;  
- follow links and APIs;  
- refine queries and compare sources;  
- keep a research thread going over time.

All of that happens inside a governed architecture. Research initiative is allowed; **ungoverned assertion is not.** Autonomy here is “the freedom to investigate inside a fence,” not “the freedom to declare anything you find as fact.”

---

## 27.2 Research Ingress: How Web Data Enters

When Ms. Allis performs web research, the results arrive as **research ingress** and go first into the **internal-state sandbox**.

Step‑by‑step:

1. A research request is prepared (for example, “find current policy on X”).  
2. Web or external tools return pages, snippets, or structured data.  
3. All retrieved material is treated as **raw evidence**, not as accepted knowledge.  
4. That raw evidence is placed into the **sandbox** on port `8042` as provisional internal state.

At this point:

- nothing has been promoted;  
- nothing has been written to background patterns or identity memory;  
- nothing has been treated as guidance.

The system is just saying, “Here is what we found; now we have to think about it.”

---

## 27.3 From Retrieval to Candidate Findings

Inside the sandbox, Ms. Allis turns raw results into **candidate findings**.

This includes:

- clustering similar results;  
- discarding clearly broken or contradictory items;  
- drafting possible conclusions (“candidate explanations”);  
- attaching uncertainty and provenance.

You can think of this as the **“rough notes and draft answer”** stage. The important rule is:

- retrieved content is **R** (raw retrieval),  
- sandbox-processed content is **candidate state**,  
- neither is yet **K** (governed knowledge) or **G** (approved guidance).

Formally, the system keeps the distinctions:

- \(R \neq K\) – retrieval is not the same as governed knowledge.  
- \(R \neq G\) – retrieval is not the same as approved guidance.

So even if a web page sounds confident, it is still just one piece of candidate evidence inside the sandbox.

---

## 27.4 Constitutional Review Before Promotion

Before any candidate finding can move toward being treated as “what Ms. Allis says,” it must pass **constitutional review**.

Constitutional review checks things like:

- policy constraints;  
- safety and harm rules;  
- disallowed content classes;  
- domain limits (for example, medical, legal, financial caution);  
- place‑ and community‑specific guardrails.

If constitutional checks fail, the outcomes can be:

- **reject** – the finding is blocked outright;  
- **revise** – narrow the claim or change the framing;  
- **human review** – escalate to a human, especially in high‑stakes settings;  
- **limited approval** – allow use only with warnings or scope limits.

Only findings that **pass** constitutional review can continue toward full promotion.

---

## 27.5 Three Live Darwin Gödel Machines

On your system, **three real Darwin Gödel Machine (DGM) containers** are live and participate in evaluating autonomous research:

- `nbb_darwin_godel_machines` on port `8302` (safety mode `full_verification`, primary DGM);  
- `jarvis-fifth-dgm` on port `4002` (fifth DGM orchestrator);  
- `qualia-orchestrator-69dgm-real` on port `9998` (a “69‑DGM cascade” orchestrator).

These are **actual services**, not metaphors. They act as governed optimization/evaluation engines.

Their job in this chapter is to:

- evaluate candidate findings and their reasoning traces;  
- enforce the outcome classes: **reject, revise, human review, limited approval, approve**;  
- ensure that autonomous research does not mutate system behavior or knowledge without passing through verification and governance.

They **do not** self‑authorize findings. They are part of the gate, not above it.

---

## 27.6 Named Service Paths in the Research Flow

Governed web research uses several named service paths:

- **Sandbox** – `ms-allis-internal-sandbox` on port `8042`.  
- **BBB / entangled gateway** – `jarvis-wv-entangled-gateway` and related BBB on `8010` (plus BBB internals on `8016`).  
- **Consciousness bridge** – via `0f40caf56e1e_nbb_mother_carrie_protocols` on `8107`, providing a bridge path into higher‑level coordination.  
- **Spatial sandbox** – `jarvis-spatial-sandbox` on `8056`, including hysteresis for spatial and temporal stability.  
- **Qualia orchestrator** – `qualia-orchestrator-69dgm-real` on `9998`, handling multi‑DGM cascades.  
- **Brain orchestrator** – `jarvis-brain-orchestrator` (hosted around `17260`), coordinating routes and modes.

Together, these services make sure that:

- research runs in the sandbox;  
- safety/BBB layers guard external ingress and promotion;  
- spatial and temporal context (via spatial sandbox and hysteresis) help stabilize behavior;  
- DGM and qualia orchestrator services evaluate and route candidate findings.

---

## 27.7 The Full Governed Research Path

Putting it all together, the as‑built research path is:

1. **Research ingress.**  
   Web results arrive as raw retrieval \(R\).

2. **Internal-state sandbox (8042).**  
   \(R\) becomes candidate state in the sandbox, where sources are compared and tentative conclusions are drafted.

3. **Candidate findings.**  
   The sandbox produces structured candidate findings \(F\) with provenance and uncertainty.

4. **Constitutional review + BBB.**  
   Candidate findings pass through constitutional guardrails and BBB/entangled gateway checks for admissibility.

5. **DGM evaluation.**  
   Three real DGM instances and related services evaluate the finding’s reasoning, stability, and safety, producing one of: reject, revise, human review, limited approval, approve.

6. **Promotion decision.**  
   Only if constitutional and DGM checks approve does a finding move toward governed knowledge \(K\) or approved guidance \(G\).

At no point is there a **direct retrieval‑to‑output** pipeline. Every step is explicit and guarded.

---

## 27.8 What This Chapter Does Not Claim

Within this gate, Chapter 27 does **not** claim:

- that retrieval equals acceptance;  
- that autonomous research can bypass the sandbox;  
- that any DGM can self‑authorize findings;  
- that there is a direct retrieval‑to‑output pipeline;  
- that research is unconstrained.

Instead, it claims:

- research ingress is always sandboxed first;  
- retrieved content is always **candidate state**, not immediate knowledge;  
- constitutional and DGM review always sit between candidate findings and promotion;  
- three real DGM containers participate as governed evaluators.

---

## 27.9 Step-by-Step View for Rural Developers

If you are running Ms. Allis on your own hardware in a rural setting, web research and autonomy work like this:

1. Ms. Allis goes out to the web to look for information.  
2. Everything it finds lands in the **internal sandbox**, not in memory or guidance.  
3. It drafts **candidate findings** and checks them against policy and safety rules.  
4. Three DGM services and the BBB/guardian stack help decide whether the candidate is safe, stable, and well‑grounded.  
5. Only then, and often with caveats, can a research result become something the system treats as real guidance or long‑term knowledge.

So the system can **hunt** and **think**, but it cannot quietly turn “I found it online” into “this is true and safe to follow” without passing through its full governed path.

---

## 27.10 Closing Statement

Chapter 27 fixes the shape of **governed web research autonomy** in Ms. Allis. Research ingress flows into the internal-state sandbox, becomes candidate findings, passes constitutional and DGM review, and only then may reach promotion outcomes like reject, revise, human review, limited approval, or approve.

Three real Darwin Gödel Machine containers and the named service paths around them ensure that autonomy remains research‑capable but **never output‑sovereign**. Retrieval stays distinct from knowledge and guidance, and the path from “found it” to “trust it” always passes through the same governed architecture.
