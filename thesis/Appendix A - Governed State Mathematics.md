# Appendix A — Verified Architecture and Epistemic Discipline
*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*  
*Last updated: July 20, 2026*

## A.0 Overview

Appendix A defines the verification discipline for Ms. Allis as it exists after the July 2026 architecture closeout. It states how claims are tested, how discrepancies are recorded, how demonstrated status is distinguished from design intent, and how verification extends across governed services, ports, schemas, Redis keyspaces, per-user memory, commons aggregation, and recurrent epistemic updates.

This appendix is not a generic testing note. It is the thesis-wide rule for what counts as built, what counts as only intended, and what evidence is required before a chapter may describe a mechanism as demonstrated.

## A.1 Verification Registers

Every claim in the thesis must appear in one of two registers:

- **Demonstrated.** A claim is demonstrated only when a running path has been exercised and corroborated across at least two independent layers such as endpoint behavior, database state, logs, scheduler state, collection contents, or Redis key inspection.
- **Not yet demonstrated.** A claim is not yet demonstrated when it remains architectural, partially implemented, synthetic-only, manually staged, or inferable from code shape without confirmed runtime evidence.

This distinction applies to all chapters equally. No mechanism may be described as live merely because a formal operator has been written in the chapter text or because a helper function exists in source.

## A.2 Multi-Layer Route Verification

Governed routes must be verified as routes, not as isolated components. Every route-level verification should test the following layers where they exist:

1. **Service identity and port binding.** Confirm which service owns the route and on which port it is actually bound.
2. **Health and status surface.** Exercise `/health`, `/status`, or equivalent service endpoints.
3. **Behavioral endpoint.** Call the route that performs the governed action, not only the health route.
4. **Storage effect.** Inspect the database, Chroma collection, or Redis keyspace that should reflect the action.
5. **Logs or scheduler traces.** Confirm that logs, crontab entries, or process traces record the action.
6. **Negative path.** Exercise at least one malformed, unauthorized, missing-parameter, or fail-closed path.

A route is not considered verified if only one layer has been checked. For example, a running service on a port is not enough without endpoint behavior; a database row is not enough without the route that created it; a formal chapter statement is not enough without code or runtime evidence.

## A.3 Verification Objects

Appendix A recognizes the following verification objects across the current architecture:

- **Services and ports,** including named runtime ownership of governance, time, GIS, assertion, and commons routes.
- **Schemas and tables,** including anti-surveillance schema design, manifest tables, publication tables, and promotion or assertion logs where they exist.
- **Vector collections,** including civic partitions, per-user conversational collections, sovereign subspaces, and commons collections.
- **Redis keyspaces,** including temporal keys, staged queues, rejection counters, and loop-state markers where implemented.
- **Crontab and scheduled runners,** including retention, promotion, DGM, and reporting cycles.
- **Projection and gate code,** including request-purpose, consent, legal-authority, and role-gated enforcement paths.

The architecture is therefore verified across service, store, and scheduler layers together.

## A.4 Discrepancy Recording

Discrepancies are first-class epistemic objects. A discrepancy exists whenever a chapter claims a mechanism, but verification reveals one of the following:

- the route exists but binds a different port than the text implies;
- the endpoint is live but the backing store is absent or named differently;
- the store exists but the route writing to it is missing;
- the formal model names more gates than live code actually enforces;
- a cron entry points to a route that does not exist;
- a collection or keyspace is present only as a test artifact, not a production path.

Each discrepancy record must include:

- **Claim under test.**
- **Observed behavior.**
- **Evidence source,** such as endpoint output, grep result, SQL output, Redis inspection, Chroma listing, or crontab output.
- **Disposition:** open, resolved, superseded, or intentionally deferred.
- **Document impact:** whether chapter language must be narrowed, revised, or moved to “not yet demonstrated.”

The purpose of discrepancy logging is not only defect tracking. It is what prevents the thesis from drifting away from the actual system.

## A.5 Demonstrated / Not Yet Demonstrated as a Global Standard

Implementation-status sections should follow the same discipline in every chapter:

### Demonstrated

A mechanism belongs here only if there is evidence of live behavior. Examples include:

- a service health route returning correctly on the bound port;
- a governed endpoint admitting, suppressing, or refusing requests in line with policy;
- a per-user collection being resolved at request time through the active service path;
- a commons route returning health on its named port and exposing its active collection name;
- Redis keys or Chroma collections showing the named state partition actually exists.

### Not yet demonstrated

A mechanism belongs here when:

- it is described formally but no runtime path confirms it;
- constants or thresholds are known from a probe session but not hardened in source;
- a gate is implied by policy but not visible in code or endpoint behavior;
- a schedule exists for downstream phases but the assessment phase is missing;
- a route is named in cron but no such endpoint exists.

This appendix requires chapters to narrow claims rather than inflate them. When in doubt, the mechanism remains in the “not yet demonstrated” register.

## A.6 H_t and Temporal Verification

The temporal axis must be verified across services, keyspaces, and promotion behavior.

### A.6.1 Service and port identity

Temporal verification begins by confirming which service owns the time route and which port is actually bound. As of the July 2026 verification pass, `jarvis-hilbert-time` is bound on `127.0.0.1:18094 -> 8092/tcp`, `jarvis-hilbert-state` is bound on `127.0.0.1:18092 -> 8081/tcp`, and `jarvis-civic-intake` is running without claiming the previously disputed `18093` port. The earlier 18093 conflict is therefore resolved at runtime in favor of `jarvis-hilbert-time` on 18094.

### A.6.2 Redis keyspace inspection

Temporal state must be verified by inspecting live Redis keys, not only by reading chapter text. The July 2026 verification pass confirmed keys under `hilbert:time:*`, including admitted and staged temporal keys such as:

- `hilbert:time:asbuilt_ch49_clean`
- `hilbert:time:staged:ch49_final`
- `hilbert:time:staged:ch49_test2`
- `hilbert:time:staged:ch49_test`
- `hilbert:time:ch49_test`
- `hilbert:time:asbuilt_ch49`

This proves that a staged temporal namespace exists, but as a subdivision under `hilbert:time:*`, not as a separate top-level `hilbert:staged:*` keyspace. No `hilbert:ephemeral:*` keys were present in the observed inspection.

### A.6.3 Demonstrated temporal properties

The following temporal properties are demonstrated:

- a live H_t service with named port ownership;
- admitted and staged temporal keys in Redis;
- promotion outcomes that distinguish admitted and suppressed states;
- a temporal architecture that is at least two-tier in runtime, with admitted and staged state visible.

### A.6.4 Not yet demonstrated temporal properties

The following temporal properties remain not yet demonstrated as named, runtime-visible mechanisms:

- a distinct top-level ephemeral temporal keyspace;
- a named hysteresis function or validator in the temporal service source;
- a fully separate three-store implementation in which ephemeral, staged, and historical layers are each independently surfaced and named.

Where the thesis uses the full three-layer model, Appendix A requires the text to say whether that model is presently architectural, partially visible, or fully implemented.

## A.7 Per-User Conversational Memory Verification

Per-user conversational memory must be verified at the collection, resolver, and scheduler layers.

### A.7.1 Collection naming and resolver path

The July 2026 verification pass confirmed that per-user conversational collections follow the `conversation_history_user_<slug>` pattern and are resolved through `conversation_manifest.py`, located at:

```text
/mnt/spiritual_drive/msjarvis-rebuild/services/hilbert/conversation_manifest.py
```

This path matters because the thesis does not treat per-user memory as conceptual only. It is implemented through a specific manifest-resolved naming mechanism.

### A.7.2 Active service resolution

Per-user conversational memory is demonstrated through request-time resolution across the active service chain, including `rag_server_main`, `retrieval_router`, `hippocampus`, and `consciousness`, with the legacy shared conversation collection retired at zero rows.

This is sufficient to mark the per-user decomposition as demonstrated at the storage-and-routing level. It is not merely a direct-sum idea written into chapter text.

### A.7.3 Scheduled retention path

The July 2026 crontab confirms an hourly retention worker:

```text
0 * * * * cd /mnt/spiritual_drive/msjarvis-rebuild && python3 services/hilbert/conversation_retention_worker.py >> /mnt/spiritual_drive/msjarvis-rebuild/logs/conv_retention.log 2>&1
```

This is evidence that per-user memory admission and retention occur on a named scheduled path, not only through interactive calls.

### A.7.4 Projection axes: demonstrated vs partial

The six-axis projection model for conversational disclosure includes consent, role, context, time, purpose, and legal authority.

The July 2026 verification pass confirms live code evidence for:

- **consent,** via consent-gated PII registration logic;
- **role,** via role-aware policy checks in the governed query path;
- **purpose,** via `request_purpose` and `permitted_use` enforcement;
- **legal authority,** via explicit `legal_authority` gating in projection wrappers and the governed query router.

The following axes are not yet demonstrated as separate, named runtime gates in the inspected code path:

- **context** as its own explicit projection parameter;
- **time** as a discrete access-validity gate rather than a general timestamp or retention concept.

Appendix A therefore treats the six-axis projection as partially implemented: four axes demonstrated, two still architectural in the inspected live path.

## A.8 Commons Verification

The Community Hilbert Commons must be verified at the gateway, collection, aggregation, and exclusion layers.

### A.8.1 Gateway and collection identity

The July 2026 verification pass confirmed a live commons gateway on port 8055:

```json
{"status":"ok","service":"mountainshares_commons_gateway","port":8055,"commons_collection":"community_hilbert_commons"}
```

This demonstrates that the commons is not just a formal operator. It has a named gateway and an active collection identity.

### A.8.2 Demonstrated aggregation facts

The following commons facts are demonstrated from the July 2026 synthetic opt-in probe and subsequent cleanup:

- 12 source documents produced 16 projected vectors and 1 visible centroid in the synthetic end-to-end aggregation check;
- the commons was then cleaned back to zero visible vectors, confirming that emptiness reflects corpus state rather than a broken gateway;
- Ms. Allis’s sovereign subspace was grep-verified as excluded from the aggregator path.

These facts are sufficient to mark the commons machinery as live at a test-grade level.

### A.8.3 Not yet demonstrated commons hardening

The following remain not yet demonstrated in live source as hardened production mechanisms:

- named `K_MIN` and `K_SENSITIVE` constants in the inspected aggregator source;
- a provenance certificate function in the active services tree;
- cryptographic provenance guarantees beyond probe-session evidence;
- a real opt-in commons corpus at scale rather than a synthetic verification run.

Appendix A therefore requires commons chapters to distinguish between a demonstrated live gateway with tested synthetic aggregation and a not-yet-demonstrated fully hardened provenance-and-threshold implementation.

## A.9 Request-Purpose, Legal Authority, and Projection Gate Verification

Governed retrieval and assertion paths must verify projection gates in code and endpoint behavior.

The July 2026 verification pass confirmed live `request_purpose` enforcement and manifest-aligned `permitted_use` matching in `gis_rag_service.py`, including fail-closed behavior when purpose is missing or mismatched. It also confirmed explicit `legal_authority` gating in projection wrappers and the governed query router.

These projection gates are considered demonstrated because they are visible in active source, tied to named request fields or headers, and enforced along a live route rather than only in utility code.

When a projection axis is present only in a chapter formula but not surfaced as a named parameter or enforced path, Appendix A requires it to remain outside the demonstrated register.

## A.10 Scheduler and Epistemic Loop Verification

The recurrent epistemic loop must be verified as a distributed runtime process rather than assumed to be a single daemon.

### A.10.1 Named scheduled runners

The July 2026 crontab confirms multiple active runners that together implement parts of the epistemic loop:

```text
*/30 * * * * /mnt/spiritual_drive/msjarvis-rebuild/dgm_cycle.sh
0 * * * * cd /mnt/spiritual_drive/msjarvis-rebuild && python3 services/hilbert/conversation_retention_worker.py >> /mnt/spiritual_drive/msjarvis-rebuild/logs/conv_retention.log 2>&1
0 3 * * * python3 /mnt/spiritual_drive/msjarvis-rebuild/services/identity_promotion.py >> /var/log/jarvis/identity_promotion.log 2>&1
```

This confirms that the epistemic loop is distributed across DGM governance, conversational retention, and identity promotion. Appendix A therefore rejects the simpler claim that the loop is either entirely absent or implemented as one monolithic scheduler.

### A.10.2 Demonstrated epistemic mechanisms

The following are demonstrated in the current architecture:

- request-purpose and permitted-use gating;
- disclosure-verdict write paths;
- belief revision and suppression behavior;
- self-assess or epistemic-log traces at the level already confirmed in the July 2026 audit trail;
- scheduled DGM and retention cycles.

### A.10.3 Not yet demonstrated epistemic mechanisms

The following remain not yet demonstrated as unified, explicit runtime artifacts:

- a single script or service named as the full recurrent epistemic loop runner;
- a dedicated Phase 1 assessment service that selects stale or priority components before downstream cycles run;
- recursive self-assessment automation in which the loop changes its own update rules through a governed mechanism;
- a human/community participation interface that operationalizes Chapter 52’s participation claims;
- variable loop frequency by domain rather than fixed cron schedules.

Appendix A therefore treats the epistemic loop as partially distributed and live, but not yet fully unified or self-governing in the strongest sense described by the architecture.

## A.11 Broken or Missing Governance Paths

Appendix A records intentionally paused or broken governance paths separately from demonstrated ones.

The July 2026 crontab includes a commented policy update entry marked `NEEDS_PARAMS`, but a subsequent source search found no `/policy/set` endpoint in the inspected services tree. This means the cron line points to a non-existent route, not merely to a route missing parameters.

This should be recorded as an open discrepancy with one of two dispositions:

- **disable honestly,** by marking the cron entry as disabled because the endpoint does not exist; or
- **build the route,** then supply the payload contract and verify it end-to-end.

Appendix A requires such paths to be logged explicitly so they cannot be mistaken for active governance machinery.

## A.12 Schemas, Tables, and Database Targeting

Database verification must confirm the correct database before governance DDL is applied.

The July 2026 investigation established that `msjarvisgis` on both inspected Postgres instances contained zero tables matching `gbim`, `manifest`, `promotion`, or `publication` in non-system schemas during the relevant search. This proves that GBIM-oriented trigger work aimed at `msjarvisgis` would be targeting the wrong database.

Appendix A therefore requires database-target verification before applying enforcement DDL:

1. list databases on the target Postgres instance;
2. search all candidate databases for the relevant schema/table names;
3. inspect the exact table with `\d+` before writing a trigger or function;
4. only then apply governance DDL.

This rule prevents architectural enforcement from being “successfully” applied to the wrong store.

## A.13 Verification Commands as First-Class Evidence

Command-level verification belongs inside the thesis discipline. For major routes, the command classes themselves are part of the evidence:

- `docker ps --format ...` for port and service identity;
- `curl` against health and governed action routes;
- `rg` or `grep` for live code enforcement paths;
- `redis-cli keys` and `type` for temporal and loop-state verification;
- `psql` introspection for schema/table targeting and trigger validation;
- Chroma collection listings for per-user, civic, and commons partitions;
- `crontab -l` for scheduled-loop verification.

Appendix A does not require these exact commands to be printed in every chapter. It does require that chapter claims rest on this style of evidence and that future verification passes preserve the same level of inspectability.

## A.14 Closing Statement

Appendix A is the operational conscience of the thesis. It binds formal chapters to live routes, live stores, live schedulers, and live discrepancies. It also requires humility: architecture may be elegant in formal notation while still partial in runtime, and the thesis remains trustworthy only when it says exactly which mechanisms are demonstrated, which are partial, and which are still aspirational.

The result is a verification discipline that matches Ms. Allis itself: governed, inspectable, discrepancy-aware, and capable of revision without pretending that a design is already the same thing as a running system.
