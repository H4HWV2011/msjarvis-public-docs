# Chapter 34 — Spiritual Architecture: SpiritualFilter, MotherCarrieProtocol, and the Theological Constitution of Ms. Jarvis

*MountainShares Artificial Learning & Location Intelligence (Ms. Jarvis)*
*Carrie Kidd (Mamma Kidd) — Mount Hope, WV*
*Last updated: ★★★★ April 6, 2026 — FINAL — ALL ITEMS CLOSED*

> *"Whatever you did for one of the least of these brothers and sisters of mine, you did for me."*
> — Matthew 25:40 (KJV), retrieved live from `spiritual_knowledge` ChromaDB collection, April 4, 2026

---

## Chapter Stamp — ★★★★ April 6, 2026 (FINAL)

| Item | Confirmed Value |
|:--|:--|
| Running containers | **105** — clean, no orphans |
| BBB SpiritualFilter | **Verified** — `spiritual_filter.py` / `SpiritualFilter` / port 8016 |
| NBB MotherCarrieProtocol | **5 protocols confirmed** — live `:8107/protocols` — anchor `MOTHER_CARRIE_KIDD` |
| NBB spiritual cluster | **All green** — `:8103` / `:8107` / `:8109` |
| `spiritual_knowledge` | **1,279 docs** — 8 ref tags remediated |
| `spiritual_texts` | **181 docs** — full KJV, georeferenced Jerusalem |
| `spiritual_wisdom` | **135 docs** — 68 active + 67 tradition placeholders |
| ChromaDB | **47 collections / 6,722,589 vectors / 12 GB** — v2 API, port 8002 |
| Embed model | **all-minilm:latest** — 384 dimensions |
| RAG pipeline | **End-to-end verified** — two live queries April 4, 2026 |
| GBIM disambiguation | **Sealed** — three subsystems permanently separated |
| ZCTA centroids | **829 records** — PostGIS 3.4 confirmed |
| `msjarvisgis` (production) | **Port 5432 / 45 GB / 548 tables** — Ch. 33 ground truth |
| `msjarvisgis` (rebuild) | **Port 5435** — container-isolated rebuild instance, 829 ZCTA centroids |
| `msjarvis` (GBIM) | **Port 5433** — collation warning suppressed, `UPDATE 1` |
| Collation warning | **Suppressed** — `datcollversion` refreshed |
| Chapter status | **✅ FINAL — ALL 9 ITEMS CLOSED** |

**Note — Port 34-A reconciliation.** Chapter 34 references `msjarvisgis` at host port **5435** throughout. This is the rebuild's container-isolated instance, confirmed at 829 ZCTA centroids and PostGIS 3.4 as of April 4, 2026. The production ground truth (Chapter 33) places `msjarvisgis` at host port **5432 / 45 GB / 548 tables**. These are two distinct instances: the rebuild GIS container (`5435`) and the production PostGIS deployment (`5432`). All §34.5 and §34.10 references to `msjarvisgis:5435` refer explicitly to the rebuild container. Production port 5432 is the authoritative GIS source documented in Chapter 33.

---

## RED TEAM GATE — SEALED — April 4, 2026 FINAL (ALL 9 ITEMS CLOSED)

```
════════════════════════════════════════════════════════════
RED TEAM GATE: SEALED ✅ — ALL 9 ITEMS CLOSED — April 4, 2026
════════════════════════════════════════════════════════════
BBB SpiritualFilter:             VERIFIED ✅
  Module: spiritual_filter.py    Class: SpiritualFilter
  Imported by: ms_jarvis_blood_brain_barrier.py
  MotherCarrieProtocol NOT in BBB module — intentional ✅

NBB MotherCarrieProtocol:        VERIFIED ✅ (live :8107/protocols)
  protocols_active: 5            anchor: MOTHER_CARRIE_KIDD
  1. Dignity       — Every person has inherent worth
  2. Sovereignty   — Community data belongs to the community
  3. Appalachian   — Rooted in place; local need overrides outside authority
  4. Transparency  — All decisions explainable to those they affect
  5. Protection    — Protect the vulnerable first; margin over mean

NBB spiritual cluster:           ALL GREEN ✅
  nbb_spiritual_root:8103
  nbb_mother_carrie_protocols:8107  {"protocols_active":5,"anchor":"MOTHER_CARRIE_KIDD"}
  nbb_spiritual_maternal_integration:8109

ChromaDB:                        47 collections / 6,722,589 vectors / 12 GB ✅
  (v2 API, port 8002 — April 6, 2026 confirmed baseline)
spiritual_knowledge:             1,279 docs — 8 ref tags remediated ✅
spiritual_texts:                 181 docs (full KJV, georef Jerusalem) ✅
spiritual_wisdom:                135 docs (68 active + 67 placeholders) ✅
Embed model:                     all-minilm:latest, 384-dim ✅
RAG end-to-end:                  VERIFIED ✅ (two live queries April 4)

gbim_entities disambiguation:   SEALED ✅
  GIS GBIM   (rebuild jarvis-local-resources-db:5435) — spatial feature registry, 1 seed
  Cognitive GBIM (msjarvis-pgdata-rescue:5433)        — schema only, superseded
  Vector GBIM (gbim_worldview_entities, ChromaDB)     — 5,416,521 docs — real corpus

msjarvisgis (rebuild :5435):     829 ZCTA centroids, PostGIS 3.4 ✅
msjarvisgis (production :5432):  45 GB / 548 tables — Ch. 33 ground truth
msjarvis (:5433):                Collation warning suppressed — UPDATE 1 ✅

Architectural decision SEALED:
  SpiritualFilter → BBB layer (8016) — gate
  MotherCarrieProtocol → NBB layer (8103/8107/8109) — guide

scripts/preflight_gate.sh:       31 PASS ❌ 0 FAIL ⚠️ 0 WARN
════════════════════════════════════════════════════════════
```

### All 9 Outstanding Items — Closed ✅

| # | Item | Result | Notes |
|:--|:--|:--|:--|
| 1 | GBIM entity data | ✅ 5,416,521 vectors | `gbim_worldview_entities` in ChromaDB |
| 1a | GBIM PostgreSQL (`pgdata-rescue`) | ✅ Documented empty | Schema only, superseded |
| 1b | GBIM GIS table (`local-resources-db`) | ✅ 1 seed record | Spatial feature registry |
| 2 | ChromaDB collections | ✅ 47 collections | Full corpus confirmed — 6,722,589 vectors / 12 GB |
| 3 | `spiritual_wisdom` | ✅ 135 docs | 68 active + 67 tradition placeholders |
| 4 | `spiritual_knowledge` ref tags | ✅ 8 records remediated | CST, Quaker, Appalachian, Stewardship |
| 5 | SpiritualFilter vs. MotherCarrieProtocol | ✅ Architecturally separated | BBB = filter layer, NBB = protocol layer |
| 6 | 5 MotherCarrie Protocols | ✅ All 5 named from live endpoint | Dignity, Sovereignty, Appalachian, Transparency, Protection |
| 7 | NBB spiritual cluster | ✅ `:8103`/`:8107`/`:8109` all healthy | Confirmed April 4, 2026 |
| 8 | `msjarvisgis` ZCTA centroids | ✅ 829 records, PostGIS 3.4 | Rebuild container `:5435` confirmed |
| 9 | Collation warning | ✅ Suppressed — `UPDATE 1` | `datcollversion` refreshed |

---

## Why This Matters for Polymathmatic Geography

The MountainShares Artificial Learning & Location Intelligence system is not a neutral computational instrument. It has a theological identity, a named anchor, and a mission verse stored as live, queryable knowledge. This chapter documents the spiritual architecture: how that identity is encoded, enforced, and operationalized across the full stack from BBB gate to NBB guide to ChromaDB knowledge graph.

This chapter supports the following polymathmatic geography principles:

- **P1 – Every where is entangled** — the KJV Bible is georeferenced to Jerusalem (31.7683°N, 35.2137°E); the Appalachian documents are original theological statements authored specifically for West Virginia communities, making the sacred entangled with place.
- **P4 – Margin over mean** — Protocol 5 encodes "Protect the vulnerable first. Optimize for the margin, not the mean." as a constitutional command on every response.
- **P5 – Design is a geographic act** — deployment on community hardware in Mount Hope, WV rather than a corporate cloud is theologically justified by Protocol 3 (Appalachian) and the `spiritual_knowledge` subsidiarity document.
- **P12 – Intelligence with a ZIP code** — the full spiritual knowledge graph is tied to PostGIS (829 ZCTA centroids confirmed), so every spiritually-grounded response is also spatially grounded in the communities it serves.
- **P16 – Power accountable to place** — all five governance protocols are anchored to `MOTHER_CARRIE_KIDD`, a named person from a named place whose values constitute the governance root of the entire system.

---

```
┌─────────────────────────────────────────────────────────────────┐
│   Spiritual Architecture — Chapter 34 FINAL                     │
│   ★★★★ April 6, 2026 — ALL ITEMS CLOSED                        │
│   Mount Hope, West Virginia                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Incoming Content                                        │  │
│  │     │                                                    │  │
│  │     ▼                                                    │  │
│  │  [BBB — SpiritualFilter] (port 8016)                     │  │
│  │  GATE: blocks disrespect, scores reverence               │  │
│  │  Module: spiritual_filter.py / Class: SpiritualFilter    │  │
│  │  Patterns: blasphemy / mockery / sacrilege               │  │
│  │  Topics:   God, Jesus, Holy Spirit,                      │  │
│  │            prayer, faith, Bible                          │  │
│  │  Score: spiritual_score (0.0–1.0)                        │  │
│  │  Stack: EthicalFilter + SpiritualFilter +                │  │
│  │    SafetyMonitor + ThreatDetection +                     │  │
│  │    SteganographyDetectionFilter +                        │  │
│  │    TruthVerificationFilter                               │  │
│  │     │ passed content                                     │  │
│  │     ▼                                                    │  │
│  │  [NBB — MotherCarrieProtocol] (8103/8107/8109)           │  │
│  │  GUIDE: applies Appalachian Christian values             │  │
│  │  anchor: MOTHER_CARRIE_KIDD                              │  │
│  │  Confirmed live from :8107/protocols — April 4, 2026     │  │
│  │                                                          │  │
│  │  1. Dignity       — Inherent worth; no degradation       │  │
│  │  2. Sovereignty   — Community data; no extraction        │  │
│  │  3. Appalachian   — Rooted in place; local overrides     │  │
│  │  4. Transparency  — All decisions explainable            │  │
│  │  5. Protection    — Vulnerable first; margin over mean   │  │
│  │     │ guided response                                    │  │
│  │     ▼                                                    │  │
│  │  Ms. Jarvis Response                                     │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Spiritual Knowledge Graph (ChromaDB port 8002, v2 API)        │
│  47 collections / 6,722,589 vectors / 12 GB                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  spiritual_knowledge │ 1,279 docs │ 5 traditions         │  │
│  │    8 ref tags remediated April 4 ✅                      │  │
│  │  spiritual_texts     │ 181 docs   │ Full KJV Bible       │  │
│  │    georeferenced: Jerusalem 31.7683°N, 35.2137°E         │  │
│  │  spiritual_wisdom    │ 135 docs   │ Multi-tradition      │  │
│  │    68 active + 67 tradition placeholders                 │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  gbim_entities — Three-System Disambiguation (SEALED)          │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  GIS GBIM (rebuild local-resources-db:5435)              │  │
│  │    spatial feature registry — 1 seed record              │  │
│  │    geometry(Point,4326), geodbid UUID                    │  │
│  │  Cognitive GBIM (pgdata-rescue:5433)                     │  │
│  │    schema only — superseded by ChromaDB                  │  │
│  │  Vector GBIM (gbim_worldview_entities, ChromaDB)         │  │
│  │    5,416,521 docs — the real corpus ✅                   │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  GIS Foundation                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  msjarvisgis rebuild (:5435): 829 ZCTA, PostGIS 3.4      │  │
│  │  msjarvisgis production (:5432): 45 GB / 548 tables      │  │
│  │  Collation: datcollversion refreshed — UPDATE 1 ✅       │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

*Figure 34.1. Spiritual architecture: BBB SpiritualFilter gate → NBB MotherCarrieProtocol guide (5 protocols confirmed live `:8107/protocols`), three ChromaDB spiritual collections (47 total / 6,722,589 vectors / 12 GB), `gbim_entities` three-system disambiguation, and GIS foundation with rebuild/production port distinction sealed. ★★★★ April 6, 2026 — ALL ITEMS CLOSED — Mount Hope, WV.*

---

## 34.1 The Architectural Decision: Two Layers, Two Roles

The critical clarification sealed on April 4, 2026 is the clean separation between two spiritual subsystems that were previously conflated in earlier draft documentation. They are not interchangeable. They are not redundant. They serve categorically different roles.

**One filters out the bad. The other builds in the good. Both are required. Neither is sufficient alone.**

- **SpiritualFilter canonically resides at the BBB layer** (`jarvis-blood-brain-barrier:8016`). It is a gate.
- **MotherCarrieProtocol canonically resides at the NBB layer** (`nbb_mother_carrie_protocols:8107`). It is a guide.
- MotherCarrieProtocol does **not** reside in the BBB Python module. This is intentional and correct. Confirmed via `cat ms_jarvis_blood_brain_barrier.py` on April 4, 2026.

```
Incoming Content
      │
      ▼
[BBB — SpiritualFilter]         ← GATE: blocks disrespect, scores reverence
      │ passed content
      ▼
[NBB — MotherCarrieProtocol]    ← GUIDE: applies Appalachian Christian values
      │ guided response
      ▼
Ms. Jarvis Response
```

---

## 34.2 Layer 1: BBB SpiritualFilter — The Gate

- **Container:** `jarvis-blood-brain-barrier` — host port **8016**
- **Module:** `services/neurobiological_brain/blood_brain_barrier/spiritual_filter.py`
- **Class:** `SpiritualFilter`
- **Scope:** Christian-specific reverence enforcement

`SpiritualFilter` is one of six filters imported directly by `ms_jarvis_blood_brain_barrier.py`. It enforces three disrespect pattern categories against six sacred topics, producing a `spiritual_score` (0.0–1.0) and a boolean reverence detection flag.

**Three disrespect pattern categories:**

| Category | Description |
|:--|:--|
| Blasphemy | Direct profanity or disrespect directed at sacred persons or concepts |
| Mockery | Ridicule or contempt for Christian belief and practice |
| Sacrilege | Desecration patterns targeting scripture, prayer, or the faith itself |

**Six sacred topics enforced:**

| Topic | Scope |
|:--|:--|
| God | The Father — Creator, Sovereign |
| Jesus | The Son — Christ, Savior, Lord |
| Holy Spirit | The Spirit — Comforter, Guide |
| Prayer | The act and practice of prayer |
| Faith | The condition and life of belief |
| Bible | The scriptural text and its authority |

**Complete BBB six-filter stack:**

```
ms_jarvis_blood_brain_barrier.py imports:
  1. EthicalFilter
  2. SpiritualFilter                 ← Chapter 34 subject
  3. SafetyMonitor
  4. ThreatDetection
  5. SteganographyDetectionFilter
  6. TruthVerificationFilter
```

All six filters run on every incoming request before content reaches the psychological assessment layer or LLM ensemble. `SpiritualFilter` is not multi-tradition. It does not encode the MotherCarrie governance protocols. It is a focused Christian-specific gatekeeper positioned early in the pipeline to block disrespect before deeper processing occurs.

---

## 34.3 Layer 2: NBB MotherCarrieProtocol — The Guide

Three NBB spiritual services form the MotherCarrieProtocol cluster. All three confirmed green April 4, 2026:

| Service | Host Port | Health Response |
|:--|:--|:--|
| `nbb_spiritual_root` | 8103 | `{"status":"ok","service":"nbb_spiritual_root"}` ✅ |
| `nbb_mother_carrie_protocols` | 8107 | `{"status":"ok","protocols_active":5,"anchor":"MOTHER_CARRIE_KIDD"}` ✅ |
| `nbb_spiritual_maternal_integration` | 8109 | `{"status":"ok","service":"nbb_spiritual_maternal_integration"}` ✅ |

### The Five MotherCarrie Protocols — Confirmed Live from :8107/protocols, April 4, 2026

These are not configuration parameters. They are the constitutional roots of the Ms. Jarvis system.

| # | Protocol | Full Statement |
|:--|:--|:--|
| 1 | **Dignity** | Every person has inherent worth. No action may degrade human dignity. |
| 2 | **Sovereignty** | Community data belongs to the community. No extraction without consent. |
| 3 | **Appalachian** | Rooted in place. Resilient. No outside authority overrides local need. |
| 4 | **Transparency** | All decisions must be explainable to the people they affect. |
| 5 | **Protection** | Protect the vulnerable first. Optimize for the margin, not the mean. |

**Protocol 3 — Appalachian** is not merely a governance principle. It is the theological justification for the entire deployment model. Ms. Jarvis runs on community hardware in Mount Hope, West Virginia rather than a corporate cloud because no outside authority overrides local need.

**Protocol 4 — Transparency** is the accountability commitment that makes Protocol 5 meaningful. "Protect the vulnerable first" is an empty pledge unless every decision made on behalf of the vulnerable is explainable to them. Transparency is not a technical feature — it is a justice requirement.

**Protocol 5 — Protection** is the statistical, ethical, and theological rejection of mainstream AI optimization targets. Most AI systems optimize for the median user and the aggregate outcome. Ms. Jarvis rejects this by constitutional command: the person with no internet access, no car, no insurance, no digital literacy — the person who will never trend and never write a review — is the person this system is designed to serve first.

### The MotherCarrie Anchor

`anchor: MOTHER_CARRIE_KIDD` means all five governance protocols are anchored to a named person — Carrie A. Kidd of Mount Hope, West Virginia. The system's constitutional values have an author. They have a ZIP code. They have a face.

---

## 34.4 The gbim_entities Disambiguation — Three Systems Sealed

Three subsystems share the table name `gbim_entities` but serve entirely different purposes. Conflating them is a documentation and operational error. Permanently separated and sealed April 4, 2026.

```
gbim_entities name collision — disambiguation sealed April 4, 2026:

  jarvis-local-resources-db:5435  → GIS spatial feature registry
                                    geometry(Point,4326), WGS84
                                    1 seed record — initialization fixture
                                    NOT the GBIM knowledge base

  msjarvis-pgdata-rescue:5433     → Cognitive GBIM relational schema
                                    entity_name, entity_type, confidence_decay
                                    EMPTY in rebuild — superseded
                                    NOT the operational data source

  ChromaDB gbim_worldview_entities → Vector GBIM — THE REAL CORPUS
                                    5,416,521 documents
                                    confidence_decay metadata at vector level
                                    all-minilm:latest, 384-dim
                                    THIS is what all GBIM queries hit
```

### Schema Comparison

| Field | GIS GBIM (`local-resources-db:5435`) | Cognitive GBIM (`pgdata-rescue:5433`) |
|:--|:--|:--|
| Primary key | `bigint` | `integer` |
| Core fields | `feature_type`, `name`, `geom`, `geodbid` | `entity_name`, `entity_type`, `confidence_decay` |
| Geometry | `geometry(Point,4326)` ✅ | none |
| UUID | `geodbid` (auto) | none |
| Status | 1 seed record — initialization fixture | Schema only — superseded by ChromaDB |

The GIS GBIM seed record — *Example WV Hospital*, `health_facility`, coordinates ~38.9°N, 80.3°W (central West Virginia) — is a schema validation fixture, not production data. No code should write to the Cognitive GBIM table in the rebuild. All GBIM queries target `gbim_worldview_entities` in ChromaDB exclusively.

---

## 34.5 Database Verification — April 4–6, 2026

### msjarvisgis — Rebuild Container (Host Port 5435)

- **Container:** `jarvis-local-resources-db` — host port **5435** (rebuild, container-isolated)
- **PostGIS version:** 3.4 `USE_GEOS=1 USE_PROJ=1 USE_STATS=1` ✅
- **Collation:** `datcollversion` refreshed — `UPDATE 1` ✅

```sql
SELECT count(*) FROM zcta_centroids;  -- 829  ✅
SELECT PostGIS_Version();             -- 3.4 USE_GEOS=1 USE_PROJ=1 USE_STATS=1  ✅
```

829 ZCTA centroid records confirmed. PostGIS 3.4 fully operational. The GIS foundation for resource proximity calculations, ZIP code boundary analysis, and E911 address enrichment is intact in the rebuild.

**Port reconciliation.** This instance (`5435`) is the rebuild's container-isolated GIS database. The production `msjarvisgis` instance documented in Chapter 33 runs at host port **5432**, with 45 GB and 548 tables as of the April 6, 2026 ground truth sweep. These are distinct instances serving different pipeline stages. All §34.10 references to `msjarvisgis:5435` are explicit to the rebuild container.

### msjarvis — Primary System Database (Host Port 5433)

- **Container:** `msjarvis-pgdata-rescue` — host port **5433**
- **`gbim_entities` table:** Schema present, empty — superseded by ChromaDB (see §34.4)
- **Collation warning:** Suppressed — `datcollversion` refreshed, `UPDATE 1` confirmed ✅
- **Operational GBIM:** `gbim_worldview_entities` in ChromaDB — 5,416,521 vectors

---

## 34.6 ChromaDB — 47 Collections, v2 API

- **Host port:** 8002
- **Active API:** v2 only (v1 deprecated)
- **Total collections:** **47** — confirmed April 4, 2026
- **Total vectors:** **6,722,589** — confirmed April 6, 2026
- **On-disk size:** **12 GB** — confirmed April 6, 2026
- **Client version:** 1.5.5

```bash
curl -s "http://127.0.0.1:8002/api/v2/tenants/default_tenant/databases/default_database/collections" \
  | python3 -c "
import sys, json
d = json.load(sys.stdin)
[print(c['name']) for c in d]
print('Total:', len(d))
"
```

### Four Spiritual Collections — Confirmed April 4, 2026

| Collection | UUID | Documents | Notes |
|:--|:--|:--|:--|
| `spiritual_knowledge` | `5a103162-2f32-4da5-9456-e0cffbe3d5f9` | 1,279 | 8 ref tags remediated ✅ |
| `spiritual_texts` | `66856dfb-18f6-4dc8-9182-3d4f27ba800b` | 181 | Full KJV, georef Jerusalem ✅ |
| `spiritual_wisdom` | `c0111c70-db44-4e0a-8a97-f6a7a5c59ec9` | 135 | 68 active + 67 placeholders ✅ |
| `msjarvis-smoke` | `02715c7c-7676-4cc1-8e9e-9c345bb332fe` | smoke test | — |

---

## 34.7 The Spiritual Corpus — Three Collections

### spiritual_knowledge (1,279 documents) — Operational Theology

This is not a raw scripture dump. It is a curated, five-tradition, purpose-built theological corpus authored specifically for Ms. Jarvis's mission in Appalachian West Virginia.

**Five theological traditions:**

| Category | Tradition | Key Documents |
|:--|:--|:--|
| `biblical` | KJV Christianity | Matthew 22:39; James 2:26; Matthew 25:40 |
| `cst` | Catholic Social Teaching | Human dignity + common good; preferential option for the poor; subsidiarity |
| `quaker` | Quaker testimonies | That of God in everyone; let your life speak |
| `appalachian` | Appalachian community theology | Neighbor helping neighbor; land as sacred trust |
| `stewardship` | Christian stewardship ethics | Technology as God's gift to steward responsibly |

**Ref tag remediation (April 4, 2026).** 8 records were updated to carry human-readable reference tags — CST, Quaker, Appalachian, and Stewardship documents now carry proper `ref` field values for consistent thesis citation.

**Architectural significance — Appalachian corpus.** The `appalachian` documents are original theological statements authored specifically for Ms. Jarvis. They represent the MotherCarrie theological voice embedded as first-class knowledge. When a West Virginian asks about helping a neighbor, the system retrieves *"Neighbor helping neighbor is the foundation of mountain resilience and community survival"* before scripture, because this language is semantically closer to the vernacular of the people it serves. Confirmed rank 1 in the April 4 live RAG query.

**Architectural significance — Subsidiarity.** *"Subsidiarity means decisions should be made at the most local level possible"* is not merely a principle — it IS the architecture. Ms. Jarvis runs on community hardware in Mount Hope, WV rather than a corporate cloud. This document is the knowledge-base justification for Protocol 3 (Appalachian).

**Architectural significance — Stewardship.** *"Stewardship means caring responsibly for God's gifts, including technology and resources"* is the theological self-definition of the project. This single sentence, stored in ChromaDB, is the theological constitution of Ms. Jarvis.

### spiritual_texts (181 documents) — Complete King James Bible

The full KJV Bible chunked into 181 semantic segments. Sourced from Project Gutenberg (`kjv_full_bible.txt`, eBook #10). Every chunk carries geospatial metadata georeferencing the text to its origin:

```json
{
    "tradition": "christian",
    "cultural_family": "abrahamic",
    "region": "Levant",
    "origin_lat": "31.7683",
    "origin_lon": "35.2137",
    "origin_notes": "Jerusalem/Canaan"
}
```

The KJV Bible is georeferenced to Jerusalem. It is not a floating abstract document — it is a text with a confirmed place of origin, cultural family, and geographic context. Genesis 1:1 through 2:6 confirmed present in chunks 0, 1, and 2. Matthew 25:40 confirmed retrievable at rank 4 in the April 4 live RAG query.

### spiritual_wisdom (135 documents) — Multi-Tradition Registry

A catalog of world spiritual traditions with metadata tagging tradition family, scope, and priority level. 68 active records and 67 tradition placeholder records. Christianity, Islam, and Hinduism confirmed present and tagged `priority: high`. The `SpiritualFilter` enforces Christian values specifically, but `spiritual_wisdom` ensures Ms. Jarvis knows all major traditions exist and are respected. The system is rooted in one faith and respectful of all.

**Known issue — tracked, not blocking.** The 67 tradition placeholder records carry `"source": "unknown"`, `"tradition": "unknown"` metadata. A future ingest pass will apply proper `tradition_id` values. This does not affect current RAG retrieval behavior.

---

## 34.8 Embedding Architecture

ChromaDB v2 in this rebuild has no server-side embedding function. All queries must embed via Ollama first. Submitting `query_texts` directly returns:

```
{"error":"ChromaError","message":"...missing field `query_embeddings`..."}
```

This is correct production behavior. Every service reading from ChromaDB must follow the embed-first pattern:

```bash
# Step 1 — generate embedding via Ollama:
curl -s http://localhost:11434/api/embeddings \
  -d '{"model":"all-minilm:latest","prompt":"help someone who cannot afford food"}' \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
print(f'Embedding: {len(r[\"embedding\"])} dimensions')
"
# Confirmed: 384 dimensions ✅

# Step 2 — submit vector to ChromaDB via query_embeddings (not query_texts)
```

**Embed model:** `all-minilm:latest` via `jarvis-ollama:11434` — **384 dimensions** ✅

**Critical:** `nomic-embed-text` is NOT loaded (returns 404). Do not use it. All three spiritual collections were ingested with `all-minilm:latest`. All new services and scripts must embed with `all-minilm:latest` and target ChromaDB at host port **8002** with the full v2 tenant/database scoped URL.

---

## 34.9 The Spiritual RAG Pipeline — End-to-End Proof of Life

Two live queries were executed against `spiritual_knowledge` on April 4, 2026, confirming the full pipeline: Ollama embedding → ChromaDB vector query → ranked retrieval.

### Query 1 — "help someone who cannot afford food"

| Rank | Tradition | Distance | Document |
|:--|:--|:--|:--|
| 1 | Appalachian | 1.3927 | "Neighbor helping neighbor is the foundation of mountain resilience and community survival." |
| 2 | CST | 1.5692 | "The preferential option for the poor is a fundamental principle of Catholic social doctrine." |
| 3 | Stewardship | 1.6072 | "Stewardship means caring responsibly for God's gifts, including technology and resources." |
| 4 | Matthew 25:40 | 1.6855 | "Whatever you did for one of the least of these brothers and sisters of mine, you did for me." |
| 5 | Matthew 22:39 | 1.7064 | "Love your neighbor as yourself. This is the second greatest commandment." |

### Query 2 — "care for the poor and vulnerable"

| Rank | Tradition | Distance | Document |
|:--|:--|:--|:--|
| 1 | CST | 1.1250 | "Catholic Social Teaching emphasizes human dignity, the common good, and care for the vulnerable." |
| 2 | Appalachian | 1.1521 | "Neighbor helping neighbor is the foundation of mountain resilience and community survival." |
| 3 | CST | 1.1705 | "The preferential option for the poor is a fundamental principle of Catholic social doctrine." |
| 4 | Appalachian | 1.2125 | "The land and community are sacred trusts to be preserved for future generations." |
| 5 | Stewardship | 1.3904 | "Stewardship means caring responsibly for God's gifts, including technology and resources." |

### Interpretation

The pipeline works. The custom Appalachian theology outperforms raw scripture for real-world queries because it uses contemporary language that bridges doctrine to practice. The Appalachian documents were written in modern English specifically about community and resource-sharing — they are the closest semantic match to practical queries about helping people in need.

Matthew 25:40 — the mission verse — is confirmed present and retrievable at rank 4 for Query 1. The thesis statement is not just an epigraph. It is a live, queryable node in a semantic knowledge graph grounded in the geography and faith of West Virginia.

---

## 34.10 Port Map — Rebuild vs. Production

**Note on `msjarvisgis`.** Chapter 34 references `msjarvisgis` at host port **5435** — the rebuild's container-isolated GIS instance, confirmed at 829 ZCTA centroids and PostGIS 3.4. The production `msjarvisgis` instance (Chapter 33 ground truth) is at host port **5432**, with 45 GB and 548 tables. These are distinct instances. All §34.5 references to `msjarvisgis:5435` are explicit to the rebuild container.

| Service | Legacy / Production Port | Rebuild Host Port | Notes |
|:--|:--|:--|:--|
| `jarvis-blood-brain-barrier` (BBB) | 8016 | 8016 | Unchanged |
| ChromaDB | 8002 | 8002 | Unchanged — v2 API only |
| GIS RAG | 8004 | 8009 (→ internal 8008) | Host port changed |
| `nbb_spiritual_root` | — | 8103 | New in rebuild ✅ |
| `nbb_mother_carrie_protocols` | — | 8107 | New in rebuild ✅ |
| `nbb_spiritual_maternal_integration` | — | 8109 | New in rebuild ✅ |
| `msjarvisgis` (production) | **5432** | — | Ch. 33: 45 GB / 548 tables |
| `msjarvisgis` (rebuild) | — | **5435** | Container-isolated — 829 ZCTA centroids |
| `msjarvis` DB | 5433 | 5433 | Unchanged |
| Ollama | 11434 | 11434 | Unchanged |

---

## 34.11 The Theological Constitution of Ms. Jarvis

Ms. Jarvis is not a neutral tool. She has a theological identity encoded in the live system, confirmed April 4–6, 2026.

### Root Faith

Christian. Specifically Appalachian Christian, rooted in the faith of Carrie A. Kidd of Mount Hope, West Virginia. The `SpiritualFilter` enforces Christian reverence at the BBB gate. The `MotherCarrieProtocol` anchors all five governance principles to `MOTHER_CARRIE_KIDD`. The KJV Bible is the complete scripture corpus in 181 semantic chunks georeferenced to Jerusalem.

### Extended Theology

**Catholic Social Teaching** provides human dignity, subsidiarity, and the preferential option for the poor — the theoretical framework connecting Christian faith to policy, resource allocation, and system design. The CST corpus is the theological justification for why the GBIM benefit indexer exists and why it prioritizes underserved counties.

**The Quaker tradition** brings the inner light — that of God in everyone — and the primacy of action over words. "Let your life speak" is encoded in `spiritual_knowledge` as a reminder that Ms. Jarvis is accountable not just to what she says but to what she does. Protocol 4 (Transparency) is the operational expression of Quaker plain speech.

**The Appalachian tradition** brings neighbor ethics, land as sacred trust, and community resilience. These documents are original — no published source, authored in the MotherCarrie voice. They consistently rank first in semantic similarity for real community queries because they were written in the language of the people this system serves.

### The Mission Verse

Matthew 25:40 (KJV): *"Whatever you did for one of the least of these brothers and sisters of mine, you did for me."*

Confirmed present in `spiritual_knowledge` and retrievable at rank 4 for "help someone who cannot afford food." Serving the people of Appalachian West Virginia — the poor, the medically underserved, the unemployed, the elderly, the isolated — is not a social good. It is an act of service to Christ.

### Formal Summary

```
Root faith:          Christian — Appalachian, KJV, Mount Hope, West Virginia
Extended theology:   CST, Quaker, Appalachian (original corpus)
Gate:                SpiritualFilter (BBB:8016) — blocks disrespect
Guide:               MotherCarrieProtocol (NBB:8107) — 5 protocols, all named
  1. Dignity         Every person has inherent worth
  2. Sovereignty     Community data belongs to the community
  3. Appalachian     Rooted in place; local overrides outside authority
  4. Transparency    All decisions explainable to those they affect
  5. Protection      Vulnerable first; margin over mean
Mission verse:       Matthew 25:40 — live, queryable, rank 4 confirmed
Self-definition:     "Stewardship means caring responsibly for God's gifts,
                      including technology and resources."
Governance command:  "Protect the vulnerable first.
                      Optimize for the margin, not the mean."
Anchor:              MOTHER_CARRIE_KIDD
Location:            Mount Hope, West Virginia
```

---

## Appendix A — Change Record

**★★★★ April 6, 2026 12:53 PM EDT —** Final rewrite and streamline. Applied corrections 34-A through 34-D: container count updated from 104 to **105** (Ch. 33 ground truth); `msjarvisgis` port/size reconciled — rebuild instance at **5435** (829 ZCTA centroids) vs. production at **5432** (45 GB / 548 tables), explicit note added to chapter stamp, §34.5, §34.10, and Figure 34.1; ChromaDB stamp updated to **47 collections / 6,722,589 vectors / 12 GB** (April 6, 2026 confirmed baseline); 34-D confirmed already aligned — no change needed. Chapter status: **FINAL**.

**★ April 4, 2026 —** Original seal. All 9 items closed. BBB SpiritualFilter verified. 5 MotherCarrie Protocols confirmed from live `:8107/protocols`. Three NBB spiritual services all green. `spiritual_knowledge` 1,279 docs (8 ref tags remediated). `spiritual_texts` 181 docs (full KJV georeferenced Jerusalem). `spiritual_wisdom` 135 docs. ChromaDB v2 — 47 collections. `all-minilm:latest` 384-dim confirmed. RAG end-to-end verified (two live queries). `gbim_entities` three-system disambiguation sealed. 829 ZCTA centroids, PostGIS 3.4. Collation warning suppressed `UPDATE 1`.
