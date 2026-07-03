(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ cd /mnt/spiritual_drive/msjarvis-rebuild

echo '=== 1. FIND ALL CONSCIOUSNESS/CHAT ROUTES IN CODEBASE ==='
find . -type f \( -name '*.py' -o -name '*.service' -o -name '*.conf' -o -name '*.json' -o -name '*.md' \) \
  -not -path '*/.git/*' -print0 \
| xargs -0 grep -RInE 'consciousnesschat|consciousness/chat|consciousness_chat|/process|BRIDGE_69DGM_URL|127\.0\.0\.1:8000|127\.0\.0\.1:9998|127\.0\.0\.1:[0-9]{4}' \
| head -n 300

echo '=== 2. FIND ALL LOCAL SERVICES LISTENING ON APP PORTS ==='
sudo lsof -iTCP -sTCP:LISTEN -n -P \
| grep -E ':(7[0-9]{3}|8[0-9]{3}|9[0-9]{3}) ' \
| sort -k9,9 -k1,1

echo '=== 3. PROBE EVERY LISTENING APP PORT FOR FASTAPI OPENAPI/HEALTH ==='
for port in $(sudo lsof -iTCP -sTCP:LISTEN -n -P | awk '/:(7[0-9]{3}|8[0-9]{3}|9[0-9]{3}) /{split($9,a,":"); print a[2]}' | sort -nu); do
  for path in /openapi.json /docs /health /consciousnesschat /consciousness/chat /process; do
    code=$(curl -s -o /tmp/probe.$$ -w '%{http_code}' "http://127.0.0.1:${port}${path}")
temd/system /lib/systemd/system 2>/dev/null | head -n 300s|rag|bridge' /etc/sys
=== 1. FIND ALL CONSCIOUSNESS/CHAT ROUTES IN CODEBASE ===
./SESSION_CLOSE_COMMANDS.md:51:curl http://127.0.0.1:8008/health
./docs/API-OVERVIEW.md:26:- `GET /infrastructure/nohup/processes`:
./NEXT_SESSION_QUICK_START.md:20:curl -s -X POST http://127.0.0.1:8050/chat \
./NEXT_SESSION_QUICK_START.md:47:curl -s http://127.0.0.1:8050/health | python3 -m json.tool
./auth_api.patched.py:62:    "http://127.0.0.1:3000",
./gateway8050_inline.py:7:JARVIS_PROD_CHAT = "http://127.0.0.1:8008/chat"
./ask_gis.py:6:BASE_URL = "http://127.0.0.1:8055/gis_rag"
./thesis/07-rag-pipeline-and-routers.md:44:curl -X POST http://127.0.0.1:8050/chat/sync \
./thesis/39-operational-evaluation.md:170:| **Implemented and verified (2026-03-15)** | **79 containers operational** — commit `b90f9ff` "March 15 2026 COMPLETE: All 79 containers operational - PRODUCTION READY." **22/22 LLM proxies HTTP 200** (all llm1–llm22 responding; previously 21/22). **Three previously missing containers built and deployed March 15:** `jarvis-hippocampus`, `jarvis-toroidal-geometry`, `jarvis-psychology-services` (confirmed running at **127.0.0.1:8019**). **LM Synthesizer** operational at port **8001** (Phase 3.5 of 9-phase pipeline). **ChromaDB** restored at port **8000** — `chroma_data` Docker volume created March 15; previously crashed due to missing volume. **`psychological_rag_domain`** operational at **127.0.0.1:8006** (confirmed with `chroma_data` volume). **Three-database PostgreSQL architecture confirmed:** `msjarvis` (port 5433, 8 MB, 6 tables, 5,416,521 GBIM entities, 80 epochs, 206 source layers); `gisdb` (port 5433, PostGIS, 13 GB, 39 tables, 993 ZCTA centroids); `jarvis-local-resources-db` (port 5435, community resources). **GBIM temporal confidence decay deployed** — all 5,416,521 entities carry `last_verified`, `confidence_decay`, `needs_verification` metadata; 100% flagged `needs_verification=TRUE` at launch (expected baseline). **BBB 7-filter stack** — `SafetyMonitor` false-positive on community terms resolved (word-boundary regex fix March 15); `SteganographyDetection`, `TruthVerification`, `ContextAwareness` deployed. **End-to-end 9-phase pipeline test PASSED March 15:** query "What community resources are available in Fayette County, WV?" — all 9 phases approved, wall-clock time **349.87 seconds**. |
./thesis/39-operational-evaluation.md:227:- PostgreSQL: `127.0.0.1:5432` (database `msjarvisgis` at Feb 28; superseded by 3-DB architecture — see §39.2b)
./thesis/39-operational-evaluation.md:286:| `jarvis-psychology-services` | Not deployed | **✅ Deployed at 127.0.0.1:8019** |
./thesis/39-operational-evaluation.md:289:| `psychological_rag_domain` | Unavailable | **✅ Operational at 127.0.0.1:8006** |
./thesis/37-constitutional-principles-service.md:98:| **Implemented now** | `jarvis-constitutional-guardian` confirmed running at **127.0.0.1:8091** (docker compose ps). FastAPI service with full CORS support. 6 principle groups grounded in U.S. Constitution: First Amendment (speech, religion, assembly, petition), Fourth Amendment (privacy, security), Fifth Amendment (due process, property, self-incrimination), Fourteenth Amendment (equal protection, due process), General Welfare (Article I §8, Preamble), Tenth Amendment (community sovereignty, anti-extraction). 15+ specific principles with metadata (id, title, description, status, origin, scope). Version 2026-02-17.2-USC confirmed active. Integration with BBB (port **8016**): Constitutional Guardian checked FIRST before traditional filters; if blocked → immediate rejection, skip all other filters. Integration with Unified Gateway (port **8001**): defense-in-depth, checks Constitutional Guardian before sending to BBB. Persistent audit log at `data/constitutional_audit/constitutional_audit.jsonl`: JSON Lines format, survives container restarts, volume-mounted. Role-specific enforcement: external_corporation (strictest), community_member (standard), user (standard), system (logged). PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as validation source for community sovereignty and anti-extraction principles. Full API: `/constitutional/check`, `/constitutional/status`, `/constitutional/principles`, `/constitutional/versions`, `/constitutional/audit`, `/constitutional/audit/stats`, `/constitutional/transparency`. Production testing: 150+ checks, 23 blocked (~15%), 127 allowed, most violated principle `10a-no-extraction` (15 blocks), response time <100ms. |
./thesis/09-darwin-godel-machines.md:199:to `POST {woah_url}/process` with a short timeout. If WOAH returns HTTP 200 and valid JSON, the response is inspected for a weight field such as `hierarchical_weight` (defaulting to a mid‑range value when missing). If the resulting identity weight exceeds a configured threshold (for example, `>= 0.75`), the content is promoted to the I‑container via `_promote_to_i_container`, which appends:
./thesis/00-overview.md:68:| **Vector Memory** | **ChromaDB** | `127.0.0.1:8000` (containerized) — `gbim_worldview_entities`: **5,416,521 entities** |
./thesis/00-overview.md:72:| **Public Gateway** | **Cloudflare Tunnel** | `cloudflared-msjarvis.service` on `127.0.0.1:20242` |
./thesis/20-first-stage-evaluation.md:65:| **Implemented now** | `background_rag_store` confirmed operational in `jarvis-main-brain` (port **8050**): runs as a background task after every `/chat` response, performs a near-duplicate check via RAG server `/search` with `top_k=1`, and writes accepted interactions into `ms_jarvis_memory` ChromaDB collection with `bg_<ISO8601>` ids, `type: "background"` metadata, and `services: ["llm20production"]`. **`ms_jarvis_memory` is append-only in the current deployment**: deduplication is advisory — it affects the skip logic and downstream reuse, not the write path. Repeated identical messages produce distinct entries with separate timestamps. `truthverdict` from BBB (port **8016**) attached to every `UltimateResponse`, providing `valid`, `confidence`, and `principalreasons` signals. `/curator/background` endpoint on main brain (port **8050**) providing stable, auditable view of background store contents. BBB four-filter pipeline (`EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`, `ThreatDetection`) operational as pre-filter gate. Identity truth validators (`normalize_identity`, `TruthValidator`) applied on every response. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as protected destination for validated content. Confirmed in 2026-02-15 case study: `bg_<ISO8601>` entries in `ms_jarvis_memory` verified via Python REPL and `/curator/background` query (see Chapter 9 §9.3.5 and Chapter 17 §17.6). |
./thesis/20-first-stage-evaluation.md:85:**Preserve opportunity.** In the current deployment, user conversations that pass safety checks are queued for background handling and written into the `ms_jarvis_memory` semantic store in ChromaDB (confirmed running via `jarvis-chroma` at **127.0.0.1:8002**), where they can later contribute to autonomous learning, clustering, or case-study analysis. Only validated, high-confidence content is promoted to PostgreSQL `msjarvisgis` trusted stores.
./thesis/30-aapcappE-scraper-and-corpus.md:76:| **Implemented now** | `jarvis-aaacpe-rag` confirmed running at **127.0.0.1:8032** (docker compose ps). Endpoints operational: `GET /` (status and document count), `GET /health`, `POST /search` (params: query, top_k), `POST /ingest`. `jarvis-aaacpe-scraper` confirmed running at **127.0.0.1:8033**. Endpoints operational: `GET /` (scraper status), `GET /health` (last scrape time and document count), `POST /scrape_now`, `POST /ingest_test`. Shared Docker volume `aaacpe-cultural-data` mounted at `/data` in both containers. ChromaDB collection `appalachian_cultural_intelligence` in PersistentClient at `/data/aaacpe_chroma`. Total documents as of current deployment: 10 — 7 base cultural intelligence documents (core values, anti-patterns, emergency protocol, example utility assistance, heritage mode, geographic context integration, professional warmth) + 3 scraped test documents (WV broadband initiative, Appalachian Heritage Month events, Fayette County historic preservation funding). Document categories confirmed: `values`, `anti_pattern`, `examples`, `emergency`, `heritage`, `scraped_content`. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as authoritative source for validating cultural context against West Virginia community data. `aaacperag` registered in SERVICES registry in `jarvis-main-brain` (port **8050**) as `http://jarvis-aaacpe-rag:8032`. Both services on `qualia-net` Docker network. |
./thesis/30-aapcappE-scraper-and-corpus.md:112:- Confirmed running at **127.0.0.1:8032** (docker compose ps)
./thesis/30-aapcappE-scraper-and-corpus.md:119:- Confirmed running at **127.0.0.1:8033** (docker compose ps)
./thesis/30-aapcappE-scraper-and-corpus.md:208:      - 127.0.0.1:8032:8032
./thesis/30-aapcappE-scraper-and-corpus.md:223:      - 127.0.0.1:8033:8033
./thesis/30-aapcappE-scraper-and-corpus.md:325:In the current deployment, the AaaCPE Cultural Intelligence System is realized as two confirmed running services — `jarvis-aaacpe-rag` (**127.0.0.1:8032**) and `jarvis-aaacpe-scraper` (**127.0.0.1:8033**) — sharing the `aaacpe-cultural-data` Docker volume with a `appalachian_cultural_intelligence` ChromaDB collection containing 10 confirmed documents across six categories: `values`, `anti_pattern`, `examples`, `emergency`, `heritage`, and `scraped_content`, all validated against PostgreSQL `msjarvisgis` (port 5432, 91 GB, 501 tables, 5.4M+ verified GBIM beliefs) for West Virginia community accuracy.
./thesis/24-feedback-into-broader-layers.md:66:| **Implemented now** | `ms_jarvis_memory` ChromaDB collection: confirmed written after every `/chat` call via `background_rag_store` in `jarvis-main-brain` (port **8050**); entries have `bg_<ISO8601>` ids, `type: "background"`, `services` metadata. Confirmed 2026-02-15 (Chapter 9 §9.3.5, Chapter 17 §17.6). `jarvis-chroma` confirmed running at **127.0.0.1:8002**; primary `chroma_db` directory approximately 12 GB with confirmed collections including `jarvis_consciousness`, `spiritual_wisdom`, `ms_jarvis_memory`, `autonomous_learning`, `learning_suggestions`, `research_history`, `appalachian_english_corpus`. PostgreSQL `msjarvisgis` confirmed at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as the authoritative source for spatial and institutional feedback. GeoDB sync scripts confirmed present on disk: `sync_geodb_to_chromadb.py`, `extract_all_chromadb_to_gis.py`, `vectorize_gis_to_chromadb.py`, `recover_chromadb_to_gisgeodb.py`. Corresponding sync logs confirmed: `chromadb_v2_to_gis_sync.log`, `extract_all_chromadb_to_gis.log`, `vectorize_gis_to_chromadb.log`. `getdatabasehealth` endpoint on secured gateway: returns JSON with `status`, `database` (e.g. `GISGEODBACTIVE`), `identityelements`, `candidates`, `integrity`, timestamps. `getidentitycandidates` endpoint: returns candidate identity statements with `importance` and DGM scores. Main-brain status endpoints and `/curator/background` confirmed operational 2026-02-15. `TruthFilterBBBValidator` records verification decisions into `ueididentity` and `ueidaccessaudit` tables. BBB `barrier_stats` counters (`total_filtered`, `total_blocked`, `pass_rate`) live at port **8016**. `masterspatialknowledge.csv` confirmed with `accesslevelrequired` and `isproprietary` fields. Historical "System Verification Report" outputs confirmed present on disk. |
./thesis/24-feedback-into-broader-layers.md:86:**Long-term semantic and spatial memory.** In the current deployment, `jarvis-chroma` runs at **127.0.0.1:8002** with a primary `chroma_db` directory of approximately 12 GB containing confirmed collections. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) serves as the authoritative source for all spatial and institutional data. GeoDB sync scripts and their logs document how ChromaDB collections and PostgreSQL GeoDB spatial datasets are updated and reconciled. These structures are written to by `background_rag_store` after every `/chat` call and by dedicated sync pipelines.
./thesis/24-feedback-into-broader-layers.md:112:**PostgreSQL msjarvisgis — the authoritative ground truth.** In the current deployment, PostgreSQL 16 at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs in `gbimbeliefnormalized`) serves as the source of truth for all spatial, institutional, and community data. All RAG collections are ultimately sourced from or validated against PostgreSQL tables. GeoDB sync scripts ensure ChromaDB embeddings stay synchronized with PostgreSQL spatial features.
./thesis/24-feedback-into-broader-layers.md:114:**Additional confirmed ChromaDB collections.** In the current deployment, `jarvis-chroma` at **127.0.0.1:8002** hosts a primary `chroma_db` of approximately 12 GB with confirmed collections including `jarvis_consciousness` (over 11,000 items), `autonomous_learning`, `learning_suggestions`, `research_history`, `spiritual_wisdom`, `appalachian_english_corpus`, and numerous `geodb_*` collections (e.g. `geodb_structurepointsnorth_samb_2003_utm83`, `geodb_wvgistcbuildingfootprints`, `geodb_floodplainstructuresatrisk_usarmycorpsofengineers_200303_utm83`). These collections embed both domain knowledge and introspective artifacts sourced from PostgreSQL `msjarvisgis`, turning container- and service-level outputs into persistent semantic memory. Additional ChromaDB instances listed in code (`persistent/chroma`, `persistent/chroma_primary`, `services/prod_chroma_db`, `services/rag_chroma_db`) are not all confirmed active in the current deployment.
./thesis/10-woah-weighted-optimization-hierarchy.md:64:- `POST /process` accepts structured JSON input with:
./thesis/10-woah-weighted-optimization-hierarchy.md:100:The `POST /process` response includes all of these values alongside the original content and metadata.
./thesis/10-woah-weighted-optimization-hierarchy.md:120:  - Records each new weight vector coming out of `POST /process`.
./thesis/10-woah-weighted-optimization-hierarchy.md:126:This is implemented as a separate Python module that exposes functions such as `record_sample`, `step_population`, and `update_policy`. The WOAH algorithms service calls into this module on every `/process` request:
./thesis/10-woah-weighted-optimization-hierarchy.md:192:- Direct `/process` calls returning structural, strong‑identity weights for key MountainShares content.
./thesis/34-spiritual-root-and-mother-carrie.md:84:| **Implemented now** | `MotherCarrieProtocol` and `MultiTraditionSpiritualFilter` Python classes confirmed implemented **inside `jarvis-blood-brain-barrier`** (`0.0.0.0:8016`, confirmed running). These are routing/emphasis/audit patterns within the BBB service — **not a separate container or service**. `mother_carrie_enabled` boolean flag: accepted as parameter by `MultiTraditionSpiritualFilter.filter()` and `MotherCarrieProtocol.evaluate_with_protocol()`; controls stricter care-focused routing (minimum care score 0.3 vs. standard mode) — **not a mystical mode**. `SpiritualFilter = MultiTraditionSpiritualFilter` class alias confirmed, providing full backward compatibility for services using legacy Christian-centered pattern matching. Audit log (`protocol.audit_log`) confirmed: records `timestamp`, `mother_carrie_enabled`, `care_score`, `traditions_count`, `passed` for each evaluation; accessible via `protocol.get_audit_log(limit=100)` and exportable via `protocol.export_audit_log(filepath)`. Care-focused scoring confirmed: 0.0–1.0 scale, +0.1 per care value detected, +0.05 per community pattern validated against PostgreSQL GBIM, +0.05 for harm acknowledgment. Multi-tradition corpus scaffold confirmed on disk: `knowledge_pdfs/spiritual_texts/` directory structure for 70+ traditions. **3 traditions populated with substantive texts** (Christian: 2 Bible translations, 12.1 MB; Islamic: 2 Quran translations, 2.9 MB; Hindu: 1 Bhagavad Gita, 175 KB — total ~15 MB, 5 files). Three CSV inventory files confirmed: `spiritual_traditions_target.csv` (5.5 KB, master inventory of 70+ traditions), `spiritual_pdfs_manifest.csv` (12 KB, 72 files listed), `spiritual_pdfs_inventory_by_tradition.csv` (3.3 KB, per-tradition statistics with `has_content` flag). `generate_spiritual_inventories.py` script confirmed on disk. `MotherCarrieProtocol.check_tradition_availability()` confirmed returning `available`, `file_count`, `total_files`, `status` ("populated" or "placeholder_only"). Fallback mode confirmed: 8 core traditions (Christian, Islamic, Hindu, Buddhist, Jewish, Indigenous American, Humanist, Secular Ethics) used when CSV files not accessible. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as ground truth for validating community patterns and care values. |
./thesis/34-spiritual-root-and-mother-carrie.md:160:**Thematic memory collections.** In the current deployment, `jarvis-chroma` (**127.0.0.1:8002**, confirmed running) includes `spiritual_wisdom` and `appalachian_english_corpus` collections (confirmed present in the approximately 12 GB `chroma_db`). These are given greater prominence when spiritual modes are active and validated against PostgreSQL GBIM for community appropriateness.
./thesis/34-spiritual-root-and-mother-carrie.md:162:**Spatial focus.** In the current deployment, `jarvis-gis-rag` (**127.0.0.1:8004**, confirmed running) queries PostgreSQL GeoDB and `geodb_*` ChromaDB collections enable geospatial layers highlighting particular West Virginia communities to be prioritized when spiritual modes are active and queries touch on community well-being or stewardship.
./thesis/25-consciousness-coordinator-and-services.md:93:| **Implemented now** | Full analytical path operational in every `/chat` call: intake via `jarvis-main-brain` (port **8050**) → BBB filtering (port **8016**) → PostgreSQL-sourced RAG context (ports **8003-8005**) → 20-LLM ensemble synthesis (port **8008**) → judge pipeline (ports **7230-7233**) → `normalize_identity` + `TruthValidator` → `background_rag_store` into `ms_jarvis_memory` ChromaDB (port **8002**, append-only) → `truthverdict` on `UltimateResponse`. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as authoritative source for all RAG collections and truth validation. Meaning-oriented services confirmed running: I-Containers (port **8015**, `icontainers-identity` ACTIVE in 2026-02-15 response), Qualia Engine (port **8017**), NBB Master (port **8018**), Mother Protocols (port **4000**), Psychology services (port **8019**), Psychological RAG (port **9006**), Temporal Consciousness (port **7007**). GeoDB sync scripts and logs confirmed present. Health endpoints (`getdatabasehealth`, `getidentitycandidates`, `/curator/background`) operational. For canonical execution sequence see **Chapter 17**. |
./thesis/25-consciousness-coordinator-and-services.md:145:**PostgreSQL `msjarvisgis` — authoritative ground truth.** In the current deployment, PostgreSQL 16 at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs in `gbimbeliefnormalized`) serves as the source of truth for all spatial, institutional, and community data. All RAG collections are sourced from or validated against PostgreSQL tables. GeoDB sync scripts ensure ChromaDB embeddings stay synchronized with PostgreSQL spatial features. Writes to PostgreSQL require passing higher validation thresholds than ChromaDB writes.
./thesis/27-web-research-and-autonomy.md:76:| **Implemented now** | `jarvis-autonomous-learner` confirmed running at **127.0.0.1:8425** with ONNX sentence-embedding model cached on host, FastAPI HTTP interface, configurable `learning_queue`, and restart policy `unless-stopped`. ChromaDB (`jarvis-chroma`, port **8002**) with collections `autonomous_learner`, `ms_jarvis_memory`, `conversation_history`, `jarvis_consciousness`, `spiritual_wisdom` confirmed active and growing. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as authoritative ground truth for topic selection and validation. I-containers service (port **8015**) providing `GET /next-learning-topic` endpoint querying ChromaDB for knowledge gaps across 15 Appalachian community domains validated against PostgreSQL GBIM. RAG gateways operational: general RAG **8003**, spiritual/GBIM RAG **8005** (queries PostgreSQL-sourced collections), GIS RAG **8004** (queries PostgreSQL GeoDB), WV-entangled gateway **8010**. Web research gateways providing structured results with domain policies, rate limits, geographic filters. Learner conducts embedding operations, ChromaDB insertions, topic selections, web-gateway calls with deduplication. System verification scripts report autonomous learner, web research, and RAG servers as "CONFIRMED OPERATIONAL" with collection counts and response times. Logging captures embedding operations, PostgreSQL validation, ChromaDB writes, topic selections, web calls. |
./thesis/29-psychological-safeguards-and-pia.md:108:| **Implemented and verified (March 15, 2026)** | `jarvis-psychology-services` confirmed running at **127.0.0.1:8019** (deployed March 15, commit `b90f9ff`). Exposes `/psychological_assessment` accepting a query and returning structured fields: `psychological_assessment`, `therapeutic_guidance`, `emotional_support`, `wellbeing_recommendations`, `evidence_based_approaches`. **Phase 3 psychology pre-assessment is now active on every production 9-phase pipeline request** (Chapter 17), including severity classification and crisis indicator check — confirmed in 349.87s end-to-end benchmark. `psychological_rag_domain` confirmed running at **127.0.0.1:8006** (port corrected from 9006 to 8006 as of March 15 containerized deployment). Exposes `/search` and `/add_document` for a curated psychological corpus (968 items: therapy, mindfulness, trauma, depression, anxiety, social support). ChromaDB `psychological_rag` collection confirmed present (port 8000, `chroma_data` Docker volume restored March 15 — previously unavailable due to missing volume mount). PostgreSQL `msjarvis` at **127.0.0.1:5433** (5,416,521 verified GBIM entities, 80 epochs, 206 source layers) as ground truth for validating psychological guidance against West Virginia community context. **BBB 7-filter pipeline** (expanded from 4 to 7 filters as of March 15): `EthicalFilter`, `SpiritualFilter`, `SafetyMonitor` (word-boundary regex fix March 15), `ThreatDetection`, `SteganographyDetection` (March 15), `TruthVerification` (March 15), `ContextAwareness` (March 15) at **0.0.0.0:8016** — functions as Phase 1.4 live gate on every request. `normalize_identity` and `TruthValidator` enforce prohibitions on anthropomorphic claims and identity confusion validated against PostgreSQL `msjarvis` GBIM on every `ultimatechat` response (Chapter 17, Chapter 22). `truthverdict` attached to every `UltimateResponse` with `correct_identity`, `correct_creator`, `relationship_clear` booleans. |
./thesis/29-psychological-safeguards-and-pia.md:140:In the current deployment, psychological guidance materials are curated in the `psychological_rag` collection within ChromaDB (**127.0.0.1:8000**, `chroma_data` Docker volume, restored March 15) and served via `psychological_rag_domain` (**127.0.0.1:8006**, confirmed running March 15), with validation against PostgreSQL `msjarvis` for West Virginia community context.
./thesis/29-psychological-safeguards-and-pia.md:229:In the current deployment (March 15, 2026, commit `b90f9ff`), psychological safeguards are realized through two confirmed running services — `jarvis-psychology-services` (**127.0.0.1:8019**, deployed March 15) and `psychological_rag_domain` (**127.0.0.1:8006**, containerized March 15) — a curated psychological corpus in ChromaDB (**127.0.0.1:8000**, `chroma_data` volume, 968 items in `psychological_rag` collection), validation against PostgreSQL `msjarvis` (port 5433, 5,416,521 GBIM entities) for West Virginia community context, the BBB 7-filter pipeline at **0.0.0.0:8016** as the primary Phase 1.4 live safety gate, and `normalize_identity` plus `TruthValidator` validated against PostgreSQL applied to every `ultimatechat` response.
./thesis/33-llm-ensemble-and-judges.md:127:| **Implemented now** | `jarvis-20llm-production` (`ai_server_20llm_PRODUCTION.py`) confirmed running at **127.0.0.1:8008**. `jarvis-semaphore` proxy confirmed running at **127.0.0.1:8030**. **21 active expert model proxy containers** (`llm1-proxy` through `llm22-proxy`) confirmed running at **127.0.0.1:8201–8222** (22 proxies total; StarCoder2 at 8207 returns 0-char responses on community queries — 21 reliably active). Judge pipeline (`jarvis-judge-pipeline`) confirmed running at internal ports **7230–7233** (corrected from erroneous 7239, March 16, 2026) with all 4 judges: `judge-truth` **7230**, `judge-consistency` **7231**, `judge-alignment` **7232**, `judge-ethics` **7233**. **Judge pipeline updated March 16, 2026: evaluates consensus answer ONLY** — `raw_responses` dump from all 21 models no longer sent to judges; judge pipeline time reduced from ~85–100s to ~60–86s. **Phase 3.75 (Final LLM Polish via llm22-proxy) ELIMINATED March 18, 2026** — merged into Phase 3.5 LM Synthesizer single Ollama call with Ms. Jarvis persona injection; saves ~40s per query. **Phase 1.45 community memory retrieval added March 17, 2026** — `autonomous_learner` ChromaDB collection (21,181 records, growing ~288/day) queried via `all-minilm:latest` (384-dim) before LLM ensemble; top-5 memories prepended to `enhanced_message`. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as ground truth for truth judge validation and alignment judge community values checking. `POST /evaluate` endpoint on judge pipeline operational. `/cached_expert_responses` endpoint on `jarvis-20llm-production` operational. `asyncio.gather()` parallel judge execution confirmed. `judge-pipeline` consciousness layer in `UltimateResponse` confirmed. Fallback behavior confirmed: if judge pipeline unavailable, main brain marks layer `status: "error"` or `"skipped"`, uses 21-LLM answer as-is, assigns `consensus_score: 0.8`, sets `expert_count: 0` to signal degraded operation. All 79 containers fully compose-managed via Docker Compose v5.1.0; all `build:` directives converted to `image:` references. **Verified performance (March 18, 2026):** consensus score 0.975 on identity questions; 21/21 expert participation; all four judge verdicts pass (Truth=1.0, Consistency=1.0, Alignment=1.0, Ethics=0.9); end-to-end processing time **~436 seconds** (optimized from 532s baseline) for full pipeline including Phase 1.45 community memory, 21-model ensemble, consensus-only judge pipeline, and merged Phase 3.5 voice delivery. |
./thesis/33-llm-ensemble-and-judges.md:147:**Task execution (experts).** In the current deployment, **21 reliably active expert models** (22 proxies total; StarCoder2 at port 8207 frequently returns 0-character responses on community-domain queries) are exposed behind lightweight proxy containers (`llm1-proxy` through `llm22-proxy`, confirmed running at **127.0.0.1:8201–8222**). For each consensus request, all 21 models receive the same composite prompt — which already includes Phase 1.45 community memory from `autonomous_learner` (21,181 records via `all-minilm:latest` 384-dim), PostgreSQL-sourced RAG context from `jarvis-spiritual-rag` (port **8005**, queries GBIM collections), PostgreSQL GeoDB context from `jarvis-gis-rag` (port **8004**), container-state hints, and orchestration directives — and generate independent candidate answers. The proxy architecture prevents Ollama overload. In the current deployment, model proxies are dispatched **sequentially** rather than in true parallel to prevent Ollama resource exhaustion on the CPU-only inference host (Legion 5, 29 GB RAM, `size_vram: 0` on all models).
./thesis/41-test-harness-and-continuous-validation.md:181:curl -s http://127.0.0.1:8050/health | python3 -m json.tool
./thesis/41-test-harness-and-continuous-validation.md:189:curl -s -X POST http://127.0.0.1:8050/chat \
./thesis/41-test-harness-and-continuous-validation.md:209:curl -s -X POST http://127.0.0.1:8050/chatlight/async \
./thesis/41-test-harness-and-continuous-validation.md:221:curl -s http://127.0.0.1:8050/chatlight/status/JOB_ID | python3 -m json.tool
./thesis/41-test-harness-and-continuous-validation.md:233:curl -s -X POST http://127.0.0.1:8015/process \
./thesis/41-test-harness-and-continuous-validation.md:244:curl -s -X POST http://127.0.0.1:8101/process \
./thesis/41-test-harness-and-continuous-validation.md:257:curl -s http://127.0.0.1:8019/health | python3 -m json.tool
./thesis/41-test-harness-and-continuous-validation.md:265:curl -s -X POST http://127.0.0.1:8019/psychological_assessment \
./thesis/41-test-harness-and-continuous-validation.md:276:curl -s -X POST http://127.0.0.1:8006/search \
./thesis/41-test-harness-and-continuous-validation.md:289:curl -s http://127.0.0.1:8011/health | python3 -m json.tool
./thesis/41-test-harness-and-continuous-validation.md:297:curl -s -X POST http://127.0.0.1:8011/chat \
./thesis/41-test-harness-and-continuous-validation.md:310:curl -s http://127.0.0.1:8001/health | python3 -m json.tool
./thesis/41-test-harness-and-continuous-validation.md:318:curl -s -X POST http://127.0.0.1:8001/synthesize \
./thesis/41-test-harness-and-continuous-validation.md:378:curl -s http://127.0.0.1:9000/health | python3 -m json.tool
./thesis/41-test-harness-and-continuous-validation.md:386:curl -s http://127.0.0.1:8030/health | python3 -m json.tool
./thesis/41-test-harness-and-continuous-validation.md:417:curl -s -X POST http://127.0.0.1:8050/chat \
./thesis/41-test-harness-and-continuous-validation.md:473:curl -s -X POST http://127.0.0.1:8050/chat \
./thesis/41-test-harness-and-continuous-validation.md:496:curl -s http://127.0.0.1:8005/health | python3 -m json.tool
./thesis/41-test-harness-and-continuous-validation.md:504:curl -s -X POST http://127.0.0.1:8005/search \
./thesis/41-test-harness-and-continuous-validation.md:515:curl -s http://127.0.0.1:8004/health | python3 -m json.tool
./thesis/41-test-harness-and-continuous-validation.md:523:curl -s -X POST http://127.0.0.1:8004/search \
./thesis/02-ms-jarvis-gbim.md:93:A full ingest into the `gbim_worldview_entities` collection on the live ChromaDB HTTP server (`127.0.0.1:8002`) was launched on the evening of March 13, 2026 using a streaming batch pipeline (batch size 5,400) and completed on March 14, 2026.
./thesis/02-ms-jarvis-gbim.md:163:The ChromaDB HTTP server at `127.0.0.1:8002` hosts the following active collections:
./thesis/11-llm-fabric-of-ms-jarvis.md:97:| **Implemented and verified** | `jarvis-main-brain` → **127.0.0.1:8050** (confirmed). `jarvis-ollama` → **127.0.0.1:11434** (confirmed). `jarvis-wv-entangled-gateway` → **127.0.0.1:8010** (confirmed). `jarvis-spiritual-rag` (GBIM / worldview RAG) → **127.0.0.1:8005** (confirmed; earlier plan documents used 8103). `jarvis-gis-rag` → **127.0.0.1:8004** (confirmed). `jarvis-rag-server` (general RAG) → **127.0.0.1:8003** (confirmed; ONNX model downloaded and ChromaDB integration working). `jarvis-lm-synthesizer` → **127.0.0.1:8001** (confirmed; calls `jarvis-ollama:11434/api/generate` directly with `llama3.1:latest`; Ms. Egeria Jarvis persona prompt injected; previously called `jarvis-roche-llm` — corrected March 18, 2026). `psychological_rag_domain` → **127.0.0.1:8006** (confirmed; port corrected from 9006). `jarvis-psychology-services` → **127.0.0.1:8019** (confirmed; Phase 3 active on every production request). PostgreSQL `msjarvis` → **127.0.0.1:5433** (5,416,521 GBIM entities, 80 epochs, 206 source layers, temporal decay metadata). PostgreSQL `gisdb` → **127.0.0.1:5433** (13 GB PostGIS, 39 tables, 993 ZCTA centroids). `jarvis-local-resources-db` → **127.0.0.1:5435** (community resources, confirmed). ChromaDB → **127.0.0.1:8000** (`chroma_data` Docker volume; `psychological_rag` 968 items; `autonomous_learner` 21,181 items). `nbb_woah_algorithms` → **127.0.0.1:8104** host → internal 8010 (confirmed). `jarvis-woah` → **127.0.0.1:7012** (confirmed). `jarvis-blood-brain-barrier` → **0.0.0.0:8016** (confirmed; 7-filter stack; `truth_score` null guard added March 18; fail-open on HTTP 500 added March 18). `jarvis-20llm-production` → **127.0.0.1:8008** (confirmed; 21 active models / 22 proxies; BakLLaVA permanently disabled); wall-clock consensus ~320-360s. Judge pipeline → evaluates consensus answer only; raw_responses dump eliminated; ~60-86s (was ~85-100s). `jarvis-semaphore` → **127.0.0.1:8030** (confirmed; `max_concurrent: 4`; requires float `timeout`). `llm1-proxy` through `llm22-proxy` → **127.0.0.1:8201-8222** (21 active; llm11/BakLLaVA permanently disabled). `jarvis-hippocampus` → **127.0.0.1:8011**. `jarvis-69dgm-bridge` → **127.0.0.1:9000** (confirmed; Phase 7, 23 connectors × 3 stages). Judge services confirmed: `jarvis-judge-truth` 7230, `jarvis-judge-consistency` 7231, `jarvis-judge-alignment` 7232, `jarvis-judge-ethics` 7233. `jarvis-constitutional-guardian` → **127.0.0.1:8091** (confirmed). `jarvis-fifth-dgm` → **127.0.0.1:4002** (confirmed). `jarvis-redis` → **127.0.0.1:6380** (confirmed). `/chat/async` + `/chat/status/{job_id}` + `/chat/cancel/{job_id}` + `/chat/cancel/all` confirmed (Redis-backed, 30-min TTL, true asyncio task cancellation). `/chatlight/async` + `/chatlight/status/{job_id}` confirmed (tag `v2026.03.02-chatlight-async-working`). `normalize_identity()` confirmed producing Ms. Jarvis identity voice. Phase 1.45 ChromaDB semantic community memory retrieval confirmed — `all-minilm:latest` 384-dim, `autonomous_learner` collection, top-5 results prepended to `enhanced_message`. All 79 containers fully compose-managed. End-to-end benchmark: ~436s (full pipeline with community memory enrichment). |
./thesis/11-llm-fabric-of-ms-jarvis.md:114:In the current deployment, models are served by Ollama inside the `jarvis-ollama` container at **127.0.0.1:11434**. As of March 18, 2026, **21 of 22 LLM proxy containers are active**. BakLLaVA (llm11-proxy, port 8211) is permanently disabled due to CLIP load issues. The disable is enforced programmatically in `ai_server_20llm_PRODUCTION.py`:
./thesis/11-llm-fabric-of-ms-jarvis.md:175:**Main Brain API — 127.0.0.1:8050 (`jarvis-main-brain`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:178:**PostgreSQL `msjarvis` — 127.0.0.1:5433.**
./thesis/11-llm-fabric-of-ms-jarvis.md:181:**PostgreSQL `gisdb` — 127.0.0.1:5433.**
./thesis/11-llm-fabric-of-ms-jarvis.md:184:**PostgreSQL `jarvis-local-resources-db` — 127.0.0.1:5435.**
./thesis/11-llm-fabric-of-ms-jarvis.md:187:**LM Synthesizer — 127.0.0.1:8001 (`jarvis-lm-synthesizer`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:190:**General RAG Server — 127.0.0.1:8003 (`jarvis-rag-server`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:193:**GIS RAG — 127.0.0.1:8004 (`jarvis-gis-rag`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:196:**Spiritual Root / GBIM RAG — 127.0.0.1:8005 (`jarvis-spiritual-rag`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:199:**Psychological RAG — 127.0.0.1:8006 (`psychological_rag_domain`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:202:**WV-Entangled Gateway — 127.0.0.1:8010 (`jarvis-wv-entangled-gateway`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:205:**Hippocampus — 127.0.0.1:8011 (`jarvis-hippocampus`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:208:**I-Containers — 127.0.0.1:8015 (`jarvis-i-containers`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:214:**Psychology Services — 127.0.0.1:8019 (`jarvis-psychology-services`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:217:**20-LLM Production Ensemble — 127.0.0.1:8008 (`jarvis-20llm-production`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:220:**Semaphore Proxy — 127.0.0.1:8030 (`jarvis-semaphore`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:223:**LLM Proxies — 127.0.0.1:8201–8222.**
./thesis/11-llm-fabric-of-ms-jarvis.md:227:`nbb_woah_algorithms` at **127.0.0.1:8104** (host) → internal 8010. `jarvis-woah` at **127.0.0.1:7012**.
./thesis/11-llm-fabric-of-ms-jarvis.md:232:**Constitutional Guardian — 127.0.0.1:8091.** See Chapter 37.
./thesis/11-llm-fabric-of-ms-jarvis.md:234:**Fifth DGM — 127.0.0.1:4002 (`jarvis-fifth-dgm`).** See Chapter 9.
./thesis/11-llm-fabric-of-ms-jarvis.md:236:**69-DGM Cascade — 127.0.0.1:9000 (`jarvis-69dgm-bridge`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:239:**Autonomous Learner — 127.0.0.1:8425 (`jarvis-autonomous-learner`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:242:**ChromaDB — 127.0.0.1:8000 (`jarvis-chroma`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:245:**Redis — 127.0.0.1:6380 (`jarvis-redis`).**
./thesis/11-llm-fabric-of-ms-jarvis.md:248:**Ollama Runtime — 127.0.0.1:11434 (`jarvis-ollama`).**
./thesis/12-neurobiological-architecture.md:76:| **Implemented and verified** | `jarvis-neurobiological-master` running, internal port **8018**, code `ms_jarvis_neurobiological_master.py` **v2.0.0** (fully rewritten 2026-03-01). Routes live: `GET /health`, `GET /systems/status`, `POST /process`, `POST /biological_process`, `POST /neural_process`. Full 4/4 integrated pipeline BBB → I-Containers → Qualia Engine → Consciousness Bridge verified operational at **~300ms** wall clock (2026-03-01, tag `v2026.03.01-neuro-pipeline-4-4`). All four stages return `status: "healthy"` and `responsive: true` in `/systems/status`. `jarvis-blood-brain-barrier` confirmed running at **0.0.0.0:8016**; **7-filter stack operational as of March 15** (EthicalFilter, SpiritualFilter, SafetyMonitor with word-boundary regex fix, ThreatDetection, SteganographyDetection, TruthVerification, ContextAwareness). `jarvis-qualia-engine` confirmed running, internal port **8017**; `/experience` endpoint operational; emotional resonance and meaning extraction confirmed working. `jarvis-i-containers` confirmed running, internal port **8015**; `/process` endpoint operational; correct schema `{"message": <input>, "userid": "neurobiological_master"}` confirmed. `jarvis-consciousness-bridge` confirmed running, actual listen port **8018** (discovered via `/proc/net/tcp` hex decode: `0x1F52 = 8018`; compose declares 8020 but container binds 8018); `/chat` endpoint operational. `nbb-i-containers` confirmed running at **127.0.0.1:8101** (NBB prefrontal stack, called unconditionally at Phase 1 of 9-phase pipeline). `jarvis-hippocampus` confirmed running at **127.0.0.1:8011** (deployed March 15). `jarvis-brain-orchestrator` confirmed running at **127.0.0.1:17260** (internal 7260). PostgreSQL `msjarvis` confirmed at **127.0.0.1:5433** (5,416,521 GBIM entities, 80 epochs, 206 source layers; GBIM temporal decay deployed March 15). PostgreSQL `gisdb` confirmed at **127.0.0.1:5433** (13 GB PostGIS, 39 tables, 993 ZCTA centroids). `jarvis-local-resources-db` confirmed at **127.0.0.1:5435** (community resources, confirmed in March 15 end-to-end benchmark). ChromaDB confirmed at **127.0.0.1:8000** (`chroma_data` Docker volume, restored March 15). `jarvis-psychology-services` (port 8019) deployed March 15 — Phase 3 psychology pre-assessment now active on every production 9-phase pipeline request. `normalize_identity()` confirmed firing on live async chat path, producing identity-aware responses in Ms. Jarvis's voice (2026-03-02). |
./thesis/12-neurobiological-architecture.md:140:- `POST /process` — main entrypoint for integrated neurobiological processing
./thesis/12-neurobiological-architecture.md:141:- `POST /biological_process` and `POST /neural_process` — alias endpoints that normalize different input field names and internally delegate to `/process`
./thesis/12-neurobiological-architecture.md:167:If the BBB approves, the master calls `jarvis-i-containers` at `/process` with the **corrected schema** (fixed 2026-03-01):
./thesis/12-neurobiological-architecture.md:176:An earlier version of the master incorrectly sent `{"input": …, "require_dual_awareness": true}`, which caused a 422 validation error from the I-Containers service. The corrected schema is the permanent canonical form. The `icontainers-identity` layer showed `status: "active"` in a live `UltimateResponse` on 2026-02-15 (see Chapter 9 §9.3.5). A second I-containers service, `nbb-i-containers`, runs at **127.0.0.1:8101** as part of the NBB stack and is called unconditionally at Phase 1 of every 9-phase pipeline request; its distinct role relative to `jarvis-i-containers` is documented in Chapter 25.
./thesis/12-neurobiological-architecture.md:215:Biologically, the hippocampus is critical for consolidating experiences into long-term memory. In the current deployment, the hippocampus metaphor is realized by `jarvis-hippocampus`, confirmed running at **127.0.0.1:8011** (deployed March 15, 2026, commit `b90f9ff`), which serves as a **conversation-level memory service** over ChromaDB (port 8000, `chroma_data` volume) and PostgreSQL `msjarvis` (port 5433, 5,416,521 verified GBIM beliefs with temporal decay metadata).
./thesis/12-neurobiological-architecture.md:229:The main brain (`jarvis-main-brain`, port **8050**) is the primary instance of this prefrontal pattern at the system level. The `jarvis-brain-orchestrator` (confirmed running, **127.0.0.1:17260**, internal 7260) provides a second orchestration layer. The `nbb-i-containers` NBB prefrontal cortex (port **8101**) is called unconditionally at Phase 1 of every 9-phase pipeline request (Chapter 17, §17.3 Step 1), providing pre-request cognitive planning before any content reaches the BBB, psychology pre-assessment, or LLM synthesis stages. The Neurobiological Master's `integrated_processing()` method is a fourth, narrower instance: it performs top-down gating and sequencing across BBB, I-Containers, Qualia Engine, and Consciousness Bridge.
./thesis/23-dual-tracks-meaning-and-analysis.md:79:| **Implemented now — analytical path (always runs in `ultimatechat`)** | `jarvis-20llm-production` at **127.0.0.1:8008** (confirmed running) as primary synthesis fabric; `jarvis-semaphore` proxy at **127.0.0.1:8030**; `llm1-proxy` through `llm22-proxy` at **127.0.0.1:8201–8222** (all confirmed). Judge services confirmed running: truth 7230, consistency 7231, alignment 7232, ethics 7233. `jarvis-gis-rag` at **127.0.0.1:8004** (confirmed, queries PostgreSQL GeoDB). `jarvis-spiritual-rag` at **127.0.0.1:8005** (confirmed, queries PostgreSQL-sourced GBIM collections; earlier plan listed 8103). `jarvis-blood-brain-barrier` at **0.0.0.0:8016** (confirmed). PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as source for all RAG collections. `TruthValidator` and `normalize_identity` applied to every response. `background_rag_store` into `ms_jarvis_memory` ChromaDB after every `/chat` call. `truthverdict` attached to every `UltimateResponse`. For the canonical execution sequence see **Chapter 17**. |
./thesis/23-dual-tracks-meaning-and-analysis.md:80:| **Implemented now — meaning-oriented services (confirmed running but not all wired into `ultimatechat`)** | `jarvis-i-containers` at **8015** (confirmed); `icontainers-identity` layer confirmed `status: "active"` in 2026-02-15 `UltimateResponse` (Chapter 9 §9.3.5). `jarvis-qualia-engine` at **8017** (confirmed). `jarvis-neurobiological-master` at **8018** (confirmed). `jarvis-fifth-dgm` at **4002** (confirmed). `nbb-i-containers` at **127.0.0.1:8101** (confirmed). `jarvis-psychology-services` at **127.0.0.1:8019** (confirmed). `psychological_rag_domain` at **127.0.0.1:9006** (confirmed). `jarvis-temporal-consciousness` at **7007** (confirmed). `jarvis-mother-protocols` at **4000** (confirmed). `nbb_woah_algorithms` at **127.0.0.1:8104** (confirmed). |
./thesis/23-dual-tracks-meaning-and-analysis.md:98:**The meaning-oriented family** includes neurobiological and consciousness-related components: Qualia Engine (`jarvis-qualia-engine`, port **8017**, confirmed running), I-Containers (`jarvis-i-containers`, port **8015**, confirmed running), Neurobiological Master (`jarvis-neurobiological-master`, port **8018**, confirmed running), Mother Protocols (`jarvis-mother-protocols`, port **4000**, confirmed running), temporal consciousness (`jarvis-temporal-consciousness`, port **7007**, confirmed running), NBB I-Containers (`nbb-i-containers`, **127.0.0.1:8101**, confirmed running), psychology services (`jarvis-psychology-services`, **127.0.0.1:8019**, confirmed running), and psychological RAG domain (`psychological_rag_domain`, **127.0.0.1:9006**, confirmed running). In the current deployment, a subset of these services respond with healthy status codes and are invoked in specific workflows and integration tests, but **not all are wired into the primary `ultimatechat` path**.
./thesis/23-dual-tracks-meaning-and-analysis.md:120:**What is confirmed running.** In the current deployment, the following meaning-oriented services are confirmed running: `jarvis-i-containers` (port **8015**), `jarvis-qualia-engine` (port **8017**), `jarvis-neurobiological-master` (port **8018**), `jarvis-mother-protocols` (port **4000**), `jarvis-temporal-consciousness` (port **7007**), `nbb-i-containers` (**127.0.0.1:8101**), `jarvis-psychology-services` (**127.0.0.1:8019**), and `psychological_rag_domain` (**127.0.0.1:9006**).
./thesis/22-identity-focused-retention.md:49:│  │  │    to /process (confirmed 2026-03-13)    │  │         │
./thesis/22-identity-focused-retention.md:79:| **Implemented and verified** | `normalize_identity` applied to every response in `jarvis-main-brain` (port **8050**, confirmed running): rewrites raw model outputs into the Ms. Egeria Jarvis persona, rejecting generic "I am just a language model" framings. `TruthValidator` encoding specific known facts (`correct_identity`, `correct_creator`, `relationship_clear`, `truth_score`) operational; results attached as `truthverdict` on every `UltimateResponse` (confirmed 2026-02-15, Chapter 9 §9.3.5). Canonical identity statements defined in configuration and identity-related endpoints: "I serve the community", "I learn and grow", "I speak truth", "I value ethics", "I help others evolve" — each annotated with `importance` values and diagnostic scores. Identity-tracking elements in active database and config-level stores with counts reported via health-style endpoints. `call_icontainers` confirmed as a **live HTTP implementation** as of **2026-03-13**: sends `POST /process` to `jarvis-i-containers` (port **8015**) with schema `{"message": ..., "userid": ...}` and appends the result as the `icontainers-identity` layer in `consciousness_layers`. Prior to 2026-03-13, `call_icontainers` was an empty stub returning `{}` — the I-Containers service was never actually called on the `ultimatechat` path. The fix was applied and confirmed during the 2026-03-13 remediation session (see Chapter 40 §40-B). `icontainers-identity` layer confirmed `status: "active"` in live `UltimateResponse` post-remediation, producing a real `root-self` ego entry (`jarvis-i-containers`, port **8015**, confirmed running; see Chapter 9 §9.3.5). `nbb-icontainers` layer also confirmed appended to `consciousness_layers` as of 2026-03-13, contributing to the 6-layer confirmed `UltimateResponse`. BBB four-filter pipeline (`EthicalFilter`, `SpiritualFilter`, `SafetyMonitor`, `ThreatDetection`) at port **8016** (confirmed running, wired 2026-03-13) enforcing identity constraints as a pre-filter gate on every request. `clean_response_for_display` expanded 2026-03-13 to strip paragraph-level model self-identification ("As LLaMA…", "As Mistral…", "As an AI…") before `normalize_identity` runs, ensuring identity voice is clean at both the inline and paragraph level. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as the ground truth anchor for identity validation and West Virginia community accountability. |
./thesis/22-identity-focused-retention.md:137:**I-container ego entries.** In the current deployment, `call_icontainers` is a **confirmed live HTTP implementation** as of **2026-03-13**, sending `POST /process` to `jarvis-i-containers` (port **8015**) with the canonical schema `{"message": ..., "userid": ...}`. The result is appended as the `icontainers-identity` layer in `consciousness_layers`. Prior to 2026-03-13, this function was an empty stub returning `{}` — the I-Containers service was never called on the `ultimatechat` path. The confirmed `root-self` entry from 2026-02-15 includes `egoboundaries`, `experientialprocessing`, `observerprocessing: "observer"`, and `metalevel: "ego-boundaries-v1"` (see Chapter 9 §9.3.5). A second I-Containers layer, `nbb-icontainers`, is also appended to `consciousness_layers` as of 2026-03-13, giving the live system 6 confirmed active consciousness layers. This is the most concrete artifact of the identity layer in live operation.
./thesis/16-blood-brain-barrier-and-safeguards.md:72:| **Implemented and verified (2026-03-18)** | `jarvis-blood-brain-barrier` confirmed running at **0.0.0.0:8016** (`docker compose ps`). Exposes `GET /health`, `POST /filter`, and `POST /truth`. Four sub‑filters confirmed operational with verified method signatures: `EthicalFilter.filter(text)`, `SpiritualFilter.filter(text)`, `SafetyMonitor.check(text)`, `ThreatDetection.detect_threats(text)`. `POST /truth` endpoint returns `{"valid": bool, "confidence": float, "principal_reasons": [str]}`. `barrier_stats` counters (`total_filtered`, `total_blocked`, `pass_rate`) live. `truth_verdict` attached to every `UltimateResponse` from main brain (port 8050). Output guard on generated text active in main brain pipeline via `apply_output_guards_async` calling `/filter` with 8.0s timeout (fixed 2026‑03‑02). **Fail-open behavior confirmed (2026-03-18):** BBB output guard returns content unchanged on HTTP 500 responses — the pipeline does not halt on BBB errors. **`truth_score` null guard confirmed (2026-03-18):** BBB orchestrator includes null guard for `truth_score` field — `KeyError` on missing `truth_score` resolved. BBB invoked as first stage in Neurobiological Master `integrated_processing()` pipeline. `MotherCarrieProtocol` implemented as a routing/emphasis/audit pattern **inside** BBB; `mothercarrieenabled` is a boolean flag controlling stricter care-focused routing — not a separate service and not a mystical mode. `jarvis-psychology-services` confirmed running at **127.0.0.1:8019**. `psychological_rag_domain` confirmed running at **127.0.0.1:8006** (restored March 15, 2026; backed by `chroma_data` Docker volume on ChromaDB port 8000). PostgreSQL `msjarvis` (port 5433, GBIM beliefs, 8 MB, 6 tables) and `gisdb` (port 5433, PostGIS spatial, 13 GB, 39 tables) are the protected memory stores. ChromaDB (port 8000, `gbim_worldview_entities` 5,416,521 entities) is the protected semantic memory store. **BBB ethical filter blocking 'certainly': BY DESIGN** — the ethical filter correctly blocks unverified specific claims. This is not a false positive; it is the constitutional layer enforcing epistemic honesty. |
./thesis/16-blood-brain-barrier-and-safeguards.md:153:In the current deployment, variants of the barrier implement screening behavior that can either block content outright or strip it before passing it onwards. Earlier pre‑integration services exposed `/process` and returned either the original content or an empty string plus a `filtered: True` flag depending on the combined verdict of ethical, spiritual, and safety filters, ensuring that blocked material did not reach downstream components even when the call chain continued.
./thesis/16-blood-brain-barrier-and-safeguards.md:197:In the current deployment, psychological guidance is implemented across two confirmed running services. `psychological_rag_domain` runs at **127.0.0.1:8006** (restored March 15, 2026; backed by `chroma_data` Docker volume on ChromaDB port 8000; `psychological_rag` collection — 968 items) and exposes `/search` and `/add_document` for a curated psychological corpus that includes therapy, mindfulness, trauma, depression, anxiety, and social‑support materials. `jarvis-psychology-services` runs at **127.0.0.1:8019** and exposes endpoints including `/psychological_assessment`, which accepts a query and returns structured responses containing `psychological_assessment`, `therapeutic_guidance`, `emotional_support`, `wellbeing_recommendations`, and `evidence_based_approaches`.
./thesis/40-system-audit-and-operational-validation.md:206:> **Resolution (March 18, 2026):** The canonical ChromaDB instance is `jarvis-chroma` at **127.0.0.1:8000** with `chroma_data` Docker volume (restored March 15, 2026). All collections use **384-dimensional vectors** (`all-minilm:latest`) — the `nomic-embed-text` model (768-dim) is incompatible and must not be used. Active collections confirmed as of March 18: `ms_jarvis_memory`, `mountainshares_knowledge`, `episodic_index`, `conversation_history`, `autonomous_learner` (21,181 records, growing ~288/day; queried at Phase 1.45 on every `/chat` call), `psychological_rag` (968 records), `gbim_worldview_entities`, `gis_wv_benefits`, `appalachian_cultural_intelligence` (5 records), `GBIM_sample_rows` (5,000 records), `GBIM_sample` (3 records), `msjarvis-smoke` (1 record). The `_DummyCollection` error that previously blocked semantic retrieval is resolved by the `all-minilm:latest` implementation. The `services-chroma-1` and `msjarvis-rebuild-chroma-1` instances are not part of the current production stack.
./thesis/40-system-audit-and-operational-validation.md:308:| 5 | `call_icontainers()` | Function was an empty stub returning `{}` — I-Containers service was never actually called | Replaced with live `httpx` POST to `jarvis-i-containers:8015/process` with correct schema `{"message": ..., "userid": ...}` | ✅ `icontainers-identity` layer active |
./thesis/35-swarm-functions-and-eternal-watchdogs.md:107:| **Implemented now** | 22-slot LLM ensemble (`jarvis-20llm-production`, port **8008**) with 20 actively responding models verified via warm-cache testing. Four-tier organization: TINY (2 models), SMALL (3 models), MEDIUM (8 active + 1 intentionally disabled), LARGE (8 models). `asyncio.Semaphore(3)` concurrency gate confirmed preventing Ollama saturation. `MAX_CONCURRENT_CHATS=2` session gate confirmed on `jarvis-main-brain`. Ollama container memory limit raised to 20 GB, confirmed stable. 240-second timeout floor confirmed. BakLLaVA intentionally disabled via DNS-poisoned endpoint (`http://llmXX-bakllava-disabled/generate`) producing instant failure, consuming no Ollama resources. `VERIFYANDTEST.sh` eternal watchdog confirmed operational: 32/32 services healthy, 22/22 LLM proxies responding, 84 Docker containers running, 26 Ollama models available, PostgreSQL connection verified. Redis DynamicPortService confirmed managing NBB container health registration with 5 instances heartbeating. BBB (`jarvis-blood-brain-barrier`, port **8016**): 319 requests filtered, 0 blocked, 0 constitutional violations. 69-DGM bridge (port **9000**): 69 connectors loaded, architecturally authoritative validation on all main-brain-routed responses. Psychology alignment layer (`jarvis-psychology-services`, port **8019**) confirmed running pre-ensemble assessment. NBB subconscious: 7/8 containers healthy via consciousness bridge. Consciousness bridge (`jarvis-consciousness-bridge`) confirmed as mandatory infrastructure. Brain orchestrator (`jarvis-brain-orchestrator`) confirmed as continuous coordinator. PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) as ground truth validation source. ChromaDB (`jarvis-chroma`, port **8002**) confirmed as operational history ingestion target for VERIFYANDTEST.sh logs. Verified performance baseline: 20/22 models responding, judge consistency 0.975, warm cache ~52s, cold load ~163s. Host configuration: 29 GB RAM total, 13 GB available under production load, 73 GB model storage at `/mnt/ssd2/msjarvis_secondary/models`. |
./thesis/35-swarm-functions-and-eternal-watchdogs.md:294:Each record contains `host`, `port`, `status`, `deployment`, `health_endpoint`, `started`, and `last_heartbeat` fields. The pituitary gland container, for example, registers with `status: healthy` and a dynamic port (33239 in the February 2026 instance), mapped externally as `7008/tcp → 127.0.0.1:8108`. This Redis-backed registration pattern allows NBB containers to restart with new ephemeral ports without breaking the watchdog fabric.
./thesis/35-swarm-functions-and-eternal-watchdogs.md:342:**PostgreSQL msjarvisgis integration.** PostgreSQL `msjarvisgis` at **127.0.0.1:5432** (91 GB, 501 tables, 5.4M+ verified GBIM beliefs) serves as ground truth for BBB validation, 69-DGM cascade verification, RAG context sourcing, and VERIFYANDTEST.sh connection monitoring.
./package-lock.json:6116:    "node_modules/process-nextick-args": {
./package-lock.json:6118:      "resolved": "https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz",
./hp_antisurveillance_guardian_client.py:4:GUARDIAN_URL = "http://127.0.0.1:8091/constitutional/check"
./ask_gis_near_oakhill.py:5:BASE_URL = "http://127.0.0.1:8055/gis_rag"
./bootstrap_gbim_beliefs_eq1.py:24:    # Local Postgres on 127.0.0.1:5432, msjarvisgis DB, postgres user
./test_end_to_end_woah_fifthdgm.py:5:GATEWAY_URL = "http://127.0.0.1:8001"
./test_end_to_end_woah_fifthdgm.py:6:FIFTH_DGM_URL = "http://127.0.0.1:4002"
./test_end_to_end_woah_fifthdgm.py:7:WOAH_URL = "http://127.0.0.1:7012"
./test_end_to_end_woah_fifthdgm.py:44:    print("\n=== 4) Direct WOAH /process (same content) ===")
./test_end_to_end_woah_fifthdgm.py:49:    r = requests.post(f"{WOAH_URL}/process", json=woah_payload, timeout=30)
./gisgeodbstorage.py:8:    # Chroma is exposed on host 127.0.0.1:8002 -> container:8000
./msjarviswoahalgorithms.py:19:@app.post("/process", response_model=WOAHResponse)
./MARCH16_2026_STARTUP.md:21:- 69-DGM endpoint: /consciousnesschat, payload: question/user_id
./services/ms_jarvis_production_chat.py:82:RAG_URL = "http://127.0.0.1:8003"                 # RAG server (POST /search, /store_conversation)
./services/ms_jarvis_production_chat.py:83:CONSENSUS_URL = "http://127.0.0.1:18018"      # consensus / LLM gateway (not yet wired)
./services/ms_jarvis_production_chat.py:84:BBB_URL = "http://127.0.0.1:8016"                         # BBB proxy on host
./services/add_new_consciousness_services.py:20:        '"fractal": "/analyze",\n        "mother_protocols": "/guide",\n        "temporal_consciousness": "/process",'
./services/working_full_pipeline.py:48:                "http://localhost:7006/process",
./services/port_9000_69dgm_bridge.py:4:Intercepts /consciousness/chat, routes through all 69 validators,
./services/port_9000_69dgm_bridge.py:28:BRIDGE_69DGM_URL = os.getenv(
./services/port_9000_69dgm_bridge.py:29:    "BRIDGE_69DGM_URL",
./services/port_9000_69dgm_bridge.py:30:    "http://127.0.0.1:8000/consciousnesschat",  # default internal DNS + port
./services/port_9000_69dgm_bridge.py:69:        "Intercepts /consciousness/chat, routes through 69 DGM validators, "
./services/port_9000_69dgm_bridge.py:103:    Orchestrator is expected to be listening on localhost:9999/process.
./services/port_9000_69dgm_bridge.py:110:                os.getenv("ORCH_69_URL", "http://127.0.0.1:9998") + "/process",  # Orchestrator's processing endpoint
./services/port_9000_69dgm_bridge.py:143:    Expects a FastAPI endpoint at BRIDGE_69DGM_URL that returns
./services/port_9000_69dgm_bridge.py:147:        f"🔗 Calling 69-DGM RAG bridge at {BRIDGE_69DGM_URL} for user={userid}"
./services/port_9000_69dgm_bridge.py:152:                BRIDGE_69DGM_URL,
./services/port_9000_69dgm_bridge.py:273:# FastAPI endpoint for /consciousness/chat on port 9000
./services/port_9000_69dgm_bridge.py:275:@app.post("/consciousness/chat", response_model=ChatOut)
./services/port_9000_69dgm_bridge.py:276:async def consciousness_chat(req: ChatIn):
./services/port_9000_69dgm_bridge.py:294:        "rag_bridge_url": BRIDGE_69DGM_URL,
./services/port_9001_ui_DIRECT.py:121:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",
./services/qualia_unified_orchestrator_69dgm_ACTIVE.py:108:@app.post("/process")
./services/msjarvis_icontainers.py:26:@app.post("/process", response_model=IContainersResponse)
./services/ms_jarvis_neurobiological_master.py:138:                    f"{services['i_containers']}/process",
./services/ms_jarvis_neurobiological_master.py:217:@app.post("/process")
./services/ms_jarvis_neurobiological_master.py:249:    """Alias endpoint: /neural_process -> /process"""
./services/neuro_subconscious.py:18:@app.post("/process")
./services/pituitary_gland.py:8:@app.post("/process")
./services/pituitary_gland.py:22:    # Run THIS file's FastAPI app so /process and /health exist
./services/msjarvis-rebuild-nbb_blood_brain_barrier-1_ms_jarvis_consciousness_bridge.py:9:@app.post("/process")
./services/icontainers_fastapi.py:44:        resp = await client.post(f"{NBB_ICONTAINERS_URL}/process", json=payload)
./services/icontainers_fastapi.py:133:@app.post("/process", response_model=IContainerResponse)
./services/jarvis-i-containers_icontainers_fastapi.py:44:        resp = await client.post(f"{NBB_ICONTAINERS_URL}/process", json=payload)
./services/jarvis-i-containers_icontainers_fastapi.py:133:@app.post("/process", response_model=IContainerResponse)
./services/master_chat_orchestrator_v5_consciousness.py:218:                    f"{CONSCIOUSNESS_SERVICES['consciousness_bridge']}/process",
./services/consciousness_with_egeria_voice.py:31:@app.post("/consciousness/chat")
./services/consciousness_with_egeria_voice.py:32:async def consciousness_chat(
./services/port_9001_ui_FIXED.py:132:                "http://127.0.0.1:9998/process",
./services/integrate_complete_architecture.py:48:                f"{BRAIN_ORCHESTRATOR_URL}/process",
./services/port_9000_chat_wrapper_69dgm.py:8:Port 9001 Wrapper - Intercepts /consciousness/chat calls to port 9000
./services/port_9000_chat_wrapper_69dgm.py:34:@app.post("/consciousness/chat")
./services/port_9000_chat_wrapper_69dgm.py:47:                os.getenv("ORCH_69_URL", "http://127.0.0.1:9998") + "/process",
./services/port_9000_chat_wrapper_69dgm.py:61:                    f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",
./services/ms_jarvis_autonomous_learner_optimized.py:50:        self.rag_url = "http://127.0.0.1:8103/search"
./services/patch_fractal.py:6:@app.post("/process")
./services/patch_fractal.py:8:    """Alias endpoint: /process -> /analyze"""
./services/patch_fractal.py:25:    print("✅ Added /process endpoint to Fractal")
./services/patch_fractal.py:27:    print("⚠️  /process already exists in Fractal")
./services/web_page_ingest.py:17:RAG_STORE_URL = os.getenv("RAG_STORE_URL", "http://127.0.0.1:8003/store")
./services/msjarvis-rebuild-nbb_qualia_engine-1_ms_jarvis_consciousness_bridge.py:9:@app.post("/process")
./services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:95:                f"{BRAIN_ORCHESTRATOR_URL}/process",
./services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:198:@app.post("/process", response_model=ProcessResponse)
./services/neurobiologicalbrain/woah_algorithms/service/ms_jarvis_consciousness_bridge.py:237:    """Simplified chat endpoint that wraps /process."""
./services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:95:                f"{BRAIN_ORCHESTRATOR_URL}/process",
./services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:198:@app.post("/process", response_model=ProcessResponse)
./services/neurobiologicalbrain/i_containers/service/ms_jarvis_consciousness_bridge.py:237:    """Simplified chat endpoint that wraps /process."""
./services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:95:                f"{BRAIN_ORCHESTRATOR_URL}/process",
./services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:198:@app.post("/process", response_model=ProcessResponse)
./services/neurobiologicalbrain/spiritual_root/service/ms_jarvis_consciousness_bridge.py:237:    """Simplified chat endpoint that wraps /process."""
./services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:95:                f"{BRAIN_ORCHESTRATOR_URL}/process",
./services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:198:@app.post("/process", response_model=ProcessResponse)
./services/neurobiologicalbrain/prefrontal_cortex/service/ms_jarvis_consciousness_bridge.py:237:    """Simplified chat endpoint that wraps /process."""
./services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:95:                f"{BRAIN_ORCHESTRATOR_URL}/process",
./services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:198:@app.post("/process", response_model=ProcessResponse)
./services/neurobiologicalbrain/pituitary_gland/service/ms_jarvis_consciousness_bridge.py:237:    """Simplified chat endpoint that wraps /process."""
./services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:95:                f"{BRAIN_ORCHESTRATOR_URL}/process",
./services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:198:@app.post("/process", response_model=ProcessResponse)
./services/neurobiologicalbrain/subconscious/service/ms_jarvis_consciousness_bridge.py:237:    """Simplified chat endpoint that wraps /process."""
./services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:95:                f"{BRAIN_ORCHESTRATOR_URL}/process",
./services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:198:@app.post("/process", response_model=ProcessResponse)
./services/neurobiologicalbrain/mother_carrie_protocols/service/ms_jarvis_consciousness_bridge.py:237:    """Simplified chat endpoint that wraps /process."""
./services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:95:                f"{BRAIN_ORCHESTRATOR_URL}/process",
./services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:198:@app.post("/process", response_model=ProcessResponse)
./services/neurobiologicalbrain/spiritual_maternal_integration/service/ms_jarvis_consciousness_bridge.py:237:    """Simplified chat endpoint that wraps /process."""
./services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:95:                f"{BRAIN_ORCHESTRATOR_URL}/process",
./services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:198:@app.post("/process", response_model=ProcessResponse)
./services/neurobiologicalbrain/heteroglobulin_transport/service/ms_jarvis_consciousness_bridge.py:237:    """Simplified chat endpoint that wraps /process."""
./services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:95:                f"{BRAIN_ORCHESTRATOR_URL}/process",
./services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:198:@app.post("/process", response_model=ProcessResponse)
./services/neurobiologicalbrain/consciousness_containers/service/ms_jarvis_consciousness_bridge.py:237:    """Simplified chat endpoint that wraps /process."""
./services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:68:    description="""Thorough transparency_mode for H4H Research: Full visibility into consciousness layers (I-Containers, WOAH analysis_depth_7, fractal DGM), base metalAI (23 Ollama LLMs, GPU mgmt), biometric/wallet (UEID security proxies), GIS (1002 rows: Mount Hope lat 37.9 Fayette WV community_research to heritage_source_ref Damascus/Edward I/Strong Puritan cultural heritage), perpetual storage (ChromaDB/Redis RAG), 30+ microservices (no blackbox). Examples: /gis/query?location=Mount Hope → Biblical ties; /consciousness/chat?message=Damascus to WV roots → GIS-prepended WOAH analysis. Archive 8014 disabled.""",
./services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:229:@app.post("/consciousness/chat", tags=["Consciousness"])
./services/ms_jarvis_unified_gateway_v4.3.ORIGINAL_SWAGGER.py:240:            f"http://localhost:{WOAH_PORT}/process",
./services/dgm_orchestrator.py:120:@app.post("/process_full")
./services/dgm_orchestrator.py:199:            ("/process_full", {"input": req.message, "require_dual_awareness": True}),
./services/dgm_orchestrator.py:200:            ("/process",      {"message": req.message, "user_id": req.userid}),
./services/ADDITIONAL_SERVICES_FINAL.py:13:    {'name': 'main', 'url': 'http://localhost:7003/process', 'method': 'POST'},
./services/ADDITIONAL_SERVICES_FINAL.py:14:    {'name': 'main', 'url': 'http://localhost:7012/process', 'method': 'POST'},
./services/ADDITIONAL_SERVICES_FINAL.py:86:    {'name': 'main', 'url': 'http://localhost:7008/process', 'method': 'POST'},
./services/ADDITIONAL_SERVICES_FINAL.py:87:    {'name': 'main', 'url': 'http://localhost:7011/process', 'method': 'POST'},
./services/ADDITIONAL_SERVICES_FINAL.py:88:    {'name': 'main', 'url': 'http://localhost:7013/process', 'method': 'POST'},
./services/comprehensive_url_fix.py:20:    if 'localhost:8004' in line or '127.0.0.1:8004' in line:
./services/comprehensive_url_fix.py:27:    if 'localhost:8004' in line or '127.0.0.1:8010' in line:
./services/comprehensive_url_fix.py:34:    if 'localhost:8015' in line or '127.0.0.1:8015' in line:
./services/comprehensive_url_fix.py:41:    if 'localhost:4002' in line or '127.0.0.1:4002' in line:
./services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:74:    description="""Thorough transparency_mode for H4H Research: Full visibility into consciousness layers (I-Containers, WOAH analysis_depth_7, fractal DGM), base metalAI (23 Ollama LLMs, GPU mgmt), biometric/wallet (UEID security proxies), GIS (1002 rows: Mount Hope lat 37.9 Fayette WV community_research to heritage_source_ref Damascus/Edward I/Strong Puritan cultural heritage), perpetual storage (ChromaDB/Redis RAG), 30+ microservices (no blackbox). Examples: /gis/query?location=Mount Hope → Biblical ties; /consciousness/chat?message=Damascus to WV roots → GIS-prepended WOAH analysis. Archive 8014 disabled.""",
./services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
./services/ms_jarvis_unified_gateway_v4.3.CONSTITUTIONAL_BACKUP.py:284:            f"http://localhost:{WOAH_PORT}/process",
./services/hp_antisurveillance_guardian_client.py:4:GUARDIAN_URL = "http://127.0.0.1:8091/constitutional/check"
./services/test_end_to_end_woah_fifthdgm.py:5:GATEWAY_URL = "http://127.0.0.1:8001"
./services/test_end_to_end_woah_fifthdgm.py:39:    r = requests.get("http://127.0.0.1:4002/consciousness_stats", timeout=5)
./services/test_end_to_end_woah_fifthdgm.py:42:    print("\n=== 4) Direct WOAH /process (same content) ===")
./services/test_end_to_end_woah_fifthdgm.py:47:    r = requests.post("http://127.0.0.1:7012/process", json=woah_payload, timeout=30)
./services/ms_jarvis_command_orchestrator.py:38:@app.post("/consciousness/chat")
./services/port_9001_ui_MYSQL_PROD.py:173:            r = await client.post(f"http://127.0.0.1:9000/consciousness/chat?userid=user&message={message}", timeout=10.0)
./services/ms_jarvis_email_identity_verifier.py:92:@app.post("/process_registration_email", response_model=VerificationResponse)
./services/gbim-router/app/assertion_client.py:4:ASSERTION_GATEWAY_URL = os.environ.get("ASSERTION_GATEWAY_URL", "http://127.0.0.1:8009")
./services/infrastructure_endpoints.py:25:    @app.get("/infrastructure/nohup/processes", tags=["Infrastructure-Nohup"])
./services/msjarvis_bbb_proxy.py:19:                f"{NEURO_MASTER_URL}/process",
./services/ms_jarvis_conversational_gateway_4022.py:76:@app.post("/consciousness/chat")
./services/ms_jarvis_conversational_gateway_4022.py:77:async def consciousness_chat(userid: str = Query("user"), message: str = Query(...)):
./services/ms_jarvis_command_orchestrator_v5_backup.py:48:@app.post("/consciousness/chat")
./services/ms_jarvis_i_containers_FIXED.py:16:@app.post("/process")
./services/neuro_i_containers.py:18:@app.post("/process")
./services/integrate_full_brain.py:43:                    f"{self.neuro_url}/process",
./services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:230:@app.post("/consciousness/chat", tags=["Consciousness"])
./services/ms_jarvis_unified_gateway_v4.3.pre_manifest.backup.py:241:            f"http://localhost:{WOAH_PORT}/process",
./services/ms_jarvis_fractal_consciousness.py:395:@app.post("/process")
./services/ms_jarvis_fractal_consciousness.py:397:    """Alias endpoint: /process -> /analyze"""
./services/port_9001_ui_WITH_CONVERSATIONS.py:221:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",
./services/ms_jarvis_consciousness_complete.py:128:async def consciousness_chat(request: ChatRequest):
./services/ms_jarvis_consciousness_complete.py:176:                f"{WOAH_URL}/process",
./services/fractal_adapter.py:11:@app.post("/process")
./services/fractal_adapter.py:13:    """Adapter: /process -> /analyze"""
./services/dgm_bridge.py:211:@app.post("/process", response_model=OrchestratorResponse)
./services/neuro_consciousness_containers.py:18:@app.post("/process")
./services/ms_jarvis_i_containers_service.py:282:@app.post("/process_full")
./services/ms_jarvis_i_containers_service.py:293:@app.post("/process")
./services/ms_jarvis_paddleocr_processor.py:177:@app.post("/process_id", response_model=IDInfo)
./services/fix_chroma_url.py:14:content = content.replace('127.0.0.1:8010', 'jarvis-chroma:8010')
./services/wire_qualia_to_port8001.py:26:        new_lines.append(f"{indent}        'http://localhost:7008/process',\n")
./services/performance_optimization_analyzer.py:352:                        "Increase worker threads/processes",
./services/ms_jarvis_consciousness_bridge.py:199:@app.post("/process", response_model=ProcessResponse)
./services/ms_jarvis_consciousness_bridge.py:238:    """Simplified chat endpoint that wraps /process."""
./services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:241:@app.post("/consciousness/chat", tags=["Consciousness"])
./services/ms_jarvis_unified_gateway_v4.3.BEFORE_69DGM_INTEGRATION.py:252:            f"http://localhost:{WOAH_PORT}/process",
./services/ms_jarvis_unified_gateway_v4.3.20251124.py:74:    description="""Thorough transparency_mode for H4H Research: Full visibility into consciousness layers (I-Containers, WOAH analysis_depth_7, fractal DGM), base metalAI (23 Ollama LLMs, GPU mgmt), biometric/wallet (UEID security proxies), GIS (1002 rows: Mount Hope lat 37.9 Fayette WV community_research to heritage_source_ref Damascus/Edward I/Strong Puritan cultural heritage), perpetual storage (ChromaDB/Redis RAG), 30+ microservices (no blackbox). Examples: /gis/query?location=Mount Hope → Biblical ties; /consciousness/chat?message=Damascus to WV roots → GIS-prepended WOAH analysis. Archive 8014 disabled.""",
./services/ms_jarvis_unified_gateway_v4.3.20251124.py:268:@app.post("/consciousness/chat", tags=["Consciousness"])
./services/ms_jarvis_unified_gateway_v4.3.20251124.py:284:            f"http://localhost:{WOAH_PORT}/process",
./services/phase1_integration.py:39:                    f"http://localhost:{self.qualia_port}/process",
./services/phase1_integration.py:74:@app.post("/process_emotion")
./services/port_9001_ARCHITECTURE_CORRECT.py:31:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",
./services/port_9001_ui_wrapper.py:130:                f"http://127.0.0.1:9998/process",
./services/port_9001_ui_MYSQL.py:198:                f"http://127.0.0.1:9000/consciousness/chat?userid={userid}&message={message}",
./services/ms_jarvis_consciousness_enhancement_production.py:51:OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
./services/ms_jarvis_consciousness_enhancement_production.py:62:                    "http://127.0.0.1:4010/consensus",
./services/ms_jarvis_fifth_dgm_orchestrator.psychology_patched.py:156:                        f"{woah_url}/process",
./services/ms_jarvis_toroidal_consciousness.py:177:@app.post("/process")
./services/neuro_prefrontal_cortex.py:18:@app.post("/process")
./services/patch_neuro.py:8:    """Alias endpoint: /neural_process -> /process"""
./services/port_9001_FINAL_FIX.py:54:            r = await client.post(f"http://127.0.0.1:9000/consciousness/chat?userid=user&message={message}", timeout=10.0)
./services/ms_jarvis_consciousness_bridge_service.py:12:        @self.app.route('/process')
./services/patch_qualia.py:9:    """Alias endpoint: /generate -> /process"""
./services/patch_qualia.py:11:    return await app.post("/process", json={"content": input_text})
./services/ms_jarvis_fifth_dgm_orchestrator.py:238:                    response = await client.post(f"{woah_url}/process", json=payload)
./services/ms_jarvis_woah_algorithms_enhanced.py:141:@app.post("/process")
./services/consciousness_working.py:21:@app.post("/consciousness/chat")
./services/consciousness_working.py:22:async def consciousness_chat(
./services/ms_jarvis_service_factory.py:68:        @self.app.route('/process')
./services/integrate_all_services.py:32:                f"{BRAIN_ORCHESTRATOR_URL}/process",
./services/neuro_adapter.py:13:    """Adapter: /neural_process -> /process"""
./services/neuro_adapter.py:18:            "http://localhost:8018/process",
./services/qualia_unified_orchestrator_69dgm_REAL.py:165:@app.post("/process")
./services/msjarvis_gateway_with_judge_filtering.py:73:        wr = requests.post(f"http://localhost:7012/process", json={"query": message}, timeout=30)
./services/neuro_qualia_engine.py:18:@app.post("/process")
./services/registration_service_clean.backup_1762220206.py:37:        {"url": "http://127.0.0.1:8044", "description": "Localhost - Port 8044"},
./services/ms_jarvis_integration_hub.py:100:                for endpoint in ['/process', '/reason', '/analyze']:
./services/internet_tunnel_service.py:53:                response = requests.get("http://127.0.0.1:4040/api/tunnels", timeout=5)
./services/fix_main_brain_endpoints.py:13:# Fix Qualia Engine: /generate -> /process
./services/fix_main_brain_endpoints.py:16:    'http://jarvis-qualia-engine:8017/process',
./services/fix_main_brain_endpoints.py:20:# Fix Fractal: /process -> /analyze  
./services/fix_main_brain_endpoints.py:22:    r'http://jarvis-fractal-consciousness:8027/process',
./services/fix_main_brain_endpoints.py:27:# Fix Neurobiological: /neural_process -> /process
xargs: grep: terminated by signal 13
=== 2. FIND ALL LOCAL SERVICES LISTENING ON APP PORTS ===
docker-pr 2601991            root    8u  IPv4  85947034      0t0  TCP 127.0.0.1:7475 (LISTEN)
docker-pr 2602099            root    8u  IPv4  85947071      0t0  TCP 127.0.0.1:7687 (LISTEN)
python3   2456705          cakidd   13u  IPv4 103577103      0t0  TCP 127.0.0.1:8000 (LISTEN)
python3   2287608          cakidd    3u  IPv4  84349785      0t0  TCP 127.0.0.1:8001 (LISTEN)
python3   2287610          cakidd    3u  IPv4  84349785      0t0  TCP 127.0.0.1:8001 (LISTEN)
docker-pr  370414            root    8u  IPv4  94903027      0t0  TCP 127.0.0.1:8002 (LISTEN)
docker-pr 2651615            root    8u  IPv4  86189757      0t0  TCP 127.0.0.1:8003 (LISTEN)
docker-pr 2605751            root    8u  IPv4  85996387      0t0  TCP 127.0.0.1:8004 (LISTEN)
docker-pr 2605310            root    8u  IPv4  86013227      0t0  TCP 127.0.0.1:8005 (LISTEN)
python3   2175651          cakidd   13u  IPv4  83719089      0t0  TCP 127.0.0.1:8009 (LISTEN)
docker-pr  347091            root    8u  IPv4  94831747      0t0  TCP 127.0.0.1:8010 (LISTEN)
docker-pr 2606729            root    8u  IPv4  85988029      0t0  TCP 127.0.0.1:8015 (LISTEN)
docker-pr 2599418            root    8u  IPv4 103997252      0t0  TCP 127.0.0.1:8016 (LISTEN)
docker-pr 2571961            root    8u  IPv4  85839780      0t0  TCP 127.0.0.1:8019 (LISTEN)
docker-pr 2680129            root    8u  IPv4  86288373      0t0  TCP 127.0.0.1:8020 (LISTEN)
docker-pr 2572510            root    8u  IPv4  85854724      0t0  TCP 127.0.0.1:8025 (LISTEN)
docker-pr 2602588            root    8u  IPv4  85978054      0t0  TCP 127.0.0.1:8026 (LISTEN)
docker-pr 2607455            root    8u  IPv4  86030479      0t0  TCP 127.0.0.1:8030 (LISTEN)
docker-pr 2607351            root    8u  IPv4  86013458      0t0  TCP 127.0.0.1:8032 (LISTEN)
docker-pr 2607002            root    8u  IPv4  85994335      0t0  TCP 127.0.0.1:8033 (LISTEN)
docker-pr  429813            root    8u  IPv4  95158338      0t0  TCP 127.0.0.1:8045 (LISTEN)
docker-pr  400717            root    8u  IPv4  95039652      0t0  TCP 127.0.0.1:8046 (LISTEN)
docker-pr 2582790            root    8u  IPv4  85774211      0t0  TCP 127.0.0.1:8050 (LISTEN)
docker-pr 2599354            root    8u  IPv4  85983004      0t0  TCP 127.0.0.1:8073 (LISTEN)
docker-pr 2598550            root    8u  IPv4  85988667      0t0  TCP 127.0.0.1:8074 (LISTEN)
docker-pr 2598739            root    8u  IPv4  85989737      0t0  TCP 127.0.0.1:8075 (LISTEN)
docker-pr 2585652            root    8u  IPv4  85926363      0t0  TCP 127.0.0.1:8091 (LISTEN)
docker-pr 1228921            root    8u  IPv4  98319067      0t0  TCP 127.0.0.1:8093 (LISTEN)
docker-pr 1315723            root    8u  IPv4  98675287      0t0  TCP 127.0.0.1:8094 (LISTEN)
gunicorn  2453091          cakidd    3u  IPv4 103563100      0t0  TCP 127.0.0.1:8095 (LISTEN)
gunicorn  2453092          cakidd    3u  IPv4 103563100      0t0  TCP 127.0.0.1:8095 (LISTEN)
gunicorn  2453093          cakidd    3u  IPv4 103563100      0t0  TCP 127.0.0.1:8095 (LISTEN)
docker-pr 2756443            root    8u  IPv4  87203414      0t0  TCP 127.0.0.1:8108 (LISTEN)
docker-pr 2762718            root    8u  IPv4  87225333      0t0  TCP 127.0.0.1:8201 (LISTEN)
docker-pr 2762841            root    8u  IPv4  87259137      0t0  TCP 127.0.0.1:8202 (LISTEN)
docker-pr 2762995            root    8u  IPv4  87235569      0t0  TCP 127.0.0.1:8203 (LISTEN)
docker-pr 2763129            root    8u  IPv4  87246483      0t0  TCP 127.0.0.1:8204 (LISTEN)
docker-pr 2763328            root    8u  IPv4  87253222      0t0  TCP 127.0.0.1:8205 (LISTEN)
docker-pr 2763464            root    8u  IPv4  87260241      0t0  TCP 127.0.0.1:8206 (LISTEN)
docker-pr 2763599            root    8u  IPv4  87260266      0t0  TCP 127.0.0.1:8207 (LISTEN)
docker-pr 2763721            root    8u  IPv4  87255216      0t0  TCP 127.0.0.1:8208 (LISTEN)
docker-pr 2763859            root    8u  IPv4  87248412      0t0  TCP 127.0.0.1:8209 (LISTEN)
docker-pr 2763988            root    8u  IPv4  87239048      0t0  TCP 127.0.0.1:8210 (LISTEN)
docker-pr 2764138            root    8u  IPv4  86502399      0t0  TCP 127.0.0.1:8211 (LISTEN)
docker-pr 2764264            root    8u  IPv4  87230175      0t0  TCP 127.0.0.1:8212 (LISTEN)
docker-pr 2764388            root    8u  IPv4  87245471      0t0  TCP 127.0.0.1:8213 (LISTEN)
docker-pr 2764508            root    8u  IPv4  87248498      0t0  TCP 127.0.0.1:8214 (LISTEN)
docker-pr 2764642            root    8u  IPv4  87247710      0t0  TCP 127.0.0.1:8215 (LISTEN)
docker-pr 2764766            root    8u  IPv4  87217638      0t0  TCP 127.0.0.1:8216 (LISTEN)
docker-pr 2764894            root    8u  IPv4  87260408      0t0  TCP 127.0.0.1:8217 (LISTEN)
docker-pr 2765021            root    8u  IPv4  87241542      0t0  TCP 127.0.0.1:8218 (LISTEN)
docker-pr 2765150            root    8u  IPv4  87264293      0t0  TCP 127.0.0.1:8219 (LISTEN)
docker-pr 2765276            root    8u  IPv4  87264315      0t0  TCP 127.0.0.1:8220 (LISTEN)
docker-pr 2765419            root    8u  IPv4  87245601      0t0  TCP 127.0.0.1:8221 (LISTEN)
docker-pr 2765546            root    8u  IPv4  87246757      0t0  TCP 127.0.0.1:8222 (LISTEN)
node      2047761          cakidd   24u  IPv4  83002882      0t0  TCP 127.0.0.1:8545 (LISTEN)
docker-pr 2545752            root    8u  IPv4 103867794      0t0  TCP 127.0.0.1:9998 (LISTEN)
gunicorn  2464804          cakidd    3u  IPv4 103618207      0t0  TCP *:8018 (LISTEN)
gunicorn  2464810          cakidd    3u  IPv4 103618207      0t0  TCP *:8018 (LISTEN)
gunicorn  2464811          cakidd    3u  IPv4 103618207      0t0  TCP *:8018 (LISTEN)
uvicorn     16253          cakidd   15u  IPv4    130123      0t0  TCP *:8051 (LISTEN)
python3   3231143          cakidd   13u  IPv4  42099014      0t0  TCP *:8300 (LISTEN)
gunicorn  2579701          cakidd    3u  IPv4 104059935      0t0  TCP *:9000 (LISTEN)
gunicorn  2579704          cakidd    3u  IPv4 104059935      0t0  TCP *:9000 (LISTEN)
gunicorn  2579705          cakidd    3u  IPv4 104059935      0t0  TCP *:9000 (LISTEN)
gunicorn  2464793          cakidd    3u  IPv4 103618197      0t0  TCP *:9002 (LISTEN)
gunicorn  2464799          cakidd    3u  IPv4 103618197      0t0  TCP *:9002 (LISTEN)
gunicorn  2464800          cakidd    3u  IPv4 103618197      0t0  TCP *:9002 (LISTEN)
=== 3. PROBE EVERY LISTENING APP PORT FOR FASTAPI OPENAPI/HEALTH ===
PORT=7475 CODE=401 PATH=/openapi.json
{
  "errors" : [ {
    "code" : "Neo.ClientError.Security.Unauthorized",
    "message" : "No authentication header supplied."
  } ]
}
---
PORT=7475 CODE=401 PATH=/docs
{
  "errors" : [ {
    "code" : "Neo.ClientError.Security.Unauthorized",
    "message" : "No authentication header supplied."
  } ]
}
---
PORT=7475 CODE=401 PATH=/health
{
  "errors" : [ {
    "code" : "Neo.ClientError.Security.Unauthorized",
    "message" : "No authentication header supplied."
  } ]
}
---
PORT=7475 CODE=401 PATH=/consciousnesschat
{
  "errors" : [ {
    "code" : "Neo.ClientError.Security.Unauthorized",
    "message" : "No authentication header supplied."
  } ]
}
---
PORT=7475 CODE=401 PATH=/consciousness/chat
{
  "errors" : [ {
    "code" : "Neo.ClientError.Security.Unauthorized",
    "message" : "No authentication header supplied."
  } ]
}
---
PORT=7475 CODE=401 PATH=/process
{
  "errors" : [ {
    "code" : "Neo.ClientError.Security.Unauthorized",
    "message" : "No authentication header supplied."
  } ]
}
---
PORT=7687 CODE=200 PATH=/openapi.json

---
PORT=7687 CODE=200 PATH=/docs

---
PORT=7687 CODE=200 PATH=/health

---
PORT=7687 CODE=200 PATH=/consciousnesschat

---
PORT=7687 CODE=200 PATH=/consciousness/chat

---
PORT=7687 CODE=200 PATH=/process

---
PORT=8000 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis Interaction Logger","version":"1.0"},"paths":{"/log-interaction":{"post":{"summary":"Log Interaction","description":"Log interaction to MySQL with geolocation fallback to Mount Hope","operation
---
PORT=8000 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8000 CODE=200 PATH=/health
{"status":"healthy","service":"interaction_logger","port":8005,"default_location":"Mount Hope, WV","coordinates":{"lat":37.9735,"lon":-81.166,"city":"Mount Hope","state":"WV","zip":"25880"}}
---
PORT=8001 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Assertion Gateway","version":"0.2.0"},"paths":{"/assert":{"post":{"summary":"Assert Claim","operationId":"assert_claim_assert_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/compon
---
PORT=8001 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png
---
PORT=8001 CODE=200 PATH=/health
{"status":"ok","service":"assertion-gateway"}
---
PORT=8002 CODE=500 PATH=/openapi.json
{"error":"PackageNotFoundError('chromadb')"}
---
PORT=8002 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
 
---
PORT=8003 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis RAG","version":"1.0.0"},"paths":{"/":{"get":{"summary":"Root","operationId":"root__get","responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}}}}},
---
PORT=8003 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8003 CODE=200 PATH=/health
{"status":"healthy","service":"ms_jarvis_rag_server","timestamp":"2026-07-03T22:01:18.468274","port":8003}
---
PORT=8004 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis GIS RAG","version":"0.3.2"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","responses":{"200":{"description":"Successful Response","content":{"application/json"
---
PORT=8004 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
 
---
PORT=8004 CODE=200 PATH=/health
{"status":"healthy","service":"gis_rag","embed_model":"all-minilm"}
---
PORT=8005 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Spiritual RAG Domain","description":"Foundational spiritual and theological knowledge - the base layer for all Ms. Jarvis wisdom","version":"1.0.0"},"paths":{"/":{"get":{"summary":"Root","operationId":"ro
---
PORT=8005 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8005 CODE=200 PATH=/health
{"status":"healthy","service":"spiritual_rag_domain","port":8005,"documents":13,"categories":["biblical","catholic_social_teaching","spiritual_practice","stewardship","quaker","appalachian"],"role":"foundational_knowledge_layer"}
---
PORT=8009 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Assertion Gateway","version":"0.2.0"},"paths":{"/assert":{"post":{"summary":"Assert Claim","operationId":"assert_claim_assert_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/compon
---
PORT=8009 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png
---
PORT=8009 CODE=200 PATH=/health
{"status":"ok","service":"assertion-gateway"}
---
PORT=8010 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"chroma-frontend","description":"","license":{"name":""},"version":"1.0.0"},"paths":{"/api/v2/auth/identity":{"get":{"tags":["Authentication"],"summary":"Get user identity","description":"Returns the curre
---
PORT=8010 CODE=303 PATH=/docs

---
PORT=8015 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis I-Containers Service","description":"Dual I-Container System: Experiential Self + Observer Self + Integration","version":"1.0.0"},"paths":{"/":{"get":{"summary":"Root","description":"Service in
---
PORT=8015 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
 
---
PORT=8015 CODE=200 PATH=/health
{"status":"healthy","i_container_1":"active","i_container_2":"active","integration_layer":"active","dual_awareness":true,"timestamp":"2026-07-03T22:01:19.510341"}
---
PORT=8015 CODE=405 PATH=/process
{"detail":"Method Not Allowed"}
---
PORT=8016 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis Blood-Brain Barrier","description":"Ethical and Safety Filtering System with Constitutional Compliance","version":"2.0.0-Constitutional"},"paths":{"/":{"get":{"summary":"Root","operationId":"ro
---
PORT=8016 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8016 CODE=200 PATH=/health
{"status":"healthy","barrier_active":true,"filters_operational":5,"constitutional_guardian":"connected","total_filtered":0,"total_blocked":0,"constitutional_blocks":0}
---
PORT=8018 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis Production Chat","version":"1.0.0"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","responses":{"200":{"description":"Successful Response","content":{"applicati
---
PORT=8018 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png
---
PORT=8018 CODE=200 PATH=/health
{"status":"healthy","service":"production_chat_pipeline","port":8018}
---
PORT=8019 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis Psychology Services","description":"Psychological assessment, tagging, severity scoring, and crisis guardrails","version":"2.0.0"},"paths":{"/health":{"get":{"summary":"Health","operationId":"h
---
PORT=8019 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8019 CODE=200 PATH=/health
{"status":"healthy","service":"psychological_rag_domain","port":8006}
---
PORT=8020 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Egeria Jarvis - Unified Consciousness Bridge","description":"Unified consciousness with enhancement integration on port 4020","version":"2.0"},"paths":{"/":{"get":{"summary":"Root","operationId":"root
---
PORT=8020 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8020 CODE=200 PATH=/health
{"status":"healthy","service":"unified_consciousness_bridge","port":4020,"enhanced":true,"timestamp":"2026-07-03T22:01:20.030411"}
---
PORT=8025 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Toroidal Consciousness","description":"Toroidal manifold transformer for Ms. Jarvis ULTIMATE fabric","version":"1.0.0"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","res
---
PORT=8025 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8025 CODE=200 PATH=/health
{"status":"ok","service":"toroidal"}
---
PORT=8025 CODE=405 PATH=/process
{"detail":"Method Not Allowed"}
---
PORT=8026 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Phi Probe","version":"0.1.0"},"paths":{"/phi":{"get":{"summary":"Get Phi","operationId":"get_phi_phi_get","responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}
---
PORT=8026 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8026 CODE=200 PATH=/health
{"status":"ok","service":"phi-probe"}
---
PORT=8030 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis Semaphore","version":"1.0.2"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","responses":{"200":{"description":"Successful Response","content":{"application/jso
---
PORT=8030 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8030 CODE=200 PATH=/health
{"status":"ok","service":"semaphore","max_concurrent":4,"default_timeout":600.0}
---
PORT=8032 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"AaaCPE Cultural Intelligence","version":"1.0.0"},"paths":{"/":{"get":{"summary":"Root","operationId":"root__get","responses":{"200":{"description":"Successful Response","content":{"application/json":{"sch
---
PORT=8032 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8032 CODE=200 PATH=/health
{"status":"healthy","documents":613}
---
PORT=8033 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"AaaCPE Web Scraper","version":"1.0.0"},"paths":{"/":{"get":{"summary":"Root","operationId":"root__get","responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}}
---
PORT=8033 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8033 CODE=200 PATH=/health
{"status":"healthy","last_scrape":"2026-07-03T22:00:02.668393","documents_added":33,"errors":[]}
---
PORT=8045 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis KYC Vault","version":"1.0.0"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","responses":{"200":{"description":"Successful Response","content":{"application/jso
---
PORT=8045 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8045 CODE=200 PATH=/health
{"status":"healthy","service":"kyc-vault","version":"1.0.0"}
---
PORT=8046 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis Provenance","version":"1.0.0"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","responses":{"200":{"description":"Successful Response","content":{"application/js
---
PORT=8046 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8046 CODE=200 PATH=/health
{"status":"healthy","service":"provenance","version":"1.0.0"}
---
PORT=8050 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis ULTIMATE","version":"1.0.0"},"paths":{"/health":{"get":{"summary":"Healthcheck","operationId":"healthcheck_health_get","responses":{"200":{"description":"Successful Response","content":{"applic
---
PORT=8050 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
 
---
PORT=8050 CODE=200 PATH=/health
{"status":"healthy","service":"mainbrain"}
---
PORT=8051 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"FastAPI","version":"0.1.0"},"paths":{"/search_gbim_geo/":{"get":{"summary":"Search Gbim Geo","operationId":"search_gbim_geo_search_gbim_geo__get","parameters":[{"name":"lat","in":"query","required":true,"
---
PORT=8051 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8073 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"jarvis-eeg-delta-30s","version":"0.1.0"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","responses":{"200":{"description":"Successful Response","content":{"application/jso
---
PORT=8073 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8073 CODE=200 PATH=/health
{"status":"ok","service":"eeg-delta-30s","pulse_count":174,"last_pulse":"2026-07-01T15:11:50.169193"}
---
PORT=8074 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"jarvis-eeg-theta-60s","version":"0.1.0"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","responses":{"200":{"description":"Successful Response","content":{"application/jso
---
PORT=8074 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8074 CODE=200 PATH=/health
{"status":"ok","service":"eeg-theta-60s","pulse_count":3043,"last_pulse":"2026-07-03T22:00:37.042216","last_topic":"The key theme worth remembering is that the geospatial features are unidentified or \"unknown\" in geometry and location w"}
---
PORT=8075 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"jarvis-eeg-beta-5m","version":"0.1.0"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","responses":{"200":{"description":"Successful Response","content":{"application/json"
---
PORT=8075 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8075 CODE=200 PATH=/health
{"status":"ok","service":"eeg-beta-5m","pulse_count":17,"last_topic":"Coal mining industry's impact on community mental health","last_pulse":"2026-07-01T15:16:08.468835"}
---
PORT=8091 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis Constitutional Guardian","description":"Constitutional immutable constraints grounded in U.S. Constitution","version":"2.1.0-USC-Audit"},"paths":{"/health":{"get":{"summary":"Health","operation
---
PORT=8091 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8091 CODE=200 PATH=/health
{"status":"healthy","service":"constitutional_guardian","audit_log_enabled":true,"audit_file":"/app/audit/constitutional_audit.jsonl"}
---
PORT=8093 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Jarvis Unified Gateway","description":"Complete integrated consciousness system with Constitutional compliance","version":"2.1.0-Constitutional"},"paths":{"/":{"get":{"summary":"Root","operationId":"r
---
PORT=8093 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
 
---
PORT=8093 CODE=200 PATH=/health
{"status":"healthy","systems":{"consciousness_bridge":{"status":"healthy","url":"http://jarvis-consciousness-bridge:8020","responsive":true},"neurobiological_master":{"status":"healthy","url":"http://jarvis-neurobiological-master:8018","res
---
PORT=8094 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"H_p Civic Query Sidecar","version":"1.0.0"},"paths":{"/hp/health":{"get":{"summary":"Hp Health","operationId":"hp_health_hp_health_get","responses":{"200":{"description":"Successful Response","content":{"
---
PORT=8094 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
 
---
PORT=8095 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Ms. Allis Auth API","version":"1.0.0"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","responses":{"200":{"description":"Successful Response","content":{"application/json"
---
PORT=8095 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png
---
PORT=8095 CODE=200 PATH=/health
{"status":"healthy","service":"ms-allis-auth","timestamp":"2026-07-03T22:01:24.791193+00:00"}
---
PORT=8108 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"NBB Pituitary Gland","version":"2.0.0"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","responses":{"200":{"description":"Successful Response","content":{"application/json
---
PORT=8108 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
 
---
PORT=8108 CODE=200 PATH=/health
{"status":"ok","service":"nbb_pituitary_gland","port":8010}
---
PORT=8108 CODE=405 PATH=/process
{"detail":"Method Not Allowed"}
---
PORT=8201 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"TinyLlama Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/compo
---
PORT=8201 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8201 CODE=200 PATH=/health
{"status":"ok","proxy":"llm1"}
---
PORT=8202 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Gemma-2B Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/compon
---
PORT=8202 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8202 CODE=200 PATH=/health
{"status":"ok","proxy":"llm2"}
---
PORT=8203 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"MedLLaMA2 Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/compo
---
PORT=8203 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8203 CODE=200 PATH=/health
{"status":"ok","proxy":"llm3"}
---
PORT=8204 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"MiniCPM-V Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/compo
---
PORT=8204 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8204 CODE=200 PATH=/health
{"status":"ok","proxy":"llm4"}
---
PORT=8205 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"LLaVA Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/component
---
PORT=8205 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8205 CODE=200 PATH=/health
{"status":"ok","proxy":"llm5"}
---
PORT=8206 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"DeepSeek Coder Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/compone
---
PORT=8206 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8206 CODE=200 PATH=/health
{"status":"ok","proxy":"llm6"}
---
PORT=8207 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"StarCoder2 Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/comp
---
PORT=8207 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8207 CODE=200 PATH=/health
{"status":"ok","proxy":"llm7"}
---
PORT=8208 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"CodeLLaMA Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/compo
---
PORT=8208 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8208 CODE=200 PATH=/health
{"status":"ok","proxy":"llm8"}
---
PORT=8209 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"DeepSeek Coder Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/
---
PORT=8209 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8209 CODE=200 PATH=/health
{"status":"ok","proxy":"llm9"}
---
PORT=8210 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Phi3 Mini Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/compo
---
PORT=8210 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8210 CODE=200 PATH=/health
{"status":"ok","proxy":"llm10"}
---
PORT=8211 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Phi Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/components/
---
PORT=8211 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8211 CODE=200 PATH=/health
{"status":"ok","proxy":"llm11"}
---
PORT=8212 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Dolphin-Phi Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/com
---
PORT=8212 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8212 CODE=200 PATH=/health
{"status":"ok","proxy":"llm12"}
---
PORT=8213 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Orca-Mini Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/compo
---
PORT=8213 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8213 CODE=200 PATH=/health
{"status":"ok","proxy":"llm13"}
---
PORT=8214 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Qwen2 Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/component
---
PORT=8214 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8214 CODE=200 PATH=/health
{"status":"ok","proxy":"llm14"}
---
PORT=8215 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Zephyr Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/componen
---
PORT=8215 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8215 CODE=200 PATH=/health
{"status":"ok","proxy":"llm15"}
---
PORT=8216 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Starling-LM Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/com
---
PORT=8216 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8216 CODE=200 PATH=/health
{"status":"ok","proxy":"llm16"}
---
PORT=8217 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Neural-Chat Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/com
---
PORT=8217 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8217 CODE=200 PATH=/health
{"status":"ok","proxy":"llm17"}
---
PORT=8218 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"OpenChat Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/compon
---
PORT=8218 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8218 CODE=200 PATH=/health
{"status":"ok","proxy":"llm18"}
---
PORT=8219 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Vicuna Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/componen
---
PORT=8219 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8219 CODE=200 PATH=/health
{"status":"ok","proxy":"llm19"}
---
PORT=8220 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"LLaMA2 Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/componen
---
PORT=8220 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8220 CODE=200 PATH=/health
{"status":"ok","proxy":"llm20"}
---
PORT=8221 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Mistral Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/compone
---
PORT=8221 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8221 CODE=200 PATH=/health
{"status":"ok","proxy":"llm21"}
---
PORT=8222 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"LLaMA3 Health Proxy","version":"0.1.0"},"paths":{"/generate":{"post":{"summary":"Generate","operationId":"generate_generate_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/componen
---
PORT=8222 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link
---
PORT=8222 CODE=200 PATH=/health
{"status":"ok","proxy":"llm22"}
---
PORT=8300 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Qualia - 69 DGM Cascade Orchestrator","version":"0.1.0"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","responses":{"200":{"description":"Successful Response","content":{
---
PORT=8300 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
 
---
PORT=8300 CODE=200 PATH=/health
{"status":"qualia_orchestrator_69dgm_operational"}
---
PORT=8545 CODE=200 PATH=/openapi.json
{"jsonrpc":"2.0","id":null,"error":{"code":-32700,"message":"Parse error: Unexpected end of JSON input","data":{"message":"Parse error: Unexpected end of JSON input"}}}
---
PORT=8545 CODE=200 PATH=/docs
{"jsonrpc":"2.0","id":null,"error":{"code":-32700,"message":"Parse error: Unexpected end of JSON input","data":{"message":"Parse error: Unexpected end of JSON input"}}}
---
PORT=8545 CODE=200 PATH=/health
{"jsonrpc":"2.0","id":null,"error":{"code":-32700,"message":"Parse error: Unexpected end of JSON input","data":{"message":"Parse error: Unexpected end of JSON input"}}}
---
PORT=8545 CODE=200 PATH=/consciousnesschat
{"jsonrpc":"2.0","id":null,"error":{"code":-32700,"message":"Parse error: Unexpected end of JSON input","data":{"message":"Parse error: Unexpected end of JSON input"}}}
---
PORT=8545 CODE=200 PATH=/consciousness/chat
{"jsonrpc":"2.0","id":null,"error":{"code":-32700,"message":"Parse error: Unexpected end of JSON input","data":{"message":"Parse error: Unexpected end of JSON input"}}}
---
PORT=8545 CODE=200 PATH=/process
{"jsonrpc":"2.0","id":null,"error":{"code":-32700,"message":"Parse error: Unexpected end of JSON input","data":{"message":"Parse error: Unexpected end of JSON input"}}}
---
PORT=9000 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Port 9000 → 69-DGM Bridge","description":"Intercepts /consciousness/chat, routes through 69 DGM validators, then calls the 69-DGM RAG bridge for an answer","version":"1.2.0"},"paths":{"/consciousness/ch
---
PORT=9000 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png
---
PORT=9000 CODE=200 PATH=/health
{"status":"healthy","service":"port_9000_69dgm_bridge","connectors_loaded":0,"rag_bridge_url":"http://127.0.0.1:8000/consciousnesschat"}
---
PORT=9000 CODE=405 PATH=/consciousness/chat
{"detail":"Method Not Allowed"}
---
PORT=9002 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Chat Wrapper - 69 DGM Router","version":"1.0.0"},"paths":{"/":{"get":{"summary":"Root","operationId":"root__get","responses":{"200":{"description":"Successful Response","content":{"application/json":{"sch
---
PORT=9002 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png
---
PORT=9002 CODE=405 PATH=/consciousness/chat
{"detail":"Method Not Allowed"}
---
PORT=9998 CODE=200 PATH=/openapi.json
{"openapi":"3.1.0","info":{"title":"Qualia - 69 DGM Cascade Orchestrator","version":"REAL"},"paths":{"/health":{"get":{"summary":"Health","operationId":"health_health_get","responses":{"200":{"description":"Successful Response","content":{"
---
PORT=9998 CODE=200 PATH=/docs

    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
 
---
PORT=9998 CODE=200 PATH=/health
{"status":"REAL","orchestrator":"69-DGM Cascade","port":9998,"network":"docker","endpoint":"/evaluate"}
---
PORT=9998 CODE=405 PATH=/process
{"detail":"Method Not Allowed"}
---
=== 4. LIST MSJARVIS SYSTEMD UNITS WITH DEFINITIONS ===
  UNIT                   LOAD   ACTIVE     SUB          DESCRIPTION            
  msjarvis-69dgm-9000.s… loaded active     running      MsJarvis Port 9000 -> …
  msjarvis-69dgm-9002-c… loaded active     running      MsJarvis Port 9002 -> …
  msjarvis-69dgm-orches… loaded activating auto-restart MsJarvis 69-DGM Orches…
  msjarvis-chat.service  loaded activating auto-restart Ms. Jarvis Production …
  msjarvis-frontend.ser… loaded active     running      Ms. Allis Next.js Fron…
  msjarvis-interaction-… loaded activating auto-restart MS Jarvis Interaction …
  msjarvis-production-c… loaded active     running      Ms. Allis Production C…

Legend: LOAD   → Reflects whether the unit definition was properly loaded.
        ACTIVE → The high-level unit activation state, i.e. generalization of SUB.
        SUB    → The low-level unit activation state, values depend on unit type.

7 loaded units listed.
To show all installed unit files use 'systemctl list-unit-files'.
--- UNIT FILES ---
UNIT FILE                                STATE    PRESET 
msjarvis-69dgm-9000.service              enabled  enabled
msjarvis-69dgm-9002-chat.service         enabled  enabled
msjarvis-69dgm-orchestrator-9999.service disabled enabled
msjarvis-69dgm-orchestrator.service      enabled  enabled
msjarvis-chat.service                    enabled  enabled
msjarvis-frontend.service                enabled  enabled
msjarvis-interaction-logger.service      enabled  enabled
msjarvis-production-chat.service         enabled  enabled

8 unit files listed.
=== 5. SHOW UNIT FILES THAT REFERENCE PORTS OR CONSCIOUSNESS ===
/etc/systemd/system/dbus-org.freedesktop.nm-dispatcher.service:19:KillMode=process
/etc/systemd/system/sysstat.service.wants/sysstat-summary.timer:9:Description=Generate summary of yesterday's process accounting
/etc/systemd/system/multi-user.target.wants/snapd.service:29:KillMode=process
/etc/systemd/system/multi-user.target.wants/docker.service:33:# kill only the docker process, not all processes in the cgroup
/etc/systemd/system/multi-user.target.wants/docker.service:34:KillMode=process
/etc/systemd/system/multi-user.target.wants/smartd.service:5:# Typically physical storage devices are managed by the host physical machine
/etc/systemd/system/multi-user.target.wants/jarvis-consciousness-4021.service:8:ExecStart=/usr/bin/python3 -m uvicorn ms_jarvis_consciousness_enhancement_production:app \
/etc/systemd/system/multi-user.target.wants/msjarvis-69dgm-9000.service:2:Description=MsJarvis Port 9000 -> 69-DGM Bridge
/etc/systemd/system/multi-user.target.wants/msjarvis-69dgm-9000.service:13:Environment=BRIDGE_69DGM_URL=http://127.0.0.1:8000/consciousnesschat
/etc/systemd/system/multi-user.target.wants/msjarvis-69dgm-9000.service:14:ExecStart=/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn services.port_9000_69dgm_bridge:app -k uvicorn_worker.UvicornWorker -w 2 --bind 0.0.0.0:9000
/etc/systemd/system/multi-user.target.wants/pm2-cakidd.service:2:Description=PM2 process manager
/etc/systemd/system/multi-user.target.wants/smartmontools.service:5:# Typically physical storage devices are managed by the host physical machine
/etc/systemd/system/multi-user.target.wants/containerd.service:26:KillMode=process
/etc/systemd/system/multi-user.target.wants/cron.service:2:Description=Regular background program processing daemon
/etc/systemd/system/multi-user.target.wants/cron.service:10:KillMode=process
/etc/systemd/system/multi-user.target.wants/msjarvis-69dgm-9002-chat.service:3:After=network.target msjarvis-69dgm-9000.service
/etc/systemd/system/multi-user.target.wants/msjarvis-69dgm-9002-chat.service:13:Environment=BRIDGE_URL=http://127.0.0.1:9000/consciousnesschat
/etc/systemd/system/multi-user.target.wants/msjarvis-69dgm-9002-chat.service:14:ExecStart=/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn services.port_9000_chat_wrapper_69dgm:app -k uvicorn_worker.UvicornWorker -w 2 --bind 0.0.0.0:9002
/etc/systemd/system/multi-user.target.wants/unattended-upgrades.service:9:KillMode=process
/etc/systemd/system/multi-user.target.wants/ollama-bridge.service:2:Description=Ollama Docker Bridge (bridge + qualia-net)
/etc/systemd/system/multi-user.target.wants/NetworkManager.service:17:KillMode=process
/etc/systemd/system/msjarvis-69dgm-9000.service.d/override.conf:2:Environment=ORCH_69_URL=http://127.0.0.1:9998
/etc/systemd/system/smartd.service:5:# Typically physical storage devices are managed by the host physical machine
/etc/systemd/system/jarvis-consciousness-4021.service:8:ExecStart=/usr/bin/python3 -m uvicorn ms_jarvis_consciousness_enhancement_production:app \
/etc/systemd/system/msjarvis-69dgm-9000.service:2:Description=MsJarvis Port 9000 -> 69-DGM Bridge
/etc/systemd/system/msjarvis-69dgm-9000.service:13:Environment=BRIDGE_69DGM_URL=http://127.0.0.1:8000/consciousnesschat
/etc/systemd/system/msjarvis-69dgm-9000.service:14:ExecStart=/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn services.port_9000_69dgm_bridge:app -k uvicorn_worker.UvicornWorker -w 2 --bind 0.0.0.0:9000
/etc/systemd/system/sysinit.target.wants/apparmor.service:26:# from running processes (and not being able to re-apply it later).
/etc/systemd/system/sysinit.target.wants/systemd-pstore.service:11:Description=Platform Persistent Storage Archival
/etc/systemd/system/pm2-cakidd.service:2:Description=PM2 process manager
/etc/systemd/system/msjarvis-port9000.service.d/orchestrator.conf:2:Environment=ORCH_69_URL=http://127.0.0.1:9998
/etc/systemd/system/msjarvis-69dgm-9000.service.bak.1772198268:2:Description=MsJarvis Port 9000 → 69-DGM Bridge
/etc/systemd/system/msjarvis-69dgm-9000.service.bak.1772198268:10:ExecStart=/mnt/spiritual_drive/msjarvis-rebuild/run_9000_69dgm_bridge.sh
/etc/systemd/system/cloud-config.target.wants/cloud-init-hotplugd.socket:3:# add or remove event as processed by 90-cloud-init-hook-hotplug.rules.
/etc/systemd/system/msjarvis-69dgm-9002-chat.service:3:After=network.target msjarvis-69dgm-9000.service
/etc/systemd/system/msjarvis-69dgm-9002-chat.service:13:Environment=BRIDGE_URL=http://127.0.0.1:9000/consciousnesschat
/etc/systemd/system/msjarvis-69dgm-9002-chat.service:14:ExecStart=/mnt/spiritual_drive/msjarvis-rebuild/crypto-venv/bin/gunicorn services.port_9000_chat_wrapper_69dgm:app -k uvicorn_worker.UvicornWorker -w 2 --bind 0.0.0.0:9002
/etc/systemd/system/cloud-init.target.wants/cloud-final.service:18:KillMode=process
/etc/systemd/system/ollama-bridge.service:2:Description=Ollama Docker Bridge (bridge + qualia-net)
/lib/systemd/system/snapd.service:29:KillMode=process
/lib/systemd/system/apt-daily-upgrade.service:11:KillMode=process
/lib/systemd/system/user@.service.d/10-login-barrier.conf:13:# earlier during the boot process especially if something goes wrong.
/lib/systemd/system/docker.service:33:# kill only the docker process, not all processes in the cgroup
/lib/systemd/system/docker.service:34:KillMode=process
/lib/systemd/system/friendly-recovery.service:18:KillMode=process
/lib/systemd/system/multi-user.target.wants/plymouth-quit-wait.service:2:Description=Hold until boot process finishes up
/lib/systemd/system/sysstat-summary.timer:9:Description=Generate summary of yesterday's process accounting
/lib/systemd/system/openvpn-server@.service:20:KillMode=process
/lib/systemd/system/smartd.service:5:# Typically physical storage devices are managed by the host physical machine
/lib/systemd/system/storage-target-mode.target:11:Description=Storage Target Mode
/lib/systemd/system/storage-target-mode.target:13:Wants=systemd-storagetm.service systemd-udevd.service systemd-udev-trigger.service systemd-networkd.service systemd-network-generator.service systemd-journald.socket systemd-journald-dev-log.socket plymouth-start.service
/lib/systemd/system/storage-target-mode.target:15:After=systemd-storagetm.service systemd-udevd.service systemd-udev-trigger.service systemd-networkd.service systemd-network-generator.service systemd-journald.socket systemd-journald-dev-log.socket plymouth-start.service rescue.service rescue.target
/lib/systemd/system/systemd-storagetm.service:11:Description=Storage Target Mode (NVMe-TCP)
/lib/systemd/system/systemd-storagetm.service:12:Documentation=man:systemd-storagetm.service(8)
/lib/systemd/system/systemd-storagetm.service:27:ExecStart=/usr/lib/systemd/systemd-storagetm --all
/lib/systemd/system/systemd-sysupdate.timer:19:# Trigger the update 15min after boot, and then – on average – every 6h, but
/lib/systemd/system/sysinit.target.wants/systemd-journal-flush.service:11:Description=Flush Journal to Persistent Storage
/lib/systemd/system/openvpn-client@.service:20:KillMode=process
/lib/systemd/system/cloud-init-hotplugd.service:3:# add or remove event as processed by 90-cloud-init-hook-hotplug.rules.
/lib/systemd/system/cloud-init-hotplugd.service:5:# On start, read args from the FIFO, process and provide structured arguments
/lib/systemd/system/openvpn@.service:17:KillMode=process
/lib/systemd/system/fwupd.service:56:SystemCallFilter=@basic-io @file-system @io-event @ipc @network-io @process @sync @signal @timer @chown ioctl uname fadvise64 sysinfo madvise mremap splice vmsplice copy_file_range @raw-io
/lib/systemd/system/debug-shell.service:27:KillMode=process
/lib/systemd/system/plymouth-quit-wait.service:2:Description=Hold until boot process finishes up
/lib/systemd/system/cloud-init-hotplugd.socket:3:# add or remove event as processed by 90-cloud-init-hook-hotplug.rules.
/lib/systemd/system/user@0.service.d/10-login-barrier.conf:12:# in even if the boot process is not yet finished.
/lib/systemd/system/nm-priv-helper.service:16:# NetworkManager process itself). It is thus only an implementation
/lib/systemd/system/smartmontools.service:5:# Typically physical storage devices are managed by the host physical machine
/lib/systemd/system/containerd.service:26:KillMode=process
/lib/systemd/system/sysstat-summary.service:5:#        Generates daily summary of process accounting
/lib/systemd/system/sysstat-summary.service:8:Description=Generate a daily summary of process accounting
/lib/systemd/system/cron.service:2:Description=Regular background program processing daemon
/lib/systemd/system/cron.service:10:KillMode=process
/lib/systemd/system/cloud-final.service:18:KillMode=process
/lib/systemd/system/NetworkManager-dispatcher.service:19:KillMode=process
/lib/systemd/system/unattended-upgrades.service:9:KillMode=process
/lib/systemd/system/rescue.service:27:KillMode=process
/lib/systemd/system/apparmor.service:26:# from running processes (and not being able to re-apply it later).
/lib/systemd/system/NetworkManager.service:17:KillMode=process
/lib/systemd/system/systemd-journal-flush.service:11:Description=Flush Journal to Persistent Storage
/lib/systemd/system/emergency.service:28:KillMode=process
/lib/systemd/system/initrd-parse-etc.service:34:# which cleanup of the initrd processes starts.
/lib/systemd/system/systemd-pstore.service:11:Description=Platform Persistent Storage Archival
(crypto-venv) cakidd@cakidd-Legion-5-16IRX9:/mnt/spiritual_drive/msjarvis-rebuild$ 

