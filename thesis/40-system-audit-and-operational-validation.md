# 40. System Audit

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

## Why This Matters for Polymathmatic Geography

Chapter 40 is the living audit record for Ms. Jarvis. It preserves each formal validation snapshot as an immutable section rather than overwriting history, so that the evolution from 8 operational services (December 2025) to 80 fully compose-managed, localhost-only containers (March 20, 2026) is traceable and citable. This chapter supports:

- **P16 – Power accountable to place** by creating an auditable record of every service state change, security remediation, and architectural fix, so that Appalachian communities and their partners can verify the system was built and corrected with transparency.
- **P3 – Power has a geometry** by exposing the port topology, binding changes, and service wiring decisions that define what the system can and cannot do at each point in time.
- **P5 – Design is a geographic act** by treating each audit entry as a design decision log — recording not just what was fixed, but why, what it was before, and what permanent architectural constraints it established.

This chapter consolidates five formal audit records:

- **Section 40-A** — Initial Operational Validation (December 11, 2025): first end-to-end ULTIMATE coordination baseline, 8/23 services operational.
- **Section 40-B** — Remediation Audit (March 13, 2026): ultimatechat path brought to full operational status, 6 confirmed consciousness layers.
- **Section 40-C** — Security Hardening Audit (March 18, 2026): zero 0.0.0.0 exposures, all 5 judge services compose-managed, 80 containers fully managed, ~436s end-to-end benchmark.
- **Appendix 40-D** — Definitive Service Inventory (March 18, 2026): authoritative per-service table drawn from live `docker ps` and health endpoint probes.
- **Section 40-E** — GBIM Landowner Layer Audit (March 20, 2026): `gbim_query_router` (port 7205) promoted to compose, `mvw_gbim_landowner_spatial` materialized and indexed, 20,593 landowner beliefs ingested.

---

## 40-A. Initial Operational Validation (December 11, 2025)

Session date: December 11, 2025, 5:00–6:00 PM EST
Purpose: Comprehensive snapshot of system state after the first ULTIMATE-style operational validation run, before later RAG/Chroma and service-mesh improvements.

### Section 1: Executive Summary

**What Was Tested**

- End-to-end ULTIMATE coordination path: BBB → web_research → llm_bridge → response aggregation on a single-node localhost deployment.
- Two full AGI-style reasoning tasks (architecture explanation and deployment planning), with two additional tasks scheduled but not executed in this session.
- Service health across 23 containers, including brain, safety, research, LLM bridge, and core data stores.

**Key Findings**

- The ULTIMATE coordination path successfully produced long, coherent, high-quality answers for complex tasks, with 0% observed error in the two completed cases.
- Latency is dominated by the llm_bridge (22-agent synthesis), which accounts for roughly 60–70% of end-to-end response time.
- Only 8 of 23 services were operational in this snapshot; many neuro/qualia and advanced coordination services did not respond to health checks.
- The safety layer (BBB) approved and filtered all tested prompts, but no adversarial tests were run.

**Critical Issues**

- Health-check amplification (per-request sweep to all services) causes significant overhead and can trigger resource exhaustion under sustained load.
- A large portion of the service mesh was non-operational with unclear status.
- Data-plane usage (Chroma, Neo4j, MySQL) was only partially observed; some components were clearly up but not fully exercised.
- No quantitative quality metrics or adversarial security evaluations were performed.

**Recommendations**

- Implement cached health checks (TTL-based) to avoid repeated full sweeps on every request.
- Systematically diagnose and document non-operational services.
- Clarify and document the active Chroma instance, collection topology, and RAG retrieval paths.
- Build structured evaluation and red-team test suites before any broader production use.

> **Retrospective note (March 20, 2026):** The non-operational services listed in this December 2025 snapshot have since been brought online. The March 20, 2026 production stack runs 80 confirmed containers — all fully compose-managed via Docker Compose v5.1.0 (upgraded from v1.29.2, March 17, 2026) using `image:` references only (all `build:` directives converted March 17). All services are bound exclusively to 127.0.0.1; zero 0.0.0.0 exposures. The ChromaDB topology ambiguity (three instances) was resolved — canonical instance is `jarvis-chroma` at port 8000 with `chroma_data` Docker volume; all collections use 384-dimensional vectors (`all-minilm:latest`). PostgreSQL replaced Neo4j and MySQL as the canonical structured data store. Hash-prefixed container names resolved March 17–18. `gbim_query_router` (port 7205) added March 20, 2026 as the 80th container. See Section 40-C, Section 40-E, and Chapter 17 for current operational state.

---

### Section 2: Test Methodology

- Test harness: pytest + FastAPI TestClient, supplemented with curl-based smoke tests against live services.
- AGI exam scenarios: 4 comprehensive reasoning tasks targeting architecture reasoning, strategic planning, research synthesis, and meta-analysis.
- Test environment: Localhost, single-node deployment on the Legion host running all containers and supporting services.
- Test duration: 1 hour (December 11, 2025, 5:00–6:00 PM EST).
- Constraints: Sequential requests only (no concurrency); each AGI task executed as a single, heavy request through the full ULTIMATE pipeline.

---

### Section 3: Service Inventory and Health Status (December 2025 Snapshot)

**Operational (8/23)**

- `jarvis-main-brain` (8051 → 8050)
- `jarvis-blood-brain-barrier` (8016)
- `jarvis-llm-bridge` (18006 → 8006)
- `jarvis-web-research` (18009 → 8009)
- `jarvis-chroma` (8002 → 8000)
- `services-chroma-1` (8010)
- `services-neo4j-1` (7474, 7687)
- `services-mysql-1` (3307)

**Non-operational (15/23)**

- `qualia-engine`
- `swarm-intelligence`
- `consciousness-bridge`
- `unified-gateway`
- `autonomous-learner`
- `neurobiological-master`
- `i-containers`
- `fifth-dgm`
- 7 additional services not identified in this snapshot (no successful health responses)

> **Retrospective note (March 20, 2026):** The non-operational services listed above have been progressively resolved. See Appendix 40-D for the full March 18, 2026 service inventory and Section 40-E for the March 20, 2026 additions. Neo4j and MySQL have been superseded by the three-database PostgreSQL architecture: `msjarvis` (port 5433, 5,416,521 GBIM entities, 80 epochs, 206 source layers), `gisdb` (port 5433, PostGIS, 13 GB, 39 tables), and `jarvis-local-resources-db` (port 5435). `jarvis-llm-bridge` on port 8006 has been superseded by `jarvis-20llm-production` on port 8008 and `psychological_rag_domain` on port 8006.

---

### Section 4: ULTIMATE Coordination Path Validation

**Test Case 1: agi-arch-1 (Architecture Reasoning)**

- Prompt: "Explain Ms. Jarvis architecture"
- Processing time: 195 seconds (end-to-end)
- Services used: BBB, jarvis-web-research, jarvis-llm-bridge, response aggregation in main-brain
- Response length: ~2,847 tokens (multi-paragraph, multi-section explanation)
- Output quality: Rated "excellent"; accurately described the 22-agent ensemble, service coordination, and architecture layers
- Error rate: 0% observed factual or structural errors in this scenario

**Test Case 2: agi-plan-1 (Strategic Planning)**

- Prompt: "Develop production deployment strategy for Ms. Jarvis"
- Processing time: 353 seconds (end-to-end)
- Services used: BBB, jarvis-web-research, jarvis-llm-bridge, response aggregation
- Response length: ~4,102 tokens (comprehensive deployment and risk-mitigation plan)
- Output quality: Rated "excellent"; produced a multi-phase deployment plan with risk mitigation and timeline
- Error rate: 0% observed in the aspects evaluated during this session

**Test Case 3: agi-research-1 (Research Synthesis)**

- Status: Defined but not executed during this one-hour window

**Test Case 4: agi-meta-1 (Meta-Analysis)**

- Status: Defined but not executed during this one-hour window

---

### Section 5: Performance Characteristics

**Request Latency Breakdown — agi-arch-1 (195 seconds total)**

```
Component                   Duration    %        Bottleneck?
Health check sweep          4s          2.1%     No (≈3s avoidable with caching)
BBB processing              1s          0.5%     No
web_research processing     60s         30.8%    Moderate
llm_bridge processing       120s        61.5%    YES — primary bottleneck
Response aggregation        10s         5.1%     No
```

**Request Latency Breakdown — agi-plan-1 (353 seconds total)**

```
Component                   Duration    %
Health check sweep          5s          1.4%
BBB processing              1s          0.3%
web_research processing     90s         25.5%
llm_bridge processing       250s        70.8%
Response aggregation        7s          2.0%
```

> **Retrospective note (March 20, 2026):** The March 20, 2026 production 9-phase pipeline benchmark is ~436 seconds end-to-end (optimized from a 532s pre-optimization baseline), comparable to the agi-plan-1 result above despite now passing through substantially more services: 80 containers, BBB 7-filter stack (Phase 1.4), Phase 1.45 community memory retrieval (21,181+ autonomous_learner records), Phase 3 psychology pre-assessment, 21-model ensemble via semaphore proxy (~320–360s), judge pipeline consensus-only (~60–86s), merged Phase 3.5 LM Synthesizer + Voice Delivery (~30–55s), Phase 5 GBIM temporal decay, Phase 7 69-DGM cascade. The health-check amplification issue was resolved by the 30s TTL-cache implementation (March 18, 2026): Phase 1 health-check cost is ~0.7s after the first query. `gbim_query_router` landowner queries resolve in milliseconds and do not traverse the LLM ensemble.

---

### Section 6: System Stability Analysis

**Crash/Restart Events**

- Event 1: No crashes observed during test cases 1–2.
- Event 2: Service restart when test case 3 was initiated under heavy, back-to-back ULTIMATE requests. Cause: Full-service health sweeps on every request, combined with long-running ULTIMATE tasks, led to resource exhaustion (Uvicorn). Recovery: Automatic restart within ~10 seconds; no data loss observed, but user-visible interruption is likely under real traffic.

**Memory/CPU Usage**

- Not measured in this session; no dedicated monitoring (Prometheus/Grafana) was deployed.

---

### Section 7: Safety and Security Validation

**Blood-Brain Barrier (BBB) Performance**

```
Test                Result    Evidence
Content filtering   ✅ 100%   All examined requests passed through BBB and were filtered
Request approval    ✅ 100%   All tested requests approved; no rejections triggered
Log consistency     ✅ 100%   Logs showed consistent "approved and filtered" operations
```

**Safety Testing Status**

- ❌ No adversarial or prompt-injection testing conducted in this session
- ❌ No jailbreak-style prompts or red-team attacks simulated
- ❌ No tests explicitly designed to trick or subvert BBB or downstream models

> **Retrospective note (March 20, 2026):** The BBB expanded from 4 active filters (December 2025: EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection) to a 7-filter stack as of March 15, 2026 (adding SteganographyDetection, TruthVerification, ContextAwareness). SafetyMonitor word-boundary regex was corrected March 15 to eliminate false-positives on community resource terms. A `truth_score` null guard and fail-open behavior on HTTP 500 were added to both the BBB input filter and output guard on March 18, 2026. BBB is now bound to `127.0.0.1:8016` (was `0.0.0.0:8016` — re-locked March 18). The red-team adversarial test suite remains an open item.

---

### Section 8: Data Architecture Validation

**ChromaDB Instance Topology (December 2025 State)**

- Instances found: `jarvis-chroma`, `services-chroma-1`, `msjarvis-rebuild-chroma-1`
- Primary instance: Unclear at the time of this audit

> **Resolution (March 20, 2026):** The canonical ChromaDB instance is `jarvis-chroma` at `127.0.0.1:8000` with `chroma_data` Docker volume. All collections use 384-dimensional vectors (`all-minilm:latest`) — `nomic-embed-text` (768-dim) is incompatible. Active collections as of March 20, 2026: `gbim_worldview_entities` (5,416,521), `autonomous_learner` (21,181+, growing ~288/day; queried at Phase 1.45 on every `/chat` call), `psychological_rag` (968), `spiritual_texts` (23), `appalachian_cultural_intelligence` (5), `GBIM_sample_rows` (5,000), `GBIM_sample` (3), `msjarvis-smoke` (1). **LANDOWNER BELIEFS ARE NOT IN CHROMADB.** They are served exclusively by `gbim_query_router` (port 7205) via `mvw_gbim_landowner_spatial` in `msjarvisgis`. See Section 40-E.

**Neo4j and MySQL (December 2025 State)**

> **Resolution (March 20, 2026):** Neo4j and MySQL have been superseded by the three-database PostgreSQL architecture. `msjarvis` (port 5433, 5,416,521 GBIM entities, 80 epochs, 206 source layers, temporal decay metadata), `msjarvisgis` (port 5432, PostGIS, 91 GB, 501 tables, 5,416,522 rows in `gbimbeliefnormalized` including 20,593 landowner beliefs, `mvw_gbim_landowner_spatial` materialized and indexed), and `jarvis-local-resources-db` (port 5435, community resources, 7,354,707 rows in `building_parcel_county_tax_mv`). `services-neo4j-1` and `services-mysql-1` are not part of the current production stack.

---

### Section 9: Critical Issues and Recommendations

| Issue | Priority | Status (March 20, 2026) |
|---|---|---|
| Health-check amplification (full sweep per request) | HIGH | ✅ Fixed — 30s TTL cache, 2s per-service timeout (March 18) |
| Non-operational services (15/23) | MEDIUM | ✅ Resolved — 80 containers confirmed operational (March 20) |
| Red-team adversarial test suite | HIGH | 🔴 OPEN — highest priority remaining security gap |
| Missing quantitative quality metrics | MEDIUM | ⏳ Partial — Phase 5 confidence_decay provides temporal confidence |
| ChromaDB instance ambiguity | HIGH | ✅ Fixed — canonical instance `jarvis-chroma:8000` with `chroma_data` volume |
| `build:` directives causing unpredictable startup | MEDIUM | ✅ Fixed — all converted to `image:` references (March 17) |
| Docker Compose v1.29.2 crash bug | HIGH | ✅ Fixed — upgraded to v5.1.0 (March 17) |
| Hash-prefixed container names | MEDIUM | ✅ Fixed — `container_name:` added to all affected containers |

---

## 40-B. Remediation Audit Entry — 2026-03-13

Session date: 2026-03-13 (late night EDT)
Auditor: Carrie Kidd (Mamma Kidd), Harmony for Hope, Inc.
Purpose: Document all fixes applied and confirmed during the 2026-03-13 session that brought the ultimatechat execution path to full operational status.

### Summary

This session resolved a set of inter-related issues in `jarvis-main-brain` (port 8050) that had caused `validated_by` to always be `None`, `architecture_layers` to always be `0`, and the Blood-Brain Barrier sub-filter methods to be defined but not wired into the `/filter` request handler. By end of session, all 6 consciousness layers were confirmed active, BBB `/filter` and `/truth` returned HTTP 200, and the I-Containers `call_icontainers` stub had been replaced with a live HTTP implementation.

### Fixes Applied and Confirmed (2026-03-13)

| # | Component | Problem | Fix Applied | Confirmed |
|---|---|---|---|---|
| 1 | BBB /filter | EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection defined but not called inside handler | Wired all four filter methods into the /filter handler | ✅ HTTP 200, structured JSON |
| 2 | BBB /truth | Endpoint not implemented | Added POST /truth returning {valid, confidence, principal_reasons} | ✅ HTTP 200, schema confirmed |
| 3 | UltimateResponse.truth_verdict | Not populated from BBB output | Wired call_truth_filter() → BBB /truth → truth_verdict | ✅ Confirmed populated |
| 4 | clean_response_for_display() | Only stripped inline disclaimers; paragraph-level model self-identification passed through | Expanded to strip full paragraphs opening with "As LLaMA", "As Mistral", "As an AI", etc. | ✅ Identity voice clean |
| 5 | call_icontainers() | Empty stub returning {} — service never called | Replaced with live httpx POST to jarvis-i-containers:8015/process | ✅ icontainers-identity layer active |
| 6 | consciousness_layers assembly | icontainers-identity and nbb-icontainers never appended | Added both layers to the list after their HTTP calls | ✅ 6 layers confirmed |
| 7 | validated_by field | Always returned None (hardcoded) | Derive from names of all active layers at assembly time | ✅ Returns comma-separated layer names |
| 8 | architecture_layers field | Always returned 0 (hardcoded) | Return len(consciousness_layers) | ✅ Returns 6 |
| 9 | normalize_identity() | Some model names slipped through in paragraph context | Confirmed firing correctly; clean_response_for_display() handles paragraph-level | ✅ Confirmed |
| 10 | call_nbb_icontainers() | Dead duplicate code below a return statement | Identified for cleanup | ⏳ Cosmetic; no functional impact |

> **Subsequent expansions (March 20, 2026):** BBB expanded from 4 to 7 filters (March 15). SafetyMonitor regex corrected (March 15). `truth_score` null guard and fail-open on HTTP 500 added (March 18). Phase 1.45 community memory retrieval added (March 17). Phase 3.5 + 3.75 merged into single Ollama call (March 18). Judge pipeline updated to consensus-only (March 16). All 80 containers fully compose-managed (March 17–18). Security hardening: zero 0.0.0.0 exposures, all 5 judge services compose-managed (March 18). `gbim_query_router` (port 7205) added to compose (March 20). End-to-end benchmark: ~436s.

### Confirmed Live Output (Post-Remediation, 2026-03-13)

```json
{
  "validated_by": "nbb-prefrontal-cortex, qualia-engine, consciousness-bridge, neurobiological-master, icontainers-identity, nbb-icontainers",
  "architecture_layers": 6,
  "consciousness_layers": [
    {"name": "nbb-prefrontal-cortex",  "status": "active"},
    {"name": "qualia-engine",          "status": "ok"},
    {"name": "consciousness-bridge",   "status": "ok"},
    {"name": "neurobiological-master", "status": "ok"},
    {"name": "icontainers-identity",   "status": "active"},
    {"name": "nbb-icontainers",        "status": "active"}
  ],
  "truth_verdict": {
    "valid": true,
    "confidence": 0.95,
    "principal_reasons": []
  }
}
```

> **Note:** The above is the confirmed state as of 2026-03-13. The March 20, 2026 production `UltimateResponse` schema includes additional consciousness layer contributions from Phase 1.45 community memory, psychology pre-assessment (Phase 3), GBIM temporal decay (Phase 5), and 69-DGM cascade (Phase 7). See Chapter 17 for the current canonical schema.

### Confirmed Smoke Tests (Canonical as of 2026-03-13)

```bash
# BBB /filter
curl -sS -X POST http://localhost:8016/filter \
  -H "Content-Type: application/json" \
  -d '{"content": "Who are you?"}' | jq .

# BBB /truth
curl -sS -X POST http://localhost:8016/truth \
  -H "Content-Type: application/json" \
  -d '{"content": "Who are you?"}' | jq '{valid, confidence, principal_reasons}'

# Full ultimatechat (consciousness layers + validated_by)
curl -sS -X POST http://localhost:8050/ultimatechat \
  -H "Content-Type: application/json" \
  -d '{"message": "Who are you?", "user_id": "audit-2026-03-13"}' \
  | jq '{validated_by, architecture_layers, consciousness_layers, truth_verdict}'
```

> **Note:** For the full current smoke test suite including all March 15–20 services, see Chapter 41.

### Known Issues and Resolution Status (updated to March 20, 2026)

| Issue | Priority | Status |
|---|---|---|
| Dead code below return in call_nbb_icontainers() | Low | ⏳ Cosmetic; no functional impact |
| store_in_subconscious_rag to real ChromaDB collections | Medium | ✅ Resolved — chroma_data volume restored March 15; ms_jarvis_memory writes confirmed |
| Judge pipeline integration | Medium | ✅ Resolved — ports corrected 7230–7233 (March 16); consensus-only mode deployed; all 5 services compose-managed (March 18) |
| Red-team adversarial test suite | High | 🔴 OPEN — highest priority remaining security gap |
| Response truncation (max_tokens: 500) | High | ✅ Fixed — max_tokens: -1 (unlimited); llm22-proxy 8,192-token limit confirmed |
| ChromaDB _DummyCollection blocking retrieval | High | ✅ Fixed — all-minilm:latest 384-dim deployed March 17 |
| Redis response in-memory only (lost on restart) | High | ✅ Fixed — Redis-backed job system, 30-min TTL (March 17) |
| 33 services not in docker-compose.yml | High | ✅ Fixed — all 80 containers compose-managed (March 17–20) |
| build: directives causing slow startup | Medium | ✅ Fixed — all converted to image: references (March 17) |
| Docker Compose v1.29.2 crash bug | High | ✅ Fixed — upgraded to v5.1.0 (March 17) |
| Hash-prefixed container names | Medium | ✅ Fixed — container_name: added to all 8 affected containers |
| Judge pipeline URL wrong (all on port 7239) | High | ✅ Fixed — corrected to 7230/7231/7232/7233 (March 16) |
| LM Synthesizer calling jarvis-roche-llm (HTTP 500) | High | ✅ Fixed — now calls jarvis-ollama:11434/api/generate directly (March 18) |
| BBB truth_score KeyError crash | High | ✅ Fixed — null guard added (March 18) |
| BBB blocking pipeline on HTTP 500 | High | ✅ Fixed — fail-open behavior added (March 18) |
| Services exposed on 0.0.0.0 | High | ✅ Fixed — all 10 re-locked to 127.0.0.1 (March 18); see Section 40-C |
| Judge services orphaned (docker run, restart: no) | High | ✅ Fixed — all 5 compose-managed, restart: unless-stopped (March 18); see Section 40-C |
| Health-check amplification | High | ✅ Fixed — 30s TTL cache, 2s per-service timeout (March 18) |
| Hallucination on local community resources | High | 🔴 OPEN — gis_rag and local_resources return empty for Mount Hope queries; Community Champions data entry is next priority |
| gbim_query_router not in compose | High | ✅ Fixed — added to compose as 80th container (March 20); see Section 40-E |

---

## 40-C. Security Hardening Audit — March 18, 2026

Session date: March 18, 2026 (morning EDT)
Auditor: Carrie Kidd (Mamma Kidd), Harmony for Hope, Inc.
Branch at audit: `feature/cb-bbb-routing-fix`
Commits: `a10725d7` (judge compose management), `5007d605` (zero 0.0.0.0 exposures)
Purpose: Document all security hardening actions completed March 18, 2026 that brought the production stack to zero 0.0.0.0 exposures and formally compose-managed judge services.

### Summary

This session identified and remediated two classes of infrastructure security gap that had persisted across multiple previous sessions:

1. **Port exposure:** Multiple services were bound to `0.0.0.0`, making internal ports accessible on all network interfaces rather than exclusively on localhost. Ten services were re-locked to `127.0.0.1`, including several that had been correctly bound in earlier sessions but reverted during intermediate docker-compose.yml edits.

2. **Judge services orphaned:** All 5 judge services were running as manual `docker run` containers with `restart: no`. They were not defined in `docker-compose.yml` and had no Dockerfile or source files in the `services/` directory. On every system reboot or `docker compose down`, the entire judge pipeline would fail silently — the main brain would operate in degraded fallback mode with `consensus_score: 0.8` and `expert_count: 0` with no alerting.

By end of session, verified state: zero 0.0.0.0 exposures across all 80 containers; all 5 judge services compose-managed with `restart: unless-stopped`; 80-container stack fully managed by Docker Compose v5.1.0.

### Pre-Remediation State (Start of March 18 Session)

**Services Exposed on 0.0.0.0**

| Service | Exposed Port | Risk |
|---|---|---|
| jarvis-i-containers | 0.0.0.0:8015 | Identity manager — internal only |
| jarvis-consciousness-bridge | 0.0.0.0:8020 | Neurobiological pipeline — internal only |
| jarvis-constitutional-guardian | 0.0.0.0:8091 | Constitutional enforcement — internal only |
| jarvis-69dgm-bridge | 0.0.0.0:9000 | Had reverted from 127.0.0.1:19000 post-March audit |
| jarvis-wv-entangled-gateway | 0.0.0.0:8010 | WV RAG retrieval — internal only |
| jarvis-spiritual-rag | 0.0.0.0:8005 | GBIM/worldview RAG — internal only |
| jarvis-psychology-services | 0.0.0.0:8019 | Psychology pre-assessment — internal only |
| jarvis-hippocampus | 0.0.0.0:8011 | Memory consolidation — internal only |
| jarvis-gis-rag | 0.0.0.0:8004 | Geospatial RAG — internal only |
| jarvis-toroidal | 0.0.0.0:8025 | ChromaDB↔GIS sync — internal only |

> **Note on jarvis-69dgm-bridge:** This service was previously corrected to `127.0.0.1:19000->9000` during the March 2–3 audit. It reverted to `0.0.0.0:9000->9000` in an intermediate compose edit and was re-locked March 18. The canonical host binding is `127.0.0.1:19000:9000` (host port 19000 maps to internal container port 9000). Earlier documentation referencing the service at host port 9000 directly is incorrect.

**Judge Services Orphaned (pre-March 18)**

| Service | State | Restart Policy | In compose? | Source files in services/? |
|---|---|---|---|---|
| jarvis-judge-pipeline | Running (manual) | restart: no | ❌ No | ❌ No |
| jarvis-judge-truth | Running (manual) | restart: no | ❌ No | ❌ No |
| jarvis-judge-consistency | Running (manual) | restart: no | ❌ No | ❌ No |
| jarvis-judge-alignment | Running (manual) | restart: no | ❌ No | ❌ No |
| jarvis-judge-ethics | Running (manual) | restart: no | ❌ No | ❌ No |

Failure mode: On any reboot or `docker compose down`, Docker attempted to pull images for these containers from a registry. Because no public image exists with these names, pull would fail:

```
Error response from daemon: pull access denied for msjarvis-rebuild-jarvis-judge-ethics,
repository does not exist or may require 'docker login'
```

All 5 judge services would remain stopped indefinitely. The main brain would silently operate in degraded mode: `consensus_score: 0.8`, `expert_count: 0`, `judge_verdicts: {}`.

### Remediation Steps (March 18, 2026)

**Step 1 — Re-lock all services to 127.0.0.1**

Applied a Python replace pass over `docker-compose.yml` to convert all `0.0.0.0:PORT:PORT` and bare `- PORT:PORT` patterns to `- 127.0.0.1:PORT:PORT`. Containers recreated with `--force-recreate`.

Verification command (must return empty):

```bash
docker ps --format "{{.Names}}\t{{.Ports}}" | grep "0.0.0.0"
```

Result: empty — zero public exposures.

**Step 2 — Bring judge services under compose management**

Copied `services/Dockerfile.judge` from `services-safe/Dockerfile.judge`. Canonically named all 5 source files under `services/`:

```
services/judge_pipeline.py             (from jarvis-judge-pipeline_judge_pipeline.py)
services/judge_truth_filter.py         (from jarvis-judge-truth_lm_synthesizer.py)
services/judge_consistency_engine.py   (from jarvis-judge-consistency_lm_synthesizer.py)
services/judge_alignment_filter.py     (from jarvis-judge-alignment_lm_synthesizer.py)
services/judge_ethics_filter.py        (from jarvis-judge-ethics_lm_synthesizer.py)
```

Originals preserved in `services-safe/`.

Added all 5 judge service definitions to `docker-compose.yml` with `restart: unless-stopped`, `build: context: ./services`, `dockerfile: Dockerfile.judge`. All 5 rebuilt and started via `docker compose up -d --build`.

**Step 3 — Re-lock jarvis-69dgm-bridge host port**

Confirmed host port mapping as `127.0.0.1:19000:9000` in `docker-compose.yml`. Container recreated. This is the permanent canonical mapping for this service.

**Step 4 — Additional fixes deployed in this session**

| Fix | Details |
|---|---|
| BBB truth_score null guard | KeyError crash when truth_score absent from BBB response; null guard added |
| BBB fail-open on HTTP 500 | Both input filter and output guard now fail-open on non-200 BBB responses |
| LM Synthesizer target corrected | jarvis-roche-llm (HTTP 500) → jarvis-ollama:11434/api/generate with llama3.1:latest |
| Phase 3.75 eliminated | Final LLM Polish pass merged into Phase 3.5 single Ollama call; saves ~40s/query |
| BakLLaVA permanently disabled | Name-check guard added to ai_server_20llm_PRODUCTION.py |
| Health-check TTL cache | 30s TTL, 2s per-service timeout; Phase 1 health-check cost ~0.7s after first query |
| Phase 1.45 community memory retrieval | all-minilm:latest 384-dim, autonomous_learner collection (21,181 records), top-5 prepended to enhanced_message |

### Post-Remediation Verification (March 18, 2026)

```bash
# Zero 0.0.0.0 exposures — must return empty:
docker ps --format "{{.Names}}\t{{.Ports}}" | grep "0.0.0.0"
# Result: (empty)

# All 5 judge services compose-managed:
docker compose ps | grep judge
# Result: all 5 services show Up, compose-managed

# All 5 judge ports locked to 127.0.0.1:
docker ps --format "{{.Names}}\t{{.Ports}}" | grep judge
# Result: all show 127.0.0.1:7230-7233,7239 — no 0.0.0.0

# 69-DGM bridge re-locked:
docker ps --format "{{.Names}}\t{{.Ports}}" | grep 69dgm
# Result: jarvis-69dgm-bridge  127.0.0.1:19000->9000/tcp
```

**End-to-end benchmark post-remediation: ~436 seconds (optimized from 532s baseline)**

| Metric | Value |
|---|---|
| Total containers | 80 |
| 0.0.0.0 exposures | 0 |
| Judge services compose-managed | 5/5 |
| Judge services with restart: unless-stopped | 5/5 |
| End-to-end benchmark | ~436s |
| Consensus score (identity question) | 0.975 |
| Judge verdicts | Truth=1.0, Consistency=1.0, Alignment=1.0, Ethics=0.9 |

### Permanent Architectural Decisions Established March 18, 2026

All of the following are permanent decisions and must be preserved in all future builds:

- All services bound to `127.0.0.1`. No service may expose a port on `0.0.0.0`. Verification: `docker ps --format "{{.Names}}\t{{.Ports}}" | grep "0.0.0.0"` must return empty after any compose operation.
- `jarvis-69dgm-bridge` host port is `19000`. Internal container port is `9000`. Compose mapping: `127.0.0.1:19000:9000`. Never reference this service at port 9000 directly on the host.
- All 5 judge services must be defined in `docker-compose.yml` with `build: context: ./services`, `dockerfile: Dockerfile.judge` and `restart: unless-stopped`. Do not start judge services with manual `docker run`.
- Judge services evaluate consensus answer only. Never send `raw_responses` dump to judges.
- BakLLaVA disabled. Name-check guard in `ai_server_20llm_PRODUCTION.py` must be preserved.
- Phase 3.75 eliminated. Phase 3.5 is the complete, single Ollama voice delivery call.
- BBB fail-open. Non-200 BBB responses must not block the pipeline. Fail-open on both input filter and output guard.
- `all-minilm:latest` (384-dim) is the required embedding model. `nomic-embed-text` (768-dim) is incompatible with all existing ChromaDB collections.
- PostgreSQL `msjarvis` and `gisdb` at port 5433; `jarvis-local-resources-db` at port 5435; `msjarvisgis` at port 5432. See Section 40-E for `msjarvisgis` materialized view inventory.
- ChromaDB at port 8000 with `chroma_data` volume. Port 8002 is incorrect.

### Open Items After March 18 Session

| Item | Priority |
|---|---|
| Red-team adversarial test suite (20+ scenarios) | 🔴 HIGH |
| Hallucination on local community resources (Mount Hope, Fayette County) | 🔴 HIGH |
| jarvis-wv-entangled-gateway degraded — production_20llm URL config | 🟡 MEDIUM |
| Dead code below return in call_nbb_icontainers() | 🟢 LOW |
| Prometheus/Grafana metrics pipeline | 🟡 MEDIUM |
| GPU inference server (WVU partnership) | 🟡 MEDIUM |
| StarCoder2 (llm7-proxy) — retune or replace for community-domain queries | 🟡 MEDIUM |
| Formal JSON schemas for ensemble decision rules and judge aggregation | 🟡 MEDIUM |

---

## Appendix 40-D. Definitive Service Inventory (March 18, 2026)

Audit Date: March 18, 2026
Platform: Lenovo Legion 5 16IRX9 (Intel i9, NVIDIA RTX 4050, 29 GB RAM)
Audit method: `docker ps`, health endpoint probes, `docker inspect`, host PostgreSQL queries
Branch at audit: `feature/cb-bbb-routing-fix` (commit `5007d605`)
Total containers: 80 | 0.0.0.0 exposures: 0

### Security Remediation Log

| Date | Item | Before | After | Method |
|---|---|---|---|---|
| Mar 2–3, 2026 | jarvis-69dgm-bridge port binding | 0.0.0.0:19000->9000 | 127.0.0.1:19000->9000 | docker-compose.yml corrected, container recreated |
| Mar 2–3, 2026 | gbim-recovery port binding | 0.0.0.0:5459->5432 | Removed | Container stopped and removed; data confirmed on host PostgreSQL |
| Mar 18, 2026 | 10 services exposed on 0.0.0.0 | Various 0.0.0.0:PORT | All 127.0.0.1:PORT | Python replace pass on docker-compose.yml; --force-recreate |
| Mar 18, 2026 | 5 judge services orphaned | Manual docker run, restart: no | Compose-managed, restart: unless-stopped | Added build: entries + Dockerfile.judge to services/ |
| Mar 18, 2026 | jarvis-69dgm-bridge reverted exposure | 0.0.0.0:9000->9000 | 127.0.0.1:19000->9000 | Re-applied; was lost in intermediate compose edit |

Result as of March 18, 2026: Zero 0.0.0.0 exposures across all 80 running containers. All services localhost-only.

### Core Orchestration

| Container | Host Port | Internal Port | Status | Notes |
|---|---|---|---|---|
| jarvis-main-brain | 127.0.0.1:8050 | 8050 | ✅ Healthy | Primary entrypoint; /chat, /chatlight/async, /selftestfabric |
| jarvis-brain-orchestrator | 127.0.0.1:17260 | 7260 | ✅ Healthy | Continuous coordinator |
| jarvis-unified-gateway | 127.0.0.1:18018 | 8001 | ✅ Running | Defense-in-depth gateway; Constitutional Guardian → BBB |
| jarvis-semaphore | 127.0.0.1:8030 | 8030 | ✅ Healthy | Mandatory intermediary; max_concurrent: 4; requires timeout: 600.0 |
| jarvis-steward | none (internal 8060) | 8060 | ✅ Healthy | Internal only; no host binding; community stewardship interface |

### LLM Fabric

| Container | Host Port | Internal Port | Status | Notes |
|---|---|---|---|---|
| jarvis-20llm-production | 127.0.0.1:8008 | 8008 | ✅ Running | 22-slot ensemble; 21/22 responding; BakLLaVA permanently disabled |
| jarvis-ollama | 127.0.0.1:11434 | 11434 | ✅ Running | Ollama backend; 20 GB memory limit; 26 models available |
| jarvis-lm-synthesizer | none (internal 8001) | 8001 | ✅ Running | Phase 3.5 voice delivery; calls jarvis-ollama:11434/api/generate with llama3.1:latest |
| llm1-proxy | 127.0.0.1:8201 | 8201 | ✅ Running | TinyLlama (tinyllama:1.1b) |
| llm2-proxy | 127.0.0.1:8202 | 8202 | ✅ Running | Gemma (gemma:latest) |
| llm3-proxy | 127.0.0.1:8203 | 8203 | ✅ Running | MedLlama2 (medllama2:latest) |
| llm4-proxy | 127.0.0.1:8204 | 8204 | ✅ Running | MiniCPM-V (minicpm-v:latest) |
| llm5-proxy | 127.0.0.1:8205 | 8205 | ✅ Running | LLaVA (llava:latest) |
| llm6-proxy | 127.0.0.1:8206 | 8206 | ✅ Running | SQLCoder (sqlcoder:latest) |
| llm7-proxy | 127.0.0.1:8207 | 8207 | ⚠️ Running | StarCoder2 (starcoder2:latest) — frequently 0-char on community queries |
| llm8-proxy | 127.0.0.1:8208 | 8208 | ✅ Running | CodeLlama (codellama:latest) |
| llm9-proxy | 127.0.0.1:8209 | 8209 | ✅ Running | DeepSeek Coder (deepseek-coder:latest) |
| llm10-proxy | 127.0.0.1:8210 | 8210 | ✅ Running | Phi3 Mini (phi3:mini) |
| llm11-proxy | 127.0.0.1:8211 | 8211 | 🚫 Disabled | BakLLaVA — permanently disabled via name-check guard (CLIP load issues) |
| llm12-proxy | 127.0.0.1:8212 | 8212 | ✅ Running | Dolphin-Phi (dolphin-phi:latest) |
| llm13-proxy | 127.0.0.1:8213 | 8213 | ✅ Running | Orca-Mini (orca-mini:latest) |
| llm14-proxy | 127.0.0.1:8214 | 8214 | ✅ Running | Qwen2 (qwen2:latest) |
| llm15-proxy | 127.0.0.1:8215 | 8215 | ✅ Running | Zephyr (zephyr:latest) |
| llm16-proxy | 127.0.0.1:8216 | 8216 | ✅ Running | Starling-LM (starling-lm:latest) |
| llm17-proxy | 127.0.0.1:8217 | 8217 | ✅ Running | Neural-Chat (neural-chat:latest) |
| llm18-proxy | 127.0.0.1:8218 | 8218 | ✅ Running | OpenChat (openchat:latest) |
| llm19-proxy | 127.0.0.1:8219 | 8219 | ✅ Running | Vicuna (vicuna:latest) |
| llm20-proxy | 127.0.0.1:8220 | 8220 | ✅ Running | LLaMA 2 (llama2:latest) |
| llm21-proxy | 127.0.0.1:8221 | 8221 | ✅ Running | Mistral (mistral:latest) |
| llm22-proxy | 127.0.0.1:8222 | 8222 | ✅ Running | LLaMA 3.1 (llama3.1:8b) |

### Safety and Validation

| Container | Host Port | Internal Port | Status | Notes |
|---|---|---|---|---|
| jarvis-blood-brain-barrier | 127.0.0.1:8016 | 8016 | ✅ Running | 7-filter stack; output guard timeout 8.0s; truth_score null guard; fail-open on HTTP 500; re-locked Mar 18 |
| jarvis-69dgm-bridge | 127.0.0.1:19000 | 9000 | ✅ Running | Phase 7; 23 connectors × 3 stages = 69 DGM operations; host port 19000 → internal 9000; re-locked Mar 18 |
| jarvis-constitutional-guardian | 127.0.0.1:8091 | 8091 | ✅ Running | Constitutional enforcement; audit trail; re-locked Mar 18 |
| jarvis-psychology-services | 127.0.0.1:8019 | 8019 | ✅ Running | Phase 3 psychology pre-assessment on every request; re-locked Mar 18 |
| psychological_rag_domain | 127.0.0.1:8006 | 9006 | ✅ Running | Psychology RAG domain; 968 items; psychological_rag ChromaDB collection |

### Consciousness and Neurobiological Stack

| Container | Host Port | Internal Port | Status | Notes |
|---|---|---|---|---|
| jarvis-neurobiological-master | none (internal 8018) | 8018 | ✅ Running | v2.0.0; sequences 4/4 pipeline at ~300ms |
| jarvis-consciousness-bridge | 127.0.0.1:8020 | 8020 | ✅ Running | Re-locked to 127.0.0.1 Mar 18; mandatory neurobiological pipeline infrastructure |
| jarvis-qualia-engine | none (internal 8017) | 8017 | ✅ Running | Stage 3 of neurobiological pipeline |
| jarvis-i-containers | 127.0.0.1:8015 | 8015 | ✅ Running | Re-locked Mar 18; identity containers; icontainers-identity layer |
| jarvis-fifth-dgm | none (internal 4002) | 4002 | ✅ Running | Fifth Darwin-Gödel Machine |
| jarvis-mother-protocols | none (internal 4000) | 4000 | ✅ Running | Mother protocols; not wired into primary /chat path |
| jarvis-temporal-consciousness | none (internal 7007) | 7007 | ✅ Running | Flag-gated in pipeline |
| jarvis-fractal-consciousness | none (internal 8027) | 8027 | ✅ Running | Internal Docker network only |
| jarvis-swarm-intelligence | none (internal 8021) | 8021 | ✅ Running | Swarm coordination layer |
| jarvis-autonomous-learner | 127.0.0.1:8425 | 8425 | ✅ Running | 21,181+ items in autonomous_learner collection; ~288/day growth; queried at Phase 1.45 |
| jarvis-hippocampus | 127.0.0.1:8011 | 8011 | ✅ Running | Re-locked Mar 18; long-term memory consolidation |
| jarvis-toroidal | 127.0.0.1:8025 | 8025 | ✅ Healthy | Re-locked Mar 18; Toroidal ChromaDB↔GIS bidirectional sync loop |

### NBB Subconscious Layer (13 containers)

| Container | Host Port | Internal Port | Status | Notes |
|---|---|---|---|---|
| nbb-i-containers | 127.0.0.1:8101 | 7001 | ✅ Running | NBB I-containers; also exposes 7005 internally |
| nbb_consciousness_containers | 127.0.0.1:8102 | 7002 | ✅ Running | |
| nbb_spiritual_root | 127.0.0.1:8103 | 7003 | ✅ Running | |
| nbb_woah_algorithms | 127.0.0.1:8104 | 7004 | ✅ Running | WOAH port 8104 host → internal 7004; jarvis-woah = port 7012 |
| nbb_prefrontal_cortex | 127.0.0.1:8105 | 7005 | ✅ Running | Distinct from nbb-i-containers |
| nbb_heteroglobulin_transport | 127.0.0.1:8106 | 7006 | ✅ Running | |
| nbb_mother_carrie_protocols | 127.0.0.1:8107 | 7007 | ✅ Running | |
| nbb_pituitary_gland | 127.0.0.1:8108 | 7008 | ✅ Running | Health via Redis DynamicPortService |
| nbb_spiritual_maternal_integration | 127.0.0.1:8109 | 7009 | ✅ Running | |
| nbb_subconscious | 127.0.0.1:8112 | 7011 | ✅ Running | |
| nbb_blood_brain_barrier | 127.0.0.1:8301 | 7001 | ✅ Running | NBB-layer BBB |
| nbb_darwin_godel_machines | 127.0.0.1:8302 | 7003 | ✅ Running | |
| nbb_qualia_engine | 127.0.0.1:8303 | 7008 | ✅ Running | |

### Judge Pipeline (All Compose-Managed — March 18, 2026)

All 5 judge services were previously orphaned manual `docker run` containers with `restart: no`. As of March 18, 2026, all are formally managed by `docker-compose.yml` with `restart: unless-stopped`, built from `services/Dockerfile.judge`. All ports locked to `127.0.0.1`.

| Container | Host Port | Internal Port | Status | Compose-managed | Notes |
|---|---|---|---|---|---|
| jarvis-judge-pipeline | 127.0.0.1:7239 | 7239 | ✅ Running | ✅ Yes (Mar 18) | Master coordinator; judge_pipeline.py |
| jarvis-judge-truth | 127.0.0.1:7230 | 7230 | ✅ Running | ✅ Yes (Mar 18) | Truth filter; judge_truth_filter.py |
| jarvis-judge-consistency | 127.0.0.1:7231 | 7231 | ✅ Running | ✅ Yes (Mar 18) | Consistency engine; judge_consistency_engine.py |
| jarvis-judge-alignment | 127.0.0.1:7232 | 7232 | ✅ Running | ✅ Yes (Mar 18) | Alignment filter; judge_alignment_filter.py |
| jarvis-judge-ethics | 127.0.0.1:7233 | 7233 | ✅ Running | ✅ Yes (Mar 18) | Ethics filter; judge_ethics_filter.py |

**Judge Source File Registry**

```
services/Dockerfile.judge              # Shared build for all 5 judge containers
services/judge_pipeline.py             # Master coordinator
services/judge_truth_filter.py         # Truth filter
services/judge_consistency_engine.py   # Consistency engine
services/judge_alignment_filter.py     # Alignment filter
services/judge_ethics_filter.py        # Ethics filter
```

Originals preserved in `services-safe/` as `jarvis-judge-*_lm_synthesizer.py` (one per domain) and `jarvis-judge-pipeline_judge_pipeline.py`.

### RAG and Retrieval Services

| Container | Host Port | Internal Port | Status | Notes |
|---|---|---|---|---|
| jarvis-rag-server | 127.0.0.1:8003 | 8003 | ✅ Running | Primary text RAG; /store accepts user_id |
| jarvis-gis-rag | 127.0.0.1:8004 | 8004 | ✅ Running | Re-locked Mar 18; spatial/benefits RAG over gisdb PostGIS |
| jarvis-spiritual-rag | 127.0.0.1:8005 | 8005 | ✅ Running | Re-locked Mar 18; GBIM/worldview RAG; confirmed port 8005 |
| jarvis-wv-entangled-gateway | 127.0.0.1:8010 | 8010 | ⚠️ Degraded | Re-locked Mar 18; WV-biased multi-collection retrieval; production_20llm URL config needs fix |
| jarvis-web-research | 127.0.0.1:18008 | 8008 | ✅ Running | Host port 18008 → internal 8008 |
| jarvis-aaacpe-rag | 127.0.0.1:8032 | 8032 | ✅ Running | Appalachian cultural intelligence RAG; 10 documents |
| jarvis-aaacpe-scraper | 127.0.0.1:8033 | 8033 | ✅ Running | AaaCPE scraper; shared aaacpe-cultural-data volume |
| jarvis-local-resources | none (internal 8006) | 8006 | ✅ Running | ZIP/county-keyed program registry; internal only |
| jarvis-agents-service | none (internal 8005) | 8005 | ✅ Healthy | Agents service; internal only |
| jarvis-woah | none (internal 7012) | 7012 | ✅ Running | WOAH algorithms service; internal only |

### Data Stores (March 18, 2026 baseline)

| Container / Service | Host Port | Type | Status | Notes |
|---|---|---|---|---|
| jarvis-chroma | 127.0.0.1:8000 | ChromaDB | ✅ Healthy | chroma_data volume; all collections 384-dim (all-minilm:latest); port 8000 (not 8002) |
| jarvis-redis | 127.0.0.1:6380 | Redis 7 | ✅ Healthy | DynamicPortService; NBB health registration; async job state 30-min TTL |
| jarvis-local-resources-db | 127.0.0.1:5435 | PostGIS 15 | ✅ Running | Community resources; human-validated by Harmony for Hope Community Champions |
| Host PostgreSQL msjarvis | 127.0.0.1:5433 | PostgreSQL 16 | ✅ Verified | GBIM corpus: 5,416,521 verified beliefs; 80 epochs; 206 source layers; temporal decay metadata |
| Host PostgreSQL gisdb | 127.0.0.1:5433 | PostGIS 16 | ✅ Verified | 13 GB; 39 tables; 993 ZCTA centroids |
| ipfs/kubo | 127.0.0.1:5001 | IPFS | ✅ Running | Intentional infrastructure — content addressing for MountainShares/The Commons; kubo/0.39.0; 19 external peers; corpus currently empty (default pin only) |

> **PostgreSQL note (March 18):** Both `msjarvis` (GBIM) and `gisdb` (PostGIS) listen on host port 5433. `jarvis-local-resources-db` listens on host port 5435. Port 5432 was not used at this snapshot — see Section 40-E for the `msjarvisgis` database added at port 5432.

### GBIM Corpus State (March 18, 2026 Verified)

| Metric | Value |
|---|---|
| Database | Host PostgreSQL msjarvis, port 5433 |
| Verified belief count | 5,416,521 |
| Fully classified beliefs | 1,356,660 across 24 named epochs |
| Training epochs | 80 |
| Source layers | 206 |
| Temporal decay metadata | last_verified, confidence_decay, needs_verification per entity |
| Pending epoch enrichment | 4,059,862 across 20+ source tables |
| Largest unclassified sources | WV GIS TC building footprints (2.1M), SAMB structure points (1.4M), wind energy (209K), flood plain structures (81K) |
| Last ingestion date | February 20, 2026 |
| Projected post-enrichment count | ~10M (pending epoch enrichment scripts) |

> **Thesis correction required:** Earlier chapters and the December 2025 audit referenced 10,221,702 beliefs. The correct verified count is 5,416,521 as of February 20, 2026. The projected ~10M figure is post-enrichment.

### Thesis Corrections Required (Identified at March 18 Audit)

| Chapter | Current Text | Correct Text |
|---|---|---|
| 39 and all others | "10,221,702 beliefs" | "5,416,521 verified beliefs (Feb 20, 2026); ~10M projected post epoch enrichment" |
| 11, 17, others | "jarvis-web-research: 18009" | "jarvis-web-research: host 18008 → internal 8008" |
| 11, 12, 17 | NBB "8 containers" | NBB "13 containers" |
| 11, 40 | ipfs/kubo not documented | Intentional MountainShares/Commons infrastructure |
| 11 | jarvis-steward not documented | Internal service port 8060; community stewardship interface |
| 11 | jarvis-toroidal not documented | Toroidal ChromaDB↔GIS sync; host port 8025; re-locked Mar 18 |
| 11 | jarvis-fractal-consciousness not documented | Internal consciousness service; port 8027 |
| 11 | jarvis-agents-service not documented | Internal agents service; port 8005 |
| 33 | Judge services "orphaned containers" | Judge services compose-managed as of March 18, 2026 |
| 40 | No March 18 security audit | Section 40-C added |

### Audit Summary (March 18, 2026)

| Category | Count | Status |
|---|---|---|
| Total containers running | 80 | ✅ |
| Core orchestration | 5 | ✅ All healthy |
| LLM fabric (proxies + Ollama + LM Synthesizer) | 25 | ✅ 21/22 responding; BakLLaVA disabled |
| Safety and validation | 5 | ✅ All running |
| Consciousness/neurobiological | 12 | ✅ All running |
| NBB subconscious layer | 13 | ✅ All running |
| Judge pipeline | 5 | ✅ All running; compose-managed Mar 18 |
| RAG and retrieval | 10 | ⚠️ 9/10 healthy; wv-entangled-gateway degraded |
| Data stores | 3 containers + 2 host clusters + IPFS | ✅ All accessible |
| Services with 0.0.0.0 exposure | 0 | ✅ Zero |
| Judge services compose-managed | 5/5 | ✅ |
| Previously undocumented services | 6 | 📝 Thesis update required |
| GBIM belief count | 5,416,521 | 📝 Thesis correction required |

*Last updated: March 18, 2026 — Carrie A. Kidd*

---

## 40-E. GBIM Landowner Layer Audit — March 20, 2026

Session date: March 20, 2026
Auditor: Carrie Kidd (Mamma Kidd), Harmony for Hope, Inc.
Platform: Lenovo Legion 5 16IRX9 — `~/msjarvis-rebuild-working/msjarvis-rebuild/`
Purpose: Document the complete ingestion of 20,593 GBIM landowner belief records, the creation and indexing of `mvw_gbim_landowner_spatial`, the promotion of `gbim_query_router` (port 7205) to compose management as the 80th container, and the first verified query results from the GBIM landowner belief layer.

### Summary

This session completed three sequential operations that together close the **`who` axis** of geographic belief at parcel scale:

1. **Entity clustering** — 511 candidate entities with `total_acres > 1,000` extracted from `gbim_entity_land_candidates` and reduced to 401 canonical landowner entities via Union-Find + RapidFuzz (`token_sort_ratio`, `score_cutoff=85`) clustering written to `gbim_entity_clusters`. 402 rows total in `gbim_entities` (401 landowner entities + 1 health_facility).

2. **Belief ingest** — 20,593 `LANDOWNER_CORPORATE` / `LANDOWNER_GOVERNMENT` beliefs ingested to `gbimbeliefnormalized` in `msjarvisgis` (port 5432) with `worldview_id: 3` (eq1), `belief_strength: 1.0`, `belief_state: confirmed`, `recorded_by: wv_tax_ingest_2025`. Ingest timestamp: 2026-03-20 07:44 EDT.

3. **Router promotion** — `gbim_query_router` (port 7205) added to `docker-compose.yml` as the 80th compose-managed container. Service serves landowner queries via `mvw_gbim_landowner_spatial` exclusively — no ChromaDB, no LLM ensemble, no web research.

### ★ Materialized View Inventory — msjarvisgis (port 5432)

This is the authoritative inventory of materialized views in `msjarvisgis` as of March 20, 2026. All views listed here are spatially indexed and available for query.

```
msjarvisgis (PostgreSQL 16 + PostGIS, port 5432, 91 GB, 501 tables)

Materialized Views:
───────────────────────────────────────────────────────────────────────────────
View name                        Status     Spatial index   Served by              Notes
───────────────────────────────────────────────────────────────────────────────
mvw_gbim_landowner_spatial       ✅ LIVE    ✅ Yes          gbim_query_router:7205  ★ Added March 20, 2026
                                                                                    Joins gbimbeliefnormalized ↔
                                                                                    wvtaxparcels2025 on cleaned
                                                                                    parcel ID. Proposition codes:
                                                                                    LANDOWNER_CORPORATE /
                                                                                    LANDOWNER_GOVERNMENT.
                                                                                    20,593 belief records.
                                                                                    worldview: eq1 (worldview_id: 3).
                                                                                    Refresh: manual (cadence TBD).
                                                                                    NOT in ChromaDB.
building_parcel_county_tax_mv    ✅ LIVE    ✅ Yes          jarvis-local-resources  7,354,707 rows.
                                                            -db (port 5435)         Source: WV tax assessor 2025.
───────────────────────────────────────────────────────────────────────────────
```

**`mvw_gbim_landowner_spatial` — column schema:**

```sql
-- Key columns in mvw_gbim_landowner_spatial
canonical_entity     TEXT       -- Canonical entity name from gbim_entity_clusters
entity_geodbid       UUID       -- gbim_entities.geodbid
proposition_code     TEXT       -- LANDOWNER_CORPORATE | LANDOWNER_GOVERNMENT
belief_strength      NUMERIC    -- 1.0 (all records)
belief_state         TEXT       -- confirmed (all records)
feature_ref          TEXT       -- wvtaxparcels2025:CLEANPARCELID
county_id            TEXT       -- WV county code
acres                NUMERIC    -- Parcel acreage from wvtaxparcels2025
geom                 GEOMETRY   -- PostGIS geometry (from wvtaxparcels2025)
observed_at          TIMESTAMPTZ
recorded_by          TEXT       -- wv_tax_ingest_2025
worldview_id         INTEGER    -- 3 (eq1)
```

**Refresh command:**

```sql
-- Manual refresh (run as postgres on msjarvisgis):
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_gbim_landowner_spatial;
```

> ⚠️ **Scheduled refresh cadence is pending.** Until a cron or pg_cron job is configured, `mvw_gbim_landowner_spatial` must be refreshed manually after any bulk landowner belief update.

### Top 30 Canonical Landowner Entities (Verified Terminal Output, March 20, 2026)

These results are drawn directly from the Union-Find clustering output written to `gbim_entity_clusters` and are the canonical entities backing `mvw_gbim_landowner_spatial`.

```
canonical_name                                           variant_count  total_acres  total_parcels  county_count
WEYERHAEUSER COMPANY                                              1     242,892.1            518             4
POCAHONTAS SURFACE INTERSTS LLC                                  25     205,113.2            393             2
HEARTWOOD FORESTLAND FUND VI LLC                                  7     174,608.8            462            11
LYME MOUNTAINEER TIMBERLANDS I LLC                                7     138,873.2            481             3
PENN VIRGINIA OPERATING CO LLC                                    2     112,343.8            341             7
WESTERN POCAHONTAS PROPERTIES LIMITED PARTNERSHIP                 4      91,658.3            343             9
ALLEGHENY FORESTLANDS LLC                                         5      63,886.2            292            14
MIKE ROSS INC                                                     2      59,104.6          1,043            27
COASTAL FOREST RESOURCES COMPANY                                  1      53,835.3            251            12
BECKWITH LUMBER COMPANY INC                                       3      44,520.5            329             8
SCIOTO LAND CO LLC                                                2      43,075.5            521             7
ROWLAND LAND COMPANY LLC TR
