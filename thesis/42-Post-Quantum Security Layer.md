# 42. Post‑Quantum Signature and Verification Layer

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 42.1 Purpose and Gate‑Bound Scope

This chapter describes how Ms. Allis uses **post‑quantum judge signing and verification** to protect authority‑bearing verdicts as they cross the Blood–Brain Barrier (BBB).

Within this sealed gate, Chapter 42 may claim only that:

- judge verdicts are signed with **ML‑DSA‑65** at the verified runtime scope;  
- corresponding **public keys** are available for verification;  
- **tampered** or **unsigned** verdicts are rejected rather than silently accepted;  
- the **BBB** delegates signature checking to a trusted verifier component;  
- a bounded **Ed25519 fallback** exists and is used only where explicitly allowed and observed.

It must **not** claim universal post‑quantum coverage, perfect cryptography across the entire stack, or future‑proof security against all quantum advances. The focus is on what is **implemented and tested**, not on ideal theory.

---

## 42.2 Why Post‑Quantum Judge Signing Matters

For rural developers, think of the judges as a panel whose written decisions control whether an action is allowed to move forward.

If anyone could forge those decisions, the rest of the safety architecture would not matter. This chapter therefore:

- treats judge verdicts as **authority‑bearing messages**;  
- protects them with **ML‑DSA‑65** signatures so that an attacker, even with future quantum capabilities, cannot easily forge them;  
- ensures that only verdicts with valid signatures can pass through the BBB into higher‑authority parts of the system.

In plain language: *“The judges sign their work, and the system checks the signature before it trusts what they say.”*

---

## 42.3 ML‑DSA‑65 Judge Signing

At the verified runtime scope, every verdict that leaves the judge pipeline is:

1. **Serialized** into a stable, canonical format.  
2. **Signed** with **ML‑DSA‑65** using a private key held by the judge signer.  
3. **Bundled** as a payload that includes:
   - the verdict body;  
   - the ML‑DSA‑65 signature;  
   - a key identifier for the corresponding public key.

The chapter is allowed to state that:

- ML‑DSA‑65 signing is the **default and active** method for judge verdicts in this configuration;  
- verdicts are not supposed to leave the judge pipeline unsigned.

Other messages in the system may still use other schemes, but this chapter’s claims are limited to the **judge verdict path**.

---

## 42.4 Public‑Key Availability at Runtime

A signature is only meaningful if verifiers can find the right **public key**.

Within this gate, Chapter 42 may claim that:

- the judge’s ML‑DSA‑65 public key (or an equivalent verifying key) is made available to verification components at runtime;  
- the BBB and its verifier can obtain this key through configuration or a small internal endpoint;  
- the key identifier in each verdict matches one of the **known, live public keys**, allowing correct verification.

For rural operators, this means there is a concrete answer to:

- “Where does the BBB get the judge’s public key?”  
- “How does it know which key to use for a given verdict?”

The architecture expects that answer to be **visible and checkable**, not hidden magic.

---

## 42.5 BBB Verifier Delegation

The **Blood–Brain Barrier (BBB)** is the choke point between lower‑authority reasoning and higher‑authority action.

Earlier, a broken verifier left the BBB unable to distinguish valid signatures from invalid ones. The fix, which this chapter is allowed to rely on, is:

- the BBB no longer tries to implement its own low‑level verifier in isolation;  
- instead, it **delegates** signature checking to a shared verifier component that already implements ML‑DSA‑65 (and its allowed fallbacks) correctly.

Operationally, at the verified scope:

1. A verdict arrives at the BBB with payload, signature, and key identifier.  
2. The BBB calls the shared verifier with these fields.  
3. The verifier:
   - looks up the correct public key;  
   - checks the ML‑DSA‑65 signature;  
   - returns “valid” or “invalid” (plus any diagnostic result).  
4. The BBB uses this result to make gate decisions.

The key point is that **verification code is centralized and known to work**, and the BBB depends on it rather than re‑implementing cryptography in a fragile way.

---

## 42.6 Tamper and Unsigned Verdict Rejection

Within this gate, Chapter 42 may claim that the BBB enforces **strict rejection** of verdicts that do not verify:

- If the ML‑DSA‑65 signature check fails, the verdict is classified as **invalid / forged / unsigned**.  
- Such verdicts are **not** allowed to grant promotion authority, regardless of their content.  
- The failure is treated as a meaningful event to be logged and investigated, not as a warning that can be ignored.

For rural developers, you can think of the logic as:

- “No valid signature, no power.”

Even if the system otherwise likes what the verdict says, it cannot act on it without a passing signature check.

---

## 42.7 Ed25519 Fallback: Bounded and Explicit

The gate instructions allow a **bounded Ed25519 fallback** at the verified runtime scope.

This chapter is allowed to claim that:

- Ed25519 is used only in **specific, documented paths**, such as compatibility with existing tools or legacy data;  
- those paths are known to the verifier and are handled explicitly;  
- Ed25519 is **not** the primary algorithm for judge verdicts; ML‑DSA‑65 is.

In practice, this means:

- the verifier component understands when a verdict or associated metadata indicates an Ed25519‑signed context;  
- the BBB can distinguish between:
  - properly ML‑DSA‑65‑signed verdicts (normal case);  
  - permitted Ed25519 cases (bounded fallback);  
  - everything else, which must be rejected.

This chapter does **not** claim that Ed25519 is post‑quantum secure. It only acknowledges its controlled, limited use where the runtime evidence shows it is still in play.

---

## 42.8 Step‑by‑Step View for Rural Developers

For someone running Ms. Allis in a rural setting, you can think of the Chapter 42 path as this sequence:

1. **Judges make a decision.**  
   - The system generates a verdict payload in a clear, structured format.

2. **Verdict is post‑quantum signed.**  
   - The judge signer uses ML‑DSA‑65 to sign the payload with its private key.

3. **BBB receives verdict + signature.**  
   - The package arrives at the BBB as part of the governance pipeline.

4. **BBB calls the verifier.**  
   - The BBB hands the payload, signature, and key ID to the shared verifier.

5. **Verifier checks the signature.**  
   - Under normal conditions, it uses ML‑DSA‑65 and the matching public key.  
   - In specific, allowed cases, it can recognize and handle Ed25519.

6. **If verification passes.**  
   - The BBB treats the verdict as authentic and allows the promotion path to continue.

7. **If verification fails or is missing.**  
   - The BBB blocks the verdict from granting authority and records the failure.

If any step in this chain is broken—for example, if the verifier cannot load the key—the expected behavior is to **fail closed**, not to silently treat all verdicts as valid.

---

## 42.9 What This Chapter Does Not Claim

Staying within the sealed scope, Chapter 42 explicitly does **not** claim:

- that every internal or external message in Ms. Allis is post‑quantum protected;  
- that all possible cryptographic attacks have been ruled out;  
- that Ed25519 is safe against large‑scale quantum adversaries;  
- that no configuration change could ever weaken the judge‑signing path.

Instead, it makes the narrower claims that:

- judge verdicts at the verified runtime scope are **signed with ML‑DSA‑65**;  
- the corresponding public keys are **available and used** for verification;  
- the BBB **delegates** verification to a working component;  
- **tampered or unsigned** verdicts are rejected;  
- **Ed25519 fallback** exists only in clearly bounded, observed contexts.

---

## 42.10 Closing Statement

Chapter 42 anchors post‑quantum security directly to **who gets to speak with authority inside Ms. Allis**.

By requiring ML‑DSA‑65 signatures for judge verdicts, ensuring that the BBB delegates to a working verifier, rejecting tampered or unsigned decisions, and keeping Ed25519 as a small, explicit fallback, the system makes verdict authenticity a concrete, testable property instead of a wish. For rural developers, this offers a clear, step‑by‑step picture of how Ms. Allis protects the path from **“the judges decided”** to **“the system is allowed to act.”**
