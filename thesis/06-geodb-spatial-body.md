# 6. GeoDB Spatial Body

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 6.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis binds spatial reasoning to a concrete
geospatial body. It documents the distinction between production geospatial
infrastructure and analysis-only workspaces, and it reflects the July 26, 2026
architecture closeout in which spatial grounding moved from an architectural
intention to a schema-level enforcement. As of that date, `spatial_unit_id`
(set to the blockgroup GEOID) and `spatial_unit_kind` (set to `'blockgroup'`)
are `NOT NULL` columns that were backfilled across all 237,655 rows in
`public.gbim_record`. Spatial grounding in this system is therefore enforced at
the schema level, not merely designed or described.

This chapter treats the spatial body not as a single database or a free-floating
layer of coordinates, but as a governed geospatial apparatus in which production
GeoDB resources, sandbox-local interpretation, and gate-controlled promotion
operate together. Spatial interpretation is an interaction among production
Postgres resources, GeoDB features, semantic memory, governed state, and
sandboxed reasoning. Geographic facts become operational only under authority,
provenance, temporality, disclosure, and governance constraints — and, as of
July 26, 2026, those constraints are enforced at the schema level.

The chapter directly supports several core principles:

- **P1 — Every where is entangled** — spatial interpretation is an interaction
  among production Postgres resources, GeoDB features, semantic memory, governed
  state, and sandboxed reasoning rather than a direct consequence of model
  output.
- **P3 — Power has a geometry** — place, infrastructure, routing, validation,
  and geospatial state transitions are auditable through services, database
  boundaries, validation gates, and promotion controls.
- **P5 — Design is a geographic act** — the separation between production
  databases, host-native analysis workspaces, sandbox reasoning, and promotion
  pathways is itself a design decision that shapes how place knowledge can
  become action.
- **P12 — Intelligence with a ZIP code** — West Virginia-specific geospatial
  grounding is preserved and enforced at the schema level, with spatial unit
  identity and kind encoded as structural `NOT NULL` columns across the full
  governed corpus.
- **P16 — Power accountable to place** — spatial interpretations, candidate
  updates, and state-changing geospatial conclusions must pass sandbox
  reasoning, blood-brain-barrier review, and DGM validation before affecting
  durable production state.

This chapter belongs to the **Computational Instrument** tier. It defines the
spatial body as a governed operational layer: production geospatial reality is
authoritative, analysis workspaces are bounded, interpretation is sandboxed, and
spatial grounding is enforced at the schema level.

---

## 6.2 Purpose and Scope

This chapter describes the spatial body of Ms. Allis as the geospatial substrate
through which place-aware reasoning becomes operational. It requires an explicit
distinction between the production geospatial stack and the host-native analysis
workspace used for normalization, auditing, and sampling-frame construction.

The production apparatus includes the Postgres and GeoDB resources that support
live service behavior, query routing, retrieval, and operational responses. The
host-native `gisdb` analysis workspace is a separate normalization and analysis
environment that may inform audits, reconciliation, or sampling preparation, but
it is excluded from the production apparatus documented in Appendix A and must
not be treated as live geospatial memory or live operational substrate.

Under the July 2026 closure, the live Chroma/PostGIS/GBIM substrate described in
this chapter is bounded to the governed West Virginia manifest. Spatial coverage
and production routing claims refer only to the verified corpus of **55
counties, 546 tracts, 1,639 blockgroups, and 741 ZCTAs**, not to universal
spatial coverage beyond West Virginia.

**Critical spatial grounding note:** as of July 26, 2026, the columns
`spatial_unit_id` and `spatial_unit_kind` are `NOT NULL` across all 237,655
rows in `public.gbim_record`. The value of `spatial_unit_id` is the blockgroup
GEOID and `spatial_unit_kind` is `'blockgroup'` for every row in the governed
corpus. This backfill was completed without error. Any sentence in earlier
drafts describing spatial grounding as "designed" or "intended" reflects a prior
state of the system; the current system enforces spatial grounding at the schema
level.

Spatial interpretations and proposed updates arise through sandboxed reasoning
over retrieved evidence, followed by validation and controlled promotion, not by
immediate model assertion.

---

## 6.3 Production GeoDB and Analysis Workspace

The spatial body is a **two-tier geospatial reality**.

**Tier 1 — Production Postgres and GeoDB resources** are the authoritative
stores used by live services and operational routing. These are the database
objects and geospatial services that participate in runtime retrieval,
GIS-aware response generation, landowner routing, registry alignment, and
durable state formation within the governed West Virginia corpus. Every
production row in `public.gbim_record` carries a `spatial_unit_id` equal to
the blockgroup GEOID and a `spatial_unit_kind` of `'blockgroup'`, enforced at
the schema level as `NOT NULL` columns. There is no production row in the
governed corpus that lacks these spatial anchors.

**Tier 2 — The host-native `gisdb` workspace** is an analysis and normalization
environment used for forensic work, deduplication, crosswalk construction,
auditing, and other mutable analytic operations. It is excluded from the
production apparatus in Appendix A and must not be described as though it were
a live memory layer or live operational substrate.

This distinction matters because a query may be investigated, normalized,
sampled, or stress-tested in analysis space without that analysis space acquiring
authority over production geospatial truth. Production Postgres and GeoDB
resources anchor live geospatial reasoning and state; `gisdb` supports analysis
and preparation only.

For another lab or rural developer, this pattern is reproducible: keep
production spatial databases separate from host-native or analyst-native
workspaces, enforce spatial unit identity as a `NOT NULL` structural column
rather than leaving it as an optional metadata field, and ensure that only the
production layer can support runtime claims or durable geospatial consequence.

---

## 6.4 The Spatial Body as Governed State

The spatial body is not just a set of coordinates, embeddings, shapes, or joined
rows. Geospatial knowledge is represented as locality-aware governed state.

A spatial state is understood as a governed tuple:

\[
x_{\mathrm{geo}} = (v_{\mathrm{geo}},\; a,\; p,\; t,\; \ell,\; g)
\]

where:

- \(v_{\mathrm{geo}}\) is the spatial content, geometry, relation, or embedded
  spatial representation;
- \(a\) is authority or source status;
- \(p\) is provenance;
- \(t\) is temporal validity or freshness;
- \(\ell\) is disclosure or access level; and
- \(g\) is governance and gate status.

The spatial component of this tuple is not resolved by model narration. It is
resolved by the `spatial_unit_id` and `spatial_unit_kind` fields in
`public.gbim_record`, which are enforced at the schema level as `NOT NULL`
columns across all 237,655 rows. Under this framing, a county polygon, a parcel
belief, a service-area inference, and a proposed geospatial update may occupy
nearby semantic or spatial positions while remaining different governed states
because they differ in authority, time, provenance, disclosure, or gate status.

A location vector is not self-authorizing, and a geospatial embedding is not by
itself a production fact. A geometry acquires operational meaning only when it
is attached to the provenance, temporal, disclosure, and governance conditions
that make it safe to retrieve, display, compare, or act upon — and, for records
in the governed corpus, when it carries the `spatial_unit_id` and
`spatial_unit_kind` values that are now structurally required.

---

## 6.5 Sandboxed Spatial Interpretation

Spatial interpretations and proposed updates arise from **sandboxed reasoning**,
not from direct model output.

At runtime, spatial evidence may be assembled from production GeoDB resources,
semantic memory, registries, and related spatial services. But the
interpretation of that evidence — whether a place condition exists, whether a
service gap is likely, whether a feature relationship is meaningful, or whether
a geospatial record should be revised — must first be formed inside a sandboxed
reasoning path.

Inside that path, candidate interpretations are provisional. They may compare
layers, test hypotheses, weigh contradictory evidence, examine locality
constraints, and stage possible updates, but they remain reversible until they
pass formal checks. Sandbox candidates that are promoted to `public.gbim_record`
receive the `spatial_unit_id` (blockgroup GEOID) and `spatial_unit_kind`
(`'blockgroup'`) values as part of the promotion write — these columns are
required at the schema level and will reject any insert that omits them.

A rural developer reproducing this architecture should treat the sandbox as the
place where geospatial meaning is assembled and tested, not as a back door into
production tables. The `NOT NULL` constraint on `spatial_unit_id` and
`spatial_unit_kind` is not just a data-quality measure; it is a structural
enforcement that a spatial anchor must be declared before a record can enter the
governed corpus.

---

## 6.6 BBB, DGM, and Spatial Promotion

The validation chain for spatial conclusions is explicit and gate-controlled.

Spatial conclusions that could affect production geospatial state must pass
blood-brain-barrier and DGM validation before they can alter durable records,
operational routing, or action-bearing state. A model output, even if
geospatially plausible, does not directly rewrite production GeoDB state or
authorize a place-based conclusion merely because it appears coherent.

The operational sequence is:

\[
S_{\mathrm{geo,raw}}
\;\rightarrow\;
S_{\mathrm{geo,sandbox}}
\;\rightarrow\;
S_{\mathrm{geo,BBB}}
\;\rightarrow\;
S_{\mathrm{geo,DGM}}
\;\rightarrow\;
S_{\mathrm{geo,prod}}
\]

where:

- \(S_{\mathrm{geo,raw}}\) contains retrieved features, raw joins, prompts, and
  unconstrained candidate interpretations;
- \(S_{\mathrm{geo,sandbox}}\) contains provisional spatial reasoning states;
- \(S_{\mathrm{geo,BBB}}\) contains candidate states that have passed safety,
  constitutional, disclosure, and boundary review;
- \(S_{\mathrm{geo,DGM}}\) contains candidate states that have passed
  operational admissibility and structural validation; and
- \(S_{\mathrm{geo,prod}}\) contains approved production geospatial state, with
  `spatial_unit_id` and `spatial_unit_kind` populated as `NOT NULL` fields
  enforced at the schema level.

BBB review screens safety, constitutional, disclosure, and boundary issues.
DGM validation checks whether the candidate interpretation or update is
sufficiently supported and operationally admissible. Only then may a spatial
conclusion affect production geospatial state. The schema-level `NOT NULL`
constraint on `spatial_unit_id` and `spatial_unit_kind` acts as a final
structural gate: the database itself will reject a promoted row that lacks a
declared spatial anchor, regardless of whether it passed all upstream gates.

---

## 6.7 \(H_{\text{geo}}\) and Tensor Relations

The spatial body described in this chapter is the implementation-facing
counterpart of \(H_{\text{geo}}\), the spatial Hilbert body formalized elsewhere
in the thesis.

Production spatial records, GIS features, and governed geospatial states are
concrete anchors or projections of states within \(H_{\text{geo}}\). Operational
interactions between semantic and geographic reasoning should be read alongside
the tensor-product bridge linking \(H_{\text{App}}\) and \(H_{\text{geo}}\).

The July 26, 2026 backfill — enforcing `spatial_unit_id = geoid` and
`spatial_unit_kind = 'blockgroup'` as `NOT NULL` across all 237,655 rows —
closes the correspondence between the formal spatial Hilbert body and the
operational corpus. Every production record in `public.gbim_record` is now
explicitly anchored to a named unit at a named spatial resolution, making the
mapping from formal states in \(H_{\text{geo}}\) to operational rows in the
governed corpus structurally unambiguous.

For technical replication, this means that a spatial stack should be designed so
that formal geographic representations and operational geospatial services are
mapped to one another without collapsing theory into infrastructure or
infrastructure into metaphor — and that the mapping should be enforced at the
schema level, not left as an implicit convention.

---

## 6.8 Production Memory and Sandbox-Local Spatial Stores

Production Postgres and GeoDB resources carry authoritative spatial records,
runtime-accessible layers, and live geospatial inputs used by the deployed
apparatus. Every row in the production corpus carries `spatial_unit_id` and
`spatial_unit_kind` as `NOT NULL` structural columns, backfilled across all
237,655 rows on July 26, 2026. This is the spatial grounding layer of the
governed corpus: it is not a design note or an architectural aspiration, it is
enforced at the schema level.

Sandbox-local stores hold provisional interpretation products such as working
hypotheses, candidate joins, temporary locality inferences, reflection traces,
or staged update proposals. Those sandbox-local materials are not production
memory. They are internal deliberation artifacts whose role is to support
interpretation without prematurely changing durable geospatial state. Promotion
rules determine whether any such candidate interpretation graduates into approved
production consequence — and at the moment of promotion, the write to
`public.gbim_record` must include valid `spatial_unit_id` and `spatial_unit_kind`
values or the database will reject the insert.

This distinction parallels the production-versus-sandbox separation documented
for Chroma semantic memory in Chapter 5. It ensures that the spatial body
remains auditable and stable even while internal reasoning remains exploratory,
revisable, and temporary. The `NOT NULL` enforcement ensures that "auditable and
stable" is a structural guarantee, not a documentation convention.

---

## 6.9 Locality, Temporality, and Disclosure

Spatial knowledge is never only spatial.

A geospatial conclusion is treated as locality-aware only when it preserves the
relation between place, source, time, and access constraints. A feature geometry
without provenance may be analytically suggestive but not operationally
sufficient; a service-area claim without temporal validity may be stale; and a
landowner or infrastructure interpretation without disclosure constraints may
violate anti-surveillance and governance commitments.

For records in the governed corpus, locality is enforced at the schema level:
`spatial_unit_id` names the blockgroup GEOID, and `spatial_unit_kind` names the
spatial resolution. Those fields are not nullable. Temporality is enforced by
the `valid_time_start` `NOT NULL` column added on the same date and by the
`degradation_status IN ('fresh', 'aging')` gate in the Postgres lifecycle runner
(see Appendix A, Condition C₇). Together, these three columns — `spatial_unit_id`,
`spatial_unit_kind`, and `valid_time_start` — close the spatial and temporal
halves of the Spacetime Contract at the schema level, not merely by convention.

For a reproducing lab or rural deployment, this means that a shapefile, table
join, or spatial API result should never be treated as operational truth by
itself. Spatial truth claims must be linked to provenance, temporal review,
disclosure rules, and promotion state — and the spatial anchor itself (`who is
this place, at what resolution?`) must be a non-nullable structural field, not
an optional annotation.

---

## 6.10 Revision Principle

The governing revision principle for this chapter is as follows:

- Production Postgres and GeoDB resources and the host-native `gisdb` analysis
  workspace are distinct and must not be collapsed into one spatial apparatus.
- The host-native `gisdb` workspace is excluded from the apparatus in Appendix A
  and functions as an analysis and normalization environment, not a live
  production geospatial substrate.
- The live spatial stack documented here is bounded to the governed West Virginia
  manifest of 55 counties, 546 tracts, 1,639 blockgroups, and 741 ZCTAs; no
  broader spatial coverage is claimed without separate proof.
- `spatial_unit_id` (blockgroup GEOID) and `spatial_unit_kind` (`'blockgroup'`)
  are `NOT NULL` columns enforced at the schema level across all 237,655 rows in
  `public.gbim_record`, backfilled and verified on July 26, 2026. Any earlier
  description of spatial grounding as "designed" or "intended" reflects a prior
  state of the system. The current system enforces spatial grounding at the
  schema level.
- Spatial interpretations and proposed updates arise through sandboxed reasoning
  rather than direct model output.
- Spatial conclusions must pass BBB and DGM validation before affecting
  production geospatial state. The `NOT NULL` schema constraint on
  `spatial_unit_id` and `spatial_unit_kind` acts as a final structural gate at
  the moment of promotion.
- Geospatial state is described as locality-aware governed state with provenance,
  authority, temporality, disclosure, and gate metadata rather than as
  coordinates or embeddings alone.
- This chapter explicitly cross-references \(H_{\text{geo}}\) and the
  tensor-product bridge so the spatial body is tied to the formal Hilbert
  framework. The July 26, 2026 backfill closes the correspondence between formal
  spatial states and operational rows.
- A reproducible deployment should preserve the same boundary structure:
  authoritative production spatial stores with `NOT NULL` spatial unit columns,
  bounded analysis workspaces, sandboxed interpretation, and gate-controlled
  promotion.

Under this revised framing, the spatial body is documented as a governed
operational layer: production geospatial reality is authoritative, analysis
workspaces are bounded, interpretation is sandboxed, and spatial grounding is
enforced at the schema level.

---

*Chapter 6 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
