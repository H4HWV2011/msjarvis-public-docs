# Chapter 8 — Quantum-Inspired Entanglement and Coupled State

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: ★★ 2026-04-17 — April 16–17 production audit complete. All subsections updated per April 2026 forensic baseline. ChromaDB v2 multi-tenant API path corrected throughout. Collection count, embedding count, BBB filter surface, pituitary API surface, memory route surface, and LLM ensemble endpoint descriptions all updated to April 17 ground truth. OI-19 and OI-21 status reviewed. Observability limits explicitly documented.*

---

This chapter presents the quantum-inspired entanglement mechanism used in Ms. Allis: a structured way of modeling coupled state across different parts of the system so that changes in one area can, in principle, influence beliefs and behavior elsewhere in a coordinated way. The term "entanglement" is used metaphorically and mathematically — the system does not run on physical quantum hardware. Instead, it borrows concepts from quantum theory — Hilbert spaces, entangled subsystems, measurement — to organize how correlated belief updates and constraints propagate through embedding spaces, semantic memory, the PostgreSQL `msallisgis` GeoDB-backed spatial body (port **5432**, `postgis-forensic` container — ★ confirmed April 16, 2026; 95 GB, 742 tables, 9 schemas), the `msallis` application database (port **5432**, same `postgis-forensic` container — **no port 5433 container exists**; confirmed April 16, 2026), a WV-biased multi-collection RAG endpoint on **port 8010**, and an autonomous learner with a persistent topic graph (★★ fully restored April 1, 2026 — LEARN-01, LEARN-02, LEARN-03 all resolved; `autonomous_learner`: 21,159 records confirmed April 17, 2026).

Within the thesis, this mechanism ties together Hilbert-space geometry (Chapter 4), ChromaDB-based semantic memory (Chapter 5), the PostgreSQL GBIM/GeoDB spatial grounding (Chapter 6), the RAG pipeline (Chapter 7), the autonomous learner (Chapter 9/27), and the judge ensemble (Chapter 33). In the live system, the current implementation distinguishes between two layers:

- A **conceptual layer**, specifying how entangled sets should be defined in terms of tags, entities, and geospatial features and how updates should, in principle, propagate across collections and services.
- A **concrete layer**, consisting of a deployed RAG server with an explicit `wv_entangled_context` envelope at **port 8010**, a WV-biased retrieval function operating across multiple ChromaDB collections (including GBIM-derived spatial memory sourced from PostgreSQL `msallisgis:5432`), and an autonomous learner topic graph that tracks and increasingly shapes entangled learning trajectories — ★★ fully operational as of April 1, 2026 with the GBIM entity lifecycle loop closed via LEARN-02 fix.

The present code realizes a first full loop from entanglement envelope to observable retrieval behavior, topic-graph updates, and confirmed belief commit back into the GBIM PostgreSQL layer.

> **★ Production baseline — April 16–17, 2026:**
> - **Thesis state (Ch. 10, April 16):** 112/112 containers Up, all bound to `127.0.0.1`, zero `0.0.0.0` exposures.
> - **Current working stack (April 17):** 105 containers Up in `msallis-rebuild` + `observability` + `services-safe`. All entanglement, BBB, memory, pituitary, and LLM services active within this subset.
> - **ChromaDB v2 multi-tenant API:** 48 collections confirmed via `GET /api/v2/tenants/default_tenant/databases/default_database/collections` and cross-checked against `chroma.sqlite3` `collections` table. Host port **8002**. Embeddings table: **6,740,611 rows** total. Per-collection embedding counts are **not directly derivable** from SQLite in this schema — see §8.9 Observability Limits.
> - **Databases:** Both `msallisgis` (95 GB, 742 tables, 9 schemas) and `msallis` (92 tables) are in the `postgis-forensic` container on port **5432**. **No container exists at port 5433. All prior references to `msallis:5433` in this chapter are superseded.**
> - **GBIM entities:** Deterministic SQL from `msallisgis` for WV landowner/geometry truth; semantic GBIM entities via ChromaDB `gbim_worldview_entities` collection (5,416,521 vectors).
> - **nbb_pituitary_gland:** host port **8108**, mode `elevated`, cortisol 0.4, urgency 0.25, warmth 0.9. Source: `auto_watchdog`. GET `/global_mode` and GET `/mode_history` are the authoritative pituitary routes.
> - **BBB:** `filters_operational: 6`, `barrier_active: true`. Confirmed routes: GET `/`, GET `/health`, POST `/filter`, POST `/truth`. No `/filters` inspection route exists in this build.
> - **allis-memory:** host port **8056**, bound to 127.0.0.1. Confirmed routes include POST `/events`, GET `/health`, POST `/memory/turn`, GET `/memory/episodic/{user_id}`, GET `/memory/quests/{user_id}`, GET `/memory/sessions`, GET `/pia_window`, GET `/steg_report`. GET `/status` returns 404.
> - **LLM ensemble / main brain:** Port 8050 exposes `/chat`, `/chat/async`, `/ultimate_chat`, `/health`, `/governance/query`. Ports 8030 and 8008 confirmed. **No `/models`, `/roster`, `/llm_status`, or `/model_status` endpoint exists on any of these services** — ensemble composition is validated via test harness and 20LLM metrics only.

---

## 8.1 Motivation for Entanglement

The entanglement metaphor addresses three practical challenges that arise when Ms. Allis is expected to reason coherently across governance, geography, ethics, and specific benefit and service domains.

**Cross-domain coupling.** Governance rules, geospatial realities, benefit eligibility criteria, and ethical principles are not independent; a change in one domain should influence reasoning in others. In the current deployment, a change to floodplain policy, a mental-health benefit rule, or a local-resource verification entry is intended to affect beliefs about specific structures, parcels, providers, and communities represented in the PostgreSQL GeoDB/PostGIS and GBIM layers — including `gbim_beliefs_v2` sourced from PostgreSQL `msallisgis` (port **5432**) and GBIM entities queryable through ChromaDB `gbim_worldview_entities` (5,416,521 vectors) — and to influence how the RAG service on port 8010 ranks and filters documents across multiple collections, rather than leaving such changes as abstract rules disconnected from place and practice. ★★ As of April 1, 2026, autonomous learner beliefs generated through daily learning cycles are also committed as GBIM entities via the LEARN-02 fix, meaning the learner's community knowledge contributions are now fully entangled with the GBIM layer.

**Consistency over time.** The design intends that when Ms. Allis learns or corrects something important — a new governance norm, a spatial boundary correction in `msallisgis:5432`, an updated program enrollment rule, or a revised interpretation of a principle — related beliefs should shift in a coordinated way. The goal is to avoid a situation where some parts of the system (one ChromaDB collection or one service) reflect the update while others silently retain outdated assumptions. In the current deployment, consistency is enforced at retrieval time via the entanglement envelope and bias function; full cross-collection write propagation is explicitly marked as future work.

**Constraint and bias propagation.** In the current deployment, constitutional, ethical, and WV-specific design constraints enter at the retrieval level via the entangled RAG path on port 8010. The design intends that if a principle or place-based priority changes, the queries, retrievals, and downstream reasoning that touch the affected regions, programs, or communities will be influenced accordingly. Propagation at the generative level — direct weight updates in language models — remains future work.

---

## 8.2 Formal Embedding, Tag, and Envelope Model

Formally, Ms. Allis's internal semantic state and retrieval metadata are modeled in a way that mirrors the Hilbert-space formalism familiar from quantum mechanics, adapted for vector embeddings, tags, and entanglement envelopes.

**State space.** Let \(\mathcal{V}\) be the embedding space, treated as a real Hilbert space where each item \(x_i\) is represented by a vector \(v_i \in \mathcal{V}\). Inner products and norms encode similarity and magnitude, and neighborhoods in this space reflect semantic relatedness as captured by the embedding model (`all-minilm:latest`, 384-dim, `hnsw:space: cosine`) and stored by ChromaDB across 48 active collections (6,740,611 total embedding rows — confirmed April 17, 2026 via SQLite `COUNT(*)`; per-collection breakdown not derivable from raw SQL in this schema — see §8.9).

**Metadata and tags.** Each item \(x_i\) is associated with metadata: a tag set \(T_i \subseteq \mathcal{T}\), where \(\mathcal{T}\) is the universe of tags (domains such as health or transportation; ethical principles; GBIM entities from PostgreSQL `msallisgis:5432`; GeoDB features such as parcels or providers; datasets; and service categories). Optional scalar weights \(w_i \in \mathbb{R}_{>0}\) used during ranking or scheduling can be adjusted as beliefs change or as certain items become more or less trusted or relevant.

**Correlation / "entanglement" sets.** For an "anchor" item \(x_a\), define a correlation tag set \(C_a \subseteq \mathcal{T}\) encoding the tags that should induce coupling. The entangled set for \(x_a\) is then

\[
S_a = \{ x_j \mid T_j \cap C_a \neq \emptyset \}.
\]

Intuitively, \(S_a\) is the set of items that share critical tags with \(x_a\) and are therefore treated as correlated or entangled; these are the items whose retrieval behavior or weights should co-evolve when the anchor is updated, including documents describing specific counties, providers, or infrastructure segments in West Virginia sourced from `msallisgis:5432`.

**WV entangled context envelope.** In the current deployment, this conceptual structure is instantiated as a JSON object called `wv_entangled_context` that appears explicitly in the RAG server's `/search` API on **port 8010**. The canonical schema for this envelope includes: `domains` (thematic domains active in the current query), `principles` (normative or design principles entangled with the query), `gbim_entity_ids` and `gbim_entities` (identifiers and descriptors for GBIM entities from `msallisgis`), `geodb_features` (objects each containing `feature_id`, `layer`, `county`, `state`, `geometry_ref`, and optional `attributes`), and `metadata` (annotating the envelope with `source_agent`, `run_id`, and `timestamp`). This envelope is the concrete, structured description of the entangled subspace relevant to a particular question: it is the thing that is "measured" against during WV-biased retrieval.

---

## 8.3 Conceptual Entanglement Update Rule

> *This section describes design intent. The update rule below serves as a conceptual and analytical framing; full cross-service weight and embedding updates are future work. Concrete behaviors currently implemented appear at retrieval time (§8.4) and in topic scheduling (§8.5). The LEARN-02 fix (April 1, 2026) partially closes this loop for autonomous learner beliefs — see §8.5 addendum.*

When an important anchor is updated — a governance rule, a spatial boundary in `msallisgis:5432`, a benefit-program constraint, or a key norm — the design intends that Ms. Allis will apply an entanglement update to the correlated set rather than only mutating the single item.

**Step 1 – Identify the entangled set.** Given anchor \(x_a\) and its correlation tags \(C_a\), compute

\[
S_a = \{ x_j \mid T_j \cap C_a \neq \emptyset \}
\]

using the current metadata store (tags in ChromaDB, GBIM entity links to `msallisgis:5432`, and any entity or feature catalogs maintained in the system).

**Step 2 – Compute coupling strengths.** For each \(x_j \in S_a\), compute a coupling strength \(\lambda_j\) measuring how tightly \(x_j\) is entangled with \(x_a\). A simple heuristic is tag-overlap fraction:

\[
\lambda_j = \frac{|T_j \cap C_a|}{|C_a|},
\]

which is large when \(x_j\) carries many of the anchor's critical tags.

**Step 3 – Apply correlated updates.** When \(x_a\) receives an update, induce proportional updates to each \(x_j \in S_a\):

- Adjusting the weight \(w_j\) for retrieval or scheduling.
- Shifting the embedding \(v_j\) in a direction correlated with the shift to \(v_a\).
- Flagging \(x_j\) for re-processing, re-indexing, or human review.
- Logging the update for inspection and governance, durable at `allis-memory:8056` (secured March 28, 2026; `_auth()` confirmed; `ALLIS_API_KEY` set).

**Step 4 – Log and audit.** Record the anchor, the entangled set, the coupling strengths, and the applied updates in `allis-memory:8056`. All entanglement update events that touch the BBB filter path are persistently logged and queryable. The BBB's `/truth` endpoint provides a structured aggregate verdict (see §8.10.3) that can serve as a post-update consistency check.

---

## 8.4 Concrete Entanglement in RAG: WV-Biased Multi-Collection Retrieval

In the live system, the most concretely realized form of entanglement appears in the WV-biased retrieval service (`allis-wv-entangled-gateway`) on **port 8010** (★★ confirmed ✅ Running, 105 containers Up, April 17, 2026).

> **⚠️ Embedding Model Lock — Confirmed March 25–26, 2026, re-confirmed April 17, 2026:**
> All ChromaDB collections queried by `allis-wv-entangled-gateway` (port 8010) use **384-dimensional vectors** produced by **`all-minilm:latest`** (`hnsw:space: cosine`). The `nomic-embed-text` model produces 768-dimensional vectors and is **incompatible** with all existing collections. Any query, script, or migration generating embeddings for use with port 8010 **must** use `all-minilm:latest`.

> **⚠️ ChromaDB v2 Multi-Tenant API Required — Confirmed March 22, 2026, re-confirmed April 17, 2026:**
> ChromaDB is running the **v2 multi-tenant API**. The `/api/v1/collections` endpoint returns an "Unimplemented: v1 deprecated" error. The path `/api/v2/collections` returns 404 — it is not the correct listing path. The authoritative REST path for listing all collections is:
>
> ```
> GET /api/v2/tenants/default_tenant/databases/default_database/collections
> ```
>
> Collection queries must use:
>
> ```
> http://allis-chroma:8000/api/v2/tenants/default_tenant/databases/default_database/collections/{name}/query
> ```
>
> Host-side access uses port **8002** (`127.0.0.1:8002`). Container-to-container calls use `allis-chroma:8000`.

**Collection health verification — dual-source cross-check (April 17, 2026):**

Collection health is verified in two ways:

1. `GET /api/v2/tenants/default_tenant/databases/default_database/collections` — the v2 manifest.
2. Direct SQL on `chroma.sqlite3`: `SELECT name FROM collections ORDER BY name;`

These two sources are cross-checked during entanglement verification to catch volume/backup discrepancies. Any collection appearing in one source but not the other is flagged for investigation before being treated as authoritative.

**Collection inventory — April 17, 2026 (confirmed via v2 manifest and SQLite cross-check):**

The live Chroma instance contains the full expected collection set, verified as present in both the v2 manifest and the `collections` table. Key confirmed collections include:

| Collection | Role |
|---|---|
| `ms_allis_memory` | Session and episodic memory |
| `ms_allis_identity` | Constitutional identity documents (8 seeded) |
| `ms_allis_docs` | System documentation (7,465+ items) |
| `geospatial_features` | WV geospatial feature embeddings |
| `address_points` | WV address point index |
| `zcta_centroids` | ZIP code tabulation area centroids |
| `local_resources` | Local community resources |
| `health_rag` | Health domain RAG corpus |
| `economic_rag` | Economic domain RAG corpus |
| `psychological_rag` | Psychological RAG corpus (968 docs, restored March 28) |
| `news_rag` | News domain RAG corpus |
| `governance_rag` | MountainShares DAO + US Constitution (643 chunks) |
| `spiritual_texts` | Spiritual text corpus |
| `spiritual_knowledge` | Spiritual knowledge RAG |
| `appalachian_english_corpus` | Appalachian language and dialect corpus |
| `fifth_dgm_subconscious` | Fifth DGM subconscious queue (384-dim HNSW, live collection) |
| `operations_history` | System operations log |
| `gbim_worldview_entities` | 5,416,521 GBIM semantic entities |
| `autonomous_learner` | 21,159 records (April 17, 2026) |
| `appalachian_cultural_intelligence` | 820 items |
| `aaacpe_corpus` | 65 docs (distinct from above) |
| `GBIM_Fayette_sample` | 1,535 items — metadata enrichment pending (OI-19) |
| `geospatialfeatures` | 60,000 items — metadata enrichment pending (OI-19) |
| `gbim_beliefs_v2` | Spatial GBIM beliefs — item count unverified (OI-21) |
| `commons_rag` | Commons governance + gamification (306 chunks) |
| *(additional collections)* | See Chapter 41 for the full 48-collection manifest |

The exact count of 48 collections is described as the "verified collection list from the v2 manifest and SQLite cross-check" — not any earlier number derived from the now-deprecated v1 endpoint.

**Endpoint and schema.** The service exposes a `/search` endpoint accepting a natural-language query, a `top_k` parameter, and an optional `wv_entangled_context` envelope as a JSON object conforming to a formal Pydantic schema enforced at runtime.

**WV-biased ranking.** The core entanglement operation is a bias function that operates over the union of retrieved items from all collections. For each item \(x_j\), the function inspects the item's metadata for West Virginia-related tags and identifiers (county, state, GBIM entities from `msallisgis:5432`, GeoDB features). If the `wv_entangled_context` envelope is populated with `geodb_features`, `gbim_entity_ids`, or `domains`, and \(x_j\) shares any of those tags, a positive boost is applied to its score. Items without relevant tags receive no boost. ★★ As of April 1, 2026, `autonomous_learner` beliefs committed as GBIM entities carry `source: autonomous_learner` and GBIM entity metadata, making them eligible for WV-tag boosting in this bias function.

**Example `/search` call (confirmed port 8010, April 17, 2026):**

```bash
curl -X POST http://127.0.0.1:8010/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Fayette County land ownership and benefit facilities",
    "top_k": 10,
    "wv_entangled_context": {
      "domains": ["land_ownership", "benefits", "spatial"],
      "principles": ["equity", "transparency"],
      "gbim_entity_ids": ["fayette_county_wv"],
      "gbim_entities": ["Fayette County WV"],
      "geodb_features": [
        {
          "feature_id": "fayette_001",
          "layer": "county_boundary",
          "county": "Fayette",
          "state": "WV",
          "geometry_ref": "msallisgis.county_boundaries"
        }
      ],
      "metadata": {
        "source_agent": "main_brain",
        "run_id": "run_20260417_001",
        "timestamp": "2026-04-17T07:00:00Z"
      }
    }
  }'
```

> All embedding calls from this service use `all-minilm:latest` (384-dim, cosine). Both `msallisgis` and `msallis` are in `postgis-forensic` on port **5432**. No port 5433 container exists.

**Health check:**

```bash
# Confirm port 8010 is Up and bound to 127.0.0.1:
curl -s http://127.0.0.1:8010/health
# Expected: {"status": "ok"} or similar

# Confirm no 0.0.0.0 exposure:
docker ps --format "{{.Names}}\t{{.Ports}}" | grep entangled
# Expected: 127.0.0.1:8010->8010/tcp — no 0.0.0.0
```

---

## 8.5 Entanglement Scaffolding in the Autonomous Learner

The autonomous learner service (`allis-autonomous-learner`) implements a complementary notion of entanglement at the level of topics and learning trajectories. ★★ As of April 1, 2026, the autonomous learner is fully restored (LEARN-01, LEARN-02, LEARN-03 resolved) with **21,159 records** in the `autonomous_learner` ChromaDB collection confirmed April 17, 2026.

**Topic graph structure.** The learner maintains a JSON-backed topic graph (`topic_graph.json`) encoding an adjacency structure over topics. Each node represents a topic the system has studied or is scheduled to study; edges connect related topics with weights reflecting co-occurrence, co-retrieval, or other measures of relatedness observed across learning cycles and RAG calls.

**Per-cycle entanglement updates.** At the end of each learning cycle, the learner calls an entanglement update hook. This hook identifies neighbors of the current topic and updates the topic graph's edge weights accordingly before persisting the updated graph back to disk.

```python
# Autonomous learner — per-cycle entanglement update hook (★★ updated April 1, 2026)
# LEARN-01 fix: float32 cast applied to all cosine_similarity calls
import json
import numpy as np

def cosine_similarity(a, b) -> float:
    """★★ LEARN-01 fix: explicit float32 cast prevents dtype mismatch."""
    a = np.array(a, dtype=np.float32)
    b = np.array(b, dtype=np.float32)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))

def update_entanglement(
    graph: dict,
    current_topic: str,
    co_retrieved_topics: list,
    weight_increment: float = 0.1
) -> dict:
    if current_topic not in graph:
        graph[current_topic] = {}
    for neighbor in co_retrieved_topics:
        current_weight = graph[current_topic].get(neighbor, 0.0)
        graph[current_topic][neighbor] = round(current_weight + weight_increment, 4)
    return graph
```

### ★★ §8.5 Addendum — LEARN-02: Learner → GBIM Entanglement Loop Closed

Prior to April 1, 2026, autonomous learner beliefs were committed to ChromaDB only — not to the GBIM PostgreSQL layer. The **LEARN-02 fix** corrected the learner's `POST /route` payload to `gbim_query_router:7205`, changing a mis-shaped nested `payload.query` structure to the correct top-level `query` field. After this fix, new learner beliefs are committed to both ChromaDB `autonomous_learner` and `msallisgis:5432` as GBIM entities with `confidence_decay` metadata. These GBIM-committed beliefs become eligible for WV-tag boosting in `allis-wv-entangled-gateway` (port 8010) retrieval traces.

**Two-phase commit protocol (post-LEARN-02):**

```python
# ★★ Post-LEARN-02 two-phase commit pattern (April 1, 2026):
router_payload = {
    "query": belief_text,        # TOP-LEVEL — not nested under "payload"
    "user_id": self.user_id,
    "context": belief_metadata
}
# Step 1: Write to ChromaDB with gbim_committed: False
# Step 2: POST to gbim_query_router:7205/route
# Step 3: On HTTP 200, update ChromaDB metadata: gbim_committed: True
```

---

## 8.6 Planned Neighbor-Biased Topic Selection

> *This section describes future work / design intent only.*

The next planned step is to let the topic graph actively influence which topics the autonomous learner studies next. For the current topic, the learner would retrieve its neighbors from `topic_graph.json` and rank them by edge weight. This causes the learner to dwell in and repeatedly revisit strongly entangled regions of the topic graph.

```python
# Future: neighbor-biased topic selection — NOT YET DEPLOYED
import random

def select_next_topic(
    graph: dict,
    current_topic: str,
    topic_queue: list,
    exploration_rate: float = 0.15
) -> str:
    neighbors = graph.get(current_topic, {})
    if neighbors and random.random() > exploration_rate:
        return max(neighbors, key=neighbors.get)
    elif topic_queue:
        return random.choice(topic_queue)
    else:
        return current_topic
```

---

## 8.7 Interaction with GeoDB, GBIM, and Multi-Collection Memory

In the current deployment, entanglement interacts closely with both the RAG pipeline on port 8010 and the PostgreSQL GeoDB/GBIM layers through the following mechanisms.

**Tags and spatial identifiers in metadata.** Documents in ChromaDB collections queried at port 8010 are increasingly annotated with tags and metadata fields that reference GBIM entities from `msallisgis:5432`, GeoDB features, counties, and states. These fields form the backbone of entangled sets and are what the WV-biased retrieval function inspects when applying coupling strengths. Metadata enrichment of `gbim_beliefs_v2`, `GBIM_Fayette_sample`, and `geospatialfeatures` remains near-term work tracked as OI-19.

> **⚠️ Confirmed metadata coverage gap (OI-19 — Open as of April 17, 2026):** `GBIM_Fayette_sample` (1,535 items) and `geospatialfeatures` (60,000 items) are live in Chroma but their WV-tag metadata coverage for entanglement biasing has not yet been fully verified. Until WV-tag metadata is confirmed present and correct in these collections, the bias function in `allis-wv-entangled-gateway` may not reliably boost results from these collections even when a WV-scoped query with a populated `wv_entangled_context` envelope is submitted. OI-21 (`gbim_beliefs_v2` item count unverified) also remains Open.

**Multi-collection entangled retrieval.** By querying multiple collections and globally ranking results under the influence of the entanglement envelope, the RAG server on port 8010 treats GBIM, GeoDB, autonomous learner knowledge, and application-specific collections as a single, coupled state for the purposes of each query.

**Bridging to the autonomous learner.** ★★ With the LEARN-02 fix in place, the full entanglement lifecycle for community learning is: learner fires a learning cycle → queries entangled RAG at port 8010 → co-retrieved topics strengthen topic graph edges → belief committed to both ChromaDB `autonomous_learner` and `msallisgis:5432` as a GBIM entity → that GBIM entity becomes eligible for WV-tag boosting in future port 8010 queries.

**Four-database and entanglement service reference (★★ April 17, 2026):**

```python
DATABASE_PORTS = {
    "msallisgis": 5432,         # PostGIS spatial — 95 GB, 742 tables, 9 schemas
    "msallis": 5432,            # Application DB — 92 tables — SAME postgis-forensic container
                                  # NO port 5433 container exists — all prior 5433 refs superseded
    "local_resources": 5435,     # allis-local-resources-db
    "chroma_host": 8002,         # Host-facing ChromaDB port
                                  # 48 collections / 6,740,611 embedding rows (SQLite COUNT*)
    "chroma_container": 8000,    # Container-internal ChromaDB port
    "wv_entangled_gateway": 8010,
    "gbim_query_router": 7205,   # LEARN-02 fix — learner → GBIM lifecycle restored
}

# ChromaDB v2 multi-tenant API paths:
CHROMA_V2_BASE = (
    "http://allis-chroma:8000"
    "/api/v2/tenants/default_tenant/databases/default_database"
)
CHROMA_COLLECTIONS_LIST = CHROMA_V2_BASE + "/collections"
CHROMA_COLLECTION_QUERY = CHROMA_V2_BASE + "/collections/{name}/query"
# /api/v1/collections → "Unimplemented: v1 deprecated"
# /api/v2/collections → 404 (not the correct multi-tenant path)
```

---

## 8.8 Distinguishing Metaphor from Implementation

To maintain academic rigor and avoid over-claiming, the following summary distinguishes clearly between metaphorical design framing and current implementation.

**Metaphor and design framing (conceptual layer).** The use of "entanglement" to describe correlated belief updates and retrieval biases across governance, ethics, space, and service domains. The treatment of the embedding state as a Hilbert-like space with entangled subsystems and measurement-like retrieval operations. The specification of tag- and entity-based entanglement in which correlated items \(S_a\) are identified via shared tags and are intended to be updated together through weight and embedding adjustments.

**Concrete implementation in the current deployment (★★ April 17, 2026):**

- A formal JSON schema and Pydantic model for `WVEntangledContext`, enforced in the running RAG server at **port 8010** (confirmed ✅ Running, bound to `127.0.0.1`, April 17, 2026).
- A WV-biased, multi-collection retrieval path that uses the entanglement envelope to modulate scores across 48 ChromaDB collections — collection inventory confirmed via v2 manifest and SQLite cross-check.
- All ChromaDB queries from this service use **`all-minilm:latest` (384-dim, `hnsw:space: cosine`)** and the **ChromaDB v2 multi-tenant API** (`/api/v1/` deprecated; `/api/v2/collections` is 404 — use full multi-tenant path).
- The service logs both pre-bias and post-bias rankings for inspection.
- A JSON-backed topic graph maintained by `allis-autonomous-learner` — ★★ **fully restored April 1, 2026** (LEARN-01, LEARN-02, LEARN-03 resolved); **21,159 records** confirmed April 17, 2026.
- ★★ **LEARN-02 fix closes the learner → GBIM entanglement loop:** autonomous learner beliefs are now committed as GBIM entities in `msallisgis:5432` via the `postgis-forensic` container, making them eligible for WV-tag boosting in port 8010 retrieval traces.
- ★ `allis-memory:8056` provides a durable, authenticated audit trail for all entanglement-adjacent BBB gate decisions — `_auth()` confirmed, `ALLIS_API_KEY` set.
- ★ **48 active ChromaDB collections / 6,740,611 total embedding rows** confirmed April 17, 2026 via v2 manifest + SQLite cross-check.

**Future work / design intent only:**

- Neighbor-biased topic selection using the topic graph (§8.6).
- Full cross-service weight and embedding updates implementing the entanglement update rule of §8.3.
- Enriched ChromaDB metadata coverage so WV-aligned documents in `gbim_beliefs_v2`, `GBIM_Fayette_sample`, and `geospatialfeatures` are reliably boosted in entangled retrieval traces (OI-19 Open).
- Verification and resolution of `gbim_beliefs_v2` item count (OI-21 Open).
- Projection-like vector operations across entangled subsets.
- Integration of entangled retrieval traces into governance dashboards.

---

## 8.9 Observability Limits — Explicit Statement

The April 17, 2026 audit established the following observability limits. These limits apply to any section of the thesis that makes claims about entanglement depth, collection population, or subconscious queue size.

**1. Per-collection embedding counts are not directly derivable from SQLite.**

The current Chroma schema does not include a `collection_id` column on the `embeddings` table. Therefore:

- `SELECT COUNT(*) FROM embeddings;` → **6,740,611 rows** — proves the overall vector space is heavily populated. ✅
- `SELECT COUNT(*) FROM embeddings WHERE collection_id = '...';` → **not a valid query in this schema.** ❌

Collection membership is resolved through Chroma's internal segment metadata, not the raw SQLite `embeddings` table. Any documentation that previously implied per-collection embedding counts could be derived from raw SQL is incorrect and superseded by this statement.

**The correct audit methodology is:**

| Question | Answer source |
|---|---|
| Is the DB populated? | `COUNT(*)` on `embeddings` table (6,740,611 confirmed) |
| Does a specific collection exist? | v2 manifest `GET /api/v2/tenants/default_tenant/databases/default_database/collections` AND `SELECT name FROM collections ORDER BY name;` cross-check |
| How many embeddings per collection? | **Not derivable from raw SQLite in this schema** — use Chroma Python client `collection.count()` via the v2 API |
| Is a collection correctly wired? | Service health (`/health`), behavior endpoint calls, and log inspection |

**2. The Fifth DGM's `i_container_size` is the authoritative indicator of subconscious queue depth.**

Because per-collection embedding counts are not directly auditable from SQLite, the thesis does not claim a specific population count for `fifth_dgm_subconscious` based on SQL queries. Instead:

- `GET http://127.0.0.1:4002/consciousness_stats` → `i_container_size` field is the authoritative measure of how many items are in the Fifth DGM's subconscious queue.
- At audit time (April 17, 2026), `i_container_size` was **0**. The collection exists and has correct 384-dim HNSW settings — visible in the v2 manifest and `collections` table — but the queue is empty in this epoch. This is correct and expected behavior; see Chapter 9 §9.3.3.

**3. Ensemble composition is not auditable via REST.**

Ports 8050, 8030, and 8008 all return 404 for `/models`, `/roster`, `/llm_status`, `/model_status`, and `/status`. Ensemble size and composition are validated via the test harness and 20LLM metrics path, not a public roster endpoint.

---

## 8.10 Cross-Subsystem Verification Methodology — April 17, 2026

The entanglement verification used in this chapter employs a multi-layer approach. Single-endpoint checks are insufficient; all subsystems require cross-source confirmation.

### 8.10.1 Chroma Verification (Two-Source Cross-Check)

```bash
# Layer 1 — v2 REST manifest:
curl -s "http://127.0.0.1:8002/api/v2/tenants/default_tenant/databases/default_database/collections" \
  | python3 -m json.tool | grep '"name"'

# Layer 2 — SQLite direct:
sqlite3 /path/to/chroma.sqlite3 "SELECT name FROM collections ORDER BY name;"

# Layer 3 — Total embedding population:
sqlite3 /path/to/chroma.sqlite3 "SELECT COUNT(*) FROM embeddings;"
# Expected: 6,740,611 (April 17, 2026)

# NOTE: Per-collection counts are NOT derivable from raw SQL in this schema.
# Use Chroma Python client collection.count() for per-collection counts.
```

### 8.10.2 allis-memory Verification

```bash
# Confirm confirmed routes:
curl -s http://127.0.0.1:8056/health
curl -s http://127.0.0.1:8056/memory/sessions
curl -s http://127.0.0.1:8056/pia_window
curl -s http://127.0.0.1:8056/steg_report

# /status returns 404 — confirmed, not a valid route in this build

# Confirm /memory/turn write semantics — requires BOTH sides of exchange:
curl -X POST http://127.0.0.1:8056/memory/turn \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "cakidd",
    "session_id": "audit-session-001",
    "turn_number": 1,
    "user_message": "Entanglement verification test",
    "assistant_response": "Acknowledged. Logging turn.",
    "topic": "system_audit",
    "source": "entanglement_chapter"
  }'
# Expected: {"stored": true, "session_id": "...", "userid": "internal"}

# NOTE: GET /memory/episodic/{user_id} may legitimately return
# {"status": "no_episodic_memory"} for users that haven't crossed
# consolidation thresholds, even if their turns have been stored.
# GET /memory/quests/{user_id} returns a list of quest IDs and a count;
# an empty list is valid and complete for a new user.
```

### 8.10.3 BBB Verification

```bash
# Confirmed BBB routes — April 17, 2026:
# GET /       — root description (4 named filters + 2 additional from health/logs)
# GET /health — filters_operational: 6, barrier_active: true
# POST /filter — main filtering endpoint
# POST /truth  — truth/content evaluation endpoint

# There is no /filters inspection route in this build.
# Filter details are inferred from health, root metadata, /truth, and logs.

# /health — confirms 6 filters operational:
curl -s http://127.0.0.1:8016/health
# Expected: {"barrier_active": true, "filters_operational": 6, ...}

# /truth — expects "content" field (NOT "claim"):
curl -X POST http://127.0.0.1:8016/truth \
  -H "Content-Type: application/json" \
  -d '{"content": "West Virginia cooperative governance narrative"}'
# Expected: {"valid": true, "confidence": 0.9, "principal_reasons": ["all BBB filters passed"]}
# Missing "content" → FastAPI validation error (422)

# The six filters confirmed for this build:
# 1. EthicalFilter        — Biblical principles
# 2. SpiritualFilter      — Wisdom alignment
# 3. SafetyMonitor (AU-02v2) — Technical security
# 4. ThreatDetection      — Community protection
# 5. Steganography / prompt-injection detection
#    (log evidence: {'type': 'prompt_injection_keywords',
#                    'detail': ['system prompt', 'jailbreak'],
#                    'severity': 'critical'})
# 6. TruthVerification    — via POST /truth; aggregates results of all filters;
#    returns valid, confidence, principal_reasons
```

### 8.10.4 Pituitary Verification

```bash
# Confirmed pituitary routes — April 17, 2026:
# GET /          — basic info
# GET /health
# GET /global_mode   ← authoritative current mode
# GET /mode_history  ← history of mode changes
# POST /process
# POST /set_mode
# POST /chat

# NOTE: /globalmode (no underscore) returns 404. Always use /global_mode.

curl -s http://127.0.0.1:8108/global_mode
# Expected at audit time:
# {
#   "mode": "elevated",
#   "cortisol": 0.4,
#   "urgency": 0.25,
#   "warmth": 0.9,
#   "source": "auto_watchdog"
# }

curl -s http://127.0.0.1:8108/mode_history
# Returns history of mode transitions with timestamps
```

### 8.10.5 LLM Ensemble / Main Brain Verification

```bash
# Confirmed routes by service — April 17, 2026:

# Port 8050 (allis-main-brain / unified gateway):
# /chat, /chat/async, /chat/status/{job_id}, /chat/cancel/...,
# /governance/query, /ultimate_chat, /health

# Port 8030 (semaphore / broadcast layer):
# /acquire, /broadcast, /proxy, /release, /semaphore_status, /health

# Port 8008 (20LLM ensemble service):
# /chat, /chat_with_context, /quick_chat,
# /cached_expert_responses, /metrics, /health

# ALL THREE return 404 for:
# /models, /model_status, /llm_status, /roster, /status

# Ensemble size and composition must be validated via test harness
# and 20LLM /metrics endpoint — NOT a public roster endpoint.
# This is intentional in the hardened build.

curl -s http://127.0.0.1:8008/health
curl -s http://127.0.0.1:8050/health
curl -s http://127.0.0.1:8030/health
```

### 8.10.6 Logs as Final Confirmation Layer

Service logs provide the fourth and final verification layer for the following where REST endpoints alone are insufficient:

- **BBB steganography / prompt-injection filter (filter 5):** Confirmed via log entries showing `{'type': 'prompt_injection_keywords', 'detail': ['system prompt', 'jailbreak'], 'severity': 'critical'}`.
- **DGM activity and subconscious routing:** Confirmed via `consciousness_stats` endpoint and logs showing `stored_in_subconscious: 1`, `last_woah_evaluation: 2026-04-17T11:18:19`.
- **Memory turn storage:** Confirmed via `allis-memory` logs showing write confirmations with `stored: true` and session normalization behavior.
- **Pituitary mode transitions:** Confirmed via `/mode_history` and watchdog logs showing `source: auto_watchdog` mode updates.

---

## 8.11 Summary

In its current state, the entanglement model serves both as a conceptual and mathematical description of how coupled state should work across Ms. Allis's belief and spatial structures, and as a description of concrete, running mechanisms.

**This chapter's description reflects the April 16–17, 2026 production state.** All prior references to `msallis:5433`, 40 collections, `/api/v1/collections`, `/api/v2/collections`, "2 collections," or any per-collection embedding count derived from raw SQLite are superseded by the April 2026 forensic baseline:

- ChromaDB: **48 collections** confirmed via v2 manifest and SQLite cross-check; **6,740,611 total embedding rows** (SQLite `COUNT(*)`); per-collection counts not derivable from raw SQL
- Both `msallisgis` (95 GB, 742 tables) and `msallis` (92 tables) in `postgis-forensic` on **port 5432**; no port 5433
- `nbb_pituitary_gland`: port 8108, mode `elevated`, cortisol 0.4, warmth 0.9; `/global_mode` and `/mode_history` are the authoritative routes
- BBB: 6 filters confirmed; routes: GET `/`, GET `/health`, POST `/filter`, POST `/truth`; no `/filters` route
- `allis-memory`: `/memory/turn` requires both `user_message` and `assistant_response`; episodic memory may legitimately return `no_episodic_memory`; GET `/status` returns 404
- LLM ensemble: no public `/models`, `/roster`, or `/llm_status` endpoint — composition validated via test harness
- `fifth_dgm_subconscious`: real collection in `default_tenant/default_database`, 384-dim HNSW, live — `i_container_size: 0` at audit time is the authoritative subconscious queue indicator
- `autonomous_learner`: 21,159 records, April 17, 2026
- Verification methodology: dual-source Chroma (v2 manifest + SQLite), service health endpoints, behavior endpoints, and logs as four independent confirmation layers

The Fifth DGM documented in Chapter 9 and the Blood-Brain Barrier documented in Chapter 16 are the primary consumers of the entangled RAG path, the pituitary mode signal, and the memory audit substrate described in this chapter. For the canonical description of how this service is called within the live `ultimatechat` and `chatlight` execution paths, see **Chapter 17**.

---

*Chapter 8 — Quantum-Inspired Entanglement and Coupled State*
*Carrie Kidd (Mamma Kidd), Mount Hope WV*

*Original entries: February–March 2026 — initial entanglement architecture, RAG port 8010, topic graph.*
*★ March 28, 2026: Security remediation; `msallisgis` port corrected from 5452 to 5432; `msallis` port 5433 restored; 40 collections / 6,675,442 vectors confirmed; `spiritual_rag` deduplicated; `psychological_rag` restored.*
*★★ April 1, 2026: LEARN-01/02/03 resolved; learner → GBIM entanglement loop closed; two-phase commit protocol added.*
*★★ April 17, 2026 — FULL REWRITE:*
*— ChromaDB API path corrected throughout: v2 multi-tenant path is `GET /api/v2/tenants/default_tenant/databases/default_database/collections`; `/api/v1/collections` deprecated; `/api/v2/collections` is 404.*
*— All "2 collections" or stale v1-derived counts removed. 48 collections confirmed via v2 + SQLite cross-check.*
*— Embeddings: 6,740,611 total rows confirmed via SQLite `COUNT(*)`; per-collection counts explicitly documented as not derivable from raw SQL.*
*— `fifth_dgm_subconscious`: documented as real collection, 384-dim HNSW; `i_container_size` is authoritative subconscious queue indicator (0 at audit).*
*— All `msallis:5433` references removed; both DBs at `postgis-forensic:5432`.*
*— `allis-memory` route surface corrected: POST `/events`, GET `/health`, POST `/memory/turn` (requires both message sides), GET `/memory/episodic/{user_id}` (may return `no_episodic_memory`), GET `/memory/quests/{user_id}`, GET `/memory/sessions`, GET `/pia_window`, GET `/steg_report`. GET `/status` → 404.*
*— BBB: 6 filters documented with names; confirmed routes: GET `/`, GET `/health`, POST `/filter`, POST `/truth` (expects `content` not `claim`); no `/filters` route.*
*— Pituitary: routes corrected — `/global_mode` (underscore, correct), `/globalmode` (no underscore, 404); `cortisol: 0.4`, `urgency: 0.25`, `warmth: 0.9`, `source: auto_watchdog` added.*
*— LLM ensemble: no public `/models`, `/roster`, `/llm_status` endpoints documented.*
*— §8.9 Observability Limits added: per-collection SQL limits, `i_container_size` as authoritative indicator, ensemble composition via test harness.*
*— §8.10 Cross-Subsystem Verification Methodology expanded to four layers: Chroma (v2 + SQLite), memory routes, BBB routes, pituitary routes, 
