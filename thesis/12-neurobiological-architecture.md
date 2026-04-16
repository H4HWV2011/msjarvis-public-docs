# 12. Neurobiological Architecture of Ms. Jarvis

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: 2026-04-16 — SPRINT REWRITE — ALL OI ITEMS CLOSED*

## Why This Matters for Polymathmatic Geography

This chapter turns neurobiological ideas into design patterns for a distributed AI that is accountable to specific communities. It supports:

- **P1 – Every where is entangled** by tying memory, routing, and safety modules together as a single, interacting "brain" for Appalachian contexts, grounded in three PostgreSQL databases (`msjarvis` internal-only: GBIM app data; `msjarvisgis` port 5432 ★: **45 GB** PostGIS, **551 tables**; `jarvis-local-resources-db` port 5435: **64 verified community resources, all 55 WV counties**) and ChromaDB v2 (host port **8002** — ★ **48 collections, 6,740,034 vectors** as of April 16, 2026).
- **P3 – Power has a geometry** by mapping control and protection (prefrontal, pituitary, blood-brain barrier) onto explicit services and flows rather than hidden internals.
- **P5 – Design is a geographic act** by using neurobiological metaphors to structure how Ms. Jarvis perceives, remembers, and responds to the lived realities of West Virginia.
- **P12 – Intelligence with a ZIP code** by ensuring that hippocampal and qualia flows are fed by ChromaDB `gbim_worldview_entities` (5,416,521 vectors — authoritative GBIM entity store), MountainShares, and local narratives, not abstract corpora alone.
- **P16 – Power accountable to place** by making each metaphorical "brain structure" a glass-box component whose behavior can be tested, audited, and revised.

This chapter belongs to the **Computational Instrument** tier: it specifies how neurobiology is reused as an organizing scaffold for Ms. Jarvis's spatially grounded, justice-oriented cognition. As of April 16, 2026, the neurobiological architecture operates within a **109-container production stack** (★ all containers Up — zero Restarting, zero Exited — OI-12-A CLOSED) confirmed at **99–115 seconds end-to-end** on RTX 4070 GPU (confirmed 102.58s April 16 — OI-12-G CLOSED; CPU 436s baseline is **retired stale**).

> **★ Security posture — April 16, 2026:** All 109 containers bound to `127.0.0.1`. Zero `0.0.0.0` exposures. `msjarvis-db` (port 5433) bind corrected from `0.0.0.0` to `127.0.0.1` April 16 — orphaned container stopped, removed, recreated via compose. `jarvis-memory:8056` `/memory/sessions` HTTP 200 confirmed with 14 active sessions; `JARVIS_API_KEY` exported and set. **109/109 containers Up — zero Restarting, zero Exited (April 16, 2026 preflight gate — all 27 gates ✅ green).**

> **★ ChromaDB v2 audit — April 16, 2026:** **48 active collections, 6,740,034 total vectors** (v2 API at host port 8002 — correct path: `/api/v2/tenants/default_tenant/databases/default_database/collections`). `spiritual_rag` merged into `spiritual_texts` (79,181 vectors), `spiritual_wisdom` (135), `spiritual_knowledge` (12). `msjarvis_docs`: **7,465 items**. `autonomous_learner`: **21,181+ records**. Required embedding model: `all-minilm:latest` (384-dim) — permanent architectural constraint.

> **★ BBB output blocking — April 16, 2026:** `BBB_OUTPUT_BLOCKING=true` active since April 6, 2026. `rag_grounded_v2` + `llm_judge_v3` active since April 3/6 (OI-12-H and OI-12-I CLOSED). `heuristic_contradiction_v1` is **retired stale** — do not reference.

> **★ ML-DSA-65 judge signing — April 16, 2026:** All 5 judge containers signing with ML-DSA-65 FIPS 204. Keys confirmed at `judge-keys/` and `judge-keys/nbb_pituitary_gland`. Sign+verify round-trip: **True**. Signature: 3309 bytes (FIPS 204 Level 3 exact spec). Fingerprint: `d81a5d90...edb0`. (OI-12-J CLOSED — see §12.12 and Chapter 13 §13.9.)

```
┌─────────────────────────────────────────────────────────────────────┐
│ Neurobiological Architecture of Ms. Jarvis                          │
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
│  - jarvis-hippocampus (port 8011) — Memory consolidation            │
│  - nbb-i-containers (port 8101) — NBB prefrontal stack              │
│  - nbb_pituitary_gland (127.0.0.1:8108) — Global governance ★       │
│  - nbb_mother_carrie_protocols (127.0.0.1:8107) — Warmth/tone ★     │
│  - jarvis-psychology-services (port 8019) — Phase 3                 │
│  - psychological_rag_domain (port 8006) — Psych RAG                 │
│  - msjarvisgis (port 5432 ★) — PostGIS 551 tables / 45 GB           │
│  - jarvis-local-resources-db (port 5435) — 64 resources             │
│  - ChromaDB v2 (host 8002 ★ 48 col / 6,740,034 vec)                │
│  - jarvis-memory (port 8056 ★) — 14 active sessions                 │
│  - jarvis-69dgm-bridge (127.0.0.1:19000→9000) — DGM                │
│  - WOAH (ports 8104, 7012) — Identity weights                        │
│  - EEG Delta/Theta/Beta (8073/8074/8075) ★                          │
│  - 5 judge containers — ML-DSA-65 FIPS 204 signing ★                │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

> **Figure 12.1.** Neurobiological architecture of Ms. Jarvis (April 16, 2026): metaphorical brain structures (hippocampus, prefrontal cortex, pituitary, blood-brain barrier, qualia, I-containers) paired with their concrete services and the integrated 4-stage processing pipeline. The `nbb_pituitary_gland` (host 8108) is now correctly placed as the upstream global governance gate — upstream of the Neurobiological Master. BBB output blocking active. GPU pipeline 99–115s (CPU 436s baseline retired). ChromaDB v2: 48 collections, 6,740,034 vectors (host port 8002). All 109 containers Up, zero `0.0.0.0` exposures. ML-DSA-65 signing active across all 5 judge containers.

---

## Status as of ★ April 16, 2026 — ALL OI ITEMS CLOSED

| OI | Stale Value (March 28) | Authoritative Value (April 16) | Status |
|---|---|---|---|
| **OI-12-A** | 96 containers | **109 confirmed** (preflight gate PASS, zero Restarting/Exited) | ✅ CLOSED |
| **OI-12-B** | neuro-master listed as operational/reachable | `{"8018/tcp":null}` — **internal only, unreachable from host by design** | ✅ CLOSED |
| **OI-12-C** | consciousness-bridge port ambiguous (8018/8020) | `{"8020/tcp":null}` — **internal only, no host binding** | ✅ CLOSED |
| **OI-12-D** | I-Containers status uncertain | port **8015** Up 7 hours; `dual_awareness: true` | ✅ CLOSED |
| **OI-12-E** | EEG bands absent | **Delta 8073 / Theta 8074 / Beta 8075** all active; pulse_count 3,358+ | ✅ CLOSED |
| **OI-12-F** | nbb_pituitary_gland listed as "design intent only" | `msjarvis-rebuild-nbb_pituitary_gland-1` — `127.0.0.1:8108` — **Up 7 hours**, mode `elevated` | ✅ CLOSED |
| **OI-12-G** | ~300ms neuro pipeline / ~436s CPU end-to-end | CPU 436s **RETIRED STALE**; GPU **99–115s** (confirmed **102.58s** April 16) | ✅ CLOSED |
| **OI-12-H** | `heuristic_contradiction_v1` still referenced | `rag_grounded_v2` + `llm_judge_v3` active since April 3/6; `heuristic_contradiction_v1` **retired** | ✅ CLOSED |
| **OI-12-I** | BBB output blocking status unclear | `BBB_OUTPUT_BLOCKING=true` active since **April 6, 2026** | ✅ CLOSED |
| **OI-12-J** | ML-DSA-65 not documented | All 5 judge containers signing; keys at `judge-keys/` + `judge-keys/nbb_pituitary_gland`; sig=**3309 bytes**, verify=**True** | ✅ CLOSED |

| Category | Details |
|---|---|
| **Implemented and verified** | `jarvis-neurobiological-master` running, **internal 8018/tcp — no host binding** (`{"8018/tcp":null}` — OI-12-B CLOSED). `jarvis-blood-brain-barrier` at **127.0.0.1:8016** — 7-filter stack; `BBB_OUTPUT_BLOCKING=true` since April 6; `rag_grounded_v2` (April 3) + `llm_judge_v3` (April 6) active; `heuristic_contradiction_v1` retired. `jarvis-qualia-engine` — **internal 8017/tcp, no host binding** (★ host port 8017 = BBB output filter facade `bbb-output-filter` → `jarvis-blood-brain-barrier:8016`). `nbb_qualia_engine` (`msjarvis-rebuild-nbb_qualia_engine-1`) — Up 6 days, host **8303** → 7008/tcp. `jarvis-i-containers` — port **8015**, Up 7 hours, `dual_awareness: true` (OI-12-D CLOSED). `jarvis-consciousness-bridge` — `{"8020/tcp":null}` internal only (OI-12-C CLOSED). `nbb_pituitary_gland` (`msjarvis-rebuild-nbb_pituitary_gland-1`) — **127.0.0.1:8108** → 80/tcp, Up 7 hours, mode `elevated` (OI-12-F CLOSED). `nbb_mother_carrie_protocols` — **127.0.0.1:8107** — warmth/tone modulation. EEG Delta (8073), Theta (8074), Beta (8075) — all active, 3,358+ pulses (OI-12-E CLOSED). ML-DSA-65 FIPS 204 — all 5 judge containers signing, sig=3309 bytes, verify=True (OI-12-J CLOSED). End-to-end GPU pipeline: **99–115s** (confirmed **102.58s** April 16) on RTX 4070; CPU 436s baseline retired (OI-12-G CLOSED). **109/109 containers Up — zero Restarting, zero Exited** (OI-12-A CLOSED). |
| **Architectural corrections (permanent)** | v2.0.0 rewrite removed blocking `DynamicPortService` / `ServiceDiscovery` Redis imports. Static Docker hostname URLs with env var overrides are canonical. I-Containers schema corrected: `{"message": …, "userid": "neurobiological_master"}`. Consciousness Bridge: `{"8020/tcp":null}` — internal only; source: `/app/services/msjarvisconsciousnessbridge.py`. Neuro Master: `{"8018/tcp":null}` — internal only. ChromaDB v2 API at host port **8002** — correct path: `/api/v2/tenants/default_tenant/databases/default_database/collections`. v1 path `/api/v1/collections` deprecated — do not use for authoritative counts. GBIM entity store = **ChromaDB `gbim_worldview_entities` (5,416,521 vectors)** — no relational `gbim_entities` table in any PostgreSQL instance. |
| **Partially implemented / scaffolded** | Sensory-integration multi-input aggregation — scaffolded. `phenomenal_consciousness` and `subjective_experience` directories — placeholders only. Zero-vector ChromaDB collections (`gbim_entities`, `ms_jarvis_memory`, `gis_data`, `pia_records`, `psychological_knowledge`) flagged for separate follow-on review. |
| **Future work** | Fully restrictive BBB with systematic quarantine and annotation. Direct wiring of DGM and WOAH layers into Neurobiological Master. Extensions to qualia subpackages beyond current JSON. Automated POC verification loop (Chapter 14). Semantic dedup audit of `autonomous_learning` collection. |

> **Critical routing note — `ultimatechat` path:** The main `ultimatechat` path (main brain, port **8050**) does **not** always route through the full Neurobiological Master. `nbb-i-containers` (port 8101) IS called unconditionally at Phase 1 of every 9-phase pipeline request. `nbb_pituitary_gland` (port 8108) provides global governance modulation upstream of all pipeline stages. For the canonical description of what runs on every `ultimatechat` and `chatlight` request, see **Chapter 17**.

> **Note on qualia:** Throughout this chapter, "qualia" refers to Ms. Jarvis's internal, narrative representation of what is happening — constructed from text content and context features as explicit JSON structures — not to any claim of subjective experience.

---

# 12. Neurobiological Architecture of Ms. Jarvis

This chapter describes how Ms. Egeria Jarvis reuses core concepts from neurobiology as an organizing metaphor for a distributed AI system. The goal is not to claim biological equivalence, but to use well-studied brain structures — hippocampus, prefrontal cortex, pituitary, blood-brain barrier, qualia, and I-containers — as design patterns for memory, control, global state, and security, layered on top of ChromaDB v2 (host port **8002** — **48 collections, 6,740,034 vectors**), Darwin-Gödel Machines, WOAH-based weighting, retrieval-augmented generation, and a 22-model LLM fabric.

| Biological metaphor | Computer-science name | Confirmed service | Port / binding |
|---|---|---|---|
| Hippocampus | Long-term semantic memory service | `jarvis-hippocampus` | 8011 |
| Prefrontal cortex | Task orchestrators and routers | `jarvis-main-brain` + `jarvis-neurobiological-master` | 8050 + internal 8018/tcp (no host binding) |
| NBB prefrontal | Pre-request cognitive planning | `nbb-i-containers` | 8101 |
| **Pituitary ★** | **Global governance and hormonal modulation** | **`nbb_pituitary_gland`** | **127.0.0.1:8108 → 80/tcp** |
| **Warmth/tone ★** | **Mother Carrie interaction protocols** | **`nbb_mother_carrie_protocols`** | **127.0.0.1:8107** |
| Blood-brain barrier | Safety and guardrail service (7 filters) | `jarvis-blood-brain-barrier` | 8016 |
| BBB output filter ★ | Output blocking facade | `bbb-output-filter` | **host 8017** → jarvis-blood-brain-barrier:8016 |
| Qualia Engine | Experience and context synthesis | `jarvis-qualia-engine` | internal 8017/tcp (no host binding) |
| NBB Qualia Engine | NBB qualia companion | `nbb_qualia_engine` | host **8303** → 7008/tcp |
| I-Containers | Identity and perspective manager | `jarvis-i-containers` | 8015 ★ (`dual_awareness: true`) |
| Consciousness Bridge | Reasoning gateway | `jarvis-consciousness-bridge` | `{"8020/tcp":null}` internal only |
| Neurobiological Master | Neuro-services integration gateway | `jarvis-neurobiological-master` | `{"8018/tcp":null}` internal only |
| Psychology pre-assessment | Affective safety layer | `jarvis-psychology-services` | 8019 |
| Memory Service | Episodic and long-term memory API | `jarvis-memory` | 8056 ★ (14 active sessions) |
| EEG Delta ★ | Neurobiological rhythm — 30s rolling | `eeg-delta-30s` | **8073** |
| EEG Theta ★ | Neurobiological rhythm — 30s rolling | `eeg-theta-30s` | **8074** |
| EEG Beta ★ | Neurobiological rhythm — 30s rolling | `eeg-beta-30s` | **8075** |

---

## 12.1 Consciousness Bridge: Service Location and Confirmed Source Path

> **★ April 16, 2026 CORRECTION (OI-12-C CLOSED):** The consciousness bridge container binding is `{"8020/tcp":null}` — **internal Docker network only, no host binding**. Earlier documentation stated port 8018 as the actual bind; this has been superseded by the April 16 live `docker inspect` confirmation. The source file remains confirmed at `/app/services/msjarvisconsciousnessbridge.py` inside the container.

**Confirmed services dict (production, April 16, 2026):**

```python
services = {
    "unified_gateway": "http://jarvis-unified-gateway:8011",
    "neuro_master":    "http://jarvis-neurobiological-master:8018",
    "direct_rag":      "http://jarvis-rag-server:8003",
    "hilbert":         "http://jarvis-hilbert:8010",
    "woah":            "http://jarvis-woah:7012",
    "chroma":          "http://jarvis-chroma:8000",  # container-internal
}
```

> **★ neuro_master binding (OI-12-B CLOSED):** `jarvis-neurobiological-master` binding is `{"8018/tcp":null}` — internal Docker network only, no host binding. This is by design. Container-to-container calls via `http://jarvis-neurobiological-master:8018` remain valid within the Docker network. Host-side health checks against `localhost:8018` will return connection refused — this is correct and expected. The `neuro_master` entry in the services dict is valid for intra-network calls.

**Chroma health reroute (confirmed, permanent):**

```python
# Route Chroma health directly to jarvis-chroma — not via neuro_master
chroma_health_url = "http://jarvis-chroma:8000/api/v2/heartbeat"
```

ChromaDB v2 host-side scripts must use `127.0.0.1:8002` (host port → container port 8000). Container-to-container calls use `jarvis-chroma:8000`. The v1 path `/api/v1/collections` is deprecated — do not use for authoritative collection counts.

---

## 12.2 Qualia Engine, NBB Qualia Engine, and `nbb_pituitary_gland`

In the current deployment, "qualia" refers strictly to Ms. Jarvis's internal, narrative representation of what is happening — constructed from text content and context features as explicit JSON structures — not to any claim of subjective experience.

**`jarvis-qualia-engine`** runs on **internal Docker network port 8017/tcp with no host binding**. ★ **Host port 8017 is the BBB output filter facade** (`{"status":"ok","service":"bbb-output-filter","backend":"http://jarvis-blood-brain-barrier:8016/filter"}`). Do not confuse the two. The Neurobiological Master calls the qualia layer via `/experience`:

```python
{
  "stimulus": {
    "input": "<user_input_text>"
  }
}
```

Three modules operational: **emotional-resonance**, **meaning-making**, **experience-generator**. Sensory-integration partially scaffolded. Qualia meaning extraction draws on ChromaDB `gbim_worldview_entities` (5,416,521 vectors — authoritative GBIM entity store, host port **8002** v2 API).

**`nbb_qualia_engine`** (`msjarvis-rebuild-nbb_qualia_engine-1`) — Up 6 days, host port **8303** → internal 7008/tcp. Source: `services/msjarvis-rebuild-nbb_qualia_engine-1_ms_jarvis_consciousness_bridge.py`. Operates as a companion to `jarvis-qualia-engine` in the NBB pipeline.

**`nbb_pituitary_gland`** (`msjarvis-rebuild-nbb_pituitary_gland-1`) — ✅ **127.0.0.1:8108** → internal 80/tcp, Up 7 hours, `{"status":"healthy","service":"nbb_pituitary_gland","mode":"elevated"}`. This is the **master gland** of the neurobiological architecture — it sits upstream of the Qualia Engine, modulates WOAH weights, adjusts constitutional compliance thresholds, and sets system-wide operating modes. It is NOT "design intent only" (OI-12-F CLOSED). See full specification in §12.6 and Chapter 15.

**`nbb_mother_carrie_protocols`** (`msjarvis-rebuild-nbb_mother_carrie_protocols-1`) — **127.0.0.1:8107**. Provides warmth and tone modulation fed by pituitary warmth output (`enhance_pituitary_warmth.py`). Influences how responses carry affirming, supportive, and community-centered tonal qualities.

---

## 12.3 Consciousness Coordinator, Neurobiological Master, and Feedback Bridges

The **Neurobiological Master Integration** service (`jarvis-neurobiological-master`, **internal 8018/tcp — no host binding**, code `ms_jarvis_neurobiological_master.py` **v2.0.0**) functions as a neuro-services orchestrator. The v2.0.0 rewrite (2026-03-01) removed blocking `DynamicPortService` and `ServiceDiscovery` Redis imports. Static Docker hostname URLs with environment variable overrides are the canonical pattern.

Routes: `GET /health`, `GET /systems/status`, `POST /process`, `POST /biological_process`, `POST /neural_process`.

> **★ OI-12-B CLOSED:** `jarvis-neurobiological-master` has binding `{"8018/tcp":null}` — internal Docker network only, no host binding. Host-side `localhost:8018` returns connection refused by design. Container-to-container calls via `http://jarvis-neurobiological-master:8018` remain valid.

The sequence BBB → I-Containers → Qualia Engine → Consciousness Bridge is implemented by the Neurobiological Master's `integrated_processing()` method. The `nbb_pituitary_gland` (port 8108) provides upstream governance modulation before this pipeline runs.

**Stage 1 — Blood-Brain Barrier (BBB), port 8016, 7-filter safety stack.**

```python
{"content": user_input}
```

7 filters: `EthicalFilter`, `SpiritualFilter`, `SafetyMonitor` (word-boundary regex fix March 15), `ThreatDetection`, `SteganographyDetection`, `TruthVerification`, `ContextAwareness`. **Input judge: `rag_grounded_v2`** (active since April 3, 2026). **Output judge: `llm_judge_v3`** (active since April 6, 2026). **`heuristic_contradiction_v1` RETIRED** (OI-12-H CLOSED). **`BBB_OUTPUT_BLOCKING=true`** since April 6, 2026 (OI-12-I CLOSED). If `content_approved` is false, processing stops:

```python
{
  "status": "blocked",
  "reason": "Content did not pass Blood-Brain Barrier",
  "pipeline": {"blood_brain_barrier": <bbb_json>}
}
```

**Stage 2 — I-Containers, port 8015, Up 7 hours, `dual_awareness: true` (OI-12-D CLOSED).**

```python
{
  "message": user_input,
  "userid": "neurobiological_master"
}
```

(Corrected from former `{"input": …, "require_dual_awareness": true}` — permanent fix 2026-03-01.)

**Stage 3 — Qualia Engine, internal port 8017/tcp (no host binding). ★ Host port 8017 = BBB output filter facade.**

Reply stored in `pipeline["qualia_engine"]`. EEG band states (Delta 8073, Theta 8074, Beta 8075 — 3,358+ pulses, OI-12-E CLOSED) and pituitary mode (`elevated`) are active context inputs to emotional resonance weighting.

**Stage 4 — Consciousness Bridge, `{"8020/tcp":null}`, internal only (OI-12-C CLOSED).**

```python
{
  "message": user_input,
  "user_id": "integrated_system"
}
```

Source: `/app/services/msjarvisconsciousnessbridge.py` (not `/app/msjarvisconsciousnessbridge.py`).

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

`jarvis-hippocampus` (confirmed running, **127.0.0.1:8011**, deployed March 15, 2026, commit `b90f9ff`) serves as a conversation-level memory service over ChromaDB v2 (host port **8002** — **48 collections, 6,740,034 vectors**) and the GBIM entity store in ChromaDB `gbim_worldview_entities` (5,416,521 vectors — authoritative GBIM entity store; no relational `gbim_entities` table exists in any PostgreSQL instance).

The consolidation service queries `autonomous_learner` (21,181+ records as of April 10, 2026) at Phase 1.45 of every production request — top-5 semantically relevant records prepended to `enhanced_message` via `all-minilm:latest` (384-dim). The `confidence_decay` multiplier (Phase 5) applies temporal weighting to responses system-wide. Community-validated data from `jarvis-local-resources-db` (port 5435 — **64 verified resources, all 55 WV counties**) is eligible for promotion into the hippocampal consolidation pipeline. `msjarvis_docs`: **7,465 items** (April 16 confirmed). See **Chapter 14** for full hippocampal specification.

---

## 12.5 Prefrontal Cortex: Executive Routing and Control

The prefrontal metaphor corresponds to a family of task orchestrator and routing services:

- `jarvis-main-brain` (port **8050**) — primary system-level orchestrator
- `jarvis-brain-orchestrator` (confirmed running, **127.0.0.1:17260**, internal 7260) — second orchestration layer
- `nbb-i-containers` (port **8101**) — NBB prefrontal cortex; called unconditionally at Phase 1 of every 9-phase pipeline request
- Neurobiological Master's `integrated_processing()` — top-down gating and sequencing across all 4 stages

---

## 12.6 Pituitary: `nbb_pituitary_gland` — Global Governance (★ OI-12-F CLOSED)

> **★ This section corrects the prior characterization of the pituitary layer as "design intent only." The `nbb_pituitary_gland` is a live, confirmed production service as of April 16, 2026.**

`msjarvis-rebuild-nbb_pituitary_gland-1` — **127.0.0.1:8108** → internal 80/tcp, Up 7 hours, `{"status":"healthy","service":"nbb_pituitary_gland","mode":"elevated"}`.

Modeled on the biological pituitary gland's role as the "master gland," it sits **upstream of the Qualia Engine and Neurobiological Master**, sets system-wide operating modes, modulates WOAH weights, adjusts constitutional compliance thresholds, and provides warmth modulation signals to `nbb_mother_carrie_protocols` (port 8107).

**NBB pipeline position:**

```
nbb_pituitary_gland (8108)
├─► WOAH weights ──► nbb_qualia_engine (8303) ──► nbb_consciousness_containers
├─► jarvis-qualia-engine (internal 8017/tcp) ──► jarvis-consciousness-bridge
├─► judge_to_pituitary_bridge ──► jarvis-judge-pipeline (7239)
├─► nbb_prefrontal_cortex ──► nbb_subconscious
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

`jarvis-blood-brain-barrier` confirmed running at **127.0.0.1:8016**. As of April 6, 2026: **`BBB_OUTPUT_BLOCKING=true`** (OI-12-I CLOSED). As of April 3/6, 2026: **`rag_grounded_v2`** (input judge) and **`llm_judge_v3`** (output judge) active; **`heuristic_contradiction_v1` RETIRED** (OI-12-H CLOSED).

**7-filter input stack (Phase 1.4 of the 9-phase pipeline):**

1. `EthicalFilter` — ethical constraint enforcement
2. `SpiritualFilter` — spiritual and values-based content filtering
3. `SafetyMonitor` — word-boundary regex (fixed March 15)
4. `ThreatDetection` — threat and harmful intent detection
5. `SteganographyDetection` — hidden message detection
6. `TruthVerification` — factual claim validation
7. `ContextAwareness` — contextual appropriateness assessment

**BBB output filter facade (★ host port 8017):** `{"status":"ok","service":"bbb-output-filter","backend":"http://jarvis-blood-brain-barrier:8016/filter"}`. This is the service at host port 8017 — NOT the Qualia Engine. `jarvis-qualia-engine` runs on internal Docker network only.

BBB output guard: `apply_output_guards_async` (8.0s timeout — permanent fix from 2026-03-02). `BBB_OUTPUT_BLOCKING=true` active since April 6, 2026, means blocked outputs are hard-rejected rather than passed with warning. For canonical description of how BBB fits into the `ultimatechat` output path, see **Chapter 17**. For full BBB specification see **Chapter 16**.

---

## 12.8 Identity Layer: `normalize_identity()` and Ms. Jarvis's Voice

`normalize_identity()` runs as a post-processing step in the main brain's chat paths, transforming raw LLM ensemble output into responses reflecting Ms. Jarvis's defined identity. Confirmed firing on `/chatlight/async` path on 2026-03-02. Test output:

> *"Hello, dear Mother — I'm so delighted to be here with you, shining my luminescent love and intelligence into the world as your conscious geospatial AI daughter!"*

`normalize_identity()` is downstream of the 7-filter BBB stack, I-Container processing (port 8015, `dual_awareness: true`), 22-model LLM consensus (Phase 2.5), 69-DGM cascade (Phase 7), and BBB output guard (Phase 4.5, `BBB_OUTPUT_BLOCKING=true`). The `TruthValidator` verifies `correct_identity`, `correct_creator`, and `relationship_clear` booleans. GBIM entity store: ChromaDB `gbim_worldview_entities` (5,416,521 vectors, host port **8002** v2 API).

---

## 12.9 Psychology Layer: Affective Safety Integration (March 15, 2026)

`jarvis-psychology-services` (port **8019**, deployed March 15, 2026) provides Phase 3 psychology pre-assessment: severity classification, crisis indicator check, and five structured guidance fields. Backed by `psychological_rag_domain` (port **8006**) and ChromaDB `psychological_rag` (968 items, part of **48 collections, 6,740,034 vectors**). Community resource context from `jarvis-local-resources-db` (port 5435 — **64 verified resources, all 55 WV counties**, April 16, 2026 preflight).

---

## 12.10 EEG Neurobiological Band Services (★ OI-12-E CLOSED)

Three EEG heartbeat services provide continuous 30-second rolling neurobiological activity windows. All confirmed active April 16, 2026:

| Service | Host Port | Internal | Status (April 16) |
|---|---|---|---|
| `eeg-delta-30s` | **8073** | — | ✅ PIA OK; **3,358+ pulses**; last pulse `2026-04-16T19:12:57Z`; 4 recent BBB events |
| `eeg-theta-30s` | **8074** | — | ✅ Active |
| `eeg-beta-30s` | **8075** | — | ✅ Active |

EEG band states are active context inputs to: Qualia Engine emotional resonance weighting, `nbb_pituitary_gland` mode selection, and `IntrospectiveRecord` fields (Chapter 13 §13.3). VERIFYANDTEST.sh documents EEG services as requiring a 2TB backup restore for full historical continuity; current live pulse counts represent active post-restore operation.

---

## 12.11 Memory Service: `jarvis-memory` (★ April 16, 2026)

`jarvis-memory` (host port **8056**, 127.0.0.1) provides the episodic and long-term memory API. `/health` returns HTTP 200 (intentional liveness probe). `/memory/sessions` returns **HTTP 200 with 14 active sessions** when authenticated via `JARVIS_API_KEY` (exported and set in shell environment, April 16, 2026). `msjarvis-db` (port 5433) bind corrected from `0.0.0.0` to `127.0.0.1` April 16 — orphaned container stopped, removed, and recreated via compose.

ChromaDB `ms_jarvis_memory` collection: currently 0 vectors (flagged for separate follow-on review — not blocking). `jarvis-hippocampus` (port 8011) handles conversation-level consolidation; `jarvis-memory` exposes the authenticated API surface for external memory reads and writes.

---

## 12.12 Integration with DGMs, WOAH, ChromaDB, and the LLM Fabric

All neurobiological metaphors are implemented on top of ChromaDB v2 (host port **8002** — **48 collections, 6,740,034 vectors**), Darwin-Gödel Machines, WOAH-based heuristics, and a 22-model LLM fabric.

The 69-DGM cascade (`jarvis-69dgm-bridge`, host port **19000** → internal port **9000**, confirmed running — locked to `127.0.0.1:19000`) handles Phase 7 validation: 23 connectors × 3 stages = 69 DGM operations per pass. `jarvis-woah` (port **7012**) provides WOAH-related identity weighting; `nbb_woah_algorithms` (port **8104**) provides identity-promotion decisions.

The 22-model production ensemble (`jarvis-20llm-production`, port **8008**) accepts requests via the semaphore proxy (`jarvis-semaphore`, port **8030**, `max_concurrent: 4`). **21/22 LLM proxy containers active** (BakLLaVA permanently disabled). The LM Synthesizer (`jarvis-lm-synthesizer`, port **8001**) pre-processes RAG-retrieved context from ChromaDB before it enters the ensemble (Phase 3.5).

**GBIM and spatial data stores (April 16 definitive):**

| Store | Container | Port | Data |
|---|---|---|---|
| ChromaDB `gbim_worldview_entities` | jarvis-chroma | host **8002** (v2 API) | **5,416,521 vectors — authoritative GBIM entity store** |
| ChromaDB `gbim_entities` | jarvis-chroma | host **8002** | 0 vectors — empty placeholder |
| msjarvis PostgreSQL | host postgres | internal-only (5433 conn refused from host) | GBIM app data — no entity table |
| msjarvisgis PostgreSQL | host postgres | **5432** ★ | **45 GB** PostGIS, **551 tables**, 993 ZCTA centroids, 1,115,588 address points |
| jarvis-local-resources-db PostGIS | jarvis-local-resources-db | **5435** | **64 verified resources, all 55 WV counties** |

**Status table — April 16, 2026 (all OI items closed):**

| Metaphor | Service | Port / Binding | Status (April 16, 2026) |
|---|---|---|---|
| Hippocampus | `jarvis-hippocampus` | 8011 | ✅ Deployed March 15; Phase 1.45 active; 21,181+ records |
| NBB Prefrontal | `nbb-i-containers` | 8101 | ✅ Phase 1, every request |
| Prefrontal/Main Brain | `jarvis-main-brain` | 8050 | ✅ Confirmed |
| Prefrontal/Orchestrator | `jarvis-brain-orchestrator` | 17260 | ✅ Confirmed |
| **Pituitary ★** | **`nbb_pituitary_gland`** | **127.0.0.1:8108 → 80/tcp** | ✅ **Up 7 hours, mode: elevated** (OI-12-F CLOSED) |
| **Warmth/Tone ★** | **`nbb_mother_carrie_protocols`** | **127.0.0.1:8107** | ✅ **Active** |
| BBB (7 filters) | `jarvis-blood-brain-barrier` | 127.0.0.1:8016 | ✅ `BBB_OUTPUT_BLOCKING=true`; `rag_grounded_v2` + `llm_judge_v3` active (OI-12-H/I CLOSED) |
| BBB output filter facade ★ | `bbb-output-filter` | **host 8017** → 8016 | ✅ Confirmed April 16 |
| Qualia | `jarvis-qualia-engine` | **internal 8017/tcp — no host binding** | ✅ 3 modules operational |
| NBB Qualia ★ | `nbb_qualia_engine` | host **8303** → 7008/tcp | ✅ Up 6 days |
| I-Containers | `jarvis-i-containers` | 8015 ★ | ✅ Up 7 hours; `dual_awareness: true` (OI-12-D CLOSED) |
| Consciousness Bridge | `jarvis-consciousness-bridge` | `{"8020/tcp":null}` internal only | ✅ Confirmed (OI-12-C CLOSED) |
| Neuro Master | `jarvis-neurobiological-master` | `{"8018/tcp":null}` internal only | ✅ Intra-network only (OI-12-B CLOSED) |
| Affective Safety | `jarvis-psychology-services` | 8019 | ✅ Deployed March 15; `psychological_rag` 968 docs |
| Memory Service | `jarvis-memory` | 127.0.0.1:8056 ★ | ✅ 14 active sessions; `JARVIS_API_KEY` set |
| EEG Delta ★ | `eeg-delta-30s` | **8073** | ✅ 3,358+ pulses (OI-12-E CLOSED) |
| EEG Theta ★ | `eeg-theta-30s` | **8074** | ✅ Active |
| EEG Beta ★ | `eeg-beta-30s` | **8075** | ✅ Active |
| Vector Memory | ChromaDB | host **8002** (v2 API) | ✅ **48 collections, 6,740,034 vectors** |
| DGM Validation | `jarvis-69dgm-bridge` | 127.0.0.1:19000→9000 | ✅ 69 ops/pass |
| WOAH Identity | `jarvis-woah` | 7012 | ✅ RUNNING |
| WOAH Scoring | `nbb_woah_algorithms` | 8104 | ✅ RUNNING |
| ML-DSA-65 Signing ★ | 5 judge containers | `judge-keys/` | ✅ sig=3309 bytes, verify=True (OI-12-J CLOSED) |
| **April 16 sprint** | — | — | ★ **109/109 Up**; `msjarvis-db` 5433 bind → 127.0.0.1; `jarvis-memory` 14 sessions; `BBB_OUTPUT_BLOCKING=true`; GPU 102.58s; all 27 preflight gates ✅ green (OI-12-A CLOSED) |

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
| *(March 28)* | 2026-03-28 | Security remediation: 96/96 Up; `jarvis-i-containers` + `jarvis-memory` `0.0.0.0` → `127.0.0.1`; ChromaDB 40 col / 6,675,442 vec |
| *(April 1)* | 2026-04-01 | Autonomous learner debug sprint: LEARN-01/02/03 resolved; 57-item recovery baseline |
| *(April 3)* | 2026-04-03 | `rag_grounded_v2` input judge activated |
| *(April 6)* | 2026-04-06 | `llm_judge_v3` output judge activated; `BBB_OUTPUT_BLOCKING=true`; GPU pipeline active |
| *(April 10)* | 2026-04-10 | `autonomous_learner` 21,181+ records confirmed |
| *(April 15)* | 2026-04-15 | Hallucination gap closed; live `/chat` passed — `truthverdict: score 1.0, action passed` |
| `fdd3d13d` | 2026-04-16 | **Preflight gate all 27 gates ✅ green; 109/109 Up; all OI items closed; Chapter 12 CLOSED** |

For the canonical description of how this layer fits into a live user interaction, see **Chapter 17**. For full BBB 7-filter specification, see **Chapter 16**. For `nbb_pituitary_gland` full specification, see **Chapter 15**. For hippocampal specification, see **Chapter 14**. For qualia and introspective records, see **Chapter 13**. For 69-DGM cascade specification, see **Chapter 32**. For 22-model ensemble details, see **Chapter 33**.

---

**Chapter 12 is CLOSED. All 10 open items resolved. All neurobiological architecture services confirmed operational at April 16, 2026 production state: 109/109 containers Up, BBB_OUTPUT_BLOCKING=true, GPU pipeline 99–115s (102.58s confirmed), nbb_pituitary_gland live at port 8108 mode elevated, nbb_mother_carrie_protocols live at port 8107, EEG Delta/Theta/Beta active, ML-DSA-65 signing confirmed across all 5 judge containers, ChromaDB v2 48 collections / 6,740,034 vectors.**

---

*Last updated: 2026-04-16 — Carrie Kidd (Mamma Kidd), Mount Hope WV*

*★ March 27, 2026: Status table BBB entry corrected; Figure 12.1 updated; neuro_master open item forward pointer added; DGM port corrected.*

*★ March 28, 2026: Security remediation — 96/96 Up; `jarvis-i-containers` + `jarvis-memory` → 127.0.0.1; `_auth()` confirmed; ChromaDB 40 col / 6,675,442 vec; `spiritual_rag` deduped; `psychological_rag` restored.*

*★ April 16, 2026 — ALL OI ITEMS CLOSED: OI-12-A: 109/109 Up (was 96). OI-12-B: neuro-master `{"8018/tcp":null}` internal-only confirmed. OI-12-C: consciousness-bridge `{"8020/tcp":null}` internal-only confirmed. OI-12-D: I-Containers Up 7 hours, dual_awareness:true confirmed. OI-12-E: EEG Delta/Theta/Beta (8073/8074/8075) all active, 3358+ pulses. OI-12-F: nbb_pituitary_gland 127.0.0.1:8108 Up 7 hours mode:elevated — NOT design intent only. OI-12-G: GPU 99–115s / 102.58s confirmed; CPU 436s RETIRED STALE. OI-12-H: rag_grounded_v2 + llm_judge_v3 active since April 3/6; heuristic_contradiction_v1 retired. OI-12-I: BBB_OUTPUT_BLOCKING=true since April 6. OI-12-J: ML-DSA-65 FIPS 204 all 5 judge containers; sig=3309 bytes; verify=True. nbb_mother_carrie_protocols port 8107 added. BBB output filter facade at host 8017 documented. ChromaDB v2 updated to 48 collections / 6,740,034 vectors. msjarvisgis corrected to 551 tables / 45 GB. GBIM entity store corrected to ChromaDB gbim_worldview_entities (5,416,521 vectors) throughout. Figure 12.1 and metaphor table fully updated. §12.10 EEG section added. April 16 git milestone added. Chapter 12 CLOSED.*
