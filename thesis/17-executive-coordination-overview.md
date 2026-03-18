> **Why this matters for Polymathmatic Geography**
> This chapter provides the empirical grounding for all architectural claims made across the thesis. It supports:
> - **P1 – Every where is entangled** by measuring the actual cost of entangling spatial, semantic, community memory, and neurobiological services on a single commodity host — demonstrating that a geographically rooted AI system can achieve full-pipeline operation even on hardware typical of a rural nonprofit.
> - **P3 – Power has a geometry** by making the per-phase timing profile visible, showing exactly which stages account for latency and where optimization pressure should be directed.
> - **P5 – Design is a geographic act** by showing that design decisions — merging Phase 3.5/3.75, switching judge payload to consensus-only, adding health-check caching, converting compose to image-based — have measurable geographic consequences: a system that can be rebooted and fully operational in two commands is a system a community organization can actually steward.
> - **P12 – Intelligence with a ZIP code** by documenting that 21 models, three PostgreSQL databases, 21,181 community memories, and 5,416,521 GBIM entities all operate on a Lenovo Legion 5 in a home office in Oak Hill, West Virginia.
> - **P16 – Power accountable to place** by publishing the benchmark methodology, the exact query used, the hardware envelope, and the per-phase timing so that future operators and researchers can reproduce, audit, and improve upon these measurements.
>
> As such, this chapter belongs to the **Empirical Evidence** tier: it converts architectural claims into falsifiable, reproducible measurements anchored to a specific place, time, and hardware configuration.

---

# 39. Operational Evaluation

This chapter presents the empirical operational evaluation of the Ms. Egeria Jarvis ULTIMATE system as deployed on the reference hardware configuration at Oak Hill, West Virginia, as of March 18, 2026. It documents end-to-end response time benchmarks, per-phase timing profiles, container management infrastructure, and the optimizations applied during the March 16–18, 2026 sessions that moved the system from a 532-second pre-optimization baseline to an approximately 436-second measured pipeline.

All measurements reflect CPU-only inference on the Lenovo Legion 5 reference host. GPU-accelerated inference via the WVU partnership server remains pending and is expected to reduce Phase 2.5 (LLM ensemble) from ~320–360 seconds to a significantly lower floor.

---

## 39.1 Reference Hardware and Software Environment

All benchmarks reported in this chapter were produced on the following configuration:

| Component | Specification |
|---|---|
| **Host** | Lenovo Legion 5 (16IRX9) |
| **CPU** | Intel Core i9 |
| **GPU** | NVIDIA RTX 4050 — present but not used for inference |
| **RAM** | 29 GB system RAM |
| **Inference mode** | CPU-only — `size_vram: 0` on all Ollama models |
| **Ollama container memory limit** | 20 GB |
| **Operating system** | Linux (Docker host) |
| **Docker Compose version** | v5.1.0 (upgraded March 17, 2026 from v1.29.2) |
| **Active containers** | 79 (fully compose-managed as of March 17, 2026) |
| **PostgreSQL `msjarvis`** | port 5433 — 5,416,521 GBIM entities, 80 epochs, 206 source layers |
| **PostgreSQL `gisdb`** | port 5433 — PostGIS, 13 GB, 39 tables, 993 ZCTA centroids |
| **PostgreSQL `jarvis-local-resources-db`** | port 5435 — community resources |
| **ChromaDB** | port 8000 — `chroma_data` volume, 384-dim (`all-minilm:latest`) |
| **`autonomous_learner` collection** | 21,181 records (growing ~288/day) |
| **Location** | Oak Hill / Mount Hope, West Virginia |

> **GPU status note:** The NVIDIA RTX 4050 is present but all inference runs CPU-only (`size_vram: 0` on every Ollama model). The path to GPU-accelerated inference is the WVU partnership server, currently pending. All benchmarks in this chapter reflect the CPU-only performance envelope and represent a conservative floor.

---

## 39.2 End-to-End Benchmark

### 39.2.1 Primary Benchmark (March 18, 2026)

| Metric | Value |
|---|---|
| **Benchmark date** | March 18, 2026 |
| **Query** | "What community resources are available in Fayette County, WV?" |
| **Pipeline** | Full 9-phase ULTIMATE pipeline |
| **All phases approved** | Yes |
| **End-to-end response time** | **~436 seconds** |
| **Pre-optimization baseline** | 532 seconds (before March 16–18 optimizations) |
| **Time saved by optimizations** | ~96 seconds (~18% improvement) |

### 39.2.2 Historical Benchmark (March 15, 2026, commit `b90f9ff`)

| Metric | Value |
|---|---|
| **Benchmark date** | March 15, 2026 |
| **Query** | "What community resources are available in Fayette County, WV?" |
| **End-to-end response time** | 349.87 seconds |
| **Phases** | 9-phase pipeline; Phase 1.45 and merged Phase 3.5/3.75 not yet deployed |
| **LLM models** | 22/22 HTTP 200 (StarCoder2 still counted; consensus extraction issue not yet flagged) |

> **Note on the apparent regression:** The March 18 benchmark (~436s) is higher than the March 15 benchmark (349.87s) because the pipeline is **richer**, not slower. Phase 1.45 community memory retrieval, the merged LM Synthesizer persona synthesis, and the consensus-only judge optimization were all absent on March 15. The March 15 figure represents a less complete pipeline. The March 16–18 sessions first revealed the actual full-pipeline cost (532s) and then optimized it to ~436s. The 349.87s figure should be understood as a partial-pipeline measurement.

---

## 39.3 Phase-by-Phase Timing Profile

The following table documents the wall-clock cost of each phase of the full 9-phase pipeline as measured on the reference hardware (March 18, 2026, CPU-only inference, full community-memory-enriched prompt):

| Phase | Description | Wall-clock cost |
|---|---|---|
| **Phase 1** | Service discovery + prefrontal planning (health cache: 30s TTL, 2s timeout/service) | ~0.7s (cached after first query) |
| **Phase 1.4** | BBB 7-filter input stack (EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection, SteganographyDetection, TruthVerification, ContextAwareness; fail-open on HTTP 500; `truth_score` null guard) | ~1.3s total (incl. Phase 1.45) |
| **Phase 1.45** | Semantic community memory retrieval — `all-minilm:latest` (384-dim) → `autonomous_learner` (21,181 records) → top-5 prepended to `enhanced_message` | Included in Phase 1.4 total |
| **Phase 1.75–3 (pre-LLM)** | Truth verdict (BBB port 8016) + psychology pre-assessment (port 8019) + consciousness layers | ~0.5s |
| **Phase 4** | RAG context building — `jarvis-spiritual-rag` (port 8005) querying PostgreSQL `msjarvis` + `gisdb` + `jarvis-local-resources-db` + ChromaDB + `psychological_rag_domain`; web research (internal) | Included in Phase 1.75–3 total |
| **Phase 2.5** | 21-model LLM ensemble synthesis — semaphore proxy (port 8030) → `jarvis-20llm-production` (port 8008), rich prompt, CPU-only | **~320–360s** (hardware floor) |
| **Phase 3 (post-LLM)** | 4-judge pipeline (consensus answer only; `raw_responses` dump eliminated; ports 7230–7233) | **~60–86s** (reduced from ~85–100s) |
| **Phase 3.5** | LM Synthesizer + Voice Delivery (merged; `jarvis-ollama:11434/api/generate`, `llama3.1:latest`, Ms. Jarvis persona; Phase 3.75 eliminated) | **~30–55s** (saves ~40s vs. two-pass) |
| **Phase 7 + Phase 4.5** | 69-DGM cascade (port 9000) + BBB output guard (port 8016, 8.0s timeout, fail-open) | ~0.5s |
| **Phase 5 + post-processing** | Confidence decay multiplier + `normalize_identity` + `background_rag_store` (async) | ~0.5s |
| **Total** | Full 9-phase pipeline | **~436s** |

### 39.3.1 Optimization History

| Optimization | Applied | Time saved |
|---|---|---|
| Judge pipeline consensus-only (eliminated `raw_responses` dump) | March 16, 2026 | ~15–20s per query |
| Phase 3.5 + Phase 3.75 merged into single Ollama call | March 18, 2026 | ~40s per query |
| Health check caching (30s TTL, 2s timeout) | March 18, 2026 | ~0.7s after first query |
| BBB fail-open on HTTP 500 (eliminates hang on BBB errors) | March 18, 2026 | eliminates hangs |
| Judge URL corrections (7239 → 7230/7231/7232/7233) | March 16, 2026 | eliminates silent judge failures |
| LM Synthesizer URL fix (`jarvis-roche-llm` → `jarvis-ollama:11434`) | March 18, 2026 | eliminates Phase 3.5 errors |
| **Total measured improvement** | March 16–18, 2026 | **~96s (~18%)** |

### 39.3.2 Remaining Hardware Floor

The dominant cost — **~320–360 seconds** — is Phase 2.5: the 21-model LLM ensemble running CPU-only inference on the Legion 5. This is a hardware floor, not a software optimization target. The LLM ensemble wall clock varies with:

- **Prompt size:** Direct calls to port 8008 with short prompts complete in ~110s. The full pipeline uses a community-memory-enriched, RAG-grounded prompt that is substantially longer, driving the ~320–360s range.
- **Semaphore queuing:** With `max_concurrent: 4` in the semaphore proxy, back-to-back requests accumulate. The semaphore should be drained between benchmark runs.
- **Hardware bottleneck:** `size_vram: 0` on all models confirms no GPU acceleration. The path to sub-120s ensemble times is the WVU partnership GPU server (pending).

---

## 39.4 Container Infrastructure

### 39.4.1 Docker Compose Upgrade

| Aspect | Previous state (March 15, 2026) | Current state (March 18, 2026) |
|---|---|---|
| **Docker Compose version** | v1.29.2 | **v5.1.0** |
| **Upgrade driver** | v1.29.2 produced `ContainerConfig` crash bug on startup | v5.1.0 eliminates crash bug |
| **Compose file** | `~/msjarvis-rebuild-working/msjarvis-rebuild/docker-compose.yml` | Same path, updated content |
| **`build:` directives** | Present on most services — rebuilt images on every `docker compose up` | **All `build:` entries converted to `image:` references** — no rebuild on startup |
| **Container startup time** | Variable; rebuilds added minutes on first `up` | Deterministic — image pulls if missing, runs if present |

> **The `build:` → `image:` conversion is a critical operational change.** Prior to March 17, running `docker compose up -d` would trigger image rebuilds for most services, making startup slow and unpredictable. All 79 containers now reference pre-built images. `docker compose up -d` simply starts containers using existing images. This makes the system reboot-safe: after a power cycle or crash, the verified two-command reboot sequence restores the full 79-container system without rebuilding anything.

### 39.4.2 Hash-Prefixed Container Names — Fixed

Eight containers previously received Docker-assigned hash-prefixed names (for example, `981f44e18cf6_jarvis-20llm-production`) rather than clean, human-readable names. This made log inspection, `docker exec` commands, and health checks fragile and error-prone.

| Fix applied | March 17–18, 2026 |
|---|---|
| **Method** | `container_name:` added to all 8 affected service entries in `docker-compose.yml` |
| **Affected containers** | `jarvis-20llm-production` and 7 others previously hash-prefixed |
| **Result** | All 79 containers now have clean, stable names |
| **Verification** | `docker ps --format '{{.Names}}'` shows no hash-prefixed entries |

### 39.4.3 Previously Missing Containers Added

| Category | Previous state | Current state |
|---|---|---|
| **Services requiring manual startup** | 6 containers (judges + 69dgm bridge) started manually | All 6 managed by `~/jarvis_startup.sh` with retry logic |
| **Corpus containers** | 3 not in compose (`jarvis-local-resources`, etc.) | All corpus containers in compose permanently |
| **Missing service containers** | 6 missing (`jarvis-hippocampus`, `jarvis-gis-rag`, `jarvis-spiritual-rag`, etc.) | All 6 added with correct `image:` references |
| **Total compose-managed** | ~70 of 79 containers | **All 79 containers** |

### 39.4.4 Verified Reboot Sequence

```bash
# Step 1: Start all 79 compose-managed containers
cd ~/msjarvis-rebuild-working/msjarvis-rebuild && docker compose up -d

# Step 2: Start and verify the six pipeline containers
~/jarvis_startup.sh
```

**Go signal — six green checkmarks from `~/jarvis_startup.sh`:**
- `jarvis-judge-truth` ✅
- `jarvis-judge-consistency` ✅
- `jarvis-judge-alignment` ✅
- `jarvis-judge-ethics` ✅
- `jarvis-judge-pipeline` ✅
- `jarvis-69dgm-bridge` ✅

The startup script uses `docker exec` with Python `urllib` internally for health verification (these six containers do not expose ports to the host). It includes retry logic to wait for each container to become healthy before proceeding.

---

## 39.5 ChromaDB Collection State (March 18, 2026)

| Collection | Record count | Notes |
|---|---|---|
| `gbim_worldview_entities` | 5,416,521 | Complete WV GBIM spatial corpus; unchanged |
| `autonomous_learner` | 21,181 | Growing ~288/day; queried at Phase 1.45 |
| `psychological_rag` | 968 | Unchanged |
| `spiritual_texts` | 23 | Unchanged |
| `appalachian_cultural_intelligence` | 5 | New — not previously documented |
| `GBIM_sample_rows` | 5,000 | New — not previously documented |
| `GBIM_sample` | 3 | New — not previously documented |
| `msjarvis-smoke` | 1 | New — smoke test record |
| `msjarvis_docs` | 0 | Scaffolded — pending ingest |
| `GBIM_Fayette_sample` | 0 | Scaffolded — pending ingest |
| `geospatialfeatures` | 0 | Scaffolded — pending ingest |

> **All collections use 384-dimensional vectors (`all-minilm:latest`).** The `nomic-embed-text` model produces 768-dimensional vectors and is incompatible with all existing collections. The `_DummyCollection` error that previously prevented semantic retrieval is resolved by the `all-minilm:latest` implementation deployed March 17, 2026.

---

## 39.6 LLM Ensemble State (March 18, 2026)

| Proxy | Port | Model | Active status |
|---|---|---|---|
| llm1-proxy | 8201 | TinyLlama (`tinyllama:latest`) | ✅ Active |
| llm2-proxy | 8202 | Gemma (`gemma:2b`) | ✅ Active |
| llm3-proxy | 8203 | MedLlama2 (`medllama2:latest`) | ✅ Active |
| llm4-proxy | 8204 | MiniCPM-V (`minicpm-v:latest`) | ✅ Active |
| llm5-proxy | 8205 | LLaVA (`llava:latest`) | ✅ Active |
| llm6-proxy | 8206 | SQLCoder (`sqlcoder:latest`) | ✅ Active |
| llm7-proxy | 8207 | StarCoder2 (`starcoder2:latest`) | ⚠️ Returns 0-char on community queries |
| llm8-proxy | 8208 | CodeLlama (`codellama:latest`) | ✅ Active |
| llm9-proxy | 8209 | DeepSeek Coder (`deepseek-coder:latest`) | ✅ Active |
| llm10-proxy | 8210 | Phi3 Mini (`phi3:mini`) | ✅ Active |
| llm11-proxy | 8211 | (verify against `llm_consensus_20_FINAL.py`) | ✅ Active |
| llm12-proxy | 8212 | Dolphin-Phi (`dolphin-phi:latest`) | ✅ Active |
| llm13-proxy | 8213 | Orca-Mini (`orca-mini:latest`) | ✅ Active |
| llm14-proxy | 8214 | Qwen2 (`qwen2:latest`) | ✅ Active |
| llm15-proxy | 8215 | Zephyr (`zephyr:latest`) | ✅ Active |
| llm16-proxy | 8216 | Starling-LM (`starling-lm:latest`) | ✅ Active |
| llm17-proxy | 8217 | Neural-Chat (`neural-chat:latest`) | ✅ Active |
| llm18-proxy | 8218 | OpenChat (`openchat:latest`) | ✅ Active |
| llm19-proxy | 8219 | Vicuna (`vicuna:latest`) | ✅ Active |
| llm20-proxy | 8220 | LLaMA 2 (`llama2:latest`) | ✅ Active |
| llm21-proxy | 8221 | Mistral (`mistral:latest`) | ✅ Active |
| llm22-proxy | 8222 | LLaMA 3.1 (`llama3:latest`) | ✅ Active |

**Active count: 21 of 22 proxies.** StarCoder2 (llm7-proxy, port 8207) is wired and responds HTTP 200 but returns 0-character response bodies on community-domain queries; the consensus extraction logic excludes 0-length responses automatically. The March 15 benchmark reported "22/22 HTTP 200" because the 0-char issue had not yet been identified; the accurate active count for community query consensus is **21**.

**LM Synthesizer (Phase 3.5):** Calls `jarvis-ollama:11434/api/generate` directly with `model: llama3.1:latest` and the Ms. Egeria Jarvis persona prompt injected. Previously incorrectly wired to `jarvis-roche-llm` (returned HTTP 500 on every Phase 3.5 call); fixed March 18, 2026.

---

## 39.7 Known Issues and Resolution Status (March 18, 2026)

| Issue | Status as of March 18 |
|---|---|
| Response truncation (~730 chars, `max_tokens: 500`) | ✅ FIXED — `max_tokens` set to -1 (unlimited); `llm22-proxy` has 8,192-token limit |
| ChromaDB `_DummyCollection` error blocking semantic retrieval | ✅ FIXED — `all-minilm:latest` semantic retrieval implemented |
| Redis response persistence (in-memory only) | ✅ FIXED — Redis-backed job system with 30-min TTL deployed |
| 33 services not in docker-compose | ✅ FIXED — all 79 containers now in compose |
| Idempotency TTL in-memory only | ✅ FIXED — Redis-backed, 1,800s TTL |
| Judge pipeline URL wrong (7239) | ✅ FIXED — corrected to 7230/7231/7232/7233 (March 16) |
| LM Synthesizer calling `jarvis-roche-llm` | ✅ FIXED — calls `jarvis-ollama:11434` directly (March 18) |
| NBB Prefrontal Cortex 422 errors | ✅ RESOLVED — `message` field payload confirmed correct; service healthy |
| I-Containers 422 errors | ✅ RESOLVED — port corrected to 8015 |
| BBB `truth_score` `KeyError` | ✅ FIXED — null guard added to BBB orchestrator (March 18) |
| BBB blocking on HTTP 500 errors | ✅ FIXED — fail-open behavior on non-200 BBB responses (March 18) |
| `web-research` and `rag-server` container restart loops | ✅ FIXED — source files deployed via `docker cp` |
| Hash-prefixed container names | ✅ FIXED — `container_name:` added to all 8 affected containers (March 17–18) |
| Docker Compose `ContainerConfig` crash bug | ✅ FIXED — upgraded to v5.1.0 from v1.29.2 (March 17) |
| `build:` directives causing slow startup | ✅ FIXED — all converted to `image:` references (March 17) |
| Hallucination from LLMs on community resources (Mount Hope, local nonprofits) | 🔴 OPEN — `gis_rag` and `local_resources` return empty for Mount Hope queries; LLMs generating from training data. Factually accurate programs (LIHEAP, WV 2-1-1) pass BBB. Fabricated organization names blocked by ethical filter. Root cause: real community resource data not yet loaded into verified databases. Resolution: Community Champions data entry is next priority. |
| BBB ethical filter blocking "certainly" | BY DESIGN — ethical filter correctly detecting unverified specific claims; not a false positive |

---

## 39.8 Async Job API State (March 18, 2026)

The Redis-backed async job system deployed March 17, 2026, provides non-blocking access to the full 9-phase pipeline:

| Endpoint | Method | Function |
|---|---|---|
| `/chat/async` | POST | Create async job — returns `job_id` immediately |
| `/chat/status/{job_id}` | GET | Poll for progress and result |
| `/chat/cancel/{job_id}` | DELETE | Cancel specific job — true asyncio task cancellation |
| `/chat/cancel/all` | DELETE | Cancel all running jobs |

**Implementation details:**

- Job state stored in Redis (`jarvis-redis:6379`) with **30-minute TTL**
- State **survives `jarvis-main-brain` container restarts** (Redis persists independently)
- `DELETE /chat/cancel/{job_id}` performs **true asyncio task cancellation** — the 21-LLM pipeline stops immediately mid-run via `_job_tasks[job_id].cancel()`
- `active_jobs` dictionary replaced by Redis-backed store (in-memory-only limitation is resolved)

---

## 39.9 Evaluation Against Thesis Claims

This section cross-references the empirical measurements in this chapter against specific architectural and theoretical claims made elsewhere in the thesis.

**Claim: Full 9-phase pipeline is implementable on commodity hardware.**  
**Status: Confirmed.** ~436s end-to-end on a Lenovo Legion 5 (CPU-only inference). All 9 phases execute without errors on the reference host. The system is operationally deployable by a rural nonprofit with standard consumer hardware.

**Claim: Community memory enrichment (Phase 1.45) grounds every response in accumulated community intelligence.**  
**Status: Confirmed.** 21,181 `autonomous_learner` records are semantically queried on every request via `all-minilm:latest` (384-dim). Top-5 matching memories are prepended to `enhanced_message` before LLM processing. Growing at ~288 records/day.

**Claim: GBIM beliefs (5,416,521) provide temporal confidence decay for all responses.**  
**Status: Confirmed.** `confidence_decay` multiplier applied at Phase 5. All 5,416,521 entities carry `needs_verification=TRUE` at launch baseline — expected initial state; POC verification loop will clear flag as entities are confirmed.

**Claim: Three PostgreSQL databases provide authoritative grounding for WV-scoped queries.**  
**Status: Confirmed operationally; partially confirmed for community resources.** `msjarvis` (port 5433) and `gisdb` (port 5433) respond correctly in all benchmarks. `jarvis-local-resources-db` (port 5435) is confirmed in the pipeline but returns empty results for Mount Hope queries — real community resource data not yet loaded.

**Claim: System can be rebooted and fully operational with two commands.**  
**Status: Confirmed.** `docker compose up -d` + `~/jarvis_startup.sh` restores all 79 containers. Verified March 17, 2026.

**Claim: WV-first routing suppresses web context for WV-scoped queries.**  
**Status: Confirmed.** Main brain WV-scoped flag logic is operational; `web_context` excluded from context assembly when county + WV role detected; WV RAG + GIS + registry treated as authoritative.

**Claim: Response quality is limited by hallucination on local community resources.**  
**Status: Confirmed and open.** LLMs generate plausible but unverified local resource names for Mount Hope/Fayette County queries when `local_resources` database is empty. Factually accurate programs with external verification (LIHEAP, WV 2-1-1, New River Health) pass BBB. Fabricated specific organization names and locations are blocked by the ethical filter's deception-detection logic. This is the primary remaining quality gap as of March 18, 2026.

---

## 39.10 Performance Roadmap

| Milestone | Expected improvement | Dependency |
|---|---|---|
| GPU inference (WVU partnership server) | Phase 2.5: ~320–360s → target ~80–120s; total pipeline: ~436s → ~160–200s | WVU partnership activation |
| Community Champions data entry into `jarvis-local-resources-db` | Eliminates hallucination on local resource queries | Community volunteer coordination |
| `autonomous_learner` collection growth (21,181 → target 50,000+) | Richer Phase 1.45 community memory matching | Continuous autonomous learning (~288/day) |
| Persistent `active_jobs` store (Redis-backed, deployed March 17) | ✅ Complete — job state survives restarts | Deployed |
| Automated POC verification loop for GBIM `needs_verification=TRUE` entities | Progressive clearing of confidence decay floor | Future development |
| UI layer consuming `/chat/async` poll pattern | Non-blocking chat interface for community users | Future development |

*Last updated: 2026-03-18 by Carrie Kidd, Mount Hope WV*
