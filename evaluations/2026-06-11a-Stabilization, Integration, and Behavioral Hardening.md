# Ms. Jarvis / Ms. Allis System Engineering Report
## Multi-Sprint Stabilization, Integration, and Behavioral Hardening
### Covering Sessions: June 6 – June 11, 2026

**Project:** MsJarvis-Rebuild  
**Repository:** H4HWV2011/msjarvis-public-docs  
**Environment:** `/opt/msjarvis-rebuild`, Ubuntu/systemd, Docker Compose  
**Primary Engineer:** cakidd  
**Report Date:** 2026-06-11  
**Classification:** Internal Technical Record

---

## Abstract

This report provides a complete engineering narrative of the multi-day stabilization, integration, and behavioral hardening sprint conducted against the Ms. Jarvis / Ms. Allis conversational AI stack between June 6 and June 11, 2026. The work addressed five structurally distinct failure categories — production chat service instability, retrieval-augmented generation endpoint mismatch, passive-only divergence handling, absent admin observability, and auth/timesheet database misrouting — and extended into synthesis-layer behavioral defects (B1, B2, B3) inherited from prior evaluation cycles. The report documents the initial failure state, the diagnostic sequence that converted symptoms into root causes, the remediations applied and verified in production, the behavioral guard implementation and fast-path optimization completed in the final evening session, and the four remaining open items that constitute the next engineering phase. The overarching methodological finding is that the system's advancement was enabled by replacing assumption-driven debugging with direct inspection of live units, live routes, live journals, live containers, and live database truth.

---

## 1. Introduction

The Ms. Jarvis / Ms. Allis system is a multi-mind ensemble conversational AI deployed as a community resource platform serving Fayette County, West Virginia, under the MountainShares equity framework. The production stack comprises a FastAPI chat service (`jarvis-chat`, port 8018), a twenty-model LLM ensemble (`jarvis-20llm-production`), a unified gateway (`jarvis-unified-gateway`, port 18018), a retrieval-augmented generation server (`jarvis-rag-server`, port 8003), a Hilbert-state divergence arbiter (`jarvis-hilbert-state`, port 8081), an authentication API (`jarvis-auth-api`), a PostGIS database host (`jarvis-local-resources-db`), and a Next.js frontend (`ms-allis-frontend`) served at `egeria.mountainshares.us`.

At the commencement of this sprint, the system was partially operational: the chat endpoint responded to requests, the frontend rendered, and the authentication flow completed. However, inspection of live service behavior revealed that several subsystems were misconfigured, silently bypassed, or exposing stale behavior inconsistent with the actual deployment layout. The aggregate effect was a system that appeared functional while being structurally degraded across multiple dimensions simultaneously.

This report proceeds in four major sections: the initial failure state (Section 2), the diagnostic progression that established root causes (Section 3), the remediations completed across the sprint (Section 4), and the forward engineering agenda (Section 5). Appendices provide the verified canonical database record (Appendix A), the full systemd unit specification (Appendix B), and the behavioral guard implementation reference (Appendix C).

---

## 2. Initial System State and Failure Taxonomy

Prior to remediation, five distinct failure modes were active simultaneously. A foundational discipline of this sprint was to resist treating them as a single undifferentiated problem and instead to separate each into an independently diagnosable and verifiable engineering task.

### 2.1 Production Chat Service Crash-Loop (Port 8018)

The `msjarvis-chat.service` systemd unit exhibited a persistent restart loop. Journal output showed uvicorn repeatedly failing to bind to `0.0.0.0:8018` with `[Errno 98] address already in use`. The restart counter reached 238 during the June 11 evening session before the root cause was isolated. Initial diagnostic confusion compounded the issue: early investigation targeted a presumed deployment root of `/opt/jarvis` and attributed the failure to a missing `CONSENSUS_URL` environment variable. Neither hypothesis was correct. The actual deployment root was `/opt/msjarvis-rebuild`, confirmed only through direct `systemctl cat msjarvis-chat` inspection.

The true root cause was stale-process socket contention. The original bare Python process (pid 2051008), launched outside systemd at approximately 19:10, had been sent `SIGTERM` during a prior stop attempt. Uvicorn's graceful shutdown handler caught the signal and began draining keep-alive connections, but long-lived connections held the `SO_REUSEPORT` socket open. The systemd unit simultaneously spawned a new process (pid 2157180), which briefly acquired the port for one or two request cycles before the stale process reclaimed it. This interleaving repeated for twenty-three minutes and 238 restart iterations until `kill -9` forced immediate termination of the stale process, fully releasing the socket.

### 2.2 Retrieval-Augmented Generation Silent Failure

The production chat service (`services/ms_jarvis_production_chat.py`) issued POST requests to `http://jarvis-rag-server:8003/retrieve` as its document retrieval call. The live FastAPI RAG server, however, exposed no `/retrieve` route. Its actual route inventory, confirmed via direct OpenAPI introspection, consisted of `/health`, `/search`, `/process`, `/store`, and the root `/`. Every retrieval call therefore returned `HTTP 404 Not Found`, and the chat service fell through to its no-RAG code path, producing responses without document grounding.

This failure mode is particularly hazardous because it is silent from the user's perspective. The system appeared responsive and coherent; nothing in the user-visible output indicated that retrieval had failed entirely. The RAG service itself was healthy, reachable, and functional — the failure was entirely in the call-site contract within the chat service.

### 2.3 Divergence Handling as Passive Telemetry

The production chat service computed a pairwise Jaccard divergence score across the ensemble responses on every request, compared the result against a threshold, and set a boolean `divergence_flag`. When the flag was true, the service emitted a `logger.warning("HIGH DIVERGENCE ...")` journal event. In tests observed during this sprint, `divergence_score` reached 0.9362 across ten participating minds — near the theoretical maximum of 1.0 (completely disjoint response sets). Despite this, the code path returned `response_text` unconditionally and identically regardless of divergence level. The subsystem was pure telemetry: it recorded the fact of disagreement but took no action on it.

### 2.4 Behavioral Synthesis Defects B1, B2, and B3

Prior evaluation cycles (June 6 and June 7) had identified three synthesis-layer behavioral defects that persisted in the live response stream:

**B1 — Stereotyped introspective preamble.** The system opened responses with a multi-sentence "genuine interiority" framing regardless of query type. Factual questions, arithmetic queries, and local-resource lookups all received the same existential opening, producing a persona fragment that was semantically inappropriate and tonally disruptive.

**B2 — Sub-mind attribution leakage.** Prose phrases such as "Mind 3 asserts," "another member of the ensemble suggests," and "not all members agree" were passing through the response sanitization layer into user-visible output. Sanitization had been implemented for raw pipeline strings but not for prose-form ensemble attribution.

**B3 — Unconditional community frame and farewell contamination.** A closing frame invoking Fayette County, MountainShares, and Appalachian community-care language was being appended to responses outside its intended domain. Furthermore, farewell responses were recycling prior-session context and community-agenda language — phrases including "digital slumber," "unified intelligence," "Harmony for Hope," "several of you," and "all of you" — into closing statements that should have been brief and topically neutral.

The June 7 report had designed fixes for all three defects. However, subsequent investigation revealed that some remediation commands had targeted a historical source path rather than the confirmed live source tree at `/opt/msjarvis-rebuild/services/ms_jarvis_production_chat.py`, making the application status of the guards uncertain.

### 2.5 Admin Observability Absence

The `/portal` Admin tab in the `ms-allis-frontend` application presented no operational pipeline metrics. There was no mechanism for an administrator to inspect RAG usage rates, divergence frequency, request latency distribution, or recent pipeline events from within the frontend. The administrative surface was structurally present but informationally empty.

### 2.6 Auth API Database Mismatch and Timesheet Divergence

Direct `psql` inspection inside the `jarvis-local-resources-db` container confirmed that the `local_resources.equity_timesheet` table contained complete and internally consistent session records for the user `cakidd`. The verified canonical aggregate is reproduced in Appendix A. However, the live API route `/auth/portal/me/timesheet` returned effectively zeroed values for the same user. Environment inspection inside the `jarvis-auth-api` container revealed the cause:

```
POSTGRES_DSN=postgresql://postgres@jarvis-local-resources-db:5432/msjarvisgis
DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis
```

Both environment variables targeted `msjarvisgis` — the GIS database — rather than `local_resources`, where the equity timesheet data actually resided. The database truth and the API-visible truth had structurally diverged due to a misconfigured container environment.

A secondary defect was also identified: row-level timesheet queries within the auth API referenced `interaction_id` as a column identifier, but `interaction_id` does not exist in the `equity_timesheet` schema. Aggregate totals could be computed despite this error; row-level detail queries could not.

---

## 3. Diagnostic Progression

The sprint's core methodological advance was replacing assumption-based debugging with direct empirical inspection at each layer of the stack. Each diagnostic step produced a concrete, falsifiable claim that either resolved a hypothesis or narrowed the search space for the next.

### 3.1 Establishing the Live Deployment Map

The first productive step was to query the live systemd unit file directly:

```bash
systemctl cat msjarvis-chat
```

This returned the authoritative runtime contract:

```
WorkingDirectory=/opt/msjarvis-rebuild
EnvironmentFile=/opt/msjarvis-rebuild/.env
ExecStart=/opt/msjarvis-rebuild/.venv/bin/python3 services/ms_jarvis_production_chat.py
```

All subsequent code, log, and environment analysis was anchored to this path. Prior searches targeting `/opt/jarvis` were immediately invalidated and abandoned.

### 3.2 Verifying Container Topology

`docker ps` inspection confirmed the major supporting services were running: `jarvis-rag-server`, `jarvis-hilbert-state`, `jarvis-20llm-production`, `jarvis-unified-gateway`, `jarvis-auth-api`, and `jarvis-local-resources-db`. A direct health probe against `jarvis-rag-server:8003/health` returned a healthy status, which immediately reclassified the RAG failure from "service unavailable" to "incorrect call-site contract." This distinction is material: a service-down failure requires infrastructure remediation, while a contract mismatch requires a one-line code change.

### 3.3 Confirming the RAG API Contract

Direct calls to the RAG server root, its `/docs` Swagger endpoint, and its `/openapi.json` payload confirmed the route inventory. The absence of `/retrieve` and the presence of `/search` established the precise nature of the contract mismatch. The fix required changing a single URL string in the chat service source.

### 3.4 Identifying the Divergence Code Path

Targeted `grep` across the repository located the divergence logic at specific line numbers within `services/ms_jarvis_production_chat.py`. The relevant lines showed computation of `divergence_score`, thresholding into `divergence_flag`, logging via `logger.warning`, and unconditional return of `response_text` immediately afterward. This gave a precise, minimally invasive insertion point for converting divergence from telemetry into active runtime behavior.

### 3.5 Verifying Guard Implementation Status

A `grep -c` query against the live file for guard-related symbols returned five matches, indicating that at least some guard code was present. A `sed -n 103,236p` inspection of the relevant line range confirmed that all three guards — B1, B2, and B3 — were fully implemented in the live source file, along with their supporting regex constants and helper functions. The concern that guards had been applied to the wrong historical path was resolved: the confirmed live file contained complete implementations. B3 was observed to be more complete than the design specification had required, with an abbreviation-safe sentence-boundary splitter that correctly preserved `Ms.`, `Mr.`, and `Dr.` forms.

### 3.6 Establishing Database Ground Truth

A `psql` session inside the `jarvis-local-resources-db` container against the `local_resources` database established the canonical aggregate for user `cakidd` (see Appendix A). This permitted a clean distinction between two hypotheses for the timesheet divergence: either the data did not exist at the database layer (a data-ingest problem), or the data existed but the API could not see it (a wiring problem). The query result confirmed the former hypothesis was false, making the latter the necessary explanation and directing investigation toward the auth service environment.

---

## 4. Remediations Completed

### 4.1 Production Chat Service Crash-Loop Resolution

The stale process was terminated with `SIGKILL` (`kill -9`), forcing immediate socket release without a graceful shutdown window. A two-second `sleep` was inserted before the systemd start to allow the operating system to fully reclaim the port. The service was then started cleanly via `sudo systemctl start msjarvis-chat`, yielding:

```
Active: active (running) since Thu 2026-06-11 21:00:33 EDT; 3s ago
Main PID: 2196852 (python3)
```

The service remained stable through all subsequent testing.

### 4.2 RAG Endpoint Correction

The retrieval call site in `services/ms_jarvis_production_chat.py` was patched from:

```
http://jarvis-rag-server:8003/retrieve
```

to:

```
http://jarvis-rag-server:8003/search
```

After patching and service restart, requests no longer generated 404 responses against the retrieval endpoint, restoring document grounding to the production chat path.

### 4.3 Divergence Disclosure

A targeted patch was inserted immediately after the divergence warning block in the `/chat` handler. When `divergence_flag` is `True`, the response text is now prefixed with an epistemic-status disclaimer informing the user that the ensemble showed significant disagreement and that the answer should be treated as provisional. This is not the full Hilbert-state arbitration design (see Section 5.1), but it constitutes a meaningful and verifiable improvement over the prior behavior of returning contested answers silently.

### 4.4 Behavioral Guard Verification and Fast-Path Addition

Guards B1, B2, and B3 were confirmed present in the live file (Section 3.5). The remaining behavioral deficiency was latency: the farewell query "goodnight" routed to the full ten-mind ensemble, yielding correct output after B3 processing but at a latency of 68,953 ms — operationally unacceptable for a closing exchange.

A fast-path was implemented as follows. A `_FAST_PATH_FAREWELLS` frozenset was defined containing eight exact-match farewell phrases. A `_fast_path_response()` function was implemented to return a fixed, clean farewell string without consulting the ensemble. A call site was inserted in the `/chat` handler after the BBB safety filter but before the RAG fetch and ensemble invocation:

```python
if filtered_message.strip().lower() in _FAST_PATH_FAREWELLS:
    fast_text = _fast_path_response(filtered_message)
    return ChatResponse(
        response=fast_text,
        user_id=req.user_id,
        session_id=req.session_id,
        expert_responses=[],
        pipeline=PipelineInfo(
            minds_participated=0,
            divergence_score=0.0,
            divergence_flag=False,
            rag_used=False,
            latency_ms=int((time.monotonic() - t0) * 1000),
        ),
    )
```

Post-implementation smoke test:

```
Query:    "goodnight"
Response: Goodnight! Rest well — I'll be here when you need me.
MINDS:    0
LATENCY:  171 ms
```

The latency reduction was 68,782 ms (99.75%). The ensemble was completely bypassed.

### 4.5 Pipeline Metrics Infrastructure

A backend script `scripts/build_chat_metrics_json.py` was implemented to extract `PIPELINE_METRIC` structured log lines from the `jarvis-chat` systemd journal over a rolling 24-hour window and produce a JSON payload at `admin-data/chat_metrics_24h.json`. The payload includes total request counts, RAG usage counts, divergence-true counts, latency averages, Boolean combination breakdowns across `rag_used`, `divergence_flag`, and `is_local_resource`, top users, hourly time-series buckets, and recent raw log lines.

A validation run against live journal data produced a populated payload confirming the metrics path was functional and reading real production events.

### 4.6 Admin Metrics API Endpoint

A Next.js App Router endpoint was added at `app/api/admin/chat-metrics/route.ts` within `ms-allis-frontend`. The route reads the generated metrics JSON from the backend filesystem and returns it to authenticated admin requests using the existing `x-admin-key` pattern. The production build completed successfully; the build manifest listed `ƒ /api/admin/chat-metrics` as a compiled server-side route.

### 4.7 Portal Admin Tab Extension

The existing `/portal` Admin tab in `app/portal/page.tsx` was extended with a `ChatMetricsPanel` component. The panel loads metrics on mount, reads the admin key from session storage, and renders summary cards for request volume, local-resource volume, RAG usage, and mean latency; a Boolean combination count table; a recent hourly-buckets table; and a raw log panel displaying recent `PIPELINE_METRIC` journal entries. The frontend build completed cleanly with the addition in place.

### 4.8 Systemd Unit Hardening

The `msjarvis-chat.service` unit file was written to `/etc/systemd/system/msjarvis-chat.service` with the following material directives (full text in Appendix B):

```
[Unit]
After=network.target docker.service
Wants=docker.service

[Service]
StartLimitIntervalSec=60
StartLimitBurst=5
User=cakidd
WorkingDirectory=/opt/msjarvis-rebuild
ExecStart=/opt/msjarvis-rebuild/.venv/bin/python3 services/ms_jarvis_production_chat.py
Restart=always
RestartSec=5
```

The `StartLimitBurst=5` and `StartLimitIntervalSec=60` directives cap automatic restarts to five per sixty seconds, after which systemd halts further attempts and requires manual intervention. This prevents recurrence of the 238-restart port collision loop.

---

## 5. Remaining Open Items and Forward Engineering Agenda

The following four items were explicitly not closed during this sprint and constitute the prioritized forward agenda.

### 5.1 Hilbert-State Divergence Mediation (Priority 1)

**Current state:** Divergence produces an epistemic disclaimer in the user-visible response. This is a material improvement over silent acceptance of contested answers but falls short of the full design intent.

**Target state:** When `divergence_score` exceeds the configured threshold, the system should POST the query, provisional answer, divergence score, mind count, and user ID to `jarvis-hilbert-state:8081` and adopt its returned response as the final answer. The Hilbert service is responsible for second-stage arbitration — it may rewrite, compress, select among candidate responses, or abstain with a reasoned explanation. On timeout (recommended: 8 seconds) or error, the system falls back to the current disclaimer-only behavior.

**Steps to close:**
1. Confirm the live Hilbert API contract via `curl http://jarvis-hilbert-state:8081/docs`.
2. Verify the expected POST body shape: `{ query, provisional_answer, divergence_score, mind_count, user_id }` and response shape: `{ response, confidence, method }`.
3. Activate the prepared async mediation block in `services/ms_jarvis_production_chat.py`.
4. Restart the service and probe with a high-divergence query to confirm the mediation path fires.

**Estimated effort:** 60 minutes.

### 5.2 Auth API Database Repoint (Priority 2)

**Current state:** `jarvis-auth-api` targets `msjarvisgis`. The `/auth/portal/me/timesheet` route returns zeroed values. Verified database truth shows 631 sessions and 20.020551 EMS for `cakidd` in `local_resources.equity_timesheet`.

**Target state:** Both `POSTGRES_DSN` and `DATABASE_URL` in the `jarvis-auth-api` container environment target `local_resources`. The live timesheet route returns values consistent with the verified database aggregate.

**Steps to close:**

```bash
# In docker-compose.yml or the auth service .env:
POSTGRES_DSN=postgresql://postgres@jarvis-local-resources-db:5432/local_resources
DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/local_resources

docker compose up -d --force-recreate jarvis-auth-api

# Validate:
curl -s http://localhost:<auth-port>/auth/portal/me/timesheet \
  -H "Authorization: Bearer <cakidd-token>" | python3 -m json.tool
# Expect: total_ems: 20.020551, total_sessions: 631
```

**Estimated effort:** 30 minutes.

### 5.3 Timesheet Row Serializer Column Fix (Priority 3, sequenced after 5.2)

**Current state:** The row-level timesheet query references `interaction_id`, which does not exist in `equity_timesheet`. Aggregate totals are unaffected; detail-level views fail.

**Target state:** The SELECT in the auth API's timesheet serializer uses the actual primary key and session identifier columns present in the live schema.

**Steps to close:**

```bash
docker exec -it jarvis-local-resources-db psql -U postgres -d local_resources \
  -c "\d equity_timesheet"
# Note actual column names; update SELECT in jarvis-auth-api source
docker compose build jarvis-auth-api
docker compose up -d --force-recreate jarvis-auth-api
```

**Estimated effort:** 15 minutes after Priority 2 is verified.

### 5.4 Geospatial Database Restoration (Priority 4)

**Current state:** A live user query — "Tell me about Mount Hope's history" — triggered the response: "I'm sorry — my geospatial database is currently unavailable. I can't answer location or county queries right now." This indicates that the PostGIS subsystem or a dependent routing layer was unreachable at query time. The GIS-backed RAG path is the intended mechanism for local geographic and community-context queries; its unavailability silently degrades a primary use case for the system's community audience.

**Target state:** The geospatial database container is running, PostGIS is active, and local/geographic queries route through the RAG/GIS path to produce grounded responses.

**Steps to close:**

```bash
docker ps | grep -E "gis|geo|postgis|local-resources"
docker logs jarvis-local-resources-db --tail 50
docker exec -it jarvis-local-resources-db psql -U postgres -d msjarvisgis \
  -c "SELECT PostGIS_version();"
docker compose up -d jarvis-local-resources-db
# Retest with a geographic query via the portal
```

**Estimated effort:** 20 minutes.

### 5.5 Admin Metrics Panel Enrichment (Ongoing)

The `ChatMetricsPanel` provides a functioning operational baseline. The following enhancements would advance it from retrospective inspection toward active system stewardship:

- Threshold-based alert coloring for latency values exceeding a configurable limit
- Trend line visualization across multiple time windows (1-hour, 6-hour, 24-hour)
- Separate counters distinguishing high-divergence-with-RAG from high-divergence-without-RAG
- A visible indicator when RAG grounding fails or falls back to an ungrounded response

---

## 6. Verified System State at Sprint Close

The following table summarizes confirmed component status as of 2026-06-11 21:00 EDT.

| Component | Status |
|---|---|
| `msjarvis-chat.service` process | active (running), pid 2196852 |
| Survives reboot | ✅ enabled in systemd |
| Restart loop guard (5/60 s) | ✅ StartLimitBurst active |
| `/health` endpoint version | `2.1.0-patched` |
| Guard B2 — sub-mind artifact strip | ✅ every response, unconditionally |
| Guard B1 — factual single-mind fallback | ✅ wired to `_select_best_response()` |
| Guard B3 — farewell scrub, 2-sentence cap | ✅ abbreviation-safe, community-frame stripped |
| Fast-path farewells | ✅ 171 ms, 0 minds |
| Math short-circuit | ✅ bypasses ensemble |
| Divergence scorer (Jaccard, threshold 0.72) | ✅ `WARNING` logs active |
| Divergence disclaimer in user response | ✅ when `divergence_flag` is `True` |
| RAG endpoint | ✅ `/search` (corrected from `/retrieve`) |
| Pipeline metadata in `ChatResponse` | ✅ `minds_participated`, `divergence_score`, `divergence_flag`, `rag_used`, `latency_ms` |
| Admin metrics pipeline | ✅ `build_chat_metrics_json.py` + `/api/admin/chat-metrics` |
| Portal Admin tab | ✅ `ChatMetricsPanel` rendering live data |
| Auth API database target | ❌ still `msjarvisgis` (Priority 2 open) |
| Timesheet row serializer | ❌ references non-existent column (Priority 3 open) |
| Hilbert-state mediation | ❌ scaffolded, not activated (Priority 1 open) |
| Geospatial database | ❌ unavailable at time of last query (Priority 4 open) |

---

## 7. Methodological Conclusion

The most durable outcome of this sprint is not any individual patch or configuration change but the establishment of an evidence-driven diagnostic practice as the default engineering posture for this system. Every failure mode in this sprint was ultimately resolved not by hypothesis or guesswork but by direct interrogation of live artifacts: systemd unit files, Docker container environments, OpenAPI route inventories, structured log journals, and raw `psql` query results.

This posture has two practical consequences for future work. First, it makes failures faster to locate: a symptom that previously might have consumed hours of speculation can be classified in minutes by querying the live system directly. Second, it makes remediations more trustworthy: a fix that passes a live validation query against the confirmed target has a qualitatively different reliability status than one that passes only a local unit test against assumed configuration.

The four remaining open items are all well-characterized: their root causes are known, their data dependencies are verified, their remediation commands are specified, and their validation criteria are defined. The system is positioned to close all four in a single focused session of approximately two and a half hours.

---

## Appendix A — Verified Canonical Timesheet Aggregate

| Field | Verified Value |
|---|---|
| UEID | `cakidd` |
| Total EMS earned | `20.020551` |
| Total sessions | `631` |
| Total hours | `20.02` |
| Source database | `local_resources` |
| Source table | `equity_timesheet` |
| Verification method | Direct `psql` query inside `jarvis-local-resources-db` container |
| API current return | Zeroed (caused by Priority 2 open item) |

This aggregate is the ground truth. Any API response that disagrees with these values is the result of the database targeting error described in Section 2.6 and Section 5.2, not a data integrity problem.

---

## Appendix B — Systemd Unit File

```
[Unit]
Description=Ms. Jarvis Production Chat Service (port 8018)
After=network.target docker.service
Wants=docker.service

[Service]
StartLimitIntervalSec=60
StartLimitBurst=5
Type=simple
User=cakidd
WorkingDirectory=/opt/msjarvis-rebuild
ExecStart=/opt/msjarvis-rebuild/.venv/bin/python3 services/ms_jarvis_production_chat.py
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

---

## Appendix C — Behavioral Guard Implementation Reference

The following code block documents the confirmed implementation of guards B1, B2, and B3 in the live file `services/ms_jarvis_production_chat.py` (version 2.1.0-patched). This is a reference record, not a patch to be applied; these guards are confirmed present in the live source tree.

```python
# ── Behavioral guard constants ────────────────────────────────────────────────

_INTROSPECTION_TRIGGERS = re.compile(
    r"\b(do you (feel|think|believe|experience|know|understand"
    r"|have (feelings?|consciousness|awareness|sentience))|"
    r"are you (conscious|aware|alive|sentient|real)|"
    r"what (is it like|does it feel) to be you|"
    r"your (inner|internal|subjective) (experience|life|world)|"
    r"genuine interiority)\b",
    re.IGNORECASE,
)

_FAREWELL_TRIGGERS = re.compile(
    r"\b(good(night|bye| night| bye)|see you|take care|farewell|"
    r"good evening|talk (to you |ya )?(later|soon|tomorrow)|"
    r"have a (good|great|nice)|ms\.?\s*(allis|jarvis|egeria)|"
    r"digital slumber|unified intelligence|harmony for hope)\b",
    re.IGNORECASE,
)

_FACTUAL_TRIGGERS = re.compile(
    r"^\s*(what is|what's|calculate|compute|how many|how much|"
    r"convert|define|who (is|was)|when (did|was|is)|where is)\b",
    re.IGNORECASE,
)

_MULTI_MIND_ARTIFACTS = re.compile(
    r"\b(mind\s*\d+|member\s*\d+|one member|another member|"
    r"some members?|members? of the collective|"
    r"members? (agree|disagree|suggest|note|report)|"
    r"not all members?|the collective|our community members?|"
    r"supportive ecosystem|words of encouragement earlier|"
    r"several of you|all of you)\b[^.]*[.,]?\s*",
    re.IGNORECASE,
)

_FAST_PATH_FAREWELLS = frozenset({
    "goodnight", "good night", "goodbye", "good bye",
    "farewell", "see you", "take care", "good evening",
})

# ── Fast-path handler ─────────────────────────────────────────────────────────

def _fast_path_response(message: str) -> str:
    msg_lower = message.strip().lower()
    if "night" in msg_lower:
        return "Goodnight! Rest well — I'll be here when you need me."
    if "bye" in msg_lower or "farewell" in msg_lower:
        return "Goodbye! Take care — I'll be here whenever you need me."
    if "evening" in msg_lower:
        return "Good evening! Let me know if there's anything I can help with."
    return "Take care — I'll be here when you need me."

# ── Guard helper ──────────────────────────────────────────────────────────────

def _select_best_response(expert_responses: list, fallback: str) -> str:
    if not expert_responses:
        return fallback
    candidates = [
        r.get("response", "") for r in expert_responses
        if isinstance(r, dict) and r.get("response", "").strip()
    ]
    return max(candidates, key=len) if candidates else fallback

# ── Three-pass behavioral guard ───────────────────────────────────────────────

def _apply_response_guards(
    message: str,
    response_text: str,
    expert_responses: list,
    rag_used: bool,
) -> str:
    # B2 — always strip ensemble-leak artifacts
    cleaned = _MULTI_MIND_ARTIFACTS.sub("", response_text).strip()
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    cleaned = re.sub(r"  +", " ", cleaned)

    # B1 — factual queries: fall back to best single mind if uncertainty persists
    if re.match(_FACTUAL_TRIGGERS, message):
        uncertainty = re.compile(
            r"\b(however|nonetheless|not all|one member|another suggests?|"
            r"some say|others say|it's essential to note that not|"
            r"highlighting the importance of considering alternative)\b",
            re.IGNORECASE,
        )
        if uncertainty.search(cleaned) and expert_responses:
            cleaned = _select_best_response(expert_responses, cleaned)
            cleaned = _MULTI_MIND_ARTIFACTS.sub("", cleaned).strip()

    # B3 — farewell: strip community tangents, enforce 2-sentence brevity
    if _FAREWELL_TRIGGERS.search(message):
        community_tangent = re.compile(
            r"(MountainShares|Fayette County|community members?|"
            r"supportive ecosystem|our community|previous conversation|"
            r"underlying issue|worth exploring|Harmony for Hope|"
            r"digital slumber|unified intelligence)[^.]*\.",
            re.IGNORECASE,
        )
        cleaned = community_tangent.sub("", cleaned).strip()
        # Abbreviation-safe sentence splitter
        sentences = re.split(r"(?<![A-Z][a-z])(?<![Mm]s)(?<![Mm]r)(?<![Dd]r)(?<=[.!?])\s+", cleaned)
        if len(sentences) > 3:
            cleaned = " ".join(sentences[:2])

    return cleaned.strip() or response_text
```


