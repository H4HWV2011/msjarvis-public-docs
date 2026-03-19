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

> Figure 6.1. High-level container-style view of the Ms. Jarvis Steward System, showing user clients, the 21-LLM ensemble, and the containerized backing stores (PostgreSQL PostGIS GeoDB, GBIM, ChromaDB vector store, `local_resources`, Redis, Neo4j).

Within the Quantarithmia program, GeoDB constitutes the spatial backbone of Ms. Jarvis's "body": a coherent, queryable mesh of features and boundaries for reasoning about risk, access, infrastructure, and spatial justice. In the current deployment, this spatial backbone runs as part of a containerized microservice stack orchestrated with Docker Compose, alongside core services such as ChromaDB, Redis, Neo4j, the `local_resources` Postgres instance, and the multi-model ensemble.

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

As of March 19, 2026, the `local_resources` database has been advanced from a flat ZIP/county registry into a spatially resolved infrastructure database. The full spatial chain — building → parcel → county → tax district — is now live and queryable, backed by the following objects:

| Object | Type | Status | Notes |
|---|---|---|---|
| `wv_tax_districts_poly` | Table | Live | 600 features, SRID 26917 + 4326, GiST indexed |
| `parcel_with_county_tax` | View | Live | ST_Within join: parcels → county + tax district |
| `building_parcel_county_tax` | View | Live | Full building → parcel → county → tax chain |
| `county_tax_building_summary` | Materialized View | Live | 707 rows, sub-millisecond reads, concurrent refresh enabled |

---

### 6.3 PostGIS as Ms. Jarvis's Spatial Backbone

At the storage level, Ms. Jarvis uses a PostgreSQL 16 PostGIS database (`msjarvisgis`) as the main container for West Virginia vector datasets. This PostGIS instance runs on the host system at /var/lib/postgresql/16/msjarvis and is accessed by multiple services for spatial reasoning and data access.

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

The core production schema includes:

- Raw and normalized source tables for individual datasets such as county boundaries, census blocks, dams, hospitals, and other facilities.
- CSV-derived tables (for example, `gbim_source_csv.*`) created from `*_attrs.csv` exports, storing key attributes including `geodb_id`, `lat`, `lon`, `bbox`, `label`, `sourcetable`, and `county`.
- GBIM-related tables (34 total), including:
  - `gbimbeliefnormalized` (5,416,522 rows, 21 GB) — the main belief table with nine JSONB axes
  - `gbim_worldview_entity` (5,416,521 rows, 47 GB) — entity relationships and worldview
  - `gbim_beliefs` (5,289,747 rows, 3 GB) — core beliefs with structured columns
  - `gbim_evidence` (2,121,230 rows, 680 MB) — supporting evidence
  - `gbim_belief_evidence` (2,121,230 rows, 232 MB) — belief-evidence linkages

Most production layers share SRID 26917 (UTM Zone 17N NAD83). Legacy tables retaining provisional SRIDs, mixed geometry types, or inconsistent precision are explicitly flagged for cleanup and excluded from the primary GBIM worldview until normalized.

---

### 6.4 Currently Integrated Statewide Layers

The current deployment includes a substantial, production-grade subset of West Virginia's public geospatial data. At a high level, the Steward System maintains:

- **Census units.**
  Statewide 2020 Census blocks and block groups in projected coordinate systems, providing population and administrative meshes at fine spatial scales.

- **Structures and buildings.**
  A dense statewide structure inventory composed of SAMB structure points, WV GIS Technical Center building footprints numbering in the millions, and Microsoft-derived building points. The multi-source nature of this inventory introduces duplication that must be managed explicitly before address extraction or program routing proceeds. See Section 6.4.1.

- **Hazard and infrastructure layers.**
  Abandoned mine lands (lines and polygons), dams (coal-related and non-coal-related), floodplain structure inventories and flood hazard zones, rail networks and terminals, navigable waterways and river-mile indexing, and energy and communication infrastructure where available.

- **Civic, facility, and benefits coverage.**
  Hospitals, nursing homes, fire and police stations, 911 centers, higher-education institutions, libraries, community centers, parks, solid waste facilities, sewer plants, and benefits-relevant facilities such as state and local offices, community action agencies, and local hubs — represented both as GeoDB features and as GBIM beliefs mirrored into collections such as `gis_wv_benefits`.

- **Governance and index layers.**
  County and state boundaries, ZIP Code Tabulation Areas, regional planning districts, tax district polygons (`wv_tax_districts_poly`, 600 features, verified March 19, 2026), named places, summits, National Register points and polygons, and related historic resources.

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

> Figure 6.2. Conceptual overview of the statewide geospatial mesh maintained in PostgreSQL GeoDB and GBIM.

---

### 6.4.1 The Multi-Source Building Inventory and Deduplication

The statewide structure inventory in `wv_buildings` is assembled from three independent sources:

- **SAMB** (Statewide Address and Mapping Base) — structure points compiled from county assessor records
- **WV GIS Technical Center building footprints** — polygon footprints derived from aerial imagery, converted to centroids, with `sourcetable = wvgistc_building_footprints`
- **Microsoft building points** — machine-learning-derived structure detections from satellite imagery

This multi-source assembly is a strength — each dataset fills gaps the others leave, producing the most complete statewide structure inventory available for West Virginia. But it introduces a well-defined problem: the same physical structure frequently appears as multiple rows in `wv_buildings` with different `building_id` values, different `sourcetable` values, and nearly identical but not identical coordinates. This is not a data error. It is the honest consequence of combining three independently produced datasets that were never designed to reference each other.

**What Was Discovered Operationally**

During the March 19, 2026 spatial chain build, this duplication became operationally visible in two ways. First, raw building counts from joins against `wv_buildings` overstate the true number of distinct structures — the `county_tax_building_summary` materialized view reports source records, not necessarily distinct physical locations. Second, the `building_parcel_county_tax` view revealed extreme building-per-parcel counts in the top offenders, with parcels carrying 266 to 985 buildings. While most of these were explained by legitimate large-tract land ownership, the multi-source duplication problem means that even on `standard` parcels, some building IDs represent the same physical structure counted two or three times.

The `wv_buildings` schema is lean by design:

| Column | Notes |
|---|---|
| `building_id` | text identifier |
| `label` | human-readable name or description |
| `btype` | building type classification |
| `sourcetable` | which source dataset the record came from |
| `country` | country-level provenance tag from multi-source ingestion |
| `geom` | PostGIS geometry (USER-DEFINED type) |

As of March 19, 2026, GiST and btree indexes have been added to `wv_buildings`:

```sql
CREATE INDEX wv_buildings_geom_idx
  ON wv_buildings USING GIST (geom);

CREATE INDEX wv_buildings_building_id_idx
  ON wv_buildings (building_id);
```

**The Deduplication Strategy**

Spatial deduplication identifies buildings within a threshold distance (5–15 meters, to be calibrated per source pair) and from different source tables, assigning them a single canonical `building_id` for address and program routing. The diagnostic query pattern is:

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
  AND a.sourcetable != b.sourcetable
  AND ST_DWithin(a.geom::geography, b.geom::geography, 10)
LIMIT 100;
```

Until full deduplication is complete, all building counts in `county_tax_building_summary` and downstream reporting carry an explicit caveat: they represent source records, not verified distinct structures. This uncertainty is surfaced explicitly in RAG responses when building-level counts are cited, consistent with Ms. Jarvis's P16 commitment that power must be accountable to place.

The architectural solution is a `canonical_building_id` field, to be added to `wv_buildings` after deduplication, that collapses duplicates to a single authoritative record per physical structure. All program routing, address extraction, and GBIM belief generation will operate on `canonical_building_id` rather than raw `building_id` once that field is populated. This is a near-term roadmap item and a prerequisite for address extraction.

**A Note on View Architecture and Query Performance**

The spatial chain in `local_resources` was built deliberately as views before materialization — a design decision that proved its value during the March 19, 2026 build sprint. Views are transparent and inspectable; every schema correction, parcel classification discovery, and anomaly was surfaced because the join logic remained queryable during development. Materialized views sacrifice that transparency for performance and should only be created after the logic is proven and anomalies are handled.

A critical operational lesson from this sprint: correlated subqueries against `building_parcel_county_tax` — which recomputes the full `ST_Within` join chain on every evaluation — must never be run at scale until the view is materialized. A query with a correlated subquery against this view across 2M+ buildings ran for 37 minutes before cancellation. Materializing `building_parcel_county_tax` with indexes on `building_id`, `parcel_id`, and `county_name` is listed as an immediate roadmap priority in Section 6.9.

---

### 6.5 Spatial Embeddings and Geo-Referenced Beliefs

To connect geometric features with high-dimensional semantic reasoning, Ms. Jarvis maintains collections derived from GBIM beliefs and spatial entities in the shared ChromaDB vector store, configured with 384-dimensional embeddings.

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

> Figure 6.3. Key relationships between PostgreSQL GeoDB source tables, GBIM beliefs, and spatial/benefits collections in ChromaDB. Deterministic joins are maintained via identity fields from embeddings back into GBIM and GeoDB.

- **Unified GBIM belief collections.** The primary collection is `gbim_beliefs_v2`, which holds embeddings for millions of beliefs derived from the nine JSONB axes, stored with metadata including belief identifier, `source_table`, `source_pk`, epoch information, and optional spatial metadata inherited from `where`.

- **Benefits-focused spatial collection.** The `gis_wv_benefits` collection stores embeddings and metadata for benefits-relevant facilities, enabling semantically and spatially aware retrieval of benefits sites with linkages to `local_resources` identifiers.

- **Legacy and thematic `geodb*` collections.** Earlier deployments mirrored selected PostGIS layers into `geodb*` collections. These remain available as historical or specialized indexes but are no longer treated as the primary spatial memory layer.

---

### 6.6 Parcel Classification and the Limits of Geographic Resolution

A critical finding from the March 19, 2026 operational build is that WV tax parcel IDs are **fiscal accounting instruments first and geographic identifiers second**. Direct analysis of the `building_parcel_county_tax` view revealed parcel IDs with extreme building multiplicity — the top offender carrying 985 buildings on a single parcel record.

This reflects well-documented characteristics of WV assessor data:

- **Rights-of-way and linear features.** Pipeline companies, power utilities, railroads, and highway departments typically hold one parcel ID per county for their entire corridor.
- **Government and exempt properties.** The Tucker County federal land parcel (parcel 161, 264 km², approximately 25% of Tucker County's total area) contains 782 structures consistent with Monongahela National Forest holdings — ranger stations, shelters, fire towers, and campground buildings.
- **Coal company surface rights.** The Mingo County parcel 1066780 covers 81 km² and contains 501 structures consistent with a coal company surface rights holding — company houses, preparation plants, tipples, mine portals, and infrastructure scattered across a hollow system under one corporate ownership record.
- **Water and utility district parcels.** Placeholder IDs for water and sewer infrastructure spanning multiple physical locations, identifiable by `cleanparcelid` patterns such as `WATERATER`.
- **Unmatched building fallback.** Buildings that fall outside any parcel polygon are assigned a default catch-all parcel for that county or district.
- **Dense multi-unit residential developments.** The Berkeley County parcel 1146728 (0.56 km², 592 buildings, all from `wvgistc_building_footprints`, distinct coordinates spread across the parcel area) represents a legitimate dense residential development — most likely a large mobile home park or apartment complex — where all units share one ownership parcel ID. Each building is a real, distinct, addressable structure requiring individual program routing through nearest 911 address point resolution rather than parcel situs address extraction.

If these parcels propagate unclassified into address extraction and program routing, the system assigns hundreds of different households the same situs address and routes them to the same program record. That is not a minor data quality issue — it is a failure mode that actively harms people navigating benefits systems.

**Parcel Classification Implementation**

The `parcel_type` column was added to `wv_parcels` on March 19, 2026, with the following classification logic applied:

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

CREATE INDEX wv_parcels_parcel_type_idx
  ON wv_parcels (parcel_type);
```

The resulting classification distribution:

| `parcel_type` | Count | Address Strategy |
|---|---|---|
| `standard` | 1,389,785 | Parcel situs address extraction |
| `unmatched` | 66 | Skip — no valid address possible |
| `large_private` | 2 | Centroid routing only |
| `federal_land` | 1 | Federal address system |
| `multi_unit` | 1 | Nearest 911 address point per building |

The addressable building universe on `standard` parcels is **2,010,808 buildings** — an upper bound refined downward as spatial deduplication proceeds. The 4,855 buildings on non-standard parcels are protected from bad address assignment.

---

### 6.6.1 Property Owner Names: Ingestion Scope and Ethical Constraint

West Virginia tax assessor records include property owner names as legally public data, accessible through county assessor websites and courthouse records. During the March 19, 2026 parcel classification sprint, the question of whether owner names should be ingested into the RAG-accessible layer of `local_resources` or `msjarvisgis` was explicitly addressed and resolved.

The decision is as follows:

**Institutional and corporate owner names** — coal companies, utilities, government agencies, LLCs, and other non-individual entities — are retained as intermediate classification signals for `parcel_type` assignment. Knowing that a parcel is owned by a corporate entity informs the `large_private` or `federal_land` classification and supports the accountability function of the spatial layer. These names may be retained in classification-support tables.

**Individual residential owner names** are not ingested into any RAG-accessible table, view, materialized view, or ChromaDB collection. They are used only as intermediate signals where necessary for classification and are not persisted after classification is applied.

The rationale is the aggregation problem. Individual owner names are legally public in the same sense that courthouse deed records are public — they are friction-protected, one record at a time, requiring deliberate search. Embedding those names into a semantically searchable AI system that reasons across 1.4 million parcels, hazard layers, program eligibility, and building locations would transform friction-protected public records into operational surveillance infrastructure. That transformation is not justified by Ms. Jarvis's stated purpose of routing households to assistance.

The distinction is between accountability for institutions with power over place and protection for individuals whose lives are shaped by place. Ms. Jarvis is designed to serve the latter, not to expose them.

This constraint is enforced at two independent layers: at the schema level through the ingestion decisions documented here, and at the constitutional layer through query refusal logic documented in Chapter [X]. Neither layer alone is sufficient. Schema-level protection prevents inadvertent ingestion; constitutional-layer protection prevents behavioral bypass even if data were present. Together they constitute a defense-in-depth architecture for one of the most sensitive data categories in the system.

---

### 6.7 Linking GeoDB to GBIM, `local_resources`, and Hilbert Space

Within the GBIM framework, spatial information constitutes one dimension of a multi-axis geometric belief state that also includes semantic, temporal, institutional, and programmatic components.

- **From GeoDB and CSVs into GBIM.** Each feature in CSV-derived tables and geospatial source tables is associated with GBIM beliefs via identity keys in PostgreSQL. Enrichment scripts use `COALESCE` over `source_table` and `source_pk` variants to join `gbimbeliefnormalized` to these attributes, updating the `what` and `where` axes to incorporate latitudes, longitudes, labels, and selected family-specific attributes.

- **From GBIM beliefs to Hilbert space via embeddings.** The embedding pipeline generates text representations for each belief, combining the nine axes into a summary sentence and embedding them into ChromaDB. This realizes a large finite subset of the spatial and institutional component of the overall Hilbert space, allowing semantic traversal over beliefs grounded in concrete geospatial and institutional facts.

- **From spatial facilities to programme records.** Benefits-relevant facilities are represented as GBIM beliefs linked to geometries in PostgreSQL and as entries in the `local_resources` registry. The full spatial chain now in production — building → parcel → county → tax district — connects households to both physical sites and programme descriptions, subject to the parcel classification constraints described in Section 6.6.

A belief that refers to a place is linked via a coherent four-step chain:

1. From embeddings and metadata in ChromaDB (in `gbim_beliefs_v2` and `gis_wv_benefits`),
2. To JSONB axes and identity keys in `gbimbeliefnormalized` in PostgreSQL,
3. To source attributes and geometries in PostgreSQL PostGIS and CSV-derived tables,
4. To `local_resources` rows describing programmes and services tied to that place — for standard parcels only; catch-all and utility parcels route through a separate spatial resolution path.

This linkage allows the Steward System to traverse semantic proximity, spatial proximity, belief-space relationships, program proximity, and resolution confidence — flagging when a building cannot be resolved to a unique situs address and surfacing that uncertainty explicitly in RAG responses rather than silently substituting a fallback.

---

### 6.8 Geo-Aware RAG, Benefits Flows, and Multi-Model Use

The PostgreSQL GeoDB layer and its GBIM/ChromaDB vector mirrors play a direct role in retrieval-augmented generation, particularly for spatially explicit and benefits-oriented queries. The resolution level at which this pipeline operates — parcel and tax district granularity — is the resolution level at which WV program eligibility actually operates.

A query as simple as "I need help" contains a location. That location contains a history of hazards, land ownership patterns, infrastructure gaps, and program eligibilities that the person asking may not know exist. The geo-aware pipeline exists to surface that knowledge without requiring the user to already know what to ask for. A household asking about a utility shutoff may be living 400 meters from a mapped AML subsidence site that explains why their heating costs are so high, near a weatherization program that addresses the same problem, and within the service area of a community action agency that handles both. A system that answers only the question asked gives them one program. Ms. Jarvis, reasoning over the full spatial layer stack, surfaces the connected picture.

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
│      here is who to contact, and it will not affect         │
│      your LIEAP eligibility."                               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> Figure 6.4. Geo-aware retrieval-augmented generation pipeline operating at parcel and tax district granularity — the resolution level at which WV program eligibility actually operates. Standard parcels route to verified program records; non-standard parcels surface explicit resolution uncertainty.

For spatial and benefits questions, the system can apply PostGIS filters to constrain candidate features by county, tax district, or spatial relationship to hazard layers; query `gbim_beliefs_v2` and `gis_wv_benefits` in ChromaDB for semantically relevant beliefs and facilities; check spatial proximity to hazard layers and surface connected programs the user did not know to ask about; and incorporate `local_resources` entries filtered by programme type, verification status, and parcel classification.

The remaining gap before full RAG integration at parcel granularity is the sync of `local_resources` spatial chain metadata — `tax_geodb_id`, `parcel_type`, and `county_geodb_id` — into ChromaDB as queryable metadata filters. Until that sync runs, spatial filtering by tax district is not yet possible in live RAG flows. Once complete, the pipeline moves from county-level granularity to parcel and tax district granularity for all household-level queries.

---

### 6.9 Roadmap for Full Statewide Integration

**Immediate priorities (post March 19, 2026):**

- **Materialize `building_parcel_county_tax`.** The current view recomputes the full spatial join chain on every query, producing 2–3 minute query times for operations that should take seconds. A correlated subquery against this view across 2M+ buildings ran for 37 minutes before cancellation during the March 19 sprint. Materializing this view with indexes on `building_id`, `parcel_id`, and `county_name` is a prerequisite for all subsequent spatial operations at scale.

```sql
CREATE MATERIALIZED VIEW building_parcel_county_tax_mv AS
SELECT * FROM building_parcel_county_tax;

CREATE INDEX bpct_mv_building_id_idx
  ON building_parcel_county_tax_mv (building_id);

CREATE INDEX bpct_mv_parcel_id_idx
  ON building_parvis_county_tax_mv (parcel_id);

CREATE INDEX bpct_mv_county_idx
  ON building_parcel_county_tax_mv (county_name);
```

- **Spatial deduplication and `canonical_building_id`.** Implement spatial clustering deduplication across `wv_buildings` source pairs. Add `canonical_building_id` to `wv_buildings`. Route all address extraction, program routing, and GBIM belief generation through canonical records.

- **WV 911 address point ingestion.** The WV Enhanced 911 Council statewide address point dataset (`WV_Addresses`) is not currently present in `msjarvisgis`. This dataset is required for `multi_unit` parcel resolution and hollow community address assignment. Download from the WV GIS Technical Center and ingest as `wv_e911_addresses`, then expose to `local_resources` via `postgres_fdw`.

- **Address extraction for standard parcels.** Once 911 address points are available and deduplication is complete, extract situs address fields for all `standard` parcels and propagate through `parcel_with_county_tax` and `building_parcel_county_tax`.

- **Sync `local_resources` spatial chain into ChromaDB.** Add `tax_geodb_id`, `parcel_type`, and `county_geodb_id` as queryable metadata filters in `gbim_beliefs_v2` and `gis_wv_benefits` to enable tax district granularity in live RAG flows.

**Medium-term priorities:**

- **Layer ingestion priority sequence.** The 500+ layers in `msjarvisgis` are ingested into `local_resources` following a priority order based on program routing value: (1) FEMA floodplains, (2) Census blocks 2020, (3) abandoned mine lands, (4) ZIP Code Tabulation Areas, (5) WV broadband coverage, (6) community action agency service areas. Each layer follows the established pattern: load raw table → classify anomalies → build view → validate → materialize.

- **Completing schema normalization.** Resolving remaining geometry, SRID, and numeric precision issues in legacy layers, adopting SRID 26917 wherever feasible.

- **Maintaining inventories and audit trails.** Periodically regenerating and archiving inventories of PostgreSQL PostGIS tables, GBIM beliefs, ChromaDB collections, and `local_resources` entries, including counts and metadata coverage, to ensure the spatial body of Ms. Jarvis remains transparent and auditable.

As these milestones are met, Ms. Jarvis will be able to reason over an increasingly comprehensive set of statewide layers at the scale of millions of entities — with each advisory behaviour traceable to specific, inspectable geographies, GBIM beliefs, and programme records in `local_resources` — and with explicit acknowledgment of the limits of that resolution where the underlying parcel data does not support it. The spatial body of the Steward System is not a backdrop for reasoning. It is the ethical substrate through which justice-oriented intelligence becomes possible in Appalachia.
