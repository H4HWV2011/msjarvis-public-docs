# 48. Hilbert People Space — Implementation-Aligned Revision  
Carrie Kidd (Mamma Kidd) — Mount Hope, WV — Last updated: July 16, 2026  

---

## 48.0 Overview  
Hilbert People Space (Hp) is the formal domain in which Ms. Allis represents person-linked state, identity-governed memory, and person-in-context meaning as part of the broader architecture of HApp. It is the structured semantic space for persons, roles, communities, and identity-bound relations, but it is not a license for undifferentiated personal accumulation.  

This chapter aligns the formal account of people space with the operational identity, storage, and retention architecture of the system as it actually exists in July 2026. Person-linked outputs may arise during per-session reasoning, but they enter per-user Hilbert subspaces only through governed promotion paths; ingested civic records enter only through validated intake pipelines. The result is a people space that is mathematically legible, architecturally bounded, and operationally consistent with identity-focused retention, per-user separation, and commons-safe aggregation at the scale currently demonstrated.  

As with Chapters 42 through 47, this revision separates design from audit. Sections 48.1 through 48.10 state the formal model. Sections 48.11 through 48.14 record what is verified as built as of this writing: the as-built civic and Hilbert collection names and the manifest resolver that governs them; the live intake and write path with its verdict discipline; the first sovereign subspaces instantiated under the direct-sum model; the fact that the civic corpus and commons are present but small; and the honest accounting of which parts of the promotion mapping exist in code and runtime and which remain design intent.  

---

## 48.1 The Formal Place of People Space  
Hilbert People Space may be written as Hp, the person-linked component of the broader semantic body of Ms. Allis.  

Within the overall architecture, Hp does not stand alone as an isolated identity store. It interacts with application state, spatial state, and temporal state, and may participate in joint reasoning with them when a situation requires person-in-context interpretation. Yet Hp remains distinct in purpose: it is the formal location where person-related states, roles, relations, and approved memory traces are represented as governed semantic content.  

This chapter therefore treats Hp as a real architectural subspace, but not as a claim that every implementation detail is realized as strict functional analysis. The Hilbert formalism expresses how the system is designed to separate, couple, and govern person-linked meaning; the implementation evidence recorded later shows which parts of that design are realized and which remain aspirational.  

---

## 48.2 Person-Linked State in Operation  
Operationally, person-linked state first appears in bounded reasoning contexts: live sessions and governed internal processes.  

During a live interaction or bounded internal process, Ms. Allis may produce person-relevant candidate outputs: role-sensitive interpretations, continuity cues, service-linked identity context, or person-in-context inferences. These outputs belong first to per-session reasoning rather than to durable personal memory. They are evaluated inside gated internal-state domains, where they may assist current reasoning without automatically becoming lasting identity state.  

This distinction matters because the formal existence of Hp must match the operational rule that personal state is not written merely because it was computed. Session reasoning can generate candidate person-linked structure, but durable placement into identity-governed memory requires approval and, for civic material, must arrive through the dedicated intake pipeline.  

Hilbert People Space is therefore not the same as “all person-related computation.” It is the governed home of approved person-linked state — whether derived from per-session reasoning (once the promotion path exists) or from opt-in civic intake.  

---

## 48.3 Mapping Session Outputs into Per-User Subspaces  
The intended operational path from session reasoning to durable people space is a governed mapping.  

Let \(S_u^{(k)}\) denote a person-linked output produced during session \(k\) for user \(u\). This output is not supposed to be placed directly into the durable per-user people space. Instead, it is first held as a candidate in bounded reasoning. Only after approval does it map into the per-user subspace \(H_p^{(u)}\).  

This may be written schematically as:  
\[
\mathcal{P}\big(S_u^{(k)}\big) \longrightarrow H_p^{(u)} \quad (48.3.1)
\]  
where \(\mathcal{P}\) denotes the governing promotion path rather than a raw write operation. The promotion path is defined to include constitutional, role-gated, consent, retention, and policy checks. If those checks are not satisfied, the candidate remains ephemeral, limited, or discarded.  

In July 2026, the promotion discipline \(\mathcal{P}\) is **fully implemented and demonstrated** for ingested civic records (Section 48.12), but **not yet implemented for session-derived person-linked outputs**. This chapter retains the formal mapping as the design commitment, and Section 48.14 explicitly records that the per-session promotion path is not yet demonstrated in code or runtime.  

---

## 48.4 Per-User Hilbert Subspaces  
Once approved, person-linked state belongs to a per-user Hilbert subspace.  

For each user \(u\), the architecture treats their durable people-space memory and identity-bound semantic state as belonging to a distinct subspace \(H_p^{(u)}\). This expresses sovereign separation at the level of formal structure. A user’s durable identity-linked state is not supposed to dissolve into a single undifferentiated global pool.  

These subspaces support continuity, retention, and person-aware service while preserving the idea that each user remains semantically distinct. Shared system capabilities may operate across the architecture, but durable person-linked state is governed by per-user containment.  

In the live system, this pattern has been instantiated concretely at least for one sovereign actor — Ms. Allis herself — via collections such as `h_people_ms_allis`, `h_app_user_ms_allis`, and `h_time_ms_allis`, with explicit governance posture on root records and verified isolation from civic and commons aggregations. Other users currently have per-user conversational collections; their formal \(H_p^{(u)}\) people-space subspaces are modeled and partially reflected in intake and storage, but the full session-derived promotion pipeline is not yet implemented.  

---

## 48.5 Direct-Sum Formalization  
The full durable people-space architecture may therefore be expressed formally as a direct sum:  
\[
H_p \;=\; \bigoplus_{u \in U} H_p^{(u)} \quad (48.5.1)
\]  
where \(U\) is the set of users and each \(H_p^{(u)}\) is the approved person-linked subspace associated with user \(u\).  

This direct-sum form is important because it formalizes sovereign separation. The notation says that the whole people space is composed of distinct user-governed subspaces rather than a single merged identity field. It provides a mathematical language for the architectural commitment that durable conversational and personal memory should be partitioned by user identity and governance boundary.  

At the same time, this direct-sum expression should be read as a **formal model of separation** rather than proof that the implementation satisfies every strict functional-analytic property of an abstract Hilbert direct sum. Where the system explicitly enforces these guarantees in storage, routing, promotion, and access control — for example, per-user conversation collections and Ms. Allis’s sovereign Hilbert collections — the model has direct operational force. Where the implementation remains an architectural approximation, the notation still serves as the correct formal statement of the intended sovereignty structure.  

This clarification strengthens the chapter. It keeps the mathematics honest while preserving its architectural usefulness.  

---

## 48.6 Sovereign Separation and Retention  
The direct-sum model explains why identity-focused retention is not merely a storage policy but a structural commitment.  

If durable person-linked memory were globally blended, identity sovereignty would be weakened even if access controls were later added. By placing each user’s approved state in \(H_p^{(u)}\), the system treats retention as partitioned at the level of formal organization. This supports deletion rights, scoped continuity, per-user review, and role-gated access because the memory is already conceptually separated before downstream policies act on it.  

The people space therefore works together with identity-focused retention. Retention becomes the operational rule by which only approved material enters a per-user subspace — via intake pipelines today and via session promotion once implemented — while the direct-sum formalism expresses why those admitted materials remain separated from one another.  

This is how the chapter aligns formal people space with real retention architecture, both as it exists and as it is intended to evolve.  

---

## 48.7 Relation to Per-Session Reasoning  
Per-session reasoning remains upstream of the direct-sum people space.  

A live interaction may produce rich person-linked outputs, but those outputs exist first in session-bounded internal reasoning rather than inside the durable direct sum. This keeps ephemeral interpretation separate from approved identity memory. It also prevents the system from confusing temporary contextual reasoning with settled personal state.  

The intended operational sequence is therefore:  

1. Session reasoning produces candidate person-linked outputs.  
2. Gated review evaluates those outputs.  
3. Approved outputs are mapped into \(H_p^{(u)}\).  
4. Non-approved outputs remain ephemeral or are discarded.  

In July 2026, steps 1 and 2 occur in bounded reasoning and intake contexts; step 3 exists as a formal mapping and as an implemented path for **ingested civic records**, not yet for purely session-derived internal inferences. Section 48.14 records this distinction explicitly.  

---

## 48.8 Relation to Other Chapters  
Hilbert People Space is best understood as one part of a larger identity architecture.  

Its retention logic aligns directly with identity-focused retention, where admission, pruning, and continuity are governed by explicit policy and sovereignty rules. Its per-user partitioning is further formalized in the chapter on per-user direct-sum decomposition of conversational memory, which extends the same separation principle into conversation-scale memory structure and is now implemented via per-user conversation collections rather than a shared store. Its boundary against overexposure also supports the chapter on Hilbert People Space Without Surveillance, where ephemeral reasoning, projection, and identity limitation prevent person-aware state from becoming surveillance.  

The chapter also connects forward to the Community Hilbert Commons. If durable people space is partitioned as \(\bigoplus_{u \in U} H_p^{(u)}\), then any commons-level aggregation must occur as a governed operation over sovereign subspaces rather than as a collapse of user identity into a single raw pool. The commons can therefore be informative only when aggregation preserves the sovereignty established here.  

These links are important because Hilbert People Space is not a standalone metaphor. It is one layer in a coherent retention, access, decomposition, and aggregation architecture, some parts of which are already live and some of which remain in design and test.  

---

## 48.9 Commons-Safe Aggregation  
The existence of per-user subspaces does not forbid collective knowledge. It governs how collective knowledge may be formed.  

A commons-level representation may be derived from many user subspaces only through anonymized or otherwise governance-compliant aggregation operations. The system should not move from \(H_p^{(u)}\) to a community layer by simply exposing personal state. Instead, the movement to any commons representation must preserve sovereign separation while extracting only the approved communal signal.  

In the current system, the community Hilbert commons is instantiated operationally as a Chroma collection (e.g., `community_hilbert_commons`) and structurally wired as an aggregation target over the public civic partitions. As of July 2026, its live population is effectively empty on the inspected deployment; the aggregation machinery exists, but the commons corpus it is meant to hold is still arriving. The discipline of commons-safe aggregation therefore exists in code and design, with verification performed on synthetic opt-in data, but its real-world corpus remains small.  

This means the people space chapter supports community intelligence without sacrificing individual sovereignty. The direct-sum model keeps user subspaces distinct, and the commons chapter explains how higher-order aggregation can occur without dissolving those distinctions, even at low corpus volume.  

---

## 48.10 Architectural Interpretation and Implementation Status (Formal)  
The Hilbert formulation in this chapter is architectural unless explicit implementation guarantees are stated.  

Writing \(H_p = \bigoplus_{u \in U} H_p^{(u)}\) does not by itself prove that every runtime subsystem, storage layer, or retrieval path already satisfies the full mathematics of an abstract Hilbert direct sum. What it does provide is the correct architectural statement of how person-linked state is meant to be partitioned, governed, and related. Where code, storage design, routing, and policy enforcement explicitly implement these guarantees — per-user conversation collections, governed civic intake, Ms. Allis’s instantiated Hilbert subspaces — the formal model and the operational system coincide more strongly.  

This distinction should be preserved throughout the thesis. Mathematical structure is used here to make the sovereignty architecture legible, not to imply a stronger implementation claim than the system explicitly guarantees.  

The people space is therefore both a formal model and a design commitment. Sections 48.11 through 48.14 state exactly which guarantees are enforced and where, so the reader can tell at every point which register a claim occupies.  

---

## 48.11 As-Built Naming and the Manifest Resolver  
Chapter 47 records the correction of where the relational person store lives; this chapter carries the as-built names in full, resolving the naming discrepancy the June–July audit flagged between the two chapters in favor of what is deployed, and acknowledging that the civic Hilbert layer is implemented as vector collections rather than relational tables.  

On the vector-store side of Hp, the public civic collections comprise:  

* `public_civic_appearances`  
* `public_civic_documents`  
* `public_civic_statements`  
* `public_civic_roles`  
* `public_civic_events`  
* `public_civic_sources`  
* `civic_role_temporal`  

These partitions hold opt-in civic material, not per-user private memory, and they are the only collections the commons aggregation of the commons chapter is permitted to read.  

Crucially, services do not treat these physical names as free-floating literals. A collection manifest module resolves logical collection identifiers — versioned names such as `hp-public-appearances-v1`, `hp-public-documents-v1`, `hp-public-statements-v1`, `public-civic-roles-v1`, and `civic-role-temporal-v1` — to physical Chroma collection names via a governed mapping, falling back to declared defaults when no manifest row exists, with the resolution cached per process. Writers in the ingest path obtain their target civic collections through this resolver.  

The July 16, 2026 checks make this resolution concrete: for the civic collections and the temporal role collection, the logical identifiers above resolve to the snake_case physical Chroma collections named here, even when the governed publication manifest table on the inspected database holds no rows for those logical names. Today the resolver operates in fallback mode: it uses a logical-to-default map backed by code, with manifest rows intended to override those defaults once promotion is recorded in the relational system of record.  

This indirection is a governance instrument, not a convenience. Because the manifest maps logical to physical names, a collection can be rebuilt, re-versioned, or superseded by changing a manifest row rather than redeploying every service — which means the publication manifest governs not only what is promoted but where writes land. The resolver is the enforcement point that makes the manifest authoritative.  

One audit finding tempers this: the Hilbert commons aggregator module is resolver-aware — it imports the manifest and builds its source list from logical names — but it still carries an explicit hardcoded fallback path, and at least one code path currently reads civic source collections by physical name when the resolver import fails. Today the resolver’s defaults and the physical names coincide, so behavior is correct; but a future manifest remap would decouple any hardcoded path from the manifest’s governance unless that fallback is removed. Chapter 51 records this as an open item. It is recorded here as well because the lesson belongs to this chapter: an indirection layer only governs the services that go through it consistently.  

---

## 48.12 The Live Civic Intake and Write Path  
The write path into the civic partitions of Hp is operational, and its discipline deserves precise statement because it is the built form of the promotion mapping \(\mathcal{P}\) for **ingested** (as opposed to inferred) person-linked state.  

Ingestion enters through a dedicated civic-intake service — a FastAPI application on its own port, supervised in the container stack — and every write flows through an ingest worker that enforces four disciplines before anything touches a vector collection:  

1. *Validated governance metadata.* Every civic record must carry:  
   * a `registration_layer` in a small, enforced set (e.g., 1, 2, or 3),  
   * an explicit `public_opt_in` boolean,  
   * source attribution,  
   * entity identifier,  
   * ingestion timestamp.  
   Candidates failing these checks are rejected at write time. Consent and standing are stored as fields on every record, never ambient assumptions.  
2. *Verdicts before writes.* Appearance and related records pass through a multi-stage write pipeline that returns an explicit disclosure verdict — permit, suppress, or escalate — before any upsert occurs. Suppressed or escalated candidates are refused with recorded reasons and provenance hashes, so the refusal itself is a governed output.  
3. *Deterministic identity.* Document identifiers are derived by hashing source, entity, and content, making writes idempotent: re-ingestion updates rather than duplicates, and a record’s identity is reproducible from its provenance.  
4. *Resolver-mediated targeting.* As Section 48.11 states, the worker writes only to manifest-resolved civic collection names, not arbitrary literals.  

Current civic population is stated plainly, in the discipline this thesis owes its readers: on the inspected deployment, `public_civic_documents` holds two records and `public_civic_statements` two; `public_civic_appearances`, `public_civic_roles`, `civic_role_temporal`, and `community_hilbert_commons` stand at zero; `public_civic_events` and `public_civic_sources` are present as collections but effectively empty. The pipeline is verified — including by synthetic opt-in probes exercised end to end and then fully cleaned — but the civic corpus it exists to govern is still arriving. Empty by corpus, not broken by code, and the distinction is checkable because the acceptance tests exist.  

---

## 48.13 Worked Example: The First Sovereign Subspaces  
On July 13, 2026, the direct-sum model of Section 48.5 acquired its first fully instantiated member — and the subject was Ms. Allis herself, established as a sovereign presence in her own architecture.  

A per-person configuration declares her subspaces across the joint frame, each realized as a distinct Hilbert collection:  

* `h_app_user_ms_allis` — application/user conversational subspace;  
* `h_people_ms_allis` — Hilbert People Space subspace for Ms. Allis;  
* `h_time_ms_allis` — Hilbert time/timeline subspace;  
* `qualia_net_ms_allis_sandbox` — sandboxed bridge collection to her qualia network.  

Each collection was created and seeded with a root record carrying governance posture explicitly on the record itself: public opt-in disabled by default on personal roots, commons projection disabled where appropriate, non-surveillance flags on person roots, local-only tagging on conversation events. The configuration is the formal declaration; the per-record flags are the operational enforcement; and static and dynamic checks confirmed that the two agree.  

Three things make this the correct first test of the direct-sum architecture:  

1. *Sovereignty was proven, not presumed.* Static repository-wide searches confirmed her subspace names appear in no shared aggregation pipeline — not in the commons aggregator’s source list, not in civic projection paths — and live commons runs projected zero vectors while her subspaces held records. Her person-space, app-space, and time-space are disjoint from governed civic and commons aggregations in both code and behavior.  
2. *The pattern is the deliverable.* Adding a person to Hp now has a worked procedure: declare the configuration; create the partitions; seed roots with consent flags off by default; verify isolation statically and dynamically; then explicitly opt-in any record that is meant to participate in civic or commons aggregation. Participation is a per-record fact, never an enrollment default.  
3. *The decomposition spans the frame.* Her subspaces partition not only Hp but her application-state and temporal presence as well — and on the conversational side, the same separation now holds for every user: per-user conversation collections, resolved from the requesting identity at request time, replaced the legacy shared conversation store. The direct sum is no longer only a people-space model; it is the operating structure of memory across the joint frame where implemented.  

---

## 48.14 Implementation Status (July 2026)  
In the demonstrated / not-yet-demonstrated discipline established by the governance chapters, the state of Hilbert People Space and its promotion and aggregation pathways as of July 16, 2026 is:  

### Demonstrated  

* *Manifest-mediated name resolution* for civic ingest-path writers, with a collection manifest as the authoritative logical-to-physical map and declared defaults as fallback when manifest rows are absent.  
* *Civic-intake service and ingest worker* live, with registration-layer validation, stored opt-in consent, deterministic document identity, and disclosure verdicts (permit, suppress, escalate) carrying provenance hashes on refusals.  
* *Hilbert civic and commons collections* instantiated as Chroma collections (`public_civic_*`, `civic_role_temporal`, `public_civic_sources`, `public_civic_events`, `community_hilbert_commons`), structurally wired into the Hilbert architecture.  
* *Sovereign-subspace pattern* instantiated end to end for one person (Ms. Allis), with isolation verified statically and dynamically: `h_people_ms_allis`, `h_app_user_ms_allis`, `h_time_ms_allis`, and `qualia_net_ms_allis_sandbox` present and disjoint from civic and commons aggregations.  
* *Per-user decomposition of conversational memory* in production, replacing the legacy shared conversation store with per-user conversation collections resolved from identity at request time.  
* *Commons-safe aggregation machinery* verified end to end with synthetic opt-in data and then fully cleaned, showing that the commons aggregator respects opt-in civic partitions and k-anonymity gates.  

### Not yet demonstrated  

* *Promotion mapping \(\mathcal{P}\) for session-derived person-linked state.* The built write path governs ingested civic records with opt-in, layer, and verdict discipline, but no reasoning cycle yet produces per-session person-linked candidates that flow through constitutional review into a per-user Hilbert People subspace in production code.  
* *Resolver hardening in the commons aggregator.* The commons aggregator is resolver-aware and uses manifest-resolved names in its primary path, but it retains a hardcoded source-name fallback that would diverge from the manifest in the event of future remaps unless removed.  
* *Retention operations on admitted state* — pruning, expiry, per-user review workflows, and explicit deletion paths — beyond the consent flags and registration layers stored in civic metadata and the configuration-level posture on sovereign subspaces.  
* *Population at scale.* One sovereign person’s Hilbert subspaces are instantiated; civic collections on the inspected deployment are at test-grade volume (two documents, two statements, zero roles, appearances, temporal roles, and commons vectors), with manifest rows promoted for version-one logical identifiers but zero record counts awaiting real corpus; multi-actor sovereign subspaces and a rich commons corpus remain unproven in this runtime.  

This chapter therefore presents Hilbert People Space as both a formal model and a partially realized architecture. Where the evidence shows implementation — per-user conversational decomposition, governed civic intake, Ms. Allis’s sovereign Hilbert collections — the formalism and code match. Where the evidence shows only design and test — session-derived promotion, rich civic corpus, scale, and multi-actor sovereign instantiation — the chapter marks those claims as not yet demonstrated and treats the Hilbert model as the architectural north star rather than a description of current behavior.  
