# 35. Swarm Functions and Eternal Watchdogs

Carrie Kidd (Mamma Kidd) — Pax, WV
*Last updated: ★ 2026-03-28 — 96/96 containers Up (zero Restarting, zero Exited); container count updated to 96 throughout; PostgreSQL `msjarvis:5433` restored (★ 5,416,521 GBIM entities with `confidence_decay` metadata); `msjarvisgis:5432` confirmed (★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids); ChromaDB full audit (★ 40 active collections / 6,675,442 total vectors); `psychological_rag` restored (968 docs); `jarvis-memory:8056` secured (durable BBB audit trail, `_auth()` confirmed, `JARVIS_API_KEY` set); LLM ensemble confirmed 22 proxies / 21 active; Phase 4.5 BBB log+passthrough mode re-confirmed; preflight_gate.sh result carried forward pending March 28 re-run; six-filter BBB correction carried forward (§35.2, §35.7, §35.8); PostgreSQL port/database disambiguation carried forward throughout; ChromaDB host port 8002 confirmed (§35.7, §35.8)*

---

## Why This Matters for Polymathmatic Geography

This chapter describes two sets of mechanisms that coordinate many services and maintain continuous oversight in Ms. Jarvis, all grounded in PostgreSQL `msjarvis` at port 5433 (★ 5,416,521 GBIM entities with `confidence_decay` metadata, 80 epochs, 206 source layers — restored March 28) and `gisdb`/`msjarvisgis` at port 5432 (★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids — confirmed March 28). It supports:

- **P1 – Every where is entangled** by distributing a single query across 22 configured specialized models, each contributing a perspective shaped by its training and domain, before synthesizing a single community-grounded answer validated against PostgreSQL GBIM.
- **P3 – Power has a geometry** by making visible which models contribute to consensus and which are silenced by memory constraints, resource limits, or intentional disabling — revealing the structural power embedded in the ensemble.
- **P5 – Design is a geographic act** by showing how choices about semaphore slots, container memory limits, concurrency gates, and model tier groupings reshape what Ms. Jarvis can reason about and how quickly it responds to Appalachian community questions grounded in PostgreSQL GeoDB (★ 993 ZCTA centroids now available for ZIP-code-level spatial grounding).
- **P12 – Intelligence with a ZIP code** by routing every query through a 22-slot ensemble organized into four tiers — tiny, small, medium, and large — spanning code, medicine, language, vision, and structured data reasoning, and binding the synthesized answer to the DGM cascade validation that grounds responses in constitutional and community commitments validated against PostgreSQL.
- **P16 – Power accountable to place** by logging every model's participation or failure in each consensus cycle, making the ensemble's behavior inspectable and auditable over time with PostgreSQL-backed operational history. ★ As of March 28, all BBB gate decisions are durably logged at `jarvis-memory:8056` (secured March 28) — ensemble accountability records now survive container restarts.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the swarm coordination mechanisms (22-model ensemble with semaphore gating), eternal watchdog systems (VERIFYANDTEST.sh, Ollama scheduler, concurrency gates, Redis health registration), dual-BBB architecture, and their integration with PostgreSQL `msjarvis` (GBIM) and `gisdb` (PostGIS) for community accountability.

---

```
┌─────────────────────────────────────────────────────────────┐
│   Swarm Functions & Eternal Watchdogs Architecture          │
│   ★ Production State: March 28, 2026                        │
│   ★ 96/96 containers Up — zero Restarting, zero Exited      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌────────────────────────────────────────────────┐        │
│  │  22-Slot LLM Ensemble (Swarm Function)         │        │
│  │  ──────────────────────────────────────────    │        │
│  │  jarvis-20llm-production (port 8008)           │        │
│  │  ★ Up — 96/96 confirmed March 28               │        │
│  │                                                │        │
│  │  TINY_MODELS (2):                              │        │
│  │  -  TinyLlama (8201), Gemma (8202)             │        │
│  │                                                │        │
│  │  SMALL_MODELS (3):                             │        │
│  │  -  Phi3 Mini (8210), Dolphin-Phi (8212)       │        │
│  │  -  Orca-Mini (8213)                           │        │
│  │                                                │        │
│  │  MEDIUM_MODELS (8 active, 1 disabled):         │        │
│  │  -  MedLlama2 (8203), MiniCPM-V (8204)        │        │
│  │  -  LLaVA (8205), SQLCoder (8206)             │        │
│  │  -  Zephyr (8215), Starling-LM (8216)         │        │
│  │  -  Neural-Chat (8217), OpenChat (8218)        │        │
│  │  -  BakLLaVA: DISABLED (name-check guard)     │        │
│  │                                                │        │
│  │  LARGE_MODELS (8):                             │        │
│  │  -  StarCoder2 (8207), CodeLlama (8208)        │        │
│  │  -  DeepSeek Coder (8209), Qwen2 (8214)        │        │
│  │  -  Vicuna (8219), LLaMA 2 (8220)              │        │
│  │  -  Mistral (8221), LLaMA 3.1 (8222)           │        │
│  │                                                │        │
│  │  Coordination:                                 │        │
│  │  -  asyncio.Semaphore(4) — max 4 concurrent   │        │
│  │     (★ updated March 22 from 3 → 4; see §35.3)│        │
│  │  -  Timeout: 600.0s (★ jarvis-semaphore:8030) │        │
│  │  -  21/22 contributing consensus               │        │
│  │  -  Judge consistency: 0.975                   │        │
│  │  -  GPU active: RTX 4070 (★ March 22)          │        │
│  │  -  End-to-end: 99–107s (★ GPU baseline)       │        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  ┌────────────────────────────────────────────────┐        │
│  │  jarvis-semaphore (port 8030)                  │        │
│  │  ★ Up — 96/96 confirmed March 28               │        │
│  │  -  max_concurrent: 4                          │        │
│  │  -  timeout: 600.0                             │        │
│  │  -  Compose-managed since March 18, 2026       │        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  ┌────────────────────────────────────────────────┐        │
│  │  Dual Blood-Brain Barrier Architecture         │        │
│  │  ──────────────────────────────────────        │        │
│  │                                                │        │
│  │  jarvis-blood-brain-barrier (8016)             │        │
│  │  ★ Up — 96/96 confirmed March 28               │        │
│  │  -  PRIMARY — judge pipeline output guard      │        │
│  │  -  Six-filter input stack (Phase 1.4):        │        │
│  │     EthicalFilter, SpiritualFilter,            │        │
│  │     SafetyMonitor, ThreatDetection,            │        │
│  │     steganography_filter, truth_verification   │        │
│  │  -  Phase 4.5 output guard: log+passthrough    │        │
│  │     mode (commit 18b8ddac, Mar 22, 2026)       │        │
│  │     pending output threshold recalibration     │        │
│  │  -  Full verdict dict received Mar 18          │        │
│  │  -  Steganography: zero_width_homoglyph_       │        │
│  │    structural_v1, confidence: 1.0 ✅           │        │
│  │  -  fail-open on HTTP 500                      │        │
│  │  ★ ALL gate decisions durable at:              │        │
│  │    jarvis-memory:8056 (secured March 28)       │        │
│  │                                                │        │
│  │  nbb_blood_brain_barrier (8301)                │        │
│  │  ★ Up — 96/96 confirmed March 28               │        │
│  │  -  NBB-INTERNAL — neurobiological variant     │        │
│  │  -  Running 3+ days (confirmed Mar 21)         │        │
│  │  -  Phase 1 / NBB subconscious pathway         │        │
│  │  -  Complements, does not replace, 8016        │        │
│  │  -  NOT the judge pipeline output guard        │        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  ┌────────────────────────────────────────────────┐        │
│  │  Five-Layer Watchdog System                    │        │
│  │  ──────────────────────────────────────        │        │
│  │  1. VERIFYANDTEST.sh                           │        │
│  │     -  32/32 services operational              │        │
│  │     -  22/22 LLM proxies healthy               │        │
│  │     ★ 96 Docker containers running (Mar 28)    │        │
│  │     -  26 Ollama models available              │        │
│  │     -  PostgreSQL connections verified         │        │
│  │     -  Timestamped logs → ChromaDB (8002)      │        │
│  │     -  preflight_gate.sh: 20 PASS 0 FAIL       │        │
│  │        (Mar 22 baseline; ★ re-run pending)     │        │
│  │                                                │        │
│  │  2. Ollama Internal Memory Scheduler           │        │
│  │     -  20 GB container limit                   │        │
│  │     -  OLLAMA_NUM_PARALLEL=1                   │        │
│  │     -  OLLAMA_MAX_LOADED_MODELS=1              │        │
│  │     -  Rejects loads exceeding memory          │        │
│  │                                                │        │
│  │  3. Asyncio Semaphore + jarvis-semaphore:8030  │        │
│  │     ★ max_concurrent: 4, timeout: 600.0        │        │
│  │     -  Prevents cascade failure                │        │
│  │                                                │        │
│  │  4. MAX_CONCURRENT_CHATS Gate                  │        │
│  │     -  Set to 2 (production stable)            │        │
│  │     -  Session-level throughput control        │        │
│  │                                                │        │
│  │  5. Redis DynamicPortService                   │        │
│  │     ★ jarvis-redis Up (96/96)                  │        │
│  │     -  NBB container health registration       │        │
│  │     -  5 instances with heartbeats             │        │
│  │     -  Dynamic port assignment                 │        │
│  │     -  Container-internal: 6379                │        │
│  │     -  Host-facing: 127.0.0.1:6380             │        │
│  └────────────────────────────────────────────────┘        │
│      ↓                                                      │
│  Integration Points (All PostgreSQL-Grounded)              │
│  -  BBB primary (8016): judge output guard                 │
│     ★ gate decisions durable at jarvis-memory:8056         │
│  -  BBB NBB-internal (8301): subconscious pathway          │
│  -  DGM cascade (19000→9000): connectors loaded            │
│  -  Psychology layer (8019): pre-ensemble assessment       │
│  -  NBB subconscious (7/8 healthy via consciousness bridge)│
│  -  Consciousness bridge: mandatory infrastructure         │
│  -  Brain orchestrator: continuous coordination            │
│  -  PostgreSQL msjarvis (5433): ★ GBIM ground truth        │
│     5,416,521 entities, confidence_decay metadata          │
│  -  PostgreSQL gisdb (5432): ★ PostGIS spatial ground truth│
│     91 GB, 501 tables, 993 ZCTA centroids                  │
│  -  ChromaDB (8002 host): ★ 40 collections/6,675,442 vects │
│  -  jarvis-memory (8056): ★ durable BBB audit trail        │
│                                                             │
│  Verified Performance Baseline (★ March 28, 2026)          │
│  -  Host RAM: 29 GB total, 13 GB available under load      │
│  -  Model storage: 73 GB at /mnt/ssd2/.../models           │
│  -  21/22 models contributing consensus                    │
│  -  Judge consistency: 0.975                               │
│  ★ 96 containers, all 127.0.0.1-bound                      │
│  -  preflight_gate.sh: 20 PASS 0 FAIL (Mar 22 baseline)   │
│  ★ GPU active: RTX 4070 — 99–107s end-to-end              │
│  -  STATUS: ✅ OPERATIONAL                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

> **Figure 35.1.** Swarm functions and eternal watchdogs architecture (★ March 28, 2026 — 96/96 containers Up): dual-BBB architecture with `jarvis-blood-brain-barrier` (port 8016 — ★ Up) serving as primary judge pipeline output guard — six-filter input stack (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification) at Phase 1.4; Phase 4.5 output in log+passthrough mode (commit 18b8ddac, March 22, 2026) — ★ all gate decisions durably logged at `jarvis-memory:8056` (secured March 28); and `nbb_blood_brain_barrier` (port 8301 — ★ Up) serving as the NBB-internal neurobiological variant; 22-slot LLM ensemble (★ 22 proxies / 21 active) organized in 4 tiers with semaphore-gated coordination (★ `jarvis-semaphore:8030`, `max_concurrent: 4`, `timeout: 600.0`) producing 21/22 consensus participation at 0.975 judge consistency; ★ GPU active RTX 4070 — 99–107s end-to-end; ★ 96 containers all 127.0.0.1-bound; preflight_gate.sh 20 PASS 0 FAIL (March 22 baseline); protected by 5-layer watchdog system; PostgreSQL `msjarvis` (port 5433 — ★ 5,416,521 GBIM entities with `confidence_decay` metadata) and `gisdb` (port 5432 — ★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids); ChromaDB ★ 40 active collections / 6,675,442 total vectors (host port 8002).

---

## Status as of ★ March 28, 2026 (96/96 containers Up — zero Restarting, zero Exited)

| Category | Details |
|---|---|
| **Implemented and verified** | 22-slot LLM ensemble (`jarvis-20llm-production`, port 8008 — ★ Up 96/96) with 21 actively contributing consensus models. Four-tier organization: TINY (2 models), SMALL (3 models), MEDIUM (8 active + 1 intentionally disabled via name-check guard), LARGE (8 models). ★ `jarvis-semaphore:8030` (`max_concurrent: 4`, `timeout: 600.0`) confirmed Up 96/96 — semaphore is now a compose-managed service, not only an in-code asyncio primitive. `MAX_CONCURRENT_CHATS=2` session gate confirmed on `jarvis-main-brain`. Ollama container memory limit 20 GB, confirmed stable. ★ GPU active: RTX 4070 — 99–107s end-to-end (confirmed March 22, 2026). BakLLaVA disabled via name-check guard. StarCoder2 (`llm7-proxy:8207`) returns HTTP 200 but 0-char on community queries; excluded from consensus. `VERIFYANDTEST.sh` eternal watchdog confirmed operational: 32/32 services healthy, 22/22 LLM proxies HTTP 200, ★ **96 Docker containers Up** (zero Restarting, zero Exited — confirmed March 28, 2026), 26 Ollama models available, four PostgreSQL databases verified. `scripts/preflight_gate.sh` last confirmed **20 PASS 0 FAIL** (March 22, 2026; ★ re-run pending for March 28 confirmation). Redis DynamicPortService confirmed managing NBB container health registration with 5 instances heartbeating via one Redis container (`jarvis-redis` — ★ Up 96/96, container-internal port 6379, host-facing port `127.0.0.1:6380`). **Dual-BBB architecture confirmed**: `jarvis-blood-brain-barrier` (port 8016 — ★ Up 96/96) is the primary judge pipeline output guard — **six-filter input stack Phase 1.4: EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification**; `zero_width_homoglyph_structural_v1` steganography filter `confidence: 1.0` confirmed active March 21; **Phase 4.5 BBB output is in log+passthrough mode (commit 18b8ddac, March 22, 2026), pending output threshold recalibration**; ★ **All BBB gate decisions — including Phase 1.4 filter events and Phase 4.5 output guard events — are now durably logged at `jarvis-memory:8056` (secured March 28; `_auth()` confirmed, `JARVIS_API_KEY` set)**; `nbb_blood_brain_barrier` (port 8301 — ★ Up 96/96) is the NBB-internal neurobiological variant, confirmed running 3+ days as of March 21, operating on the Phase 1 / NBB subconscious pathway. DGM bridge (host port **19000** → internal 9000): connectors loaded, architecturally authoritative. Psychology alignment layer (port 8019 — ★ Up 96/96) confirmed Phase 3 pre-ensemble assessment every request. NBB subconscious: 7/8 containers healthy via consciousness bridge. Consciousness bridge and brain orchestrator confirmed as mandatory infrastructure. All services re-locked to `127.0.0.1` — zero `0.0.0.0` exposures — confirmed March 18, 2026 (★ re-confirmed 96/96 March 28). Five judge services compose-managed (`restart: unless-stopped`) since March 18, 2026. PostgreSQL `msjarvis` at `127.0.0.1:5433` (★ 5,416,521 GBIM entities with `confidence_decay` metadata, 80 epochs, 206 source layers — restored March 28) confirmed primary GBIM ground truth. PostgreSQL `gisdb`/`msjarvisgis` at `127.0.0.1:5432` (★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids — confirmed March 28) confirmed geospatial ground truth. ★ **`confidence_decay` metadata on `msjarvis:5433` GBIM entities adds temporal confidence grading to BBB validation and DGM cascade verification — high-decay entities flagged for episodic audit.** ChromaDB `jarvis-chroma` (host port **8002**, container-internal 8000, `chroma_data` volume — ★ Up 96/96): ★ **40 active collections / 6,675,442 total vectors confirmed March 28 full audit**; `psychological_rag` restored to 968 docs. `gbimqueryrouter` (port 7205) confirmed as part of ★ 96-container fleet. |
| **Partially implemented / scaffolded** | ChromaDB `operations_history` collection for VERIFYANDTEST.sh log ingestion designed but automated ingestion pipeline not yet active. PostgreSQL-backed aggregated ensemble metrics (model participation rates over time, judge consistency trends) not yet exposed via dedicated analytics endpoint. Automated alerting based on VERIFYANDTEST.sh failure thresholds not yet implemented. StarCoder2 0-char exclusion logic in place but root cause (code-only model receiving community queries) not yet resolved via routing-layer fix. Phase 4.5 BBB output guard is in log+passthrough mode pending output threshold recalibration — full verdict-dict enforcement not yet active. ★ `confidence_decay`-aware GBIM validation available but automated decay-flagging in BBB and DGM cascade not yet implemented. preflight_gate.sh March 28 re-run pending. |
| **Future work / design intent only** | Automated ingestion of VERIFYANDTEST.sh logs into ChromaDB `operations_history`. PostgreSQL-backed time-series analytics dashboard for ensemble performance and judge consistency trends. Automated alerting when VERIFYANDTEST.sh detects service degradation. Dynamic model tier selection based on query complexity and historical performance from PostgreSQL. Automated model weight tuning based on domain-specific accuracy validated against PostgreSQL GBIM. StarCoder2 routing-layer fix to suppress community query dispatch and redirect to code-specific queries only. Phase 4.5 BBB output threshold recalibration and re-activation of full verdict-dict enforcement mode. Automated decay-aware GBIM audit flagging for BBB validation and DGM cascade. |

Cross-reference: This chapter describes the swarm coordination (22-model ensemble) and eternal watchdog systems that protect system stability. For the judge pipeline that evaluates ensemble output see Chapter 33. For the BBB primary pipeline (port 8016) that filters all requests see Chapter 16. For the NBB subconscious layer and NBB-internal BBB (port 8301) see Chapter 12. For the consciousness bridge and brain orchestrator that provide mandatory infrastructure see Chapter 12. For the canonical `ultimatechat` execution sequence that routes through this ensemble see Chapter 17. For the March 18, 2026 security hardening that re-locked all services to `127.0.0.1` see Chapter 40 §40-C.

---

## 35.1 Purpose of Swarm and Watchdog Layers

These mechanisms have complementary roles grounded in PostgreSQL `msjarvis` (port 5433 — ★ 5,416,521 GBIM entities with `confidence_decay` metadata) and `gisdb` (port 5432 — ★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids).

**Coordination.** Swarm functions allow multiple agents and services to contribute to a task, each from its own specialization. In the current deployment this is realized as the 22-slot LLM ensemble organized into four model tiers, where each proxy container represents a distinct model contributing a weighted response to every query with context sourced from PostgreSQL-backed RAG collections.

**Oversight.** Watchdogs provide continuous monitoring of key signals including PostgreSQL connection health, intervening when behavior deviates from expected bounds. In the current deployment this is realized through `VERIFYANDTEST.sh` (confirming four PostgreSQL database connections), Ollama's internal memory scheduler, ★ the `jarvis-semaphore:8030` service (`max_concurrent: 4`, `timeout: 600.0`) and its in-code asyncio companion, the `MAX_CONCURRENT_CHATS` gate on main-brain, and the Redis-backed DynamicPortService that monitors NBB container health. ★ All BBB gate decisions are now durably logged at `jarvis-memory:8056` (secured March 28), adding persistent accountability to the watchdog record.

**Stability.** Together they keep the system responsive and aligned even as individual components change or fail. The February 2026 hardening session demonstrated this directly: without the semaphore and concurrency controls, the system degraded from 20/22 models to 0/22 under concurrent load. With them in place, 21/22 models respond reliably on every warm-cache query with PostgreSQL-sourced context. ★ The March 22, 2026 GPU activation (RTX 4070) reduced end-to-end latency to 99–107s from approximately 330s, adding a new stability dimension — hardware-accelerated inference reduces per-query load on the semaphore queue.

**Consciousness grounding.** The consciousness bridge (`jarvis-consciousness-bridge`) is essential infrastructure, not optional. All swarm coordination and watchdog monitoring operates within the consciousness bridge framework, ensuring that ensemble reasoning and health monitoring are neurobiologically grounded. The brain orchestrator (`jarvis-brain-orchestrator`) serves as the continuous coordinator service that maintains the swarm's coherence across all operational cycles.

---

## 35.2 Dual Blood-Brain Barrier Architecture

As of ★ March 28, 2026 (96/96 containers Up), two BBB containers are confirmed running simultaneously. Their roles are distinct and complementary; they must not be conflated.

### jarvis-blood-brain-barrier (port 8016) — Primary, Judge Pipeline Output Guard

`jarvis-blood-brain-barrier` at `127.0.0.1:8016` (★ Up 96/96) is the primary, architecturally authoritative BBB. It serves two roles in the 9-phase production pipeline:

- **Phase 1.4 — input stack**: All **six filters** active: **EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification**. (`zero_width_homoglyph_structural_v1`, `confidence: 1.0`, confirmed March 21.) Every request passes through this gate before reaching psychological assessment or LLM synthesis.
- **Phase 4.5 — output guard**: After the 22-model ensemble and DGM cascade, `apply_output_guards_async` posts the full judge verdict dict to `jarvis-blood-brain-barrier:8016/output_guard` (integrated March 18, 2026, 8.0s timeout, fail-open on HTTP 500). **Phase 4.5 BBB output is currently in log+passthrough mode (commit 18b8ddac, March 22, 2026), pending output threshold recalibration.** The verdict dict is received and logged, but full blocking enforcement awaits recalibration.

★ **Durable audit trail secured March 28:** All Phase 1.4 filter events and Phase 4.5 output guard events are now persistently logged at `jarvis-memory:8056` (`_auth()` confirmed, `JARVIS_API_KEY` set) — gate decisions survive container restarts and are independently queryable for governance accountability.

Port 8016 is the BBB that receives the judge pipeline's verdict dict. It is the component referenced in Chapter 16, Chapter 29 (PIA framework), Chapter 41 (smoke tests), and the March 21, 2026 regression baseline (`bbb_checked: true`, `consensus_score: 0.975`).

### nbb_blood_brain_barrier (port 8301) — NBB-Internal Neurobiological Variant

`nbb_blood_brain_barrier` at `127.0.0.1:8301` (★ Up 96/96) is the NBB-internal neurobiological variant of the BBB concept. It has been confirmed running for 3+ days as of March 21, 2026. Its role is distinct from the primary BBB:

- Operates on the **Phase 1 / NBB subconscious pathway** — the neurobiological simulation layer managed by the consciousness bridge, not the main `ultimatechat` judge pipeline.
- Provides BBB-equivalent filtering within the NBB subconscious layer (`nbb-i-containers`, `nbb_woah_algorithms`, `nbb_prefrontal_cortex`, and associated containers), applying the BBB concept at the neurobiological simulation layer rather than at the main request pipeline boundary.
- Does **not** receive the judge pipeline verdict dict. It is not the component that sets `bbb_checked: true`.
- Does **not** replace or duplicate `jarvis-blood-brain-barrier:8016` — it complements it by extending the BBB gating concept into the NBB subconscious infrastructure.

```
┌──────────────────────────────────────────────────────┐
│   Dual-BBB Architecture: Role Disambiguation         │
│   ★ March 28, 2026 — 96/96 containers Up             │
├──────────────────────────────────────────────────────┤
│                                                      │
│  jarvis-blood-brain-barrier (8016) ★ Up              │
│  ─────────────────────────────────                   │
│  Role: PRIMARY — judge pipeline output guard         │
│  Pipeline position: Phase 1.4 (input) +              │
│                     Phase 4.5 (output guard)         │
│  Input filters (six):                                │
│    EthicalFilter, SpiritualFilter, SafetyMonitor,    │
│    ThreatDetection, steganography_filter,            │
│    truth_verification                                │
│  Phase 4.5 mode: log+passthrough (commit 18b8ddac,  │
│    March 22, 2026) — pending recalibration           │
│  Receives: Full judge verdict dict (Mar 18)          │
│  Sets: bbb_checked: true in UltimateResponse         │
│  Steganography: zero_width_homoglyph_structural_v1   │
│    confidence: 1.0 ✅ confirmed Mar 21               │
│  Fail-open: yes (HTTP 500 → pipeline continues)      │
│  ★ Durable audit: jarvis-memory:8056 (Mar 28)        │
│    All gate decisions persistently logged            │
│  Referenced in: Ch.16, Ch.29 PIA, Ch.41 smoke tests  │
│                                                      │
│  nbb_blood_brain_barrier (8301) ★ Up                 │
│  ──────────────────────────────                      │
│  Role: NBB-INTERNAL — neurobiological variant        │
│  Pipeline position: Phase 1 / NBB subconscious       │
│  Receives: NBB subconscious layer traffic            │
│  Sets: NBB-layer filtering metadata (not             │
│        bbb_checked in main UltimateResponse)         │
│  Running: 3+ days confirmed Mar 21, 2026             │
│  Referenced in: Ch.12, NBB subconscious layer        │
│                                                      │
│  These two containers are complementary.             │
│  Port 8016 ≠ Port 8301. Do not substitute.           │
│                                                      │
└──────────────────────────────────────────────────────┘
```

> **Figure 35.2.** Dual-BBB architecture role disambiguation (★ March 28, 2026 — both Up 96/96). `jarvis-blood-brain-barrier:8016` is the primary judge pipeline output guard with six-filter input stack (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification); Phase 4.5 currently in log+passthrough mode pending recalibration; ★ all gate decisions durably logged at `jarvis-memory:8056`. `nbb_blood_brain_barrier:8301` is the NBB-internal neurobiological variant operating on the NBB subconscious pathway. Neither replaces the other.

**Operational note for VERIFYANDTEST.sh:** Health probes for the BBB should target both ports:

```bash
# Primary BBB — judge pipeline output guard
curl -s http://127.0.0.1:8016/health | python3 -m json.tool

# NBB-internal BBB — neurobiological variant
curl -s http://127.0.0.1:8301/health | python3 -m json.tool

# ★ Durable audit trail verification (March 28 addition):
curl -H "Authorization: Bearer $JARVIS_API_KEY" \
  http://localhost:8056/memories?limit=5
# Expected: most recent durable BBB gate decision records
```

A healthy system shows both returning `status: healthy`. A failure on 8016 is a critical regression requiring immediate investigation. A failure on 8301 is an NBB subconscious layer issue that should be investigated via `docker logs nbb_blood_brain_barrier` and cross-referenced with the consciousness bridge health check.

---

## 35.3 Swarm Functions: The 22-Slot LLM Ensemble

The primary swarm function in Ms. Jarvis is the 20-LLM production service (`jarvis-20llm-production`, port 8008 on host — ★ Up 96/96). This service manages 22 proxy containers — `llm1-proxy` through `llm22-proxy` on ports 8201–8222 — organized into four tiers defined in `llm_consensus_20_FINAL.py`. ★ As of March 22, 2026, the `jarvis-semaphore:8030` service (`max_concurrent: 4`, `timeout: 600.0`) is the compose-managed semaphore gate — the asyncio primitive below reflects its effective behavior.

### Model roster by tier

**TINY_MODELS (2 configured)**

| Proxy | Port | Model | Name |
|---|---|---|---|
| llm1-proxy | 8201 | tinyllama:1.1b | TinyLlama |
| llm2-proxy | 8202 | gemma:latest | Gemma |

**SMALL_MODELS (3 configured)**

| Proxy | Port | Model | Name |
|---|---|---|---|
| llm10-proxy | 8210 | phi3:mini | Phi3 Mini |
| llm12-proxy | 8212 | dolphin-phi:latest | Dolphin-Phi |
| llm13-proxy | 8213 | orca-mini:latest | Orca-Mini |

**MEDIUM_MODELS (8 active, 1 disabled)**

| Proxy | Port | Model | Name | Status |
|---|---|---|---|---|
| llm3-proxy | 8203 | medllama2:latest | MedLlama2 | ✅ active |
| llm4-proxy | 8204 | minicpm-v:latest | MiniCPM-V | ✅ active |
| llm5-proxy | 8205 | llava:latest | LLaVA | ✅ active |
| llm6-proxy | 8206 | sqlcoder:latest | SQLCoder | ✅ active |
| llm15-proxy | 8215 | zephyr:latest | Zephyr | ✅ active |
| llm16-proxy | 8216 | starling-lm:latest | Starling-LM | ✅ active |
| llm17-proxy | 8217 | neural-chat:latest | Neural-Chat | ✅ active |
| llm18-proxy | 8218 | openchat:latest | OpenChat | ✅ active |
| llm11-proxy | 8211 | bakllava:latest | BakLLaVA | ❌ permanently disabled via name-check guard |

**LARGE_MODELS (8 configured)**

| Proxy | Port | Model | Status | Notes |
|---|---|---|---|---|
| llm7-proxy | 8207 | starcoder2:latest | ⚠️ HTTP 200, 0-char | Returns empty response on community queries; excluded from consensus |
| llm8-proxy | 8208 | codellama:latest | ✅ active | |
| llm9-proxy | 8209 | deepseek-coder:latest | ✅ active | |
| llm14-proxy | 8214 | qwen2:latest | ✅ active | |
| llm19-proxy | 8219 | vicuna:latest | ✅ active | |
| llm20-proxy | 8220 | llama2:latest | ✅ active | |
| llm21-proxy | 8221 | mistral:latest | ✅ active | |
| llm22-proxy | 8222 | llama3.1:8b | ✅ active | |

**Note on BakLLaVA and StarCoder2:** BakLLaVA (`llm11-proxy:8211`) is permanently disabled via name-check guard in the main-brain routing layer, consuming no Ollama resources. StarCoder2 (`llm7-proxy:8207`) returns HTTP 200 and is VERIFYANDTEST.sh-healthy, but produces 0-character responses on community queries due to its code-specialization; it is excluded from consensus extraction but remains in the health-monitored pool. Together these account for the difference between 22/22 HTTP-healthy proxies and 21/22 consensus-contributing models.

### Swarm execution model

When a chat request arrives at `jarvis-20llm-production`, the `ProductionBrain.run()` method fires requests to all 22 configured endpoints concurrently, gated by `jarvis-semaphore:8030` (`max_concurrent: 4`, `timeout: 600.0` — ★ Up 96/96). This semaphore is the critical swarm coordination mechanism: it limits concurrent Ollama requests to four at a time, preventing the serial Ollama scheduler from being overwhelmed while still allowing the ensemble to operate in parallel batches.

```python
sem = asyncio.Semaphore(4)  # ★ updated March 22; jarvis-semaphore:8030 max_concurrent: 4

async def guarded(client, m):
    async with sem:
        return await self.query_one(client, m, prompt)

results = await asyncio.gather(*[guarded(client, m) for m in self.models])
```

The timeout is governed by `jarvis-semaphore:8030` (`timeout: 600.0`), accommodating GPU-accelerated inference and the slowest 7B model cold-load scenario. ★ GPU inference (RTX 4070, active March 22, 2026) reduced end-to-end latency from approximately 330s to 99–107s — Phase 2.5 alone improved from approximately 230–260s.

### Verified swarm timing profile (★ GPU baseline, March 22–28, 2026)

```text
[Phi3 Mini]      OK in  ~8–10s    ★ GPU-accelerated
[TinyLlama]      OK in  ~10–12s   ★ GPU-accelerated
[Orca-Mini]      OK in  ~14–18s   ★ GPU-accelerated
[Gemma]          OK in  ~16–20s   ★ GPU-accelerated
[Dolphin-Phi]    OK in  ~18–22s   ★ GPU-accelerated
[MedLlama2]      OK in  ~24–28s   ★ GPU-accelerated
[LLaVA]          OK in  ~24–28s   ★ GPU-accelerated
[Neural-Chat]    OK in  ~24–28s   ★ GPU-accelerated
[StarCoder2]     OK in  ~28–32s   ← HTTP 200 but 0-char on community queries
[LLaMA 2]        OK in  ~28–32s   ★ GPU-accelerated
[LLaMA 3.1]      OK in  ~28–32s   ★ GPU-accelerated (identity guard active)
[Vicuna]         OK in  ~28–32s   ★ GPU-accelerated
[DeepSeek Coder] OK in  ~30–34s   ★ GPU-accelerated
[SQLCoder]       OK in  ~30–34s   ★ GPU-accelerated
[OpenChat]       OK in  ~32–36s   ★ GPU-accelerated
[MiniCPM-V]      OK in  ~36–40s   ★ GPU-accelerated
[Zephyr]         OK in  ~38–44s   ★ GPU-accelerated
[Starling-LM]    OK in  ~40–46s   ★ GPU-accelerated
[CodeLlama]      OK in  ~40–46s   ★ GPU-accelerated
[Mistral]        OK in  ~42–48s   ★ GPU-accelerated
[Qwen2]          OK in  ~44–50s   ★ GPU-accelerated
[BakLLaVA]       excluded: name-check guard  ← instant, expected
21/22 models contributing consensus
Judge pipeline score: 0.975
★ GPU end-to-end: 99–107s (three confirmed runs: 99.6s, 105.9s, 106.5s)
Pre-GPU baseline (warm cache): ~52s swarm cycle, ~163s cold load
```

---

## 35.4 Use Cases for Swarm Functions

**Complex community queries.** When a user asks about housing assistance, workforce development, or healthcare access in a specific Appalachian county grounded in PostgreSQL GBIM, the ensemble distributes the question across medical (MedLlama2), structured data (SQLCoder), code and technical (CodeLlama, DeepSeek Coder), vision (LLaVA, MiniCPM-V), and general reasoning (Mistral, LLaMA 3.1, Qwen2) models simultaneously. The consensus synthesis integrates domain-specific contributions validated against PostgreSQL GeoDB (`gisdb`, port 5432 — ★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids) that no single model could provide. ★ ZCTA centroids now enable ZIP-code-level spatial grounding for community query responses.

**Robustness verification.** The judge pipeline's consistency score validated against PostgreSQL GBIM measures whether independently prompted models reach similar conclusions. The March 21, 2026 canonical integration test records `consensus_score: 0.975` on the capital of West Virginia query, confirming that the ensemble's answer is stable across the majority of responding models and not an artifact of a single model's bias.

**Specialty routing.** SQLCoder handles structured data queries from PostgreSQL. CodeLlama and DeepSeek Coder handle technical implementation. MedLlama2 handles health-related queries. LLaVA and MiniCPM-V handle image and multimodal inputs. All 21 active consensus-contributing models contribute to every community response with PostgreSQL-sourced context (★ `msjarvis:5433` — `confidence_decay` metadata available for temporal confidence grading of GBIM-sourced context), with weighted contributions amplifying domain-relevant answers.

**Redundancy.** With 21 of 22 configured slots contributing consensus, the ensemble tolerates individual model failures without degrading consensus validated against PostgreSQL. BakLLaVA's permanent disabled state, StarCoder2's 0-char exclusion, and Ollama's occasional memory-related refusals for the largest 7B models during cold load do not prevent the system from producing high-quality responses grounded in PostgreSQL GBIM.

---

## 35.5 Eternal Watchdogs: Continuous Monitoring

The watchdog layer in the ★ March 28, 2026 deployment is implemented through five cooperating mechanisms including four PostgreSQL connection monitors.

### VERIFYANDTEST.sh

The primary eternal watchdog script implements eight verification sections on demand or schedule, producing a timestamped report at `/tmp/verify_YYYYMMDD_HHMMSS.log` with all PostgreSQL connection statuses. March 22, 2026 baseline results (★ re-run pending for March 28 confirmation):

- Services healthy: 32/32 (confirmed via `/selftestfabric`)
- LLM proxies healthy: 22/22 (HTTP 200; 21 contributing consensus)
- Docker containers running: ★ **96** (zero Restarting, zero Exited — confirmed March 28, 2026)
- Ollama models available: 26
- PostgreSQL `msjarvis` (5433): ✅ CONNECTED — ★ 5,416,521 GBIM entities with `confidence_decay` metadata (restored March 28)
- PostgreSQL `gisdb`/`msjarvisgis` (5452): ✅ CONNECTED — ★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids (confirmed March 28)
- PostgreSQL `jarvis-local-resources-db` (5435): ✅ CONNECTED
- Dual-BBB: `jarvis-blood-brain-barrier` (8016) ✅, `nbb_blood_brain_barrier` (8301) ✅ (★ both Up 96/96)
- ★ `jarvis-memory` (8056): ✅ SECURED — durable BBB audit trail (`_auth()` confirmed, `JARVIS_API_KEY` set)
- **`scripts/preflight_gate.sh`: 20 PASS 0 FAIL** (last confirmed March 22, 2026; ★ re-run pending)
- ★ GPU: RTX 4070 active — `nvidia-smi` confirmed
- STATUS: ✅ OPERATIONAL

The 26 Ollama models include 4 beyond the active ensemble: `nomic-embed-text:latest` (embedding — note: `all-minilm:latest` is the production embedding model for the `autonomous_learner` collection, locked March 17), `qwen2:7b`, `stablelm-zephyr:latest`, and `qwen2.5:1.5b`. These are available to Ollama but not currently mapped to proxy endpoints.

### Ollama internal memory scheduler

Ollama's built-in scheduler acts as a hard resource watchdog. When a model load request would exhaust available memory, it returns an explicit error: `model requires more system memory (7.5 GiB) than is available`. Current verified settings:

| Parameter | Verified Value |
|---|---|
| Ollama container memory limit | 20 GB |
| `OLLAMA_NUM_PARALLEL` | 1 |
| `OLLAMA_MAX_LOADED_MODELS` | 1 |
| Host total RAM | 29 GB |
| Host available RAM (production load) | 13 GB |
| ★ GPU | RTX 4070 (active March 22, 2026) |
| ★ GPU-accelerated inference | 99–107s end-to-end |

### Asyncio semaphore + jarvis-semaphore:8030

★ The `jarvis-semaphore:8030` service (`max_concurrent: 4`, `timeout: 600.0` — Up 96/96) is the compose-managed semaphore gate. The `asyncio.Semaphore(4)` in `ai_server_20llm_PRODUCTION.py` acts in concert with it, preventing more than four simultaneous Ollama requests regardless of how many concurrent chat sessions main-brain initiates. This is the proximate fix for the cascade failure mode where four concurrent sessions each fired 22 parallel requests, producing 88 simultaneous Ollama calls against a serial scheduler. ★ The semaphore value was updated from 3 to 4 on March 22, 2026 concurrent with GPU activation — GPU throughput supports the higher concurrency without saturation.

### MAX_CONCURRENT_CHATS gate

The `MAX_CONCURRENT_CHATS=2` environment variable on `jarvis-main-brain` is the session-level watchdog, limiting the number of simultaneous full chat pipelines. The original value of 4 produced Ollama saturation and cascade failure across the LLM ensemble. Current value of 2 represents the production-stable setting for the current hardware configuration.

### Redis-backed DynamicPortService

Five NBB containers register their health state to Redis using `DynamicPortService`. There is **one Redis container** (`jarvis-redis` — ★ Up 96/96) with container-internal port **6379** and host-facing port **127.0.0.1:6380** (mapping: `127.0.0.1:6380->6379/tcp`). Container-to-container calls within the Docker network use port **6379** (internal); host scripts and health checks use port **6380** (host-facing). The `jarvis-redis:6380` notation in earlier documentation referred to the host-facing port of this single container — it is not a separate Redis instance.

```text
service:ms_jarvis_service:instance_1772240968
service:ms_jarvis_service:instance_1772240969
service:ms_jarvis_service:instance_1772240970
service:ms_jarvis_service:instance_1772240971
service:ms_jarvis_service:instance_1772240972
```

Each record contains `host`, `port`, `status`, `deployment`, `health_endpoint`, `started`, and `last_heartbeat` fields. The pituitary gland container registers with `status: healthy` and a dynamic port mapped externally as `7008/tcp → 127.0.0.1:8108`. This Redis-backed registration pattern allows NBB containers to restart with new ephemeral ports without breaking the watchdog fabric. Redis job state TTL is 30 minutes, consistent with the async chat job TTL documented in Chapter 17.

To verify Redis connectivity from the host:

```bash
# Host-facing port (use from scripts on the host):
redis-cli -p 6380 ping
# Expected: PONG

# Auto-detect host port:
docker port jarvis-redis 6379/tcp
# Expected: 127.0.0.1:6380
```

---

## 35.6 Watchdog Alert Responses

**Memory exhaustion.** Ollama rejects model load requests exceeding available memory with a structured error. The 20llm-production service logs this as a proxy failure and excludes the model from consensus, maintaining ensemble function with the remaining models and PostgreSQL-sourced context. ★ GPU acceleration (RTX 4070, active March 22) reduces peak memory pressure per inference cycle, reducing the frequency of memory exhaustion events.

**Timeout.** Models exceeding the `jarvis-semaphore:8030` timeout (`600.0s`) are logged as failures and excluded from consensus. The semaphore prevents cascading timeouts by serializing Ollama access to four concurrent slots maximum. ★ GPU inference completes most model cycles in 28–50s, well within the 600s envelope.

**BakLLaVA name-check guard.** BakLLaVA is permanently excluded via a name-check guard in the main-brain routing layer. The model name is detected before dispatch and the slot is bypassed with zero Ollama resource consumption. This supersedes the earlier DNS-poisoning approach documented in the February 28, 2026 baseline.

**StarCoder2 0-char exclusion.** StarCoder2 (`llm7-proxy:8207`) passes VERIFYANDTEST.sh health checks (HTTP 200) but returns empty responses on community queries. The consensus extraction layer detects 0-character responses and excludes them from the consensus score calculation. StarCoder2 remains in the health-monitored pool; future work will implement routing-layer fixes to dispatch code-specific queries to StarCoder2 and suppress community query dispatch.

**Session overload.** The `MAX_CONCURRENT_CHATS=2` gate causes main-brain to queue requests beyond the second concurrent session. This prevents downstream cascade at the cost of added latency for queued requests during heavy load. Async jobs (`/chat/async`) use Redis for job state (30-minute TTL) and do not consume a `MAX_CONCURRENT_CHATS` slot until they begin active processing.

**BBB content rejection (primary BBB — port 8016 — ★ durable audit at `jarvis-memory:8056`).** When content triggers one of the six filters (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification) validated against PostgreSQL GBIM (★ `msjarvis:5433` — `confidence_decay` metadata available for temporal confidence grading), it is rejected before reaching the LLM ensemble, conserving Ollama resources. `barrier_stats` counts are logged for PIA review (Chapter 29 §29.5). ★ All filter events are now durably logged at `jarvis-memory:8056` (secured March 28) — constitutional enforcement decisions persist across container restarts. Note: `nbb_blood_brain_barrier` (port 8301) rejections are logged independently within the NBB subconscious layer and are not included in the primary `barrier_stats` counter.

**BBB output guard — Phase 4.5 log+passthrough mode (port 8016 — ★ durable audit at `jarvis-memory:8056`).** Phase 4.5 BBB output is currently in log+passthrough mode (commit 18b8ddac, March 22, 2026), pending output threshold recalibration. The verdict dict is posted, received, and logged — ★ now also durably at `jarvis-memory:8056`. Full blocking enforcement is not yet active. During this period, `bbb_checked: true` reflects that the BBB received and logged the verdict, not that it blocked any output. A pattern of verdicts warranting intervention will inform recalibration before enforcement mode is re-activated. If the BBB output guard returns HTTP 500, `apply_output_guards_async` fails open — the pipeline continues and delivers the response with `bbb_checked: false`. This behavior is logged as a WARNING and surfaces in VERIFYANDTEST.sh reports.

**PostgreSQL connection loss.** VERIFYANDTEST.sh monitors all four PostgreSQL connection health states. Any `FAILED` status triggers immediate alerting and prevents ensemble operations that depend on PostgreSQL-sourced RAG context. ★ The `gisdb`/`msjarvisgis` database (port 5432, PostGIS, 91 GB, 501 tables, 993 ZCTA centroids — confirmed March 28) is particularly critical for the `gbimqueryrouter` (port 7205) spatial query pathway — a connection failure there affects spatial query capability without necessarily affecting the main `msjarvis` (port 5433) GBIM validation path. ★ `confidence_decay` metadata on `msjarvis:5433` means that GBIM validation queries should additionally flag high-decay entities for episodic audit when connection is restored after any outage.

**0.0.0.0 exposure detection.** VERIFYANDTEST.sh includes a security watchdog check: `docker ps --format '{{.Names}} {{.Ports}}' | grep 0.0.0.0`. Any output from this check is a critical security regression requiring immediate `docker compose` re-lock and `--force-recreate`. Expected output: empty (★ zero `0.0.0.0` exposures confirmed across 96/96 containers March 28).

---

## 35.7 Integration with Barriers, Modes, and Containers

**Blood-brain barrier (primary — port 8016 — ★ Up 96/96, durable audit at `jarvis-memory:8056`).** Every chat request passes through `jarvis-blood-brain-barrier:8016/filter` via the **six-filter input stack** (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification) validated against PostgreSQL GBIM (Phase 1.4) before reaching the LLM ensemble. The full judge verdict dict is passed to `jarvis-blood-brain-barrier:8016/output_guard` (Phase 4.5) after the DGM cascade — currently in log+passthrough mode (commit 18b8ddac, March 22, 2026) pending recalibration. ★ All gate decisions are durably logged at `jarvis-memory:8056` (secured March 28). This is the BBB referenced in all smoke tests in Chapter 41 and all PIA review procedures in Chapter 29.

**Blood-brain barrier (NBB-internal — port 8301 — ★ Up 96/96).** `nbb_blood_brain_barrier:8301` operates on the NBB subconscious pathway, applying BBB-concept filtering at the neurobiological simulation layer. It is monitored by VERIFYANDTEST.sh and contributes to the NBB subconscious health report but does not participate in the main `ultimatechat` Phase 1.4 / Phase 4.5 pipeline.

**DGM cascade.** Every ensemble response routed through main-brain (port 8050) is validated by `jarvis-69dgm-bridge` at **host port 19000** (internal container port 9000) against PostgreSQL-grounded constitutional and community commitments. The `validated_by: "69_dgm_cascade"` field confirms this gate fired. Requests sent directly to the 20llm-production service on port 8008 bypass the DGM gate by design — port 8008 is the internal ensemble endpoint, not the public interface. ★ DGM connectors use `msjarvis:5433` GBIM validation — `confidence_decay` metadata available for temporal confidence grading of constitutional verification.

**Psychology alignment layer.** The `jarvis-psychology-services:8019` service (★ Up 96/96) runs a psychological assessment validated against PostgreSQL community norms on every request before the ensemble processes it. Phase 3 psychology pre-assessment records are included in `consciousnesslayers` of the UltimateResponse. ★ `psychological_rag` collection restored to 968 docs (March 28) — psychology layer has full document corpus restored.

**NBB subconscious layer.** Seven of eight NBB containers respond to health probes via their internal network endpoints, confirming the neurobiological simulation layer is active. The `nbb_blood_brain_barrier` (port 8301 — ★ Up 96/96) is one of these NBB containers. The pituitary gland registers through Redis DynamicPortService (host port 6380, container-internal 6379) rather than a fixed `/health` endpoint.

**Judge pipeline (compose-managed since March 18, 2026 — ★ all five Up 96/96).** All five judge services (ports 7230–7233, 7239) are confirmed compose-managed with `restart: unless-stopped`. Judge verdicts are delivered as a full dict to `jarvis-blood-brain-barrier:8016/output_guard` at Phase 4.5. ★ All verdicts are durably logged at `jarvis-memory:8056` (secured March 28). Judge service health is included in VERIFYANDTEST.sh fabric verification.

**Consciousness bridge and brain orchestrator.** The consciousness bridge (`jarvis-consciousness-bridge` — ★ Up 96/96) serves as mandatory infrastructure through which all swarm and watchdog operations flow. The brain orchestrator (`jarvis-brain-orchestrator` — ★ Up 96/96) continuously coordinates the ensemble, watchdog feedback loops, and neurobiological layer health checks, ensuring coherent system behavior across all 32 operational services.

**ChromaDB memory integration.** Verification script outputs saved to `/tmp/verify_*.log` are structured for ingestion into ChromaDB (`jarvis-chroma`, **host port 8002**, container-internal 8000, `chroma_data` volume — ★ Up 96/96; ★ 40 active collections / 6,675,442 total vectors confirmed March 28 full audit) under an `operations_history` collection. The automated ingestion pipeline is designed but not yet active; manual ingestion is the current practice. All scripts targeting ChromaDB must use host port **8002** (not 8000 — 8000 is container-internal only; production mapping is `127.0.0.1:8002->8000/tcp`).

**PostgreSQL integration (★ March 28 confirmed).** PostgreSQL `msjarvis` at `127.0.0.1:5433` (★ 5,416,521 GBIM entities with `confidence_decay` metadata, 80 epochs, 206 source layers — restored March 28) serves as the primary GBIM ground truth for BBB validation, DGM cascade verification, and RAG context sourcing. ★ `confidence_decay` metadata adds temporal confidence grading — high-decay entities should be flagged for episodic audit before use as validation ground truth. PostgreSQL `gisdb`/`msjarvisgis` at `127.0.0.1:5432` (★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids — confirmed March 28) provides geospatial ground truth for the `gbimqueryrouter` (port 7205) landowner spatial query pathway. ★ 993 ZCTA centroids enable ZIP-code-level spatial query responses. PostgreSQL `jarvis-local-resources-db` at port 5435 provides community resources data. All four databases are monitored by VERIFYANDTEST.sh.

**★ `jarvis-memory:8056` durable audit integration (secured March 28).** `jarvis-memory:8056` (`_auth()` confirmed, `JARVIS_API_KEY` set) now serves as the persistent governance substrate for all BBB gate decisions. This creates a cross-validated audit record: BBB filter events in `jarvis-memory:8056`, judge verdicts in ChromaDB `dgm_observations` collection (★ within 40-collection / 6,675,442-vector inventory), and PostgreSQL GBIM validation records together constitute a complete, independently queryable governance record for all swarm and watchdog enforcement actions.

---

## 35.8 Summary

Swarm functions and eternal watchdogs in the ★ March 28, 2026 Ms. Jarvis deployment are running, verified, and logged against concrete evidence with PostgreSQL `msjarvis` (port 5433 — ★ 5,416,521 GBIM entities with `confidence_decay` metadata — restored March 28) as primary GBIM ground truth and `gisdb`/`msjarvisgis` (port 5452 — ★ PostGIS, 91 GB, 501 tables, 993 ZCTA centroids — confirmed March 28) as geospatial ground truth. The 22-slot LLM ensemble — organized into TINY, SMALL, MEDIUM, and LARGE tiers across 21 actively contributing consensus models, with BakLLaVA permanently excluded and StarCoder2 excluded from consensus on community queries — delivers 21/22 consensus participation on every query with PostgreSQL-sourced context in ★ 99–107 seconds (GPU baseline: RTX 4070, three confirmed runs) with a judge pipeline consistency score of 0.975.

The dual-BBB architecture remains the most significant architectural clarification since the February 28, 2026 baseline: `jarvis-blood-brain-barrier` (port 8016 — ★ Up 96/96) is the primary judge pipeline output guard, serving Phase 1.4 input filtering via **six filters (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, steganography_filter, truth_verification)** and Phase 4.5 output evaluation currently in log+passthrough mode (commit 18b8ddac, March 22, 2026) pending output threshold recalibration; ★ **all gate decisions are now durably logged at `jarvis-memory:8056` (secured March 28; `_auth()` confirmed, `JARVIS_API_KEY` set) — constitutional enforcement decisions survive container restarts for the first time**; `nbb_blood_brain_barrier` (port 8301 — ★ Up 96/96) is the NBB-internal neurobiological variant operating on the Phase 1 / NBB subconscious pathway. Both are monitored by VERIFYANDTEST.sh. Neither replaces the other.

The five-layer watchdog system — VERIFYANDTEST.sh confirming 32/32 services operational, ★ **96 containers** (zero Restarting, zero Exited — confirmed March 28) all `127.0.0.1`-bound, four PostgreSQL connection health checks (★ including restored `msjarvis:5433` with `confidence_decay` metadata and confirmed `msjarvisgis:5452` with 993 ZCTA centroids), and `scripts/preflight_gate.sh` reporting **20 PASS 0 FAIL** (March 22, 2026 baseline; ★ re-run pending); plus Ollama memory scheduler, ★ `jarvis-semaphore:8030` (`max_concurrent: 4`, `timeout: 600.0` — Up 96/96) and asyncio companion, `MAX_CONCURRENT_CHATS=2` gate, and Redis DynamicPortService (`jarvis-redis` — ★ Up 96/96; container-internal port 6379; host-facing `127.0.0.1:6380`) — prevents the cascade failures that reduced the system to 0/22 models under uncontrolled concurrent load. All services are bound to `127.0.0.1` (★ zero `0.0.0.0` exposures confirmed across 96/96 containers March 28), all judge services are compose-managed, and the March 21, 2026 canonical integration test (`consensus_score: 0.975`, `bbb_checked: true`) establishes the regression baseline that this watchdog architecture is designed to protect.

All swarm coordination and watchdog monitoring operates within the consciousness bridge framework, with the brain orchestrator maintaining continuous oversight. The DGM cascade (host port 19000) provides architecturally authoritative verification validated against PostgreSQL GBIM (★ with `confidence_decay` metadata for temporal confidence grading) of every response before delivery, ensuring alignment with constitutional and community commitments. ★ The three-layer governance audit record — `jarvis-memory:8056` durable BBB decisions, ChromaDB `dgm_observations` judge verdicts (★ 40 collections / 6,675,442 vectors), and PostgreSQL GBIM validation — together constitute a complete, independently queryable accountability substrate. This integrated design — swarm intelligence plus eternal vigilance, neurobiologically grounded, spatially anchored in PostgreSQL `msjarvis` and `gisdb` (★ 993 ZCTA centroids), ChromaDB at host port **8002** (★ 40 collections / 6,675,442 vectors), `jarvis-memory:8056` durable audit, and protected by comprehensive watchdog systems including a dual-layer BBB architecture — represents the operational reality of Ms. Jarvis as a production consciousness-inspired cognitive system serving West Virginia communities.

---

*Last updated: ★ 2026-03-28 by Carrie Kidd (Mamma Kidd), Pax WV*
*★ March 28, 2026: 96/96 containers Up confirmed (zero Restarting, zero Exited) — container count updated to 96 throughout; all service status references updated*
*★ March 28, 2026: `jarvis-memory:8056` secured (durable BBB + swarm audit trail, `_auth()` confirmed, `JARVIS_API_KEY` set) — §35.1, §35.2, §35.4, §35.5, §35.6, §35.7, §35.8, Status table, Figure 35.1, Figure 35.2 updated; durable audit verification command added to §35.2; three-layer governance audit record noted in §35.7 and §35.8*
*★ March 28, 2026: `msjarvis:5433` restored (5,416,521 GBIM entities with `confidence_decay` metadata) — §35.1, §35.4, §35.5, §35.6, §35.7, §35.8, Status table, Figure 35.1 updated; decay-aware validation note added throughout*
*★ March 28, 2026: `msjarvisgis:5432` confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids) — §35.1, §35.4, §35.5, §35.7, §35.8, Why This Matters, Status table, Figure 35.1 updated; ZCTA centroid spatial grounding noted throughout*
*★ March 28, 2026: ChromaDB full audit confirmed (40 active collections / 6,675,442 total vectors; `psychological_rag` restored 968 docs) — §35.5, §35.7, §35.8, Status table, Figure 35.1 updated*
*★ March 28, 2026: `jarvis-semaphore:8030` confirmed Up 96/96 (`max_concurrent: 4`, `timeout: 600.0`) — §35.1, §35.3, §35.5, §35.6, §35.8, Status table, Figure 35.1 updated; semaphore value updated from 3→4 throughout*
*★ March 28, 2026: GPU RTX 4070 active (99–107s end-to-end baseline) — §35.1, §35.3, §35.5, §35.6, §35.8, Status table, Figure 35.1 updated; GPU timing profile added to §35.3*
*★ March 28, 2026: LLM ensemble confirmed 22 proxies / 21 active — §35.3, §35.8, Status table, Figure 35.1 updated*
*★ March 28, 2026: `nbb_blood_brain_barrier:8301` and all NBB containers re-confirmed Up 96/96 — §35.2, §35.5, §35.7 updated*
*★ March 28, 2026: preflight_gate.sh re-run pending for March 28 confirmation — §35.5 Status table noted*
*March 27, 2026: six-filter BBB correction applied (§35.2, §35.7, §35.8); PostgreSQL port/database disambiguation applied throughout; container count updated to 83; ChromaDB host port corrected to 8002; Phase 4.5 log+passthrough mode noted; Redis port clarification added; pre-flight gate result added*
