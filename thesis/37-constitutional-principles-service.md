# 37. Constitutional Principles Service

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 37.1 What This Service Does

The constitutional principles service is a **governance gate** that checks whether a proposed action fits the project's constitutional commitments before it is allowed to gain authority.

Here, "constitutional" is concrete, not decorative. The service is rooted in:

- the **United States Constitution**;
- the **West Virginia Constitution**.

These are used as reference frameworks for rights, limits, due process, and bounded authority. The service sits in the promotion path to help decide whether a candidate action may move from **internal proposal** to **approved system behavior**.

As of the July 26, 2026 architecture closeout, the Constitutional Principles Service is named in Chapter 52 as one of the **two built components of the Recurrent Epistemic Loop** — alongside the DGM validators. Its governance filtering is invoked on a daily scheduled cadence by `runtime_governance.gbim_runtime_lifecycle_daily()`, the pg_cron job (jobid 3) that fires every day at 03:05 in `wv_gis`. That connection is detailed in §37.8 and §37.9 below.

---

## 37.2 Live Service and Ports (July 2026)

As of the July 26, 2026 evidence:

- The **constitutional guardian** is live on host port **8091**.
- The **BBB** (blood-brain barrier) is live on host port **8016** and connected to the guardian.
- The guardian exposes two review endpoints:
  - `/constitutional-principles/review`
  - `/constitutional/review`

These endpoints accept structured payloads and return governance decisions. This chapter does **not** rely on any April 2026 container counts or database sizes; it reflects the as-built July 2026 state only.

---

## 37.3 Constitutional Materials in the System

The constitutional principles service works alongside:

- internal corpora that store the **U.S.** and **West Virginia** constitutions;
- related governance texts and commentary;
- retrieval tools that can pull relevant passages for context.

The purpose is **not** to act as a court or replace lawyers. Instead, the service:

- brings constitutional ideas (rights, restraints, due process) into the decision pipeline;
- helps flag actions that look like they would violate those commitments;
- supports a place-rooted understanding of lawful power in West Virginia communities.

---

## 37.4 The Guardian Payload Contract

Every request to the constitutional service must carry a **structured payload**. A typical contract includes:

- `actor_role` — who is acting (for example, system module, operator, automation).
- `context` — in what situation (session, workflow, scenario).
- `action_type` — what kind of action is proposed (promotion, disclosure, registration, memory write, etc.).
- `content` — the substance of what is being promoted or done.
- `metadata` — provenance, identifiers, and other details needed for review.

If this payload is **missing required fields** or structurally invalid, the guardian:

- rejects the request;
- treats the action as **not constitutionally approved**;
- causes the promotion path to **fail closed**.

Simply calling the endpoint is not enough; the payload must be complete and valid.

---

## 37.5 What the Guardian Checks

When a valid payload is sent to `/constitutional-principles/review` or `/constitutional/review`, the service checks questions such as:

- Is this actor allowed to attempt this action in this context?
- Does the action respect consent and privacy (for example, no private disclosure without permission)?
- Does it avoid obvious conflicts with constitutional rights or protections?
- Is there any sign of bypassing required oversight or due process within the system's own rules?

Examples:

- A **governed promotion payload** with proper consent and context can pass.
- A **consent-bypass** or **private-disclosure** payload is expected to **fail closed**.
- A payload that omits required consent fields is rejected at the schema level.

---

## 37.6 BBB and Guardian Together

The **BBB** and the **constitutional guardian** work together in the promotion path:

- BBB sits at a boundary between lower-risk internal reasoning and higher-authority consequences.
- The guardian provides constitutional review within that boundary.
- Both expose **health surfaces** so watchdogs and operators can confirm they are up and responding.

For rural operators, this means you can:

- check that BBB on port **8016** is healthy;
- check that the guardian on port **8091** is healthy;
- verify that promotion calls actually pass through these gates instead of bypassing them.

---

## 37.7 Valid vs. Invalid Promotion Payloads

From the July 26, 2026 closure evidence:

- **Valid governed promotion payloads pass** constitutional review.
- **Consent-bypass or private-disclosure payloads fail closed.**
- **Missing required fields** are **rejected by schema validation** before approval.

In practice:

- a well-formed request, with all required fields and consent markers, can be approved;
- a request trying to expose private information without consent is blocked;
- a request that forgets to include necessary context fields is treated as **invalid**, not "probably fine."

---

## 37.8 Role in the Recurrent Epistemic Loop (Chapter 52)

The Constitutional Principles Service is one of the **two named built components of the Recurrent Epistemic Loop**, as confirmed in Chapter 52. The other named component is the DGM validators. Together, these two components form the loop's governance filtering layer: DGM validators check whether proposed self-modifications are coherent and bounded; the Constitutional Principles Service checks whether proposed actions respect constitutional rights, consent, and due process.

The Recurrent Epistemic Loop is not a design idea — it is a running structure. Its two components are not passive services waiting to be called manually; they are invoked on a scheduled cadence by the database-layer heartbeat described in Chapter 28.

The scheduled surface that invokes governance filtering is `runtime_governance.gbim_runtime_lifecycle_daily()`, registered as pg_cron jobid 3 with schedule `5 3 * * *`. Every day at 03:05, this procedure advances the GBIM lifecycle and, as part of that advancement, triggers the governance filtering pass that includes constitutional review of records in the promotion pipeline. This is the mechanism by which the Constitutional Principles Service participates in the continuous, observable governance cycle rather than being invoked only on demand.

For rural developers, the implication is concrete: constitutional filtering is not something that happens once when a record is first ingested. It happens again at every daily governance pass. A record that was constitutionally acceptable when ingested will be re-evaluated during the daily cycle. If its context has changed — if consent was withdrawn, if a prohibited metadata field was added, if the action type shifted — the daily pass provides the scheduled surface on which that re-evaluation occurs.

---

## 37.9 Role in the Broader Promotion Pipeline

The constitutional principles service is one part of a broader promotion gate. A typical path is:

1. **Sandbox reasoning** produces a candidate action or answer.
2. Other judges and checks evaluate truth, coherence, safety, provenance, and the ten-condition admissibility predicate (Appendix A).
3. A promotion request is constructed with a **guardian payload**.
4. The request is sent through BBB and the **constitutional review endpoints**.
5. Only if constitutional review **approves** — and other gates agree — can promotion proceed.
6. At the next daily governance pass (`runtime_governance.gbim_runtime_lifecycle_daily()`), promoted records are re-evaluated through the governance filtering layer as part of the Recurrent Epistemic Loop (Chapter 52).

If the guardian response is a failure, or if the payload is malformed, the system:

- does **not** treat the action as approved;
- fails closed and logs the problem;
- records the failure state in `runtime_governance.public_answer_audit` so operators can inspect it.

---

## 37.10 Place-Aware Constitutional Orientation

Because Ms. Allis is rooted in **Mount Hope, West Virginia**, the constitutional service:

- names and respects both the **U.S. Constitution** and the **West Virginia Constitution**;
- treats local state-level rights and limits as part of its frame of reference;
- avoids pretending that governance is the same everywhere.

The daily governance pass through `runtime_governance.gbim_runtime_lifecycle_daily()` is itself place-aware: it operates on records in `wv_gis`, the West Virginia geographic information system database, and its admissibility checks include the spatial anchor columns (`spatial_unit_id`, `spatial_unit_kind`) that tie every public claim to a named West Virginia geography. Constitutional filtering and spatial grounding run in the same daily cycle.

The service still does **not** give legal advice or act as a lawyer. It is a **technical mechanism** to enforce internal rules that are themselves influenced by constitutional traditions.

---

## 37.11 What This Chapter Does Not Claim

Within this closure, Chapter 37 does **not** claim:

- perfect legal correctness;
- that the system is a court or legal advisor;
- that all constitutional questions are solved or provably encoded;
- clinical or safety guarantees for downstream human decisions;
- that `runtime_governance.gbim_runtime_lifecycle_daily()` performs constitutional review directly in SQL — it invokes the governance filtering layer that includes constitutional review as one of its gates, not a SQL-native constitutional analysis.

It only claims:

- a **live constitutional guardian** on port 8091;
- a connected **BBB** on port 8016;
- working review endpoints;
- fail-closed handling of malformed and consent-bypass payloads;
- explicit naming of the **United States** and **West Virginia** constitutions as reference frameworks;
- the Constitutional Principles Service as one of **two named built components of the Recurrent Epistemic Loop** (Chapter 52), alongside the DGM validators;
- `runtime_governance.gbim_runtime_lifecycle_daily()` (pg_cron jobid 3, schedule `5 3 * * *`) as the scheduled surface that invokes governance filtering on a daily cadence.

---

## 37.12 Step-by-Step View for Rural Developers

In everyday terms, when something important is about to happen (for example, a promotion or disclosure that touches identity or public impact), the flow is:

1. Ms. Allis builds a **guardian payload** describing who is acting, what they want to do, in what context, and with what content.
2. That payload is sent through the **BBB** to the **constitutional review endpoints**.
3. The guardian checks that the payload is structurally valid and constitutionally acceptable under the project's rules.
4. If checks pass, the rest of the promotion gates may proceed.
5. If checks fail, the action is **blocked** and the event is logged to `runtime_governance.public_answer_audit`.
6. Every day at 03:05, `runtime_governance.gbim_runtime_lifecycle_daily()` (jobid 3) fires and advances the governance filtering pass — including constitutional review — across all records currently in the promotion pipeline. This is the Recurrent Epistemic Loop (Chapter 52) executing on its scheduled cadence.

For rural developers, step 6 is the key addition from July 26, 2026: constitutional filtering is not just an on-demand gate. It is a daily scheduled pass. You can verify it ran by checking `cron.job_run_details` for jobid 3 and reading the corresponding `lifecycle_snapshot` row in `runtime_governance.public_answer_audit`.

---

## 37.13 Closing Statement

The Constitutional Principles Service makes **constitutional restraint** a real part of Ms. Allis's promotion path. By running on live ports, requiring structured guardian payloads, failing closed on malformed or consent-bypass requests, and explicitly naming the **U.S.** and **West Virginia** constitutions as reference points, it turns constitutional ideas into an operational gate.

As one of the two named built components of the Recurrent Epistemic Loop (Chapter 52) — alongside the DGM validators — the Constitutional Principles Service is not a standalone check. It participates in a continuous, scheduled governance cycle. The scheduled surface that invokes it is `runtime_governance.gbim_runtime_lifecycle_daily()`, the daily pg_cron job that fires at 03:05 each morning and advances the governance filtering layer across all records in the promotion pipeline.

For rural communities, this means the system's big moves — especially around disclosure and authority — must pass through a **concrete constitutional checkpoint** on a repeating daily schedule, not just the good intentions of the developers, and not just once at ingestion time.

---

*Chapter 37 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
