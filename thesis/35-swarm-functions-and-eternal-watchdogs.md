# 35. Swarm Functions and Eternal Watchdogs

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 35.1 Swarm Functions in Ms. Allis

Swarm functions in Ms. Allis are the **small, distributed support jobs** that keep the system honest and running, rather than a single big “brain” making all decisions.

They:

- watch services, queues, and logs;  
- compare expected behavior to what is actually happening;  
- route work or alerts when something drifts;  
- retry, halt, or flag operations that look unhealthy.

Think of swarm functions as a barn crew: lots of small, steady tasks that together keep the place in order.

---

## 35.2 Eternal Watchdogs as Continuous Monitors

Within the swarm, **eternal watchdogs** are the processes that **keep watching over time** for problems that should never be ignored.

They look for:

- silent failures or drift;  
- missing reviews or skipped gates;  
- growing queues that nobody is working off;  
- transitions that happen without the normal paperwork (logs, flags, or receipts).

They are “eternal” in the sense that they are **always on**, not that they have any mystical quality. Their job is to ask, over and over: “Is the system really following its own rules?”

---

## 35.3 Watchdogs and the Judge Fabric

Because Chapters 33 and 35 describe a **signed, fail‑closed judge fabric**, watchdogs pay special attention to judge behavior.

They watch that:

- judge containers (truth, consistency, alignment, ethics, pipelines) are up and healthy;  
- each judge’s `/health` and `/judge-public-key` endpoints respond;  
- public keys report the expected **ML‑DSA‑65** scheme;  
- verdicts include detached signatures in the expected `_sig` shape;  
- tampered or unsigned verdicts are being rejected, not quietly accepted.

If watchdogs see verdicts without valid signatures being used as if they were trustworthy, that is treated as a serious governance fault and should trigger alerts or fail‑closed behavior.

---

## 35.4 BBB Detached-Verification Under Watch

Watchdogs also monitor the **BBB detached‑signature verification path**.

They check that:

- the verification logic is reconstructing verdict payloads correctly;  
- signature checks succeed only when the payload and signature really match;  
- tampered or unsigned verdicts are being rejected by BBB;  
- BBB and the Constitutional Guardian host health endpoints stay responsive.

In plain language: watchdogs make sure that **the bouncer at the door is awake and checking IDs**, not just waving everyone through.

---

## 35.5 Swarm Oversight of Promotion and Gates

Swarm functions do more than look at individual services; they watch **promotion and gate behavior**.

They ask:

- Are candidate answers being judged before use, or skipping straight past judges?  
- Are gate results (approve / revise / reject / limited) logged?  
- Are blocked transitions staying blocked?  
- Can you reconstruct, after the fact, **why** something was approved?

This keeps the system from drifting into “it works, but nobody knows why” territory. In this architecture, movement from **candidate** to **approved** should always leave tracks.

---

## 35.6 Concrete Watch Targets for Rural Operators

For someone running Ms. Allis on local hardware, the practical watchdog targets include:

- **Judge services.**  
  Truth, consistency, alignment, ethics, and pipeline judges: healthy, key‑serving, and signing verdicts.

- **Signed verdicts.**  
  Presence of ML‑DSA‑65 signatures, correct `_sig` shape, and logs of failed verification.

- **BBB and guardian.**  
  Health endpoints responding; failed signature checks causing rejections, not silent passes.

- **Gate and promotion logs.**  
  Records showing how a candidate answer moved through judges, verification, and final decision.

In a rural environment, this gives you concrete things you can **grep and tail in logs**, not just concepts.

---

## 35.7 What This Chapter Does Not Claim

Within this gate, Chapters 33 and 35 **do not** claim:

- perfect truth or universal moral correctness;  
- absence of all model error;  
- legal advice or clinical safety guarantees;  
- sentience or biological consciousness.

They claim only that:

- the judge fabric is **live, signed, and fail‑closed**;  
- tampered and unsigned verdicts are rejected;  
- BBB and guardian surfaces are healthy and involved in verification;  
- focused contract tests for judge verdict behavior pass.

The watchdog swarm helps ensure these claims stay true over time.

---

## 35.8 Closing Statement

In Ms. Allis, **swarm functions** and **eternal watchdogs** are the quiet machinery that keeps the signed judge fabric trustworthy. They monitor judge health, ML‑DSA‑65 keys, detached signatures, BBB verification, and gate behavior so that verdicts used in decisions are **both verifiable and checked**, not just well‑worded.

For rural developers, this means you can verify with your own tools that the system’s “inner judges” and “bouncers” are awake, signed, and failing closed—without having to take any of it on faith.
