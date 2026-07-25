# Chapter 53: The Spacetime Contract

## How a rural civic AI is prevented from inventing geography

### What this chapter is for

If you are building an AI system that answers questions about real places —
counties, towns, census tracts, service areas, or neighborhoods — you will run
into a problem that is easy to miss until it fails in front of the people you
serve. This chapter explains that problem, describes a tested solution, and
shows how to reproduce the same guard in a small rural civic setting.

It is written step-by-step for rural developers, especially those working in
small nonprofits, local government, health access networks, mutual aid systems,
or community technology projects. The system described here was built under
tight resource constraints, calibrated on a live laptop deployment, and tested
against real place queries. No research lab is required. What is required is a
discipline of measurement, a refusal to guess, and a willingness to define the
boundary of the system honestly.

The scope of this chapter is deliberately narrow. It covers one question only:
how the system decides whether it knows *where* a user’s question is about, and
what it does when it does not know. It does not cover answer phrasing, document
ingestion, model selection, user memory, or private conversation history. Those
belong to other chapters. This narrow scope is not a limitation of the method;
it is part of the method. A guard that tries to solve every problem at once is
too broad to test and too vague to trust.

---

### 1. Why this is called a spacetime contract

The title of this chapter is intentionally metaphorical, but the metaphor is
disciplined rather than decorative. In physics, spacetime provides the
coordinate structure within which events can be located. A statement about an
event is meaningful only if it can be placed somewhere and somewhen. In the
same engineered sense, this civic AI is not allowed to make a grounded
geographic claim unless it can place that claim within an explicit coordinate
system of civic data.

That is why the chapter uses the phrase **spacetime contract**. The contract is
not a claim about physics, relativity, or \(E = mc^2\). It is a rule for system
behavior. In this system, every grounded civic claim must be attachable to a
specific **where** and a specific **when**. If no trustworthy coordinate can be
produced, the system must refuse rather than improvise.

The comparison to physics is useful only at that level. Just as physical events
are not meaningful without coordinates, civic claims in this system are not
authorized without provenance. The analogy stops there. This chapter remains
within its academic scope: geographic grounding in a rural civic AI.

---

### 2. The system context: what is being guarded

Before describing the guard, it is important to name the exact path it governs.

The system holds West Virginia civic geography in a retrieval layer. Place
records such as counties, tracts, and block groups are embedded into vectors and
stored in a vector database. When a user asks a question involving a place, the
system embeds the query and retrieves the nearest geographic records from that
index.

That retrieval step is useful, but it is not self-validating. It tells the
system which stored record is *closest* to the query, not whether the query is
actually about a place the system should answer for. The guard exists to decide
whether retrieval has found a place the system is entitled to treat as real,
in-scope, and trustworthy.

In this chapter, the guarded path is the **public civic geography path** only.
That means the path used to resolve counties, towns, census tracts, and related
regional geography. It does **not** apply to private user memory, conversation
history, or person-specific data. Those paths require different rules and must
not be conflated with broad civic retrieval.

---

### 3. The problem: retrieval always answers, even when it should refuse

A vector database always returns the nearest match from what it has. That is its
job. It does not know when the correct answer should be “this question is out of
scope” or “this is not a place at all.”

This creates a predictable failure mode. If the system is asked about a place it
does not cover, or about something that is not a place, the database still
returns the nearest stored West Virginia record. The result contains a distance
value, but by itself that value does not say, “this is invalid.” It only says,
“this is the least wrong thing I found.”

In a rural civic system, this matters because the answer may look specific even
when it is wrong. A confident wrong county is more dangerous than an explicit
refusal. It gives the appearance of geographic authority without the substance
of geographic truth.

This is the problem the chapter addresses. The goal is not to make retrieval
more eloquent. The goal is to stop the system from turning nearest-neighbor
behavior into false geographic certainty.

---

### 4. The measured failure: nearest does not mean correct

This failure is easiest to understand through direct examples. In the live
system, queries that were clearly outside the intended West Virginia civic scope
still resolved to specific West Virginia counties because the vector database
returned the nearest available match.

```text
query: "Cook County Illinois"        -> resolved to Taylor County, WV
query: "the surface of the moon"     -> resolved to Putnam County, WV
query: "how do I bake sourdough"     -> resolved to Cabell County, WV
```

These are not edge cases in the abstract. They are the ordinary consequence of
how vector retrieval works. Cook County is real, but it is outside the system’s
regional scope. The moon is not in West Virginia. A sourdough recipe is not a
place. Yet without a guard, all three still produce an apparently geographic
answer.

For rural developers, this is the first practical lesson: a vector database does
not know your program boundary. It knows only relative similarity inside the
corpus it was given. If you do not add a separate scope guard, retrieval alone
will confidently map the world into your region.

---

### 5. The contract: no grounded claim without a where and a when

The system therefore needs a rule stronger than “take the nearest hit.” The rule
used here is called the **spacetime contract**.

It can be stated in one sentence:

**The system may not state a geographic fact unless it can attach that fact to a
trustworthy `(where, when)` tuple that it actually retrieved.**

The two parts of that tuple are:

- **Where**: a canonical geographic identifier drawn from the matched record,
  such as a county ID, a tract ID, or a county-plus-tract-plus-block-group key.
- **When**: a version or snapshot identifier showing which dated dataset the
  claim comes from.

This chapter enforces the **where** half of the contract. The **when** half is
described later as future work. That distinction matters. A good contract names
both the part that is already enforced and the part that is not yet enforceable.

The central difficulty is that retrieval always produces *some* candidate where.
The guard’s job is to determine whether that where is trustworthy enough to
authorize a claim.

---

### 6. Why a simple threshold does not solve the problem

The obvious solution is a distance threshold: accept close matches, reject far
ones. This is attractive because it is simple, measurable, and easy to
implement. It is also incomplete.

To test whether a clean threshold existed, the system was evaluated on two
groups of queries:

- queries about real West Virginia places that should be accepted
- queries about places elsewhere, or non-places, that should be refused

Representative in-scope results looked like this:

```text
Kanawha county West Virginia    distance 0.2517
McDowell county                 distance 0.2769
Fayette county West Virginia    distance 0.2971
Raleigh county                  distance 0.3302
Monongalia county Morgantown    distance 0.3710
census tract 54019020101        distance 0.5067
Mount Hope West Virginia        distance 0.5783
```

Representative out-of-scope results looked like this:

```text
King County Washington          distance 0.5180
Cook County Illinois            distance 0.5960
Harris County Texas             distance 0.6102
Los Angeles California          distance 0.6298
Toronto Ontario Canada          distance 0.7982
the surface of the moon         distance 0.8216
how do I bake sourdough bread   distance 0.8638
```

The overlap is the critical finding. A genuine West Virginia place such as Mount
Hope can score *farther* than an out-of-state query such as King County
Washington. That means no single threshold can perfectly separate “belongs in
West Virginia” from “does not belong in West Virginia.”

For rural developers, this is the second practical lesson: embedding distance
captures how much a phrase **looks like a place**, not whether it belongs to
your service region. Texts shaped like county names remain close to other county
names even if they refer to the wrong state. Distance measures placeness more
reliably than belonging.

That is why the threshold can only be one layer of the guard, not the whole
guard.

---

### 7. The design principle: separate kinds of error

Once the threshold is shown to be insufficient on its own, the design principle
becomes clearer. Different error types need different checks.

There are at least three distinct failure modes:

1. The query is not about a place at all.
2. The query is about a real place, but outside the region.
3. The query is about a place whose name collides with a place elsewhere.

A single distance threshold cannot reliably solve all three. The guard therefore
uses multiple signals, with each signal doing one job and no more.

This is a useful design habit for small teams. Instead of searching for one
perfect score, ask which kinds of mistake the system makes, then assign a
specific check to each one. The result is easier to test and easier to explain.

---

### 8. The guard: three signals working together

The production guard described in this chapter uses three layers.

#### 8.1 A loose distance ceiling for nonsense

The first layer is a high distance ceiling. In this system, the ceiling is 0.75.

Anything beyond that ceiling is treated as too far away to authorize a
geographic claim. This layer does **not** try to distinguish West Virginia from
other states. It only catches the obviously absurd tail: questions that are not
really place questions at all.

```text
what is the capital of France   distance 0.9069   rejected
how tall is Mount Everest       distance 0.9027   rejected
the surface of the moon         distance 0.8020   rejected
recipe for cornbread            distance 0.8438   rejected
```

This ceiling is intentionally loose. It sits above the farthest measured valid
West Virginia query, so it does not reject legitimate in-region places. Its
purpose is modest and important: remove pure nonsense before it can be
canonicalized into a fake county.

#### 8.2 A lexical scope check on the question itself

The second layer reads the question text directly. This is the layer that
actually separates in-region from out-of-region place questions.

The rule is simple:

- If the question names another US state, refuse it.
- If the question names a major out-of-state city, refuse it.
- If the question explicitly says “West Virginia” or “WV,” preserve it as
  in-scope unless a stronger contradiction appears.

This check does something distance cannot do. It honors the user’s explicit
language about scope. If someone asks about Illinois, the system should not
silently translate that into West Virginia just because the embeddings are
close.

#### 8.3 An authoritative in-region place list

The third layer protects small towns and name collisions by carrying an
authoritative list of the region’s own places.

In the West Virginia deployment, that list includes every county and every
incorporated town used by the guard. The list was baked directly into the guard
code so that it survives deletion of the source shapefile or other staging
artifacts.

That matters operationally. A rural system often runs on fragile hardware,
temporary directories, hand-built pipelines, and imperfect storage practices. If
the guard depends on a live external file to know that Mount Hope or Thurmond is
a real West Virginia place, it is not robust enough for production. Baking the
place universe into the guard turns a data dependency into a tested invariant.

---

### 9. Handling collisions: where rural systems get embarrassed

Name collisions are where many otherwise sensible guards fail.

A system that merely blocks out-of-state names will still make mistakes if it
does not account for place names shared across the country. West Virginia has
many such collisions.

Examples include:

- **Charleston** — a West Virginia city, but also a city in South Carolina
- **Raleigh** — a West Virginia county, but also a major city elsewhere
- **Wyoming** and **Ohio** — names of both states and West Virginia counties

The solution is not to guess from the name alone. The solution is to use
context.

- “Raleigh county” should be accepted because the county form matches the West
  Virginia county.
- bare “Wyoming” should not automatically be accepted, because it may refer to
  the state.
- any name appearing on the authoritative West Virginia place list must be
  protected from naive rejection rules.

For rural developers, this is the third practical lesson: local credibility is
often lost on small, obvious errors. A guard that rejects one real county or
misplaces one local town will be remembered for that mistake long after the
larger architecture is forgotten.

---

### 10. The operational rule: refuse out loud

A guard does not finish its job when it rejects a query internally. It finishes
its job when the user receives a clear refusal message.

In this system, a rejected query yields a plain explanation: the requested
location appears to be outside the West Virginia civic dataset, or the query is
not specific enough to ground safely, so the system declines rather than guess.

This matters for user trust. Silent failure feels arbitrary. Wrong confidence
feels deceptive. Explicit refusal teaches the user the system’s boundary and
shows that the boundary is intentional rather than broken.

For civic use, this is not a cosmetic feature. It is part of accountability.

---

### 11. Step-by-step implementation path for a rural developer

A rural developer reproducing this method in another region can follow the same
order.

#### Step 1: Define the geographic scope plainly

Decide exactly what region the system serves. A state, a county network, a set
of tribal lands, a metro area, or a service catchment are all valid choices.
What matters is that the scope is explicit.

#### Step 2: Build a canonical civic geography corpus

Store the region’s counties, tracts, block groups, towns, or other relevant
units in a structured corpus with canonical identifiers. This corpus becomes the
retrieval layer’s answer space.

#### Step 3: Measure retrieval before adding a guard

Run known in-scope and known out-of-scope queries through the system and record
the top-hit distances. Do not guess where the threshold belongs. Measure it.

#### Step 4: Find the overlap

Look for whether real in-scope places and out-of-scope places overlap in
distance. In most cases they will. That overlap is the proof that distance alone
is not enough.

#### Step 5: Set a loose nonsense ceiling

Choose a ceiling high enough to preserve all valid in-region queries but low
enough to reject clearly non-geographic queries. This is your nonsense filter,
not your geography filter.

#### Step 6: Add lexical scope checks

Reject queries that explicitly name other states, other countries, or out-of-
scope major cities. Respect the user’s language about place.

#### Step 7: Bake an authoritative local place list into the guard

Carry your region’s own towns, counties, and other names inside the guard logic
so real local places are protected and the guard survives missing source files.

#### Step 8: Test collisions deliberately

Create tests for shared names, ambiguous names, county-versus-city forms, and
small local places. Do not assume these will work automatically.

#### Step 9: Refuse explicitly

Return a visible refusal message when the system cannot ground the place
safely. Never let a rejection vanish silently.

#### Step 10: Keep the guard scoped

Apply this guard only to the civic geography retrieval path. Do not reuse it for
private user memory or other pipelines with different governance rules.

---

### 12. Proof of behavior in production

After the layers were combined, the live system behaved correctly on the tested
cases.

```text
Kanawha county West Virginia   -> answered normally
Cook County Illinois           -> refused: names another state
the surface of the moon        -> refused: beyond the distance ceiling
Mount Hope West Virginia       -> answered normally
```

The significance of this result is not just that some examples worked. It is
that the layered guard succeeded exactly where the simple threshold failed. The
overlapping case — Mount Hope — remained answerable, while clearly out-of-scope
queries were refused for explicit reasons.

That is the practical success criterion for the chapter: preserve real local
places, reject outside geography, reject non-places, and explain the refusal.

---

### 13. What this guard does not do

An honest academic chapter should name the boundary of its claims.

This guard does **not** solve every geographic grounding problem. At least three
gaps remain.

First, the out-of-state city list is finite. It catches the cities most likely
to appear, but not every small municipality elsewhere in the country.

Second, the distance ceiling was set from a modest evaluation set. It is
evidence-based, but not mathematically universal.

Third, vague references, paraphrases, and misspellings can evade lexical checks
and fall through to the ceiling logic.

These limitations do not invalidate the method. They define the next increment
of work. A useful guard is allowed to be incomplete, provided its incompleteness
is named and testable.

---

### 14. The boundary of this chapter

This chapter governs one path only: the path that answers questions about public
civic geography.

It does **not** govern the system’s private per-person memory. That path follows
the opposite rule. Civic geography is supposed to range across counties and
tracts inside the public regional corpus. Private memory must never range across
people. Confusing the two would turn a public geography rule into a privacy
violation.

That boundary is part of the academic scope of this chapter. The chapter is
about geographic grounding only, not about memory sovereignty, user identity, or
cross-user data isolation.

---

### 15. The half not yet enforced: time

The spacetime contract requires both a **where** and a **when**. In the current
system, the **where** half is implemented and tested. The **when** half is not
yet fully enforceable.

To enforce the *when*, the system would need policy facts, eligibility rules,
and similar changing facts to live in structured tables that carry a snapshot
version or effective date. Only then can a claim be checked against the dated
state of the data it came from.

If those facts are later reintroduced only as unstructured documents, the
temporal half of the contract will remain aspirational. A text paragraph without
a version key has no reliable *when*. If those facts are stored in structured,
dated tables, then the contract can be extended from “this claim belongs to this
place” to “this claim belongs to this place at this time.”

This chapter therefore ends with a design instruction for future work:
time-sensitive civic facts should be stored in dated, structured form from the
start, or the temporal half of the contract will never become enforceable.

---

### 16. What rural developers should take away

A rural civic AI does not become trustworthy by sounding confident. It becomes
trustworthy by refusing to cross the boundary of what it can ground.

The practical lessons of this chapter are these:

1. Retrieval will always return something. That is not the same as knowing.
2. Distance alone does not tell you whether a place belongs to your region.
3. A layered guard is more honest than a magical threshold.
4. Your region needs an authoritative place list, and the guard should survive
   losing the source file.
5. Name collisions must be handled deliberately.
6. Refusals should be visible and plain.
7. Geographic grounding and private memory are different pipelines and need
   different rules.
8. If the system will ever make time-sensitive civic claims, the data must be
   stored with explicit temporal keys.

The deepest point is simple: when the system does not know where a question is
about, it must say so. Everything else in this chapter is machinery built to
make that sentence true, measurable, and defensible.
