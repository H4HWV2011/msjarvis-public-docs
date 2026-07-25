# Chapter: The Spacetime Contract

## How a rural civic AI is prevented from inventing geography

### What this chapter is for

If you are building an AI system that answers questions about real places —
counties, towns, census tracts — you will run into a problem that is easy to
miss until it embarrasses you in front of the people you serve. This chapter
explains that problem, shows a working solution running in production, and gives
you the reasoning so you can build the same guard for your own region.

It is written for a developer in a small organization with limited resources,
because that is who built the system it describes: a nonprofit in Mount Hope,
West Virginia. Everything here was calibrated against a live system on a single
laptop. You do not need a research lab to do this. You need to measure honestly
and refuse to guess.

The scope of this chapter is deliberately narrow. It covers one thing: how the
system decides whether it knows *where* a question is about, and what it does
when it does not. It does not cover how the answer is written, how the data was
gathered, or how the system remembers past conversations. Those are other
chapters. Keeping the scope narrow is itself part of the method — a guard that
tries to do everything is a guard you cannot test.

---

### 1. The problem: retrieval always answers, even when it shouldn't

The system stores knowledge about West Virginia geography as *embeddings* —
numeric fingerprints of text — inside a vector database. When someone asks a
question, the system turns their question into the same kind of fingerprint and
asks the database: *which stored places are closest to this?*

Here is the trap. A vector database always returns the closest match. It has no
concept of "nothing here fits." Ask it about a place it has never heard of, and
it will still hand back the nearest West Virginia county it happens to have,
along with a distance number saying how far off the match was. Nothing in that
result says *this is not really a match* — it only says *this is the closest one
I have.*

We measured this directly against the live system. These are real results:

```
query: "Cook County Illinois"        -> resolved to Taylor County, WV
query: "the surface of the moon"     -> resolved to Putnam County, WV
query: "how do I bake sourdough"     -> resolved to Cabell County, WV
```

Cook County is in Illinois. The moon is not in West Virginia. "How do I bake
sourdough" is not a place at all. Yet each one came back as a confident,
specific West Virginia county. If the system had simply trusted retrieval, it
would have told a community member that the moon is in Putnam County — and said
it with the same certainty it uses for real answers.

That is the failure this chapter prevents. The goal is not to make the system
smarter about geography. The goal is to make it honest about the edges of what
it knows.

---

### 2. The contract: no claim without a where and a when

The rule is simple to state. Every grounded claim the system makes about a place
must be able to point back to two things:

- a **where** — a specific, canonical place identifier: a county, or a county
  and tract, or a county and tract and block group, drawn from the matched
  record.
- a **when** — a version stamp saying which snapshot of the data the claim came
  from, so the answer can always be traced to a dated source.

Together these form a *(where, when)* tuple. The contract is one sentence: **the
system may not state a geographic fact unless it can attach that fact to a
(where, when) it actually retrieved.** If it cannot produce a trustworthy where,
it must say so and decline, rather than answer against the nearest guess.

The entire difficulty lives in the word *trustworthy*. Retrieval always produces
*a* where. The job of the guard is to decide whether that where is real.

---

### 3. Why the obvious solution does not work

The obvious idea is a distance threshold. The database gives you a distance
number for each match — smaller means closer. So pick a cutoff: accept matches
closer than some number, reject the rest. Clean and simple.

We tested whether that cutoff exists. We ran a set of questions we knew were
about real West Virginia places, and a set we knew were not, and recorded the
distance of the closest match for each.

Questions about real West Virginia places (should be accepted):

```
Kanawha county West Virginia    distance 0.2517
McDowell county                 distance 0.2769
Fayette county West Virginia    distance 0.2971
Raleigh county                  distance 0.3302
Monongalia county Morgantown    distance 0.3710
census tract 54019020101        distance 0.5067
Mount Hope West Virginia        distance 0.5783
```

Questions about places elsewhere (should be refused):

```
King County Washington          distance 0.5180
Cook County Illinois            distance 0.5960
Harris County Texas             distance 0.6102
Los Angeles California          distance 0.6298
Toronto Ontario Canada          distance 0.7982
the surface of the moon         distance 0.8216
how do I bake sourdough bread   distance 0.8638
```

Look at the two lists carefully. The worst real West Virginia question —
"Mount Hope West Virginia" at 0.5783 — is *farther away* than a genuinely
out-of-state question, "King County Washington" at 0.5180. The two groups
overlap. There is no single cutoff you can draw that keeps every real place and
rejects every foreign one. Any line that catches King County also throws out
Mount Hope, a real West Virginia town.

The reason is worth understanding, because it will be true for your region too.
The embedding measures how similar the *text* is. "King County Washington" and
"Kanawha County West Virginia" are both "[name] County [state]" — structurally
almost identical. The fingerprint rewards *sounding like a place*, not *being in
West Virginia*. Distance alone cannot tell the difference between a county here
and a county two thousand miles away, because as text, they are nearly the same
shape.

This is the central finding of the chapter: **distance measures placeness, not
belonging.** A guard built only on distance will confidently misplace the world.

---

### 4. The guard: three signals, each doing one job

Because no single number works, the guard uses layers. Each layer catches a
different kind of mistake, and together they cover the field.

#### Layer one: a loose distance ceiling for nonsense

Set a distance ceiling — we use 0.75 — and reject anything beyond it. This does
not try to separate West Virginia from other states; we just proved that is
impossible with distance. It only catches the truly absurd: questions that
correspond to no place at all.

```
what is the capital of France   distance 0.9069   rejected
how tall is Mount Everest        distance 0.9027   rejected
the surface of the moon          distance 0.8020   rejected
recipe for cornbread             distance 0.8438   rejected
```

The ceiling sits *above* the worst real West Virginia question (0.5783), so it
never throws out a legitimate query. Its only job is the far tail of nonsense.

#### Layer two: check the words of the question

This is the layer that actually separates West Virginia from elsewhere, and it
does not use distance at all. It reads the question itself:

- If the question names a US state other than West Virginia — "Illinois",
  "Texas", "California" — refuse it. It does not matter how close the nearest
  West Virginia match sits; the person asked about another state.
- If the question names a major city that is not in West Virginia — "Chicago",
  "Los Angeles", "Boston" — refuse it. This catches the cases distance misses:
  a bare city name with no state attached, sitting below the ceiling.
- If the question affirmatively says "West Virginia" or "WV", accept it. This
  protects real queries from being rejected by accident.

To make the city check work, the guard carries a list of the state's own
places — every incorporated town and every county — so it never mistakes a real
West Virginia place for a foreign one.

#### Handling the collisions

This is the part that takes care, because West Virginia shares names with the
rest of the country, and a careless list would reject its own towns.

- **Charleston** is the capital of West Virginia. It is also a city in South
  Carolina. It must never go on the reject list.
- **Raleigh** is a West Virginia county. It is also the capital of North
  Carolina. A naive city list would reject "Raleigh county" — a real place here.
- **Wyoming** and **Ohio** are both US states *and* West Virginia counties. The
  guard resolves this by context: "Wyoming county" means the West Virginia
  county and is accepted; bare "Wyoming" is read as the state and refused.

The guard handles all of these by starting from the state's authoritative list
of its own places and never rejecting a name that appears on it. The place list
holds 493 names — every West Virginia town and county — and it is built directly
into the guard so it keeps working even if the source map file is deleted from
the machine. The system was tested with that file removed, and it still
correctly accepted Mount Hope, Oak Hill, Thurmond, and every other small town.

#### Refuse out loud, never in silence

When any layer rejects a question, the guard does not simply return nothing. It
returns a plain message: *that location appears to be outside West Virginia; I
only hold West Virginia civic data, so I can't answer about other places without
guessing.* A refusal the person never sees is just as confusing as a wrong
answer. The system must say why it is declining.

---

### 5. Proof that it works

The guard was checked against every measured question above, plus the tricky
name collisions, and it answered all of them correctly. In production, on the
live system:

```
Kanawha county West Virginia   ->  answered normally
Cook County Illinois           ->  refused: names another state
the surface of the moon        ->  refused: beyond the distance ceiling
```

Every real West Virginia question is answered, including Mount Hope at the
overlapping distance that broke the simple threshold. Every out-of-state
question is refused by name. Every non-place is refused by the ceiling. The moon
no longer lives in Putnam County.

---

### 6. What this guard does not do

An honest guard names its own gaps. This one has three.

First, the city list is not the whole country. It holds the major cities most
likely to come up. A small out-of-state town that no one thought to add, with no
state named alongside it, can still slip through to the loose ceiling. The list
shrinks the problem from "every city leaks" to "listed cities are caught." It is
an improvement, not a proof.

Second, the ceiling number was set from a few dozen test questions. Nothing
legitimate came near it, so it is well placed — but a larger test set would make
it firmer. Treat 0.75 as evidence-based, not eternal.

Third, misspellings and vague references — "the big city up north" — carry no
state or city name for the word-check to catch, and fall through to the ceiling
only.

None of these are reasons to skip the guard. They are the honest edges of what
it covers, written down so the next piece of work aims correctly.

---

### 7. The boundary of this chapter

This guard governs one path only: the path that answers questions about public
civic geography. It does not govern the system's private, per-person memory,
which follows the opposite rule — that path must *never* reach across people,
while the geography path is meant to reach across all of the region's counties
and tracts. The two must not be confused. Applying this chapter's "search
broadly" logic to private memory would break the promise of privacy that memory
path is built to keep. A guard for that path is a separate piece of work with
its own rules, and it is not this chapter.

---

### 8. The half that is not yet built: time

The contract asks for a *where* and a *when*. The *where* is enforced, live, and
proven. The *when* is not — and the reason is honest and specific.

Enforcing the *when* would mean checking a stated fact — say, an eligibility rule
for a benefit program — against the dated version of the data it came from. That
requires the benefit and policy facts to live in structured tables that carry a
version stamp or an effective date. In this system, those facts are not yet in
the corpus at all; re-adding them is future work.

That timing is an opportunity, not a defect. Because the data has not been
re-added yet, the decision about how to store it is still open — and this is the
moment to make it correctly. When benefit and policy facts are brought back,
they must land in structured tables that carry a version or effective-date
stamp, not as loose document text. Document text has no *when* to check against;
a rule pulled from an undated manual can never be verified as current. If the
facts return as keyed tables, the *when* half of the contract becomes
enforceable. If they return as plain text, it never will. The contract, by
existing before the data returns, tells you which choice to make.

---

### 9. What to take away for your own region

If you are building this for somewhere else, the method transfers directly:

1. Do not trust retrieval distance to tell you whether a place is in scope. Test
   it against known in-scope and out-of-scope questions. You will almost
   certainly find the same overlap we did.
2. Get your region's authoritative list of its own place names. Census place and
   county files exist for every US state and most jurisdictions. Build that list
   into your guard so it survives losing the source file.
3. Refuse by name, not by distance, for the cases that matter — questions that
   name somewhere else. Use distance only for the nonsense tail.
4. Handle the name collisions deliberately. Your region shares names with
   others; find them before they embarrass you.
5. Refuse out loud. A silent empty answer teaches people nothing.
6. If your facts carry dates — benefit rules, policies, anything that changes —
   store them in tables with a version stamp from the start, so the *when* half
   is enforceable rather than aspirational.

The whole discipline reduces to one habit: when the system does not know, it must
say so, and you must be able to prove it says so. Everything above is machinery
in service of that one honest sentence.
