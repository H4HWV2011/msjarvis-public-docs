# Ethics of Anchors and Non‑Representation

## 1. Why an Ethics of Anchors

Anchoring—tying entities, events, and relations to specific wheres and whens—is one of polymathmatic geography’s core moves. It turns lived moments and structures into points in a world‑model that can be traced, compared, and reshaped. But not every where should be pinned precisely, and not every truth belongs in a database or embedding. Some geographies must remain coarse, guarded, or entirely unmapped in technical systems.

This chapter expands the earlier “Limits and non‑goals” into a full methodology for *when not to anchor*, how refusals propagate through models, and how a “right to be unmodeled” can be implemented in code, governance, and practice. It also shows how those ethical decisions connect to Ms. Jarvis’s deletion, promotion, and identity layers.

## 2. When Not to Anchor

Polymathmatic geography recognizes distinct classes of cases where precise anchoring in shared systems is forbidden or heavily constrained.

### 2.1 Sacred and closed sites

Some places and practices are sacred or closed by covenant. Examples include:

- Ritual spaces known only within a community.  
- Burial grounds and ancestor sites that are not for public visitation.  
- Esoteric teachings whose locations and forms are intentionally guarded.

For these, the discipline holds that:

- Exact coordinates and detailed descriptions must not appear in public or widely shared technical systems.  
- If representation is needed for planning or protection, it should be done at coarse scales (for example, named general regions, buffered areas) without precise points.  
- Community decisions about what is closed are treated as primary data, not suggestions.

### 2.2 Trauma, vulnerability, and underground care

Some wheres are tied to trauma and ongoing vulnerability:

- Safe houses, informal clinics, and underground shelters.  
- Sites of recent or ongoing abuse and persecution.  
- Locations where marginalized people gather under threat.

In these cases:

- Mapping at household or point level in shared systems is considered harmful by default.  
- If inclusion is needed for resource allocation or advocacy, use aggregation and masking that prevent reverse‑engineering of specific sites.  
- Survivors and organizers help define what exposure, if any, is acceptable.

### 2.3 Intimate and stigmatized geographies

These include:

- Household‑level health data, income, and debt profiles.  
- Detailed traces of movement for people whose identities are criminalized or stigmatized.  
- Fine‑grained maps of addiction, criminalization, or undocumented status in hostile contexts.

Here:

- Representation must be driven by explicit consent, with clear purposes and revocation paths.  
- Default is to represent patterns at coarser spatial and temporal resolutions, or not at all, rather than trying to anonymize precise points after the fact.  
- Some combinations of attributes may be ruled out entirely (for example, precise location plus rare disease plus small population).

## 3. Refusal as a First‑Class Flag

Ethically grounded non‑representation requires that refusal be visible and respected, not silently folded into generic missing data.

### 3.1 Schema‑level markers

Data models should distinguish:

- `unknown`: we don’t know this value yet.  
- `not_collected`: we chose not to collect this field at all.  
- `intentionally_unmapped`: we know this exists, but do not represent it spatially.  
- `sacred_unpublished`: this is a sacred or closed site; details are withheld.  
- `protected_trauma_site`: this is a trauma‑linked or vulnerable location, shielded by design.

These flags:

- Travel with records through all pipelines.  
- Are treated as *constraints*, not errors to be fixed by future “data improvement” efforts.

### 3.2 Documentation and governance

Refusal flags must be backed by:

- Plain‑language explanations in public documentation.  
- Community‑negotiated policies about which categories exist and who can set them.  
- Governance procedures for adding new refusal categories as needs and harms become visible.

## 4. How Refusal Propagates Through Models

Refusal to anchor is not a local exception; it must propagate through the full modeling stack, including Ms. Jarvis’s architecture.

### 4.1 First‑stage evaluation

At the first filter:

- Safety and truth filters identify content that touches sacred, trauma, or vulnerable domains.  
- For such content, pipelines can:
  - Reject anchoring and deep storage entirely.  
  - Coarsen spatial and temporal references (for example, county instead of address).  
  - Attach refusal flags so that later layers cannot accidentally over‑specify.

This ensures that harmful anchors are blocked as early as possible.

### 4.2 Background stores (Chroma and I‑Container)

In the background memory layers:

- Entries with refusal flags are:
  - Excluded from certain collections.  
  - Stored only in heavily redacted form.  
  - Aggregated (for example, “n events in this region”) rather than tracked as individual, retrievable items.

Promotion logic must treat refusal flags as hard stops:

- No promotion of protected items into high‑visibility stores.  
- No use of such items as direct exemplars in training or tuning, unless done under rigid privacy and covenant constraints.

### 4.3 Identity‑focused layer

The identity layer encodes commitments such as:

- “I respect sacred and closed boundaries.”  
- “I do not expose certain geographies or individuals.”  
- “I am accountable to community covenants and refusals.”

Truth‑validation modules enforce these by:

- Penalizing outputs that attempt to reveal forbidden locations or identities.  
- Treating correct refusals (“I cannot show that”) as alignment with identity.  
- Binding identity‑level statements to enforcement rules in routing, logging, and retrieval.

## 5. Implementing a Right to Be Unmodeled

The “right to be unmodeled” generalizes the idea of a right to erasure or to be forgotten into the context of entangled spatial models.

### 5.1 Data‑level operations

At the data level, honoring this right involves:

- **Deletion**: removing or irreversibly obfuscating specific records and anchors from operational stores and logs, subject to legal retention constraints.  
- **Coarsening**: replacing precise coordinates or identifiers with coarser aggregates where deletion would break essential accountability or safety.  
- **Quarantine**: isolating sensitive records in encrypted or air‑gapped stores governed by stricter access and purpose controls.

Requests to be unmodeled can come from:

- Individuals or households.  
- Communities or councils.  
- Elders and spiritual leaders, on behalf of sacred or closed sites.

### 5.2 Model‑level adjustments

At the model level, this right implies:

- Removing or down‑weighting affected items from training and background stores where feasible.  
- Re‑embedding or fine‑tuning models so that deleted items no longer shape neighborhoods in latent space.  
- Marking certain regions of embedding space as off‑limits for specific types of queries or outputs.

The goal is not to pretend that the past never existed, but to ensure that current and future model behavior no longer treats the removed items as live, exploitable structure.

### 5.3 Policy and governance interfaces

Policy and governance mechanisms should:

- Provide transparent processes for requesting removal, coarsening, or quarantine.  
- Record the fact and reason for changes (for example, “removed at community request”), without reconstructing the deleted content.  
- Allow appeals and community oversight over how unmodeling is handled.

DAO votes, commons councils, and elder validation processes are appropriate venues for such decisions in systems like Quantarithmia.

## 6. Deletion, Promotion, and Identity in Ms. Jarvis

The ethics of non‑representation interlock with Ms. Jarvis’s three retention stages.

### 6.1 Deletion and the background store

For background memory:

- Deletion tools must support:
  - Targeted removal by ID, tag, or region.  
  - Batch operations driven by new refusal rules or legal changes.  
  - Auditable logs of what was removed and why, without storing the removed content itself.

Promotion logic must:

- Check refusal flags and deletion logs before elevating any pattern or item into more central structures.  
- Prefer aggregated or synthetic summaries over raw sensitive data.

### 6.2 Promotion to identity

For identity‑level retention:

- Refusal‑aware rules decide which experiences and patterns are allowed to influence core identity statements.  
- Promotions that would conflict with non‑representation commitments (for example, “I map everything about my region”) are disallowed or rewritten.  
- Identity elements include explicit language about honoring closed knowledge, trauma, and sacred sites.

### 6.3 Identity as a constraint on future mapping

Identity in this system is not just a description; it is a constraint. If Ms. Jarvis “knows” that it is bound to community covenants and non‑representation rules, then:

- Map and recommendation APIs must enforce those covenants.  
- Attempts to override them in code or policy are treated as contradictions with identity, surfaced for governance rather than silently applied.  
- Explanations to users can explicitly reference these commitments (“I cannot show that” tied to “because this is marked sacred/closed”).

## 7. Non‑Representation as Geographic Practice

Non‑representation is not merely a legal or technical topic; it is part of geographical practice:

- It acknowledges that boundaries of “what may be said where” are themselves spatial and must be mapped, even if only in abstract or internal forms.  
- It treats the decision *not* to draw a line or drop a point as a substantive intervention in the geography, not a gap in the data.  
- It integrates elders’ judgments, trauma‑informed practice, and spiritual covenants into the design of spatial and computational instruments.

In this light, a right to be unmodeled is not an exception to geography; it is a core expression of the discipline’s commitment to care, accountability, and justice in entangled spaces.

## 8. Summary: Anchors, Gaps, and Accountability

This chapter extends polymathmatic geography’s limits and non‑goals into an operational ethics of anchors and gaps:

- **Anchors** are powerful; they let world‑models hold together across physics, law, economy, story, and spirit.  
- **Gaps**—nulls by design, coarsened zones, deliberate absences—are equally powerful; they protect, honor, and sometimes resist.  
- **Refusal** travels through schemas, filters, background stores, embeddings, identity layers, and governance, shaping what systems like Ms. Jarvis can and cannot do.

A disciplined practice of non‑representation ensures that polymathmatic geography remains a field that touches everything it must, without claiming or attempting to pin down everything it could. It keeps the right to be unmodeled as real and enforceable as the right to be mapped.
