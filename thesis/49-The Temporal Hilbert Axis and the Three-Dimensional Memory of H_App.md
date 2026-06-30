# Chapter 49 — H_t: The Temporal Hilbert Axis and the Three-Dimensional Memory of H_App

The semantic body (H_App) and the spatial body (H_geo) established in earlier chapters
describe *what* the system knows and *where* that knowledge is anchored. This chapter
introduces the third axis that completes the system's operational memory model:
**H_t — the temporal Hilbert body**, implemented as `jarvis-hilbert-time`. Where H_App
holds semantic embeddings and H_geo holds spatial geometry, H_t holds the *when* of every
belief, event, and ingest operation as an ordered, decay-weighted timeline.

Together the three form a genuine three-dimensional memory space:

```
H_App  ×  H_geo  ×  H_t
 what       where      when
```

Every document ingested, every query answered, and every state transition recorded in the
system touches all three axes simultaneously.

***

## What jarvis-hilbert-time Is

`jarvis-hilbert-time` is a lightweight FastAPI service (port 18093 internally, `8092`
inside the Docker network) backed entirely by **Redis sorted sets**. It does not write to
ChromaDB. It does not hold embeddings. Its sole responsibility is recording *when*
something happened and computing how much that event still matters now.

Each entity — typically a ChromaDB collection name — maintains an independent timeline:

```
hilbert:time:{entity_id}  →  Redis ZSET scored by Unix epoch
    member format:  "{ISO-8601 timestamp}|{payload}"
    score:          float Unix timestamp (for ZREVRANGE ordering)
```

The service exposes three endpoints:

| Endpoint | Method | Purpose |
|---|---|---|
| `/timeline/register-json` | POST | Record a new event for an entity |
| `/timeline/query` | GET | Retrieve the N most recent events with decay weights |
| `/timeline/decay` | GET | Compute the recency weight for an arbitrary timestamp |

### Recency Decay

Each event carries a **recency weight** — a number between 0 and 1 representing how
fresh the event is relative to now. The weight follows a half-life decay function:

$$
w(t) = 0.5^{\,d \,/\, \tau}
$$

where $$d$$ is the age of the event in days and $$\tau$$ is the configurable half-life
(default 30 days, set via `TIME_HALF_LIFE_DAYS`). An event logged seconds ago has weight
≈ 1.0; one logged 30 days ago has weight 0.5; one logged 90 days ago has weight 0.125.

This is not bookkeeping metadata — it is a live scoring input used by the semantic
gateway at query time.

***

## How H_t Fits into the Full Ingest Pipeline

Every document upload triggers a synchronized write across all three memory axes. The
sequence within a single ingest call is:

```
intake_service  (port 8007)
    │
    ├── writes file to /data/incoming
    │
    └── spawns ms_allis_ingest_worker
            │
            ├──► Chroma  (ms_allis_uploads or named collection)
            │      chunk text → embedding → vector
            │      chunk_id hash + document_id hash stored
            │      → H_App axis written ✅
            │
            ├──► PostgreSQL  (msjarvisgis)
            │      lat/lon stripped from source
            │      collection_hash + feature_id from Chroma
            │      gbim_id = sha256(collection:chunk_id)
            │      INSERT INTO gbim_entities (...)
            │      → H_geo axis written ✅
            │
            ├──► hilbert-state  /state/set
            │      dimensions: {"chunk_count": N}
            │      triggers auto_entangle() to six known peer collections
            │
            └──► hilbert-time  /timeline/register-json
                    entity_id: collection_name
                    timestamp: datetime.now(UTC).isoformat()   # "+00:00" format
                    payload:   "ingest:{N}_chunks:{document_id}:{ext}"
                    → H_t axis written ✅
```

The result is that three Redis events land for every upload — one from the intake service
(file received), one from the ingest worker (chunks stored), one from hilbert-state
(state updated) — all within the same millisecond burst and all queryable immediately via
`/timeline/query`.

### The Timestamp Format Constraint

`jarvis-hilbert-time` runs Python 3.10. `datetime.fromisoformat()` in Python 3.10 does
**not** accept the `Z` UTC suffix — that was added in Python 3.11. The `parse_ts()`
function in the service handles `+00:00` and space-separated offsets but not `Z`. All
internal callers (intake service, hilbert-state, hilbert-gateway) use
`datetime.now(timezone.utc).isoformat()` which produces the `+00:00` form and therefore
works correctly. External clients sending `Z`-terminated timestamps will receive a 500
error until the container image is rebuilt on Python 3.11 or the `parse_ts()` function is
patched to strip the `Z` before parsing.

***

## How H_t Powers the Semantic Gateway

`jarvis-hilbert-semantic` (the Hilbert gateway, port 18091) implements
**decay-weighted semantic retrieval**. When a query arrives, it does not simply return
the closest vectors by cosine distance. It computes a composite score:

$$
\text{final\_score} = \text{semantic\_score} \times \text{freshness\_weight} \times \text{recency\_boost}
$$

where:

- **semantic\_score** = `1 / (1 + cosine_distance)` from ChromaDB — the H_App
  contribution
- **freshness\_weight** = `0.5^(age_days / half_life)` from the document's
  `ingested_at` metadata — the document-level H_t contribution
- **recency\_boost** = a multiplier in [1.0, 1.05] derived from the entity's most
  recent hilbert-time event — the collection-level H_t contribution

The recency boost is computed by `get_collection_recency()`, which calls
`/timeline/query` with `limit=5`, reads the top event's `recency_weight`, and maps it to
a small boost if the collection has been active within the last few minutes. A collection
touched 10 seconds ago scores up to 5% higher than an identical-content collection last
touched two weeks ago. This ensures that an active investigation — a parcel dispute, an
ongoing community health query — surfaces its most recently ingested material preferentially
without discarding older evidence.

***

## The Three-Hilbert-Body Architecture

The three services form a complete operational memory:

| Axis | Service | Store | Records |
|---|---|---|---|
| **H_App** — *what* | jarvis-hilbert-semantic | ChromaDB | Semantic embeddings, decay-scored retrieval |
| **H_geo** — *where* | GBIM / PostGIS | PostgreSQL | Spatial geometry, lat/lon, GBIM entities |
| **H_t** — *when* | jarvis-hilbert-time | Redis | Ordered event timelines, recency weights |

And the fourth service that reads across all three:

| Service | Role |
|---|---|
| **jarvis-hilbert-state** | Maintains the state machine over entity identity — *what state something is in* — and records each transition into H_t. Acts as the coordinator between the three axes. |

### Why Redis, Not ChromaDB, for Time

The choice to use Redis sorted sets rather than a ChromaDB collection for the temporal
axis is deliberate. Time is an ordering problem, not a similarity problem. Redis sorted
sets provide O(log N) insertion and O(log N + M) range retrieval by score, which maps
perfectly to "give me the M most recent events for entity X." A vector store would add
embedding overhead, approximate nearest-neighbor search semantics, and collection
management complexity to what is fundamentally an append-only ordered log. Redis is the
right data structure for this axis.

***

## The Live Timeline — Observed Behavior

As of the session documented here, the following entity timelines were confirmed present
in Redis:

| Entity | Events | Most Recent Payload |
|---|---|---|
| `ms_allis_uploads` | 3+ | `ingest:1_chunks:{hash}:.txt` |
| `ms_allis_active` | 4 | `entanglement:ms_allis_uploads<->ms_allis_active` |
| `ms_allis_uploads` | 5 | `semantic_query:Ms. Allis parcel boundary` |
| `ms_allis` | 2 | `semantic-ingest` |

The presence of `semantic_query:` payloads in the `ms_allis_uploads` timeline confirms
that query events — not just ingest events — are also registered into H_t, providing a
complete record of both *what was stored* and *what was asked*.

***

## Relationship to Earlier Chapters

| Chapter | Establishes | H_t Role |
|---|---|---|
| 04 — Hilbert Space & State | H_App as a semantic Hilbert space; hilbert-state as the state machine | H_t extends the state machine with an ordered temporal record of every transition |
| 45 — H_geo | The spatial body, PostGIS, GBIM entity binding | H_t records *when* each spatial entity was last observed or queried |
| 46 — H_App ⊗ H_geo | The tensor product bridge joining semantic and spatial arms | H_t adds the third tensor dimension, making the full product H_App ⊗ H_geo ⊗ H_t |
| 44 — Phi Probe | Semantic coherence measurement across H_App | Recency weighting from H_t modulates which vectors the Phi probe sees as "current" |
| 42 — Post-Quantum Security | Signed, auditable provenance for all belief operations | H_t's Redis timeline provides the append-only audit log that the security layer can anchor signatures to |
| 43 — Role-Gated Knowledge | Access control by role over collections | H_t timelines are themselves collection-scoped, so role gates apply to temporal queries as well |

***

## Operational Notes

**Filesystem immutability.** The `jarvis-hilbert-time` container mounts its service file
read-only (`/mnt/nvme1/msjarvis-rebuild/services/jarvis_hilbert_time.py:/app/services/...:ro`).
Patches to the running service require editing the source file on the host and restarting
the container — they cannot be applied inside the container with `docker exec`.

**No Chroma collection named `hilbert_time`.** There is no ChromaDB collection with this
name and none is expected. The service is Redis-only by design. Any health check that
tests for a `hilbert_time` Chroma collection is incorrect and should be removed.

**DB_HOST configuration.** The ingest worker that feeds H_t (via hilbert-state) connects
to PostgreSQL by Docker service name (`jarvis-local-resources-db`), not by bridge IP. The
compose file must not hardcode `172.17.0.1` or `172.18.0.1` for `DB_HOST` — those IPs
are unreachable from inside containers and will produce connection timeouts on every
upload.

***

*Formal derivations of the decay operator and the tensor-product composition H_App ⊗
H_geo ⊗ H_t are in the work-repo thesis. This chapter documents the implemented
architecture as observed in the running system.*
