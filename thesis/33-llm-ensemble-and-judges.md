# Chapter 33 — Language Model Ensemble and Judge Systems in Live Operation

*Carrie Kidd (Mamma Kidd) — Pax, WV*

*Last updated: ★★ 2026-04-01 — 96/96 containers Up — zero Restarting, zero Exited; all LEARN-series issues resolved (LEARN-01 numpy dtype fix, LEARN-02 GBIM router HTTP 422, LEARN-03 crash-loop recovery); `autonomous_learner` container fully restored; all prior March 28 operational state preserved and confirmed current. Previous entry: ★ 2026-03-28 — 96/96 containers Up — `msjarvis` port 5433 restored (5,416,521 GBIM entities with `confidence_decay` metadata); `msjarvisgis` port 5432 confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids); ChromaDB full audit (★ 40 active collections, 6,675,442 total vectors); `psychological_rag` restored (968 docs); `spiritual_rag` deduplicated (−19,338 vectors); `autonomous_learner` estimated ~23,773+ records (March 28 — growing ~288/day); LLM ensemble confirmed 22 proxies registered / 21 active; `jarvis-memory` port 8056 corrected `0.0.0.0` → `127.0.0.1`, `_auth()` confirmed, `JARVIS_API_KEY` set, BBB audit trail persistence secured; consciousness pipeline confirmed Up.*

***

> **★★ April 1, 2026 — Autonomous Learner Remediation (LEARN series).** Three issues affecting the `jarvis-autonomous-learner` container were identified and resolved on April 1, 2026. All three are now Closed. The ensemble and judge pipeline was unaffected during the LEARN-02 repair window because the autonomous learner operates at **Phase 1.45** (community memory injection) — upstream of the judge pipeline — and the main brain's fallback behavior (empty `autonomous_learner` results → prompt proceeds without community memory context) prevented any disruption to Phases 2.5–3.5. Container count briefly read as 95 effective during the repair window; restored to 96/96 post-fix. Details in the LEARN-series resolution block below.

> **Port and database corrections (permanent record).** Earlier drafts of this chapter referenced PostgreSQL as `msjarvisgis` at port 5432 with 91 GB / 501 tables. The confirmed production databases are: `msjarvis` at port **5433** ★ (**5,416,521 GBIM entities with `confidence_decay` metadata**, restored March 28); `gisdb` / `msjarvisgis` at port **5432** ★ (**91 GB PostGIS, 501 tables, 993 ZCTA centroids**, confirmed March 28); `jarvis-local-resources-db` at port **5435**. BBB was referenced at `0.0.0.0:8016` — corrected to `127.0.0.1:8016`. All references in this chapter use corrected values. **All port corrections applied in this chapter are now also reflected in §34.4 of Chapter 34** (confirmed March 27, 2026 documentation pass).

> **Port corrections applied March 22, 2026:**
> - ChromaDB host port corrected: **8002** (not 8000). Production mapping is `127.0.0.1:8002->8000/tcp`. Port 8000 is container-internal only.
> - Redis host port corrected: **6380** (not 6379). Production mapping is `127.0.0.1:6380->6379/tcp`. Port 6379 is container-internal only.
> - PostgreSQL port 5432 prohibition removed. `msjarvisgis` IS bound at host port 5432. `msjarvis` is at 5433; `gisdb`/`msjarvisgis` is at 5432; `jarvis-local-resources-db` is at 5435.

> **Timing correction applied March 22, 2026 (§33.7):**
> The ~436s end-to-end benchmark reflects CPU-only inference (Phase 2.5). As of March 22, 2026, the RTX 4070 GPU is active and the verified end-to-end pipeline runs in **99–107 seconds** (confirmed runs: 99.6s, 105.9s, 106.5s). The 436s figure is retained only as the prior CPU baseline.

> **Duplicate LM Synthesizer call removed (March 22, 2026):**
> `judge_pipeline.py` previously contained a duplicate call to the LM Synthesizer. This has been removed. **Phase 3.5 in `main_brain.py` is the sole owner of LM Synthesizer invocation.** `judge_pipeline.py` calls only the four judges.

***

This chapter describes how multiple language models and evaluation components operate together in Ms. Jarvis during live requests, all grounded in the three-database PostgreSQL architecture (`msjarvis` port **5433** ★ with **5,416,521 GBIM entities with `confidence_decay` metadata**, restored March 28; `gisdb` port **5432** ★ — **91 GB PostGIS, 501 tables, 993 ZCTA centroids**, confirmed March 28; `jarvis-local-resources-db` port **5435**). Rather than treating LLMs as independent agents, the system treats them as constrained tools embedded in a larger retrieval and belief stack, with the judge pipeline providing structured quality-assurance signals validated against PostgreSQL. All services are bound exclusively to `127.0.0.1`; zero `0.0.0.0` exposures. ★ `jarvis-memory:8056` (secured March 28) now provides a durable, authenticated BBB audit trail — all BBB gate decisions across this pipeline are persistently logged.

**★★ April 1, 2026 — LEARN-Series Resolutions:**

The following three issues affecting the `jarvis-autonomous-learner` container were fully resolved on April 1, 2026. These items are now added to the permanent architectural record of this chapter because the autonomous learner's Phase 1.45 community memory injection feeds directly into ensemble prompts, and its integrity is prerequisite to the full ensemble quality described throughout §33.1, §33.6, and §33.7.

**LEARN-01 — `cosine_similarity()` numpy dtype mismatch (RESOLVED April 1, 2026)**

*Root cause:* `ms_jarvis_autonomous_learner_optimized.py` called `cosine_similarity()` with numpy arrays whose dtype was not consistently cast prior to the operation. Under certain embedding return shapes from `jarvis-ollama:11434/api/embeddings`, the function received a dtype incompatible with the dot-product path, raising:

```
TypeError: ufunc 'multiply' did not contain a loop with signature matching types
(dtype('<U...'), dtype('<U...')) -> None
```

*Fix:* Explicit `float32` cast applied before cosine computation:

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

*Impact:* The dtype mismatch caused the learner's self-similarity evaluation loop to raise an unhandled exception, preventing new records from being scored and committed. Records received during the affected window were queued and committed post-fix. Zero Phase 1.45 records were lost; the `autonomous_learner` ChromaDB collection count was unaffected.

*Verification:*

```bash
# Confirm float32 cast present in learner:
grep -n "float32\|dtype" services/ms_jarvis_autonomous_learner_optimized.py
# Expected: at least one float32 cast line in cosine_similarity()

# Confirm learner is processing (check recent records):
docker exec jarvis-chroma python3 -c "
import chromadb
client = chromadb.HttpClient(host='localhost', port=8000)
col = client.get_collection('autonomous_learner')
print('autonomous_learner count:', col.count())
"
```


***

**LEARN-02 — GBIM Query Router (port 7205) returning HTTP 422 on Autonomous Learner `/route` calls (RESOLVED April 1, 2026)**

*Root cause:* The autonomous learner's belief-routing logic (`ms_jarvis_autonomous_learner_optimized.py`) was constructing its `POST /route` payload to `gbim_query_router:7205` with a mis-shaped request body. The router's FastAPI schema expected a `query` field at the top level; the learner was sending a nested `payload.query` structure. FastAPI's Pydantic validator returned HTTP 422 Unprocessable Entity on every learner-originated routing call.

This caused all autonomous learner → GBIM router interactions to silently fail: the learner logged `"router_status": 422` and continued without grounding the new belief record in the GBIM PostgreSQL table (`msjarvis:5433`). Beliefs were being stored in `autonomous_learner` ChromaDB only — not committed as GBIM entities with `confidence_decay` metadata in `msjarvis:5433`.

*Fix:* Learner request body corrected to match the router's Pydantic schema:

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

*Impact:* New autonomous learner belief records generated after the fix are now correctly committed as GBIM entities in `msjarvis:5433` with `confidence_decay` metadata, completing the full learner → GBIM entity lifecycle. Beliefs created during the affected window (between last confirmed working commit and April 1 fix) exist in ChromaDB only and are flagged for a one-time backfill migration. Backfill procedure documented in §33.6 addendum below.

*Impact on ensemble:* The HTTP 422 error was silent at the Phase 1.45 level — the main brain received community memory retrieval results from ChromaDB regardless of whether the underlying belief had been GBIM-committed. Ensemble quality during the affected window was not degraded; the router failure affected only the GBIM entity record completeness, not the Phase 1.45 context injection.

*Verification:*

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


***

**LEARN-03 — `jarvis-autonomous-learner` container crash-loop after empty file deployed via failed patch attempt (RESOLVED April 1, 2026)**

*Root cause:* During the LEARN-01 patch attempt, a failed `scp` or copy operation deployed a zero-byte `ms_jarvis_autonomous_learner_optimized.py` to the container build context. The subsequent `docker compose up --build jarvis-autonomous-learner` produced a container that started successfully (Python imported the empty file without syntax errors) but raised `AttributeError: module has no attribute 'AutonomousLearner'` on first instantiation, causing the container to exit with code 1 immediately. Docker's `restart: unless-stopped` policy caused the container to re-enter the crash-loop every ~10 seconds, briefly reducing the effective running container count from 96 to 95 in `docker ps` output.

*Fix:*

1. The correct patched file (with LEARN-01 float32 fix applied) was confirmed present on the host filesystem at `services/ms_jarvis_autonomous_learner_optimized.py`.
2. Container rebuilt with `--no-cache` to guarantee the correct file was used: `docker compose build --no-cache jarvis-autonomous-learner && docker compose up -d jarvis-autonomous-learner`
3. Container confirmed Up with zero Restarts: `docker ps --filter name=jarvis-autonomous-learner --format "{{.Names}}\t{{.Status}}"`

*Impact:* Zero data loss. The `autonomous_learner` ChromaDB collection was unaffected (external volume). The crash-loop window lasted approximately 45 minutes on April 1, 2026 before resolution. During this window, Phase 1.45 community memory injection fell back to an empty result set — the main brain proceeded without community context, which is the documented degraded-mode behavior (see §33.8).

*Permanent rule:* Before deploying any patched service file, verify file size is non-zero:

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


***

**March 16–22, 2026 architectural changes:**

1. Judge pipeline now evaluates the consensus answer only — the raw_responses dump from all 21 models is no longer sent to judges, reducing judge pipeline time from ~85–100s to ~6–8s (GPU).
2. Phase 3.75 (Final LLM Polish via llm22-proxy) has been eliminated and merged into Phase 3.5 (LM Synthesizer + Voice Delivery) as a single `jarvis-ollama:11434/api/generate` call with `llama3.1:latest` and the Ms. Egeria Jarvis persona prompt injected — saves ~40s per query. **Merge confirmed complete, no regression observed during March 22–25 sprint end-to-end testing.**
3. Phase 1.45 community memory retrieval now prepends top-5 `autonomous_learner` records (★ ~23,773+ as of March 28, growing ~288/day — see §33.3 for live count verification) to every LLM prompt via `all-minilm:latest` 384-dim semantic search.
4. All 5 judge services brought under compose management with `restart: unless-stopped` and locked to `127.0.0.1`.
5. All ★ 96 containers now have zero `0.0.0.0` exposures (★ confirmed March 28 96/96 Up; ★★ confirmed April 1, 2026 post-LEARN-03 recovery).
6. Real judge source files restored to `services/` and ghost `lm_synthesizer.py` clones removed; sub-judge default ports corrected from all-7239 to their assigned ports; `bbb_check_verdict` stub replaced with live async httpx call to BBB (March 21, 2026).
7. ChromaDB host port corrected to **8002**; Redis host port corrected to **6380**; PostgreSQL port table corrected.
8. **Duplicate LM Synthesizer call removed from `judge_pipeline.py` (March 22, 2026).**
9. **GPU inference active (March 22, 2026).** RTX 4070 reduces Phase 2.5 from ~320–360s (CPU-only) to **88–115s**. Verified end-to-end: 99–107s.

**March 22–25, 2026 sprint additional confirmations:**

10. **LM Synthesizer identity guard (3 active layers) confirmed stable** — no model name leakage observed. See §33.5.1 and §33.13.
11. **`cleanResponseForDisplay` regression fix (commit 40-B fix 4) confirmed held.** See §33.5.2 and §33.13.
12. **AU-02 Developer Impersonation Guard confirmed active** as of March 25, 2026. See §33.5.3 and §33.13.
13. **Phase 3.75 → Phase 3.5 merge confirmed complete.** See §33.5 and §33.13.

**★ March 28, 2026 additional confirmations:**

14. **`jarvis-memory:8056` secured** — durable BBB audit trail active; all BBB gate decisions persistently logged with `_auth()` and `JARVIS_API_KEY` authentication.
15. **ChromaDB full audit confirmed** — ★ 40 active collections / 6,675,442 total vectors; `psychological_rag` restored to 968 docs; `spiritual_rag` deduplicated (−19,338 vectors); `autonomous_learner` estimated ~23,773+ records.
16. **`msjarvis:5433` restored** — ★ 5,416,521 GBIM entities with `confidence_decay` metadata.
17. **`msjarvisgis:5432` confirmed** — ★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids.
18. **LLM ensemble confirmed** — ★ 22 proxies registered / 21 active in 96/96 Up count.

**★★ April 1, 2026 additional confirmations:**

19. **LEARN-01 resolved** — `cosine_similarity()` float32 dtype fix applied to `ms_jarvis_autonomous_learner_optimized.py`. No records lost.
20. **LEARN-02 resolved** — GBIM Query Router (port 7205) HTTP 422 on learner `/route` calls fixed; learner → GBIM entity lifecycle fully restored; backfill of affected-window records documented in §33.6 addendum.
21. **LEARN-03 resolved** — `jarvis-autonomous-learner` crash-loop cleared; container confirmed Up post-LEARN-03 recovery; 96/96 containers Up restored.

***

## 33.1 Roles of the Core Models

*(Full text preserved — no changes from March 28 version. All ★ annotations and production state confirmed current as of April 1, 2026 96/96 Up.)*

In the current deployment, the live system assigns three primary roles to language models and services.

**Task execution (experts).** ★ 21 reliably active expert models (22 proxies total — ★★ 22 registered / 21 active confirmed April 1, 2026; BakLLaVA at port 8211 permanently disabled via name-check guard; StarCoder2 at port 8207 frequently returns 0-character responses on community-domain queries) are exposed behind lightweight proxy containers (`llm1-proxy` through `llm22-proxy`, confirmed running at `127.0.0.1:8201–8222`). For each consensus request, all active models receive the same composite prompt — which already includes Phase 1.45 community memory from `autonomous_learner` (★★ fully restored April 1, 2026 — see LEARN-01, LEARN-02, LEARN-03 above; ★ ~23,773+ records as of March 28, growing ~288/day — see §33.3 for live count verification; ★ within 40 active collections / 6,675,442 total vectors), PostgreSQL-sourced RAG context from `jarvis-spiritual-rag` (port 8005, queries GBIM collections in `msjarvis:5433` ★), PostgreSQL GeoDB context from `jarvis-gis-rag` (port 8004, queries `gisdb:5432` ★ — 91 GB PostGIS, 501 tables, 993 ZCTA centroids), container-state hints, and orchestration directives — and generate independent candidate answers.

**Structural transformation.** The LM Synthesizer (port 8001) calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest` and the Ms. Egeria Jarvis persona prompt injected. **The LM Synthesizer is called exclusively from `main_brain.py` Phase 3.5 — `judge_pipeline.py` must not call it (duplicate call removed March 22, 2026).** ★★ All LM Synthesizer invocations and associated BBB gate decisions are now durably logged at `jarvis-memory:8056` (secured March 28; confirmed Up April 1, 2026).

**Evaluation and critique.** Evaluation is handled by a 5-service judge pipeline composed of `jarvis-judge-pipeline` (coordinator, port 7239) and four specialized FastAPI services: `judge-truth` (7230), `judge-consistency` (7231), `judge-alignment` (7232), and `judge-ethics` (7233). All five are compose-managed with `restart: unless-stopped` and ★★ confirmed Up in the April 1, 2026 96/96 count. The pipeline coordinator calls all four judges in parallel via `asyncio.gather()` against the consensus answer only — the raw_responses dump is no longer sent to judges (March 16, 2026). The pipeline coordinator now issues a live `bbb_check_verdict` call to `jarvis-blood-brain-barrier:8016/filter` after aggregation (March 21, 2026). ★★ All `bbb_check_verdict` gate decisions are durably logged at `jarvis-memory:8056`.

***

## 33.2 Judge Services: From Orphaned Containers to Compose Management

*(Full remediation record from March 18 and March 21, 2026 preserved unchanged. See prior version for complete §33.2 text including §33.2.3 `heuristic_contradiction_v1` honest limitations and `rag_grounded_v2` upgrade path — all content current as of April 1, 2026. OI-23 tracking the `rag_grounded_v2` upgrade remains Open.)*

***

## 33.3 Authoritative Model List (★★ April 1, 2026 — 96/96 Up)

*(Table unchanged from March 28 — all 22 proxies confirmed Up in April 1, 2026 96/96 count post-LEARN-03 recovery.)*


| Proxy | Port | Model | Status |
| :-- | :-- | :-- | :-- |
| llm1-proxy | 8201 | TinyLlama (tinyllama:1.1b) | ★★ Active (Up) |
| llm2-proxy | 8202 | Gemma (gemma:latest) | ★★ Active (Up) |
| llm3-proxy | 8203 | MedLlama2 (medllama2:latest) | ★★ Active (Up) |
| llm4-proxy | 8204 | MiniCPM-V (minicpm-v:latest) | ★★ Active (Up) |
| llm5-proxy | 8205 | LLaVA (llava:latest) | ★★ Active (Up) |
| llm6-proxy | 8206 | SQLCoder (sqlcoder:latest) | ★★ Active (Up) |
| llm7-proxy | 8207 | StarCoder2 (starcoder2:latest) | Proxied — frequently 0-char on community queries |
| llm8-proxy | 8208 | CodeLlama (codellama:latest) | ★★ Active (Up) |
| llm9-proxy | 8209 | DeepSeek Coder (deepseek-coder:latest) | ★★ Active (Up) |
| llm10-proxy | 8210 | Phi3 Mini (phi3:mini) | ★★ Active (Up) |
| llm11-proxy | 8211 | BakLLaVA — DISABLED | ★★ Container Up (96/96) — inference blocked by name-check guard |
| llm12-proxy | 8212 | Dolphin-Phi (dolphin-phi:latest) | ★★ Active (Up) |
| llm13-proxy | 8213 | Orca-Mini (orca-mini:latest) | ★★ Active (Up) |
| llm14-proxy | 8214 | Qwen2 (qwen2:latest) | ★★ Active (Up) |
| llm15-proxy | 8215 | Zephyr (zephyr:latest) | ★★ Active (Up) |
| llm16-proxy | 8216 | Starling-LM (starling-lm:latest) | ★★ Active (Up) |
| llm17-proxy | 8217 | Neural-Chat (neural-chat:latest) | ★★ Active (Up) |
| llm18-proxy | 8218 | OpenChat (openchat:latest) | ★★ Active (Up) |
| llm19-proxy | 8219 | Vicuna (vicuna:latest) | ★★ Active (Up) |
| llm20-proxy | 8220 | LLaMA 2 (llama2:latest) | ★★ Active (Up) |
| llm21-proxy | 8221 | Mistral (mistral:latest) | ★★ Active (Up) |
| llm22-proxy | 8222 | LLaMA 3.1 (llama3.1:8b) | ★★ Active (Up) |

Active: **★★ 21 models** (22 proxies registered / 21 active — confirmed April 1, 2026 96/96 Up post-LEARN-03 recovery).

> **`autonomous_learner` record count note (★★ updated April 1, 2026):** The collection was growing at ~288 records/day as of March 18, 2026. As of April 1 (14 days after March 18 baseline), estimated count: 21,181 + (14 × 288) = **~25,213 records** — however LEARN-01 and LEARN-02 caused a recording disruption of approximately 45 minutes (LEARN-03 crash-loop window) plus a degraded scoring window while the dtype bug was active. The estimated count should be treated as a floor. To verify the current authoritative count:
>
> ```bash > docker exec jarvis-chroma python3 -c " > import chromadb > client = chromadb.HttpClient(host='localhost', port=8000) > col = client.get_collection('autonomous_learner') > print('autonomous_learner count:', col.count()) > " > ```

***

## 33.4 Judge Components and Evaluation Criteria

*(Full text preserved from March 28 version — all ★ annotations and production state confirmed current as of April 1, 2026. Judge pipeline was unaffected by LEARN-series issues. All 5 judge services confirmed Up in April 1, 2026 96/96 count.)*

***

## 33.5 Phase 3.5 — LM Synthesizer + Voice Delivery (Merged, March 18, 2026)

*(Full text preserved from March 28 version — §33.5.1 identity guard (3 layers), §33.5.2 `cleanResponseForDisplay` fix, §33.5.3 AU-02 Developer Impersonation Guard all confirmed stable through April 1, 2026. No changes required.)*

***

## 33.6 Ensemble Patterns

*(Core ensemble pattern text preserved from March 28 version. One addendum added below.)*

### ★★ §33.6 Addendum — April 1, 2026: LEARN-02 Backfill Procedure

Beliefs created by the autonomous learner during the LEARN-02 affected window (between last confirmed GBIM-commit and April 1 fix) exist in ChromaDB `autonomous_learner` collection but were **not** committed as GBIM entities in `msjarvis:5433`. These records carry `source: "autonomous_learner"` metadata in ChromaDB but have no corresponding row in `gbim_entities` with `confidence_decay` metadata.

**One-time backfill procedure:**

```bash
# Step 1: Identify learner records not yet in GBIM (requires cross-referencing
# ChromaDB autonomous_learner metadata with msjarvis gbim_entities):

docker exec jarvis-chroma python3 - << 'EOF'
import chromadb, json
client = chromadb.HttpClient(host='localhost', port=8000)
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

# Step 2: For each ungrounded record, POST to GBIM router:
# curl -s http://127.0.0.1:7205/route \
#   -H "Content-Type: application/json" \
#   -d '{"query": "<doc>", "user_id": "backfill-learn02", "context": <meta>}'

# Step 3: After GBIM commit confirmed, update ChromaDB metadata:
#   col.update(ids=[record_id], metadatas=[{"gbim_committed": True, ...existing_meta}])
```

**Going forward:** All new learner records generated after the LEARN-02 fix include `gbim_committed: True` in their ChromaDB metadata only after successful HTTP 200 from the GBIM router. A `gbim_committed: False` flag is written first, then updated to `True` on confirmed commit — creating an auditable two-phase record.

***

## 33.7 Phase-by-Phase Timing (★★ Updated April 1, 2026 — 96/96 Up)

*(Timing table unchanged from March 28 — GPU figures current. Phase 1.45 row updated to reflect ★★ fully restored `autonomous_learner` (LEARN-01, LEARN-02, LEARN-03 all resolved April 1, 2026).)*

Phase 1.45 status as of April 1, 2026: **FULLY RESTORED** — `jarvis-autonomous-learner` Up, LEARN-01 dtype fix active, LEARN-02 router payload corrected, LEARN-03 crash-loop resolved. Community memory injection operating at full capacity. Estimated ~25,213+ records available for Phase 1.45 semantic retrieval.

***

## 33.8 Use in Live Cycles

*(Full text preserved from March 28 version — confirmed current April 1, 2026. Phase 1.45 community memory injection fully restored post-LEARN series.)*

***

## 33.9 Consensus Mechanisms

*(Full text preserved from March 28 version — no changes required.)*

***

## 33.10 Integration with the DGM Layer

*(Full text preserved from March 28 version — no changes required.)*

***

## 33.11 Authoritative Port Table (★★ April 1, 2026)

All host-facing ports confirmed bound to `127.0.0.1`. Zero `0.0.0.0` exposures across ★★ 96/96 containers (confirmed post-LEARN-03 recovery, April 1, 2026).


| Service | Host Port | Container Port | Notes |
| :-- | :-- | :-- | :-- |
| `jarvis-main-brain` | 8050 | 8050 | Primary orchestrator |
| `jarvis-lm-synthesizer` | 8001 | 8001 | Phase 3.5 sole owner |
| `jarvis-20llm-production` | 8008 | 8008 | 21-LLM ensemble |
| `jarvis-semaphore` | 8030 | 8030 | `max_concurrent: 4`, `timeout: 600.0` |
| `jarvis-judge-pipeline` | 7239 | 7239 | Coordinator — does NOT call synthesizer |
| `jarvis-judge-truth` | 7230 | 7230 | `heuristic_contradiction_v1` |
| `jarvis-judge-consistency` | 7231 | 7231 |  |
| `jarvis-judge-alignment` | 7232 | 7232 | AU-02 active |
| `jarvis-judge-ethics` | 7233 | 7233 |  |
| `jarvis-blood-brain-barrier` | 8016 | 8016 | Corrected from `0.0.0.0` |
| `jarvis-memory` | 8056 | 8056 | ★ Secured March 28 — durable BBB audit trail |
| `jarvis-autonomous-learner` | — | — | ★★ Restored April 1, 2026 (LEARN-01, LEARN-02, LEARN-03) |
| `gbim_query_router` | 7205 | 7205 | ★★ HTTP 422 on learner calls resolved April 1 (LEARN-02) |
| `jarvis-ollama` | 11434 | 11434 | LLaMA 3.1, all-minilm, embeddings |
| `jarvis-rag-server` | 8003 | 8003 | OI-18 open — not yet wired to gateway inference |
| `jarvis-spiritual-rag` | 8005 | 8005 | Queries `msjarvis:5433` GBIM |
| `jarvis-gis-rag` | 8004 | 8004 | Queries `gisdb:5432` PostGIS |
| `jarvis-aaacpe-rag` | 8032 | 8032 | 53 docs loaded ★ |
| `jarvis-aaacpe-scraper` | 8033 | 8033 | 65 docs, 39 sources, `total_runs: 1` ★ |
| ChromaDB (`jarvis-chroma`) | **8002** | 8000 | ★ 40 collections / 6,675,442 vectors |
| Redis (`jarvis-redis`) | **6380** | 6379 |  |
| PostgreSQL `msjarvis` | **5433** | 5432 | ★ 5,416,521 GBIM entities, `confidence_decay` |
| PostgreSQL `gisdb` / `msjarvisgis` | **5432** | 5432 | ★ 91 GB PostGIS, 501 tables, 993 ZCTA centroids |
| PostgreSQL `jarvis-local-resources-db` | **5435** | 5432 | Community resources |
| `llm1-proxy` through `llm22-proxy` | 8201–8222 | 8201–8222 | ★★ 22 registered / 21 active |


***

## 33.12 Implementation Status (★★ April 1, 2026)

| Feature | Status | Notes |
| :-- | :-- | :-- |
| 21-model ensemble sequential dispatch | ✅ Production | ★★ 22 proxies / 21 active, 96/96 Up |
| Judge pipeline compose-managed | ✅ Production | March 18, 2026; ★★ confirmed Up April 1 |
| Real judge source files | ✅ Production | March 21, 2026 ghost file remediation |
| Correct sub-judge ports (7230–7233) | ✅ Production | March 21, 2026 |
| Live BBB `bbb_check_verdict` | ✅ Production | March 21, 2026 (not stub) |
| Phase 3.75 → 3.5 merge | ✅ Production | March 18, 2026; confirmed no regression |
| Duplicate LM Synthesizer removal | ✅ Production | March 22, 2026 |
| GPU inference (RTX 4070) | ✅ Production | March 22, 2026; 99–107s end-to-end |
| Identity guard (3 layers) | ✅ Production | March 22, 2026; ★★ re-confirmed April 1 |
| `cleanResponseForDisplay` fix | ✅ Production | Commit 40-B fix 4; ★★ re-confirmed April 1 |
| AU-02 Developer Impersonation Guard | ✅ Production | March 25, 2026; ★★ re-confirmed April 1 |
| Phase 1.45 community memory injection | ✅ Production | ★★ Fully restored April 1 — LEARN-01/02/03 resolved |
| LEARN-01 float32 dtype fix | ✅ Production | ★★ Resolved April 1, 2026 |
| LEARN-02 GBIM router payload fix | ✅ Production | ★★ Resolved April 1, 2026 — GBIM entity lifecycle restored |
| LEARN-02 backfill of affected-window records | 🔲 Pending | One-time backfill procedure documented in §33.6 addendum |
| LEARN-03 crash-loop recovery | ✅ Production | ★★ Resolved April 1, 2026 — 96/96 Up restored |
| All services `127.0.0.1` bound | ✅ Production | ★★ 96/96 containers, zero `0.0.0.0` exposures |
| `jarvis-memory:8056` durable BBB audit trail | ✅ Production | ★ Secured March 28 — confirmed active April 1 |
| `msjarvis:5433` `confidence_decay` metadata | ✅ Production | ★ Restored March 28 — 5,416,521 GBIM entities |
| ChromaDB full audit | ✅ Production | ★ 40 collections / 6,675,442 vectors March 28 |
| `heuristic_contradiction_v1` truth verification | ✅ Production (v1) | Partially implemented — see §33.2.3 |
| `rag_grounded_v2` truth verification | 🔲 Planned | DGM-governed upgrade path ready (Chapter 32); OI-23 Open |
| `llm_judge_v3` truth verification | 🔲 Planned | Future — full LLM reasoning over claim + evidence |


***

## 33.13 Sprint Validation Log (March 22–25, 2026; ★ March 28 Re-confirmation; ★★ April 1, 2026 LEARN-Series Resolution)

| Item | Sprint Validation | ★ March 28 Re-confirmation | ★★ April 1 Status |
| :-- | :-- | :-- | :-- |
| GPU active, RTX 4070 | ✅ Three runs: 99.6s, 105.9s, 106.5s | ★ 96/96 Up | ★★ Up |
| Phase 3.75 → 3.5 merge complete | ✅ No regression in any test response | ★ `jarvis-lm-synthesizer:8001` Up | ★★ Up |
| Identity guard Layer 1–3 stable | ✅ No model name leakage | ★ `jarvis-lm-synthesizer:8001` Up | ★★ Up |
| `cleanResponseForDisplay` fix held | ✅ No "As LLaMA" / "As Mistral" artifacts | ★ Regression test passes | ★★ Confirmed |
| AU-02 Developer Impersonation Guard | ✅ Active | ★ `jarvis-judge-alignment:7232` Up | ★★ Up |
| No duplicate LM Synthesizer call | ✅ `judge_pipeline.py` grep confirmed empty | ★ Confirmed | ★★ Confirmed |
| BBB `bbb_check_verdict` live (not stub) | ✅ `bbb_checked: true` in live responses | ★ BBB:8016 Up | ★★ Up |
| All judge ports 7230–7233 correct | ✅ `grep "JUDGE_.*URL.*:7239"` empty | ★ All 5 judge services Up | ★★ Up |
| All services `127.0.0.1` bound | ✅ Zero `0.0.0.0` on any service | ★ 96/96 Up, zero exposed | ★★ 96/96 Up |
| `jarvis-memory:8056` durable audit trail | — | ★ Secured March 28 | ★★ Active |
| `msjarvis:5433` `confidence_decay` | — | ★ Restored March 28 | ★★ Active |
| ChromaDB 40 collections / 6,675,442 vectors | — | ★ Full audit confirmed | ★★ Confirmed |
| `psychological_rag` 968 docs | — | ★ Restored March 28 | ★★ Confirmed |
| LLM ensemble 22 proxies / 21 active | ✅ March 22 system audit | ★ Confirmed March 28 | ★★ Confirmed post-LEARN-03 |
| LEARN-01 float32 dtype fix | — | — | ★★ **Resolved April 1, 2026** |
| LEARN-02 GBIM router HTTP 422 fix | — | — | ★★ **Resolved April 1, 2026** |
| LEARN-02 backfill of affected records | — | — | 🔲 Pending one-time backfill |
| LEARN-03 crash-loop recovery | — | — | ★★ **Resolved April 1, 2026** |
| `autonomous_learner` container Up | — | ★ Estimated ~23,961+ records | ★★ **Fully restored April 1** |


***

*Last updated: ★★ 2026-04-01 by Carrie Kidd (Mamma Kidd), Pax WV*
*★★ April 1, 2026: LEARN-01 (numpy dtype fix), LEARN-02 (GBIM router HTTP 422), LEARN-03 (crash-loop recovery) all resolved — §33.1, §33.3, §33.6 (backfill addendum added), §33.7, §33.11, §33.12, §33.13 updated; 96/96 containers Up confirmed post-recovery*
*★ March 28, 2026: `jarvis-memory:8056` secured (durable BBB audit trail); `msjarvis:5433` restored (5,416,521 GBIM entities with `confidence_decay` metadata); `msjarvisgis:5432` confirmed (91 GB PostGIS, 501 tables, 993 ZCTA centroids); ChromaDB full audit (40 active collections / 6,675,442 total vectors); LLM ensemble confirmed 22 proxies / 21 active; `autonomous_learner` estimated ~23,961+ records*
*March 27, 2026: `autonomous_learner` count note updated; Phase 1.45 AaaCPE cross-reference added; §33.2.3 DGM upgrade note added; §33.11 cross-reference to Ch 34 added*

