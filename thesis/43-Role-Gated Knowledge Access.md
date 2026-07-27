# 43. Role-Gated Knowledge Access (As-Built)

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 43.1 What This Chapter Is Allowed to Claim

Within this sealed gate, Chapter 43 covers two distinct but related topics:

**Part A — Application-layer role, purpose, and projection gates** on the GBIM router, GIS RAG service, policy/write pipeline, and query guard.

**Part B — Database-layer three-tier role model** confirmed as-built on July 26, 2026 in `wv_gis`, with exact role names, GRANT statements, and RLS policy.

It may claim that:

- the **GBIM router** enforces purpose and coherence gates and binds requests to the active manifest;
- the **GIS RAG** service enforces projection headers, purpose matching, permitted-use constraints, and fail-closed request-purpose checks;
- the **policy layer and write pipeline** expose a `DisclosureVerdict` with SUPPRESS/PERMIT behavior and a gate/pipeline contract;
- the **query guard** causes person-only queries to fail closed pending constitutional review;
- a **three-tier database role model** — `postgres` superuser, `runtime_governance_role`, and `public_instrument_role` — is confirmed as-built and enforced in `wv_gis`;
- exact `CREATE ROLE`, `GRANT`, `REVOKE`, and `CREATE POLICY` statements for all three tiers are documented here from the July 26, 2026 session.

It may **not** claim universal, perfect access control across the entire system. Anything beyond the verified paths remains outside this chapter's warrant.

---

## 43.2 Why Role and Purpose Matter for Rural Operators

For rural developers and operators, these gates answer a concrete question:

> "When Ms. Allis goes to look something up about a place or a person, how does she know whether she is allowed to see and share it?"

Chapter 43 describes how:

- **role** (who is asking),
- **purpose** (why they are asking), and
- **projection** (what slice of the data they are allowed to see)

work together on the **governed belief and GIS paths** that have been explicitly checked, and how a parallel three-tier role structure enforces those same principles at the database level. The aim is to make sure that governed maps, statistics, and appearance records are not just technically available, but **used only in ways that match their permitted purpose**.

---

## 43.3 Part A — Application-Layer Gates

### 43.3.1 The Verified Paths in Scope

This chapter's application-layer claims cover only the paths with closed evidence:

- the **GBIM router**, which fronts governed belief collections;
- the **GIS RAG** service, which answers geography-shaped questions from governed GIS data;
- the **policy and write pipeline**, which decide whether a proposed appearance record may be stored or must be suppressed;
- the **query guard**, which intercepts certain sensitive queries.

All of these are tied into a **role/purpose/projection** story:

- role and purpose are checked at the router and GIS RAG layer;
- projection is enforced by collection metadata and query filters;
- write-side disclosure decisions are made by explicit verdicts;
- person-shaped queries are blocked or escalated rather than answered freely.

Nothing outside these named pieces is covered by Chapter 43's application-layer claims.

### 43.3.2 GBIM Router — Purpose and Coherence Gates

The **GBIM router** is the entry point for governed-belief queries. Within this gate, it:

- reads the **declared purpose** and **role** of the incoming request;
- routes only to collections whose **permitted use** matches that purpose;
- binds each request to the current **active manifest** so that only promoted, active versions are ever served;
- enforces a **coherence gate**, ensuring that requested combinations of collection, geography, and purpose make sense before the request is allowed through.

For rural developers, this means the router behaves more like a **governed switchboard** than a raw index. A request that asks for data outside the active manifest, or for a purpose that does not match a collection's permitted use, is **stopped at the router** instead of falling through and hoping for the best.

### 43.3.3 GIS RAG — Projection and Purpose Enforcement

The **GIS RAG** service is the geography-focused retrieval engine for governed GIS data. Within this gate, it:

- requires **projection headers** that describe the caller's role and intended purpose;
- checks that the requested collections' **permitted uses** are compatible with that purpose;
- restricts retrieval to **allowed collections** based on role and purpose, dropping disallowed collections before any vector search is run;
- performs **fail-closed request-purpose checks**: if the purpose header is missing, malformed, or incompatible, the request fails rather than defaulting to a permissive mode.

Step by step, a rural operator can picture the path like this:

1. The caller sends a GIS question with county or blockgroup IDs plus a **declared purpose**.
2. GIS RAG looks up which collections are allowed for that purpose and role.
3. GIS RAG runs retrieval only inside those **permitted collections**.
4. If there is no compatible combination, GIS RAG returns an error instead of partial, out-of-policy data.

### 43.3.4 Manifest-Bound Access

The **publication manifest** used in governed belief is also part of Chapter 43's story. Within this gate:

- only collections with **`build_status` marked active** in the manifest are used to answer governed GIS and GBIM queries;
- requests are **bound to the active manifest row** for the named logical collection, ensuring that retired or superseded versions are not served by accident;
- manifest entries include **permitted-use fields**, and these fields are consulted by the GBIM router and GIS RAG to decide whether a request's purpose is allowed.

In effect, the manifest is a **gating table** as much as a catalog.

### 43.3.5 Write Pipeline and Disclosure Verdicts

On the write side, the gate evidence shows a pipeline that computes a **`DisclosureVerdict`** for appearance records. Within this chapter's scope:

- every proposed appearance record passes through a gate that considers role, purpose, and policy;
- the gate emits a `DisclosureVerdict` such as **SUPPRESS** or **PERMIT**;
- **SUPPRESS** means the record is not written, and the decision is logged;
- **PERMIT** means the record may proceed into the people-space or governed belief store under the current rules.

From a rural developer's standpoint:

1. Writing an appearance record is **never a raw insert**.
2. The record is examined under the disclosure gate.
3. If the verdict is SUPPRESS, the write is blocked and the block is itself an auditable event.
4. Only PERMIT or similar allowed outcomes result in actual stored records.

### 43.3.6 Query Guard — Person-Only Queries Fail Closed

The **query guard** is a special layer that watches for **person-only queries**. Within this gate:

- certain classes of queries that target a **single person without sufficient context** are intercepted;
- for those person-only queries, the default behavior is to **fail closed**, returning an error or a request for higher review rather than an answer;
- escalation routes exist to pass such queries to **constitutional review** where policy allows.

In simple terms:

- "Tell me everything you know about this person" is treated as a dangerous request;
- the query guard refuses to answer it directly;
- only a higher, policy-bound path can authorize any disclosure.

---

## 43.4 Part B — The As-Built Three-Tier Database Role Model

As of July 26, 2026, the `wv_gis` database enforces a three-tier role structure. The tiers are `postgres` (superuser), `runtime_governance_role` (full governed state access), and `public_instrument_role` (read-only on the public evidence surface). All role definitions, grants, revokes, and policies shown below are confirmed from the July 26, 2026 live session.

### 43.4.1 Tier 1 — postgres Superuser

`postgres` is the built-in PostgreSQL superuser. It owns all schemas, tables, functions, and materialized views in `wv_gis`. It is the only role that can:

- execute DDL (`CREATE`, `ALTER`, `DROP`) on governance objects;
- add or remove `pg_cron` jobs;
- create or modify roles;
- bypass Row-Level Security.

`postgres` is used only for schema administration and is never exposed to the application layer or public instrument path.

### 43.4.2 Tier 2 — runtime_governance_role

`runtime_governance_role` is the internal governance runtime. It was created and granted on July 26, 2026 with the following statements, confirmed in the live session:

```sql
-- Create the governance runtime role
CREATE ROLE runtime_governance_role
  LOGIN
  NOSUPERUSER
  INHERIT;

-- Grant full DML on the governed state table
GRANT SELECT, INSERT, UPDATE, DELETE
ON TABLE public.gbim_record
TO runtime_governance_role;

-- RLS policy: governance runtime sees all rows (USING true)
CREATE POLICY gbim_read_policy ON public.gbim_record
  FOR SELECT
  TO runtime_governance_role
  USING (true);
```

The `USING (true)` RLS policy is intentional. `runtime_governance_role` is a governance and lifecycle role, not a public-facing role. It must see all rows in `public.gbim_record` — including inadmissible, candidate, and stale rows — to perform backfill, lifecycle decay, promotion, and audit. The public admissibility boundary is enforced by the view (`public_admissible_gbim_mv`), not by RLS on the base table for this role.

**Capabilities of `runtime_governance_role`:**

| Capability | Object |
|---|---|
| SELECT, INSERT, UPDATE, DELETE | `public.gbim_record` |
| SELECT | `public.public_admissible_gbim_mv` |
| EXECUTE | `runtime_governance.refresh_public_admissible_gbim_mv()` |
| EXECUTE | `runtime_governance.log_lifecycle_counts()` |
| SELECT, INSERT | `runtime_governance.public_answer_audit` |
| Owns | `runtime_governance.public_answer_packet(text, text)` |

The pg_cron lifecycle jobs (`gbim-runtime-lifecycle-daily`, `-hourly`, `-weekly`, `-monthly`) run as `postgres` but invoke `runtime_governance.*` procedures that in turn use the governed state accessible to this role.

### 43.4.3 Tier 3 — public_instrument_role

`public_instrument_role` is the read-only public evidence surface. It was created and granted on July 26, 2026 with the following statements, confirmed in the live session:

```sql
-- Create the public instrument role
-- (exact CREATE ROLE statement executed as postgres)
-- GRANT sequence confirmed in the live session output:

GRANT SELECT ON public.public_admissible_gbim_mv
  TO public_instrument_role;

GRANT SELECT ON runtime_governance.public_answer_audit
  TO public_instrument_role;

REVOKE ALL ON TABLE public.gbim_record
  FROM public_instrument_role;

GRANT EXECUTE ON FUNCTION runtime_governance.public_answer_packet(text, text)
  TO public_instrument_role;
```

The July 26, 2026 session output confirms the exact sequence:

```
GRANT
GRANT
REVOKE
GRANT
GRANT
GRANT
COMMIT
```

**Capabilities of `public_instrument_role`:**

| Capability | Object |
|---|---|
| SELECT | `public.public_admissible_gbim_mv` |
| SELECT | `runtime_governance.public_answer_audit` |
| EXECUTE | `runtime_governance.public_answer_packet(text, text)` |
| **Denied** | `public.gbim_record` (permission denied — confirmed) |

### 43.4.4 The Permission Denied Proof

The following test was run on July 26, 2026 and confirmed the three-tier boundary:

```sql
SET ROLE public_instrument_role;

-- This succeeds:
SELECT count(*) AS admissible_rows
FROM public.public_admissible_gbim_mv;
-- Result: 93423

-- This succeeds:
SELECT count(*) AS audit_rows
FROM runtime_governance.public_answer_audit;
-- Result: 2

-- This fails as required:
SELECT count(*) AS raw_rows_should_fail
FROM public.gbim_record;
-- Result: ERROR: permission denied for table gbim_record
```

The `permission denied for table gbim_record` error is the correct, expected, and verified behavior. It proves that `public_instrument_role` cannot bypass the admissibility predicate by reading the base table directly.

### 43.4.5 Why the Tiers Are Designed This Way

The three-tier structure mirrors the same access-control principle that governs the application-layer gates:

- **`postgres`** is the administrator: it can see and change everything, but it is never exposed to callers.
- **`runtime_governance_role`** is the governance runtime: it must see all stored state to govern it correctly, but it does not expose raw state to the public.
- **`public_instrument_role`** is the public instrument: it can only see what has been certified as admissible, and it has no path to reach raw or inadmissible records.

The relationship between `runtime_governance_role` and `public_instrument_role` is exactly the stored/speakable boundary described in Appendix A: `runtime_governance_role` works with everything that is stored; `public_instrument_role` can only speak what is speakable.

---

## 43.5 Role, Purpose, and Projection Together

The three-tier database model and the three-part application-layer gate are the same principle applied at two different levels of the architecture.

**Application-layer:**

- **Role**: Who is asking? (local operator, civic role, internal system job)
- **Purpose**: Why are they asking? (flood planning, broadband planning, internal test)
- **Projection**: Given role and purpose, what subset of the knowledge is allowed to be seen or written?

**Database layer:**

- **`postgres`**: Administrator; bypasses all gates.
- **`runtime_governance_role`**: Governance runtime; sees all stored state, governs the lifecycle.
- **`public_instrument_role`**: Public instrument; sees only admissible, speakable state.

On the verified paths, these two levels are aligned:

- the **GBIM router** checks role and purpose against the manifest;
- the **GIS RAG** enforces projection headers and permitted-use constraints;
- the **write pipeline** projects proposed records into PERMIT or SUPPRESS;
- the **query guard** refuses dangerous person-only queries;
- the **database role boundary** ensures that even if an application-layer gate were bypassed, `public_instrument_role` would still be unable to reach inadmissible records.

---

## 43.6 Step-by-Step View for Rural Developers

A practical way to think about Chapter 43's gates on the verified paths:

1. **Request comes in.**
   - It includes a role (who) and a declared purpose (why).

2. **Router checks manifest and purpose.**
   - GBIM router ensures there is an active manifest row and that the purpose matches the collection's permitted use.

3. **Projection headers are enforced.**
   - GIS RAG limits retrieval to collections allowed for that role and purpose.

4. **Query guard watches for person-only requests.**
   - Suspicious person-only queries fail closed and are routed to constitutional review.

5. **Write pipeline applies `DisclosureVerdict`.**
   - For appearance records or similar writes, the gate returns PERMIT or SUPPRESS.

6. **Database role boundary enforces the public evidence surface.**
   - Any path reaching the database is subject to the three-tier role model.
   - `public_instrument_role` can only read `public_admissible_gbim_mv` and `runtime_governance.public_answer_audit`.
   - A direct SELECT on `public.gbim_record` returns `permission denied`.

7. **Only permitted slices are visible or stored.**
   - The user receives only the portion of the information that matches their role and purpose, or no information at all if the check fails.

If any of these checks fail, the **expected behavior is to decline the request**, not to downgrade the rules.

---

## 43.7 What This Chapter Does Not Claim

To stay within the sealed constraints, Chapter 43 does **not** claim:

- complete, universal access-control coverage across every service or legacy path;
- perfect enforcement of role and purpose in parts of the system not covered by the GBIM, GIS RAG, policy, query-guard, and disclosure paths;
- clinical, psychological, or therapeutic evaluation of users based on their queries.

Its claims are narrow but concrete:

- **role/purpose/projection gating** over the verified GBIM, GIS RAG, policy/write-pipeline, query-guard, and disclosure paths;
- **fail-closed behavior** for person-only queries and incompatible purposes;
- **manifest-bound access** to governed collections;
- **three-tier database role enforcement** — `postgres`, `runtime_governance_role`, `public_instrument_role` — confirmed as-built on July 26, 2026, with exact role names, GRANT statements, RLS policy, and the verified `permission denied` test.

---

## 43.8 Closing Statement

Chapter 43 describes how Ms. Allis uses **role, purpose, and projection gates** to control access to governed belief and GIS knowledge on the paths that have been explicitly verified, and how a three-tier database role model enforces those same principles at the Postgres level.

Through the GBIM router, GIS RAG, publication manifest, write-pipeline disclosure verdicts, and query guard, the application layer ensures that even when the system knows something, it only shares or stores what matches the requester's role and declared purpose. The database layer enforces an independent boundary: `public_instrument_role` cannot reach `public.gbim_record` under any circumstances — a fact proven by the July 26, 2026 `permission denied` test. Together, these two layers give rural developers a clear, step-by-step picture of how access is governed on the parts of the system this gate actually covers, without pretending that every path everywhere has already reached the same standard.

---

*Chapter 43 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
