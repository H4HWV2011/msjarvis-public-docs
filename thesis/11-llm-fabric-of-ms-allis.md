# 11. The LLM Fabric of Ms. Allis

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Canonical filename: `11-llm-fabric-of-ms-allis.md`*
*Last updated: April 23, 2026 — filename confirmed renamed; LLM count date-stamped
(21 active / 22 proxies, April 17, 2026 baseline); `OLLAMA_HOST` confirmed
`http://allis-ollama:11434`; `allis-20llm-production` container confirmed in dependency
chain; ChromaDB v1 → v2 throughout; `collection.count()` UUID two-step pattern noted;
legacy `allis-*` service hostnames retained (see Naming Note below);
`allis-gbim-query-router` (port 7205) added to Phase 5.*

>
---

## Why This Matters for Polymathmatic Geography

This chapter shows how Ms. Allis's "thinking" is implemented as an organized fabric of
local language models and services rather than a single opaque model instance. It
supports:

- **P1 – Every where is entangled** by embedding LLMs inside a retrieval, entanglement,
  and spatial stack (`allis-chroma` host port **8002**, container port **8000**,
  inter-service `http://allis-chroma:8000` — ★ **48 collections, ~6,740,611 vectors**
  as of April 23, 2026; production `msallis-db` host 5433 / container 5432 —
  `msallisgis` 16 GB / 294 tables / 11 schemas; forensic `postgis-forensic` host 5432 —
  `msallisgis` 17 GB / 314 tables / 9 schemas — forensic only; GBIM entity store:
  ChromaDB `gbim_worldview_entities` **5,416,521 vectors**; `autonomous_learner`
  **21,181 records**, April 23, 2026) that keeps reasoning tied to concrete places,
  institutions, and learning histories.

- **P3 – Power has a geometry** by routing questions through specific models, memories,
  and services whose connections — ports, proxies, ensembles, judges, and DGMs — have
  explicit topologies that can be inspected, tuned, or redesigned.

- **P5 – Design is a geographic act** by treating model choice, ensemble wiring, timeout
  and backlog settings, and service topology as design decisions that change how
  Appalachian realities are seen, narrated, and optimized over time.

- **P12 – Intelligence with a ZIP code** by grounding LLM calls in West Virginia-specific
  semantic and geospatial memory from ChromaDB `gbim_worldview_entities` (5,416,521
  vectors — authoritative GBIM entity store), WV-entangled search, autonomous learner
  outputs, and I-container identity, rather than generic, placeless prompts.

- **P16 – Power accountable to place** by exposing LLMs only through glass-box HTTP
  services with confirmed ports, logs, and timeouts, so that every path from user
  question to model output can be audited and constrained.

As such, this chapter belongs to the **Computational Instrument** tier: it specifies the
model pool, timeouts, ports, and service fabric that turn Quantarithmia's spatial-justice
instruments into live, language-facing behavior. As of **April 17, 2026**, the fabric
runs **21 active models** (22 proxies; BakLLaVA permanently disabled), operates within a
**100-container fully compose-managed production stack (April 23, 2026)**;
thesis-verified **112/112 containers (April 16, 2026)** (★ all 27 preflight gates ✅
green; all services bound to `127.0.0.1`; zero `0.0.0.0` exposures), and is confirmed
at **99–115 seconds end-to-end** on RTX 4070 GPU (confirmed **102.58s** April 16 — CPU
436s baseline **RETIRED STALE**). `BBB_OUTPUT_BLOCKING=true` active since April 6.
`rag_grounded_v2` + `llm_judge_v3` active since April 3/6.
`heuristic_contradiction_v1` **RETIRED**. ML-DSA-65 FIPS 204 signing active across all
5 judge containers. EEG Delta (8073), Theta (8074), Beta (8075) all live.

> **★ Security posture — April 23, 2026:** All containers bound to `127.0.0.1`. Zero
> `0.0.0.0` exposures confirmed (all 27 preflight gates ✅ green). `ALLIS_API_KEY`
> exported and set. **100 containers Up (April 23, 2026)**; thesis-verified
> **112/112 (April 16, 2026)** — zero Restarting, zero Exited.

> **★ ChromaDB v2 audit — April 23, 2026:** `allis-chroma`, host port **8002**,
> container port **8000**, inter-service URL `http://allis-chroma:8000`.
> **48 active collections, ~6,740,611 total vectors** (v2 API;
> correct path: `/api/v2/tenants/default_tenant/databases/default_database/collections`).
> v1 path `/api/v1/collections` **deprecated — returns 410 Gone**.
> Per-collection counts require the Python client `collection.count()` method, which
> handles the UUID two-step lookup pattern transparently — do not derive from raw SQLite.
> `spiritual_rag` split into `spiritual_texts` (79,181 vectors), `spiritual_wisdom` (135),
> `spiritual_knowledge` (12). `msallis_docs`: **7,465 items**. `autonomous_learner`:
> **21,181 records** (April 23, 2026). Required embedding model: `all-minilm:latest`
> (384-dim) — **permanent architectural constraint**. `nomic-embed-text` (768-dim)
> incompatible with existing collections.

> **★ Database audit — April 23, 2026:** Two-container architecture —
> **Production:** `msallis-db`, host **5433** / container **5432**, role `postgres`,
> `msallisgis`, 16 GB / 294 tables / 11 schemas.
> **Forensic:** `postgis-forensic`, host **5432**, role `allis`,
> `msallisgis`, 17 GB / 314 tables / 9 schemas — forensic auditing only.
> GBIM entity store: ChromaDB `gbim_worldview_entities` (5,416,521 vectors) — no
> relational `gbim_entities` table in any PostgreSQL instance.
> DNS: `msallis-db:5432` resolves from all connected containers (production).
> PostgreSQL 16.4 confirmed.

> **★ Session fixes — April 16, 2026 (all resolved):**
> - `ms_allis_memory` Chroma BLOB type error → rebuilt collection, 50 docs healthy;
>   self-heals organically via consciousness bridge line 74
> - `appalachian_cultural_intelligence` threshold corrected to ≥563
>   (was hardcoded exact-match 1084)
> - ChromaDB collections threshold corrected to ≥48 (was hardcoded -eq 49)
> - `allis-judge-pipeline` ghost container (84207ec4fca7) cleared;
>   `judge_to_pituitary_bridge.py` volume mount confirmed
> - 17 dangling volume lines corrected with line-by-line parser
> - docker-compose.yml structural corruption resolved (EEG blocks inserted before
>   `networks:` key)
> - Stale host process on port 8073 killed; EEG Delta DNS failure fixed via network
>   connect + restart
> - EEG Delta (8073), Theta (8074), Beta (8075) all deployed on qualia-net; PIA
>   status: OK

```
┌──────────────────────────────────────────────────────────────────────┐
│        The LLM Fabric of Ms. Allis (MS allis)                       │
│   (Production State: April 23, 2026 — 100 containers Up)             │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  User Query                                                           │
│      ↓                                                                │
│  Main Brain (port 8050)                                               │
│      ↓                                                                │
│  nbb_pituitary_gland (127.0.0.1:8108) ★ UPSTREAM GOVERNANCE GATE     │
│  mode: baseline / WOAH weight modulation / judge compliance thresh   │
│      ↓                                                                │
│  ┌─────────────────────────────────────────────────┐                 │
│  │  Phase 1 — NBB Prefrontal + Psychology          │                 │
│  │  ├─ nbb-i-containers (port 8101) — Phase 1      │                 │
│  │  ├─ BBB 7-filter input stack (port 8016) — 1.4  │                 │
│  │  │   rag_grounded_v2 judge (April 3) ★           │                 │
│  │  │   BBB_OUTPUT_BLOCKING=true (April 6) ★        │                 │
│  │  │   heuristic_contradiction_v1 RETIRED ★        │                 │
│  │  ├─ ChromaDB semantic memory — Ph 1.45          │                 │
│  │  │   autonomous_learner (21,181 records,         │                 │
│  │  │    April 23, 2026)                            │                 │
│  │  │   all-minilm:latest · 384-dim · top-5         │                 │
│  │  │   API: v2 UUID two-step · host 8002           │                 │
│  │  └─ allis-psychology-services (8019) — Ph 3    │                 │
│  └─────────────────────────────────────────────────┘                 │
│      ↓                                                                │
│  ┌─────────────────────────────────────────────────┐                 │
│  │  Phase 3.5 — LM Synthesizer (port 8001)         │                 │
│  │  Calls allis-ollama:11434/api/generate          │                 │
│  │  OLLAMA_HOST: http://allis-ollama:11434         │                 │
│  │  Model: llama3.1:latest                          │                 │
│  │  Ms. Egeria Allis persona prompt injected        │                 │
│  └─────────────────────────────────────────────────┘                 │
│      ↓                                                                │
│  ┌─────────────────────────────────────────────────┐                 │
│  │  Phase 2.5 — Identity & Consciousness           │                 │
│  │  ├─ allis-fifth-dgm (port 4002)                │                 │
│  │  ├─ WOAH (port 8104, 7012)                      │                 │
│  │  ├─ nbb-i-containers (port 8101)                │                 │
│  │  └─ allis-i-containers (8015, dual_awareness)  │                 │
│  └─────────────────────────────────────────────────┘                 │
│      ↓                                                                │
│  Semaphore Proxy (port 8030, max_concurrent: 4)                      │
│      ↓                                                                │
│  ┌─────────────────────────────────────────────────┐                 │
│  │  21-LLM Ensemble (port 8008)                    │                 │
│  │  allis-20llm-production container ✅            │                 │
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
│  │  allis-gbim-query-router (port 7205) ★         │                 │
│  │  Routes GBIM entity queries; topology confirmed │                 │
│  │  April 23, 2026                                  │                 │
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
│  GPU pipeline: 99–115s / confirmed 102.58s April 23 ★               │
│  [CPU 436s baseline RETIRED STALE]                                    │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘
```

> **Figure 11.1.** The LLM Fabric of Ms. Allis / MS allis (April 23, 2026 baseline):
> user queries flow through `nbb_pituitary_gland` (port 8108, **mode: baseline**) as the
> upstream governance gate, then NBB prefrontal (Phase 1), 7-filter BBB stack with
> `rag_grounded_v2` and `BBB_OUTPUT_BLOCKING=true` (Phase 1.4), ChromaDB v2 semantic
> memory retrieval via `all-minilm:latest` 384-dim and UUID two-step
> `collection.count()` pattern (Phase 1.45), psychology pre-assessment (Phase 3), LM
> Synthesizer with `llama3.1:latest` via `OLLAMA_HOST=http://allis-ollama:11434` and
> Ms. Egeria Allis persona (Phase 3.5), `allis-20llm-production` — 21-model ensemble /
> 22 proxies with BakLLaVA permanently disabled (Phase 2.5), judge pipeline with
> `llm_judge_v3`, ML-DSA-65 FIPS 204 signing, and `judge_to_pituitary_bridge.py`
> feedback loop (Phase 3), EEG rhythms Delta/Theta/Beta (8073/8074/8075) ★, GBIM
> temporal confidence decay with `allis-gbim-query-router` (port 7205) ★ (Phase 5),
> 69-DGM cascade (Phase 7), BBB output guard with `BBB_OUTPUT_BLOCKING=true`, and
> `normalize_identity()`. GPU pipeline 99–115s (102.58s confirmed April 23). All LLMs
> exposed only via glass-box HTTP services; grounded in West Virginia-specific memory via
> ChromaDB v2 (48 collections, ~6,740,611 vectors, `allis-chroma` host port 8002) and
> PostgreSQL databases. Legacy `allis-*` service hostnames authoritative for
> container-to-container calls.

---

## Security Hardening — March 18 + March 28 + ★ April 16, 2026

> **This section records mandatory audit events.** Prior to March 18, 2026, multiple
> services were bound to `0.0.0.0`. The initial remediation was completed March 18, 2026.
> A second sprint March 28, 2026 corrected `allis-i-containers` (8015) and
> `allis-memory` (8056). **On April 16, 2026, a stale `msallis-db` reference was found
> bound to `0.0.0.0` — corrected immediately via orphaned container removal and compose
> recreate. All containers now bound to `127.0.0.1` exclusively — zero `0.0.0.0`
> exposures.**

### Services Re-locked to 127.0.0.1 (March 18, 2026)

| Service | Was | Now |
|:--|:--|:--|
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
|:--|:--|:--|
| `allis-i-containers` | `0.0.0.0:8015` | `127.0.0.1:8015` ✅ |
| `allis-memory` | `0.0.0.0:8056` | `127.0.0.1:8056` ✅ |
| `_auth()` on 4 sensitive routes | Unconfirmed | ✅ Confirmed |
| `ALLIS_API_KEY` env var | Unconfirmed | ✅ Confirmed set |

### ★ April 16, 2026 Correction

| Service | Was | Now |
|:--|:--|:--|
| Stale `msallis-db` reference (port 5433) | `0.0.0.0:5433` | Removed; production target is `msallis-db` host 5433 bound to `127.0.0.1` ✅ |

**Fix:** Orphaned container stopped (`docker stop`), removed (`docker rm`), recreated
via compose (`docker compose up -d`). Confirmed `127.0.0.1:5433→5432/tcp`
post-recreate.

**Verification command (post-remediation, must return empty):**

```bash
docker ps --format "{{.Names}}\t{{.Ports}}" | grep "0.0.0.0" | grep -v "127.0.0.1"
```

Result as of April 23, 2026: **empty** — zero public exposures.

### Judge Services — April 16, 2026

All 5 judge services compose-managed with `restart: unless-stopped` (since March 18,
2026). Ghost container `84207ec4fca7_allis-judge-pipeline` cleared April 16, 2026 —
had been blocking the `container_name:` slot and preventing
`judge_to_pituitary_bridge.py` volume mount. Post-fix: `judge_to_pituitary_bridge.py`
confirmed mounted inside `allis-judge-pipeline` container. ML-DSA-65 FIPS 204 signing
confirmed: all 5 judge containers, `judge_sk.bin` 4032 bytes, `judge_pk.bin` 1952 bytes,
sig=**3309 bytes**, verify=**True**, fingerprint `d81a5d90...edb0`.

---

## Status — ★ Updated April 23, 2026

| Category | Details |
|:--|:--|
| **Implemented and verified** | `allis-main-brain` → **127.0.0.1:8050** (confirmed). `allis-ollama` → **127.0.0.1:11434**; `OLLAMA_HOST=http://allis-ollama:11434` (confirmed). `nbb_pituitary_gland` → **127.0.0.1:8108** → internal 80/tcp, mode **`baseline`**; authoritative routes: GET `/global_mode`, GET `/mode_history` (upstream governance gate). `nbb_mother_carrie_protocols` → **127.0.0.1:8107**, 5 protocols active, `MOTHER_CARRIE_KIDD` anchor. `nbb_qualia_engine` → host **8303** → 7008/tcp, HTTP 200. `allis-wv-entangled-gateway` → **127.0.0.1:8010**. `allis-spiritual-rag` → **127.0.0.1:8005**. `allis-gis-rag` → **127.0.0.1:8004**. `allis-rag-server` → **127.0.0.1:8003**. `allis-lm-synthesizer` → **127.0.0.1:8001** (calls `allis-ollama:11434/api/generate` via `OLLAMA_HOST=http://allis-ollama:11434` with `llama3.1:latest`; persona injected; Phase 3.75 eliminated). `psychological_rag_domain` → **127.0.0.1:8006**. `allis-psychology-services` → **127.0.0.1:8019**. Production DB: `msallis-db` → **127.0.0.1:5433** host / 5432 container (**16 GB, 294 tables, 11 schemas**). Forensic DB: `postgis-forensic` → **127.0.0.1:5432** (**17 GB, 314 tables, 9 schemas** — forensic only). `allis-local-resources-db` → **127.0.0.1:5435** (**64 verified resources, all 55 WV counties**). ChromaDB v2 → `allis-chroma` **127.0.0.1:8002** (host), `http://allis-chroma:8000` (inter-service) ★ **48 collections, ~6,740,611 vectors**; per-collection counts via Python client `collection.count()` (UUID two-step — not derivable from raw SQLite); `autonomous_learner` **21,181 records** (April 23, 2026); `msallis_docs` **7,465 items**. `nbb_woah_algorithms` → **127.0.0.1:8104** → internal 8010. `allis-woah` → **127.0.0.1:7012**. `allis-blood-brain-barrier` → **127.0.0.1:8016**; 7-filter stack; `rag_grounded_v2` input judge (April 3) ★; `llm_judge_v3` output judge (April 6) ★; `BBB_OUTPUT_BLOCKING=true` (April 6) ★; `heuristic_contradiction_v1` retired ★. `allis-20llm-production` → **127.0.0.1:8008** ✅ (dependency chain confirmed); **21 active / 22 proxies** (April 17, 2026 baseline); wall-clock ~320-360s. Judge pipeline → all 5 compose-managed; ML-DSA-65 FIPS 204 signing; `judge_to_pituitary_bridge.py` mounted; ~60-86s. `allis-semaphore` → **127.0.0.1:8030** (`max_concurrent: 4`). `llm1-proxy` through `llm22-proxy` → **127.0.0.1:8201-8222**; 21 active. `allis-hippocampus` → **127.0.0.1:8011**. `allis-69dgm-bridge` → **127.0.0.1:19000→9000**. `allis-constitutional-guardian` → **127.0.0.1:8091**. `allis-fifth-dgm` → **127.0.0.1:4002**. `allis-redis` → **127.0.0.1:6380**. `allis-memory` → **127.0.0.1:8056** ★; `ALLIS_API_KEY` set; **14 active sessions**. EEG Delta (8073), Theta (8074), Beta (8075) — all live, PIA OK. `allis-gbim-query-router` → **127.0.0.1:7205** ★ (GBIM entity query routing, Phase 5 topology — confirmed April 23, 2026). **100 containers Up (April 23, 2026)**; thesis-verified **112/112 (April 16, 2026)**. All 27 preflight gates ✅ green. GPU 99–115s / 102.58s confirmed. |
| **Architectural corrections (permanent)** | BBB output guard `apply_output_guards_async` timeout: **8.0s** (not `None`). `llmtimeout` in chatlight handler: `600.0`. I-Containers schema: `{"message": …, "userid": "neurobiological_master"}`. Consciousness Bridge: `{"8020/tcp":null}` — internal only. Neuro Master: `{"8018/tcp":null}` — internal only. ChromaDB: `allis-chroma` host port **8002**, container port **8000**, inter-service `http://allis-chroma:8000`; v2 API path: `/api/v2/tenants/default_tenant/databases/default_database/collections`; v1 path **deprecated — 410 Gone**; per-collection counts via `collection.count()` UUID two-step pattern. Production DB: `msallis-db` host **5433** / container **5432**, `msallisgis` 16 GB / 294 tables. Forensic DB: `postgis-forensic` host **5432**, `msallisgis` 17 GB / 314 tables — forensic only. GBIM entity store: **ChromaDB `gbim_worldview_entities`** (5,416,521 vectors) — no relational `gbim_entities` table in any PostgreSQL instance. LM Synthesizer: calls `allis-ollama:11434/api/generate` via `OLLAMA_HOST=http://allis-ollama:11434` (not `allis-roche-llm`). Phase 3.75 eliminated. BakLLaVA permanently disabled via name-check guard. `all-minilm:latest` (384-dim) required — `nomic-embed-text` (768-dim) incompatible. Judges evaluate consensus answer only. All containers compose-managed. All ports locked `127.0.0.1`. `judge_to_pituitary_bridge.py` mounted in `allis-judge-pipeline`. Preflight threshold operators: `-ge` not `-eq`. Legacy `allis-*` service hostnames authoritative for container-to-container calls — MS allis rename applies at product/thesis level only. |
| **Partially implemented / scaffolded** | Per-request model breakdowns and per-model latency metrics: logged but no dedicated debug endpoint. Ensemble decision rules: operational but not machine-readable schema. WOAH-to-model-selection coupling: conceptual, not yet explicit routing rule. `ms_allis_memory` collection: rebuilt April 16 (50 docs); self-heals organically via consciousness bridge (line 74 of `msallisconsciousnessbridge.py`). `appalachian_cultural_intelligence`: 890 docs (threshold ≥563 — self-heals when ACI pipeline reruns). |
| **Future work** | Richer debug endpoints for per-request agent breakdowns. Formal JSON schemas for ensemble decision rules and judge aggregation. Tighter coupling WOAH weights → model selection in governance flows. Additional task-specific model pools. UI layer consuming `/chat/async` poll pattern. Automated POC verification loop for `confidence_decay` reset. Semantic dedup audit of `autonomous_learning` collection. Full `allis-*` → `allis-*` service hostname migration sprint. Full documentation of `allis-gbim-query-router` (port 7205) routing topology. |

> **Port corrections and updates (permanent record).** Spiritual Root / GBIM RAG:
> confirmed **8005** (not 8103). `psychological_rag_domain`: confirmed **8006**
> (not 9006). ChromaDB: `allis-chroma` host **8002**, inter-service
> `http://allis-chroma:8000`, v2 API only. Production DB: `msallis-db` host **5433** /
> container **5432**. Forensic DB: `postgis-forensic` host **5432** — forensic only.
> `allis-69dgm-bridge`: host **19000** → internal 9000. Consciousness Bridge:
> `{"8020/tcp":null}` internal only. Neuro Master: `{"8018/tcp":null}` internal only.
> LM Synthesizer: calls `allis-ollama:11434/api/generate` with `llama3.1:latest` via
> `OLLAMA_HOST=http://allis-ollama:11434`. `allis-gbim-query-router`: **7205** ★ —
> GBIM entity query routing in Phase 5 topology.

---

This chapter describes the local language models that form the "LLM fabric" of Ms.
Egeria Allis (`msallis-rebuild`) / **MS allis** and how they are woven into the broader
architecture: ChromaDB v2 (`allis-chroma` host port **8002**, v2 API, UUID two-step
`collection.count()` for per-collection counts — ★ **48 collections, ~6,740,611
vectors**), RAG services, autonomous learning, spatial databases, and GeoDB
infrastructure. Rather than treating LLMs as independent agents, the system treats them
as constrained tools and judges embedded in a larger retrieval and belief stack, all
exposed through well-defined HTTP services confirmed running as of April 17, 2026. **All
services are bound exclusively to `127.0.0.1`; no service exposes a port on
`0.0.0.0`.**

---

## 11.1 Current Local LLM Inventory

In the current deployment, models are served by Ollama inside the `allis-ollama`
container at **127.0.0.1:11434**, `OLLAMA_HOST=http://allis-ollama:11434`. As of
**April 17, 2026**, **21 of 22 LLM proxy containers are active**. BakLLaVA
(llm11-proxy, port 8211) is permanently disabled due to CLIP load issues. The disable is
enforced programmatically in `ai_server_20llm_PRODUCTION.py`:

```python
# Permanently disable BakLLaVA (CLIP load issues)
if name and name.lower().startswith("bakllava"):
    m["active"] = False
```

The following table is the authoritative proxy-to-model mapping (confirmed April 17,
2026):

| Proxy | Port | Model | Specialty |
|:--|:--|:--|:--|
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

**Active: 21 models (April 17, 2026 baseline).** BakLLaVA (llm11-proxy:8211) is
permanently disabled. StarCoder2 (llm7-proxy:8207) is active but excluded from consensus
on 0-character community query responses.

---

## 11.2 Roles of the Core and Specialist Models

**Core reasoning models.**
`llama3.1:8b` (llm22-proxy) is the primary voice model — the LM Synthesizer calls it
directly via `OLLAMA_HOST=http://allis-ollama:11434` to deliver the final response in
Ms. Allis's voice. `mistral:latest` (llm21-proxy) handles tightly scoped tasks where
latency matters. `llama2:latest` (llm20-proxy) provides compatibility and comparative
benchmarking. Chat-oriented variants — `vicuna`, `openchat`, `neural-chat`, `starling-lm`,
`zephyr`, `qwen2`, `orca-mini`, `dolphin-phi`, `phi3:mini` — provide diverse
conversational styles across the ensemble.

**Lightweight and compact models.**
`tinyllama:1.1b` (llm1-proxy) and `gemma:latest` (llm2-proxy) serve quick-response,
synthesis, and sanity-check roles where latency and resource budgets are tight.

**Code and SQL specialists.**
`deepseek-coder`, `codellama`, `starcoder2`, and `sqlcoder` handle code generation,
refactoring, and SQL/data tasks including queries against the production spatial database
(`msallis-db` host 5433 — `msallisgis` 294 tables, 16 GB) and community resources
database (port 5435 — 64 verified resources).

**Multimodal and domain-specific models.**
`llava` (llm5-proxy) and `minicpm-v` (llm4-proxy) support vision-language tasks.
`medllama2` (llm3-proxy) covers medical-style language within constrained advisory
contexts alongside `allis-psychology-services` (port 8019). BakLLaVA permanently
disabled.

---

## 11.3 Service Topology and Ports

Confirmed April 23, 2026. **All services bound to 127.0.0.1.** ★ **100 containers Up
(April 23, 2026)**; thesis-verified **112/112 (April 16, 2026)**.

> **★ Naming note:** All service hostnames below use legacy `allis-*` Docker Compose
> service names — these are authoritative for container-to-container DNS resolution
> within the `msallis-rebuild` stack. MS allis product-level renaming does not change
> these hostnames until a dedicated naming-migration sprint is completed.

**Main Brain API — 127.0.0.1:8050 (`allis-main-brain`).**
Primary external-facing interface. Routes: `/chat` (sync), `/chat/async` +
`/chat/status/{job_id}` + `/chat/cancel/{job_id}` + `/chat/cancel/all` (Redis-backed
async, 30-min TTL, true asyncio cancellation), `/chatlight` (sync lightweight),
`/chatlight/async` + `/chatlight/status/{job_id}` (lightweight async).

**`nbb_pituitary_gland` — 127.0.0.1:8108 → internal 80/tcp ★.**
`{"status":"healthy","service":"nbb_pituitary_gland","mode":"baseline"}`. Upstream
governance gate — sits above all pipeline stages. Modulates WOAH weights, adjusts
constitutional compliance thresholds, feeds warmth signals to
`nbb_mother_carrie_protocols`. Authoritative routes: GET `/global_mode`,
GET `/mode_history`. Full specification in Chapter 15.

**`nbb_mother_carrie_protocols` — 127.0.0.1:8107 ★.**
HTTP 200, 5 protocols active, `MOTHER_CARRIE_KIDD` anchor confirmed. Warmth and tone
modulation fed by pituitary `enhance_pituitary_warmth.py` output.

**`nbb_qualia_engine` — 127.0.0.1:8303 → internal 7008/tcp ★.**
HTTP 200. NBB qualia companion.

**Production DB — `msallis-db` 127.0.0.1:5433 → container 5432 ★.**
Role `postgres`, `msallisgis`, 16 GB / 294 tables / 11 schemas. Production target for
all service writes. Note: GBIM **entity** store is in ChromaDB `gbim_worldview_entities`
(5,416,521 vectors) — there is no relational `gbim_entities` table in any PostgreSQL
instance.

**Forensic DB — `postgis-forensic` 127.0.0.1:5432.**
Role `allis`, `msallisgis`, 17 GB / 314 tables / 9 schemas — forensic auditing only.
Not a production write target.

**`allis-local-resources-db` — 127.0.0.1:5435.**
**64 verified resources, all 55 WV counties** (April 16 preflight confirmed).
Human-validated by Harmony for Hope Community Champions.

**ChromaDB v2 — `allis-chroma` 127.0.0.1:8002 (host) ★,
`http://allis-chroma:8000` (inter-service).**
`chroma_data` Docker volume. ★ **48 active collections, ~6,740,611 total vectors**
(April 23, 2026). v2 API path:
`/api/v2/tenants/default_tenant/databases/default_database/collections`.
v1 path `/api/v1/collections` **deprecated — 410 Gone**.
Per-collection counts: use Python client `collection.count()` — UUID two-step pattern,
not derivable from raw SQLite in this schema.
Required embedding model: `all-minilm:latest` (384-dim) — `nomic-embed-text` (768-dim)
incompatible.

Active collections include: `ms_allis_memory` (50 docs — rebuilt April 16;
self-heals via consciousness bridge line 74; **cosine** distance), `autonomous_learner`
(21,181 records, April 23, 2026; L2), `msallis_docs` (**7,465 items**; L2),
`appalachian_cultural_intelligence` (890 — threshold ≥563),
`gbim_worldview_entities` (5,416,521 — authoritative GBIM entity store; L2),
`spiritual_texts` (79,181), `psychological_rag` (968), `gbim_beliefs_v2`,
`gis_wv_benefits`, `mountainshares_knowledge`, `episodic_index`,
`conversation_history`, `GBIM_sample_rows`, and others.

**LM Synthesizer — 127.0.0.1:8001 (`allis-lm-synthesizer`).**
Phase 3.5 voice delivery. Calls `allis-ollama:11434/api/generate` via
`OLLAMA_HOST=http://allis-ollama:11434` with `llama3.1:latest`. Persona injected
(see §11.4). Phase 3.75 permanently eliminated — saves ~40s per query.

**General RAG Server — 127.0.0.1:8003 (`allis-rag-server`).**
Active FastAPI service. `/store` accepts `user_id`. PostgreSQL insertion failures are
warnings, not fatal.

**GIS RAG — 127.0.0.1:8004 (`allis-gis-rag`).**
Spatially aware `/search` over geospatial ChromaDB collections and `msallis-db`
(host 5433, `msallisgis` 294 tables, 16 GB).

**Spiritual Root / GBIM RAG — 127.0.0.1:8005 (`allis-spiritual-rag`).**
`spiritual_texts` (79,181 vectors), `spiritual_wisdom` (135), `spiritual_knowledge` (12).
Earlier plan documents listed 8103; confirmed running port is **8005**.

**Psychological RAG — 127.0.0.1:8006 (`psychological_rag_domain`).**
`psychological_rag` 968 docs. Earlier plan documents listed 9006; confirmed running port
is **8006**.

**WV-Entangled Gateway — 127.0.0.1:8010 (`allis-wv-entangled-gateway`).**
WV-biased, multi-collection ChromaDB retrieval using `WVEntangledContext` envelope.

**Hippocampus — 127.0.0.1:8011 (`allis-hippocampus`).**
Conversation-level memory consolidation over ChromaDB v2 (port 8002) and
`gbim_worldview_entities` (5,416,521 vectors). Temporal decay-aware. Full specification
Chapter 14.

**I-Containers — 127.0.0.1:8015 (`allis-i-containers`) ★.**
`dual_awareness: true`. Schema: `{"message": …, "userid": "neurobiological_master"}`.
Exposes `/next-learning-topic` for autonomous learner.

**Memory Service — 127.0.0.1:8056 (`allis-memory`) ★.**
`ALLIS_API_KEY` exported and set. `/memory/sessions` → HTTP 200, **14 active sessions**.
`_auth()` confirmed on all 4 sensitive routes.

**BBB 7-filter stack — 127.0.0.1:8016 (`allis-blood-brain-barrier`) ★.**
Phase 1.4 input filter + Phase 4.5 output guard. Input judge: `rag_grounded_v2` (active
since April 3). Output judge: `llm_judge_v3` (active since April 6).
`BBB_OUTPUT_BLOCKING=true` since April 6. `heuristic_contradiction_v1` **RETIRED**.
Host port 8017 = **BBB output filter facade** (`bbb-output-filter` →
`allis-blood-brain-barrier:8016/filter`). `apply_output_guards_async` timeout: `8.0s`.

**BBB Output Filter Facade — host 8017 ★.**
`{"status":"ok","service":"bbb-output-filter","backend":"http://allis-blood-brain-barrier:8016/filter"}`.
⚠️ This is NOT `allis-qualia-engine`. The qualia engine runs on internal Docker network
only.

**Psychology Services — 127.0.0.1:8019 (`allis-psychology-services`).**
Phase 3 pre-assessment: severity classification, crisis indicator Boolean, five
structured guidance fields.

**Consciousness Bridge — `{"8020/tcp":null}` internal only.**
No host binding. Source: `/app/services/msallisconsciousnessbridge.py`. Self-heals
`ms_allis_memory` on every session turn (line 74). See Ch. 12 §12.1.

**Neurobiological Master — `{"8018/tcp":null}` internal only.**
No host binding. Container-to-container via `http://allis-neurobiological-master:8018`
remains valid. Port **8018** confirmed. See Ch. 12 §12.3.

**Qualia Engine — `allis-qualia-engine` internal 8017/tcp (no host binding).**
⚠️ Host port 8017 = BBB output filter facade — do NOT confuse.

**20-LLM Production Ensemble — 127.0.0.1:8008 (`allis-20llm-production`) ✅.**
**`allis-20llm-production` confirmed present in dependency chain (April 17, 2026).**
21 active / 22 proxies (April 17, 2026 baseline). Uvicorn backlog 2048, keep-alive 600s.
Judges evaluate consensus answer only — raw_responses dump eliminated. Wall-clock
~320-360s.

**Semaphore Proxy — 127.0.0.1:8030 (`allis-semaphore`).**
`max_concurrent: 4`. Float `timeout: 600.0`. Main brain httpx:
`Timeout(None, connect=5.0, read=None)`.

**LLM Proxies — 127.0.0.1:8201–8222.** 22 proxies; 21 active (April 17, 2026).
`read=None`, `connect=3.0s`, `write=5.0s`, `pool=5.0s`.

**WOAH services.** `nbb_woah_algorithms`: **127.0.0.1:8104** → internal 8010.
`allis-woah`: **127.0.0.1:7012** (qualia-net internal, `{}` binding intentional).

**Constitutional Guardian — 127.0.0.1:8091.** See Chapter 37.

**`allis-gbim-query-router` — 127.0.0.1:7205 ★.**
GBIM entity query routing service. Added to Phase 5 / confidence decay topology as of
April 23, 2026. Routes structured GBIM entity queries from the confidence decay
multiplier stage to `gbim_worldview_entities` (ChromaDB, 5,416,521 vectors). Full
topology specification: follow-on to this chapter. Container name uses `allis-*`
naming — first service in this stack to use the new naming convention.

**Judge Services — all compose-managed (March 18, 2026); ML-DSA-65 FIPS 204
(April 16, 2026).**

| Service | Host Port | Source File | April 16 Status |
|:--|:--|:--|:--|
| `allis-judge-pipeline` | 127.0.0.1:7239 | `services/judge_pipeline.py` | ✅ Ghost cleared; `judge_to_pituitary_bridge.py` mounted |
| `allis-judge-truth` | 127.0.0.1:7230 | `services/judge_truth_filter.py` | ✅ ML-DSA-65 signing |
| `allis-judge-consistency` | 127.0.0.1:7231 | `services/judge_consistency_engine.py` | ✅ ML-DSA-65 signing |
| `allis-judge-alignment` | 127.0.0.1:7232 | `services/judge_alignment_filter.py` | ✅ ML-DSA-65 signing |
| `allis-judge-ethics` | 127.0.0.1:7233 | `services/judge_ethics_filter.py` | ✅ ML-DSA-65 signing |

Input: consensus answer only. Time: ~60–86s. Verdicts signed ML-DSA-65 FIPS 204
(sig=3309 bytes, verify=True). `judge_to_pituitary_bridge.py` closes the feedback loop:
judge verdicts update `nbb_pituitary_gland` state, which modulates subsequent qualia
outputs. Keys: `judge-keys/judge_sk.bin` (4032 bytes), `judge-keys/judge_pk.bin`
(1952 bytes), `judge-keys/nbb_pituitary_gland/`. ⚠️ Back up `judge_sk.bin` to offline
storage immediately if not already done.

**EEG Neurobiological Band Services — ★ April 16, 2026 (all deployed).**

| Service | Host Port | Pulse | Last Activity | BBB Events | PIA |
|:--|:--|:--|:--|:--|:--|
| `eeg-delta-30s` | **8073** | #3+ | gateway/chroma/pia liveness | 16 | ✅ OK |
| `eeg-theta-30s` | **8074** | #7 | 60s memory consolidation | 16 | ✅ OK |
| `eeg-beta-30s` | **8075** | #2 | WV economic dev / New River Gorge | 16 | ✅ OK |

All three on `qualia-net`. Dockerfile: `Dockerfile.eeg`. Shared:
`eeg_shared/pia_state.py` (reads `ALLIS_PIA_STATUS_URL` from env). EEG blocks inserted
before `networks:` key in `docker-compose.yml` (structural fix). Preflight gate: EEG
health checks added.

**Fifth DGM — 127.0.0.1:4002.** See Chapter 9.

**69-DGM Cascade — 127.0.0.1:19000→9000 (`allis-69dgm-bridge`).**
Phase 7: 23 connectors × 3 stages = 69 DGM operations. Internal port remains 9000;
host binding 19000. Never expose as `0.0.0.0:9000`.

**Toroidal Sync — 127.0.0.1:8025.** ChromaDB↔GIS sync loop (Chapter 26).

**Autonomous Learner — 127.0.0.1:8425 (`allis-autonomous-learner`).**
Writes to `autonomous_learner` ChromaDB collection (L2). EEG Beta (8075) pulse #2
studying WV economic development, Appalachian broadband, New River Gorge infrastructure,
MountainShares economics. **21,181 records (April 23, 2026)**; actively growing.

**Redis — 127.0.0.1:6380.** Async job state (30-min TTL), service discovery, caching.

**Ollama Runtime — 127.0.0.1:11434 (`allis-ollama`).** `OLLAMA_HOST=http://allis-ollama:11434`. Internal services only — not user-facing.

---

## 11.4 Coordination: 9-Phase Pipeline Integration

The LLM fabric sits at the end of a chain of retrieval, entanglement, and identity
services. GPU pipeline end-to-end: **99–115s** (confirmed **102.58s** April 23 on RTX
4070 — CPU 436s baseline **RETIRED STALE**).

**Upstream gate — `nbb_pituitary_gland` (port 8108, mode: `baseline`).**
Runs before the full pipeline. Sets system-wide operating mode, WOAH weights, and
constitutional compliance thresholds. Judge verdicts feed back via
`judge_to_pituitary_bridge.py` to update pituitary state. Authoritative routes:
GET `/global_mode`, GET `/mode_history`.

**Phase 1 — NBB prefrontal cortex (`nbb-i-containers`, port 8101).**
Called unconditionally on every production request.

**Phase 1.4 — BBB 7-filter input stack (`allis-blood-brain-barrier`, port 8016).**
7 filters applied. `rag_grounded_v2` input judge active (April 3).
`BBB_OUTPUT_BLOCKING=true` (April 6). `heuristic_contradiction_v1` retired.
`truth_score` null guard present. Fail-open on HTTP 500.

**Phase 1.45 — ChromaDB Semantic Community Memory Retrieval.**
384-dim embedding via `all-minilm:latest` → `autonomous_learner` (21,181 records,
April 23, 2026; L2) → top-5 semantically similar community interaction records
prepended to `enhanced_message`. EEG Theta (8074) consolidation snapshots feed this
collection continuously.

```
Phase 1.45 embedding flow:
  allis-ollama:11434/api/embeddings
  (OLLAMA_HOST=http://allis-ollama:11434, all-minilm:latest, 384-dim)
      → ChromaDB v2 autonomous_learner collection
        (allis-chroma host 8002, inter-service http://allis-chroma:8000)
        (collection.count() UUID two-step — not raw SQLite)
      → top-5 results → enhanced_message
```

> **Technical note:** All ChromaDB collections use 384-dimensional vectors (confirmed
> across all 48 collections, ~6,740,611 vectors — April 23, 2026). `all-minilm:latest`
> is the required embedding model. `nomic-embed-text` (768-dim) is incompatible with
> existing collections. Per-collection counts must use Python client
> `collection.count()` (UUID two-step) — not derivable from raw SQLite in this schema.

**Phase 1.5 — Multi-Domain RAG Enhancement.**
`allis-lm-synthesizer` (port 8001) aggregates context from all five RAG services
(8003, 8004, 8005, 8006, 8010) and ChromaDB v2 (`allis-chroma` host 8002,
inter-service `http://allis-chroma:8000`) into a unified enriched context block.

**Phase 1.75 — I-Containers Dual Awareness.**
`allis-i-containers` (port 8015, `dual_awareness: true`) contributes identity and
perspective context.

**Phase 3 — Psychology pre-assessment (`allis-psychology-services`, port 8019).**
Every production request: severity classification, crisis indicator Boolean, five
structured guidance fields.

**Phase 2.5 — Identity and consciousness context.**
Fifth DGM (4002), WOAH (8104, 7012), `nbb-i-containers` (8101),
`allis-i-containers` (8015).

**Phase 2.5 → Semaphore → 21-LLM ensemble synthesis.**
`allis-20llm-production` (8008) ✅ via `allis-semaphore` (8030,
`max_concurrent: 4`, `timeout=600.0`). 22 proxies (8201–8222); 21 active
(April 17, 2026). StarCoder2 excluded on 0-char responses. Wall-clock ~320–360s.

**Phase 3 — Judge Pipeline (compose-managed; ML-DSA-65 signing;
`judge_to_pituitary_bridge.py` active).**
Consensus answer only — never raw_responses. Rule-based: Truth (7230), Consistency
(7231), Alignment (7232), Ethics (7233). Coordinator: `allis-judge-pipeline` (7239).
Time: ~60–86s. All verdicts signed ML-DSA-65 FIPS 204 (sig=3309 bytes, verify=True).
`judge_to_pituitary_bridge.py` sends verdict back to `nbb_pituitary_gland` (8108) to
update mode and WOAH weights for subsequent requests.

**Phase 3.5 — LM Synthesizer + Voice Delivery (Phase 3.75 eliminated).**
The LM Synthesizer takes the judge pipeline's `final_answer` and calls
`allis-ollama:11434/api/generate` (via `OLLAMA_HOST=http://allis-ollama:11434`)
with `llama3.1:latest`. Persona prompt injected:

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

Phase 3.75 Final Polish is **permanently eliminated** — this single Ollama call is the
complete voice delivery step. Time saved: ~40 seconds per query.

**Phase 5 — GBIM temporal confidence decay + `allis-gbim-query-router` (port 7205).**
`confidence_decay` multiplier applied from `gbim_worldview_entities` (ChromaDB
`allis-chroma`, 5,416,521 vectors; L2; host 8002, inter-service
`http://allis-chroma:8000`). Entities with `needs_verification=TRUE` receive attenuated
confidence scores. **`allis-gbim-query-router` (127.0.0.1:7205)** routes structured
GBIM entity queries within this phase — confirmed April 23, 2026. This is the first
`allis-*` named service in the production stack; full routing topology to be documented
in a follow-on sprint.

**Phase 7 — 69-DGM cascade (host 19000 → internal 9000).**
23 connectors × 3 stages = 69 DGM operations.

**Phase 4.5 and governance — BBB output guard, judges, constitutional guardian.**
`apply_output_guards_async` (port 8016, `timeout=8.0s`).
`BBB_OUTPUT_BLOCKING=true` since April 6 — blocked outputs are hard-rejected.
`llm_judge_v3` validates output. Constitutional Guardian (8091) enforces principles
audit. `nbb_mother_carrie_protocols` (8107) applies warmth/tone modulation from
`nbb_pituitary_gland` warmth output.

**EEG rhythm integration.**
Delta (8073) watches gateway/chroma/PIA liveness (16 BBB events). Theta (8074)
consolidates ChromaDB memory every 60s. Beta (8075) runs autonomous learner every
5 minutes — currently studying WV economic development, Appalachian broadband, New
River Gorge infrastructure, MountainShares economics. EEG band states feed into Qualia
Engine emotional resonance weighting and `IntrospectiveRecord` fields (Chapter 13 §13.3).

**Post-processing — identity normalization.**
`normalize_identity()` produces Ms. Allis's identity voice. `TruthValidator` verifies
`correct_identity`, `correct_creator`, `relationship_clear`. Response logged to
`ms_allis_memory` ChromaDB collection (cosine; self-heals from 50 docs organically; see
Chapter 12 §12.3 note on consciousness bridge line 74) and `episodic_log`.

---

## 11.5 LLMs in Consciousness, Autonomy, and Ensembles

**Consciousness and identity.**
The Fifth DGM and I-container services use LLM calls (via WOAH) to decide which content
should shape Ms. Allis's evolving identity narrative. `normalize_identity()` runs as a
final post-processing step on all chat paths. The `nbb_pituitary_gland` (port 8108,
mode: `baseline`) modulates governance context that flows through WOAH into identity
decisions.

**Autonomous learning and EEG Beta.**
The autonomous learner (port 8425) writes processed knowledge into `autonomous_learner`
ChromaDB collection (`allis-chroma` host 8002, inter-service
`http://allis-chroma:8000`, v2 API, L2 distance) using `all-minilm:latest` 384-dim
embeddings. EEG Beta (8075) pulse #2 was studying WV economic development, Appalachian
broadband, New River Gorge infrastructure, MountainShares economics as of April 16. The
Phase 1.45 retrieval step means this growing corpus actively enriches every production
query. EEG Theta (8074) consolidates memory every 60s, snapshotting ChromaDB collection
state.

**Ensemble and judge patterns.**
21 active models (April 17, 2026) produce independent responses. Phase 5 GBIM temporal
decay weights attenuate confidence for aged GBIM entities — `allis-gbim-query-router`
(port 7205) routes structured entity queries within this phase. Phase 7 69-DGM cascade
provides post-ensemble validation. Judges evaluate consensus answer only — ML-DSA-65
FIPS 204 signed. `judge_to_pituitary_bridge.py` closes the feedback loop from judge
verdicts back to pituitary governance state.

---

## 11.6 Operational Constraints and Fabric Behavior

**Resource and disk constraints.**
GPU pipeline active: RTX 4070, 99–115s end-to-end (confirmed 102.58s April 23). CPU
436s baseline retired. Disk utilization: 661 GB used / 937 GB total (75%).

**Timeouts and free-flow thinking.**
All 22 LLM proxies: `read=None`. BBB output guard: `timeout=8.0s`. Semaphore:
`max_concurrent: 4`.

**Semaphore queuing behavior.**
Sequential Ollama model runs — back-to-back requests add ~320–360s each. Drain before
benchmarking.

**GBIM temporal decay.**
Phase 5 `confidence_decay` from ChromaDB `gbim_worldview_entities` (5,416,521 vectors).
`allis-gbim-query-router` (port 7205) routes entity queries in this phase. POC
verification loop (future work) will restore `confidence_decay` to 1.0 for
community-confirmed entities.

**BBB output blocking.**
`BBB_OUTPUT_BLOCKING=true` since April 6, 2026. Blocked outputs are hard-rejected (not
passed with warning). `llm_judge_v3` validation enforced on all outputs.

**Collection self-healing.**
`ms_allis_memory`: 50 docs (rebuilt April 16); self-heals organically via consciousness
bridge (line 74 of `msallisconsciousnessbridge.py`) on every session turn — will return
to 296+ naturally. `appalachian_cultural_intelligence`: 890 docs; threshold ≥563 — will
exceed on next ACI pipeline run.

**Failure modes and fallbacks.**
Judge services down → main brain falls back to ensemble answer, marks metrics degraded.
Any neuro pipeline stage failure → `{"status": "bypassed", "error": "…"}`, processing
continues. BBB non-200 → fail-open. Judge services reboot-safe (compose-managed,
`restart: unless-stopped`). `nbb_pituitary_gland` (8108) not reachable → pipeline
degrades gracefully to non-modulated governance defaults.

---

## 11.7 Implementation Notes and Persistence

- **LLM proxy timeouts.** All `llm{n}_health_proxy.py`: `read=None`, shorter
  connect/write/pool. Persist to source; survive container rebuilds.
- **20-LLM production server.** `ai_server_20llm_PRODUCTION.py` in
  `allis-20llm-production` container ✅: backlog 2048, keep-alive 600s. BakLLaVA
  disable guard must be preserved in all future versions.
- **Semaphore proxy.** Mandatory intermediary port 8030. Float `timeout: 600.0`.
  Permanent decision (2026-03-02).
- **BBB output guard timeout.** `apply_output_guards_async` must use
  `httpx.AsyncClient(timeout=8.0)`. `timeout=None` is a known regression risk.
  `BBB_OUTPUT_BLOCKING=true` must be preserved.
- **LM Synthesizer.** Port 8001. Calls `allis-ollama:11434/api/generate` via
  `OLLAMA_HOST=http://allis-ollama:11434` with `llama3.1:latest`. Persona prompt must
  be preserved in all rebuilds. Phase 3.75 is permanently eliminated.
- **Judge pipeline.** Consensus answer only — never raw_responses dump. All 5 judge
  containers in `docker-compose.yml` with
  `build: context: ./services, dockerfile: Dockerfile.judge` and
  `restart: unless-stopped`. `judge_to_pituitary_bridge.py` must be volume-mounted into
  `allis-judge-pipeline`. Ghost containers on `container_name:
  - **Judge pipeline.** Consensus answer only — never raw_responses dump. All 5 judge
  containers in `docker-compose.yml` with
  `build: context: ./services, dockerfile: Dockerfile.judge` and
  `restart: unless-stopped`. `judge_to_pituitary_bridge.py` must be volume-mounted into
  `allis-judge-pipeline`. Ghost containers on `container_name:` slot block volume mounts
  — clear orphans before recreating. ML-DSA-65 keys: back up
  `judge-keys/judge_sk.bin` (4032 bytes) to offline storage.
- **ChromaDB.** `allis-chroma` host port **8002**, container port **8000**,
  inter-service `http://allis-chroma:8000`. v2 API only — v1 deprecated (410 Gone).
  Required model: `all-minilm:latest` (384-dim). Per-collection counts: Python client
  `collection.count()` (UUID two-step pattern — not derivable from raw SQLite).
  **48 collections, ~6,740,611 vectors** (April 23, 2026). `ms_allis_memory`: 50 docs
  — self-heals via consciousness bridge line 74; **cosine** distance.
  `appalachian_cultural_intelligence`: 890 docs, threshold ≥563. Preflight thresholds
  use `-ge` not `-eq`.
- **Production DB.** `msallis-db` host port **5433** / container **5432**, bound to
  `127.0.0.1`, role `postgres`, `msallisgis` 16 GB / 294 tables / 11 schemas.
  GBIM entity store is **ChromaDB `gbim_worldview_entities`** (5,416,521 vectors),
  not a relational table.
- **Forensic DB.** `postgis-forensic` host port **5432**, role `allis`,
  `msallisgis` 17 GB / 314 tables / 9 schemas — forensic auditing only.
- **Community resources.** Port 5435, **64 verified resources, all 55 WV counties**
  (April 16 preflight).
- **Autonomous learner.** Port 8425. `autonomous_learner` collection, **21,181 records
  (April 23, 2026)**; L2; actively growing. EEG Beta (8075) drives 5-min learning
  cycles.
- **`allis-gbim-query-router`.** Port **7205**, bound to `127.0.0.1`. Routes structured
  GBIM entity queries in Phase 5 confidence decay topology. First `allis-*` named
  service in the stack — naming migration sprint will align remaining `allis-*` hostnames
  to `allis-*`. Full routing topology specification deferred to follow-on sprint. Must
  be included in all future `docker-compose.yml` definitions and preflight gate checks.
- **EEG stack.** `Dockerfile.eeg` single image for all three EEG services.
  `eeg_shared/pia_state.py` reads `ALLIS_PIA_STATUS_URL` from env. EEG blocks must be
  inserted before `networks:` key in `docker-compose.yml`. Preflight gate includes EEG
  health checks. Backups in `~/msallis-repair-backups/`.
- **`nbb_pituitary_gland`.** Port 8108, `127.0.0.1`, mode **`baseline`**. Authoritative
  routes: GET `/global_mode`, GET `/mode_history`. Full spec Chapter 15.
- **`nbb_mother_carrie_protocols`.** Port 8107. 5 protocols active,
  `MOTHER_CARRIE_KIDD` anchor.
- **Hippocampus.** Port 8011. Must be in all future compose definitions. Locked to
  `127.0.0.1`. Full spec Chapter 14.
- **69-DGM cascade.** Host port 19000 → internal 9000. Must be `127.0.0.1:19000`.
  Never expose as `0.0.0.0:9000`. Full spec Chapter 9.
- **Naming convention.** Legacy `allis-*` Docker Compose service names are authoritative
  for all container-to-container DNS resolution until a dedicated naming-migration sprint
  is completed. Do not rename service hostnames in `docker-compose.yml` without a full
  dependency audit. `allis-gbim-query-router` is the sole exception as of April 23,
  2026.
- **Preflight gates.** All 27 gates must be ✅ green before production traffic. Threshold
  operators: `-ge` not `-eq`. ChromaDB threshold: ≥48 collections. EEG health checks
  included. `appalachian_cultural_intelligence` threshold: ≥563.
- **Security.** Run
  `docker ps --format "{{.Names}}\t{{.Ports}}" | grep "0.0.0.0" | grep -v "127.0.0.1"`
  after every compose recreate — must return empty. `ALLIS_API_KEY` must be exported
  before starting `allis-memory` (8056). All judge keys stored at `judge-keys/`; offline
  backup of `judge_sk.bin` is mandatory.
