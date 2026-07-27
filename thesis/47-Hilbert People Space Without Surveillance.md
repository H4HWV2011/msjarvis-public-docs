# 47. Hilbert People and Noun Space Without Surveillance (As-Built)

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 47.1 What This Chapter Is Allowed to Claim

Within this gate, Chapter 47 is limited to **people-space non-surveillance at the scope already proven by Chapter 48**, extended on July 26, 2026 by the as-built three-tier database role model described in Chapter 43.

It may claim that, for Ms. Allis's people-space:

- per-user promotion is **consented, role/permitted, and non-expired**;
- **surveillance-shaped metadata** is suppressed;
- **deletion and expiry-based pruning** work and are no longer "not yet demonstrated";
- **commons isolation** holds: private people-space does not leak into commons without explicit, governed promotion;
- the **`public_instrument_role` receiving `permission denied` on `public.gbim_record`** — confirmed on July 26, 2026 — is the architectural enforcement of the non-surveillance boundary at the database layer: the public instrument cannot introspect raw records, cannot count inadmissible rows, and cannot reconstruct any person's record history from the base table, regardless of what is stored there.

It must **not** claim non-surveillance beyond the Ch48-proven scope, and it must not suggest that all possible retention or access-control patterns in the system are covered. The focus is on **what is actually built and checked** for people-space as of this gate.

---

## 47.2 Plain-Language Purpose for Rural Developers

For rural operators, this chapter answers:

> "If Ms. Allis remembers anything about people, how do we know she isn't quietly turning into a surveillance system?"

This chapter explains, step by step:

- how **people-space** is structured per user;
- how **consent and role** control what gets promoted into that space;
- how **surveillance-shaped metadata is suppressed**;
- how **deletion and pruning** work in practice;
- how **commons collections stay separate** from private people-space;
- how the **database role boundary** — the `permission denied` result confirmed on July 26, 2026 — ensures that even if every other layer were bypassed, the public instrument still could not reach raw records.

The goal is to show that Ms. Allis **can help people using some memory**, without turning that memory into an unbounded tracking dossier — and that the boundary enforcing that promise is not just a policy commitment but a running database constraint.

---

## 47.3 The Database-Layer Non-Surveillance Boundary — As-Built Proof

On July 26, 2026, the following test was run in `wv_gis` as part of the three-tier role model verification:

```sql
SET ROLE public_instrument_role;

-- Attempt to read raw governed records directly:
SELECT count(*) AS raw_rows_should_fail
FROM public.gbim_record;
```

The database returned:

```
ERROR: permission denied for table gbim_record
```

This single error message is the as-built proof that the non-surveillance boundary is architecturally enforced, not merely assumed. The same session confirmed that `public_instrument_role` **can** read the admissible surface:

```sql
-- This succeeds:
SELECT count(*) AS admissible_rows
FROM public.public_admissible_gbim_mv;
-- Result: 93423
```

The contrast between these two results is the boundary in operation:

| Query | Role | Result |
|---|---|---|
| `SELECT count(*) FROM public.gbim_record` | `public_instrument_role` | `ERROR: permission denied` |
| `SELECT count(*) FROM public.public_admissible_gbim_mv` | `public_instrument_role` | `93423` |
| `SELECT count(*) FROM public.gbim_record` | `runtime_governance_role` | `237655` |

### 47.3.1 What This Boundary Prevents

The `permission denied` result is not a minor technical detail. It prevents the following surveillance-shaped queries from being possible through the public instrument path:

- **Raw record enumeration**: counting or listing all 237,655 rows, including those with `public_claim_allowed = false`, to reconstruct what the system knows about specific places or people.
- **Inadmissible record inspection**: reading the 144,232 rows that did not pass the ten-condition admissibility predicate to discover what was ingested but suppressed.
- **Lifecycle state bypass**: querying `degradation_status = 'stale'` rows directly to see records that have been aged out of the public surface.
- **Provenance bypass**: reading `under_whose_authority` and `company_name` fields on inadmissible rows to map the full scope of what has been ingested.

None of these queries can be constructed through `public_instrument_role`. The architecture makes them structurally impossible, not merely discouraged.

### 47.3.2 Why This Is the Right Place to Enforce the Boundary

The non-surveillance boundary for people-space is enforced at **multiple layers** — application gates, query guards, and policy checks (Chapter 43). But the database-layer enforcement has a specific property the other layers do not: it **cannot be bypassed by any application-layer bug or misconfiguration**.

If a query router has a bug and fails to check purpose correctly, the database role boundary still holds. If a new service is added without complete policy wiring, the database role boundary still holds. If a test or debugging session uses `public_instrument_role`, the database role boundary still holds.

For rural developers, this means:

- the surveillance boundary is not only in the code — it is in the **grants table of the database itself**;
- removing it requires a deliberate `GRANT` from the `postgres` superuser, which is an auditable, intentional act;
- it cannot be removed by accident, by a misconfigured service, or by a caller who simply does not know the rules.

---

## 47.4 People-Space at the Ch48-Proven Scope

Chapter 48's probe provides the evidence this chapter can lean on. At that scope, people-space is implemented as:

- **per-user partitions**, so each person has their own people-space;
- **role- and consent-controlled promotion**, so only specific, allowed signals move from an interaction into that space;
- **expiry and pruning logic**, so person-linked records do not live forever by default;
- **commons isolation**, so private records do not automatically join community-wide or public aggregates.

This chapter **inherits** that scope: any non-surveillance claim here is tied to those same mechanisms and tests, not to the entire system in the abstract. The July 26, 2026 database role boundary adds a fourth layer of enforcement beneath all of these.

---

## 47.5 Per-User, Consented People-Space Promotion

At this gate, people-space promotion is:

- **per-user**: each user's records are written into that user's own people-space partition, not into a shared bucket;
- **consented**: promotion of certain person-linked records only happens when consent flags say it is allowed;
- **role/permitted**: promotion happens only when the requester or process has a role that is allowed to perform that promotion;
- **non-expired**: records are created with lifetimes or expiry rules, so promotion does not mean "forever."

In practical terms, for a rural operator:

- Ms. Allis can store **"this person asked for this kind of help"** under that person's space, but only if consent has been given and the active role and purpose allow it;
- older or expired person-linked records are not treated as permanent; they are pruning candidates.

Even if a promoted record exists in the governed store, `public_instrument_role` cannot reach it through `public.gbim_record`. It can only reach records that have passed all ten admissibility conditions and appear in `public_admissible_gbim_mv`. The database layer enforces this without requiring the application layer to ask permission.

---

## 47.6 Surveillance-Shaped Metadata Suppression

"Surveillance-shaped metadata" refers to fields that would obviously support tracking, profiling, or dossier building if left unchecked:

- unnecessary high-frequency timestamps;
- cross-session device fingerprints;
- detailed location breadcrumbs when not needed for the task;
- free-floating identifiers that would let someone reconstruct a person's full history without context.

At the Ch48-proven scope, people-space implements **suppression** of such metadata by:

- **not writing** these fields into the people-space store at all; or
- **sanitizing or dropping** them at write time when they are not needed;
- **keeping only the minimum** needed to serve the declared purpose.

At the database layer, suppression is reinforced structurally: even if surveillance-shaped fields were somehow written into `public.gbim_record`, `public_instrument_role` cannot read them. The only fields the public instrument can observe are those in `public_admissible_gbim_mv`, which is defined by the ten-condition admissibility predicate and the `SELECT` list of the view — not by the full column list of the base table.

---

## 47.7 Deletion and Expiry-Based Pruning (No Longer "Not Yet Demonstrated")

Under this gate, deletion and pruning are **implemented and exercised**, so prior "not yet demonstrated" language is removed.

People-space now supports:

- **explicit deletion**: a person's records (or a subset) in people-space can be deleted on request;
- **expiry pruning**: records can be given lifetimes, after which a pruning job removes or archives them;
- **non-expired promotion**: promotion logic respects expiry; records that should have expired are not treated as active.

For rural operators, this means:

- if someone asks Ms. Allis **"forget this conversation for me"** (within the implemented UI/flow), there is a mechanism that actually deletes or prunes those records from people-space;
- background pruning keeps people-space from turning into a **permanent log of everything**.

The pruning and deletion paths work at the application and governance layers. At the database layer, they are reinforced by the pg_cron lifecycle jobs (`gbim-runtime-lifecycle-daily`, `-hourly`, `-weekly`, `-monthly`) confirmed on July 26, 2026, which run `runtime_governance.*` procedures responsible for decay and lifecycle maintenance of governed records.

---

## 47.8 Commons Isolation for People-Space

Commons isolation means that:

- **private people-space** is not automatically used to populate commons or public datasets;
- any movement from private people-space to commons must go through an **explicit, governed promotion path** (often involving anonymization and aggregation).

At the Ch48-proven scope, this is enforced by:

- keeping people-space collections separate from commons collections;
- having **no code paths** that copy people-space records into commons by default;
- requiring **consent and explicit promotion logic** before any person-linked pattern participates in a shared summary.

At the database layer, this isolation is reinforced by the `public_instrument_role` boundary: the public instrument reads only `public_admissible_gbim_mv`, which contains only records that have been deliberately promoted through the ten-condition predicate. A person's raw interaction record in `public.gbim_record` with `public_claim_allowed = false` is structurally invisible to the public instrument — not because the application layer filters it out, but because the role grants do not permit the query at all.

---

## 47.9 How People-Space Non-Surveillance Feels in Use

From a user or local operator perspective, people-space non-surveillance at this scope looks like:

- Ms. Allis can **remember enough** about past conversations and interactions to provide continuity;
- that memory is **scoped per user**, so one person's record is not casually shown to another;
- sensitive, tracking-shaped fields are **not present** or are stripped before going into long-term storage;
- requests to **delete or clear** certain history are actually honored;
- shared or public outputs are **aggregates and anonymized views**, not raw personal logs;
- the public instrument — the role that backs any outward-facing answer function — **cannot read raw records at all**, regardless of what is stored in the governed base table.

The system is still capable of **learning and helping**, but the way it stores and reuses information is **designed around non-surveillance boundaries** that are enforced in code, in tests, in governance procedures, and in the database grant table itself.

---

## 47.10 Step-by-Step View for Rural Developers

At the Ch48-proven scope and with the July 26, 2026 database role boundary, you can think of people-space non-surveillance as this sequence:

1. **Interaction happens.**
   - Ms. Allis reasons about a person in context, in sandboxed internal state.

2. **Decide whether to promote.**
   - Check consent, role, purpose, and expiry settings.
   - If checks fail, keep the reasoning ephemeral or discard it.

3. **Write into per-user people-space (if allowed).**
   - Store only the necessary fields; suppress surveillance-shaped metadata.

4. **Apply expiry and pruning.**
   - Records carry lifetimes; pg_cron lifecycle jobs remove or decay expired entries.

5. **Keep commons separate.**
   - Do not let private records feed commons collections unless an explicit, governed promotion says so.

6. **Honor deletion.**
   - When a person or operator requests deletion within the supported interface, remove those records from people-space.

7. **Verify the database role boundary.**
   - Run `SET ROLE public_instrument_role; SELECT count(*) FROM public.gbim_record;`
   - Confirm the result is `ERROR: permission denied for table gbim_record`.
   - This confirms that the public instrument cannot introspect raw records regardless of application-layer state.

If any step fails, the expected behavior is to **fail closed** — do not promote, do not leak to commons, do not keep extra data "just in case." Step 7 is the structural backstop: even if steps 1 through 6 have a bug, step 7 remains in force.

---

## 47.11 What This Chapter Does Not Claim

To stay exactly within the gate:

- It does **not** claim that all possible storage, log, or service paths in Ms. Allis are non-surveillance;
- It does **not** claim that people-space retention and pruning are mathematically perfect across every subsystem;
- It does **not** claim universal deletion across all layers (for example, OS-level logs, backups) beyond the Ch48-proven scope;
- It does **not** claim that `permission denied` on `gbim_record` covers every table in `wv_gis` — it covers the governed GBIM base table specifically, which is the table that backs the public answer surface.

It only claims:

- **consented, role/permitted, non-expired per-user promotion** into people-space;
- **surveillance-shaped metadata suppression** for that space;
- **working deletion and expiry-based pruning** for people-space records;
- **commons isolation** for people-space at the scope demonstrated by Chapter 48;
- **`public_instrument_role` receiving `permission denied` on `public.gbim_record`** — confirmed July 26, 2026 — as the as-built architectural proof that the public instrument cannot introspect raw records.

---

## 47.12 Closing Statement

Chapter 47, at this gate, describes **non-surveillance people-space as it is actually built and proven**, not as a general promise for everything.

By tying its claims to the Ch48-proven scope, it shows that Ms. Allis can hold per-user people-space that is **consented, role-controlled, non-expired, pruned, and isolated from commons**, while still being useful for rural communities. The system can remember enough to serve, but not enough to quietly watch — within the specific, tested pathways this chapter is allowed to talk about.

The July 26, 2026 three-tier role model adds one more layer of proof beneath all the others. The `public_instrument_role` receiving `ERROR: permission denied for table gbim_record` is not incidental. It is the **architectural enforcement of the non-surveillance boundary** — the proof that the public instrument, no matter what it is asked, cannot reach raw governed records, cannot enumerate what is stored but suppressed, and cannot reconstruct any person's record history from the base table. That boundary lives in the database grant table, not in any single application, and it requires a deliberate superuser action to remove.

---

*Chapter 47 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
