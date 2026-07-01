# Chapter 47 — H_p: Hilbert People Space Without Surveillance

The three Hilbert bodies established in earlier chapters — H_App (semantic), H_geo
(spatial), and H_t (temporal) — describe *what* the system knows, *where* it is anchored,
and *when* it happened. This chapter introduces the fourth axis that completes the civic
reasoning frame: **H_p — Hilbert People Space**, implemented as `jarvis-hilbert-people`.

The full civic reasoning state becomes:

```
H_App  ⊗  H_geo  ⊗  H_t  ⊗  H_p
 what       where      when      person-in-context
```

Every query that asks *who* — who signed a grant, who represented a community in a public
meeting, who organized the coalfield labor action of 1921 — activates all four spaces
simultaneously. The people axis is not an afterthought. It is the axis that makes the
system capable of genuine civic memory rather than just document retrieval.

The governing principle of this entire chapter:

> H_p should not ask *Who is this person, and what can we learn about them?*
> It should ask *Where does this person appear in a public, historical, permissioned, or
> accountable context? In what role? At what place? At what time? From what source?
> Under what disclosure rule?*

That is the difference between surveillance and historicity.

***

## The Three-Layer Identity Architecture

H_p does not store raw identity. It receives projections from a three-layer registration
system that governs what is sealed, what is private, and what is public.

### Layer 1 — KYC Private Vault

The KYC Docker is the sealed identity layer. It stores legal name, identity verification
records, private documents, private contact data, and sensitive verification material. It
is encrypted at rest, not embedded, not available for analytics, and not shared into
public space unless a strict authorization condition is met — court order, protective
emergency measure, constitutional review, or authorized safety process.

KYC answers exactly two questions:

- Is this person or entity verified?
- What verification level applies, and is it active, expired, or revoked?

KYC does not become the public person record.

> **The KYC rule:** KYC proves the person. KYC does not publish the person.

### Layer 2 — Private Participation Layer

Layer 2 is the default for all users. It uses a UUID that is explicitly *not* the KYC
identity:

```
kyc_subject_id  ≠  private_participation_uuid
```

This layer allows the system to serve users and collect privacy-preserving aggregate
metrics — users served, service categories requested, county-level usage, program
interest, referral outcomes, accessibility preferences — without exposing legal name,
home address, private hardship, or raw identity records.

> **The Layer 2 rule:** Layer 2 serves the person privately. Layer 2 may support
> aggregate metrics. Layer 2 does not make the person public.

### Layer 3 — Public User Layer

Layer 3 is optional and requires explicit user action. A user may choose to make their
name, organization, or public profile visible — as a partner, artist, volunteer, board
member, speaker, or contributor. The system never assumes Layer 3 and never moves a user
there without their decision.

> **The Layer 3 rule:** A user wanting to go public must make that decision. The system
> does not make it for them.

***

## How KYC Connects to H_p

KYC does not enter H_p directly. Instead, it produces a **verification assertion** — a
minimal, privacy-preserving claim that a subject has been verified at a given level,
without exposing the underlying identity records:

```json
{
  "subject_ref": "private_hash_91fa",
  "kyc_verified": true,
  "verification_level": "verified_human",
  "verification_status": "active",
  "raw_kyc_visible": false
}
```

H_p may receive the *class* of verification:

- `verified_human`
- `verified_organization`
- `verified_representative`
- `verified_public_role`
- `verified_historical_deceased`

H_p does not receive legal name, address, birthdate, ID scan, biometric record, private
documents, or sensitive household data.

The flow is:

```
KYC Docker
  ↓
encrypted verification
  ↓
private assertion (verification class only)
  ↓
permissioned person projection
  ↓
H_p (Hilbert People Space)
```

***

## What H_p Actually Stores

H_p stores **person appearances**, not person dossiers. A person appearance is:

> A person appeared in a source, in a role, at a time, in a place, under a disclosure
> rule.

The canonical record schema:

```json
{
  "appearance_id": "appearance_001",
  "person_ref": "person_hash_or_public_id",
  "name_as_recorded": "Name from source if allowed by disclosure rule",
  "role_in_record": "city council member",
  "event_or_document": "public meeting minutes",
  "place": "Mount Hope, WV",
  "date": "2026-05-12",
  "source_ref": "provenance_442",
  "merkle_ref": "merkle_991",
  "public_display_allowed": true,
  "reason_allowed": "official public role",
  "private_inference_allowed": false
}
```

This lets the system truthfully state:

> This person appeared in this public record in this role on this date.

It does not let the system state:

> Here is everything we know about this person.

***

## Person Categories and Disclosure Status

Every entity in H_p carries a classification that governs its disclosure rules.

| Category | Condition | Default Public | Notes |
|---|---|---|---|
| **Private verified user** | Layer 2 UUID only | No | Never exposed without Layer 3 opt-in |
| **Public opt-in user** | User explicitly chose Layer 3 | Yes — in chosen context | Scope limited to what user consented to |
| **Public official** | Holds elected or appointed office | Yes — in official role only | Home address, private life remain protected |
| **Public contributor** | Artist, volunteer, nonprofit officer, grant partner | Yes — in stated role only | Role-limited; no personal inference |
| **Historical person** | Source-bound, archival threshold met | Yes — as documented | Requires `source_ref`, `merkle_ref`, time logic |
| **Sensitive person** | Minor, victim, witness, benefits recipient | No | Sensitive flag overrides any public curiosity |
| **Unknown status** | No verified classification | No | Protected by default until verified otherwise |

The safety rules that govern this table:

- Unknown defaults to protected.
- Sensitive overrides public curiosity.
- Public role is context-limited, not a full identity grant.
- Historical status requires source and time logic — not assumed from age alone.

***

## Public Accountability Without Surveillance

Certain people should appear in H_p because they hold public accountability: mayors, city
council members, public agency staff, grant officers, board members, official signers,
public meeting speakers, contractors, project representatives, and elected officials. Their
inclusion is permitted — and necessary for civic memory — but it is bounded.

**Allowed:**

> Jane Doe appeared as city council member in public minutes dated May 12, 2026, in Mount
> Hope, Fayette County. Source: provenance_442. Merkle proof: merkle_991.

**Not allowed:**

> Here is Jane Doe's private life, relationships, home address, habits, or inferred
> beliefs.

> **The public accountability rule:** Public accountability allows role-bound civic
> context, not personal exposure.

***

## Historical People

H_p is the primary mechanism for place-based historical memory. People like Sarah
"Ma" Blizzard, Bill Blizzard, Mother Jones, local veterans, historic landowners, labor
organizers, teachers, and community builders are part of Appalachia's recorded knowledge
and belong in the system's civic memory — connected to role, event, place, time, and
source.

Historical person record:

```json
{
  "person": "Sarah Rebecca Blizzard",
  "status": "historical",
  "role": "labor organizer / community figure",
  "place": "West Virginia coalfields",
  "time_period": "early 1900s",
  "source_ref": "historical_record_123",
  "merkle_ref": "merkle_882",
  "public_display_allowed": true,
  "reason_allowed": "verified historical / public role"
}
```

The constitutional standard for historical inclusion:

> A private person becomes generally available for public historical treatment only after
> verified death and the required archival threshold — 70 years after verifiable death —
> unless they were already public in an official or historically documented role.

***

## The Trust and Proof Layer

No person claim enters H_p without provenance and Merkle backing. The three proof
services work together:

| Service | Function |
|---|---|
| **KYC Docker** | Encrypted identity verification vault; produces verification assertions only |
| **Provenance Docker** | Records the source lineage of every claim — where the person-role assertion came from |
| **Merkle Docker** | Tamper-evident proof that the source record has not been altered since it was ingested |

Every `appearance_id` in H_p carries a `source_ref` and a `merkle_ref`. A claim without
both is incomplete and should not be surfaced publicly.

***

## The Governance and Disclosure Layer

After provenance and proof, every person claim passes through the governance layer before
it can appear in a governed output.

```
Constitutional Docker
  → Is this person's appearance in this context allowed under the constitutional rules?
  → Possible verdicts: allowed / denied / redacted / generalized / escalated

Blood-Brain Barrier (BBB)
  → Should any private context that helped generate the answer be suppressed from output?
  → Enforces: private context may inform the answer; private context must not leak into it
```

The clean division of labor:

> KYC owns the secret.
> Provenance owns the source.
> Merkle owns the proof.
> Constitution owns the permission.
> BBB owns the crossing.
> I-Container owns the first-person boundary.

***

## How All Four Hilbert Spaces Work Together

A query activates all four spaces simultaneously. Example:

**Query:** *Who was involved in the Mount Hope community project?*

| Space | What It Contributes |
|---|---|
| **H_App** (semantic) | Project documents, topic vectors, service descriptions, relevant corpus chunks |
| **H_geo** (spatial) | Mount Hope, Fayette County, parcel geometry, agency jurisdiction, service area |
| **H_t** (temporal) | Meeting dates, grant cycles, archival periods, recency weights |
| **H_p** (people) | Source-bound person-role appearances linked to the project and place |
| **Provenance** | Source lineage for every named person and document |
| **Merkle** | Tamper-evident proof for each source record |
| **Constitution** | May each person be named in this context? |
| **BBB** | Should anything be redacted before public output? |

The governed answer would be:

> The publicly documented participants include [Name], listed as [role] in [source/date],
> and [Organization], listed as [role] in [source/date].

Not:

> Here is everything we know about everyone connected to this project.

***

## Aggregate Metrics Without Surveillance

Layer 2 supports useful system metrics that do not expose private identity.

**Acceptable metrics:**
- How many people used the system in a given period
- What service categories were most requested
- Which county or service area was involved
- Which resources and programs received referrals
- How many users opted into public Layer 3 profiles
- How many users remained private

**Not acceptable:**
- Individual behavioral trails
- Private identity linkage across sessions
- Inferred vulnerability scoring
- Unnecessary location history
- Sensitive profile building
- Public exposure of private Layer 2 users

> **The metric design principle:** aggregate first, pseudonymous where needed,
> identity-separated always, public only by consent.

***

## The Full Four-Space Architecture

```
                     Ms. Allis I-Container
                              |
                              v
                Constitutional Operating Frame
                              |
                              v
┌──────────────────────────────────────────────────────────────┐
│                     Four Hilbert Spaces                      │
├──────────────────────────────────────────────────────────────┤
│ H_App — Hilbert Semantic Space                               │
│   meaning, documents, concepts, services                     │
│                                                              │
│ H_geo — Hilbert Geographic Space                             │
│   place, jurisdiction, parcels, service areas                │
│                                                              │
│ H_t — Hilbert Time Space                                     │
│   dates, sequence, history, deadlines, archival age          │
│                                                              │
│ H_p — Hilbert People Space                                   │
│   person-in-context, public roles, historical actors,        │
│   consented users, private UUID projections                  │
└──────────────────────────────────────────────────────────────┘
                              |
                              v
┌──────────────────────────────────────────────────────────────┐
│                    Trust and Proof Layer                     │
├──────────────────────────────────────────────────────────────┤
│ KYC Docker        encrypted identity verification            │
│ Provenance Docker source lineage                             │
│ Merkle Docker     tamper-evident proof                       │
└──────────────────────────────────────────────────────────────┘
                              |
                              v
┌──────────────────────────────────────────────────────────────┐
│               Governance and Disclosure Layer                │
├──────────────────────────────────────────────────────────────┤
│ Constitutional Docker  allowed / denied / redacted           │
│ Blood-Brain Barrier    private-public crossing control       │
└──────────────────────────────────────────────────────────────┘
                              |
                              v
                       Governed Civic Answer
```

***

## Relationship to Earlier Chapters

| Chapter | Establishes | H_p Role |
|---|---|---|
| 04 — Hilbert Space & State | H_App as semantic Hilbert space; hilbert-state as state machine | H_p adds person-in-context as a fourth dimension to the state space |
| 42 — Post-Quantum Security | Signed, auditable provenance for all operations | Every H_p appearance record is signed; KYC assertions are cryptographically sealed |
| 43 — Role-Gated Knowledge | Access control by role over collections | H_p is itself a role-gated space; disclosure rules are enforced at query time |
| 44 — Phi Probe | Semantic coherence measurement across H_App | Person-role claims contribute to coherence scoring when sources corroborate each other |
| 45 — H_geo | Spatial body, PostGIS, GBIM entity binding | Every H_p appearance record carries a `place` field linked to H_geo geometry |
| 46 — H_App ⊗ H_geo | Tensor product bridge joining semantic and spatial | H_p extends the product to H_App ⊗ H_geo ⊗ H_t ⊗ H_p |
| 47 — H_t | Temporal axis, recency decay, ordered event timelines | Every H_p appearance carries a `date` that is scored by H_t recency logic |

***

## Implementation Notes

**Service name:** `jarvis-hilbert-people`

**Storage:** A dedicated PostgreSQL schema (`hilbert_people`) within `msjarvisgis` for
appearance records. Redis for short-lived session context (Layer 2 UUID mappings). No
Chroma collection for the people axis — person appearances are structured relational
records, not embeddings.

**KYC Docker isolation:** The KYC container must not share a network bridge with
`jarvis-hilbert-people`. KYC communicates only via the assertion endpoint (returning
verification class, not identity) and only when invoked by the Constitutional Docker or
an authorized safety process. Direct container-to-container calls from H_p to KYC are
not permitted.

**Sensitive flag enforcement:** The `sensitive_person` flag must be evaluated *before* the
Constitutional Docker verdict. A sensitive classification is not a constitutional question
— it is a hard stop. Sensitive records do not reach the constitutional layer; they are
suppressed by the BBB before routing.

**Merkle coverage:** Every ingest path that writes an appearance record to H_p must call
the Merkle Docker to stamp the source record before writing. Appearance records written
without a `merkle_ref` are incomplete and must not be surfaced by the semantic gateway.

***

*Formal derivation of the four-space tensor product H_App ⊗ H_geo ⊗ H_t ⊗ H_p and the
disclosure algebra over person categories are in the work-repo thesis. This chapter
documents the design principles, data model, and governance rules as the basis for
implementation.*
