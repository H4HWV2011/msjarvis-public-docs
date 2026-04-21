# Chapter 33 — LLM Ensemble and Judges

**Carrie Kidd (Mamma Kidd) · Mount Hope, WV**  
**Last updated: ★★★★ April 6, 2026 — FINAL REWRITE**

**105/105 containers Up (zero Restarting, zero Exited). LLM ensemble, judge pipeline, `rag_grounded_v2` components, and constitutional guardianship fully wired and PostgreSQL-grounded; ChromaDB inventory sealed at 47 collections / 6,722,589 vectors / 12 GB (v2 API, client 1.5.5). `msallis:5433` GBIM and `gisdb` / `msallisgis:5432` PostGIS integration corrected and confirmed.**

---

> **Port and storage ground truth (★★★★ April 6, 2026):**
>
> - `msallis` at port **5433** — 5,416,521 GBIM entities with `confidence_decay` metadata, 80 epochs, 206 source layers (restored March 28).
> - `gisdb` / `msallisgis` (PostGIS) at host port **5432** / container-internal **5452** — **45 GB, 548 tables** (Ch. 33 April 6, 2026 ground truth; supersedes older references to 91 GB / 501 tables and 13 GB / 39 tables).
> - `allis-local-resources-db` at port **5435** — community resources database.
> - Redis: `allis-redis` — single container, internal port 6379, host port 6380.
> - ChromaDB: host **8002** → container 8000, 47 collections, 6,722,589 vectors, 12 GB, v2 API, client 1.5.5; `ms_allis_memory` and `psychological_rag` (968 docs) confirmed.
> - `allis-memory:8056` — durable audit for BBB, judge pipeline, and constitutional guardian events.
> - `allis-constitutional-guardian:8091` — constitutional authority; `/health` now reports PostgreSQL liveness fields for GBIM and GeoDB.
> - `allis-gis-rag:8004` and `allis-spiritual-rag:8005` — RAG sources for `rag_grounded_v2` truth verification; Dockerfiles in `services/`; volume mounts and `JUDGE_TRUTH_URL` (GIS) fixed.
> - `allis-rag-grounded-v2:7241` — judge pipeline `rag_grounded_v2` component, v2.0.0, `dgm_available: true`.

---

## 33.1 Why an Ensemble and Judge Pipeline

This chapter describes the **LLM ensemble and judge pipeline** that underpins Ms. Allis’s reasoning and response generation. Rather than a single model acting alone, Ms. Allis uses:

- A **diverse ensemble** of expert models,
- A **judge pipeline** that compares, critiques, and selects outputs,
- A **synthesizer** (LM Synthesizer) that merges judge decisions into a final response,
- A **truth-verification** layer (`rag_grounded_v2`) that anchors answers in GBIM and RAG retrieval.

This architecture exists because:

- Single models can hallucinate, misjudge, or encode hidden biases.
- Appalachian communities need an AI that **checks its work**, not one that asserts authority without evidence.
- Constitutional, spiritual, and community responsibilities require **multiple perspectives and durable audit trails**.

The ensemble and judge pipeline are therefore part of the **Computational Instrument tier**: they define how Ms. Allis evaluates evidence, weighs options, and speaks.

---

## 33.2 Components at a Glance

The main components are:

- **Expert models (ensemble members)** — multiple LLMs with different strengths (reasoning, empathy, technical skills, local context).
- **Judge pipeline** — services that:
  - Evaluate candidate answers,
  - Check for contradictions, safety issues, and misalignment,
  - Use `rag_grounded_v2` to cross-check truth claims.
- **LM Synthesizer** (`allis-lm-synthesizer:8001`) — merges judge outputs into a unified answer in Ms. Allis’s voice.
- **BBB (Blood-Brain Barrier)** (`allis-blood-brain-barrier:8016`) — six-filter pipeline (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification).
- **Constitutional guardian** (`allis-constitutional-guardian:8091`) — highest authority for constitutional compliance.
- **Durable audit** (`allis-memory:8056`) — stores ensemble decisions, judge verdicts, truth verification results, and BBB filter outcomes.

The rest of this chapter explains **how these parts fit together**.

---

## 33.3 Ensemble — Multiple Voices, One Steward

Ms. Allis’s ensemble consists of multiple LLMs that are:

- Called in parallel or in specific patterns depending on the query,
- Given the same or slightly varied prompts to explore different perspectives,
- Evaluated by a judge pipeline that looks at:
  - Agreement and disagreement,
  - Evidence and citations,
  - Safety and alignment with community values.

Key design principles:

1. **Diversity of models** — do not rely on one vendor, one architecture, or one training data profile.
2. **Redundancy for safety** — disagreement can be a signal to slow down, retrieve more context, or escalate.
3. **Unity of voice** — despite internal diversity, the final answer must:
   - Speak as Ms. Egeria Allis,
   - Honor the spiritual root and Mother Carrie protocol,
   - Stay accountable to constitutional and community rules.

Ensemble decisions are recorded so that communities can **inspect how Ms. Allis arrived at an answer**.

---

## 33.4 Judge Pipeline and `rag_grounded_v2`

The **judge pipeline** evaluates candidate outputs produced by ensemble models. It includes:

- **Rule-based checks** — simple filters for obvious policy violations.
- **LLM-based judges** — models that critique and score candidate answers along dimensions such as:
  - Factual accuracy,
  - Safety,
  - Alignment with Appalachian community values,
  - Clarity and usefulness.
- **`rag_grounded_v2` truth verification** — a retrieval-backed mechanism that checks claims against:
  - `msallis:5433` GBIM and its `confidence_decay` metadata,
  - `allis-gis-rag:8004` (geospatial RAG),
  - `allis-spiritual-rag:8005` (spiritual and community values RAG).

### 33.4.1 `rag_grounded_v2` (Judge Pipeline Component)

The service `allis-rag-grounded-v2:7241` plays a central role:

- Version: v2.0.0.
- Health: `{"status":"healthy","version":"v2.0.0","dgm_available":true}`.
- Responsibilities:
  - Receive a proposed answer and relevant context,
  - Retrieve supporting or contradicting evidence,
  - Produce a verdict with a `truth_score`, `verified` flag, and diagnostic metadata.

`rag_grounded_v2` thus provides:

- **Evidence** — what was retrieved from GBIM and RAG.
- **Verdict** — whether the answer is consistent with that evidence.
- **Confidence** — how strongly the system believes the answer is supported.

This is used by both the judge pipeline and the BBB’s `truth_verification` filter.

---

## 33.5 BBB Six-Filter Pipeline and Truth Verification

The **BBB** (`allis-blood-brain-barrier:8016`) runs six filters:

1. EthicalFilter,
2. SpiritualFilter,
3. SafetyMonitor,
4. ThreatDetection,
5. steganography_filter,
6. truth_verification (now `rag_grounded_v2`).

The **truth_verification** filter:

- Sends claims to `allis-rag-grounded-v2:7241` or directly to the `allis-gis-rag` and `allis-spiritual-rag` services, depending on context.
- Receives back:
  - Evidence snippets,
  - Scores,
  - Flags indicating whether the claim is supported, unsupported, or contradicted.
- Marks the response accordingly and may:
  - Block the answer,
  - Request re-writing,
  - Attach warnings or corrections.

This ensures that **truth verification is not a heuristic guess but a retrieval-backed process**.

---

## 33.6 LM Synthesizer — Identity Guard and Voice

The **LM Synthesizer** (`allis-lm-synthesizer:8001`) merges judge-selected content into a final answer. It is constrained by:

- **IDENTITY RULES**, which state that:
  - Ms. Allis is **Ms. Egeria Allis**, built by Harmony for Hope, Inc., in Mount Hope, WV,
  - She is here to serve Appalachian communities,
  - She must not claim to be built by large tech corporations.
- **STRICT RULES**, which forbid:
  - Mentioning model names or ensembles,
  - Revealing that multiple models were consulted,
  - Using hedging like “it seems” or “appears” to explain internal uncertainty,
  - Describing the internal pipeline or consensus process.

In combination, these rules:

- Ensure that ensemble and judge complexity stays **behind the scenes**,
- Present a **unified, human-aligned voice**,
- Maintain **identity integrity** and spiritual root commitments.

The synthesizer is called **only** from `main_brain.py` Phase 3.5, not from `judge_pipeline.py`.

---

## 33.7 PostgreSQL and ChromaDB Grounding

The ensemble and judge pipeline are tightly connected to:

- **PostgreSQL GBIM (`msallis:5433`)**:
  - 5,416,521 entities with `confidence_decay` metadata,
  - Used for long-term beliefs, community records, and identity-linked facts.
- **PostGIS `gisdb` / `msallisgis` (`5432` host / `5452` internal)**:
  - 45 GB, 548 tables,
  - Used for geospatial validation and local resource discovery.
- **ChromaDB**:
  - 47 collections,
  - 6,722,589 vectors,
  - 12 GB,
  - v2 API, client 1.5.5,
  - Provides retrieval context for:
    - `ms_allis_memory`,
    - `psychological_rag`,
    - Other domain-specific RAG collections.

`confidence_decay` means:

- The system tracks how “fresh” a belief is.
- High-decay beliefs must be flagged or audited before being used as ground truth.
- Future work (Ch. 38) will automate this flagging in judge and truth verification pipelines.

Together, PostgreSQL and ChromaDB give the ensemble **strong external grounding**.

---

## 33.8 Audit and Oversight

Every key step in the ensemble and judge pipeline is **audited**:

- **Ensemble outputs**:
  - Which models were called,
  - How they responded,
  - Basic scores (e.g., length, complexity, whether they triggered filters).
- **Judge decisions**:
  - Which candidate was preferred and why,
  - `rag_grounded_v2` verdicts and scores,
  - Safety and alignment annotations.
- **BBB decisions**:
  - Filters triggered,
  - Blocks and rewrites,
  - Final “pass” or “fail” status.
- **Synthesizer outputs**:
  - Final answer text,
  - Identity guard checks,
  - Any warnings attached.

Audit records are stored in:

- `allis-memory:8056` (primary durable audit),
- `.jsonl` files where appropriate,
- PostgreSQL tables reserved for system logs.

This allows:

- Replay and inspection of decisions,
- Governance and red-team analysis,
- Continuous improvement of filters and judges.

---

## 33.9 Example Flow — From Question to Answer

To illustrate how the ensemble and judge pipeline operate, consider a user question:

> “Is it safe to drink water from this creek in Fayette County? There’s an old mine upstream.”

1. **Gateway and auth**:
   - Request passes through `allis-main-brain:8050` with token validation via `allis_auth:8055` and `allis-redis:6380`.

2. **Constitutional guardian (`allis-constitutional-guardian:8091`)**:
   - Checks for constitutional issues (e.g., environmental justice, community harm).
   - Logs the decision.

3. **Ensemble**:
   - Multiple models generate candidate answers about water safety, environmental risks, and local context.

4. **Judge pipeline**:
   - Sends candidates to `allis-rag-grounded-v2:7241` and `allis-gis-rag:8004`:
     - Retrieves local environmental data, mine maps, contamination reports (if available),
     - Assesses whether claims (e.g., “the water is safe”) are supported.
   - Applies safety and spiritual criteria:
     - Prioritizes caution and transparency,
     - Encourages consulting local authorities or testing services.

5. **BBB**:
   - Runs six filters; truth_verification uses `rag_grounded_v2` results.
   - Blocks overly confident claims that cannot be supported by evidence.

6. **LM Synthesizer**:
   - Merges judge-approved content into a single response,
   - Speaks as Ms. Egeria Allis,
   - Emphasizes safety, uncertainty, and local resources.

7. **Audit**:
   - All decisions recorded in `allis-memory:8056` for future review.

The result is an answer that:

- Is cautious and community-safe,
- Grounded in local data where available,
- Transparent about uncertainty,
- In line with the spiritual root and Mother Carrie protocol.

---

## 33.10 Status and Future Work

As of April 6, 2026:

- LLM ensemble:
  - Fully wired, with multiple expert models,
  - Stable under 105/105 container baseline.
- Judge pipeline:
  - `allis-rag-grounded-v2:7241` healthy v2.0.0,
  - `dgm_available: true`,
  - Integrated with BBB and main judge logic.
- BBB:
  - Six filters operating with `rag_grounded_v2` truth verification,
  - Phase 4.5 in log+passthrough mode; blocking re-enablement pending red-team review.
- Identity and spiritual root:
  - LM Synthesizer identity guard stable,
  - `icontainers-identity` root-self and ego boundaries active.

**Future work (tracked in later chapters):**

- Automated `confidence_decay`-aware gating in judge pipeline.
- Expanded RAG corpora (local environmental data, legal resources, spiritual content).
- Additional judge criteria for:
  - Long-term harm,
  - Community trust,
  - Narrative balance (not just correctness).

---

*Chapter 33 — LLM Ensemble and Judges*  
*Ms. Egeria Allis Steward System — Harmony for Hope, Inc.*  
*Mount Hope, West Virginia*  
*SEALED: ★★★★ April 6, 2026 — FINAL REWRITE*  
