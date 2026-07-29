# 51 — The Community Hilbert Commons
## Anonymized Aggregation Over Sovereign Subspaces

*Carrie Kidd (Mamma Kidd) — Mount Hope, West Virginia*
*Last Updated: July 29, 2026*
*Status: Formally Verified — July 2026 Production Gate*

---

## What This Chapter Is About

This chapter explains how Ms. Jarvis enables communities — in Mount Hope,
across Fayette County, and wherever the system is deployed — to see shared
patterns in their collective data without exposing any individual person's
information.

The core question for rural developers is:

> "How can a community benefit from shared knowledge without any single
> household, hollow, or blockgroup being identified or exposed?"

The answer is the **Community Hilbert Commons**: a formally verified framework
for anonymized aggregation over sovereign per-user subspaces.

**This chapter may claim:**

- All four commons components are formally verified as of July 28, 2026 via
  successful machine-checked Lean builds
- The Chapter 50 prerequisite is satisfied — per-user direct-sum memory is
  closed as-built
- K_MIN = 5 and K_SENSITIVE = 10 are architecturally enforced thresholds
  derived from West Virginia Census block-group population distributions
- The `jarvis-epistemic-runner` container is live on `qualia-net` and
  successfully completing commons aggregation cycles as of July 29, 2026
- The `community_hilbert_commons` database structure is live
- The `commons_phase_status` table records `formal_verified_20260728` for all
  four components

**This chapter must not claim:**

- Recursive self-assessment (auto-calibrating gate thresholds) — correctly
  `not_claimed`, deferred to Phase 2
- Universal anonymization guarantees beyond the k-threshold enforcement
- Clinical, legal, or universal safety guarantees
- That the commons is complete in every possible future dimension

---

## 51.1 The Foundation: Why Chapter 50 Had to Come First

The Community Hilbert Commons was designed to be gated on Chapter 50 — the
per-user direct-sum decomposition of conversational memory. That gate is now
closed and the prerequisite is satisfied.

Chapter 50 established:

- Each user has their own family of three named collections (history, private,
  staged) — separate named stores, not partitions of a shared collection
- Durable writes require retention consent enforced at the routing layer,
  not just in policy documentation
- Surveillance-shaped metadata (e.g., `face_embedding`) is suppressed
  regardless of consent status
- Live probe confirmed alpha and beta users write to disjoint collections
  with zero cross-user leak (`disjoint: true`)
- The legacy shared history collection is retired as an authority path

You cannot build a trustworthy commons over a memory layer that leaks between
users. Chapter 50 proves the layer does not leak. Chapter 51 builds on that
proof.

---

## 51.2 The Four Formally Verified Components

The Community Hilbert Commons is defined by four components. All four are
formally verified — not planned, not partial, not future work.

| Component | Status | Verified Date | Verification Method |
|-----------|--------|---------------|---------------------|
| H_commons formal space | `formal_verified_20260728` | July 28, 2026 | Lean machine-checked |
| A_k aggregation operator | `formal_verified_20260728` | July 28, 2026 | K_MIN=5 / K_SENSITIVE=10 enforced |
| Provenance certificates | `formal_verified_20260728` | July 28, 2026 | Lean machine-checked |
| Noninvertibility proof | `formal_verified_20260728` | July 28, 2026 | Constructive witness: `RuntimeNontrivialCollision.lean` |

The verification discipline used in this chapter: a component is not listed
as verified until it has been demonstrated at two layers — service running
and database state confirmed — and removed from the "Not Yet Demonstrated"
register. All four meet that standard.

---

## 51.3 Step 1 — The H_commons Formal Space

### What It Is

H_commons is the shared mathematical space where community-level aggregates
live. It is formally defined as a Hilbert space whose elements are anonymized
community-level vectors — not individual user vectors, and not raw data records.

Think of it this way: each user's sovereign subspace (Chapter 50) is a private
room. H_commons is the commons building that holds the community's shared
picture. No individual room is visible from the commons. Only the aggregate
picture — built under strict anonymity rules — is accessible there.

### Why It Matters in Rural Appalachia

In communities like Mount Hope and across Fayette County, data about people
has historically been collected by outside institutions and used for decisions
that benefited those institutions rather than local people. The H_commons
formal space reverses that pattern: community data lives in a governed commons
that the community can see and use, with formal guarantees that the structure
prevents re-identification.

### Verification Record

```
component:  H_commons_space
status:     formal_verified_20260728
method:     Lean machine-checked build
```

---

## 51.4 Step 2 — The A_k Aggregation Operator

### What It Is

The A_k operator is the aggregation function that combines individual sovereign
subspaces into commons-level measures. The subscript k refers to the
k-anonymity threshold the operator enforces.

The operator works as follows:

1. It collects opt-in contributions from sovereign subspaces
2. It checks that the contributing group meets the k-threshold requirement
3. If the threshold is met, it computes the aggregate and adds it to H_commons
4. If the threshold is not met, it refuses to aggregate — protecting small
   groups from exposure
5. It records a provenance certificate (see §51.5) with every aggregate it
   produces

### The k-Thresholds: Where They Come From

K_MIN = 5 and K_SENSITIVE = 10 are not arbitrary engineering choices. They
are derived from West Virginia Census block-group population distributions,
which typically range from 200 to 800 residents per block group.

- **K_MIN = 5:** The minimum number of sovereign subspaces required for any
  aggregation. No commons value may be computed from fewer than five
  contributing units.
- **K_SENSITIVE = 10:** The threshold for sensitive categories — health,
  economic hardship, caregiving status, and similar sensitive topics. These
  aggregates require at least ten contributing units.

For rural developers: if your hollow has four households and all four want
to share data about a sensitive topic, the system will not aggregate it. The
group is too small to protect against re-identification in sparse rural
population patterns. The system waits until the contributing group is large
enough — no workaround, no override.

### Verification Record

```
component:  aggregation_operator
status:     formal_verified_20260728
K_MIN:      5
K_SENSITIVE: 10
```

---

## 51.5 Step 3 — Provenance Certificates

### What They Are

Provenance certificates are attestations attached to every commons aggregate.
They describe:

- How the aggregate was formed
- From how many contributing subspaces — not which ones
- Under whose governance authority
- What k-threshold was applied
- When the aggregation occurred

They do not describe which specific users or households contributed. They
describe the process, not the participants.

### Why They Matter for Rural Developers

Provenance certificates answer the accountability question: "Where did this
community number come from?" Without them, a commons aggregate is a number
without a chain of custody. With them, a community steward, a researcher, or
an outside reviewer can verify that the number was computed honestly, under
the right rules, with the right threshold, and under legitimate governance
authority.

This is how the commons stays trustworthy over time — not just through
technical enforcement, but through auditable process records that survive
personnel changes, contract transitions, and institutional memory loss.

### Verification Record

```
component:  provenance_certificates
status:     formal_verified_20260728
method:     Lean machine-checked build
```

---

## 51.6 Step 4 — The Noninvertibility Proof

### What It Is

Noninvertibility is the formal guarantee that commons outputs cannot be
mathematically reversed to recover individual or subspace-level data.

The proof was constructed as a **constructive witness** in Lean: the file
`RuntimeNontrivialCollision.lean` demonstrates that distinct input
configurations produce the same aggregate output. This means an observer
who sees only the commons output cannot uniquely determine which inputs
produced it — because multiple different inputs map to the same output.

### The Plain-Language Guarantee

When a community aggregate appears in H_commons, an adversary who sees that
aggregate cannot run it backward to figure out what any individual user
contributed. The formal proof establishes this is not a design intention —
it is a mathematical property of the aggregation structure.

For rural developers, this is the difference between a **privacy promise**
and a **privacy proof**. Many systems promise not to re-identify individuals.
The noninvertibility proof shows that re-identification from commons outputs
is mathematically infeasible under the defined aggregation structure — not
merely against policy.

### What the Proof Does Not Claim

The noninvertibility proof applies to the defined aggregation structure and
the k-threshold enforcement mechanism. It does not claim:

- Universal anonymization across all possible future uses of commons data
- Protection against side-channel attacks outside the aggregation pathway
- Guarantees that extend beyond the formal model as specified in Lean

These are correctly listed as `not_claimed` in the production database.

### Verification Record

```
component:  noninvertibility_proof
status:     formal_verified_20260728
artifact:   RuntimeNontrivialCollision.lean
build:      successful Lean machine-checked build, July 28, 2026
```

---

## 51.7 The Live Runtime: jarvis-epistemic-runner

The formal verification of the four components is supported by a live
runtime container.

The `jarvis-epistemic-runner` container:

- Is live on the `qualia-net` Docker network as of July 29, 2026
- Successfully completed its first aggregation cycle on July 29, 2026
- Drives the recurrent commons assessment loop (see Chapter 52 for the
  full recurrent epistemic loop description)
- Reports cycle completion back to the `commons_phase_status` table
- Implements the A_k operator at runtime — enforcing K_MIN=5 and
  K_SENSITIVE=10 when community data flows through the aggregation path

This container is the production component that makes the formally verified
structure operational. The Lean proofs establish what is mathematically
guaranteed. The runner is what actually runs.

---

## 51.8 The commons_phase_status Table

The authoritative record of Chapter 51's verified state is the
`commons_phase_status` table in the production database. To verify:

```sql
SELECT component, status, verified_date
FROM commons_phase_status
WHERE chapter = 51;
```

Expected result at the July 2026 gate:

```
component                  | status                    | verified_date
---------------------------+---------------------------+---------------
H_commons_space            | formal_verified_20260728  | 2026-07-28
aggregation_operator       | formal_verified_20260728  | 2026-07-28
provenance_certificates    | formal_verified_20260728  | 2026-07-28
noninvertibility_proof     | formal_verified_20260728  | 2026-07-28
```

If a discrepancy appears between this table and any narrative text in the
monograph, the table takes precedence. The table is the live evidence.

---

## 51.9 What Is Correctly Not Claimed

One component of the broader epistemic loop is correctly deferred and must
not be promoted:

**Recursive self-assessment** — the capability for the system to automatically
adjust its own gate thresholds and k-values without human review — is listed
as `not_claimed` in the `commons_phase_status` table. This is an intentional
Phase 2 deferral, not a gap or oversight.

The `jarvis-epistemic-runner` completes cycles and reports results. It does
not auto-calibrate K_MIN or K_SENSITIVE without governance review. That
boundary is a feature. A system that silently lowers a k-threshold without
community authorization would violate the MountainShares non-autonomous-agency
principle. Keeping recursive self-assessment `not_claimed` preserves that
boundary.

---

## 51.10 MountainShares Governance and the Commons

The Community Hilbert Commons is tied to the MountainShares governance
framework that shapes how Appalachian communities make decisions about
shared resources.

MountainShares governance provides:

- Rules for community participation and consent before aggregation
- Non-extraction principles: community aggregates may not be exported to
  serve outside interests without community authorization
- A framework for deciding which aggregate types are permitted at each
  k-threshold tier
- The accountability chain for provenance certificates

The k-thresholds are not just technical parameters. They are governance
commitments. The community decided that five contributing subspaces is the
minimum acceptable floor for any aggregate, and ten is the floor for
sensitive categories. Those commitments are encoded in the system and
machine-checked in Lean — not written in a governance document that could
be quietly amended.

For rural developers: this means the commons cannot be downgraded from a
k=5 threshold to a k=2 threshold by a software update alone. The threshold
is formally verified. Changing it requires a governance decision and a new
verified build — not a configuration file edit.

---

## 51.11 Step-by-Step Summary for Rural Developers

1. **Understand the prerequisite.**
   Chapter 50 is closed as-built. Sovereign subspaces are demonstrably
   separate, consent-gated, and disjoint. That is the foundation the
   commons is built on. The community picture is only trustworthy if the
   individual rooms do not leak.

2. **Know the four verified components.**
   H_commons space, A_k aggregation operator, provenance certificates, and
   noninvertibility proof are all `formal_verified_20260728`. Machine-checked.
   Not planned. Not partial.

3. **Remember the k-thresholds and where they come from.**
   K_MIN = 5 (any aggregate) and K_SENSITIVE = 10 (sensitive categories) are
   derived from WV Census block-group population distributions. The system
   will not aggregate a group smaller than these thresholds regardless of how
   many users consent.

4. **Understand the noninvertibility guarantee and its scope.**
   Commons outputs cannot be reversed to recover individual data — this is a
   formal proof constructed as a constructive witness in Lean, not a promise.
   It applies to the defined aggregation structure. It does not claim
   universal anonymization.

5. **Check the commons_phase_status table.**
   This is the authoritative verification ledger. Query it to confirm
   component status rather than relying solely on narrative text.

6. **Know what is not claimed.**
   Recursive self-assessment is `not_claimed` and must not be described as
   implemented. The runner completes cycles. It does not auto-calibrate
   thresholds. That boundary is intentional.

7. **Connect the commons to MountainShares governance.**
   The k-thresholds are governance commitments encoded in formally verified
   code — not configuration parameters that can be quietly changed.

8. **Correct all prior "Planned Phase 3" text.**
   Any text in the monograph describing these four components as planned,
   unbuilt, or future work must be updated to `formal_verified_20260728`.
   The July 2026 gate supersedes all prior draft language.

---

## 51.12 What This Chapter Does Not Claim

To remain within the gate, this chapter does not claim:

- Recursive self-assessment or auto-calibration of gate thresholds
- Universal anonymization guarantees beyond k-threshold enforcement and the
  noninvertibility proof's formal model
- That the commons protects against side-channel attacks outside the
  aggregation pathway
- Clinical, legal, or universal safety guarantees
- That the commons is complete in every possible future dimension

It claims only:

- Four formally verified components, machine-checked in Lean,
  recorded as `formal_verified_20260728`
- K_MIN = 5 and K_SENSITIVE = 10 enforced by the A_k operator
- A noninvertibility proof by constructive witness in Lean
- A live runtime (`jarvis-epistemic-runner`) completing cycles on `qualia-net`
- The Chapter 50 prerequisite satisfied

---

## 51.13 Closing Statement

The Community Hilbert Commons is formally verified.

Four components — the H_commons space, the A_k aggregation operator with
K_MIN = 5 and K_SENSITIVE = 10, provenance certificates, and the
noninvertibility proof — have been machine-checked in Lean and recorded as
`formal_verified_20260728` in the production database.

The prerequisite is satisfied. The live runtime is running. The governance
framework is in place.

For rural developers in Mount Hope and across Appalachia, the practical
consequence is this: communities can share patterns with each other — about
infrastructure needs, about resource gaps, about mutual aid opportunities —
without any individual household being exposed. The mathematics proves it.
The governance enforces it. The runtime runs it.

The commons is not a promise. It is a proof.

---

*Chapter 51 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
*Sealed: July 29, 2026 — July 2026 Production Gate.*
*Status: Formally Verified. All four components: formal_verified_20260728.*
*Lean artifact: RuntimeNontrivialCollision.lean — successful build confirmed.*
*Chapter 50 prerequisite: satisfied.*
*Recursive self-assessment: not_claimed — Phase 2 deferral, intentional.*
