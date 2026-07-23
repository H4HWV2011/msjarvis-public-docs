# 43. Role, Purpose, and Projection Gates

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 43.1 What This Chapter Is Allowed to Claim

Within this sealed gate, Chapter 43 is limited to **role, purpose, and projection gates** on a specific, verified set of paths.

It may claim that:

- the **GBIM router** enforces purpose and coherence gates and binds requests to the active manifest;  
- the **GIS RAG** service enforces projection headers, purpose matching, permitted‑use constraints, and fail‑closed request‑purpose checks;  
- the **policy layer and write pipeline** expose a `DisclosureVerdict` with SUPPRESS/PERMIT behavior and a gate/pipeline contract;  
- the **query guard** causes person‑only queries to fail closed pending constitutional review;  
- these pieces together implement **role/purpose/projection gating** on GBIM, GIS RAG, policy, query‑guard, and disclosure paths.

It may **not** claim universal, perfect access control across the entire system. Anything beyond the verified paths remains outside this chapter’s warrant.

---

## 43.2 Why Role and Purpose Matter for Rural Operators

For rural developers and operators, these gates answer a concrete question:

> “When Ms. Allis goes to look something up about a place or a person, how does she know whether she is allowed to see and share it?”

Chapter 43 describes how:

- **role** (who is asking),  
- **purpose** (why they are asking), and  
- **projection** (what slice of the data they are allowed to see)

work together on the **governed belief and GIS paths** that have been explicitly checked. The aim is to make sure that governed maps, statistics, and appearance records are not just technically available, but **used only in ways that match their permitted purpose**.

---

## 43.3 The Verified Paths in Scope

This chapter only speaks about the paths that have closed evidence:

- the **GBIM router**, which fronts governed belief collections;  
- the **GIS RAG** service, which answers geography‑shaped questions from governed GIS data;  
- the **policy and write pipeline**, which decide whether a proposed appearance record may be stored or must be suppressed;  
- the **query guard**, which intercepts certain sensitive queries.

All of these are tied into a **role/purpose/projection** story:

- role and purpose are checked at the router and GIS RAG layer;  
- projection is enforced by collection metadata and query filters;  
- write‑side disclosure decisions are made by explicit verdicts;  
- person‑shaped queries are blocked or escalated rather than answered freely.

Nothing outside these named pieces is covered by Chapter 43’s claims.

---

## 43.4 GBIM Router: Purpose and Coherence Gates

The **GBIM router** is the entry point for governed‑belief queries.

Within this gate, Chapter 43 may claim that the router:

- reads the **declared purpose** and **role** of the incoming request;  
- routes only to collections whose **permitted use** matches that purpose;  
- binds each request to the current **active manifest** so that only promoted, active versions are ever served;  
- enforces a **coherence gate**, ensuring that requested combinations of collection, geography, and purpose make sense before the request is allowed through.

For rural developers, this means the router behaves more like a **governed switchboard** than a raw index. A request that asks for data outside the active manifest, or for a purpose that does not match a collection’s permitted use, is **stopped at the router** instead of falling through and hoping for the best.

---

## 43.5 GIS RAG: Projection and Purpose Enforcement

The **GIS RAG** service is the geography‑focused retrieval engine for governed GIS data.

Within this gate, the chapter may claim that GIS RAG:

- requires **projection headers** that describe the caller’s role and intended purpose;  
- checks that the requested collections’ **permitted uses** are compatible with that purpose;  
- restricts retrieval to **allowed collections** based on role and purpose, dropping disallowed collections before any vector search is run;  
- performs **fail‑closed request‑purpose checks**: if the purpose header is missing, malformed, or incompatible, the request fails rather than defaulting to a permissive mode.

Step by step, a rural operator can picture the path like this:

1. The caller sends a GIS question with county or blockgroup IDs plus a **declared purpose**.  
2. GIS RAG looks up which collections are allowed for that purpose and role.  
3. GIS RAG runs retrieval only inside those **permitted collections**.  
4. If there is no compatible combination, GIS RAG returns an error instead of partial, out‑of‑policy data.

This is what “projection” means here: the system **projects** the full GIS knowledge down to the slice that matches role and purpose.

---

## 43.6 Manifest‑Bound Access

The **publication manifest** used in governed belief is also part of Chapter 43’s story.

Within this gate, it is accurate to say that:

- only collections with **`build_status` marked active** in the manifest are used to answer governed GIS and GBIM queries;  
- requests are **bound to the active manifest row** for the named logical collection, ensuring that retired or superseded versions are not served by accident;  
- manifest entries include **permitted‑use fields**, and these fields are consulted by the GBIM router and GIS RAG to decide whether a request’s purpose is allowed.

In effect, the manifest is a **gating table** as much as a catalog:

- a collection can exist without being active;  
- a collection can be active only under certain permitted purposes;  
- Chapter 43’s verified paths respect both of those constraints.

---

## 43.7 Write Pipeline and Disclosure Verdicts

On the write side, the gate evidence shows a pipeline that computes a **`DisclosureVerdict`** for appearance records.

Within this chapter’s scope, it may claim that:

- every proposed appearance record passes through a gate that considers role, purpose, and policy;  
- the gate emits a `DisclosureVerdict` such as **SUPPRESS** or **PERMIT**;  
- **SUPPRESS** means the record is not written, and the decision is logged;  
- **PERMIT** means the record may proceed into the people‑space or governed belief store under the current rules.

From a rural developer’s standpoint:

1. Writing an appearance record is **never a raw insert**.  
2. The record is examined under the disclosure gate.  
3. If the verdict is SUPPRESS, the write is blocked and the block is itself an auditable event.  
4. Only PERMIT or similar allowed outcomes result in actual stored records.

This makes write‑side projection explicit: the pipeline decides not just *who can read*, but *what gets stored at all*.

---

## 43.8 Query Guard: Person‑Only Queries Fail Closed

The **query guard** is a special layer that watches for **person‑only queries**.

Within this gate, Chapter 43 may claim that:

- certain classes of queries that target a **single person without sufficient context** are intercepted;  
- for those person‑only queries, the default behavior is to **fail closed**, returning an error or a request for higher review rather than an answer;  
- escalation routes exist to pass such queries to **constitutional review** where policy allows.

In simple terms:

- “Tell me everything you know about this person” is treated as a dangerous request;  
- the query guard refuses to answer it directly;  
- only a higher, policy‑bound path can authorize any disclosure.

This aligns with the non‑surveillance aim of the surrounding chapters while staying strictly at the level of **access control**, not psychology.

---

## 43.9 Role, Purpose, and Projection Together

These pieces work together as a **three‑part gate**:

- **Role**: Who is asking? (for example, local operator, civic role, internal system job)  
- **Purpose**: Why are they asking? (for example, flood planning, broadband planning, internal test)  
- **Projection**: Given role and purpose, what subset of the knowledge is allowed to be seen or written?

On the verified paths:

- the **GBIM router** checks role and purpose against the manifest;  
- the **GIS RAG** enforces projection headers and permitted‑use constraints;  
- the **write pipeline** projects proposed records into PERMIT or SUPPRESS;  
- the **query guard** refuses dangerous person‑only queries.

For rural operators, this means that even if the data exists inside Ms. Allis, the answer to *“Can I see it?”* or *“Can I store this?”* depends on a concrete combination of **who**, **why**, and **how**—not just whether the data happens to be there.

---

## 43.10 Step‑by‑Step View for Rural Developers

A practical way to think about Chapter 43’s gates on the verified paths is as the following steps:

1. **Request comes in.**  
   - It includes a role (who) and a declared purpose (why).

2. **Router checks manifest and purpose.**  
   - GBIM router ensures there is an active manifest row and that the purpose matches the collection’s permitted use.

3. **Projection headers are enforced.**  
   - GIS RAG limits retrieval to collections allowed for that role and purpose.

4. **Query guard watches for person‑only requests.**  
   - Suspicious person‑only queries fail closed and are routed to constitutional review rather than answered.

5. **Write pipeline applies `DisclosureVerdict`.**  
   - For appearance records or similar writes, the gate returns PERMIT or SUPPRESS based on role, purpose, and policy.

6. **Only permitted slices are visible or stored.**  
   - The user receives only the portion of the information that matches their role and purpose, or no information at all if the check fails.

If any of these checks fail, the **expected behavior is to decline the request**, not to downgrade the rules.

---

## 43.11 What This Chapter Does Not Claim

To stay within the sealed constraints, Chapter 43 does **not** claim:

- complete, universal access‑control coverage across every service or legacy path;  
- perfect enforcement of role and purpose in parts of the system not covered by the GBIM, GIS RAG, policy, query‑guard, and disclosure paths;  
- clinical, psychological, or therapeutic evaluation of users based on their queries.

Its claims are narrow but concrete:

- **role/purpose/projection gating** over the verified GBIM, GIS RAG, policy/write‑pipeline, query‑guard, and disclosure paths;  
- **fail‑closed behavior** for person‑only queries and incompatible purposes;  
- manifest‑bound access to governed collections.

---

## 43.12 Closing Statement

Chapter 43 describes how Ms. Allis uses **role, purpose, and projection gates** to control access to governed belief and GIS knowledge on the paths that have been explicitly verified.

Through the GBIM router, GIS RAG, publication manifest, write‑pipeline disclosure verdicts, and query guard, the system ensures that even when it knows something, it only shares or stores what matches the requester’s **role** and **declared purpose**. Everything else either stays inside or is suppressed, giving rural developers a clear, step‑by‑step picture of how access is governed on the parts of the system this gate actually covers—without pretending that every path everywhere has already reached the same standard.
