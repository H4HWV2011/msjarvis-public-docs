# 33. Judge Ensemble and Signed Verdicts

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 33.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis uses a **live, signed judge fabric** instead of taking unverified model outputs at face value. It focuses on how judges issue cryptographically signed verdicts, how those verdicts are checked, and how tampering is rejected.

It supports:

- **P1 – Every where is entangled** by tying judgment, provenance, and system state together through signed decisions.  
- **P3 – Power has a geometry** by placing authority in verifiable judge chains and barriers (like BBB), not in anonymous model whispers.  
- **P5 – Design is a geographic act** by making the evaluative fabric a concrete piece of infrastructure with addresses, keys, and health checks.  
- **P12 – Intelligence with a ZIP code** by letting local, place-aware reasoning still pass through the same signed judge layer as anything else.  
- **P16 – Power accountable to place** by requiring that important verdicts carry signatures that can be audited, not just trusted on style.

This chapter belongs to the **Computational Instrument** tier. It documents a **bounded, as-built judge/verdict system**, not perfect truth or universal morality.

---

## 33.2 The Judge Fabric: Truth, Consistency, Alignment, Ethics

The judge fabric is an **ensemble of specialized judge services**:

- **Truth judges** – check factual grounding, retrieval consistency, and contradictions.  
- **Consistency judges** – check whether an answer fits previous commitments and internal constraints.  
- **Alignment / policy judges** – check for policy, ethics, or community‑defined alignment.  
- **Safety judges** – flag potentially harmful or high‑risk content.

Each judge runs as its own service with:

- a `/health` endpoint – to show it is alive;  
- a `/judge-public-key` endpoint – to publish the key needed to verify its signatures.

Judges do not generate the main answer. They **evaluate candidate answers** produced elsewhere (for example, by the reasoning sandbox) and emit **verdicts** about those candidates.

---

## 33.3 ML‑DSA‑65 Signing of Verdicts

Every judge verdict is accompanied by a **detached digital signature**.

Key properties:

- Judges use an **ML‑DSA‑65** signing scheme (a lattice‑based post‑quantum signature algorithm) to sign their verdicts.  
- Each judge publishes its ML‑DSA‑65 public key via `/judge-public-key`.  
- The verdict itself and its signature are kept separate (detached), so the system can reconstruct the signed payload and verify the signature independently.

This means that:

- when a judge says “this answer is coherent enough” or “this answer fails truth,” that statement is cryptographically verifiable as coming from that judge service;  
- if someone tampers with the verdict body or the signature, the check will fail;  
- an unsigned verdict is treated as **invalid**.

So the system does not just ask, “What did the judge say?” It also asks, “Can we prove this is really what the judge said?”

---

## 33.4 BBB Detached-Signature Verification

The **BBB layer** (blood–brain barrier / entangled gateway) performs detached-signature verification.

Its responsibilities include:

1. **Reconstruct verdict payload.**  
   From the verdict object, BBB reconstructs the exact payload the judge claims to have signed.

2. **Check `_sig` shape.**  
   It ensures the verdict’s signature field (`_sig` or equivalent) has the expected ML‑DSA‑65 format for that judge.

3. **Verify signature with judge’s public key.**  
   It retrieves the judge’s public key (already cached from `/judge-public-key`) and verifies the signature against the reconstructed payload.

4. **Fail closed.**  
   - If verification passes: the verdict is **valid and signed**.  
   - If the verdict is tampered, unsigned, or malformed: the verdict is **rejected**.

In short:

- **signed, valid** verdicts may enter the decision path;  
- **tampered or unsigned** verdicts are treated as **no verdict** and cannot be used as authority.

---

## 33.5 Fail-Closed Behavior

The judge fabric is designed to **fail closed**:

- If BBB cannot validate a verdict’s signature, that verdict is not trusted.  
- If a judge is down or its public key cannot be obtained, its verdicts are not used for gating.  
- If verdicts disagree strongly or look inconsistent with expectations, higher‑level components can route the case to **human review** or a more conservative path.

Fail-closed behavior means:

- the system prefers **“no verdict”** over **“a suspicious verdict”**;  
- missing or invalid signatures **do not** silently pass as valid.

This is essential in any setting where judge decisions affect promotion, safety, or commons behavior.

---

## 33.6 Judges in the Reasoning and Promotion Pipeline

Signed judge verdicts are used inside the broader pipeline like this:

1. The reasoning sandbox (8042) produces a **candidate answer**.  
2. The answer is sent to one or more judge services (truth, consistency, safety, etc.).  
3. Each judge returns a **verdict + ML‑DSA‑65 signature**.  
4. BBB verifies each verdict’s signature using judge public keys.  
5. Verified verdicts are combined into a **validation summary**.  
6. Based on this summary, the system decides whether to:  
   - reject the answer;  
   - revise it;  
   - route to human review;  
   - give limited approval;  
   - treat it as eligible for full approval by downstream gates.

The judge layer therefore **influences** promotion decisions, but it is still one component in a larger path that includes BBB, guardian, and DGM evaluation where applicable.

---

## 33.7 What is Actually Guaranteed (and What Is Not)

The signed judge fabric guarantees:

- That a verdict accepted into the pipeline really came from a known judge service.  
- That verdicts are not silently modified between judge and BBB.  
- That tampered or unsigned verdicts are rejected.  
- That judge health and key presence can be checked via `/health` and `/judge-public-key`.

It does **not** guarantee:

- perfect truth;  
- universal moral correctness;  
- absence of all model error;  
- legal advice;  
- clinical or therapeutic safety;  
- sentience or biological consciousness.

In other words, the system can prove **who said what** and **that it wasn’t tampered with**, but it cannot prove that what was said is infallible.

---

## 33.8 Judge-Public-Key and Health Surfaces

Each judge exposes two important surfaces:

- **`/health`** – shows whether the judge service is up and responsive.  
- **`/judge-public-key`** – returns the judge’s ML‑DSA‑65 public key (and sometimes metadata such as key id or rotation info).

The system uses these to:

- confirm that necessary judges are live before relying on their verdicts;  
- obtain or refresh public keys for signature verification;  
- detect when a particular judge is down and respond accordingly (for example, require human review in high‑stakes cases instead of relying on a partial judge set).

For rural operators, these endpoints make the judge fabric something you can **inspect with simple tools** instead of having to trust as a black box.

---

## 33.9 Handling Tampered and Unsigned Verdicts

Tampered or unsigned verdicts are handled carefully:

- If the payload has been changed after signing, the ML‑DSA‑65 verification will fail.  
- If the `_sig` field is missing or malformed, the verdict is treated as **unsigned**.  
- In both cases, BBB and related components treat the verdict as **invalid** and exclude it from the trusted verdict set.

Possible follow-up behaviors include:

- Retry a fresh judgment request (in case of transient errors).  
- Route the case toward **more conservative decisions** (reject, revise, or human review).  
- Log the event for audit and future inspection.

This ensures that **verdict integrity is treated as first-class safety information**, not a minor detail.

---

## 33.10 Relationship to Chapters 35 and the Wider Stack

Chapters 33 and 35 together describe:

- the **judge ensemble** and signed verdict infrastructure;  
- how **delegated verification** via BBB and guardian works;  
- how the judge fabric fits into larger governance, temporal, and DGM structures.

In the wider system:

- Temporal and heartbeat chapters ensure that judge services are not just up, but reliably up over time.  
- DGM chapters can help tune judge behavior in bounded ways (such as adjusting thresholds) without bypassing signatures or verification.  
- Identity and retention chapters ensure that verdict logs can be audited without turning them into surveillance dossiers.

So the judge fabric is **one layer** in a larger protected stack, not a standalone oracle.

---

## 33.11 Step-by-Step View for Rural Developers

On a running system, judge verdict handling looks like this:

1. A candidate answer is produced in the sandbox.  
2. The system asks the truth/consistency/alignment judges to evaluate it.  
3. Each judge replies with a verdict plus an ML‑DSA‑65 signature.  
4. BBB reconstructs the signed payload and verifies each signature with the judge’s public key.  
5. Invalid or unsigned verdicts are discarded; valid ones are combined into a decision summary.  
6. Based on that summary, the system either tightens, revises, rejects, or cautiously approves the answer.

From your point of view, this means the system’s “inner critics” **sign their work**, and the rest of the stack refuses to treat unsigned or tampered criticism as binding.

---

## 33.12 Closing Statement

Chapters 33 and 35 establish a **live, signed, fail‑closed judge fabric** over Ms. Allis’s evaluative services. Truth, consistency, alignment, and safety judges each publish ML‑DSA‑65 public keys, sign their verdicts, and rely on BBB and guardian layers to verify these signatures and reject tampering.

This does not create perfect truth or moral certainty, but it does create a concrete, auditable chain from “who judged this answer” to “how do we know this verdict is real,” anchoring the system’s evaluative geometry in verifiable infrastructure instead of unmarked model output.
