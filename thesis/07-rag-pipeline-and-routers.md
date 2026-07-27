# 7. RAG Pipeline and Routers

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: July 27, 2026*

---

## 7.0 How to Read This Chapter (Rural Developer Guide)

This chapter is for anyone building or auditing a retrieval-augmented reasoning
system in a rural or under-resourced context. It explains, step by step, how
the Ms. Allis / Ms. Egeria Allis system routes a question through retrieval,
reasoning, validation, and promotion — and why each step exists.

The single most important idea in this chapter is this: **retrieval is not the
same as truth**. Pulling a passage from a database and using it to answer a
question are two different acts. Between those acts there is a governed pipeline
with real gates. This chapter documents that pipeline.

Five things a rural developer should take from this chapter:

1. The retrieval step does not query a generic evidence layer. It queries
   `public_admissible_gbim_mv`, a PostgreSQL materialized view that enforces a
   ten-condition admissibility predicate before any record can be seen by the
   retrieval step. If a record does not pass that predicate, the retrieval step
   cannot return it.
2. Retrieved material enters a sandboxed reasoning workspace, not a production
   answer buffer. Nothing is committed until it passes downstream gates.
3. Model outputs inside the sandbox are candidate reasoning steps, not
   conclusions.
4. Three sequential gates — truth filtering, constitutional review, and DGM
   gating — must pass before any candidate reasoning step becomes validated
   state.
5. The router is upstream of commitment; it proposes context, it does not
   authorize action.

---

## 7.1 Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis routes retrieval, context assembly, model
inference, and validation through a governed reasoning pipeline rather than
treating RAG as a direct bridge from query to answer or from retrieval to
durable state.

It supports:

- **P1 — Every where is entangled** — semantic, spatial, temporal, governance,
  and registry context are assembled into a common reasoning path rather than
  left as disconnected retrieval outputs.
- **P3 — Power has a geometry** — router behavior is inspectable as a sequence
  of retrieval from a governed evidence surface, sandbox reasoning, truth
  filtering, constitutional review, DGM gating, and controlled promotion.
- **P5 — Design is a geographic act** — routing decisions determine not only
  what information is seen, but what may become consequential within the system.
- **P12 — Intelligence with a ZIP code** — WV-first and place-aware routing is
  preserved while ephemeral reasoning context is distinguished from
  approved action-bearing state.
- **P16 — Power accountable to place** — no retrieved or generated content
  becomes durable memory, production action, or authoritative answer merely
  because it was routed into context.

This chapter belongs to the **Computational Instrument** tier. It defines the
router not as a direct answer engine but as the upstream coordinator of a gated
reasoning pipeline whose outputs remain provisional until validated and promoted.

---

## 7.2 Purpose and Scope

This chapter describes how Ms. Allis assembles and routes context from semantic
memory, spatial stores, registries, and related services into the live reasoning
path. The routing model reflects the actual operational pipeline in which
retrieval feeds the internal-state sandbox rather than directly producing
production action, persistence, or self-authorizing conclusions.

RAG retrieval remains essential. Retrieved material is routed into a provisional
internal reasoning regime where it serves as candidate context for
interpretation, comparison, and validation.

**The authoritative evidence surface for the retrieval step is
`public_admissible_gbim_mv`.** This is a PostgreSQL materialized view over
`public.gbim_record` whose `WHERE` clause enforces a ten-condition admissibility
predicate including `promotion_state = 'authorized'`, `public_claim_allowed =
true`, `degradation_status IN ('fresh', 'aging')`, `spatial_unit_id IS NOT
NULL`, `spatial_unit_kind IS NOT NULL`, and `valid_time_start IS NOT NULL`
(Appendix A, §A.4). Any description of the retrieval step as querying a generic
or loosely bounded evidence layer should be read as referring to this view. The
view is the governing contract between the retrieval step and the governed
corpus; material excluded by the view predicate is invisible to the retrieval
step.

The central rule of this chapter is simple: **RAG provides context to sandboxed
reasoning, not direct authority to production consequence**.

---

## 7.3 Routing Path

The routing path starts at the query and ends at the sandbox — not at a
production answer.

A user query, internal signal, or scheduled reasoning task first triggers router
selection over available sources such as semantic memory, GIS-aware stores,
registry data, governance text, and other task-specific layers. The retrieved
material is assembled into a context package and passed into the internal-state
sandbox, where it becomes part of a reversible reasoning cycle rather than an
immediately committed answer or memory update.

**Retrieval from structured GBIM-linked stores queries `public_admissible_gbim_mv`
directly.** This materialized view is the only surface through which governed
corpus evidence enters the retrieval step; records excluded by the
admissibility predicate do not appear in the context package regardless of their
presence in `public.gbim_record`. The view is refreshed by
`runtime_governance.refresh_public_admissible_gbim_mv()` on the schedule defined
by the pg_cron lifecycle runners (Appendix A, §A.10).

The routing path is formally:

\[
Q \;\rightarrow\; R_{\mathrm{retrieve}}(\text{\textit{public\_admissible\_gbim\_mv}})
\;\rightarrow\; C_{\mathrm{assembled}} \;\rightarrow\; S_{\mathrm{sandbox}}
\]

The router is therefore a context-construction mechanism feeding deliberation,
not a bypass around validation.

**Step-by-step for rural developers:**

1. A query arrives (user, internal signal, or scheduler).
2. The router selects source layers appropriate to the query type.
3. For GBIM-linked evidence, the retrieval step queries
   `public_admissible_gbim_mv`. Only records passing all ten admissibility
   conditions are returned.
4. For vector-based semantic retrieval (Chroma), only collections in the
   production corpus are queried; sandbox-local Chroma collections are not
   reachable from the retrieval step.
5. Retrieved material is assembled into a context package.
6. The context package enters the internal-state sandbox as provisional input.

---

## 7.4 Ephemeral RAG Context

RAG outputs are **ephemeral reasoning context until promoted**.

A retrieved passage, GIS feature set, registry result, landowner record, or
semantic memory hit may be highly relevant, but relevance alone does not make
it durable memory, public output, or actionable system state. Retrieval creates
a temporary interpretive window inside the internal-state sandbox, where the
material may be compared, rejected, refined, contradicted, or staged for further
review.

The correct statement is that RAG outputs remain sandbox-local context until
applicable gates approve promotion into validated response, memory, or
action-bearing state. Even a context package assembled entirely from
`public_admissible_gbim_mv` — records that have passed the full ten-condition
predicate — is still provisional at the sandbox boundary. Admissibility in the
evidence surface means the evidence is safe to retrieve; it does not mean the
reasoning product assembled from that evidence is safe to commit.

**For rural developers:** think of the admissible evidence surface as a
pre-screened library. The library contains only verified books. But reading from
a verified book does not make your notes correct — the reasoning step still has
to happen, and the validation gates still apply.

---

## 7.5 Candidate Reasoning Steps

Model outputs inside the routed context are **candidate reasoning steps**, not
final authoritative conclusions.

Once context has been routed into the sandbox, model-generated statements,
intermediate inferences, hypotheses, summaries, or proposed next steps are
provisional transformations over the current state. They are candidate reasoning
steps that may support interpretation, but they do not yet carry durable
authority.

This distinction is important because it aligns the routing chapter with the
sandbox architecture documented elsewhere. A model output can be useful,
coherent, and well-grounded in material drawn from `public_admissible_gbim_mv`
while still failing later truth checks, constitutional checks, or DGM
admissibility requirements. The quality of the evidence surface does not
substitute for the validation gates.

---

## 7.6 Truth, Constitutional, and DGM Gates

The post-routing validation sequence is explicit and sequential.

After candidate reasoning steps are formed inside the sandbox, they must pass
three gates before becoming validated state:

1. **Truth filtering** — evaluates whether claims are sufficiently supported by
   evidence, provenance, consistency, or grounded retrieval. Evidence grounded
   in `public_admissible_gbim_mv` enters this gate with the ten-condition
   predicate already satisfied, which reduces but does not eliminate the
   evidentiary burden at this step.
2. **Constitutional review** — checks the content against the governing
   principles, permissions, and boundary conditions of the system.
3. **DGM gating** — evaluates whether the candidate state is admissible for
   promotion under the system's operational and safety criteria.

In plain prose: router output becomes sandbox context; sandbox context yields
candidate reasoning; candidate reasoning faces truth filtering, constitutional
review, and DGM gating; only approved results proceed toward consequence.

**For rural developers:** these three gates are the checkpoints between "the
system has an idea" and "the system does something with that idea." Skipping any
gate collapses the distinction between retrieval and action — which is exactly
the failure mode this architecture is built to prevent.

---

## 7.7 Raw to Validated Chain

The full transition chain formalizes router behavior:

\[
S_{\mathrm{raw}} \;\rightarrow\; S_{\mathrm{sandbox}} \;\rightarrow\;
S_{\mathrm{validated}} \;\rightarrow\; S_{\mathrm{memory}} \;\rightarrow\;
S_{\mathrm{action}}
\]

where:

- \(S_{\mathrm{raw}}\) is the initial retrieved and assembled context, drawn
  from `public_admissible_gbim_mv` for GBIM-linked evidence and from production
  Chroma collections for semantic evidence;
- \(S_{\mathrm{sandbox}}\) is the provisional internal reasoning state;
- \(S_{\mathrm{validated}}\) is the state that has passed truth, constitutional,
  and DGM checks;
- \(S_{\mathrm{memory}}\) is the subset approved for durable retention, which
  upon promotion writes to `public.gbim_record` with all required `NOT NULL`
  spacetime and provenance columns; and
- \(S_{\mathrm{action}}\) is the subset approved for external consequence or
  operational execution.

This chain clarifies that routing is only the opening movement of the pipeline.
The router is upstream of commitment, not identical with commitment.

**Note on the transition from \(S_{\mathrm{validated}}\) to
\(S_{\mathrm{memory}}\):** promotion to memory writes a row to
`public.gbim_record` that must satisfy `spatial_unit_id IS NOT NULL`,
`spatial_unit_kind IS NOT NULL`, and `valid_time_start IS NOT NULL` — enforced
by the `gbim_record_spacetime_provenance_chk` constraint. The database will
reject the write if those fields are absent. At the next scheduled refresh of
`public_admissible_gbim_mv`, a freshly promoted row will enter the admissible
evidence surface if and only if all ten conditions of the predicate hold.

---

## 7.8 Router Semantics and Non-Commitment

The router is a proposal-forming subsystem.

Its job is to select sources, assemble context, and shape the initial conditions
under which reasoning occurs. It does not itself authorize memory writes, public
claims, tool execution, geospatial state changes, or governance consequence.

Even a successful routing pass — one that correctly selects sources, retrieves
only admissible evidence from `public_admissible_gbim_mv`, and assembles a
coherent context package — should be interpreted as non-committing. The router
may have done its job perfectly and still produce a candidate state that is
later rejected, revised, quarantined, or escalated.

**For rural developers:** a router that returns good results is not a router
that has answered the question. It has handed a well-sourced brief to a
deliberation process. That deliberation process has its own gates and its own
authority structure. Confusing the two is the most common architectural error
in RAG systems built without an explicit validation layer.

---

## 7.9 Relation to GeoDB and Hilbert Framing

The routing chapter remains linked to the spatial and formal chapters.

RAG routing may gather material from semantic stores, GeoDB resources,
registries, and other domain-specific layers, but those routed materials only
become operationally meaningful through the same governed transition logic
described in the Hilbert and governed-state chapters. In that sense, routed
context is an input to state formation across \(H_{\text{App}}\),
\(H_{\text{geo}}\), temporal, and people-linked domains, but it does not
directly determine the committed state of those domains.

The connection to `public_admissible_gbim_mv` is specifically the connection
between the retrieval step and \(H_{\text{geo}}\) at the operational level.
The materialized view surfaces only those records that carry `spatial_unit_id`
(blockgroup GEOID), `spatial_unit_kind` (`'blockgroup'`), and `valid_time_start`
as non-null values — the same three columns added to the governed state
definition on July 26, 2026. The retrieval step therefore draws from a spatially
and temporally anchored evidence surface, not from a raw coordinate store.

This keeps the chapter consistent with the view that vectors, retrievals, and
generated outputs are not self-authorizing. They must become governed, validated,
and promoted before they count as operational state.

---

## 7.10 Revision Principle

The governing revision principle for this chapter is:

- RAG retrieval provides context into the internal-state sandbox, not direct
  production action or persistence.
- The retrieval step queries `public_admissible_gbim_mv` as the authoritative
  evidence surface for GBIM-linked records. This materialized view enforces a
  ten-condition admissibility predicate (Appendix A, §A.4). Any reference to a
  generic or loosely bounded retrieval layer refers to this view.
- RAG outputs are ephemeral reasoning context until promoted. Admissibility in
  the evidence surface does not substitute for downstream validation gates.
- Model outputs inside the routed context are candidate reasoning steps, not
  final conclusions.
- Candidate reasoning steps must pass truth filtering, constitutional review,
  and DGM gating before they become validated state.
- Router behavior is formalized through the transition chain
  \(S_{\mathrm{raw}} \rightarrow S_{\mathrm{sandbox}} \rightarrow
  S_{\mathrm{validated}} \rightarrow S_{\mathrm{memory}} \rightarrow
  S_{\mathrm{action}}\), where \(S_{\mathrm{raw}}\) is drawn from
  `public_admissible_gbim_mv` for GBIM-linked evidence.
- Promotion to \(S_{\mathrm{memory}}\) writes to `public.gbim_record` subject
  to the `gbim_record_spacetime_provenance_chk` constraint; the row will appear
  in `public_admissible_gbim_mv` only after the next scheduled refresh and only
  if all ten admissibility conditions hold.
- The router is upstream of commitment and must not be documented as a direct
  persistence or action mechanism.

Under this revised framing, the RAG pipeline remains central to Ms. Allis, but
it is documented as the context-routing front end of a governed reasoning
architecture: retrieval queries a governed evidence surface
(`public_admissible_gbim_mv`), retrieval feeds sandbox deliberation,
deliberation yields candidate reasoning, validation determines admissibility,
and only promoted state becomes durable or consequential.

---

*Chapter 7 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Egeria Allis is an original system designed and built by Carrie Ann Kidd.*
*See LICENSE for terms.*
