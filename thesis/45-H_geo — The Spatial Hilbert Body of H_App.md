# 45. H_geo — The Spatial Hilbert Body of H_App

*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: May 16, 2026*

---

## Why This Is a Second Hilbert Space

\(H_{\text{geo}}\) is not a metaphor and not a subsystem of \(H_{\text{App}}\). It is a
genuinely distinct mathematical object — a second inner product space instantiated on
the same physical machine as \(H_{\text{App}}\) but with a different basis, a different
metric, different operators, and a different physical store.

| Property | \(H_{\text{App}}\) — Ch. 4 | \(H_{\text{geo}}\) — Ch. 45 |
|---|---|---|
| Space | \(\mathbb{R}^{384}\) | \(\mathbb{R}^2\) (geodesic surface) |
| Inner product | Cosine similarity | PostGIS geodesic distance (`ST_Distance`) |
| Vectors | 384-dim semantic embeddings | Coordinate geometries: points, polygons, lines |
| Physical store | `jarvis-chroma` ChromaDB | `jarvis-local-resources-db` PostGIS 15-3.4 |
| Database | ChromaDB collections | `msjarvisgis` (owner: msjarvis) + `local_resources` |
| Primary SRID | — | EPSG:4326 (230 layers) + EPSG:4269 (12 layers) |
| Dimension | 384 | 2 (geodesic lat/lon) |
| Basis | `all-minilm:latest` | WGS84 / NAD83 ellipsoid |
| Total geometry tables | 48 collections | **242 geometry tables** |
| Total geometry rows | ~6.74M vectors | **~26.96M geometry features** |

The two spaces share one physical bridge: `gbim_worldview_entities` in ChromaDB (5.4M L2
vectors, Chapter 44) encodes geographic place-names and spatial relationships as semantic
vectors, projecting \(H_{\text{geo}}\) into \(H_{\text{App}}\). This is the tensor product
connection — the operator that allows a query in one space to retrieve context from the other.

**★ Confirmed operational — May 16, 2026. 242 geometry tables across two databases.
26.9M rows in `geospatial_features` alone. `wv_buildings` 1,055,625 polygons. 
`fayette_parcels` 39,515 parcels. `census_tl_2020_54_tabblock20` 72,558 blocks.
`jarvis-local-resources-db` container: postgis/postgis:15-3.4, host port 5435.**

---

## 45.1 Physical Instantiation

\(H_{\text{geo}}\) is physically instantiated across two PostgreSQL/PostGIS databases
in the `jarvis-local-resources-db` container.

### 45.1.1 Container Configuration

| Property | Value |
|---|---|
| Container name | `jarvis-local-resources-db` |
| Image | `postgis/postgis:15-3.4` |
| Host port | **5435** → internal 5432 |
| Primary database | `msjarvisgis` (owner: `msjarvis`) |
| Secondary database | `local_resources` (owner: `postgres`) |
| PostGIS extension | 3.4 |
| PostgreSQL version | 15 |

### 45.1.2 Database Roles

| Role | Attributes |
|---|---|
| `msjarvis` | Superuser — owns `msjarvisgis` |
| `postgres` | Superuser, Create role, Create DB, Replication, Bypass RLS — owns `local_resources` |

---

## 45.2 The Geometry of H_geo

\(H_{\text{geo}}\) is a two-dimensional geodesic space. Every point in the space is a
coordinate pair \((\lambda, \phi)\) — longitude and latitude — on the WGS84 ellipsoid
(EPSG:4326) or the NAD83 ellipsoid (EPSG:4269). The inner product that defines proximity
in this space is the PostGIS geodesic distance operator:

\[
d(\mathbf{p}_i, \mathbf{p}_j) = \text{ST\_Distance}(\mathbf{p}_i\text{::geography}, \mathbf{p}_j\text{::geography})
\]

which returns the shortest path distance in meters along the ellipsoidal surface — not
the flat-plane approximation. For polygon and line geometries, proximity is defined by
`ST_DWithin`, `ST_Intersects`, and `ST_Contains` — the spatial join operators that
replace the cosine similarity query of \(H_{\text{App}}\).

### 45.2.1 Coordinate Reference Systems

| SRID | Name | Layer count | Usage |
|---|---|---|---|
| EPSG:4326 | WGS84 Geographic | 230 | Primary — all modern WV layers |
| EPSG:4269 | NAD83 Geographic | 12 | Legacy TIGER/Census layers |

All geometry is stored in 2D (`coord_dimension = 2`). Elevation data (3D) is not yet
present in confirmed layers.

### 45.2.2 Geometry Type Distribution

| Type | Count | Examples |
|---|---|---|
| POINT | 221 | 911 centers, bridges, hospitals, schools, fire stations |
| MULTIPOLYGON | 15 | Counties, census tracts, ZIP codes, parcels |
| POLYGON | 3 | Census block groups, tabblocks, Fayette parcels |
| MULTILINESTRING | 1 | Address edges |
| LINESTRING | 1 | Address features |
| GEOMETRY | 1 | `geospatial_features` — mixed master table |

---

## 45.3 The msjarvisgis Database — Spatial Layer Inventory

`msjarvisgis` contains 242 geometry-registered tables and 232 total public tables.
The confirmed populated layers (non-zero row count) are the operational substrate of
\(H_{\text{geo}}\):

### 45.3.1 Confirmed Populated Geometry Layers

| Table | Type | Row count | Domain |
|---|---|---|---|
| `geospatial_features` | GEOMETRY | **26,923,473** | Master spatial feature store — mixed geometry |
| `census_tl_2020_54_tabblock20` | POLYGON | 72,558 | WV 2020 Census blocks |
| `census_tl_2020_us_zcta520` | MULTIPOLYGON | 33,791 | US ZIP Code Tabulation Areas 2020 |
| `census_tl_2020_us_zcta510` | MULTIPOLYGON | 33,144 | US ZIP Code Tabulation Areas 2010 |
| `census_tl_2020_us_county` | MULTIPOLYGON | 3,234 | US county boundaries |
| `wv_buildings` | POLYGON | **1,055,625** | WV building footprints |
| `fayette_parcels` | MULTIPOLYGON | 39,515 | Fayette County parcel boundaries |
| `mvw_gbim_landowner_spatial` | MULTIPOLYGON | 38,979 | GBIM landowner spatial view |
| `census_tl_2020_54_bg` | POLYGON | 1,639 | WV 2020 Census block groups |

> **Note on zero-row layers.** 221 of 242 geometry tables are registered in
> `geometry_columns` but contain zero rows. These are schema-present but data-absent —
> they represent the intended layer coverage of \(H_{\text{geo}}\), not its current
> populated state. Loading these layers is the primary open item for spatial corpus
> completion (OI-C45-LOAD).

---

## 45.4 The local_resources Database — Community Intelligence Layer

`local_resources` is the second physical component of \(H_{\text{geo}}\). It is not a
raw geometry store — it is the **community intelligence overlay**: the tables that
connect spatial coordinates to lived human infrastructure in West Virginia and Appalachia.

### 45.4.1 Confirmed Tables — local_resources

The 69 tables in `local_resources` span five functional domains:

**WV Address and Building Infrastructure**

| Table | Description |
|---|---|
| `wv_address_points_raw` | Raw WV address point dataset |
| `wv_address_aliases` | Address alias resolution |
| `wv_address_dual` | Dual-range address matching |
| `wv_address_zones` | Address zone polygons |
| `wv_buildings` | WV building footprints (shared with msjarvisgis) |
| `wv_industrial_buildings` | Industrial building inventory |
| `wv_office_buildings` | Office building inventory |
| `wv_wvgistc_buildings` | WVGISTC building dataset |
| `building_profile` | Enriched building profiles |
| `enriched_buildings_with_samb` | Buildings with SAMB data joined |

**WV Emergency and Civic Services**

| Table | Description |
|---|---|
| `wv_ems_stations` | EMS station locations |
| `wv_fire_stations` | Fire station locations |
| `wv_fire_stations_clean` | Deduplicated fire station dataset |
| `wv_hospitals` | Hospital locations |
| `wv_floodplain_structures` | Floodplain structure registry |
| `wv_hazard_buyouts` | Hazard buyout property records |
| `wv_aml_lines` | Abandoned mine land — lines |
| `wv_aml_points` | Abandoned mine land — points |
| `wv_aml_polygons` | Abandoned mine land — polygons |
| `wv_mineral_operations` | Active mineral operations |

**WV Administrative and Tax Geography**

| Table | Description |
|---|---|
| `wv_counties` | WV county table |
| `wv_county_boundaries_raw` | Raw county boundary data |
| `wv_county_lookup` | County FIPS and name lookup |
| `wv_municipalities` | WV municipal boundaries |
| `wv_parcels` | WV parcel registry |
| `wv_tax_districts` | Tax district definitions |
| `wv_tax_districts_poly` | Tax district polygons |
| `wv_zip_codes` | WV ZIP code boundaries |
| `wv_zip_zcta_raw` | ZIP-to-ZCTA crosswalk raw |
| `wv_samb_north` | SAMB structure data — northern WV |
| `wv_samb_south` | SAMB structure data — southern WV |
| `gbim_zcta_2020` | GBIM ZCTA 2020 layer |

**Community Resources and MountainShares Integration**

| Table | Description |
|---|---|
| `community_resources` | Community resource registry |
| `local_resources` | Local resource catalog |
| `local_resources_index` | Resource search index |
| `gbim_worldview_entity` | GBIM worldview entity table (bridge to \(H_{\text{App}}\)) |
| `mountainshares_balances` | MountainShares token balances |
| `mountainshares_ledger` | MountainShares transaction ledger |
| `mountainshares_participation` | Participation registry |
| `ms_governance_log` | Governance action log |
| `ms_participation` | Participation records |
| `ms_reserve_bands` | Reserve band definitions |
| `ms_treasury` | Treasury state |
| `ms_user_profile` | User profiles |
| `founder_tokens` | Founder token registry |
| `travel_regions` | Travel region definitions |

**Identity and Security**

| Table | Description |
|---|---|
| `ueid_immutable_security` | Universal Entity ID immutable security records |
| `spatial_role_scopes` | Role-scoped spatial access definitions |
| `user_longterm_memory` | Long-term user memory store |
| `conversation_beliefs` | Conversation belief state |
| `county_lookup` | County lookup table |
| `us_counties` | US county reference table |
| `us_zips` | US ZIP code reference table |

---

## 45.5 The Tensor Product Bridge

The connection between \(H_{\text{geo}}\) and \(H_{\text{App}}\) is the
`gbim_worldview_entity` table in `local_resources` and the `gbim_worldview_entities`
collection in ChromaDB (5,416,521 vectors, L2 metric, Chapter 44).

The bridge works as follows:

**Forward projection** \(H_{\text{geo}} \rightarrow H_{\text{App}}\): A geographic
entity (parcel, building, flood zone, mine site) is embedded via `all-minilm:latest`
and stored in `gbim_worldview_entities`. Semantic queries in \(H_{\text{App}}\) can
retrieve geographic entities by meaning — "flood-prone communities near Fayette County"
retrieves parcel and building records whose spatial attributes were encoded as text and
embedded.

**Backward projection** \(H_{\text{App}} \rightarrow H_{\text{geo}}\): A semantic
retrieval result containing a geographic reference (place name, parcel ID, ZIP code) is
resolved against `local_resources` tables via `ST_DWithin` or exact join — returning
the spatial geometry for map rendering, proximity analysis, or further spatial query.

**The tensor product.** In \(H_{\text{App}} \otimes H_{\text{geo}}\), a query state
vector \(\psi\) is not purely semantic or purely spatial — it is a superposition of both.
The `jarvis-gis-rag` service (port 8004) is the operator that collapses this superposition
into a concrete retrieval result by dispatching to whichever space the query primarily
inhabits, then enriching with the other.

---

## 45.6 The Spatial Coherence Score — Geo-Phi

Where Chapter 44 defined the phi score as the mean pairwise cosine similarity of semantic
centroids in \(H_{\text{App}}\), the analogous instrument for \(H_{\text{geo}}\) is
the **geo-phi score** — a measure of spatial coverage coherence across the active
geometry layers of \(H_{\text{geo}}\).

Geo-phi is defined as the fraction of West Virginia's geographic extent covered by
populated geometry layers, weighted by domain importance:

\[
\phi_{\text{geo}} = \frac{1}{W} \sum_{i=1}^{N} w_i \cdot \mathbb{1}[\text{rows}(L_i) > 0]
\]

where \(L_i\) is the \(i\)-th geometry layer, \(w_i\) is its domain weight, and \(W\)
is the sum of all weights.

**Current state (May 16, 2026):**

\[
\phi_{\text{geo}} = \frac{9}{242} \approx 0.037 \text{ (raw populated fraction)}
\]

9 of 242 registered geometry layers are populated. The remaining 233 layers are
schema-present, data-absent. This is the primary open item — loading the WV GIS data
corpus that the schema was built to receive.

> **Note on geospatial_features.** The single table `geospatial_features` (26.9M rows,
> GEOMETRY type) may itself represent a consolidation of many of the 221 empty point
> layers. Row count queries against it confirm it is the dominant populated table in
> \(H_{\text{geo}}\). Its internal feature type distribution requires a schema inspection
> to determine effective layer coverage — see OI-C45-GEOFEATURES.

---

## 45.7 The jarvis-gis-rag Service

`jarvis-gis-rag` (host port 8004, image `db9c58f414fd`) is the query interface layer
for \(H_{\text{geo}}\). It translates natural-language spatial queries into PostGIS
operations and returns structured geographic results to the RAG pipeline.

```bash
# Health check
curl -s http://localhost:8004/health | python3 -m json.tool

# Inspect available endpoints
curl -s http://localhost:8004/docs | python3 -m json.tool

# Test a spatial query
curl -s -X POST http://localhost:8004/query \
  -H "Content-Type: application/json" \
  -d '{"query": "fire stations in Fayette County", "limit": 5}' \
  | python3 -m json.tool
```

---

## 45.8 Operational Procedures

```bash
# Connect to msjarvisgis
docker exec jarvis-local-resources-db psql -U msjarvis -d msjarvisgis

# Connect to local_resources
docker exec jarvis-local-resources-db psql -U postgres -d local_resources

# Count populated vs empty geometry layers
docker exec jarvis-local-resources-db psql -U msjarvis -d msjarvisgis -c "
SELECT
  COUNT(*) FILTER (WHERE row_count > 0) AS populated,
  COUNT(*) FILTER (WHERE row_count = 0) AS empty,
  COUNT(*) AS total
FROM (
  SELECT f_table_name,
    (xpath('/row/cnt/text()',
      query_to_xml('SELECT COUNT(*) AS cnt FROM ' || quote_ident(f_table_name),
      false, true, '')))::text::int AS row_count[1]
  FROM geometry_columns
) sub;
"

# WV bounding box coverage check
docker exec jarvis-local-resources-db psql -U msjarvis -d msjarvisgis -c "
SELECT ST_AsText(ST_Extent(geom)) AS wv_extent
FROM census_tl_2020_us_county
WHERE ST_Within(
  ST_Centroid(geom),
  ST_MakeEnvelope(-82.65, 37.20, -77.72, 40.64, 4326)
);
"

# Fayette County parcel coverage
docker exec jarvis-local-resources-db psql -U msjarvis -d msjarvisgis -c "
SELECT COUNT(*), ST_AsText(ST_Extent(geom)) FROM fayette_parcels;
"

# local_resources community resource count
docker exec jarvis-local-resources-db psql -U postgres -d local_resources -c "
SELECT COUNT(*) FROM community_resources;
"
```

---

## 45.9 Open Items — May 16, 2026

| OI | Description | Status | Priority |
|---|---|---|---|
| OI-C45-GEOFEATURES | Inspect `geospatial_features` internal type distribution — 26.9M rows may consolidate many of the 221 empty point layers | 🔄 Open | High |
| OI-C45-LOAD | Load WV GIS corpus into 221 empty geometry layers — schema present, data absent | 🔄 Open | High |
| OI-C45-GEOGPHI | Implement `jarvis-geo-phi` service (analog of phi probe) — compute spatial coverage coherence score \(\phi_{\text{geo}}\) | 🔄 Open | Medium |
| OI-C45-SRID | Standardize 12 EPSG:4269 layers to EPSG:4326 for uniform geodesic distance computation | 🔄 Open | Medium |
| OI-C45-3D | Evaluate elevation (3D geometry, `coord_dimension=3`) for DEM layers — terrain model for Appalachian topology | 🔄 Open | Low |
| OI-C45-BRIDGE | Confirm `gbim_worldview_entity` (local_resources) ↔ `gbim_worldview_entities` (ChromaDB) sync is live | 🔄 Open | Medium |
| OI-C45-FAYETTE | `fayette_parcels` (39,515) and `mvw_gbim_landowner_spatial` (38,979) confirmed populated — verify spatial index health | 🔄 Open | Low |

---

## 45.10 Production Status Summary — May 16, 2026

| Component | Status | Notes |
|---|---|---|
| `jarvis-local-resources-db` | ✅ Operational | postgis/postgis:15-3.4, host port 5435 |
| `msjarvisgis` database | ✅ Live | Owner: msjarvis, 242 geometry tables |
| `local_resources` database | ✅ Live | Owner: postgres, 69 tables |
| `jarvis-gis-rag` | ✅ Running | host port 8004 — spatial query interface |
| Total geometry tables | ✅ 242 | 232 public tables in msjarvisgis |
| Populated geometry layers | ⚠ 9 of 242 | 233 layers schema-present, data-absent |
| `geospatial_features` | ✅ 26,923,473 rows | Master spatial store — GEOMETRY type |
| `wv_buildings` | ✅ 1,055,625 rows | WV building footprints — POLYGON |
| `fayette_parcels` | ✅ 39,515 rows | Fayette County parcels — MULTIPOLYGON |
| `mvw_gbim_landowner_spatial` | ✅ 38,979 rows | GBIM landowner view — MULTIPOLYGON |
| `census_tl_2020_54_tabblock20` | ✅ 72,558 rows | WV 2020 Census blocks — POLYGON |
| `census_tl_2020_us_county` | ✅ 3,234 rows | US county boundaries — MULTIPOLYGON |
| Primary SRID | ✅ EPSG:4326 | 230 of 242 layers |
| GBIM bridge to \(H_{\text{App}}\) | ✅ Schema present | `gbim_worldview_entity` in local_resources |
| MountainShares tables | ✅ Present | 7 tables in local_resources |
| Inner product operator | ✅ `ST_Distance` | Geodesic — WGS84 ellipsoidal surface |
| \(\phi_{\text{geo}}\) raw | ⚠ ~0.037 | 9/242 layers populated — corpus loading needed |
| Relationship to \(H_{\text{App}}\) | ✅ Defined | Tensor product via `gbim_worldview_entities` bridge |

---

*Chapter 45 authored by Carrie Ann Kidd — Mount Hope, West Virginia.*
*Ms. Jarvis is an original system designed and built by Carrie Ann Kidd.*
*See [LICENSE](../LICENSE) for terms.*
*Last verified: May 16, 2026 — jarvis-local-resources-db operational; postgis/postgis:15-3.4;
msjarvisgis: 242 geometry tables, 9 populated, 26.9M rows in geospatial_features,
1,055,625 wv_buildings, 39,515 fayette_parcels, 72,558 census blocks;
local_resources: 69 tables including community_resources, MountainShares ledger,
GBIM worldview entity bridge; primary SRID EPSG:4326; inner product ST_Distance geodesic;
phi_geo raw 0.037 (9/242 populated); tensor product bridge to H_App via gbim_worldview_entities
(5,416,521 L2 vectors, ChromaDB); msjarvis-rebuild namespace; host port 5435.*
