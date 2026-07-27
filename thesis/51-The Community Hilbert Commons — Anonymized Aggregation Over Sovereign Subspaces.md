# 51. The Community Hilbert Commons — Anonymized Aggregation Over Sovereign Subspaces

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 51.1 What This Chapter Is Allowed to Claim

Within this gate, Chapter 51 may claim that:

- the **community commons gateway** is live on port 8055;
- a `community_hilbert_commons` collection **exists in Chroma**;
- **private people-space collections remain separate** from commons;
- commons aggregation requires **public opt-in** on contributing records;
- the aggregator **suppresses groups below `K_MIN`**;
- **sensitive groupings require `K_SENSITIVE`** and are suppressed if they fall below it;
- permitted commons outputs contain **centroid and provenance only**, and do **not** retain source user hashes;
- BBB, guardian, and Chroma **health checks pass**;
- focused Chapter 51 tests **pass**;
- the **k-anonymity threshold of k ≥ 5** is architecturally committed, derived from prior census work with West Virginia block-group population distributions;
- the **MountainShares governance connection** references Chapter 31 infrastructure as the organizational authority layer for commons decisions in this deployment.

It must **not** claim:

- mathematical impossibility of re-identification under all attacks;
- raw publication of personal subspaces;
- commons access to private \(H_p\) records;
- a universal anonymization guarantee;
- clinical or legal safety guarantees;
- that the four formal commons components — commons space, aggregation operator, provenance certificates, and noninvertibility — are implemented end-to-end beyond the architectural commitment stage.

---

## 51.2 Plain-Language Purpose for Rural Developers

For rural operators, this chapter answers:

> "If people in a community choose to share some of their data, how does Ms. Allis turn that into *community-level patterns* without exposing private histories?"

This chapter explains, step by step:

- how the **Community Hilbert Commons service** works;
- how it uses **k-thresholds** to decide what can be shown;
- how it keeps **private people-space separate** from commons;
- what information **does** and **does not** appear in a commons record;
- which components are **running today** and which remain **planned for Phase 3**;
- how the **MountainShares governance infrastructure** (Chapter 31) provides the organizational authority for commons decisions in this Appalachian deployment.

It describes **what exists today** and is honest about what is still planned.

---

## 51.3 The Commons Gateway and Collection

The as-built commons stack has two main pieces:

- a **gateway service** on port 8055;
- a **vector collection** in Chroma named `community_hilbert_commons`.

The gateway:

- receives aggregation requests;
- talks to Chroma to read or write commons vectors;
- applies **k-threshold and sensitivity rules** before permitting an output.

The `community_hilbert_commons` collection:

- holds **commons-level vectors and metadata**;
- does **not** store user-level identifiers or per-user subspace names;
- is the **only collection** where commons vectors are stored.

This separates "community-wide patterns" (in `community_hilbert_commons`) from "individual histories" (in per-user or civic collections).

---

## 51.4 Sovereign Subspaces and Commons Separation

The gate confirms that **private people-space collections remain separate from commons**.

In practice:

- per-user people-space and per-user conversation collections **are not read** by the commons aggregator;
- the gateway uses **only public-opt-in, commons-eligible sources**;
- there is **no code path** that lets the commons service read directly from private \(H_p\) partitions.

For rural communities, this means:

- using Ms. Allis personally does **not** automatically make a user's private memory part of the commons;
- commons aggregation is built **on top of** sovereign subspaces, not *instead of* them.

---

## 51.5 Public Opt-In as a Hard Requirement

Commons aggregation **requires public opt-in**.

On each candidate source record, the aggregator expects a flag like:

- `public_opt_in: true` for commons-eligible contributions;
- `public_opt_in: false` otherwise.

The gateway:

- **skips or suppresses** records without public opt-in;
- builds commons groups **only** from records where public opt-in is explicitly true.

This means:

- opt-in is **stored as data**, not assumed;
- there is no "silent inclusion" in the commons;
- if a record's opt-in flag is removed or turned off, it is **no longer a commons candidate**.

---

## 51.6 k-Thresholds: `K_MIN`, `K_SENSITIVE`, and the k ≥ 5 Architectural Commitment

The commons aggregator enforces **k-anonymity-style thresholds**:

- `K_MIN` — the minimum group size for **any commons output**;
- `K_SENSITIVE` — a higher minimum group size for **sensitive groupings**.

The gate confirms:

- "Commons aggregation suppresses groups below `K_MIN`";
- "Sensitive metadata requires `K_SENSITIVE`".

In practice:

- if a candidate group (for example, "people matching filter X") has **fewer than `K_MIN` members**, the gateway returns **no commons record** for that group;
- if a group involves **sensitive attributes** (for example, marginalized status or certain health-like signals) and is **below `K_SENSITIVE`**, it is suppressed even if it is above `K_MIN`.

This is how the system avoids answering "What is the vector for this group of 2 people?" — the answer is: "No commons vector; group too small."

### 51.6.1 The k ≥ 5 Architectural Commitment

The specific threshold **k ≥ 5** is architecturally committed for this deployment, derived from prior census work with West Virginia block-group population distributions. Census block groups in rural West Virginia frequently have populations in the low hundreds. Setting k below 5 in these distributions risks allowing aggregate outputs that are practically re-identifiable given the small denominator. The prior census work established that k = 5 provides a defensible lower bound for community-level suppression in this geography, while still permitting meaningful aggregation over groups of sufficient size.

This threshold is **architecturally committed** — it is the agreed design constraint — but the full formal proof of noninvertibility under this threshold is part of the Phase 3 commons mathematics work described in §51.13. The commitment means: no deployment of commons aggregation in this system may use a threshold below k = 5 without an explicit gate-level review.

For rural developers, k ≥ 5 means: "If fewer than five households or participants are represented in a commons group, the answer is silence, not a weak estimate."

---

## 51.7 What a Commons Record Contains (Centroid + Provenance, No User Hashes)

The gate states: "Permitted commons output records centroid and provenance while not retaining source user hashes."

A permitted commons record includes:

- a **centroid vector**: the average or representative embedding for the group;
- **provenance metadata**: high-level information about which **sources and filters** generated the group (for example, "derived from public_civic_statements with opt-in true, filtered by region and time window").

It explicitly does **not** include:

- raw user IDs;
- per-user subspace names;
- per-user hashes or stable per-user tokens.

In plain language:

- the commons record tells you **"what this group looks like as a whole"**;
- it does **not** tell you **"who the individuals in the group are"**.

---

## 51.8 Sensitive Metadata Handling

If aggregation involves attributes considered **sensitive** (for example, certain kinds of inferred hardship or vulnerable status), then:

- **only groups reaching `K_SENSITIVE` or higher** can produce a commons record;
- below that size, the gateway returns **no record**.

There are effectively **two k-filters**:

- one general (`K_MIN`);
- one for sensitive material (`K_SENSITIVE` ≥ `K_MIN`).

This gives the system a way to:

- still compute **some** community-level patterns in sensitive areas;
- but **only when enough people** are represented that individual inference becomes harder.

---

## 51.9 MountainShares Governance Connection (Chapter 31)

The commons layer does not make governance decisions in isolation. Decisions about which sources are commons-eligible, which sensitivity categories require elevated thresholds, and which communities may access aggregated outputs are governed through the **MountainShares infrastructure** described in Chapter 31.

Chapter 31 establishes the organizational authority layer for this deployment: the cooperative governance model that treats data as a shared community resource rather than a platform asset. The Community Hilbert Commons extends that infrastructure into the vector and governed-state layer:

- **commons eligibility rules** (which opt-in sources are accepted) trace back to MountainShares cooperative membership and consent agreements;
- **sensitivity categorization** (what attributes require `K_SENSITIVE`) is set by the MountainShares governance process, not by a technical parameter alone;
- **access policy** (who may query commons outputs and for what purposes) references Chapter 31 role and purpose constraints.

For rural developers, this means: the k-thresholds and suppression rules are not just database parameters. They are expressions of an organizational commitment made in Chapter 31. Changing them requires governance review at the MountainShares level, not just a configuration file edit.

---

## 51.10 BBB, Guardian, and Health Checks

The gate confirms that:

- **BBB and guardian checks** for the commons pathway pass;
- **Chroma health checks** pass;
- focused Chapter 51 tests **pass**.

This shows:

- commons aggregation is not a "sidecar" bypassing governance;
- the same safeguard stack (BBB, guardian) used elsewhere still applies when the system builds or serves commons vectors;
- Chroma is healthy for commons operations.

For rural developers, this means that commons aggregation is **wired into the same guard system** as other authority-bearing operations, not an ungoverned background job.

---

## 51.11 Step-by-Step View for Rural Developers

At this gate, the Community Hilbert Commons works like this:

1. **People and civic sources exist in sovereign subspaces.**
   - Per-user and civic collections hold their own records separately.

2. **Some records are marked `public_opt_in: true`.**
   - Only these records are considered for commons.
   - Opt-in is governed by MountainShares consent agreements (Chapter 31).

3. **The commons gateway on port 8055 receives an aggregation request.**
   - It may specify filters (location, time window, topic, etc.).

4. **The gateway selects only opt-in records via the manifest/resolver.**
   - It never reads private \(H_p\) collections.
   - It uses only commons-eligible civic or public sources.

5. **Records are grouped, and group sizes are counted.**
   - If a group is smaller than `K_MIN` (minimum k = 5), it is suppressed.
   - If sensitive fields are involved and the group is smaller than `K_SENSITIVE`, it is suppressed.

6. **For permitted groups, the gateway computes a centroid.**
   - It writes/reads centroid vectors into/from `community_hilbert_commons`.
   - It records high-level provenance (where the group came from, not who).

7. **The gateway returns commons vectors and provenance.**
   - It **never returns user IDs** or per-user hashes.
   - Under-threshold groups yield **no result**, not a "weak" result.

That is the "anonymized aggregation over sovereign subspaces" in running code.

---

## 51.12 What This Chapter Does Not Claim

To stay within the gate, this chapter does **not** claim:

- that re-identification is mathematically impossible under all future attack models;
- that people's private subspaces are never at risk under misconfiguration or misuse;
- that commons access could never be misused by an external actor;
- a universal anonymization guarantee;
- clinical or legal safety guarantees;
- that the four formal commons components are fully implemented (see §51.13).

It only claims:

- as-built **k-thresholded aggregation** over public-opt-in contributions;
- **commons/private separation** in the code paths and collections used;
- **centroid + provenance** structure for permitted commons records;
- **suppression** of under-threshold and sensitive-under-threshold groups;
- passing **governance and health checks** for the commons gateway;
- **architectural commitment** of k ≥ 5 derived from prior census work;
- **MountainShares governance** as the organizational authority layer (Chapter 31).

---

## 51.13 Implementation Status Addendum — As-Built and Planned (July 27, 2026)

This addendum is the honest accounting of what is running, what is architecturally committed, and what remains planned. It uses the same two-register discipline as Appendix A: **demonstrated** means a real path has been exercised and confirmed; **planned** means the design is committed but end-to-end exercise has not yet occurred.

---

### 51.13.1 Status of the Four Formal Commons Components

The mathematical formalization of the Community Hilbert Commons has four components. Their implementation status is:

| Component | Formal Role | Implementation Status |
|---|---|---|
| **Commons space** \(H_{\text{commons}}\) | The shared vector space into which opt-in contributions are projected for aggregation | **Planned Phase 3** — the Chroma `community_hilbert_commons` collection provides the operational container, but the formal projection mapping from \(H_p\) to \(H_{\text{commons}}\) has not been defined, implemented, or end-to-end exercised |
| **Aggregation operator** \(\mathcal{A}_k\) | The k-thresholded operator that maps a set of opt-in contributions to a centroid, suppressing groups below k | **Planned Phase 3** — the gateway enforces k-suppression rules operationally, but the formal operator definition with proof of k-anonymity properties under the WV block-group distribution has not been completed |
| **Provenance certificates** | Structured attestations that record which filters, sources, and thresholds produced a given commons record | **Planned Phase 3** — the gateway records high-level provenance metadata today, but a formal certificate structure with verifiable provenance chain has not been implemented or gated |
| **Noninvertibility** | The formal property that no commons output can be inverted to recover individual contributions | **Planned Phase 3** — the k ≥ 5 threshold and the centroid-plus-provenance structure make inversion practically difficult, but a formal noninvertibility proof under this deployment's parameters has not been completed |

All four remain **Planned Phase 3**, gated on Chapter 50 per-user partition completion. The dependency is direct: the commons projection operator cannot be formally defined until the per-user partition structure (Chapter 50) is stable enough to specify what is being projected from. Phase 3 commons mathematics will be opened only after the Chapter 50 gate closes.

For rural developers, this means: the suppression rules and opt-in enforcement are running and protecting community members today. The formal mathematical proof that those protections are sufficient under all attack models is the Phase 3 work. The system is being honest about that distinction.

---

### 51.13.2 The k ≥ 5 Architectural Commitment — Derivation and Binding Force

The k ≥ 5 threshold is not an arbitrary configuration value. It is an **architecturally committed constraint** derived from prior census work examining West Virginia block-group population distributions.

The derivation reasoning:

- WV rural block groups frequently contain 200–800 residents;
- at these population sizes, a group of 2 or 3 members sharing a distinctive attribute (for example, a specific employer, a specific health signal, or a specific civic statement type) can be practically re-identified by a motivated local actor even without user IDs;
- k = 5 was established as the lower bound that, in WV rural distributions, prevents the smallest commons groups from being trivially matchable against known community members;
- this threshold was confirmed against block-group population data from the authoritative WV spatial domain used throughout the GBIM corpus.

The binding force of this commitment:

- **No configuration change** to `K_MIN` below 5 may be made without a gate-level review that re-examines the census basis;
- **No new deployment** of commons aggregation in this system may use a lower threshold without equivalent census-grounded justification for the target geography;
- the threshold is recorded here, in the thesis, so that future maintainers understand its origin and cannot silently lower it without encountering this documentation.

The formal proof that k = 5 is *sufficient* (not merely *committed*) for noninvertibility under WV distributions is part of the Phase 3 work in §51.13.1. The commitment and the proof are different things: the commitment is binding now; the proof is pending.

---

### 51.13.3 Chapter 50 Per-User Partition Dependency

All four Phase 3 commons components are gated on **Chapter 50 per-user partition completion** for the following reason:

The commons projection operator \(\mathcal{A}_k\) must know what it is projecting *from*. It takes contributions out of per-user partitions and places them into the shared commons space. If the per-user partition structure is still in flux — if the schema, namespace rules, and isolation guarantees of Chapter 50 are not yet closed — then defining the projection formally would be premature. A formal operator defined against an unstable partition structure would need to be rewritten when Chapter 50 closes, creating unnecessary rework and potentially introducing gaps in the privacy boundary.

The gating order is therefore:

1. Chapter 50 per-user partition gate closes (per-user structure stable and verified);
2. Phase 3 commons work opens (formal operator, provenance certificates, noninvertibility proof);
3. Phase 3 gate closes (four components demonstrated);
4. Chapter 51 advances from "architecturally committed" to "formally proven."

For rural developers, this is the same logic as not installing a roof before the walls are load-bearing. The commons layer sits on top of the per-user partition layer. The partition layer must be solid first.

---

### 51.13.4 MountainShares Governance — What Chapter 31 Provides

The MountainShares governance connection (Chapter 31) provides three things to the commons layer that the technical stack cannot provide on its own:

1. **Organizational consent authority** — MountainShares cooperative agreements are the legal and social basis on which `public_opt_in: true` is meaningful. Without an organizational framework that community members trust and have agreed to, the opt-in flag is just a database column. Chapter 31 establishes that framework.

2. **Sensitivity categorization authority** — The determination that a particular attribute type requires `K_SENSITIVE` rather than `K_MIN` is a governance decision, not a technical one. Who decides that "inferred economic hardship" is a sensitive category? Chapter 31's cooperative governance process decides. The technical layer enforces whatever sensitivity map the governance process produces.

3. **Access policy authority** — Who may query commons outputs, for what purposes, and under what accountability conditions? These are Chapter 31 questions. The commons gateway enforces access policy, but it does not set it. MountainShares governance sets it, and the gateway implements it.

For rural developers: the k-thresholds in the code are the enforcement layer. Chapter 31 is the authority layer. Neither works without the other.

---

### 51.13.5 Demonstrated vs. Planned Summary

| Capability | Status | Evidence |
|---|---|---|
| Commons gateway live on port 8055 | **Demonstrated** | Service running; BBB, guardian, and Chroma health checks pass |
| `community_hilbert_commons` collection in Chroma | **Demonstrated** | Collection confirmed present at July gate |
| Private \(H_p\) separation from commons | **Demonstrated** | No code path from commons gateway to private per-user collections |
| Public opt-in enforcement | **Demonstrated** | Gateway skips records with `public_opt_in: false` |
| k-suppression (`K_MIN`, `K_SENSITIVE`) | **Demonstrated** | Groups below threshold return no commons record |
| Centroid + provenance output (no user hashes) | **Demonstrated** | Commons records contain centroid and high-level provenance only |
| k ≥ 5 architectural commitment | **Architecturally committed** | Derived from WV census work; binding constraint on all deployments |
| MountainShares governance connection | **Architecturally committed** | Chapter 31 infrastructure named as organizational authority layer |
| Formal commons space \(H_{\text{commons}}\) | **Planned Phase 3** | Gated on Chapter 50 per-user partition completion |
| Formal aggregation operator \(\mathcal{A}_k\) | **Planned Phase 3** | Gated on Chapter 50 per-user partition completion |
| Provenance certificates (verifiable chain) | **Planned Phase 3** | Gated on Chapter 50 per-user partition completion |
| Formal noninvertibility proof | **Planned Phase 3** | Gated on Chapter 50 per-user partition completion |

---

## 51.14 Closing Statement

Chapter 51 presents the Community Hilbert Commons at two levels of resolution.

At the operational level, the system is running: the gateway on port 8055 aggregates only public-opt-in contributions, private people-space remains separate, groups must meet k ≥ 5 (and `K_SENSITIVE` for sensitive attributes), permitted outputs contain only centroids and high-level provenance, and under-threshold groups are suppressed. The k ≥ 5 threshold is architecturally committed, grounded in prior census work with West Virginia block-group populations, and binding on all deployments in this system. Governance authority for commons decisions traces back to MountainShares cooperative infrastructure in Chapter 31.

At the formal mathematical level, four components — commons space, aggregation operator, provenance certificates, and noninvertibility — remain Planned Phase 3, gated on Chapter 50 per-user partition completion. This is not a gap in the operational system; it is an honest accounting of where the formal proof work stands. The system is protecting community members today with the operational layer. The Phase 3 work will provide the formal proof that those protections are provably sufficient.

For rural communities in Appalachia, this chapter is a commitment: the patterns that belong to a community can be computed and used to benefit that community, without those patterns being traceable back to individual households or individuals — under the rules stated here, governed by the organizations and agreements stated in Chapter 31, and only when the mathematics of Phase 3 have been closed.

---

*Chapter 51 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
