# 43 — Role-Gated Knowledge Access

*Carrie Kidd (Mamma Kidd) — Mount Hope, West Virginia*  
*Last Updated: July 27, 2026*

---

## 43.1 Purpose of Role-Gated Access

This chapter describes the **three-tier role model** that governs who can see what inside Ms. Jarvis’s knowledge system.

Instead of letting any part of the system read any table, the architecture uses:

- A **superuser** for maintenance and emergency work.
- A **runtime governance role** for internal lifecycle and admissibility work.
- A **public instrument role** for serving governed answers and overflow events.

For rural developers, this is the chapter that explains why some queries succeed and others fail, and why that is intentional rather than a bug.

---

## 43.2 The Three-Tier Role Model

The three roles are:

1. `postgres` superuser.
2. `runtime_governance_role`.
3. `public_instrument_role`.

Each role has a specific job and specific permissions. Together, they ensure that:

- Full access is rare and carefully handled.
- Governance operations see everything they need but do not speak directly to the public.
- Public-facing tools see only filtered, admissible evidence and audit logs.

---

## 43.3 Tier One — postgres Superuser

### 43.3.1 Responsibilities

The `postgres` superuser is the top-level database administrator. This role:

- Manages schema changes and migrations.
- Creates and alters roles and permissions.
- Installs or updates functions, views, and policies.

In practice, this role is used sparingly. It exists primarily for maintenance and emergency operations, not for everyday queries.

### 43.3.2 Access Level

The superuser:

- Can bypass row-level security and see all tables.
- Can modify governed tables and views.
- Can create or drop policies and constraints.

Because this role is powerful, it is not used by application code. Rural developers should treat it like the key to the whole building: necessary, but not something to hand out freely.

---

## 43.4 Tier Two — runtime_governance_role

### 43.4.1 Responsibilities

The `runtime_governance_role` is responsible for **internal governance operations**. This includes:

- Running lifecycle refresh functions.
- Maintaining admissible views.
- Logging audit entries.
- Performing test harness operations.

This role is where runtime governance lives. It sees both stored and admissible state in order to make decisions about what becomes speakable.

### 43.4.2 Access Level

The `runtime_governance_role` has:

- Full access to `public.gbim_record` — the stored governed table.
- A row-level security policy (`USING (true)`) that allows it to see all rows.
- Permission to read and write governance tables in `runtime_governance`.
- Permission to call governance functions that affect lifecycle and admissibility.

In effect, `runtime_governance_role` is the internal caretaker of governed state. It must see everything to decide what becomes admissible, but it does not speak directly to the public.

For rural developers, this role is like the worker who can enter the storage rooms, rearrange shelves, and update stock, but cannot directly run the front desk.

---

## 43.5 Tier Three — public_instrument_role

### 43.5.1 Responsibilities

The `public_instrument_role` is the role that backs the public-facing tools and services. This role:

- Calls `public_answer_packet` to serve structured answers.
- Reads from admissible views and audit logs.
- Interacts with overflow queues and other public-context surfaces.

It is the “voice” of the system to the outside world, but its vision is deliberately limited.

### 43.5.2 Access Level

The `public_instrument_role` has:

- **Read-only access** to the admissible materialized view, such as `public.public_admissible_gbim_mv`.
- **Read-only access** to governance audit tables, such as `runtime_governance.public_answer_audit`.
- Permission to execute hardened functions like `runtime_governance.public_answer_packet`.
- **No access** to `public.gbim_record` — attempts to select from this raw table result in a permission error.

This means that the public instrument can only see what has been declared admissible or logged. It cannot browse raw governed state.

For rural developers, this role is like the front desk clerk: able to see the catalog and records of what has been handed out, but unable to walk into the back room without permission.

---

## 43.6 How Row-Level Security Fits In

### 43.6.1 Row-Level Security on gbim_record

Row-level security (RLS) is enabled on `public.gbim_record`. The policy for `runtime_governance_role` is:

```text
USING (true)
```

This means:

- For this role, all rows are visible.
- Other roles must abide by different policies or have no access at all.

Row-level security ensures that:

- Even if a table is technically accessible, the role’s view of its rows is filtered.
- Policies can be tightened or adjusted over time without rewriting all application logic.

### 43.6.2 Why RLS Matters Here

RLS provides fine-grained control over which roles can see which rows. In this architecture:

- `runtime_governance_role` sees all rows in `gbim_record` because it must manage lifecycle and admissibility.
- `public_instrument_role` does not see `gbim_record` at all; it relies on admissible views instead.

This distinction is central to role-gated knowledge access. It prevents the public instrument from bypassing governance rules by querying internal tables directly.

---

## 43.7 Overflow and Person-Space in Context of Roles

Overflow enforcement and person-space promotion are meaningful only when viewed through these roles.

### 43.7.1 Person-Space Promotion

Person-space promotion — moving a cognition packet into a committed person-space event — is managed by governance scripts and functions that run as `runtime_governance_role`.

This role:

- Evaluates readiness and validation.
- Ensures that person-space events are constructed properly.
- Logs decisions for later review.

It does not expose raw person-space events directly to the public. Instead, it prepares minimized events and passes them into controlled lanes.

### 43.7.2 Overflow Enforcement

Overflow enforcement — sending events to queues like:

```text
overflow:queue:overflow_retriable_public_context
```

is also carried out under governance roles and functions.

The overflow path:

- Checks person-space validation.
- Minimizes event payloads to public-context fields.
- Enqueues events into bounded queues.

From the public instrument’s perspective, overflow is visible only through:

- High-level functions and APIs.
- Admissible views and audit logs.

The public instrument does not directly manipulate overflow queues at the raw record level. Governance roles handle the details.

---

## 43.8 Why Role-Gated Access Is Necessary

Role-gated knowledge access is not just a design choice; it is a necessity for:

- **Privacy** — preventing raw person-space records from being visible to public tools.
- **Governance** — ensuring that lifecycle decisions are made by the right role.
- **Security** — limiting the blast radius of potential mistakes or attacks.

Without this three-tier model:

- Any part of the system could query `gbim_record` directly.
- Admissibility rules might be bypassed.
- Overflow and person-space handling could become leaky.

For rural developers, role-gated access is the difference between a system where everything is readable by anyone who finds a connection string, and a system where responsibilities are divided and enforced.

---

## 43.9 Implementation Status

**Role-Gated Knowledge Access: Demonstrated.**

As of July 27, 2026:

- The three-tier role model is in place:

  - `postgres` superuser for maintenance.
  - `runtime_governance_role` with full `gbim_record` access and row-level policy `USING (true)`.
  - `public_instrument_role` with read-only access to `public_admissible_gbim_mv` and `runtime_governance.public_answer_audit`.

- Attempts by `public_instrument_role` to read `public.gbim_record` result in permission errors, confirming the non-surveillance boundary.
- Governance functions and overflow scripts run under appropriate roles, enforcing promotion, validation, and minimization.

Within the academic scope of this chapter, the architecture’s claims about role-gated knowledge access are supported by concrete role definitions and observed behavior.

---

## 43.10 Step-by-Step Summary for Rural Developers

To use or reason about role-gated access:

1. **Know the three roles.**  
   `postgres`, `runtime_governance_role`, and `public_instrument_role` each have a distinct job.

2. **Understand what each role can do.**  
   Superuser can see everything; runtime governance can see and manage internal state; public instrument can only see admissible evidence and audit logs.

3. **Remember row-level security.**  
   RLS policies ensure that even inside the same table, different roles see different sets of rows.

4. **Connect roles to overflow and person-space.**  
   Governance roles handle promotion and overflow. Public roles only see the results.

5. **Use errors as guides.**  
   If a query fails with permission denied, that is often a sign that the role-gated boundaries are doing their job.

6. **Stay within scope.**  
   This chapter does not claim to describe every possible role. It documents the three-tier model that matters most for governed knowledge access and overflow behavior.

---

## 43.11 Closing

Role-gated knowledge access is the backbone of Ms. Jarvis’s privacy and governance story. By clearly defining what `postgres`, `runtime_governance_role`, and `public_instrument_role` can and cannot do, the system keeps sensitive state behind appropriate gates and exposes only governed, admissible evidence to the public.

For rural developers, this chapter provides the map: who has the keys to which rooms, what each room contains, and how the doors are kept locked or open as needed. That map is essential for both building and trusting the system.
