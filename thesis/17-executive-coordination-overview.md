# 17. Executive Coordination Overview

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 17.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis coordinates work across her subsystems so that reasoning, safety, and commitment happen in a controlled order rather than all at once. It shows how the “executive plane” treats the internal sandbox, BBB, consciousness bridge, pituitary, and brain orchestrator as named parts of one governed path.

It supports:

- **P1 – Every where is entangled** by routing each task through memory, sandbox, and safeguards instead of letting any one component act alone.  
- **P3 – Power has a geometry** by making dispatch, sandbox deliberation, BBB review, bridge promotion, and authority tracking explicit steps.  
- **P5 – Design is a geographic act** by treating coordination order as a design choice that shapes how Appalachian contexts are handled.  
- **P12 – Intelligence with a ZIP code** by ensuring that local, place‑aware evidence is part of the coordinated path before the system commits to anything.  
- **P16 – Power accountable to place** by requiring that authority increases only happen through named gates, not silent internal escalation.

This chapter belongs to the **Computational Instrument** tier. It documents the executive plane as actually built, with concrete ports and services, rather than as an abstract control idea.

---

## 17.2 The Executive Plane and Its Services

The executive plane is the set of services that coordinate which parts of Ms. Allis handle a task and in what order.

Key named services and paths include:

- **Brain orchestrator** at host port 17260 → 7260/tcp inside the fabric.  
- **Internal sandbox** at host port 8042, version 1.2.0, explicitly marked `bbb_enforced`.  
- **Consciousness bridge** reachable at port 8010, with an internal URL such as `http://jarvis-consciousness-bridge:8018`.  
- **BBB‑class layer** reachable on host port 8010 once the WV‑entangled gateway and neurobiological BBB paths are live.  
- **Pituitary and global modes** reported healthy, with dual‑awareness and integration layers active.  
- **Agents service** at an internal port for multi‑agent coordination.

Together, these services form the executive plane: they manage dispatch into the sandbox, coordinate BBB and bridge sequencing, and track which results have authority to affect the rest of the system.

---

## 17.3 Sandbox as First‑Class Control Stage

The internal sandbox (`ms_allis_internal_sandbox`) is a first‑class control stage, not an afterthought.

It is:

- a dedicated container with its own health endpoint on 8042;  
- explicitly configured with `bbb_enforced: true`;  
- connected to EEG, pituitary, I‑containers, qualia orchestrator, and the consciousness bridge;  
- monitored by a `/status` overlay that reports `ch14_bridge_overlay: active`.

When the executive plane dispatches a task into the sandbox, it is asking for **reversible deliberation**, not immediate action. The sandbox can think, compare, and synthesize, but anything it produces returns as a *candidate* result. The executive plane must still decide what happens next.

---

## 17.4 Executive Dispatch: Step by Step

For rural developers, executive dispatch can be understood as a simple sequence:

1. **Receive a request.**  
   A task comes in through the gateway and is handed to the brain orchestrator.

2. **Decide how to handle it.**  
   The orchestrator decides whether this is a simple task (direct service), a reasoning task (sandbox), or a case needing extra review.

3. **Dispatch into the sandbox when needed.**  
   For reasoning tasks, the orchestrator sends the request and gathered context to the sandbox at 8042.

4. **Let the sandbox deliberate.**  
   The sandbox uses EEG bands, pituitary modes, qualia, I‑containers, and retrieval to form candidate conclusions. These remain internal and reversible.

5. **Classify sandbox returns.**  
   The executive plane treats each sandbox return as either **validated** (ready to enter the promotion path) or **non‑validated** (still provisional).

6. **Route toward promotion or back for revision.**  
   Validated candidates move into BBB and bridge sequencing; non‑validated ones are kept in the sandbox, revised, or escalated for human review.

This pattern keeps the sandbox firmly inside the control path without granting it the right to act on its own.

---

## 17.5 Validated vs Non‑Validated Sandbox Returns

The executive plane must distinguish between different kinds of sandbox output:

- **Validated returns.**  
  These have passed whatever internal checks the sandbox and its judges apply. They are eligible to enter BBB review and bridge promotion, but they are still not yet committed actions.

- **Non‑validated returns.**  
  These remain provisional, conflicted, or incomplete. They may be useful for internal thinking but are not allowed into BBB or bridge paths for committed use.

Routing logic in the executive services makes this classification a live behavior, not just a diagram. The brain orchestrator and related services decide which path each return takes based on flags and status fields.

---

## 17.6 BBB Review and Promotion Sequencing

After a sandbox result is deemed validated, the executive plane routes it through **BBB review** before any promotion.

In practice:

- BBB‑class services at port 8010 check safety, ethics, truth, alignment, and manipulation rules.  
- If BBB review fails, the candidate is rejected or sent back for revision.  
- Only BBB‑approved results move toward the consciousness bridge for integration.

The chapter cannot claim sandbox bypass of BBB. Every route from sandbox to committed action must pass BBB review, or else be held in internal state without promotion.

---

## 17.7 Consciousness Bridge and Promotion

The consciousness bridge is the named path through which BBB‑cleared candidates become part of active, integrated behavior.

Executive coordination over the bridge includes:

- choosing which validated candidates are actually sent to the bridge;  
- ensuring bridge health is checked and logged;  
- recording which bridge promotions happened, when, and under what pituitary mode.

Promotion through the bridge is where a candidate state stops being “a thought” and becomes part of live integrated behavior. The executive plane manages this step carefully; promotion is never automatic.

---

## 17.8 Reject, Revise, Escalate, Approve

Promotion is not a yes/no switch in one place. Executive coordination represents different paths as service behaviors:

- **Reject.**  
  Mark a candidate as not suitable for promotion; keep it internal for reference only.

- **Revise.**  
  Send the candidate back to the sandbox with instructions to gather more evidence, change assumptions, or refine reasoning.

- **Escalate.**  
  Route difficult or high‑consequence cases to human stewards or to specialized review services. This is never a replacement for oversight.

- **Approve.**  
  Allow a BBB‑cleared candidate to cross the bridge and become part of active system behavior or memory.

These paths exist as live behaviors in the executive service layer. They make it clear that not every sandbox result moves forward, and that different outcomes are handled differently.

---

## 17.9 Promotion‑Aware Authority Tracking

Executive services keep track of **authority levels** for each result:

- sandbox‑provisional;  
- internally validated;  
- BBB‑cleared;  
- bridge‑promoted;  
- committed and eligible for downstream memory or external use.

This promotion‑aware tracking ensures that:

- internal speculation does not silently become committed policy;  
- a sandbox result can be used for internal thinking without ever leaving the sandbox;  
- BBB and bridge steps are visible in logs and status, not hidden.

For rural developers, this means they can inspect not just what the system answered, but how far through the promotion chain each answer traveled.

---

## 17.10 Boundaries and Limits

Within this gate, Chapter 17 must not claim:

- autonomous self‑authorization by the system;  
- sandbox paths that bypass BBB;  
- committed actions without promotion review;  
- escalations that happen without any review;  
- replacement of human oversight on high‑consequence decisions.

Instead, the executive plane is described as a **coordinator of governed paths**. It controls how tasks move into sandbox reasoning, how results are classified, how BBB and bridge are sequenced, and how authority levels change, always under the assumption that human stewards remain in the loop for serious decisions.

---

## 17.11 Closing Statement

Executive coordination in Ms. Allis is an as‑built control plane over sandbox, BBB, bridge, pituitary, and orchestration services. It dispatches tasks into the sandbox as needed, classifies returns as validated or non‑validated, and then sequences BBB review and bridge promotion so that reversible deliberation always comes before committed action.

By treating the sandbox as first‑class, requiring BBB review, naming the bridge path, and tracking promotion‑aware authority, this chapter shows how Ms. Allis keeps its internal thinking accountable to place, evidence, and constitutional guardrails instead of letting raw model output decide what happens next.
