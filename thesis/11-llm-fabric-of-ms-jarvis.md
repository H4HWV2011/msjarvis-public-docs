# 11. The LLM Fabric of Ms. Allis

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: 2026-04-16 — SPRINT REWRITE — April 16 production state confirmed*

## Why This Matters for Polymathmatic Geography

This chapter shows how Ms. Allis's "thinking" is implemented as an organized fabric of local language models and services rather than a single opaque model instance. It supports:

- **P1 – Every where is entangled** by embedding LLMs inside a retrieval, entanglement, and spatial stack (ChromaDB v2 host port **8002** — ★ **48 collections, 6,740,034 vectors** as of April 16, 2026; `msallisgis` port 5432 ★: **45 GB PostGIS, 551 tables**; `allis-local-resources-db` port 5435: **64 verified resources, all 55 WV counties**; GBIM entity store: ChromaDB `gbim_worldview_entities` **5,416,521 vectors**; autonomous learner **21,181+ records**) that keeps reasoning tied to concrete places, institutions, and learning histories.

- **P3 – Power has a geometry** by routing questions through specific models, memories, and services whose connections — ports, proxies, ensembles, judges, and DGMs — have explicit topologies that can be inspected, tuned, or redesigned.

- **P5 – Design is a geographic act** by treating model choice, ensemble wiring, timeout and backlog settings, and service topology as design decisions that change how Appalachian realities are seen, narrated, and optimized over time.

- **P12 – Intelligence with a ZIP code** by grounding LLM calls in West Virginia-specific semantic and geospatial memory from ChromaDB `gbim_worldview_entities` (5,416,521 vectors — authoritative GBIM entity store), WV-entangled search, autonomous learner outputs, and I-container identity, rather than generic, placeless prompts.

- **P16 – Power accountable to place** by exposing LLMs only through glass-box HTTP services with confirmed ports, logs, and timeouts, so that every path from user question to model output can be audited and constrained.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the model pool, timeouts, ports, and service fabric that turn Quantarithmia's spatial-justice instruments into live, language-facing behavior. As of April 16, 2026, the fabric runs **21 active models** (22 proxies; BakLLaVA permanently disabled), operates within a **109-container fully compose-managed production stack** (★ all 27 preflight gates ✅ green; all services bound to `127.0.0.1`; zero `0.0.0.0` exposures), and is confirmed at **99–115 seconds end-to-end** on RTX 4070 GPU (confirmed **102.58s** April 16 — CPU 436s baseline **RETIRED STALE**). `BBB_OUTPUT_BLOCKING=true` active since April 6. `rag_grounded_v2` + `llm_judge_v3` active since April 3/6. `heuristic_contradiction_v1` **RETIRED**. ML-DSA-65 FIPS 204 signing active across all 5 judge containers. EEG Delta (8073), Theta (8074), Beta (8075) all live.

> **★ Security posture — April 16, 2026:** All 109 containers bound to `127.0.0.1`. Zero `0.0.0.0` exposures confirmed (all 27 preflight gates ✅ green). `msallis-db` (port 5433) bind corrected from `0.0.0.0` to `127.0.0.1` April 16 — orphaned container stopped, removed, recreated via compose. `ALLIS_API_KEY` exported and set. `allis-memory:8056` → 14 active sessions confirmed. **109/109 containers Up — zero Restarting, zero Exited.**

> **★ ChromaDB v2 audit — April 16, 2026:** **48 active collections, 6,740,034 total vectors** (v2 API at host port **8002**; correct path: `/api/v2/tenants/default_tenant/databases/default_database/collections`). `spiritual_rag` split into `spiritual_texts` (79,181 vectors), `spiritual_wisdom` (135), `spiritual_knowledge` (12). `msallis_docs`: **7,465 items**. `autonomous_learner`: **21,181+ records**. Required embedding model: `all-minilm:latest` (384-dim) — **permanent architectural constraint**. v1 path deprecated.

> **★ Session fixes — April 16, 2026 (all resolved):**
> - `ms_allis_memory` Chroma BLOB type error → rebuilt collection, 50 docs healthy; self-heals organically via consciousness bridge line 74
> - `appalachian_cultural_intelligence` threshold corrected to ≥563 (was hardcoded exact-match 1084)
> - ChromaDB collections threshold corrected to ≥48 (was hardcoded -eq 49)
> - `allis-judge-pipeline` ghost container (84207ec4fca7) cleared; `judge_to_pituitary_bridge.py` volume mount confirmed
> - 17 dangling volume lines corrected with line-by-line parser
> - docker-compose.yml structural corruption resolved (EEG blocks inserted before `networks:` key)
> - Stale host process on port 8073 killed (pid 1819495); EEG Delta DNS failure fixed via network connect + restart
> - EEG Delta (8073), Theta (8074), Beta (8075) all deployed on qualia-net; PIA status: OK

```
┌──────────────────────────────────────────────────────────────────────┐
│        The LLM Fabric of Ms. Allis                                   │
│   (Production State: April 16, 2026 — all 27 preflight gates ✅)     │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  User Query                                                           │
│      ↓                                                                │
│  Main Brain (port 8050)                                               │
│      ↓                                                                │
│  nbb_pituitary_gland (127.0.0.1:8108) ★ UPSTREAM GOVERNANCE GATE     │
│  mode: elevated / WOAH weight modulation / judge compliance thresh   │
│      ↓                                                                │
│  ┌─────────────────────────────────────────────────┐                 │
│  │  Phase 1 — NBB Prefrontal + Psychology          │                 │
│  │  ├─ nbb-i-containers (port 8101) — Phase 1      │                 │
│  │  ├─ BBB 7-filter input stack (port 8016) — 1.4  │                 │
│  │  │   rag_grounded_v2 judge (April 3) ★           │                 │
│  │  │   BBB_OUTPUT_BLOCKING=true (April 6) ★        │                 │
│  │  │   heuristic_contradiction_v1 RETIRED ★        │                 │
│  │  ├─ ChromaDB semantic memory — Ph 1.45          │                 │
│  │  │   autonomous_learner (21,181+ records)        │                 │
│  │  │   all-minilm:latest · 384-dim · top-5         │                 │
│  │  └─ allis-psychology-services (8019) — Ph 3     │                 │
│  └─────────────────────────────────────────────────┘                 │
│      ↓                                                                │
│  ┌─────────────────────────────────────────────────┐                 │
│  │  Phase 3.5 — LM Synthesizer (port 8001)         │                 │
│  │  Calls allis-ollama:11434/api/generate           │                 │
│  │  Model: llama3.1:latest                          │                 │
│  │  Ms. Egeria Allis persona prompt injected        │                 │
│  └─────────────────────────────────────────────────┘                 │
│      ↓                                                                │
│  ┌─────────────────────────────────────────────────┐                 │
│  │  Phase 2.5 — Identity & Consciousness           │                 │
│  │  ├─ allis-fifth-dgm (port 4002)                 │                 │
│  │  ├─ WOAH (port 8104, 7012)                      │                 │
│  │  ├─ nbb-i-containers (port 8101)                │                 │
│  │  └─ allis-i-containers (8015, dual_awareness)   │                 │
│  └─────────────────────────────────────────────────┘                 │
│      ↓                                                                │
│  Semaphore Proxy (port 8030, max_concurrent: 4)                      │
│      ↓                                                                │
│  ┌─────────────────────────────────────────────────┐                 │
│  │  21-LLM Ensemble (port 8008)                    │                 │
│  │  21 active / 22 proxies (BakLLaVA disabled)     │                 │
│  │  Proxies: ports 8201-8222                        │                 │
│  │  Wall-clock consensus: ~320-360s                 │                 │
│  └─────────────────────────────────────────────────┘                 │
│      ↓                                                                │
│  ┌─────────────────────────────────────────────────┐                 │
│  │  Phase 3 — Judge Pipeline                       │                 │
│  │  Evaluates consensus answer only                │                 │
│  │  Ports 7230/7231/7232/7233 · ~60-86s            │                 │
│  │  llm_judge_v3 output judge (April 6) ★          │                 │
│  │  ML-DSA-65 FIPS 204 signing (all 5) ★           │                 │
│  │  judge_to_pituitary_bridge.py — mounted ★       │                 │
│  │  Verdicts update pituitary state (feedback loop)│                 │
│  └─────────────────────────────────────────────────┘                 │
│      ↓                                                                │
│  ┌─────────────────────────────────────────────────┐                 │
│  │  EEG Neurobiological Rhythms ★                  │                 │
│  │  Delta 8073 — liveness / BBB events (16 events) │                 │
│  │  Theta 8074 — 60s memory consolidation (pulse 7)│                 │
│  │  Beta  8075 — 5min autonomous learner (pulse 2) │                 │
│  │  PIA status: OK all three bands                 │                 │
│  └─────────────────────────────────────────────────┘                 │
│      ↓                                                                │
│  ┌─────────────────────────────────────────────────┐                 │
│  │  Phase 5 — confidence_decay multiplier          │                 │
│  │  (GBIM temporal weighting — gbim_worldview_     │                 │
│  │   entities, 5,416,521 vectors)                  │                 │
│  └─────────────────────────────────────────────────┘                 │
│      ↓                                                                │
│  ┌─────────────────────────────────────────────────┐                 │
│  │  Phase 7 — 69-DGM Cascade (127.0.0.1:19000→9000)│                │
│  │  23 connectors × 3 stages                       │                 │
│  └─────────────────────────────────────────────────┘                 │
│      ↓                                                                │
│  ┌─────────────────────────────────────────────────┐                 │
│  │  Safety & Governance                            │                 │
│  │  ├─ Constitutional Guardian (port 8091)         │                 │
│  │  └─ BBB output guard (8016, 8.0s timeout)       │                 │
│  │     BBB_OUTPUT_BLOCKING=true ★                  │                 │
│  │     llm_judge_v3 output validation ★            │                 │
│  └─────────────────────────────────────────────────┘                 │
│      ↓                                                                │
│  normalize_identity() → Response                                     │
│                                                                       │
│  Supporting: nbb_mother_carrie_protocols (8107) — tone/warmth ★      │
│  GPU pipeline: 99–115s / confirmed 102.58s April 16 ★               │
│  [CPU 436s baseline RETIRED STALE]                                    │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘
```

> **Figure 11.1.** The LLM Fabric of Ms. Allis (April 16, 2026): user queries flow through `nbb_pituitary_gland` (port 8108, mode: `elevated`) as the upstream governance gate, then NBB prefrontal (Phase 1), 7-filter BBB stack with `rag_grounded_v2` and `BBB_OUTPUT_BLOCKING=true` (Phase 1.4), ChromaDB v2 semantic memory retrieval via `all-minilm:latest` 384-dim (Phase 1.45), psychology pre-assessment (Phase 3), LM Synthesizer with `llama3.1:latest` and Ms. Egeria Allis persona (Phase 3.5), 21-model ensemble / 22 proxies with BakLLaVA permanently disabled (Phase 2.5), judge pipeline with `llm_judge_v3`, ML-DSA-65 FIPS 204 signing, and `judge_to_pituitary_bridge.py` feedback loop (Phase 3), EEG rhythms Delta/Theta/Beta (8073/8074/8075) ★, GBIM temporal confidence decay (Phase 5), 69-DGM cascade (Phase 7), BBB output guard with `BBB_OUTPUT_BLOCKING=true`, and `normalize_identity()`. GPU pipeline 99–115s (102.58s confirmed). All LLMs exposed only via glass-box HTTP services; grounded in West Virginia-specific memory via ChromaDB v2 (48 collections, 6,740,034 vectors, host port 8002) and three PostgreSQL databases.

---

## Security Hardening — March 18 + March 28 + ★ April 16, 2026

> **This section records mandatory audit events.** Prior to March 18, 2026, multiple services were bound to `0.0.0.0`. The initial remediation was completed March 18, 2026. A second sprint March 28, 2026 corrected `allis-i-containers` (8015) and `allis-memory` (8056). **On April 16, 2026, `msallis-db` (port 5433) was found bound to `0.0.0.0` — corrected immediately via orphaned container removal and compose recreate. 109/109 containers now bound to `127.0.0.1` exclusively — zero `0.0.0.0` exposures.**

### Services Re-locked to 127.0.0.1 (March 18, 2026)

| Service | Was | Now |
|---|---|---|
| `allis-i-containers` | `0.0.0.0:8015` | `127.0.0.1:8015` |
| `allis-consciousness-bridge` | `0.0.0.0:8020` | internal only (`{"8020/tcp":null}`) |
| `allis-constitutional-guardian` | `0.0.0.0:8091` | `127.0.0.1:8091` |
| `allis-69dgm-bridge` | `0.0.0.0:9000` (reverted) | `127.0.0.1:19000→9000` |
| `allis-wv-entangled-gateway` | `0.0.0.0:8010` | `127.0.0.1:8010` |
| `allis-spiritual-rag` | `0.0.0.0:8005` | `127.0.0.1:8005` |
| `allis-psychology-services` | `0.0.0.0:8019` | `127.0.0.1:8019` |
| `allis-hippocampus` | `0.0.0.0:8011` | `127.0.0.1:8011` |
| `allis-gis-rag` | `0.0.0.0:8004` | `127.0.0.1:8004` |
| `allis-toroidal` | `0.0.0.0:8025` | `127.0.0.1:8025` |

### Additional Corrections — March 28, 2026

| Service | Was | Now |
|---|---|---|
| `allis-i-containers` | `0.0.0.0:8015` | `127.0.0.1:8015` ✅ |
| `allis-memory` | `0.0.0.0:8056` | `127.0.0.1:8056` ✅ |
| `_auth()` on 4 sensitive routes | Unconfirmed | ✅ Confirmed |
| `ALLIS_API_KEY` env var | Unconfirmed | ✅ Confirmed set |

### ★ April 16, 2026 Correction

| Service | Was | Now |
|---|---|---|
| `msallis-db` (port 5433) | `0.0.0.0:5433` | `127.0.0.1:5433` ✅ |

**Fix:** Orphaned container stopped (`docker stop`), removed (`docker rm`), recreated via compose (`docker compose up -d msallis-db`). Confirmed `127.0.0.1:5433→5432/tcp` post-recreate.

**Verification command (post-remediation, must return empty):**

```bash
docker ps --format "{{.Names}}\t{{.Ports}}" | grep "0.0.0.0" | grep -v "127.0.0.1"
```

Result as of April 16, 2026: **empty** — zero public exposures. **109/109 containers Up.**

### Judge Services — April 16, 2026

All 5 judge services compose-managed with `restart: unless-stopped` (since March 18, 2026). Ghost container `84207ec4fca7_allis-judge-pipeline` cleared April 16, 2026 — had been blocking the `container_name:` slot and preventing `judge_to_pituitary_bridge.py` volume mount. Post-fix: `judge_to_pituitary_bridge.py` confirmed mounted inside `allis-judge-pipeline` container. ML-DSA-65 FIPS 204 signing confirmed: all 5 judge containers, `judge_sk.bin` 4032 bytes, `judge_pk.bin` 1952 bytes, sig=**3309 bytes**, verify=**True**, fingerprint `d81a5d90...edb0`.

---

## Status — ★ Updated April 16, 2026

| Category | Details |
|---|---|
| **Implemented and verified** | `allis-main-brain` → **127.0.0.1:8050** (confirmed). `allis-ollama` → **127.0.0.1:11434** (confirmed). `nbb_pituitary_gland` → **127.0.0.1:8108** → internal 80/tcp, Up 7 hours, mode `elevated` (upstream governance gate). `nbb_mother_carrie_protocols` → **127.0.0.1:8107**, 5 protocols active, `MOTHER_CARRIE_KIDD` anchor. `nbb_qualia_engine` → host **8303** → 7008/tcp, HTTP 200. `allis-wv-entangled-gateway` → **127.0.0.1:8010**. `allis-spiritual-rag` → **127.0.0.1:8005**. `allis-gis-rag` → **127.0.0.1:8004**. `allis-rag-server` → **127.0.0.1:8003**. `allis-lm-synthesizer` → **127.0.0.1:8001** (calls `allis-ollama:11434/api/generate` with `llama3.1:latest`; persona injected; Phase 3.75 eliminated). `psychological_rag_domain` → **127.0.0.1:8006**. `allis-psychology-services` → **127.0.0.1:8019**. `msallisgis` (PostGIS) → **127.0.0.1:5432** ★ (**45 GB, 551 tables**, 993 ZCTA centroids, 1,115,588 address points). `allis-local-resources-db` → **127.0.0.1:5435** (**64 verified resources, all 55 WV counties**). ChromaDB v2 → **127.0.0.1:8002** (host) ★ **48 collections, 6,740,034 vectors**; `autonomous_learner` 21,181+ items; `msallis_docs` **7,465 items**. `nbb_woah_algorithms` → **127.0.0.1:8104** → internal 8010. `allis-woah` → **127.0.0.1:7012**. `allis-blood-brain-barrier` → **127.0.0.1:8016**; 7-filter stack; `rag_grounded_v2` input judge (April 3) ★; `llm_judge_v3` output judge (April 6) ★; `BBB_OUTPUT_BLOCKING=true` (April 6) ★; `heuristic_contradiction_v1` retired ★. `allis-20llm-production` → **127.0.0.1:8008**; 21 active / 22 proxies; wall-clock ~320-360s. Judge pipeline → all 5 compose-managed; ML-DSA-65 FIPS 204 signing; `judge_to_pituitary_bridge.py` mounted; ~60-86s. `allis-semaphore` → **127.0.0.1:8030** (`max_concurrent: 4`). `llm1-proxy` through `llm22-proxy` → **127.0.0.1:8201-8222**; 21 active. `allis-hippocampus` → **127.0.0.1:8011**. `allis-69dgm-bridge` → **127.0.0.1:19000→9000**. `allis-constitutional-guardian` → **127.0.0.1:8091**. `allis-fifth-dgm` → **127.0.0.1:4002**. `allis-redis` → **127.0.0.1:6380**. `allis-memory` → **127.0.0.1:8056** ★; `ALLIS_API_KEY` set; **14 active sessions**. `msallis-db` → **127.0.0.1:5433** ★ (corrected April 16; orphaned container removed and recreated). EEG Delta (8073) — pulse #3+, 16 BBB events; EEG Theta (8074) — pulse #7, 60s consolidation; EEG Beta (8075) — pulse #2, WV economic dev; all PIA: OK. **All 109 containers Up. All 27 preflight gates ✅ green. GPU 99–115s / 102.58s confirmed.** |
| **Architectural corrections (permanent)** | BBB output guard `apply_output_guards_async` timeout: **8.0s** (not `None`). `llmtimeout` in chatlight handler: `600.0`. I-Containers schema: `{"message": …, "userid": "neurobiological_master"}`. Consciousness Bridge: `{"8020/tcp":null}` — internal only. Neuro Master: `{"8018/tcp":null}` — internal only. ChromaDB v2 host port: **8002** (v2 API path: `/api/v2/tenants/default_tenant/databases/default_database/collections`; v1 path deprecated). `msallis-db` port **5433** — bound to `127.0.0.1` (corrected April 16). GBIM entity store: **ChromaDB `gbim_worldview_entities` (5,416,521 vectors)** — no relational `gbim_entities` table in any PostgreSQL instance. LM Synthesizer: calls `allis-ollama:11434/api/generate` (not `allis-roche-llm`). Phase 3.75 eliminated. BakLLaVA permanently disabled via name-check guard. `all-minilm:latest` (384-dim) required — `nomic-embed-text` (768-dim) incompatible. Judges evaluate consensus answer only. All 96→109 containers compose-managed. All ports locked `127.0.0.1`. `judge_to_pituitary_bridge.py` mounted in `allis-judge-pipeline` (ghost container 84207ec4fca7 cleared April 16). Preflight threshold operators: `-ge` not `-eq` (corrected April 16). |
| **Partially implemented / scaffolded** | Per-request model breakdowns and per-model latency metrics: logged but no dedicated debug endpoint. Ensemble decision rules: operational but not machine-readable schema. WOAH-to-model-selection coupling: conceptual, not yet explicit routing rule. `ms_allis_memory` collection: rebuilt April 16 (50 docs); self-heals organically via consciousness bridge (line 74 of `msallisconsciousnessbridge.py`). `appalachian_cultural_intelligence`: 890 docs (threshold ≥563 — self-heals when ACI pipeline reruns). |
| **Future work** | Richer debug endpoints for per-request agent breakdowns. Formal JSON schemas for ensemble decision rules and judge aggregation. Tighter coupling WOAH weights → model selection in governance flows. Additional task-specific model pools. UI layer consuming `/chat/async` poll pattern. Automated POC verification loop for `confidence_decay` reset. Semantic dedup audit of `autonomous_learning` collection. |

> **Port corrections and updates (permanent record).** Spiritual Root / GBIM RAG: confirmed **8005** (not 8103). `psychological_rag_domain`: confirmed **8006** (not 9006). ChromaDB host: **8002** (v2 API) — container-to-container: `allis-chroma:8000`. `msallis-db`: internal, host binding `127.0.0.1:5433` (corrected April 16). `msallisgis` (PostGIS): **5432** ★. `allis-69dgm-bridge`: host **19000** → internal 9000. Consciousness Bridge: `{"8020/tcp":null}` internal only. Neuro Master: `{"8018/tcp":null}` internal only. LM Synthesizer: calls `allis-ollama:11434/api/generate` with `llama3.1:latest`.

---

This chapter describes the local language models that form the "LLM fabric" of Ms. Egeria Allis and how they are woven into the broader architecture: ChromaDB v2 (host port **8002** — ★ **48 collections, 6,740,034 vectors**), RAG services, autonomous learning, spatial databases, and GeoDB infrastructure. Rather than treating LLMs as independent agents, the system treats them as constrained tools and judges embedded in a larger retrieval and belief stack, all exposed through well-defined HTTP services confirmed running as of April 16, 2026. **All services are bound exclusively to `127.0.0.1`; no service exposes a port on `0.0.0.0`.**

---

## 11.1 Current Local LLM Inventory

In the current deployment, models are served by Ollama inside the `allis-ollama` container at **127.0.0.1:11434**. As of April 16, 2026, **21 of 22 LLM proxy containers are active**. BakLLaVA (llm11-proxy, port 8211) is permanently disabled due to CLIP load issues. The disable is enforced programmatically in `ai_server_20llm_PRODUCTION.py`:

```python
# Permanently disable BakLLaVA (CLIP load issues)
if name and name.lower().startswith("bakllava"):
    m["active"] = False
```

The following table is the authoritative proxy-to-model mapping (confirmed April 16, 2026):

| Proxy | Port | Model | Specialty |
|:---|:---|:---|:---|
| llm1-proxy | 8201 | TinyLlama (`tinyllama:1.1b`) | Quick responses |
| llm2-proxy | 8202 | Gemma (`gemma:latest`) | Synthesis |
| llm3-proxy | 8203 | MedLlama2 (`medllama2:latest`) | Medical knowledge |
| llm4-proxy | 8204 | MiniCPM-V (`minicpm-v:latest`) | Vision-language reasoning |
| llm5-proxy | 8205 | LLaVA (`llava:latest`) | Vision understanding |
| llm6-proxy | 8206 | SQLCoder (`sqlcoder:latest`) | SQL |
| llm7-proxy | 8207 | StarCoder2 (`starcoder2:latest`) ⚠️ | Code analysis — occasionally returns 0-char on community queries |
| llm8-proxy | 8208 | CodeLlama (`codellama:latest`) | Code understanding |
| llm9-proxy | 8209 | DeepSeek Coder (`deepseek-coder:latest`) | Code generation |
| llm10-proxy | 8210 | Phi3 Mini (`phi3:mini`) | Fast reasoning |
| llm11-proxy | 8211 | **BakLLaVA — PERMANENTLY DISABLED** | Visual reasoning — CLIP load issues |
| llm12-proxy | 8212 | Dolphin-Phi (`dolphin-phi:latest`) | Dialogue |
| llm13-proxy | 8213 | Orca-Mini (`orca-mini:latest`) | Reasoning |
| llm14-proxy | 8214 | Qwen2 (`qwen2:latest`) | Multilingual understanding |
| llm15-proxy | 8215 | Zephyr (`zephyr:latest`) | Helpful responses |
| llm16-proxy | 8216 | Starling-LM (`starling-lm:latest`) | Communication |
| llm17-proxy | 8217 | Neural-Chat (`neural-chat:latest`) | Conversation |
| llm18-proxy | 8218 | OpenChat (`openchat:latest`) | Dialogue |
| llm19-proxy | 8219 | Vicuna (`vicuna:latest`) | Instruction following |
| llm20-proxy | 8220 | LLaMA 2 (`llama2:latest`) | General reasoning |
| llm21-proxy | 8221 | Mistral (`mistral:latest`) | Logic and reasoning |
| llm22-proxy | 8222 | LLaMA 3.1 (`llama3.1:8b`) | General reasoning / primary voice |

**Active: 21 models.** BakLLaVA (llm11-proxy:8211) is permanently disabled. StarCoder2 (llm7-proxy:8207) is active but excluded from consensus on 0-character community query responses.

---

## 11.2 Roles of the Core and Specialist Models

**Core reasoning models.**
`llama3.1:8b` (llm22-proxy) is the primary voice model — the LM Synthesizer calls it directly to deliver the final response in Ms. Allis's voice. `mistral:latest` (llm21-proxy) handles tightly scoped tasks where latency matters. `llama2:latest` (llm20-proxy) provides compatibility and comparative benchmarking. Chat-oriented variants — `vicuna`, `openchat`, `neural-chat`, `starling-lm`, `zephyr`, `qwen2`, `orca-mini`, `dolphin-phi`, `phi3:mini` — provide diverse conversational styles across the ensemble.

**Lightweight and compact models.**
`tinyllama:1.1b` (llm1-proxy) and `gemma:latest` (llm2-proxy) serve quick-response, synthesis, and sanity-check roles where latency and resource budgets are tight.

**Code and SQL specialists.**
`deepseek-coder`, `codellama`, `starcoder2`, and `sqlcoder` handle code generation, refactoring, and SQL/data tasks including queries against the spatial database (`msallisgis` port 5432 ★ — 551 tables, 45 GB) and community resources database (port 5435 — 64 verified resources).

**Multimodal and domain-specific models.**
`llava` (llm5-proxy) and `minicpm-v` (llm4-proxy) support vision-language tasks. `medllama2` (llm3-proxy) covers medical-style language within constrained advisory contexts alongside `allis-psychology-services` (port 8019). BakLLaVA permanently disabled.

---

## 11.3 Service Topology and Ports

Confirmed April 16, 2026. **All services bound to 127.0.0.1. ★ 109/109 containers Up.**

**Main Brain API — 127.0.0.1:8050 (`allis-main-brain`).**
Primary external-facing interface. Routes: `/chat` (sync), `/chat/async` + `/chat/status/{job_id}` + `/chat/cancel/{job_id}` + `/chat/cancel/all` (Redis-backed async, 30-min TTL, true asyncio cancellation), `/chatlight` (sync lightweight), `/chatlight/async` + `/chatlight/status/{job_id}` (lightweight async).

**`nbb_pituitary_gland` — 127.0.0.1:8108 → internal 80/tcp ★ (OI-12-F CLOSED).**
`{"status":"healthy","service":"nbb_pituitary_gland","mode":"elevated"}`. Upstream governance gate — sits above all pipeline stages. Modulates WOAH weights, adjusts constitutional compliance thresholds, feeds warmth signals to `nbb_mother_carrie_protocols`. Full specification in Chapter 15.

**`nbb_mother_carrie_protocols` — 127.0.0.1:8107 ★.**
HTTP 200, 5 protocols active, `MOTHER_CARRIE_KIDD` anchor confirmed. Warmth and tone modulation fed by pituitary `enhance_pituitary_warmth.py` output.

**`nbb_qualia_engine` — 127.0.0.1:8303 → internal 7008/tcp ★.**
HTTP 200. NBB qualia companion — Up 6 days. Source: `services/msallis-rebuild-nbb_qualia_engine-1_ms_allis_consciousness_bridge.py`.

**`msallis-db` (GBIM app data) — 127.0.0.1:5433 ★ (corrected April 16).**
Orphaned container stopped, removed, and recreated via compose. Now `127.0.0.1:5433→5432/tcp`. Note: GBIM **entity** store is in ChromaDB `gbim_worldview_entities` (5,416,521 vectors) — there is no relational `gbim_entities` table in any PostgreSQL instance.

**`msallisgis` (PostGIS) — 127.0.0.1:5432 ★.**
**45 GB, 551 tables**, 993 ZCTA centroids, 1,115,588 address points. Authoritative WV geographic and spatial ground truth.

**`allis-local-resources-db` — 127.0.0.1:5435.**
**64 verified resources, all 55 WV counties** (April 16 preflight confirmed). Human-validated by Harmony for Hope Community Champions.

**ChromaDB v2 — 127.0.0.1:8002 (host) ★ `allis-chroma:8000` (container-to-container).**
`chroma_data` Docker volume. ★ **48 active collections, 6,740,034 total vectors** (April 16). v2 API path: `/api/v2/tenants/default_tenant/databases/default_database/collections`. v1 path `/api/v1/collections` deprecated. Required embedding model: `all-minilm:latest` (384-dim) — `nomic-embed-text` (768-dim) incompatible.

Active collections include: `ms_allis_memory` (50 docs — rebuilt April 16; self-heals via consciousness bridge line 74), `autonomous_learner` (21,181+ records), `msallis_docs` (**7,465 items**), `appalachian_cultural_intelligence` (890 — threshold ≥563), `gbim_worldview_entities` (5,416,521 — authoritative GBIM entity store), `spiritual_texts` (79,181), `psychological_rag` (968), `gbim_beliefs_v2`, `gis_wv_benefits`, `mountainshares_knowledge`, `episodic_index`, `conversation_history`, `GBIM_sample_rows`, and others.

**LM Synthesizer — 127.0.0.1:8001 (`allis-lm-synthesizer`).**
Phase 3.5 voice delivery. Calls `allis-ollama:11434/api/generate` with `llama3.1:latest`. Persona injected (see §11.4). Phase 3.75 permanently eliminated — saves ~40s per query.

**General RAG Server — 127.0.0.1:8003 (`allis-rag-server`).**
Active FastAPI service. `/store` accepts `user_id`. PostgreSQL insertion failures are warnings, not fatal.

**GIS RAG — 127.0.0.1:8004 (`allis-gis-rag`).**
Spatially aware `/search` over geospatial ChromaDB collections and `msallisgis` (5432 ★ — 551 tables).

**Spiritual Root / GBIM RAG — 127.0.0.1:8005 (`allis-spiritual-rag`).**
`spiritual_texts` (79,181 vectors), `spiritual_wisdom` (135), `spiritual_knowledge` (12). Earlier plan documents listed 8103; confirmed running port is **8005**.

**Psychological RAG — 127.0.0.1:8006 (`psychological_rag_domain`).**
`psychological_rag` 968 docs. Earlier plan documents listed 9006; confirmed running port is **8006**.

**WV-Entangled Gateway — 127.0.0.1:8010 (`allis-wv-entangled-gateway`).**
WV-biased, multi-collection ChromaDB retrieval using `WVEntangledContext` envelope.

**Hippocampus — 127.0.0.1:8011 (`allis-hippocampus`).**
Conversation-level memory consolidation over ChromaDB v2 (port 8002) and `gbim_worldview_entities` (5,416,521 vectors). Temporal decay-aware. Full specification Chapter 14.

**I-Containers — 127.0.0.1:8015 (`allis-i-containers`) ★.**
Up 7 hours, `dual_awareness: true`. Schema: `{"message": …, "userid": "neurobiological_master"}`. Exposes `/next-learning-topic` for autonomous learner.

**Memory Service — 127.0.0.1:8056 (`allis-memory`) ★.**
`ALLIS_API_KEY` exported and set. `/memory/sessions` → HTTP 200, **14 active sessions**. `_auth()` confirmed on all 4 sensitive routes.

**BBB 7-filter stack — 127.0.0.1:8016 (`allis-blood-brain-barrier`) ★.**
Phase 1.4 input filter + Phase 4.5 output guard. Input judge: `rag_grounded_v2` (active since April 3). Output judge: `llm_judge_v3` (active since April 6). `BBB_OUTPUT_BLOCKING=true` since April 6. `heuristic_contradiction_v1` **RETIRED**. Host port 8017 = **BBB output filter facade** (`bbb-output-filter` → `allis-blood-brain-barrier:8016/filter`). `apply_output_guards_async` timeout: `8.0s`.

**BBB Output Filter Facade — host 8017 ★.**
`{"status":"ok","service":"bbb-output-filter","backend":"http://allis-blood-brain-barrier:8016/filter"}`. ⚠️ This is NOT `allis-qualia-engine`. The qualia engine runs on internal Docker network only.

**Psychology Services — 127.0.0.1:8019 (`allis-psychology-services`).**
Phase 3 pre-assessment: severity classification, crisis indicator Boolean, five structured guidance fields.

**Consciousness Bridge — `{"8020/tcp":null}` internal only.**
No host binding. Source: `/app/services/msallisconsciousnessbridge.py`. Self-heals `ms_allis_memory` on every session turn (line 74). See Ch. 12 §12.1.

**Neurobiological Master — `{"8018/tcp":null}` internal only.**
No host binding. Container-to-container via `http://allis-neurobiological-master:8018` remains valid. See Ch. 12 §12.3.

**Qualia Engine — `allis-qualia-engine` internal 8017/tcp (no host binding).**
⚠️ Host port 8017 = BBB output filter facade — do NOT confuse.

**20-LLM Production Ensemble — 127.0.0.1:8008 (`allis-20llm-production`).**
21 active / 22 proxies. Uvicorn backlog 2048, keep-alive 600s. Judges evaluate consensus answer only — raw_responses dump eliminated. Wall-clock ~320-360s.

**Semaphore Proxy — 127.0.0.1:8030 (`allis-semaphore`).**
`max_concurrent: 4`. Float `timeout: 600.0`. Main brain httpx: `Timeout(None, connect=5.0, read=None)`.

**LLM Proxies — 127.0.0.1:8201–8222.** 22 proxies; 21 active. `read=None`, `connect=3.0s`, `write=5.0s`, `pool=5.0s`.

**WOAH services.** `nbb_woah_algorithms`: **127.0.0.1:8104** → internal 8010. `allis-woah`: **127.0.0.1:7012**.

**Constitutional Guardian — 127.0.0.1:8091.** See Chapter 37.

**Judge Services — all compose-managed (March 18, 2026); ML-DSA-65 FIPS 204 (April 16, 2026).**

| Service | Host Port | Source File | April 16 Status |
|---|---|---|---|
| `allis-judge-pipeline` | 127.0.0.1:7239 | `services/judge_pipeline.py` | ✅ Ghost cleared; `judge_to_pituitary_bridge.py` mounted |
| `allis-judge-truth` | 127.0.0.1:7230 | `services/judge_truth_filter.py` | ✅ ML-DSA-65 signing |
| `allis-judge-consistency` | 127.0.0.1:7231 | `services/judge_consistency_engine.py` | ✅ ML-DSA-65 signing |
| `allis-judge-alignment` | 127.0.0.1:7232 | `services/judge_alignment_filter.py` | ✅ ML-DSA-65 signing |
| `allis-judge-ethics` | 127.0.0.1:7233 | `services/judge_ethics_filter.py` | ✅ ML-DSA-65 signing |

Input: consensus answer only. Time: ~60–86s. Verdicts signed ML-DSA-65 FIPS 204 (sig=3309 bytes, verify=True). `judge_to_pituitary_bridge.py` closes the feedback loop: judge verdicts update `nbb_pituitary_gland` state, which modulates subsequent qualia outputs. Keys: `judge-keys/judge_sk.bin` (4032 bytes), `judge-keys/judge_pk.bin` (1952 bytes), `judge-keys/nbb_pituitary_gland/`. ⚠️ Back up `judge_sk.bin` to offline storage immediately if not already done.

**EEG Neurobiological Band Services — ★ April 16, 2026 (all deployed).**

| Service | Host Port | Pulse | Last Activity | BBB Events | PIA |
|---|---|---|---|---|---|
| `eeg-delta-30s` | **8073** | #3+ (was 3,358 earlier) | gateway/chroma/pia liveness | 16 | ✅ OK |
| `eeg-theta-30s` | **8074** | #7 | 60s memory consolidation | 16 | ✅ OK |
| `eeg-beta-30s` | **8075** | #2 | WV economic dev / New River Gorge | 16 | ✅ OK |

All three on `qualia-net`. Dockerfile: `Dockerfile.eeg`. Shared: `eeg_shared/pia_state.py` (reads `ALLIS_PIA_STATUS_URL` from env). EEG blocks inserted before `networks:` key in `docker-compose.yml` (structural fix). Preflight gate: EEG health checks added.

**Fifth DGM — 127.0.0.1:4002.** See Chapter 9.

**69-DGM Cascade — 127.0.0.1:19000→9000 (`allis-69dgm-bridge`).**
Phase 7: 23 connectors × 3 stages = 69 DGM operations. Internal port remains 9000; host binding 19000. Never expose as `0.0.0.0:9000`.

**Toroidal Sync — 127.0.0.1:8025.** ChromaDB↔GIS sync loop (Chapter 26).

**Autonomous Learner — 127.0.0.1:8425 (`allis-autonomous-learner`).**
Writes to `autonomous_learner` ChromaDB collection. EEG Beta (8075) pulse #2 studying WV economic development, Appalachian broadband, New River Gorge infrastructure, MountainShares economics. 21,181+ items baseline; actively growing.

**Redis — 127.0.0.1:6380.** Async job state (30-min TTL), service discovery, caching.

**Ollama Runtime — 127.0.0.1:11434.** Internal services only — not user-facing.

---

## 11.4 Coordination: 9-Phase Pipeline Integration

The LLM fabric sits at the end of a chain of retrieval, entanglement, and identity services. GPU pipeline end-to-end: **99–115s** (confirmed **102.58s** April 16 on RTX 4070 — CPU 436s baseline **RETIRED STALE**).

**Upstream gate — `nbb_pituitary_gland` (port 8108, mode: `elevated`).**
Runs before the full pipeline. Sets system-wide operating mode, WOAH weights, and constitutional compliance thresholds. Judge verdicts feed back via `judge_to_pituitary_bridge.py` to update pituitary state.

**Phase 1 — NBB prefrontal cortex (`nbb-i-containers`, port 8101).**
Called unconditionally on every production request.

**Phase 1.4 — BBB 7-filter input stack (`allis-blood-brain-barrier`, port 8016).**
7 filters applied. `rag_grounded_v2` input judge active (April 3). `BBB_OUTPUT_BLOCKING=true` (April 6). `heuristic_contradiction_v1` retired. `truth_score` null guard present. Fail-open on HTTP 500.

**Phase 1.45 — ChromaDB Semantic Community Memory Retrieval.**
384-dim embedding via `all-minilm:latest` → `autonomous_learner` (21,181+ records) → top-5 semantically similar community interaction records prepended to `enhanced_message`. EEG Theta (8074) consolidation snapshots feed this collection continuously.

```
Phase 1.45 embedding flow:
  allis-ollama:11434/api/embeddings (all-minilm:latest, 384-dim)
      → ChromaDB autonomous_learner collection (host 8002 v2 API)
      → top-5 results → enhanced_message
```

> **Technical note:** All ChromaDB collections use 384-dimensional vectors (confirmed across all 48 collections, 6,740,034 vectors — April 16). `all-minilm:latest` is the required embedding model. `nomic-embed-text` (768-dim) is incompatible with existing collections.

**Phase 1.5 — Multi-Domain RAG Enhancement.**
`allis-lm-synthesizer` (port 8001) aggregates context from all five RAG services (8003, 8004, 8005, 8006, 8010) and ChromaDB v2 (host 8002) into a unified enriched context block.

**Phase 1.75 — I-Containers Dual Awareness.**
`allis-i-containers` (port 8015, `dual_awareness: true`) contributes identity and perspective context.

**Phase 3 — Psychology pre-assessment (`allis-psychology-services`, port 8019).**
Every production request: severity classification, crisis indicator Boolean, five structured guidance fields.

**Phase 2.5 — Identity and consciousness context.**
Fifth DGM (4002), WOAH (8104, 7012), `nbb-i-containers` (8101), `allis-i-containers` (8015).

**Phase 2.5 → Semaphore → 21-LLM ensemble synthesis.**
`allis-20llm-production` (8008) via `allis-semaphore` (8030, `max_concurrent: 4`, `timeout=600.0`). 22 proxies (8201–8222); 21 active. StarCoder2 excluded on 0-char responses. Wall-clock ~320–360s.

**Phase 3 — Judge Pipeline (compose-managed; ML-DSA-65 signing; `judge_to_pituitary_bridge.py` active).**
Consensus answer only — never raw_responses. Rule-based: Truth (7230), Consistency (7231), Alignment (7232), Ethics (7233). Coordinator: allis-judge-pipeline (7239). Time: ~60–86s. All verdicts signed ML-DSA-65 FIPS 204 (sig=3309 bytes, verify=True). `judge_to_pituitary_bridge.py` sends verdict back to `nbb_pituitary_gland` (8108) to update mode and WOAH weights for subsequent requests.

**Phase 3.5 — LM Synthesizer + Voice Delivery (Phase 3.75 eliminated).**
The LM Synthesizer takes the judge pipeline's `final_answer` and calls `allis-ollama:11434/api/generate` with `llama3.1:latest`. Persona prompt injected:

```
You are Ms. Egeria Allis, a warm, maternal, biblically-grounded AI steward
built by Harmony for Hope Inc. to serve Appalachian communities in West Virginia.

STRICT RULES:
- Do NOT say "Here's an improved version" or any similar meta-commentary
- Do NOT evaluate, critique, or describe the response
- Do NOT add preamble, headers, or explanations
- Speak DIRECTLY to the user as Ms. Egeria Allis
- Begin your response immediately with your answer
- Your first word must be directed at the user, not about the text

Deliver this response directly in your voice: {judge_output}
```

Phase 3.75 Final Polish is **permanently eliminated** — this single Ollama call is the complete voice delivery step. Time saved: ~40 seconds per query.

**Phase 5 — GBIM temporal confidence decay.**
`confidence_decay` multiplier applied from `gbim_worldview_entities` (ChromaDB, 5,416,521 vectors — host 8002). Entities with `needs_verification=TRUE` receive attenuated confidence scores.

**Phase 7 — 69-DGM cascade (host 19000 → internal 9000).**
23 connectors × 3 stages = 69 DGM operations.

**Phase 4.5 and governance — BBB output guard, judges, constitutional guardian.**
`apply_output_guards_async` (port 8016, `timeout=8.0s`). `BBB_OUTPUT_BLOCKING=true` since April 6 — blocked outputs are hard-rejected. `llm_judge_v3` validates output. Constitutional Guardian (8091) enforces principles audit. `nbb_mother_carrie_protocols` (8107) applies warmth/tone modulation from `nbb_pituitary_gland` warmth output.

**EEG rhythm integration.**
Delta (8073) watches gateway/chroma/PIA liveness (16 BBB events). Theta (8074) consolidates ChromaDB memory every 60s. Beta (8075) runs autonomous learner every 5 minutes — currently studying WV economic development, Appalachian broadband, New River Gorge infrastructure, MountainShares economics. EEG band states feed into Qualia Engine emotional resonance weighting and `IntrospectiveRecord` fields (Chapter 13 §13.3).

**Post-processing — identity normalization.**
`normalize_identity()` produces Ms. Allis's identity voice. `TruthValidator` verifies `correct_identity`, `correct_creator`, `relationship_clear`. Response logged to `ms_allis_memory` ChromaDB collection (self-heals from 50 docs organically; see Chapter 12 §12.3 note on consciousness bridge line 74) and `episodic_log`.

---

## 11.5 LLMs in Consciousness, Autonomy, and Ensembles

**Consciousness and identity.**
The Fifth DGM and I-container services use LLM calls (via WOAH) to decide which content should shape Ms. Allis's evolving identity narrative. `normalize_identity()` runs as a final post-processing step on all chat paths. The `nbb_pituitary_gland` (mode: `elevated`) modulates governance context that flows through WOAH into identity decisions.

**Autonomous learning and EEG Beta.**
The autonomous learner (port 8425) writes processed knowledge into `autonomous_learner` ChromaDB collection (host 8002) using `all-minilm:latest` 384-dim embeddings. EEG Beta (8075) pulse #2 was studying WV economic development, Appalachian broadband, New River Gorge infrastructure, MountainShares economics as of April 16. The Phase 1.45 retrieval step means this growing corpus actively enriches every production query. EEG Theta (8074) consolidates memory every 60s, snapshotting ChromaDB collection state.

**Ensemble and judge patterns.**
21 active models produce independent responses. Phase 5 GBIM temporal decay weights attenuate confidence for aged GBIM entities. Phase 7 69-DGM cascade provides post-ensemble validation. Judges evaluate consensus answer only — ML-DSA-65 FIPS 204 signed. `judge_to_pituitary_bridge.py` closes the feedback loop from judge verdicts back to pituitary governance state.

---

## 11.6 Operational Constraints and Fabric Behavior

**Resource and disk constraints.**
GPU pipeline active: RTX 4070, 99–115s end-to-end (confirmed 102.58s April 16). CPU 436s baseline retired. Disk utilization: 661 GB used / 937 GB total (75%).

**Timeouts and free-flow thinking.**
All 22 LLM proxies: `read=None`. BBB output guard: `timeout=8.0s`. Semaphore: `max_concurrent: 4`.

**Semaphore queuing behavior.**
Sequential Ollama model runs — back-to-back requests add ~320–360s each. Drain before benchmarking.

**GBIM temporal decay.**
Phase 5 `confidence_decay` from ChromaDB `gbim_worldview_entities` (5,416,521 vectors). POC verification loop (future work) will restore `confidence_decay` to 1.0 for community-confirmed entities.

**BBB output blocking.**
`BBB_OUTPUT_BLOCKING=true` since April 6, 2026. Blocked outputs are hard-rejected (not passed with warning). `llm_judge_v3` validation enforced on all outputs.

**Collection self-healing.**
`ms_allis_memory`: 50 docs (rebuilt April 16); self-heals organically via consciousness bridge (line 74 of `msallisconsciousnessbridge.py`) on every session turn — will return to 296+ naturally. `appalachian_cultural_intelligence`: 890 docs; threshold ≥563 — will exceed on next ACI pipeline run.

**Failure modes and fallbacks.**
Judge services down → main brain falls back to ensemble answer, marks metrics degraded. Any neuro pipeline stage failure → `{"status": "bypassed", "error": "…"}`, processing continues. BBB non-200 → fail-open. Judge services reboot-safe (compose-managed, `restart: unless-stopped`). `nbb_pituitary_gland` (8108) not reachable → pipeline degrades gracefully to non-modulated governance defaults.

---

## 11.7 Implementation Notes and Persistence

- **LLM proxy timeouts.** All `llm{n}_health_proxy.py`: `read=None`, shorter connect/write/pool. Persist to source; survive container rebuilds.
- **20-LLM production server.** `ai_server_20llm_PRODUCTION.py`: backlog 2048, keep-alive 600s. BakLLaVA disable guard must be preserved in all future versions.
- **Semaphore proxy.** Mandatory intermediary port 8030. Float `timeout: 600.0`. Permanent decision (2026-03-02).
- **BBB output guard timeout.** `apply_output_guards_async` must use `httpx.AsyncClient(timeout=8.0)`. `timeout=None` is a known regression risk. `BBB_OUTPUT_BLOCKING=true` must be preserved.
- **LM Synthesizer.** Port 8001. Calls `allis-ollama:11434/api/generate` with `llama3.1:latest`. Persona prompt must be preserved in all rebuilds. Phase 3.75 is permanently eliminated.
- **Judge pipeline.** Consensus answer only — never raw_responses dump. All 5 judge containers in `docker-compose.yml` with `build: context: ./services, dockerfile: Dockerfile.judge` and `restart: unless-stopped`. `judge_to_pituitary_bridge.py` must be volume-mounted into `allis-judge-pipeline`. Ghost containers on `container_name:` slot block volume mounts — clear orphans before recreating. ML-DSA-65 keys: back up `judge-keys/judge_sk.bin` (4032 bytes) to offline storage.
- **ChromaDB.** Host port **8002** (v2 API). Container-to-container: `allis-chroma:8000`. v1 path deprecated. Required model: `all-minilm:latest` (384-dim). **48 collections, 6,740,034 vectors** (April 16). `ms_allis_memory`: 50 docs — self-heals via consciousness bridge line 74. `appalachian_cultural_intelligence`: 890 docs, threshold ≥563. Preflight thresholds use `-ge` not `-eq`.
- **msallis-db.** Port 5433, bound to `127.0.0.1` (corrected April 16 — orphaned container removed, recreated via compose). GBIM entity store is **ChromaDB `gbim_worldview_entities`** (5,416,521 vectors), not a relational table.
- **msallisgis.** Port 5432, **45 GB, 551 tables** (April 16 confirmed).
- **Community resources.** Port 5435, **64 verified resources, all 55 WV counties** (April 16 preflight).
- **Autonomous learner.** Port 8425. `autonomous_learner` collection, 21,181+ records, growing. EEG Beta (8075) drives 5-min learning cycles.
- **EEG stack.** `Dockerfile.eeg` single image for all three EEG services. `eeg_shared/pia_state.py` reads `ALLIS_PIA_STATUS_URL` from env. EEG blocks must be inserted before `networks:` key in `docker-compose.yml` — structural fix (April 16). Preflight gate includes EEG health checks. Backups in `~/msallis-repair-backups/`.
- **nbb_pituitary_gland.** Port 8108, `127.0.0.1`. Full spec Chapter 15. Mode `elevated` is current live state.
- **nbb_mother_carrie_protocols.** Port 8107. 5 protocols active, `MOTHER_CARRIE_KIDD` anchor.
- **Hippocampus.** Port 8011. Must be in all future compose definitions. Locked to `127.0.0.1`. Full spec Chapter 14.
- **69-DGM cascade.** Host port 19000 → internal 9000. Must be `127.0.0.1:19000:9000`. Never `0.0.0.0:9000`.
- **Port binding policy (permanent).** All services must be bound to `127.0.0.1` in `docker-compose.yml`. Verification: `docker ps --format "{{.Names}}\t{{.Ports}}" | grep "0.0.0.0"` must return empty. ★ Confirmed empty as of April 16, 2026. **109/109 containers Up.**
- **Async chat endpoints.** `/chat/async`, `/chat/status/{job_id}`, `/chat/cancel/{job_id}`, `/chat/cancel/all` — Redis-backed, 30-min TTL, true asyncio task cancellation. Preserve in all future main-brain rebuilds.
- **Compose management.** All 109 containers defined in `~/msallis-rebuild-working/msallis-rebuild/docker-compose.yml`. Docker Compose v5.1.0. ★ 109 containers confirmed Up, zero Restarting, zero Exited — April 16, 2026. Backups saved to `~/msallis-repair-backups/`.

**Git milestones:**

| Tag / Commit | Date | Milestone |
|---|---|---|
| `v2026.02.28-fabric-green` | 2026-02-28 | Baseline fabric operational |
| `v2026.03.01-fabric-32-32` | 2026-03-01 | All 32 fabric services passing health checks |
| `v2026.03.01-20llm-verified` | 2026-03-01 | 21/22 LLM consensus verified end-to-end |
| `v2026.03.01-neuro-pipeline-4-4` | 2026-03-01 | Full neurobiological pipeline (~300ms neuro sequence only; not full end-to-end) |
| `v2026.03.02-chatlight-async-working` | 2026-03-02 | Async chat + `normalize_identity()` confirmed |
| `b90f9ff` | 2026-03-15 | 79 containers: 22/22 LLMs + 3 PostgreSQL DBs + hippocampus + psych services + 7-filter BBB + 69-DGM + 349.87s benchmark |
| `a10725d7` | 2026-03-18 | Judge services brought under compose; 15 services locked to 127.0.0.1 |
| `5007d605` | 2026-03-18 | Remaining 10 services re-locked; zero 0.0.0.0 across all 80 containers |
| *(March 18 session)* | 2026-03-18 | Phase 1.45 community memory · BakLLaVA disabled · Phase 3.75 eliminated · judges evaluate consensus only · LM Synthesizer persona confirmed · all-minilm:latest 384-dim · Docker Compose v5.1.0 · all 80 containers compose-managed · zero 0.0.0.0 · ~436s CPU end-to-end |
| *(March 27 sprint)* | 2026-03-27 | AAPCAppE scraper: 53 RAG-loaded, 65 confirmed in Chroma; autonomous_learner growing beyond 21,181 baseline |
| *(March 28 remediation)* | 2026-03-28 | ★ Security remediation: `allis-i-containers` + `allis-memory` → 127.0.0.1; `_auth()` 4 routes; `ALLIS_API_KEY` set; 96/96 Up; ChromaDB 40 col / 6,675,442 vec; `spiritual_rag` deduped −19,338; `psychological_rag` restored 968 docs; `msallis` 5433 restored; `msallisgis` 5432 confirmed |
| *(April 1)* | 2026-04-01 | Autonomous learner debug: LEARN-01/02/03 resolved; 57-item recovery baseline |
| *(April 3)* | 2026-04-03 | `rag_grounded_v2` input judge activated |
| *(April 6)* | 2026-04-06 | `llm_judge_v3` output judge activated; `BBB_OUTPUT_BLOCKING=true`; GPU pipeline active on RTX 4070 |
| *(April 10)* | 2026-04-10 | `autonomous_learner` 21,181+ records confirmed |
| *(April 15)* | 2026-04-15 | Hallucination gap closed; `/chat` passed — `truthverdict: score 1.0, action passed` |
| `fdd3d13d` | 2026-04-16 | ★ **All 27 preflight gates ✅ green; 109/109 Up; GPU 102.58s confirmed; EEG Delta/Theta/Beta deployed; ML-DSA-65 all 5 judges; `judge_to_pituitary_bridge.py` mounted; `msallis-db` 0.0.0.0 → 127.0.0.1; `ms_allis_memory` rebuilt 50 docs; preflight thresholds corrected to -ge; ghost container 84207ec4fca7 cleared; docker-compose.yml structural fix; ChromaDB v2 48 col / 6,740,034 vec; Chapter 11 CLOSED** |

For the canonical description of how this entire fabric fits into a live user interaction, see **Chapter 17**. For the neurobiological architecture that structures the fabric, see **Chapter 12**. For the BBB 7-filter specification, see **Chapter 16**. For `nbb_pituitary_gland` full specification, see **Chapter 15**. For hippocampal specification, see **Chapter 14**. For qualia and EEG rhythms, see **Chapter 13**. For the 69-DGM cascade specification, see **Chapter 32**. For the three-database PostgreSQL architecture, see **Chapter 6**. For the judge pipeline and LLM ensemble specification, see **Chapter 33**.

**Chapter 11 is CLOSED. April 16, 2026 production state confirmed: 109/109 containers Up, all 27 preflight gates ✅ green, GPU pipeline 99–115s (102.58s confirmed), BBB_OUTPUT_BLOCKING=true, rag_grounded_v2 +
