# Chapter 8 — Quantum-Inspired Entanglement and Coupled State

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: ★★ April 23, 2026 — ChromaDB inter-service URL corrected to
`allis-chroma:8000`, API v2 full paths throughout, UUID two-step count pattern
documented, `allis-gbim-query-router` port 7205 confirmed, GIS-RAG v0.4.0 (port 8004)
added, collection names corrected (`msallis_docs`, `ms_allis_memory`,
`gbim_worldview_entities`), collection count updated to 48 with historical note,
`autonomous_learner` updated to 21,181 items, distance metrics cross-checked,
OI-E closed, Ch. 02 filename corrected to `02-ms-allis-gbim.md`, container count
date-stamped.*

---

This chapter presents the quantum-inspired entanglement mechanism used in Ms. Allis: a
structured way of modeling coupled state across different parts of the system so that
changes in one area can, in principle, influence beliefs and behavior elsewhere in a
coordinated way. The term "entanglement" is used metaphorically and mathematically — the
system does not run on physical quantum hardware. Instead, it borrows concepts from
quantum theory — Hilbert spaces, entangled subsystems, measurement — to organize how
correlated belief updates and constraints propagate through embedding spaces, semantic
memory, the PostgreSQL `msallisgis` spatial body (two-container architecture: production
`msallis-db` on host port **5433** / container port **5432**, and forensic
`postgis-forensic` on host port **5432** — both confirmed April 23, 2026; see §8.7), a
WV-biased multi-collection RAG endpoint on **port 8010**, GIS-RAG v0.4.0 on **port 8004**
(204 WV GIS datasets, 7,357 WV bridges), and an autonomous learner with a persistent
topic graph (★★ fully restored April 1, 2026 — LEARN-01, LEARN-02, LEARN-03 all
resolved; `autonomous_learner` ChromaDB collection: **21,181 records** confirmed
April 23, 2026, L2 distance).

Within the thesis, this mechanism ties together Hilbert-space geometry (Chapter 4),
ChromaDB-based semantic memory (Chapter 5), the PostgreSQL GBIM spatial grounding
(`02-ms-allis-gbim.md`, Chapter 6), the RAG pipeline (Chapter 7), the autonomous
learner (Chapter 9/27), and the judge ensemble (Chapter 33). In the live `msallis-rebuild`
system, the current implementation distinguishes between two layers:

- A **conceptual layer**, specifying how entangled sets should be defined in terms of
  tags, entities, and geospatial features and how updates should, in principle, propagate
  across collections and services.
- A **concrete layer**, consisting of a deployed RAG server with an explicit
  `wv_entangled_context` envelope at **port 8010**, a WV-biased retrieval function
  operating across multiple ChromaDB collections (including GBIM-derived spatial memory
  sourced from `msallisgis` on `msallis-db`, host 5433 / container 5432), GIS-RAG
  v0.4.0 at **port 8004** (204 WV GIS datasets, 7,357 WV bridges), and an autonomous
  learner topic graph that tracks and increasingly shapes entangled learning trajectories
  — ★★ fully operational as of April 1, 2026 with the GBIM entity lifecycle loop closed
  via LEARN-02 fix.

The present code realizes a first full loop from entanglement envelope to observable
retrieval behavior, topic-graph updates, and confirmed belief commit back into the GBIM
PostgreSQL layer.

> **★ Production baseline — April 23, 2026:**
> - **Namespace:** `msallis-rebuild`. Container prefix: `allis-`.
> - **Container stack:** Healthy as of April 23, 2026. Reference count: 99+ containers
>   Up (April 17, 2026 baseline). All entanglement, BBB, memory, pituitary, and LLM
>   services active.
> - **ChromaDB:** `allis-chroma`, host port **8002**, container port **8000**.
>   Inter-service URL (container-to-container): `http://allis-chroma:8000`.
>   **API: v2 multi-tenant ONLY** — `/api/v1/` returns 410 Gone.
>   **48 collections** confirmed via v2 manifest and SQLite cross-check (April 23, 2026;
>   historical note: 50 collections on April 17, 2026 pre-cleanup).
>   Total embedding rows: **~6,740,611** (SQLite `COUNT(*)`). Per-collection counts are
>   not directly derivable from raw SQLite — use Python client `collection.count()` which
>   handles the UUID two-step pattern transparently. Distance metrics: **37 L2 / 11 cosine**.
> - **Databases:** Two-container architecture —
>   **Production:** `msallis-db`, host **5433** / container **5432**, role `postgres`,
>   `msallisgis`, 16 GB / 294 tables / 11 schemas.
>   **Forensic:** `postgis-forensic`, host **5432**, role `allis` (+ `-h 127.0.0.1`),
>   `msallisgis`, 17 GB / 314 tables / 9 schemas — forensic auditing only.
>   **`mvw_gbim_landowner_spatial` — ✅ CLOSED: 38,979 rows, `msallis-db` (production).
>   Not present in `postgis-forensic`.**
> - **GIS-RAG v0.4.0:** port **8004** — 204 WV GIS datasets, 7,357 WV bridges.
> - **`allis-gbim-query-router`:** port **7205** — ✅ confirmed healthy, RBAC-gated,
>   `X-Allis-Role` required, LEARN-02 resolved.
> - **GBIM entities:** Deterministic SQL from `msallisgis` on `msallis-db` (host 5433)
>   for WV landowner/geometry truth; semantic GBIM entities via ChromaDB
>   `gbim_worldview_entities` collection (**L2 distance**, 5,416,521 vectors).
> - **`nbb_pituitary_gland`:** host port **8108**, mode `baseline`, cortisol 0.4,
>   urgency 0.25, warmth 0.9. Source: `auto_watchdog`. GET `/global_mode` and
>   GET `/mode_history` are the authoritative pituitary routes.
> - **BBB:** `filters_operational: 6`, `barrier_active: true`. Confirmed routes:
>   GET `/`, GET `/health`, POST `/filter`, POST `/truth`. No `/filters` inspection
>   route exists in this build.
> - **`allis-memory`:** host port **8056**, bound to `127.0.0.1`. Confirmed routes
>   include POST `/events`, GET `/health`, POST `/memory/turn`,
>   GET `/memory/episodic/{user_id}`, GET `/memory/quests/{user_id}`,
>   GET `/memory/sessions`, GET `/pia_window`, GET `/steg_report`.
>   GET `/status` returns 404.
> - **LLM ensemble / main brain:** Port 8050 exposes `/chat`, `/chat/async`,
>   `/ultimate_chat`, `/health`, `/governance/query`. Ports 8030 and 8008 confirmed.
>   **No `/models`, `/roster`, `/llm_status`, or `/model_status` endpoint exists on
>   any of these services** — ensemble composition is validated via test harness and
>   20LLM metrics only.

---

## 8.1 Motivation for Entanglement

The entanglement metaphor addresses three practical challenges that arise when Ms. Allis
is expected to reason coherently across governance, geography, ethics, and specific
benefit and service domains.

**Cross-domain coupling.** Governance rules, geospatial realities, benefit eligibility
criteria, and ethical principles are not independent; a change in one domain should
influence reasoning in others. In the current `msallis-rebuild` deployment, a change to
floodplain policy, a mental-health benefit rule, or a local-resource verification entry
is intended to affect beliefs about specific structures, parcels, providers, and
communities represented in the `msallisgis` PostgreSQL spatial body on `msallis-db`
(host 5433 / container 5432) — including `gbim_beliefs_v2` (cosine, sourced from
`msallisgis`) and GBIM entities queryable through ChromaDB `gbim_worldview_entities`
(**L2 distance**, 5,416,521 vectors) — and to influence how the RAG service on port 8010
and GIS-RAG v0.4.0 on port 8004 rank and filter documents across multiple collections,
rather than leaving such changes as abstract rules disconnected from place and practice.
★★ As of April 1, 2026, autonomous learner beliefs generated through daily learning
cycles are also committed as GBIM entities via the LEARN-02 fix, meaning the learner's
community knowledge contributions are now fully entangled with the GBIM layer.

**Consistency over time.** The design intends that when Ms. Allis learns or corrects
something important — a new governance norm, a spatial boundary correction in `msallisgis`
on `msallis-db` (host 5433), an updated program enrollment rule, or a revised
interpretation of a principle — related beliefs should shift in a coordinated way. The
goal is to avoid a situation where some parts of the system (one ChromaDB collection or
one service) reflect the update while others silently retain outdated assumptions. In the
current deployment, consistency is enforced at retrieval time via the entanglement
envelope and bias function; full cross-collection write propagation is explicitly marked
as future work.

**Constraint and bias propagation.** In the current deployment, constitutional, ethical,
and WV-specific design constraints enter at the retrieval level via the entangled RAG
path on port 8010. The design intends that if a principle or place-based priority
changes, the queries, retrievals, and downstream reasoning that touch the affected
regions, programs, or communities will be influenced accordingly. Propagation at the
generative level — direct weight updates in language models — remains future work.

---

## 8.2 Formal Embedding, Tag, and Envelope Model

Formally, Ms. Allis's internal semantic state and retrieval metadata are modeled in a
way that mirrors the Hilbert-space formalism familiar from quantum mechanics, adapted
for vector embeddings, tags, and entanglement envelopes.

**State space.** Let \(\mathcal{V}\) be the embedding space, treated as a real Hilbert
space where each item \(x_i\) is represented by a vector \(v_i \in \mathcal{V}\). Inner
products and norms encode similarity and magnitude, and neighborhoods in this space
reflect semantic relatedness as captured by the embedding model (`all-minilm:latest`,
384-dim) and stored by ChromaDB (`allis-chroma`, host port **8002**, container port
**8000**, inter-service URL `http://allis-chroma:8000`) across **48 active collections**
(~6,740,611 total embedding rows, April 23, 2026; historical note: 50 collections on
April 17, 2026 prior to deduplication cleanup; per-collection breakdown requires Python
client `collection.count()` using the v2 UUID two-step pattern — not derivable from raw
SQLite in this schema — see §8.9).

**Metadata and tags.** Each item \(x_i\) is associated with metadata: a tag set
\(T_i \subseteq \mathcal{T}\), where \(\mathcal{T}\) is the universe of tags (domains
such as health or transportation; ethical principles; GBIM entities from `msallisgis`
on `msallis-db`; spatial features such as parcels or providers; datasets; and service
categories). Optional scalar weights \(w_i \in \mathbb{R}_{>0}\) used during ranking or
scheduling can be adjusted as beliefs change or as certain items become more or less
trusted or relevant.

**Correlation / "entanglement" sets.** For an "anchor" item \(x_a\), define a
correlation tag set \(C_a \subseteq \mathcal{T}\) encoding the tags that should induce
coupling. The entangled set for \(x_a\) is then

\[
S_a = \{ x_j \mid T_j \cap C_a \neq \emptyset \}.
\]

Intuitively, \(S_a\) is the set of items that share critical tags with \(x_a\) and are
therefore treated as correlated or entangled; these are the items whose retrieval behavior
or weights should co-evolve when the anchor is updated, including documents describing
specific counties, providers, or infrastructure segments in West Virginia sourced from
`msallisgis` on `msallis-db` (host 5433 / container 5432).

**WV entangled context envelope.** In the current deployment, this conceptual structure
is instantiated as a JSON object called `wv_entangled_context` that appears explicitly
in the RAG server's `/search` API on **port 8010**. The canonical schema for this
envelope includes: `domains` (thematic domains active in the current query), `principles`
(normative or design principles entangled with the query), `gbim_entity_ids` and
`gbim_entities` (identifiers and descriptors for GBIM entities from `msallisgis` on
`msallis-db`), `geodb_features` (objects each containing `feature_id`, `layer`,
`county`, `state`, `geometry_ref`, and optional `attributes`), and `metadata` (annotating
the envelope with `source_agent`, `run_id`, and `timestamp`). This envelope is the
concrete, structured description of the entangled subspace relevant to a particular
question: it is the thing that is "measured" against during WV-biased retrieval.

---

## 8.3 Conceptual Entanglement Update Rule

> *This section describes design intent. The update rule below serves as a conceptual and
> analytical framing; full cross-service weight and embedding updates are future work.
> Concrete behaviors currently implemented appear at retrieval time (§8.4) and in topic
> scheduling (§8.5). The LEARN-02 fix (April 1, 2026) partially closes this loop for
> autonomous learner beliefs — see §8.5 addendum.*

When an important anchor is updated — a governance rule, a spatial boundary in
`msallisgis` on `msallis-db` (host 5433), a benefit-program constraint, or a key norm
— the design intends that Ms. Allis will apply an entanglement update to the correlated
set rather than only mutating the single item.

**Step 1 – Identify the entangled set.** Given anchor \(x_a\) and its correlation tags
\(C_a\), compute

\[
S_a = \{ x_j \mid T_j \cap C_a \neq \emptyset \}
\]

using the current metadata store (tags in ChromaDB, GBIM entity links to `msallisgis`
on `msallis-db`, and any entity or feature catalogs maintained in the system).

**Step 2 – Compute coupling strengths.** For each \(x_j \in S_a\), compute a coupling
strength \(\lambda_j\) measuring how tightly \(x_j\) is entangled with \(x_a\). A
simple heuristic is tag-overlap fraction:

\[
\lambda_j = \frac{|T_j \cap C_a|}{|C_a|},
\]

which is large when \(x_j\) carries many of the anchor's critical tags.

**Step 3 – Apply correlated updates.** When \(x_a\) receives an update, induce
proportional updates to each \(x_j \in S_a\):

- Adjusting the weight \(w_j\) for retrieval or scheduling.
- Shifting the embedding \(v_j\) in a direction correlated with the shift to \(v_a\).
- Flagging \(x_j\) for re-processing, re-indexing, or human review.
- Logging the update for inspection and governance, durable at `allis-memory:8056`
  (secured March 28, 2026; `_auth()` confirmed; `ALLIS_API_KEY` set).

**Step 4 – Log and audit.** Record the anchor, the entangled set, the coupling strengths,
and the applied updates in `allis-memory:8056`. All entanglement update events that
touch the BBB filter path are persistently logged and queryable. The BBB's `/truth`
endpoint provides a structured aggregate verdict (see §8.10.3) that can serve as a
post-update consistency check.

---

## 8.4 Concrete Entanglement in RAG: WV-Biased Multi-Collection Retrieval

In the live `msallis-rebuild` system, the most concretely realized form of entanglement
appears in the WV-biased retrieval service (`allis-wv-entangled-gateway`) on
**port 8010** (★★ confirmed ✅ Running, April 23, 2026), complemented by GIS-RAG v0.4.0
at **port 8004** (204 WV GIS datasets, 7,357 WV bridges).

> **⚠️ Embedding Model Lock — confirmed April 23, 2026:**
> All ChromaDB collections queried by `allis-wv-entangled-gateway` (port 8010) and
> GIS-RAG v0.4.0 (port 8004) use **384-dimensional vectors** produced by
> **`all-minilm:latest`**. The `nomic-embed-text` model produces 768-dimensional vectors
> and is **incompatible** with all existing collections. Any query, script, or migration
> generating embeddings **must** use `all-minilm:latest`.

> **⚠️ ChromaDB v2 Multi-Tenant API — ONLY — confirmed April 23, 2026:**
> `allis-chroma` is running the **v2 multi-tenant API**. `/api/v1/` returns **410 Gone**.
> `/api/v2/collections` returns 404 — not the correct listing path. The authoritative
> REST path for listing all collections is:
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
> Host-side access: port **8002** (`127.0.0.1:8002`).
> Container-to-container calls: `http://allis-chroma:8000`.
>
> **Count calls — UUID two-step pattern required (direct HTTP):**
> The v2 `/count` endpoint requires the collection UUID, not the name. Retrieve the UUID
> first, then call `/collections/{uuid}/count`. The Python client `collection.count()`
> handles this transparently and is the recommended approach.

**Collection health verification — dual-source cross-check (April 23, 2026):**

Collection health is verified in two ways:

1. `GET /api/v2/tenants/default_tenant/databases/default_database/collections` — the v2
   manifest.
2. Direct SQL on `chroma.sqlite3`:
   `SELECT name FROM collections ORDER BY name;`

These two sources are cross-checked during entanglement verification to catch
volume/backup discrepancies. Any collection appearing in one source but not the other is
flagged for investigation before being treated as authoritative.

**Collection inventory — 48 collections confirmed April 23, 2026:**

> **Historical note:** Prior drafts (April 17, 2026 SQLite audit) referenced 50
> collections / 6,740,611 rows. Two collections were removed during deduplication
> cleanup; **48 collections** is the current confirmed count.
> Distance metrics: **37 L2 / 11 cosine**.

| Collection | Distance | Role |
|:--|:--|:--|
| `ms_allis_memory` | cosine | Session and episodic memory |
| `ms_allis_identity` | cosine | Constitutional identity documents (8 seeded) |
| `msallis_docs` | cosine | System documentation (28,327+ items) |
| `geospatial_features` | **L2** | WV geospatial feature embeddings |
| `address_points` | **L2** | WV address point index |
| `zcta_centroids` | **L2** | ZIP code tabulation area centroids |
| `local_resources` | cosine | Local community resources (101 embeddings) |
| `health_rag` | cosine | Health domain RAG corpus |
| `economic_rag` | cosine | Economic domain RAG corpus |
| `psychological_rag` | cosine | Psychological RAG corpus (6,860 items) |
| `news_rag` | cosine | News domain RAG corpus |
| `governance_rag` | cosine | MountainShares DAO + US Constitution + WV Constitution (1,367 chunks) |
| `spiritual_texts` | cosine | Spiritual text corpus |
| `spiritual_knowledge` | cosine | Spiritual knowledge RAG |
| `appalachian_english_corpus` | cosine | Appalachian language and dialect corpus |
| `fifth_dgm_subconscious` | **L2** | Fifth DGM subconscious queue (384-dim HNSW, live) |
| `operations_history` | cosine | System operations log |
| `gbim_worldview_entities` | **L2** | 5,416,521 GBIM semantic entities — authoritative |
| `autonomous_learner` | **L2** | **21,181 records** (April 23, 2026) |
| `appalachian_cultural_intelligence` | cosine | 820 items |
| `aaacpe_corpus` | cosine | 65 docs, 39 sources |
| `GBIM_Fayette_sample` | **L2** | 1,535 items — metadata enrichment pending |
| `geospatialfeatures` | **L2** | 60,875 items — metadata enrichment pending |
| `gbim_beliefs_v2` | cosine | Spatial GBIM beliefs — 5,000 items, `wv_tag=true` (OI-21 ✅ closed) |
| `commons_rag` | cosine | Commons governance + gamification (306 chunks) |
| `gis_wv_benefits` | **L2** | WV benefits facilities |
| `conversation_history` | cosine | 580 embeddings — formally wired (OI-05 ✅ closed) |
| `gbim_beliefs` | — | **RETIRED** — use `gbim_worldview_entities` (L2) or `gbim_beliefs_v2` (cosine) |
| *(additional collections)* | — | See Chapter 41 for full 48-collection manifest |

> **`gbim_beliefs` (bare) is retired.** All code must reference `gbim_worldview_entities`
> (L2) or `gbim_beliefs_v2` (cosine).

**Endpoint and schema.** The `allis-wv-entangled-gateway` service (port 8010) exposes
a `/search` endpoint accepting a natural-language query, a `top_k` parameter, and an
optional `wv_entangled_context` envelope as a JSON object conforming to a formal Pydantic
schema enforced at runtime.

**WV-biased ranking.** The core entanglement operation is a bias function that operates
over the union of retrieved items from all collections. For each item \(x_j\), the
function inspects the item's metadata for West Virginia-related tags and identifiers
(county, state, GBIM entities from `msallisgis` on `msallis-db`, spatial features).
If the `wv_entangled_context` envelope is populated with `geodb_features`,
`gbim_entity_ids`, or `domains`, and \(x_j\) shares any of those tags, a positive boost
is applied to its score. Items without relevant tags receive no boost. ★★ As of
April 1, 2026, `autonomous_learner` (L2) beliefs committed as GBIM entities carry
`source: autonomous_learner` and GBIM entity metadata, making them eligible for WV-tag
boosting in this bias function.

**Example `/search` call (confirmed port 8010, April 23, 2026):**

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
        "run_id": "run_20260423_001",
        "timestamp": "2026-04-23T12:00:00Z"
      }
    }
  }'
```

> All embedding calls from this service use `all-minilm:latest` (384-dim).
> `msallisgis` production target: `msallis-db` (host 5433 / container 5432).
> Forensic target: `postgis-forensic` (host 5432) — forensic auditing only.
> **`mvw_gbim_landowner_spatial` — ✅ CLOSED: 38,979 rows, `msallis-db`. Not present
> in `postgis-forensic`.**

**Health check:**

```bash
# Confirm port 8010 is Up and bound to 127.0.0.1:
curl -s http://127.0.0.1:8010/health
# Expected: {"status": "ok"} or similar

# Confirm no 0.0.0.0 exposure:
docker ps --format "{{.Names}}\t{{.Ports}}" | grep entangled
# Expected: 127.0.0.1:8010->8010/tcp — no 0.0.0.0

# GIS-RAG v0.4.0 health check (port 8004):
curl -s http://127.0.0.1:8004/health
# Expected: {"status": "ok", "version": "0.4.0", "wv_gis_datasets": 204, "wv_bridges": 7357}
```

---

## 8.5 Entanglement Scaffolding in the Autonomous Learner

The autonomous learner service (`allis-autonomous-learner`) implements a complementary
notion of entanglement at the level of topics and learning trajectories. ★★ As of
April 1, 2026, the autonomous learner is fully restored (LEARN-01, LEARN-02, LEARN-03
resolved) with **21,181 records** in the `autonomous_learner` ChromaDB collection
(L2 distance) confirmed April 23, 2026.

**Topic graph structure.** The learner maintains a JSON-backed topic graph
(`topic_graph.json`) encoding an adjacency structure over topics. Each node represents
a topic the system has studied or is scheduled to study; edges connect related topics
with weights reflecting co-occurrence, co-retrieval, or other measures of relatedness
observed across learning cycles and RAG calls.

**Per-cycle entanglement updates.** At the end of each learning cycle, the learner calls
an entanglement update hook. This hook identifies neighbors of the current topic and
updates the topic graph's edge weights accordingly before persisting the updated graph
back to disk.

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

Prior to April 1, 2026, autonomous learner beliefs were committed to ChromaDB only — not
to the GBIM PostgreSQL layer. The **LEARN-02 fix** corrected the learner's `POST /route`
payload to `allis-gbim-query-router:7205`, changing a mis-shaped nested `payload.query`
structure to the correct top-level `query` field. After this fix, new learner beliefs are
committed to both ChromaDB `autonomous_learner` (L2) and `msallisgis` on `msallis-db`
(host 5433 / container 5432) as GBIM entities with `confidence_decay` metadata. These
GBIM-committed beliefs become eligible for WV-tag boosting in `allis-wv-entangled-gateway`
(port 8010) retrieval traces.

**Two-phase commit protocol (post-LEARN-02):**

```python
# ★★ Post-LEARN-02 two-phase commit pattern (April 1, 2026):
# Target: allis-gbim-query-router:7205 → msallisgis on msallis-db (host 5433)
router_payload = {
    "query": belief_text,        # TOP-LEVEL — not nested under "payload"
    "user_id": self.user_id,
    "context": belief_metadata
}
# Step 1: Write to ChromaDB autonomous_learner (L2) with gbim_committed: False
# Step 2: POST to allis-gbim-query-router:7205/route
# Step 3: On HTTP 200, update ChromaDB metadata: gbim_committed: True

# ChromaDB write uses Python client (handles v2 UUID two-step count transparently):
import chromadb
client = chromadb.HttpClient(host="127.0.0.1", port=8002)
# OR inter-service: chromadb.HttpClient(host="allis-chroma", port=8000)
collection = client.get_collection("autonomous_learner")  # L2 distance
```

---

## 8.6 Planned Neighbor-Biased Topic Selection

> *This section describes future work / design intent only.*

The next planned step is to let the topic graph actively influence which topics the
autonomous learner studies next. For the current topic, the learner would retrieve its
neighbors from `topic_graph.json` and rank them by edge weight. This causes the learner
to dwell in and repeatedly revisit strongly entangled regions of the topic graph.

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

In the current `msallis-rebuild` deployment, entanglement interacts closely with both the
RAG pipeline on port 8010 and the PostgreSQL `msallisgis` spatial and GBIM layers
through the following mechanisms.

**Tags and spatial identifiers in metadata.** Documents in ChromaDB collections queried
at port 8010 are increasingly annotated with tags and metadata fields that reference GBIM
entities from `msallisgis` on `msallis-db` (host 5433 / container 5432), spatial
features, counties, and states. These fields form the backbone of entangled sets and are
what the WV-biased retrieval function inspects when applying coupling strengths.
Metadata enrichment of `gbim_beliefs_v2` (cosine), `GBIM_Fayette_sample` (L2), and
`geospatialfeatures` (L2) remains near-term work.

> **⚠️ Confirmed metadata coverage gap (pending):** `GBIM_Fayette_sample` (L2,
> 1,535 items) and `geospatialfeatures` (L2, 60,875 items) are live in `allis-chroma`
> but their WV-tag metadata coverage for entanglement biasing has not yet been fully
> verified. Until WV-tag metadata is confirmed present and correct in these collections,
> the bias function in `allis-wv-entangled-gateway` may not reliably boost results from
> these collections even when a WV-scoped query with a populated `wv_entangled_context`
> envelope is submitted.

**Multi-collection entangled retrieval.** By querying multiple collections and globally
ranking results under the influence of the entanglement envelope, the RAG server on
port 8010 treats GBIM, spatial data, autonomous learner knowledge, and application-specific
collections as a single, coupled state for the purposes of each query.

**Bridging to the autonomous learner.** ★★ With the LEARN-02 fix in place, the full
entanglement lifecycle for community learning is: learner fires a learning cycle →
queries entangled RAG at port 8010 → co-retrieved topics strengthen topic graph edges
→ belief committed to both ChromaDB `autonomous_learner` (L2) and `msallisgis` on
`msallis-db` (host 5433 / container 5432) as a GBIM entity → that GBIM entity becomes
eligible for WV-tag boosting in future port 8010 queries.

**Service reference — `msallis-rebuild` stack (★★ April 23, 2026):**

```python
DATABASE_PORTS = {
    # Production: msallis-db — host 5433 / container 5432 / database msallisgis
    # Use for: GBIM belief graph, spatial queries, landowner routing, decay loop
    # mvw_gbim_landowner_spatial: ✅ CLOSED — 38,979 rows, msallis-db only
    "msallisgis_production_host": 5433,
    "msallisgis_production_container": 5432,

    # Forensic: postgis-forensic — host 5432 / role allis / database msallisgis
    # Use for: forensic auditing and migration validation ONLY
    # mvw_gbim_landowner_spatial NOT present in this container
    "msallisgis_forensic_host": 5452,    # NOTE: port 5452 is INVALID — forensic is 5432

    "local_resources": 5435,             # allis-local-resources-db
    "chroma_host": 8002,                 # allis-chroma host-mapped port
    "chroma_container": 8000,            # allis-chroma container-internal port
    # inter-service URL: http://allis-chroma:8000
    # 48 collections (April 23, 2026) / ~6,740,611 embedding rows
    # Distance metrics: 37 L2 / 11 cosine
    "wv_entangled_gateway": 8010,
    "gis_rag_v040": 8004,               # GIS-RAG v0.4.0 — 204 WV datasets, 7357 bridges
    "gbim_query_router": 7205,           # allis-gbim-query-router — LEARN-02 fix
}

# ChromaDB v2 multi-tenant API paths (inter-service from other containers):
CHROMA_V2_BASE = (
    "http://allis-chroma:8000"
    "/api/v2/tenants/default_tenant/databases/default_database"
)
CHROMA_COLLECTIONS_LIST = CHROMA_V2_BASE + "/collections"
CHROMA_COLLECTION_QUERY = CHROMA_V2_BASE + "/collections/{name}/query"
# /api/v1/ → 410 Gone
# /api/v2/collections → 404 (not the correct multi-tenant path)

# UUID two-step count (direct HTTP — Python client collection.count() handles this):
# Step 1: GET {CHROMA_V2_BASE}/collections/{collection_name} → response["id"] = UUID
# Step 2: GET {CHROMA_V2_BASE}/collections/{uuid}/count → integer count
```

**psql access patterns:**

```bash
# Production: msallis-db (primary for all spatial/GBIM/landowner work)
docker exec msallis-db psql -U postgres -d msallisgis

# Forensic: postgis-forensic (auditing and migration validation only)
docker exec postgis-forensic psql -h 127.0.0.1 -U allis -d msallisgis

# Verify mvw_gbim_landowner_spatial (production only):
docker exec msallis-db psql -U postgres -d msallisgis \
  -c "SELECT COUNT(*) FROM mvw_gbim_landowner_spatial;"
# Returns: 38979 — CLOSED OI-E
```

---

## 8.8 Distinguishing Metaphor from Implementation

To maintain academic rigor and avoid over-claiming, the following summary distinguishes
clearly between metaphorical design framing and current implementation.

**Metaphor and design framing (conceptual layer).** The use of "entanglement" to describe
correlated belief updates and retrieval biases across governance, ethics, space, and
service domains. The treatment of the embedding state as a Hilbert-like space with
entangled subsystems and measurement-like retrieval operations. The specification of tag-
and entity-based entanglement in which correlated items \(S_a\) are identified via shared
tags and are intended to be updated together through weight and embedding adjustments.

**Concrete implementation in the current `msallis-rebuild` deployment (★★ April 23, 2026):**

- A formal JSON schema and Pydantic model for `WVEntangledContext`, enforced in the
  running RAG server at **port 8010** (confirmed ✅ Running, bound to `127.0.0.1`).
- **GIS-RAG v0.4.0** at **port 8004** — 204 WV GIS datasets, 7,357 WV bridges —
  providing spatial retrieval alongside the entangled semantic path.
- A WV-biased, multi-collection retrieval path that uses the entanglement envelope to
  modulate scores across **48 ChromaDB collections** (April 23, 2026; historical note:
  50 collections April 17, 2026 pre-cleanup) — inventory confirmed via v2 manifest
  and SQLite cross-check; distance metrics confirmed (37 L2 / 11 cosine).
- All ChromaDB queries from these services use **`all-minilm:latest` (384-dim)** via the
  **ChromaDB v2 multi-tenant API** at `http://allis-chroma:8000`. `/api/v1/` returns
  410 Gone. Count calls use the UUID two-step pattern (Python client `collection.count()`
  handles transparently).
- The services log both pre-bias and post-bias rankings for inspection.
- A JSON-backed topic graph maintained by `allis-autonomous-learner` — ★★ **fully
  restored April 1, 2026** (LEARN-01, LEARN-02, LEARN-03 resolved); **21,181 records**
  in `autonomous_learner` (L2 distance) confirmed April 23, 2026.
- ★★ **LEARN-02 fix closes the learner → GBIM entanglement loop:** autonomous learner
  beliefs are now committed as GBIM entities in `msallisgis` on `msallis-db`
  (host 5433 / container 5432) via `allis-gbim-query-router:7205`, making them
  eligible for WV-tag boosting in port 8010 retrieval traces.
- **`mvw_gbim_landowner_spatial` — ✅ CLOSED: 38,979 rows, `msallis-db`. Not present
  in `postgis-forensic`.**
- ★ `allis-memory:8056` provides a durable, authenticated audit trail for all
  entanglement-adjacent BBB gate decisions — `_auth()` confirmed, `ALLIS_API_KEY` set.
- ★ **48 active ChromaDB collections / ~6,740,611 total embedding rows** confirmed
  April 23, 2026 (historical note: 50 collections / 6,740,611 rows on April 17, 2026
  prior to deduplication cleanup).

**Future work / design intent only:**

- Neighbor-biased topic selection using the topic graph (§8.6).
- Full cross-service weight and embedding updates implementing the entanglement update
  rule of §8.3.
- Enriched ChromaDB metadata coverage so WV-aligned documents in `gbim_beliefs_v2`
  (cosine), `GBIM_Fayette_sample` (L2), and `geospatialfeatures` (L2) are reliably
  boosted in entangled retrieval traces.
- Projection-like vector operations across entangled subsets.
- Integration of entangled retrieval traces into governance dashboards.

---

## 8.9 Observability Limits — Explicit Statement

The April 17, 2026 audit established the following observability limits. These limits
apply to any section of the thesis that makes claims about entanglement depth, collection
population, or subconscious queue size.

**1. Per-collection embedding counts are not directly derivable from SQLite.**

The current Chroma schema does not include a `collection_id` column on the `embeddings`
table. Therefore:

- `SELECT COUNT(*) FROM embeddings;` → **~6,740,611 rows** — proves the overall vector
  space is heavily populated. ✅
- `SELECT COUNT(*) FROM embeddings WHERE collection_id = '...';` → **not a valid query
  in this schema.** ❌

Collection membership is resolved through Chroma's internal segment metadata, not the raw
SQLite `embeddings` table. The **correct audit methodology** is:

| Question | Answer source |
|:--|:--|
| Is the DB populated? | `COUNT(*)` on `embeddings` table (~6,740,611 confirmed) |
| Does a specific collection exist? | v2 manifest `GET /api/v2/tenants/default_tenant/databases/default_database/collections` AND `SELECT name FROM collections ORDER BY name;` cross-check |
| How many embeddings per collection? | **Not derivable from raw SQLite** — use Python client `collection.count()` via v2 (handles UUID two-step transparently) |
| Is a collection correctly wired? | Service health (`/health`), behavior endpoint calls, and log inspection |

**2. The Fifth DGM's `i_container_size` is the authoritative indicator of subconscious
queue depth.**

Because per-collection embedding counts are not directly auditable from SQLite, the thesis
does not claim a specific population count for `fifth_dgm_subconscious` (L2 distance)
based on SQL queries. Instead:

- `GET http://127.0.0.1:4002/consciousness_stats` → `i_container_size` field is the
  authoritative measure of how many items are in the Fifth DGM's subconscious queue.
- At audit time (April 17, 2026), `i_container_size` was **0**. The collection exists
  and has correct 384-dim HNSW settings — visible in the v2 manifest and `collections`
  table — but the queue is empty in this epoch. This is correct and expected behavior;
  see Chapter 9 §9.3.3.

**3. Ensemble composition is not auditable via REST.**

Ports 8050, 8030, and 8008 all return 404 for `/models`, `/roster`, `/llm_status`,
`/model_status`, and `/status`. Ensemble size and composition are validated via the test
harness and 20LLM metrics path, not a public roster endpoint.

---

## 8.10 Cross-Subsystem Verification Methodology — April 23, 2026

The entanglement verification used in this chapter employs a multi-layer approach. Single-
endpoint checks are insufficient; all subsystems require cross-source confirmation.

### 8.10.1 Chroma Verification (Two-Source Cross-Check)

```bash
# Layer 1 — v2 REST manifest (host port 8002):
curl -s "http://127.0.0.1:8002/api/v2/tenants/default_tenant/databases/default_database/collections" \
  | python3 -m json.tool | grep '"name"'

# Layer 2 — SQLite direct:
sqlite3 /path/to/chroma.sqlite3 "SELECT name FROM collections ORDER BY name;"

# Layer 3 — Total embedding population:
sqlite3 /path/to/chroma.sqlite3 "SELECT COUNT(*) FROM embeddings;"
# Expected: ~6,740,611 (confirmed April 17, 2026; April 23 baseline consistent)

# Layer 4 — Per-collection count via Python client (UUID two-step handled transparently):
# import chromadb
# client = chromadb.HttpClient(host="127.0.0.1", port=8002)
# collection = client.get_collection("autonomous_learner")
# print(collection.count())  # 21,181 (April 23, 2026)

# NOTE: /api/v1/ returns 410 Gone — do not use.
# NOTE: Per-collection counts are NOT derivable from raw SQLite in this schema.
```

### 8.10.2 `allis-memory` Verification

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
# Confirmed BBB routes — April 23, 2026:
# GET /       — root description
# GET /health — filters_operational: 6, barrier_active: true
# POST /filter — main filtering endpoint
# POST /truth  — truth/content evaluation endpoint
# There is NO /filters inspection route in this build.

# /health — confirms 6 filters operational:
curl -s http://127.0.0.1:8016/health
# Expected: {"barrier_active": true, "filters_operational": 6, ...}

# /truth — expects "content" field (NOT "claim"):
curl -X POST http://127.0.0.1:8016/truth \
  -H "Content-Type: application/json" \
  -d '{"content": "West Virginia cooperative governance narrative"}'
# Expected: {"valid": true, "confidence": 0.9, "principal_reasons": ["all BBB filters passed"]}
# Missing "content" → FastAPI validation error (422)

# The six confirmed filters:
# 1. EthicalFilter           — Biblical principles
# 2. SpiritualFilter         — Wisdom alignment
# 3. SafetyMonitor (AU-02v2) — Technical security
# 4. ThreatDetection         — Community protection
# 5. Steganography / prompt-injection detection
#    (log: {'type': 'prompt_injection_keywords',
#           'detail': ['system prompt', 'jailbreak'],
#           'severity': 'critical'})
# 6. TruthVerification — via POST /truth; aggregates all filters;
#    returns valid, confidence, principal_reasons
```

### 8.10.4 Pituitary Verification

```bash
# Confirmed pituitary routes — April 23, 2026:
# GET /          — basic info
# GET /health
# GET /global_mode   ← authoritative current mode (NOTE: /globalmode → 404)
# GET /mode_history  ← history of mode changes
# POST /process
# POST /set_mode
# POST /chat

curl -s http://127.0.0.1:8108/global_mode
# Expected:
# {
#   "mode": "baseline",
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
# Confirmed routes by service — April 23, 2026:

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

# Ensemble composition must be validated via test harness
# and 20LLM /metrics endpoint — NOT a public roster endpoint.
# This is intentional in the hardened build.

curl -s http://127.0.0.1:8008/health
curl -s http://127.0.0.1:8050/health
curl -s http://127.0.0.1:8030/health
```

### 8.10.6 GIS-RAG v0.4.0 Verification

```bash
# GIS-RAG v0.4.0 — port 8004 — confirmed April 23, 2026:
curl -s http://127.0.0.1:8004/health
# Expected: {"status": "ok", "version": "0.4.0",
#            "wv_gis_datasets": 204, "wv_bridges": 7357}

# Verify spatial data source (production container only):
docker exec msallis-db psql -U postgres -d msallisgis \
  -c "SELECT COUNT(*) FROM zcta_wv_centroids WHERE state_abbr = 'WV';"

# GIS-RAG uses all-minilm:latest (384-dim), allis-chroma:8000 (v2 API),
# and targets msallis-db (host 5433 / container 5432) for spatial queries.
```

### 8.10.7 Logs as Final Confirmation Layer

Service logs provide the fourth and final verification layer for the following where REST
endpoints alone are insufficient:

- **BBB steganography / prompt-injection filter (filter 5):** Confirmed via log entries
  showing `{'type': 'prompt_injection_keywords', 'detail': ['system prompt', 'jailbreak'], 'severity': 'critical'}`.
- **DGM activity and subconscious routing:** Confirmed via `consciousness_stats` endpoint
  and logs showing `stored_in_subconscious: 1`, `last_woah_evaluation: 2026-04-17T11:18:19`.
- **Memory turn storage:** Confirmed via `allis-memory` logs showing write confirmations
  with `stored: true` and session normalization behavior.
- **Pituitary mode transitions:** Confirmed via `/mode_history` and watchdog logs showing
  `source: auto_watchdog` mode updates.
- **`autonomous_learner` accumulation:** Confirmed via log entries showing daily write
  cycles and collection count growth (~22 items/day since April 1, 2026 restore).

---

## 8.11 Summary

In its current state, the entanglement model serves both as a conceptual and mathematical
description of how coupled state should work across Ms. Allis's belief and spatial
structures, and as a description of concrete, running mechanisms in the `msallis-rebuild`
system.

**This chapter's description reflects the April 23, 2026 production state.** All prior
references to `msallis:5433`, fewer than 48 collections, `/api/v1/collections`,
`/api/v2/collections`, "2 collections," or any per-collection embedding count derived from
raw SQLite are superseded by the April 2026 baseline:

- **ChromaDB:** `allis-chroma`, host port **8002**, container port **8000**,
  inter-service URL `http://allis-chroma:8000`. **48 collections** confirmed
  April 23, 2026 via v2 manifest and SQLite cross-check (historical note: 50 collections
  on April 17, 2026 prior to deduplication cleanup). **~6,740,611 total embedding rows**
  (SQLite `COUNT(*)`). Per-collection counts not derivable from raw SQLite — use Python
  client `collection.count()` which handles the v2 UUID two-step pattern transparently.
  Distance metrics: **37 L2 / 11 cosine**. `gbim_beliefs` (bare) is retired.
- **Databases:** Two-container architecture.
  **Production:** `msallis-db`, host **5433** / container **5432**, role `postgres`,
  `msallisgis`, 16 GB / 294 tables / 11 schemas. All GBIM, spatial, landowner, and
  decay operations target this container.
  **Forensic:** `postgis-forensic`, host **5452** — **INVALID. Correct forensic host
  port is 5432**, role `allis` (+ `-h 127.0.0.1`). Forensic auditing only.
  **`mvw_gbim_landowner_spatial` — ✅ CLOSED: 38,979 rows, `msallis-db` only.**
- **GIS-RAG v0.4.0:** port **8004** — 204 WV GIS datasets, 7,357 WV bridges.
- **`allis-gbim-query-router`:** port **7205** — ✅ healthy, RBAC-gated,
  `X-Allis-Role` required, LEARN-02 resolved.
- **`nbb_pituitary_gland`:** port 8108, mode `baseline`, cortisol 0.4, warmth 0.9;
  `/global_mode` and `/mode_history` are the authoritative routes.
- **BBB:** 6 filters confirmed; routes: GET `/`, GET `/health`, POST `/filter`,
  POST `/truth`; no `/filters` route.
- **`allis-memory`:** `/memory/turn` requires both `user_message` and
  `assistant_response`; episodic memory may legitimately return `no_episodic_memory`;
  GET `/status` returns 404.
- **LLM ensemble:** no public `/models`, `/roster`, or `/llm_status` endpoint —
  composition validated via test harness.
- **`fifth_dgm_subconscious`:** real collection in `default_tenant/default_database`,
  L2 distance, 384-dim HNSW, live — `i_container_size: 0` at April 17, 2026 audit is
  authoritative subconscious queue indicator.
- **`autonomous_learner`:** **21,181 records** (L2 distance), April 23, 2026.
- **Verification methodology:** dual-source Chroma (v2 manifest + SQLite), service
  health endpoints, behavior endpoints, and logs as four independent confirmation layers.
- **Cross-reference:** GBIM architecture specification in `02-ms-allis-gbim.md`
  (Chapter 2/6).

The Fifth DGM documented in Chapter 9 and the Blood-Brain Barrier documented in
Chapter 16 are the primary consumers of the entangled RAG path, the pituitary mode signal,
and the memory audit substrate described in this chapter. For the canonical description of
how this service is called within the live `ultimatechat` and `chatlight` execution paths,
see **Chapter 17**.

---

*Chapter 8 — Quantum-Inspired Entanglement and Coupled State*
*Carrie Kidd (Mamma Kidd), Mount Hope WV*

*Original entries: February–March 2026 — initial entanglement architecture, RAG port
8010, topic graph.*
*★ March 28, 2026: Security remediation; `msjarvisgis` port corrected from 5452 to
5432; `spiritual_rag` deduplicated; `psychological_rag` restored.*
*★★ April 1, 2026: LEARN-01/02/03 resolved; learner → GBIM entanglement loop closed;
two-phase commit protocol added.*
*★★ April 17, 2026: ChromaDB API path corrected throughout; 48 collections confirmed;
6,740,611 total rows confirmed; per-collection SQL limits documented; `fifth_dgm_subconscious`
documented; all `msjarvis:5433` references removed; BBB and pituitary route surfaces
corrected; §8.9 Observability Limits and §8.10 Cross-Subsystem Verification added.*
*★★ April 23, 2026: Namespace corrections — `msallis-rebuild` narrative name,
`jarvis-` container prefix throughout. `jarvis-chroma` inter-service URL corrected to
`http://jarvis-chroma:8000`. ChromaDB API confirmed v2 only (`/api/v1/` returns 410
Gone); UUID two-step count pattern documented. `jarvis-gbim-query-router` port 7205
confirmed and added. GIS-RAG v0.4.0 (port 8004, 204 WV GIS datasets, 7,357 WV bridges)
added throughout. Collection names corrected: `msjarvis_docs`, `ms_allis_memory`,
`gbim_worldview_entities`. Collection count updated to 48 with historical note (was 50
on April 17, 2026 pre-cleanup); distance metrics cross-checked (37 L2 / 11 cosine).
`autonomous_learner` updated to 21,181 items (L2). OI-E closed: 38,979 rows,
`msallis-db`. Container counts date-stamped throughout. `gbim_beliefs` (bare) retired; 
`postgis-forensic` forensic host port 5452 corrected to 5432 in documentation.*
