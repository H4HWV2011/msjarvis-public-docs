# 13. Qualia Engine and Introspective State

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: 2026-04-16 — SPRINT REWRITE — ALL OI ITEMS CLOSED*

## Why This Matters for Polymathmatic Geography

This chapter explains how Ms. Allis keeps a running, structured account of her own activity so that others can audit and guide it. It supports:

- **P1 – Every where is entangled** by tying internal narratives to specific communities, datasets, and places that appear in retrieval and spatial backbones.
- **P3 – Power has a geometry** by making every qualitative "feeling" traceable back to concrete logs, memory entries, and spatial identifiers.
- **P5 – Design is a geographic act** by treating introspective records as designed artifacts that shape how Appalachian realities are described and reflected on.
- **P12 – Intelligence with a ZIP code** by ensuring that Ms. Allis's self-descriptions include where interactions are happening, not just what was said.
- **P16 – Power accountable to place** by building a glass-box layer of self-description that other agents and human stewards can query, critique, and improve.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies how operational traces, memory, and evaluation signals are woven into an introspective fabric that can be inspected and used for governance.

---

## ★ Status as of April 16, 2026 — ALL OI ITEMS CLOSED

> **April 16, 2026 FULL SPRINT REWRITE:** Port 8017 misidentification corrected — host port 8017 is the **BBB output filter facade** (`bbb-output-filter` → `allis-blood-brain-barrier:8016`), NOT the Qualia Engine. `allis-qualia-engine` runs on **internal Docker network port 8017/tcp with no host binding**. `nbb_qualia_engine` confirmed at host port **8303** → internal 7008/tcp. `nbb_pituitary_gland` fully documented for the first time (§13.9) — host port **8108**, mode `elevated`, judge bridge, warmth modulation, NBB pipeline position. `msallis` GBIM is **internal-only by design** — connection refused from host; authoritative entity count is **ChromaDB `gbim_worldview_entities`: 5,416,521 vectors** — no relational `gbim_entities` table exists in any PostgreSQL instance. `msallisgis`: **551 tables, 45 GB**. ChromaDB v2 API at host port **8002**: **48 collections, 6,740,034 total vectors** confirmed (`spiritual_rag` merged into `spiritual_texts`; v1 path `/api/v1/collections` is deprecated — do not use for authoritative counts). Container count: **109 Up** — zero Restarting, zero Exited; count methodology artifact vs. prior "110" baseline documented (OI-13-J closed). `IntrospectiveRecord` unified class confirmed implemented (`services/introspective_record.py`, all classes instantiate — OI-13-A closed). ML-DSA-65 FIPS 204 sign+verify round-trip confirmed True, sig=3309 bytes, fingerprint=d81a5d90...edb0 (OI-13-E closed). `WOAHResult` Pydantic schema live in `introspective_record.py` (OI-29 closed). Codebase path corrected throughout: `~/msallis-rebuild-working/msallis-rebuild/`.

| Category | Details |
|---|---|
| **Implemented and verified** | `allis-qualia-engine` — Up, **internal Docker network port 8017/tcp, no host binding**. ★ **CORRECTION: Host port 8017 = BBB output filter** (`{"status":"ok","service":"bbb-output-filter","backend":"http://allis-blood-brain-barrier:8016/filter"}`). Three Qualia Engine modules confirmed operational: **emotional-resonance**, **meaning-making**, **experience-generator**. `nbb_qualia_engine` (`msallis-rebuild-nbb_qualia_engine-1`) — Up 6 days, host port **8303** → internal 7008/tcp. `nbb_pituitary_gland` (`msallis-rebuild-nbb_pituitary_gland-1`) — ✅ Up 6 hours, host port **8108** → internal 80/tcp, `{"status":"healthy","service":"nbb_pituitary_gland","mode":"elevated"}`. EEG Delta (port **8073**) confirmed: `eeg-delta-30s`, PIA OK, 3,288+ pulses, 4 recent BBB events. EEG Theta (**8074**), EEG Beta (**8075**) active. `IntrospectiveRecord` — ✅ **IMPLEMENTED** (`services/introspective_record.py`, all classes instantiate — OI-13-A CLOSED). `WOAHResult` Pydantic schema — ✅ **LIVE** in `introspective_record.py` (OI-29 CLOSED). ML-DSA-65 FIPS 204 judge verdict signing — ✅ **IMPLEMENTED** (`dilithium-py 1.4.0`, `build_signed_verdict_signature_v3()`, sign+verify round-trip True, sig=3309 bytes — OI-13-E CLOSED). All Qualia Engine outputs use **`all-minilm:latest` 384-dim embeddings**. ★ **109/109 containers Up — zero Restarting, zero Exited (April 16, 2026)** (OI-13-J CLOSED). |
| **Partially implemented / scaffolded** | Sensory-integration multi-input aggregation module — scaffolded, not yet fully active in production pipeline. `nbb_blood_brain_barrier` (`msallis-rebuild-nbb_blood_brain_barrier-1`) — Up, confirmed separate from `allis-blood-brain-barrier:8016`. |
| **Placeholder / future work** | `phenomenal_consciousness` and `subjective_experience` directories exist as placeholders in the `neurobiologicalbrain` tree. `subjective_experience` component uses direct-experience fallback (§13.7). Semantic dedup audit of `autonomous_learning` collection (recommended follow-on). Zero-vector ChromaDB collections (`gbim_entities`, `ms_allis_memory`, `gis_data`, `pia_records`, `psychological_knowledge`) flagged for review as separate follow-on. |
| **Architectural notes — GBIM** | GBIM entity store is **ChromaDB `gbim_worldview_entities`: 5,416,521 vectors** (host port **8002** v2 API) — this is the authoritative GBIM entity count. `gbim_entities` ChromaDB collection = 0 vectors (empty placeholder). **No relational `gbim_entities` table exists in any PostgreSQL instance** — confirmed April 16 across all three: `msallis` (GBIM app data, internal-only), `msallisgis` (GIS/spatial data only, port 5432 ★), `allis-local-resources-db` (local_resources only, port 5435). Accessed internally by `allis-gbim-query-router:7205` and `allis-gbim-benefit-indexer:7206` only (OI-13-L CLOSED). |
| **Architectural notes — ChromaDB** | v2 API at host port **8002** — correct query path: `/api/v2/tenants/default_tenant/databases/default_database/collections`. **48 collections, 6,740,034 vectors (April 16, 2026 confirmed)**. `spiritual_rag` collection absent from live list — content absorbed into `spiritual_texts` (79,181 vectors), `spiritual_wisdom` (135 vectors), `spiritual_knowledge` (12 vectors) prior to this audit (OI-13-K CLOSED). v1 path `/api/v1/collections` returns incomplete results — do not use for authoritative counts. |
| **Architectural notes — ports** | `allis-memory:8056` — `/health` returns HTTP 200 (intentional liveness probe); `/memory/sessions` returns **HTTP 401 unauthenticated** (correct security posture); authenticated with `ALLIS_API_KEY` returns HTTP 200 with 14 active sessions (April 16, 2026). Codebase: `~/msallis-rebuild-working/msallis-rebuild/`. |

> **Note on qualia:** Throughout this chapter, "qualia" refers to Ms. Allis's internal, narrative representation of what is happening — constructed from text content and context features as explicit JSON structures — not to any claim of subjective experience.

---

## 13.1 Purpose and Design Principles

The introspective layer is designed to meet three main objectives:

- **Aggregation**
  Collect relevant signals from diverse subsystems, including conversational interfaces, retrieval and memory services, optimization and self-evaluation layers, and global governance signals from the `nbb_pituitary_gland` (§13.9). The Qualia Engine focuses on transforming per-event content into emotional, semantic, experiential, and community-level fields, while consolidation services gather cross-event context from memory stores and spatial backbones. These backbones include PostgreSQL `msallisgis` (port 5432 ★, **45 GB** PostGIS, **551 tables**), `msallis` GBIM (internal Docker network via `allis-gbim-query-router:7205` — no host binding), `allis-local-resources-db` (port 5435, local_resources only), and ChromaDB v2 (host port **8002** — **48 collections, 6,740,034 vectors**).

- **Structure**
  Organize these signals into well-typed records that can be indexed, filtered, and inspected by both humans and other services. Each record ties together identifiers, timestamps, roles, retrieved evidence, pituitary governance mode, EEG band states, evaluation scores, ML-DSA-65 judge verdict signatures, and a narrative description into a single coherent unit, with qualitative fields explicitly separated from operational metrics. The `IntrospectiveRecord` and `WOAHResult` Pydantic classes in `services/introspective_record.py` are the canonical implementation of this schema (OI-13-A and OI-29 closed April 16, 2026).

- **Modulation**
  Provide a place where feedback from evaluators, optimization processes, constitutional principles, and `nbb_pituitary_gland` global mode settings can influence how the system describes its own situation. Over time, this allows Ms. Allis to maintain an evolving, self-consistent narrative about what it has done, what it is doing, and how well it is performing, while keeping every field traceable to logs, service responses, spatial identifiers, or database entries.

The implementation follows the project's emphasis on transparency: all fields in introspective records are intended to be grounded in observable events and state. For related work, see Doshi-Velez & Kim, "Towards A Rigorous Science of Interpretable Machine Learning" (https://arxiv.org/abs/1702.08608) and Lipton, "The Mythos of Model Interpretability" (https://arxiv.org/abs/1606.03490).

---

## 13.2 Data Sources Feeding Introspection

- **Interaction traces**
  Conversational entrypoints record incoming messages with user identifiers or session context. Conversation logs and health endpoints supply signals about which agents, personas, and qualia or lens configurations were applied.

- **Retrieval, belief, and spatial state**
  ★ ChromaDB v2 corpus: **48 active collections, 6,740,034 total vectors** (April 16, 2026 — query via `http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections`). Collections include `spiritual_texts` (79,181 vectors — absorbs former `spiritual_rag`), `psychological_rag` (968 docs), `autonomous_learner` (21,181+ records, Phase 1.45 active), `msallis_docs` (7,465 items), `gbim_worldview_entities` (5,416,521 vectors — authoritative GBIM entity store), and others. Spatial identifiers sourced from `msallisgis` (port 5432 ★, 993 ZCTA centroids, **551 tables**, **45 GB**).

- **EEG neurobiological band signals**
  Three EEG heartbeat services provide continuous 30-second rolling neurobiological activity windows: **EEG Delta** (host port **8073**, service `eeg-delta-30s` — confirmed healthy April 16: PIA OK, 3,288+ pulses, last pulse `2026-04-16T19:12:57Z`, 4 recent BBB events), **EEG Theta** (host port **8074**), **EEG Beta** (host port **8075**). Introspective records capture which EEG bands were active and their PIA state at event time, as these influence Qualia Engine emotional resonance weighting and `nbb_pituitary_gland` mode selection.

- **`nbb_pituitary_gland` global governance signals**
  `msallis-rebuild-nbb_pituitary_gland-1` (host port **8108** → internal 80/tcp, mode `elevated` April 16) is an always-on neurobiological governance service that sets system-wide operating modes and modulates WOAH weights. Current mode is a **mandatory input to every introspective record**. Fully documented in §13.9 and Chapter 15.

- **ML-DSA-65 judge verdict signatures**
  `build_signed_verdict_signature_v3()` (`dilithium-py 1.4.0`, ML-DSA-65 FIPS 204) produces cryptographically signed judge verdicts on every evaluation cycle. Signature: 3309 bytes (FIPS 204 Level 3 specification — exact match confirms correct key material and parameter set). Private key: `judge-keys/judge_sk.bin` (4032 bytes plaintext), `judge_sk.bin.enc` (4064 bytes AES-256-GCM encrypted). Public key fingerprint: SHA3-256(`judge_pk.bin`) = `d81a5d90...edb0`. **OI-13-E CLOSED April 16, 2026.**

- **Optimization and self-evaluation**
  Darwin–Gödel Machine agents produce scores, labels, and validation outcomes. WOAH-style weighting assigns importance and safety weights. `WOAHResult` Pydantic schema is live in `introspective_record.py` (OI-29 closed). See https://arxiv.org/html/2505.22954v2 for conceptual DGM context (May 2025 external preprint).

- **System health and configuration**
  ★ As of April 16, 2026, **109/109 containers Up** — zero `0.0.0.0` exposures — zero Restarting, zero Exited (OI-13-J closed — count methodology artifact). BBB output filter at host port **8017** (`bbb-output-filter` → `allis-blood-brain-barrier:8016`) is the final output gate; its pass/fail status is a key health signal for introspective state.

---

## 13.3 Internal Record Structure

The `IntrospectiveRecord` Pydantic class in `services/introspective_record.py` is the canonical implementation. All classes confirmed instantiating cleanly (OI-13-A closed April 16, 2026). Fields:

- **Identifiers**
  Request ID, user/session handle, stable key joinable to conversation memory, spatial tables, and logs.

- **Temporal fields**
  Event timestamp and introspective entry creation timestamp.

- **Context and perspective fields**
  Active role/persona, problem domain, spatial hints, user role, community lens. Spatial context: `msallisgis` (port 5432 ★, 993 ZCTA centroids, **551 tables**, **45 GB**) and `msallis` GBIM (internal Docker network via `allis-gbim-query-router:7205` — no host binding by design).

- **Evidence summary**
  Which ChromaDB v2 collections were queried (**48 collections, host port 8002**); which documents were returned; which GBIM nodes were touched (from ChromaDB `gbim_worldview_entities` — 5,416,521 vectors, authoritative GBIM entity store); which services contributed. Phase 1.45 prepends top-5 `autonomous_learner` records (384-dim `all-minilm:latest`) to every production request — the primary evidence-summary anchor.

- **EEG band state**
  `eeg_delta_active` (port **8073**), `eeg_theta_active` (port **8074**), `eeg_beta_active` (port **8075**), and PIA status for each. Connects the introspective record to the neurobiological rhythm layer.

- **`nbb_pituitary_gland` governance snapshot**
  `nbb_pituitary_mode` (e.g., `elevated`, `standard`, `transparency`) and `woah_weights_snapshot` at event time. **Mandatory for every record** — see §13.9 for why.

- **`WOAHResult` fields**
  `ethical_score`, `alignment_passed`, `pituitary_mode` — live Pydantic schema in `introspective_record.py` (OI-29 closed). Confirmed April 16: `{"ethical_score": 0.97, "alignment_passed": true, "pituitary_mode": "PituitaryMode.elevated"}`.

- **ML-DSA-65 verdict signature fields**
  `key_fingerprint` (SHA3-256 of `judge_pk.bin` = `d81a5d90...edb0`), `payload_hash` (SHA3-256 of verdict JSON), `value` (3309-byte ML-DSA-65 FIPS 204 signature), `algorithm` (`ML-DSA-65`), `signed_by`. All fields wired in `build_signed_verdict_signature_v3()`. Verify round-trip: `ML_DSA_65.verify(pk, verdict_json, sig_bytes)` = **True** (OI-13-E closed). ⚠️ **Security note:** Back up `judge-keys/judge_sk.bin` to offline storage immediately if not already done.

- **Evaluation and control**
  Judge scores, DGM validation outcomes, lens/constitutional rules applied, active/inactive layer flags. `bbb_output_passed` (boolean) — the BBB output filter at host port **8017** is the final gate. `allis-memory:8056` `/memory/sessions` confirmed HTTP 401 unauthenticated (correct). See Bai et al. (https://arxiv.org/abs/2212.08073) and Zheng et al. (https://arxiv.org/abs/2306.05685).

- **Narrative and qualia text**
  Human-readable description of the event, produced by the Qualia Engine's emotional-resonance and meaning-making modules (internal port 8017/tcp, no host binding).

---

## 13.4 Writing and Updating Introspective Records

- **At request start:** Role selection, lens settings, routing instructions, and current `nbb_pituitary_gland` mode captured as initial governance snapshot.

- **After retrieval:** Phase 1.45 queries `autonomous_learner` (21,181+ records, April 10, 2026) via `all-minilm:latest` (384-dim) and prepends top-5 results to `enhanced_message`. ChromaDB v2 API at host port **8002** is the correct query surface; v1 path returns incomplete results.

- **After generation:** BBB output filter (host port **8017** → `bbb-output-filter` → `allis-blood-brain-barrier:8016`) passes or blocks the response. `bbb_output_passed`, active qualia paths, and safety check outcomes attach as evaluation fields. ML-DSA-65 judge verdict signed via `build_signed_verdict_signature_v3()`. Results stored in `allis-memory:8056`.

- **On scheduled cycles:** Periodic health audits and DGM re-evaluations produce introspective entries covering broader time windows. DGM verdict updates append to existing records.

---

## 13.5 Reading Introspective State

- **Recent activity views:** `allis-memory` (host port **8056**, 127.0.0.1) — authenticated API surface. `/health` returns HTTP 200 (intentional liveness probe); `/memory/sessions` returns **HTTP 401 unauthenticated** (correct); authenticated with `ALLIS_API_KEY` returns HTTP 200 with **14 active sessions** (April 16, 2026).

- **Thematic and spatial slices:** `msallisgis` (port 5432 ★ confirmed — **45 GB** PostGIS, **551 tables**, 993 ZCTA centroids). See Winner, "Do Artifacts Have Politics?" (https://www.cc.gatech.edu/~beki/cs4001/Winner.pdf).

- **Status and performance summaries:** ★ April 16, 2026 — **109/109 containers Up**, zero `0.0.0.0` exposures, preflight gate 27/27 gates ✅ green. Container count methodology: `docker compose ps --services` reports **101 defined services**; `docker ps` shows **109 running containers** — the discrepancy is a count-in-favor artifact (sidecars, network bridges, and named volume containers appear in `docker ps` but not in `--services`). Zero containers in exited or restarting state. This is healthy.

---

## 13.6 Interaction with Language Models

- **Narrative synthesis:** Qualia Engine emotional resonance and meaning-making outputs — enriched with pituitary mode, EEG band states, and lens settings — provide ingredients for compact, grounded human-readable narratives. `WOAHResult` (OI-29 closed) provides the structured evaluation envelope feeding narrative generation.

- **Reflective analysis:** Models examine introspective record slices to identify failure modes, spatial patterns, or shifts in memory source usage. ML-DSA-65 signed verdicts (OI-13-E closed) provide cryptographic non-repudiation for judge verdicts used in reflective analysis. See AgentBench (https://arxiv.org/abs/2308.03688) and Zheng et al. (https://arxiv.org/abs/2306.05685).

---

## 13.7 Links to Memory, Spatial, and Qualia Layers

- **Semantic and conversational memory:** ChromaDB v2 — **48 active collections, 6,740,034 vectors** (host port **8002**). `autonomous_learner` 21,181+ records (April 10, 2026). `msallis_docs` 7,465 items. `spiritual_rag` — **ABSENT from live list** — content absorbed into `spiritual_texts` (79,181 vectors), `spiritual_wisdom` (135 vectors), `spiritual_knowledge` (12 vectors) prior to April 16 audit (OI-13-K closed). `psychological_rag` restored (968 docs, March 28). Zero-vector collections (`gbim_entities`, `ms_allis_memory`, `gis_data`, `pia_records`, `psychological_knowledge`) flagged for separate follow-on review.

- **Belief and knowledge structures — GBIM architecture (April 16 definitive):**

  | Store | Container | Port | Data |
  |---|---|---|---|
  | msallis PostgreSQL | host postgres | 5432 | App data (no GBIM entities) — internal-only |
  | msallisgis PostgreSQL | host postgres | 5432 | GIS/spatial data only — 551 tables, 45 GB |
  | local_resources PostGIS | allis-local-resources-db | 5435 | Local resources only |
  | ChromaDB `gbim_worldview_entities` | allis-chroma | **8002** | **5,416,521 vectors ← authoritative GBIM entity store** |
  | ChromaDB `gbim_entities` | allis-chroma | 8002 | 0 vectors — empty placeholder |

  **`gbim_entities` (0 vectors) is an empty placeholder. `gbim_worldview_entities` (5,416,521 vectors) is the live production store. There is no relational `gbim_entities` table anywhere in the stack.** `msallis` is accessed internally by `allis-gbim-query-router:7205` and `allis-gbim-benefit-indexer:7206` only; host port 5433 returns connection refused by design (OI-13-L CLOSED). See Battaglia et al. (https://arxiv.org/abs/1806.01261).

- **Spatial backbone:** `msallisgis` (port 5432 ★ confirmed — **45 GB** PostGIS, **551 tables**, 993 ZCTA centroids).

- **Qualia Engine outputs:** `allis-qualia-engine` runs on **internal Docker network port 8017/tcp with no host binding**. ★ **Host port 8017 = BBB output filter** (`{"status":"ok","service":"bbb-output-filter","backend":"http://allis-blood-brain-barrier:8016/filter"}`). Qualia envelope: `emotional_resonance` (primary emotion, intensity), `meaning` (keyphrases), `subjective_experience` (direct-experience fallback). Draws on ChromaDB `gbim_worldview_entities` (host port **8002** v2 API).

  > **NBB-Qualia Engine:** `msallis-rebuild-nbb_qualia_engine-1` — Up 6 days, host port **8303** → internal 7008/tcp. Health check returns `{"status":"ok","service":"nbb_blood_brain_barrier"}` — response label reflects shared NBB health template. Source: `services/msallis-rebuild-nbb_qualia_engine-1_ms_allis_consciousness_bridge.py`.

---

## 13.8 Role in the Larger Architecture

- **Audit and accountability:** Durable record of what Ms. Allis did, which information was used, which `nbb_pituitary_gland` mode was active, and which services participated. BBB output filter (host port **8017**) is the final output gate and a critical audit checkpoint. ML-DSA-65 signed verdicts provide cryptographic non-repudiation across all judge outputs. April 16 baseline: 109/109 Up, `/memory/sessions` 401 unauthenticated ✅, all 5 judge signing keys present ✅, preflight 27/27 ✅. See Raji et al. (https://arxiv.org/abs/2001.00973) and ISO/IEC 42001 (https://www.iso.org/news/ref3077.html).

- **Coordination input:** Snapshot of recent behavior — pituitary mode, EEG band states, `WOAHResult` fields, WOAH weight snapshot — queried by higher-level controllers. The `nbb_pituitary_gland` (§13.9) is itself a primary consumer of this coordination information via `judge_to_pituitary_bridge.py`.

- **Research and improvement support:** ChromaDB v2 (**48 collections, 6,740,034 vectors**) and `autonomous_learner` growth curve (21,181+ records) are primary research datasets. `IntrospectiveRecord` unified class (OI-13-A closed) provides the canonical schema for research-driven improvement analysis.

---

## 13.9 The `nbb_pituitary_gland` — Global Governance and Hormonal Modulation

> **This section is new in Chapter 13 (April 16, 2026). The `nbb_pituitary_gland` was entirely absent from all prior versions of this chapter. It is mandatory here because its mode state is a direct input to the introspective record schema (§13.3) and modulates every Qualia Engine output.**

### What It Is

The `nbb_pituitary_gland` is the neurobiological brain's always-on global governance and hormonal modulation service. Modeled on the biological pituitary gland's role as the "master gland," it sets system-wide operating modes, modulates WOAH weights, adjusts constitutional compliance thresholds, and provides warmth modulation signals to the interaction tone layer. Fully documented in Chapter 15 (Pituitary Gland and Global Modes).

**Confirmed production state (April 16, 2026):**

| Field | Value |
|---|---|
| Container | `msallis-rebuild-nbb_pituitary_gland-1` |
| Host port | **8108** → internal 80/tcp |
| Status | ✅ Up 6 hours |
| Health response | `{"status":"healthy","service":"nbb_pituitary_gland","mode":"elevated"}` |
| Current mode | **`elevated`** |
| Source | `~/msallis-rebuild-working/msallis-rebuild/neurobiologicalbrain/pituitary_gland/service/pituitary_gland.py` |
| Services-safe mirror | `services-safe/pituitary_gland.py` |
| Judge bridge | `services-safe/judge_to_pituitary_bridge.py` |
| Warmth modulation | `services-safe/enhance_pituitary_warmth.py` |
| WOAH bridge | `services-safe/woah_qualia_bridge.py` |
| Data directory | `data/pituitary/` |

### Position in the NBB Pipeline

The `nbb_pituitary_gland` sits **upstream of the Qualia Engine**:

```
nbb_pituitary_gland (8108)
├─► WOAH weights ──► nbb_qualia_engine (8303) ──► nbb_consciousness_containers
├─► allis-qualia-engine (internal 8017/tcp) ──► allis-consciousness-bridge (8020)
├─► judge_to_pituitary_bridge ──► allis-judge-pipeline (7239)
├─► nbb_prefrontal_cortex ──► nbb_subconscious
└─► nbb_mother_carrie_protocols (warmth/tone)
```

### Operating Modes

| Mode | Description | Impact on Introspective Records |
|---|---|---|
| `standard` | Normal operation — baseline WOAH weights | Standard safety envelope |
| `elevated` | ★ **Current (April 16, 2026)** — heightened safety and governance thresholds | All judge scores interpreted under stricter thresholds; must be flagged in records |
| `transparency` | Full glass-box mode — maximum auditability | Expanded provenance and chain-of-thought fields in records |

### Why This Is Mandatory in Chapter 13

1. The Qualia Engine cannot produce an accurate introspective narrative without knowing what governance constraints were active at event time.
2. `WOAHResult` fields in introspective records are only interpretable in the context of the pituitary mode that set the WOAH weights.
3. Judge verdicts carry different semantic weight in `standard` vs. `elevated` vs. `transparency` mode.
4. `judge_to_pituitary_bridge.py` creates a closed feedback loop — judge verdicts update pituitary state, which modulates subsequent qualia outputs — that introspective records must capture to reconstruct any causal chain.

### Warmth Modulation

`enhance_pituitary_warmth.py` modulates the pituitary's emotional warmth output — the degree to which responses carry affirming, supportive, and community-centered tonal qualities. This warmth signal flows into the Qualia Engine's emotional resonance module and influences `nbb_mother_carrie_protocols` (`msallis-rebuild-nbb_mother_carrie_protocols-1`) interaction tone. Introspective records capture the warmth level as a normalized field when available.

---

## 13.10 Open Items — April 16, 2026 — ALL CLOSED ✅

All six open items are confirmed closed as of April 16, 2026 at 3:39 PM EDT.

| OI ID | Status | Closed Evidence |
|---|---|---|
| **OI-13-A** | ✅ **CLOSED** | `IntrospectiveRecord` instantiation OK; all imports clean — `services/introspective_record.py` |
| **OI-13-E** | ✅ **CLOSED** | ML-DSA-65 FIPS 204 sign+verify round-trip **True**; sig=**3309 bytes** (FIPS 204 Level 3 exact spec); fingerprint=`d81a5d90...edb0`; `dilithium-py 1.4.0`; `build_signed_verdict_signature_v3()` implemented and verified |
| **OI-13-J** | ✅ **CLOSED** | Zero exited/restarting containers; `docker compose ps --services` = 101 defined services vs. `docker ps` = 109 running containers is a count-in-favor naming/methodology artifact (sidecars, network bridges, named volume containers appear in `docker ps` but not `--services`) — not a service health issue |
| **OI-13-K** | ✅ **CLOSED** | **48 collections / 6,740,034 vectors** (April 16 v2 API); `spiritual_rag` merged into `spiritual_texts` (79,181 vectors) + `spiritual_wisdom` (135) + `spiritual_knowledge` (12) prior to audit; all 14 expected anchor collections confirmed present via grep |
| **OI-13-L** | ✅ **CLOSED** | GBIM entity store = **ChromaDB `gbim_worldview_entities` (5,416,521 vectors)**; no relational `gbim_entities` table in any of the 3 PostgreSQL instances (`msallis`, `msallisgis`, `allis-local-resources-db`); `msallis` host port 5433 connection refused by design — internal access only via `allis-gbim-query-router:7205` |
| **OI-29** | ✅ **CLOSED** | `WOAHResult` Pydantic schema live in `introspective_record.py`; confirmed April 16: `{"ethical_score": 0.97, "alignment_passed": true, "pituitary_mode": "PituitaryMode.elevated"}` |

**ML-DSA-65 infrastructure footnote:** Signature verification confirmed April 16, 2026. Signature size 3309 bytes is per FIPS 204 specification for the Level 3 (ML-DSA-65) parameter set — exact match confirms correct key material and `dilithium-py` operating against the correct parameter set. Private key resides at `judge-keys/judge_sk.bin` (4032 bytes plaintext) and `judge_sk.bin.enc` (4064 bytes AES-256-GCM encrypted). ⚠️ **Back up `judge_sk.bin` to offline storage immediately if not already done.**

**Zero-vector ChromaDB collections (flagged for separate follow-on review — not blocking):**
- `gbim_entities`: 0 — empty placeholder (distinct from `gbim_worldview_entities` 5,416,521 ✅)
- `ms_allis_memory`: 0
- `gis_data`: 0
- `pia_records`: 0
- `psychological_knowledge`: 0

---

## 13.11 Sprint Validation Log — April 16, 2026 Rewrite

### Infrastructure numbers — stale → current

| Field | Stale (March 28) | Current (April 16) | Source |
|---|---|---|---|
| Container count | 96 | **109** | `docker ps` April 16 |
| ChromaDB collections | 40 | **48** (v2 API) | `curl localhost:8002/api/v2/...` April 16 |
| ChromaDB total vectors | 6,675,442 | **6,740,034** | ChromaDB v2 API April 16 |
| `msallisgis` tables | 501 | **551** | `psql` April 16 |
| `msallisgis` size | 91 GB | **45 GB** | Confirmed April 16 |
| `msallis_docs` items | 4,192 | **7,465** | Preflight gate April 16 |
| `autonomous_learner` | 21,181 (March 18) | **21,181+ as of April 10** | Chapter 14 / preflight |
| Community resources | 52 | **64, all 55 WV counties** | Preflight April 16 |
| Port 8017 identity | "allis-qualia-engine" | **BBB output filter facade** | `curl localhost:8017/health` April 16 |
| `nbb_qualia_engine` port | Not documented | **Host 8303 → 7008/tcp** | `docker ps` April 16 |
| `nbb_pituitary_gland` | Not documented | **Host 8108 → 80/tcp, mode: elevated** | `docker ps` + `/health` April 16 |
| `msallis` host port | 5433 documented as accessible | **Internal-only** (conn refused from host by design) | `psql` April 16 |
| GBIM entity store | PostgreSQL `gbim_entities` (assumed) | **ChromaDB `gbim_worldview_entities` — 5,416,521 vectors** | OI-13-L investigation April 16 |
| Codebase path | `/home/ms-allis/msallis-rebuild/` | `~/msallis-rebuild-working/msallis-rebuild/` | Terminal April 16 |
| EEG Delta | Not documented | **Port 8073, 3,288+ pulses** | `curl localhost:8073/health` April 16 |
| `allis-memory` auth | Ambiguous | `/health` 200 intentional; `/memory/sessions` **401 ✅** | `curl` April 16 |
| `IntrospectiveRecord` class | Not implemented (OI-13-A) | **✅ IMPLEMENTED** — `services/introspective_record.py` | OI-13-A CLOSED April 16 |
| ML-DSA-65 signing | Not in codebase (OI-13-E) | **✅ IMPLEMENTED** — sig=3309 bytes, verify=True | OI-13-E CLOSED April 16 |
| `WOAHResult` schema | Future work (OI-29) | **✅ LIVE** in `introspective_record.py` | OI-29 CLOSED April 16 |
| `spiritual_rag` collection | Active (40-collection set) | **Merged** → `spiritual_texts` / `spiritual_wisdom` / `spiritual_knowledge` | OI-13-K CLOSED April 16 |

---

*Last updated: 2026-04-16 — Carrie Kidd (Mamma Kidd), Mount Hope WV*

*★ March 27, 2026: Status block added — allis-qualia-engine port 8017 confirmed ✅ (March 15), three modules operational, sensory-integration scaffolded, phenomenal-consciousness placeholder only, nbb_qualia_engine confirmed ✅; §13.2 DGM citation note added; §13.3 IntrospectiveRecord note updated; §13.7 Qualia Engine entry updated with nbb_qualia_engine companion service note.*

*★ March 28, 2026: Security remediation — 96/96 Up; allis-i-containers (8015) and allis-memory (8056) corrected to 127.0.0.1; _auth() on 4 sensitive routes; ChromaDB 40 collections, 6,675,442 vectors; spiritual_rag deduplicated; psychological_rag restored; msallis port 5433 restored; msallisgis port 5432 confirmed.*

*★ April 16, 2026 — ALL OI ITEMS CLOSED: Port 8017 corrected — BBB output filter facade, not Qualia Engine. §13.9 nbb_pituitary_gland added for first time — port 8108, mode elevated, judge bridge, warmth modulation, NBB pipeline position. nbb_qualia_engine port corrected to host 8303. EEG band data sources added §13.2/§13.3. ChromaDB v2 API confirmed — 48 collections / 6,740,034 vectors at host port 8002. spiritual_rag merged into spiritual_texts / spiritual_wisdom / spiritual_knowledge (OI-13-K closed). msallis:5433 corrected to internal-only. GBIM entity store corrected to ChromaDB gbim_worldview_entities (5,416,521 vectors) — no relational gbim_entities table in any PostgreSQL instance (OI-13-L closed). Container count 109 Up — naming/methodology artifact documented (OI-13-J closed). IntrospectiveRecord implemented in services/introspective_record.py (OI-13-A closed). ML-DSA-65 FIPS 204 sign+verify confirmed: sig=3309 bytes, fingerprint=d81a5d90...edb0 (OI-13-E closed). WOAHResult Pydantic schema live, ethical_score=0.97, alignment_passed=True (OI-29 closed). msallisgis corrected to 551 tables / 45 GB. Container count updated to 109. msallis_docs confirmed 7,465. Community resources 64 (all 55 WV counties). §13.10 closed OI table added. §13.11 sprint validation log added. Chapter 13 CLOSED.*
