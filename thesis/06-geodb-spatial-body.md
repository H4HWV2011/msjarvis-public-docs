## Why This Matters for Polymathmatic Geography

This chapter defines the spatial "body" of Ms. Jarvis and specifies how West Virginia's physical infrastructures, hazards, civic facilities, and benefits-related sites are represented as a mature, computable geography. It supports:

- **P1 – Every where is entangled** by representing structures, rivers, floodplains, institutions, and program sites as a connected mesh rather than isolated map layers, and by linking them to GBIM belief records and spatial embeddings derived from the PostgreSQL `msjarvisgis` database — specifically from `gbimbeliefnormalized` (5.4M+ verified rows) and related worldview tables, including the unified GBIM belief collection `gbim_beliefs_v2` that is already in production.

- **P3 – Power has a geometry** by enabling operational analysis of how risk, access, infrastructure, and access-to-help are distributed across counties, hollows, ZIP codes, and corridors, and by exposing these distributions through PostGIS queries in the PostgreSQL `msjarvisgis` database and through vector-backed RAG neighborhoods over GBIM-derived spatial collections and benefits-focused collections such as `gis_wv_benefits`.

- **P5 – Design is a geographic act** by showing how concrete schema choices, key conventions, CSV pipelines, RAG routing, collection design, layer prioritization, and parcel classification decisions in the live GBIM/GeoDB/Chroma stack have already reshaped how the state "appears" in analysis, governance, and search — and how those choices carry consequences for the households the system is meant to serve.

- **P12 – Intelligence with a ZIP code** by binding Ms. Jarvis's reasoning to a concrete, statewide PostgreSQL PostGIS geodatabase (`msjarvisgis`, port 5432, 91 GB with 501 tables), to a spatially resolved `local_resources` registry keyed by building, parcel, county, and tax district, and to their embeddings — especially the unified GBIM belief collection `gbim_beliefs_v2` and the `gis_wv_benefits` collection used in GIS RAG flows — so that queries about help, risk, or opportunity are resolved through structures that explicitly encode where people live and which institutions serve them.

- **P16 – Power accountable to place** by ensuring that advisory and governance behaviors are traceable to specific, queryable features, facilities, and programme footprints in West Virginia, with logged retrieval paths from the PostgreSQL `msjarvisgis` database, GBIM belief tables, vector collections such as `gbim_beliefs_v2` and `gis_wv_benefits`, and `local_resources` into the ensemble stack and governance logs — and by being honest about the limits of parcel-level resolution where the underlying data does not support it.

The question "I need help" contains a location. The location contains a history. The history contains a set of programs, hazards, rights, and remedies that the person asking may not know exist. Ms. Jarvis's spatial body exists to make that knowledge computable and to surface it without requiring the person to already know what to ask for.

Accordingly, this chapter belongs to the **Computational Instrument** tier: it specifies the geospatial substrate — centred on the PostgreSQL 16 `msjarvisgis` PostGIS database (port 5432, 91 GB, 501 tables), the current GBIM corpus (5.4M+ verified beliefs), and their Chroma collections — that already allows Quantarithmia's justice-oriented reasoning to operate on real communities, infrastructures, and landscapes in Appalachia and to route actual households to concrete, locally valid forms of assistance.

---

## 6. GeoDB and the Spatial Body of Ms. Jarvis

### 6.1 Purpose and Scope

This chapter describes the geospatial substrate that anchors Ms. Egeria Jarvis in the physical world of West Virginia. The GeoDB layer is tightly coupled to GBIM, to the Hilbert-space-backed semantic memory accessed via text and GIS RAG services, and to the verified `local_resources` registry, so that beliefs and narratives are grounded not only in abstract embeddings but also in specific buildings, river reaches, floodplains, mines, benefits hubs, and infrastructure corridors.

The focus is on the current structure and status of the PostgreSQL PostGIS-based geodatabase and its relationship to vector collections and RAG flows, rather than on exhaustive cataloguing of every dataset. Figure 6.1 summarizes the main containers and data stores involved in this spatial body.

**Database Configuration (Verified March 19, 2026):**
- **Type:** PostgreSQL 16 with PostGIS extensions
- **Database Name:** `msjarvisgis`
- **Port:** 5432 (host system)
- **Location:** /var/lib/postgresql/16/msjarvis
- **Size:** 91 GB
- **Tables:** 501 total (34 GBIM-related)
- **GBIM Corpus:** 5.4M+ verified beliefs across 5 main tables

**`local_resources` Database Configuration (Verified March 19, 2026):**
- **Type:** PostgreSQL 15 (Docker container: `jarvis-local-resources-db`)
- **Database Name:** `local_resources`
- **Role:** Spatially resolved building, parcel, county, and tax district registry
- **Key Views:** `building_with_parcel`, `parcel_with_county_tax`, `building_parcel_county_tax`
- **Key Materialized Views:** `county_tax_building_summary` (707 rows, sub-millisecond reads, concurrent refresh enabled)

```
┌─────────────────────────────────────────────────────────────┐
│                    Ms. Jarvis Architecture                   │
├─────────────────────────────────────────────────────────────┤
│  User Clients (Web, Mobile, API)                            │
│         ↓                                                    │
│  21-LLM Ensemble (Weighted Consensus)                       │
│         ↓                                                    │
│  ┌──────────────┬──────────────┬──────────────────────────┐ │
│  │ PostgreSQL   │ ChromaDB     │ Support Services         │ │
│  │ msjarvisgis  │ Vector Store │ (Redis, Neo4j)           │ │
│  │              │              │                          │ │
│  │ - PostGIS    │ - Embeddings │ - local_resources        │ │
│  │ - 501 tables │ - Collections│   (Postgres/Docker)      │ │
│  │ - GBIM       │   - beliefs  │ - Spatial cache          │ │
│  │   corpus     │   - spatial  │ - Graph relationships    │ │
│  │ - 91 GB      │   - benefits │                          │ │
│  └──────────────┴──────────────┴──────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6.1. High-level container-style view of the Ms. Jarvis Steward System, showing user clients, the 21-LLM ensemble, and the containerized backing stores (PostgreSQL PostGIS GeoDB, GBIM, ChromaDB vector store, `local_resources`, Redis, Neo4j). The diagram emphasizes PostgreSQL as the spatial backbone, GBIM as the worldview and belief layer, and spatial/benefits collections as the primary spatial memory in Hilbert space.

Within the Quantarithmia program, GeoDB constitutes the spatial backbone of Ms. Jarvis's "body": a coherent, queryable mesh of features and boundaries for reasoning about risk, access, infrastructure, and spatial justice. In the current deployment, this spatial backbone runs as part of a containerized microservice stack orchestrated with Docker Compose, alongside core services such as ChromaDB (the vector store exposed over HTTP and used as the canonical embedding store), Redis, Neo4j, the `local_resources` Postgres instance, and the multi-model ensemble.

The chapter documents what is currently integrated, which layers are staged, and how these components are linked into the broader Hilbert-space and GBIM framework, including their representation in GBIM belief embeddings (currently dominated by `gbim_beliefs_v2`) and in the `gis_wv_benefits` collection, and their use in `/chat/light`, `/chat/sync`, and benefits-focused RAG flows.

---

### 6.2 Operational Objectives and Current Capabilities

The GeoDB layer now satisfies three primary objectives:

- **Coherent statewide mesh.**
  It represents West Virginia as a coherent, queryable geospatial mesh of structures, hazards, networks, civic facilities, benefits sites, administrative boundaries, and named places, with millions of features integrated into a common, GBIM-aware schema within the PostgreSQL `msjarvisgis` database.

- **Programmatic access.**
  It provides fast, programmatic access to this mesh for reasoning, retrieval, visualization, and analytics through well-defined schemas, spatial indexes, and HTTP-accessible services that expose GBIM and GeoDB content to RAG.

- **Integration with GBIM, semantic memory, `local_resources`, and RAG.**
  It integrates cleanly with GBIM belief tables, the shared ChromaDB vector store, and the `local_resources` registry so that spatial, semantic, institutional, and programme dimensions are used together in a single reasoning pipeline.

Operationally, this entails a PostgreSQL PostGIS-backed geodatabase that holds authoritative feature classes for core themes and, for prioritized subsets, mirrors those features into GBIM belief embeddings and vector collections. Earlier deployments relied on numerous `geodb*` collections; in the 2026 deployment the primary spatial memory indices are the unified GBIM embedding collections (realized in practice as `gbim_beliefs_v2`) and the `gis_wv_benefits` collection, with legacy `geodb*` collections serving as thematic and historical subsets.

As of March 19, 2026, the `local_resources` database has been advanced from a flat ZIP/county registry into a spatially resolved infrastructure database. The full spatial chain — building → parcel → county → tax district — is now live and queryable, backed by the following objects:

| Object | Type | Status | Notes |
|---|---|---|---|
| `wv_tax_districts_poly` | Table | Live | 600 features, SRID 26917 + 4326, GiST indexed |
| `parcel_with_county_tax` | View | Live | ST_Within join: parcels → county + tax district |
| `building_parcel_county_tax` | View | Live | Full building → parcel → county → tax chain |
| `county_tax_building_summary` | Materialized View | Live | 707 rows, <1ms reads, concurrent refresh enabled |

---

### 6.3 PostGIS as Ms. Jarvis's Spatial Backbone

At the storage level, Ms. Jarvis uses a PostgreSQL 16 PostGIS database (`msjarvisgis`) as the main container for West Virginia vector datasets. This PostGIS instance runs on the host system (not in Docker) at /var/lib/postgresql/16/msjarvis and is accessed by multiple services for spatial reasoning and data access.

**Access Configuration:**

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="msjarvisgis",
    user="postgres"
)

cursor = conn.cursor()
cursor.execute("""
    SELECT COUNT(*) FROM gbimbeliefnormalized
    WHERE (where_axis->>'county') = 'Fayette'
""")
```

```bash
sudo -u postgres psql -p 5432 -d msjarvisgis
\dt gbim*
SELECT COUNT(*) FROM gbim_worldview_entity;
```

Feature classes are organized by theme and provenance — census units, structure points, building footprints, hydrology, transportation networks, hazards, facilities, benefits-relevant sites, and governance geometries — with consistent naming and key conventions across ingestion pipelines.

The core production schema includes:

- Raw and normalized source tables for individual datasets, such as county boundaries, census blocks, dams, hospitals, and other facilities.
- A set of CSV-derived tables (for example, `gbim_source_csv.*`) created from `*_attrs.csv` exports, which store key attributes (including `geodb_id`, `lat`, `lon`, `bbox`, `label`, `sourcetable`, `county`, and, where present, additional fields) converted directly from shapefiles and other GIS formats.
- GBIM-related tables (34 total), including:
  - `gbimbeliefnormalized` (5,416,522 rows, 21 GB) — the main belief table with nine JSONB axes
  - `gbim_worldview_entity` (5,416,521 rows, 47 GB) — entity relationships and worldview
  - `gbim_beliefs` (5,289,747 rows, 3 GB) — core beliefs with structured columns
  - `gbim_evidence` (2,121,230 rows, 680 MB) — supporting evidence
  - `gbim_belief_evidence` (2,121,230 rows, 232 MB) — belief-evidence linkages

Most production layers share a common projected coordinate system, SRID 26917 (UTM Zone 17N NAD83). Legacy tables that retain provisional SRIDs, mixed geometry types, or inconsistent precision are explicitly flagged for cleanup and are not included in the primary GBIM worldview until normalized.

The database is populated from state and federal sources including the WV GIS Technical Center, USGS, the U.S. Census Bureau, USACE, NREL, and various state agencies. Ingestion converts shapefiles and file geodatabases into PostGIS tables, resolves geometry and projection issues, and normalizes keys so that features can be cross-referenced from GBIM, ChromaDB, `local_resources`, and higher-level reasoning services.

---

### 6.4 Currently Integrated Statewide Layers

The current deployment includes a substantial, production-grade subset of West Virginia's public geospatial data, with additional layers actively being integrated. At a high level, the Steward System maintains:

- **Census units.**
  Statewide 2020 Census blocks and block groups in projected coordinate systems appropriate for analysis and mapping, providing population and administrative meshes at fine spatial scales.

- **Structures and buildings.**
  A dense statewide structure inventory composed of:
  - SAMB structure points in northern and southern regions,
  - WV GIS Technical Center building footprints numbering in the millions,
  - Microsoft-derived building points contributing additional structure-like locations.

  The multi-source nature of this inventory introduces duplication that must be managed explicitly before address extraction or program routing proceeds. See Section 6.4.1.

- **Hazard and infrastructure layers.**
  Datasets representing:
  - abandoned mine lands (lines and polygons),
  - dams (coal-related and non-coal-related),
  - floodplain structure inventories and flood hazard zones,
  - rail networks and terminals,
  - navigable waterways and river-mile indexing,
  - energy and communication infrastructure, where available.

- **Civic, facility, and benefits coverage.**
  Layers capturing:
  - hospitals, nursing homes, and other healthcare facilities,
  - fire and police stations and 911 centers,
  - higher-education institutions,
  - libraries and community centers,
  - parks and recreational sites,
  - solid waste facilities, sewer plants, and related utilities,
  - benefits-relevant facilities such as state and local offices, community action agencies, and local hubs, represented both as GeoDB features and as GBIM beliefs and mirrored into collections such as `gis_wv_benefits`.

- **Governance and index layers.**
  Tables representing:
  - county and state boundaries,
  - ZIP Code Tabulation Areas and related postal geography,
  - regional planning districts and similar governance regions,
  - tax district polygons (`wv_tax_districts_poly`, 600 features, verified March 19, 2026),
  - named places, summits, and other geographic names,
  - National Register points and polygons and related historic resources.

```
┌─────────────────────────────────────────────────────────────┐
│        West Virginia Statewide Geospatial Mesh              │
│              (msjarvisgis Database, 501 Tables)             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Census & Demographics        Infrastructure & Hazards      │
│  ┌──────────────────────┐    ┌──────────────────────┐      │
│  │ - Blocks (2020)      │    │ - Mines (abandoned)  │      │
│  │ - Block groups       │    │ - Dams               │      │
│  │ - ZIP codes          │    │ - Floodplains        │      │
│  │ - Counties           │    │ - Rail networks      │      │
│  └──────────────────────┘    │ - Waterways          │      │
│                               └──────────────────────┘      │
│  Structures & Buildings       Facilities & Services         │
│  ┌──────────────────────┐    ┌──────────────────────┐      │
│  │ - SAMB points        │    │ - Hospitals          │      │
│  │ - Building footprints│    │ - Libraries          │      │
│  │ - Microsoft points   │    │ - Benefits offices   │      │
│  │   (millions)        │    │ - Community centers  │      │
│  └──────────────────────┘    └──────────────────────┘      │
│                                                              │
│  All integrated with GBIM beliefs (5.4M+ rows)              │
│  All accessible via PostGIS spatial queries                 │
│  All embedded in ChromaDB for semantic retrieval            │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6.2. Conceptual overview of the statewide geospatial mesh maintained in PostgreSQL GeoDB and GBIM, summarizing integrated census units, structures, hazards, civic facilities, governance layers, and benefits-relevant sites.

---

### 6.4.1 The Multi-Source Building Inventory and Deduplication

The statewide structure inventory in `wv_buildings` is assembled from three independent sources, each produced by a different organization using different methodology, vintage, and coverage logic:

- **SAMB** (Statewide Address and Mapping Base) — structure points compiled from county assessor records
- **WV GIS Technical Center building footprints** — polygon footprints derived from aerial imagery, converted to centroids, with `sourcetable = wvgistc_building_footprints`
- **Microsoft building points** — machine-learning-derived structure detections from satellite imagery

This multi-source assembly is a strength — each dataset fills gaps the others leave, and together they produce the most complete statewide structure inventory available for West Virginia. But it introduces a well-defined problem: the same physical structure frequently appears as multiple rows in `wv_buildings` with different `building_id` values, different `sourcetable` values, and nearly identical but not identical coordinates.

This is not a data error. It is the honest consequence of combining three independently produced datasets that were never designed to reference each other.

**What Was Discovered Operationally**

During the March 19, 2026 spatial chain build — constructing the building → parcel → county → tax district linkage in `local_resources` — this duplication became operationally visible in two ways.

First, raw building counts from joins against `wv_buildings` overstate the true number of distinct structures. The `county_tax_building_summary` materialized view reports `building_count` values that represent source records, not necessarily distinct physical locations. The true count of distinct addressable structures is lower by a factor that varies by county and reflects the overlap between source datasets.

Second, the `building_parcel_county_tax` view revealed extreme building-per-parcel counts in the top offenders — parcels carrying 266 to 985 buildings. While most of these were explained by legitimate large-tract land ownership (federal land, coal company holdings, utility corridors, and placeholder district IDs), the multi-source duplication problem means that even on `standard` parcels, some building IDs represent the same physical structure counted twice or three times.

**The Deduplication Strategy**

Spatial deduplication identifies buildings within a threshold distance (5–15 meters, to be calibrated per source pair) that share the same parcel and assigns them a single canonical `building_id` for address and program routing. The diagnostic query pattern is:

```sql
SELECT
  a.building_id   AS building_a,
  b.building_id   AS building_b,
  a.sourcetable   AS source_a,
  b.sourcetable   AS source_b,
  ST_Distance(
    a.geom::geography,
    b.geom::geography
  )               AS dist_m
FROM wv_buildings a
JOIN wv_buildings b
  ON a.building_id < b.building_id
  AND ST_DWithin(a.geom::geography, b.geom::geography, 10)
WHERE a.sourcetable != b.sourcetable
LIMIT 100;
```

Until full deduplication is complete, all building counts in `county_tax_building_summary` and downstream reporting carry an explicit caveat: they represent source records, not verified distinct structures. This uncertainty is surfaced explicitly in RAG responses when building-level counts are cited, consistent with Ms. Jarvis's P16 commitment that power must be accountable to place — which requires being honest about the limits of the data, not just its capabilities.

The architectural solution is a `canonical_building_id` field, to be added to `wv_buildings` after deduplication, that collapses duplicates to a single authoritative record per physical structure. All program routing, address extraction, and GBIM belief generation will operate on `canonical_building_id` rather than raw `building_id` once that field is populated. This is a near-term roadmap item and a prerequisite for address extraction.

**Why This Matters for RAG and Program Routing**

The deduplication problem has a direct consequence for the geo-aware RAG pipeline described in Section 6.8. If a duplicate building record is resolved to a program entry in `local_resources`, the same household could appear to qualify for the same program under two different `building_id` values. In a benefits routing context this is not just an analytical error — it is a failure of the system's core promise to route real households to real help accurately.

---

### 6.5 Spatial Embeddings and Geo-Referenced Beliefs

To connect geometric features with high-dimensional semantic reasoning, Ms. Jarvis maintains collections derived from GBIM beliefs and spatial entities in the shared ChromaDB vector store. These collections are hosted in a shared HTTP-backed instance, configured with 384-dimensional embeddings, and serve as the canonical spatial memory layer for RAG.

```
┌─────────────────────────────────────────────────────────────┐
│   GeoDB → GBIM → ChromaDB → RAG Pipeline                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  PostgreSQL msjarvisgis                                      │
│  ┌────────────────────────────────────────────────┐         │
│  │  501 spatial tables                            │         │
│  │    ↓                                           │         │
│  │  gbimbeliefnormalized (5.4M rows)              │         │
│  │    - identity axis (source_table, source_pk)   │         │
│  │    - where axis (lat, lon, geometry)           │         │
│  │    - 9 JSONB axes total                        │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  ChromaDB Vector Collections                                │
│  ┌────────────────────────────────────────────────┐         │
│  │  gbim_beliefs_v2 (primary GBIM collection)     │         │
│  │    - Embeddings from 9 axes                    │         │
│  │    - Metadata: belief_id, source_table,        │         │
│  │      source_pk, epoch, spatial coords          │         │
│  │                                                │         │
│  │  gis_wv_benefits (benefits facilities)        │         │
│  │    - Benefits-specific embeddings              │         │
│  │    - Metadata: facility type, county, ZIP,     │         │
│  │      local_resource_id                         │         │
│  └────────────────────────────────────────────────┘         │
│              ↓                                               │
│  RAG Services → LLM Ensemble                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6.3. Key relationships between PostgreSQL GeoDB source tables, GBIM beliefs (`gbimbeliefnormalized`), worldview entities, and spatial/benefits collections in ChromaDB. Deterministic joins are maintained via identity fields (for example, `source_table` and `source_pk`) from embeddings back into GBIM and GeoDB.

- **Unified GBIM belief collections.**
  The primary collection is `gbim_beliefs_v2`, which holds embeddings for millions of beliefs derived from the nine JSONB axes. For each belief, a text representation is constructed from the axes (`identity`, `what`, `where`, `who`, `forwhom`, `why`, `how`, `authority`, `when`), and embeddings are stored with metadata including the belief identifier, `source_table` and `source_pk` values, epoch information, and optional spatial metadata inherited from `where`.

- **Benefits-focused spatial collection.**
  The `gis_wv_benefits` collection stores embeddings and metadata for benefits-relevant facilities, built from GBIM beliefs and resource descriptions. Documents encode facility names, locations, roles, and linkages to `local_resources` identifiers, enabling semantically and spatially aware retrieval of benefits sites.

- **Legacy and thematic `geodb*` collections.**
  Earlier deployments mirrored selected PostGIS layers into `geodb*` collections. These remain available as historical or specialized indexes but are no longer treated as the primary spatial memory layer; current work prefers `gbim_beliefs_v2` and `gis_wv_benefits`.

Identifiers and metadata are defined so that ChromaDB vector search results can be rejoined deterministically to GBIM and GeoDB in PostgreSQL. Belief embeddings carry an `id` field that maps to `gbimbeliefnormalized.id`, and metadata include `source_table` and `source_pk` fields that can be aligned with source tables and geometries.

---

### 6.6 Parcel Classification and the Limits of Geographic Resolution

A critical finding from the March 19, 2026 operational build is that WV tax parcel IDs are **fiscal accounting instruments first and geographic identifiers second**. Direct analysis of the `building_parcel_county_tax` view revealed parcel IDs with extreme building multiplicity — the top offender carrying 985 buildings on a single parcel record, with the top 20 parcels each carrying between 266 and 985 buildings.

This is not a data error. It reflects well-documented characteristics of WV assessor data:

- **Rights-of-way and linear features.** Pipeline companies, power utilities, railroads, and highway departments typically hold one parcel ID per county for their entire corridor. Every building spatially assigned to that corridor shares the parcel ID.
- **Government and exempt properties.** State-owned land, federal land, and municipal property often carry a single parcel ID for entire tracts. The Tucker County federal land parcel (parcel 161, `cleanparcelid = 47NO0IDO0ID`) covers 264 km² — approximately 25% of Tucker County's total area — and contains 782 structures including ranger stations, shelters, fire towers, and campground buildings consistent with Monongahela National Forest holdings.
- **Coal company surface rights.** Large corporate land holdings in the southern coalfield counties carry one parcel ID for entire tracts. The Mingo County parcel 1066780 covers 81 km² and contains 501 structures consistent with a coal company surface rights holding — company houses, preparation plants, tipples, mine portals, and infrastructure scattered across a hollow system under one corporate ownership record.
- **Water and utility district parcels.** Placeholder IDs for water and sewer infrastructure that spans multiple physical locations, identifiable in the data by `cleanparcelid` patterns such as `WATERATER`.
- **Unmatched building fallback.** Buildings that fall outside any parcel polygon — along county lines, in hollow communities where parcel data is sparse, or for structures built after the last parcel update — are assigned a default catch-all parcel for that county or district.
- **Dense multi-unit residential developments.** The Berkeley County parcel 1146728 (0.56 km², 592 buildings, all from `wvgistc_building_footprints`, distinct coordinates spread across the parcel area) represents a legitimate dense residential development — most likely a large mobile home park or apartment complex — where all units share one ownership parcel ID. Each building is a real, distinct, addressable structure requiring individual program routing through nearest 911 address point resolution rather than parcel situs address extraction.

**This matters critically for P16 — Power accountable to place.** If these catch-all parcels are allowed to propagate unclassified into address extraction and program routing, the system will assign hundreds of different households the same situs address and route them to the same program record. That is not a minor data quality issue — it is a failure mode that actively harms people navigating benefits systems.

**Parcel Classification Implementation**

The `parcel_type` column was added to `wv_parcels` on March 19, 2026:

```sql
ALTER TABLE wv_parcels
  ADD COLUMN IF NOT EXISTS parcel_type text DEFAULT 'standard';

UPDATE wv_parcels SET parcel_type = 'federal_land'
  WHERE parcel_id = 161;

UPDATE wv_parcels SET parcel_type = 'large_private'
  WHERE parcel_id IN (1066780, 1165188);

UPDATE wv_parcels SET parcel_type = 'unmatched'
  WHERE parcel_id = 1389823;

UPDATE wv_parcels SET parcel_type = 'multi_unit'
  WHERE parcel_id = 1146728;

UPDATE wv_parcels SET parcel_type = 'unmatched'
WHERE parcel_type = 'standard'
  AND (
    cleanparcelid ILIKE '%WATER%'
    OR cleanparcelid ILIKE '%0ID0ID%'
    OR cleanparcelid ILIKE '%NOID%'
    OR cleanparcelid ~ '^[0-9]{1,4}$'
  );
```

The resulting classification distribution across 1,389,855 total parcels:

| `parcel_type` | Count | Addressable Strategy |
|---|---|---|
| `standard` | 1,389,785 | Parcel situs address extraction |
| `unmatched` | 66 | Skip — no valid address possible |
| `large_private` | 2 | Centroid routing only |
| `federal_land` | 1 | Federal address system |
| `multi_unit` | 1 | Nearest 911 address point per building |

The addressable building universe on `standard` parcels is **2,010,808 buildings** — an upper bound that will be refined downward as spatial deduplication proceeds. The 4,855 buildings on non-standard parcels are protected from bad address assignment.

---

### 6.7 Linking GeoDB to GBIM, `local_resources`, and Hilbert Space

Within the GBIM framework, spatial information constitutes one dimension of a multi-axis geometric belief state that also includes semantic, temporal, institutional, and programmatic components.

- **From GeoDB and CSVs into GBIM.**
  Each feature represented in CSV-derived tables (for example, `gbim_source_csv.*`) and in geospatial source tables is associated with GBIM beliefs via identity keys in PostgreSQL. Enrichment scripts use `COALESCE` over `source_table` and `source_pk` variants to join `gbimbeliefnormalized` to these attributes, updating the `what` and `where` axes to incorporate fields such as latitudes, longitudes, labels, and selected family-specific attributes.

- **From GBIM beliefs to Hilbert space via embeddings.**
  The embedding pipeline generates text representations for each belief, combining the nine axes into a summary sentence and embedding them into ChromaDB. This realizes a large finite subset of the spatial and institutional component of the overall Hilbert space, allowing semantic traversal over beliefs that remain grounded in concrete geospatial and institutional facts.

- **From spatial facilities to programme records.**
  Benefits-relevant facilities are represented as GBIM beliefs linked to geometries in PostgreSQL and as entries in the `local_resources` registry. The full spatial chain now in production — building → parcel → county → tax district — connects households to both physical sites and programme descriptions, subject to the parcel classification constraints described in Section 6.6.

As a result, a belief that refers to a place is linked via a coherent four-step chain:

1. From embeddings and metadata in ChromaDB (in `gbim_beliefs_v2` and `gis_wv_benefits`),
2. To JSONB axes and identity keys in `gbimbeliefnormalized` in PostgreSQL,
3. To source attributes and geometries in PostgreSQL PostGIS and CSV-derived tables,
4. To `local_resources` rows describing programmes and services tied to that place — for standard parcels only; catch-all and utility parcels route through a separate spatial resolution path.

This linkage allows the Steward System to traverse:

- **Semantic proximity**, retrieving entities and texts that share conceptual similarity via ChromaDB.
- **Spatial proximity**, identifying features that are geographically close or spatially related via PostgreSQL PostGIS queries.
- **Belief-space relationships**, reasoning over institutional and normative structures encoded in GBIM.
- **Program proximity**, resolving beliefs and facilities to concrete programme records with coverage, contact, and verification information.
- **Resolution confidence**, flagging when a building cannot be resolved to a unique situs address and surfacing that uncertainty explicitly in RAG responses rather than silently substituting a fallback.

---

### 6.8 Geo-Aware RAG, Benefits Flows, and Multi-Model Use

The PostgreSQL GeoDB layer and its GBIM/ChromaDB vector mirrors play a direct role in retrieval-augmented generation, particularly for spatially explicit and benefits-oriented queries. The resolution level at which this pipeline operates — parcel and tax district granularity — is the resolution level at which WV program eligibility actually operates. A query as simple as "I need help" contains a location; that location contains a history of hazards, land ownership patterns, infrastructure gaps, and program eligibilities that the person asking may not know exist. The geo-aware pipeline exists to surface that knowledge without requiring the user to already know what to ask for.

```
┌─────────────────────────────────────────────────────────────┐
│   Geo-Aware Benefits RAG Pipeline                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. User Query: "I need help with my electric bill"         │
│              ↓                                               │
│  2. Location Resolution                                     │
│     building_id → parcel_id → county → tax_district        │
│     parcel_type = 'standard' → full address resolution      │
│              ↓                                               │
│  3. PostgreSQL Spatial Filter                               │
│     SELECT * FROM gbimbeliefnormalized                       │
│     WHERE (where_axis->>'county') = 'Mingo'                 │
│     AND (what_axis->>'type') LIKE '%utility%'               │
│              ↓                                               │
│  4. ChromaDB Vector Search                                  │
│     collection: gis_wv_benefits                             │
│     filter: {county: "Mingo", type: "utility_assistance"}   │
│     → Returns relevant facilities and programs              │
│              ↓                                               │
│  5. Spatial Hazard Check                                    │
│     ST_DWithin(building.geom, aml_sites.geom, 500)         │
│     ST_Intersects(building.geom, floodplains.geom)          │
│     → Surfaces related hazards and connected programs       │
│              ↓                                               │
│  6. Join to local_resources                                 │
│     WHERE county = 'Mingo'                                  │
│     AND program_type IN ('utility_assistance', 'aml',       │
│       'weatherization')                                     │
│     AND verification_status = 'verified'                    │
│     AND parcel_type = 'standard'                            │
│              ↓                                               │
│  7. Assemble Context with Resolution Confidence             │
│     - GBIM beliefs (spatial + institutional)                │
│     - Verified program records from local_resources         │
│     - Hazard proximity flags                                │
│     - parcel_type confidence signal                         │
│              ↓                                               │
│  8. LLM Ensemble Response                                   │
│     "Here is your LIEAP contact. Your address is also       │
│      within 400m of a mapped AML subsidence area —          │
│      here is who to contact about that separately,          │
│      and it will not affect your LIEAP eligibility."        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6.4. Geo-aware retrieval-augmented generation pipeline updated to include parcel classification filtering, hazard proximity checking, and resolution confidence surfacing. The pipeline operates at parcel and tax district granularity — the resolution level at which WV program eligibility actually operates.

For spatial and benefits questions, the system can:

- Apply PostgreSQL PostGIS filters to constrain candidate features by county, tax district, or spatial relationship to hazard layers.
- Query GBIM belief collections in ChromaDB to retrieve semantically and spatially relevant beliefs.
- Query `gis_wv_benefits` in ChromaDB to retrieve benefits facilities relevant to a specified county, ZIP, or named place.
- Check spatial proximity to hazard layers (AML sites, floodplains, dam inundation zones) and surface connected programs the user did not know to ask about.
- Incorporate local resource entries filtered by programme type, verification status, and parcel classification.
- Surface resolution confidence explicitly so that models distinguish between a household address resolved to a specific standard parcel versus one resolved only to a county or tax district.

Different models within the ensemble specialize in tasks such as:

- Public-facing narrative explanations that reference specific places, facilities, and programmes.
- Technical analyses of risk that combine hazards, infrastructure, demographics, and benefit access.
- Code generation for spatial queries in SQL or GIS scripting languages.
- Governance-focused advice concerning service coverage, jurisdictional responsibilities, and distributional impacts.

---

### 6.9 Roadmap for Full Statewide Integration

**Immediate priorities (post March 19, 2026):**

- **Spatial deduplication and `canonical_building_id`.** Implement the spatial clustering deduplication strategy described in Section 6.4.1. Add `canonical_building_id` to `wv_buildings`. Route all address extraction, program routing, and GBIM belief generation through canonical records rather than raw `building_id` values.

- **WV 911 address point ingestion.** The WV Enhanced 911 Council statewide address point dataset (`WV_Addresses`) is not currently present in `msjarvisgis`. This dataset is the authoritative source for situs addresses at the parcel and unit level and is required for `multi_unit` parcel resolution and hollow community address assignment. Download from the WV GIS Technical Center and ingest as `wv_e911_addresses`, then expose to `local_resources` via `postgres_fdw`.

- **Address extraction for standard parcels.** Once 911 address points are available and deduplication is complete, extract situs address fields joined by `parcel_id` for all `standard` parcels. Propagate `situs_street`, `situs_city`, `situs_state`, `situs_zip` through `parcel_with_county_tax` and `building_parcel_county_tax`.

- **Materialize `building_parcel_county_tax`.** The current view recomputes the full spatial join chain on every query, producing 2–3 minute query times for operations that should take seconds. Materializing this view with indexes on `building_id`, `parcel_id`, and `county_name` is a prerequisite for production-grade query performance.

**Medium-term priorities:**

- **Completing schema normalization.**
  Resolving remaining geometry, SRID, and numeric precision issues in legacy WV GIS Technical Center and federal/state layers, adopting the common SRID 26917 convention wherever feasible.

- **Layer ingestion priority sequence.**
  The 500+ layers in `msjarvisgis` are ingested into `local_resources` following a priority order based on program routing value: (1) FEMA floodplains, (2) Census blocks 2020, (3) abandoned mine lands, (4) ZIP Code Tabulation Areas, (5) WV broadband coverage, (6) community action agency service areas. Each layer follows the established pattern: load raw table → classify anomalies → build view → validate → materialize.

- **Syncing `local_resources` spatial chain into GBIM.**
  The building → parcel → county → tax district chain in `local_resources` is not yet reflected in `gbim_beliefs_v2` embeddings or `gis_wv_benefits` metadata. The `tax_geodb_id`, `parcel_type`, and `county_geodb_id` fields are not yet available as ChromaDB metadata filters, which means spatial filtering by tax district is not yet possible in live RAG flows. Syncing these fields into ChromaDB metadata is the next major integration milestone after address extraction.

- **Maintaining coverage in GBIM and embeddings.**
  Ensuring that beliefs associated with newly normalized datasets receive complete axis values, text representations, and embeddings in `gbim_beliefs_v2`, and that their spatial and institutional metadata are exposed for RAG.

- **Maintaining inventories and audit trails.**
  Periodically regenerating and archiving inventories of PostgreSQL PostGIS tables, GBIM beliefs, ChromaDB collections, and `local_resources` entries, including counts and metadata coverage, to ensure that the spatial body of Ms. Jarvis remains transparent and auditable.

As these milestones are met, Ms. Jarvis will be able to reason over an increasingly comprehensive set of statewide layers at the scale of millions of entities — with each advisory behaviour traceable to specific, inspectable geographies, GBIM beliefs, and programme records in `local_resources` — and with explicit acknowledgment of the limits of that resolution where the underlying parcel data does not support it. The spatial body of the Steward System is not a backdrop for reasoning. It is the ethical substrate through which justice-oriented intelligence becomes possible in Appalachia.
