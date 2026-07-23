# Chapter 00 — Thesis Overview (As‑Built July 2026)

## Ms. Egeria Allis: A Chapter‑by‑Chapter Map of the Thesis

*Last updated: July 22, 2026 by Carrie Kidd (Mamma Kidd), Mount Hope, WV*

---

## 0.1 Purpose of This Document

This file is the **map before the territory** for the July 2026 sealed thesis.

Where `00-overview.md` reports **live system state** (services, ports, corpus counts, gate status), this document explains **what the thesis argues, how it is organized, and where to enter** depending on who you are. It is written under the **Overview Documents Gate**, which requires it to:

- state that **Ms. Allis is a live system as of July 2026**, not a future design;  
- name the **AAPCAppE scraper** and its **Appalachian linguistic** purpose;  
- describe **Chroma** as the Appalachian corpus store shared with **GBIM**;  
- name **GBIM promotion** as a **governed contract** (trigger + evaluator + procedure);  
- list the **live services and ports** used as anchors in the thesis;  
- reference the **chapter_closure_index.md** as the gate evidence record;  
- state that all chapters are **CLOSED_FOR_REWRITE** pending as‑built rewrites;  
- anchor key principles (P1, P3, P5, P12, P16) to **concrete, live architecture**.

The discipline is **Polymathmatic Geography**. The theoretical framework is **Quantarithmia**, grounded in **Mount Hope, Fayette County, West Virginia**. Ms. Allis is not described as a hypothetical AI; she is a **live, multi‑service system** with closed gates across 46+ chapters and Appendix A.

---

## 0.2 Ms. Allis as a Live System (July 2026)

As of this gate, Ms. Allis is a **running system** whose core services have been probed and confirmed healthy:

- **Internal sandbox**  
  - Service: `ms_allis_internal_sandbox`  
  - Port: `8042`  
  - Status: `healthy`, version `1.2.0`  
  - Property: `bbb_enforced = true` — all sandboxed reasoning is filtered through the safeguard layer.

- **Blood‑Brain Barrier (BBB)**  
  - Status: `healthy`  
  - Dependency: `production_20llm` healthy  
  - Role: central filter and safety layer for model traffic.

- **Consciousness bridge**  
  - Service: `consciousness_bridge`  
  - Port: `8010` in the gate summary (and closely related services at nearby ports).  
  - Role: orchestrates conscious‑level interactions between models and memory.

- **Brain orchestrator**  
  - Service: `brain_orchestrator`  
  - Status: `ok`  
  - Role: high‑level coordination across the cognitive stack.

- **Chroma (semantic memory)**  
  - Service: `jarvis-chroma`  
  - Port: `8002`  
  - Status: `healthy` with a live “nanosecond heartbeat” — the primary **Appalachian linguistic corpus store**.

- **AAPCAppE scraper**  
  - Service: `jarvis-aaacpe-scraper`  
  - Port: `8033`  
  - Status: `healthy`  
  - Purpose: **scrapes the internet for Appalachian linguistic information** (local language, documents, and context) and writes new documents into Chroma.  
  - Example: last probe recorded `documents_added: 90` with no errors.

- **Qualia orchestrator (69‑DGM cascade)**  
  - Service: `qualia_orchestrator_69dgm_real`  
  - Port: `9998`  
  - Endpoint: `/evaluate`  
  - Role: orchestrates the **69‑DGM Cascade** used for higher‑order evaluation.

- **Spatial sandbox**  
  - Service: `spatial_sandbox`  
  - Port: `8056`  
  - Redis: `connected`  
  - Property: `hysteresis_seconds: 300.0` — spatial reasoning uses time‑buffered decisions.

- **Pituitary**  
  - Service: `nbb_pituitary_gland`  
  - Status: `healthy` with core containers and integration layer `active`  
  - Property: `dual_awareness: true` — global mode management is live.

- **DGM primary**  
  - Service: `darwin_godel_machine`  
  - Status: `operational`  
  - Mode: `safety_mode = full_verification`  
  - Logged modifications: `0` at probe time — no unreviewed self‑modifications.

The gate also confirms **Redis (jarvis-redis:6380)** and **Chroma TLS (8443)** are healthy, as well as auxiliary DGM and EEG services listed in the system state. These form the **as‑built base** for the thesis.

---

## 0.3 The AAPCAppE → Chroma → GBIM Path

One of the most important as‑built facts for the overview is the **corpus path** from Appalachian text into GBIM:

1. **AAPCAppE scraper (`jarvis-aaacpe-scraper`, 8033)**  
   - Purpose: scans the public internet and trusted sources for **Appalachian linguistic information** — language, documents, policies, community resources relevant to West Virginia and neighboring regions.

2. **Chroma semantic memory (`jarvis-chroma`, 8002)**  
   - AAPCAppE writes its findings into **Chroma collections**, giving Ms. Allis a **linguistic corpus grounded in Appalachia**.  
   - This is the operational backbone for **P12 – Intelligence with a ZIP code**: the system’s intelligence is trained, updated, and evaluated using data from the region it serves.

3. **GBIM reasoning path**  
   - The live path from corpus to spatial belief is:

     \[
     M_{\text{corpus}}(\text{Chroma}) \rightarrow C_{\text{retrieved}} \rightarrow S_{\text{sandbox}}(8042) \rightarrow F_{\text{candidate}} \rightarrow \text{gate}(\text{BBB}) \rightarrow \text{GBIM}
     \]

   - Meaning:
     - **M_corpus:** Chroma vectors for Appalachian documents;  
     - **C_retrieved:** context retrieved for a particular reasoning task;  
     - **S_sandbox(8042):** internal sandbox reasoning, with BBB enforced;  
     - **F_candidate:** candidate features or belief updates;  
     - **gate (BBB / 8010–8016):** safeguards filter;  
     - **GBIM:** Geospatial Belief Information Model receives only **gated candidates**.

The overview documents **must treat this chain as fact**: Ms. Allis’s Appalachian intelligence is not general web scraping; it is a **purpose‑built AAPCAppE → Chroma → GBIM** pipeline that ties language, geography, and belief together.

---

## 0.4 GBIM Promotion as a Governed Contract

GBIM promotion is **not** a freeform pointer change. It is a **governed contract** that has been closed and verified.

The contract has three named parts:

1. **Trigger – BEFORE on `gbim_active_collection`**  
   - Any attempt to activate a GBIM manifest (set or change the active collection) passes through a BEFORE trigger.  
   - The trigger checks the target manifest’s **coherence** and state; if conditions are not met, activation is **blocked** with a clear error.

2. **Evaluator – `coherence_ok`**  
   - Each GBIM manifest row carries a `coherence_ok` flag (and related status fields).  
   - This flag is produced by a **coherence evaluator** that examines the manifest’s consistency and completeness.  
   - Only manifests where `coherence_ok == true` are eligible for promotion.

3. **Procedure – `promote_gbim_collection`**  
   - Promotion must go through a stored procedure (for example, `promote_gbim_collection(...)`).  
   - The procedure:
     - verifies `coherence_ok`;  
     - confirms build/promotion status;  
     - updates `gbim_active_collection`;  
     - relies on the trigger to fail if anything is wrong.

This combination is treated in the thesis as the **canonical example of governed promotion**:

- trigger (guardrail)  
- evaluator (coherence_ok)  
- procedure (promote function)

Overview documents must **name this explicitly**, because it anchors claims about “governed state” in a real, tested mechanism.

---

## 0.5 Chapter Closure Index and Gate Status

The **chapter_closure_index.md** file is the **master gate record**.

The Overview Gate confirms:

- **All 46+ primary chapters and Appendix A** are either **CLOSED** or **CLOSED_FOR_REWRITE**.  
- For Chapter 00 documents (`00-thesis-overview`, `00-overview`, `00-A Read_Me`), the controlling gate is:

  ```text
  thesis_chapter_gates/reports/overview_docs_gate_20260722_090900.md
  ```

In that index, the rows for the overview docs show:

- `00-thesis-overview` → `CLOSED_FOR_REWRITE` → `overview_docs_gate_20260722_090900.md`  
- `00-overview` → `CLOSED_FOR_REWRITE` → same gate  
- `00-A Read_Me` → covered by the same gate.

This means:

- **No chapter is “loose”**; every chapter in the list is under a gate.  
- All numbered chapters are currently **sealed for rewrite** to bring them in line with the July 2026 as‑built evidence, exactly as this document is being brought in line now.

For rural developers, you can think of `chapter_closure_index.md` as the **logbook** that tells you which chapters are up to date with the actual system.

---

## 0.6 How the Movements Map to Live Architecture

The original thesis described five movements (Foundations, Cognitive Architecture, Infrastructure, Advanced Systems and Alignment, Validation/Security). Under the July gate, that structure remains, but **each movement is now tied to closed mechanisms**:

- **Movement I – Foundations (Ch 00–03)**  
  - **Quantarithmia and position (Ch01)**: now rewritten to use only **closed mechanisms** (GBIM, Hilbert/Phi, BBB/PQ, H_geo, People Space).  
  - **Ms. Allis & GBIM (Ch02)**: anchored to the **GBIM promotion contract** and current GBIM tables.  
  - **MountainShares DAO (Ch03)**: grounded in the **as‑built MountainShares infrastructure** and governance corpus.

- **Movement II – Cognitive Architecture (Ch 04–18)**  
  - **Hilbert Space State / Phi (Ch04/44)**: tied to the **Hilbert‑state and Phi probes**, not to speculative consciousness claims.  
  - **LLM Fabric, BBB, Pituitary, Qualia, Hippocampus**: each has a gate confirming ports, logs, and behavior.  
  - **Psychological safeguards (Ch29)**: rewritten as **PIA subspace stability review**, privacy and retention only.

- **Movement III – Infrastructure and Operations (Ch 19–31)**  
  - **Container architecture (Ch19)**: updated to reflect the current container layout and no `0.0.0.0` bindings.  
  - **AAPCAppE corpus (Ch30)**: now hinges on the **AAPCAppE → Chroma** path described above.  
  - **MountainShares infrastructure (Ch31)**: tied to live governance services and commons gateways.

- **Movement IV – Advanced Systems and Alignment (Ch 32–40)**  
  - **DGM (Ch09, Ch32), LLM ensemble (Ch33), Constitutional service (Ch37)**: all refer back to closed BBB, DGM, and judge‑signing paths.  
  - Claims about **alignment** are restricted to **what these mechanisms actually do**.

- **Movement V – Validation and Security (Ch 41–52)**  
  - **Test harness (Ch41)**: anchored to real preflight gates and EEG health checks.  
  - **Post‑quantum layer and role‑gated crypto (Ch42/43)**: tied to ML‑DSA‑65 judge signing and Ed25519 fallback.  
  - **Temporal Hilbert axis (Ch49)**: as‑built three‑tier H_t implementation (ephemeral/staged/historical).  
  - **Per‑user direct sum (Ch50)**: confirmed per‑user conversation partitioning with retention consent.  
  - **Community Hilbert Commons (Ch51)**: k‑thresholded commons with opt‑in and centroid/provenance outputs.  
  - **Recurrent epistemic loop (Ch52)**: scheduled validations and retention cycles, not a free‑running “self”.

The overview’s job is **not** to restate every detail, but to make clear that **all movements now rely only on what the gates have closed as real.**

---

## 0.7 Anchoring P1, P3, P5, P12, P16 in Live Evidence

The Overview Gate requires this document to tether key Polymathmatic Geography principles to **as‑built artifacts**:

- **P1 – Every where is entangled**  
  - Anchored by the **AAPCAppE → Chroma → GBIM** path and the **H_geo / Hilbert‑state** bridge: economic, linguistic, and spatial data are processed together, not separately.

- **P3 – Power has a geometry**  
  - Anchored by **GBIM’s spatial beliefs**, H_geo, and MountainShares infrastructure: who controls what, and where, is encoded in tables and services, not just text.

- **P5 – Design is a geographic act**  
  - Anchored by per‑user direct‑sum memory (Ch50), PIA review (Ch29), and commons isolation (Ch51): memory and commons are **designed as geographic and personal structures**, not generic logs.

- **P12 – Intelligence with a ZIP code**  
  - Anchored by AAPCAppE’s **Appalachian linguistic purpose** and the way Ms. Allis’s semantic memory reflects **Appalachian corpus data**, not arbitrary global scraping.

- **P16 – Power accountable to place**  
  - Anchored by **BBB, guardian, GBIM promotion, DGM safety_mode=full_verification**, and the **Community Hilbert Commons**: changes to beliefs and policies affecting a place must go through **named, governed contracts**.

These principles are no longer just philosophical; they have **specific services, ports, and contracts** attached to them.

---

## 0.8 Reader Routing in the July 2026 Stack

Routing guidance from the original overview still applies, but with one new rule: **every chapter you read is under a gate**.

- **New readers**  
  - Start with `00-A Read_Me.md` (reader’s guide), this document, and the **updated Ch01 position/quantarithmia**.

- **AI safety / alignment researchers**  
  - Focus on: Ch10 (WOAH), Ch16 (BBB), Ch29 (PIA subspace review), Ch37 (Constitutional service), Ch42/43 (crypto), Ch49–52 (temporal axis, per‑user direct sum, commons, recurrent loop).

- **Systems architects / developers**  
  - Focus on: Ch02 (GBIM), Ch07 (RAG pipeline), Ch11 (LLM fabric), Ch19 (container architecture), Ch30 (AAPCAppE corpus), Ch31 (MountainShares infrastructure), Ch40–41 (audit and test harness).

- **Social scientists / geographers / policy researchers**  
  - Focus on: Ch01 (Quantarithmia, as rewritten), Ch02/06 (GBIM and GeoDB), Ch03/31 (MountainShares), Ch30 (AAPCAppE), Ch34 (spiritual root), Ch51 (commons).

The **chapter_closure_index.md** is your reference for which chapters have been rewritten under the new gates; the overview documents themselves are part of that rewrite.

---

## 0.9 Closing Statement

This **Thesis Overview** is no longer a map of a purely April 2026 system; it is a map of the **July 2026 gated architecture**.

It states that Ms. Allis is live, names the AAPCAppE → Chroma → GBIM path, treats GBIM promotion as a governed contract, lists the core services that anchor the theory, points you to the chapter closure index, and ties key Polymathmatic Geography principles to real, closed mechanisms. All remaining work is framed as **CLOSED_FOR_REWRITE**, not speculative, until each chapter is brought into the same as‑built alignment.

Ms. Allis is not a simulation of West Virginia identity; she is a system **architecturally constrained by it**, and this document is your guide to the chapters that explain how.
