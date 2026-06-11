# Engineering Report: Ms. Jarvis / Ms. Allis System Advancement Summary

## Scope

This report documents the recent multi-day stabilization, instrumentation, and integration work completed across the Ms. Jarvis / Ms. Allis stack. It captures the initial system condition, major defects encountered, specific remediations applied, validated outcomes, and the next development steps needed to continue improving reliability, grounded response quality, observability, and data integrity.

The work centered on five intertwined areas: production chat service stability, retrieval-augmented generation wiring, divergence handling, admin observability through the existing `/portal` experience, and equity timesheet data correctness across the auth/API path.

## Initial System Condition

At the beginning of this effort, the system was partially operational but structurally inconsistent across runtime paths, API contracts, and data sources. The stack was responding in some places, but key services were either misconfigured, silently bypassed, or exposing stale behavior relative to the actual deployment layout.

### Production chat instability

The production chat service initially exhibited a systemd crash-loop pattern. Journal output showed uvicorn repeatedly failing to bind to `0.0.0.0:8018` with `[Errno 98] address already in use`, leading to dozens of rapid restart attempts before eventually stabilizing once the old process was fully stopped.

There was also early diagnostic confusion around a presumed `/opt/jarvis` deployment root and missing `CONSENSUS_URL`, but the live unit file later confirmed the real deployment root was `/opt/msjarvis-rebuild`, with the chat service launched from that directory and reading `/opt/msjarvis-rebuild/.env`.

### Retrieval layer failure

A more consequential issue was present in the RAG path. The production chat service was issuing POST requests to `http://jarvis-rag-server:8003/retrieve`, but the live FastAPI RAG server did not expose `/retrieve`; its advertised routes were `/health`, `/search`, `/process`, `/store`, and `/`. As a result, the chat service logged repeated `HTTP/1.1 404 Not Found` responses from the RAG backend and produced answers without grounded retrieval.

This meant the system could appear responsive while still being functionally degraded, because document grounding was silently bypassed despite the RAG service itself being alive and healthy.

### Divergence behavior was passive only

The production chat service already computed `divergence_score` and `divergence_flag`, and logs showed repeated `HIGH DIVERGENCE` warnings with 11 participating minds and scores consistently above threshold. However, the code path only logged the divergence event and returned the response unchanged, so the divergence subsystem acted as passive telemetry rather than an active safety or quality-control mechanism.

### Behavioral synthesis defects

Prior evaluation history identified three synthesis-layer behavior problems that remained relevant during this workstream:

- A stereotyped introspective opening was being applied too broadly, even on non-introspective questions.
- Sub-mind references such as “Mind 3 asserts” could leak into output because sanitization covered raw pipeline strings but not prose attributions.
- A universal Appalachian / Fayette County frame could be appended outside its intended domain, and farewell handling could accidentally recycle unrelated closing content.

These issues framed the need for conditional response shaping rather than globally applied persona fragments.

### Missing observability in admin workflow

Before this work, there was no useful operational visibility inside the existing `/portal` Admin tab for understanding live pipeline behavior. Metrics generation either did not exist or produced effectively empty output, and there was no integrated way for an admin user to inspect RAG usage, divergence frequency, latency, or recent pipeline events from within the frontend.

### Auth and timesheet mismatch

A separate but critical integrity issue existed in the user equity/timesheet flow. Direct database inspection showed that the `local_resources.equity_timesheet` table contained completed sessions and EMS totals for `cakidd`, but the live API path serving `/auth/portal/me/timesheet` returned effectively zeroed values. This indicated that the API-visible truth and database truth had diverged.

## Investigation and Diagnostic Progression

The work advanced by replacing assumptions with direct inspection of live units, containers, routes, logs, and database contents.

### Resolving the real deployment map

Systemd inspection established the true runtime contract for the production chat service:

```text
WorkingDirectory=/opt/msjarvis-rebuild
EnvironmentFile=/opt/msjarvis-rebuild/.env
ExecStart=/opt/msjarvis-rebuild/.venv/bin/python3 services/ms_jarvis_production_chat.py
```

This corrected the earlier mistaken search path and allowed all subsequent code, log, and environment analysis to target the actual live files.

### Verifying live container topology

Docker inspection showed the major supporting services were running, including `jarvis-rag-server`, `jarvis-hilbert-state`, `jarvis-20llm-production`, `jarvis-unified-gateway`, `jarvis-auth-api`, and others. The RAG server on port 8003 was specifically verified as healthy and reachable, which narrowed the retrieval issue from “service down” to “wrong endpoint contract.”

### Inspecting the RAG API contract

Direct calls to the RAG server root, Swagger docs, and OpenAPI JSON confirmed the route set exposed by the service. The absence of `/retrieve` and presence of `/search` established that the problem was in the chat service call site, not the retrieval server itself.

### Locating divergence logic in code

A targeted grep across the repo found the active divergence logic inside `services/ms_jarvis_production_chat.py`, with a patched twin under `patches/ms_jarvis_production_chat_patched.py`. The relevant lines showed:

- computation of `divergence_score`,
- boolean thresholding into `divergence_flag`,
- logging via `logger.warning("HIGH DIVERGENCE ...")`, and
- unconditional return of the original `response_text` afterward.

This gave a precise insertion point for turning divergence from telemetry into runtime behavior.

### Establishing database truth for timesheets

A direct `psql` query run inside the Postgres container against `local_resources` established the canonical aggregate for the user:

| Field | Verified value |
|---|---|
| UEID | `cakidd` |
| Total EMS earned | `20.020551` |
| Total sessions | `631` |
| Total hours | `20.02` |

This confirmed that the data existed and was internally consistent at the database layer.

### Identifying the auth-service DB mismatch

Inside `jarvis-auth-api`, environment inspection showed:

- `POSTGRES_DSN=postgresql://postgres@jarvis-local-resources-db:5432/msjarvisgis`
- `DATABASE_URL=postgresql://postgres:postgres@jarvis-local-resources-db:5432/msjarvisgis`

That was the wrong target database for the verified timesheet data, which lived in `local_resources`. This explained why the route-visible totals were wrong even though the table contents were correct.

## Remediations Completed

### 1. Production chat crash-loop stabilized

The address-in-use restart loop on port 8018 was diagnosed as stale-process contention rather than a missing application import or bad root path. Once the lingering process was stopped and the service restarted from the confirmed live working directory, `jarvis-chat.service` came up cleanly and remained active.

This removed the immediate operational blocker and established a stable foundation for subsequent debugging and patch deployment.

### 2. RAG endpoint corrected

The production chat service was patched so that its retrieval call targets the actual route exposed by the live RAG server:

```text
http://jarvis-rag-server:8003/search
```

instead of:

```text
http://jarvis-rag-server:8003/retrieve
```

After patching, syntax-checking, and restarting the service, new requests no longer generated 404 retrieval failures against `/retrieve`. This restored grounded retrieval to the production chat path.

### 3. Divergence now affects response behavior

A targeted patch was inserted immediately after the divergence warning block so that high-divergence responses are no longer returned silently. When `divergence_flag` is true, the response now receives an epistemic-status disclaimer explaining that the ensemble showed significant disagreement and that the answer should be treated as provisional.

This is not yet the final Hilbert-state mediation design, but it is a meaningful shift from passive logging to active user-visible uncertainty disclosure.

### 4. Hilbert-state mediation path was prepared

Because divergence was conceptually assigned to Hilbert-state, live route inspection and patch scaffolding were prepared to send high-divergence responses to the `jarvis-hilbert-state` service on port 8081. A concrete async mediation block was drafted to POST the query, provisional answer, divergence score, mind count, and user ID to a Hilbert endpoint and adopt its returned response when successful.

This work created a near-ready insertion point for true second-stage arbitration, even if final endpoint selection and production activation still remain ahead.

### 5. Pipeline metrics generator was implemented

A new backend script, `scripts/build_chat_metrics_json.py`, was created to extract `PIPELINE_METRIC` lines from the `jarvis-chat` journal over the prior 24 hours and transform them into a structured JSON payload at `admin-data/chat_metrics_24h.json`.

The generator computes:

- total requests,
- local-resource request counts,
- RAG-true counts,
- divergence-true counts,
- average latency,
- combination counts across `rag_used`, `divergence_flag`, and `is_local_resource`,
- top users,
- hourly timeseries buckets, and
- recent raw log lines.

A validation run produced a populated payload with 3 events, 2 local-resource requests, 3 divergence-true requests, and a 100 percent high-divergence-with-RAG rate, proving the metrics path was functional and reading real live logs.

### 6. Metrics exposed through Next.js API

A new App Router endpoint was added at `app/api/admin/chat-metrics/route.ts` inside `ms-allis-frontend`. That route reads the generated metrics JSON from the backend filesystem and returns it to authenticated admin requests using the existing `x-admin-key` pattern already present in the broader admin flow.

The production frontend build completed successfully, and the build manifest explicitly listed `ƒ /api/admin/chat-metrics`, confirming that the route compiled into the deployed application bundle.

### 7. Existing `/portal` Admin tab extended with metrics UI

Rather than introducing a new detached admin page, the existing `/portal` Admin tab was extended with a new `ChatMetricsPanel` component in `app/portal/page.tsx`.

The panel now loads metrics on mount, reads the admin key from session storage, and presents:

- summary cards for request volume, local-resource volume, RAG usage, and latency,
- a table of boolean combination counts,
- a recent-hourly-buckets table, and
- a recent-log panel with raw `PIPELINE_METRIC` entries.

The frontend still built cleanly after this insertion, and the route listing confirmed the portal remained operational.

## Verified Outcomes

### Chat pipeline is now more grounded and transparent

The system no longer attempts to hit a nonexistent `/retrieve` endpoint, which means the production chat flow can actually benefit from the live RAG service rather than degrading silently into ungrounded responses.

High-divergence conditions are also no longer invisible to users, because flagged answers now receive explicit cautionary framing instead of being returned unchanged after a warning-only log event.

### Admin observability is materially improved

The stack now has a functioning 24-hour metrics extraction path and a frontend surface for consuming it. An administrator using the existing `/portal` Admin tab can inspect concrete pipeline characteristics from the live system, including whether retrieval was used, whether a request was treated as local-resource oriented, how often divergence triggers, and how latency trends over time.

This represents a real shift from anecdotal debugging to evidence-driven operation.

### Database truth is now known with certainty

The timesheet domain now has a verified canonical aggregate at the database layer. For `cakidd`, the system has confirmed 631 completed sessions, 20.020551 EMS earned, and 20.02 hours in the `local_resources.equity_timesheet` table.

This makes it possible to distinguish between data-ingest problems and API wiring problems; the current issue is clearly the latter.

### Root causes are now better separated

A major accomplishment of the work was conceptual separation of failure modes:

- service instability was a port-binding lifecycle issue,
- RAG failure was an endpoint contract mismatch,
- divergence weakness was a control-flow omission,
- metrics absence was an observability gap, and
- timesheet inaccuracy was a database-target mismatch plus schema-query drift.

That separation matters because it turns one seemingly chaotic system problem into several tractable engineering tasks with different owners and validation paths.

## Remaining Gaps and Incomplete Items

Not all objectives were fully closed during this period.

### Hilbert-state not yet fully live as divergence arbiter

The code scaffolding for Hilbert-state mediation exists conceptually and was prepared in patch form, but the final production implementation still needs confirmation of the exact Hilbert API contract and activation in the live response path.

### Behavioral defects B1, B2, and B3 still need final code placement

The earlier proposed fixes for introspection gating, sub-mind prose sanitization, community-frame gating, and farewell short-circuiting were valid in design, but some earlier commands targeted the wrong historical source path. Those fixes still need to be re-applied against the confirmed live source tree under `/opt/msjarvis-rebuild`.

### Auth API still points at the wrong database

The auth container environment still showed `msjarvisgis` as its active DB target, while the verified timesheet data resides in `local_resources`. Until that mapping is corrected and the service rebuilt or recreated, the live timesheet route will continue to disagree with the underlying database truth.

### Timesheet entries query uses the wrong schema assumption

Attempts to query recent entries using `interaction_id` failed because that column does not exist in `equity_timesheet`. The aggregate path is validated, but the row-level serialization path still needs to be updated to the actual table schema.

## Recommended Next Steps

### 1. Complete Hilbert-state divergence mediation

The highest-value next improvement on the chat-quality side is to promote divergence from “disclaimer only” to “arbitrated finalization.” The prepared Hilbert-state block should be wired to the actual live endpoint and allowed to rewrite, compress, abstain, or otherwise stabilize answers under high-disagreement conditions.

A safe rollout pattern would be:

- verify the Hilbert endpoint and JSON contract,
- enable mediation only when `divergence_score` exceeds threshold,
- preserve existing metadata fields, and
- fall back to disclaimer-only behavior if Hilbert-state errors or times out.

### 2. Repoint auth service to `local_resources`

The auth container should be reconfigured so that both `POSTGRES_DSN` and `DATABASE_URL` target `local_resources` instead of `msjarvisgis`, followed by a rebuild or force-recreate of `jarvis-auth-api`.

This is the only way the live `/auth/portal/me/timesheet` route can begin reflecting the verified 631-session / 20.020551-EMS ground truth already established directly in Postgres.

### 3. Fix the timesheet entries serializer

After repointing the auth API, the timesheet route should inspect `\d+ equity_timesheet` and update its recent-entry SELECT to use columns that actually exist. The current use of `interaction_id` is incorrect and will prevent row-level detail views from succeeding even if the aggregates are fixed.

### 4. Apply behavioral response guards in the live source tree

The synthesis-layer quality improvements identified earlier should now be implemented in the actual production source path:

- conditional introspection preamble only for self-awareness or consciousness prompts,
- regex-based removal of prose sub-mind attribution,
- conditional Appalachian/community closing frame only for relevant community-domain prompts, and
- direct farewell short-circuit to avoid unrelated closing content.

These changes would reduce persona bleed, improve topical discipline, and make the system feel more intentionally scoped.

### 5. Expand admin metrics into a true operations panel

The new metrics panel is a strong first milestone, but it can be developed into a more complete operations console by adding:

- thresholds and alert coloring for extreme latency,
- trend lines across multiple time windows,
- specific counts for high-divergence-without-RAG vs high-divergence-with-RAG, and
- a visible indicator when RAG grounding fails or falls back.

That would make the Admin tab useful not only for retrospective inspection but also for active system stewardship.

## Conclusion

Across this workstream, the system moved from a state of partial responsiveness and hidden failure into a much more inspectable and structurally coherent platform. The production chat service was stabilized, RAG was reconnected to the live endpoint contract, divergence was made visible in user-facing behavior, pipeline metrics were turned into a real admin dashboard, and the timesheet data mismatch was traced to a concrete database-targeting error rather than a missing-record problem.

The most important overall outcome is that the system is no longer being advanced by guesswork alone. Live units, live routes, live logs, live containers, and direct database truth were all used to separate symptoms from causes. That shift in method is itself part of the system’s advancement, because it creates a reproducible engineering basis for the next phase: Hilbert-state divergence arbitration, behavioral prompt hygiene, and end-to-end correction of the auth/timesheet data path.
