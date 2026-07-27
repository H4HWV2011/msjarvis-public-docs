# 42 — Post-Quantum Security Layer

*Carrie Kidd (Mamma Kidd) — Mount Hope, West Virginia*  
*Last Updated: July 27, 2026*

---

## 42.1 Purpose of This Layer

This chapter explains how the public answer path in Ms. Jarvis is hardened at the database function level, using Postgres features that help protect against subtle attacks — including those that could become more important in a post-quantum world.

Instead of focusing on encryption algorithms, this chapter focuses on **authorization discipline**: the way the system ensures that only governed evidence enters public answers, and that even privileged functions cannot be tricked into reading or writing the wrong tables.

For rural developers, this chapter translates those ideas into a step-by-step explanation of how one function, `runtime_governance.public_answer_packet`, is secured.

---

## 42.2 The Public Answer Path in Plain Terms

The **public answer path** is the route by which a civic question, such as “How many weather stations are in this blockgroup?” turns into a structured answer backed by governed evidence.

Inside the database, the central piece of this path is the function:

```text
runtime_governance.public_answer_packet(p_geoid text, p_metric_name text)
```

When the public instrument calls this function, it expects:

- To receive an answer packet that states whether it has **seen**, **inferred**, or has **no admissible evidence** for the requested geoid and metric.
- To rely on the function to enforce admissibility rules and evidence selection.
- To avoid direct access to raw internal tables.

The Post-Quantum Security Layer described in this chapter ensures that this function behaves correctly, safely, and consistently, even when called by different roles or in different contexts.

---

## 42.3 SECURITY DEFINER — What It Is and Why It Matters

### 42.3.1 What SECURITY DEFINER Does

In Postgres, a function marked with `SECURITY DEFINER` runs with the privileges of its owner, not the privileges of the caller.

For `runtime_governance.public_answer_packet`, this means:

- The function can read from governed views and tables that the calling role cannot see directly.
- The function can perform operations that would normally require higher privileges.
- The function can package governed evidence into a safe answer packet without exposing raw internals.

In everyday terms, the function acts like a trusted clerk inside the system. Rural developers can think of it as a person behind the counter who is allowed to look in the back room but only brings the right items to the front.

### 42.3.2 Why SECURITY DEFINER Is Used Here

Using `SECURITY DEFINER` on `public_answer_packet` is a deliberate choice:

- It keeps admissibility logic in one place, inside the function.
- It lets the public instrument role call the function without needing broad read access.
- It ensures that the function is the only path by which raw governed evidence is transformed into a public answer.

This reduces the number of places where mistakes or attacks could slip through. Instead of many scripts duplicating logic, one hardened function carries the responsibility.

---

## 42.4 Pinning the search_path — public, runtime_governance, pg_temp

### 42.4.1 What search_path Is

In Postgres, `search_path` is the ordered list of schemas the system searches when a function references a table or view without specifying a schema name.

By default, temporary tables live in a schema that can be first in the search path. If a function is not careful, it might accidentally read or write a temporary table that a caller has created, instead of the intended table in a governed schema.

### 42.4.2 How search_path Is Pinned for public_answer_packet

To prevent that, `public_answer_packet` is defined with a pinned search path:

```text
SET search_path = public, runtime_governance, pg_temp
```

This ordering does three things:

- Ensures that references to objects in `public` and `runtime_governance` resolve as intended.
- Puts `pg_temp` at the end of the search path rather than at the front.
- Makes it explicit which schemas the function is allowed to search.

### 42.4.3 Why This Hardening Matters

Pinning the search path protects against a subtle class of attacks:

- A caller with permission to create temporary tables could create a table with the same name as a governed view.
- If `pg_temp` were implicitly at the front of the search path, the function might read from that temporary table instead of the real governed view.
- By placing `pg_temp` at the end and naming the intended schemas, the function avoids this confusion.

For rural developers, this means that the function is not easily tricked into reading or writing the wrong data. It consistently uses the intended governed objects.

---

## 42.5 How the Function Is Hardened Step-by-Step

This section explains the security measures around `public_answer_packet` in clear order.

### Step 1 — Define the Function with SECURITY DEFINER

The function is created with:

- `SECURITY DEFINER` — runs with the owner’s rights.
- A carefully chosen owner — typically a governance role, not a general user.

This ensures the function can access governed evidence while the caller cannot.

### Step 2 — Pin search_path to Known Schemas

The function’s definition includes:

```text
SET search_path = public, runtime_governance, pg_temp
```

This ensures:

- `public` — the schema where admissible views live — is used reliably.
- `runtime_governance` — the schema where audit tables and helper functions live — is available.
- `pg_temp` — the temporary schema — is present but not first, preventing accidental or malicious masking.

### Step 3 — Restrict Execution to the Intended Role

After defining the function, its execution permissions are tightened:

- All default execution rights are revoked from `PUBLIC`.
- Execution is granted only to the intended public instrument role.

This way, not just anyone can call the function. Only the public instrument, which has been designed to operate within specific bounds, can use it.

### Step 4 — Use Governed Views Instead of Raw Tables

Inside the function:

- Evidence is drawn from governed views like the admissible materialized view.
- Raw tables holding stored state are not directly exposed to callers.

This keeps the function aligned with the broader governance rules. It acts only on already-filtered evidence surfaces.

### Step 5 — Log Each Invocation in an Audit Table

The function writes an entry to an audit table in the `runtime_governance` schema whenever it is called.

This records:

- The requested geoid and metric.
- The type of answer returned (`seen`, `inferred`, or `inadmissible`).
- When the answer was generated.

For rural developers, this is the equivalent of keeping a logbook of who asked what and what the system answered.

---

## 42.6 Relation to Overflow and Bounded Events

The same function-level discipline that hardens `public_answer_packet` applies to overflow handling.

### 42.6.1 Overflow Events and Minimal Payloads

Overflow events, such as those in the `overflow:queue:overflow_retriable_public_context` lane, are constructed as minimized records:

- Only allowlisted public-context fields are included.
- Person-space validation ensures the event is safe to route.
- Queue behavior is bounded, preventing uncontrolled growth.

These events are handled by scripts and functions that follow similar principles: they operate on minimized payloads and governed queues, not on arbitrary raw state.

### 42.6.2 Shared Hardening Philosophy

The shared philosophy is:

- Use privileged functions that are tightly scoped and configured.
- Pin their search paths so they cannot be tricked by temporary objects.
- Restrict their execution to roles that are designed for their specific job.
- Log their behavior for later review.

By treating overflow routing and public answering as governed function paths rather than open queries, the system reduces exposure to both conventional and future threats, including those that may arise in post-quantum scenarios.

---

## 42.7 Why This Matters in a Post-Quantum Context

Post-quantum security usually focuses on cryptographic algorithms resistant to quantum attacks. This chapter focuses on **structural hardening**, which complements cryptography.

If a future attacker can break or weaken encryption, the system still benefits from:

- Narrow roles and permissions.
- Hardened function paths that refuse to operate on unexpected tables or views.
- Clear boundaries between stored state and public evidence.

For rural developers, the lesson is that good security is not just about math; it is also about clear, disciplined architecture. Even as cryptographic methods evolve, these structural protections remain valuable.

---

## 42.8 Implementation Status

**Post-Quantum Security Layer (function-level hardening of public answers): Demonstrated for `public_answer_packet`.**

As of July 27, 2026:

- `runtime_governance.public_answer_packet` is defined as a `SECURITY DEFINER` function with a pinned `search_path = public, runtime_governance, pg_temp`.
- Its execution is restricted to the public instrument role.
- It uses governed views and audit tables to transform admissible evidence into structured answer packets.
- Its hardening shows how overflow and answer paths are protected at the function level, not just at the application or network level.

Within the academic scope of this chapter, the thesis is justified in claiming that the public answer path is hardened by design, using concrete database mechanisms that guard against subtle misuse.

---

## 42.9 Step-by-Step Summary for Rural Developers

To understand and apply this chapter:

1. **Recognize the critical function.**  
   `public_answer_packet` is the main path from questions to governed answers.

2. **Understand SECURITY DEFINER.**  
   The function runs with owner privileges, allowing it to access governed evidence without exposing raw data.

3. **See why search_path is pinned.**  
   Pinning `search_path` prevents temporary tables from tricking the function into using the wrong objects.

4. **Note the execution restrictions.**  
   Only the public instrument role can call the function. Others cannot.

5. **Appreciate the audit trail.**  
   Each call is logged, making the function’s behavior reviewable.

6. **Connect the pattern to overflow.**  
   Overflow handling uses the same idea: privileged, bounded functions and queues rather than open, unguarded paths.

---

## 42.10 Closing

The Post-Quantum Security Layer in this chapter is not about a specific encryption algorithm. It is about **function-level discipline**: using `SECURITY DEFINER`, pinned search paths, restricted execution roles, and governed evidence surfaces to keep public answers safe.

For rural developers, this means that public-facing behavior is not left to chance. It is routed through hardened, auditable functions that respect the system’s governance rules, now and as security expectations evolve.
