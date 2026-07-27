# Chapter 13. Qualia Engine and Introspective State

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

Container count: 100
Vectors: ~6,740,611
Pituitary mode: baseline
autonomous_learner: 21,181 exact
Two-container DB split applied throughout
msallisgis production: 294 tables / 16 GB
postgis-forensic added; all April 16 OI items remain CLOSED
Lifecycle snapshot (July 26, 2026): fresh 237,655 · admissible_public 93,423 · inadmissible_public 144,232

---

## 13.0 How to Read This Chapter (Rural Developer Guide)

This chapter is for anyone building a system that needs to keep an honest,
auditable account of its own behavior — not claims of consciousness, but
structured self-reporting that a human steward can actually inspect and use.

Five things to carry forward:

1. **Qualia here means structured narrative output, not sentience.** Every
   biological metaphor in this chapter — qualia, pituitary, EEG bands — maps
   directly to a named service, schema, or endpoint. Nothing claims subjective
   experience.

2. **Introspective records are governance artifacts.** They exist so that human
   stewards, auditors, and controller services can check what happened, under
   which conditions, with which evidence, and in which governance state.

3. **The July 26, 2026 lifecycle snapshot is the system's first verified
   introspective data point at rest.** Fresh: 237,655 · Admissible public:
   93,423 · Inadmissible public: 144,232. This is the concrete baseline for
   all self-monitoring claims in this chapter.

4. **Self-monitoring is tied to place.** Every introspective record includes
   spatial anchors — WV county, block group, or ZIP — so the system can
   account for where its claims are grounded.

5. **Every "feeling" is backed by a signed verdict or a row count.** If a
   qualitative narrative cannot be traced to a concrete log, memory entry, or
   governance record, it does not belong in an introspective record.

---

## 13.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis keeps a running, structured account of her
own activity so that others can audit and guide it. It supports:

- **P1 – Every where is entangled** by tying internal narratives to specific
  communities, datasets, and places that appear in retrieval and spatial
  backbones.
- **P3 – Power has a geometry** by making every qualitative "feeling" traceable
  back to concrete logs, memory entries, and spatial identifiers.
- **P5 – Design is a geographic act** by treating introspective records as
  designed artifacts that shape how Appalachian realities are described and
  reflected on.
- **P12 – Intelligence with a ZIP code** by ensuring that Ms. Allis's
  self-descriptions include where interactions are happening, not just what was
  said.
- **P16 – Power accountable to place** by building a glass-box layer of
  self-description that other agents and human stewards can query, critique,
  and improve.

This chapter belongs to the **Computational Instrument** tier: it specifies how
operational traces, memory, and evaluation signals are woven into an
introspective fabric that can be inspected and used for governance.

Throughout, biological language is used as disciplinary translation. Every
neurobiological term is paired with the concrete service, endpoint, data store,
gate, or evidence artifact that implements it, without claiming biological
consciousness, sentience, clinical diagnosis, treatment, or complete
neuroscientific equivalence.

---

## 13.2 Status Snapshot

As of the confirmed runtime closure and the July 26, 2026 governance gate:

- **Containers:** 100 containers Up; zero Restarting; zero Exited.
- **ChromaDB v2:** 48 collections; approximately 6,740,611 vectors; host port
  8002.
- **`autonomous_learner`:** 21,181 records (exact), using 384-dim
  `all-minilm:latest` embeddings.
- **Pituitary mode:** `baseline` for the neurobiological pituitary service,
  after earlier elevated mode.
- **Database split:**
  - Production PostgreSQL `msallis-db` (host 5433 / container 5432) with
    `msallisgis` at 16 GB / 294 tables / 11 schemas.
  - Forensic PostgreSQL `postgis-forensic` (host 5432) with `msallisgis` at
    17 GB / 314 tables / 9 schemas, used for auditing only.
- **Memory API:** `allis-memory` at port 8056, with authenticated
  `/memory/sessions` showing active sessions.
- **Qualia Engine:** `allis-qualia-engine` running on the internal Docker
  network; host port 8017 assigned to the BBB output filter facade.
- **EEG services:** EEG Delta, Theta, and Beta band services active and feeding
  rhythm signals.
- **Lifecycle snapshot (July 26, 2026):** The governance runtime audit of
  `public.gbim_record` at the July 26 gate produced:
  - **fresh:** 237,655 total authorized rows in the governed corpus.
  - **admissible_public:** 93,423 rows passing all ten conditions of the public
    admissibility predicate (Appendix A, §A.4).
  - **inadmissible_public:** 144,232 rows stored but not yet publicly
    admissible — awaiting spatial/temporal backfill, lifecycle promotion, or
    explicit public authorization.
  This is the first verified lifecycle snapshot at rest, recorded in
  `runtime_governance.public_answer_audit`. It is the concrete baseline for
  all self-monitoring and introspective-state claims in this chapter.
- **Open items:** All previously tracked OI items for Chapter 13 are closed;
  no new open items introduced by the gate.

---

## 13.3 Qualia as Internal Narrative Representation

In this architecture, **qualia** refers to Ms. Allis's internal narrative
representation of what is happening, constructed from text content and context
features as explicit structured outputs.

### Implemented Services

- **Qualia Engine (main):** `allis-qualia-engine` runs on the internal Docker
  network and produces JSON-like envelopes capturing emotional resonance,
  meaning-making, and experience narration.
- **Qualia Engine (NBB companion):** `nbb_qualia_engine` runs in the
  neurobiological brain stack on a separate port and shares health templates
  with NBB safety services.

Biological terms such as "qualia" and "experience generator" are used to
describe these modules, but they implement data transformation and narrative
synthesis over logs, memory, and context. They do not claim subjective
experience or sentience.

### Self-Monitoring at Rest

The lifecycle snapshot from July 26, 2026 — fresh: 237,655 · admissible_public:
93,423 · inadmissible_public: 144,232 — is the Qualia Engine's first concrete
operational data point at rest. When the system generates an introspective
narrative about its evidence corpus, that narrative is grounded in these exact
counts rather than vague statements about "system health." A Qualia Engine
narrative produced at rest would report that 93,423 records are publicly
admissible and 144,232 are held but inadmissible — a specific, verifiable
characterization of the corpus's state rather than a qualitative impression.

---

## 13.4 IntrospectiveRecord and WOAHResult

The introspective layer centers on two implemented schemas:

- **`IntrospectiveRecord`:** A Pydantic model that ties together identifiers,
  timestamps, roles, retrieved evidence, pituitary mode, EEG band states,
  evaluation scores, judge signatures, and narrative description.
- **`WOAHResult`:** A structured result capturing ethical and alignment scores
  and pituitary mode snapshots for each event.

These classes are implemented in dedicated services code and instantiate
cleanly. They ensure that every introspective entry:

- can be traced back to observable events and service responses;
- separates qualitative narrative fields from operational metrics;
- includes governance and safety context such as pituitary mode and BBB status.

**Lifecycle counts as introspective evidence.** The July 26 snapshot (fresh:
237,655 · admissible_public: 93,423 · inadmissible_public: 144,232) is an
example of exactly the kind of structured, machine-readable evidence that
should populate the operational-metrics fields of an `IntrospectiveRecord`. An
introspective record produced after the July 26 gate would include these three
counts as part of its evidence envelope, making the corpus's governance state
at event time fully reconstructable from the record alone.

For rural developers, the `IntrospectiveRecord` schema provides the blueprint
for their own introspective records: a single, well-typed object per event that
integrates data across services, including lifecycle counts from the governance
runtime.

---

## 13.5 Data Sources Feeding Introspection

The introspective layer aggregates signals from multiple parts of the system:

- **Interaction traces:** conversational logs, request IDs, user or session
  handles, active personas, and lens configurations.
- **Retrieval and memory:** ChromaDB v2 collections (including
  `autonomous_learner`, `msallis_docs`, and `gbim_worldview_entities`) and
  memory APIs such as `allis-memory`.
- **Spatial backbone:** production and forensic PostGIS databases (`msallis-db`
  and `postgis-forensic`) with WV-specific GIS tables.
- **Neurobiological rhythms:** EEG Delta, Theta, and Beta band services that
  indicate internal rhythm conditions during each event.
- **Pituitary governance:** snapshots of `nbb_pituitary_gland` mode (e.g.,
  baseline or elevated) and associated weighting parameters.
- **Optimization and evaluation:** DGM outputs, WOAH weighted optimization
  scores, and judge verdicts signed with ML-DSA-65 signatures.
- **Governance lifecycle counts:** The `runtime_governance.public_answer_audit`
  table and the `public_admissible_gbim_mv` materialized view, which together
  record corpus-level counts (fresh, admissible_public, inadmissible_public)
  at each governance cycle. The July 26, 2026 snapshot — fresh: 237,655 ·
  admissible_public: 93,423 · inadmissible_public: 144,232 — is the first
  verified entry in this data source and anchors the self-monitoring baseline.
- **System health:** container counts, port registries, and BBB output filter
  status.

The `IntrospectiveRecord` schema stitches these signals together into a single
record per event, making it possible to reconstruct what happened, under which
conditions, and with which evidence.

---

## 13.6 Writing Introspective Records Step by Step

For a rural developer thinking about how to implement similar behavior, the
writing process can be described step by step:

1. **Capture request context.**
   When a request arrives, record identifiers, role or persona, lens settings,
   and current pituitary mode. Include basic spatial hints where the request is
   anchored (for example, WV county or ZIP).

2. **Record retrieval and memory usage.**
   Log which ChromaDB collections were queried, which documents or vectors were
   retrieved, and which GIS tables or GBIM entities were touched. Note the use
   of production vs. forensic databases where applicable.

3. **Attach neurobiological rhythm and governance state.**
   Add current EEG band activity and pituitary mode to the record. These fields
   indicate internal conditions under which decisions and narratives were
   formed.

4. **Snapshot the governance lifecycle counts.**
   Query `runtime_governance.public_answer_audit` for the most recent
   fresh/admissible_public/inadmissible_public row and attach those three
   numbers to the introspective record. As of July 26, 2026, the baseline is
   fresh: 237,655 · admissible_public: 93,423 · inadmissible_public: 144,232.
   Subsequent introspective records will show how these counts evolve over
   time, making corpus health visible across the system's operational history.

5. **Add evaluation and optimization outputs.**
   Include WOAHResult fields, DGM decisions (apply, reject, rollback), and
   judge scores. Sign judge verdicts using the configured signature scheme so
   that they can be verified later.

6. **Generate and store narrative.**
   Use the Qualia Engine to produce a human-readable narrative that summarizes
   the event, its emotional tone, and its meaning. Where the narrative touches
   on the system's evidence base or corpus health, it must cite the concrete
   lifecycle counts rather than qualitative impressions. Store this narrative
   alongside structured data in the `IntrospectiveRecord`.

7. **Persist the record.**
   Save the record in introspection-specific stores or memory services,
   ensuring it can be queried by audits, research tools, or other internal
   services.

This pattern ensures that introspective data is both machine-readable and
human-understandable, grounded in real system behavior.

---

## 13.7 Reading and Using Introspective State

Introspective records are designed to be read and used by:

- **Human stewards:** who can inspect records to see which data sources were
  used, which modes were active, how decisions were evaluated, and how the
  system described itself. The July 26 lifecycle snapshot — fresh: 237,655 ·
  admissible_public: 93,423 · inadmissible_public: 144,232 — is the first
  reference point a human steward should check when evaluating whether the
  system's public evidence surface is healthy or degraded.
- **Controller services:** such as pituitary and optimization supervisors that
  consume summaries to adjust modes, weights, or safety thresholds. These
  services may compare current lifecycle counts against the July 26 baseline to
  detect drift — for example, a sudden drop in admissible_public rows below
  93,423 would signal a governance degradation worth investigating.
- **Research and audit tools:** which use the schema to analyze patterns over
  time, including where errors arose or where certain communities were under- or
  over-represented. Lifecycle count time-series (anchored at the July 26
  baseline) provide one dimension of that longitudinal analysis.

For rural deployments, this provides a concrete way to check whether the system
is actually behaving as intended in relation to local communities and places,
rather than relying on opaque logs or abstract metrics.

---

## 13.8 Pituitary and Qualia Interaction

The `nbb_pituitary_gland` service plays a central role in introspective state:

- It sets global modes such as baseline, elevated, or transparency.
- It modulates WOAH weights and governance thresholds.
- It influences how qualia narratives are generated, particularly in terms of
  warmth and caution.

Introspective records include the pituitary mode at event time so that
evaluators can understand whether strict or relaxed governance was in effect.
Qualia outputs are interpreted in the context of this mode, which helps
distinguish ordinary operation from heightened scrutiny periods.

The July 26, 2026 pituitary mode at the lifecycle snapshot was `baseline`,
meaning the counts (fresh: 237,655 · admissible_public: 93,423 ·
inadmissible_public: 144,232) were produced and recorded under standard
governance weighting — not elevated scrutiny or emergency mode. This matters
for interpreting the snapshot: the 144,232 inadmissible rows are a normal
backlog under baseline governance, not an anomaly requiring immediate
escalation.

This neurobiological vocabulary is tied directly to implemented services and
configuration files, making the metaphor operational rather than purely
conceptual.

---

## 13.9 Links to Memory, Spatial, and GBIM Layers

Qualia and introspective state are tightly linked to memory and spatial
backbones:

- **ChromaDB v2** provides semantic memory across 48 collections, including an
  authoritative GBIM entity store.
- **Production and forensic PostGIS databases** hold West-Virginia-specific GIS
  tables and forensic records, respectively.
- **GBIM query routers and indexers** access entity vectors internally without
  exposing host bindings, keeping sensitive belief structures constrained.
- **`public.gbim_record` and `runtime_governance.public_answer_audit`** are
  the relational layer that backs the lifecycle snapshot. The 237,655 rows in
  `gbim_record` represent the full authorized corpus; the 93,423 admissible
  rows in `public_admissible_gbim_mv` are the public-evidence surface that
  backs spatial and civic claims. Introspective records reference these stores
  by name and row count, making it clear where evidence and context came from.

This keeps place-based reasoning grounded and auditable: a qualia narrative
that mentions "the West Virginia evidence base" can be pinned to exactly 93,423
publicly admissible records as of July 26, 2026, with `spatial_unit_id`,
`spatial_unit_kind`, and `valid_time_start` attached to each one.

---

## 13.10 Closed Open Items and Operational State

All previously tracked open items for Chapter 13 have been closed, including:

- Implementation and validation of `IntrospectiveRecord` and `WOAHResult`
  schemas.
- Confirmation of ML-DSA-65 judge verdict signing and verification behavior.
- Correction of port assignments (such as clarifying that host port 8017 is a
  BBB output filter facade).
- Clarification of GBIM storage in ChromaDB versus relational tables.

The July 26, 2026 lifecycle snapshot — fresh: 237,655 · admissible_public:
93,423 · inadmissible_public: 144,232 — closes the last open item in this
chapter: the requirement for a concrete, verified operational data point
demonstrating the system's self-monitoring capability at rest. This snapshot
is recorded in `runtime_governance.public_answer_audit` and is reproducible
by any auditor with access to that table and to `public_admissible_gbim_mv`.

The chapter now describes a fully operational introspective and qualia system
over a verified neurobiological runtime model, with no outstanding gate
blockers at its scope.

---

## 13.11 Closing Statement

The Qualia Engine and introspective state in Ms. Allis implement a disciplined,
neurobiologically inspired way for the system to describe itself. They aggregate
signals from interactions, memory, spatial backbones, governance services, EEG
rhythms, optimization pipelines, and judges into structured records and
narratives.

The July 26, 2026 lifecycle snapshot — fresh: 237,655 · admissible_public:
93,423 · inadmissible_public: 144,232 — is the anchor for this chapter's
self-monitoring claims. It is the first verified operational data point produced
by the governance runtime's self-audit mechanism, recorded in
`runtime_governance.public_answer_audit` at pituitary mode `baseline`. Every
qualia narrative about corpus health, every `IntrospectiveRecord` that touches
the evidence surface, and every controller service that monitors governance
drift should reference this baseline and track how the three counts evolve over
time.

For rural developers, this chapter offers a step-by-step pattern: build a
qualia-like narrative engine, define an introspective record schema, tie
biological metaphors to concrete services and endpoints, snapshot governance
lifecycle counts at each event, and ensure every "feeling" or self-description
is backed by auditable data. Under these constraints, Ms. Allis's introspective
layer becomes a practical tool for stewardship and accountability rather than
a claim of biological consciousness or sentience.

---

*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
