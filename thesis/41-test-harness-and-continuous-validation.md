# 41. Test Harness and Continuous Validation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 41.1 What This Chapter Is Allowed to Claim

Chapter 41 is limited to **an implemented continuous validation harness** over the currently built governed chain.

At the July 2026 sealed scope, it may claim that:

- a continuous validation harness is installed at `services/hilbert/continuous_validation_harness.py`;  
- harness unit tests pass;  
- the final live harness status is recorded as **closed**;  
- core health endpoints pass along the governed chain;  
- sandbox readiness, BBB enforcement, guardian, judge, and bridge visibility are validated;  
- guardian valid/risk/malformed schema probes pass;  
- DGM pass/fail/immutable‑target behavior is validated through the actual governed DGM `run_cycle` contract when direct test targets are outside the allowlist;  
- classification outcomes stay inside the declared set;  
- an hourly cron runner (`scripts/ch41_continuous_validation.sh`) is installed and has executed successfully at least once.

It must **not** claim exhaustive coverage, perfect system health, mathematical completeness for all future invariants, or absolute drift prevention.

---

## 41.2 Harness Location and Installation

The continuous validation harness is a real, installed program, not just a design sketch.

Within this chapter, it may claim that:

- the harness code lives at `services/hilbert/continuous_validation_harness.py`;  
- the harness has its own **unit tests**, and those tests pass;  
- the harness has been exercised against the live governed chain at least once, with its final status marked as **closed** in the evidence.

For rural developers, the practical meaning is that there is a **single, named script** you can look at and run to see how the system tests itself.

---

## 41.3 Core Health and Readiness Checks

The harness begins by checking **core health endpoints** along the governed chain.

These checks cover at least:

- BBB and Constitutional Guardian health;  
- Commons Gateway;  
- Chroma;  
- Hilbert State;  
- Hilbert Time;  
- Phi;  
- the internal sandbox.

It also verifies **sandbox readiness**, which includes:

- sandbox itself is healthy;  
- BBB enforcement is visible;  
- guardian, truth‑judging, and consciousness‑bridge dependencies appear as live from the sandbox point of view.

This confirms that the core path needed for governed reasoning is **up and reachable** before deeper tests run.

---

## 41.4 Guardian Schema and Risk Probes

The harness exercises the **guardian** with several categories of payloads.

Within this scope, Chapter 41 may claim that the harness successfully sends:

- **valid** guardian payloads that should pass;  
- **risk‑flagged** payloads that should be treated as review or block;  
- **malformed or schema‑broken** payloads that should be rejected or fail closed.

The passing probes show that:

- required fields are enforced;  
- malformed submissions are not silently accepted;  
- the guardian’s responses stay inside the **declared outcome set** for its classification scheme.

This keeps the guardian’s schema contract tied to live, repeatable tests.

---

## 41.5 DGM Pass/Fail and Immutable Targets

The harness also validates **DGM behavior** through the actual governed `run_cycle` contract.

At the sealed scope, it may claim that:

- DGM **pass** cases are handled as expected;  
- DGM **fail** cases are handled as expected;  
- attempts against **immutable targets** are blocked according to the governed rules;  
- when direct test targets are outside the allowlist, the validation is still tied to the **real `run_cycle` contract**, not to a fake or bypass route.

This means DGM testing is anchored to the same governed pathway that would operate in practice, while still respecting the allowlist boundaries.

---

## 41.6 Classification Outcome Invariants

The harness verifies that classification outcomes stay inside a **declared outcome set**.

Within this chapter, classification invariants are limited to statements such as:

- guardian and harness classification results remain within a fixed set of allowed labels;  
- tests confirm that no unexpected or out‑of‑contract outcome labels appear during harness runs.

The chapter may **not** claim that every future classifier or decision rule has been proven mathematically complete. It only claims that, for the harnessed chain, **observed outcomes stay within the intended classification space**.

---

## 41.7 Continuous Validation Cadence

Continuous validation is wired into the running system via an **hourly cron runner**.

This chapter may claim that:

- `scripts/ch41_continuous_validation.sh` is installed as a scheduled runner;  
- the cron entry has been executed successfully at least once;  
- the harness can be invoked on a repeating schedule to re‑check the governed chain over time.

For rural operators, the key idea is that validation is **not a one‑time event**. The system is set up to keep testing itself as it runs.

---

## 41.8 Bounded Claims About Coverage and Drift

The rewrite rule keeps the chapter honest about what it **cannot** say.

Chapter 41 does **not** claim:

- exhaustive coverage of every service, route, or edge case;  
- perfect system health at all times;  
- a mathematically complete set of invariants for all future behaviors;  
- permanent protection against configuration drift or regression.

Instead, it claims:

- an implemented, passing harness over the **currently built governed chain**;  
- a real schedule for running that harness;  
- specific validated behaviors (health, readiness, guardian schema, DGM pass/fail/immutable, classification outcomes) inside that chain.

---

## 41.9 Step‑by‑Step View for Rural Developers

From a rural developer’s perspective, the Chapter 41 harness can be understood as a simple, repeatable script that checks:

1. **Core health.**  
   - Call the health endpoints for BBB, guardian, commons gateway, Chroma, Hilbert time/state, Phi, and the sandbox.

2. **Sandbox and enforcement visibility.**  
   - Ask the sandbox for its status and verify it sees BBB, guardian, judge, and bridge as live.

3. **Guardian behavior.**  
   - Send good, risky, and malformed payloads; check that the guardian’s responses and classifications match the contract.

4. **DGM behavior.**  
   - Through the governed `run_cycle`, confirm pass, fail, and immutable‑target handling behaves as designed, respecting any allowlist limits.

5. **Classification invariants.**  
   - Confirm that all classification outputs are within the allowed label set.

6. **Schedule and logs.**  
   - Let the hourly runner invoke this harness; watch its logs or status to see whether the governed chain still passes.

If any of these checks fail, the harness is doing its job: it flags drift or breakage early, before those problems become authority‑bearing faults.

---

## 41.10 Closing Statement

Chapter 41 presents a **living test harness** for Ms. Allis’s governed chain.

By installing a continuous validation script, running unit tests, exercising core health endpoints, checking sandbox readiness and enforcement visibility, probing guardian schema behavior, validating DGM pass/fail/immutable handling, enforcing classification outcome sets, and wiring an hourly cron runner, the system gains a practical way to keep its core governance path under ongoing scrutiny—without pretending that coverage is exhaustive or that future drift is impossible.
