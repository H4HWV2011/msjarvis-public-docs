
*Figure 00-5. Full production pipeline flow, March 25, 2026. ★ marks changes confirmed March 25: consciousness pipeline ACTIVE; dict.lower() guard in gateway patched; jarvis-rag-server port corrected to 8003→8016; Chroma v2 API in use throughout.*

---

## 00.7 Service Count History

| Date | Services | Notable Addition / Change |
|---|---|---|
| Initial deployment | 79 | Core stack |
| Pre-March 14, 2026 | 82 | Phase 1.45 community memory services added |
| March 14, 2026 | 83 | psychological-rag (port 8006) promoted to production |
| March 19, 2026 | 84 | Spatial infrastructure services finalized (3D GiST, materialized views) |
| March 20, 2026 | 85 (reported) | gbim_query_router (port 7205) — landowner belief layer live |
| March 21–22, 2026 | 83 (verified) | 3 orphaned containers added to docker-compose.yml; verified compose count: 83 |
| March 22, 2026 (afternoon) | 83 compose + 3 systemd | Caddy (8443), jarvis-auth (8055), cloudflared added as systemd services. Public URL https://egeria.mountainshares.us confirmed live. |
| March 22–25, 2026 | 83 compose + 3 systemd | Consciousness pipeline sprint: jarvis-woah, jarvis-consciousness-bridge, jarvis-rag-server patched and confirmed active. No compose count change. |

---

## 00.8 System Health Snapshot — March 25, 2026 ★ UPDATED

| Metric | Value | Verified |
|---|---|---|
| Total services (Docker Compose–managed) | 83 | March 21–22, 2026 |
| External systemd services | 3 (Caddy, jarvis-auth, cloudflared) | March 22, 2026 |
| Public HTTPS URL | https://egeria.mountainshares.us | March 22, 2026 — confirmed live |
| Pipeline speed (single-user, GPU) | ~100–107s | March 22, 2026 (three confirmed runs: 99.6s, 105.9s, 106.5s) |
| LLM models contributing | 21/21 | March 22, 2026 |
| **Pre-flight gate** | **24 PASS 0 FAIL ★** | **March 22, 2026 — re-validated March 25, 2026; no regression** |
| Output BBB block rate | 0% (log+passthrough) | March 22, 2026 — was 31%, disabled for tuning |
| Community resources verified | 52 | March 22, 2026 (50 Kanawha + 2 Fayette) |
| Active red team tokens | 4 | March 22, 2026 (carrie_admin ×2, hayden_test ×2) |
| LLM ensemble ports | 8201–8222 | March 22, 2026 |
| GBIM beliefs (gbimbeliefnormalized) | 5,416,522 | March 20, 2026 |
| — of which: landowner beliefs ★ | 20,593 | March 20, 2026 |
| — of which: spatial/facility beliefs | 5,395,929 | March 20, 2026 |
| GBIM worldview entities (ChromaDB) | 5,416,521 | March 20, 2026 |
| autonomous_learner items | 21,181+ | March 20, 2026 (~288/day) |
| psychological_rag items | 968 | March 20, 2026 |
| msjarvis_docs items | 2,348 | March 22, 2026 |
| **ChromaDB collections (confirmed)** | **31 ★** | **March 25, 2026 (up from 13 at March 22 audit)** |
| **ChromaDB total items** | **6,665,093 ★** | **March 25, 2026** |
| **ChromaDB API version** | **v2 active ★ — v1 returns 410** | **March 25, 2026** |
| **Consciousness pipeline** | **ACTIVE ★** | **March 25, 2026 — Chroma 200, WOAH stub live, bridge patched** |
| **RAG pipeline (`jarvis-rag-server`)** | **PARTIALLY ACTIVE ★** | **March 25, 2026 — /query confirmed; embedder v2 fix pending restart** |
| Canonical buildings (wv_buildings) | 2,120,976 | March 19, 2026 |
| Building-parcel records (MV) | 7,354,707 | March 19, 2026 |
| Address coverage (verified situs) | 97.17% | March 19, 2026 |
| msjarvisgis tables | 501 | March 20, 2026 |
| msjarvisgis size | 91 GB | March 20, 2026 |
| Embedding dimensions (all collections) | 384 | all-minilm:latest |
| Worldview | eq1 | All production beliefs |
| ChromaDB host port | 8002 (127.0.0.1:8002->8000/tcp) | March 22, 2026 |
| Redis host port | 6380 (127.0.0.1:6380->6379/tcp) | March 22, 2026 |
| Redis async job status key | 'complete' (NOT 'done') | March 22, 2026 |
| Caddy version | 2.6.2 (Ubuntu apt package) | March 22, 2026 — NOT xcaddy; no caddy-ratelimit; no forward_auth |
| MountainShares services (8080–8084) | ❌ NOT DEPLOYED | March 22, 2026 — all return HTTP 000 |
| BBB output filter port | 8016 (same as input) | March 22, 2026 — port 8017 does not exist |
| BBB output filter mode | log+passthrough (not blocking) | March 22, 2026 |
| LM Synthesizer identity guard | Active — 3 layers, no leakage confirmed | March 25, 2026 |
| Cloudflare Tunnel UUID | 42ef9893-f4df-4cc5-8881-bb55b995e022 | March 22, 2026 |
| Auth service token TTL | 30 days | March 22, 2026 |

---

## 00.9 Sprint Progress Log

| Sprint | Dates | Items Closed | Status |
|---|---|---|---|
| Landowner belief sprint | March 20, 2026 | gbim_query_router promoted; 20,593 landowner beliefs ingested; mvw_gbim_landowner_spatial materialized | ✅ Complete |
| Red team hardening sprint | March 21–22, 2026 | Orphaned containers added to compose; systemd services (Caddy, jarvis-auth, cloudflared) deployed; public URL live; 0.0.0.0→127.0.0.1 hardening; 3 immutable containers protected; BBB bbbCheckVerdict wired; MS docs ingested (2,348 items); first public end-to-end test PASS | ✅ Complete |
| Consciousness pipeline restoration sprint | March 22–25, 2026 | WOAH service fixed (stdlib stub, qualia-net); Chroma v2 API migration (bridge + rag-server); consciousness bridge patched (3 fixes); RAG server port/endpoint/schema corrected; gateway dict.lower() guard added; end-to-end chat confirmed ACTIVE with Hilbert entity recall and prior session context; two commits merged to main | ✅ Closed — RAG embedder restart pending |

---

*Last updated: 2026-03-25 (evening), Carrie Kidd (Mamma Kidd), Mount Hope WV*
*Public URL: https://egeria.mountainshares.us*
