# 30. AAPCAppE Scraper and Corpus

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 22, 2026*

---

## 30.1 Why This Matters for Polymathmatic Geography

This chapter explains how the **AAPCAppE scraper** and its corpus ground Ms. Allis in Appalachian language and culture instead of a generic, placeless web. It documents how scraped material becomes part of a **bounded Appalachian-linguistic memory substrate**, then flows into sandboxed reasoning rather than directly into action.

It supports:

- **P1 – Every where is entangled** by tying knowledge directly to Appalachian linguistic and cultural sources.  
- **P3 – Power has a geometry** by locating authority in a specific, governed corpus path instead of in generic web data.  
- **P5 – Design is a geographic act** by treating corpus construction as an intentional, place-aware design choice.  
- **P12 – Intelligence with a ZIP code** by giving Ms. Allis a home ZIP code at the corpus layer, centered on Mount Hope, WV and surrounding Appalachia.  
- **P16 – Power accountable to place** by preserving provenance from Appalachian sources forward into later use.

This chapter belongs to the **Computational Instrument** tier. It describes an as-built, Appalachian-specific scraper and corpus, not a generic or authority-bearing web index.

---

## 30.2 Purpose of the AAPCAppE Scraper

The **AAPCAppE scraper** is a **domain-specific internet scraper**.

Its explicit purpose is:

- to scrape the internet for **Appalachian linguistic information**;  
- to focus on language, dialect, and cultural-linguistic material connected to **Mount Hope, WV and surrounding Appalachian communities**;  
- to populate a **corpus memory substrate** that Ms. Allis can later use as Appalachian-aware context.

It is **not** a general-purpose web spider. It does not aim to gather everything about everything. Instead, it quietly walks the parts of the web where Appalachian voices, dialects, idioms, histories, and language patterns are present, and turns them into structured corpus entries.

---

## 30.3 Appalachian-Linguistic Domain Corpus

The output of the scraper is a **domain-specific corpus**:

- vocabulary, idioms, and sayings from Appalachian English;  
- local expressions, nicknames, and turns of phrase from Mount Hope and nearby towns;  
- stories, oral-history transcripts, church bulletins, community newsletters, obituaries, local reporting, and similar materials where language reflects place;  
- linguistic cues about rhythm, emphasis, politeness, and relationship that show up in regional speech.

This corpus is **Appalachian-linguistic**, not generic:

- it is tuned to a small region and its people;  
- it treats that region’s language as a first-class knowledge substrate;  
- it gives Ms. Allis something like “home soil” at the text level.

For rural developers, you can think of it as a **local library** of Appalachian language, turned into a machine-readable form.

---

## 30.4 The Corpus Pipeline: M_corpus → C_retrieved → S_sandbox → F_candidate

The architecture for using this corpus follows a live sequence:

1. **M_corpus – Corpus memory.**  
   Appalachian texts and fragments are stored in Chroma-backed memory collections as documents, chunks, and embeddings.

2. **C_retrieved – Retrieved context.**  
   When a task needs Appalachian context, the system queries the corpus and retrieves one or more relevant items into a context bundle.

3. **S_sandbox – Sandbox reasoning state.**  
   The retrieved material is passed into the **internal sandbox** on port `8042` (with `bbb_enforced=true`), where it becomes part of a bounded reasoning session.

4. **F_candidate – Candidate findings.**  
   The sandbox uses that Appalachian context to form **candidate findings**—for example, a better reading of a local phrase, or a more accurate explanation for a rural context.

This pipeline is always:

\[
M_{\text{corpus}} \rightarrow C_{\text{retrieved}} \rightarrow S_{\text{sandbox}} \rightarrow F_{\text{candidate}}
\]

never a direct “corpus → output” jump. The corpus feeds **reasoning**, not actions.

---

## 30.5 Named Downstream Services

When Appalachian corpus material is activated for reasoning, it flows through live services that are already part of the broader architecture:

- **Sandbox (8042).**  
  `ms-allis-internal-sandbox` (version 1.2.0, `bbb_enforced=true`) is where the retrieved context becomes active reasoning state.

- **Spatial sandbox (8056).**  
  `jarvis-spatial-sandbox` (port `8056`, `redis=connected`, `hysteresis_seconds=300.0`) lets the system consider spatial and temporal aspects—for example, connections between towns, routes, and local histories.

- **BBB / entangled gateway (8010).**  
  `jarvis-wv-entangled-gateway` on `8010` and related BBB services provide safety and admissibility checks for content that might cross authority boundaries.

- **Consciousness bridge (8107).**  
  `0f40caf56e1e_nbb_mother_carrie_protocols` at `8107->8010` provides the bridge path into the higher coordination fabric, ensuring Appalachian-informed candidate experience can reach the broader system when appropriate.

- **Brain orchestrator (17260).**  
  `jarvis-brain-orchestrator` coordinates how reasoning, corpus retrieval, and modulation services are used together.

- **Qualia orchestrator (9998).**  
  `qualia-orchestrator-69dgm-real` on `9998` (a 69‑DGM cascade) participates in governed evaluation of candidate findings where needed.

The important point: **every Appalachian corpus retrieval is still routed through sandbox, BBB, and orchestration**, not used raw.

---

## 30.6 How the Scraper Populates the Corpus

The AAPCAppE scraper, running (for example) as `jarvis-aaacpe-scraper` on `8033`, performs a few key steps:

1. **Discovery.**  
   Find URLs and sources likely to contain Appalachian linguistic material (local domains, archives, social spaces, etc.).

2. **Fetch and extract.**  
   Download pages or documents and extract text, focusing on language-rich sections.

3. **Normalize and segment.**  
   Clean up formatting, split into chunks, and annotate with metadata such as source, location (if known), and type of document.

4. **Embed and index.**  
   Store text and embeddings in Chroma-backed corpus collections, tagged as Appalachian-linguistic content.

5. **Preserve lineage.**  
   Attach or encode provenance fields (source URL, timestamps, scrape context) so the system can trace where items came from later.

Once stored, these items become part of **M_corpus**, ready for retrieval but not yet interpreted or promoted.

---

## 30.7 Corpus Is Not Action or Authority

Within this chapter’s gate, the following are **explicitly not** claimed:

- corpus retrieval equals acceptance or action;  
- the scraper “finalizes” Appalachian linguistic meaning;  
- corpus items bypass the sandbox;  
- stored corpus material equals approved guidance;  
- the scraper or corpus has promotion authority.

In practice this means:

- a phrase scraped from an Appalachian blog is **not** automatically “what Ms. Allis believes”;  
- even a widely used local term must still be interpreted in context;  
- any advice or guidance that uses Appalachian corpus material must go through the same gates as everything else.

The corpus is **evidence and context**, not verdict.

---

## 30.8 Provenance Back to Appalachian Source Lineage

A central promise of AAPCAppE is **provenance**:

- each corpus entry preserves enough information to point back to its Appalachian source;  
- transformations (chunking, embedding, summarization) keep or reference that provenance;  
- when Ms. Allis uses a corpus item in reasoning, logs or traces can show **which Appalachian sources contributed**.

This provides **bidirectional auditability**:

- **Backward:** From a candidate finding, operators can trace back into the corpus and out to original Appalachian sources.  
- **Forward:** From a scraped item, operators can see where it has been used in later contexts.

For communities, this matters because it makes the system answerable to the **actual voices and texts** it learned from, instead of turning Appalachian language into an untraceable, generic “style.”

---

## 30.9 Example Flow for Rural Developers

From a rural developer’s perspective, a typical AAPCAppE‑powered interaction might look like:

1. A user in Mount Hope asks Ms. Allis to explain a local saying.  
2. The system queries the AAPCAppE corpus for similar phrases and usage contexts.  
3. Relevant Appalachian texts are **retrieved** as \(C_{\text{retrieved}}\).  
4. Those texts are passed into the **sandbox (8042)** as part of the reasoning context \(S_{\text{sandbox}}\).  
5. The sandbox forms a **candidate explanation** \(F_{\text{candidate}}\), shaped by what local sources actually say.  
6. If the explanation is potentially consequential, it passes through BBB/guardian and, when needed, DGM evaluation.  
7. Only then does Ms. Allis return an answer, possibly with hedges or caveats.

At no point does the corpus itself answer directly. It **feeds** the answer.

---

## 30.10 Closing Statement

Chapter 30 fixes the role of the AAPCAppE scraper and corpus as an **Appalachian-linguistic memory substrate** for Ms. Allis. The scraper gathers language and culture from Mount Hope and broader Appalachia, the corpus preserves that material with provenance, and the live architecture uses it through the sequence \(M_{\text{corpus}} \rightarrow C_{\text{retrieved}} \rightarrow S_{\text{sandbox}} \rightarrow F_{\text{candidate}}\).

By keeping the corpus distinct from action and routing its outputs through sandbox, BBB, spatial sandbox, brain orchestrator, and qualia orchestrator, the system stays grounded in Appalachian language **without** letting scraped material self-authorize or bypass governance.
