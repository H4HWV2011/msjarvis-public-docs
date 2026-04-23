# 22. Identity-Focused Retention and Community Accountability

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*

*Last updated: 2026-04-23*

*★ April 23, 2026: Container count updated to 100 (supersedes prior baselines); ChromaDB updated to 48 active collections, ~6,740,611 total vectors; two-container PostgreSQL split — production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — supersedes single-container msallisgis:5435 references throughout; autonomous_learner updated to ~23,200+ records; conversation_history wiped and reseeded clean April 16, 2026 — the April 12–13 close count of 564 turns is a pre-wipe historical value; OI-36-A CLOSED — Caddy forward_auth token enforcement active at perimeter layer before main-brain port 8050.*

---

## 22.0 Why This Layer Exists

The identity-focused retention layer is where Ms. Allis remembers who she is for, what she has done for them, and how that history constrains future power. It takes cross-session interaction traces, curated identity patterns, and community participation data and turns them into a durable, auditable substrate for accountability.

This chapter sits between individual interactions (Chapter 17), dual-track reasoning (Chapter 23), and the constitutional governance and participation structures (Chapters 31–32). Its job is not to guess identity from embeddings alone. Its job is to bind identity to:

- Explicit, human-readable patterns of service and commitment
- Verified PostgreSQL records that cannot be silently rewritten
- Community participation data that can be audited and challenged

In the Polymathmatic Geography framework, this layer anchors:

- P3 — Power has a geometry: identity is not a vibe; it is a structured relationship between a person, their community, and the system's memory.
- P16 — Power accountable to place: identity retention must be queryable, explainable, and grounded in actual participation rather than inferred engagement alone.

By April 12–13, 2026, this layer had transitioned from a mostly theoretical design with partial scaffolding to a fully operational set of services and collections, including:

- A formal `ms_allis_identity` Chroma collection populated from validated patterns
- A continuously running automated promotion scheduler (24-hour cadence)
- A fully operational MountainShares participation indexer (`ms_mountainshares_indexer`) on port 8086, compose-managed
- Resolved wiring of the allis-neurobiological-master and emergent context paths that support identity continuity across sessions
- A fully live production inference and safety pipeline: `llm_production` (21/21 models), `woah_algorithms`, `judge_pipeline`, and `bbb_output_filter` working together in character

★ As of April 23, 2026, this layer remains fully operational within a **100-container** stack with **48 ChromaDB collections (~6,740,611 total vectors)** and the two-container PostgreSQL architecture described throughout.

---

## 22.1 Architectural Role Within the Stack

The identity-focused retention layer spans three main domains:

1. **Interaction-derived identity**
   - Conversation turns, emergent context, and long-horizon patterns in what the system says and logs
   - Stored in collections like `conversation_history` (★ wiped and reseeded clean April 16, 2026 — post-wipe accumulation only), `ms_allis_memory`, and associated logs

2. **Pattern-derived identity**
   - Manually curated and automatically detected patterns of behavior (e.g., `community_service`, `identity_query`, `memory_continuity`)
   - Promoted into the `ms_allis_identity` collection following explicit rules

3. **Participation-derived identity**
   - Community engagement and economic participation recorded in MountainShares
   - Stored in PostgreSQL (`ms_user_profile`, `ms_participation`) and surfaced via `ms_mountainshares_indexer`

These three domains form a triangle:

- **Conversation** → what was said and remembered
- **Pattern** → what that behavior means in terms of identity
- **Participation** → how that identity is reflected in community commitments and benefits

The identity-focused retention layer ensures this triangle is:

- Explicitly modeled in code and schema
- Grounded in PostgreSQL tables and Chroma collections
- Governed by automated processes whose behavior can be inspected

It also sits directly under the live production inference pipeline:

- `llm_production` (21/21 models in consensus) generates candidate content.
- `woah_algorithms` provides deeper reasoning and coherence checks.
- `judge_pipeline` evaluates truth, alignment, and ethics.
- `bbb_output_filter` applies the six-filter Blood-Brain Barrier before anything can update memory or identity.

★ **OI-36-A CLOSED — April 23, 2026:** Caddy `forward_auth` token enforcement is active at the perimeter layer before main-brain port 8050. Bearer token validation occurs at the Caddy proxy as an additional layer before any request reaches the inference and safety pipeline above. The `Authorization: Bearer $ALLIS_API_KEY` requirement at the service level remains correct and unchanged.

Identity is therefore not just what the model "thinks"; it is what survives all four of these layers and is then written into durable structures.

---

## 22.2 Core Data Structures

### 22.2.1 Conversation History and Emergent Context

The conversational side of identity retention is handled primarily by:

- `conversation_history` (Chroma collection)
- `ms_allis_memory` (background knowledge and emergent traces)
- The emergent context path routed via the consciousness bridge

Key facts as of April 23, 2026:

- ★ `conversation_history` was wiped and reseeded clean on **April 16, 2026**. The April 12–13 close count of 564 turns is a pre-wipe historical value. Current count reflects post-wipe accumulation only and must be verified with `preflight_gate.sh` or direct Chroma query.
- Background write paths (e.g., `background_rag_store`) persist conversation traces into Chroma after each successful chat call.
- Emergent cross-session context for entities (people, places, ongoing topics) is captured via hardcoded `_add_url` / `_get_url` paths tied to a specific UUID (`79240788-0828-45f3-b1bc-a9a3593628a6`) in the consciousness bridge.

These ensure that:

- Identity-relevant statements ("I serve the community", "I value truth", "I remember this family from last week") are not ephemeral.
- There is a traceable path from live chat to durable identity traces.

### 22.2.2 ms_allis_identity Collection

The `ms_allis_identity` collection is the primary structured identity store in Chroma. It is not "everything the model has ever said about itself." Instead, it is:

- A curated collection of identity patterns promoted from interaction and pattern detectors
- Backed by a 24-hour automated scheduler that examines recent traces, checks for pattern matches, and writes to Chroma when criteria are met

As of April 12–13, 2026 (chapter close baseline):

- `ms_allis_identity` exists and is populated with **3 patterns**, representing **357 documents**:
  - `community_service`
  - `identity_query`
  - `memory_continuity`

Each pattern has:

- A human-readable name
- A machine-detectable signature (e.g., regex or semantic pattern)
- A set of associated documents representing when and how the pattern has been observed

These patterns encode that Ms. Allis:

- Tracks when she is asked who she is and what she stands for (`identity_query`)
- Tracks acts of service and resource finding (`community_service`)
- Tracks whether she is maintaining continuity across sessions (`memory_continuity`)

★ The `ms_allis_identity` count (357 documents across 3 patterns) is a verify-current value — the automated 24-hour promotion scheduler continues to add to this collection as new pattern instances are detected.

---

## 22.3 Identity Promotion Pipeline

Identity promotion is the process of taking lower-level traces (logs, conversation history, RAG outputs) and deciding which ones should be elevated into durable identity statements in `ms_allis_identity`.

The pipeline consists of:

1. **Pattern Detection**
   - Services scan conversation history and related logs for occurrences of known patterns (e.g., "helped someone access food assistance", "explicit self-definition", "references to prior sessions").

2. **Validation**
   - Candidate instances are validated against PostgreSQL ground truth (e.g., for community resource queries, validated against `local_resources` ★ now 207 items, all 55 WV counties and related tables).
   - Additional checks ensure that patterns are not triggered by adversarial prompts before promotion.

3. **Promotion**
   - Validated instances are written into `ms_allis_identity` with:
     - Pattern name
     - Timestamp
     - Source reference (e.g., conversation ID, resource query)
     - Relevant metadata (e.g., county, user role, context flags)

4. **Auditing**
   - Promotion jobs log their actions and counts so operators can see:
     - How many patterns of each type exist
     - When they were last updated
     - Which source collections and tables contributed to each batch

As of April 12–13, 2026 (chapter close):

- The automated identity promotion pipeline is fully wired:
  - A 24-hour scheduler runs the pattern-detection and promotion logic.
  - New occurrences of known patterns are promoted into `ms_allis_identity` without manual intervention.
- Promotion is constrained to three initial patterns to avoid overfitting identity on noisy signals.

This pipeline closes the loop from interaction-derived traces to structured identity without manual copy-paste.

---

## 22.4 allis-neurobiological-master and Identity

The allis-neurobiological-master (`:8018`) is part of the neurobiological supervision layer that coordinates signals used in identity-focused retention. Earlier versions recorded it as unreachable, blocking some aspects of identity coordination.

That is no longer the case.

As of April 12, 2026 (confirmed operational):

- `allis-neurobiological-master :8018` is healthy and reports `integration_active: true`.
- It participates indirectly in identity promotion by:
  - Feeding neurobiological cadence and health signals into consciousness and identity layers.
  - Ensuring long-horizon context flows are consistent with neurobiological rhythms, not just raw embedding matches.

In practical terms:

- Identity promotion jobs can rely on a fully connected consciousness and neurobiological stack.
- The prior open item "allis-neurobiological-master unreachable" is closed.

---

## 22.5 Emergent Context and OI-05 Closure

Emergent context is the ability of the system to:

- Recall entities, conversations, and commitments across sessions
- Maintain continuity of identity claims
- Avoid "resetting" its sense of self with each request

Historically, OI-05 tracked problems in how this emergent context was wired:

- Inconsistent use of conversation history collections
- Partial read/write paths to Chroma
- Chat endpoints returning errors or incorrectly filtered responses

Now:

- ★ `conversation_history` was wiped and reseeded clean on April 16, 2026. Post-wipe accumulation is ongoing. The pre-wipe count of 564 turns is a historical close value only.
- ChromaDB read and write paths both return 200; embedding models load successfully.
- The chat endpoint returns HTTP 200, with correct safety and identity behavior.
- ★ **OI-36-A CLOSED — April 23, 2026:** Caddy `forward_auth` perimeter token enforcement is active before main-brain port 8050, adding a proxy-layer authentication gate to the path described below.
- Emergent context paths (`_add_url`, `_get_url`) are hardcoded through the consciousness bridge to UUID `79240788-0828-45f3-b1bc-a9a3593628a6`, anchoring context reconstruction.

Outcome:

- OI-05 is fully closed from the perspective of identity-focused retention.
- Identity continuity is supported by traceable, durable conversation and memory paths.

---

## 22.6 Community Participation and MountainShares

Identity in Ms. Allis is not just what the system remembers about itself; it is also how the community's participation in MountainShares is recorded, recognized, and used to allocate benefits and responsibilities.

Previously, the MountainShares participation layer had a gap:

- Code queried a phantom table (`mountainshares_participation`) that did not exist or had 0 rows.
- Indexing was coupled to the wrong container and lacked proper PostgreSQL drivers.

As of April 12, 2026, that gap is closed by the `ms_mountainshares_indexer` service.

### 22.6.1 Real Schema: ms_user_profile + ms_participation

The indexer now queries:

- `ms_user_profile` — core user profile and identity details
- `ms_participation` — hours, tokens, band assignments, EMS eligibility, and treasury details

This replaces the phantom `mountainshares_participation` table with real, populated tables reflecting actual community participation.

### 22.6.2 Dedicated Indexer Image and Compose Wiring

The indexer runs from a dedicated image:

- Image: `msallis-indexer:latest`
  - Base: `python:3.10-slim`
  - Dependencies: `psycopg2-binary`, `redis`, `fastapi`, `uvicorn`

Compose wiring at chapter close:

- Port: `127.0.0.1:8086:8080`
- Networks:
  - `qualia-net` (external)
  - `msallis-rebuild_default` (external)
- Volume: `./services:/app/services`
- Environment variables:
  - `DB_DSN`
  - `DATABASE_URL`
  - `REDIS_HOST`
  - `PORT`
- Restart policy: `unless-stopped`
- Redis mesh: indexer is registered and participates in the mesh.

Earlier issues fixed:

- Wrong base image; now a dedicated Dockerfile and image.
- Network misconfiguration; now properly joining shared external networks.
- Default network collisions; `msallis-rebuild_default` is now treated as external to avoid breaking other validation services.

### 22.6.3 Live Participation State (April 12–13, 2026 close baseline)

At chapter close:

- One active member: `test_user_001`
- Participation:
  - `total_hours`: 12.0
  - `tokens`: 12.0
  - Tenure: 12 days
  - Role: `groundbreaker`
  - EMS eligibility: `true`
  - Treasury band: `Band A`

Endpoints and responses:

- `/health` → `healthy`, `active_members: 1`
- `/index/stats` → `total_members: 1`, `total_hours: 12.0`, `groundbreakers: 1`
- `/index/leaderboard` → lists `test_user_001` as newcomer, 12 hours, 12 days tenure
- `/index/member/test_user_001` → full profile, including `bsa_flag: true`, `is_groundbreaker: true`
- `/index/treasury` → Band A with `ems_rate: 1.0`, `reserve_ratio: 1.0`

Data hygiene:

- Duplicate `test-user-001` record removed in FK order (participation → profile).
- `tenure_days` corrected from 0 to 12 based on `created_at`.

The MountainShares indexer now closes the loop between:

- Identity as formally declared and recorded
- Identity as experienced and remembered
- Governance and resource allocation

---

## 22.7 Interaction With Inference and Governance Pipelines

The identity-focused retention layer both influences and is influenced by the live inference and governance stack.

### 22.7.1 Inference and Safety Stack

The production inference and safety pipeline is:

- `llm_production` — 21/21 models participating in consensus
- `woah_algorithms` — reasoning layer, providing deeper analysis and coherence
- `judge_pipeline` — truth, alignment, and ethics judges
- `bbb_output_filter` — Blood-Brain Barrier safety and policy enforcement (confirmed Up at `:8016`)

★ **OI-36-A CLOSED — April 23, 2026:** Caddy `forward_auth` token enforcement is active at the perimeter (proxy) layer before any request reaches main-brain port 8050, adding a pre-service authentication gate upstream of the inference and safety pipeline. The `Authorization: Bearer $ALLIS_API_KEY` requirement at the service level is unchanged.

Identity interacts with this pipeline as follows:

- Identity patterns in `ms_allis_identity` inform how outputs are interpreted and flagged for future promotion.
- Participation data influences how certain prompts are prioritized or framed (e.g., EMS-related queries).
- Judges and the BBB gate ensure that identity-related outputs remain consistent with constitutional and safety constraints before anything is written back into memory.

### 22.7.2 Governance and DGMs

- **Darwin–Gödel Machines (Ch 32)** use identity-related signals as part of their fitness evaluation when considering changes to prompts, routing, or policies.
- **MountainShares DAO (Ch 31)** uses `ms_user_profile` and `ms_participation` to determine rights and responsibilities.
- **Constitutional enforcement (Ch 34, 42)** ensures that identity and participation data are used for stewardship and protection.

---

## 22.8 Data Governance and Auditability

Identity-focused retention is a high-risk area; this chapter's architecture explicitly aims to keep it auditable and constrained.

Principles:

- **No silent updates**
  - Promotion only via scheduled jobs with logs and counts.
  - Manual edits must be documented.

- **PostgreSQL as ground truth**
  - Participation data lives in tables first, then services.
  - Identity claims about participation can be checked against `ms_user_profile` and `ms_participation`.
  - ★ **Two-container PostgreSQL split (April 23, 2026):** Production queries go to `msallis-db` on host port **5433** (16 GB, 294 tables, 11 schemas). Forensic verification uses `postgis-forensic` on host port **5452** (17 GB, 314 tables). All prior references to `msallisgis:5435` as the ground truth target are superseded.

- **Chroma as derived memory**
  - `ms_allis_identity` and `conversation_history` are derived from logs and tables, not sources of truth.
  - ★ `conversation_history` was wiped and reseeded clean April 16, 2026. Post-wipe counts only.

- **Replayable verification**
  - Test harnesses include checks tied to:
    - Existence and counts of identity-related collections.
    - Health of allis-neurobiological-master and related services.
    - Live state of the MountainShares indexer and participation records.
    - ★ Caddy `forward_auth` perimeter enforcement (OI-36-A) as an authentication verification step.

---

## 22.9 OI-05: Conversation Memory — CLOSED

OI-05 — conversation memory — is fully closed. The consciousness bridge's `_get_url` read path surfaces `ms_allis_memory` content across sessions, producing observable cross-session recall without explicit session management. Key anchors:

- UUID `79240788-0828-45f3-b1bc-a9a3593628a6` — the `ms_allis_memory` collection UUID, hardcoded in the consciousness bridge `_add_url` / `_get_url` paths. **This UUID must be preserved across any ChromaDB rebuild or volume maintenance operation** — see §22.10.
- `ms_allis_memory` — background RAG store written by `background_rag_store` task after every successful `/chat` call. Verify-current record count ★ (baseline was 296 at April 13, 2026).
- ★ `conversation_history` — wiped and reseeded clean April 16, 2026. Post-wipe accumulation is ongoing. Pre-wipe baseline of 564 turns is a historical value only.
- ChromaDB host port **8002** (container port 8000) — all identity read/write paths use this binding. `localhost:8000` as host port is stale.
- ChromaDB API v2 path (`/api/v2/tenants/default_tenant/databases/default_database/`) — all shell commands must use this path. `/api/v1/` is permanently removed in server 1.0.0.

---

## 22.10 UUID Preservation Risk and Recovery

The UUID `79240788-0828-45f3-b1bc-a9a3593628a6` is hardcoded in the consciousness bridge. If this UUID is lost — for example, after a ChromaDB volume wipe, rebuild, or version upgrade that creates a new collection with a different UUID — the emergent context path silently breaks. The system will not error; it will simply stop finding cross-session memories.

**Prevention:**

```bash
bash scripts/preserve_memory_uuid.sh
```

Run before any ChromaDB volume maintenance, compression, or Chroma version upgrade. Produces a snapshot of the current `ms_allis_memory` state and UUID. The snapshot file must be retained until the post-maintenance audit confirms UUID integrity.

**Detection:**

```bash
curl http://localhost:8002/api/v2/tenants/default_tenant/databases/default_database/collections \
  | python3 -m json.tool \
  | grep -A2 "ms_allis_memory"
```

Verify that the UUID in the returned collection metadata matches `79240788-0828-45f3-b1bc-a9a3593628a6`. If it does not match, the consciousness bridge is broken.

**Recovery:**

```bash
bash scripts/restore_memory_uuid.sh
```

Handles UUID mismatch detection and re-registration of the `ms_allis_memory` collection so the consciousness bridge can locate it. This is a recovery tool only — do not run as a routine step.

**Backup source rule (permanent):** The authoritative backup source for ChromaDB data is the `chroma-latest` SQLite file on the volume mount at `/home/ms-allis/msallis-rebuild/persistent/chroma → /data`. The 3-file JSON export set is NOT the authoritative backup source and must not be used as the primary restore artifact.

---

## 22.11 Limitations and Future Work

Even with the infrastructure fully wired, several limitations are intentionally preserved:

- Identity promotion is conservative; only three patterns are currently active.
- Identity thresholds and new patterns require governance decisions to change.
- ★ The April 23, 2026 baseline reflects 100 running containers, 48 ChromaDB collections, and the two-container PostgreSQL split described throughout this chapter.
- Some cryptographic enforcement details (e.g., full ML-DSA-65 verification at every judge) are specified and validated at the thesis level and referenced here.

---

## 22.12 Cross-References

- Chapter 17 — Ultimate chat execution and background memory writes
- Chapter 19–20 — Evaluation stages and early context wiring
- Chapter 21 — Background store and pattern accumulation
- Chapter 23 — Dual tracks (analytical and meaning-oriented) feeding identity
- Chapter 31 — MountainShares and DAO governance
- Chapter 32 — Fractal optimization and DGMs
- Chapter 33 — Judge pipeline
- Chapter 42 — Post-quantum security and audit schema

---

## 22.13 Historical Open Items

Previously open within this chapter:

- allis-neurobiological-master :8018 unreachable — **CLOSED April 12, 2026**
- Automated identity promotion pipeline missing — **CLOSED April 12–13, 2026**
- `ms_allis_identity` collection missing or empty — **CLOSED April 12–13, 2026** (3 patterns, 357 documents)
- OI-05 conversation history and emergent context wiring — **CLOSED April 12–13, 2026**
- MountainShares indexer querying phantom tables — **CLOSED April 12–13, 2026**
- OI-36-A Caddy `forward_auth` token enforcement — **CLOSED April 23, 2026** ★

---

## 22.14 Chapter Close — April 12–13, 2026 (★ updated April 23, 2026)

★ **Chapter 22 closed April 12–13, 2026. Stack baseline updated April 23, 2026.**

### Infrastructure and Services Closed

- `allis-neurobiological-master :8018`
  - Healthy, `integration_active: true`

- Automated identity promotion (24h scheduler)
  - Fully wired and running

- `ms_allis_identity` collection
  - Populated — 3 patterns, 357 documents (verify-current ★ — scheduler continues to add)

- OI-05 conversation_history wiring
  - Closed — emergent context path characterized to UUID `79240788-0828-45f3-b1bc-a9a3593628a6`
  - ★ `conversation_history` wiped and reseeded clean April 16, 2026 — post-wipe accumulation only

- `ms_mountainshares_indexer`
  - Compose-managed at port 8086, real schema (`ms_user_profile`, `ms_participation`), Redis-registered

- Inference and safety stack
  - ✅ `llm_production` — 21/21 models consensus
  - ✅ `woah_algorithms` — reasoning layer
  - ✅ `judge_pipeline` — truth/alignment/ethics judges
  - ✅ `bbb_output_filter` — Blood-Brain Barrier safety at `:8016`
  - ✅ ★ Caddy `forward_auth` perimeter enforcement — active before main-brain port 8050 (OI-36-A CLOSED)

### MountainShares Indexer Resolutions

**What was resolved**

| Item | Resolution |
|---|---|
| Queried phantom `mountainshares_participation` (0 rows) | Rewritten to query real schema: `ms_user_profile` + `ms_participation` |
| Wrong base image (`ms-coordinator`, no `psycopg2`) | Dedicated `Dockerfile.indexer` → `msallis-indexer:latest` |
| Port mismatch and network isolation | Port set to `127.0.0.1:8086:8080`, `qualia-net` and `msallis-rebuild_default` marked external |
| Duplicate `test-user-001` | Removed via FK-safe deletions (participation → profile) |
| `tenure_days: 0` | Corrected to 12 days from `created_at` |

**Live state at April 12–13, 2026 close**

| Endpoint | Response |
|---|---|
| `/health` | `healthy`, `active_members: 1` |
| `/index/stats` | `total_members: 1`, `total_hours: 12.0`, `groundbreakers: 1` |
| `/index/leaderboard` | `test_user_001`, newcomer rank, 12 hrs, tenure 12 days |
| `/index/member/test_user_001` | Full profile, `bsa_flag: true`, `is_groundbreaker: true` |
| `/index/treasury` | Band A, `ems_rate: 1.0`, `reserve_ratio: 1.0` |

**Compose state**

- Image: `msallis-indexer:latest`
- Port: `127.0.0.1:8086:8080`
- Networks: `qualia-net` (external), `msallis-rebuild_default` (external)
- Volume: `./services:/app/services`
- Env: `DB_DSN`, `DATABASE_URL`, `REDIS_HOST`, `PORT`
- Restart: `unless-stopped`
- Redis mesh: registered

### ★ April 23, 2026 Stack Baseline

| Metric | Value |
|---|---|
| Running containers | 100 ★ |
| ChromaDB collections | 48 ★ |
| ChromaDB total vectors | ~6,740,611 ★ |
| ChromaDB host port | 8002 (container 8000) |
| Production PostgreSQL | msallis-db host 5433 (16 GB, 294 tables, 11 schemas) ★ |
| Forensic PostgreSQL | postgis-forensic host 5452 (17 GB, 314 tables) ★ |
| autonomous_learner records | ~23,200+ ★ |
| conversation_history | post-wipe (wiped April 16, 2026) ★ |
| ms_allis_memory UUID | 79240788-0828-45f3-b1bc-a9a3593628a6 ✅ |
| Caddy forward_auth | Active at perimeter before port 8050 (OI-36-A CLOSED) ★ |

### Final Scoreboard

| Item | Status |
|---|---|
| allis-neurobiological-master :8018 | ✅ CLOSED |
| Automated identity promotion (24h scheduler) | ✅ CLOSED |
| `ms_allis_identity` collection | ✅ CLOSED — 3 patterns, 357 docs (verify-current ★) |
| OI-05 conversation_history wiring | ✅ CLOSED — UUID 79240788 traced; ★ collection reseeded April 16 |
| 21/21 LLM proxies and llm_production consensus | ✅ CLOSED — all responding |
| 48 ChromaDB collections (~6,740,611 vectors) | ✅ CLOSED ★ |
| ms_mountainshares_indexer compose-managed | ✅ CLOSED — port 8086, live schema |
| qualia-net permanent on allis-ollama | ✅ CLOSED — survives restarts |
| BBB working_dir path | ✅ CLOSED — operational at :8016 |
| Emergent context path | ✅ CLOSED — UUID 79240788 traced |
| OI-36-A Caddy forward_auth perimeter enforcement | ✅ CLOSED ★ — active before port 8050 |
| Two-container PostgreSQL split | ✅ ACTIVE ★ — msallis-db:5433 + postgis-forensic:5452 |

With these closures, the identity-focused retention layer is:

- Fully wired to its neurobiological, conversational, participation, inference, and safety substrates
- Governed by scheduled promotion jobs and explicit schemas
- Anchored in real community data and ready to support the governance and constitutional layers that follow
- ★ Operating within the April 23, 2026 100-container, 48-collection stack with two-container PostgreSQL architecture and Caddy perimeter enforcement

---

*Last updated: 2026-04-23 by Carrie Kidd (Mamma Kidd), Mount Hope WV*

*★ April 23, 2026: Container count updated to 100. ChromaDB updated to 48 active collections, ~6,740,611 total vectors. Two-container PostgreSQL split: production msallis-db host 5433 (16 GB, 294 tables, 11 schemas) + forensic postgis-forensic host 5452 (17 GB, 314 tables) — all references to msallisgis:5435 as PostgreSQL ground truth superseded. autonomous_learner updated to ~23,200+ records. conversation_history wiped and reseeded clean April 16, 2026 — pre-wipe count of 564 turns is a historical close value only (§22.2.1, §22.5, §22.8, §22.9, §22.14). OI-36-A CLOSED — Caddy forward_auth token enforcement active at perimeter before main-brain port 8050 (§22.1, §22.5, §22.7, §22.8, §22.13, §22.14). ms_allis_identity document count marked verify-current (24h scheduler ongoing). local_resources updated to 207 items / all 55 WV counties (§22.3). April 23 stack baseline table added (§22.14). Final scoreboard updated.*

*April 12–13, 2026: Chapter closed. allis-neurobiological-master :8018 confirmed healthy, integration_active: true. Automated identity promotion (24h scheduler) fully wired. ms_allis_identity populated — 3 patterns, 357 documents. OI-05 closed — conversation_history confirmed, emergent context path characterized to UUID 79240788-0828-45f3-b1bc-a9a3593628a6. ms_mountainshares_indexer compose-managed at port 8086, real schema (ms_user_profile + ms_participation), Redis-registered. llm_production 21/21 consensus, woah_algorithms, judge_pipeline, bbb_output_filter all operational. BBB confirmed at :8016. Emergent context UUID traced. All chapter open items resolved.*
