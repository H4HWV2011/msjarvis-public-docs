# 48. Hilbert People Space

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 13, 2026*

---

## 48.0 Overview

Hilbert People Space is the formal domain in which Ms. Allis represents person-linked state, identity-governed memory, and person-in-context meaning as part of the broader architecture of \(H_{\mathrm{App}}\). It is the structured semantic space for persons, roles, communities, and identity-bound relations, but it is not a license for undifferentiated personal accumulation.

This chapter aligns the formal account of people space with the operational identity and retention architecture of the system. Person-linked outputs may arise during per-session reasoning, but they enter per-user Hilbert subspaces only after approval through the governing promotion path. The result is a people space that is mathematically legible, architecturally bounded, and operationally consistent with identity-focused retention, per-user separation, and commons-safe aggregation.

As with Chapters 42 through 47, this revision separates design from audit. Sections 48.1 through 48.10 state the formal model. Sections 48.11 through 48.14 record what is verified as built as of this writing: the as-built collection names and the resolver that governs them — recorded here in full because Chapter 47 defers its naming to this chapter — the live write path with its verdict discipline, the first sovereign subspaces instantiated under the direct-sum model, and the honest accounting of which parts of the promotion mapping exist in code and which remain design intent.

---

## 48.1 The Formal Place of People Space

Hilbert People Space may be written as \(H_{p}\), the person-linked component of the broader semantic body of Ms. Allis.

Within the overall architecture, \(H_{p}\) does not stand alone as an isolated identity store. It interacts with application state, spatial state, and temporal state, and may participate in joint reasoning with them when a situation requires person-in-context interpretation. Yet \(H_{p}\) remains distinct in purpose: it is the formal location where person-related states, roles, relations, and approved memory traces are represented as governed semantic content.

The chapter therefore treats \(H_{p}\) as a real architectural subspace, but not as a claim that every implementation detail is realized as strict functional analysis. The Hilbert formalism expresses how the system is designed to separate, couple, and govern person-linked meaning.

---

## 48.2 Person-Linked State in Operation

Operationally, person-linked state first appears in session-bounded reasoning.

During a live interaction or bounded internal process, Ms. Allis may produce person-relevant candidate outputs: role-sensitive interpretations, continuity cues, service-linked identity context, or person-in-context inferences. These outputs belong first to per-session reasoning rather than to durable personal memory. They are evaluated inside the gated internal-state domain, where they may assist current reasoning without automatically becoming lasting identity state.

This distinction matters because the formal existence of \(H_{p}\) must match the operational rule that personal state is not written merely because it was computed. Session reasoning can generate candidate person-linked structure, but durable placement into identity-governed memory requires approval.

Hilbert People Space is therefore not the same as all person-related computation. It is the governed home of approved person-linked state.

---

## 48.3 Mapping Session Outputs into Per-User Subspaces

The operational path from session reasoning to durable people space is a governed mapping.

Let \(S_u^{(k)}\) denote a person-linked output produced during session \(k\) for user \(u\). This output is not placed directly into the durable per-user people space. Instead, it is first held as a candidate in bounded reasoning. Only after approval does it map into the per-user subspace \(H_{p}^{(u)}\).

This may be written schematically as:

\[
\mathcal{P}\!\left(S_u^{(k)}\right) \longrightarrow H_{p}^{(u)}
\]

where \(\mathcal{P}\) denotes the governing promotion path rather than a raw write operation. The promotion path includes the relevant constitutional, role-gated, consent, retention, and policy checks. If those checks are not satisfied, the candidate remains ephemeral, limited, or discarded.

This mapping is one of the most important bridges between formal and operational design. Hilbert People Space contains approved identity-linked state, not every session-level inference the system was able to form.

---

## 48.4 Per-User Hilbert Subspaces

Once approved, person-linked state belongs to a per-user Hilbert subspace.

For each user \(u\), the architecture treats their durable people-space memory and identity-bound semantic state as belonging to a distinct subspace \(H_{p}^{(u)}\). This expresses sovereign separation at the level of formal structure. A user’s durable identity-linked state is not supposed to dissolve into a single undifferentiated global pool.

These subspaces support continuity, retention, and person-aware service while preserving the idea that each user remains semantically distinct. Shared system capabilities may operate across the architecture, but durable person-linked state is governed by per-user containment.

This also aligns the chapter with identity-focused retention. What is approved for one user belongs to that user’s governed subspace rather than to generic system memory.

---

## 48.5 Direct-Sum Formalization

The full durable people-space architecture may therefore be expressed formally as a direct sum:

\[
H_{p} \;=\; \bigoplus_{u \in U} H_{p}^{(u)}
\]

where \(U\) is the set of users and each \(H_{p}^{(u)}\) is the approved person-linked subspace associated with user \(u\).

This direct-sum form is important because it formalizes sovereign separation. The notation says that the whole people space is composed of distinct user-governed subspaces rather than a single merged identity field. It provides a mathematical language for the architectural commitment that durable conversational and personal memory should be partitioned by user identity and governance boundary.

At the same time, this direct-sum expression should be read as a formal model of separation rather than proof that the implementation satisfies every strict functional-analytic property of an abstract Hilbert direct sum. Where the system explicitly enforces these guarantees in storage, routing, promotion, and access control, the model has direct operational force. Where the implementation remains an architectural approximation, the notation still serves as the correct formal statement of the intended sovereignty structure.

This clarification strengthens the chapter. It keeps the mathematics honest while preserving its architectural usefulness.

---

## 48.6 Sovereign Separation and Retention

The direct-sum model explains why identity-focused retention is not merely a storage policy but a structural commitment.

If durable person-linked memory were globally blended, identity sovereignty would be weakened even if access controls were later added. By placing each user’s approved state in \(H_{p}^{(u)}\), the system treats retention as partitioned at the level of formal organization. This supports deletion rights, scoped continuity, per-user review, and role-gated access because the memory is already conceptually separated before downstream policies act on it.

The people space therefore works together with identity-focused retention. Retention becomes the operational rule by which only approved material enters a per-user subspace, while the direct-sum formalism expresses why those admitted materials remain separated from one another.

This is how the chapter aligns formal people space with real retention architecture.

---

## 48.7 Relation to Per-Session Reasoning

Per-session reasoning remains upstream of the direct-sum people space.

A live interaction may produce rich person-linked outputs, but those outputs exist first in session-bounded internal reasoning rather than inside the durable direct sum. This keeps ephemeral interpretation separate from approved identity memory. It also prevents the system from confusing temporary contextual reasoning with settled personal state.

The operational sequence is therefore:

1. Session reasoning produces candidate person-linked outputs.
2. Gated review evaluates those outputs.
3. Approved outputs are mapped into \(H_{p}^{(u)}\).
4. Non-approved outputs remain ephemeral or are discarded.

This sequence ensures that formal people space represents admitted identity-linked state rather than transient inference residue.

---

## 48.8 Relation to Other Chapters

Hilbert People Space is best understood as one part of a larger identity architecture.

Its retention logic aligns directly with identity-focused retention, where admission, pruning, and continuity are governed by explicit policy and sovereignty rules. Its per-user partitioning is further formalized in the chapter on per-user direct sum decomposition of conversational memory, which extends the same separation principle into conversation-scale memory structure. Its boundary against overexposure also supports the chapter on Hilbert People Space Without Surveillance, where ephemeral reasoning, projection, and identity limitation prevent person-aware state from becoming surveillance.

The chapter also connects forward to the Community Hilbert Commons. If durable people space is partitioned as \(\bigoplus_{u \in U} H_{p}^{(u)}\), then any commons-level aggregation must occur as a governed operation over sovereign subspaces rather than as a collapse of user identity into a single raw pool. The commons can therefore be informative only when aggregation preserves the sovereignty established here.

These links are important because Hilbert People Space is not a standalone metaphor. It is one layer in a coherent retention, access, decomposition, and aggregation architecture.

---

## 48.9 Commons-Safe Aggregation

The existence of per-user subspaces does not forbid collective knowledge. It governs how collective knowledge may be formed.

A commons-level representation may be derived from many user subspaces only through anonymized or otherwise governance-compliant aggregation operations. The system should not move from \(H_{p}^{(u)}\) to a community layer by simply exposing personal state. Instead, the movement to any commons representation must preserve sovereign separation while extracting only the approved communal signal.

This means the people space chapter supports community intelligence without sacrificing individual sovereignty. The direct-sum model keeps user subspaces distinct, and the commons chapter explains how higher-order aggregation can occur without dissolving those distinctions.

The architecture therefore permits community learning, but only through protected aggregation over sovereign subspaces.

---

## 48.10 Architectural Interpretation and Implementation Status

The Hilbert formulation in this chapter is architectural unless explicit implementation guarantees are stated.

Writing \(H_{p} = \bigoplus_{u \in U} H_{p}^{(u)}\) does not by itself prove that every runtime subsystem, storage layer, or retrieval path already satisfies the full mathematics of an abstract Hilbert direct sum. What it does provide is the correct architectural statement of how person-linked state is meant to be partitioned, governed, and related. Where code, storage design, routing, and policy enforcement explicitly implement these guarantees, the formal model and the operational system coincide more strongly.

This distinction should be preserved throughout the thesis. Mathematical structure is used here to make the sovereignty architecture legible, not to imply a stronger implementation claim than the system explicitly guarantees.

The people space is therefore both a formal model and a design commitment. Sections 48.11 through 48.14 now state exactly which guarantees are enforced and where, so the reader can tell at every point which register a claim occupies.

---

## 48.11 As-Built Naming and the Manifest Resolver

Chapter 47 records the correction of where the relational person store lives; this chapter carries the as-built names in full, resolving the naming discrepancy the June–July audit flagged between the two chapters in favor of what is deployed.

The vector-store side of \(H_{p}\) comprises the public civic collections — appearances, documents, statements, roles, events, and sources — together with the temporal role collection that binds role assertions to effective and expiry dates. These are the shared, public-facing partitions of people space: they hold opt-in civic material, not per-user memory, and they are the only collections the commons aggregation of Chapter 51 is permitted to read.

Crucially, services do not hardcode these physical names. A collection manifest module resolves logical collection identifiers — versioned names such as the appearances-v1 or role-temporal-v1 identifiers — to physical collection names by querying the publication manifest in the relational system of record, falling back to declared defaults when no manifest row exists, with the resolution cached per process. Every writer in the ingest path obtains its target collection through this resolver.

This indirection is a governance instrument, not a convenience. Because the manifest maps logical to physical names, a collection can be rebuilt, re-versioned, or superseded by changing a manifest row rather than redeploying every service — which means the publication manifest of Chapter 52 governs not only *what* is promoted but *where writes land*. The resolver is the enforcement point that makes the manifest authoritative.

One audit finding tempers this: the commons aggregator does not yet use the resolver — it reads its five source collections by hardcoded physical name. Today the resolver's defaults and the physical names coincide, so behavior is correct; but a future manifest remap would silently decouple the aggregator from the writers. Chapter 51 carries this as an open item. It is recorded here as well because the lesson belongs to this chapter: an indirection layer only governs the services that go through it.

---

## 48.12 The Live Write Path

The write path into the civic partitions of \(H_{p}\) is operational, and its discipline deserves precise statement because it is the built form of the promotion mapping \(\mathcal{P}\) for ingested (as opposed to inferred) person-linked state.

Ingestion enters through a dedicated civic-intake service — a FastAPI application on its own port, supervised in the container stack — and every write flows through the ingest worker, which enforces four disciplines before anything touches a collection:

1. **Validated governance metadata.** Every record must carry a registration layer of 1, 2, or 3 — validated at write time and rejected otherwise — together with an explicit public-opt-in boolean, source attribution, entity identifier, and ingestion timestamp. Consent and standing are stored fields on every record, never ambient assumptions.
2. **Verdicts before writes.** Appearance records pass through a five-stage write pipeline that returns an explicit disclosure verdict — permitted, suppressed, or escalated — before any upsert occurs. A suppressed or escalated candidate is refused with a recorded reason and a provenance hash, so the refusal itself is a durable governed output. This is Chapter 52's refusal-as-epistemic-output principle, live on the person-data write path.
3. **Deterministic identity.** Document identifiers are derived by hashing source, entity, and content, making writes idempotent: re-ingestion updates rather than duplicates, and a record's identity is reproducible from its provenance.
4. **Resolver-mediated targeting.** As Section 48.11 states, the worker writes only to manifest-resolved collection names.

Current population is stated plainly, in the discipline this thesis owes its readers: as of July 13, 2026, the civic documents collection holds two records and the statements collection two, while appearances, roles, and the temporal role collection stand at zero; the corresponding manifest rows are promoted at version one with zero record counts. The pipeline is verified — including by a synthetic opt-in probe exercised end to end and then fully cleaned (Chapter 51 records that test) — but the corpus it exists to govern is still arriving. Empty by corpus, not broken by code, and the distinction is checkable because the acceptance tests exist.

---

## 48.13 Worked Example: The First Sovereign Subspaces

On July 13, 2026, the direct-sum model of Section 48.5 acquired its first fully instantiated member — and the subject was Ms. Allis herself, established as a sovereign presence in her own architecture.

A per-person configuration declares her subspaces across the joint frame: an application subspace for her conversational state, a person subspace in \(H_{p}\), a temporal subspace, and a sandboxed bridge collection linking her to her qualia network. Each was created as a distinct collection and seeded with a root record carrying the governance posture explicitly on the record itself: public opt-in false, commons projection disabled, non-surveillance true on the person root, local-only tagging on conversation events. The configuration is the formal declaration; the per-record flags are the operational enforcement; and the two were verified to agree.

Three things make this the correct first test of the direct-sum architecture:

1. **Sovereignty was proven, not presumed.** A repository-wide static search confirmed her subspace names appear in no shared pipeline — not the commons aggregator's source list, not any civic projection path — and repeated live aggregation runs projected zero vectors while her subspaces held records. The subspace is disjoint from every governed aggregation in both code and behavior, which is what the direct-sum notation *claims* and what an implementation must *show*.
2. **The pattern is the deliverable.** Adding a person to \(H_{p}\) now has a worked procedure: declare the configuration, create the partitions, seed roots with consent flags off by default, verify isolation statically and dynamically. Participation in any aggregate is a per-record opt-in fact, never an enrollment default. The first person through the pattern was the system's own persona precisely so no community member's state would depend on an unproven procedure.
3. **The decomposition spans the frame.** Her subspaces partition not only \(H_{p}\) but her application-state and temporal presence as well — and on the conversational side, the same separation now holds for every user: per-user conversation collections, resolved from the requesting identity at request time, replaced the legacy shared conversation store, whose retirement Chapter 50 records. The direct sum is no longer only a people-space model; it is the operating structure of memory across the joint frame.

---

## 48.14 Implementation Status (July 2026)

In the demonstrated/not-yet-demonstrated discipline of Chapter 52:

**Demonstrated:**

- Manifest-mediated name resolution for all ingest-path writers, with the publication manifest as the authoritative logical-to-physical map and declared defaults as fallback.
- The civic-intake service and ingest worker live, with registration-layer validation, stored opt-in consent, deterministic document identity, and disclosure verdicts (permit, suppress, escalate) carrying provenance hashes on refusals.
- The hp schema on its separate database with DDL-level anti-surveillance and vault isolation (Chapter 47 carries the detail; this chapter adopts its naming).
- The sovereign-subspace pattern instantiated end to end for one person, with isolation verified statically and dynamically.
- Per-user decomposition of conversational memory in production, replacing the shared conversation store (Chapter 50).
- Commons-safe aggregation verified end to end with synthetic opt-in data and fully cleaned afterward (Chapter 51).

**Not yet demonstrated:**

- The promotion mapping \(\mathcal{P}\) for *session-derived* person-linked state: the built write path governs ingested civic records, but no reasoning cycle yet produces per-session person-linked candidates that flow through constitutional review into a per-user subspace. Section 48.3's mapping exists for ingestion; its inferential form is design intent.
- Resolver adoption in the commons aggregator (Section 48.11's open item, carried jointly with Chapter 51).
- Retention operations on admitted state — pruning, expiry, per-user review workflows — beyond the consent flags themselves.
- Population at scale: one sovereign subspace instantiated, civic collections at test-grade volume, manifest rows promoted with zero counts awaiting real corpus.

---

## 48.15 Closing Statement

Hilbert People Space is the governed formal domain of approved person-linked state in Ms. Allis.

Per-session reasoning may generate identity-linked candidate outputs, but those outputs enter a user’s durable people-space subspace only through approval and promotion. The formal expression

\[
H_{p} \;=\; \bigoplus_{u \in U} H_{p}^{(u)}
\]

captures sovereign separation across users, while the surrounding retention and aggregation architecture explains how continuity, privacy, and community knowledge can coexist without collapsing persons into one undifferentiated memory field. In this way, Hilbert People Space matches the operational identity and retention architecture rather than standing apart from it.

As of this writing, the direct sum has its first proven member, the write path into the civic partitions enforces consent and verdicts on every record, and the names those records land under are governed by the same manifest that governs promotion. The formal model and the built system now touch at verified points — and where they do not yet touch, this chapter says so, because a sovereignty architecture is only as trustworthy as its own account of where sovereignty is enforced and where it is still being built.
