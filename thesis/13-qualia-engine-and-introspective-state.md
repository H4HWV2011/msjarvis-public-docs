# 13. Qualia Engine and Introspective State

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: April 23, 2026 — ALL OI ITEMS CLOSED; container count → 100;
vectors → ~6,740,611; pituitary mode → `baseline`; `autonomous_learner` → 21,181 exact;
two-container DB split applied throughout; `msallisgis` → 294 tables / 16 GB;
`postgis-forensic` added; all April 16 OI items remain CLOSED.*

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis keeps a running, structured account of her own
activity so that others can audit and guide it. It supports:

- **P1 – Every where is entangled** by tying internal narratives to specific communities,
  datasets, and places that appear in retrieval and spatial backbones.
- **P3 – Power has a geometry** by making every qualitative "feeling" traceable back to
  concrete logs, memory entries, and spatial identifiers.
- **P5 – Design is a geographic act** by treating introspective records as designed
  artifacts that shape how Appalachian realities are described and reflected on.
- **P12 – Intelligence with a ZIP code** by ensuring that Ms. Allis's self-descriptions
  include where interactions are happening, not just what was said.
- **P16 – Power accountable to place** by building a glass-box layer of self-description
  that other agents and human stewards can query, critique, and improve.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies how
operational traces, memory, and evaluation signals are woven into an introspective fabric
that can be inspected and used for governance.

---

## ★ Status as of April 23, 2026 — ALL OI ITEMS CLOSED

> **April 23, 2026 UPDATE:** Values updated from April 16 baseline.
> Container count → **100 Up** (zero Restarting, zero Exited).
> ChromaDB v2 → **48 collections, ~6,740,611 vectors** (host port **8002**).
> `autonomous_learner` → **21,181 records** (exact, April 23, 2026).
> `nbb_pituitary_gland` mode → **`baseline`** (was `elevated` April 16).
> Two-container DB split: **Production:** `msallis-db` / `msallis-db` host **5433** /
> container **5432** — `msallisgis` **16 GB / 294 tables / 11 schemas**.
> **Forensic:** `postgis-forensic` host **5432** — `msallisgis` **17 GB / 314 tables /
> 9 schemas** — forensic only.
> `allis-memory` / `allis-memory` (port **8056**) `/memory/sessions` → HTTP 200,
> **14 active sessions** confirmed with `ALLIS_API_KEY`.
> All April 16 OI items remain CLOSED. ML-DSA-65 FIPS 204 signing confirmed:
> sig=**3309 bytes**, verify=**True**, fingerprint=`d81a5d90...edb0`.

| Category | Details |
|:--|:--|
| **Implemented and verified** | `allis-qualia-engine` — Up, **internal Docker network port 8017/tcp, no host binding**. ★ **CORRECTION (permanent): Host port 8017 = BBB output filter** (`{"status":"ok","service":"bbb-output-filter","backend":"http://allis-blood-brain-barrier:8016/filter"}`). Three Qualia Engine modules confirmed operational: **emotional-resonance**, **meaning-making**, **experience-generator**. `nbb_qualia_engine` (`msallis-rebuild-nbb_qualia_engine-1`) — Up, host port **8303** → internal 7008/tcp. `nbb_pituitary_gland` — ✅ Up, host port **8108** → internal 80/tcp, **mode `baseline`** (April 23, 2026). EEG Delta (port **8073**), EEG Theta (**8074**), EEG Beta (**8075**) — all active, PIA OK. `IntrospectiveRecord` — ✅ **IMPLEMENTED** (`services/introspective_record.py`, all classes instantiate — OI-13-A CLOSED). `WOAHResult` Pydantic schema — ✅ **LIVE** in `introspective_record.py` (OI-29 CLOSED). ML-DSA-65 FIPS 204 judge verdict signing — ✅ **IMPLEMENTED** (`dilithium-py 1.4.0`, `build_signed_verdict_signature_v3()`, sign+verify round-trip True, sig=3309 bytes — OI-13-E CLOSED). All Qualia Engine outputs use **`all-minilm:latest` 384-dim embeddings**. ★ **100 containers Up — zero Restarting, zero Exited (April 23, 2026)**. |
| **Partially implemented / scaffolded** | Sensory-integration multi-input aggregation module — scaffolded, not yet fully active in production pipeline. `nbb_blood_brain_barrier` (`msallis-rebuild-nbb_blood_brain_barrier-1`) — Up, confirmed separate from `allis-blood-brain-barrier:8016`. |
| **Placeholder / future work** | `phenomenal_consciousness` and `subjective_experience` directories exist as placeholders in the `neurobiologicalbrain` tree. `subjective_experience` component uses direct-experience fallback (§13.7). Semantic dedup audit of `autonomous_learning` collection (recommended follow-on). Zero-vector ChromaDB collections (`gbim_entities`, `ms_allis_memory`, `gis_data`, `pia_records`, `psychological_knowledge`) flagged for review as separate follow-on. |
| **Architectural notes — DB (April 23, 2026 — two-container split)** | **Production:** `msallis-db` / `msallis-db` host **5433** / container **5432**, role `postgres`, `msallisgis`, **16 GB / 294 tables / 11 schemas** — production write target for all services. **Forensic:** `postgis-forensic` host **5432**, role `allis`, `msallisgis`, **17 GB / 314 tables / 9 schemas** — forensic auditing only, not a production write target. GBIM entity store is **ChromaDB `gbim_worldview_entities`: 5,416,521 vectors** (host port **8002** v2 API) — no relational `gbim_entities` table exists in any PostgreSQL instance. Accessed internally by `allis-gbim-query-router:7205` and `allis-gbim-benefit-indexer:7206` only. |
| **Architectural notes — ChromaDB** | v2 API at host port **8002** — correct query path: `/api/v2/tenants/default_tenant/databases/default_database/collections`. **48 collections, ~6,740,611 vectors (April 23, 2026)**. `spiritual_rag` absent — content absorbed into `spiritual_texts` (79,181 vectors), `spiritual_wisdom` (135 vectors), `spiritual_knowledge` (12 vectors) (OI-13-K CLOSED). v1 path `/api/v1/collections` returns incomplete results — do not use for authoritative counts. |
| **Architectural notes — ports** | `allis-memory` / `allis-memory` (port **8056**) — `/health` returns HTTP 200 (intentional liveness probe); `/memory/sessions` → HTTP 200 with **14 active sessions** (April 23, 2026, authenticated with `ALLIS_API_KEY`). Codebase: `~/msallis-rebuild-working/msallis-rebuild/`. |

> **Note on qualia:** Throughout this chapter, "qualia" refers to Ms. Allis's internal,
> narrative representation of what is happening — constructed from text content and
> context features as explicit JSON structures — not to any claim of subjective
> experience.

---

## 13.1 Purpose and Design Principles

The introspective layer is designed to meet three main objectives:

- **Aggregation**
  Collect relevant signals from diverse subsystems, including conversational interfaces,
  retrieval and memory services, optimization and self-evaluation layers, and global
  governance signals from the `nbb_pituitary_gland` (§13.9). The Qualia Engine focuses
  on transforming per-event content into emotional, semantic, experiential, and
  community-level fields, while consolidation services gather cross-event context from
  memory stores and spatial backbones. These backbones include:
  - **Production DB:** `msallis-db` host **5433** / container **5432** — `msallisgis`
    **16 GB / 294 tables / 11 schemas** (PostGIS)
  - **Forensic DB:** `postgis-forensic` host **5432** — `msallisgis` **17 GB / 314
    tables / 9 schemas** — forensic auditing only
  - **GBIM (internal only):** via `allis-gbim-query-router:7205` — no host binding
  - **Local resources:** `allis-local-resources-db` port **5435** — local_resources only
  - **ChromaDB v2:** host port **8002** — **48 collections, ~6,740,611 vectors**
    (April 23, 2026)

- **Structure**
  Organize these signals into well-typed records that can be indexed, filtered, and
  inspected by both humans and other services. Each record ties together identifiers,
  timestamps, roles, retrieved evidence, pituitary governance mode, EEG band states,
  evaluation scores, ML-DSA-65 judge verdict signatures, and a narrative description
  into a single coherent unit, with qualitative fields explicitly separated from
  operational metrics. The `IntrospectiveRecord` and `WOAHResult` Pydantic classes in
  `services/introspective_record.py` are the canonical implementation of this schema
  (OI-13-A and OI-29 closed April 16, 2026).

- **Modulation**
  Provide a place where feedback from evaluators, optimization processes, constitutional
  principles, and `nbb_pituitary_gland` global mode settings can influence how the
  system describes its own situation. Over time, this allows Ms. Allis to maintain an
  evolving, self-consistent narrative about what it has done, what it is doing, and how
  well it is performing, while keeping every field traceable to logs, service responses,
  spatial identifiers, or database entries.

The implementation follows the project's emphasis on transparency: all fields in
introspective records are intended to be grounded in observable events and state. For
related work, see Doshi-Velez & Kim, "Towards A Rigorous Science of Interpretable
Machine Learning" (https://arxiv.org/abs/1702.08608) and Lipton, "The Mythos of Model
Interpretability" (https://arxiv.org/abs/1606.03490).

---

## 13.2 Data Sources Feeding Introspection

- **Interaction traces**
  Conversational entrypoints record incoming messages with user identifiers or session
  context. Conversation logs and health endpoints supply signals about which agents,
  personas, and qualia or lens configurations were applied.

- **Retrieval, belief, and spatial state**
  ★ ChromaDB v2 corpus: **48 active collections, ~6,740,611 total vectors** (April 23,
  2026 — query via
  `http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections`).
  Collections include `spiritual_texts` (79,181 vectors — absorbs former `spiritual_rag`),
  `psychological_rag` (968 docs), `autonomous_learner` (**21,181 records**, April 23,
  2026 — exact; Phase 1.45 active), `msallis_docs` (7,465 items),
  `gbim_worldview_entities` (5,416,521 vectors — authoritative GBIM entity store), and
  others. Spatial identifiers sourced from production DB `msallis-db` (host **5433**,
  `msallisgis` **294 tables**, **16 GB**) and forensic DB `postgis-forensic` (host
  **5432**, **314 tables**, **17 GB** — forensic only).

- **EEG neurobiological band signals**
  Three EEG heartbeat services provide continuous 30-second rolling neurobiological
  activity windows: **EEG Delta** (host port **8073**, `eeg-delta-30s` — PIA OK),
  **EEG Theta** (host port **8074**), **EEG Beta** (host port **8075**). Introspective
  records capture which EEG bands were active and their PIA state at event time, as
  these influence Qualia Engine emotional resonance weighting and `nbb_pituitary_gland`
  mode selection.

- **`nbb_pituitary_gland` global governance signals**
  `msallis-rebuild-nbb_pituitary_gland-1` (host port **8108** → internal 80/tcp,
  **mode `baseline`** April 23, 2026) is an always-on neurobiological governance
  service that sets system-wide operating modes and modulates WOAH weights. Current mode
  is a **mandatory input to every introspective record**. Fully documented in §13.9 and
  Chapter 15.

- **ML-DSA-65 judge verdict signatures**
  `build_signed_verdict_signature_v3()` (`dilithium-py 1.4.0`, ML-DSA-65 FIPS 204)
  produces cryptographically signed judge verdicts on every evaluation cycle. Signature:
  3309 bytes (FIPS 204 Level 3 specification — exact match confirms correct key material
  and parameter set). Private key: `judge-keys/judge_sk.bin` (4032 bytes plaintext),
  `judge_sk.bin.enc` (4064 bytes AES-256-GCM encrypted). Public key fingerprint:
  SHA3-256(`judge_pk.bin`) = `d81a5d90...edb0`. **OI-13-E CLOSED April 16, 2026.**

- **Optimization and self-evaluation**
  Darwin–Gödel Machine agents produce scores, labels, and validation outcomes.
  WOAH-style weighting assigns importance and safety weights. `WOAHResult` Pydantic
  schema is live in `introspective_record.py` (OI-29 closed). See
  https://arxiv.org/html/2505.22954v2 for conceptual DGM context.

- **System health and configuration**
  ★ As of April 23, 2026, **100 containers Up** — zero `0.0.0.0` exposures — zero
  Restarting, zero Exited. BBB output filter at host port **8017** (`bbb-output-filter`
  → `allis-blood-brain-barrier:8016`) is the final output gate; its pass/fail status
  is a key health signal for introspective state. `allis-memory` / `allis-memory`
  (port **8056**): `/memory/sessions` → HTTP 200, **14 active sessions** (authenticated
  with `ALLIS_API_KEY`).

---

## 13.3 Internal Record Structure

The `IntrospectiveRecord` Pydantic class in `services/introspective_record.py` is the
canonical implementation. All classes confirmed instantiating cleanly (OI-13-A closed
April 16, 2026). Fields:

- **Identifiers**
  Request ID, user/session handle, stable key joinable to conversation memory, spatial
  tables, and logs.

- **Temporal fields**
  Event timestamp and introspective entry creation timestamp.

- **Context and perspective fields**
  Active role/persona, problem domain, spatial hints, user role, community lens. Spatial
  context: production DB `msallis-db` (host **5433**, `msallisgis` **294 tables**,
  **16 GB**) and forensic DB `postgis-forensic` (host **5432**, **314 tables**, **17 GB**
  — forensic only). GBIM via `allis-gbim-query-router:7205` — no host binding by design.

- **Evidence summary**
  Which ChromaDB v2 collections were queried (**48 collections, host port 8002**); which
  documents were returned; which GBIM nodes were touched (from ChromaDB
  `gbim_worldview_entities` — 5,416,521 vectors, authoritative GBIM entity store); which
  services contributed. Phase 1.45 prepends top-5 `autonomous_learner` records
  (**21,181 records**, April 23, 2026; 384-dim `all-minilm:latest`) to every production
  request — the primary evidence-summary anchor.

- **EEG band state**
  `eeg_delta_active` (port **8073**), `eeg_theta_active` (port **8074**),
  `eeg_beta_active` (port **8075**), and PIA status for each. Connects the introspective
  record to the neurobiological rhythm layer.

- **`nbb_pituitary_gland` governance snapshot**
  `nbb_pituitary_mode` (e.g., `baseline`, `elevated`, `transparency`) and
  `woah_weights_snapshot` at event time. **Mandatory for every record** — see §13.9
  for why. Current mode: **`baseline`** (April 23, 2026).

- **`WOAHResult` fields**
  `ethical_score`, `alignment_passed`, `pituitary_mode` — live Pydantic schema in
  `introspective_record.py` (OI-29 closed). Confirmed April 16:
  `{"ethical_score": 0.97, "alignment_passed": true, "pituitary_mode": "PituitaryMode.elevated"}`.

- **ML-DSA-65 verdict signature fields**
  `key_fingerprint` (SHA3-256 of `judge_pk.bin` = `d81a5d90...edb0`), `payload_hash`
  (SHA3-256 of verdict JSON), `value` (3309-byte ML-DSA-65 FIPS 204 signature),
  `algorithm` (`ML-DSA-65`), `signed_by`. All fields wired in
  `build_signed_verdict_signature_v3()`. Verify round-trip:
  `ML_DSA_65.verify(pk, verdict_json, sig_bytes)` = **True** (OI-13-E closed).
  ⚠️ **Security note:** Back up `judge-keys/judge_sk.bin` to offline storage
  immediately if not already done.

- **Evaluation and control**
  Judge scores, DGM validation outcomes, lens/constitutional rules applied,
  active/inactive layer flags. `bbb_output_passed` (boolean) — the BBB output filter
  at host port **8017** is the final gate. `allis-memory` / `allis-memory` (port
  **8056**): `/memory/sessions` → HTTP 200, 14 active sessions (authenticated). See
  Bai et al. (https://arxiv.org/abs/2212.08073) and Zheng et al.
  (https://arxiv.org/abs/2306.05685).

- **Narrative and qualia text**
  Human-readable description of the event, produced by the Qualia Engine's
  emotional-resonance and meaning-making modules (internal port 8017/tcp, no host
  binding).

---

## 13.4 Writing and Updating Introspective Records

- **At request start:** Role selection, lens settings, routing instructions, and current
  `nbb_pituitary_gland` mode (**`baseline`**, April 23, 2026) captured as initial
  governance snapshot.

- **After retrieval:** Phase 1.45 queries `autonomous_learner` (**21,181 records**,
  April 23, 2026) via `all-minilm:latest` (384-dim) and prepends top-5 results to
  `enhanced_message`. ChromaDB v2 API at host port **8002** is the correct query
  surface; v1 path returns incomplete results.

- **After generation:** BBB output filter (host port **8017** → `bbb-output-filter` →
  `allis-blood-brain-barrier:8016`) passes or blocks the response.
  `BBB_OUTPUT_BLOCKING=true` since April 6, 2026. `bbb_output_passed`, active qualia
  paths, and safety check outcomes attach as evaluation fields. ML-DSA-65 judge verdict
  signed via `build_signed_verdict_signature_v3()`. Results stored in `allis-memory`
  / `allis-memory` (port **8056**).

- **On scheduled cycles:** Periodic health audits and DGM re-evaluations produce
  introspective entries covering broader time windows. DGM verdict updates append to
  existing records.

---

## 13.5 Reading Introspective State

- **Recent activity views:** `allis-memory` / `allis-memory` (host port **8056**,
  127.0.0.1) — authenticated API surface. `/health` returns HTTP 200 (intentional
  liveness probe); `/memory/sessions` → HTTP 200 with **14 active sessions** (April 23,
  2026, authenticated with `ALLIS_API_KEY`).

- **Thematic and spatial slices:** Production DB `msallis-db` (host **5433**,
  `msallisgis` **16 GB**, **294 tables**). Forensic DB `postgis-forensic` (host
  **5432**, `msallisgis` **17 GB**, **314 tables** — forensic only). See Winner, "Do
  Artifacts Have Politics?" (https://www.cc.gatech.edu/~beki/cs4001/Winner.pdf).

- **Status and performance summaries:** ★ April 23, 2026 — **100 containers Up**, zero
  `0.0.0.0` exposures, preflight gate 27/27 gates ✅ green. All containers bound to
  `127.0.0.1`. GPU pipeline: **102.58s** confirmed on RTX 4070 (CPU 436s baseline
  **RETIRED STALE**).

---

## 13.6 Interaction with Language Models

- **Narrative synthesis:** Qualia Engine emotional resonance and meaning-making outputs
  — enriched with pituitary mode (**`baseline`**, April 23), EEG band states, and lens
  settings — provide ingredients for compact, grounded human-readable narratives.
  `WOAHResult` (OI-29 closed) provides the structured evaluation envelope feeding
  narrative generation.

- **Reflective analysis:** Models examine introspective record slices to identify failure
  modes, spatial patterns, or shifts in memory source usage. ML-DSA-65 signed verdicts
  (OI-13-E closed) provide cryptographic non-repudiation for judge verdicts used in
  reflective analysis. See AgentBench (https://arxiv.org/abs/2308.03688) and Zheng et
  al. (https://arxiv.org/abs/2306.05685).

---

## 13.7 Links to Memory, Spatial, and Qualia Layers

- **Semantic and conversational memory:** ChromaDB v2 — **48 active collections,
  ~6,740,611 vectors** (host port **8002**, April 23, 2026). `autonomous_learner`
  **21,181 records** (April 23, 2026 — exact). `msallis_docs` 7,465 items.
  `spiritual_rag` — **ABSENT from live list** — content absorbed into `spiritual_texts`
  (79,181 vectors), `spiritual_wisdom` (135 vectors), `spiritual_knowledge` (12 vectors)
  (OI-13-K closed). `psychological_rag` restored (968 docs, March 28). Zero-vector
  collections (`gbim_entities`, `ms_allis_memory`, `gis_data`, `pia_records`,
  `psychological_knowledge`) flagged for separate follow-on review.

- **Belief and knowledge structures — GBIM architecture (April 23, 2026 — definitive):**

  | Store | Container | Port | Data |
  |:--|:--|:--|:--|
  | Production PostgreSQL | `msallis-db` | host **5433** / container **5432** | `msallisgis` — 16 GB / 294 tables / 11 schemas — production writes |
  | Forensic PostgreSQL | `postgis-forensic` | host **5432** | `msallisgis` — 17 GB / 314 tables / 9 schemas — forensic only |
  | Local resources PostGIS | `allis-local-resources-db` | **5435** | Local resources only — 64 resources, all 55 WV counties |
  | ChromaDB `gbim_worldview_entities` | `allis-chroma` | **8002** | **5,416,521 vectors ← authoritative GBIM entity store** |
  | ChromaDB `gbim_entities` | `allis-chroma` | 8002 | 0 vectors — empty placeholder |

  **`gbim_entities` (0 vectors) is an empty placeholder. `gbim_worldview_entities`
  (5,416,521 vectors) is the live production store. There is no relational
  `gbim_entities` table anywhere in the stack.** GBIM app data accessed internally by
  `allis-gbim-query-router:7205` and `allis-gbim-benefit-indexer:7206` only — no host
  binding (OI-13-L CLOSED). See Battaglia et al.
  (https://arxiv.org/abs/1806.01261).

- **Spatial backbone:** Production DB `msallis-db` (host **5433**, `msallisgis`
  **16 GB**, **294 tables**). Forensic DB `postgis-forensic` (host **5432**,
  `msallisgis` **17 GB**, **314 tables** — forensic only).

- **Qualia Engine outputs:** `allis-qualia-engine` runs on **internal Docker network
  port 8017/tcp with no host binding**. ★ **Host port 8017 = BBB output filter**
  (`{"status":"ok","service":"bbb-output-filter","backend":"http://allis-blood-brain-barrier:8016/filter"}`).
  Qualia envelope: `emotional_resonance` (primary emotion, intensity), `meaning`
  (keyphrases), `subjective_experience` (direct-experience fallback). Draws on ChromaDB
  `gbim_worldview_entities` (host port **8002** v2 API).

  > **NBB-Qualia Engine:** `msallis-rebuild-nbb_qualia_engine-1` — Up, host port
  > **8303** → internal 7008/tcp. Health check returns
  > `{"status":"ok","service":"nbb_blood_brain_barrier"}` — response label reflects
  > shared NBB health template. Source:
  > `services/msallis-rebuild-nbb_qualia_engine-1_ms_allis_consciousness_bridge.py`.

---

## 13.8 Role in the Larger Architecture

- **Audit and accountability:** Durable record of what Ms. Allis did, which information
  was used, which `nbb_pituitary_gland` mode was active (**`baseline`**, April 23,
  2026), and which services participated. BBB output filter (host port **8017**) is the
  final output gate and a critical audit checkpoint. `BBB_OUTPUT_BLOCKING=true` since
  April 6, 2026. ML-DSA-65 signed verdicts provide cryptographic non-repudiation across
  all judge outputs. April 23 baseline: 100 containers Up, `/memory/sessions` HTTP 200
  with 14 sessions ✅, all 5 judge signing keys present ✅, preflight 27/27 ✅. See
  Raji et al. (https://arxiv.org/abs/2001.00973) and ISO/IEC 42001
  (https://www.iso.org/news/ref3077.html).

- **Coordination input:** Snapshot of recent behavior — pituitary mode, EEG band states,
  `WOAHResult` fields, WOAH weight snapshot — queried by higher-level controllers. The
  `nbb_pituitary_gland` (§13.9) is itself a primary consumer of this coordination
  information via `judge_to_pituitary_bridge.py`.

- **Research and improvement support:** ChromaDB v2 (**48 collections, ~6,740,611
  vectors**) and `autonomous_learner` growth curve (**21,181 records**, April 23, 2026)
  are primary research datasets. `IntrospectiveRecord` unified class (OI-13-A closed)
  provides the canonical schema for research-driven improvement analysis.

---

## 13.9 The `nbb_pituitary_gland` — Global Governance and Hormonal Modulation

> **This section was added April 16, 2026. The `nbb_pituitary_gland` was entirely absent
> from all prior versions of this chapter. It is mandatory here because its mode state
> is a direct input to the introspective record schema (§13.3) and modulates every
> Qualia Engine output.**

### What It Is

The `nbb_pituitary_gland` is the neurobiological brain's always-on global governance and
hormonal modulation service. Modeled on the biological pituitary gland's role as the
"master gland," it sets system-wide operating modes, modulates WOAH weights, adjusts
constitutional compliance thresholds, and provides warmth modulation signals to the
interaction tone layer. Fully documented in Chapter 15 (Pituitary Gland and Global
Modes).

**Confirmed production state (April 23, 2026):**

| Field | Value |
|:--|:--|
| Container | `msallis-rebuild-nbb_pituitary_gland-1` |
| Host port | **8108** → internal 80/tcp |
| Status | ✅ Up |
| Health response | `{"status":"healthy","service":"nbb_pituitary_gland","mode":"baseline"}` |
| Current mode | **`baseline`** (updated from `elevated` April 16) |
| Source | `~/msallis-rebuild-working/msallis-rebuild/neurobiologicalbrain/pituitary_gland/service/pituitary_gland.py` |
| Services-safe mirror | `services-safe/pituitary_gland.py` |
| Judge bridge | `services-safe/judge_to_pituitary_bridge.py` |
| Warmth modulation | `services-safe/enhance_pituitary_warmth.py` |
| WOAH bridge | `services-safe/woah_qualia_bridge.py` |
| Data directory | `data/pituitary/` |

### Position in the NBB Pipeline

The `nbb_pituitary_gland` sits **upstream of the Qualia Engine**:

```
nbb_pituitary_gland (8108, mode: baseline)
├─► WOAH weights ──► nbb_qualia_engine (8303) ──► nbb_consciousness_containers
├─► allis-qualia-engine (internal 8017/tcp) ──► allis-consciousness-bridge (8020)
├─► judge_to_pituitary_bridge ──► allis-judge-pipeline (7239)
├─► nbb_prefrontal_cortex ──► nbb_subconscious
└─► nbb_mother_carrie_protocols (warmth/tone, port 8107)
```

### Operating Modes

| Mode | Description | Impact on Introspective Records |
|:--|:--|:--|
| `baseline` | ★ **Current (April 23, 2026)** — standard WOAH weights and governance thresholds | Standard safety envelope; baseline compliance thresholds |
| `standard` | Normal operation — equivalent to baseline in most contexts | Standard safety envelope |
| `elevated` | Heightened safety and governance thresholds (was active April 16) | All judge scores interpreted under stricter thresholds; must be flagged in records |
| `transparency` | Full glass-box mode — maximum auditability | Expanded provenance and chain-of-thought fields in records |

### Why This Is Mandatory in Chapter 13

1. The Qualia Engine cannot produce an accurate introspective narrative without knowing
   what governance constraints were active at event time.
2. `WOAHResult` fields in introspective records are only interpretable in the context of
   the pituitary mode that set the WOAH weights.
3. Judge verdicts carry different semantic weight in `baseline` vs. `elevated` vs.
   `transparency` mode.
4. `judge_to_pituitary_bridge.py` creates a closed feedback loop — judge verdicts update
   pituitary state, which modulates subsequent qualia outputs — that introspective
   records must capture to reconstruct any causal chain.

### Warmth Modulation

`enhance_pituitary_warmth.py` modulates the pituitary's emotional warmth output — the
degree to which responses carry affirming, supportive, and community-centered tonal
qualities. This warmth signal flows into the Qualia Engine's emotional resonance module
and influences `nbb_mother_carrie_protocols` (`msallis-rebuild-nbb_mother_carrie_protocols-1`,
host port **8107**) interaction tone. Introspective records capture the warmth level as
a normalized field when available.

---

## 13.10 Open Items — ALL CLOSED ✅

All OI items confirmed closed. No new open items as of April 23, 2026.

| OI ID | Status | Closed Evidence |
|:--|:--|:--|
| **OI-13-A** | ✅ **CLOSED** | `IntrospectiveRecord` instantiation OK; all imports clean — `services/introspective_record.py` |
| **OI-13-E** | ✅ **CLOSED** | ML-DSA-65 FIPS 204 sign+verify round-trip **True**; sig=**3309 bytes** (FIPS 204 Level 3 exact spec); fingerprint=`d81a5d90...edb0`; `dilithium-py 1.4.0`; `build_signed_verdict_signature_v3()` implemented and verified |
| **OI-13-J** | ✅ **CLOSED** | Zero exited/restarting containers; count methodology artifact documented — healthy |
| **OI-13-K** | ✅ **CLOSED** | **48 collections / ~6,740,611 vectors** (April 23, 2026 v2 API); `spiritual_rag` merged into `spiritual_texts` / `spiritual_wisdom` / `spiritual_knowledge` |
| **OI-13-L** | ✅ **CLOSED** | GBIM entity store = **ChromaDB `gbim_worldview_entities` (5,416,521 vectors)**; no relational `gbim_entities` table in any PostgreSQL instance; internal access only via `allis-gbim-query-router:7205` |
| **OI-29** | ✅ **CLOSED** | `WOAHResult` Pydantic schema live in `introspective_record.py`; confirmed: `{"ethical_score": 0.97, "alignment_passed": true, "pituitary_mode": "PituitaryMode.elevated"}` |

**ML-DSA-65 infrastructure footnote:** Signature verification confirmed. Signature size
3309 bytes is per FIPS 204 specification for the Level 3 (ML-DSA-65) parameter set —
exact match confirms correct key material and `dilithium-py` operating against the
correct parameter set. Private key resides at `judge-keys/judge_sk.bin` (4032 bytes
plaintext) and `judge_sk.bin.enc` (4064 bytes AES-256-GCM encrypted).
⚠️ **Back up `judge_sk.bin` to offline storage immediately if not already done.**

**Zero-vector ChromaDB collections (flagged for separate follow-on review — not
blocking):**
- `gbim_entities`: 0 — empty placeholder (distinct from `gbim_worldview_entities`
  5,416,521 ✅)
- `ms_allis_memory`: 0
- `gis_data`: 0
- `pia_records`: 0
- `psychological_knowledge`: 0

---

## 13.11 Sprint Validation Log — April 23, 2026 Update

### Infrastructure numbers — stale (April 16) → current (April 23)

| Field | April 16 Value | April 23 Value | Source |
|:--|:--|:--|:--|
| Container count | 109 | **100** | `docker ps` April 23 |
| ChromaDB total vectors | 6,740,034 | **~6,740,611** | ChromaDB v2 API April 23 |
| ChromaDB collections | 48 | **48** | v2 API confirmed |
| `autonomous_learner` records | 21,181+ | **21,181 exact** | April 23, 2026 |
| `nbb_pituitary_gland` mode | `elevated` | **`baseline`** | `/health` April 23 |
| Production DB | `msallisgis` 551 tables / 45 GB | **`msallis-db` host 5433 / 294 tables / 16 GB** | Two-container split confirmed |
| Forensic DB | Not split | **`postgis-forensic` host 5432 / 314 tables / 17 GB** | Two-container split confirmed |
| `allis-memory` `/memory/sessions` | HTTP 401 unauthenticated | **HTTP 200, 14 sessions** (authenticated with `ALLIS_API_KEY`) | `curl` April 23 |
| GPU pipeline | 102.58s (April 16) | **102.58s confirmed** (RTX 4070) | April 23 |
| CPU baseline | 436s (stale) | **RETIRED STALE** | Permanent |
| Port 8017 identity | BBB output filter (corrected April 16) | **BBB output filter — confirmed** | Permanent correction |
| `nbb_qualia_engine` port | Host 8303 → 7008/tcp | **Confirmed unchanged** | `docker ps` April 23 |

---

*Last updated: April 23, 2026 — Carrie Kidd (Mamma Kidd), Mount Hope WV*

*★ April 16, 2026 — ALL OI ITEMS CLOSED: Port 8017 corrected (BBB output filter facade).
§13.9 `nbb_pituitary_gland` added for first time. nbb_qualia_engine port confirmed 8303.
EEG band data sources added. ChromaDB v2 API confirmed 48 collections / 6,740,034
vectors. `spiritual_rag` merged. GBIM entity store corrected to ChromaDB
`gbim_worldview_entities`. `IntrospectiveRecord` implemented. ML-DSA-65 FIPS 204
confirmed. `WOAHResult` Pydantic schema live. Chapter 13 CLOSED.*

*★ April 23, 2026 UPDATE: Container count → 100. Vectors → ~6,740,611.
`autonomous_learner` → 21,181 exact. Pituitary mode → `baseline`. Two-container DB
split applied throughout (production `msallis-db` host 5433 / 294 tables / 16 GB;
forensic `postgis-forensic` host 5432 / 314 tables / 17 GB). `allis-memory`
`/memory/sessions` → HTTP 200 / 14 sessions confirmed. All OI items remain CLOSED.*
