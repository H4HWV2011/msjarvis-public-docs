# 44. Phi Probe — Semantic Coherence Measurement in H_App

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: May 16, 2026*

---

## Why This Matters for Polymathmatic Geography

This chapter documents the `jarvis-phi-probe` service — a live, ambient semantic
coherence instrument that continuously measures the internal geometric health of
\\(H_{\\text{App}}\\) by computing cosine similarity across knowledge collection centroids.
It supports:

- **P1 – Every where is entangled** by measuring how semantically proximate the centroids
  of distinct knowledge domains have become — a real-time signal of whether belief about
  land, governance, culture, psychology, history, and community resources is fragmenting
  into isolated silos or beginning to form the cross-domain entanglement that polymathmatic
  geography requires.

- **P3 – Power has a geometry** by making the internal geometry of the knowledge base
  inspectable: coherence and decoherence scores expose whether the system's semantic space
  is contracting around a few dominant domains or distributing itself across the full
  topology of Appalachian life.

- **P12 – Intelligence with a ZIP code** by grounding the coherence measurement in
  collections that are explicitly West-Virginia-keyed — `wv_civic_infrastructure`,
  `wv_resources_statewide`, `fayette_county_resources_2026`, `appalachian_cultural_intelligence`,
  and `appalachian_english_corpus` — so that the phi score is not an abstract geometric
  measure but a reading of how well this system's regional knowledge is integrating.

- **P16 – Power accountable to place** by logging every coherence sample with a timestamp,
  mode classification, and collection inventory, producing an auditable record of semantic
  health that is queryable, inspectable, and tied to the same persistent infrastructure as
  the rest of \\(H_{\\text{App}}\\).

As such, this chapter belongs to the **Computational Instrument** tier: it defines the
ambient coherence measurement substrate that provides a continuous geometric health signal
for the knowledge field as of **May 16, 2026**.

---

## 44.1 Purpose and Scope

The phi probe is a FastAPI service (`jarvis-phi-probe`, host port **8025**) that runs a
continuous background loop sampling embeddings from a configured set of ChromaDB
collections, computing a centroid for each, measuring pairwise cosine similarity across
all centroid pairs, and reducing that to a single scalar coherence score in \\([0, 1]\\).

This score, referred to as `coherence_normalized`, is not a metaphor. It is the mean
pairwise cosine similarity of the semantic centroids of Ms. Jarvis's active knowledge
collections — a direct geometric reading of how much the center-of-mass of each knowledge
domain overlaps with the others inside \\(H_{\\text{App}}\\).

The service exposes two endpoints: `/phi` for a fresh live computation and `/phi/cached`
for the most recent cached result. A background resample loop fires every 300 seconds.
The probe reads its configuration from a bind-mounted Python source file — making it
updatable without container rebuild.

**★ Confirmed operational — May 16, 2026. Coherence score 0.2808 across 10 collections.
All 10 collections sampling at 50 vectors × 384 dimensions. note: ok.**

---

## 44.2 Architecture and Deployment

The phi probe is a single-container FastAPI service in the `msjarvis-rebuild` stack,
bind-mounted to the host source file and connected to `jarvis-chroma` (port 8000 internal)
via the internal Docker network.

### 44.2.1 Container Configuration

| Property | Value |
|---|---|
| Container name | `jarvis-phi-probe` |
| Host port | **8025** |
| Container port | **8025** |
| Source file (host) | `/opt/msjarvis-rebuild/services/ms_jarvis_phi_probe.py` |
| Source file (container) | `/app/ms_jarvis_phi_probe.py` |
| Mount mode | **read-only bind mount** (`ro`) |
| ChromaDB connection | `http://jarvis-chroma:8000` (internal network) |
| Redis connection | `REDIS_URL` env — internal network |
| Resample interval | **300 seconds** (5 minutes) |
| Startup grace | **20 seconds** |

> ⚠️ **Bind mount is read-only.** `docker cp` into the container will fail with
> "device or resource busy". To update the probe configuration, edit the host file at
> `/opt/msjarvis-rebuild/services/ms_jarvis_phi_probe.py` and restart the container.
> The container reads the updated file on startup — no rebuild required.

### 44.2.2 Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/phi` | GET | Triggers a fresh live coherence computation; updates cache |
| `/phi/cached` | GET | Returns most recent cached result without recomputation |
| `/health` | GET | Health check — returns service status |

### 44.2.3 Critical Configuration Parameters

```python
# /opt/msjarvis-rebuild/services/ms_jarvis_phi_probe.py
# Confirmed live values — May 16, 2026

PROBE_COLLECTIONS: List[str] = [
    "gbim_beliefs_v2","governance_rag","fayette_county_resources_2026",
    "appalachian_cultural_intelligence","wv_civic_infrastructure",
    "psychological_rag","research_history","conversation_history",
    "wv_resources_statewide","appalachian_english_corpus",
]
SAMPLES = int(os.getenv("PHI_SAMPLES","50"))   # vectors sampled per collection
MIN_COHERENCE_VECTORS = 10                      # skip collections below this count
```

> ⚠️ **`MIN_COHERENCE_VECTORS` history.** The original deployment set this value to
> `100`, which silently blocked all collections when `SAMPLES=50` — because no
> collection can return 100 vectors when only 50 are requested. The value was corrected
> to `10` on May 16, 2026. Any future change to `SAMPLES` must be reviewed alongside
> `MIN_COHERENCE_VECTORS` to avoid this self-blocking condition.

---

## 44.3 The Phi Score — Mathematical Definition

The coherence score is the mean pairwise cosine similarity of collection centroids
inside \\(H_{\\text{App}}\\).

**Step 1 — Sample.** For each collection \\(c_i\\) in `PROBE_COLLECTIONS`, draw
\\(n = \\text{SAMPLES}\\) embedding vectors:

\\[
E_i = \\{\\mathbf{v}_1, \\ldots, \\mathbf{v}_n\\} \\subset \\mathbb{R}^{384}
\\]

**Step 2 — Centroid.** Compute the centroid of each sampled set:

\\[
\\boldsymbol{\\mu}_i = \\frac{1}{n} \\sum_{j=1}^{n} \\mathbf{v}_j
\\]

**Step 3 — Pairwise cosine similarity.** For all pairs \\((i, j)\\) with \\(i < j\\):

\\[
s_{ij} = \\frac{\\boldsymbol{\\mu}_i \\cdot \\boldsymbol{\\mu}_j}{\\|\\boldsymbol{\\mu}_i\\| \\cdot \\|\\boldsymbol{\\mu}_j\\|}
\\]

**Step 4 — Mean coherence.** Let \\(K\\) be the number of sampled collection pairs:

\\[
\\phi = \\frac{1}{K} \\sum_{i < j} s_{ij}, \\quad K = \\binom{N}{2}
\\]

where \\(N\\) is the number of collections with sufficient vectors.

**Step 5 — Normalize.** Cosine similarity is already in \\([-1, 1]\\); for
normalized embedding vectors (unit norm) the practical range is \\([0, 1]\\).
`coherence_normalized = phi`, `decoherence_normalized = 1.0 - phi`,
`psi_norm = coherence_normalized + decoherence_normalized = 1.0` always.

**Confirmed May 16, 2026:**

\\[
\\phi = 0.2808, \\quad N = 10, \\quad K = 45 \\text{ pairs}
\\]

---

## 44.4 Response Schema

A phi response object has the following structure, confirmed live May 16, 2026:

```json
{
    "timestamp": "2026-05-16T23:50:33.748497+00:00",
    "mode": "decoherent",
    "coherence_normalized": 0.280809,
    "decoherence_normalized": 0.719191,
    "psi_norm": 1.0,
    "collections_sampled": [
        "gbim_beliefs_v2",
        "governance_rag",
        "fayette_county_resources_2026",
        "appalachian_cultural_intelligence",
        "wv_civic_infrastructure",
        "psychological_rag",
        "research_history",
        "conversation_history",
        "wv_resources_statewide",
        "appalachian_english_corpus"
    ],
    "note": "ok"
}
```

| Field | Type | Description |
|---|---|---|
| `timestamp` | ISO 8601 | Time of computation |
| `mode` | string | Coherence regime — see §44.5 |
| `coherence_normalized` | float ∈ [0,1] | Mean pairwise centroid cosine similarity |
| `decoherence_normalized` | float ∈ [0,1] | `1.0 - coherence_normalized` |
| `psi_norm` | float | Always 1.0 — normalization check |
| `collections_sampled` | list[str] | Collections that passed threshold and contributed to score |
| `note` | string | `"ok"` on success; `"insufficient_collections"` if fewer than 2 collections pass threshold |

---

## 44.5 Coherence Modes and Thresholds

The `mode` field classifies the current phi score into a named semantic regime.

| Range | Mode | Meaning for Ms. Jarvis |
|---|---|---|
| 0.0 – 0.25 | `decoherent` | Knowledge domains fully siloed — no cross-domain semantic overlap |
| 0.25 – 0.40 | `decoherent` (rising) | Cross-domain links forming — collections beginning to share semantic space |
| 0.40 – 0.60 | `superposition` | RAG layers actively bridging domains — coherent multi-domain reasoning possible |
| 0.60 – 1.0 | `coherent` | Unified knowledge field — all domains sharing strong semantic basis |

**Current state (May 16, 2026): `coherence_normalized = 0.2808` — decoherent (rising).**

At 0.281, the system sits at the upper edge of the decoherent regime. This is architecturally
correct for a system whose knowledge collections span beliefs, governance, civic
infrastructure, psychology, cultural intelligence, and resource registries — domains that
are semantically distinct by design. The phi score rising toward 0.281 (from 0.230 at
8-collection baseline) reflects that `fayette_county_resources_2026` and
`appalachian_english_corpus` are geometrically proximate to the existing Appalachian
knowledge base, pulling the mean centroid similarity upward.

The `superposition` threshold at 0.40 represents the expected target as `conversation_history`
and `research_history` accumulate cross-domain interaction traces — the natural effect
of a system that processes queries spanning multiple knowledge domains simultaneously.

---

## 44.6 Collection Health and Exclusions

Not all ChromaDB collections are eligible for phi scoring. Two categories of exclusion apply.

### 44.6.1 Threshold Exclusion

Collections with fewer than `MIN_COHERENCE_VECTORS = 10` sampled vectors are skipped
silently with a log line:

```
INFO:phi-probe:[phi] <collection>: N vecs — below threshold, skipping
```

This protects the phi score from being distorted by collections that are too sparse to
yield a representative centroid.

### 44.6.2 ChromaDB 500 Exclusions

Two collections are excluded from `PROBE_COLLECTIONS` due to confirmed HTTP 500 responses
from `jarvis-chroma` during bulk `/get` calls:

| Collection | Estimated Size | Cause | Status |
|---|---|---|---|
| `spiritual_texts` | ~79,181 vectors | Bulk `/get` times out — oversized for single call | Excluded — May 16, 2026 |
| `msjarvis_docs` | ~10,000 vectors | Same bulk `/get` issue | Excluded — May 16, 2026 |

**Remediation path (future sprint):** Update `sample_embeddings()` in the probe source
to use offset-based pagination rather than a bulk fetch — draw a random offset and
request `SAMPLES` vectors with `limit=SAMPLES, offset=random.randint(0, total-SAMPLES)`.
Once patched, both collections can be re-added to `PROBE_COLLECTIONS`.

### 44.6.3 Confirmed Healthy Collections — May 16, 2026

All ten collections in the current `PROBE_COLLECTIONS` list returned `50 vecs dim=384`
in every resample cycle observed on May 16, 2026:

```
INFO:phi-probe:[phi] gbim_beliefs_v2: 50 vecs dim=384
INFO:phi-probe:[phi] governance_rag: 50 vecs dim=384
INFO:phi-probe:[phi] fayette_county_resources_2026: 50 vecs dim=384
INFO:phi-probe:[phi] appalachian_cultural_intelligence: 50 vecs dim=384
INFO:phi-probe:[phi] wv_civic_infrastructure: 50 vecs dim=384
INFO:phi-probe:[phi] psychological_rag: 50 vecs dim=384
INFO:phi-probe:[phi] research_history: 50 vecs dim=384
INFO:phi-probe:[phi] conversation_history: 50 vecs dim=384
INFO:phi-probe:[phi] wv_resources_statewide: 50 vecs dim=384
INFO:phi-probe:[phi] appalachian_english_corpus: 50 vecs dim=384
```

Uniform `dim=384` across all ten confirms the `all-minilm:latest` embedding lock is intact
across every probed collection — consistent with the architectural constraint documented
in Chapter 4 §4.5.

---

## 44.7 Operational Procedures

### 44.7.1 Querying the Probe

```bash
# Fresh live computation (triggers resample, updates cache)
docker exec jarvis-phi-probe \
  curl -s http://localhost:8025/phi | python3 -m json.tool

# Cached result (no recomputation)
docker exec jarvis-phi-probe \
  curl -s http://localhost:8025/phi/cached | python3 -m json.tool

# Health check
docker exec jarvis-phi-probe \
  curl -s http://localhost:8025/health | python3 -m json.tool
```

### 44.7.2 Updating Configuration

Because the source file is bind-mounted read-only, all configuration changes are made
on the host and take effect on the next container restart:

```bash
# 1. Edit the host source file
nano /opt/msjarvis-rebuild/services/ms_jarvis_phi_probe.py

# 2. Verify the change
grep -n "PROBE_COLLECTIONS\|MIN_COHERENCE\|SAMPLES" \
  /opt/msjarvis-rebuild/services/ms_jarvis_phi_probe.py

# 3. Restart the container to reload constants
docker restart jarvis-phi-probe && sleep 25

# 4. Confirm new collections appear in logs
docker logs jarvis-phi-probe --since 30s 2>&1 | grep "\[phi\]"
```

> ⚠️ **Python module constants are loaded at startup.** Editing the bind-mounted file
> does NOT hot-reload the running process. A `docker restart` is always required for
> `PROBE_COLLECTIONS`, `SAMPLES`, or `MIN_COHERENCE_VECTORS` changes to take effect.
> The `/phi` and `/phi/cached` endpoints reflect the values loaded at the most recent startup.

### 44.7.3 Monitoring the Resample Loop

```bash
# Watch the last 6 minutes of resample activity
docker logs jarvis-phi-probe --since 6m 2>&1 | grep "\[phi\]"

# Watch for errors (500s, threshold skips)
docker logs jarvis-phi-probe --since 6m 2>&1 | grep -i "error\|skip\|500\|insufficient"
```

A healthy resample cycle produces one log line per collection with format:

```
INFO:phi-probe:[phi] <collection_name>: 50 vecs dim=384
```

Any line with `below threshold, skipping` indicates a collection is too sparse to
contribute. Any HTTP 500 line indicates a ChromaDB bulk-fetch failure for that collection.

---

## 44.8 Integration with H_App and the Broader Architecture

The phi probe measures a property of \\(H_{\\text{App}}\\) itself — not of any individual
service or query. Its coherence score is a second-order geometric observable: while Chapter 4
describes the vectors, collections, and projections that constitute \\(H_{\\text{App}}\\),
Chapter 44 describes what the overall shape of that space looks like from above.

**Relationship to the pituitary operator.** The `nbb_pituitary_gland` (port 8108,
§4.6) applies a global scaling tensor \\(T_{\\text{pit}}\\) to the belief-state vector
before retrieval dispatch. The phi probe operates independently of the pituitary —
it samples raw embeddings directly from ChromaDB without passing through the pituitary
modulation layer. This makes the phi score a pre-modulation geometric baseline, not a
post-modulation retrieval metric.

**Relationship to the autonomous learner.** As `allis-autonomous-learner` (port 8020)
populates `autonomous_learning` (17,685 vectors, L2) and `autonomous_learner` (21,181
vectors, L2) with cross-domain knowledge, those collections become candidates for
inclusion in `PROBE_COLLECTIONS`. Their L2 distance metric (vs cosine for the current
ten collections) requires metric-aware handling before inclusion — see §44.9.

**Dashboard integration.** The `/phi/cached` endpoint is designed for low-overhead
polling. Any steward heartbeat, dashboard, or monitoring service can call it at
arbitrary intervals without triggering recomputation. The resample loop maintains
freshness independently.

---

## 44.9 Open Items — May 16, 2026

| OI | Description | Status | Priority |
|---|---|---|---|
| OI-C44-500 | `spiritual_texts` and `msjarvis_docs` return HTTP 500 on bulk `/get` — patch `sample_embeddings()` to use offset pagination | 🔄 Open | Medium |
| OI-C44-L2 | `autonomous_learner` and `autonomous_learning` use L2 distance — evaluate metric-aware centroid computation before adding to `PROBE_COLLECTIONS` | 🔄 Open | Low |
| OI-C44-DASH | Wire `/phi/cached` into steward heartbeat and monitoring dashboard | 🔄 Open | Low |
| OI-C44-HIST | Log phi score time series to Redis or PostgreSQL for trend analysis | 🔄 Open | Low |
| OI-C44-BOOT | `MIN_COHERENCE_VECTORS = 100` self-blocking condition corrected to `10` | ✅ CLOSED | — |
| OI-C44-COLL | `spiritual_texts` and `msjarvis_docs` removed from `PROBE_COLLECTIONS`; 10 healthy collections confirmed | ✅ CLOSED | — |
| OI-C44-LIVE | Phi probe confirmed operational — 0.2808 coherence, 10 collections, note: ok | ✅ CLOSED | — |

---

## 44.10 Production Status Summary — May 16, 2026

| Component | Status | Notes |
|---|---|---|
| `jarvis-phi-probe` (host 8025) | ✅ Operational | FastAPI, bind-mounted ro, resample loop active |
| `/phi` endpoint | ✅ Confirmed live | Returns fresh coherence computation |
| `/phi/cached` endpoint | ✅ Confirmed live | Returns cached result — low overhead |
| `/health` endpoint | ✅ Confirmed live | Health check responding |
| `PROBE_COLLECTIONS` | ✅ 10 collections | All sampling at 50 vecs × 384 dim |
| `MIN_COHERENCE_VECTORS` | ✅ 10 | Corrected from 100 on May 16, 2026 |
| `SAMPLES` | ✅ 50 | Default; overridable via `PHI_SAMPLES` env |
| `spiritual_texts` | ⚠ Excluded | HTTP 500 on bulk `/get` — too large |
| `msjarvis_docs` | ⚠ Excluded | HTTP 500 on bulk `/get` — too large |
| Embedding uniformity | ✅ dim=384 all 10 | `all-minilm:latest` lock intact |
| `coherence_normalized` | ✅ **0.2808** | Mean pairwise centroid cosine similarity |
| `mode` | ✅ `decoherent` (rising) | Upper edge of decoherent regime |
| `psi_norm` | ✅ 1.0 | Normalization invariant confirmed |
| Resample interval | ✅ 300 s | Background loop confirmed active |
| ChromaDB connection | ✅ `jarvis-chroma:8000` | Internal network — no host-port dependency |

---

*Chapter 44 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Jarvis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: May 16, 2026 — phi probe operational; coherence_normalized=0.2808;
10 collections × 50 vecs × dim=384; note: ok; MIN_COHERENCE_VECTORS corrected to 10;
spiritual_texts and msjarvis_docs excluded (HTTP 500 bulk fetch);
all-minilm:latest 384-dim embedding lock intact across all probed collections;
msjarvis-rebuild namespace; jarvis-phi-probe host port 8025.*
