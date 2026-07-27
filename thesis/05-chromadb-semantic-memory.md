# 5. ChromaDB as Semantic Memory

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 5.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis uses ChromaDB as a governed semantic-memory
substrate rather than as a generic vector store. In the production system,
ChromaDB holds long-term semantic memory for place-based reasoning about West
Virginia, while a separate internal-state sandbox holds ephemeral reasoning
traces, hypothesis staging, qualia-adjacent signals, and reflection artifacts
that must not be treated as production memory.

This distinction matters because the system explicitly separates:

- **Persistent semantic memory** — production corpus memory used for retrieval,
  grounding, GBIM linkage, geospatial reasoning, commons governance analysis,
  and auditable user-facing evidence.
- **Sandbox workspace memory** — session-bounded internal reasoning state used
  for reversible experimentation before promotion.
- **Promotion-governed memory consolidation** — the process by which a state
  may change epistemic status from speculative to validated to retained, with
  provenance conserved across the chain.

Under the July 2026 closure, the Chroma/PostGIS/GBIM substrate is **bounded to
the verified West Virginia manifest**. Spatial coverage and GBIM linkage in this
chapter refer to the governed corpus of **55 counties, 546 tracts, 1,639
blockgroups, and 741 ZCTAs**, not to universal spatial coverage beyond West
Virginia.

This architecture supports:

- **P1 — Every where is entangled** by storing GBIM entities, GIS features,
  governance texts, and community resources in long-term production collections
  while preserving a distinct sandbox for provisional reasoning that has not yet
  earned corpus status.
- **P3 — Power has a geometry** by making not only retrieval paths but also
  promotion gates, provenance chains, and authority changes inspectable across
  memory layers.
- **P5 — Design is a geographic act** by treating collection boundaries, sandbox
  isolation, promotion criteria, and audit rules as design choices that shape how
  West Virginia is represented and acted upon.
- **P12 — Intelligence with a ZIP code** by grounding production memory in
  West-Virginia-specific collections and registries at manifest scope while
  preventing session-local speculation from contaminating those place-bound
  stores.
- **P16 — Power accountable to place** by requiring that durable memory be
  attributable, reviewable, and promotable under explicit governance rather than
  silently retained as raw internal thought.

This chapter belongs to the **Computational Instrument** tier of the thesis. It
defines the long-term semantic-memory substrate, the sandbox boundary, and the
promotion logic that links raw internal reasoning to governed memory in a way
that can be replicated by other labs or rural developers.

---

## 5.2 Purpose and Scope

This chapter documents how Ms. Allis uses ChromaDB across two sharply distinct
roles:

1. **Production corpus memory** — durable semantic collections used for
   retrieval, grounding, and evidence-bearing system behaviour.
2. **Internal-state sandbox memory** — ephemeral, sandbox-local collections used
   only for internal reasoning, hypothesis testing, reflection, and temporary
   working state.

It therefore covers:

- long-term semantic collections for GBIM worldview entities, governance, law,
  resources, autonomous learning, and other durable corpora;
- the distinction between the main production Chroma instance and the dedicated
  internal-state Chroma used only for sandbox reasoning;
- retention, audit, promotion, and provenance rules that determine when a state
  remains workspace, when it becomes validated memory, and when it becomes
  actionable; and
- the relationship between vector storage, Hilbert-space state, and governed
  memory status at the West Virginia manifest scale.

**Critical architectural point on retention authority:** ChromaDB collection
membership is a storage fact, not an admissibility signal. The authoritative
signal for whether a GBIM-linked record is admissible for public claims is the
PostgreSQL `degradation_status` field on `public.gbim_record`. Only records
where `degradation_status IN ('fresh', 'aging')` satisfy the lifecycle gate
defined in the `public_admissible_gbim_mv` view predicate (Appendix A,
Condition C₇). Any section of this chapter that describes retention rules for
ChromaDB collections must be read against that Postgres lifecycle gate as the
governing admissibility authority, not ChromaDB collection expiry alone.

The core claim is simple: **a vector is not yet memory in the full architectural
sense merely because it is stored**. In Ms. Allis, durable memory is a governed
state with authority, provenance, confidence, temporal status, disclosure level,
and gate state — including a live `degradation_status` signal from PostgreSQL —
not just an embedding.

---

## 5.3 Two Chroma Roles

### 5.3.1 Production Corpus Chroma

The main production Chroma instance is the long-term semantic memory layer for
the system. In the current architecture this is the canonical corpus store used
for retrieval-augmented generation, judge grounding, GBIM linkage, governance
lookup, and geospatial-semantic recall.

This production instance contains collections such as:

- `gbim_worldview_entities`
- `gbim_beliefs_v2`
- `governance_rag`
- `commons_rag`
- `legal_rag`
- `economic_rag`
- `gis_wv_benefits`
- `local_resources`
- `fayette_county_resources_2026`
- `autonomous_learner`
- `autonomous_learning`
- `conversation_history`
- other durable collections documented in the production inventory.

These collections are part of the **main corpus**. They are intended to outlive
individual sessions, support user-facing and system-facing retrieval, and remain
auditable against PostgreSQL, GBIM, source documents, or other verified backing
stores.

In spatial terms, these collections operate over the governed West Virginia
corpus of **55 counties, 546 tracts, 1,639 blockgroups, and 741 ZCTAs**. No
broader spatial coverage is claimed in this chapter.

**Retention boundary for GBIM-linked collections:** A Chroma vector in a
GBIM-linked collection such as `gbim_worldview_entities` or `gbim_beliefs_v2`
that corresponds to a `public.gbim_record` row is admissible for public claims
only when the backing PostgreSQL row carries `degradation_status IN ('fresh',
'aging')`. If that row's `degradation_status` transitions to `'stale'`, the
Chroma vector remains in the collection — it is not automatically deleted — but
the PostgreSQL lifecycle gate closes and the record is excluded from
`public_admissible_gbim_mv`. ChromaDB collection presence is therefore not the
controlling retention signal; the Postgres `degradation_status` gate is.

### 5.3.2 Internal-State Sandbox Chroma

Separate from the production corpus is a dedicated **internal-state Chroma**
used only for sandbox reasoning. This store is not a public-facing semantic
memory layer and must not be conflated with the main corpus instance.

Its purpose is to hold ephemeral, reversible internal reasoning state such as:

- working memory for an active reasoning session;
- hypothesis staging for possible interpretations or action paths;
- qualia-adjacent or mode-related internal signals used in introspective
  processing;
- reflection logs and self-evaluation traces; and
- temporary contradiction checks, synthesis drafts, and promotion candidates.

This sandbox store is intentionally isolated from the production corpus. It
exists so the system can think, test, compare, and revise before anything is
allowed to count as durable semantic memory.

### 5.3.3 Why the Separation Is Mandatory

The system must distinguish **long-term semantic memory** from **internal
reasoning workspace** for several reasons:

- production memory supports retrieval and therefore affects outward behaviour;
- workspace state is provisional and may include false starts, abandoned
  hypotheses, or contradictory partial views;
- persistent memory requires provenance and auditability that sandbox traces may
  not yet satisfy;
- corpus maintenance tasks such as rebuilds, re-chunking, or re-embedding must
  not overwrite or erase active sandbox reasoning; and
- promotion is an epistemic change in status, not just a copy operation from one
  database to another.

The architectural rule is therefore strict: **sandbox-local stores are not
production memory merely because they contain vectors or text**.

---

## 5.4 Ephemeral Sandbox Collections

The internal-state sandbox may use Chroma-style collections or equivalent
vectorised stores for short-lived internal cognition. These collections are
sandbox-local and are not part of the production corpus.

Illustrative collection families include:

```text
┌─────────────────────────────────────────────────────────────┐
│          Sandbox Collections and Their Roles                │
├─────────────────────────────────────────────────────────────┤
│  working_memory       — active session reasoning context    │
│  hypothesis_staging   — candidate interpretations, drafts   │
│  qualia_signals       — internal mode/coherence traces      │
│  reflection_logs      — self-review, introspection notes    │
│  contradiction_checks — temporary consistency traces        │
└─────────────────────────────────────────────────────────────┘
```

These stores function as a **workspace**, not as a long-term archive. They may
be flushed, summarised, anonymised, or partially retained only as governed audit
artifacts, depending on the promotion and review pathway.

The key implication is: the existence of a sandbox collection does **not** imply
that its contents should be retrievable as truth-bearing evidence in the same
way as `governance_rag`, `gbim_worldview_entities`, or `legal_rag`. Sandbox
vectors are not subject to the Postgres `degradation_status` lifecycle gate
because they have not yet entered the GBIM promotion path at all — they are
pre-candidate material.

---

## 5.5 Governed Memory State

### 5.5.1 A Stored Vector Is Not Self-Authorizing

In this architecture, a Chroma vector is never treated as self-authorizing
memory. A stored embedding may be a useful geometric object in H_App, but it
becomes governed memory only when it is accompanied by the metadata and gates
that make it safe to retain, retrieve, and act upon.

The governed memory state is modelled as:
