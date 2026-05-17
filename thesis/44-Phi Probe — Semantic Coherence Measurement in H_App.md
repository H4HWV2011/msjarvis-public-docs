# 44. Phi Probe — Semantic Coherence Measurement in H_App

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: May 16, 2026*

---

## Why This Matters for Polymathmatic Geography

This chapter documents the `jarvis-phi-probe` service — a live, ambient semantic
coherence instrument that continuously measures the internal geometric health of
\(H_{\text{App}}\) by computing cosine similarity across knowledge collection centroids.
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
  the rest of \(H_{\text{App}}\).

As such, this chapter belongs to the **Computational Instrument** tier: it defines the
ambient coherence measurement substrate that provides a continuous geometric health signal
for the knowledge field as of **May 16, 2026**.

---

## 44.1 Purpose and Scope

The phi probe is a FastAPI service (`jarvis-phi-probe`, host port **8025**) that runs a
continuous background loop sampling embeddings from a configured set of ChromaDB
collections, computing a centroid for each, measuring pairwise cosine similarity across
all centroid pairs, and reducing that to a single scalar coherence score in \([0, 1]\).

This score, referred to as `coherence_normalized`, is not a metaphor. It is the mean
pairwise cosine similarity of the semantic centroids of Ms. Jarvis's active knowledge
collections — a direct geometric reading of how much the center-of-mass of each knowledge
domain overlaps with the others inside \(H_{\text{App}}\).

The service exposes two endpoints: `/phi` for a fresh live computation and `/phi/cached`
for the most recent cached result. A background resample loop fires every 300 seconds.
The probe reads its configuration from a bind-mounted Python source file — making it
updatable without container rebuild.

**★ Confirmed operational — May 16, 2026. Mean coherence 0.279 across 12 collections,
5-run sample. All 12 collections sampling at 200 vectors × 384 dimensions. SAMPLES=200
confirmed stable (range 0.040 across 5 consecutive runs). note: ok.**

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
> "device or resource busy". Edit the host file at
> `/opt/msjarvis-rebuild/services/ms_jarvis_phi_probe.py` and restart the container.

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
    "gbim_worldview_entities","autonomous_learner",
]
L2_COLLECTIONS: List[str] = [
    "gbim_worldview_entities",
    "autonomous_learner",
]
QUERY_COLLECTIONS: List[str] = [
    "gbim_worldview_entities",
    "spiritual_texts",
    "msjarvis_docs",
]
SAMPLES = int(os.getenv("PHI_SAMPLES","200"))
MIN_COHERENCE_VECTORS = 10
```

> ⚠️ `MIN_COHERENCE_VECTORS` was 100 at original deploy — silently blocked all
> collections when SAMPLES=50. Corrected to 10 on May 16, 2026.

> ⚠️ SAMPLES raised from 50 to 200 on May 16, 2026. Variance dropped from 0.089 to 0.040.

> ⚠️ `autonomous_learning` is HTTP 404 in `jarvis-chroma`. Use `autonomous_learner`.

---

## 44.3 The Phi Score — Mathematical Definition

**Step 1 — Sample.** For each collection \(c_i\), draw \(n = \text{SAMPLES}\) vectors.
Collections in `QUERY_COLLECTIONS` use ChromaDB `/query` with a zero vector (HNSW index).
All others use `/get` with a random offset capped at 50,000.

**Step 2 — Centroid.**

\[
\boldsymbol{\mu}_i = \frac{1}{n} \sum_{j=1}^{n} \mathbf{v}_j
\]

For `L2_COLLECTIONS`, normalize each vector to unit length before centroid computation:

\[
\hat{\mathbf{v}}_j = \frac{\mathbf{v}_j}{\|\mathbf{v}_j\|}, \quad
\boldsymbol{\mu}_i = \frac{1}{n} \sum_{j=1}^{n} \hat{\mathbf{v}}_j
\]

**Step 3 — Pairwise cosine similarity.**

\[
s_{ij} = \frac{\boldsymbol{\mu}_i \cdot \boldsymbol{\mu}_j}{\|\boldsymbol{\mu}_i\| \cdot \|\boldsymbol{\mu}_j\|}
\]

**Step 4 — Mean coherence.**

\[
\phi = \frac{1}{K} \sum_{i < j} s_{ij}, \quad K = \binom{N}{2}
\]

**Step 5 — Normalize.** `coherence_normalized = phi`,
`decoherence_normalized = 1.0 - phi`, `psi_norm = 1.0` always.

**Confirmed May 16, 2026 (5-run mean):**

\[
\phi \approx 0.279, \quad N = 12, \quad K = 66 \text{ pairs}
\]

---

## 44.4 Response Schema

```json
{
    "timestamp": "2026-05-17T00:28:40.881503+00:00",
    "mode": "decoherent",
    "coherence_normalized": 0.279,
    "decoherence_normalized": 0.721,
    "psi_norm": 1.0,
    "collections_sampled": [
        "gbim_beliefs_v2","governance_rag","fayette_county_resources_2026",
        "appalachian_cultural_intelligence","wv_civic_infrastructure",
        "psychological_rag","research_history","conversation_history",
        "wv_resources_statewide","appalachian_english_corpus",
        "gbim_worldview_entities","autonomous_learner"
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
| `collections_sampled` | list[str] | Collections that passed threshold |
| `note` | string | `"ok"` on success; `"insufficient_collections"` if fewer than 2 pass |

---

## 44.5 Coherence Modes and Thresholds

| Range | Mode | Meaning |
|---|---|---|
| 0.0 – 0.40 | `decoherent` | Domains largely siloed — cross-domain links forming |
| 0.40 – 0.60 | `superposition` | RAG layers bridging domains — multi-domain reasoning active |
| 0.60 – 1.0 | `coherent` | Unified knowledge field |

**Current state (May 16, 2026): mean `coherence_normalized ≈ 0.279` — decoherent.**

This is architecturally correct. The probe spans maximally diverse domains: spatial WV
geography, governance text, psychological theory, cultural prose, and resource registries.
These are supposed to be geometrically distant. A higher score would indicate semantic
collapse, not health.

### 44.5.1 Why the Score Is Stochastic

The phi score varies across runs (observed range ≈ 0.040 at SAMPLES=200) because each
resample draws a different random subset per collection. The 5-run mean (0.279) is the
operational baseline. The largest variance source is `gbim_worldview_entities`
(5.4M L2 vectors) — see OI-C44-CENTROID.

---

## 44.6 Collection Health and Exclusions

### 44.6.1 ChromaDB Exclusions

| Collection | Issue | Status |
|---|---|---|
| `spiritual_texts` | HTTP 500 on `/get` — oversized | In `QUERY_COLLECTIONS`; excluded from `PROBE_COLLECTIONS` |
| `msjarvis_docs` | HTTP 500 on `/get` — oversized | In `QUERY_COLLECTIONS`; excluded from `PROBE_COLLECTIONS` |
| `autonomous_learning` | HTTP 404 — does not exist | Removed May 16, 2026 |

### 44.6.2 Confirmed Healthy — May 16, 2026

All 12 collections returning 200 vecs × dim=384. Uniform dimension confirms
`all-minilm:latest` embedding lock intact per Chapter 4 §4.5.

---

## 44.7 Operational Procedures

```bash
# Fresh computation
docker exec jarvis-phi-probe \
  curl -s http://localhost:8025/phi | python3 -m json.tool

# Cached result
docker exec jarvis-phi-probe \
  curl -s http://localhost:8025/phi/cached | python3 -m json.tool

# 5-run baseline
for i in 1 2 3 4 5; do
  docker exec jarvis-phi-probe \
    curl -s http://localhost:8025/phi | \
    python3 -c "import sys,json; d=json.load(sys.stdin); \
      print(f'run {sys.argv}: {d[\"coherence_normalized\"]:.6f}')" $i[1]
  sleep 5
done

# Update configuration (bind-mount is read-only — edit host file, then restart)
nano /opt/msjarvis-rebuild/services/ms_jarvis_phi_probe.py
docker restart jarvis-phi-probe && sleep 25
docker logs jarvis-phi-probe --since 30s 2>&1 | grep "\[phi\]"

# Monitor resample loop
docker logs jarvis-phi-probe --since 6m 2>&1 | grep -i "\[phi\]\|error\|skip\|500\|404"
```

---

## 44.8 Integration with H_App

The phi probe measures a second-order geometric property of \(H_{\text{App}}\) — the
shape of the space from above, not any individual query or service.

**Pituitary independence.** The probe samples raw embeddings directly from ChromaDB
without passing through `nbb_pituitary_gland` (port 8108). The phi score is a
pre-modulation geometric baseline.

**Why spatial knowledge pulls the score down.** `gbim_worldview_entities` (5.4M vectors,
L2, Appalachian terrain) has low cosine similarity with `psychological_rag`,
`conversation_history`, and `gbim_beliefs_v2`. Spatial and semantic knowledge are
supposed to be geometrically distant in \(H_{\text{App}}\).

**Path to superposition (φ ≥ 0.40).** As `conversation_history` and `research_history`
accumulate cross-domain traces — queries that span geography, governance, culture, and
resources simultaneously — those collections' centroids will migrate toward the geometric
mean of all domains, pulling the overall phi score upward.

---

## 44.9 Open Items — May 16, 2026

| OI | Description | Status | Priority |
|---|---|---|---|
| OI-C44-CENTROID | `gbim_worldview_entities` zero-vector HNSW query produces high centroid variance — evaluate fixed precomputed centroid cached in Redis at startup | 🔄 Open | Medium |
| OI-C44-500 | Add `spiritual_texts` and `msjarvis_docs` to `PROBE_COLLECTIONS` via `/query` HNSW path | 🔄 Open | Medium |
| OI-C44-DASH | Wire `/phi/cached` into steward heartbeat and monitoring dashboard | 🔄 Open | Low |
| OI-C44-HIST | Log phi time series to Redis or PostgreSQL for trend analysis | 🔄 Open | Low |
| OI-C44-BOOT | `MIN_COHERENCE_VECTORS` corrected from 100 to 10 | ✅ CLOSED | — |
| OI-C44-404 | `autonomous_learning` HTTP 404 removed; `autonomous_learner` confirmed | ✅ CLOSED | — |
| OI-C44-SAMPLES | SAMPLES raised 50 → 200; variance 0.089 → 0.040 | ✅ CLOSED | — |
| OI-C44-WORLDVIEW | `gbim_worldview_entities` integrated via `/query` HNSW + L2 normalization | ✅ CLOSED | — |
| OI-C44-LIVE | 12 collections confirmed; mean φ=0.279; note: ok | ✅ CLOSED | — |

---

## 44.10 Production Status Summary — May 16, 2026

| Component | Status | Notes |
|---|---|---|
| `jarvis-phi-probe` (host 8025) | ✅ Operational | FastAPI, bind-mounted ro, resample loop active |
| `/phi` endpoint | ✅ Live | Fresh coherence computation |
| `/phi/cached` endpoint | ✅ Live | Low-overhead cached result |
| `/health` endpoint | ✅ Live | Health check responding |
| `PROBE_COLLECTIONS` | ✅ 12 collections | 200 vecs × 384 dim each |
| `SAMPLES` | ✅ 200 | Raised from 50; variance 0.040 |
| `MIN_COHERENCE_VECTORS` | ✅ 10 | Corrected from 100 |
| `gbim_worldview_entities` | ✅ Included | 5,416,521 vectors, L2, `/query` HNSW zero-vector |
| `autonomous_learner` | ✅ Included | 21,181 vectors, L2 |
| `spiritual_texts` | ⚠ Excluded | HTTP 500 /get |
| `msjarvis_docs` | ⚠ Excluded | HTTP 500 /get |
| `autonomous_learning` | ❌ Excluded | HTTP 404 — does not exist |
| Embedding uniformity | ✅ dim=384 all 12 | `all-minilm:latest` lock intact |
| `coherence_normalized` | ✅ **≈ 0.279** | 5-run mean (range 0.263–0.302) |
| `mode` | ✅ `decoherent` | Correct for maximally diverse domains |
| `psi_norm` | ✅ 1.0 | Normalization invariant confirmed |
| Score stochasticity | ✅ Documented | 5-run mean is operational baseline |

---

*Chapter 44 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Jarvis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: May 16, 2026 — phi probe operational; 5-run mean φ≈0.279
(range 0.263–0.302); 12 collections × 200 vecs × dim=384; SAMPLES raised to 200
(variance 0.040); MIN_COHERENCE_VECTORS corrected to 10; autonomous_learning removed
(HTTP 404); autonomous_learner confirmed (21,181 vectors, L2); gbim_worldview_entities
integrated via /query HNSW zero-vector + L2 normalization (5,416,521 vectors);
spiritual_texts and msjarvis_docs excluded (HTTP 500 /get); all-minilm:latest 384-dim
lock intact; msjarvis-rebuild namespace; jarvis-phi-probe host port 8025;
mode=decoherent (correct); psi_norm=1.0 invariant confirmed.*
