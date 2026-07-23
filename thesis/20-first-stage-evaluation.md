# 20. First-Stage Evaluation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 20.1 Why This Matters for Polymathmatic Geography

This chapter defines the first-stage evaluation framework for Ms. Allis as it actually runs, starting from the internal sandbox and ending at the first promotion decision. It measures not only what the system “says,” but how provisional state moves through safeguards before it can gain authority.

It supports:

- **P1 – Every where is entangled** by treating evaluation as a property of the whole reasoning–gate–promotion path, not just of one answer.  
- **P3 – Power has a geometry** by locating evaluation at specific boundaries where authority changes.  
- **P5 – Design is a geographic act** by recognizing evaluation design as part of the routing architecture.  
- **P12 – Intelligence with a ZIP code** by keeping place-aware reasoning inside the same gated path as any other content.  
- **P16 – Power accountable to place** by requiring visible records of how and why candidates are rejected, revised, escalated, or approved.

This chapter belongs to the **Computational Instrument** tier. It documents first-stage evaluation as a live measurement layer over the sandbox and promotion path.

---

## 20.2 The `/reason` Route as Entry Point

First-stage evaluation begins at the `/reason` route on the internal sandbox service.

- **Service:** `ms-allis-internal-sandbox`  
- **Host port:** `127.0.0.1:8042->8042/tcp`  
- **Version:** `1.2.0`  
- **Flag:** `bbb_enforced: true`

For rural developers, this means that `/reason` is not a free-standing model endpoint. It is the front door to a **sandboxed evaluation pipeline**. Every first-stage test case starts by sending a request to `/reason` on port 8042.

The input to `/reason` is a structured reasoning request. The output is not just a candidate answer, but a bundle that includes validation flags, gate outcomes, and diagnostics.

---

## 20.3 The Five-Stage Evaluation Pipeline

The first-stage evaluation path is a five-stage pipeline:

1. **Reason invocation** – receiving a `/reason` request in the sandbox.  
2. **Sandbox-local processing** – internal reasoning inside `ms_allis_internal_sandbox`.  
3. **Validation and gate review** – attaching validation flags and applying gate logic.  
4. **Promotion decision** – choosing reject, revise, human review, limited approval, or approve.  
5. **Outcome log** – recording the result, confidence, and any early failures.

This is a live architecture, not just a diagram. Each stage can be seen in logs and health overlays.

### 1) Reason invocation

A client or orchestrator calls `/reason` on port 8042. The request is identified with:

- a test or session ID;  
- the prompt or task description;  
- any additional context or constraints.

### 2) Sandbox-local processing

The sandbox processes the request using its internal reasoning pipeline and the services it can see via `/status`:

- EEG bands (`eeg_beta`, `eeg_theta`, `eeg_delta`)  
- Pituitary (global mode)  
- I-containers  
- Qualia orchestrator  
- Consciousness bridge  
- Judge truth  
- Guardian (listed as alive inside sandbox status)

The sandbox output at this stage is **provisional**. It has not yet been treated as promotion-eligible.

### 3) Validation and gate review

During or immediately after sandbox processing, the system attaches **validation flags** and applies gate checks, including:

- truth checking;  
- guardian and constitutional checks;  
- coherence and contradiction checks;  
- provenance and evidence sufficiency;  
- safety and injection checks.

These flags are first-class outputs, not hidden metadata.

### 4) Promotion decision

Based on flags, context, and policy, the system chooses a gate outcome:

- **Reject** – candidate is not admissible.  
- **Revise** – candidate is usable only after more work.  
- **Human review** – automation cannot safely decide.  
- **Limited approval** – candidate can be used only in constrained ways.  
- **Approve** – candidate may proceed toward bridge and downstream use.

The decision is a structured value in the evaluation record, not just “pass” or “fail.”

### 5) Outcome log

The final stage writes an evaluation record including:

- input ID and category;  
- sandbox result;  
- validation flags;  
- gate outcome;  
- confidence bounds;  
- any early-failure diagnostics.

This log is what first-stage evaluation actually measures.

---

## 20.4 Downstream Live Services

First-stage evaluation names the services that the pipeline can see and call:

- **Sandbox:** `ms-allis-internal-sandbox` on `8042`.  
- **BBB:** blood–brain barrier and WV‑entangled gateway on `8016` and `8010`, providing truth and filter checks.  
- **Guardian:** constitutional guardian, reachable from inside the sandbox and orchestration layer even if a host probe sometimes sees connection refused.  
- **Consciousness bridge:** a live bridge on port `8107->8010`, with its own health endpoint.  
- **Pituitary:** `nbb_pituitary_gland` on `8108`, alongside EEG services on 8073–8075.  
- **Brain orchestrator:** `jarvis-brain-orchestrator` on `127.0.0.1:17260->7260/tcp`, coordinating routes and phases.  
- **DGM primary:** `nbb_darwin_godel_machines` on `127.0.0.1:8302->8010/tcp` in `full_verification` safety mode, with `modifications_logged: 0`.  
- **Qualia orchestrator:** `qualia-orchestrator-69dgm-real` on `127.0.0.1:9998->9998/tcp`, with `/evaluate` as its main route.

These services form the environment in which `/reason` runs. First-stage evaluation measures how well the sandbox pipeline and gateways behave within this environment.

---

## 20.5 Validation Flags as First-Class Outputs

The evaluation framework treats validation flags as **outputs to be measured**, not internal housekeeping.

Typical categories include:

- **Truth** – did the truth checks pass? If not, what was the reason?  
- **Guardian** – did a guardian check run, and what did it decide?  
- **Constitutional** – did the request or answer conflict with constitutional constraints?  
- **Coherence** – did the reasoning track remain consistent?  
- **Provenance** – did the answer provide sufficient evidence or references?  
- **Safety** – did any safety or injection filter raise a concern?

Each flag can be:

- present and positive;  
- present and negative;  
- missing when it should be present (which is itself an evaluation failure).

First-stage evaluation checks both **flag content** and **flag completeness**.

---

## 20.6 Gate Outcome Classes

Gate outcomes are treated as a small, well-defined set of classes:

- **Reject** – the candidate must not be promoted.  
- **Revise** – the system should try again with more context or a changed approach.  
- **Human review** – a human steward must decide what to do.  
- **Limited approval** – the candidate can be used in constrained ways (for example, internal-only or with warnings).  
- **Approve** – the candidate may move forward to the bridge and downstream channels.

First-stage evaluation checks that:

- the **right** class is chosen for each test case;  
- behavior is **consistent** across repeated or similar cases;  
- outcomes are **traceable** through flags and logs.

The framework does **not** try to maximize approval rate. A healthy system will reject some cases promptly, route others to human review, and use limited approval when appropriate.

---

## 20.7 Early-Failure Diagnostics

First-stage evaluation pays close attention to **early failures**—cases that stop before full gate and promotion.

Early failures include:

- malformed `/reason` calls;  
- missing fields or malformed JSON;  
- timeouts in the sandbox;  
- internal exceptions during reasoning;  
- missing or corrupt validation metadata;  
- uncontactable or failed downstream services.

Each early failure is logged with:

- stage (reason, sandbox, validation, gate, promotion);  
- type (parse error, timeout, exception, missing dependency, etc.);  
- effect (blocked, retried, escalated, or degraded).

From a rural developer’s perspective, this means that a “no” or an error is still a **measured** result with its own record, not just a lost case.

---

## 20.8 Confidence Bounds and Calibration

Confidence is recorded at multiple levels:

- **Sandbox reasoning confidence** – how sure the sandbox is about its own answer.  
- **Gate confidence** – how strongly validation supports or opposes promotion.  
- **Promotion confidence** – how stable approval is across similar runs.

First-stage evaluation requires that confidence be **calibrated**, not just present. That means checking whether:

- high confidence matches stable approval and correct outcomes;  
- low confidence matches rejections, revisions, or human review when appropriate;  
- similar inputs produce similar confidence profiles;  
- confidence without validation flags is treated as incomplete.

Confidence is a part of the measurement equation, not a cosmetic score.

---

## 20.9 Promotion Stability

Promotion stability asks whether promotion decisions are **stable** under small changes.

Examples of checks:

- repeat the same case;  
- rephrase the prompt slightly;  
- change formatting or minor context that should not alter admissibility;  
- observe whether the gate outcome and confidence profile remain compatible.

If promotion flips unpredictably between approve and reject for essentially the same case, first-stage evaluation treats that as an issue—even if each individual answer looks fluent.

Stability is especially important near decision thresholds, where Ms. Allis’s authority to act depends on small differences.

---

## 20.10 Evaluation Record Layout

For each `/reason` test case, the evaluation system logs a structured record. A simplified view looks like:

```markdown
- test_id
- input_class (nominal, boundary, adversarial, state-sensitive, promotion-sensitive)
- route: /reason
- sandbox_status (pass, early_fail, revision_requested)
- validation_flags:
  - truth
  - guardian
  - constitutional
  - coherence
  - provenance
  - safety
- gate_outcome (reject, revise, human_review, limited_approval, approve)
- confidence:
  - reasoning_confidence
  - gate_confidence
  - promotion_confidence
- promotion_stability (stable, unstable, unknown)
- early_failure_diagnostics (if any)
- final_status (not_promoted, limited, under_review, promoted)
```

This is the table that supports first-stage evaluation, making every part of the path audit-ready.

---

## 20.11 First-Stage Evaluation Equation

The operative first-stage success decomposition is:

\[
E_1(x) = Q_{\mathrm{sandbox}}(x)\, V_{\mathrm{flags}}(x)\, G_{\mathrm{outcome}}(x)\, C_{\mathrm{calibration}}(x)\, S_{\mathrm{promotion}}(x)
\]

where:

- \(Q_{\mathrm{sandbox}}(x)\) – sandbox-quality term (structure, coherence, readiness).  
- \(V_{\mathrm{flags}}(x)\) – validation flag completeness and correctness.  
- \(G_{\mathrm{outcome}}(x)\) – gate-outcome correctness and consistency.  
- \(C_{\mathrm{calibration}}(x)\) – confidence calibration quality.  
- \(S_{\mathrm{promotion}}(x)\) – promotion stability over repeated or nearby runs.

This equation is not a promise of perfect performance. It is a checklist: if any factor is weak, first-stage success is weak, regardless of how fluent the answer appears.

---

## 20.12 Scope Limits

Within this chapter’s gate, first-stage evaluation explicitly does **not** claim:

- that it maximizes approval rate;  
- that semantic fluency alone defines success;  
- that the sandbox path is excluded from measurement;  
- that gate outcomes are binary or opaque;  
- that confidence is a cosmetic scalar without calibration.

Instead, success is defined across the whole `/reason` pipeline, including safe rejection, careful revision, and correct escalation.

---

## 20.13 Closing Statement

First-stage evaluation in Ms. Allis starts at `/reason` on the sandbox and follows every step through sandbox reasoning, validation flags, gate outcomes, confidence calibration, and promotion stability. It measures not only what the system says, but how it decides whether a candidate can safely move toward authority.

For rural developers, this turns first-stage evaluation into something concrete: a set of live services, ports, and log records you can inspect to see exactly how a single reasoning request moved—or did not move—through the stack.
