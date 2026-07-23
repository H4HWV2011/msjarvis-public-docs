# 51. The Community Hilbert Commons — As‑Built k‑Thresholded Aggregation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 51.1 What This Chapter Is Allowed to Claim

Within this gate, Chapter 51 may be rewritten as an **as‑built Community Hilbert Commons** chapter.

It may claim that:

- the **community commons gateway** is live on port 8055;  
- a `community_hilbert_commons` collection **exists in Chroma**;  
- **private people‑space collections remain separate** from commons;  
- commons aggregation requires **public opt‑in** on contributing records;  
- the aggregator **suppresses groups below `K_MIN`**;  
- **sensitive groupings require `K_SENSITIVE`** and are suppressed if they fall below it;  
- permitted commons outputs contain **centroid and provenance only**, and do **not** retain source user hashes;  
- BBB, guardian, and Chroma **health checks pass**;  
- focused Chapter 51 tests **pass**.

It must **not** claim:

- mathematical impossibility of re‑identification under all attacks;  
- raw publication of personal subspaces;  
- commons access to private \(H_p\) records;  
- a universal anonymization guarantee;  
- clinical or legal safety guarantees.

---

## 51.2 Plain‑Language Purpose for Rural Developers

For rural operators, this chapter answers:

> “If people in a community choose to share some of their data, how does Ms. Jarvis turn that into *community‑level patterns* without exposing private histories?”

This chapter explains, step by step:

- how the **Community Hilbert Commons service** works;  
- how it uses **k‑thresholds** to decide what can be shown;  
- how it keeps **private people‑space separate** from commons;  
- what information **does** and **does not** appear in a commons record.

It describes the **implementation that exists today**, not an idealized future system.

---

## 51.3 The Commons Gateway and Collection

The as‑built commons stack has two main pieces:

- a **gateway service** on port 8055;  
- a **vector collection** in Chroma named `community_hilbert_commons`.

The gateway:

- receives aggregation requests;  
- talks to Chroma to read or write commons vectors;  
- applies **k‑threshold and sensitivity rules** before permitting an output.

The `community_hilbert_commons` collection:

- holds **commons‑level vectors and metadata**;  
- does **not** store user‑level identifiers or per‑user subspace names;  
- is the **only collection** where commons vectors are stored.

This separates “community‑wide patterns” (in `community_hilbert_commons`) from “individual histories” (in per‑user or civic collections).

---

## 51.4 Sovereign Subspaces and Commons Separation

The gate confirms that:

- **private people‑space collections remain separate from commons**.

In practice, this means:

- per‑user people‑space and per‑user conversation collections **are not read** by the commons aggregator;  
- the gateway uses **only public‑opt‑in, commons‑eligible sources**;  
- there is **no code path** that lets the commons service read directly from private \(H_p\) partitions.

For rural communities, this means:

- using Ms. Jarvis personally does **not** automatically make a user’s private memory part of the commons;  
- commons aggregation is built **on top of** sovereign subspaces, not *instead of* them.

---

## 51.5 Public Opt‑In as a Hard Requirement

Commons aggregation **requires public opt‑in**.

On each candidate source record, the aggregator expects a flag like:

- `public_opt_in: true` for commons‑eligible contributions;  
- `public_opt_in: false` otherwise.

The gateway:

- **skips or suppresses** records without public opt‑in;  
- builds commons groups **only** from records where public opt‑in is explicitly true.

This means that:

- opt‑in is **stored as data**, not assumed;  
- there is no “silent inclusion” in the commons;  
- if a record’s opt‑in flag is removed or turned off, it is **no longer a commons candidate**.

---

## 51.6 k‑Thresholds: `K_MIN` and `K_SENSITIVE`

The commons aggregator enforces **k‑anonymity‑style thresholds**:

- `K_MIN` — the minimum group size for **any commons output**;  
- `K_SENSITIVE` — a higher minimum group size for **sensitive groupings**.

The gate confirms:

- “Commons aggregation suppresses groups below `K_MIN`”;  
- “Sensitive metadata requires `K_SENSITIVE`”.

In practice:

- if a candidate group (for example, “people matching filter X”) has **fewer than `K_MIN` members**, the gateway returns **no commons record** for that group;  
- if a group involves **sensitive attributes** (for example, marginalized status or certain health‑like signals) and is **below `K_SENSITIVE`**, it is suppressed even if it is above `K_MIN`.

This is how the system avoids answering “What is the vector for this group of 2 people?” — the answer is: “No commons vector; group too small.”

---

## 51.7 What a Commons Record Contains (Centroid + Provenance, No User Hashes)

The gate states:

- “Permitted commons output records centroid and provenance while not retaining source user hashes.”

This means a permitted commons record includes:

- a **centroid vector**: the average or representative embedding for the group;  
- **provenance metadata**: high‑level information about which **sources and filters** generated the group (for example, “derived from public_civic_statements with opt‑in true, filtered by region and time window”).

It explicitly does **not** include:

- raw user IDs;  
- per‑user subspace names;  
- per‑user hashes or stable per‑user tokens.

In plain language:

- the commons record tells you **“what this group looks like as a whole”**;  
- it does **not** tell you **“who the individuals in the group are”**.

---

## 51.8 Sensitive Metadata Handling

The gate notes:

- “Sensitive metadata requires `K_SENSITIVE`.”

This means that if aggregation involves attributes considered **sensitive** (for example, certain kinds of inferred hardship or vulnerable status), then:

- **only groups reaching `K_SENSITIVE` or higher** can produce a commons record;  
- below that size, the gateway returns **no record**.

So there are effectively **two k‑filters**:

- one general (`K_MIN`);  
- one for sensitive material (`K_SENSITIVE` ≥ `K_MIN`).

This gives the system a way to:

- still compute **some** community‑level patterns in sensitive areas;  
- but **only when enough people** are represented that individual inference becomes harder.

---

## 51.9 BBB, Guardian, and Health Checks

The gate confirms that:

- **BBB and guardian checks** for the commons pathway pass;  
- **Chroma health checks** pass;  
- focused Chapter 51 tests **pass**.

This shows:

- commons aggregation is not a “sidecar” bypassing governance;  
- the same safeguard stack (BBB, guardian) used elsewhere still applies when the system builds or serves commons vectors;  
- Chroma (the vector store) is healthy for commons operations.

For rural developers, this means that commons aggregation is **wired into the same guard system** as other authority‑bearing operations, not an ungoverned background job.

---

## 51.10 Step‑by‑Step View for Rural Developers

At this gate, the Community Hilbert Commons works like this:

1. **People and civic sources exist in sovereign subspaces.**  
   - Per‑user and civic collections hold their own records separately.

2. **Some records are marked `public_opt_in: true`.**  
   - Only these records are considered for commons.

3. **The commons gateway on port 8055 receives an aggregation request.**  
   - It may specify filters (location, time window, topic, etc.).

4. **The gateway selects only opt‑in records via the manifest/resolver.**  
   - It never reads private \(H_p\) collections.  
   - It uses only commons‑eligible civic or public sources.

5. **Records are grouped, and group sizes are counted.**  
   - If a group is smaller than `K_MIN`, it is suppressed.  
   - If sensitive fields are involved and the group is smaller than `K_SENSITIVE`, it is suppressed.

6. **For permitted groups, the gateway computes a centroid.**  
   - It writes/reads centroid vectors into/from `community_hilbert_commons`.  
   - It records high‑level provenance (where the group came from, not who).

7. **The gateway returns commons vectors and provenance.**  
   - It **never returns user IDs** or per‑user hashes.  
   - Under‑threshold groups yield **no result**, not a “weak” result.

That is the “anonymized aggregation over sovereign subspaces” in running code.

---

## 51.11 What This Chapter Does Not Claim

To stay within the gate, this chapter does **not** claim:

- that re‑identification is mathematically impossible under all future attack models;  
- that people’s private subspaces are never at risk under misconfiguration or misuse;  
- that commons access could never be misused by an external actor;  
- a universal anonymization guarantee;  
- clinical or legal safety guarantees.

It only claims:

- as‑built **k‑thresholded aggregation** over public‑opt‑in contributions;  
- **commons/private separation** in the code paths and collections used;  
- **centroid + provenance** structure for permitted commons records;  
- **suppression** of under‑threshold and sensitive‑under‑threshold groups;  
- passing **governance and health checks** for the commons gateway.

---

## 51.12 Closing Statement

Chapter 51, at this closure, presents the **Community Hilbert Commons as it actually runs today**.

The commons gateway on port 8055 aggregates only **public‑opt‑in** contributions; private people‑space remains separate; groups must meet `K_MIN` (and `K_SENSITIVE` for sensitive attributes); permitted outputs contain only centroids and high‑level provenance; and under‑threshold groups are suppressed. This gives rural communities a way to benefit from **community‑level patterns** without turning individual contributions into raw public data, within the carefully bounded scope this gate allows.
