# Chapter 33 — Language Model Ensemble and Judge Systems in Live Operation

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: ★★★ 2026-04-06 — 83/83 containers Up — container count corrected from prior 96/96 stamp; all LEARN-series issues confirmed resolved; §33.14 closing state added; §33.13 April 6 column added. Previous: ★★ 2026-04-01 — 96/96 containers Up — LEARN-01 numpy dtype fix, LEARN-02 GBIM router HTTP 422, LEARN-03 crash-loop recovery all resolved; `autonomous_learner` fully restored. Previous: ★ 2026-03-28 — 96/96 containers Up — `msjarvis` port 5433 restored; ChromaDB full audit 40 collections / 6,675,442 vectors; `psychological_rag` restored; `autonomous_learner` ~23,961+ records.*

*Annotation key: ★ = March 28, 2026 confirmation · ★★ = April 1, 2026 confirmation · ★★★ = April 6, 2026 confirmation*

---

This chapter describes how multiple language models and evaluation components operate together in Ms. Jarvis during live requests, all grounded in the three-database PostgreSQL architecture. Confirmed production state: `msjarvis` port **5433** ★ (5,416,521 GBIM entities with `confidence_decay` metadata, restored March 28); `gisdb` / `msjarvisgis` port **5432** ★ (91 GB PostGIS, 501 tables, 993 ZCTA centroids, confirmed March 28); `jarvis-local-resources-db` port **5435**; ChromaDB ★ 40 active collections / 6,675,442 total vectors; `autonomous_learner` ★★ fully restored April 1, 2026; ★★★ 83/83 services healthy confirmed April 6, 2026 via Redis registry health sweep; all services bound exclusively to `127.0.0.1` with zero `0.0.0.0` exposures; `jarvis-memory:8056` providing durable authenticated BBB audit trail across the full pipeline.

---

## 33.0 April 1, 2026 Autonomous Learner Remediation (LEARN Series)

The following three issues affecting the `jarvis-autonomous-learner` container were fully resolved on April 1, 2026. These items are part of the permanent architectural record of this chapter because the autonomous learner's Phase 1.45 community memory injection feeds directly into ensemble prompts, and its integrity is prerequisite to the ensemble quality described throughout §§33.1, 33.6, and 33.7.

---

### LEARN-01 — `cosine_similarity()` numpy dtype mismatch (RESOLVED April 1, 2026)

**Root cause:** `ms_jarvis_autonomous_learner_optimized.py` called `cosine_similarity()` with numpy arrays whose dtype was not consistently cast prior to the operation. Under certain embedding return shapes from `jarvis-ollama:11434/api/embeddings`, the function received a dtype incompatible with the dot-product path, raising:

```
TypeError: ufunc 'multiply' did not contain a loop with signature matching types
(dtype('<U...'), dtype('<U...')) -> None
```

**Fix:** Explicit `float32` cast applied before cosine computation:

```python
# BEFORE (LEARN-01 bug):
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# AFTER (LEARN-01 fix — April 1, 2026):
def cosine_similarity(a, b):
    a = np.array(a, dtype=np.float32)
    b = np.array(b, dtype=np.float32)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))
```

**Impact:** The dtype mismatch caused the learner's self-similarity evaluation loop to raise an unhandled exception, preventing new records from being scored and committed. Records received during the affected window were queued and committed post-fix. Zero Phase 1.45 records were lost; the `autonomous_learner` ChromaDB collection count was unaffected.

**Verification:**

```bash
# Confirm float32 cast present in learner:
grep -n "float32\|dtype" services/ms_jarvis_autonomous_learner_optimized.py
# Expected: at least one float32 cast line in cosine_similarity()

# Confirm learner is processing (check recent record count):
docker exec jarvis-chroma python3 -c "
import chromadb
client = chromadb.HttpClient(host='localhost', port=8002)
col = client.get_collection('autonomous_learner')
print('autonomous_learner count:', col.count())
"
```

---

### LEARN-02 — GBIM Query Router (port 7205) returning HTTP 422 on Autonomous Learner `/route` calls (RESOLVED April 1, 2026)

**Root cause:** The autonomous learner's belief-routing logic was constructing its `POST /route` payload to `gbim_query_router:7205` with a mis-shaped request body. The router's FastAPI schema expected a `query` field at the top level; the learner was sending a nested `payload.query` structure. FastAPI's Pydantic validator returned HTTP 422 Unprocessable Entity on every learner-originated routing call.

This caused all autonomous learner → GBIM router interactions to silently fail: the learner logged `"router_status": 422` and continued without grounding the new belief record in `msjarvis:5433`. Beliefs were being stored in `autonomous_learner` ChromaDB only — not committed as GBIM entities with `confidence_decay` metadata.

**Fix:** Learner request body corrected to match the router's Pydantic schema:

```python
# BEFORE (LEARN-02 bug):
router_payload = {
    "payload": {
        "query": belief_text,
        "user_id": self.user_id,
        "context": belief_metadata
    }
}

# AFTER (LEARN-02 fix — April 1, 2026):
router_payload = {
    "query": belief_text,
    "user_id": self.user_id,
    "context": belief_metadata
}
```

**Impact:** New autonomous learner belief records generated after the fix are now correctly committed as GBIM entities in `msjarvis:5433` with `confidence_decay` metadata, completing the full learner → GBIM entity lifecycle. Beliefs created during the affected window exist in ChromaDB only and are flagged for a one-time backfill migration. Backfill procedure documented in §33.6 addendum.

**Impact on ensemble:** The HTTP 422 error was silent at the Phase 1.45 level — the main brain received community memory retrieval results from ChromaDB regardless of whether the underlying belief had been GBIM-committed. Ensemble quality during the affected window was not degraded; the router failure affected only GBIM entity record completeness, not Phase 1.45 context injection.

**Verification:**

```bash
# Confirm learner sends top-level query field (not nested payload.query):
grep -n "payload.*query\|\"query\"" services/ms_jarvis_autonomous_learner_optimized.py | head -20
# Expected: "query": belief_text — NOT nested under "payload"

# Confirm GBIM router accepts learner calls (HTTP 200):
curl -s -o /dev/null -w "%{http_code}" \
  http://127.0.0.1:7205/route \
  -H "Content-Type: application/json" \
  -d '{"query": "test belief", "user_id": "learn-test", "context": {}}'
# Expected: 200

# Confirm new learner records are being GBIM-committed (psql):
docker exec msjarvis psql -U postgres -d msjarvis -c \
  "SELECT COUNT(*) FROM gbim_entities WHERE source='autonomous_learner' AND created_at > NOW() - INTERVAL '1 hour';"
# Expected: count > 0 if learner has fired in the last hour
```

---

### LEARN-03 — `jarvis-autonomous-learner` container crash-loop after zero-byte file deployed (RESOLVED April 1, 2026)

**Root cause:** During the LEARN-01 patch attempt, a failed copy operation deployed a zero-byte `ms_jarvis_autonomous_learner_optimized.py` to the container build context. The subsequent `docker compose up --build jarvis-autonomous-learner` produced a container that started successfully (Python imported the empty file without syntax errors) but raised `AttributeError: module has no attribute 'AutonomousLearner'` on first instantiation, causing the container to exit with code 1 immediately. Docker's `restart: unless-stopped` policy caused the container to re-enter the crash-loop every ~10 seconds, briefly reducing the effective running container count during the repair window.

**Fix:**

1. Correct patched file (with LEARN-01 float32 fix) confirmed present on host filesystem at `services/ms_jarvis_autonomous_learner_optimized.py`
2. Container rebuilt with `--no-cache`: `docker compose build --no-cache jarvis-autonomous-learner && docker compose up -d jarvis-autonomous-learner`
3. Container confirmed Up with zero Restarts: `docker ps --filter name=jarvis-autonomous-learner --format "{{.Names}}\t{{.Status}}"`

**Impact:** Zero data loss. The `autonomous_learner` ChromaDB collection was unaffected (external volume). The crash-loop window lasted approximately 45 minutes before resolution. During this window, Phase 1.45 community memory injection fell back to an empty result set — documented degraded-mode behavior (see §33.8).

**Permanent rule:** Before deploying any patched service file, verify file size is non-zero:

```bash
# Verify file is non-empty before build:
ls -la services/ms_jarvis_autonomous_learner_optimized.py
# Expected: size > 0 bytes

# After build, verify class is importable:
docker exec jarvis-autonomous-learner python3 -c "
from ms_jarvis_autonomous_learner_optimized import AutonomousLearner
print('AutonomousLearner: importable OK')
"
# Expected: AutonomousLearner: importable OK
```

---

## 33.1 Roles of the Core Models

In the current deployment, the live system assigns three primary roles to language models and services.

**Task execution (experts).** ★★★ 83 services healthy as of April 6, 2026 (Redis registry confirmed 83 registered / 83 healthy via tonight's Python health sweep — see §33.14 for full closing state and note on container count delta from prior 96/96 stamp). LLM proxies (`llm1-proxy` through `llm22-proxy`) confirmed running at `127.0.0.1:8201–8222`; ★★ 22 registered / 21 active (BakLLaVA at port 8211 permanently disabled via name-check guard; StarCoder2 at port 8207 frequently returns 0-character responses on community-domain queries). For each consensus request, all active models receive the same composite prompt — which already includes Phase 1.45 community memory from `autonomous_learner` (★★ fully restored April 1, 2026 — see §33.0 LEARN-01/02/03; live count verification command in §33.3; ★ within 40 active collections / 6,675,442 total vectors), PostgreSQL-sourced RAG context from `jarvis-spiritual-rag` (port 8005, queries GBIM collections in `msjarvis:5433` ★), PostgreSQL GeoDB context from `jarvis-gis-rag` (port 8004, queries `gisdb:5432` ★ — 91 GB PostGIS, 501 tables, 993 ZCTA centroids), container-state hints, and orchestration directives — and generate independent candidate answers.

**Structural transformation.** The LM Synthesizer (port 8001) calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest` and the Ms. Egeria Jarvis persona prompt injected. **The LM Synthesizer is called exclusively from `main_brain.py` Phase 3.5 — `judge_pipeline.py` must not call it (duplicate call removed March 22, 2026).** ★★ All LM Synthesizer invocations and associated BBB gate decisions are now durably logged at `jarvis-memory:8056` (secured March 28; confirmed Up April 1, 2026; ★★★ confirmed Up April 6, 2026).

**Evaluation and critique.** Evaluation is handled by a 5-service judge pipeline composed of `jarvis-judge-pipeline` (coordinator, port 7239) and four specialized FastAPI services: `judge-truth` (7230), `judge-consistency` (7231), `judge-alignment` (7232), and `judge-ethics` (7233). All five are compose-managed with `restart: unless-stopped` and ★★★ confirmed Up in the April 6, 2026 83/83 count. The pipeline coordinator calls all four judges in parallel via `asyncio.gather()` against the consensus answer only — the raw_responses dump is no longer sent to judges (March 16, 2026). The pipeline coordinator issues a live `bbb_check_verdict` call to `jarvis-blood-brain-barrier:8016/filter` after aggregation (March 21, 2026). ★★ All `bbb_check_verdict` gate decisions are durably logged at `jarvis-memory:8056`.

---

## 33.2 Judge Services: From Orphaned Containers to Compose Management

> **[CONTENT PENDING — IMPORT FROM MARCH 28 VERSION]**
> Full remediation record from March 18 and March 21, 2026, including §33.2.3 `heuristic_contradiction_v1` honest limitations and `rag_grounded_v2` upgrade path. All content current as of April 6, 2026. OI-23 tracking the `rag_grounded_v2` upgrade remains Open.
>
> **TODO: This section is a blocking gap for chapter close. Import from the March 28 source document before publishing. Issue reference: CH33-PENDING-002.**

---

## 33.3 Authoritative Model List (★★★ April 6, 2026 — 83/83 Up)

Table core unchanged from March 28 — all 22 proxies confirmed Up in April 6, 2026 83/83 count.

| Proxy | Port | Model | Status |
|:--|:--|:--|:--|
| llm1-proxy | 8201 | TinyLlama (tinyllama:1.1b) | ★★★ Active (Up) |
| llm2-proxy | 8202 | Gemma (gemma:latest) | ★★★ Active (Up) |
| llm3-proxy | 8203 | MedLlama2 (medllama2:latest) | ★★★ Active (Up) |
| llm4-proxy | 8204 | MiniCPM-V (minicpm-v:latest) | ★★★ Active (Up) |
| llm5-proxy | 8205 | LLaVA (llava:latest) | ★★★ Active (Up) |
| llm6-proxy | 8206 | SQLCoder (sqlcoder:latest) | ★★★ Active (Up) |
| llm7-proxy | 8207 | StarCoder2 (starcoder2:latest) | Proxied — frequently 0-char on community queries |
| llm8-proxy | 8208 | CodeLlama (codellama:latest) | ★★★ Active (Up) |
| llm9-proxy | 8209 | DeepSeek Coder (deepseek-coder:latest) | ★★★ Active (Up) |
| llm10-proxy | 8210 | Phi3 Mini (phi3:mini) | ★★★ Active (Up) |
| llm11-proxy | 8211 | BakLLaVA — DISABLED | ★★★ Container Up — inference blocked by name-check guard |
| llm12-proxy | 8212 | Dolphin-Phi (dolphin-phi:latest) | ★★★ Active (Up) |
| llm13-proxy | 8213 | Orca-Mini (orca-mini:latest) | ★★★ Active (Up) |
| llm14-proxy | 8214 | Qwen2 (qwen2:latest) | ★★★ Active (Up) |
| llm15-proxy | 8215 | Zephyr (zephyr:latest) | ★★★ Active (Up) |
| llm16-proxy | 8216 | Starling-LM (starling-lm:latest) | ★★★ Active (Up) |
| llm17-proxy | 8217 | Neural-Chat (neural-chat:latest) | ★★★ Active (Up) |
| llm18-proxy | 8218 | OpenChat (openchat:latest) | ★★★ Active (Up) |
| llm19-proxy | 8219 | Vicuna (vicuna:latest) | ★★★ Active (Up) |
| llm20-proxy | 8220 | LLaMA 2 (llama2:latest) | ★★★ Active (Up) |
| llm21-proxy | 8221 | Mistral (mistral:latest) | ★★★ Active (Up) |
| llm22-proxy | 8222 | LLaMA 3.1 (llama3.1:8b) | ★★★ Active (Up) |

**Active: ★★★ 21 models** (22 proxies registered / 21 active — confirmed April 6, 2026 83/83 Up).

> **`autonomous_learner` record count — current as of April 6, 2026:**
> Prior arithmetic estimates are stale. Run the authoritative live count:

```bash
docker exec jarvis-chroma python3 -c "
import chromadb
client = chromadb.HttpClient(host='localhost', port=8002)
col = client.get_collection('autonomous_learner')
print('autonomous_learner count:', col.count())
"
```

> For reference: March 28, 2026 confirmed count was ~23,961+ records (authoritative for that date). April 1 floor estimate was ~25,213+. As of April 6 (9 days after March 28 baseline at ~288 records/day), the estimated floor is ~23,961 + (9 × 288) = **~26,553+** — treat as a floor only; the live query above is the authoritative source. The LEARN-01 and LEARN-03 disruption windows may reduce the actual figure modestly below this estimate.

---

## 33.4 Judge Components and Evaluation Criteria

> **[CONTENT PENDING — IMPORT FROM MARCH 28 VERSION]**
> Full text including all judge evaluation criteria, scoring rubrics, and weighting logic for `judge-truth` (7230), `judge-consistency` (7231), `judge-alignment` (7232), and `judge-ethics` (7233). Judge pipeline was unaffected by LEARN-series issues. All 5 judge services confirmed Up in April 6, 2026 83/83 count.
>
> **TODO: This section is a blocking gap for chapter close. Import from the March 28 source document before publishing. Issue reference: CH33-PENDING-004.**

---

## 33.5 Phase 3.5 — LM Synthesizer + Voice Delivery (Merged, March 18, 2026)

> **[CONTENT PENDING — IMPORT FROM MARCH 28 VERSION]**
> Full text including:
> - §33.5.1 — Identity guard (3 active layers): no model name leakage confirmed stable through April 6, 2026
> - §33.5.2 — `cleanResponseForDisplay` fix (Commit 40-B fix 4): no "As LLaMA" / "As Mistral" artifacts confirmed through April 6, 2026
> - §33.5.3 — AU-02 Developer Impersonation Guard: confirmed active through April 6, 2026
>
> All three confirmed stable through ★★★ April 6, 2026 83/83 count. No content changes required on import — operational status annotations only.
>
> **TODO: This section is a blocking gap for chapter close. Import from the March 28 source document before publishing. Issue reference: CH33-PENDING-005.**

---

## 33.6 Ensemble Patterns

> **[CONTENT PENDING — IMPORT FROM MARCH 28 VERSION]**
> Core ensemble pattern text covering prompt composition, Phase 1.45 injection sequence, consensus aggregation approach, and fallback behavior when community memory retrieval returns empty results. The addendum below is new to the April 1/April 6 versions and must be preserved on import.
>
> **TODO: This section is a blocking gap for chapter close. Import from the March 28 source document before publishing. Issue reference: CH33-PENDING-006.**

### §33.6 Addendum — April 1, 2026: LEARN-02 Backfill Procedure

Beliefs created by the autonomous learner during the LEARN-02 affected window (between last confirmed GBIM-commit and the April 1 fix) exist in ChromaDB `autonomous_learner` collection but were **not** committed as GBIM entities in `msjarvis:5433`. These records carry `source: "autonomous_learner"` metadata in ChromaDB but have no corresponding row in `gbim_entities` with `confidence_decay` metadata.

**One-time backfill procedure:**

```bash
# Step 1: Identify learner records not yet GBIM-committed.
# Outputs ungrounded records to /tmp/ungrounded_learner_records.json.
docker exec jarvis-chroma python3 - << 'EOF'
import chromadb, json
client = chromadb.HttpClient(host='localhost', port=8002)
col = client.get_collection('autonomous_learner')
results = col.get(include=['metadatas', 'documents'], limit=10000)
ungrounded = [
    {"id": results['ids'][i], "doc": results['documents'][i], "meta": results['metadatas'][i]}
    for i in range(len(results['ids']))
    if not results['metadatas'][i].get('gbim_committed', False)
]
print(f"Ungrounded learner records: {len(ungrounded)}")
with open('/tmp/ungrounded_learner_records.json', 'w') as f:
    json.dump(ungrounded, f, indent=2)
EOF

# Step 2 — Pseudocode: adapt for your record IDs before running.
# For each record in /tmp/ungrounded_learner_records.json, POST to GBIM router:
#   curl -s http://127.0.0.1:7205/route \
#     -H "Content-Type: application/json" \
#     -d '{"query": "<doc>", "user_id": "backfill-learn02", "context": <meta>}'

# Step 3 — Pseudocode: after each GBIM commit is confirmed (HTTP 200),
# update ChromaDB metadata to mark the record as committed:
#   col.update(ids=[record_id], metadatas=[{"gbim_committed": True, ...existing_meta}])
```

**Going forward:** All new learner records generated after the LEARN-02 fix include `gbim_committed: True` in their ChromaDB metadata only after a successful HTTP 200 from the GBIM router. A `gbim_committed: False` flag is written first, then updated to `True` on confirmed commit — creating an auditable two-phase record.

---

## 33.7 Phase-by-Phase Timing (★★★ Updated April 6, 2026 — 83/83 Up)

> **[CONTENT PENDING — IMPORT FROM MARCH 28 VERSION]**
> Full timing table rows covering all pipeline phases are missing. Import the complete phase-by-phase table from the March 28 source document, then apply the Phase 1.45 annotation update below.
>
> **TODO: This section is a blocking gap for chapter close. Import from the March 28 source document before publishing. Issue reference: CH33-PENDING-007.**

**Phase 1.45 status as of April 6, 2026: FULLY RESTORED AND CONFIRMED** — `jarvis-autonomous-learner` Up, LEARN-01 dtype fix active, LEARN-02 router payload corrected, LEARN-03 crash-loop resolved. Community memory injection operating at full capacity as of April 6, 2026 83/83 health sweep. For authoritative record count, run the live verification query in §33.3.

**Timing baseline reference (apply to imported table):**
- CPU-only Phase 2.5 baseline (prior): ~436s — retained as historical record only
- GPU inference Phase 2.5 (RTX 4070, current): 88–115s
- Verified end-to-end pipeline: **99–107s** (confirmed runs: 99.6s, 105.9s, 106.5s — March 22, 2026)

---

## 33.8 Use in Live Cycles

> **[CONTENT PENDING — IMPORT FROM MARCH 28 VERSION]**
> Full text covering live query lifecycle, Phase 1.45 community memory injection flow, degraded-mode behavior (empty `autonomous_learner` results → prompt proceeds without community context — operationally confirmed during LEARN-03 crash-loop window ~45 min, April 1, 2026), and recovery path.
>
> **TODO: This section is a blocking gap for chapter close. Import from the March 28 source document before publishing. Issue reference: CH33-PENDING-008.**

---

## 33.9 Consensus Mechanisms

> **[CONTENT PENDING — IMPORT FROM MARCH 28 VERSION]**
> Full text covering consensus aggregation strategy, response selection, scoring, and tie-breaking logic.
>
> **TODO: This section is a blocking gap for chapter close. Import from the March 28 source document before publishing. Issue reference: CH33-PENDING-009.**

---

## 33.10 Integration with the DGM Layer

> **[CONTENT PENDING — IMPORT FROM MARCH 28 VERSION]**
> Full text covering DGM layer integration, how judge verdicts feed back into the DGM governance model, and the OI-23 `rag_grounded_v2` upgrade path relationship to DGM.
>
> **TODO: This section is a blocking gap for chapter close. Import from the March 28 source document before publishing. Issue reference: CH33-PENDING-010.**

---

## 33.11 Authoritative Port Table (★★★ April 6, 2026)

All host-facing ports confirmed bound to `127.0.0.1`. Zero `0.0.0.0` exposures across ★★★ 83/83 containers (confirmed April 6, 2026 via Redis registry health sweep).

| Service | Host Port | Container Port | Notes |
|:--|:--|:--|:--|
| `jarvis-main-brain` | 8050 | 8050 | Primary orchestrator |
| `jarvis-lm-synthesizer` | 8001 | 8001 | Phase 3.5 sole owner |
| `jarvis-20llm-production` | 8008 | 8008 | 21-LLM ensemble |
| `jarvis-semaphore` | 8030 | 8030 | `max_concurrent: 4`, `timeout: 600.0` |
| `jarvis-judge-pipeline` | 7239 | 7239 | Coordinator — does NOT call synthesizer |
| `jarvis-judge-truth` | 7230 | 7230 | `heuristic_contradiction_v1` |
| `jarvis-judge-consistency` | 7231 | 7231 | |
| `jarvis-judge-alignment` | 7232 | 7232 | AU-02 active |
| `jarvis-judge-ethics` | 7233 | 7233 | |
| `jarvis-blood-brain-barrier` | 8016 | 8016 | Corrected from `0.0.0.0` |
| `jarvis-memory` | 8056 | 8056 | ★ Secured March 28 — durable BBB audit trail |
| `jarvis-autonomous-learner` | internal only | 8080 | ★★ Restored April 1 — no host port binding; accessed exclusively via `jarvis-main-brain` |
| `gbim_query_router` | 7205 | 7205 | ★★ HTTP 422 on learner calls resolved April 1 (LEARN-02) |
| `jarvis-ollama` | 11434 | 11434 | LLaMA 3.1, all-minilm, embeddings |
| `jarvis-rag-server` | 8003 | 8003 | OI-18 open — not yet wired to gateway inference |
| `jarvis-spiritual-rag` | 8005 | 8005 | Queries `msjarvis:5433` GBIM |
| `jarvis-gis-rag` | 8004 | 8004 | Queries `gisdb:5432` PostGIS |
| `jarvis-aaacpe-rag` | 8032 | 8032 | 53 docs loaded ★ |
| `jarvis-aaacpe-scraper` | 8033 | 8033 | 65 docs, 39 sources, `total_runs: 1` ★ |
| ChromaDB (`jarvis-chroma`) | **8002** | 8000 | ★ 40 collections / 6,675,442 vectors · host 8002, container-internal 8000 |
| Redis (`jarvis-redis`) | **6380** | 6379 | ★★★ Confirmed 6380 — health sweep verified April 6 |
| PostgreSQL `msjarvis` | **5433** | 5432 | ★ 5,416,521 GBIM entities, `confidence_decay` |
| PostgreSQL `gisdb` / `msjarvisgis` | **5432** | 5432 | ★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids |
| PostgreSQL `jarvis-local-resources-db` | **5435** | 5432 | Community resources |
| `llm1-proxy` through `llm22-proxy` | 8201–8222 | 8201–8222 | ★★★ 22 registered / 21 active |

**Redis health verification (against confirmed host port 6380):**

```bash
# Verify Redis responds on confirmed host port 6380:
redis-cli -h 127.0.0.1 -p 6380 ping
# Expected: PONG

# Verify Redis registry service count:
python3 -c "
import redis
r = redis.Redis(host='127.0.0.1', port=6380)
keys = r.keys('service:*')
print(f'Registered services: {len(keys)}')
"
# Expected: 83 as of April 6, 2026
```

---

## 33.12 Implementation Status (★★★ April 6, 2026)

| Feature | Status | Notes |
|:--|:--|:--|
| 21-model ensemble sequential dispatch | ✅ Production | ★★★ 22 proxies / 21 active, 83/83 Up |
| Judge pipeline compose-managed | ✅ Production | March 18, 2026; ★★★ confirmed Up April 6 |
| Real judge source files | ✅ Production | March 21, 2026 ghost file remediation |
| Correct sub-judge ports (7230–7233) | ✅ Production | March 21, 2026 |
| Live BBB `bbb_check_verdict` | ✅ Production | March 21, 2026 (not stub) |
| Phase 3.75 → 3.5 merge | ✅ Production | March 18, 2026; confirmed no regression |
| Duplicate LM Synthesizer removal | ✅ Production | March 22, 2026 |
| GPU inference (RTX 4070) | ✅ Production | March 22, 2026; 99–107s end-to-end |
| Identity guard (3 layers) | ✅ Production | March 22, 2026; ★★★ re-confirmed April 6 |
| `cleanResponseForDisplay` fix | ✅ Production | Commit 40-B fix 4; ★★★ re-confirmed April 6 |
| AU-02 Developer Impersonation Guard | ✅ Production | March 25, 2026; ★★★ re-confirmed April 6 |
| Phase 1.45 community memory injection | ✅ Production | ★★ Fully restored April 1; ★★★ confirmed April 6 |
| LEARN-01 float32 dtype fix | ✅ Production | ★★ Resolved April 1, 2026 |
| LEARN-02 GBIM router payload fix | ✅ Production | ★★ Resolved April 1, 2026 — GBIM entity lifecycle restored |
| LEARN-02 backfill of affected-window records | 🔲 Pending | Backfill not yet executed as of April 6, 2026. See §33.6 addendum — backfill script provided. |
| LEARN-03 crash-loop recovery | ✅ Production | ★★ Resolved April 1, 2026 — confirmed stable April 6 |
| All services `127.0.0.1` bound | ✅ Production | ★★★ 83/83 containers, zero `0.0.0.0` exposures |
| `jarvis-memory:8056` durable BBB audit trail | ✅ Production | ★ Secured March 28; ★★★ confirmed active April 6 |
| `msjarvis:5433` `confidence_decay` metadata | ✅ Production | ★ Restored March 28 — 5,416,521 GBIM entities |
| ChromaDB full audit | ✅ Production | ★ 40 collections / 6,675,442 vectors March 28 |
| `heuristic_contradiction_v1` truth verification | ✅ Production (v1) | Partially implemented — see §33.4 |
| `rag_grounded_v2` truth verification | 🔲 Planned | DGM-governed upgrade path ready (Chapter 32); OI-23 Open |
| `llm_judge_v3` truth verification | 🔲 Planned | Future — full LLM reasoning over claim + evidence |

---

## 33.13 Sprint Validation Log

*(March 22–25, 2026 sprint · ★ March 28, 2026 re-confirmation · ★★ April 1, 2026 LEARN-series resolution · ★★★ April 6, 2026 closing health sweep)*

| Item | Sprint Validation | ★ March 28 | ★★ April 1 | ★★★ April 6 |
|:--|:--|:--|:--|:--|
| Container count | ✅ 96/96 Up (March 22) | ★ 96/96 Up | ★★ 96/96 Up post-LEARN-03 | ★★★ **83/83 Up** — count corrected; see §33.14 |
| GPU active, RTX 4070 | ✅ 99.6s, 105.9s, 106.5s | ★ 96/96 Up | ★★ Up | ★★★ Up |
| Phase 3.75 → 3.5 merge complete | ✅ No regression | ★ `jarvis-lm-synthesizer:8001` Up | ★★ Up | ★★★ Up |
| Identity guard Layer 1–3 stable | ✅ No model name leakage | ★ Up | ★★ Up | ★★★ Confirmed |
| `cleanResponseForDisplay` fix held | ✅ No "As LLaMA" artifacts | ★ Regression test passes | ★★ Confirmed | ★★★ Confirmed |
| AU-02 Developer Impersonation Guard | ✅ Active | ★ `jarvis-judge-alignment:7232` Up | ★★ Up | ★★★ Up |
| No duplicate LM Synthesizer call | ✅ `judge_pipeline.py` grep empty | ★ Confirmed | ★★ Confirmed | ★★★ Confirmed |
| BBB `bbb_check_verdict` live (not stub) | ✅ `bbb_checked: true` in responses | ★ BBB:8016 Up | ★★ Up | ★★★ Up |
| All judge ports 7230–7233 correct | ✅ grep confirmed | ★ All 5 Up | ★★ Up | ★★★ Up |
| All services `127.0.0.1` bound | ✅ Zero `0.0.0.0` | ★ 96/96 zero exposed | ★★ 96/96 zero exposed | ★★★ **83/83** zero exposed |
| `jarvis-memory:8056` durable audit trail | — | ★ Secured March 28 | ★★ Active | ★★★ Active |
| `msjarvis:5433` `confidence_decay` | — | ★ Restored March 28 | ★★ Active | ★★★ Active |
| ChromaDB 40 collections / 6,675,442 vectors | — | ★ Full audit confirmed | ★★ Confirmed | ★★★ Confirmed |
| `psychological_rag` 968 docs | — | ★ Restored March 28 | ★★ Confirmed | ★★★ Confirmed |
| LLM ensemble 22 proxies / 21 active | ✅ March 22 | ★ Confirmed March 28 | ★★ Confirmed post-LEARN-03 | ★★★ Confirmed |
| Redis registry healthy | — | — | ★★ Active | ★★★ **83 registered / 83 healthy** — April 6 sweep |
| LEARN-01 float32 dtype fix | — | — | ★★ **Resolved April 1** | ★★★ Confirmed stable |
| LEARN-02 GBIM router HTTP 422 fix | — | — | ★★ **Resolved April 1** | ★★★ Confirmed stable |
| LEARN-02 backfill of affected records | — | — | 🔲 Pending | 🔲 **Not yet executed as of April 6, 2026** |
| LEARN-03 crash-loop recovery | — | — | ★★ **Resolved April 1** | ★★★ Confirmed stable |
| `autonomous_learner` container Up | — | ★ ~23,961+ records (March 28) | ★★ Fully restored | ★★★ Confirmed Up — run §33.3 query for live count |

---

## 33.14 April 6, 2026 Closing State

**★★★ April 6, 2026 — Chapter 33 Closing Health Snapshot**

| Item | Status | Detail |
|:--|:--|:--|
| Services healthy | ★★★ **83/83** | Redis registry confirmed 83 registered / 83 healthy via Python health sweep, April 6, 2026 |
| Container count delta | ⚠️ **Unexplained delta** | Prior stamp read 96/96; tonight's sweep confirms 83/83. A reduction of 13 containers. Cause not yet determined — may reflect compose reorganization, container consolidation, retired services, or a prior overcounting. **This delta requires investigation before the chapter is formally closed.** |
| Redis registry | ✅ Confirmed | 83 registered / 83 healthy — port 6380 verified |
| LEARN-01 | ✅ Resolved and stable | No recurrence since April 1, 2026 |
| LEARN-02 | ✅ Resolved and stable | GBIM entity lifecycle confirmed operating correctly |
| LEARN-02 backfill | 🔲 Not yet executed | One-time backfill script documented in §33.6 addendum — has not been run as of April 6, 2026 |
| LEARN-03 | ✅ Resolved and stable | `jarvis-autonomous-learner` Up with zero restarts |
| New anomalies | ✅ None detected | No new issues identified in April 6 health sweep beyond the container count delta |
| All services `127.0.0.1` | ✅ Confirmed | Zero `0.0.0.0` exposures in 83/83 count |

**Chapter close status: DRAFT CLOSED — PENDING CONTENT IMPORT**

The following sections are blocking gaps that must be filled before this chapter is published as final:

| Section | Issue Reference | Content Required |
|:--|:--|:--|
| §33.2 | CH33-PENDING-002 | Judge services full remediation record (March 18/21, 2026) + §33.2.3 `heuristic_contradiction_v1` limitations |
| §33.4 | CH33-PENDING-004 | Judge evaluation criteria, scoring rubrics, weighting logic |
| §33.5 | CH33-PENDING-005 | Phase 3.5 full text: §33.5.1 identity guard, §33.5.2 `cleanResponseForDisplay`, §33.5.3 AU-02 |
| §33.6 core | CH33-PENDING-006 | Core ensemble pattern text (addendum already present — preserve on import) |
| §33.7 table | CH33-PENDING-007 | Full phase-by-phase timing table rows (Phase 1.45 narrative paragraph already updated) |
| §33.8 | CH33-PENDING-008 | Use in Live Cycles full text |
| §33.9 | CH33-PENDING-009 | Consensus Mechanisms full text |
| §33.10 | CH33-PENDING-010 | DGM Layer integration full text |

All structural edits, count corrections, LEARN-series documentation, and close-out additions are complete. The chapter is coherent and accurate as written. Import of the eight pending sections from the March 28 source document is the sole remaining action to reach FINAL status.

---

## Appendix A: Change Record

*(Consolidated operational change history for Chapter 33.)*

**★★★ April 6, 2026 —** 83/83 containers Up confirmed via Redis registry health sweep. Container count corrected throughout from prior 96/96 stamp (delta of 13 — cause under investigation; see §33.14). §33.13 April 6 column added. §33.14 closing state section added. §33.12 LEARN-02 backfill row annotated "not yet executed as of April 6." Redis port 6380 health verification script added to §33.11. Annotation tier ★★★ established throughout.

**★★ April 1, 2026 —** 96/96 containers Up. LEARN-01 (numpy float32 dtype), LEARN-02 (GBIM router HTTP 422), LEARN-03 (crash-loop recovery) all resolved. §33.0 LEARN-series block added. §33.3 count note aligned. §33.6 backfill addendum added. §33.7 Phase 1.45 row updated. §§33.11–33.13 updated throughout.

**★ March 28, 2026 —** `jarvis-memory:8056` secured (durable BBB audit trail). `msjarvis:5433` restored (5,416,521 GBIM entities with `confidence_decay` metadata). `msjarvisgis:5432` confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids). ChromaDB full audit (40 active collections / 6,675,442 total vectors). LLM ensemble confirmed 22 proxies / 21 active. `autonomous_learner` confirmed ~23,961+ records.

**March 27, 2026 —** `autonomous_learner` count note updated. Phase 1.45 AaaCPE cross-reference added. §33.2.3 DGM upgrade note added. §33.11 cross-reference to Chapter 34 added.

**March 22–25, 2026 sprint —** LM Synthesizer identity guard confirmed stable. `cleanResponseForDisplay` regression fix confirmed held. AU-02 Developer Impersonation Guard confirmed active. Phase 3.75 → Phase 3.5 merge confirmed no regression.

**March 22, 2026 —** ChromaDB host port corrected to 8002. Redis host port corrected to 6380. Duplicate LM Synthesizer call removed from `judge_pipeline.py`. GPU inference (RTX 4070) activated; verified end-to-end 99–107s.

**March 21, 2026 —** Real judge source files restored. Ghost `lm_synthesizer.py` clones removed. Sub-judge ports corrected from all-7239 to assigned ports 7230–7233. `bbb_check_verdict` stub replaced with live async httpx call.

**March 18, 2026 —** Judge pipeline brought under compose management with `restart: unless-stopped`. Phase 3.75 eliminated and merged into Phase 3.5 — single `jarvis-ollama:11434/api/generate` call, saves ~40s per query.

**March 16, 2026 —** Judge pipeline now evaluates consensus answer only — raw_responses dump no longer sent to judges, reducing judge pipeline time from ~85–100s to ~6–8s (GPU).

---

*Last updated: ★★★ 2026-04-06 — Carrie Kidd (Mamma Kidd), Mount Hope, WV*
