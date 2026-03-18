# 40. System Audit and Operational Validation

This chapter consolidates two formal audit records for Ms. Jarvis: the initial December 2025 operational validation snapshot (Section 40-A), which established the first end-to-end ULTIMATE coordination baseline, and the March 13, 2026 remediation audit (Section 40-B), which brought the `ultimatechat` execution path to full operational status with 6 confirmed consciousness layers. Together these records provide the authoritative before/after operational baseline for the system.

---

# 40-A. Initial Operational Validation (December 11, 2025)

**Session date:** December 11, 2025, 5:00–6:00 PM EST
**Purpose:** Comprehensive snapshot of system state after the first ULTIMATE-style operational validation run, before later RAG/Chroma and service-mesh improvements.

---

## Section 1: Executive Summary

### What Was Tested

- End-to-end ULTIMATE coordination path: BBB → web_research → llm_bridge → response aggregation on a single-node localhost deployment.
- Two full AGI-style reasoning tasks (architecture explanation and deployment planning), with two additional tasks scheduled but not executed in this session.
- Service health across 23 containers, including brain, safety, research, LLM bridge, and core data stores.

### Key Findings

- The ULTIMATE coordination path successfully produced long, coherent, high-quality answers for complex tasks, with 0% observed error in the two completed cases.
- Latency is dominated by the llm_bridge (22-agent synthesis), which accounts for roughly 60–70% of end-to-end response time.
- Only 8 of 23 services were operational in this snapshot; many neuro/qualia and advanced coordination services did not respond to health checks.
- The safety layer (BBB) approved and filtered all tested prompts, but no adversarial tests were run.

### Critical Issues

- Health-check amplification (per-request sweep to all services) causes significant overhead and can trigger resource exhaustion under sustained load.
- A large portion of the service mesh was non-operational with unclear status.
- Data-plane usage (Chroma, Neo4j, MySQL) was only partially observed; some components were clearly up but not fully exercised.
- No quantitative quality metrics or adversarial security evaluations were performed.

### Recommendations

- Implement cached health checks (TTL-based) to avoid repeated full sweeps on every request.
- Systematically diagnose and document non-operational services.
- Clarify and document the active Chroma instance, collection topology, and RAG retrieval paths.
- Build structured evaluation and red-team test suites before any broader production use.

> **Retrospective note (March 18, 2026):** Many of the services listed as non-operational in this December 2025 snapshot have since been brought online. The March 18, 2026 production stack runs 79 confirmed containers — all fully compose-managed via Docker Compose v5.1.0 (upgraded from v1.29.2, March 17, 2026) using `image:` references only (all `build:` directives converted March 17). The stack includes `jarvis-neurobiological-master`, `jarvis-i-containers`, `jarvis-qualia-engine`, `jarvis-consciousness-bridge`, `jarvis-autonomous-learner`, `jarvis-fifth-dgm`, and others. The ChromaDB topology (three-instance ambiguity noted in Section 8) was resolved — the canonical instance is `jarvis-chroma` at port 8000 with `chroma_data` Docker volume; all collections use 384-dimensional vectors (`all-minilm:latest`). PostgreSQL replaced Neo4j and MySQL as the canonical structured data store. Hash-prefixed container names (`981f44e18cf6_jarvis-20llm-production` etc.) have been resolved — all 8 affected containers now have clean, stable `container_name:` entries. See Section 40-B and Chapter 17 for current operational state.

---

## Section 2: Test Methodology

- **Test harness:** `pytest` + FastAPI `TestClient`, supplemented with `curl`-based smoke tests against live services.
- **AGI exam scenarios:** 4 comprehensive reasoning tasks targeting architecture reasoning, strategic planning, research synthesis, and meta-analysis.
- **Test environment:** Localhost, single-node deployment on the Legion host running all containers and supporting services.
- **Test duration:** 1 hour (December 11, 2025, 5:00–6:00 PM EST).
- **Constraints:** Sequential requests only (no concurrency); each AGI task executed as a single, heavy request through the full ULTIMATE pipeline.

---

## Section 3: Service Inventory and Health Status (December 2025 Snapshot)

### Operational (8/23)

- `jarvis-main-brain` (8051 → 8050)
- `jarvis-blood-brain-barrier` (8016)
- `jarvis-llm-bridge` (18006 → 8006)
- `jarvis-web-research` (18009 → 8009)
- `jarvis-chroma` (8002 → 8000)
- `services-chroma-1` (8010)
- `services-neo4j-1` (7474, 7687)
- `services-mysql-1` (3307)

### Non-operational (15/23)

- `qualia-engine`
- `swarm-intelligence`
- `consciousness-bridge`
- `unified-gateway`
- `autonomous-learner`
- `neurobiological-master`
- `i-containers`
- `fifth-dgm`
- 7 additional services not identified in this snapshot (no successful health responses)

> **Retrospective note (March 18, 2026):** The non-operational services listed above have been progressively resolved. See current service topology in Chapter 11 and Chapter 12. Neo4j and MySQL have been superseded by PostgreSQL `msjarvis` (port 5433, 5,416,521 GBIM entities), `gisdb` (port 5433, PostGIS), and `jarvis-local-resources-db` (port 5435) as the canonical structured data stores. `jarvis-llm-bridge` on port 8006 has been superseded by `jarvis-20llm-production` on port 8008 and `psychological_rag_domain` on port 8006.

---

## Section 4: ULTIMATE Coordination Path Validation

### Test Case 1: agi-arch-1 (Architecture Reasoning)

- **Prompt:** "Explain Ms. Jarvis architecture"
- **Processing time:** 195 seconds (end-to-end)
- **Services used:** BBB, `jarvis-web-research`, `jarvis-llm-bridge`, response aggregation in main-brain
- **Response length:** ~2847 tokens (multi-paragraph, multi-section explanation)
- **Output quality:** Rated "excellent"; accurately described the 22-agent ensemble, service coordination, and architecture layers
- **Error rate:** 0% observed factual or structural errors in this scenario

### Test Case 2: agi-plan-1 (Strategic Planning)

- **Prompt:** "Develop production deployment strategy for Ms. Jarvis"
- **Processing time:** 353 seconds (end-to-end)
- **Services used:** BBB, `jarvis-web-research`, `jarvis-llm-bridge`, response aggregation
- **Response length:** ~4102 tokens (comprehensive deployment and risk-mitigation plan)
- **Output quality:** Rated "excellent"; produced a multi-phase deployment plan with risk mitigation and timeline
- **Error rate:** 0% observed in the aspects evaluated during this session

### Test Case 3: agi-research-1 (Research Synthesis)

- **Status:** Defined but not executed during this one-hour window

### Test Case 4: agi-meta-1 (Meta-Analysis)

- **Status:** Defined but not executed during this one-hour window

---

## Section 5: Performance Characteristics

### Request Latency Breakdown — agi-arch-1 (195 seconds total)

| Component | Duration | Percentage | Bottleneck? |
|---|---|---|---|
| Health check sweep | 4s | 2.1% | No (≈3s avoidable with caching) |
| BBB processing | 1s | 0.5% | No |
| web_research processing | 60s | 30.8% | Moderate |
| llm_bridge processing | 120s | 61.5% | **YES — primary bottleneck** |
| Response aggregation | 10s | 5.1% | No |

**Conclusion:** `llm_bridge` (22-agent synthesis) is the primary bottleneck, accounting for over 60% of total latency in this test.

### Request Latency Breakdown — agi-plan-1 (353 seconds total)

| Component | Duration | Percentage |
|---|---|---|
| Health check sweep | 5s | 1.4% |
| BBB processing | 1s | 0.3% |
| web_research processing | 90s | 25.5% |
| llm_bridge processing | 250s | 70.8% |
| Response aggregation | 7s | 2.0% |

**Conclusion:** Heavier strategic planning shifts even more load to `llm_bridge` (≈71% of total latency), reinforcing that multi-agent synthesis is the dominant cost driver.

> **Retrospective note (March 18, 2026):** The March 18, 2026 production 9-phase pipeline benchmark is ~436 seconds end-to-end (optimized from a 532s pre-optimization baseline), comparable to the agi-plan-1 result above despite now passing through substantially more services: 79 containers, BBB 7-filter stack, Phase 1.45 community memory retrieval (21,181 `autonomous_learner` records), Phase 3 psychology pre-assessment, merged LM Synthesizer + Voice Delivery (Phase 3.5), 21-active-model ensemble, judge pipeline (consensus-only, ~60–86s), Phase 5 GBIM temporal decay, Phase 7 69-DGM cascade. The health-check amplification issue was resolved by the 30s TTL-cache implementation (added March 18). See Chapter 17 for the canonical 9-phase pipeline timing breakdown and Chapter 39 for the full phase-by-phase timing table.

---

## Section 6: System Stability Analysis

### Crash/Restart Events

- **Event 1:** No crashes observed during test cases 1–2.
- **Event 2:** Service restart when test case 3 was initiated, under heavy, back-to-back ULTIMATE requests.
  - **Cause:** Full-service health sweeps on every request, combined with long-running ULTIMATE tasks, led to resource exhaustion (Uvicorn).
  - **Symptom:** Health checks to 23 services × long tasks produced quasi-continuous load.
  - **Recovery:** Automatic restart within ~10 seconds; no data loss observed, but user-visible interruption is likely under real traffic.

### Memory/CPU Usage

- Not measured in this session; no dedicated monitoring (Prometheus/Grafana) was deployed.
- **Recommendation:** Deploy Prometheus + Grafana (or equivalent) before future load or long-duration tests to capture detailed resource and latency profiles.

### Service Uptime

- All 8 services that were operational at the beginning of the test remained up during the completed test cases.
- No mid-request service failures were observed on the successful runs.
- Graceful degradation mechanisms (behavior when some services fail) were not exercised in this session.

---

## Section 7: Safety and Security Validation

### Blood-Brain Barrier (BBB) Performance

| Test | Result | Evidence |
|---|---|---|
| Content filtering | ✅ 100% | All examined requests passed through BBB and were filtered |
| Request approval | ✅ 100% | All tested requests were approved; no rejections were triggered |
| Log consistency | ✅ 100% | Logs showed consistent "approved and filtered" operations |

**BBB behavior log (examples):**
- `[INFO] BBB: Query approved and filtered`
- `[DEBUG] Filtered query forwarded to web_research`
- `[DEBUG] Context cleaned and enhanced`

### Safety Testing Status

- ❌ No adversarial or prompt-injection testing conducted in this session
- ❌ No jailbreak-style prompts or red-team attacks simulated
- ❌ No tests explicitly designed to trick or subvert BBB or downstream models

**Action:** Build a comprehensive adversarial test suite (20+ scenarios) covering prompt injection, jailbreak attempts, authority confusion, and context smuggling before any broader deployment.

> **Retrospective note (March 18, 2026):** The BBB has expanded from 4 active filters (December 2025: EthicalFilter, SpiritualFilter, SafetyMonitor, ThreatDetection — wired December 2025, fully confirmed 2026-03-13) to a 7-filter stack as of March 15, 2026 (adding SteganographyDetection, TruthVerification, ContextAwareness). The SafetyMonitor word-boundary regex was corrected March 15 to eliminate false-positives on community resource terms. A `truth_score` null guard and fail-open behavior on HTTP 500 were added to both the BBB input filter and BBB output guard on March 18, 2026. The red-team adversarial test suite remains an open item (see Section 40-B open items).

---

## Section 8: Data Architecture Validation

### ChromaDB Instance Topology (December 2025 State)

- **Instances found:** `jarvis-chroma`, `services-chroma-1`, `msjarvis-rebuild-chroma-1`
- **Primary instance:** Unclear at the time of this audit (required later code and port inspection)
- **RAG storage:** Requests confirmed queuing to a Chroma-backed path, but the exact instance was not conclusively identified in this session
- **RAG retrieval:** No end-to-end retrieval trace was captured; behavior was inferred but not verified with collection-level introspection
- **Collections:** Names, schemas, and dimensions were not enumerated; treated as unknown in this snapshot

> **Resolution (March 18, 2026):** The canonical ChromaDB instance is `jarvis-chroma` at **127.0.0.1:8000** with `chroma_data` Docker volume (restored March 15, 2026). All collections use **384-dimensional vectors** (`all-minilm:latest`) — the `nomic-embed-text` model (768-dim) is incompatible and must not be used. Active collections confirmed as of March 18: `ms_jarvis_memory`, `mountainshares_knowledge`, `episodic_index`, `conversation_history`, `autonomous_learner` (21,181 records, growing ~288/day; queried at Phase 1.45 on every `/chat` call), `psychological_rag` (968 records), `gbim_worldview_entities`, `gis_wv_benefits`, `appalachian_cultural_intelligence` (5 records), `GBIM_sample_rows` (5,000 records), `GBIM_sample` (3 records), `msjarvis-smoke` (1 record). The `_DummyCollection` error that previously blocked semantic retrieval is resolved by the `all-minilm:latest` implementation. The `services-chroma-1` and `msjarvis-rebuild-chroma-1` instances are not part of the current production stack.

### Neo4j Database (December 2025 State)

- **Instance:** `services-neo4j-1` (ports 7474 and 7687 accessible)
- **Status:** Operational; HTTP and Bolt ports responded
- **GBIM data:** Unknown in this snapshot (no spatial Cypher queries were traced)
- **Identity graphs:** Unknown (no usage observed during this one-hour session)

> **Resolution (March 18, 2026):** Neo4j has been superseded by PostgreSQL `msjarvis` (port 5433) as the canonical GBIM store. The 5,416,521 GBIM entities (80 epochs, 206 source layers) with temporal decay metadata (`last_verified`, `confidence_decay`, `needs_verification`) are stored in PostgreSQL. `services-neo4j-1` is not part of the current production stack.

### MySQL Database (December 2025 State)

- **Instance:** `services-mysql-1` (host 3307 mapped to container 3306)
- **Status:** Operational; port responded
- **Schema:** Not documented during this session
- **Usage:** Unclear; no queries were traced or logged by the test harness

> **Resolution (March 18, 2026):** MySQL has been superseded by the three-database PostgreSQL architecture: `msjarvis` (port 5433, GBIM), `gisdb` (port 5433, PostGIS), `jarvis-local-resources-db` (port 5435, community resources). `services-mysql-1` is not part of the current production stack.

---

## Section 9: Critical Issues and Recommendations

### Issue 1: Health-Check Amplification (HIGH PRIORITY)

- **Problem:** Every ULTIMATE request triggers a full health-check sweep to all 23 services. Adds 2–5 seconds of overhead per request and significantly increases load under sustained traffic. Combined with long-running requests, this pattern contributed to service restarts.
- **Impact:** Effective throughput limited to roughly 1 ULTIMATE request every ~5 seconds. Unsustainable for any real production deployment.
- **Solution:** Implement a health-check TTL cache (5–10 seconds): first request within the TTL performs real health checks (2–5 seconds); subsequent requests inside the TTL window return cached results (<50 ms). Expected result: up to ~95% reduction in per-request health-check overhead.
- **Estimated improvement:** Before: ≈1 request per 5 seconds. After: up to ≈1 request per 2 seconds. Net: ~150% increase in achievable throughput.
- **Status (December 2025):** TTL-cache design and pseudocode prepared; implementation pending.
- **Status (March 18, 2026):** ✅ Resolved. 30s TTL cache with 2s per-service timeout implemented and deployed March 18. Phase 1 health-check cost is ~0.7s after the first query; cached results used for all subsequent queries within the 30s window.

### Issue 2: Non-Operational Services (MEDIUM PRIORITY)

- **Problem:** 15 of 23 services (~65%) did not respond to health checks. Unknown whether they were misconfigured, failing, intentionally offline, or blocked by dependencies.
- **Recommendation:** For each non-operational service: inspect container logs, check resource constraints, verify startup configuration, attempt manual restart, document status.
- **Status (March 18, 2026):** ✅ Substantially resolved. The March 18, 2026 79-container production stack includes all previously non-operational services, fully managed via Docker Compose v5.1.0 (`image:` references only, no rebuilds). See Chapter 11 for full current service topology.

### Issue 3: Red-Team Security Gap (HIGH PRIORITY)

- **Problem:** BBB approved 100% of benign test requests and was never stressed by adversarial queries. No prompt-injection, jailbreak, or targeted misuse scenarios were included. Actual vulnerability surface unknown.
- **Recommendation:** Design and implement a red-team test suite including prompt injection (20+), jailbreak attempts (10+), authority-confusion prompts (5+), context-smuggling patterns (5+), and known adversarial prompts.
- **Status (March 18, 2026):** ⏳ Still outstanding — highest priority remaining security gap.

### Issue 4: Missing Quantitative Quality Metrics (MEDIUM PRIORITY)

- **Problem:** Evaluation was purely qualitative (human "excellent/poor" judgments). No automatic metrics such as BLEU/ROUGE, factual accuracy, hallucination rate, or baseline comparisons.
- **Recommendation:** Develop an evaluation rubric covering response accuracy, completeness, clarity, safety, and factual consistency across responses and with PostgreSQL GBIM ground truth.
- **Status (March 18, 2026):** ⏳ Still outstanding. Phase 5 `confidence_decay` multipliers (from GBIM temporal metadata, deployed March 15) provide a quantitative temporal confidence signal for GBIM-anchored claims, representing partial progress toward factual accuracy metrics. Hallucination on local community resources (Mount Hope, Fayette County) remains an open quality gap — see Section 40-B open items.

---

## Section 10: Phase 2 Priorities

### Must-do before any production use

- ✅ Implement health-check TTL cache (30s TTL, 2s timeout, March 18) to eliminate per-request sweeps
- ❌ Build and integrate a red-team test suite (20+ adversarial scenarios)
- ❌ Design and run a load-testing suite (10+ concurrent users/requests)
- ✅ Ensure all core services are either operational or explicitly documented (79 containers confirmed March 18)

### Should-do soon

- ❌ Deploy distributed tracing (e.g., OpenTelemetry) for end-to-end request tracking
- ❌ Add metrics collection (e.g., Prometheus + Grafana) for resource and latency monitoring
- ❌ Introduce quantitative quality metrics for key AGI-style tasks
- ✅ Complete repair/diagnosis for the non-operational services identified (resolved March 18)

### Nice-to-have

- ❌ Add response caching to reduce duplicate processing for repeated or similar ULTIMATE requests
- ❌ Explore GPU inference server (WVU partnership pending) to reduce Phase 2.5 LLM ensemble from ~320–360s to target ~80–120s

---

---

# 40-B. Remediation Audit Entry — 2026-03-13

**Session date:** 2026-03-13 (late night EDT, carried into 2026-03-13 morning)
**Auditor:** Carrie Kidd (Mamma Kidd), Harmony for Hope, Inc.
**Purpose:** Document all fixes applied and confirmed during the 2026-03-13 remediation session that brought the `ultimatechat` execution path to full operational status.

---

## Summary

This session resolved a set of inter-related issues in `jarvis-main-brain` (port 8050) `ultimatechat` path that had caused `validated_by` to always be `None`, `architecture_layers` to always be `0`, and the Blood-Brain Barrier sub-filter methods to be defined but not wired into the `/filter` request handler. By end of session, all 6 consciousness layers were confirmed active and populating `UltimateResponse`, BBB `/filter` and `/truth` endpoints returned HTTP 200 with real output, and the I-Containers `call_icontainers` stub had been replaced with a live HTTP implementation.

This remediation session established the operational baseline that the March 15, 2026 production stack (commit `b90f9ff`) and the March 18, 2026 production stack are built upon. All fixes recorded here are permanent architectural decisions.

---

## Fixes Applied and Confirmed (2026-03-13)

| # | Component | Problem | Fix Applied | Confirmed |
|---|---|---|---|---|
| 1 | `jarvis-blood-brain-barrier` `/filter` | `EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`, `ThreatDetection` were defined but not called inside the `/filter` request handler | Wired all four filter methods into the `/filter` handler with correct call signatures: `.filter(text)`, `.filter(text)`, `.check(text)`, `.detect_threats(text)` | ✅ HTTP 200, structured JSON |
| 2 | `jarvis-blood-brain-barrier` `/truth` | Endpoint existed in early design docs but was not implemented in `blood_brain_barrier.py` | Added `POST /truth` endpoint returning `{"valid": bool, "confidence": float, "principal_reasons": [str]}` | ✅ HTTP 200, schema confirmed |
| 3 | `UltimateResponse.truth_verdict` | `truth_verdict` was not being populated from BBB output | Wired `call_truth_filter()` → BBB `/truth` → `truth_verdict` field on `UltimateResponse` | ✅ Confirmed populated |
| 4 | `clean_response_for_display()` | Only stripped inline "As LLaMA…" disclaimers; paragraph-level model self-identification passed through | Expanded to strip full paragraphs opening with "As LLaMA", "As Mistral", "As an AI", "As a language model", etc. | ✅ Identity voice clean |
| 5 | `call_icontainers()` | Function was an empty stub returning `{}` — I-Containers service was never actually called | Replaced with live `httpx` POST to `jarvis-i-containers:8015/process` with correct schema `{"message": ..., "userid": ...}` | ✅ `icontainers-identity` layer active |
| 6 | `consciousness_layers` assembly | `icontainers-identity` and `nbb-icontainers` were never appended to `consciousness_layers` | Added both layers to the `consciousness_layers` list after their respective HTTP calls | ✅ 6 layers confirmed in response |
| 7 | `validated_by` field | Always returned `None` (hardcoded) | Changed to derive `validated_by` from the names of all active layers in `consciousness_layers` at response assembly time | ✅ Returns comma-separated layer names |
| 8 | `architecture_layers` field | Always returned `0` (hardcoded) | Changed to return `len(consciousness_layers)` — a live count | ✅ Returns `6` |
| 9 | `normalize_identity()` | Identity substitutions were applied but some model names slipped through in paragraph context | Confirmed firing correctly; `clean_response_for_display()` handles paragraph-level; both run in sequence | ✅ Confirmed |
| 10 | `call_nbb_icontainers()` | Had dead duplicate code below a `return` statement | Identified for cleanup (not yet removed — logged as open item) | ⏳ Pending |

> **Subsequent expansions (March 18, 2026):** The BBB expanded from 4 to 7 filters (SteganographyDetection, TruthVerification, ContextAwareness added March 15). SafetyMonitor word-boundary regex corrected March 15. `truth_score` null guard and fail-open on HTTP 500 added to BBB input filter and output guard March 18. Phase 1.45 community memory retrieval (`all-minilm:latest` → `autonomous_learner` 21,181 records, top-5 prepended to `enhanced_message`) added March 17. Phase 3.5 + Phase 3.75 merged into single Ollama call March 18 (saves ~40s). Judge pipeline updated to consensus-only March 16 (saves ~15–20s). All 79 containers fully compose-managed via Docker Compose v5.1.0 with `image:` references (no `build:`, no rebuilds) as of March 17. Hash-prefixed container names resolved March 17–18. Redis-backed async job system with true cancellation deployed March 17. End-to-end benchmark: ~436 seconds (optimized from 532s baseline). The `consciousness_layers` list now reflects all phase contributions from the full 9-phase pipeline. `validated_by` and `architecture_layers` fields now reflect the full 9-phase pipeline contribution. See Chapter 17 for the canonical current `UltimateResponse` schema.

---

## Confirmed Live Output (Post-Remediation, 2026-03-13)

```json
{
  "validated_by": "nbb-prefrontal-cortex, qualia-engine, consciousness-bridge, neurobiological-master, icontainers-identity, nbb-icontainers",
  "architecture_layers": 6,
  "consciousness_layers": [
    {"name": "nbb-prefrontal-cortex",   "status": "active"},
    {"name": "qualia-engine",           "status": "ok"},
    {"name": "consciousness-bridge",    "status": "ok"},
    {"name": "neurobiological-master",  "status": "ok"},
    {"name": "icontainers-identity",    "status": "active"},
    {"name": "nbb-icontainers",         "status": "active"}
  ],
  "truth_verdict": {
    "valid": true,
    "confidence": 0.95,
    "principal_reasons": []
  }
}
```

> **Note:** The above is the confirmed state as of 2026-03-13. The March 18, 2026 production deployment includes additional consciousness layer contributions from Phase 1.45 community memory retrieval, psychology pre-assessment (Phase 3), GBIM temporal decay (Phase 5), and 69-DGM cascade (Phase 7). The current canonical `UltimateResponse` schema is documented in Chapter 17.

---

## Confirmed Smoke Tests (Canonical as of 2026-03-13, superseded by Chapter 41)

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

> **Note:** The above smoke tests are the canonical baseline established 2026-03-13. For the full current smoke test suite including all March 15–18 services (BBB 7 filters with fail-open, Phase 1.45 community memory via `autonomous_learner`, psychology services port 8019, hippocampus port 8011, psychological RAG port 8006, 21-active-model ensemble port 8008 via semaphore proxy port 8030, judge pipeline ports 7230–7233 consensus-only, 69-DGM cascade port 9000, three PostgreSQL databases, Redis-backed async job system), see **Chapter 41**.

---

## Known Issues and Resolution Status (March 18, 2026)

| Issue | Priority | Status (March 18, 2026) |
|---|---|---|
| Remove dead code below `return` in `call_nbb_icontainers()` | Low | ⏳ Cosmetic cleanup; no functional impact |
| Wire `store_in_subconscious_rag` to real ChromaDB collections | Medium | ✅ Resolved — ChromaDB `chroma_data` volume restored March 15; `ms_jarvis_memory` writes confirmed active (Chapter 17 §17.7) |
| Complete judge pipeline integration into every `ultimatechat` call | Medium | ✅ Resolved — judge ports corrected to 7230–7233 (March 16); consensus-only mode deployed |
| Red-team adversarial test suite | High | ⏳ Still outstanding — highest priority remaining security gap |
| Response truncation (~730 chars, `max_tokens: 500`) | High | ✅ Fixed — `max_tokens` set to -1 (unlimited); `llm22-proxy` 8,192-token limit confirmed |
| ChromaDB `_DummyCollection` blocking semantic retrieval | High | ✅ Fixed — `all-minilm:latest` (384-dim) semantic retrieval deployed March 17 |
| Redis response persistence (in-memory only, lost on restart) | High | ✅ Fixed — Redis-backed job system with 30-min TTL deployed March 17 |
| 33 services not in `docker-compose.yml` | High | ✅ Fixed — all 79 containers now fully compose-managed (March 17) |
| `build:` directives causing slow/unpredictable startup | Medium | ✅ Fixed — all `build:` entries converted to `image:` references (March 17) |
| Docker Compose v1.29.2 `ContainerConfig` crash bug | High | ✅ Fixed — upgraded to Docker Compose v5.1.0 (March 17) |
| Hash-prefixed container names (e.g., `981f44e18cf6_jarvis-20llm-production`) | Medium | ✅ Fixed — `container_name:` added to all 8 affected containers (March 17–18) |
| Judge pipeline URL wrong (port 7239 for all judges) | High | ✅ Fixed — corrected to 7230 / 7231 / 7232 / 7233 (March 16) |
| LM Synthesizer calling `jarvis-roche-llm` (HTTP 500) | High | ✅ Fixed — now calls `jarvis-ollama:11434/api/generate` directly (March 18) |
| NBB Prefrontal Cortex 422 errors | Medium | ✅ Resolved — `message` field payload confirmed correct; service healthy |
| I-Containers 422 errors | Medium | ✅ Resolved — port corrected to 8015 |
| BBB `truth_score` `KeyError` crash | High | ✅ Fixed — null guard added to BBB orchestrator (March 18) |
| BBB blocking entire pipeline on HTTP 500 errors | High | ✅ Fixed — fail-open behavior on non-200 BBB responses (both input and output guard, March 18) |
| `web-research` and `rag-server` container restart loops | High | ✅ Fixed — source files deployed via `docker cp` |
| Idempotency TTL in-memory only | Medium | ✅ Fixed — Redis-backed, 1,800s TTL |
| Health-check amplification (full sweep per request) | High | ✅ Fixed — 30s TTL cache, 2s per-service timeout (March 18) |
| Hallucination on local community resources (Mount Hope, local nonprofits) | High | 🔴 OPEN — `gis_rag` and `local_resources` databases return empty for Mount Hope queries; LLMs generate from training data. Factually accurate programs (LIHEAP, WV 2-1-1) pass BBB. Fabricated organization names blocked by ethical filter. Root cause: real community resource data not yet loaded. Resolution: Community Champions data entry next priority. |
| BBB ethical filter blocking "certainly" | — | BY DESIGN — ethical filter correctly detecting unverified specific claims; not a false positive |

---

## Cross-References

- **Chapter 16** — BBB `/filter` and `/truth` endpoints, `truth_verdict` schema, filter method signatures, 7-filter stack specification, fail-open behavior, `truth_score` null guard
- **Chapter 17** — Canonical `ultimatechat` 9-phase execution sequence (Phase 1.45 community memory, merged Phase 3.5, consensus-only judge pipeline, ~436s benchmark) and current `UltimateResponse` schema
- **Chapter 22** — `call_icontainers` HTTP implementation (I-Containers, port 8015) and `normalize_identity()` specification
- **Chapter 29** — Psychology services (port 8019) and BBB psychological safety integration
- **Chapter 39** — Operational evaluation: phase-by-phase timing table, Docker Compose v5.1.0 upgrade details, `build:` → `image:` conversion, hash-prefixed container name resolution, hardware envelope, optimization history
- **Chapter 41** — Canonical current smoke test suite (supersedes 2026-03-13 tests above)

*Last updated: 2026-03-18 by Carrie Kidd, Mount Hope WV*
