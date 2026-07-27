# Chapter 10. WOAH — Weighted Optimization Hierarchy

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 10.0 How to Read This Chapter (Rural Developer Guide)

This chapter is for anyone building a system that needs to rank options and
choose among them without losing accountability. It explains the WOAH weighted
optimization hierarchy in Ms. Allis — the governed pattern that assigns
priorities and weights when judging candidate states, routes, or actions under
explicit guardrails.

Five things a rural developer should carry forward:

1. **WOAH is weighted evaluation, not global optimization.** It assigns scores
   and ranks options locally under guardrails. It does not claim to compute a
   universal utility function or find mathematically optimal solutions.

2. **"Stable" in this system means cryptographically committed.** When this
   chapter says that a state is stable or that an option is accepted, it means
   the state has survived gating and been recorded as a cryptographically
   committed state via a signed verdict. It does not mean thermodynamic
   stability, Lyapunov stability, or any physical low-energy equilibrium.
   Those are different claims that this architecture does not make.

3. **Optimization is subordinate to constitutional and BBB guardrails.** A
   candidate that scores well on optimization criteria is still rejected if it
   fails the Constitutional Principles Service or BBB filters. There is no
   override path around those gates.

4. **WOAH contributes to the DGM cycle.** Proposals that score poorly on truth,
   ethics, or safety are rejected before they can reach the promotion step. WOAH
   is one layer of the governed evaluation pipeline, not a separate process.

5. **The system keeps optimization answerable to place and community.** In rural
   contexts, "better" is defined in terms of local commitments, constitutional
   boundaries, and guardrails — not computational performance alone.

---

## 10.1 Purpose

This chapter explains the WOAH weighted optimization hierarchy in Ms. Allis as
an **as-built, bounded evaluation pattern**, not as a claim of global
mathematical optimality or autonomous moral agency. WOAH describes how the
system assigns priorities and weights when judging candidate states, routes, or
actions under guardrails such as truth, alignment, ethics, coherence, safety,
and constitutional limits.

For rural developers, the goal is practical: show how Ms. Allis uses real
services, judges, and recurrent runners to rank and filter options, and how
those evaluations stay inside bounded governance rather than becoming
unconstrained optimization behavior.

---

## 10.2 Gate Scope and Limits

The live gate for Chapter 10 allows the thesis to claim:

- A working **weighted/priority evaluation pattern** ("WOAH") grounded in
  actual source and runtime evidence.
- Optimization tied to guardrails: truth, alignment, ethics, coherence, BBB,
  constitutional guardian, Phi, and recurrent assessment.
- Partial implementation where appropriate, explicitly labeled as architectural
  vocabulary versus runtime gate behavior.

The gate forbids Chapter 10 from claiming:

- Global optimization or universal utility maximization.
- Autonomous moral agency or a system that "decides what is right" on its own.
- Perfect safety, universal truth, or guaranteed correct decisions.
- Thermodynamic, Lyapunov, or any physical-stability property for system
  states. What the system calls a "stable" or "accepted" state is a
  **cryptographically committed state** — one that has passed governance gates
  and been recorded with a signed verdict. That is not low free energy; it is
  a governed, verifiable, non-repudiable record.

Under this scope, WOAH is documented as a real weighted evaluation hierarchy
that helps the steward system choose among options safely, but it is never
described as infallible or globally optimal.

---

## 10.3 WOAH in the Running Stack

WOAH is implemented as a pattern of services and judges rather than a single
monolithic optimizer.

Runtime evidence shows:

- A **jarvis-woah** service and an **nbb_woah_algorithms** container operating
  alongside the steward, stewardship scheduler, fifth DGM, and qualia
  orchestrator.
- A **judge pipeline** with dedicated ports for:
  - truth
  - alignment
  - ethics
  - consistency

These components form a hierarchy of evaluation where candidate states and
proposals are weighed against multiple criteria before they can move toward
consequence. WOAH labels describe how these weights and priorities are applied,
while the judges and guardian services enforce actual decisions about
acceptance, rejection, or review.

When a proposal clears all evaluation gates and is accepted, it becomes a
**cryptographically committed state** — recorded with a signed verdict rather
than held as an unverified candidate. That commitment is the operational
meaning of acceptance in this system.

---

## 10.4 Biology and Geography Vocabulary as Translation

WOAH has its roots in biology- and geography-inspired language, but in this
chapter those metaphors are treated as **translation tools** rather than
literal claims.

Biological phrases such as "fitness," "adaptation," or "survival" are used to
help rural developers reason about which options the system tends to preserve,
but the implementation is still just software: weights, scores, thresholds, and
gates. Geographic metaphors (terrain, routes, gradients) provide intuition for
how the system moves through configuration space or policy space.

The chapter therefore uses biology and geography vocabulary where it clarifies
the architecture, but it always ties back to concrete services, judges, and
guardrails rather than implying physical or metaphysical processes beyond the
code. In particular, the notion of moving from a "high-energy candidate state"
to an "accepted state" is used only as an analogy for governance promotion — it
makes no claim about energy, entropy, or physical phase transitions. An
accepted, cryptographically committed state is a verified record, not a
thermodynamic minimum.

---

## 10.5 Guardrails: Truth, Alignment, Ethics, Coherence

The WOAH hierarchy is anchored by explicit guardrails.

At minimum, candidate states are evaluated against:

- **Truth**: Does the claim match available evidence and retrieval results?
- **Alignment**: Does the claim or action remain aligned with the system's
  steward purpose and configured goals?
- **Ethics**: Does it respect boundaries on harm, dignity, fairness, and local
  commitments?
- **Consistency**: Does it cohere with existing state, previous decisions, and
  internal records?

Dedicated judge services operate on these dimensions, and the WOAH pattern ties
their outputs into a weighted evaluation: some failures (for example, clear
ethical violations) may be hard blockers, while softer inconsistencies may
route a candidate to review rather than immediate rejection.

For a rural developer, this means any optimization logic should consider these
guardrails as first-class criteria, not as optional post-filters. A candidate
that fails any hard-blocker gate does not become a cryptographically committed
state regardless of how well it scores on other dimensions.

---

## 10.6 Constitutional Guardian and BBB

Optimization in Ms. Allis never runs outside constitutional and BBB oversight.

A constitutional guardian service maintains an audit log and reports healthy
status when connected. BBB (blood-brain barrier) filters sit in front of
sensitive routes, enforcing safety and constitutional constraints. Together,
these components ensure that weighted evaluation cannot quietly override core
rules of the system.

WOAH's role is subordinate to these guardians: even if a candidate scores
highly on some optimization metric, it still cannot cross BBB or constitutional
gates if it violates constraints on privacy, surveillance, role boundaries, or
prohibited content. Only proposals that clear both the constitutional guardian
and the BBB surface as candidates for cryptographic commitment.

This keeps weighted evaluation compatible with the steward's commitments to
safety and governance rather than allowing optimization to become a bypass
around policy.

---

## 10.7 Hilbert State, Hilbert Time, and Phi

The WOAH hierarchy operates in the presence of Hilbert-state and Hilbert-time
services, as well as a Phi probe.

Hilbert-state provides a structured view of current system state, while
Hilbert-time provides temporal tiers (ephemeral, staged, historical) with
half-life parameters and hysteresis. Phi probes track aspects of the system's
integrated behavior. Together, these components allow weighted evaluation to
consider not just instantaneous scores, but history, recency, and continuity.

For example:

- A proposal may be weighed differently if it affects historical records versus
  ephemeral caches.
- A repeated pattern of failures over time may lower the effective weight of
  similar future proposals.

WOAH, in this context, is not a standalone optimizer but a pattern for how
weights and priorities can be made time-aware and state-aware within the
system's Hilbert framing. When a proposal is ultimately accepted across all
gates, it is recorded as a cryptographically committed state with a signed
verdict — that record is what persists across Hilbert-time tiers, not a
thermodynamic energy level.

---

## 10.8 Recurrent Epistemic Runner and Scheduling

Optimization is connected to recurrent assessment, not only on demand.

The live runtime scheduler confirms that the following four
`runtime_governance` pg_cron procedures form the scheduled execution surface
for the DGM lifecycle in the production `wv_gis` database:

- `runtime_governance.gbim_runtime_lifecycle_hourly()` — runs at 15 minutes
  past every hour (schedule: `15 * * * *`)
- `runtime_governance.gbim_runtime_lifecycle_daily()` — runs at 03:05 daily
  (schedule: `5 3 * * *`)
- `runtime_governance.gbim_runtime_lifecycle_weekly()` — runs Sunday at 02:00
  (schedule: `0 2 * * 0`)
- `runtime_governance.gbim_runtime_lifecycle_monthly()` — runs at 01:30 on the
  last day of each month (schedule: `30 1 $ * *`)

These four procedures are the operational heartbeat through which WOAH
criteria, DGM evaluation, lifecycle decay, and admissibility refresh are
applied to the live governed corpus on a fixed schedule.

Runtime evidence also shows that a **recurrent epistemic runner** is launched
at boot and runs continuously, replacing earlier direct calls to `dgm_cycle.sh`
(now paused). This runner coordinates periodic evaluations, identity promotion,
privacy impact assessments, and DGM cycles, all under the same governance
envelope as the `runtime_governance` pg_cron surface.

WOAH interacts with this scheduler in two ways:

- It provides weighted criteria for which tasks and proposals should be
  evaluated or promoted next.
- It helps ensure that repeated evaluations do not drift into unsafe behavior
  by keeping guardrails in place across every scheduled cycle.

For rural developers, this means optimization is part of a scheduled
stewardship loop rather than a set of ad-hoc scripts, and any changes to
weights or priorities must be considered in light of their long-running effects
on the governed corpus.

---

## 10.9 WOAH in Source Files and Services

The WOAH pattern is visible in multiple source files and services.

Examples include:

- Supervisors and orchestrators that mention **woah** in their names or roles.
- Integration scripts that connect DGM behavior, fifth DGM, and multi-LLM
  servers to a common evaluation logic.
- Audit and port registry files that document how services are wired into the
  broader optimization and stewardship stack.

These files provide anchors for describing WOAH as implemented behavior: where
the system routes requests through WOAH supervisors, how it uses weighted
criteria to choose among services, and how it keeps an audit trail of those
decisions.

The chapter does not claim that every WOAH reference is a fully realized
optimizer. Instead, it distinguishes between:

- **Implemented anchors**, where weighted evaluation and guardrails are active
  at runtime.
- **Architectural vocabulary**, where WOAH language marks intended patterns or
  future extensions that are not yet fully deployed.

---

## 10.10 Weighted Evaluation, Not Global Optimization

WOAH is explicitly framed as **weighted evaluation**, not global optimization.

The system may assign scores or priorities to options based on truth,
alignment, ethics, coherence, and other criteria, but it does not try to
compute a single global utility function that covers all possible states,
times, and people. Nor does it claim to find mathematically optimal solutions
to complex social or geographic problems.

Instead, WOAH is used to:

- Rank candidate states or actions within a local context.
- Decide which proposals deserve further evaluation or promotion toward
  cryptographic commitment.
- Filter out options that fail key guardrails.

The outcome of a successful evaluation is a **cryptographically committed
state** — a signed verdict that records the proposal, its evidence, and its
governance result. This is operational finality through governance, not
thermodynamic stability or mathematical convergence. This local, bounded
behavior is appropriate for a steward system operating in rural contexts, where
global optimality is neither attainable nor desirable.

---

## 10.11 WOAH and the DGM Cycle

WOAH interacts directly with the Darwin-Gödel cycle described in Chapter 9.

The DGM cycle proposes bounded changes, evaluates them, applies allowed
proposals, rejects unsafe ones, and records rollback evidence. WOAH contributes
to this cycle by providing weighted evaluation criteria and priority patterns:

- Proposals that score poorly on truth, ethics, or safety are rejected.
- Proposals targeting immutable production artifacts are rejected outright.
- Proposals affecting allowlisted workspace files can be applied, but only
  under DGM and guardrail supervision.

When a proposal clears the full DGM cycle and WOAH evaluation together, it
transitions from candidate to **cryptographically committed state** via a
signed verdict. That transition is what closes the proposal's lifecycle — not
a convergence to a thermodynamic equilibrium or a Lyapunov-stable region.

The scheduled execution surface for this lifecycle is the four
`runtime_governance` pg_cron procedures named in §10.8. Each scheduled firing
represents one cycle of WOAH-weighted, DGM-governed evaluation over the live
corpus.

For rural developers, this means that optimization is one layer of the DGM
pipeline, not a separate process. Any change that looks like "optimization"
still passes through the same governed cycle of proposal, evaluation, guarded
application, rejection, and rollback.

---

## 10.12 WOAH for Rural Stewardship

In rural deployment, WOAH is used to keep optimization answerable to place and
community.

Examples include:

- Prioritizing tasks that improve local safety or reliability over tasks that
  only increase throughput.
- Weighing ethical and alignment criteria more heavily when decisions affect
  people or landowners directly.
- Using Hilbert-time tiers to avoid over-reacting to short-lived anomalies in
  rural network or service conditions.

WOAH helps Ms. Allis act as a steward system by making sure that "better" is
defined in terms of local commitments, constitutional boundaries, and
guardrails, not just computational performance. A proposal that earns a
cryptographically committed state in this system has not merely scored well —
it has cleared the full constitutional, BBB, truth, alignment, ethics, and
coherence evaluation surface that makes it trustworthy for local civic use.

---

## 10.13 Architectural Vocabulary vs Runtime Gates

The chapter explicitly distinguishes **architectural vocabulary** from
**runtime gates**.

Architectural vocabulary includes:

- WOAH language used in design documents or code comments.
- Conceptual frameworks for how optimization *should* work in future
  extensions.

Runtime gates include:

- Actual judge services and guardian endpoints.
- BBB filters and constitutional auditors.
- DGM cycles with evidence and rollback files.
- Hilbert-state and Hilbert-time services with verified health checks.
- The four `runtime_governance` pg_cron lifecycle procedures executing on
  fixed schedules (§10.8).

Where evidence shows that WOAH is fully wired into these runtime gates, the
chapter may describe it as implemented behavior. Where evidence shows only
references or partial integration, the chapter must describe WOAH as
architectural intent and mark the limits clearly.

---

## 10.14 What This Chapter Claims

Under the verified gate, this chapter claims:

- Ms. Allis contains a working, bounded WOAH weighted evaluation hierarchy.
- WOAH is grounded in real services, judges, guardians, and recurrent runners.
- Optimization is tied to truth, alignment, ethics, coherence, BBB,
  constitutional guardians, Phi, and scheduled assessment.
- WOAH contributes to the DGM cycle and stewardship behavior, especially in
  rural contexts.
- The scheduled execution surface for the DGM lifecycle consists of
  `runtime_governance.gbim_runtime_lifecycle_hourly()`,
  `runtime_governance.gbim_runtime_lifecycle_daily()`,
  `runtime_governance.gbim_runtime_lifecycle_weekly()`, and
  `runtime_governance.gbim_runtime_lifecycle_monthly()`, all confirmed active
  in the live `wv_gis` database.
- Accepted proposals become **cryptographically committed states** recorded
  with signed verdicts. The word "stable" in this chapter refers exclusively
  to that cryptographic commitment, not to thermodynamic, energetic, or
  Lyapunov stability.

It does **not** claim:

- Global optimization over all states and times.
- Autonomous moral agency.
- Perfect safety, universal truth, or guaranteed correct decisions.
- Mathematical optimality beyond the scope of tested optimizers.
- Thermodynamic, Lyapunov, or physical-stability properties for any system
  state.

---

## 10.15 Closing Statement

WOAH in Ms. Allis is the weighted optimization hierarchy that helps the system
decide which options to consider, promote, or reject under strict guardrails.
It is built from real services and judges, operates alongside DGM cycles and
Hilbert bodies, and remains accountable to BBB, constitutional guardians, Phi,
and the four `runtime_governance` lifecycle procedures that execute on a fixed
schedule as the DGM operational heartbeat.

Accepted proposals in this system become cryptographically committed states via
signed verdicts. That is the operational meaning of acceptance: a governed,
verifiable, non-repudiable record. It is not thermodynamic stability or a
Lyapunov-stable equilibrium, and the chapter makes no such physical claim.

By documenting WOAH as a bounded, as-built evaluation pattern rather than a
universal optimizer, this chapter keeps optimization answerable to evidence,
ethics, alignment, coherence, and local stewardship. That is the level of
rigor and constraint appropriate for a rural steward system designed to serve
people, not merely numbers.

---

*Chapter 10 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
