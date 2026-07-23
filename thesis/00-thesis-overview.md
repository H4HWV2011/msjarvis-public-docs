# Chapter 00 — Full System Overview (July 2026 Gate)

## Ms. Allis / MountainShares / The Commons

*Authored by Carrie Ann Kidd — Mount Hope, West Virginia*  
*Gate: Overview Documents Gate — Generated 2026‑07‑22T09:09:01‑04:00*  

---

## 00.1 What This Document Is (For Rural Developers)

This chapter is the **plain‑language operational overview** of the Ms. Allis system under the **July 2026 Overview Documents Gate**.

It explains:

- what Ms. Allis is doing **right now**, as a live system;  
- which core services are up, on which **ports**;  
- how Appalachian language and documents travel from the web into **Chroma** and then into **GBIM**;  
- how this ties back to the **chapter_closure_index.md** and the gated chapters.

It is not **future design** or a promise of what might be built later. It is a **record of the current, probed system state**, written so that a rural operator can follow it from “what is running” to “which chapter explains it.”

---

## 00.2 Ms. Allis Is Live (Not Future)

As of this gate, **Ms. Allis is a live, running system**.

The probe for the overview documents confirmed that key services are healthy:

- `ms_allis_internal_sandbox` — **port 8042**  
  - Status: `healthy`  
  - Version: `1.2.0`  
  - Property: `bbb_enforced: true`  
  - This is the internal sandbox where reasoning happens **under** the safety filter.

- Blood‑Brain Barrier (BBB)  
  - Status: `healthy`  
  - Depends on: `production_20llm` (healthy)  
  - This is the **safety wall** that filters what can reach core reasoning.

- `consciousness_bridge` — **port 8010**  
  - Status: `healthy`  
  - Connects higher‑level reasoning with memory and services.

- `brain_orchestrator`  
  - Status: `ok`  
  - Coordinates the “whole brain” behavior.

- `jarvis-chroma` — **port 8002**  
  - Status: `healthy` (nanosecond heartbeat present)  
  - Stores the **Appalachian linguistic corpus**.

- `jarvis-aaacpe-scraper` — **port 8033**  
  - Status: `healthy`  
  - Last scrape: `2026‑07‑22T10:00:02.135820`  
  - `documents_added: 90`, `errors: []`.

- `qualia-orchestrator-69dgm-real` — **port 9998**, endpoint `/evaluate`  
  - Status: `REAL`  
  - Orchestrator: **69‑DGM Cascade**.

- `jarvis-spatial-sandbox` — **port 8056**  
  - Status: `ok`  
  - `redis: connected`  
  - `hysteresis_seconds: 300.0` — changes in spatial reasoning are **time‑buffered**.

- `nbb_pituitary_gland`  
  - Status: `healthy`  
  - `i_container_1: active`, `i_container_2: active`, `integration_layer: active`  
  - `dual_awareness: true`.

- Primary Darwin‑Gödel Machine  
  - Service: `darwin_godel_machine`  
  - Status: `operational`  
  - `safety_mode: full_verification`, `modifications_logged: 0`.

For rural developers, this means: **there is a real system you can point to**, with named services and ports, not just an idea on paper.

---

## 00.3 The AAPCAppE → Chroma → GBIM Path

The Overview Gate emphasizes one critical data path: **how Appalachian language gets into Ms. Allis’s reasoning.**

### 00.3.1 AAPCAppE Scraper: What It Does

- Service: `jarvis-aaacpe-scraper`  
- Port: **8033**

This scraper **does one job**:

> Scrape the internet for **Appalachian linguistic information** and send that content into Chroma.

“Appalachian linguistic information” means documents, language, and resources **about Appalachia and its people**, not a random sample of the global web. This is how **P12 – Intelligence with a ZIP code** becomes real: the model’s knowledge is fed by **Appalachian‑focused corpus work**, not by generic scraping.

### 00.3.2 Chroma: The Appalachian Corpus Store

- Service: `jarvis-chroma`  
- Port: **8002**

Chroma is where the **Appalachian corpus is stored as vectors**.

In this gate:

- Chroma has a live **nanosecond heartbeat**;  
- The corpus written by AAPCAppE is part of the **M_corpus** used in reasoning;  
- This Chroma corpus is explicitly **shared with GBIM** as an input for spatial and belief reasoning.

Think of Chroma as the **“Appalachian library shelves”** in vector form.

### 00.3.3 Data Path in Plain Terms

The gate summary gives the data path as:

> AAPCAppE → Chroma → M_corpus → C_retrieved → S_sandbox(8042, bbb_enforced) → F_candidate → gate → GBIM

For a rural operator, step‑by‑step:

1. **AAPCAppE** pulls new Appalachian documents from the web.  
2. **Chroma** stores those documents as vectors.  
3. When Ms. Allis needs context, she builds **M_corpus** from Chroma.  
4. From M_corpus she pulls a specific **C_retrieved** set for the current question.  
5. That context goes into **S_sandbox** at **port 8042**, which is **BBB‑enforced**.  
6. The sandbox reasoning produces **F_candidate** — candidate beliefs or updates.  
7. These candidates must pass through a **gate** (BBB / governed logic).  
8. Only then can they influence **GBIM**.

The thesis overview must present this path as the **live, as‑built pipeline** for Appalachian intelligence.

---

## 00.4 GBIM Promotion as a Governed Contract

Under this gate, **GBIM is not a simple “write a pointer” operation**. Updating which GBIM collection is active is a **governed contract** with three parts:

1. **BEFORE Trigger on `gbim_active_collection`**  
   - Any attempt to change the active GBIM collection fires a trigger **before** the change is applied.

2. **Coherence Evaluator (`coherence_ok`)**  
   - Each GBIM manifest has a **coherence flag**.  
   - Only manifests with `coherence_ok == true` are even eligible for activation.

3. **Promotion Procedure (`promote_gbim_collection`)**  
   - A stored procedure performs the actual promotion.  
   - It checks `coherence_ok`, enforces rules, and then updates `gbim_active_collection`.

In plain speech:

> “To change what GBIM believes is ‘the active worldview,’ the system must pass a **trigger**, a **coherence check**, and a **promotion procedure**. There is no hidden shortcut.”

This is one of the **main examples** of governed state in the thesis and is required content for the overview.

---

## 00.5 Chapter Closure Index and Gate Logic

The **chapter_closure_index.md** file is the **official record** of which chapters are:

- `CLOSED` (fully sealed under their gate), or  
- `CLOSED_FOR_REWRITE` (sealed, but awaiting updated text like this).

The Overview Documents Gate confirms:

- **46 primary chapters** plus **Appendix A** are all under gates (no open chapters).  
- `closed_chapter_count: 46`, `open_chapter_count: 0`.  
- Both `00-thesis-overview` and `00-overview` are **CLOSED_FOR_REWRITE**, with this gate as their controlling report.

The gate logic reads:

> “All primary chapters and Appendix A must be CLOSED or CLOSED_FOR_REWRITE before overview docs gate.”

That means the Chapter 00 files are **designed to gate last**, after the rest of the system has been pulled into governed state. This document must **point readers to `chapter_closure_index.md`** as the evidence of that closure.

---

## 00.6 Live Services and Ports (July 2026 Snapshot)

The gate records the following services as **live and confirmed** for this overview:

- `ms-allis-internal-sandbox:8042`  
  - `bbb_enforced = true`, version `1.2.0`.

- `jarvis-wv-entangled-gateway:8010`  
  - Part of the live gateway & safeguard path.

- `jarvis-blood-brain-barrier:8016`  
  - Core BBB safety layer.

- `jarvis-consciousness-bridge:8107`  
  - Consciousness bridge service.

- `jarvis-brain-orchestrator:17260`  
  - High‑level orchestration.

- `nbb_pituitary_gland:8108`  
  - System‑wide mode and state regulator.

- EEG services:  
  - `jarvis-eeg-beta:8075`  
  - `jarvis-eeg-theta:8074`  
  - `jarvis-eeg-delta:8073`

- DGM stack:  
  - `nbb_darwin_godel_machines:8302`  
  - `jarvis-fifth-dgm:4002`  
  - `qualia-orchestrator-69dgm-real:9998` (69‑DGM Cascade).

- Spatial and memory:  
  - `jarvis-spatial-sandbox:8056` (redis connected)  
  - `jarvis-redis:6380` (healthy).

- Corpus:  
  - `jarvis-aaacpe-scraper:8033`  
  - `jarvis-chroma:8002` (healthy)  
  - `jarvis-chroma-tls:8443`.

For a rural developer or operator, this is the **port checklist**: if you can see these services, you are looking at the same system the thesis describes.

---

## 00.7 How the Overview Fits the Chapters

The gate enumerates a **complete chapter list** (01–52 plus Appendix A). In simple terms:

- Chapters **01–03**: Quantarithmia, GBIM, MountainShares DAO.  
- 04/44–18: Hilbert/Phi, Chroma, neurobiological metaphor, qualia, BBB, etc.  
- 19–31: containers, operations, web research, AAPCAppE, MountainShares infrastructure.  
- 32–40: DGMs, LLM ensemble, swarm, spiritual root, constitutional service, audit.  
- 41–52: test harness, post‑quantum, H_geo, Hilbert people space, temporal axis, per‑user direct sum, community commons, recurrent loops.  
- Appendix A: governed‑state mathematics.

The **Overview Documents** (this file, `00-thesis-overview`, `00-A Read_Me`) sit above this stack and are restricted by the gate to:

- talk about **live, probed mechanisms**;  
- avoid saying any chapter is **fully rewritten** (they are all `CLOSED_FOR_REWRITE` until their own gates are satisfied);  
- refer readers back to the **closure index** when making claims about chapter status.

---

## 00.8 Principles P1, P3, P5, P12, P16 — Concrete Links

The gate requires that this overview tie the core Polymathmatic Geography principles to **real architecture**, not abstractions:

- **P1 – Every where is entangled**  
  - Shown by the **AAPCAppE → Chroma → GBIM** pipeline: language, geography, and belief are handled together, not separately.

- **P3 – Power has a geometry**  
  - Shown by GBIM and H_geo (in other chapters) and by how services like `jarvis-wv-entangled-gateway` and `jarvis-spatial-sandbox` connect data to **real places**.

- **P5 – Design is a geographic act**  
  - Shown by per‑place corpus design (AAPCAppE), spatial sandbox, and the use of GBIM as a **governed state layer**, not just a database.

- **P12 – Intelligence with a ZIP code**  
  - Explicitly grounded in **AAPCAppE’s Appalachian focus** and the use of Chroma as an **Appalachian linguistic corpus store** shared with GBIM.

- **P16 – Power accountable to place**  
  - Shown by **GBIM promotion contracts**, BBB safety enforcement, DGM `full_verification` mode, and the way chapter gates are tied to concrete services and ports.

This chapter is required to **say exactly that**: these principles are backed by the **specific mechanisms** listed in the gate, not by general aspirations.

---

## 00.9 What This Overview Must Not Claim

To stay inside the gate:

- It must **not** say AAPCAppE is a general‑purpose scraper; it is **Appalachian‑specific**.  
- It must **not** say that “corpus retrieval equals direct action” — there is always a **gate** between candidates and GBIM.  
- It must **not** claim any chapter is fully rewritten; all are **CLOSED_FOR_REWRITE** until their own rewrites are completed.  
- It must **not** present the system as speculative; it must stick to **demonstrated evidence**.  
- It must **not** treat GBIM as an unguided, bare pointer write.

If a rural operator reads only this chapter, the idea should be:

> “This is a real Appalachian‑grounded AI system, with its own ports and safety checks, and every big claim has a named chapter and a gate behind it.”

---

## 00.10 Closing Note for Rural Operators

From a command line in Mount Hope or Oak Hill, the practical path is:

1. Check that the **live services and ports** listed here respond.  
2. Open `chapter_closure_index.md` to see which chapters are sealed under which gates.  
3. Use `00-thesis-overview.md` to choose the chapters that match your role (developer, policy maker, community member).  
4. Remember that **AAPCAppE, Chroma, GBIM promotion, and BBB** are the core paths this overview is allowed to claim — everything else should trace back to them.

Ms. Allis, as presented here, is **architecturally constrained by Appalachian reality**, not a free‑floating general AI. This chapter’s job is to make that constraint visible and navigable.
