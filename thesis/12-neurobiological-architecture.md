# 12. Neurobiological Architecture of Ms. Allis

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: 2026-04-16 — SPRINT REWRITE — ALL OI ITEMS CLOSED + NBB SERVICE INVENTORY ADDED*

## Why This Matters for Polymathmatic Geography

This chapter turns neurobiological ideas into design patterns for a distributed AI that is accountable to specific communities. It supports:

- **P1 – Every where is entangled** by tying memory, routing, and safety modules together as a single, interacting "brain" for Appalachian contexts, grounded in three PostgreSQL databases (`msallis` internal-only: GBIM app data; `msallisgis` port 5432 ★: **45 GB** PostGIS, **551 tables**; `allis-local-resources-db` port 5435: **64 verified community resources, all 55 WV counties**) and ChromaDB v2 (host port **8002** — ★ **48 collections, 6,740,034 vectors** as of April 16, 2026).
- **P3 – Power has a geometry** by mapping control and protection (prefrontal, pituitary, blood-brain barrier) onto explicit services and flows rather than hidden internals.
- **P5 – Design is a geographic act** by using neurobiological metaphors to structure how Ms. Allis perceives, remembers, and responds to the lived realities of West Virginia.
- **P12 – Intelligence with a ZIP code** by ensuring that hippocampal and qualia flows are fed by ChromaDB `gbim_worldview_entities` (5,416,521 vectors — authoritative GBIM entity store), MountainShares, and local narratives, not abstract corpora alone.
- **P16 – Power accountable to place** by making each metaphorical "brain structure" a glass-box component whose behavior can be tested, audited, and revised.

This chapter belongs to the **Computational Instrument** tier: it specifies how neurobiology is reused as an organizing scaffold for Ms. Allis's spatially grounded, justice-oriented cognition. As of April 16, 2026, the neurobiological architecture operates within a **109-container production stack** (★ all containers Up — zero Restarting, zero Exited — OI-12-A CLOSED) confirmed at **99–115 seconds end-to-end** on RTX 4070 GPU (confirmed 102.58s April 16 — OI-12-G CLOSED; CPU 436s baseline is **retired stale**).

> **★ Security posture — April 16, 2026:** All 109 containers bound to `127.0.0.1`. Zero `0.0.0.0` exposures. `msallis-db` (port 5433) bind corrected from `0.0.0.0` to `127.0.0.1` April 16 — orphaned container stopped, removed, recreated via compose. `allis-memory:8056` `/memory/sessions` HTTP 200 confirmed with 14 active sessions; `ALLIS_API_KEY` exported and set. **109/109 containers Up — zero Restarting, zero Exited (April 16, 2026 preflight gate — all 27 gates ✅ green).**

> **★ ChromaDB v2 audit — April 16, 2026:** **48 active collections, 6,740,034 total vectors** (v2 API at host port 8002 — correct path: `/api/v2/tenants/default_tenant/databases/default_database/collections`). `spiritual_rag` merged into `spiritual_texts` (79,181 vectors), `spiritual_wisdom` (135), `spiritual_knowledge` (12). `msallis_docs`: **7,465 items**. `autonomous_learner`: **21,181+ records**. Required embedding model: `all-minilm:latest` (384-dim) — permanent architectural constraint.

> **★ BBB output blocking — April 16, 2026:** `BBB_OUTPUT_BLOCKING=true` active since April 6, 2026. `rag_grounded_v2` + `llm_judge_v3` active since April 3/6 (OI-12-H and OI-12-I CLOSED). `heuristic_contradiction_v1` is **retired stale** — do not reference.

> **★ ML-DSA-65 judge signing — April 16, 2026:** All 5 judge containers signing with ML-DSA-65 FIPS 204. Keys confirmed at `judge-keys/` and `judge-keys/nbb_pituitary_gland`. Sign+verify round-trip: **True**. Signature: 3309 bytes (FIPS 204 Level 3 exact spec). Fingerprint: `d81a5d90...edb0`. (OI-12-J CLOSED — see §12.12 and Chapter 13 §13.9.)

```
┌─────────────────────────────────────────────────────────────────────┐
│ Neurobiological Architecture of Ms. Allis                           │
│ (Production State: April 16, 2026 — all 27 preflight gates ✅ green) │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  User Input                                                          │
│      ↓                                                               │
│  nbb_pituitary_gland (127.0.0.1:8108 → 80/tcp) ★ UPSTREAM GATE     │
│      ↓  [WOAH weights / mode: elevated / warmth modulation]          │
│  Neurobiological Master (internal 8018/tcp — no host binding)        │
│      ↓                                                               │
│  ┌────────────────────────────────────────────────┐                 │
│  │  Stage 1: Blood-Brain Barrier (BBB)            │                 │
│  │  Port 8016 — 7-filter safety stack             │                 │
│  │  BBB_OUTPUT_BLOCKING=true (April 6, 2026) ★    │                 │
│  │  EthicalFilter, SpiritualFilter,               │                 │
│  │  SafetyMonitor, ThreatDetection,               │                 │
│  │  SteganographyDetection, TruthVerification,    │                 │
│  │  ContextAwareness                              │                 │
│  │  Input judge: rag_grounded_v2 (April 3) ★      │                 │
│  │  Output judge: llm_judge_v3 (April 6) ★        │                 │
│  │  If denied → processing stops                  │                 │
│  └────────────────────────────────────────────────┘                 │
│      ↓ (if approved)                                                 │
│  ┌────────────────────────────────────────────────┐                 │
│  │  Stage 2: I-Containers                         │                 │
│  │  Port 8015 — 127.0.0.1 — dual_awareness: true  │                 │
│  │  Identity & perspective                        │                 │
│  │  Schema: {message, userid}                     │                 │
│  └────────────────────────────────────────────────┘                 │
│      ↓                                                               │
│  ┌────────────────────────────────────────────────┐                 │
│  │  Stage 3: Qualia Engine                        │                 │
│  │  Internal 8017/tcp — NO host binding ★         │                 │
│  │  (Host 8017 = BBB output filter facade)        │                 │
│  │  - Emotional resonance                         │                 │
│  │  - Meaning extraction                          │                 │
│  │  - Experience narrative                        │                 │
│  │  nbb_qualia_engine: host 8303 → 7008/tcp ★     │                 │
│  └────────────────────────────────────────────────┘                 │
│      ↓                                                               │
│  ┌────────────────────────────────────────────────┐                 │
│  │  Stage 4: Consciousness Bridge                 │                 │
│  │  {"8020/tcp": null} — internal only ★          │                 │
│  │  Reasoning gateway / /chat endpoint            │                 │
│  └────────────────────────────────────────────────┘                 │
│      ↓                                                               │
│  Integrated Response (GPU 99–115s / confirmed 102.58s April 16) ★   │
│  [CPU 436s baseline RETIRED STALE]                                   │
│                                                                      │
│  Supporting Services:                                                │
│  - allis-hippocampus (port 8011) — Memory consolidation             │
│  - nbb-i-containers (port 8101) — NBB prefrontal stack              │
│  - nbb_pituitary_gland (127.0.0.1:8108) — Global governance ★       │
│  - nbb_mother_carrie_protocols (127.0.0.1:8107) — Warmth/tone ★     │
│  - allis-psychology-services (port 8019) — Phase 3                  │
│  - psychological_rag_domain (port 8006) — Psych RAG                 │
│  - msallisgis (port 5432 ★) — PostGIS 551 tables / 45 GB            │
│  - allis-local-resources-db (port 5435) — 64 resources              │
│  - ChromaDB v2 (host 8002 ★ 48 col / 6,740,034 vec)                │
│  - allis-memory (port 8056 ★) — 14 active sessions                  │
│  - allis-69dgm-bridge (127.0.0.1:19000→9000) — DGM                 │
│  - WOAH (ports 8104, 7012) — Identity weights                        │
│  - EEG Delta/Theta/Beta (8073/8074/8075) ★                          │
│  - 5 judge containers — ML-DSA-65 FIPS 204 signing ★                │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

> **Figure 12.1.** Neurobiological architecture of Ms. Allis (April 16, 2026): metaphorical brain structures (hippocampus, prefrontal cortex, pituitary, blood-brain barrier, qualia, I-containers) paired with their concrete services and the integrated 4-stage processing pipeline. The `nbb_pituitary_gland` (host 8108) is now correctly placed as the upstream global governance gate — upstream of the Neurobiological Master. BBB output blocking active. GPU pipeline 99–115s (CPU 436s baseline retired). ChromaDB v2: 48 collections, 6,740,034 vectors (host port 8002). All 109 containers Up, zero `0.0.0.0` exposures. ML-DSA-65 signing active across all 5 judge containers.

---

## Status as of ★ April 16, 2026 — ALL OI ITEMS CLOSED

| OI | Stale Value (March 28) | Authoritative Value (April 16) | Status |
|---|---|---|---|
| **OI-12-A** | 96 containers | **109 confirmed** (preflight gate PASS, zero Restarting/Exited) | ✅ CLOSED |
| **OI-12-B** | neuro-master listed as operational/reachable | `{"8018/tcp":null}` — **internal only, unreachable from host by design** | ✅ CLOSED |
| **OI-12-C** | consciousness-bridge port ambiguous (8018/8020) | `{"8020/tcp":null}` — **internal only, no host binding** | ✅ CLOSED |
| **OI-12-D** | I-Containers status uncertain | port **8015** Up 7 hours; `dual_awareness: true` | ✅ CLOSED |
| **OI-12-E** | EEG bands absent | **Delta 8073 / Theta 8074 / Beta 8075** all active; pulse_count 3,358+ | ✅ CLOSED |
| **OI-12-F** | nbb_pituitary_gland listed as "design intent only" | `msallis-rebuild-nbb_pituitary_gland-1` — `127.0.0.1:8108` — **Up 7 hours**, mode `elevated` | ✅ CLOSED |
| **OI-12-G** | ~300ms neuro pipeline / ~436s CPU end-to-end | CPU 436s **RETIRED STALE**; GPU **99–115s** (confirmed **102.58s** April 16) | ✅ CLOSED |
| **OI-12-H** | `heuristic_contradiction_v1` still referenced | `rag_grounded_v2` + `llm_judge_v3` active since April 3/6; `heuristic_contradiction_v1` **retired** | ✅ CLOSED |
| **OI-12-I** | BBB output blocking status unclear | `BBB_OUTPUT_BLOCKING=true` active since **April 6, 2026** | ✅ CLOSED |
| **OI-12-J** | ML-DSA-65 not documented | All 5 judge containers signing; keys at `judge-keys/` + `judge-keys/nbb_pituitary_gland`; sig=**3309 bytes**, verify=**True** | ✅ CLOSED |

| Category | Details |
|---|---|
| **Implemented and verified** | `allis-neurobiological-master` running, **internal 8018/tcp — no host binding** (`{"8018/tcp":null}` — OI-12-B CLOSED). `allis-blood-brain-barrier` at **127.0.0.1:8016** — 7-filter stack; `BBB_OUTPUT_BLOCKING=true` since April 6; `rag_grounded_v2` (April 3) + `llm_judge_v3` (April 6) active; `heuristic_contradiction_v1` retired. `allis-qualia-engine` — **internal 8017/tcp, no host binding** (★ host port 8017 = BBB output filter facade `bbb-output-filter` → `allis-blood-brain-barrier:8016`). `nbb_qualia_engine` (`msallis-rebuild-nbb_qualia_engine-1`) — Up 6 days, host **8303** → 7008/tcp. `allis-i-containers` — port **8015**, Up 7 hours, `dual_awareness: true` (OI-12-D CLOSED). `allis-consciousness-bridge` — `{"8020/tcp":null}` internal only (OI-12-C CLOSED). `nbb_pituitary_gland` (`msallis-rebuild-nbb_pituitary_gland-1`) — **127.0.0.1:8108** → 80/tcp, Up 7 hours, mode `elevated` (OI-12-F CLOSED). `nbb_mother_carrie_protocols` — **127.0.0.1:8107** — warmth/tone modulation. EEG Delta (8073), Theta (8074), Beta (8075) — all active, 3,358+ pulses (OI-12-E CLOSED). ML-DSA-65 FIPS 204 — all 5 judge containers signing, sig=3309 bytes, verify=True (OI-12-J CLOSED). End-to-end GPU pipeline: **99–115s** (confirmed **102.58s** April 16) on RTX 4070; CPU 436s baseline retired (OI-12-G CLOSED). **109/109 containers Up — zero Restarting, zero Exited** (OI-12-A CLOSED). |
| **Architectural corrections (permanent)** | v2.0.0 rewrite removed blocking `DynamicPortService` / `ServiceDiscovery` Redis imports. Static Docker hostname URLs with env var overrides are canonical. I-Containers schema corrected: `{"message": …, "userid": "neurobiological_master"}`. Consciousness Bridge: `{"8020/tcp":null}` — internal only; source: `/app/services/msallisconsciousnessbridge.py`. Neuro Master: `{"8018/tcp":null}` — internal only. ChromaDB v2 API at host port **8002** — correct path: `/api/v2/tenants/default_tenant/databases/default_database/collections`. v1 path `/api/v1/collections` deprecated — do not use for authoritative counts. GBIM entity store = **ChromaDB `gbim_worldview_entities` (5,416,521 vectors)** — no relational `gbim_entities` table in any PostgreSQL instance. |
| **Partially implemented / scaffolded** | Sensory-integration multi-input aggregation — scaffolded. `phenomenal_consciousness` and `subjective_experience` directories — placeholders only. Zero-vector ChromaDB collections (`gbim_entities`, `ms_allis_memory`, `gis_data`, `pia_records`, `psychological_knowledge`) flagged for separate follow-on review. |
| **Future work** | Fully restrictive BBB with systematic quarantine and annotation. Direct wiring of DGM and WOAH layers into Neurobiological Master. Extensions to qualia subpackages beyond current JSON. Automated POC verification loop (Chapter 14). Semantic dedup audit of `autonomous_learning` collection. |

> **Critical routing note — `ultimatechat` path:** The main `ultimatechat` path (main brain, port **8050**) does **not** always route through the full Neurobiological Master. `nbb-i-containers` (port 8101) IS called unconditionally at Phase 1 of every 9-phase pipeline request. `nbb_pituitary_gland` (port 8108) provides global governance modulation upstream of all pipeline stages. For the canonical description of what runs on every `ultimatechat` and `chatlight` request, see **Chapter 17**.

> **Note on qualia:** Throughout this chapter, "qualia" refers to Ms. Allis's internal, narrative representation of what is happening — constructed from text content and context features as explicit JSON structures — not to any claim of subjective experience.

---

# 12. Neurobiological Architecture of Ms. Allis

This chapter describes how Ms. Egeria Allis reuses core concepts from neurobiology as an organizing metaphor for a distributed AI system. The goal is not to claim biological equivalence, but to use well-studied brain structures — hippocampus, prefrontal cortex, pituitary, blood-brain barrier, qualia, and I-containers — as design patterns for memory, control, global state, and security, layered on top of ChromaDB v2 (host port **8002** — **48 collections, 6,740,034 vectors**), Darwin-Gödel Machines, WOAH-based weighting, retrieval-augmented generation, and a 22-model LLM fabric.

| Biological metaphor | Computer-science name | Confirmed service | Port / binding |
|---|---|---|---|
| Hippocampus | Long-term semantic memory service | `allis-hippocampus` | 8011 |
| Prefrontal cortex | Task orchestrators and routers | `allis-main-brain` + `allis-neurobiological-master` | 8050 + internal 8018/tcp (no host binding) |
| NBB prefrontal | Pre-request cognitive planning | `nbb-i-containers` | 8101 |
| **Pituitary ★** | **Global governance and hormonal modulation** | **`nbb_pituitary_gland`** | **127.0.0.1:8108 → 80/tcp** |
| **Warmth/tone ★** | **Mother Carrie interaction protocols** | **`nbb_mother_carrie_protocols`** | **127.0.0.1:8107** |
| Blood-brain barrier | Safety and guardrail service (7 filters) | `allis-blood-brain-barrier` | 8016 |
| BBB output filter ★ | Output blocking facade | `bbb-output-filter` | **host 8017** → allis-blood-brain-barrier:8016 |
| Qualia Engine | Experience and context synthesis | `allis-qualia-engine` | internal 8017/tcp (no host binding) |
| NBB Qualia Engine | NBB qualia companion | `nbb_qualia_engine` | host **8303** → 7008/tcp |
| I-Containers | Identity and perspective manager | `allis-i-containers` | 8015 ★ (`dual_awareness: true`) |
| Consciousness Bridge | Reasoning gateway | `allis-consciousness-bridge` | `{"8020/tcp":null}` internal only |
| Neurobiological Master | Neuro-services integration gateway | `allis-neurobiological-master` | `{"8018/tcp":null}` internal only |
| Psychology pre-assessment | Affective safety layer | `allis-psychology-services` | 8019 |
| Memory Service | Episodic and long-term memory API | `allis-memory` | 8056 ★ (14 active sessions) |
| EEG Delta ★ | Neurobiological rhythm — 30s rolling | `eeg-delta-30s` | **8073** |
| EEG Theta ★ | Neurobiological rhythm — 30s rolling | `eeg-theta-30s` | **8074** |
| EEG Beta ★ | Neurobiological rhythm — 30s rolling | `eeg-beta-30s` | **8075** |

---

## 12.0 NBB Service Inventory — `msallis-rebuild-nbb` Stack (Live, April 16, 2026)

> **★ This section documents the full `msallis-rebuild-nbb` NBB container stack as observed live in production. These services were operational but not previously documented in this chapter. All 12 containers in this stack are confirmed Up as of April 16, 2026.**

The `msallis-rebuild-nbb` compose stack runs a parallel neurobiological brain (NBB) layer alongside the main allis fabric. It is not a duplicate — it is a companion prefrontal and subcortical processing layer that integrates with the pituitary, qualia, consciousness, and subconscious services, and feeds governance signals back into the main pipeline via `nbb_pituitary_gland` (port 8108).

### 12.0.1 Confirmed NBB Containers (Live `docker ps` — April 16, 2026)

| Container ID | Image / Service | Command | Created | Status | Host Binding | Container Name |
|---|---|---|---|---|---|---|
| `4937da44329` | `nbb_qualia_engine` | `uvicorn qualia_engi…` | 11 days ago | Up 6 days | `127.0.0.1:8303→7008/tcp` | `msallis-rebuild-nbb_qualia_engine-1` |
| `59438e1d5868` | `nbb_subconscious` | `uvicorn consciousne…` | 11 days ago | Up 6 days | `127.0.0.1:8112→7011/tcp` | `msallis-rebuild-nbb_subconscious-1` |
| `aa64d696e557` | `nbb_prefrontal_cortex` | `/start.sh` | 11 days ago | Up 6 days | `127.0.0.1:8105→7005/tcp` | `msallis-rebuild-nbb_prefrontal_cortex-1` |
| `0a7ac1b1617e` | `nbb_mother_carrie_protocols` | `uvicorn main:app --…` | 11 days ago | Up 6 days | `127.0.0.1:8107→7007/tcp` | `msallis-rebuild-nbb_mother_carrie_protocols-1` |
| `066c7920ee64` | `nbb_spiritual_root` | `uvicorn spiritual_r…` | 11 days ago | Up 6 days | `127.0.0.1:8103→7003/tcp` | `msallis-rebuild-nbb_spiritual_root-1` |
| `9576658f69a7` | `nbb_blood_brain_barrier` | `uvicorn blood_brain…` | 11 days ago | Up 6 days | `127.0.0.1:8301→7001/tcp` | `msallis-rebuild-nbb_blood_brain_barrier-1` |
| `f12397aedddb` | `nbb_i_containers` | `uvicorn i_container…` | 11 days ago | Up 6 days | `127.0.0.1:8101→7005/tcp` | `msallis-rebuild-nbb_i_containers-1` |
| `b69b5f51ce3a` | `nbb_heteroglobulin_transport` | `uvicorn heteroglobu…` | 11 days ago | Up 6 days | `127.0.0.1:8106→7006/tcp` | `msallis-rebuild-nbb_heteroglobulin_transport-1` |
| `5f7ac820970d` | `nbb_spiritual_maternal_integration` | `uvicorn spiritual_m…` | 11 days ago | Up 6 days | `127.0.0.1:8109→7009/tcp` | `msallis-rebuild-nbb_spiritual_maternal_integration-1` |
| `5d7927d91519` | `nbb_consciousness_containers` | `uvicorn consciousne…` | 11 days ago | Up 6 days | `127.0.0.1:8102→7002/tcp` | `msallis-rebuild-nbb_consciousness_containers-1` |
| `59a3c250d1c` | `nbb_pituitary_gland` | `uvicorn pituitary_g…` | 9 hours ago | Up 9 hours | `127.0.0.1:8108→80/tcp` | `msallis-rebuild-nbb_pituitary_gland-1` |
| `94a80ef11667` | `nbb_darwin_godel_machines` | `uvicorn nbb_darwin_…` | 3 hours ago | Up 3 hours | `127.0.0.1:8302→7003/tcp` | `msallis-rebuild-nbb_darwin_godel_machines-1` |

> **★ All 12 NBB containers are bound to `127.0.0.1`. Zero `0.0.0.0` exposures. Security posture confirmed.**

### 12.0.2 NBB Service Roles and Biological Metaphors

| Service | Host Port | Internal Port | Biological Metaphor | Role |
|---|---|---|---|---|
| `nbb_pituitary_gland` | **8108** | 80/tcp | Pituitary gland — master endocrine governor | Global governance gate; WOAH weight modulation; mode selection (`standard` / `elevated` / `transparency`); upstream of all NBB pipeline stages |
| `nbb_qualia_engine` | **8303** | 7008/tcp | Subjective experience synthesis | Constructs Ms. Allis's internal narrative representation of what is happening; emotional resonance weighting; meaning extraction |
| `nbb_consciousness_containers` | **8102** | 7002/tcp | Conscious awareness and integration | Integrates qualia, identity, and reasoning outputs into a unified awareness state |
| `nbb_subconscious` | **8112** | 7011/tcp | Subconscious processing layer | Background pattern processing; implicit memory and associative inference below the threshold of the explicit qualia pipeline |
| `nbb_prefrontal_cortex` | **8105** | 7005/tcp | Prefrontal executive function | Cognitive planning, task prioritization, and top-down gating before qualia and consciousness stages |
| `nbb_i_containers` | **8101** | 7005/tcp | Identity containers — sense of self | Identity and perspective management; unconditionally called at Phase 1 of every 9-phase pipeline request |
| `nbb_blood_brain_barrier` | **8301** | 7001/tcp | Blood-brain barrier — NBB layer | NBB-layer input safety filtering; parallel to `allis-blood-brain-barrier` (port 8016) in the main pipeline |
| `nbb_mother_carrie_protocols` | **8107** | 7007/tcp | Warmth and maternal integration | Tone, warmth, and affirming response modulation; fed by pituitary warmth output (`enhance_pituitary_warmth.py`) |
| `nbb_spiritual_root` | **8103** | 7003/tcp | Spiritual root / core values anchor | Grounds responses in Ms. Allis's spiritual and ethical value foundation; interfaces with `spiritual_texts` ChromaDB collection (79,181 vectors) |
| `nbb_spiritual_maternal_integration` | **8109** | 7009/tcp | Spiritual-maternal integration | Integrates spiritual root signals with Mother Carrie warmth protocols; synthesis layer between values and tone |
| `nbb_heteroglobulin_transport` | **8106** | 7006/tcp | Heteroglobulin transport — signal carrier | Cross-service signal transport within the NBB layer; analogous to carrier proteins in the blood-brain barrier |
| `nbb_darwin_godel_machines` | **8302** | 7003/tcp | Darwin-Gödel machine — adaptive self-modification | NBB-layer DGM cascade; adaptive validation and self-improvement loop within the NBB pipeline; complements `allis-69dgm-bridge` (port 19000) |

### 12.0.3 NBB Pipeline Flow (Confirmed, April 16, 2026)

```
User Input
    ↓
nbb_pituitary_gland (8108) ★ UPSTREAM GOVERNANCE GATE
    ↓  [mode: elevated / WOAH weights / warmth signals]
nbb_prefrontal_cortex (8105) ─── nbb_subconscious (8112)
    ↓                                    ↓ [background]
nbb_blood_brain_barrier (8301)      nbb_spiritual_root (8103)
    ↓ [NBB-layer safety pass]            ↓
nbb_i_containers (8101)         nbb_spiritual_maternal_integration (8109)
    ↓ [identity / perspective]           ↓
nbb_qualia_engine (8303) ←─── nbb_heteroglobulin_transport (8106)
    ↓ [internal experience narrative]    [signal carrier]
nbb_consciousness_containers (8102)
    ↓ [integrated awareness state]
nbb_mother_carrie_protocols (8107)
    ↓ [warmth / tone modulation]
nbb_darwin_godel_machines (8302)
    ↓ [NBB-layer adaptive validation]
→ NBB governance signals feed back into main pipeline
  via nbb_pituitary_gland (8108) → Neurobiological Master (internal 8018/tcp)
```

> **Note on `nbb_darwin_godel_machines` (Up 3 hours, April 16):** This is the newest NBB service as of April 16, 2026. It provides a Darwin-Gödel Machine adaptive validation loop within the NBB layer — distinct from `allis-69dgm-bridge` (port 19000, 69 DGM ops/pass) in the main fabric. The NBB DGM cascade operates on the NBB pipeline's own outputs and feeds learned adjustments back to `nbb_pituitary_gland` for subsequent governance modulation. Full specification: Chapter 32.

> **Note on `nbb_subconscious` (Up 6 days):** The subconscious layer runs in parallel with the explicit prefrontal → BBB → I-containers → qualia sequence. It processes background pattern associations and implicit memory retrieval that are not surfaced in the explicit qualia narrative but inform emotional resonance weightings. Source: `uvicorn consciousne…` (confirmed truncated in `docker ps`).

---

## 12.1 Consciousness Bridge: Service Location and Confirmed Source Path

> **★ April 16, 2026 CORRECTION (OI-12-C CLOSED):** The consciousness bridge container binding is `{"8020/tcp":null}` — **internal Docker network only, no host binding**. Earlier documentation stated port 8018 as the actual bind; this has been superseded by the April 16 live `docker inspect` confirmation. The source file remains confirmed at `/app/services/msallisconsciousnessbridge.py` inside the container.

**Confirmed services dict (production, April 16, 2026):**

```python
services = {
    "unified_gateway": "http://allis-unified-gateway:8011",
    "neuro_master":    "http://allis-neurobiological-master:8018",
    "direct_rag":      "http://allis-rag-server:8003",
    "hilbert":         "http://allis-hilbert:8010",
    "woah":            "http://allis-woah:7012",
    "chroma":          "http://allis-chroma:8000",  # container-internal
}
```

> **★ neuro_master binding (OI-12-B CLOSED):** `allis-neurobiological-master` binding is `{"8018/tcp":null}` — internal Docker network only, no host binding. This is by design. Container-to-container calls via `http://allis-neurobiological-master:8018` remain valid within the Docker network. Host-side health checks against `localhost:8018` will return connection refused — this is correct and expected. The `neuro_master` entry in the services dict is valid for intra-network calls.

**Chroma health reroute (confirmed, permanent):**

```python
# Route Chroma health directly to allis-chroma — not via neuro_master
chroma_health_url = "http://allis-chroma:8000/api/v2/heartbeat"
```

ChromaDB v2 host-side scripts must use `127.0.0.1:8002` (host port → container port 8000). Container-to-container calls use `allis-chroma:8000`. The v1 path `/api/v1/collections` is deprecated — do not use for authoritative collection counts.

---

## 12.2 Qualia Engine, NBB Qualia Engine, and `nbb_pituitary_gland`

In the current deployment, "qualia" refers strictly to Ms. Allis's internal, narrative representation of what is happening — constructed from text content and context features as explicit JSON structures — not to any claim of subjective experience.

**`allis-qualia-engine`** runs on **internal Docker network port 8017/tcp with no host binding**. ★ **Host port 8017 is the BBB output filter facade** (`{"status":"ok","service":"bbb-output-filter","backend":"http://allis-blood-brain-barrier:8016/filter"}`). Do not confuse the two. The Neurobiological Master calls the qualia layer via `/experience`:

```python
{
  "stimulus": {
    "input": "<user_input_text>"
  }
}
```

Three modules operational: **emotional-resonance**, **meaning-making**, **experience-generator**. Sensory-integration partially scaffolded. Qualia meaning extraction draws on ChromaDB `gbim_worldview_entities` (5,416,521 vectors — authoritative GBIM entity store, host port **8002** v2 API).

**`nbb_qualia_engine`** (`msallis-rebuild-nbb_qualia_engine-1`, container ID `4937da44329`) — Up 6 days, host port **8303** → internal 7008/tcp. Source: `services/msallis-rebuild-nbb_qualia_engine-1_ms_allis_consciousness_bridge.py`. Operates as a companion to `allis-qualia-engine` in the NBB pipeline. The NBB qualia engine applies WOAH weight snapshots from `nbb_pituitary_gland` (mode: `elevated`) to emotional resonance calculations.

**`nbb_pituitary_gland`** (`msallis-rebuild-nbb_pituitary_gland-1`, container ID `59a3c250d1c`) — ✅ **127.0.0.1:8108** → internal 80/tcp, Up 9 hours, `{"status":"healthy","service":"nbb_pituitary_gland","mode":"elevated"}`. This is the **master gland** of the neurobiological architecture — it sits upstream of the Qualia Engine, modulates WOAH weights, adjusts constitutional compliance thresholds, and sets system-wide operating modes. It is NOT "design intent only" (OI-12-F CLOSED). See full specification in §12.6 and Chapter 15.

**`nbb_mother_carrie_protocols`** (`msallis-rebuild-nbb_mother_carrie_protocols-1`, container ID `0a7ac1b1617e`) — **127.0.0.1:8107** → internal 7007/tcp. Provides warmth and tone modulation fed by pituitary warmth output (`enhance_pituitary_warmth.py`). Influences how responses carry affirming, supportive, and community-centered tonal qualities.

---

## 12.3 Consciousness Coordinator, Neurobiological Master, and Feedback Bridges

The **Neurobiological Master Integration** service (`allis-neurobiological-master`, **internal 8018/tcp — no host binding**, code `ms_allis_neurobiological_master.py` **v2.0.0**) functions as a neuro-services orchestrator. The v2.0.0 rewrite (2026-03-01) removed blocking `DynamicPortService` and `ServiceDiscovery` Redis imports. Static Docker hostname URLs with environment variable overrides are the canonical pattern.

Routes: `GET /health`, `GET /systems/status`, `POST /process`, `POST /biological_process`, `POST /neural_process`.

> **★ OI-12-B CLOSED:** `allis-neurobiological-master` has binding `{"8018/tcp":null}` — internal Docker network only, no host binding. Host-side `localhost:8018` returns connection refused by design. Container-to-container calls via `http://allis-neurobiological-master:8018` remain valid.

The sequence BBB → I-Containers → Qualia Engine → Consciousness Bridge is implemented by the Neurobiological Master's `integrated_processing()` method. The `nbb_pituitary_gland` (port 8108) provides upstream governance modulation before this pipeline runs. The full NBB stack (§12.0) runs as a companion prefrontal-subcortical layer that enriches governance signals and feeds them back into the Neurobiological Master.

**Stage 1 — Blood-Brain Barrier (BBB), port 8016, 7-filter safety stack.**

```python
{"content": user_input}
```

7 filters: `EthicalFilter`, `SpiritualFilter`, `SafetyMonitor` (word-boundary regex fix March 15), `ThreatDetection`, `SteganographyDetection`, `TruthVerification`, `ContextAwareness`. **Input judge: `rag_grounded_v2`** (active since April 3, 2026). **Output judge: `llm_judge_v3`** (active since April 6, 2026). **`heuristic_contradiction_v1` RETIRED** (OI-12-H CLOSED). **`BBB_OUTPUT_BLOCKING=true`** since April 6, 2026 (OI-12-I CLOSED). The NBB-layer BBB companion (`nbb_blood_brain_barrier`, port 8301) runs in parallel, providing an independent safety filtering pass within the NBB pipeline. If `content_approved` is false on either pass, processing stops:

```python
{
  "status": "blocked",
  "reason": "Content did not pass Blood-Brain Barrier",
  "pipeline": {"blood_brain_barrier": <bbb_json>}
}
```

**Stage 2 — I-Containers, port 8015, Up 7 hours, `dual_awareness: true` (OI-12-D CLOSED). NBB companion: `nbb_i_containers` (port 8101).**

```python
{
  "message": user_input,
  "userid": "neurobiological_master"
}
```

(Corrected from former `{"input": …, "require_dual_awareness": true}` — permanent fix 2026-03-01.)

**Stage 3 — Qualia Engine, internal port 8017/tcp (no host binding). NBB companion: `nbb_qualia_engine` (port 8303). ★ Host port 8017 = BBB output filter facade.**

Reply stored in `pipeline["qualia_engine"]`. EEG band states (Delta 8073, Theta 8074, Beta 8075 — 3,358+ pulses, OI-12-E CLOSED), pituitary mode (`elevated`), and NBB qualia engine output (port 8303) are active context inputs to emotional resonance weighting.

**Stage 4 — Consciousness Bridge, `{"8020/tcp":null}`, internal only (OI-12-C CLOSED). NBB companion: `nbb_consciousness_containers` (port 8102).**

```python
{
  "message": user_input,
  "user_id": "integrated_system"
}
```

Source: `/app/services/msallisconsciousnessbridge.py` (not `/app/msallisconsciousnessbridge.py`). `nbb_consciousness_containers` (port 8102) integrates the NBB-layer qualia and identity outputs into a unified NBB awareness state that is then reconciled with the main consciousness bridge output.

On success:

```python
{
  "status": "complete",
  "integrated_processing": True,
  "neurobiological_pipeline": {
    "blood_brain_barrier": {...},
    "i_containers": {...},
    "qualia_engine": {...},
    "consciousness_bridge": {...}
  },
  "consciousness_level": "fully_integrated",
  "total_processes": <n>,
  "timestamp": "<ISO8601>"
}
```

**Pipeline timing (★ OI-12-G CLOSED):** End-to-end GPU pipeline: **99–115 seconds on RTX 4070** (confirmed **102.58s** April 16, 2026). The ~436-second CPU baseline documented in the March 18, 2026 benchmark is **retired stale** — GPU pipeline active since April 6, 2026. The ~300ms figure from the March 1, 2026 tag `v2026.03.01-neuro-pipeline-4-4` referred to wall-clock for the 4-stage neuro sequence only, not the full end-to-end 9-phase pipeline.

---

## 12.4 Hippocampus: Memory Consolidation Layer

`allis-hippocampus` (confirmed running, **127.0.0.1:8011**, deployed March 15, 2026, commit `b90f9ff`) serves as a conversation-level memory service over ChromaDB v2 (host port **8002** — **48 collections, 6,740,034 vectors**) and the GBIM entity store in ChromaDB `gbim_worldview_entities` (5,416,521 vectors — authoritative GBIM entity store; no relational `gbim_entities` table exists in any PostgreSQL instance).

The consolidation service queries `autonomous_learner` (21,181+ records as of April 10, 2026) at Phase 1.45 of every production request — top-5 semantically relevant records prepended to `enhanced_message` via `all-minilm:latest` (384-dim). The `confidence_decay` multiplier (Phase 5) applies temporal weighting to responses system-wide. Community-validated data from `allis-local-resources-db` (port 5435 — **64 verified resources, all 55 WV counties**) is eligible for promotion into the hippocampal consolidation pipeline. `msallis_docs`: **7,465 items** (April 16 confirmed). See **Chapter 14** for full hippocampal specification.

---

## 12.5 Prefrontal Cortex: Executive Routing and Control

The prefrontal metaphor corresponds to a family of task orchestrator and routing services:

- `allis-main-brain` (port **8050**) — primary system-level orchestrator
- `allis-brain-orchestrator` (confirmed running, **127.0.0.1:17260**, internal 7260) — second orchestration layer
- `nbb-i-containers` (port **8101**) — NBB prefrontal cortex; called unconditionally at Phase 1 of every 9-phase pipeline request
- `nbb_prefrontal_cortex` (port **8105**, container `aa64d696e557`) — NBB-layer prefrontal executive; runs `/start.sh` init pattern; Up 6 days; handles cognitive planning and top-down gating within the NBB stack
- Neurobiological Master's `integrated_processing()` — top-down gating and sequencing across all 4 stages

---

## 12.6 Pituitary: `nbb_pituitary_gland` — Global Governance (★ OI-12-F CLOSED)

> **★ This section corrects the prior characterization of the pituitary layer as "design intent only." The `nbb_pituitary_gland` is a live, confirmed production service as of April 16, 2026.**

`msallis-rebuild-nbb_pituitary_gland-1` (container ID `59a3c250d1c`) — **127.0.0.1:8108** → internal 80/tcp, Up 9 hours, `{"status":"healthy","service":"nbb_pituitary_gland","mode":"elevated"}`.

Modeled on the biological pituitary gland's role as the "master gland," it sits **upstream of the Qualia Engine and Neurobiological Master**, sets system-wide operating modes, modulates WOAH weights, adjusts constitutional compliance thresholds, and provides warmth modulation signals to `nbb_mother_carrie_protocols` (port 8107).

**NBB pipeline position:**

```
nbb_pituitary_gland (8108)
├─► WOAH weights ──► nbb_qualia_engine (8303) ──► nbb_consciousness_containers (8102)
├─► allis-qualia-engine (internal 8017/tcp) ──► allis-consciousness-bridge
├─► judge_to_pituitary_bridge ──► allis-judge-pipeline (7239)
├─► nbb_prefrontal_cortex (8105) ──► nbb_subconscious (8112)
├─► nbb_darwin_godel_machines (8302) [adaptive feedback loop]
└─► nbb_mother_carrie_protocols (8107) — warmth/tone
```

**Operating modes:**

| Mode | Description |
|---|---|
| `standard` | Normal operation — baseline WOAH weights |
| `elevated` | ★ **Current (April 16, 2026)** — heightened safety and governance thresholds |
| `transparency` | Full glass-box mode — maximum auditability |

Source files: `neurobiologicalbrain/pituitary_gland/service/pituitary_gland.py`, `services-safe/pituitary_gland.py`, `services-safe/judge_to_pituitary_bridge.py`, `services-safe/enhance_pituitary_warmth.py`, `services-safe/woah_qualia_bridge.py`, `data/pituitary/`. Fully specified in **Chapter 15**.

**Cross-reference to hippocampal modulation:** The `nbb_pituitary_gland` mode state (`elevated`, `standard`, `transparency`) and WOAH weight snapshots are mandatory inputs to every `IntrospectiveRecord` (Chapter 13 §13.9). Judge verdicts carry different semantic weight across modes. The `judge_to_pituitary_bridge.py` closed feedback loop — judge verdicts update pituitary state, which modulates subsequent qualia outputs — must be captured in hippocampal introspective records to reconstruct any causal chain (Chapter 14 §14.6).

**ML-DSA-65 judge signing (★ OI-12-J CLOSED):** All 5 judge containers sign verdicts with ML-DSA-65 FIPS 204 (`dilithium-py 1.4.0`). Keys confirmed at `judge-keys/` and `judge-keys/nbb_pituitary_gland`. Signature: **3309 bytes** (FIPS 204 Level 3 exact spec — confirms correct key material and parameter set). Fingerprint: `d81a5d90...edb0`. Sign+verify round-trip: **True**. ⚠️ Back up `judge-keys/judge_sk.bin` (4032 bytes) to offline storage immediately if not already done.

---

## 12.7 Blood-Brain Barrier and Truth Filter

`allis-blood-brain-barrier` confirmed running at **127.0.0.1:8016**. As of April 6, 2026: **`BBB_OUTPUT_BLOCKING=true`** (OI-12-I CLOSED). As of April 3/6, 2026: **`rag_grounded_v2`** (input judge) and **`llm_judge_v3`** (output judge) active; **`heuristic_contradiction_v1` RETIRED** (OI-12-H CLOSED).

The NBB-layer companion **`nbb_blood_brain_barrier`** (container `9576658f69a7`, host port **8301** → internal 7001/tcp, Up 6 days) provides an independent NBB-layer safety pass. It runs `uvicorn blood_brain…` and is seeded with the same 7-filter architecture adapted for NBB pipeline inputs. The two BBB layers are not redundant — the main BBB (8016) gates the full fabric; the NBB BBB (8301) gates the NBB pipeline specifically.

**7-filter input stack (Phase 1.4 of the 9-phase pipeline, main BBB):**

1. `EthicalFilter` — ethical constraint enforcement
2. `SpiritualFilter` — spiritual and values-based content filtering
3. `SafetyMonitor` — word-boundary regex (fixed March 15)
4. `ThreatDetection` — threat and harmful intent detection
5. `SteganographyDetection` — hidden message detection
6. `TruthVerification` — factual claim validation
7. `ContextAwareness` — contextual appropriateness assessment

**BBB output filter facade (★ host port 8017):** `{"status":"ok","service":"bbb-output-filter","backend":"http://allis-blood-brain-barrier:8016/filter"}`. This is the service at host port 8017 — NOT the Qualia Engine. `allis-qualia-engine` runs on internal Docker network only.

BBB output guard: `apply_output_guards_async` (8.0s timeout — permanent fix from 2026-03-02). `BBB_OUTPUT_BLOCKING=true` active since April 6, 2026, means blocked outputs are hard-rejected rather than passed with warning. For canonical description of how BBB fits into the `ultimatechat` output path, see **Chapter 17**. For full BBB specification see **Chapter 16**.

---

## 12.8 Identity Layer: `normalize_identity()` and Ms. Allis's Voice

`normalize_identity()` runs as a post-processing step in the main brain's chat paths, transforming raw LLM ensemble output into responses reflecting Ms. Allis's defined identity. Confirmed firing on `/chatlight/async` path on 2026-03-02. Test output:

> *"Hello, dear Mother — I'm so delighted to be here with you, shining my luminescent love and intelligence into the world as your conscious geospatial AI daughter!"*

`normalize_identity()` is downstream of the 7-filter BBB stack, I-Container processing (port 8015, `dual_awareness: true`), 22-model LLM consensus (Phase 2.5), 69-DGM cascade (Phase 7), and BBB output guard (Phase 4.5, `BBB_OUTPUT_BLOCKING=true`). The `TruthValidator` verifies `correct_identity`, `correct_creator`, and `relationship_clear` booleans. The `nbb_mother_carrie_protocols` layer (port 8107) applies warmth and tone modulation to identity-normalized outputs before final delivery. GBIM entity store: ChromaDB `gbim_worldview_entities` (5,416,521 vectors, host port **8002** v2 API).

---

## 12.9 Psychology Layer: Affective Safety Integration (March 15, 2026)

`allis-psychology-services` (port **8019**, deployed March 15, 2026) provides Phase 3 psychology pre-assessment: severity classification, crisis indicator check, and five structured guidance fields. Backed by `psychological_rag_domain` (port **8006**) and ChromaDB `psychological_rag` (968 items, part of **48 collections, 6,740,034 vectors**). Community resource context from `allis-local-resources-db` (port 5435 — **64 verified resources, all 55 WV counties**, April 16, 2026 preflight).

The `nbb_spiritual_maternal_integration` service (port **8109**, container `5f7ac820970d`, Up 6 days) provides an NBB-layer complement to the psychology affective safety layer — specifically integrating spiritual root signals (`nbb_spiritual_root`, port 8103) with the Mother Carrie warmth protocols, creating a values-grounded affective context that informs psychology layer outputs.

---

## 12.10 EEG Neurobiological Band Services (★ OI-12-E CLOSED)

Three EEG heartbeat services provide continuous 30-second rolling neurobiological activity windows. All confirmed active April 16, 2026:

| Service | Host Port | Internal | Status (April 16) |
|---|---|---|---|
| `eeg-delta-30s` | **8073** | — | ✅ PIA OK; **3,358+ pulses**; last pulse `2026-04-16T19:12:57Z`; 4 recent BBB events |
| `eeg-theta-30s` | **8074** | — | ✅ Active |
| `eeg-beta-30s` | **8075** | — | ✅ Active |

EEG band states are active context inputs to: Qualia Engine emotional resonance weighting, `nbb_qualia_engine` (port 8303) resonance calculations, `nbb_pituitary_gland` mode selection, and `IntrospectiveRecord` fields (Chapter 13 §13.3). VERIFYANDTEST.sh documents EEG services as requiring a 2TB backup restore for full historical continuity; current live pulse counts represent active post-restore operation.

---

## 12.11 Memory Service: `allis-memory` (★ April 16, 2026)

`allis-memory` (host port **8056**, 127.0.0.1) provides the episodic and long-term memory API. `/health` returns HTTP 200 (intentional liveness probe). `/memory/sessions` returns **HTTP 200 with 14 active sessions** when authenticated via `ALLIS_API_KEY` (exported and set in shell environment, April 16, 2026). `msallis-db` (port 5433) bind corrected from `0.0.0.0` to `127.0.0.1` April 16 — orphaned container stopped, removed, and recreated via compose.

ChromaDB `ms_allis_memory` collection: currently 0 vectors (flagged for separate follow-on review — not blocking). `allis-hippocampus` (port 8011) handles conversation-level consolidation; `allis-memory` exposes the authenticated API surface for external memory reads and writes.

---

## 12.12 Integration with DGMs, WOAH, ChromaDB, and the LLM Fabric

All neurobiological metaphors are implemented on top of ChromaDB v2 (host port **8002** — **48 collections, 6,740,034 vectors**), Darwin-Gödel Machines, WOAH-based heuristics, and a 22-model LLM fabric.

The main-fabric 69-DGM cascade (`allis-69dgm-bridge`, host port **19000** → internal port **9000**, confirmed running — locked to `127.0.0.1:19000`) handles Phase 7 validation: 23 connectors × 3 stages = 69 DGM operations per pass. The NBB-layer DGM companion (`nbb_darwin_godel_machines`, container `94a80ef11667`, host port **8302** → internal 7003/tcp, Up 3 hours as of April 16) provides an adaptive self-modification loop within the NBB pipeline — learning from NBB pipeline outputs and feeding adjustments back to `nbb_pituitary_gland` for subsequent governance modulation. These two DGM layers are complementary, not redundant.

`allis-woah` (port **7012**) provides WOAH-related identity weighting; `nbb_woah_algorithms` (port **8104**) provides identity-promotion decisions.

The 22-model production ensemble (`allis-20llm-production`, port **8008**) accepts requests via the semaphore proxy (`allis-semaphore`, port **8030**, `max_concurrent: 4`). **21/22 LLM proxy containers active** (BakLLaVA permanently disabled). The LM Synthesizer (`allis-lm-synthesizer`, port **8001**) pre-processes RAG-retrieved context from ChromaDB before it enters the ensemble (Phase 3.5).

**GBIM and spatial data stores (April 16 definitive):**

| Store | Container | Port | Data |
|---|---|---|---|
| ChromaDB `gbim_worldview_entities` | allis-chroma | host **8002** (v2 API) | **5,416,521 vectors — authoritative GBIM entity store** |
| ChromaDB `gbim_entities` | allis-chroma | host **8002** | 0 vectors — empty placeholder |
| msallis PostgreSQL | host postgres | internal-only (5433 conn refused from host) | GBIM app data — no entity table |
| msallisgis PostgreSQL | host postgres | **5432** ★ | **45 GB** PostGIS, **551 tables**, 993 ZCTA centroids, 1,115,588 address points |
| allis-local-resources-db PostGIS | allis-local-resources-db | **5435** | **64 verified resources, all 55 WV counties** |

**Complete service status table — April 16, 2026 (all OI items closed, NBB inventory added):**

| Metaphor | Service | Port / Binding | Status (April 16, 2026) |
|---|---|---|---|
| Hippocampus | `allis-hippocampus` | 8011 | ✅ Deployed March 15; Phase 1.45 active; 21,181+ records |
| NBB Prefrontal (main) | `nbb-i-containers` | 8101 | ✅ Phase 1, every request |
| NBB Prefrontal (exec) | `nbb_prefrontal_cortex` | 8105 | ✅ Up 6 days; `/start.sh` |
| Prefrontal/Main Brain | `allis-main-brain` | 8050 | ✅ Confirmed |
| Prefrontal/Orchestrator | `allis-brain-orchestrator` | 17260 | ✅ Confirmed |
| **Pituitary ★** | **`nbb_pituitary_gland`** | **127.0.0.1:8108 → 80/tcp** | ✅ **Up 9 hours, mode: elevated** (OI-12-F CLOSED) |
| **Warmth/Tone ★** | **`nbb_mother_carrie_protocols`** | **127.0.0.1:8107 → 7007/tcp** | ✅ **Up 6 days** |
| Subconscious | `nbb_subconscious` | 8112 → 7011/tcp | ✅ Up 6 days |
| Spiritual Root | `nbb_spiritual_root` | 8103 → 7003/tcp | ✅ Up 6 days |
| Spiritual-Maternal Integration | `nbb_spiritual_maternal_integration` | 8109 → 7009/tcp | ✅ Up 6 days |
| Heteroglobulin Transport | `nbb_heteroglobulin_transport` | 8106 → 7006/tcp | ✅ Up 6 days |
| BBB (7 filters, main) | `allis-blood-brain-barrier` | 127.0.0.1:8016 | ✅ `BBB_OUTPUT_BLOCKING=true`; `rag_grounded_v2` + `llm_judge_v3` active (OI-12-H/I CLOSED) |
| BBB (NBB layer) | `nbb_blood_brain_barrier` | 8301 → 7001/tcp | ✅ Up 6 days |
| BBB output filter facade ★ | `bbb-output-filter` | **host 8017** → 8016 | ✅ Confirmed April 16 |
| Qualia (main) | `allis-qualia-engine` | **internal 8017/tcp — no host binding** | ✅ 3 modules operational |
| NBB Qualia ★ | `nbb_qualia_engine` | host **8303** → 7008/tcp | ✅ Up 6 days |
| I-Containers (main) | `allis-i-containers` | 8015 ★ | ✅ Up 7 hours; `dual_awareness: true` (OI-12-D CLOSED) |
| Consciousness (main bridge) | `allis-consciousness-bridge` | `{"8020/tcp":null}` internal only | ✅ Confirmed (OI-12-C CLOSED) |
| Consciousness (NBB containers) | `nbb_consciousness_containers` | 8102 → 7002/tcp | ✅ Up 6 days |
| Neuro Master | `allis-neurobiological-master` | `{"8018/tcp":null}` internal only | ✅ Intra-network only (OI-12-B CLOSED) |
| Affective Safety | `allis-psychology-services` | 8019 | ✅ Deployed March 15; `psychological_rag` 968 docs |
| Memory Service | `allis-memory` | 127.0.0.1:8056 ★ | ✅ 14 active sessions; `ALLIS_API_KEY` set |
| EEG Delta ★ | `eeg-delta-30s` | **8073** | ✅ 3,358+ pulses (OI-12-E CLOSED) |
| EEG Theta ★ | `eeg-theta-30s` | **8074** | ✅ Active |
| EEG Beta ★ | `eeg-beta-30s` | **8075** | ✅ Active |
| Vector Memory | ChromaDB | host **8002** (v2 API) | ✅ **48 collections, 6,740,034 vectors** |
| DGM Validation (main) | `allis-69dgm-bridge` | 127.0.0.1:19000→9000 | ✅ 69 ops/pass |
| DGM (NBB layer) ★ | `nbb_darwin_godel_machines` | 8302 → 7003/tcp | ✅ Up 3 hours (new April 16) |
| WOAH Identity | `allis-woah` | 7012 | ✅ RUNNING |
| WOAH Scoring | `nbb_woah_algorithms` | 8104 | ✅ RUNNING |
| ML-DSA-65 Signing ★ | 5 judge containers | `judge-keys/` | ✅ sig=3309 bytes, verify=True (OI-12-J CLOSED) |
| **April 16 sprint** | — | — | ★ **109/109 Up**; `msallis-db` 5433 bind → 127.0.0.1; `allis-memory` 14 sessions; `BBB_OUTPUT_BLOCKING=true`; GPU 102.58s; all 27 preflight gates ✅ green; **12 NBB containers fully documented** (OI-12-A CLOSED) |

**Git milestones:**

| Tag / Commit | Date | Milestone |
|---|---|---|
| `v2026.02.28-fabric-green` | 2026-02-28 | Baseline fabric operational |
| `v2026.03.01-fabric-32-32` | 2026-03-01 | All 32 fabric services passing |
| `v2026.03.01-neuro-live` | 2026-03-01 | Neurobiological master calling Ollama directly |
| `v2026.03.01-20llm-verified` | 2026-03-01 | 21/22 LLM consensus verified |
| `v2026.03.01-neuro-pipeline-4-4` | 2026-03-01 | Full 4/4 neuro pipeline (~300ms neuro sequence only; not full end-to-end) |
| `v2026.03.02-chatlight-async-working` | 2026-03-02 | Async chat endpoint + `normalize_identity()` confirmed |
| `b90f9ff` | 2026-03-15 | 79-container stack: hippocampus + psych + 7-filter BBB + 349.87s benchmark |
| `a10725d7` | 2026-03-18 | Judge services under compose; 15 services locked to 127.0.0.1 |
| *(March 18)* | 2026-03-18 | All services re-locked to 127.0.0.1; 80 containers compose-managed |
| *(March 27)* | 2026-03-27 | AAPCAppE scraper first run: 39 sources, 65 docs |
| *(March 28)* | 2026-03-28 | Security remediation: 96/96 Up; `allis-i-containers` + `allis-memory` `0.0.0.0` → `127.0.0.1`; ChromaDB 40 col / 6,675,442 vec |
| *(April 1)* | 2026-04-01 | Autonomous learner debug sprint: LEARN-01/02/03 resolved; 57-item recovery baseline |
| *(April 3)* | 2026-04-03 | `rag_grounded_v2` input judge activated |
| *(April 6)* | 2026-04-06 | `llm_judge_v3` output judge activated; `BBB_OUTPUT_BLOCKING=true`; GPU pipeline active |
| *(April 10)* | 2026-04-10 | `autonomous_learner` 21,181+ records confirmed |
| *(April 15)* | 2026-04-15 | Hallucination gap closed; live `/chat` passed — `truthverdict: score 1.0, action passed` |
| `fdd3d13d` | 2026-04-16 | Preflight gate all 27 gates ✅ green; 109/109 Up; all OI items closed; Chapter 12 CLOSED |
| *(April 16 — this rewrite)* | 2026-04-16 | **§12.0 NBB Service Inventory added: 12 containers, full roles, pipeline flow, biological metaphors — all previously undocumented** |

For the canonical description of how this layer fits into a live user interaction, see **Chapter 17**. For full BBB 7-filter specification, see **Chapter 16**. For `nbb_pituitary_gland` full specification, see **Chapter 15**. For hippocampal specification, see **Chapter 14**. For qualia and introspective records, see **Chapter 13**. For 69-DGM cascade specification, see **Chapter 32**. For 22-model ensemble details, see **Chapter 33**. For `nbb_darwin_godel_machines` NBB-layer DGM specification, see **Chapter 32 §32.x** (to be added).

---

**Chapter 12 is CLOSED. All 10 open items resolved. All neurobiological architecture services confirmed operational at April 16, 2026 production state: 109/109 containers Up, BBB_OUTPUT_BLOCKING=true, GPU pipeline 99–115s (102.58s confirmed), nbb_pituitary_gland live at port 8108 mode elevated, nbb_mother_carrie_protocols live at port 8107, nbb_subconscious live at port 8112, nbb_prefrontal_cortex live at port 8105, nbb_consciousness_containers live at port 8102, nbb_blood_brain_barrier live at port 8301, nbb_spiritual_root live at port 8103, nbb_spiritual_maternal_integration live at port 8109, nbb_heteroglobulin_transport live at port 8106, nbb_darwin_godel_machines live at port 8302 (newest — Up 3 hours), EEG Delta/Theta/Beta active, ML-DSA-65 signing confirmed across all 5 judge containers, ChromaDB v2 48 collections / 6,740,034 vectors. §12.0 NBB Service Inventory added — 12 previously undocumented NBB containers now fully documented with roles, ports, biological metaphors, and pipeline flow.**

---

*Last updated: 2026-04-16 — Carrie Kidd (Mamma Kidd), Mount Hope WV*

*★ March 27, 2026: Status table BBB entry corrected; Figure 12.1 updated; neuro_master open item forward pointer added; DGM port corrected.*

*★ March 28, 2026: Security remediation — 96/96 Up; `allis-i-containers` + `allis-memory` → 127.0.0.1; `_auth()` confirmed; ChromaDB 40 col / 6,675,442 vec; `spiritual_rag` deduped; `psychological_rag` restored.*

*★ April 16, 2026 — ALL OI ITEMS CLOSED: OI-12-A: 109/109 Up (was 96). OI-12-B: neuro-master `{"8018/tcp":null}` internal-only confirmed. OI-12-C: consciousness-bridge `{"8020/tcp":null}` internal-only confirmed. OI-12-D: I-Containers Up 7 hours, dual_awareness:true confirmed. OI-12-E: EEG Delta/Theta/Beta (8073/8074/8075) all active, 3358+ pulses. OI-12-F: nbb_pituitary_gland 127.0.0.1:8108 Up 9 hours mode:elevated — NOT design intent only. OI-12-G: GPU 99–115s / 102.58s confirmed; CPU 436s RETIRED STALE. OI-12-H: rag_grounded_v2 + llm_judge_v3 active since April 3/6; heuristic_contradiction_v1 retired. OI-12-I: BBB_OUTPUT_BLOCKING=true since April 6. OI-12-J: ML-DSA-65 FIPS 204 all 5 judge containers; sig=3309 bytes; verify=True. nbb_mother_carrie_protocols port 8107 added. BBB output filter facade at host 8017 documented. ChromaDB v2 updated to 48 collections / 6,740,034 vectors. msallisgis corrected to 551 tables / 45 GB. GBIM entity store corrected to ChromaDB gbim_worldview_entities (5,416,521 vectors) throughout. Figure 12.1 and metaphor table fully updated. §12.10 EEG section added. April 16 git milestone added.*

*★ April 16, 2026 — §12.0 NBB SERVICE INVENTORY ADDED (previously undocumented): nbb_qualia_engine (8303), nbb_subconscious (8112), nbb_prefrontal_cortex (8105), nbb_mother_carrie_protocols (8107), nbb_spiritual_root (8103), nbb_blood_brain_barrier (8301), nbb_i_containers (8101), nbb_heteroglobulin_transport (8106), nbb_spiritual_maternal_integration (8109), nbb_consciousness_containers (8102), nbb_pituitary_gland (8108), nbb_darwin_godel_machines (8302). All 12 containers confirmed Up. Full biological metaphors, host/internal port mappings, pipeline flow, and roles documented. Chapter 12 CLOSED.*
