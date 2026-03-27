
> Figure 00-5. Full production pipeline flow, March 27, 2026. ★ RAG corpus fully populated — `governance_rag` (643 chunks), `commons_rag` (306 chunks), and `aaacpe_corpus` (65 docs, growing) semantically verified. Gateway wiring of RAG collections to inference endpoint remains pending next sprint.

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
| March 26, 2026 | **56 confirmed (msjarvis-rebuild)** | RAG corpus completion sprint — all collections populated; EEG heartbeats confirmed; rebuild namespace active. **Note:** The discrepancy between 83–85 (prior namespace) and 56 (msjarvis-rebuild namespace) reflects a namespace rebuild/rename, not a reduction in services. The `msjarvis-rebuild` namespace is the authoritative production namespace as of March 26, 2026. Full reconciliation pending §19.14 audit. |
| March 27, 2026 | **96 confirmed (msjarvis-rebuild)** | MountainShares Phase 0 beta launch (5 contracts on Arbitrum One mainnet, chain 42161); AAPCAppE scraper + RAG activated (ports 8032, 8033); 13 NBB neurobiological containers confirmed; IPFS (kubo) confirmed; full `docker ps` count verified. |

---

## 00.8 System Health Snapshot — March 27, 2026 ★ UPDATED

| Metric | Value | Verified |
|---|---|---|
| **Total containers (msjarvis-rebuild namespace)** | **96 ★** | **March 27, 2026** |
| External systemd services | **3** (Caddy, jarvis-auth, cloudflared) | March 22, 2026 |
| Public HTTPS URL | **https://egeria.mountainshares.us** | March 22, 2026 |
| Pipeline speed (single-user, GPU) | **~100–107s** | March 22, 2026 |
| LLM models contributing | **22/22 ★** | March 27, 2026 |
| Preflight gate | **24 PASS 0 FAIL** | March 25, 2026 |
| **EEG eeg-delta** | **1 pulse — 30s cadence ★** | **March 26, 2026** |
| **EEG eeg-theta** | **486 pulses — 60s cadence ★** | **March 26, 2026** |
| **EEG eeg-beta** | **1 pulse — 5-min, topic: Appalachian ★** | **March 26, 2026** |
| **governance_rag** | **643 chunks ★** | **March 26, 2026 — OI-19 CLOSED** |
| **commons_rag** | **306 chunks ★** | **March 26, 2026 — OI-20 CLOSED** |
| **aaacpe_corpus** | **65 docs, 39 sources ★** | **March 27, 2026 — Ch.30 Active** |
| **geospatialfeatures** | **60,000 items ★** | **March 26, 2026 — OI-12 CLOSED** |
| **GBIM_Fayette_sample** | **1,535 items ★** | **March 26, 2026 — OI-13 CLOSED** |
| **appalachian_cultural_intelligence** | **820 items ★** | **March 26, 2026 — OI-14 CLOSED** |
| **spiritual_texts** | **19,338 items ★** | **March 26, 2026 — OI-15 CLOSED** |
| GBIM beliefs (`gbimbeliefnormalized`) | **5,416,522** | March 20, 2026 |
| — of which: landowner beliefs | **20,593** | March 20, 2026 |
| `autonomous_learner` items | **21,181+** | March 20, 2026 |
| `psychological_rag` items | **968** | March 20, 2026 |
| `msjarvis_docs` items | **2,348** | March 22, 2026 |
| Embedding model | **all-minilm:latest (384-dim, cosine)** | Confirmed |
| Chunk constraint | **100 words max, 20-word overlap** | March 26, 2026 |
| ChromaDB API version | **v2 active — v1 returns 410** | March 25, 2026 |
| Consciousness pipeline | **ACTIVE** | March 25, 2026 |
| **MountainShares services (8080–8084)** | **✅ DEPLOYED — Phase 0 beta live ★** | **March 26–27, 2026** |
| MountainShares blockchain | **Arbitrum One — chain ID 42161 ★** | **March 27, 2026** |
| Smart contracts on-chain | **5 (phase_mgmt, central_cmd, ms_token, backbone, volunteer_hrs) ★** | **March 27, 2026** |
| BBB output filter mode | **log+passthrough** (not blocking) | March 22, 2026 |
| Cloudflare Tunnel UUID | **42ef9893-f4df-4cc5-8881-bb55b995e022** | March 22, 2026 |
| Rebuild namespace | **msjarvis-rebuild** | March 26, 2026 |
| IPFS node | **✅ Live — ipfs/kubo:latest, port 5001 ★** | **March 27, 2026** |

---

## 00.9 Sprint Progress Log

| Sprint | Dates | Items Closed | Status |
|---|---|---|---|
| Landowner belief sprint | March 20, 2026 | `gbim_query_router` promoted; 20,593 landowner beliefs ingested; `mvw_gbim_landowner_spatial` live | ✅ Complete |
| Red team hardening sprint | March 21–22, 2026 | Orphaned containers added to compose; systemd services deployed; public URL live; first public end-to-end test PASS | ✅ Complete |
| Consciousness pipeline restoration sprint | March 22–25, 2026 | WOAH fixed; Chroma v2 migration; RAG server corrected; gateway crash guard; end-to-end chat ACTIVE | ✅ Complete — RAG embedder restart pending |
| RAG corpus completion sprint | March 26, 2026 | OI-12 through OI-20 closed; all RAG collections fully populated; EEG heartbeats confirmed; semantic retrieval smoke-tested across all four RAG domains; US Constitution ingested (97 chunks); rebuild namespace `msjarvis-rebuild` confirmed | ✅ Complete |
| MountainShares Phase 0 beta launch | March 26–27, 2026 | All five MountainShares/DAO services (8080–8084) deployed and healthy; five smart contracts deployed to Arbitrum One mainnet (chain ID 42161); contract addresses verified via `/health` endpoint; `governance_rag` (643 chunks) and `commons_rag` (306 chunks) confirmed as live corpus backing | ✅ Complete |
| AAPCAppE corpus activation sprint | March 27, 2026 | `jarvis-aaacpe-scraper` (port 8033) and `jarvis-aaacpe-rag` (port 8032) activated; scraper reporting 39 sources; `total_runs: 1`; 65 documents ingested into ChromaDB from first scrape run on startup; RAG search returning correct results (emergency protocol + Fayette County utility example verified); Chapter 30 stub status upgraded to Active; total confirmed live containers: **96** | ✅ Complete |

---

*Last updated: 2026-03-27, Carrie Kidd (Mamma Kidd), Mount Hope WV*
*Public URL: https://egeria.mountainshares.us*
*Rebuild namespace: msjarvis-rebuild — 96 containers confirmed live*
*MountainShares Phase 0 beta: LIVE — Arbitrum One (chain 42161), 5 contracts on-chain*
