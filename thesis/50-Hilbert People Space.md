# 50-Hilbert People Space — Person-in-Context Without Surveillance

*Design document — work-repo thesis. Status: **built and operational.** H_people runs as
a Postgres schema `hp` in database `hilbert_people` on `msjarvisgis-db`, served by
`jarvis-hilbert-state` (image `jarvis-main-brain:latest`, host port 18092), coordinated
alongside H_t and Redis. As of this writing the appearance ledger holds live records and
the disclosure-assertion gateway is verified end-to-end — it correctly permits backed
subjects and denies unbacked ones, persisting every verdict to `hp.appearance_assertion`.
The fourth Hilbert body is real and measurable; the MountainShares-Commons evidence
pipeline extends to probe the `hp` schema and the architecture moves from three measured
bodies to four under the same regenerate-from-evidence discipline.*

## 1. Where this fits

Ms. Allis reasons over coupled Hilbert bodies. Three are running and measured today:

```
Hilbert Semantic Space (H_App)  = meaning   → ChromaDB
Hilbert Geographic Space (H_geo) = place    → PostGIS
Hilbert Time Space (H_t)         = history / sequence / recency → Redis timelines
```

This chapter documents the **fourth** body, now built and running:

```
Hilbert People Space (H_people)  = person-in-context
```

The full civic reasoning state becomes a four-way tensor product:

```
Civic State = meaning ⊗ place ⊗ time ⊗ person-in-context
            = H_App ⊗ H_geo ⊗ H_t ⊗ H_people
```

## 2. The governing rule

> **Hilbert People Space is not a surveillance database. It is a public, historical,
> role-based, consent-governed person-context space.**

The system is not tracking people. It represents a person **only** when they appear in a
sourced, permissioned, public, historical, or accountable role. The distinction is
between **surveillance** and **historicity**.

H_people never asks *"Who is this person, and what can we learn about them?"* It asks:

```
Where does this person appear in a public, historical, permissioned, or accountable context?
In what role? At what place? At what time? From what source? Under what disclosure rule?
```

## 3. What H_people stores: appearances, not dossiers

H_people stores **person appearances** — a person appeared in a source, in a role, at a
time, in a place, under a disclosure rule — not full person records.

```json
{
  "appearance_id": "appearance_001",
  "person_ref": "person_hash_or_public_id",
  "name_as_recorded": "Name from source if allowed",
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

This lets the system say *"This person appeared in this public record in this role on
this date,"* and structurally prevents it from saying *"Here is everything we know about
this person."*

## 4. The three-layer registration system

### Layer 1 — KYC Private Vault
The sealed identity layer: legal name, identity verification, private documents and
contact data, sensitive verification records. It is encrypted, sealed, not embedded, not
used for analytics, not exposed to H_people. Access only under court order, protective
emergency measure, constitutional/legal review, or authorized safety process.

KYC answers only: *is this person/entity verified, at what level, and is the verification
active/expired/revoked?* **KYC proves the person; KYC does not publish the person.**

### Layer 2 — Private Participation Layer (default)
A separate UUID that is **not** the KYC ID:

```
kyc_subject_id ≠ private_participation_uuid
```

Serves users and supports privacy-preserving aggregate metrics (users served, service
categories, county-level usage, referral success, repeat engagement, accessibility
preferences, eligibility tags) **without** exposing legal name, address, hardship, or raw
KYC records. *Layer 2 serves the person privately and may support aggregate metrics; it
does not make the person public.*

### Layer 3 — Public User Layer (opt-in only)
Exists only when a user explicitly chooses to be public — named as partner, artist,
volunteer, board member, speaker, or contributor. Default is private in Layer 2; public
only by explicit opt-in. *The system never assumes it.*

## 5. KYC → H_people: assertion, not identity

KYC does not enter H_people. It emits a **verification assertion**:

```json
{
  "subject_ref": "private_hash_91fa",
  "kyc_verified": true,
  "verification_level": "verified_human",
  "verification_status": "active",
  "raw_kyc_visible": false
}
```

H_people may receive *verified human / organization / representative / public role /
historical-deceased status*. It must never receive legal name, address, birthdate, ID
scan, biometric, private documents, or sensitive household data. Flow:

```
KYC Docker → encrypted verification → private assertion
           → permissioned person projection → Hilbert People Space
```

## 6. Person categories (by disclosure status)

```
1. Private verified user   — default: private Layer 2 UUID only
2. Public opt-in user      — public only because the user chose it
3. Public official         — public only in official capacity
4. Public contributor      — artist/volunteer/speaker/officer/owner/grant partner,
                             public only in the role they entered
5. Historical person       — public when source-bound and historical/death threshold met
6. Sensitive person        — minor, victim, witness, benefits recipient, medical/legal/
                             housing subject; protected even if mentioned in a record
7. Unknown status          — treated as private until verified otherwise
```

Safety rule: **unknown defaults to protected; sensitive overrides public curiosity;
public role is context-limited; historical status requires source and time logic.**

## 7. Public accountability without surveillance

Public-accountability figures (mayors, council members, agency staff, grant officers,
board members acting publicly, official signers, public speakers, contractors, elected
officials, organization representatives) may appear — but only **in relation to their
public role**.

- Allowed: *"Jane Doe appeared as city council member in public minutes dated May 12,
  2026."*
- Not allowed: private life, relationships, home address, habits, inferred beliefs.

> Public accountability allows role-bound civic context, not personal exposure.

## 8. Historical people

Historical figures (e.g., Sarah "Ma" Blizzard, Bill Blizzard, Mother Jones, local
veterans, historic landowners, teachers, labor organizers) connect person → role → event
→ place → time period → source → historical significance.

Proposed constitutional standard:

> A private person becomes generally available for public historical treatment only after
> verified death and a required archival threshold — e.g., 70 years after verifiable death
> — unless they were already public in an official or historically documented role.

## 9. Trust, proof, and disclosure layers

```
KYC Docker            = encrypted verification vault   — owns the secret
Provenance Docker     = source lineage                 — owns the source
Merkle Docker         = tamper-evident proof           — owns the proof
Constitutional Docker = allowed / denied / redacted    — owns the permission
Blood-Brain Barrier   = private→public crossing control — owns the crossing
I-Container           = Ms. Allis first-person boundary — owns the first person
```

**Closed disclosure vocabulary (verified in the running gateway).** Claim types are
**allowlisted**, not open. The assertion gateway distinguishes three outcomes, all observed
in regression:

- **Unknown claim type** (e.g. `not_a_real_claim`) → rejected at the HTTP layer with
  `403 — "Claim type is not in the approved list."` It never becomes a verdict. The
  disclosure vocabulary is closed; you cannot ask a question the system isn't sanctioned to
  answer.
- **Valid claim, backing supports it** (e.g. `verified_county_resident` for a backed
  subject) → `200, result: true`, persisted to `hp.appearance_assertion`.
- **Valid claim, backing does not support it** (e.g. `verified_adult` for a subject whose
  backing doesn't establish it) → `200, result: false`, persisted. A legitimate, logged
  "no" — distinct from "you may not ask."

The `403`-on-unknown vs. `200 false`-on-unsupported distinction is load-bearing: it
separates *vocabulary control* (which questions exist) from *evidence control* (whether the
answer is yes), and both are enforced and audited.

## 10. Four-space query flow

Query: *"Who was involved in the Mount Hope project?"* activates all four spaces plus the
trust/governance layers:

```
Semantic  : what project, documents, topic
Geo       : Mount Hope, Fayette County, parcels, agencies, jurisdiction
Time      : year, meeting, grant cycle, historical period
People    : who appears in source-bound public or permissioned records
Provenance: where each person-role claim came from
Merkle    : has the record/proof been altered
Constitution: may this person be named in this context
BBB       : redact anything before output
```

Governed output names only source-bound, permissioned participants and their roles —
never "everything we know about everyone connected to this project."

## 11. Metrics without surveillance

Acceptable (Layer 2, aggregate): users served, help categories, county/service area,
most-requested resources, referral counts, public-page views, opt-in vs. private counts.

Avoid: individual behavioral tracking, private identity trails, unnecessary location
history, sensitive profile building, inferred vulnerability scoring, exposure of private
users.

Design posture: **aggregate first; pseudonymous where needed; identity-separated always;
public only by consent.**

## 12. Mapping to the running stack

Most of the *governance* machinery already exists; the net-new is the person store, the
vault, and the registration tiers.

| Design component | Stack status | Maps to / becomes |
|---|---|---|
| Blood-Brain Barrier | **exists** (`jarvis-blood-brain-barrier`) | extend to redact person-names per disclosure rule |
| Constitutional Docker | **exists** (Constitutional Guardian) | extend verdict logic to person-disclosure |
| Provenance + Merkle | **partial** (PQ signing / append-only audit) | reuse for per-appearance provenance and merkle_ref |
| Assertion gateway | **exists** (already gates the wallet/balances path) | the same `result: true/false` pattern is the disclosure gate |
| I-Container | **exists** | unchanged; owns the first-person boundary |
| Hilbert People Space | **built and serving** — Postgres schema `hp` (13 tables) in DB `hilbert_people` on `msjarvisgis-db`, served by `jarvis-hilbert-state`; appearance ledger populated, disclosure-gate verified | live; extend the Commons collector to probe it |
| KYC Private Vault | **net-new** | new sealed, encrypted store, outside the Hilbert spaces |
| Three-layer registration | **partial** (`registration language.md` exists) | new: UUID separation + opt-in gating |

Note: the assertion-gateway-as-policy-gate is **already running** in the balances route
(`_assert_claim(public_uuid, "verified_state_resident", …) → result: true/false`). The
disclosure permission model for H_people is the same pattern keyed to a `public_uuid`
with raw identity sealed elsewhere — reuse, not new architecture.

## 13. Design decisions — resolved at build, and still-open

**13.1 — Separate store, or person-typed GBIM extension? → RESOLVED: separate store.**
The built implementation uses a dedicated Postgres schema `hp` (13 tables, appearance-centric)
in database `hilbert_people`, not a person-typed GBIM record. The appearance ledger
(`hp.appearance` + satellite tables for name/role/source/place/time/assertion/verdict/
suppression) stands on its own, with the KYC vault in a separate database the appearance
role cannot reach. *Original design note retained below for provenance.*

A "person appearance" (`person_ref + role + place + time + source + disclosure_rule`) is
structurally a GBIM entity. GBIM already binds claims to where/when/source/confidence in
PostGIS. Implementing appearances as a person-typed GBIM record with disclosure
governance on top would reuse H_geo's machinery and keep person-context spatially and
temporally joined automatically. The KYC vault stays separate regardless; the
*appearances* may not need a wholly separate store. **Built decision: dedicated `hp`
schema.**

**13.2 — Unlinkability is the load-bearing guarantee. → IMPLEMENTED at the database level.**
The migration enforces this structurally: the `hilbert_app` role is granted SELECT/INSERT/
UPDATE on the `hp` schema only, is REVOKEd from `public`, and has **no connect rights to
the KYC vault database** (enforced at `pg_hba` per the migration's documented posture). The
appearance side and the identity side live in separate databases, and the role that reads
appearances literally cannot reach KYC. Additionally, `hp.appearance_name` carries an
inline DDL prohibition (`legal_name is FORBIDDEN here — store public display values only`),
and the schema comment declares it appearance-centric with no identity mirrors. The
`kyc_subject_id ≠ private_participation_uuid` separation is therefore not a convention but a
grant-and-database boundary. *Original design note retained below for provenance.*

The entire anti-surveillance promise rests on `kyc_subject_id ≠ private_participation_uuid`
being genuinely unlinkable. If the two can be re-joined by anyone short of a court order,
the design collapses. The mapping must be one-way and access-gated at the same
constitutional level as the KYC vault itself — not merely two columns in a table.

**13.3 — Rural re-identification risk in Layer 2 metrics. → STILL OPEN.**
"County-level usage + service category + repeat engagement + accessibility preferences"
sounds aggregate, but in a county of a few thousand, "user in this county requesting this
rare service" can resolve to one person — the k-anonymity problem, sharpened by rural WV
population scale. Metrics need small-cell suppression / minimum-count thresholds before any
breakdown is exposed, or the "metrics without surveillance" guarantee leaks exactly where
the most vulnerable users are. **Suppression thresholds must be defined before any Layer 2
breakdown is surfaced.**

**13.4 — Sensitive-person category overlaps BSA. → STILL OPEN.**
The "sensitive person" category (minors, victims, witnesses, **benefits recipients**)
overlaps exactly with Benefits-Sensitive Accounts. A BSA flag *is* a sensitive-person
status. Wiring both to the same protected-default would let the two systems reinforce each
other rather than run parallel. **Recommended: unify the protected-default.**

## 14. The design principles, as built

The principles below are the governing rules; the build realizes 1–10 as the `hp` schema,
the `hilbert_app`/KYC database boundary, and the assertion gateway. Items 13.3 (rural
small-cell suppression) and 13.4 (sensitive/BSA unification) remain the active design work
on top of the running base.

1. Keep KYC sealed and encrypted; it verifies, never publishes.
2. Create a private Layer 2 UUID by default (separate from KYC ID).
3. Make public Layer 3 opt-in only.
4. Build H_people from person-in-context appearance records — roles, sources, places,
   dates, disclosure status — not dossiers.
5. Use public-accountability rules for officials and public actors (role-bound, sourced).
6. Use historical rules for deceased/archival people (source-bound, time-valid).
7. Protect sensitive and unknown people by default.
8. Require provenance + Merkle proof for every person claim; no unsourced personhood.
9. Use the Constitutional Docker to decide disclosure (name / redact / generalize /
   escalate).
10. Use the BBB to prevent private→public leakage.

## 15. One-sentence statement

> Hilbert People Space represents people as source-bound, time-bound, place-bound,
> role-bound, and consent-governed participants in public or historical knowledge, while
> KYC remains sealed, Layer 2 supports private metrics through separate UUIDs, and Layer 3
> makes public identity available only by explicit user choice.

That is the path to include people accurately without building surveillance.

---
*Design document, now describing a built system. H_people runs as Postgres schema `hp` in
database `hilbert_people` on `msjarvisgis-db`, served by `jarvis-hilbert-state`, with a
populated appearance ledger and a verified disclosure-assertion gateway. The
MountainShares-Commons evidence pipeline extends to probe the `hp` schema, and the
architecture moves from three measured bodies to four — under the same
regenerate-from-evidence discipline that governs every other body: the public repo claims
H_people because the collector counts its records, not because this document asserts it.*
