# 32. Fractal Optimization and DGMs

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 32.1 Fractal Optimization in Ms. Allis

Fractal optimization in Ms. Allis means **repeating the same “propose → test → evaluate → gate” pattern** at several levels of the system, without ever letting an optimizer promote its own changes directly into production. The pattern looks similar at each scale, but the authority and safety boundaries stay fixed.

This chapter treats optimization as **governed improvement**, not free‑running self‑modification. DGMs can suggest better ways of doing things, try them in safe sandboxes, and compare results; but any change that might touch production must still go through outside safety channels.

---

## 32.2 23/69 DGM Sandboxes as Bounded Experiment Environments

The architecture includes **23/69 DGM sandboxes** as **bounded experiment environments**.

Key points:

- Each DGM sandbox is **separate from the main reasoning sandbox** (the one on port 8042).  
- Inside a DGM sandbox, the system can test:  
  - new thresholds;  
  - judge combinations;  
  - small code or policy tweaks;  
  - alternative evaluation strategies.  
- These experiments are **local**: they do not change live system behavior on their own.

You can think of each DGM sandbox as a **workbench** where the system tries adjustments safely before anything is considered for wider use.

---

## 32.3 Three-Stage DGM Process

Optimization via DGMs follows a **three-stage gated process**:

1. **Local DGM sandbox.**  
   - The DGM proposes candidate changes (for example, “tighten this threshold” or “try a different judge ordering”).  
   - It tests them in its own sandbox, scoring how well they work **locally**.

2. **Comparative selection.**  
   - The DGM compares candidates against the current baseline and against each other.  
   - It picks a “winner” or a small set of promising variants.  
   - At this point, the change is only an **adoption candidate**, not a production rule.

3. **External safety channels.**  
   - Adoption candidates are sent out of the DGM sandbox and into external safety channels (truth checks, guardians, policy review, etc.).  
   - Only if these **external checks** approve can the change move toward affecting production behavior.

This keeps optimization and authorization separate: **DGMs can propose and internally select**, but only **external safety channels** can approve for production.

---

## 32.4 Named Services in the Optimization Fabric

Several services participate in how fractal optimization plugs into the rest of the system:

- **Qualia orchestrator (9998).**  
  A “69‑DGM cascade” orchestrator that coordinates multiple DGMs, reachable at port 9998.

- **Brain orchestrator (17260).**  
  `jarvis-brain-orchestrator` routes work and coordinates which DGMs, sandboxes, and evaluation paths are used.

- **Reasoning sandbox (8042).**  
  `ms-allis-internal-sandbox` is the main reasoning sandbox, with `bbb_enforced=true`, separate from DGM sandboxes.

- **BBB / entangled gateway (8010).**  
  Blood–brain barrier and entangled gateway provide external safety checks and policy filters.

- **Pituitary.**  
  Mode and modulation controller, influencing global “how hard to push” or “how cautious to be.”

- **Consciousness bridge.**  
  A bridge service that lets vetted candidate changes and behaviors connect into higher‑level coordination.

These services together ensure that DGM experiments stay **sandboxed**, and that any proposed change must cross known, inspectable boundaries.

---

## 32.5 DGM Sandbox vs Production Reasoning Sandbox

This chapter draws a hard line between:

- **DGM sandbox.**  
  Used for *optimization experiments*; lives alongside BBB and qualia orchestrator; does not handle user‑facing reasoning.

- **Production reasoning sandbox (8042).**  
  Used for normal `/reason` flows; handles candidate answers for users; is itself governed and monitored.

Fractal optimization treats the **DGM sandbox** as a place to adjust evaluation machinery and policies, while the **reasoning sandbox** remains the place where user‑facing candidate states are formed and judged. A DGM never uses its sandbox to “sneak” changes straight into the reasoning sandbox.

---

## 32.6 Boundedness of Candidate Change Search

All DGM optimization is **bounded** in at least two ways:

- **Search space bounds.**  
  - What can be changed (for example, only certain thresholds, judge combinations, or small code areas).  
  - How far a parameter can move per step (no wild jumps).

- **Authority bounds.**  
  - DGMs cannot add new unchecked powers to themselves.  
  - They cannot widen their own domain of influence without going through external review.

This prevents a slow drift where small “good” changes gradually turn into a major shift in behavior that nobody reviewed.

---

## 32.7 Non-Expansive Promotion

Optimization is required to be **non‑expansive** with respect to authority:

- A DGM can make evaluation smarter or more calibrated.  
- It **cannot** silently expand what is allowed to be promoted or approved.

Examples of what non‑expansive promotion forbids:

- Removing a guardian or truth check just to speed things up.  
- Lowering approval thresholds so more things get approved without review.  
- Reordering checks to skip safety paths.

Any change that would expand promotion authority must be **explicitly validated via external safety channels**, not inferred from a local optimization score.

---

## 32.8 Stability and Anti-Oscillation

Optimization is only useful if it leads to **stable behavior**, not to flapping between settings.

Stability requirements include:

- **No rapid oscillation** around promotion thresholds (for example, approve‑reject‑approve‑reject on nearly identical cases).  
- Limits on how fast key parameters can move, even if DGM experiments suggest they could be pushed harder.  
- Sufficient observation windows to tell real improvements from noise.

In practice, this means a DGM must:

- demonstrate that a proposed change **stays helpful** across many trials;  
- avoid “chasing” short‑term metrics at the cost of long‑term coherence.

---

## 32.9 Fractal Optimization Across Nested Sandboxes

The term **fractal** comes from how the same pattern repeats across nested levels:

- Inside DGM sandboxes (23/69), the system proposes and tests **optimizer‑level changes**.  
- Inside the reasoning sandbox, it proposes and tests **answer‑level changes**.  
- Above both, external safety channels (BBB, guardian, truth checks, pituitary modes) perform **governance‑level checks**.

At every level, the loop is:

1. Propose a candidate.  
2. Test in a bounded sandbox.  
3. Compare and select internally.  
4. Send promising candidates outward.  
5. Let external safety decide what, if anything, can be adopted.

Fractal coherence means that **improvements at one level do not break safety at another**. A smarter DGM must still respect external guards; a smarter reasoning sandbox must still respect promotion rules.

---

## 32.10 What Chapter 32 Does Not Claim

Within this gate, Chapter 32 **does not** claim:

- that a DGM can self‑authorize changes into production;  
- that any sandbox can bypass external safety channels;  
- that optimization can remove guardian or truth checks;  
- that DGMs can perform unconstrained recursive self‑modification;  
- that thresholds can widen autonomously without external validation.

Instead, it claims:

- 23/69 DGM sandboxes exist as bounded experiment environments;  
- a **three-stage process** is in place (local sandbox → comparative selection → external safety channels);  
- promotion remains **non‑expansive and bounded**;  
- stability and fractal coherence are enforced via external safety paths.

---

## 32.11 Step-by-Step View for Rural Developers

If you are operating this system yourself, fractal optimization via DGMs behaves roughly like this:

1. A DGM tries a small change in **its own sandbox** and scores the result.  
2. It compares multiple candidates and picks a “winner.”  
3. That winner is sent to **outside safety mechanisms** (BBB, guardian, etc.).  
4. If external checks approve, the change may be rolled into configuration or code used by the main reasoning sandbox.  
5. If external checks reject or ask for revision, the DGM must try again within its bounds.

No matter how clever a DGM gets, **it cannot skip step 3–4**.

---

## 32.12 Closing Statement

Fractal optimization in Ms. Allis uses 23/69 DGMs and nested sandboxes to refine thresholds, judges, and evaluation behavior without letting optimization turn into self‑authorization. A three‑stage process—DGM sandbox, comparative selection, external safety channels—ensures that every proposed improvement remains bounded, non‑expansive, and stable before it can touch production behavior.

This keeps the system adaptive and tunable while preserving the same core rule throughout: **optimization suggests, governance decides.**
