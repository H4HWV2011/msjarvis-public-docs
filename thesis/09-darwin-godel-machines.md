# Chapter 9. Darwin-Gödel Machines

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 9.0 How to Read This Chapter (Rural Developer Guide)

This chapter is for anyone building a system that needs to improve itself over
time without losing accountability. It explains the Darwin-Gödel Machine (DGM)
layer of Ms. Allis — the governed machinery that decides whether a candidate
change (to code or to a reasoning conclusion) is allowed to become permanent.

Five things a rural developer should take from this chapter:

1. **DGMs govern two kinds of promotion.** They govern code evolution (new code
   proving itself before touching production) and reasoning promotion (sandbox
   conclusions proving themselves before becoming memory, experience, or action).
   Both use the same bounded-transition logic.

2. **The scheduled execution surface for the DGM lifecycle is the four
   `runtime_governance` pg_cron procedures:** `gbim_runtime_lifecycle_hourly()`,
   `gbim_runtime_lifecycle_daily()`, `gbim_runtime_lifecycle_weekly()`, and
   `gbim_runtime_lifecycle_monthly()`. These run on a fixed schedule in the live
   system and are the operational heartbeat of the DGM lifecycle. They are not
   separate from the governance schema — they are registered inside it.

3. **Governance filtering runs through the Constitutional Principles Service**
   (Chapter 37). A DGM proposal that would violate a constitutional principle is
   rejected there before it can reach the promotion step. This is a
   non-overrideable gate.

4. **Promotion is a partial function.** Not every sandbox conclusion becomes
   validated state. The gate \(G(x)\) is a conjunction — every sub-gate must
   pass or the whole proposal is rejected. A score of five out of six sub-gates
   is still a rejection.

5. **Certainty cannot be inflated by passing a gate.** Promotion changes a
   state's authority level; it does not change the maximum confidence that the
   evidence supports. The non-inflation principle is a hard constraint, not a
   guideline.

---

## 9.1 Purpose

This chapter explains how Darwin-Gödel Machines function inside Ms. Allis as
the governed self-modification and self-evaluation layer responsible for
improvement under constraint. DGMs are not limited to code mutation or
deployment approval. In the current architecture, they govern both code
evolution and the promotion of reasoning outcomes from the internal-state
sandbox into validated, experience-bearing, memory-bearing, or otherwise
persistent state.

The chapter therefore treats DGMs as a bridge between adaptive intelligence and
constitutional restraint. They are the machinery through which change becomes
admissible. Their role is to test, compare, gate, and authorize transitions —
not merely to generate novelty or reward escalation.

---

## 9.2 Why DGMs Matter

Ms. Allis is a steward system rather than a static model. That means the system
must be capable of learning, adaptation, and self-improvement without allowing
uncontrolled propagation of error, hallucination, overconfidence, unsafe code,
or constitutionally prohibited state.

DGMs provide that discipline. The sandbox model is easiest to understand in
code terms: new code proves itself in isolation before it can touch production.
The architecture extends that same pattern to reasoning. A sandbox conclusion
must prove itself before it can become experience, durable memory, operational
belief, or externally consequential state.

This extension is not a theoretical aspiration. The live DGM lifecycle runs on
a scheduled basis through the `runtime_governance` schema procedures named in
§9.10 below. Every hourly, daily, weekly, and monthly execution of those
procedures is an execution of the DGM lifecycle over the governed corpus.

---

## 9.3 Scope of DGM Governance

DGMs govern more than code promotion. They govern at least two major classes of
promotion:

- **Code evolution** — candidate changes to services, routing, optimization
  logic, or supporting infrastructure are tested before deployment.
- **Reasoning promotion** — candidate conclusions formed inside the
  internal-state sandbox are evaluated before they may become validated state,
  remembered state, experiential trace, or action-bearing output.

This distinction is essential because the system contains a protected
internal-state sandbox for high-level reasoning. Once that sandbox exists, DGMs
cannot be described as if they supervise only software artifacts. They also
supervise epistemic transitions.

Governance filtering across both classes runs through two authorities:

1. **The Constitutional Principles Service (Chapter 37)**, which provides the
   non-overrideable constitutional gate that rejects any proposal — code or
   reasoning — that violates the system's governing principles.
2. **DGM validators**, which apply the evidence, coherence, privacy, security,
   and operational sub-gates described in §9.7.

Both authorities are consulted for every promotion attempt. The Constitutional
Principles Service gates first; DGM validators gate second.

---

## 9.4 DGMs and the Internal-State Sandbox

The internal-state sandbox creates a reversible domain for speculative
reasoning. Retrieved context, model-generated hypotheses, qualitative signals,
and multidomain constraints can interact there without immediate production
consequence.

DGMs sit at the edge of that sandbox. They evaluate whether a candidate state
emerging from the sandbox may cross from provisional deliberation into a higher
authority state. In this role, DGMs do not merely score usefulness. They assess
admissibility under evidence, coherence, constitutional boundaries, operational
safety, and downstream effect.

**DGMs govern promotion out of the sandbox just as they govern promotion of code
into production.**

The constitutional boundary check at the sandbox edge is performed by the
Constitutional Principles Service (Chapter 37), which is invoked as part of
\(G_{\mathrm{constitutional}}(x)\) in the combined gate described in §9.7. A
candidate that fails constitutional review does not proceed to the DGM
validators and does not appear in the scheduled lifecycle procedures.

---

## 9.5 Candidate Reasoning and DGM Gating

A sandbox conclusion is a candidate reasoning product, not accepted knowledge.

A reasoning cycle may produce summaries, inferred relations, proposed actions,
governance interpretations, identity-linked suggestions, or place-based
conclusions. These outputs remain provisional while inside the sandbox. Before
they can become experience or persistent state, they must face DGM-style gating.

That gating includes at minimum:

- evidentiary sufficiency;
- cross-domain coherence;
- constitutional admissibility (via the Constitutional Principles Service,
  Chapter 37);
- privacy and disclosure compatibility;
- service-level safety and rollback feasibility; and
- consistency with the system's optimization and evaluation regime.

A conclusion that is coherent but weakly grounded must not be promoted. A
conclusion that is strongly grounded but constitutionally disallowed must not be
promoted. A conclusion that passes one layer but introduces instability elsewhere
may be quarantined, revised, or escalated for review.

**For rural developers:** design your gating predicate as a strict conjunction.
If any sub-gate returns false, the whole promotion returns false. This is how
the Constitutional Principles Service and the DGM validators work together: the
constitutional gate is evaluated first, and only if it passes does the full
validator set run. There is no weighted averaging across gates.

---

## 9.6 From Sandbox to Experience

Sandbox conclusions become experience or persistent state only by surviving DGM
gating.

A candidate conclusion formed in the sandbox may contribute to later memory,
identity-continuity, internal experience traces, or service-level adaptation
only if it survives the combined gate. "Experience" in Ms. Allis is not merely
whatever occurred inside deliberation. Experience-bearing state is a promoted
subset of sandbox activity that has passed the required checks.

The promotion chain is:

\[
S_{\mathrm{raw}} \;\rightarrow\; S_{\mathrm{sandbox}} \;\rightarrow\;
S_{\mathrm{candidate}} \;\xrightarrow{G_{\mathrm{DGM}}}\;
S_{\mathrm{validated}} \;\rightarrow\; S_{\mathrm{experience}}
\;\rightarrow\; S_{\mathrm{memory}}
\]

This is not automatic progression. Each arrow is partial. Some candidate states
are rejected, some are quarantined, some are approved only for limited internal
use, and some are promoted further into durable memory or external consequence.

For states that reach \(S_{\mathrm{memory}}\), the promotion write to
`public.gbim_record` must satisfy the `gbim_record_spacetime_provenance_chk`
constraint: `spatial_unit_id`, `spatial_unit_kind`, and `valid_time_start` must
all be non-null. The database enforces this structurally. The next scheduled
refresh of `public_admissible_gbim_mv` will then determine whether the promoted
row enters the admissible evidence surface.

---

## 9.7 Gated-Promotion Algebra

Let \(S_{\mathrm{sandbox}}\), \(S_{\mathrm{validated}}\), \(S_{\mathrm{memory}}\),
and \(S_{\mathrm{action}}\) denote distinct state spaces. Promotion is partial:
it is defined only for states that satisfy the required gates.

\[
T_{\mathrm{promote}} : S_{\mathrm{sandbox}} \rightharpoonup S_{\mathrm{validated}}
\]

with

\[
T_{\mathrm{promote}}(x) =
\begin{cases}
P(x), & G(x) = 1 \\
\bot,  & G(x) = 0
\end{cases}
\]

where \(P(x)\) is the promoted form of \(x\), \(\bot\) denotes rejection,
nonpromotion, quarantine, or unresolved status, and \(G(x)\) is the combined
gate outcome decomposed as:

\[
G(x) = G_{\mathrm{constitutional}}(x)\; G_{\mathrm{evidence}}(x)\;
G_{\mathrm{coherence}}(x)\; G_{\mathrm{privacy}}(x)\;
G_{\mathrm{security}}(x)\; G_{\mathrm{operational}}(x)
\]

\(G_{\mathrm{constitutional}}(x)\) is evaluated by the Constitutional Principles
Service (Chapter 37) and is listed first because it is evaluated first. If it
returns 0, the remaining sub-gates are not evaluated and the promotion returns
\(\bot\) immediately.

DGM promotion is not arbitrary escalation. Promotion changes the authority of a
state only when governance and evidence justify the change — and only when every
sub-gate in the conjunction holds.

---

## 9.8 Non-Inflation of Certainty

DGM promotion must not inflate certainty beyond the evidence.

A sandbox hypothesis can become better governed, better documented, or better
situated after passing through DGM evaluation, but it must not become more
certain than the evidentiary record allows merely because it crossed a gate. If
\(C(x)\) is system confidence and \(E(x)\) is the maximum confidence warranted
by evidence, the safety condition is:

\[
C\bigl(T_{\mathrm{promote}}(x)\bigr) \leq E(x)
\]

This is the non-inflation principle. It prevents DGM promotion from turning
provisional reasoning into overclaimed fact. A passed gate licenses status
change, not unjustified certainty growth.

---

## 9.9 Code Evolution and Reasoning Evolution

The same DGM pattern applies across both software and cognition-like transitions.

For code evolution, the DGM pipeline evaluates candidate changes against tests,
safety checks, compatibility constraints, and deployment criteria. For reasoning
evolution, the DGM pipeline evaluates candidate conclusions against evidence,
coherence, constitutional rules enforced by the Constitutional Principles Service
(Chapter 37), and persistence criteria. The two are analogous but not identical:
one governs executable artifacts, the other governs epistemic artifacts.

The unifying principle is that no candidate becomes production consequence merely
because it exists. It must survive the same architecture of disciplined
transition.

---

## 9.10 Live Governed DGM Cycle

The current architecture includes a live governed DGM cycle that operates over
an allowlisted workspace.

**Scheduled execution surface.** The DGM lifecycle is executed on a fixed
schedule by four pg_cron procedures registered in the `runtime_governance`
schema:

```sql
-- Hourly: gbim_runtime_lifecycle_hourly()
-- Daily at 03:05: gbim_runtime_lifecycle_daily()
-- Weekly on Sunday at 02:00: gbim_runtime_lifecycle_weekly()
-- Monthly on the 1st at 01:30: gbim_runtime_lifecycle_monthly()
```

These four procedures — `runtime_governance.gbim_runtime_lifecycle_hourly()`,
`runtime_governance.gbim_runtime_lifecycle_daily()`,
`runtime_governance.gbim_runtime_lifecycle_weekly()`, and
`runtime_governance.gbim_runtime_lifecycle_monthly()` — are the operational
heartbeat of the DGM lifecycle. Each execution applies the governed cycle to the
corpus of records within the `runtime_governance` schema, advancing or
degrading `degradation_status` values, refreshing `public_admissible_gbim_mv`,
and writing lifecycle snapshots to `runtime_governance.public_answer_audit`. The
schedules are registered in `cron.job` in the `wv_gis` database and observable
in `cron.job_run_details`.

**Cycle behavior.** A governed DGM cycle performs proposal, evaluation, guarded
application, rejection, evidence recording, and rollback. Valid proposals are
applied only to allowlisted DGM workspace targets. Immutable production targets
are rejected outright. Proposals that fail safety, coherence, constitutional
review (via the Constitutional Principles Service, Chapter 37), or hash
consistency checks are rejected. Applied changes carry explicit rollback evidence
so previous content can be restored.

**For rural developers:** to verify the cycle is running, query
`cron.job_run_details` in `wv_gis` and confirm recent entries for each of the
four procedure names. A missing or stale entry means the scheduled runner is not
executing and the lifecycle gates are not being applied. This is an auditable
fact, not an assumption.

---

## 9.11 Application, Rejection, and Rollback

The live DGM cycle produces three primary verdicts:

- **APPLY** — a proposal passes evidence, safety, constitutional (Chapter 37),
  and coherence gates and is written to the allowlisted target along with an
  evidence record and rollback file.
- **REJECT** — a proposal is refused because the target is immutable, the safety
  score is too low, the constitutional gate fails, the precondition hash does not
  match, or other gate checks fail.
- **ROLLBACK** — a previously applied change is reversed, restoring the earlier
  content recorded in rollback evidence.

This triplet keeps the DGM cycle bounded. Code evolution and state evolution
occur only within controlled workspaces, unsafe or constitutionally prohibited
proposals are rejected, and rollback remains available and verified for applied
changes.

The constitutional filtering at the REJECT step is provided by the
Constitutional Principles Service (Chapter 37), which is the same service
invoked as \(G_{\mathrm{constitutional}}(x)\) in the algebraic gate of §9.7.
The service is not a post-hoc check; it is a pre-condition gate that runs before
any write is attempted.

---

## 9.12 Relationship to BBB, Guardians, and Temporal Bodies

The governed DGM cycle operates alongside the Blood-Brain Barrier (BBB),
constitutional guardians, temporal Hilbert bodies, and Phi-aware recurrent
runners.

During verification, these components remain live and participate in the
evaluation and gating of proposals. BBB and constitutional guardians (including
the Constitutional Principles Service, Chapter 37) enforce non-overrideable
safety and boundary conditions. Temporal and Phi-aware layers help ensure that
proposals are evaluated in light of time, continuity, and recurrent behavior
rather than as isolated instantaneous changes.

The four scheduled lifecycle procedures — hourly, daily, weekly, monthly — are
the integration point where these components converge in the live system. Each
scheduled execution is a timestamped, auditable event that can be cross-checked
against BBB behavior, constitutional gate outcomes, and temporal validity records
in the same database.

DGM activity is therefore not a free agent. It is embedded within a wider safety
and governance apparatus, and its execution record is visible in
`cron.job_run_details`.

---

## 9.13 DGM Self-Improvement Without Arbitrary Escalation

A major risk in self-improving systems is confusing change with progress.

The DGM architecture prevents that mistake by requiring that self-improvement
be mediated by governance, evidence, and validation. Code does not get promoted
because it is novel. A reasoning state does not become memory because it feels
coherent. A claim does not gain authority because it was repeated often. Each
must pass through bounded transition rules.

The Constitutional Principles Service (Chapter 37) is the component that ensures
self-improvement cannot proceed in a direction that is constitutionally
prohibited, regardless of how coherent or evidentially well-supported the
proposal appears by other metrics. It is the final non-overrideable authority in
the gate conjunction.

Promotion is earned through admissibility, not granted by enthusiasm, recurrence,
or internal pressure.

---

## 9.14 Relationship to Other Chapters

This chapter sits at an important intersection in the thesis.

It connects backward to the RAG routing and internal-state sandbox chapters
(Chapters 7 and the sandbox sections) because those chapters define where
candidate reasoning comes from. It connects sideways to the BBB and
Constitutional Principles Service chapters (including Chapter 37) because those
define non-overrideable gating conditions. It connects forward to fractal
optimization, evaluation, audit, and test-harness chapters because those define
how DGM behavior is measured and improved over time.

It also connects to memory and Hilbert-state chapters because promotion changes
not only where a state lives but what authority it carries. The scheduled
lifecycle procedures named in §9.10 are the live bridge between the Hilbert-state
mathematics and the operational `runtime_governance` schema: they execute the
governed transition logic that the formal chapters describe.

---

## 9.15 Closing Statement

Darwin-Gödel Machines in Ms. Allis are the governed transition machinery of
adaptation. They supervise both code evolution and reasoning promotion, including
the passage from internal-state sandbox conclusions into validated, experiential,
persistent, or actionable state.

The scheduled execution surface for the DGM lifecycle is the four
`runtime_governance` procedures:
`gbim_runtime_lifecycle_hourly()`,
`gbim_runtime_lifecycle_daily()`,
`gbim_runtime_lifecycle_weekly()`, and
`gbim_runtime_lifecycle_monthly()`.
These procedures run on a fixed pg_cron schedule in the live system and are
observable in `cron.job_run_details` in the `wv_gis` database. They are the
operational heartbeat through which the DGM governed cycle executes, the
Constitutional Principles Service (Chapter 37) enforces constitutional filtering,
and the `degradation_status` lifecycle gate advances or closes admissibility for
records in `public_admissible_gbim_mv`.

Their defining property is not mutation alone but disciplined admissibility.
DGMs make change answerable to evidence, coherence, constitutional limits,
privacy, safety, and evaluation. That is what allows Ms. Allis to improve
without treating self-modification or self-belief as inherently trustworthy.

---

*Chapter 9 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
