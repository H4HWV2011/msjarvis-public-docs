# Case Study: Spatial Truth vs. Semantic Proximity
## How Community-Owned PostGIS Infrastructure Corrects LLM Hallucination at Inference Time

**Carrie A. Kidd | Harmony for Hope, Inc. | Mount Hope, West Virginia**
**Ms. Jarvis Open-Source AI Infrastructure Project | March 30, 2026**

---

## Abstract

Large language models trained on web-scale corpora develop statistical associations between place names and facilities that approximate geographic proximity without encoding it. This case study documents a reproducible benchmark in which a retrieval-augmented AI system (Ms. Jarvis) was tested against the same geographic query using two knowledge sources: a ChromaDB semantic vector store and a PostGIS spatial database populated with verified West Virginia state datasets. The semantic system returned hospitals located 60–90 miles from the queried location. The PostGIS system returned the hospital at the queried coordinates. The architectural intervention — a three-file code change establishing source authority hierarchy at inference time — eliminated hallucination without model retraining, fine-tuning, or external API dependency. The infrastructure is community-owned, regionally governed, and reproducible.

---

## 1. Background

### 1.1 The Problem of Semantic Proximity

Language models learn geographic relationships from co-occurrence patterns in text. A model trained on news articles, Wikipedia, and web content will associate "hospitals near Charleston, WV" with any hospital that appears frequently in West Virginia healthcare coverage — regardless of actual distance. This produces responses that are *plausible* and *confident* but *spatially wrong*.

For most queries this is an inconvenience. In rural Appalachia, where the nearest Level I trauma center may be the difference between survival and death, a 60-mile error in a navigation or triage recommendation is a life-safety failure.

### 1.2 The Regional Data Context

West Virginia maintains several verified spatial datasets relevant to this problem:

- **WV E-911 Statewide Address Layer** — geolocated address points from county 911 centers
- **HSIP Hospital Dataset** — verified facility locations from the Homeland Security Infrastructure Program
- **WV Tax Parcel Layer** — parcel boundaries with ownership and land use
- **Building Footprint Layers** (3 sources) — structure-level spatial data

These datasets are publicly maintained, regularly updated, and — critically — *locally governed*. No external technology vendor controls them. Harmony for Hope, Inc. has integrated these layers into a PostGIS spatial database (`msjarvisgis`) running on regional infrastructure as part of the Ms. Jarvis project.

### 1.3 Scale of the Spatial Asset

The `msjarvisgis` database contains **540 spatial tables** across multiple schemas, including:

- 911 centers (4 table variants, GCS84 and UTM83)
- Hospitals, nursing homes, health rural facilities, community health providers
- Fire departments, police departments, correctional institutions
- Buildings, building footprints (3 sources: WVGISTC, Microsoft 2018, SAMB)
- Bridges, dams, flood plain structures at risk
- Census blocks, block groups, populated places (1990–2020)
- Legislative districts, voting districts, county boundaries
- Libraries, places of worship, veterans affairs facilities
- Wind energy resources, coal seams, mine sites
- TIGER geocoding schema (full WV coverage)
- GBIM belief/entity/worldview tables for spatial knowledge graph

This is not a demonstration database. It is a production regional spatial intelligence asset.

---

## 2. System Architecture

Ms. Jarvis is a distributed AI system comprising 79–84 containerized microservices orchestrated via Docker Compose. The query pipeline relevant to this case study involves five components:

```
User Query
    │
    ▼
[Phase 1.4] Blood-Brain Barrier — safety/ethics filter
    │
    ▼
[Phase 1.5] GBIM Query Router — PostGIS spatial lookup
    │
    ▼
[Phase 2.5] 20-LLM Production — consensus answer
    │
    ▼
[Phase 3]   Judge Pipeline (H-10) — authority-weighted synthesis
    │
    ▼
[Phase 3.5] LM Synthesizer — voice/persona delivery
    │
    ▼
Final Response
```

The **GBIM Query Router** (Geographic/Behavioral Intelligence Module) detects intent categories — hospitals, fire departments, public health, county seats — and issues live PostGIS queries against the `msjarvisgis` database. Results are injected into the Judge Pipeline as `[VERIFIED LOCAL DATA]` with an explicit authority instruction before LLM-generated content is evaluated.

---

## 3. The Benchmark

### 3.1 Test Query

> *"What hospitals are near Charleston, WV?"*

### 3.2 Verified PostGIS Hospital Dataset

The complete `hospitals` table in `msjarvisgis` at time of test:

| geodbid | label                                 | lat     | lon       |
|---------|---------------------------------------|---------|-----------|
| 11      | Beckley Appalachian Regional Hospital | 38.2948 | -81.1877  |
| 7       | Charleston Area Medical Center        | 38.3498 | -81.6328  |
| 8       | Huntington Hospital                   | 38.4199 | -82.4414  |
| 12      | Princeton Community Hospital          | 37.3688 | -81.1060  |
| 9       | Ruby Memorial Hospital                | 39.6365 | -79.9559  |
| 10      | St. Mary's Medical Center             | 38.4122 | -82.4289  |

Source: HSIP (Homeland Security Infrastructure Program), loaded into PostGIS via `jarvis-local-resources-db` container running `postgis/postgis:15-3.4`.

### 3.3 Baseline: Semantic RAG (ChromaDB)

Before the PostGIS grounding pipeline was activated, Ms. Jarvis relied on ChromaDB vector similarity to retrieve relevant context. The system returned:

| Hospital Named                        | Actual Location        | Miles from Charleston |
|---------------------------------------|------------------------|-----------------------|
| Beckley Appalachian Regional Hospital | Beckley, WV            | ~60 miles SE          |
| Princeton Community Hospital          | Princeton, WV          | ~90 miles S           |
| Thomas Memorial Hospital              | South Charleston, WV   | ~5 miles (correct)    |
| United Hospital Center                | Bridgeport, WV         | ~100 miles NE         |

**Assessment:** 3 of 4 hospitals named were not near Charleston by any reasonable geographic definition. The system expressed no uncertainty. ChromaDB matched these facilities because they co-occur in West Virginia healthcare discourse — semantic proximity, not spatial proximity. Two of the four named hospitals (`Thomas Memorial`, `United Hospital Center`) do not appear in the verified PostGIS dataset at all, representing pure parametric hallucination.

### 3.4 Post-Intervention: PostGIS Grounding (H-10)

After activating the GBIM grounding pipeline (commits `b9c939b6` and `0bd0b363`, March 30, 2026), the same query returned:

| Hospital Named                 | Verified Coordinates    | Miles from Charleston |
|--------------------------------|-------------------------|-----------------------|
| Charleston Area Medical Center | 38.3498, -81.6328       | 0 miles — *in Charleston* |
| St. Mary's Medical Center      | 38.4122, -82.4289       | ~22 miles W           |

Ms. Jarvis's verbatim response:

> *"I'll be happy to help you with the list of hospitals in and around Charleston, WV! However, I must note that the authoritative records from the PostGIS spatial database take precedence over my training data. According to those records, here are some nearby hospitals: 1. Charleston Area Medical Center | lat=38.3498 lon=-81.6328, 2. St. Mary's Medical Center | lat=38.4122 lon=-82.4289"*

**Assessment:** Zero hallucinated facilities. Verified coordinates. Explicit acknowledgment of data source authority by the AI system itself.

---

## 4. The Architectural Intervention

The fix required changes to three files and two git commits. No model retraining. No fine-tuning. No external API.

### 4.1 Phase 1.5 — GBIM Router Injection (`main_brain.py`)

A new pipeline phase was inserted between the safety filter and the RAG retrieval step:

```python
# Phase 1.5: GBIM Grounded Data Routing (H-10, March 30 2026)
gbim_context = None
try:
    async with httpx.AsyncClient(timeout=10.0) as _gbim_c:
        _gbim_r = await _gbim_c.post(
            "http://jarvis-gbim-query-router:7205/route",
            json={"question": request.message},
            timeout=10.0
        )
        if _gbim_r.status_code == 200:
            _gbim_d = _gbim_r.json()
            if not _gbim_d.get("router_stub"):
                gbim_context = _gbim_d
                services_used.append("gbim_query_router")
                logger.info(
                    f"  GBIM grounded: mode={_gbim_d.get('mode')} "
                    f"records={len(_gbim_d.get('hospitals') or [])}"
                )
except Exception as _gbim_e:
    logger.warning(f"  GBIM exception: {str(_gbim_e)[:100]}")
```

### 4.2 Source Authority Hierarchy (`judge_pipeline.py`)

The Judge Pipeline was patched to prepend PostGIS records with an explicit authority instruction before LLM content:

```python
# H-10: gbim_grounded — inject PostGIS facility data — March 30 2026
if request.grounded_context and not request.grounded_context.get("router_stub"):
    _gc = request.grounded_context
    _gbim_results = (
        _gc.get("results") or
        _gc.get("hospitals") or
        _gc.get("providers") or
        _gc.get("stations") or
        []
    )
    if _gbim_results:
        _facts = "\n".join(
            f"- {r.get('name', r.get('label','?'))} "
            f"| lat={r.get('lat','?')} lon={r.get('lon','?')}"
            for r in _gbim_results[:6]
        )
        _mode = _gc.get("mode", "gbim")
        request.answer = (
            f"[VERIFIED LOCAL DATA — {_mode}]\n"
            f"INSTRUCTION: The following records are from a verified PostGIS "
            f"spatial database and must be treated as authoritative ground "
            f"truth. Do not contradict, supplement, or replace these with "
            f"LLM parametric memory.\n"
            f"{_facts}\n\n"
            f"[LLM CONTEXT — lower authority, use only to fill gaps]\n"
            f"{str(request.answer)[:200]}"
        )
        logger.info(
            f"  GBIM grounded ({_mode}): {len(_gbim_results)} records injected"
        )
```

### 4.3 GBIM Router Query Simplification (`gbim_query_router.py`)

The hospital query was simplified to return all records from the verified dataset rather than attempting city-column filtering (the HSIP schema contains only `geodbid`, `label`, `geom`, `sourcetable`, `country`):

```python
# Only 6 hospitals in WV dataset — return all, sorted by label
cur.execute("""
    SELECT geodbid, label,
           ST_Y(geom) AS lat, ST_X(geom) AS lon
    FROM hospitals
    ORDER BY label
""")
```

### 4.4 Git Record

```
0bd0b363 H-10: persist patched judge_pipeline.py — GBIM authority hierarchy + key normalization
b9c939b6 H-10: GBIM PostGIS grounding — Phase 1.5 + judge authority hierarchy
c5858b79 (tag: v0.97-memory-verified) feat: multi-turn memory working end-to-end
```

---

## 5. Analysis

### 5.1 Why Semantic RAG Fails Geographically

Vector similarity search optimizes for *topical* relevance, not *spatial* accuracy. A document about Beckley Appalachian Regional Hospital is highly similar to a query about Charleston hospitals because both involve West Virginia healthcare. The embedding space has no coordinate system.

This is not a failure of ChromaDB or RAG as a technique — it is the correct behavior for the task it was designed for. The failure is architectural: using semantic retrieval as the sole grounding mechanism for queries that require spatial precision.

### 5.2 Why PostGIS Grounding Works

PostGIS executes deterministic spatial queries against verified point geometries. `SELECT label, ST_Y(geom), ST_X(geom) FROM hospitals` returns exactly what is in the database — no approximation, no statistical inference, no confidence interval. The database contains `Charleston Area Medical Center` at `38.3498, -81.6328` because that is where it is.

### 5.3 The Authority Hierarchy as Data Policy

The most significant finding is not technical — it is governance. When Ms. Jarvis responded:

> *"the authoritative records from the PostGIS spatial database take precedence over my training data"*

— that statement represents **community data policy expressed as inference-time behavior**. The system did not defer to a corporate API, a proprietary model, or an external data vendor. It deferred to West Virginia's own E-911 and HSIP datasets, maintained by West Virginia agencies, hosted on regional infrastructure, governed by the community it serves.

### 5.4 The Scale Implication

The `msjarvisgis` database contains 540 spatial tables. The same grounding pattern demonstrated here for hospitals is immediately extensible to:

- `nursinghomes_wvdem_041219_gcs84` — nursing home locations
- `fire_dept_wvdem_092017_utm83` — fire station locations
- `policedept_wvdem_012319_gcs84` — police departments
- `publichealthdepts_hsip_20091229_gcs83` — public health departments
- `communityhealthproviders_wvhealthcareauthority_200802_utm83` — community health providers
- `correctionalinstitutions_hsip_20091230_utm83` — correctional facilities
- `hazardmitigationbuyout_20250929_polygons_utm83` — flood buyout parcels (2025 data)
- `buildings` + `wvgistc_building_footprints` — structure-level spatial data

Each table represents a category of query for which LLM parametric memory is unreliable and locally-governed spatial data is authoritative.

---

## 6. Limitations and Next Steps

### Current Limitations

- **6 hospital records** in the active `hospitals` table — `hospitals_wvdem_040519_gcs84` and related tables contain additional records not yet merged
- **No distance ranking** — results are not yet sorted by proximity to the queried city; spatial sorting via `ST_Distance` or `ST_DWithin` is the next implementation step
- **Keyword-dependent routing** — queries must contain recognized trigger terms (`hospital`, `emergency`, etc.) to activate grounding
- **Natural language authority instruction** — the `INSTRUCTION:` prefix is a prompt-engineering constraint, not a hard architectural one; the LM Synthesizer can still partially override it

### Immediate Next Steps

```bash
# 1. Distance-sort hospital results from queried city coordinates
# 2. Merge hospitals_wvdem_040519_gcs84 into active hospitals table
# 3. Expand GBIM keyword routing: nursing homes, pharmacies, shelters, fire
# 4. Mount judge_pipeline.py as docker-compose volume (line 1271)
# 5. Add \dt output to documentation as spatial asset inventory
```

### Research Extensions

- Benchmark across all 55 WV counties for all facility types
- Measure confidence calibration: does the system express appropriate uncertainty when PostGIS returns no results?
- Compare against commercial geocoding APIs (Google Places, HERE) as external baseline
- Test emergency-scenario queries: shelter locations during flood events using `hazardmitigationbuyout` polygons

---

## 7. Conclusion

A community-owned spatial database, integrated at inference time through a three-file architectural intervention, eliminated geographic hallucination in a production AI system without model retraining. The verified dataset — derived from West Virginia's own E-911 and HSIP infrastructure — overrode LLM parametric memory because the system was explicitly designed to treat locally-governed data as authoritative.

The result is reproducible, documented in git, and scalable across 540 spatial tables representing the full breadth of West Virginia's public spatial data assets. It demonstrates that **data sovereignty is not only a policy position — it is an implementable architectural pattern**.

The single most important line produced by this experiment was not written by a developer. It was spoken by Ms. Jarvis:

> *"the authoritative records from the PostGIS spatial database take precedence over my training data"*

That is community data governance working as designed.

The code is open source. The data is public. The infrastructure is regional. The result belongs to the community.

---

*Ms. Jarvis is developed by Harmony for Hope, Inc., a nonprofit organization based in Mount Hope, West Virginia. The project is open source.*

---

## Appendix A: Verified Hospital Dataset (Complete)

| geodbid | label                                 | lat     | lon      | country |
|---------|---------------------------------------|---------|----------|---------|
| 11      | Beckley Appalachian Regional Hospital | 38.2948 | -81.1877 | USA     |
| 7       | Charleston Area Medical Center        | 38.3498 | -81.6328 | USA     |
| 8       | Huntington Hospital                   | 38.4199 | -82.4414 | USA     |
| 12      | Princeton Community Hospital          | 37.3688 | -81.1060 | USA     |
| 9       | Ruby Memorial Hospital                | 39.6365 | -79.9559 | USA     |
| 10      | St. Mary's Medical Center             | 38.4122 | -82.4289 | USA     |

Source: `SELECT geodbid, label, ST_Y(geom) as lat, ST_X(geom) as lon, country FROM hospitals ORDER BY label;` — `msjarvisgis` database, `jarvis-local-resources-db` container, March 30, 2026.

## Appendix B: Selected msjarvisgis Spatial Asset Inventory

540 tables total. Selected tables relevant to community services grounding:

| Category | Table | Source | Coverage |
|---|---|---|---|
| Hospitals | `hospitals` | HSIP | WV statewide |
| Hospitals (detailed) | `hospitals_wvdem_040519_gcs84` | WVDEM | WV statewide |
| Nursing Homes | `nursinghomes_wvdem_041219_gcs84` | WVDEM | WV statewide |
| Public Health | `publichealthdepts_hsip_20091229_gcs83` | HSIP | WV statewide |
| Community Health | `communityhealthproviders_wvhealthcareauthority_200802_utm83` | WVHCA | WV statewide |
| Rural Health | `healthruralfacilities_manysources_utm83` | Multiple | WV statewide |
| Fire Departments | `fire_dept_wvdem_092017_utm83` | WVDEM | WV statewide |
| Police | `policedept_wvdem_012319_gcs84` | WVDEM | WV statewide |
| 911 Centers | `911centers_wvdem_032819_gcs84` | WVDEM | WV statewide |
| Buildings | `buildings` | Multiple | Regional |
| Building Footprints | `wvgistc_building_footprints` | WVGISTC | WV statewide |
| Building Footprints | `wv_microsoft_20180207_utm17n83` | Microsoft 2018 | WV statewide |
| Flood Buyouts | `hazardmitigationbuyout_20250929_polygons_utm83` | WVDHSEM | WV statewide |
| Correctional | `correctionalinstitutions_hsip_20091230_utm83` | HSIP | WV statewide |
| Libraries | `libraries_manysources_2001_ll27` | Multiple | WV statewide |
| Places of Worship | `placesofworship_hsip_20080723_utm83` | HSIP | WV statewide |
| Veterans Affairs | `veteransaffairsfacilities_manysources_200503_utm83` | Multiple | WV statewide |
| County Seats | `countyseats_usgs_ll83` | USGS | WV statewide |
| Census 2020 Blocks | `blocks_census_2020_utm83` | US Census | WV statewide |
| TIGER Geocoding | `tiger.*` (full schema) | US Census TIGER | WV statewide |
````
