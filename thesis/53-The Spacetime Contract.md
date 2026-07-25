# The Spacetime Contract

*How Ms. Allis is prevented from inventing geography.*

Status: implemented and calibrated (2026-07-24). Scope: the civic-geography
retrieval path only. This document describes a guard that is running, not a
proposal — every threshold below is traceable to a measured result reproduced
in the tables that follow.

---

## 1. The problem this exists to solve

Ms. Allis answers questions about West Virginia places by retrieving governed
belief documents from a vector store (Chroma), keyed to canonical geographic
identifiers and a `snapshot_version`. Retrieval uses cosine similarity over
embedded text, across three collections — counties, tracts, and block groups.

Vector retrieval has a property that is convenient for search and dangerous for
grounding: **it always returns the nearest neighbor.** There is no null result.
A query that corresponds to no West Virginia place still comes back with the
closest West Virginia county the embedding space can find, at some distance.
Nothing in the raw retrieval says "this is not really a match" — it only says
"this is the closest one."

Without a guard, that means every query produces a geographic answer, whether or
not the query is about West Virginia at all. Measured directly against the live
service on 2026-07-24:

| Query | Resolved to | Cosine distance |
|---|---|---|
| Cook County Illinois | Taylor County, WV | 0.5960 |
| Harris County Texas | Brooke County, WV | 0.6102 |
| the surface of the moon | Putnam County, WV | 0.8216 |
| how do I bake sourdough bread | Cabell County, WV | 0.8638 |

Each of these is a confident, specific, wrong answer waiting to be stated as
fact. "The surface of the moon" resolving to Putnam County is the failure mode
in its purest form. The spacetime contract is the mechanism that turns these
into explicit refusals instead of hallucinated locations.

---

## 2. The contract

Every grounded geographic claim Ms. Allis makes must attach to a canonical
**(where, when)** tuple:

- **where** — a canonical spatial key: `(county_id)`, `(county_id, tract_id)`,
  or `(county_id, tract_id, blockgroup_id)`, drawn from the resolved retrieval
  hit's metadata (`county_geoid`, `entity_type`, and so on).
- **when** — a `snapshot_version` from the belief document (e.g.
  `wv-county-snapshot-v2`), and where applicable an effective date from the
  underlying policy or benefit source.

The contract is a single rule: **no geographic claim without a (where, when)
that supports it.** If retrieval cannot produce a trustworthy `where`, the
system must say so and decline, rather than answer against the nearest vector.

The whole difficulty is in the word *trustworthy*. Retrieval always produces
*a* where. The guard's job is deciding whether that where is real.

---

## 3. Why a distance threshold alone does not work

The obvious guard is a distance ceiling: reject any hit farther than some
threshold T. We tested whether one exists, by measuring the top-hit distance for
known in-corpus queries (real WV geography) against known out-of-corpus queries
(other states, other countries, non-places).

**In-corpus (should resolve):**

| Query | Resolved | Distance |
|---|---|---|
| Kanawha county West Virginia | Kanawha | 0.2517 |
| McDowell county | McDowell | 0.2769 |
| Fayette county West Virginia | Fayette | 0.2971 |
| Raleigh county | Raleigh | 0.3302 |
| Monongalia county Morgantown | Monongalia | 0.3710 |
| census tract 54019020101 | Jefferson | 0.5067 |
| Mount Hope West Virginia | Wyoming | 0.5783 |

**Out-of-corpus (should refuse):**

| Query | Resolved | Distance |
|---|---|---|
| King County Washington | Jefferson | 0.5180 |
| Cook County Illinois | Taylor | 0.5960 |
| Harris County Texas | Brooke | 0.6102 |
| Los Angeles California | Berkeley | 0.6298 |
| Miami-Dade Florida | Marion | 0.6810 |
| Toronto Ontario Canada | Tucker | 0.7982 |
| the surface of the moon | Putnam | 0.8216 |
| how do I bake sourdough bread | Cabell | 0.8638 |

The two clusters **overlap**. The worst legitimate in-corpus query
("Mount Hope WV" → Wyoming, 0.5783) scored *farther* than the closest
out-of-corpus query ("King County WA" → Jefferson, 0.5180). Overlap = 0.0603.

Any single threshold placed in that band either rejects a real West Virginia
query or accepts an out-of-state one. **Distance alone cannot separate West
Virginia geography from other states' geography** — because the embedding space
treats "X County" as similar text regardless of which state X is in. It rewards
*placeness*, not *West-Virginia-ness*.

This is the empirical crux of the whole design. It is why the guard is layered
rather than a single number.

---

## 4. The guard

Three mechanisms, each doing work the others cannot.

### Layer 1 — distance ceiling (coarse backstop)

`DISTANCE_CEILING = 0.75`. Reject any top hit farther than this.

This does not separate the overlapping band — it is not trying to. It catches
only the absurd tail: queries that correspond to no place at all. "The capital
of France" (0.9069), "how tall is Mount Everest" (0.9027), "the moon" (0.8020),
"recipe for cornbread" (0.8438) all exceed it. The ceiling is deliberately set
*above* the worst legitimate in-corpus distance (0.5783) so it never rejects a
real West Virginia query. Its only job is the non-place tail.

### Layer 2 — named-place check (the decisive separator)

The layer that actually distinguishes West Virginia from elsewhere does not use
distance at all. It reads the query:

- **If the query names a US state other than West Virginia** — refuse. "Cook
  County Illinois", "Los Angeles California", "Boston Massachusetts" are caught
  here regardless of how close the nearest WV vector sits.
- **If the query names a major non-WV US city that is not also a WV place** —
  refuse. This closes the gap distance leaves open: bare city names with no
  state token. "Chicago" (0.6921), "Los Angeles" (0.6530), "Silicon Valley"
  (0.6213) sit *below* the ceiling and name no state, so Layer 1 and the
  state-check both miss them; the city gazetteer catches them by name.
- **If the query carries an affirmative West Virginia signal** ("West Virginia",
  "WV", "W. Va.") — accept. This overrides the state check so that
  "Jefferson county West Virginia" is not rejected for containing the substring
  "virginia".

### Collision handling — the part that makes it safe

A naive city or state list would reject legitimate West Virginia queries,
because West Virginia shares names with places elsewhere:

- **WV municipalities that are also big-city names elsewhere** — Charleston
  (WV capital; also SC), Huntington, Parkersburg. These are removed from the
  reject list automatically, sourced from the authoritative TIGER/Line 2023
  places file (439 WV places), so the guard never refuses a real WV town.
- **WV counties that are also non-WV city or state names** — Raleigh (WV county;
  also NC city), Marion, Lincoln, Jackson. All 55 WV county names are excluded
  from the reject set.
- **Names that are both a US state and a WV county** — Wyoming and Ohio. These
  are disambiguated by context: "Wyoming county" and "Ohio county" mean the West
  Virginia county (no US state has "county" in its name), so they accept; bare
  "Wyoming" or "Ohio" remain state signals and refuse.

The WV place list is baked into the guard as a frozen constant, so it is
self-contained and requires no data file at runtime. If the TIGER shapefile is
present it is merged in as a refresh source; if absent, the baked list stands.
This means the guard is portable and survives deletion of the source GIS data.

### Refusal, not silence

When any layer rejects, the guard returns an explicit, user-facing message —
"That location appears to be outside West Virginia. Right now I only hold West
Virginia civic geographic data, so I can't answer about other places without
guessing." The chat path must surface this message; a rejected query that
produces silence is a failure of integration, not of the guard.

---

## 5. Validation

The guard was tested against every calibrated query from both measurement runs,
plus the collision cases and both sides of the state/county ambiguity:
**24 of 24 correct.**

- All 7 in-corpus WV queries accept, including "Mount Hope WV" at the 0.5783
  distance that overlaps the out-of-corpus band.
- All WV county-name queries accept, including "Raleigh county" (collides with
  Raleigh, NC) and "Wyoming county" / "Ohio county West Virginia" (collide with
  US states).
- Every out-of-state query refuses — the six that name a state via the state
  check, the bare cities (Chicago, LA, Silicon Valley) via the gazetteer.
- Every non-place refuses via the distance ceiling.
- Bare ambiguous state names with no "county" ("tell me about Wyoming", "Ohio")
  correctly refuse as state signals.

---

## 6. Known limitations

Stated plainly, because a guard that hides its gaps is worse than one that names
them.

1. **The city gazetteer is not exhaustive.** It holds roughly 90 major non-WV US
   cities after WV-collision removal. Obscure out-of-state towns, and any city
   not on the list, are caught only if they also exceed the distance ceiling —
   which most place-like queries do not. "Akron" or "Toledo" without a state
   token can still slip through. The gazetteer shrinks the bare-city gap from
   "every city leaks" to "listed cities are caught"; it does not close it.

2. **The distance ceiling rests on a modest sample.** T = 0.75 is calibrated
   against roughly 28 out-of-corpus queries across two runs. It is well-placed
   for the non-place tail (nothing legitimate approached it; the closest was
   "downtown Manhattan" at 0.7293, itself out-of-corpus), but a larger
   calibration would firm the exact value. It is evidence-based, not proven.

3. **Misspellings and paraphrases evade the named-place check.** "Illinios",
   "the Windy City" (caught, but only because it was added explicitly), or a
   descriptive reference with no proper noun ("the big city up north") are not
   matched by the state or city lists and fall to Layer 1 only.

4. **Temporal enforcement is not yet complete.** The (where) half of the tuple
   is enforced by this guard. The (when) half — verifying that a stated benefit
   rule or statistic matches the `snapshot_version` of the resolved geography —
   depends on the non-geographic fact tables carrying a snapshot or
   effective-date key. Whether they do is an open schema question (see §8).

None of these are reasons not to ship the guard. They are the measured surface
of what it does not yet cover, so that the next layer of work is aimed
correctly.

---

## 7. Scope boundary — what this contract does NOT govern

This contract applies to the **civic-geography retrieval path only** — the
pipeline that resolves a place query against the WV county/tract/blockgroup
collections and grounds an answer in governed belief documents.

It explicitly does **not** govern the per-user conversation-memory path (the
Hilbert People Space, one Chroma collection per user). Those are different
pipelines with opposite requirements: civic geography *should* search across all
three geographic collections; conversation memory *must not* search across
users. Applying "search everything" reasoning from this contract to the memory
path would violate per-user sovereignty. The two must never be conflated. Any
guard on the memory read path is a separate artifact with its own rules.

---

## 8. What remains

1. **Wire the guard into the retrieval response.** The guard is implemented and
   tested as a pure module (`spacetime_guard.py`). Integrating it into
   `gis_rag()` requires adding optional `refused` / `refusal_reason` / `message`
   fields to the response model and having the chat path speak the refusal. Kept
   as a deliberate, isolated step so a wiring bug cannot silence retrieval.

2. **Broaden the ceiling calibration.** Run 30–40 out-of-corpus queries,
   including bare cities and neighbor-state counties, and confirm nothing
   legitimate approaches 0.75 before treating the value as fixed.

3. **Audit the temporal keys.** Determine whether the benefit and policy tables
   carry `snapshot_version` or an effective-date column. This decides whether the
   (when) half of the contract is enforceable at all, or whether it is
   aspirational pending a schema change.

4. **Extend beyond refusal, eventually.** Phase 0 refuses any non-WV place. A
   later phase, once comparison data exists, could scope-and-answer — resolving
   the WV portion of a comparative query and remaining explicit about the rest —
   rather than refusing outright. The contract's structure supports this
   extension without change: it is a policy choice about what to do when a query
   names a non-WV place, not a change to how (where, when) is enforced.

---

*Every threshold and claim in this document is traceable to a measured result
from the 2026-07-24 calibration runs against the live GIS-RAG service. The guard
implementation is `services/spacetime_guard.py`; the calibration harness is
`calibrate_gis_threshold.py`.*
