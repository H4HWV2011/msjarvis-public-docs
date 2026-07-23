# 39. Operational Evaluation and Automated Learning

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 39.1 What This Chapter Is Allowed to Claim

In Ms. Allis, Chapter 39 is limited to **operational evaluation** of a very specific loop.

At the July 2026 sealed scope, it may claim that the system supports:

- **gap detection** in the local corpus;  
- **escalation to web research** when Ms. Jarvis cannot answer truthfully from local data;  
- **truth‑oriented review** of research results;  
- **storage of reviewed findings** into a Chroma learning sink such as `autonomous_learner`.

It must not claim universal truth, hallucination impossibility, clinical cognition, or unrestricted autonomous authority. Automated learning here is a **bounded, governed process**, not a guarantee that the system is always right.

---

## 39.2 Automated Learning as a Process, Not a Database

The sealed gate stresses that **automated learning is a process**, and the learning sinks are **destinations**.

In this chapter:

- **Automated learning** means:  
  1. reviewing what the local corpus knows;  
  2. detecting when that is not enough for an honest answer;  
  3. escalating to web research;  
  4. reviewing the new material for truth and coherence;  
  5. writing only the reviewed pieces into a learning sink.

- **`automated_learner` / `autonomous_learner`** are **Chroma learning sink collections** that hold the results of that loop.

The chapter must not describe those collections as “the automated‑learning loop.” They are **where** truth‑reviewed research is stored, not **how** the learning happens.

---

## 39.3 Gap Detection in the Local Corpus

Operational evaluation begins with **corpus‑gap detection**.

When Ms. Jarvis is asked a question, the system first searches her **local corpora**, which include collections such as:

- conversation histories;  
- community and Appalachian corpora;  
- commons and civic RAG collections;  
- other domain‑specific knowledge bases.

The evaluation logic asks:

- Is there enough relevant material to support a truthful, grounded answer?  
- Are the retrieved documents consistent and coherent?  
- Do internal truth filters agree that a draft answer is adequately supported?

If the answer is no, the system treats this as a **gap**. The correct operational behavior is:

- admit that the local corpus is insufficient;  
- avoid pretending to know;  
- consider escalation to web research rather than fabricating.

This gap‑first posture is the chapter’s anchored anti‑hallucination behavior.

---

## 39.4 Escalation to Web Research

When a gap is detected and policy allows it, the system escalates to **web research**.

This happens through a dedicated **web research service** running in its own container, which the gate evidence confirms is present in the deployment. That container:

- receives a structured research request derived from the gap;  
- queries external sources;  
- returns candidate documents, passages, or snippets relevant to the question.

At this stage, web content is treated as **candidate evidence**, not as trusted truth. Operational evaluation is concerned with verifying that:

- gap conditions actually trigger the research path;  
- research calls go through the dedicated service;  
- failures or timeouts are handled without granting accidental authority.

---

## 39.5 Truth‑Reviewed Storage into Learning Sinks

After web research, candidate findings enter a **truth‑oriented review** step.

In this step:

1. Candidate snippets are brought into the internal sandbox and judged for:  
   - basic factual plausibility;  
   - consistency with known, trusted material;  
   - presence of obvious contradictions or low‑quality sources.

2. Findings that fail these checks are **rejected** or quarantined.  
3. Surviving findings are structured with:  
   - provenance hashes;  
   - source identifiers or URLs;  
   - timestamps;  
   - topical tags or embeddings.

4. Only these reviewed entries are written into the **learning sink collections** such as `autonomous_learner`.

Operational evaluation can therefore claim that the learning sink is:

- a **durable Chroma destination** for externally researched information;  
- populated **after** corpus gaps, web research, and truth‑oriented review;  
- not a raw dump of everything the web service ever returns.

---

## 39.6 Learning Sinks and Collection Structure

The sealed probe shows that the deployment includes many Chroma collections, including at least:

- `autonomous_learner` (for learning sink storage);  
- other collections like `appalachian_cultural_intelligence`, `commons_rag`, civic role and GBIM collections, and multiple conversation histories.

Within this architecture:

- **Learning sinks** (`autonomous_learner` and related names) are **write targets** for reviewed research results.  
- They sit alongside other collections but are conceptually different:  
  - local corpora store baseline knowledge and conversation history;  
  - learning sinks store **post‑research, post‑review** material.

The chapter is allowed to say that these collections exist and serve as **durable destinations** for the automated learning loop, but only at the level demonstrated by the gate: presence, healthy Chroma family membership, and successful writes in tested scenarios.

---

## 39.7 Role of the Recurrent Epistemic Runner and EEG Context

Chapters 28 and 39 share the **recurrent epistemic runner** as a backbone.

From the closed evidence, operational evaluation of automated learning can rely on:

- a live recurrent runner process;  
- reboot/cron registration so the runner survives restart;  
- healthy **Hilbert time** and **Hilbert state** services;  
- a healthy **Phi probe** at its actual deployed host mapping;  
- present **EEG containers** (theta, delta, beta) that provide additional state context.

For Chapter 39, this means:

- gap‑review and web research escalation run **on top of** a live‑cycle that is already heart‑checked;  
- learning updates can be conditioned on time/state stability and coherence signals;  
- the system is not supposed to write into long‑term sinks during obvious runtime instability.

Operational evaluation can therefore talk about automated learning as a loop that **respects heartbeat and coherence**, not as a free‑running background scraper.

---

## 39.8 What Operational Evaluation Measures

Within this chapter, operational evaluation looks at questions such as:

- How often does the system correctly **detect gaps** instead of answering from inadequate local data?  
- When gaps are detected, how reliably does it **escalate to web research**?  
- How frequently do research calls **succeed**, timeout, or fail?  
- What fraction of research results pass truth‑review and are written to the **learning sink**?  
- How often does the system **fail closed** rather than writing unreviewed or contradictory material?

These quantities are empirical, not absolute. They should be reported as **observed behavior**, not as timeless guarantees. The chapter remains clear that this is about **bounded improvement over time**, not about perfection.

---

## 39.9 Anti‑Hallucination in This Scope

At this gate, Chapter 39’s anti‑hallucination claim is deliberately narrow.

It may claim that:

- the system **detects when it does not know** enough to answer truthfully from local corpus;  
- when allowed, it **goes out to research** instead of fabricating;  
- it performs **truth‑oriented review** on research results;  
- it **only writes reviewed findings** into learning sinks.

It may **not** claim that:

- the system always tells the truth;  
- hallucinations are impossible;  
- the system has clinical judgment or cognitive parity with humans;  
- the system can act with unrestricted autonomous authority.

In plain language, the promise is: *“When I don’t know, I say so, go look, and try to store only what holds up under review,”* not *“I can never be wrong.”*

---

## 39.10 Step‑by‑Step View for Rural Developers

For someone running Ms. Allis on the ground, the automated learning path in this chapter can be pictured as:

1. **Question comes in.**  
2. System searches its **local Chroma corpora**.  
3. If local hits are strong and consistent, it answers from that base.  
4. If there is a **gap**, it marks the gap instead of pretending to know.  
5. If policy allows, it calls the **web research service**.  
6. The research results are pulled into the **sandbox** as candidates.  
7. Truth and coherence filters review those candidates.  
8. Only reviewed findings are written into the **`autonomous_learner` learning sink** with provenance.  
9. Future answers can draw on that sink, but still pass through normal guardrails.

At every step, the system is expected to **fail closed**—not answer or not write—when something important is missing or broken.

---

## 39.11 What This Chapter Does Not Claim

Within the sealed constraints, Chapter 39 does **not** claim:

- universal truth or hallucination impossibility;  
- medical, legal, or clinical cognition;  
- unrestricted autonomous authority or self‑governance;  
- any guarantee that all research sources are perfect or unbiased.

It only claims:

- operational **gap detection** in the local corpus;  
- **web‑research escalation** when permitted;  
- **truth‑reviewed storage** into learning sinks such as `autonomous_learner`;  
- a clear separation between the **automated learning loop** and the **Chroma collections** that store its outcomes.

---

## 39.12 Closing Statement

Operational evaluation in Chapter 39 treats automated learning as a **governed, step‑by‑step loop** that runs on top of the verified live‑cycle from Chapter 28. The system notices when local knowledge is not enough, uses web research to fill gaps, reviews what it finds, and writes only reviewed results into durable learning sinks.

By keeping a sharp line between **process** (automated learning) and **storage** (`autonomous_learner` and related collections), and by refusing to over‑claim about truth or autonomy, this chapter stays exactly within the academic scope sealed by the joint 28/39 gate.
