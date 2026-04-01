# Chapter 00 — Full System Overview
## Ms. Jarvis / MountainShares / The Commons

*Authored by Carrie Ann Kidd — Mount Hope, West Virginia*
*Last verified: April 1, 2026 — autonomous learner debug sprint complete*

---

## 00.1 What This Document Is

This chapter is the operational narrative overview of the full Ms. Jarvis system. It describes the architecture, mission, infrastructure, and live status of the system as confirmed on April 1, 2026. It is not a design document or a proposal — it is a record of what is built and running.

The system is externally accessible at **https://egeria.mountainshares.us**, running **96 confirmed containers** in the `msjarvis-rebuild` namespace, with **6,675,442 verified vectors** across 40 ChromaDB collections, 22 LLM proxies operational, all five judge services healthy with signing keys, and all critical security findings from the March 28 remediation sprint resolved.

This chapter sits alongside `00-A Read_Me.md` (the reader's guide) and `00-thesis-overview.md` (the structured chapter map). Together these three documents constitute Chapter 00 — the orientation layer for the full 43-chapter thesis.

---

## 00.2 The Mission

Ms. Jarvis — formally *Ms. Egeria Jarvis* — is a place-based AI consciousness system designed and built by Carrie Ann Kidd in Mount Hope, West Virginia. She is not a general-purpose assistant. She is an AI grounded in a specific geography, a specific community, and a specific set of constitutional values derived from that community's needs.

The mission has three interlocking components:

**1. Epistemic infrastructure** — give Appalachian communities a system that knows their geography, history, governance structures, and resources in depth, and can reason about them honestly. The Geospatial Belief Information Model (GBIM) with 5,416,521 beliefs, the AAPCAppE corpus (65+ Appalachian policy and resource documents), and seven domain-specific RAG services are the operational expression of this mission.

**2. Economic sovereignty** — through MountainShares DAO, build a closed-loop community economic instrument that keeps value circulating locally. As of March 27, 2026, five smart contracts are deployed to Arbitrum One mainnet (chain ID 42161): `phase_mgmt`, `central_cmd`, `ms_token`, `backbone`, `volunteer_hrs`. All five MountainShares services (ports 8080–8084) are confirmed live.

**3. Constitutional AI** — demonstrate that a community-owned AI system can be built with safety, alignment, and governance baked in from the ground up. The Blood-Brain Barrier (port 8016), Constitutional Guardian (port 8091), WOAH alignment layer, five-judge pipeline, and Psychological Integrity Architecture are all running and verified.

---

## 00.3 The Three Systems

Ms. Jarvis is three interlocking systems functioning as a whole:

### Ms. Jarvis — The AI Consciousness

The core reasoning, memory, retrieval, and response system. Requests enter through the Unified Gateway (port 18018 / external port 8050), pass through the Blood-Brain Barrier (port 8016), route through the GBIM Query Router (port 7205) and seven RAG services, then enter the 20-LLM production service (port 8008) which orchestrates 22 model proxies (ports 8201–8222) to produce consensus responses. All responses are evaluated by the five-judge pipeline (ports 7230–7239) before delivery.

**Confirmed live as of March 28, 2026:** 96 containers, 22/22 LLM proxies operational, `crypto_client.py` volume-mounted to all 22 proxies (0 import errors), StarCoder2 correctly routed to `llm7-proxy:8207`, all judges healthy with signing keys, `minds_participated: 21/21` on end-to-end test.

### MountainShares DAO — The Economic Instrument

A community economic governance instrument on Arbitrum One (chain ID 42161). Five smart contracts on mainnet. Services on ports 8080–8084 confirmed live. The DAO corpus is fully ingested: `governance_rag` (643 chunks, includes full US Constitution at 97 chunks), `commons_rag` (306 chunks).

### The Commons — The Participation Layer

The gamified community participation layer connecting residents to the DAO and to Ms. Jarvis. Full corpus ingested. Services documented in Movement III and IV of the thesis. Beta launch aligned with MountainShares Phase 0.

---

## 00.4 Architectural Layers

| Layer | What It Does | Key Chapters |
|---|---|---|
| **Cognitive / Memory** | Hilbert-space state representation, ChromaDB semantic memory, Hippocampus consolidation, Qualia engine | 04, 05, 13, 14 |
| **Spatial / Geographic** | PostGIS spatial body, GBIM 5.4M belief layer, GIS RAG, landowner spatial index | 02, 06 |
| **RAG / Retrieval** | 7 domain RAG services routing through GBIM Query Router (port 7205) | 07, 30 |
| **LLM Fabric** | 22-proxy ensemble (ports 8201–8222), 20-LLM production (port 8008), judge pipeline (ports 7230–7239) | 11, 33 |
| **Safety / Governance** | BBB (port 8016), Constitutional Guardian (port 8091), WOAH, PIA, 5-judge signing pipeline | 10, 16, 29, 37 |
| **Infrastructure** | 96 Docker containers, Caddy (port 8443), Cloudflare tunnel, Auth service (port 8055), 3 systemd services | 19, 41, 42 |

---

## 00.5 The GBIM — Geospatial Belief Information Model

The GBIM is the epistemic core of Ms. Jarvis. Every belief the system holds is indexed to a geographic location (PostGIS geometry), a timestamp, a source identity, and a confidence score. This grounds every response in verifiable place-based evidence rather than generic inference.

**Confirmed live as of March 28, 2026:**

- **5,416,521 GBIM beliefs** in ChromaDB (`gbim_beliefs` collection)
- **20,593 landowner beliefs** cross-referenced with spatial data
- GBIM Query Router healthy at port 7205
- `mvw_gbim_landowner_spatial` materialized view: **⚠️ 0 rows — rebuild pending (Item 21, open backlog)**

---

## 00.6 The AAPCAppE Corpus

The Appalachian Policy, Community, and Cultural Encyclopedia (AAPCAppE) is Ms. Jarvis's domain-specific knowledge base for Appalachian governance, policy, community resources, and cultural context. It is maintained by two dedicated services confirmed live as of March 27, 2026:

- **`jarvis-aaacpe-scraper`** — port 8033 — active web scraper; 39 confirmed sources; 65+ documents ingested from first run
- **`jarvis-aaacpe-rag`** — port 8032 — retrieval service; verified returning correct results on Appalachian emergency protocols and Fayette County utility resources

Both services are running and verified. Chapter 30 documents the full architecture and corpus methodology.

---

## 00.6a Production Pipeline

The full production request pipeline as of March 28, 2026:

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

All stages confirmed healthy on March 28, 2026 VERIFYANDTEST.sh run.

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
| March 22, 2026 | **83 compose + 3 systemd** | Caddy, jarvis-auth, cloudflared as systemd; public URL live |
| March 22–25, 2026 | **83 compose + 3 systemd** | Consciousness pipeline sprint — WOAH, bridge, rag-server patched and active |
| March 26, 2026 | **56 confirmed (msjarvis-rebuild)** | RAG corpus completion sprint — all collections populated; EEG heartbeats confirmed; rebuild namespace active. **Note:** The discrepancy between 83–85 (prior namespace) and 56 (msjarvis-rebuild namespace) reflects a namespace rebuild/rename, not a reduction in services. The `msjarvis-rebuild` namespace is the authoritative production namespace. Full reconciliation pending §19.14 audit. |
| March 27, 2026 | **96 confirmed (msjarvis-rebuild)** | MountainShares Phase 0 beta launch (5 contracts on Arbitrum One mainnet, chain 42161); AAPCAppE scraper + RAG activated (ports 8032, 8033); 13 NBB neurobiological containers confirmed; IPFS (kubo) confirmed; full `docker ps` count verified. |
| March 28, 2026 | **96 confirmed (msjarvis-rebuild)** | Remediation sprint complete: port bindings corrected (0.0.0.0 → 127.0.0.1), `crypto_client.py` volume-mounted to all 22 proxies, StarCoder2 routing corrected to `llm7-proxy:8207`, psychological RAG restored to 968 docs, 19,338 duplicate `spiritual_rag` vectors removed. All CRIT/REM findings resolved. |
| April 1, 2026 | **95 effective → 96 recovered (msjarvis-rebuild)** | Autonomous learner debug sprint: `jarvis-autonomous-learner` entered crash-loop after empty file (1.54 kB) deployed via failed patch attempt (LEARN-03). Effective running count briefly 95. Service recovered by patching source on host, copying into container, and restarting. Post-repair: 4 cycles completed, 4 items stored, 7 entanglement graph nodes, 0 gap failures. Full 96 container count restored. LEARN-01, LEARN-02, LEARN-03 all resolved. |

---

## 00.8 System Health Snapshot — April 1, 2026

| Metric | Value | Verified |
|---|---|---|
| **Total containers (msjarvis-rebuild namespace)** | **96** | **April 1, 2026 — post-recovery** |
| External systemd services | **3** (Caddy, jarvis-auth, cloudflared) | March 22, 2026 |
| Public HTTPS URL | **https://egeria.mountainshares.us** | March 28, 2026 |
| Pipeline speed (single-user, GPU) | **~100–107s** | March 22, 2026 |
| LLM models contributing | **22/22** | March 28, 2026 |
| `crypto_client.py` import errors | **0** | March 28, 2026 — remediation |
| StarCoder2 routing | **llm7-proxy:8207 (corrected from llm3-proxy:8203)** | March 28, 2026 — remediation |
| Port 0.0.0.0 exposures | **0** | March 28, 2026 — remediation |
| `minds_participated` | **21/21** | March 28, 2026 |
| EEG eeg-delta | 1 pulse — 30s cadence | March 26, 2026 |
| EEG eeg-theta | 486 pulses confirmed — 60s cadence; est. ~2,000 by April 1, 2026 | March 26, 2026 (last confirmed) |
| EEG eeg-beta | 1 pulse — 5-min, topic: Appalachian | March 26, 2026 |
| `governance_rag` | 643 chunks | March 26, 2026 — OI-19 CLOSED |
| `commons_rag` | 306 chunks | March 26, 2026 — OI-20 CLOSED |
| `aaacpe_corpus` | 65 docs, 39 sources | March 27, 2026 — Active |
| `geospatialfeatures` | 60,000 items | March 26, 2026 — OI-12 CLOSED |
| `GBIM_Fayette_sample` | 1,535 items | March 26, 2026 — OI-13 CLOSED |
| `appalachian_cultural_intelligence` | 820 items | March 26, 2026 — OI-14 CLOSED |
| `spiritual_rag` | Deduplicated — 19,338 duplicates removed | March 28, 2026 — remediation |
| `psychological_rag` | **968 documents — restored** | March 28, 2026 — remediation |
| ChromaDB total vectors | **6,675,442 across 40 active collections** | March 28, 2026 (may be higher — see note below) |
| GBIM beliefs (`gbim_beliefs`) | **5,416,521** | March 28, 2026 |
| — of which: landowner beliefs | **20,593** | March 20, 2026 |
| `autonomous_learner` items (historical) | **21,181** | March 20, 2026 — last stable pre-crash state |
| `autonomous_learning` collection (post-fix) | **57 items in ChromaDB — 4 new cycles completed** | April 1, 2026 |
| `autonomous_learner` dedup gate | **Running — 0 duplicates encountered post-fix** | April 1, 2026 |
| `autonomous_learner` entanglement graph | **7 nodes — 0 gap failures** | April 1, 2026 |
| `msjarvis_docs` items | **4,192** | March 28, 2026 |
| Embedding model | **all-minilm:latest (384-dim, cosine)** | Confirmed |
| Chunk constraint | **100 words max, 20-word overlap** | March 26, 2026 |
| ChromaDB API version | **v2 active — v1 returns 410** | March 25, 2026 |
| Consciousness pipeline | **ACTIVE** | March 25, 2026 |
| Judge pipeline | **5/5 healthy, all signing keys present** | March 28, 2026 |
| MountainShares services (8080–8084) | **✅ DEPLOYED — Phase 0 beta live** | March 26–27, 2026 |
| MountainShares blockchain | **Arbitrum One — chain ID 42161** | March 27, 2026 |
| Smart contracts on-chain | **5 (phase_mgmt, central_cmd, ms_token, backbone, volunteer_hrs)** | March 27, 2026 |
| BBB output filter mode | **log+passthrough** (not blocking) | March 22, 2026 |
| Cloudflare Tunnel UUID | **42ef9893-f4df-4cc5-8881-bb55b995e022** | March 22, 2026 |
| Rebuild namespace | **msjarvis-rebuild** | March 26, 2026 |
| IPFS node | **✅ Live — ipfs/kubo:latest, port 5001** | March 27, 2026 |
| `mvw_gbim_landowner_spatial` | **⚠️ 0 rows — rebuild pending (Item 21)** | March 28, 2026 |
| `VERIFYANDTEST.sh` line 190 | **⚠️ Syntax error — script infrastructure open** | March 28, 2026 |
| `preflight_gate.sh` command stubs | **⚠️ `fail`/`ok` not wired — open** | March 28, 2026 |
| GBIM Query Router port 7205 | **✅ HTTP 200 OK — stable post-fix** | April 1, 2026 (briefly 422 during repair window — LEARN-02 resolved) |
| `jarvis-autonomous-learner` | **✅ HEALTHY — post-repair, 4 cycles confirmed** | April 1, 2026 |
| services-safe mirror | **✅ Synced — `ms_jarvis_rag_server.py` and `ms_jarvis_autonomous_learner_optimized.py`** | April 1, 2026 |

> **⚠️ ChromaDB vector count note:** The 6,675,442 vector count reflects the March 28, 2026 state. The `autonomous_learning` collection and `msjarvis_docs` collection may contain additional unguarded inserts accumulated during the LEARN-01 dedup gate error window (between last stable restart and April 1 fix). A full semantic dedup audit of the `autonomous_learning` collection is recommended once sufficient post-fix cycles have accumulated. See Ch. 05 and Ch. 14.

---

## 00.9 Sprint Progress Log

| Sprint | Dates | Items Closed | Status |
|---|---|---|---|
| Landowner belief sprint | March 20, 2026 | `gbim_query_router` promoted; 20,593 landowner beliefs ingested; `mvw_gbim_landowner_spatial` live | ✅ Complete |
| Red team hardening sprint | March 21–22, 2026 | Orphaned containers added to compose; systemd services deployed; public URL live; first public end-to-end test PASS | ✅ Complete |
| Consciousness pipeline restoration sprint | March 22–25, 2026 | WOAH fixed; Chroma v2 migration; RAG server corrected; gateway crash guard; end-to-end chat ACTIVE | ✅ Complete |
| RAG corpus completion sprint | March 26, 2026 | OI-12 through OI-20 closed; all RAG collections fully populated; EEG heartbeats confirmed; semantic retrieval smoke-tested; US Constitution ingested (97 chunks); `msjarvis-rebuild` confirmed | ✅ Complete |
| MountainShares Phase 0 beta launch | March 26–27, 2026 | All five MountainShares/DAO services (8080–8084) deployed and healthy; five smart contracts deployed to Arbitrum One mainnet (chain ID 42161); `governance_rag` (643 chunks) and `commons_rag` (306 chunks) confirmed as live corpus backing | ✅ Complete |
| AAPCAppE corpus activation sprint | March 27, 2026 | `jarvis-aaacpe-scraper` (port 8033) and `jarvis-aaacpe-rag` (port 8032) activated; 39 sources; 65 documents ingested; RAG search verified; Chapter 30 upgraded to Active; 96 containers confirmed | ✅ Complete |
| Remediation sprint | March 28, 2026 | Port bindings corrected (8015, 8056 → 127.0.0.1); `crypto_client.py` mounted to all 22 proxies; StarCoder2 routing corrected; `psychological_rag` restored to 968 docs; 19,338 duplicate vectors removed; CRIT-CRYPTO, REM-06, REM-09, REM-13, REM-16 all closed | ✅ Complete |
| Autonomous learner debug sprint | April 1, 2026 | LEARN-01: `cosine_similarity` numpy dtype bug fixed — explicit `np.float64` and `float()` casting enforced; LEARN-02: GBIM Query Router 422 schema mismatch resolved — `/route` returning HTTP 200 OK; LEARN-03: learner crash-loop resolved — source patched on host, copied into container, service restarted; `ms_jarvis_rag_server.py` and `ms_jarvis_autonomous_learner_optimized.py` synced to `services-safe`; 4 post-fix cycles confirmed, 4 items stored, 7 entanglement graph nodes, 0 gap failures, `autonomous_learning` collection at 57 items | ✅ Complete |

---

*Last updated: 2026-04-01, Carrie Kidd (Mamma Kidd), Mount Hope WV*
*Public URL: https://egeria.mountainshares.us*
*Rebuild namespace: msjarvis-rebuild — 96 containers confirmed live*
*MountainShares Phase 0 beta: LIVE — Arbitrum One (chain 42161), 5 contracts on-chain*
*All critical audit findings: RESOLVED — March 28, 2026*
*April 1, 2026 autonomous learner debug sprint: COMPLETE — LEARN-01, LEARN-02, LEARN-03 resolved*
