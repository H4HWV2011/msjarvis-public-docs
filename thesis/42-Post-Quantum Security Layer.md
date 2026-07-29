# 42 — Post-Quantum Security Layer

*Carrie Kidd (Mamma Kidd) — Mount Hope, West Virginia*
*Last Updated: July 29, 2026*
*Status: Demonstrated — July 2026 Production Gate*

> **Gate Corrections Applied (July 29, 2026):**
> All references to `gbim_runtime_lifecycle_hourly()` are removed. The verified
> functional entry point for all four pg_cron governance lifecycle jobs is
> `apply_runtime_lifecycle()`. Four live jobs are confirmed active in `wv_gis`:
> hourly (`:15`), daily (`03:05`), weekly (Sunday `02:00`), monthly (1st `01:30`).

---

## What This Chapter Is About

This chapter explains how the public answer path in Ms. Jarvis is hardened at
the database function level — using Postgres security mechanisms that guard
against subtle misuse, including attacks that become more dangerous as
cryptographic assumptions weaken in a post-quantum world.

The central question for rural developers is:

> "When someone asks Ms. Jarvis a civic question about my community, how does
> the system make sure the answer comes from governed evidence and cannot be
> tricked, forged, or misdirected?"

The answer is **function-level discipline**: a hardened, auditable function path
that enforces authorization, pins its own search scope, restricts who can call
it, and logs every invocation.

**This chapter may claim:**

- `runtime_governance.public_answer_packet` is a `SECURITY DEFINER` function
  with pinned `search_path = public, runtime_governance, pg_temp`
- Execution is restricted to the `public_instrument_role` only
- The function uses governed views and audit tables — never raw internal tables
- Each invocation is logged in `runtime_governance.public_answer_audit`
- Overflow handling follows the same hardening philosophy: minimized payloads,
  bounded queues, governed paths
- The four pg_cron lifecycle jobs run via `apply_runtime_lifecycle()` and provide
  an independent governance pulse at the database level

**This chapter must not claim:**

- That this layer replaces cryptographic post-quantum algorithms
- Universal security guarantees beyond the specific function-level mechanisms
- Clinical, legal, or platform-wide security certifications

---

## 42.1 The Public Answer Path in Plain Terms

The public answer path is the route by which a civic question — "How many
weather stations are in this blockgroup?" — turns into a structured answer
backed by governed evidence.

Inside the database, the central piece of this path is:

```
runtime_governance.public_answer_packet(p_geoid text, p_metric_name text)
```

When the public instrument calls this function, it expects:

- An answer packet stating whether the system has **seen**, **inferred**, or
  has **no admissible evidence** for the requested geographic unit and metric
- Admissibility rules and evidence selection enforced inside the function
- No direct access to raw internal tables — all evidence is pre-filtered

The Post-Quantum Security Layer described in this chapter ensures that function
behaves correctly and safely regardless of who calls it or in what context.

The July 26, 2026 gate confirmed this function returned its first live structured
civic answer for geoid `540019656003`, metric `atm_weather_stations_count`,
under `public_instrument_role`. It emitted a `seen` answer with full provenance
— or it would have refused entirely.

---

## 42.2 SECURITY DEFINER: The Trusted Clerk Model

### What It Does

In Postgres, a function marked `SECURITY DEFINER` runs with the privileges of
its **owner**, not the privileges of the **caller**.

For `public_answer_packet`, this means:

- The function can read from governed views and tables that the calling role
  cannot see directly
- The function can perform operations that would normally require higher
  privileges
- The function packages governed evidence into a safe answer packet without
  exposing raw internals to the caller

For rural developers: think of this as a trusted clerk behind a counter. The
caller (the public instrument) can ask a question. The clerk (the function) is
allowed to go into the back room and retrieve the right records. The caller
never gets direct access to the back room. Only the clerk does, and the clerk
only brings back what the governance rules permit.

### Why It Is Used Here

Using `SECURITY DEFINER` on `public_answer_packet` is a deliberate architectural
choice:

- Admissibility logic lives in exactly one place — inside the function
- The public instrument role can call the function without needing broad read
  access to internal schemas
- The function is the only sanctioned path by which raw governed evidence is
  transformed into a public answer

This reduces the attack surface. Instead of many scripts duplicating logic in
different ways, one hardened function carries the sole responsibility.

---

## 42.3 Pinning the search_path

### What search_path Is

In Postgres, `search_path` is the ordered list of schemas the database searches
when a query references an object without specifying its schema. By default,
temporary tables live in a schema that can silently appear first in that list.

If a function is not careful, an attacker or misconfiguration could cause it to
read or write a temporary table with the same name as a governed view — instead
of the real governed object. This is a subtle but real class of database attack.

### How It Is Pinned for public_answer_packet

The function is defined with:

```sql
SET search_path = public, runtime_governance, pg_temp
```

This ordering does three things:

1. `public` — where admissible views live — is the first search target
2. `runtime_governance` — where audit tables and helper functions live — is
   second
3. `pg_temp` — the temporary schema — is present but **last**, not first,
   preventing temporary objects from masking governed ones

### Why This Matters for Rural Developers

Without this pinning, a caller with permission to create temporary tables could:

- Create a temp table named `public_admissible_gbim_mv`
- Trick the function into reading from that temp table instead of the real
  governed materialized view
- Receive a fabricated answer that looks legitimate

With `pg_temp` pinned to the end of the search path, this cannot happen. The
function will always find the real governed object first.

---

## 42.4 Execution Restrictions: Only the Right Role Can Call It

After the function is defined, its execution permissions are tightened through
two steps:

**Step 1 — Revoke from PUBLIC:**

```sql
REVOKE ALL ON FUNCTION runtime_governance.public_answer_packet
FROM PUBLIC;
```

This removes the default assumption that any authenticated user can call the
function.

**Step 2 — Grant only to public_instrument_role:**

```sql
GRANT EXECUTE ON FUNCTION runtime_governance.public_answer_packet
TO public_instrument_role;
```

Only the public instrument — a role designed to operate within specific civic
bounds — can invoke this function. No other role, no general user, no internal
admin process calling from outside the governed pathway has execution rights.

For rural developers, this is the equivalent of a county courthouse where only
the clerk of court can stamp and issue official records. Anyone can submit a
request. Only the authorised clerk can produce the official document.

---

## 42.5 Governed Views, Not Raw Tables

Inside `public_answer_packet`, evidence is drawn exclusively from governed
views — specifically `public.public_admissible_gbim_mv`, the ten-condition
admissibility materialized view that is refreshed by the hourly
`apply_runtime_lifecycle()` pg_cron job.

Raw tables holding stored state are not directly exposed to callers. This means:

- The function operates on already-filtered evidence surfaces
- A record that failed the admissibility predicate at ingestion time cannot
  appear in a public answer
- There is no code path inside the function that bypasses the admissibility gate

The admissibility predicate enforces ten conditions on every row before it
enters the view. The function then draws only from that pre-filtered surface.
This is two layers of filtering: the view enforces what is admissible, and the
function enforces how admissible evidence becomes a public answer.

---

## 42.6 The Audit Trail: Every Call Is Logged

Every invocation of `public_answer_packet` writes an entry to
`runtime_governance.public_answer_audit`. The entry records:

- The requested `geoid` and `metric_name`
- The answer label returned: `seen`, `inferred`, or `inadmissible`
- The timestamp when the answer was generated (`generated_at`)
- The evidence IDs that supported the answer, if any

For rural developers, this is the logbook. If a community steward or outside
reviewer asks "what did the system say about this blockgroup on this date, and
what evidence was it using?", the audit table provides the answer.

The audit trail is not optional and not bypassable — it is written inside the
`SECURITY DEFINER` function before the answer packet is returned. The caller
cannot suppress it.

---

## 42.7 The pg_cron Governance Lifecycle Pulse

The post-quantum security layer does not operate in isolation. It depends on the
governance lifecycle being kept current. This is done by the four pg_cron jobs
registered in `wv_gis`, all running via the verified entry point
`apply_runtime_lifecycle()`.

| Schedule | What It Does |
|----------|-------------|
| Every hour at `:15` | Refreshes `public_admissible_gbim_mv` — keeps the evidence surface current |
| Daily at `03:05` | Runs degradation status updates — advances `fresh` → `aging` → `stale` |
| Sunday at `02:00` | Deeper coherence check across the governed corpus |
| 1st of month at `01:30` | Full lifecycle reconciliation; archives stale audit records |

> **Deprecation notice:** The function `gbim_runtime_lifecycle_hourly()` no
> longer exists. Any configuration, documentation, or code referencing that
> name must be updated to use `apply_runtime_lifecycle()` as the entry point.

To verify all four jobs are live:

```sql
SELECT jobname, schedule, command, active
FROM cron.job
WHERE jobname LIKE 'gbim-runtime-lifecycle-%'
ORDER BY jobname;
```

If the hourly job is not running, `public_admissible_gbim_mv` will go stale and
`public_answer_packet` will operate on outdated evidence. The audit trail will
still record calls — but the evidence surface feeding them will not be fresh.
Keeping the pg_cron jobs active is therefore a direct security concern, not just
an operational one.

---

## 42.8 Overflow Handling: The Same Philosophy

The same hardening discipline that governs `public_answer_packet` applies to
overflow event handling.

Overflow events (such as those in the
`overflow:queue:overflow_retriable_public_context` lane) are constructed as
**minimized records**:

- Only allowlisted public-context fields are included
- Person-space validation ensures the event is safe to route
- Queue behavior is bounded — no uncontrolled growth

These events are handled by functions that follow the same principles:
- Operate on minimized, governed payloads
- Use privileged, tightly scoped functions
- Pin search paths
- Restrict execution to the intended role
- Log behavior for review

For rural developers: overflow is not an escape hatch. An event that overflows
the primary path does not bypass the security layer — it enters a governed
secondary lane that applies the same rules.

---

## 42.9 Why This Is Post-Quantum Security

"Post-quantum security" typically refers to cryptographic algorithms that remain
safe against quantum computers. This chapter focuses on **structural hardening**,
which is the complement to cryptography — not a replacement for it.

If a future attacker breaks or weakens an encryption layer, the system still
benefits from:

- Narrow roles and permissions that cannot be escalated by decryption alone
- Hardened function paths that refuse to read wrong tables regardless of who
  calls them
- Clear boundaries between stored state and public evidence that encryption
  alone cannot enforce
- Audit trails that record behavior even if network-layer security is compromised

For rural developers, the practical lesson is: good security is not only
mathematics. It is disciplined architecture. The structural protections in this
chapter remain effective as cryptographic methods evolve, because they are
enforced at the database level — below the application layer and independent of
which encryption algorithm is in use.

---

## 42.10 Step-by-Step Summary for Rural Developers

1. **Identify the hardened function.**
   `runtime_governance.public_answer_packet` is the single governed path from
   civic questions to structured answers. It is the only function that may
   produce public answer packets.

2. **Understand SECURITY DEFINER.**
   The function runs with owner privileges. The caller cannot see the back room.
   Only the function can, and it only brings back what governance permits.

3. **Understand search_path pinning.**
   `SET search_path = public, runtime_governance, pg_temp` ensures the function
   always finds the real governed objects — never a temporary masking table.
   `pg_temp` is present but last.

4. **Know the execution restriction.**
   Only `public_instrument_role` can call the function. All other execution
   rights are revoked. No workaround, no shortcut.

5. **Know the evidence source.**
   The function reads from `public.public_admissible_gbim_mv` only. Raw tables
   are not accessible. Evidence has already passed the ten-condition
   admissibility predicate before the function sees it.

6. **Check the audit table.**
   `runtime_governance.public_answer_audit` records every call. Query it to
   confirm the function is being used as intended and to audit what the system
   said about any given blockgroup.

7. **Keep the pg_cron jobs active.**
   All four jobs run via `apply_runtime_lifecycle()`. The deprecated
   `gbim_runtime_lifecycle_hourly()` no longer exists. If the hourly job stops,
   the evidence surface goes stale. Verify with:

   ```sql
   SELECT jobname, schedule, active
   FROM cron.job
   WHERE jobname LIKE 'gbim-runtime-lifecycle-%';
   ```

8. **Apply the same philosophy to overflow.**
   Overflow paths use minimized payloads, bounded queues, and governed function
   paths. Overflow is not an escape from the security layer.

9. **Understand the structural-plus-cryptographic model.**
   Structural hardening (this chapter) and cryptographic algorithms work
   together. Structural protections remain effective even as cryptographic
   assumptions evolve. They are enforced at the database level, independent of
   the application or network layer.

---

## 42.11 What This Chapter Does Not Claim

To remain within the gate:

- This chapter does not claim that function-level hardening replaces
  post-quantum cryptographic algorithms
- It does not claim universal security against all possible attacks
- It does not claim clinical, legal, or platform-wide security certification
- It claims only that `public_answer_packet` is hardened by demonstrated
  database mechanisms, and that those mechanisms are live and auditable
  as of the July 2026 production gate

---

## 42.12 Closing Statement

The Post-Quantum Security Layer in this chapter is function-level discipline
made concrete.

`SECURITY DEFINER` ensures the function runs under the right privileges.
A pinned `search_path` ensures it never reads the wrong objects. Execution
restrictions ensure only the intended role can invoke it. Governed views ensure
it operates on pre-filtered evidence. An audit trail ensures every call is
recorded. The four pg_cron jobs keep the evidence surface fresh via
`apply_runtime_lifecycle()`.

For rural developers in Mount Hope and across Appalachia, the practical
consequence is this: the civic answers your community receives from this system
come through a hardened, auditable path. It cannot be tricked into reading
fabricated data. It cannot be called by unauthorised roles. It records what it
said and why. That is structural security — and it is live.

---

*Chapter 42 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
*Sealed: July 29, 2026 — July 2026 Production Gate.*
*`public_answer_packet`: live, SECURITY DEFINER, pinned search_path, restricted*
*to `public_instrument_role`, audit-logged.*
*pg_cron entry point: `apply_runtime_lifecycle()` — four live jobs in `wv_gis`.*
*Deprecated: `gbim_runtime_lifecycle_hourly()` — remove all references.*
