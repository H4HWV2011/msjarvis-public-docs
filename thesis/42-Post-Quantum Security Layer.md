# 42. Post‑Quantum Signature and Verification Layer

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 42.1 Purpose and Gate‑Bound Scope

This chapter describes how Ms. Allis uses **post‑quantum judge signing and verification** to protect authority‑bearing verdicts as they cross the Blood–Brain Barrier (BBB), and how the **public answer path** is hardened at the database layer through `SECURITY DEFINER` function design and a pinned `search_path`.

Within this sealed gate, Chapter 42 may claim only that:

- judge verdicts are signed with **ML‑DSA‑65** at the verified runtime scope;
- corresponding **public keys** are available for verification;
- **tampered** or **unsigned** verdicts are rejected rather than silently accepted;
- the **BBB** delegates signature checking to a trusted verifier component;
- a bounded **Ed25519 fallback** exists and is used only where explicitly allowed and observed;
- the `runtime_governance.public_answer_packet` function implements **post-quantum-adjacent security hardening** through `SECURITY DEFINER` semantics and a pinned `search_path = public, runtime_governance, pg_temp`, confirmed as live on July 26, 2026.

It must **not** claim universal post‑quantum coverage, perfect cryptography across the entire stack, or future‑proof security against all quantum advances. The focus is on what is **implemented and tested**, not on ideal theory.

---

## 42.2 Why Post‑Quantum Judge Signing Matters

For rural developers, think of the judges as a panel whose written decisions control whether an action is allowed to move forward.

If anyone could forge those decisions, the rest of the safety architecture would not matter. This chapter therefore:

- treats judge verdicts as **authority‑bearing messages**;
- protects them with **ML‑DSA‑65** signatures so that an attacker, even with future quantum capabilities, cannot easily forge them;
- ensures that only verdicts with valid signatures can pass through the BBB into higher‑authority parts of the system.

The same principle — that **authority‑bearing paths must be hardened against injection and impersonation** — applies to the database-layer public answer path. The `public_answer_packet` function enforces this at the SQL level through `SECURITY DEFINER` and a pinned `search_path`, described fully in §42.10 below.

In plain language: *"The judges sign their work, and the system checks the signature before it trusts what they say. At the database layer, the public answer function runs under its own pinned authority so that no caller can redirect it to malicious objects."*

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

Other messages in the system may still use other schemes, but this chapter's claims are limited to the **judge verdict path**.

---

## 42.4 Public‑Key Availability at Runtime

A signature is only meaningful if verifiers can find the right **public key**.

Within this gate, Chapter 42 may claim that:

- the judge's ML‑DSA‑65 public key (or an equivalent verifying key) is made available to verification components at runtime;
- the BBB and its verifier can obtain this key through configuration or a small internal endpoint;
- the key identifier in each verdict matches one of the **known, live public keys**, allowing correct verification.

For rural operators, this means there is a concrete answer to:

- "Where does the BBB get the judge's public key?"
- "How does it know which key to use for a given verdict?"

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
   - returns "valid" or "invalid" (plus any diagnostic result).
4. The BBB uses this result to make gate decisions.

The key point is that **verification code is centralized and known to work**, and the BBB depends on it rather than re‑implementing cryptography in a fragile way.

---

## 42.6 Tamper and Unsigned Verdict Rejection

Within this gate, Chapter 42 may claim that the BBB enforces **strict rejection** of verdicts that do not verify:

- If the ML‑DSA‑65 signature check fails, the verdict is classified as **invalid / forged / unsigned**.
- Such verdicts are **not** allowed to grant promotion authority, regardless of their content.
- The failure is treated as a meaningful event to be logged and investigated, not as a warning that can be ignored.

For rural developers, you can think of the logic as:

- "No valid signature, no power."

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

## 42.8 Step‑by‑Step View for Rural Developers: Judge Signing Path

For someone running Ms. Allis in a rural setting, the judge signing path is this sequence:

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

If any step in this chain is broken — for example, if the verifier cannot load the key — the expected behavior is to **fail closed**, not to silently treat all verdicts as valid.

---

## 42.9 Step‑by‑Step View for Rural Developers: Public Answer Path Hardening

The `runtime_governance.public_answer_packet` function is the public-facing evidence surface of the database-layer governance cycle. It is the function that `public_instrument_role` calls to receive a structured `(where, when)` answer. Because it executes with access to admissible governed evidence and writes to `runtime_governance.public_answer_audit`, it is a security-sensitive path. Two database-level hardening measures, both confirmed live on July 26, 2026, protect it.

### Measure 1 — SECURITY DEFINER

The function is declared `SECURITY DEFINER`:

```sql
CREATE OR REPLACE FUNCTION runtime_governance.public_answer_packet(
    p_geoid      text,
    p_metric_name text
)
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public, runtime_governance, pg_temp
AS $$
-- function body
$$;
```

`SECURITY DEFINER` means the function executes with the privileges of the **function owner** — the `runtime_governance_role` — rather than the privileges of the **caller**. This is the same principle as the ML‑DSA‑65 judge signing path: authority is attached to the signed/defined artifact, not granted freely to the caller.

For rural developers, the practical effect is:

- `public_instrument_role` can call `public_answer_packet` and receive a governed answer.
- `public_instrument_role` cannot directly read `public.gbim_record`, cannot read internal `runtime_governance` tables beyond what is explicitly granted, and cannot write to `runtime_governance.public_answer_audit`.
- Yet the function itself can do all of those things — because it runs as the owner.

This is delegation with a locked door. The caller gets a governed result. The caller does not get the keys.

### Measure 2 — Pinned search_path = public, runtime_governance, pg_temp

The function declaration includes `SET search_path = public, runtime_governance, pg_temp`. This is the post-quantum-adjacent hardening measure.

In PostgreSQL, `search_path` controls which schemas are searched when an unqualified object name (a table name or function name without a schema prefix) is resolved. If `search_path` is not pinned, a caller with the ability to create objects in any schema that appears earlier in the search path could create a malicious substitute — for example, a `public.gbim_record` shadow table or a replacement `refresh_public_admissible_gbim_mv` function — and the `SECURITY DEFINER` function would silently resolve to the attacker's object instead of the legitimate one.

Pinning `search_path = public, runtime_governance, pg_temp` means:

- Only objects in `public`, `runtime_governance`, and the session-local `pg_temp` schema are resolved by unqualified names inside the function body.
- The `pg_temp` inclusion is intentional and standard: it allows temporary tables created during the session to be used, but temporary objects are session-scoped and cannot be pre-planted by an attacker across sessions.
- No other schema — including `pg_catalog` implicitly prepended in unpinned configurations — can be used to inject substitute objects.

For rural developers, the plain-language description is:

- Without a pinned `search_path`, a `SECURITY DEFINER` function is like a trusted official who reads whatever paper is placed on their desk. An attacker can swap the paper.
- With a pinned `search_path`, the official only reads papers from two specific locked filing cabinets (`public` and `runtime_governance`) and their own current session scratch pad (`pg_temp`). No substitution is possible from outside those cabinets.

This is called "post-quantum-adjacent" because it addresses the same threat model as post-quantum cryptography at a different layer: it prevents an attacker who has gained partial access to the environment from forging or substituting the authority-bearing objects the function relies on. The attack this prevents is not a quantum cryptographic attack — it is a SQL injection/schema confusion attack — but the defensive posture is structurally identical: the path from "caller invokes function" to "function produces governed answer" must be immune to substitution.

### Why Both Measures Are Required Together

`SECURITY DEFINER` without a pinned `search_path` is dangerous: it elevates caller privilege but leaves the function vulnerable to schema injection. A pinned `search_path` without `SECURITY DEFINER` is incomplete: it pins name resolution but does not prevent the caller from using their own elevated privileges to read directly from the tables the function reads.

Together, they enforce two independent properties:

| Property | Enforced by | Effect |
|---|---|---|
| Caller cannot exceed their granted privileges | `SECURITY DEFINER` + role boundary | `public_instrument_role` cannot read `gbim_record` directly |
| Function cannot be redirected to malicious objects | pinned `search_path` | No schema injection possible for unqualified object names inside the function body |

Both were confirmed live on July 26, 2026. The July 26 behavioral Test 4 (Public Reader Isolation, Chapter 41) validated the first property. The `SECURITY DEFINER` and `SET search_path` declarations are visible in the function definition and were verified as part of the July 26 session.

---

## 42.10 What This Chapter Does Not Claim

Staying within the sealed scope, Chapter 42 explicitly does **not** claim:

- that every internal or external message in Ms. Allis is post‑quantum protected;
- that all possible cryptographic attacks have been ruled out;
- that Ed25519 is safe against large‑scale quantum adversaries;
- that no configuration change could ever weaken the judge‑signing path;
- that `SECURITY DEFINER` and a pinned `search_path` are post-quantum cryptographic measures — they are database-level hardening measures that address injection and impersonation attacks at the SQL layer, and are described as "post-quantum-adjacent" because they share the same fail-closed, substitution-resistant defensive posture as the ML‑DSA‑65 judge signing path.

Instead, it makes the narrower claims that:

- judge verdicts at the verified runtime scope are **signed with ML‑DSA‑65**;
- the corresponding public keys are **available and used** for verification;
- the BBB **delegates** verification to a working component;
- **tampered or unsigned** verdicts are rejected;
- **Ed25519 fallback** exists only in clearly bounded, observed contexts;
- `runtime_governance.public_answer_packet` is declared `SECURITY DEFINER` with `search_path = public, runtime_governance, pg_temp`, confirmed live on July 26, 2026, hardening the public answer path against caller privilege escalation and schema injection.

---

## 42.11 Closing Statement

Chapter 42 anchors post‑quantum security directly to **who gets to speak with authority inside Ms. Allis**.

By requiring ML‑DSA‑65 signatures for judge verdicts, ensuring that the BBB delegates to a working verifier, rejecting tampered or unsigned decisions, and keeping Ed25519 as a small, explicit fallback, the system makes verdict authenticity a concrete, testable property instead of a wish.

At the database layer, the same principle is applied through the `SECURITY DEFINER` declaration and pinned `search_path = public, runtime_governance, pg_temp` on `runtime_governance.public_answer_packet`. These two implementation details, confirmed live on July 26, 2026, close the public answer path against the two most practical attack vectors at the SQL layer: a caller using the function's elevated privileges to read beyond their grant, and a schema-injection attack that would redirect the function to malicious substitute objects. Together with the ML‑DSA‑65 judge signing path, they form a coherent security posture across two layers of the architecture: the verdict authority path and the public evidence surface.

For rural developers, this chapter offers a step‑by‑step picture of how Ms. Allis protects two distinct authority paths — from "the judges decided" to "the system is allowed to act" at the application layer, and from "the caller asked a question" to "the system produced a governed answer" at the database layer — using implementation techniques that are documented, confirmed, and re-testable.

---

*Chapter 42 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
