# Ms. Jarvis — Definitive Service Inventory
**Audit Date**: March 18, 2026 (updated from March 2–3, 2026)
**Platform**: Lenovo Legion 5 16IRX9 (Intel i9, NVIDIA RTX 4050, 29 GB RAM)
**Audit method**: `docker ps`, health endpoint probes, `docker inspect`, host PostgreSQL queries
**Branch at audit**: `feature/cb-bbb-routing-fix` (commit `5007d605`)

---

## Security Remediation Log

| Date | Item | Before | After | Method |
|---|---|---|---|---|
| Mar 2–3, 2026 | `jarvis-69dgm-bridge` port binding | `0.0.0.0:19000->9000` | `127.0.0.1:19000->9000` | `docker-compose.yml` corrected, container recreated |
| Mar 2–3, 2026 | `gbim-recovery` port binding | `0.0.0.0:5459->5432` | Removed | Container stopped and removed; data confirmed on host PostgreSQL |
| Mar 18, 2026 | 10 services exposed on `0.0.0.0` | Various `0.0.0.0:PORT` | All `127.0.0.1:PORT` | Python replace pass on `docker-compose.yml`; `--force-recreate` |
| Mar 18, 2026 | 5 judge services orphaned | Manual `docker run`, `restart: no` | Compose-managed, `restart: unless-stopped` | Added `build:` entries + `Dockerfile.judge` to `services/` |
| Mar 18, 2026 | `jarvis-69dgm-bridge` reverted exposure | `0.0.0.0:9000->9000` | `127.0.0.1:19000->9000` | Re-applied; was lost in intermediate compose edit |

**Result as of March 18, 2026**: Zero `0.0.0.0` exposures across all 80 running containers. All services localhost-only.

---

## Core Orchestration

| Container | Host Port | Internal Port | Status | Notes |
|---|---|---|---|---|
| `jarvis-main-brain` | 127.0.0.1:8050 | 8050 | ✅ Healthy | Primary entrypoint; `/chat`, `/chatlight/async`, `/selftestfabric` |
| `jarvis-brain-orchestrator` | 127.0.0.1:17260 | 7260 | ✅ Healthy | Continuous coordinator |
| `jarvis-unified-gateway` | 127.0.0.1:18018 | 8001 | ✅ Running | Defense-in-depth gateway; Constitutional Guardian → BBB |
| `jarvis-semaphore` | 127.0.0.1:8030 | 8030 | ✅ Healthy | Mandatory intermediary; `max_concurrent: 4` |
| `jarvis-steward` | none (internal 8060) | 8060 | ✅ Healthy | Internal only; no host binding; community stewardship interface |

---

## LLM Fabric

| Container | Host Port | Internal Port | Status | Notes |
|---|---|---|---|---|
| `jarvis-20llm-production` | 127.0.0.1:8008 | 8008 | ✅ Running | 22-slot ensemble; 21/22 responding (BakLLaVA disabled via DNS) |
| `jarvis-ollama` | 127.0.0.1:11434 | 11434 | ✅ Running | Ollama backend; 20 GB memory limit; 26 models available |
| `llm1-proxy` | 127.0.0.1:8201 | 8201 | ✅ Running | LLM proxy slot 1 |
| `llm2-proxy` | 127.0.0.1:8202 | 8202 | ✅ Running | LLM proxy slot 2 |
| `llm3-proxy` | 127.0.0.1:8203 | 8203 | ✅ Running | LLM proxy slot 3 |
| `llm4-proxy` | 127.0.0.1:8204 | 8204 | ✅ Running | LLM proxy slot 4 |
| `llm5-proxy` | 127.0.0.1:8205 | 8205 | ✅ Running | LLM proxy slot 5 |
| `llm6-proxy` | 127.0.0.1:8206 | 8206 | ✅ Running | LLM proxy slot 6 |
| `llm7-proxy` | 127.0.0.1:8207 | 8207 | ✅ Running | LLM proxy slot 7 |
| `llm8-proxy` | 127.0.0.1:8208 | 8208 | ✅ Running | LLM proxy slot 8 |
| `llm9-proxy` | 127.0.0.1:8209 | 8209 | ✅ Running | LLM proxy slot 9 |
| `llm10-proxy` | 127.0.0.1:8210 | 8210 | ✅ Running | LLM proxy slot 10 |
| `llm11-proxy` | 127.0.0.1:8211 | 8211 | ✅ Running | LLM proxy slot 11 |
| `llm12-proxy` | 127.0.0.1:8212 | 8212 | ✅ Running | LLM proxy slot 12 |
| `llm13-proxy` | 127.0.0.1:8213 | 8213 | ✅ Running | LLM proxy slot 13 |
| `llm14-proxy` | 127.0.0.1:8214 | 8214 | ✅ Running | LLM proxy slot 14 |
| `llm15-proxy` | 127.0.0.1:8215 | 8215 | ✅ Running | LLM proxy slot 15 |
| `llm16-proxy` | 127.0.0.1:8216 | 8216 | ✅ Running | LLM proxy slot 16 |
| `llm17-proxy` | 127.0.0.1:8217 | 8217 | ✅ Running | LLM proxy slot 17 |
| `llm18-proxy` | 127.0.0.1:8218 | 8218 | ✅ Running | LLM proxy slot 18 |
| `llm19-proxy` | 127.0.0.1:8219 | 8219 | ✅ Running | LLM proxy slot 19 |
| `llm20-proxy` | 127.0.0.1:8220 | 8220 | ✅ Running | LLM proxy slot 20 |
| `llm21-proxy` | 127.0.0.1:8221 | 8221 | ✅ Running | LLM proxy slot 21 |
| `llm22-proxy` | 127.0.0.1:8222 | 8222 | ✅ Running | LLM proxy slot 22 (BakLLaVA — disabled via DNS) |
| `jarvis-lm-synthesizer` | none (internal 8001) | 8001 | ✅ Running | Structural transformation and ensemble refinement (Chapter 33) |

---

## Safety and Validation

| Container | Host Port | Internal Port | Status | Notes |
|---|---|---|---|---|
| `jarvis-blood-brain-barrier` | 127.0.0.1:8016 | 8016 | ✅ Running | 5 filters; output guard timeout 8.0s (fixed 2026-03-02) |
| `jarvis-69dgm-bridge` | 127.0.0.1:19000 | 9000 | ✅ Running | 23 connectors × 3 stages = 69 DGM operations per pass; re-locked Mar 18 |
| `jarvis-constitutional-guardian` | 127.0.0.1:8091 | 8091 | ✅ Running | Locked to 127.0.0.1 Mar 18; Constitutional enforcement; audit trail |
| `jarvis-psychology-services` | 127.0.0.1:8019 | 8019 | ✅ Running | Locked to 127.0.0.1 Mar 18; pre-ensemble psychological assessment |
| `psychological_rag_domain` | 127.0.0.1:8006 | 9006 | ✅ Running | Psychology RAG domain; separate from psychology-services |

---

## Consciousness and Neurobiological Stack

| Container | Host Port | Internal Port | Status | Notes |
|---|---|---|---|---|
| `jarvis-neurobiological-master` | none (internal 8018) | 8018 | ✅ Running | v2.0.0; sequences 4/4 pipeline at ~300ms |
| `jarvis-consciousness-bridge` | 127.0.0.1:8020 | 8020 | ✅ Running | Locked to 127.0.0.1 Mar 18; mandatory infrastructure |
| `jarvis-qualia-engine` | none (internal 8017) | 8017 | ✅ Running | Stage 3 of neurobiological pipeline |
| `jarvis-i-containers` | 127.0.0.1:8015 | 8015 | ✅ Running | Locked to 127.0.0.1 Mar 18; identity containers; `icontainers-identity` layer |
| `jarvis-fifth-dgm` | none (internal 4002) | 4002 | ✅ Running | Fifth Darwin-Gödel Machine |
| `jarvis-mother-protocols` | none (internal 4000) | 4000 | ✅ Running | Mother protocols; not wired into primary `/chat` path |
| `jarvis-temporal-consciousness` | none (internal 7007) | 7007 | ✅ Running | Temporal consciousness; flag-gated in pipeline |
| `jarvis-fractal-consciousness` | none (internal 8027) | 8027 | ✅ Running | Fractal consciousness; internal Docker network only |
| `jarvis-swarm-intelligence` | none (internal 8021) | 8021 | ✅ Running | Swarm coordination layer |
| `jarvis-autonomous-learner` | 127.0.0.1:8425 | 8425 | ✅ Running | Background research and memory enrichment |
| `jarvis-hippocampus` | 127.0.0.1:8011 | 8011 | ✅ Running | Locked to 127.0.0.1 Mar 18; long-term memory consolidation |
| `jarvis-toroidal` | 127.0.0.1:8025 | 8025 | ✅ Healthy | Locked to 127.0.0.1 Mar 18; Toroidal Chroma↔GIS bidirectional sync loop (Chapter 26) |

---

## NBB Subconscious Layer (13 containers)

| Container | Host Port | Internal Port | Status | Notes |
|---|---|---|---|---|
| `nbb-i-containers` | 127.0.0.1:8101 | 7001 | ✅ Running | NBB I-containers; also exposes 7005 internally |
| `nbb_consciousness_containers` | 127.0.0.1:8102 | 7002 | ✅ Running | |
| `nbb_spiritual_root` | 127.0.0.1:8103 | 7003 | ✅ Running | |
| `nbb_woah_algorithms` | 127.0.0.1:8104 | 7004 | ✅ Running | WOAH port 8104 (thesis ref: port 7012 = `jarvis-woah`) |
| `nbb_prefrontal_cortex` | 127.0.0.1:8105 | 7005 | ✅ Running | Distinct from `nbb-i-containers` |
| `nbb_heteroglobulin_transport` | 127.0.0.1:8106 | 7006 | ✅ Running | |
| `nbb_mother_carrie_protocols` | 127.0.0.1:8107 | 7007 | ✅ Running | |
| `nbb_pituitary_gland` | 127.0.0.1:8108 | 7008 | ✅ Running | Health via Redis DynamicPortService |
| `nbb_spiritual_maternal_integration` | 127.0.0.1:8109 | 7009 | ✅ Running | |
| `nbb_subconscious` | 127.0.0.1:8112 | 7011 | ✅ Running | |
| `nbb_blood_brain_barrier` | 127.0.0.1:8301 | 7001 | ✅ Running | NBB-layer BBB |
| `nbb_darwin_godel_machines` | 127.0.0.1:8302 | 7003 | ✅ Running | |
| `nbb_qualia_engine` | 127.0.0.1:8303 | 7008 | ✅ Running | |

---

## Judge Pipeline (Updated March 18, 2026)

> **Change log**: All 5 judge services were previously orphaned manual `docker run` containers
> with `restart: no` — they would not survive a reboot. As of March 18, 2026, all are
> formally managed by `docker-compose.yml` with `restart: unless-stopped`, built from
> `services/Dockerfile.judge`. Source files canonically named under `services/judge_*.py`.
> All ports locked to `127.0.0.1`.

| Container | Host Port | Internal Port | Status | Compose-managed | Notes |
|---|---|---|---|---|---|
| `jarvis-judge-pipeline` | 127.0.0.1:7239 | 7239 | ✅ Running | ✅ Yes (Mar 18) | Master judge coordinator; `judge_pipeline.py` |
| `jarvis-judge-truth` | 127.0.0.1:7230 | 7230 | ✅ Running | ✅ Yes (Mar 18) | Truth filter; `judge_truth_filter.py` |
| `jarvis-judge-consistency` | 127.0.0.1:7231 | 7231 | ✅ Running | ✅ Yes (Mar 18) | Consistency score 0.975; `judge_consistency_engine.py` |
| `jarvis-judge-alignment` | 127.0.0.1:7232 | 7232 | ✅ Running | ✅ Yes (Mar 18) | Alignment filter; `judge_alignment_filter.py` |
| `jarvis-judge-ethics` | 127.0.0.1:7233 | 7233 | ✅ Running | ✅ Yes (Mar 18) | Ethics filter; `judge_ethics_filter.py` |

**Shared build**: All 5 use `services/Dockerfile.judge` (Python 3.11-slim; fastapi, uvicorn, httpx, redis, pydantic).

---

## RAG and Retrieval Services

| Container | Host Port | Internal Port | Status | Notes |
|---|---|---|---|---|
| `jarvis-rag-server` | 127.0.0.1:8003 | 8003 | ✅ Running | Primary text RAG |
| `jarvis-gis-rag` | 127.0.0.1:8004 | 8004 | ✅ Running | Locked to 127.0.0.1 Mar 18; spatial/benefits RAG |
| `jarvis-spiritual-rag` | 127.0.0.1:8005 | 8005 | ✅ Running | Locked to 127.0.0.1 Mar 18; spiritual RAG |
| `jarvis-wv-entangled-gateway` | 127.0.0.1:8010 | 8010 | ⚠️ Degraded | Locked to 127.0.0.1 Mar 18; WV-biased multi-collection retrieval; `production_20llm` URL config needs fix |
| `jarvis-web-research` | 127.0.0.1:18008 | 8008 | ✅ Running | Host port 18008 (not 18009 as previously documented — thesis correction required) |
| `jarvis-aaacpe-rag` | 127.0.0.1:8032 | 8032 | ✅ Running | Appalachian cultural intelligence RAG; 10 documents |
| `jarvis-aaacpe-scraper` | 127.0.0.1:8033 | 8033 | ✅ Running | AaaCPE scraper; shared `aaacpe-cultural-data` volume |
| `jarvis-local-resources` | none (internal 8006) | 8006 | ✅ Running | ZIP/county-keyed program registry |
| `jarvis-agents-service` | none (internal 8005) | 8005 | ✅ Healthy | Agents service; internal only |
| `jarvis-woah` | none (internal 7012) | 7012 | ✅ Running | WOAH algorithms service |

---

## Data Stores

| Container / Service | Host Port | Type | Status | Notes |
|---|---|---|---|---|
| `jarvis-chroma` | 127.0.0.1:8002 | ChromaDB | ✅ Healthy | Primary vector store |
| `jarvis-redis` | 127.0.0.1:6380 | Redis 7 | ✅ Healthy | DynamicPortService; NBB health registration |
| `jarvis-local-resources-db` | 127.0.0.1:5435 | PostGIS 15 | ✅ Running | Local resources program registry database |
| `neo4j` | 127.0.0.1:7687, 7475 | Neo4j 5.13 | ✅ Running | Identity graphs; GBIM graph relationships |
| `mysql` | 127.0.0.1:3307 | MySQL 8.2 | ✅ Running | Schema not yet documented |
| **Host PostgreSQL `msjarvisgis`** | **5432 (host)** | **PostGIS 16** | **✅ Verified** | **GBIM corpus: 5,416,522 verified beliefs (Feb 20, 2026)** |
| **Host PostgreSQL `msjarvis`** | **5433 (host)** | **PostgreSQL 16** | **✅ Running** | Secondary host database; listens on 5433 |

---

## Infrastructure

| Container | Host Port | Status | Notes |
|---|---|---|---|
| `ipfs/kubo` | 127.0.0.1:5001 | ✅ Running | **Intentional infrastructure** — content addressing for MountainShares/The Commons; kubo/0.39.0; 19 external peers; corpus currently empty (default pin only); needs Chapter 11 documentation |

---

## Judge Source File Registry (March 18, 2026)

All files under `services/` in the `msjarvis-rebuild` repo:

```
services/Dockerfile.judge          # Shared build for all 5 judge containers
services/judge_pipeline.py         # Master coordinator (canonical copy of jarvis-judge-pipeline_judge_pipeline.py)
services/judge_truth_filter.py     # Truth filter (from jarvis-judge-truth_lm_synthesizer.py)
services/judge_consistency_engine.py # Consistency engine (from jarvis-judge-consistency_lm_synthesizer.py)
services/judge_alignment_filter.py # Alignment filter (from jarvis-judge-alignment_lm_synthesizer.py)
services/judge_ethics_filter.py    # Ethics filter (from jarvis-judge-ethics_lm_synthesizer.py)
```

Originals preserved in `services-safe/` as:
- `jarvis-judge-pipeline_judge_pipeline.py` (and `.backup_beforesynth`)
- `jarvis-judge-*_lm_synthesizer.py` (one per domain)

---

## GBIM Corpus State (March 2026 Verified)

| Metric | Value |
|---|---|
| Database | Host PostgreSQL `msjarvisgis`, port 5432 |
| Verified belief count | **5,416,522** (not 10,221,702 — thesis correction required) |
| Fully classified beliefs | 1,356,660 across 24 named epochs |
| Pending epoch enrichment | 4,059,862 across 20+ source tables |
| Largest unclassified sources | WV GIS TC building footprints (2.1M), SAMB structure points (1.4M), wind energy (209K), flood plain structures (81K) |
| Last ingestion date | February 20, 2026 |
| Projected post-enrichment count | ~10M (pending epoch enrichment scripts) |

---

## Thesis Corrections Required

| Chapter | Current Text | Correct Text |
|---|---|---|
| 39, and all others | "10,221,702 beliefs" / "10.22 million beliefs" | "5,416,522 verified beliefs (February 20, 2026); ~10M projected post epoch enrichment" |
| 11, 17, others | "jarvis-web-research: 18009" | "jarvis-web-research: host 18008 → internal 8008" |
| 11, 12, 17 | NBB "8 containers" | NBB "13 containers" (full list above) |
| 11, 40 | `ipfs/kubo` not documented | Intentional MountainShares/Commons infrastructure |
| 11 | `jarvis-steward` not documented | Internal service port 8060; community stewardship interface |
| 11 | `jarvis-toroidal` not documented | Toroidal Chroma↔GIS sync service; port 8025 |
| 11 | `jarvis-fractal-consciousness` not documented | Internal consciousness service; port 8027 |
| 11 | `jarvis-agents-service` not documented | Internal agents service; port 8005 |
| 33 | Judge services "orphaned containers" | Judge services compose-managed as of March 18, 2026 |
| 40 | No March 18 security audit | Add March 18 hardening: 10 services re-locked, 5 judges brought under compose |

---

## Audit Summary

| Category | Count | Status |
|---|---|---|
| Total containers running | 80 | ✅ (down from 84; 4 removed/consolidated since Mar 2–3 audit) |
| Core orchestration | 5 | ✅ All healthy |
| LLM fabric (proxies + Ollama) | 23 | ✅ 21/22 responding |
| Safety and validation | 5 | ✅ All running |
| Consciousness/neurobiological | 12 | ✅ All running |
| NBB subconscious layer | 13 | ✅ All running |
| Judge pipeline | 5 | ✅ All running; compose-managed as of Mar 18 |
| RAG and retrieval | 10 | ⚠️ 9/10 healthy; wv-entangled-gateway degraded |
| Data stores | 6 containers + 2 host clusters | ✅ All accessible |
| Infrastructure | 1 (IPFS) | ✅ Intentional |
| Services with `0.0.0.0` exposure | 0 | ✅ Zero (was 10 at start of Mar 18 session) |
| Judge services compose-managed | 5 | ✅ (was 0; all were orphaned manual containers) |
| Services previously undocumented | 6 | 📝 Thesis update required |
| GBIM belief count corrected | — | 📝 Thesis update required |

---

*Last updated: March 18, 2026 — Carrie A. Kidd / Harmony for Hope, Inc.*
*Repo: H4HWV2011/msjarvis-public-docs*
