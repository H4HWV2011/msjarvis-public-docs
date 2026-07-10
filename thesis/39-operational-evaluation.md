# 39. Operational Evaluation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 10, 2026*

---

## 39.1 Purpose of Operational Evaluation

Operational evaluation in Ms. Allis measures not only whether individual services answer requests, but whether the full governed pathway from sandboxed reasoning to gated promotion behaves reliably under real conditions.

The object of evaluation is therefore the entire controlled sequence: internal or external input, sandbox interpretation, intermediate validation, promotion attempt, bridge behavior, gated experience creation, and fail-closed handling where approval is not obtained. This chapter treats successful operation as a property of the whole path rather than of any single endpoint in isolation.

For that reason, health metrics alone are insufficient. A healthy service can still participate in an unsafe or unstable pipeline if promotion control, bridge handling, or fail-closed behavior is weak.

---

## 39.2 The Full Sandbox Pathway

The operational pathway under evaluation begins in the sandbox.

A candidate reasoning cycle enters a bounded workspace in which provisional state may be explored without immediate authority escalation. From there, the system may produce a sandbox result, attempt a promotion, encounter one or more gates, and, if approved, create a higher-authority experience through the relevant bridge. If the gates do not pass, the candidate remains unpromoted and the pathway must terminate safely.

Operational evaluation must therefore observe at least five distinct stages:

- sandbox initiation;
- sandbox success or failure;
- promotion attempt;
- gate outcome;
- bridge-mediated experience creation or fail-closed non-creation.

This decomposition matters because the system can succeed at one stage and fail at another. A good evaluation framework must preserve those distinctions.

---

## 39.3 Sandbox Success and Failure

Sandbox success is not the same as final system success.

A sandbox cycle counts as successful when the bounded reasoning environment completes its internal work coherently enough to produce a candidate output, intermediate state, or actionable proposal for further review. A sandbox cycle counts as failed when the internal path cannot complete due to error, contradiction, timeout, malformed state, unavailable dependencies, or another condition that prevents a viable candidate from being formed.

These outcomes should be measured separately from promotion outcomes. The sandbox may succeed while the gates correctly block promotion, and the sandbox may fail before any promotion attempt is even possible. Treating all non-promotion as one undifferentiated failure would erase an important part of the system’s behavior.

---

## 39.4 Promotion Attempts and Gate Outcomes

A promotion attempt begins when the system presents a sandbox-derived candidate for authority-bearing review.

At that point, operational evaluation should measure whether the candidate actually reached the gate path, which sub-gates were traversed, whether the review completed, and what outcome was returned. This includes approval, limited approval, revise, human review, reject, and fail-closed termination where the pathway cannot safely continue.

The gate path should be evaluated as a sequence of observable outcome states rather than a single pass/fail bit. This allows the system to distinguish “good candidate, blocked on bridge,” “candidate rejected by truth review,” “candidate blocked by missing guardian fields,” and “candidate never reached promotion because sandbox formation failed.”

---

## 39.5 Gated Experience Creation

A central object of evaluation is gated experience creation.

In this architecture, a promoted experience is not merely an internal computation that happened to occur. It is a higher-authority state that has crossed the relevant gate path and has been admitted through the bridge into a form the system is allowed to treat as operative, durable, or consequential. This can include authorized internal registration, consciousness-bridge promotion, durable memory eligibility, or another governed form of admitted state.

Operational evaluation should therefore ask not only whether a candidate was generated, but whether a gated experience was actually created. The distinction matters because the system is designed to produce many provisional states that should never become authoritative experiences.

---

## 39.6 Health and Availability Metrics

Health metrics remain necessary, but they belong inside a wider evaluation frame.

Relevant health measures include sandbox service health, gate service health, bridge availability, memory availability where applicable, and the health of supporting governance services involved in promotion. A healthy stack should show that the required services are reachable, responsive, and able to participate in the governed pathway without hidden degradation.

These metrics should be read alongside pathway outcomes. A service reporting healthy status does not prove that sandbox cycles are forming valid candidates, that gates are behaving coherently, or that approved candidates are crossing the bridge correctly.

---

## 39.7 Approval Rates and Bridge Failures

Approval rates and bridge failures are indispensable operational metrics.

Approval rate should be measured over attempted promotions, not over raw user turns or raw sandbox starts. This makes it possible to distinguish between low approval because the system is appropriately selective and low approval because upstream formation is poor or downstream gates are malformed. Bridge failure rate should be measured over approved or approval-eligible candidates that attempted bridge transition but did not successfully create the intended higher-authority experience.

These metrics reveal different pathologies:

- low sandbox success suggests formation instability;
- low promotion-attempt rate suggests candidates are not reaching review;
- low approval rate may indicate strict but working governance, poor candidate quality, or gate misconfiguration;
- high bridge failure rate indicates a breakdown after approval-stage progress;
- high fail-closed rate with poor logs indicates observability weakness rather than safe governance.

---

## 39.8 Fail-Closed Behavior

Fail-closed behavior is part of successful operation, not merely an exception case.

When a required review does not complete, a bridge call fails, a non-200 response occurs, a truth check fails, required guardian fields are missing, or an exception interrupts promotion, the correct behavior is controlled non-promotion. The system should preserve the lower-authority status of the candidate and should not create an unauthorized experience merely because the pathway was partially traversed.

Operational evaluation should therefore include explicit fail-closed scenarios. These scenarios test whether blocked promotions remain blocked, whether partial downstream effects are prevented, and whether the system records the failure in a way that permits diagnosis without granting accidental authority.

---

## 39.9 Scenario-Based Evaluation

Operational evaluation should include scenario families rather than only aggregate counts.

Useful scenarios include: normal sandbox completion followed by approval, sandbox completion followed by rejection, sandbox completion followed by bridge failure, malformed guardian payload causing fail-closed review, truth-check failure blocking promotion, service-health degradation during promotion, and external directive intake that remains bounded inside the sandbox rather than bypassing gates. These scenarios probe whether the architecture preserves authority order under different operational stresses.

Scenario testing is especially important because averages can hide unsafe edges. A system that performs well under ordinary traffic but misbehaves during bridge interruption or malformed review payloads is not operationally trustworthy in the sense this thesis requires.

---

## 39.10 Confidence Bounds and Uncertainty

Where measured quantitatively, operational results should be reported with confidence bounds or equivalent uncertainty language.

If approval rates, bridge failure rates, sandbox success rates, or stability indicators are estimated from observed runs, those estimates should be presented as bounded measurements rather than as absolute timeless facts. This is especially important when sample size is limited, scenarios are heterogeneous, or the system configuration changes over time.

Confidence language matters because operational evaluation is empirical, not metaphysical. The chapter should therefore distinguish clearly between observed results, estimated rates, and architectural expectations.

---

## 39.11 Stability Properties

Operational evaluation should also document stability properties where they are measured.

Relevant stability properties include repeatability of gate outcomes for similar inputs, bounded variation in approval behavior across runs, resilience of fail-closed behavior under degraded service conditions, and consistency of bridge-mediated promotion when all prerequisite conditions are satisfied. Stability in this context does not require identical outputs in every case. It requires that authority transitions remain governed, non-accidental, and interpretable across repeated operation.

This makes stability a governance property as much as a performance property. A system that answers quickly but varies unpredictably in promotion or disclosure behavior is operationally unstable in a way that matters more than raw latency.

---

## 39.12 Formal Evaluation Frame

A compact formal frame helps organize the measured pathway.

Let \(s\) denote a sandbox episode, \(p\) a promotion attempt, \(g\) a gate outcome, and \(b\) a bridge result. Then an evaluated run may be represented as:

\[
s \rightarrow p \rightarrow g \rightarrow b
\]

with the understanding that some runs terminate earlier. A sandbox failure may stop before \(p\); a gate rejection may stop before \(b\); and a bridge failure may occur after a favorable gate outcome but before authorized experience creation.

Where measured, one may report quantities such as sandbox success probability, promotion-attempt rate conditional on sandbox completion, gate outcome frequencies, bridge success rate conditional on approval, and fail-closed retention rate. These quantities are useful only if they preserve the ordering of the pathway rather than collapsing all outcomes into a single undifferentiated score.

---

## 39.13 Closing Statement

Operational evaluation in Ms. Allis concerns the full governed pathway from sandbox reasoning to gated experience creation.

It therefore includes sandbox success and failure, promotion attempts, gate outcomes, bridge failures, approval rates, service health, and fail-closed behavior as distinct evaluative objects. Where results are measured, they should be reported with formal uncertainty language, explicit gate-outcome interpretation, and stability properties that show whether the system preserves bounded authority under repeated operation.
