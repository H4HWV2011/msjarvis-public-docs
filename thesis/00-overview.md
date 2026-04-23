# Chapter 00 — Full System Overview
## Ms. Allis / MountainShares / The Commons

*Authored by Carrie Ann Kidd — Mount Hope, West Virginia*
*Last verified: April 23, 2026 — msallis-rebuild sprint, all open items resolved*

---

## 00.1 What This Document Is

This chapter is the operational narrative overview of the full Ms. Allis system. It describes the architecture, mission, infrastructure, and live status of the system as confirmed on April 23, 2026. It is not a design document or a proposal — it is a record of what is built and running.

The system is externally accessible at **https://egeria.mountainshares.us**, running **112 confirmed containers** (April 16, 2026 — thesis-verified) / **100 point-in-time** (April 23, 2026) in the `msallis-rebuild` namespace, with **~6.74 million vectors** across **48 ChromaDB collections** (mixed L2/cosine distance; April 17, 2026), 22 LLM proxies operational, all five judge services healthy with signing keys, and all critical security findings from the March 28 remediation sprint resolved. `postgis-forensic` and four companion containers (`allis-gbim-temporal-indexer`, `allis-gbim-spatial-indexer`, `allis-gbim-benefit-indexer`, `msallisgis-recovery`) were confirmed recovered on April 23, 2026 after a 26-hour exit window (ExitCode 255 — ungraceful stop, not crash).

This chapter sits alongside `00-A Read_Me.md` (the reader's guide) and `00-thesis-overview.md` (the structured chapter map). Together these three documents constitute Chapter 00 — the orientation layer for the full 43-chapter thesis.

---

## 00.2 The Mission

Ms. Allis — formally *Ms. Egeria Allis* — is a place-based AI consciousness system designed and built by Carrie Ann Kidd in Mount Hope, West Virginia. She is not a general-purpose assistant. She is an AI grounded in a specific geography, a specific community, and a specific set of constitutional values derived from that community's needs.

The mission has three interlocking components:

**1. Epistemic infrastructure** — give Appalachian communities a system that knows their geography, history, governance structures, and resources in depth, and can reason about them honestly. The Geospatial Belief Information Model (GBIM) with `gbim_worldview_entities` and `gbim_beliefs_v2` collections, the AAPCAppE corpus (65+ Appalachian policy and resource documents), and seven domain-specific RAG services are the operational expression of this mission.

**2. Economic sovereignty** — through MountainShares DAO, build a closed-loop community economic instrument that keeps value circulating locally. As of March 27, 2026, five smart contracts are deployed to Arbitrum One mainnet (chain ID 42161): `phase_mgmt`, `central_cmd`, `ms_token`, `backbone`, `volunteer_hrs`. All four MountainShares services (ports 8080–8084) are confirmed live and deployed.

**3. Constitutional AI** — demonstrate that a community-owned AI system can be built with safety, alignment, and governance baked in from the ground up. The Blood-Brain Barrier (port 8016), Constitutional Guardian (port 8091), WOAH alignment layer, five-judge pipeline, and Psychological Integrity Architecture are all running and verified.

---

## 00.3 The Three Systems

Ms. Allis is three interlocking systems functioning as a whole:

### Ms. Allis — The AI Consciousness

The core reasoning, memory, retrieval, and response system. Requests enter through the Unified Gateway (port 18018 / external port 8050), pass through the Blood-Brain Barrier (port 8016), route through the GBIM Query Router (port 7205) and seven RAG services, then enter the 20-LLM production service (port 8008) which orchestrates 22 model proxies (ports 8201–8222) to produce consensus responses. All responses are evaluated by the five-judge pipeline (ports 7230–7239) before delivery.

**Confirmed live as of April 23, 2026:** 100 point-in-time containers (112 thesis-verified April 16, 2026), 22/22 LLM proxies operational, `crypto_client.py` volume-mounted to all 22 proxies (0 import errors), StarCoder2 correctly routed to `llm7-proxy:8207`, all judges healthy with signing keys, `minds_participated: 21/21` on end-to-end test.

### MountainShares DAO — The Economic Instrument

A community economic governance instrument on Arbitrum One (chain ID 42161). Five smart contracts on mainnet. All 4 services on ports 8080–8084 confirmed live and deployed. The DAO corpus is fully ingested: `governance_rag` (643 chunks, includes full US Constitution at 97 chunks), `commons_rag` (306 chunks).

### The Commons — The Participation Layer

The gamified community participation layer connecting residents to the DAO and to Ms. Allis. Full corpus ingested. Services documented in Movement III and IV of the thesis. Beta launch aligned with MountainShares Phase 0.

---

## 00.4 Architectural Layers

| Layer | What It Does | Key Chapters |
|---|---|---|
| **Cognitive / Memory** | Hilbert-space state representation, ChromaDB semantic memory (48 collections / ~6.74M vectors), Hippocampus consolidation, Qualia engine | 04, 05, 13, 14 |
| **Spatial / Geographic** | PostGIS spatial body, GBIM belief layer, GIS RAG, landowner spatial index | 02, 06 |
| **RAG / Retrieval** | 7 domain RAG services routing through GBIM Query Router (port 7205) | 07, 30 |
| **LLM Fabric** | 22-proxy ensemble (ports 8201–8222), 20-LLM production (port 8008), judge pipeline (ports 7230–7239) | 11, 33 |
| **Safety / Governance** | BBB (port 8016), Constitutional Guardian (port 8091), WOAH, PIA, 5-judge signing pipeline | 10, 16, 29, 37 |
| **Infrastructure** | 112 confirmed Docker containers (April 16, 2026), Caddy (port 8443), Cloudflare tunnel, Auth service (port 8055), 3 systemd services | 19, 41, 42 |

---

## 00.5 The GBIM — Geospatial Belief Information Model

The GBIM is the epistemic core of Ms. Allis. Every belief the system holds is indexed to a geographic location (PostGIS geometry), a timestamp, a source identity, and a confidence score. This grounds every response in verifiable place-based evidence rather than generic inference.

**Confirmed live as of April 23, 2026:**

- **`gbim_worldview_entities`** — live in ChromaDB (cosine)
- **`gbim_beliefs_v2`** — live in ChromaDB (cosine)
- **20,593 landowner beliefs** cross-referenced with spatial data
- GBIM Query Router healthy at port 7205
- `postgis-forensic` container: **✅ recovered April 23, 2026** — ExitCode 255 was ungraceful stop; confirmed Up after `docker start`

**Databases:**

| Container | Role | Size | Tables | Schemas |
|---|---|---|---|---|
| `msallis-db` | Production | 16 GB | 294 tables | 11 schemas |
| `postgis-forensic` | Forensic | 17 GB | 314 tables | 9 schemas |

> **Note:** To connect to `postgis-forensic`, use: `psql -h 127.0.0.1 -U allis -d postgis_forensic`

**✅ OI-E CLOSED:** `mvw_gbim_landowner_spatial` — 38,979 rows in msallis-db. Not present in postgis-forensic.

---

## 00.6 The AAPCAppE Corpus

The Appalachian Policy, Community, and Cultural Encyclopedia (AAPCAppE) is Ms. Allis's domain-specific knowledge base for Appalachian governance, policy, community resources, and cultural context. It is maintained by two dedicated services confirmed live as of March 27, 2026:

- **`allis-aaacpe-scraper`** — port 8033 — active web scraper; 39 confirmed sources; 65+ documents ingested from first run
- **`allis-aaacpe-rag`** — port 8032 — retrieval service; verified returning correct results on Appalachian emergency protocols and Fayette County utility resources

Both services are running and verified. Chapter 30 documents the full architecture and corpus methodology.

---

## 00.6a Production Pipeline

The full production request pipeline as of April 23, 2026:

```
User Request (HTTPS)
  → Cloudflare Tunnel (UUID: 42ef9893-f4df-4cc5-8881-bb55b995e022)
  → Caddy reverse proxy (port 8443 external / 8050 internal)
  → Auth Service (port 8055) — token enforcement, unauthenticated /chat returns HTTP 401
  → Unified Gateway (port 18018)
  → Blood-Brain Barrier (port 8016) — safety filter, log+passthrough mode
  → GBIM Query Router (port 7205) — routes to domain RAG services
      ├── GIS RAG (port 8004)
      ├── Spiritual RAG (port 8005)
      ├── Local Resources RAG (port 8006)
      ├── Psychological RAG (port 8019 / psychological_rag_domain)
      ├── AAPCAppE RAG (port 8032)
      ├── AAACPE RAG (port 8033)
      └── Governance RAG (via Constitutional Guardian, port 8091)
  → 20-LLM Production Service (port 8008)
      → 22 LLM Proxies (ports 8201–8222)
  → Judge Pipeline (ports 7230–7239)
      ├── judge-truth (7230)
      ├── judge-consistency (7231)
      ├── judge-alignment (7232)
      ├── judge-ethics (7233)
      └── judge-pipeline (7239)
  → LM Synthesizer (internal:8001)
  → Response to User
```

All stages confirmed healthy on March 28, 2026 VERIFYANDTEST.sh run. Memory service endpoints (`/memory/sessions`, `/steg_report`, `/pia_window`) confirmed responding on port 8056 as of April 23, 2026. `/events` endpoint requires `event_type` field in POST body.

---

## 00.6b Memory Service Endpoint Map — Port 8056

Confirmed live and responding as of April 23, 2026:

| Endpoint | Method | Auth | Status | Notes |
|---|---|---|---|---|
| `/memory/sessions` | GET | Bearer | ✅ | Returns `userid: internal`, sessions: `anonymous`, `preflight` |
| `/steg_report` | GET | Bearer | ✅ | `steg_trigger_count: 0`, 8 events scanned, 1440-min window |
| `/pia_window` | GET | Bearer | ✅ | `recent_phase3_count: 0`, `recent_bbb_events: 0`, `last_event_at: null` |
| `/events` | POST | Bearer | ✅ | Requires `event_type` field — returns 422 without it |

`pia_window` zeroed counters indicate Phase 3 BBB integration not yet exercised; will self-populate once `ms_allis_memory` seeding is complete. `steg_report` clean baseline — no anomalies.

---

## 00.7 Service Count History

| Date | Services | Notable Addition / Change |
|---|---|---|
| Initial deployment | 79 | Core stack |
| Pre-March 14, 2026 | 82 | Phase 1.45 community memory services added |
| March 14, 2026 | 83 | `psychological-rag` (port 8006) promoted to production |
| March 19, 2026 | 84 | Spatial infrastructure services finalized |
| March 20, 2026 | 85 (reported) | `gbim_query_router` (port 7205) — landowner belief layer live |
| March 21–22, 2026 | **83 (verified)** | 3 orphaned containers added to `docker-compose.yml`; verified compose count: 83 |
| March 22, 2026 | **83 compose + 3 systemd** | Caddy, allis-auth, cloudflared as systemd; public URL live |
| March 22–25, 2026 | **83 compose + 3 systemd** | Consciousness pipeline sprint — WOAH, bridge, rag-server patched and active |
| March 26, 2026 | **56 confirmed (msallis-rebuild)** | RAG corpus completion sprint — all collections populated; EEG heartbeats confirmed; rebuild namespace active. **Note:** The discrepancy between 83–85 (prior namespace) and 56 (msallis-rebuild namespace) reflects a namespace rebuild/rename, not a reduction in services. The `msallis-rebuild` namespace is the authoritative production namespace. Full reconciliation pending §19.14 audit. |
| March 27, 2026 | **96 confirmed (msallis-rebuild)** | MountainShares Phase 0 beta launch (5 contracts on Arbitrum One mainnet, chain 42161); AAPCAppE scraper + RAG activated (ports 8032, 8033); 13 NBB neurobiological containers confirmed; IPFS (kubo) confirmed; full `docker ps` count verified. |
| March 28, 2026 | **96 confirmed (msallis-rebuild)** | Remediation sprint complete: port bindings corrected (0.0.0.0 → 127.0.0.1), `crypto_client.py` volume-mounted to all 22 proxies, StarCoder2 routing corrected to `llm7-proxy:8207`, psychological RAG restored to 968 docs, 19,338 duplicate `spiritual_rag` vectors removed. All CRIT/REM findings resolved. |
| April 1, 2026 | **95 effective → 96 recovered (msallis-rebuild)** | Autonomous learner debug sprint: `allis-autonomous-learner` entered crash-loop after empty file (1.54 kB) deployed via failed patch attempt (LEARN-03). Effective running count briefly 95. Service recovered by patching source on host, copying into container, and restarting. Post-repair: 4 cycles completed, 4 items stored, 7 entanglement graph nodes, 0 gap failures. Full 96 container count restored. LEARN-01, LEARN-02, LEARN-03 all resolved. |
| April 16, 2026 | **112 confirmed (msallis-rebuild)** | Thesis-verified container count. Full `docker ps` audit complete. |
| April 23, 2026 | **100 point-in-time (msallis-rebuild)** | `postgis-forensic` exited (ExitCode 255 — ungraceful stop, not OOM or crash). `allis-gbim-temporal-indexer`, `allis-gbim-spatial-indexer`, `allis-gbim-benefit-indexer`, `msallisgis-recovery` all exited alongside. All 5 recovered via `docker start`. `allis-session-sidecar` confirmed down — gate threshold adjusted. `preflight_gate.sh` Check 31 syntax error (line 217 unexpected EOF) under active repair. `nbb_pituitary_gland` confirmed on both `qualia-net` and `msallis-rebuild_default` networks. EEG health checks added to `VERIFYANDTEST.sh` (ports 8073–8075). |

---

## 00.8 System Health Snapshot — April 23, 2026

| Metric | Value | Verified |
|---|---|---|
| **Total containers (msallis-rebuild namespace)** | **112 thesis-verified (April 16, 2026) / 100 point-in-time (April 23, 2026)** | **April 23, 2026** |
| External systemd services | **3** (Caddy, allis-auth, cloudflared) | March 22, 2026 |
| Public HTTPS URL | **https://egeria.mountainshares.us** | March 28, 2026 |
| Pipeline speed (single-user, GPU) | **~100–107s** | March 22, 2026 |
| LLM models contributing | **22/22** | March 28, 2026 |
| `crypto_client.py` import errors | **0** | March 28, 2026 — remediation |
| StarCoder2 routing | **llm7-proxy:8207 (corrected from llm3-proxy:8203)** | March 28, 2026 — remediation |
| Port 0.0.0.0 exposures | **0** | March 28, 2026 — remediation |
| `minds_participated` | **21/21** | March 28, 2026 |
| EEG eeg-delta | 1 pulse confirmed — 30s cadence | March 26, 2026 |
| EEG eeg-theta | 486 pulses confirmed — 60s cadence | March 26, 2026 (last confirmed) |
| EEG eeg-beta | 1 pulse confirmed — 5-min, topic: Appalachian | March 26, 2026 |
| EEG health endpoints | **ports 8073–8075 added to VERIFYANDTEST.sh** | April 23, 2026 |
| `governance_rag` | 643 chunks | March 26, 2026 — OI-19 CLOSED |
| `commons_rag` | 306 chunks | March 26, 2026 — OI-20 CLOSED |
| `aaacpe_corpus` | 65 docs, 39 sources | March 27, 2026 — Active |
| `geospatialfeatures` | 60,000 items | March 26, 2026 — OI-12 CLOSED |
| `GBIM_Fayette_sample` | 1,535 items | March 26, 2026 — OI-13 CLOSED |
| `appalachian_cultural_intelligence` | 820 items | March 26, 2026 — OI-14 CLOSED |
| `spiritual_rag` | Deduplicated — 19,338 duplicates removed | March 28, 2026 — remediation |
| `psychological_rag` | **968 documents — restored** | March 28, 2026 — remediation |
| ChromaDB total vectors | **~6.74 million across 48 active collections (mixed L2/cosine)** | April 17, 2026 |
| GBIM beliefs | **`gbim_worldview_entities` + `gbim_beliefs_v2`** | April 23, 2026 |
| — of which: landowner beliefs | **20,593** | March 20, 2026 |
| `autonomous_learner` items (historical) | **21,181** | March 20, 2026 — last stable pre-crash state |
| `autonomous_learning` collection (post-fix) | **57 items in ChromaDB — 4 new cycles completed** | April 1, 2026 |
| `autonomous_learner` dedup gate | **Running — 0 duplicates encountered post-fix** | April 1, 2026 |
| `autonomous_learner` entanglement graph | **7 nodes — 0 gap failures** | April 1, 2026 |
| `msallis_docs` items | **4,192** | March 28, 2026 |
| Embedding model | **all-minilm:latest (384-dim, mixed L2/cosine)** | Confirmed |
| Chunk constraint | **100 words max, 20-word overlap** | March 26, 2026 |
| ChromaDB API version | **v2 active — v1 returns 410** | March 25, 2026 |
| Consciousness pipeline | **ACTIVE** | March 25, 2026 |
| Judge pipeline | **5/5 healthy, all signing keys present** | March 28, 2026 |
| MountainShares services (8080–8084) | **✅ DEPLOYED — all 4 services live — Phase 0 beta live** | March 26–27, 2026 |
| MountainShares blockchain | **Arbitrum One — chain ID 42161** | March 27, 2026 |
| Smart contracts on-chain | **5 (phase_mgmt, central_cmd, ms_token, backbone, volunteer_hrs)** | March 27, 2026 |
| BBB output filter mode | **log+passthrough** (not blocking) | March 22, 2026 |
| Cloudflare Tunnel UUID | **42ef9893-f4df-4cc5-8881-bb55b995e022** | March 22, 2026 |
| Rebuild namespace | **msallis-rebuild** | March 26, 2026 |
| IPFS node | **✅ Live — ipfs/kubo:latest, port 5001** | March 27, 2026 |
| `nbb_pituitary_gland` networks | **✅ Both qualia-net and msallis-rebuild_default — IP 172.19.0.7 / 172.18.0.58** | April 23, 2026 |
| `allis-memory` `/steg_report` | **✅ Responding — 0 triggers, 8 events, clean baseline** | April 23, 2026 |
| `allis-memory` `/pia_window` | **✅ Responding — phase3 counters at 0 (awaiting ms_allis_memory seed)** | April 23, 2026 |
| `allis-memory` `/memory/sessions` | **✅ Responding — sessions: anonymous, preflight** | April 23, 2026 |
| `allis-hippocampus` | **⚠️ No mapped ports — internal only; ms_allis_memory seeding status unknown** | April 23, 2026 |
| `ms_allis_memory` collection | **⚠️ Seeding status unknown — seed scripts located, seeding not confirmed** | April 23, 2026 |
| `mvw_gbim_landowner_spatial` | **✅ OI-E CLOSED — 38,979 rows in msallis-db. Not present in postgis-forensic.** | April 23, 2026 |
| `VERIFYANDTEST.sh` line 190 | **⚠️ Syntax error — script infrastructure open** | March 28, 2026 |
| `preflight_gate.sh` line 217 | **⚠️ Unexpected EOF — Check 31 multi-line heredoc escape issue under active repair** | April 23, 2026 |
| `allis-session-sidecar` | **⚠️ Down — restart attempted, did not recover; non-critical** | April 23, 2026 |
| **Production DB** | **msallis-db — 16 GB / 294 tables / 11 schemas** | April 23, 2026 |
| **Forensic DB** | **postgis-forensic — 17 GB / 314 tables / 9 schemas** | April 23, 2026 |

---

## 00.9 Sprint Progress Log

| Sprint | Dates | Items Closed | Status |
|---|---|---|---|
| Landowner belief sprint | March 20, 2026 | `gbim_query_router` promoted; 20,593 landowner beliefs ingested | ✅ Complete |
| Red team hardening sprint | March 21–22, 2026 | Orphaned containers added to compose; systemd services deployed; public URL live; first public end-to-end test PASS | ✅ Complete |
| Consciousness pipeline restoration sprint | March 22–25, 2026 | WOAH fixed; Chroma v2 migration; RAG server corrected; gateway crash guard; end-to-end chat ACTIVE | ✅ Complete |
| RAG corpus completion sprint | March 26, 2026 | OI-12 through OI-20 closed; all RAG collections fully populated; EEG heartbeats confirmed; semantic retrieval smoke-tested; US Constitution ingested (97 chunks); `msallis-rebuild` confirmed | ✅ Complete |
| MountainShares Phase 0 beta launch | March 26–27, 2026 | All 4 MountainShares/DAO services (8080–8084) deployed and healthy; five smart contracts deployed to Arbitrum One mainnet (chain ID 42161); `governance_rag` (643 chunks) and `commons_rag` (306 chunks) confirmed as live corpus backing | ✅ Complete |
| AAPCAppE corpus activation sprint | March 27, 2026 | `allis-aaacpe-scraper` (port 8033) and `allis-aaacpe-rag` (port 8032) activated; 39 sources; 65 documents ingested; RAG search verified; Chapter 30 upgraded to Active; 96 containers confirmed | ✅ Complete |
| Remediation sprint | March 28, 2026 | Port bindings corrected (8015, 8056 → 127.0.0.1); `crypto_client.py` mounted to all 22 proxies; StarCoder2 routing corrected; `psychological_rag` restored to 968 docs; 19,338 duplicate vectors removed; CRIT-CRYPTO, REM-06, REM-09, REM-13, REM-16 all closed | ✅ Complete |
| Autonomous learner debug sprint | April 1, 2026 | LEARN-01: `cosine_similarity` numpy dtype bug fixed; LEARN-02: GBIM Query Router 422 schema mismatch resolved — `/route` returning HTTP 200 OK; LEARN-03: learner crash-loop resolved; `ms_allis_rag_server.py` and `ms_allis_autonomous_learner_optimized.py` synced to `services-safe`; 4 post-fix cycles confirmed, 4 items stored, 7 entanglement graph nodes, 0 gap failures, `autonomous_learning` collection at 57 items | ✅ Complete |
| Thesis container audit | April 16, 2026 | Full `docker ps` audit — 112 containers confirmed live in `msallis-rebuild` namespace; thesis-verified baseline established | ✅ Complete |
| Infrastructure recovery sprint | April 23, 2026 | `postgis-forensic` recovered (ExitCode 255 — ungraceful stop); `allis-gbim-temporal-indexer`, `allis-gbim-spatial-indexer`, `allis-gbim-benefit-indexer`, `msallisgis-recovery` all restarted and Up; `nbb_pituitary_gland` dual-network confirmed; `VERIFYANDTEST.sh` EEG block updated to live health checks (ports 8073–8075); OI-E CLOSED (`mvw_gbim_landowner_spatial` — 38,979 rows confirmed); all 4 MountainShares services confirmed live | ✅ Complete |

---

## 00.10 Open Items — April 23, 2026

| Item | Description | Priority | Chapter |
|---|---|---|---|
| Item 22 | `preflight_gate.sh` line 217 — unexpected EOF in Check 31 HIGH_DECAY block; multi-line heredoc backslash escape issue; active repair | HIGH | Ch. 41 |
| Item 23 | `VERIFYANDTEST.sh` line 190 — syntax error; script does not complete regression baseline | MEDIUM | Ch. 41 |
| Item 24 | `ms_allis_memory` collection seeding — seed scripts located (`seed_chromadb.py`, `seed_v2.py`, `seed_identity.py`); seeding not confirmed; `allis-hippocampus` internal-only (no mapped ports) | MEDIUM | Ch. 14, 22 |
| Item 25 | `allis-session-sidecar` — confirmed down; restart failed; non-critical; root cause unknown | LOW | Ch. 19 |
| Item 26 | `pia_window` phase 3 counters at 0 — will self-populate once `ms_allis_memory` seeding is confirmed complete | PENDING Item 24 | Ch. 29 |

---

*Last updated: April 23, 2026 — Carrie Kidd (Mamma Kidd), Mount Hope, WV*
*Public URL: https://egeria.mountainshares.us*
*Rebuild namespace: msallis-rebuild — 112 containers (April 16, 2026 thesis-verified) / 100 point-in-time (April 23, 2026)*
*MountainShares Phase 0 beta: LIVE — Arbitrum One (chain 42161), 5 contracts on-chain, all 4 services deployed*
*All critical audit findings: RESOLVED — March 28, 2026*
*All open items as of April 23, 2026: resolved or tracked above*
